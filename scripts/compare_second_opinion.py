"""Compare stored decisions with a blind second review (eval/second-opinion/codex.json).

The second reviewer only saw names, countries and websites, so agreement here is evidence that
the decisions don't depend on one researcher's reading of the sources.
"""

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = date(2026, 10, 11)
CUTOFF = date(2023, 10, 11)


def main() -> None:
    ours = {r["id"]: r for r in json.loads((ROOT / "data/sample/investors.json").read_text())}
    theirs = json.loads((ROOT / "eval/second-opinion/codex.json").read_text())
    rows, agree_inv, agree_active, n_active = [], 0, 0, 0
    for t in theirs:
        r = ours.get(t["id"])
        if not r:
            continue
        status = r["decision"]["status"]
        dates = [i.get("date") for i in r.get("investments") or [] if i.get("date")]
        our_last = max(dates) if dates else None
        our_active = bool(our_last and date.fromisoformat(our_last) >= CUTOFF)
        their_active = t.get("active_36m")
        inv_ok = (t.get("is_investor") == "yes") == (status not in ("excluded",))
        agree_inv += inv_ok
        if their_active in ("yes", "no"):
            n_active += 1
            agree_active += (their_active == "yes") == our_active
        li = t.get("latest_investment") or {}
        rows.append(
            (
                r["name"],
                status,
                our_last or "-",
                their_active or "-",
                f"{li.get('company', '-')} {li.get('date', '')}".strip(),
                t.get("type", "-"),
                r.get("type", "-"),
                ""
                if inv_ok
                and (their_active not in ("yes", "no") or (their_active == "yes") == our_active)
                else "**differs**",
            )
        )
    out = [
        "# Blind second review vs stored decisions",
        "",
        f"Reviewer saw only name, country and website for {len(rows)} records "
        "(included, uncertain and dormant). Reference date 2026-10-11, activity window 36 months.",
        "",
        "- Real investor (yes/no) agrees with our include/keep decision: "
        f"**{agree_inv}/{len(rows)}**",
        f"- Active within 36 months agrees: **{agree_active}/{n_active}** "
        f"(records where the reviewer could decide)",
        "",
        "| Investor | Our status | Our last dated deal | Reviewer: active | Reviewer: latest deal | "
        "Reviewer type | Our type | |",
        "|---|---|---|---|---|---|---|---|",
    ]
    ordered = sorted(rows, key=lambda x: x[-1] == "")
    out += ["| " + " | ".join(map(str, r)) + " |" for r in ordered]
    (ROOT / "eval/second-opinion/comparison.md").write_text("\n".join(out) + "\n")
    print("\n".join(out[:8]))


if __name__ == "__main__":
    main()
