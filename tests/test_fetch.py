from types import SimpleNamespace

from investordb.fetch import (
    HostThrottle,
    collect_urls,
    extract_text,
    fetch_one,
    html_to_text,
    looks_like_homepage_redirect,
)


def test_html_to_text_drops_scripts_styles_nav():
    html = """<html><head><style>p{color:red}</style><script>var x = 'secret';</script></head>
    <body><nav>Home | About</nav><p>Fund I closed at&nbsp;30 mil.&nbsp;EUR.</p>
    <noscript>enable js</noscript><footer>Contact</footer></body></html>"""
    text = html_to_text(html)
    assert "secret" not in text and "color" not in text
    assert "Home | About" not in text and "enable js" not in text
    assert "Fund I closed at 30 mil. EUR." in text
    assert "Contact" in text


def test_extract_text_plain_and_html_sniffing():
    assert extract_text("text/plain", b"hello") == "hello"
    assert "Hi" in extract_text("", b"<html><body><p>Hi</p></body></html>")


def test_homepage_redirect():
    assert looks_like_homepage_redirect("https://a.sk/portfolio/x", "https://a.sk/")
    assert not looks_like_homepage_redirect("https://a.sk/", "https://a.sk/")
    assert not looks_like_homepage_redirect("https://a.sk/x", "https://a.sk/x/")


def test_throttle_waits_per_host():
    now = [0.0]
    slept = []

    def sleep(s):
        slept.append(s)
        now[0] += s

    t = HostThrottle(1.0, clock=lambda: now[0], sleep=sleep)
    t.wait("https://a.sk/1")
    t.wait("https://b.sk/1")  # other host: no wait
    now[0] += 0.25
    t.wait("https://a.sk/2")
    assert slept == [0.75]


def test_collect_urls_dedupes(records):
    urls = collect_urls(records)
    assert len(urls) == len(set(urls)) == 5


class FakeSession:
    def __init__(self, responses):
        self.responses = responses
        self.calls = []

    def get(self, url, headers=None, params=None, timeout=None, allow_redirects=True):
        self.calls.append((url, params, headers))
        status, ctype, body, json_data = self.responses[url]
        return SimpleNamespace(status_code=status, url=url, content=body,
                               headers={"Content-Type": ctype}, json=lambda: json_data)


def test_fetch_falls_back_to_wayback(tmp_path):
    url = "https://example.com/gone"
    snap = "http://web.archive.org/web/20240101000000/https://example.com/gone"
    raw = "https://web.archive.org/web/20240101000000id_/https://example.com/gone"
    api = "https://archive.org/wayback/available?url=https%3A%2F%2Fexample.com%2Fgone"
    session = FakeSession({
        url: (404, "text/html", b"not found", None),
        api: (200, "application/json", b"", {"archived_snapshots": {"closest": {
            "available": True, "url": snap, "timestamp": "20240101000000"}}}),
        raw: (200, "text/html", b"<p>Fund I closed at 30 mil. EUR.</p>", None),
    })
    throttle = HostThrottle(0.0)
    entry = fetch_one(session, throttle, url, tmp_path)
    assert entry["status"] == 404
    assert entry["used"] == "wayback"
    assert entry["body_url"] == raw
    assert entry["sha256"]
    assert "30 mil. EUR" in (tmp_path / entry["text_file"].split("/")[-1]).read_text()
    # archive.org gets a plain tool UA, the site gets a browser one
    assert "Mozilla" in session.calls[0][2]["User-Agent"]
    assert "Mozilla" not in session.calls[1][2]["User-Agent"]


def test_fetch_uses_cdx_when_availability_is_empty(tmp_path):
    url = "https://example.com/old.pdf"
    api = "https://archive.org/wayback/available?url=https%3A%2F%2Fexample.com%2Fold.pdf"
    cdx = "https://web.archive.org/cdx/search/cdx"
    raw = "https://web.archive.org/web/20230505000000id_/https://example.com/old.pdf"
    session = FakeSession({
        url: (403, "text/html", b"denied", None),
        api: (200, "application/json", b"", {"archived_snapshots": {}}),
        cdx: (200, "application/json", b"", [["timestamp", "original"],
                                             ["20230505000000", url]]),
        raw: (200, "text/plain", b"plain snapshot text", None),
    })
    entry = fetch_one(session, HostThrottle(0.0), url, tmp_path)
    assert entry["used"] == "wayback" and entry["wayback_lookup"] == "cdx"
    assert entry["body_url"] == raw


def test_fetch_records_failure_without_snapshot(tmp_path):
    url = "https://example.com/missing"
    api = "https://archive.org/wayback/available?url=https%3A%2F%2Fexample.com%2Fmissing"
    session = FakeSession({
        url: (404, "text/html", b"nope", None),
        api: (200, "application/json", b"", {"archived_snapshots": {}}),
        "https://web.archive.org/cdx/search/cdx": (200, "application/json", b"", []),
    })
    entry = fetch_one(session, HostThrottle(0.0), url, tmp_path)
    assert entry["used"] is None and entry["text_file"] is None
