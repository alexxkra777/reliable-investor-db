"""Merge the per-country parts into data/sample/investors.json.

Both researchers ran into the same firms (Czech VCs show up in Slovak lists and the other way
round). One record per investor survives: the one written by the researcher of the country the
manager actually sits in. A short override list covers the cases where that rule picks the
weaker record.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS = {"SK": ROOT / "data/sample/parts/sk.json", "CZ": ROOT / "data/sample/parts/cz.json"}
OUT = ROOT / "data/sample/investors.json"

# name key -> part to keep, when the HQ rule gets it wrong
OVERRIDES = {
    # Warsaw private-debt manager: the SK record has the sharper call (E3, lender), CZ only says PE
    "cvi": "SK",
}


def key(name: str) -> str:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"\b(vc|ventures?|capital|fund|a\.?s\.?|s\.?r\.?o\.?|investments?)\b", "", s)
    s = re.sub(r"[^a-z0-9]", "", s)
    return {"n1": "nation1", "jetjet": "jet"}.get(s, s)


def main() -> int:
    parts = {c: json.loads(p.read_text()) for c, p in PARTS.items()}
    chosen: dict[str, tuple[str, dict]] = {}
    log = []
    for country, records in parts.items():
        for rec in records:
            k = key(rec["name"])
            if k not in chosen:
                chosen[k] = (country, rec)
                continue
            prev_country, prev = chosen[k]
            hq = (rec.get("hq") or {}).get("country")
            keep = OVERRIDES.get(k) or (country if hq == country else prev_country)
            if keep == country:
                chosen[k] = (country, rec)
            dropped = prev if keep == country else rec
            log.append(f"{rec['name']}: kept {keep}, dropped {dropped['decision']['status']} from "
                       f"{prev_country if keep == country else country}")
    merged = sorted((r for _, r in chosen.values()), key=lambda r: r["id"])
    ids = [r["id"] for r in merged]
    if len(ids) != len(set(ids)):
        dup = sorted({i for i in ids if ids.count(i) > 1})
        print(f"duplicate ids after merge: {dup}", file=sys.stderr)
        return 1
    OUT.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n")
    print("\n".join(log))
    total = sum(len(v) for v in parts.values())
    print(f"{total} part records -> {len(merged)} investors in {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
