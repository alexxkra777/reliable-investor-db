import csv
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from investordb.records import iter_targets, parse_date
from investordb.textnorm import name_key

TYPE_EXCLUSIONS = {
    "platform": ("E1", "type is platform (routes other people's money)"),
    "adviser": ("E2", "type is adviser"),
}
SEPARATE_LIST = {"fund_of_funds", "public_dfi"}
PERSON_TYPES = {"angel", "private_investor"}
# rules that need human judgement; the engine can't derive them from the data
HUMAN_ONLY = {"E2", "E3", "E5", "E6", "E7", "E8", "E9", "E10"}

COLUMNS = [
    "record_id", "name", "type", "stored_status", "stored_rules", "computed_status",
    "computed_rules", "agreement", "last_ab_investment", "months_since", "reasons",
]


@dataclass
class Decision:
    status: str
    rules: list[str]
    reasons: list[str] = field(default_factory=list)
    last_ab_investment: date | None = None


def months_back(d: date, months: int) -> date:
    y, m = divmod(d.year * 12 + (d.month - 1) - months, 12)
    m += 1
    # clamp e.g. 31 May -> 30 Apr, 29 Feb -> 28 Feb
    for day in (d.day, 30, 29, 28):
        try:
            return date(y, m, min(d.day, day))
        except ValueError:
            continue
    raise ValueError(d)


def months_between(a: date, b: date) -> int:
    """Whole months from a to b (b later)."""
    n = (b.year - a.year) * 12 + (b.month - a.month)
    return n - 1 if b.day < a.day else n


def load_negative_list(path) -> dict[str, dict]:
    p = Path(path)
    if not p.exists():
        return {}
    with p.open(newline="", encoding="utf-8") as f:
        return {name_key(row["name"]): row for row in csv.DictReader(f) if row.get("name")}


def record_names(rec: dict) -> list[str]:
    names = [rec.get("name") or ""] + list(rec.get("aliases") or [])
    names += [le.get("name", "") for le in rec.get("legal_entities") or []]
    return [n for n in names if n]


def last_investment(rec: dict, tiers=("A", "B")) -> date | None:
    dates = []
    for inv in rec.get("investments") or []:
        d = parse_date(inv.get("date"))
        if d and any(s.get("tier") in tiers for s in inv.get("sources") or []):
            dates.append(d)
    return max(dates) if dates else None


def has_identity(rec: dict) -> bool:
    if any(le.get("id") for le in rec.get("legal_entities") or []):
        return True
    # a person needs a stable public profile instead of a registry id
    return rec.get("type") in PERSON_TYPES and bool(rec.get("website"))


def core_activity(rec: dict) -> tuple[bool, str]:
    if any(le.get("id_type") == "CRD" for le in rec.get("legal_entities") or []):
        return True, "SEC-registered adviser (CRD)"
    for t in iter_targets(rec):
        if t.kind != "investment" and any(s.get("tier") == "A" for s in t.sources):
            return True, f"Tier A source for {t.kind}"
    companies = {
        name_key(inv.get("company", ""))
        for inv in rec.get("investments") or []
        if any(s.get("tier") in ("A", "B") for s in inv.get("sources") or [])
    }
    if len(companies) >= 3:
        return True, f"{len(companies)} portfolio companies with Tier A/B sources"
    return False, (f"no registration/FoF evidence and only {len(companies)} "
                   "sourced portfolio companies")


def decide(rec: dict, negative: dict[str, dict], ref: date, window_months: int = 36) -> Decision:
    rtype = rec.get("type")
    last = last_investment(rec)
    if rtype in TYPE_EXCLUSIONS:
        rule, why = TYPE_EXCLUSIONS[rtype]
        return Decision("excluded", [rule], [why], last)
    for n in record_names(rec):
        hit = negative.get(name_key(n))
        if hit:
            return Decision("excluded", [hit.get("rule") or "E1"],
                            [f"negative list: {hit.get('name')} ({hit.get('reason', '')})"], last)

    reasons = []
    if rtype in SEPARATE_LIST:
        reasons.append("type belongs to the separate fund-of-funds / DFI list")
    if rtype == "accelerator":
        reasons.append("accelerator: keep out of ticket statistics")

    cutoff = months_back(ref, window_months)
    if last is None or last < cutoff:
        last_any = last_investment(rec, ("A", "B", "C"))
        if last_any and last_any >= cutoff:
            return Decision("uncertain", ["I3?"], reasons + [
                f"investment on {last_any} is shown only by Tier C sources"], last)
        if last_any:
            return Decision("dormant", ["E4"], reasons + [
                f"last dated investment {last_any} is before {cutoff}"], last)
        return Decision("uncertain", ["I3?"],
                        reasons + ["no dated investment with a Tier A/B source"], None)

    failed = []
    if not has_identity(rec):
        failed.append("I1?")
        reasons.append("no registry identifier")
    ok, why = core_activity(rec)
    if not ok:
        failed.append("I2?")
    reasons.append(why)
    if failed:
        return Decision("uncertain", failed, reasons, last)
    return Decision("included", ["I1", "I2", "I3", "I4"], reasons, last)


def agreement(rec: dict, d: Decision) -> str:
    stored = rec.get("decision") or {}
    if stored.get("status") == d.status:
        return "agree"
    stored_rules = set(stored.get("rules") or [])
    if stored.get("status") == "excluded" and stored_rules & HUMAN_ONLY:
        return "human_only"
    return "DISAGREE"


def run_decide(records: list[dict], negative_path, out, ref_date: date,
               window_months: int = 36) -> int:
    negative = load_negative_list(negative_path)
    if not negative:
        print(f"warning: negative list {negative_path} is missing or empty")
    rows = []
    for rec in records:
        d = decide(rec, negative, ref_date, window_months)
        stored = rec.get("decision") or {}
        rows.append({
            "record_id": rec.get("id"), "name": rec.get("name"), "type": rec.get("type"),
            "stored_status": stored.get("status"),
            "stored_rules": ";".join(stored.get("rules") or []),
            "computed_status": d.status, "computed_rules": ";".join(d.rules),
            "agreement": agreement(rec, d),
            "last_ab_investment": d.last_ab_investment.isoformat() if d.last_ab_investment else "",
            "months_since": (months_between(d.last_ab_investment, ref_date)
                             if d.last_ab_investment else ""),
            "reasons": "; ".join(d.reasons),
        })
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)

    counts: dict[str, int] = {}
    for r in rows:
        counts[r["agreement"]] = counts.get(r["agreement"], 0) + 1
    print(f"reference date {ref_date}, window {window_months} months; "
          + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    for r in rows:
        if r["agreement"] != "agree":
            print(f"  {r['agreement']:10} {r['record_id']}: stored {r['stored_status']} "
                  f"[{r['stored_rules']}] vs computed {r['computed_status']} "
                  f"[{r['computed_rules']}] - {r['reasons']}")
    print(f"wrote {out} (stored decisions were not changed)")
    return 0
