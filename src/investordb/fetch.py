import hashlib
import io
import json
import time
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import quote, urlsplit

import requests
from bs4 import BeautifulSoup

from investordb.records import iter_targets

BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": BROWSER_UA,
    "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8",
    "Accept-Language": "en,sk;q=0.9,cs;q=0.8",
}
TIMEOUT = 20
RETRIES = 2
MIN_INTERVAL = 1.0  # seconds between requests to the same host
WAYBACK_API = "https://archive.org/wayback/available?url="
WAYBACK_CDX = "https://web.archive.org/cdx/search/cdx"
# archive.org flags a browser UA coming from a non-browser client as a bot (HTTP 429),
# so it gets a plain tool UA instead
ARCHIVE_UA = "investordb/0.1 (source verification; 1 req/s)"
DROP_TAGS = ("script", "style", "nav", "noscript", "template", "svg", "iframe")


class HostThrottle:
    def __init__(self, interval: float = MIN_INTERVAL, clock=time.monotonic, sleep=time.sleep):
        self.interval = interval
        self.last: dict[str, float] = {}
        self.clock, self.sleep = clock, sleep

    def wait(self, url: str) -> None:
        host = urlsplit(url).netloc.lower()
        prev = self.last.get(host)
        if prev is not None:
            gap = self.clock() - prev
            if gap < self.interval:
                self.sleep(self.interval - gap)
        self.last[host] = self.clock()


def collect_urls(records: list[dict]) -> list[str]:
    seen: dict[str, None] = {}
    for rec in records:
        for t in iter_targets(rec):
            for s in t.sources:
                if s.get("url"):
                    seen.setdefault(s["url"], None)
    return list(seen)


def cache_key(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()


def html_to_text(html: str | bytes) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(DROP_TAGS):
        tag.decompose()
    # keep block structure so sentences from different elements don't glue together
    text = soup.get_text(separator="\n")
    lines = (ln.strip() for ln in text.splitlines())
    return "\n".join(ln for ln in lines if ln)


def pdf_to_text(data: bytes) -> str:
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(data))
    return "\n".join((page.extract_text() or "") for page in reader.pages)


def is_pdf(content_type: str, data: bytes) -> bool:
    return "pdf" in (content_type or "").lower() or data[:5] == b"%PDF-"


def extract_text(content_type: str, data: bytes) -> str:
    if is_pdf(content_type, data):
        return pdf_to_text(data)
    if "html" in (content_type or "").lower() or data.lstrip()[:1] == b"<":
        return html_to_text(data)
    return data.decode("utf-8", errors="replace")


def looks_like_homepage_redirect(url: str, final_url: str) -> bool:
    # a deep link that lands on "/" usually means the page is gone
    a, b = urlsplit(url), urlsplit(final_url)
    return a.path.strip("/") != "" and b.path.strip("/") == "" and not b.query


