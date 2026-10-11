import csv
import json
from collections import Counter
from datetime import date
from pathlib import Path

from investordb.records import DataError, load_records
from investordb.review import read_claims_csv
from investordb.rules import record_names
from investordb.stats import rate
from investordb.textnorm import name_key
from investordb.verify import PASS, read_rows

LABEL_ALIASES = {
    "correct": "correct", "ok": "correct", "true": "correct",
    "wrong": "wrong", "incorrect": "wrong", "false": "wrong",
    "cant_verify": "cant_verify", "can't verify": "cant_verify", "cant verify": "cant_verify",
    "cannot_verify": "cant_verify", "unverifiable": "cant_verify",
}


def read_labels(path) -> tuple[dict[str, dict], list[str]]:
    labels, problems = {}, []
    with Path(path).open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            cid = (row.get("claim_id") or "").strip()
            lab = LABEL_ALIASES.get((row.get("label") or "").strip().lower())
            if not cid:
                continue
            if lab is None:
                problems.append(f"{cid}: unknown label {row.get('label')!r}")
                continue
            labels[cid] = {"label": lab, "note": row.get("note", ""),
                           "reviewed_at": row.get("reviewed_at", "")}
    return labels, problems


def _metric(labs: list[str]) -> dict:
    c = Counter(labs)
    n = len(labs)
    decided = c["correct"] + c["wrong"]
    return {
        "labelled": n, "correct": c["correct"], "wrong": c["wrong"],
        "cant_verify": c["cant_verify"],
        # strict: can't verify counts as wrong (the database promises checkable sources)
        "strict": rate(c["correct"], n),
        # lenient: only claims the reviewer could decide
        "lenient": rate(c["correct"], decided),
    }


def human_metrics(claims: list[dict], labels: dict[str, dict]) -> dict:
    joined = [(c, labels[c["claim_id"]]["label"]) for c in claims if c["claim_id"] in labels]
    out = {
        "sampled_claims": len(claims),
        "labelled_claims": len(joined),
        "inclusion_precision": _metric([lab for c, lab in joined if c["kind"] == "existence"
                                        and c.get("decision_status") == "included"]),
        "investment_date_accuracy": _metric([lab for c, lab in joined
                                             if c["kind"] == "investment"]),
        "overall_claim_accuracy": _metric([lab for _, lab in joined]),
        "field_accuracy": {},
    }
    fields = sorted({c["field"] for c, _ in joined if c["kind"] == "field"})
    for f in fields:
        out["field_accuracy"][f] = _metric([lab for c, lab in joined
                                            if c["kind"] == "field" and c["field"] == f])
    return out


def recall(records: list[dict], reference_dir) -> dict:
    by_key: dict[str, dict] = {}
    for rec in records:
        for n in record_names(rec):
            by_key.setdefault(name_key(n), rec)
    out = {}
    for path in sorted(Path(reference_dir).glob("*.csv")):
        with path.open(newline="", encoding="utf-8-sig") as f:
            rows = [r for r in csv.DictReader(f) if (r.get("name") or "").strip()]
        covered, missing, statuses = 0, [], Counter()
        for r in rows:
            rec = by_key.get(name_key(r["name"]))
            if rec:
                covered += 1
                statuses[(rec.get("decision") or {}).get("status", "?")] += 1
            else:
                missing.append(r["name"].strip())
        out[path.stem] = {**rate(covered, len(rows)), "by_status": dict(statuses),
                          "missing": missing}
    return out


