import copy
import csv
import json
from pathlib import Path

from investordb.records import TIER_RANK, Target, iter_targets, parse_date, primary_source
from investordb.textnorm import name_key
from investordb.verify import PASS, read_rows, target_fingerprint

CSV_COLUMNS = [
    "id", "name", "type", "hq_country", "hq_city", "website", "legal_entities",
    "decision_status", "decision_rules",
    "sectors", "sectors_source", "stages", "stages_source", "geography", "geography_source",
    "ticket_min", "ticket_max", "ticket_currency", "ticket_source",
    "funds", "funds_source", "aum_amount", "aum_currency", "aum_as_of", "aum_source",
    "investments_count", "last_investment_date", "last_investment_company",
    "last_investment_source", "confidence", "confidence_reason",
]


class Checks:
    """Looks up verify results; a source counts only if its quote was found and the
    quote doesn't contradict the value."""

    def __init__(self, rows: list[dict] | None):
        self.ignore = rows is None
        self.by_key = {(r["record_id"], r["target"], int(r["source_index"])): r
                       for r in rows or []}

    def counts(self, rid: str, t: Target, i: int, source: dict) -> bool:
        if self.ignore:
            return True
        r = self.by_key.get((rid, t.key, i))
        if (r is None or r["url"] != source.get("url")
                or r.get("target_fingerprint") != target_fingerprint(t)):
            return False  # not verified, or verification is stale
        value = r.get("claim_value_status") or r["value_status"]
        return r["quote_status"] in PASS and value in ("ok", "n/a")


def _best(tiers) -> str | None:
    tiers = [t for t in tiers if t in TIER_RANK]
    return min(tiers, key=TIER_RANK.__getitem__) if tiers else None


def grade_record(rec: dict, checks: Checks) -> dict:
    rid = rec.get("id")
    evidence: dict[str, str] = {}
    counted: dict[str, list[dict]] = {}
    for t in iter_targets(rec):
        ok = [s for i, s in enumerate(t.sources) if checks.counts(rid, t, i, s)]
        counted[t.key] = ok
        best = _best(s.get("tier") for s in ok)
        evidence[t.key] = ("verified" if best in ("A", "B")
                           else "unverified" if best == "C" else "unsupported")

    all_counted = [s for srcs in counted.values() for s in srcs]
    existence_a = any(s.get("tier") == "A" for s in all_counted)

    dated_tier, last_date, last_inv = None, None, None
    companies = set()
    for i, inv in enumerate(rec.get("investments") or []):
        srcs = counted.get(f"investments[{i}]", [])
        tier = _best(s.get("tier") for s in srcs)
        if tier in ("A", "B"):
            companies.add(name_key(inv.get("company", "")))
        d = parse_date(inv.get("date"))
        if d and tier:
            dated_tier = _best([dated_tier, tier])
            if tier in ("A", "B") and (last_date is None or d > last_date):
                last_date, last_inv = d, inv

    proven_dated = dated_tier in ("A", "B")
    if existence_a and proven_dated:
        conf, why = "A", "existence by Tier A, dated investment by Tier " + dated_tier
    elif len(companies) >= 3 and proven_dated:
        conf, why = "B", f"own portfolio of {len(companies)} companies, dated investment by Tier B"
    else:
        missing = []
        if not proven_dated:
            missing.append("no dated investment proven by Tier A/B"
                           + (" (Tier C only)" if dated_tier == "C" else ""))
        if not existence_a and len(companies) < 3:
            missing.append(f"existence not proven (no Tier A, {len(companies)} A/B companies)")
        conf, why = "C", "; ".join(missing) or "relies on Tier C"

    return {
        "confidence": conf,
        "reason": why,
        "last_investment_date": last_date.isoformat() if last_date else None,
        "last_investment_company": last_inv.get("company") if last_inv else None,
        "existence_tier_a": existence_a,
        "dated_investment_tier": dated_tier,
        "portfolio_count": len(companies),
        "evidence": evidence,
        "_counted": counted,
    }


