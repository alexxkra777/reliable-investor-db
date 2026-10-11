import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

from investordb.fetch import load_index, load_text
from investordb.records import Target, iter_targets, parse_date
from investordb.textnorm import date_match, match_quote, normalize, number_in

COLUMNS = [
    "record_id", "record_name", "target", "target_fingerprint", "kind", "label", "source_index",
    "url", "tier",
    "publisher", "quote_status", "similarity", "value_status", "value_detail",
    "claim_value_status", "fetch_used", "http_status", "final_url",
]
PASS = ("exact", "fuzzy")


def target_fingerprint(t: Target) -> str:
    # Bind a check to the whole claim, including the sources supporting it together.
    payload = {"kind": t.kind, "value": t.value, "label": t.label, "sources": t.sources}
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _fmt(x: float) -> str:
    return str(int(x)) if float(x).is_integer() else str(x)


def value_facts(t: Target, source: dict, nquote: str) -> list[tuple[str, str]]:
    """(fact, status) pairs for numbers and dates the claim relies on.

    status: ok | published (asserted metadata) | partial | missing
    """
    facts: list[tuple[str, str]] = []

    def num(name: str, v):
        if v is not None:
            facts.append((f"{name}={_fmt(v)}", "ok" if number_in(float(v), nquote) else "missing"))

    def year(name: str, y):
        if y is not None:
            d = parse_date(f"{int(y):04d}-01-01")
            facts.append((f"{name}={y}", "ok" if d and date_match(d, nquote) else "missing"))

    v = t.value
    if t.kind in ("ticket", "ticket_observed") and isinstance(v, dict):
        num("min", v.get("min"))
        num("max", v.get("max"))
    elif t.kind == "funds" and isinstance(v, list):
        for fd in v:
            num(f"size[{fd.get('name')}]", fd.get("size"))
            year(f"vintage[{fd.get('name')}]", fd.get("vintage"))
    elif t.kind == "aum" and isinstance(v, dict):
        num("aum", v.get("amount"))
    elif t.kind == "investment" and isinstance(v, dict):
        d = parse_date(v.get("date"))
        if d:
            how = date_match(d, nquote)
            if how == "full":
                st = "ok"
            elif source.get("published") == v.get("date"):
                st = "published"  # asserted metadata, not checked against the fetched page
            elif how in ("month", "year"):
                st = "partial"
            else:
                st = "missing"
            facts.append((f"date={d.isoformat()}", st))
        rs = v.get("round_size") or {}
        num("round", rs.get("amount"))
    return facts


def value_status(facts: list[tuple[str, str]]) -> str:
    if not facts:
        return "n/a"
    states = [s for _, s in facts]
    if all(s == "ok" for s in states):
        return "ok"
    if all(s == "missing" for s in states):
        return "value_not_in_quote"
    return "partial"


def check_records(records: list[dict], index: dict, cache_dir) -> list[dict]:
    norm_pages: dict[str, str | None] = {}
    rows = []
    for rec in records:
        for t in iter_targets(rec):
            target_rows, passing_quotes, passing_sources = [], [], []
            for i, s in enumerate(t.sources):
                url = s.get("url", "")
                entry = index.get(url)
                if url not in norm_pages:
                    text = load_text(cache_dir, entry)
                    norm_pages[url] = normalize(text) if text else None
                npage = norm_pages[url]
                quote = s.get("quote") or ""
                if npage is None:
                    status, sim = "unreachable", 0.0
                else:
                    status, sim = match_quote(quote, None, npage)
                nquote = normalize(quote)
                if status in PASS:
                    passing_quotes.append(nquote)
                    passing_sources.append(s)
                facts = value_facts(t, s, nquote)
                detail = "; ".join(f"{f}:{st}" for f, st in facts)
                if t.kind == "investment" and t.label and normalize(t.label) not in nquote:
                    detail = (detail + "; " if detail else "") + "company_not_in_quote"
                target_rows.append({
                    "record_id": rec.get("id"), "record_name": rec.get("name"),
                    "target": t.key, "target_fingerprint": target_fingerprint(t),
                    "kind": t.kind, "label": t.label, "source_index": i,
                    "url": url, "tier": s.get("tier"), "publisher": s.get("publisher"),
                    "quote_status": status, "similarity": sim,
                    "value_status": value_status(facts), "value_detail": detail,
                    "fetch_used": (entry or {}).get("used") or "",
                    "http_status": (entry or {}).get("status") or "",
                    "final_url": (entry or {}).get("final_url") or "",
                })
            # sources often split a claim: one names the investor, another has the date and amount.
            # the claim holds if the verified quotes together carry every number and date
            published = {s.get("published") for s in passing_sources}
            date = t.value.get("date") if isinstance(t.value, dict) else None
            merged = {"published": date if date in published else None}
            merged_quote = " | ".join(passing_quotes)
            facts = value_facts(t, merged, merged_quote)
            if t.kind == "investment" and t.label:
                facts.append(("company", "ok" if normalize(t.label) in merged_quote else "missing"))
            claim = value_status(facts)
            for row in target_rows:
                row["claim_value_status"] = claim
            rows.extend(target_rows)
    return rows


def write_rows(rows: list[dict], out) -> None:
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)


def read_rows(path) -> list[dict]:
    with Path(path).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def summary(rows: list[dict]) -> str:
    n = len(rows)
    if not n:
        return "no source checks (no sourced values in the records)"
    qs = Counter(r["quote_status"] for r in rows)
    vs = Counter(r["value_status"] for r in rows)
    lines = [f"{n} checks over {len({r['record_id'] for r in rows})} records, "
             f"{len({r['url'] for r in rows})} URLs"]
    passed = qs["exact"] + qs["fuzzy"]
    lines.append(f"quote: {passed}/{n} pass ({100 * passed / n:.1f} %) - "
                 + ", ".join(f"{k} {qs[k]}" for k in ("exact", "fuzzy", "missing", "unreachable")))
    lines.append("value: " + ", ".join(f"{k} {v}" for k, v in sorted(vs.items())))
    for tier in ("A", "B", "C"):
        tr = [r for r in rows if r["tier"] == tier]
        if tr:
            ok = sum(r["quote_status"] in PASS for r in tr)
            lines.append(f"tier {tier}: {ok}/{len(tr)} quotes pass")
    claims = {(r["record_id"], r["target"]): r["claim_value_status"] for r in rows}
    cs = Counter(claims.values())
    lines.append("claims (all verified quotes together): "
                 + ", ".join(f"{k} {v}" for k, v in sorted(cs.items())))
    bad = [r for r in rows if r["quote_status"] not in PASS or r["claim_value_status"] ==
           "value_not_in_quote"]
    if bad:
        lines.append("problems (first 20):")
        for r in bad[:20]:
            lines.append(f"  {r['record_id']} {r['target']} #{r['source_index']}: "
                         f"{r['quote_status']}/{r['value_status']} {r['url']}")
    return "\n".join(lines)


def run_verify(records: list[dict], cache_dir, out) -> int:
    index = load_index(cache_dir)
    if not index:
        print(f"warning: no fetch index in {cache_dir}; every source will be 'unreachable'. "
              "Run `python -m investordb fetch` first.")
    rows = check_records(records, index, cache_dir)
    write_rows(rows, out)
    print(summary(rows))
    print(f"wrote {out}")
    return 0