def automated_metrics(verification, decision_check, graded) -> dict:
    out: dict = {}
    if Path(verification).exists():
        rows = read_rows(verification)
        qs = Counter(r["quote_status"] for r in rows)
        vs = Counter(r["value_status"] for r in rows)
        passed = qs["exact"] + qs["fuzzy"]
        out["quote_checks"] = {
            "total": len(rows), "by_status": dict(qs),
            "pass_rate": rate(passed, len(rows)),
            "reachable_pass_rate": rate(passed, len(rows) - qs["unreachable"]),
            "by_tier": {t: rate(sum(r["quote_status"] in PASS for r in rows if r["tier"] == t),
                                sum(r["tier"] == t for r in rows))
                        for t in ("A", "B", "C") if any(r["tier"] == t for r in rows)},
        }
        with_values = [r for r in rows if r["value_status"] != "n/a"]
        # one row per claim: a claim is backed when its verified quotes together carry the values
        claims = {(r["record_id"], r["target"]): r.get("claim_value_status") or r["value_status"]
                  for r in rows}
        claim_values = [v for v in claims.values() if v != "n/a"]
        out["value_checks"] = {
            "by_status": dict(vs),
            "value_in_quote_rate": rate(sum(r["value_status"] == "ok" for r in with_values),
                                        len(with_values)),
            "claims_by_status": dict(Counter(claim_values)),
            "claim_backed_rate": rate(sum(v == "ok" for v in claim_values), len(claim_values)),
            "claim_not_contradicted_rate": rate(
                sum(v != "value_not_in_quote" for v in claim_values), len(claim_values)),
        }
    if Path(decision_check).exists():
        with Path(decision_check).open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        ag = Counter(r["agreement"] for r in rows)
        # human_only rows are decisions the engine can't make (scope, rules it has no data for)
        decidable = ag["agree"] + ag["DISAGREE"]
        out["decision_agreement"] = {"by_agreement": dict(ag),
                                     "agree_rate": rate(ag["agree"], decidable)}
    if Path(graded).exists():
        recs = json.loads(Path(graded).read_text(encoding="utf-8"))
        conf = Counter((r.get("grade") or {}).get("confidence", "?") for r in recs)
        out["confidence"] = dict(sorted(conf.items()))
    return out


# --- report --------------------------------------------------------------------

def _pct(r: dict | None) -> str:
    if not r or r.get("value") is None:
        return "-"
    lo, hi = r["ci95"]
    return f"{100 * r['value']:.1f} % ({100 * lo:.1f}-{100 * hi:.1f})"


def _row(name: str, m: dict) -> str:
    return (f"| {name} | {m['labelled']} | {m['correct']} | {m['wrong']} | {m['cant_verify']} | "
            f"{_pct(m['strict'])} | {_pct(m['lenient'])} |")


def render_md(metrics: dict) -> str:
    L = ["# Accuracy report", "",
         f"Built by `python -m investordb eval` on {metrics['date']}.", ""]
    hm = metrics.get("human")
    L.append("## Human review")
    L.append("")
    if hm is None:
        L += [f"**No review labels found** ({metrics['labels_path']}). Only the automated "
              "metrics below were computed; they say whether sources still contain the quoted "
              "text, not whether the claims are right. Run `review-pack`, review "
              "`eval/review.html`, export `eval/labels.csv` and run `eval` again.", ""]
    else:
        L += [f"{hm['labelled_claims']} of {hm['sampled_claims']} sampled claims labelled.", "",
              "| Metric | Labelled | Correct | Wrong | Can't verify | Strict (95 % CI) "
              "| Lenient (95 % CI) |",
              "|---|---:|---:|---:|---:|---|---|",
              _row("Inclusion precision", hm["inclusion_precision"])]
        for f, m in hm["field_accuracy"].items():
            L.append(_row(f"Field: {f}", m))
        L += [_row("Investment date", hm["investment_date_accuracy"]),
              _row("**All claims**", hm["overall_claim_accuracy"]), ""]
        if metrics.get("label_problems"):
            L += ["Ignored label rows: " + "; ".join(metrics["label_problems"]), ""]

    L += ["## Recall against reference lists", ""]
    rc = metrics.get("recall")
    if rc is None:
        L += [metrics.get("recall_note", "Not computed."), ""]
    elif not rc:
        L += ["No reference lists found in `data/reference/`.", ""]
    else:
        L += ["| List | Entities | Covered | Recall (95 % CI) | Decisions of covered |",
              "|---|---:|---:|---|---|"]
        for name, r in rc.items():
            st = ", ".join(f"{k} {v}" for k, v in sorted(r["by_status"].items())) or "-"
            L.append(f"| {name} | {r['n']} | {r['k']} | {_pct(r)} | {st} |")
        L.append("")
        for name, r in rc.items():
            if r["missing"]:
                L.append(f"Not covered from `{name}`: " + ", ".join(r["missing"]) + ".")
        L.append("")

    am = metrics.get("automated") or {}
    L += ["## Automated checks", ""]
    if not am:
        L += ["No verification, decision check or grade files found.", ""]
    if "quote_checks" in am:
        q = am["quote_checks"]
        L += ["| Check | Value (95 % CI) |", "|---|---|",
              f"| Quote found on page, all sources | {_pct(q['pass_rate'])} |",
              f"| Quote found on page, reachable sources only | "
              f"{_pct(q['reachable_pass_rate'])} |"]
        for t, r in q["by_tier"].items():
            L.append(f"| Quote found, Tier {t} | {_pct(r)} |")
        if "value_checks" in am:
            v = am["value_checks"]
            if "claim_backed_rate" in v:
                L.append(f"| Claims whose numbers/dates are all in their quotes | "
                         f"{_pct(v['claim_backed_rate'])} |")
                L.append(f"| Claims with at least part of the value in the quotes | "
                         f"{_pct(v['claim_not_contradicted_rate'])} |")
            L.append(f"| Number/date present, per single source | "
                     f"{_pct(v['value_in_quote_rate'])} |")
        if "decision_agreement" in am:
            d = am["decision_agreement"]
            L.append(f"| Stored decision = rule engine (decidable cases) | "
                     f"{_pct(d['agree_rate'])} |")
            L.append("")
            L.append("Rule engine vs stored decisions: " + ", ".join(
                f"{k} {n}" for k, n in sorted(d["by_agreement"].items())) + ". `human_only` = "
                "a decision the engine can't make (pilot scope, or a rule it has no data for).")
        L.append("")
        L.append("Quote statuses: " + ", ".join(f"{k} {v}" for k, v in
                                                sorted(q["by_status"].items())) + ".")
        L.append("")
    elif "decision_agreement" in am:
        L += [f"Stored decision = rule engine: {_pct(am['decision_agreement']['agree_rate'])}", ""]
    if "confidence" in am:
        L += ["Confidence grades: " + ", ".join(f"{k} {v}" for k, v in
                                                am["confidence"].items()) + ".", ""]

    L += ["## Method", "",
          "- Claims are sampled with `review-pack` (stratified by claim type: existence, each "
          "field, investments; proportional allocation with at least 3 per stratum, fixed seed). "
          "Overall accuracy is the plain sample share and leans towards the smaller strata.",
          "- Inclusion precision uses existence claims of records whose stored decision is "
          "`included`. Investment claims are judged on company and date.",
          "- **Strict** counts \"Can't verify\" as wrong, because a value whose source doesn't "
          "back it breaks the provenance promise. **Lenient** drops those claims.",
          "- Intervals are 95 % Wilson score intervals.",
          "- Recall: a reference entity is covered if a record with the same normalised name, "
          "alias or legal entity name exists, whatever its decision.",
          "- Automated checks: `verify` looks for each stored quote on the cached page "
          "(normalised text, exact or fuzzy >= 0.85 with matching numbers) and for the "
          "claimed number/date inside the quote.", ""]
    return "\n".join(L)