def _src(counted: list[dict], all_sources: list[dict]) -> str:
    s = primary_source(counted) or primary_source(all_sources)
    return s.get("url", "") if s else ""


def _join(xs) -> str:
    return ";".join(str(x) for x in xs if x is not None and x != "")


def _num(x) -> str:
    if x is None:
        return ""
    return str(int(x)) if float(x).is_integer() else str(x)


def flat_row(rec: dict, g: dict) -> dict:
    fields = rec.get("fields") or {}
    counted = g["_counted"]

    def val(name):
        f = fields.get(name)
        return (f or {}).get("value")

    def src(name):
        f = fields.get(name)
        return _src(counted.get(f"fields.{name}", []), (f or {}).get("sources") or []) if f else ""

    hq = rec.get("hq") or {}
    ticket = val("ticket") or {}
    aum = val("aum") or {}
    funds = val("funds") or []
    dec = rec.get("decision") or {}
    last_src = ""
    if g["last_investment_company"]:
        for i, inv in enumerate(rec.get("investments") or []):
            if (inv.get("company") == g["last_investment_company"]
                    and inv.get("date") == g["last_investment_date"]):
                last_src = _src(counted.get(f"investments[{i}]", []), inv.get("sources") or [])
                break
    return {
        "id": rec.get("id"), "name": rec.get("name"), "type": rec.get("type"),
        "hq_country": hq.get("country", ""), "hq_city": hq.get("city") or "",
        "website": rec.get("website") or "",
        "legal_entities": _join(f"{le.get('id_type')}:{le.get('id')}"
                                for le in rec.get("legal_entities") or []),
        "decision_status": dec.get("status", ""), "decision_rules": _join(dec.get("rules") or []),
        "sectors": _join(val("sectors") or []), "sectors_source": src("sectors"),
        "stages": _join(val("stages") or []), "stages_source": src("stages"),
        "geography": _join(val("geography") or []), "geography_source": src("geography"),
        "ticket_min": _num(ticket.get("min")), "ticket_max": _num(ticket.get("max")),
        "ticket_currency": ticket.get("currency", ""), "ticket_source": src("ticket"),
        "funds": _join(
            f"{fd.get('name')} ({_num(fd.get('size')) or '?'} {fd.get('currency') or ''}, "
            f"{fd.get('vintage') or '?'})".replace(" ,", ",")
            for fd in funds),
        "funds_source": src("funds"),
        "aum_amount": _num(aum.get("amount")), "aum_currency": aum.get("currency", ""),
        "aum_as_of": aum.get("as_of") or "", "aum_source": src("aum"),
        "investments_count": len(rec.get("investments") or []),
        "last_investment_date": g["last_investment_date"] or "",
        "last_investment_company": g["last_investment_company"] or "",
        "last_investment_source": last_src,
        "confidence": g["confidence"], "confidence_reason": g["reason"],
    }


def run_grade(records: list[dict], verification, out_json, out_csv,
              ignore_verify: bool = False) -> int:
    if ignore_verify:
        checks = Checks(None)
        print("note: grading on claimed tiers only, verification results ignored")
    else:
        if not Path(verification).exists():
            print(f"error: {verification} not found; run `python -m investordb verify` first "
                  "or pass --ignore-verify")
            return 2
        checks = Checks(read_rows(verification))

    graded, rows = [], []
    for rec in records:
        g = grade_record(rec, checks)
        rows.append(flat_row(rec, g))
        out = copy.deepcopy(rec)
        out["grade"] = {k: v for k, v in g.items() if not k.startswith("_")}
        graded.append(out)

    for path in (out_json, out_csv):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_json).write_text(json.dumps(graded, indent=2, ensure_ascii=False) + "\n",
                              encoding="utf-8")
    with Path(out_csv).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        w.writeheader()
        w.writerows(rows)

    dist = {c: sum(r["confidence"] == c for r in rows) for c in "ABC"}
    print(f"{len(rows)} records graded: " + ", ".join(f"{k} {v}" for k, v in dist.items()))
    print(f"wrote {out_json} and {out_csv}")
    return 0
