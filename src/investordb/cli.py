import argparse
import sys
from datetime import date

from investordb.records import DataError

RECORDS = "data/sample/investors.json"
CACHE = "data/cache"
VERIFICATION = "data/sample/verification.csv"


def _date(s: str) -> date:
    try:
        return date.fromisoformat(s)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"expected YYYY-MM-DD, got {s!r}") from e


def cmd_validate(a) -> int:
    from investordb.records import load_records
    from investordb.validate import load_validator, validate

    records = load_records(a.records)
    rep = validate(records, load_validator(a.schema), today=a.today)
    for e in rep.errors:
        print(f"ERROR   {e}")
    for w in rep.warnings:
        print(f"WARNING {w}")
    print(f"{len(records)} records, {len(rep.errors)} errors, {len(rep.warnings)} warnings")
    return 0 if rep.ok else 1


def cmd_fetch(a) -> int:
    from investordb.fetch import fetch_all
    from investordb.records import load_records

    return fetch_all(load_records(a.records), a.cache, force=a.force,
                     use_wayback=not a.no_wayback, limit=a.limit)


def cmd_verify(a) -> int:
    from investordb.records import load_records
    from investordb.verify import run_verify

    return run_verify(load_records(a.records), a.cache, a.out)


def cmd_decide(a) -> int:
    from investordb.records import load_records
    from investordb.rules import run_decide

    return run_decide(load_records(a.records), a.negative_list, a.out,
                      ref_date=a.ref_date or date.today(), window_months=a.months)


def cmd_grade(a) -> int:
    from investordb.grade import run_grade
    from investordb.records import load_records

    return run_grade(load_records(a.records), a.verification, a.out_json, a.out_csv,
                     ignore_verify=a.ignore_verify)


def cmd_review_pack(a) -> int:
    from investordb.records import load_records
    from investordb.review import run_review_pack

    return run_review_pack(load_records(a.records), a.n, a.seed, a.html, a.claims)


def cmd_eval(a) -> int:
    from investordb.evaluate import run_eval

    return run_eval(a.records, a.claims, a.labels, a.reference, a.verification,
                    a.decision_check, a.graded, a.out_md, a.out_json, a.model_labels)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="investordb", description="Investor database tooling")
    sub = p.add_subparsers(dest="cmd", required=True)

    def add(name, fn, help_):
        sp = sub.add_parser(name, help=help_)
        sp.add_argument("--records", default=RECORDS, help=f"records JSON (default {RECORDS})")
        sp.set_defaults(fn=fn)
        return sp

    sp = add("validate", cmd_validate, "schema + consistency checks")
    sp.add_argument("--schema", default=None)
    sp.add_argument("--today", type=_date, default=None, help="date treated as today")

    sp = add("fetch", cmd_fetch, "download every source URL into the cache")
    sp.add_argument("--cache", default=CACHE)
    sp.add_argument("--force", action="store_true", help="re-download cached URLs")
    sp.add_argument("--no-wayback", action="store_true")
    sp.add_argument("--limit", type=int, default=None, help="fetch at most N URLs")

    sp = add("verify", cmd_verify, "check quotes and values against fetched pages")
    sp.add_argument("--cache", default=CACHE)
    sp.add_argument("--out", default=VERIFICATION)

    sp = add("decide", cmd_decide, "recompute decisions and compare with stored ones")
    sp.add_argument("--negative-list", default="data/negative_list.csv")
    sp.add_argument("--out", default="data/sample/decision_check.csv")
    sp.add_argument("--ref-date", type=_date, default=None, help="default: today")
    sp.add_argument("--months", type=int, default=36, help="recency window (I3/E4)")

    sp = add("grade", cmd_grade, "confidence A/B/C per record")
    sp.add_argument("--verification", default=VERIFICATION)
    sp.add_argument("--out-json", default="data/sample/investors.graded.json")
    sp.add_argument("--out-csv", default="data/sample/investors.csv")
    sp.add_argument("--ignore-verify", action="store_true",
                    help="grade on claimed tiers only (no verification file)")

    sp = add("review-pack", cmd_review_pack, "build the static review page")
    sp.add_argument("--n", type=int, default=60)
    sp.add_argument("--seed", type=int, default=7)
    sp.add_argument("--html", default="eval/review.html")
    sp.add_argument("--claims", default="eval/claims.csv")

    sp = add("eval", cmd_eval, "accuracy metrics from review labels")
    sp.add_argument("--labels", default="eval/labels.csv")
    sp.add_argument("--model-labels", default="eval/labels-model.csv",
                    help="labels from a model review of the same sample, reported separately")
    sp.add_argument("--claims", default="eval/claims.csv")
    sp.add_argument("--reference", default="data/reference")
    sp.add_argument("--verification", default=VERIFICATION)
    sp.add_argument("--decision-check", default="data/sample/decision_check.csv")
    sp.add_argument("--graded", default="data/sample/investors.graded.json")
    sp.add_argument("--out-md", default="eval/ACCURACY.md")
    sp.add_argument("--out-json", default="eval/metrics.json")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.fn(args)
    except DataError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