def _site(url: str) -> str:
    host = urlsplit(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def _headers(url: str) -> dict:
    host = urlsplit(url).netloc.lower()
    if host == "archive.org" or host.endswith(".archive.org"):
        return {**HEADERS, "User-Agent": ARCHIVE_UA}
    return HEADERS


def _get(session, throttle: HostThrottle, url: str, params: dict | None = None):
    last_exc = None
    for attempt in range(RETRIES + 1):
        throttle.wait(url)
        try:
            r = session.get(url, headers=_headers(url), params=params, timeout=TIMEOUT,
                            allow_redirects=True)
            if r.status_code in (429, 500, 502, 503, 504) and attempt < RETRIES:
                time.sleep(2 * (attempt + 1))
                continue
            return r, None
        except requests.RequestException as e:
            last_exc = e
            if attempt < RETRIES:
                time.sleep(2 * (attempt + 1))
    return None, f"{type(last_exc).__name__}: {last_exc}"


def _raw_snapshot(snap: str, ts: str | None) -> str:
    snap = snap.replace("http://web.archive.org/", "https://web.archive.org/", 1)
    # "id_" asks for the original bytes, without the archive toolbar
    if ts and f"/{ts}/" in snap:
        snap = snap.replace(f"/{ts}/", f"/{ts}id_/", 1)
    return snap


def wayback_snapshot(session, throttle: HostThrottle, url: str) -> tuple[str | None, str | None]:
    """Return (snapshot_url, how_found). Availability API first, CDX when it says nothing."""
    r, _ = _get(session, throttle, WAYBACK_API + quote(url, safe=""))
    if r is not None and r.status_code == 200:
        try:
            closest = r.json().get("archived_snapshots", {}).get("closest") or {}
        except ValueError:
            closest = {}
        if closest.get("available") and closest.get("url"):
            return _raw_snapshot(closest["url"], closest.get("timestamp")), "availability"
    # the availability API often returns nothing for pages that are archived
    params = {"url": url, "output": "json", "limit": "-1", "filter": "statuscode:200",
              "fl": "timestamp,original"}
    r, _ = _get(session, throttle, WAYBACK_CDX, params=params)
    if r is not None and r.status_code == 200:
        try:
            rows = r.json()
        except ValueError:
            rows = []
        if len(rows) > 1:
            ts, original = rows[-1][0], rows[-1][1]
            return f"https://web.archive.org/web/{ts}id_/{original}", "cdx"
    return None, None


def fetch_one(session, throttle: HostThrottle, url: str, files_dir: Path,
              use_wayback: bool = True) -> dict:
    entry: dict = {"url": url, "fetched_at": datetime.now(UTC).isoformat(timespec="seconds")}
    r, err = _get(session, throttle, url)
    live_ok = False
    if r is not None:
        entry.update(status=r.status_code, final_url=r.url,
                     content_type=r.headers.get("Content-Type", ""))
        entry["redirected_to_homepage"] = looks_like_homepage_redirect(url, r.url)
        entry["redirected_offsite"] = _site(url) != _site(r.url)
        live_ok = r.status_code < 400 and not entry["redirected_to_homepage"]
    else:
        entry.update(status=None, final_url=None, content_type=None, error=err)

    used, body, ctype = None, None, None
    if live_ok:
        used, body, ctype = "live", r.content, entry["content_type"]
    elif use_wayback:
        snap, how = wayback_snapshot(session, throttle, url)
        entry["wayback_url"] = snap
        entry["wayback_lookup"] = how
        if snap:
            wr, werr = _get(session, throttle, snap)
            if wr is not None and wr.status_code < 400:
                used, body, ctype = "wayback", wr.content, wr.headers.get("Content-Type", "")
                entry["wayback_status"] = wr.status_code
            else:
                entry["wayback_error"] = werr or f"HTTP {wr.status_code}"
    if used is None and r is not None and r.status_code < 400:
        # soft failure (homepage redirect) and no snapshot: keep what we got
        used, body, ctype = "live", r.content, entry["content_type"]

    entry["used"] = used
    # status/final_url/content_type above describe the live request; these describe
    # the bytes actually stored (live page or snapshot)
    entry["body_url"] = (entry["final_url"] if used == "live"
                         else entry.get("wayback_url") if used == "wayback" else None)
    entry["body_content_type"] = ctype
    if body is not None:
        key = cache_key(url)
        entry["sha256"] = hashlib.sha256(body).hexdigest()
        raw_path = files_dir / f"{key}.raw"
        raw_path.write_bytes(body)
        try:
            text = extract_text(ctype, body)
        except Exception as e:  # broken PDFs etc. should not stop the run
            text = ""
            entry["extract_error"] = f"{type(e).__name__}: {e}"
        (files_dir / f"{key}.txt").write_text(text, encoding="utf-8")
        entry["text_file"] = f"files/{key}.txt"
        entry["text_chars"] = len(text)
    else:
        entry["sha256"] = None
        entry["text_file"] = None
    return entry


def load_index(cache_dir: str | Path) -> dict:
    p = Path(cache_dir) / "index.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def save_index(cache_dir: str | Path, index: dict) -> None:
    p = Path(cache_dir) / "index.json"
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(index, indent=2, ensure_ascii=False, sort_keys=True),
                   encoding="utf-8")
    tmp.replace(p)


def load_text(cache_dir: str | Path, entry: dict | None) -> str | None:
    if not entry or not entry.get("text_file"):
        return None
    p = Path(cache_dir) / entry["text_file"]
    return p.read_text(encoding="utf-8") if p.exists() else None


def fetch_all(records: list[dict], cache_dir: str | Path, force: bool = False,
              use_wayback: bool = True, limit: int | None = None, session=None) -> int:
    cache_dir = Path(cache_dir)
    files_dir = cache_dir / "files"
    files_dir.mkdir(parents=True, exist_ok=True)
    index = load_index(cache_dir)
    urls = collect_urls(records)
    todo = [u for u in urls if force or not index.get(u, {}).get("used")]
    if limit is not None:
        todo = todo[:limit]
    print(f"{len(urls)} distinct URLs, {len(urls) - len(todo)} already cached, "
          f"fetching {len(todo)}")
    session = session or requests.Session()
    throttle = HostThrottle()
    counts = {"live": 0, "wayback": 0, "failed": 0}
    for n, url in enumerate(todo, 1):
        entry = fetch_one(session, throttle, url, files_dir, use_wayback)
        index[url] = entry
        counts[entry["used"] or "failed"] += 1
        print(f"[{n}/{len(todo)}] {entry['used'] or 'FAILED':8} {entry.get('status')} {url}")
        if n % 10 == 0:
            save_index(cache_dir, index)
    save_index(cache_dir, index)
    print(f"done: {counts['live']} live, {counts['wayback']} from Wayback, "
          f"{counts['failed']} failed")
    return 0
