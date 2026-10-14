"""Build the public copy of the review page (deployed to Vercel).

eval/review.html is the frozen snapshot the reviewers actually used, so it stays untouched.
This script copies it to public/index.html, adds a short banner on top and pre-fills the
reviewers' verdicts from eval/labels.csv, so a visitor sees the finished review instead of
60 empty cards. Anything the visitor clicks stays in their own browser.
"""

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/alexxkra777/reliable-investor-db"
REVIEWED_ON = "2026-10-11"

BANNER = """<section class="card live-note">
    <p><b>Live copy of the review tool used to measure accuracy.</b> Two reviewers checked all
      60 sampled claims against their sources on 11 October 2026: {correct} correct,
      {wrong} wrong. Their verdicts and notes are filled in below. The cards show the data as it
      was reviewed; both wrong values were corrected in the dataset afterwards.</p>
    <p>You can change any verdict to try the tool &mdash; your marks stay in this browser only.</p>
    <p class="live-links"><button type="button" id="restore">Restore reviewers' verdicts</button>
      <a href="{repo}/blob/main/eval/ACCURACY.md">Accuracy report</a>
      <a href="{repo}/blob/main/eval/CORRECTIONS.md">Corrections</a>
      <a href="{repo}">Repository</a></p>
  </section>
  """

EXTRA_CSS = """.live-note { border-left: 5px solid var(--accent); font-size: 15px; }
.live-note p { margin: 0 0 8px; }
.live-links { display: flex; flex-wrap: wrap; gap: 8px 16px; align-items: center; }
.live-links a { color: var(--accent); }
</style>"""

RESTORE_JS = """<script>
document.getElementById("restore").addEventListener("click", function () {
  try { window.localStorage.removeItem(KEY_FOR_RESTORE); } catch (e) {}
  window.location.reload();
});
</script>
</body>"""


def read_verdicts(path: Path) -> dict:
    with path.open(newline="", encoding="utf-8") as f:
        return {
            row["claim_id"]: {
                "label": row["label"],
                "note": row.get("note") or "",
                "reviewed_at": REVIEWED_ON,
            }
            for row in csv.DictReader(f)
        }


def replace_once(html: str, old: str, new: str) -> str:
    # the page is generated, so if any anchor moved we'd rather fail loudly than ship it broken
    if html.count(old) != 1:
        raise SystemExit(f"anchor not found exactly once: {old!r}")
    return html.replace(old, new)


def build(review_html: str, verdicts: dict) -> str:
    counts = {"correct": 0, "wrong": 0}
    for v in verdicts.values():
        counts[v["label"]] = counts.get(v["label"], 0) + 1

    key = re.search(r'var KEY = "([^"]+)";', review_html)
    if not key:
        raise SystemExit("storage key not found in review.html")

    html = review_html
    html = replace_once(
        html,
        "<title>Investor claims review</title>",
        "<title>Investor claims review &mdash; reliable investor database</title>",
    )
    html = replace_once(html, "</style>", EXTRA_CSS)
    # the review is finished, so the reviewer instructions start folded
    html = replace_once(html, '<details class="help" open>', '<details class="help">')
    html = replace_once(html, "<main>\n", "<main>\n  " + BANNER.format(repo=REPO_URL, **counts))
    # reviewers' verdicts are the starting state; a visitor's own edits override them
    prefill = json.dumps(verdicts, ensure_ascii=False).replace("</", "<\\/")
    fresh = "JSON.parse(JSON.stringify(REVIEWED))"
    html = replace_once(
        html, "  var state = {};", f"  var REVIEWED = {prefill};\n  var state = {fresh};"
    )
    html = replace_once(
        html, "storageOk = false; state = {};", f"storageOk = false; state = {fresh};"
    )
    html = replace_once(
        html, "</body>", RESTORE_JS.replace("KEY_FOR_RESTORE", json.dumps(key.group(1)))
    )
    return html


def main(out_dir: Path) -> None:
    html = build(
        (ROOT / "eval/review.html").read_text(encoding="utf-8"),
        read_verdicts(ROOT / "eval/labels.csv"),
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"wrote {out_dir / 'index.html'}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "public")