def run_eval(records_path, claims_path, labels_path, reference_dir, verification,
             decision_check, graded, out_md, out_json) -> int:
    metrics: dict = {"date": date.today().isoformat(), "labels_path": str(labels_path)}

    if Path(labels_path).exists():
        if not Path(claims_path).exists():
            print(f"error: labels given but {claims_path} is missing")
            return 2
        claims = read_claims_csv(claims_path)
        labels, problems = read_labels(labels_path)
        unknown = sorted(set(labels) - {c["claim_id"] for c in claims})
        problems += [f"{cid}: not in claims.csv" for cid in unknown]
        metrics["human"] = human_metrics(claims, labels)
        metrics["label_problems"] = problems
    else:
        metrics["human"] = None
        print(f"note: {labels_path} not found - computing automated metrics only")

    try:
        records = load_records(records_path)
        metrics["recall"] = recall(records, reference_dir) if Path(reference_dir).exists() else {}
    except DataError as e:
        metrics["recall"] = None
        metrics["recall_note"] = f"Recall not computed: {e}."

    metrics["automated"] = automated_metrics(verification, decision_check, graded)

    for p in (out_md, out_json):
        Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(out_json).write_text(json.dumps(metrics, indent=2, ensure_ascii=False) + "\n",
                              encoding="utf-8")
    Path(out_md).write_text(render_md(metrics), encoding="utf-8")

    hm = metrics["human"]
    if hm:
        print(f"labelled {hm['labelled_claims']}/{hm['sampled_claims']}; overall strict "
              f"{_pct(hm['overall_claim_accuracy']['strict'])}; inclusion precision strict "
              f"{_pct(hm['inclusion_precision']['strict'])}")
    for name, r in (metrics.get("recall") or {}).items():
        print(f"recall {name}: {r['k']}/{r['n']} {_pct(r)}")
    q = metrics["automated"].get("quote_checks")
    if q:
        print(f"quote pass rate {_pct(q['pass_rate'])}")
    print(f"wrote {out_md} and {out_json}")
    return 0
