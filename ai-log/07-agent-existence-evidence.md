# Agent: existence evidence and re-decisions

Claude Code sub-agent log, exported from `agent-a7c9068e4184f1a94.jsonl`.
Tool outputs longer than 1,500 characters are shortened.
Russian narrative has been translated into English; executed tool code and source quotations are retained.

## Brief

You are a data analyst on an investor-database project in [redacted: local path] Read PLAN.md (rules I1–I4, E1–E10, S1, tiers A/B/C) and schema/investor.schema.json (note the new `fields.existence` field) first. All file content in English (source quotes stay verbatim in their language). Final message in English.

Task: enrich the pilot records with evidence for rule I2 ("investing is a core activity") and resolve open cases. Edit ONLY data/sample/parts/sk.json and data/sample/parts/cz.json (the per-country source files), and data/sample/parts/sk-decisions.md / cz-decisions.md lines for records whose decision you change. Then run `.venv/bin/python scripts/merge_parts.py` and `.venv/bin/python -m investordb validate --today 2026-10-11` (must end with 0 errors).

1. For every record with decision status included, uncertain or dormant (about 45), add `fields.existence` = {"value": [one or more of "regulator_register", "fund_of_funds_commitment", "association_full_member", "portfolio_page"], "sources": [...]} with at least one source:
   - regulator_register (tier A): ESMA register entry (EuVECA/AIFM), ČNB JERRS / NBS register page, SEC IAPD — if you can get a raw page that names the manager.
   - fund_of_funds_commitment (tier A): EIF list of equity fund managers for CZ/SK (PDFs on eif.org — find the current ones), SIH / NDF II / NRI portfolio pages naming the fund.
   - association_full_member (tier B): CVCA members page (https://www.cvca.cz/en/members/ — check which section is full members), SLOVCA ordinary members page (https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html).
   - portfolio_page (tier B): the investor's own portfolio page listing at least 3 companies — the quote must contain 3+ company names as they appear in the raw text.
   If none exists, leave existence null and say so in the decision note.
2. Re-decide the 13 uncertain records (Startguide, GAIN Ventures, BHM Ventures, Czech Founders VC, Orbit Capital, Impulse Ventures, KOOPEO, Air Ventures, Springtide, UP21, RockawayX, ČS Seed Starter, Baryon Fund): with a bit more searching, move each to included / excluded / dormant / out_of_scope where the evidence allows; keep "uncertain" only when truly unresolvable, with the reason. For included ones a dated investment within 36 months before 2026-10-11 with a Tier A/B source is required (I3).
3. Quotes: VERBATIM from the raw page text. WebFetch returns a model-written summary — never copy quotes from it. Fetch raw with curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36" (or python urllib), extract text (strip script/style, html.unescape; PDFs via [redacted: local path] with pypdf), and confirm each quote with a substring check on whitespace-normalised text before writing it. accessed = 2026-10-11.
4. Afterwards run `.venv/bin/python -m investordb fetch` then `verify` then `decide --ref-date 2026-10-11` and report the decide disagreements that remain, with your view on each (is the stored decision or the rule engine right?). Don't change the engine code.

Rules: keep working files in [redacted: local path] and delete nothing outside it. Don't run git. Don't use the Playwright MCP browser. No signups/forms. No AI/tool mentions in data files.

Final message: per-status counts before/after, how many records got existence evidence by kind, the remaining disagreements with your view, and any decision changes with one-line reasons.

→ `Bash` — Read plan, schema, list project files
```sh
ls -la && cat PLAN.md && cat schema/investor.schema.json && ls -la data/sample/parts scripts investordb
```

<details><summary>result</summary>

```
Exit code 1
total 48
drwxr-xr-x  16 [user]  staff    512 11 Oct  06:12 .
drwxr-xr-x   5 [user]  staff    160 11 Oct  01:56 ..
drwxr-xr-x  12 [user]  staff    384 11 Oct  06:16 .git
-rw-r--r--   1 [user]  staff     72 11 Oct  01:27 .gitignore
drwxr-xr-x   6 [user]  staff    192 11 Oct  01:45 .pytest_cache
drwxr-xr-x   5 [user]  staff    160 11 Oct  01:29 .ruff_cache
drwxr-xr-x   7 [user]  staff    224 11 Oct  01:27 .venv
drwxr-xr-x   6 [user]  staff    192 11 Oct  06:12 data
drwxr-xr-x   3 [user]  staff     96 11 Oct  06:13 eval
-rw-r--r--   1 [user]  staff  13005 11 Oct  06:02 PLAN.md
-rw-r--r--   1 [user]  staff    788 11 Oct  01:27 pyproject.toml
drwxr-xr-x   5 [user]  staff    160 11 Oct  01:34 research
drwxr-xr-x   3 [user]  staff     96 11 Oct  01:28 schema
drwxr-xr-x   3 [user]  staff     96 11 Oct  06:12 scripts
drwxr-xr-x   4 [user]  staff    128 11 Oct  01:29 src
drwxr-xr-x  13 [user]  staff    416 11 Oct  01:47 tests
# Plan: a reliable database of investors

The point of this database is trust. A record is only worth something if a reader can click
through to a public page and see for themselves that the entity invests, in what, how much,
and since when. So the plan is built around evidence first and coverage second.

Research behind the numbers below: [`research/sources-and-universe.md`](research/sources-and-universe.md).

---

## 1. What counts as an investor

**Unit of a record = the investing organisation (manager), or a person investing in their own name.**
Not
… [8540 more characters]
```
</details>

→ `Read` [redacted: local path]

<details><summary>result</summary>

```
1	# Plan: a reliable database of investors
2
3	The point of this database is trust. A record is only worth something if a reader can click
4	through to a public page and see for themselves that the entity invests, in what, how much,
5	and since when. So the plan is built around evidence first and coverage second.
6
7	Research behind the numbers below: [`research/sources-and-universe.md`](research/sources-and-universe.md).
8
9	---
10
11	## 1. What counts as an investor
12
13	**Unit of a record = the investing organisation (manager), or a person investing in their own name.**
14	Not the fund vehicle, not the SPV, not the brand. A manager with five funds is one record with
15	five funds attached. This matters a lot: 64 % of "venture capital fund" issuers in the last
16	four quarters of SEC Form D filings are one-deal SPVs or series vehicles. Counting vehicles
17	would triple the database with noise.
18
19	### Types
20
21	| Type | Definition used here |
22	|---|---|
23	| `vc` | Manages third-party or own capital and takes minority equity / convertible stakes in young private companies (pre-seed to growth). |
24	| `pe` | Buyout, growth or mezzanine investor in established private companies, usually majority or significant minority stakes. |
25	| `cvc` | Investment arm of a corporation (banks and insurers included) that puts balance-sheet money into third-party startups. A bank's lending is E3; a bank's startup equity program is `cvc`. |
26	| `family_office` | Single or mult
… [12030 more characters]
```
</details>

→ `Bash` — Read schema head, merge script, src listing
```sh
sed -n 1,200p schema/investor.schema.json; cat scripts/merge_parts.py; ls -R src | head -50; ls data data/sample
```

<details><summary>result</summary>

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/investor-db/investor.schema.json",
  "title": "Investor records",
  "description": "A JSON array of investor records. Every non-null value carries its own sources.",
  "type": "array",
  "items": {
    "$ref": "#/$defs/record"
  },
  "$defs": {
    "date": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "format": "date"
    },
    "currency": {
      "type": "string",
      "pattern": "^[A-Z]{3}$"
    },
    "money": {
      "type": [
        "number",
        "null"
      ],
      "minimum": 0
    },
    "url": {
      "type": "string",
      "pattern": "^https?://\\S+$"
    },
    "source": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "url",
        "tier",
        "publisher",
        "published",
        "accessed",
        "quote"
      ],
      "properties": {
        "url": {
          "$ref": "#/$defs/url"
        },
        "tier": {
          "enum": [
            "A",
            "B",
            "C"
          ]
        },
        "publisher": {
          "type": "string",
          "minLength": 1
        },
        "published": {
          "oneOf": [
            {
              "$ref": "#/$defs/date"
            },
            {
              "type": "null"
            }
          ]
        },
        "accessed": {
          "$ref": "#/$defs/date"
        },
        "quote": {
          "type": "strin
… [5890 more characters]
```
</details>

→ `Bash` — Read rest of schema, rule engine, CLI
```sh
sed -n 200,330p schema/investor.schema.json; cat src/investordb/rules.py; cat src/investordb/cli.py | head -150
```

<details><summary>result</summary>

```
      ]
    },
    "legalEntity": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "name",
        "role",
        "id_type",
        "id"
      ],
      "properties": {
        "name": {
          "type": "string",
          "minLength": 1
        },
        "role": {
          "enum": [
            "manager",
            "fund",
            "vehicle"
          ]
        },
        "id_type": {
          "enum": [
            "ICO",
            "LEI",
            "CRD",
            "CIK",
            "company_number"
          ]
        },
        "id": {
          "type": "string",
          "minLength": 1
        },
        "register_url": {
          "oneOf": [
            {
              "$ref": "#/$defs/url"
            },
            {
              "type": "null"
            }
          ]
        }
      }
    },
    "investment": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "company",
        "date",
        "date_kind",
        "sources"
      ],
      "properties": {
        "company": {
          "type": "string",
          "minLength": 1
        },
        "date": {
          "oneOf": [
            {
              "$ref": "#/$defs/date"
            },
            {
              "type": "null"
            }
          ]
        },
        "date_kind": {
          "enum": [
            "announced",
            "registry_entry",
            "portfolio_page"
          ]
        },
… [14474 more characters]
```
</details>

→ `Bash` — Summarise records per country and status
```sh
.venv/bin/python - <<'EOF'
import json
for c in ['sk','cz']:
    recs=json.load(open(f'data/sample/parts/{c}.json'))
    print('==',c,len(recs))
    from collections import Counter
    print(Counter(r['decision']['status'] for r in recs))
    for r in recs:
        d=r['decision']
        f=r['fields']
        print(f"{r['id']:35} {r['type']:15} {d['status']:12} {d.get('rules')} web={r.get('website')} exist={'Y' if f.get('existence') else '-'} inv={len(r.get('investments') or [])} hq={(r.get('hq') or {}).get('country')}")
EOF
cat data/sample/parts/sk-decisions.md | head -80
```

<details><summary>result</summary>

```
== sk 49
Counter({'excluded': 19, 'out_of_scope': 16, 'included': 7, 'dormant': 6, 'uncertain': 1})
neulogy-ventures                    vc              included     ['I1', 'I2', 'I3', 'I4'] web=https://www.neulogy.vc/ exist=- inv=3 hq=SK
vision-ventures                     vc              included     ['I1', 'I2', 'I3', 'I4'] web=https://visionventures.vc/ exist=- inv=3 hq=SK
venture-to-future-fund              vc              included     ['I1', 'I2', 'I3', 'I4'] web=https://vff.sk/ exist=- inv=4 hq=SK
zero-one-hundred                    vc              included     ['I1', 'I2', 'I3', 'I4'] web=https://0100.vc/ exist=- inv=2 hq=SK
g-force                             accelerator     included     ['I1', 'I2', 'I3', 'I4'] web=None exist=- inv=1 hq=SK
cb-investment-management            vc              included     ['I1', 'I2', 'I3', 'I4'] web=https://www.cbim.sk/ exist=- inv=2 hq=SK
seed-starter-slovenskej-sporitelne  cvc             included     ['I1', 'I2', 'I3', 'I4'] web=None exist=- inv=3 hq=SK
baryon-fund                         vc              uncertain    ['I2'] web=https://www.baryon.fund/ exist=- inv=1 hq=None
lrj-capital                         vc              dormant      ['E4'] web=None exist=- inv=1 hq=None
ipm-group                           vc              dormant      ['E4'] web=None exist=- inv=3 hq=GB
fond-inovacii-a-technologii         vc              dormant      ['E4'] web=https://www.fondfit.sk/ exist=- inv=0 hq=SK
limerock                            vc
… [17017 more characters]
```
</details>

→ `Bash` — Read CZ decisions and one sample record
```sh
cat data/sample/parts/cz-decisions.md; .venv/bin/python - <<'EOF'
import json
recs={r['id']:r for r in json.load(open('data/sample/parts/cz.json'))}
print(json.dumps(recs['credo-ventures'],ensure_ascii=False,indent=1)[:6000])
EOF
```

<details><summary>result</summary>

```
# Czech pilot candidates: decisions

Accessed 2026-10-11. One line per candidate: name — status — rule IDs — reason. All records are in `cz.json`; the last section lists candidates that got no record.

## Records in cz.json

- Credo Ventures — included — I1, I2, I3, I4 — Prague pre-seed VC, CVCA full member; latest dated deal Supernova (30 Sep 2025), Tier A holding in Delta Green (May 2024).
- Presto Ventures — included — I1, I2, I3, I4 — Prague seed/Series A and defence VC; Presto Ventures II entered Lakmoos AI on 9 Jun 2026 (justice.cz).
- Reflex Capital — included — I1, I2, I3, I4 — Prague VC; Reflex 3 entered Ranketta on 7 Oct 2026 (justice.cz).
- J&T Ventures — included — I1, I2, I3, I4 — Prague VC with Czech SICAV vehicles; own blog dates investments in Finlay (Mar 2025) and grid.online (Apr 2025).
- Tilia Impact Ventures — included — I1, I2, I3, I4 — Prague impact VC, EIF-backed Fund II; Tier A holding in Delta Green (May 2024), led Flox Seed+ (Feb 2026, media).
- KAYA VC — included — I1, I2, I3, I4 — Prague-seated CEE VC (KAYA Advisory s.r.o., EIF list); E2B Series A (28 Jul 2025) on the startup's own blog.
- Lighthouse Ventures — included — I1, I2, I3, I4 — Prague seed VC backed by the Czech ESIF fund of funds; own news dates Hermetiq (31 Aug 2026), Seed Fund II in Ranketta (justice.cz).
- ZAKA VC — included — I1, I2, I3, I4 — Prague-registered seed VC investing mainly in US/Europe; own news dates PerfectBit (18 Aug 2026) and FinalDose (16 Jul 2026).
- Purple Venture
… [12649 more characters]
```
</details>

→ `Bash` — Read validator and text normalisation
```sh
cat src/investordb/validate.py | head -200; cat src/investordb/textnorm.py; grep -n "existence\|portfolio_page" -r src | head -30
```

<details><summary>result</summary>

```
import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator

from investordb.records import FIELD_NAMES, parse_date, repo_root

INCLUSION_RULES = {"I1", "I2", "I3", "I4"}


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def default_schema_path() -> Path:
    local = Path("schema/investor.schema.json")
    return local if local.exists() else repo_root() / "schema" / "investor.schema.json"


def load_validator(schema_path: str | Path | None = None) -> Draft202012Validator:
    schema = json.loads(Path(schema_path or default_schema_path()).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)


def _where(rec: dict, i: int) -> str:
    return rec.get("id") or f"#{i}"


def _deepest(err):
    # oneOf/allOf hide the useful message somewhere inside err.context
    if not err.context:
        return err
    cands = [_deepest(e) for e in err.context]
    return max(cands, key=lambda e: (len(e.absolute_path), e.validator != "type"))


def schema_errors(records, validator: Draft202012Validator) -> list[str]:
    out = []
    for top in sorted(validator.iter_errors(records), key=lambda e: list(e.absolute_path)):
        err = _deepes
… [15743 more characters]
```
</details>

→ `Bash` — Check field names and fetch/caching logic
```sh
grep -n "FIELD_NAMES" -A3 src/investordb/records.py; sed -n 1,80p src/investordb/fetch.py; ls data/cache | head; ls data/cache | wc -l; ls data/reference
```

<details><summary>result</summary>

```
8:FIELD_NAMES = ("sectors", "stages", "geography", "ticket", "ticket_observed", "funds", "aum")
9-TIER_RANK = {"A": 0, "B": 1, "C": 2}
10-
11-
--
42:    for name in FIELD_NAMES:
43-        f = fields.get(name)
44-        if not f:
45-            continue
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
        self.clock, se
… [1317 more characters]
```
</details>

→ `Bash` — Read records helpers and reference lists
```sh
sed -n 1,80p src/investordb/records.py; cat data/reference/cvca-full-members.csv | head -80; cat data/negative_list.csv | head -40
```

<details><summary>result</summary>

```
import json
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

FIELD_NAMES = ("sectors", "stages", "geography", "ticket", "ticket_observed", "funds", "aum")
TIER_RANK = {"A": 0, "B": 1, "C": 2}


class DataError(Exception):
    pass


@dataclass
class Target:
    """One sourced thing inside a record: a field or an investment."""

    key: str  # "fields.ticket" or "investments[3]"
    kind: str  # field name or "investment"
    value: Any
    sources: list[dict]
    label: str = ""


def load_records(path: str | Path) -> list[dict]:
    p = Path(path)
    if not p.exists():
        raise DataError(f"records file not found: {p}")
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise DataError(f"{p} is not valid JSON: {e}") from e
    if not isinstance(data, list):
        raise DataError(f"{p} must contain a JSON array of records")
    return data


def iter_targets(rec: dict) -> Iterator[Target]:
    fields = rec.get("fields") or {}
    for name in FIELD_NAMES:
        f = fields.get(name)
        if not f:
            continue
        yield Target(f"fields.{name}", name, f.get("value"), f.get("sources") or [], name)
    for i, inv in enumerate(rec.get("investments") or []):
        yield Target(f"investments[{i}]", "investment", inv, inv.get("sources") or [],
                     inv.get("company", ""))


def parse_dat
… [2554 more characters]
```
</details>

→ `Bash` — Create work dirs and inspect fetch/verify
```sh
mkdir -p [redacted: local path] [redacted: local path] && cd [redacted: local path] && sed -n 80,200p src/investordb/fetch.py | head -80; grep -n "def \|pdf\|text" src/investordb/verify.py | head -40
```

<details><summary>result</summary>

```
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
            return
… [2495 more characters]
```
</details>

**Agent:**

Now I'll write the fetch and quote-check helpers.

→ `Bash` — Write fetch, quote-check and grep helpers
```sh
cat > [redacted: local path] <<'EOF'
"""get.py URL [URL...] -> saves raw bytes + extracted text in pages/, prints path and size."""
import hashlib, sys, subprocess, re, html
from pathlib import Path
sys.path.insert(0, "[redacted: local path]")
from investordb.fetch import extract_text

PAGES = Path("[redacted: local path]")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"

def key(u): return hashlib.sha1(u.encode()).hexdigest()[:16]

def get(url, force=False):
    k = key(url)
    raw, txt = PAGES / f"{k}.raw", PAGES / f"{k}.txt"
    if force or not txt.exists():
        r = subprocess.run(["curl", "-sL", "--max-time", "40", "-A", UA, "-H", "Accept-Language: en,cs;q=0.9,sk;q=0.8",
                            "-w", "\n__STATUS__%{http_code} %{content_type} %{url_effective}", url], capture_output=True)
        data = r.stdout
        m = data.rfind(b"\n__STATUS__")
        meta = data[m+11:].decode(errors="replace") if m >= 0 else "?"
        body = data[:m] if m >= 0 else data
        raw.write_bytes(body)
        ct = meta.split(
… [2003 more characters]
```

<details><summary>result</summary>

```
ok
```
</details>

→ `Bash` — Fetch CVCA and SLOVCA member pages
```sh
cd [redacted: local path] && P=bin; ../../investor-db/.venv/bin/python bin/get.py https://www.cvca.cz/en/members/ https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html;
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://cvca.cz/en/membership/  len=41912
[redacted: local path]  200 text/html; charset=UTF-8 https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html  len=1060
```
</details>

→ `Bash` — Inspect SLOVCA page text and raw
```sh
cd [redacted: local path] && cat pages/4dfaff18d247468c.txt; echo ======; head -c 3000 pages/4dfaff18d247468c.raw | tail -c 1500; echo; grep -o 'members[^"]*' pages/4dfaff18d247468c.raw | sort -u | head
```

<details><summary>result</summary>

```
Exit code 1
Riadni členovia / Slovak Venture Capital & Private Equity Association SLOVCA
Riadni členovia
ARX Equity Partners
CVI
Enterprise Investors
Eterus Capital
Fond inovácií a technológií
Genesis Capital
Jet Investment
Národný holdingový fond s.r.o.
Neulogy Ventures
Sandberg Capital
Venture to Future Fund
Vision Ventures
Členstvo
Riadni členovia
Pridružení členovia
Partnerskí členovia
Partneri
Etický kódex
Prihláška
Čerstvé správy!
Prihláste sa na odber noviniek SLOVCA a získajte informácie o private equity trhu v EU a na Slovensku ako aj najnovšie štatistiky o investovanom rozvojovom kapitáli.
Registrovať
Slovak Venture Capital & Private Equity Association SLOVCA
+421-2-21 201 010
[redacted: email address]
Štúrova 12/4, 811 02 Bratislava-Staré Mesto
Slovakia
O nás
SLOVCA dnes
Správna rada
Legal & Tax Committee
Stanovy
Členstvo
Riadni členovia
Pridružení členovia
Partnerskí členovia
Partneri
Etický kódex
Prihláška
Na stiahnutie
Štatistiky
Tlačové správy
Vzorové dokumenty
Novinky
Novinky ohľadom PE-VC
Podujatia
Web vytvoril
Fresh idea
. Dizajn Michaela Lipková.(eval):1: ===== not found
```
</details>

→ `Bash` — Inspect CVCA membership page sections
```sh
cd [redacted: local path] && sed -n 1,400p pages/adbdfc25bd2e2860.txt | grep -n -i -E "member|ventures|capital|biotech|fund|startup|seed|depo|kaya|nation|tensor|orbit|tilia|inven|credo|presto|reflex|lighthouse|zaka|purple|rockaway|miton|soulmates|startguide|gain|czech founders|springtide|j&t|jt " | head -150
```

<details><summary>result</summary>

```
1:Membership – CVCA
4:CVCA offers two types of membership – full membership and associated membership.
5:Full members
7:Associate members
9:Full members
10:Associate members
11:Full members
12:Abris Capital
15:Full members
17:Address ul. Grzybowska 5a Grzybowska Park 00-132 Warsaw Poland www.abris-capital.com Contact Renáta Ďurčová [redacted: email address] Information about the company Volume of Funds Managed EUR 502 mil (Abris Fund III), EUR 450 mil (Abris Fund II) Type of Investment Growth and buyout acquisitions – management buyouts (MBO & MBI), expansion financing, industry consolidation Preferred Ammount of Investment …
24:Full members
26:Address 28. října 12110 00 Prague 1+420 224 235 399www.arxequity.com Contact Michal [redacted: email address] Information about the company Volume of Funds Managed EUR 300 million Type of Investment acquisitions, management buyout (MBO & MBI), expansion capital, sector consolidation Preferred Ammount of Investment EUR 5 – 50 million (total transaction) Sectore Preferences – Geographical Focus Central Europe …
30:Credo Ventures
33:Full members
35:Address Karlovo Náměstí 10120 00 Prague 2+420 211 153 211www.credoventures.com Contact Vladislav [redacted: email address] Information about the company Volume of Funds Managed EUR 170 million Type of Investment start-up, growth capital, expansion capital Preferred Ammount of Investment 50k EUR – 10M EUR Sector Preferences IT & internet, mobile communication, Geographical Focus CEE
… [13909 more characters]
```
</details>

→ `Bash` — Inspect CVCA entry layout and associate VC members
```sh
cd [redacted: local path] && sed -n 28,36p pages/adbdfc25bd2e2860.txt; sed -n 118,128p pages/adbdfc25bd2e2860.txt;  sed -n 224,232p pages/adbdfc25bd2e2860.txt; grep -n -i -E "ventures|startup|seed|fund" pages/adbdfc25bd2e2860.txt | awk -F: '$1>253' | head -40
```

<details><summary>result</summary>

```
…
Read More
Credo Ventures
dk
14. 1. 2020
Full members
(0)
Address Karlovo Náměstí 10120 00 Prague 2+420 211 153 211www.credoventures.com Contact Vladislav [redacted: email address] Information about the company Volume of Funds Managed EUR 170 million Type of Investment start-up, growth capital, expansion capital Preferred Ammount of Investment 50k EUR – 10M EUR Sector Preferences IT & internet, mobile communication, Geographical Focus CEE Number of Deals in …
Více…
…
Read More
Inven Capital
dk
14. 1. 2020
Full members
(0)
Address Pod křížkem 1773/2147 00 Prague 4 – Braník+420 602 758 498www.invencapital.cz Contact Petr MíkovecManaging [redacted: email address] Information about the company Volume of Funds Managed 250 mio EUR (Subfund A + B) + 250 mio EUR (Subfund C + D) Type of Investment Investments into small to middle-market innovative cleantech companies in later stage growth. Preferred …
Více…
…
Read More
…
Read More
Tilia Impact Ventures – Honorary Member
dk
6. 1. 2020
Full members
(0)
Address Tilia Impact VenturesDrtinova 557/10150 00 Praha [redacted: email address] Contact Magdaléna RadováImpact & Investment [redacted: email address] Information about the company Volume of Funds Managed CZK 62,7 mil. Type of Investment Investment with societal and environmental impact Preferred Ammount of Investment CZK 1 mil – CZK 5 mil Sector Preferences Impact areas – Environment, Education, Inclusion & Civic …
Více…
405:Address Barckhausstraße 12-1
… [3406 more characters]
```
</details>

→ `Bash` — Dump compact view of the 45 target records
```sh
.venv/bin/python - <<'EOF'
import json
for c in ['sk','cz']:
    for r in json.load(open(f'data/sample/parts/{c}.json')):
        d=r['decision']
        if d['status'] not in ('included','uncertain','dormant'): continue
        print(f"### [{c}] {r['id']} | {r['name']} | {r['type']} | {d['status']} {d['rules']} | web={r.get('website')} | aliases={r.get('aliases')}")
        for le in r.get('legal_entities') or []: print("   LE:",le['name'],le['role'],le['id_type'],le['id'])
        print("   NOTE:",d.get('note'))
        f=r['fields'].get('funds')
        if f: print("   FUNDS:",[x['name'] for x in f['value']])
        for i in r.get('investments') or []:
            print("   INV:",i['company'],i['date'],[(s['tier'],s['url'][:90]) for s in i['sources']])
EOF
```

<details><summary>result</summary>

```
<persisted-output>
Output too large (33.2KB). Full output saved to: [redacted: private assistant config]

Preview (first 2KB):
### [sk] neulogy-ventures | Neulogy Ventures | vc | included ['I1', 'I2', 'I3', 'I4'] | web=https://www.neulogy.vc/ | aliases=['Neulogy Ventures, a. s.', 'Neulogy VC', 'Slovak Venture Fund S.C.A., SICAR']
   LE: Neulogy Ventures, a. s. manager ICO 47367610
   LE: Slovak Venture Fund S.C.A., SICAR fund company_number B185175
   NOTE: SLOVCA full member; EIF lists Neulogy Ventures a.s. as manager of Slovak Venture Fund S.C.A., SICAR (end of investment period 14/03/2027). Latest dated investment: the fund re-entered MultiplexDX, s.r.o. as shareholder on 17.01.2026 (it had left in 2018), so this is most likely a follow-on in a known portfolio company, not a new deal. SIH says its own SIH-backed compartments invested in 2014-2016 and are divesting. The Staffino registry line dated 18.10.2024 is only an address change of the fund (shareholder since 2015), so it is not counted. No new-company deal found after StratifAI (2024, aggregator only, not stored).
   FUNDS: ['Slovak Venture Fund S.C.A., SICAR']
   INV: MultiplexDX, s.r.o. 2026-01-17 [('A', 'https://www.orsr.sk/vypis.asp?ID=554899&SID=2&P=0'), ('A', 'https://www.orsr.sk/vypis.asp?ID=554899&SID=2&P=1')]
   INV: GA Drilling 2024-04-18 [('C', 'https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-
… [505 more characters]
```
</details>

→ `Read` [redacted: private assistant config]

<details><summary>result</summary>

```
1	### [sk] neulogy-ventures | Neulogy Ventures | vc | included ['I1', 'I2', 'I3', 'I4'] | web=https://www.neulogy.vc/ | aliases=['Neulogy Ventures, a. s.', 'Neulogy VC', 'Slovak Venture Fund S.C.A., SICAR']
2	   LE: Neulogy Ventures, a. s. manager ICO 47367610
3	   LE: Slovak Venture Fund S.C.A., SICAR fund company_number B185175
4	   NOTE: SLOVCA full member; EIF lists Neulogy Ventures a.s. as manager of Slovak Venture Fund S.C.A., SICAR (end of investment period 14/03/2027). Latest dated investment: the fund re-entered MultiplexDX, s.r.o. as shareholder on 17.01.2026 (it had left in 2018), so this is most likely a follow-on in a known portfolio company, not a new deal. SIH says its own SIH-backed compartments invested in 2014-2016 and are divesting. The Staffino registry line dated 18.10.2024 is only an address change of the fund (shareholder since 2015), so it is not counted. No new-company deal found after StratifAI (2024, aggregator only, not stored).
5	   FUNDS: ['Slovak Venture Fund S.C.A., SICAR']
6	   INV: MultiplexDX, s.r.o. 2026-01-17 [('A', 'https://www.orsr.sk/vypis.asp?ID=554899&SID=2&P=0'), ('A', 'https://www.orsr.sk/vypis.asp?ID=554899&SID=2&P=1')]
7	   INV: GA Drilling 2024-04-18 [('C', 'https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-g'), ('C', 'https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-g')]
8	   INV: Trustmatic 2023-10-24 [('B', 'https://neulogy.vc/news/')]
9	### [sk] vi
… [33219 more characters]
```
</details>

→ `Bash` — Find existing registry/FoF URLs used in data
```sh
grep -oh '"url": "[^"]*' data/sample/parts/*.json | sed 's/"url": "//' | grep -i -E "eif|sih|nri|nrinv|cvca|slovca|esma|cnb|nbs|sec.gov|fondfondu|ndf" | sort | uniq -c; ls research; grep -rl -i "eif.org" research | head
```

<details><summary>result</summary>

```
   1 https://cvca.cz/en/abris-capital-2/
   1 https://cvca.cz/en/arx-equity-partners-2/
   2 https://cvca.cz/en/credo-ventures-2/
   1 https://cvca.cz/en/cvi-2/
   1 https://cvca.cz/en/enterprise-investors-2/
   1 https://cvca.cz/en/espira-investments-2/
   1 https://cvca.cz/en/everita-capital-en/
   1 https://cvca.cz/en/genesis-capital-equity-s-r-o-2/
   1 https://cvca.cz/en/innova-capital-2/
   1 https://cvca.cz/en/integral-capital-group-2/
   1 https://cvca.cz/en/inven-capital-2/
   1 https://cvca.cz/en/jet-investment-2/
   1 https://cvca.cz/en/mam-private-equity-fund-sicav-a-s/
   1 https://cvca.cz/en/mid-europa-partners-2/
   5 https://cvca.cz/en/nation1-2/
   4 https://cvca.cz/en/orbit-capital-2/
   1 https://cvca.cz/en/sandberg-capital/
   1 https://cvca.cz/en/skylimit-investments-2/
   1 https://cvca.cz/en/stratum-partners-en/
   3 https://cvca.cz/en/tensor-ventures/
   1 https://cvca.cz/en/thein-2/
   1 https://cvca.cz/en/v4c-investment-advisers-limited-2/
   1 https://cvca.cz/en/versute-investments-2/
   4 https://www.eif.org/files/attachments/czechia-equity-fundmanagers.pdf
   1 https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf
   1 https://www.nrinvesticni.cz/
   1 https://www.sih.sk/en/aktuality/venture-to-future-fund-navysuje-kapital-o-15-3-miliona-eur-na-podporu-slovenskych-startupov
   1 https://www.slovca.sk/sk/riadni-clenovia/fond-inovacii-a-technologii.html
   5 https://www.slovca.sk/sk/riadni-clenovia/neulogy-ventures.html
   1 https:/
… [259 more characters]
```
</details>

→ `Bash` — Fetch EIF CZ and SK fund manager PDFs
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.eif.org/files/attachments/czechia-equity-fundmanagers.pdf https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf; for f in pages/*.txt; do :; done
```

<details><summary>result</summary>

```
[redacted: local path]  200 application/pdf https://www.eif.org/files/attachments/czechia-equity-fundmanagers.pdf  len=2367
[redacted: local path]  200 application/pdf https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf  len=611
```
</details>

→ `Bash` — Show EIF PDF texts
```sh
cd [redacted: local path] && cat pages/390aac3b6c876253.txt; echo =====; cat pages/1956281a9eeb9bef.txt
```

<details><summary>result</summary>

```
Exit code 1
 Public #
Fund name Fund manager Team location Mandate(s) short name Target area Geographical focus Strategy Main sector Stage focus Investment strategy set up End of investment period Fund Manager website
Tilia Impact Ventures Fund II Tilia Impact Partners Czech Republic IEU - Equity - LP Agriculture, Food, natural capital preservation and
use of land resources;Energy and built-environment
solutions;Industrial decarbonisation & environmental
sustainability;Mobility and transport solutions;Skills &
Education;Social impact Investing & Social Innovation
Multi-Country Venture Capital ICT Early Stage Fund Fund 01/08/2028 https://tiliaimpactventures.cz/en/
ARX CE V Cooperatief U.A ARX Equity Partners B.V. Czech Republic 3SIIF;EIF;IEU - Equity - PP;RCR Growth and expansion;Industrial decarbonisation &
environmental sustainability
Multi-Country Private Equity Generalist Growth-Oriented Buyout Fund 16/09/2029 http://www.arxequity.com/
Tensor Co-Investment Fund SCSp Tensor Advisory s.r.o Czech Republic RRF Czech Republic Artificial Intelligence (AI);Blockchain and Distributed
Ledger Technologies (BT/DLT);Clean Energy
Transition-Climate;Digital Connectivity & Data
Infrastructure;Other Digital;Quantum
Computing;Space Infrastructure
Multi-Country Venture Capital ICT Early Stage Fund Fund 30/06/2030
EVERITA Fund I Coöperatief U.A. EVERITA Capital sro Czech Republic 3SIIF;EIF;IEU - Equity - PP;RCR Growth and expansion Multi-Country Private Equity Generalist Lower-Mid M
… [903 more characters]
```
</details>

→ `Bash` — Show EIF SK PDF text
```sh
cd [redacted: local path] && cat pages/1956281a9eeb9bef.txt
```

<details><summary>result</summary>

```
 Public #
Fund name Fund manager Team location Mandate(s) short name Target area Geographical focus Strategy Main sector Stage focus Investment strategy set up End of investment period Fund Manager website
Sandberg Investment Fund II SCSp Sandberg Capital, sprav. spol., a.s. Slovakia CEFoF;COSME-EFG;EIF Multi-Country Private Equity Generalist Lower-Mid Market Fund 12/01/2027 https://sandberg.capital/#hero
Slovak Venture Fund S.C.A., SICAR Neulogy Ventures a.s. Slovakia CEFoF;EGF Slovakia Venture Capital ICT Balanced Fund 14/03/2027 https://www.neulogy.vc/
EIF equity fund partners
as at 30 September 2026
```
</details>

→ `Bash` — Fetch SIH intermediary investment pages
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov https://www.sih.sk/investicie/investicie-cez-financnych-sprostredkovatelov https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/vision-ventures-kapitalova-investicia https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/cb-investment-management-kapitalova-investicia https://sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia
```

<details><summary>result</summary>

```
Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
[redacted: local path]  200 text/html; charset=UTF-8 https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov  len=0
[redacted: local path]  200 text/html; charset=UTF-8 https://www.sih.sk/investicie/investicie-cez-financnych-sprostredkovatelov  len=0
[redacted: local path]  200 text/html; charset=UTF-8 https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/vision-ventures-kapitalova-investicia  len=1055
[redacted: local path]  200 text/html; charset=UTF-8 https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/cb-investment-management-kapitalova-investicia  len=1123
[redacted: local path]  200 text/html; charset=UTF-8 https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia  len=1017
```
</details>

→ `Bash` — Show SIH fund pages text
```sh
cd [redacted: local path] && for k in 806d18bfc9d3015c 9a2c569d52fa534b 66a13966adb885ef; do cat pages/$k.txt; echo; echo '-----'; done; head -c 600 pages/133267c21d330abe.raw | xxd | head -5
```

<details><summary>result</summary>

```
Vision Ventures | Slovak Investment Holding, a. s.
Vision Ventures
Slovak Investment Holding is an investor in the fund managed by Vision Ventures, which bears sole responsibility for its management and the execution of its investment strategy. The fund was designed as a fixed-term investment vehicle with an anticipated duration of 10 years; it launched operations in 2020 and finalised its investment period in December 2023.
Over the course of the investment period, capital was aimed at supporting early-stage startups, particularly enterprises up to five years post-incorporation, alongside micro and small businesses with strong scaling potential. The deployed investments drove the development of innovative business projects and unlocked new opportunities within the entrepreneurial ecosystem.
The fund is currently its divestment phase, with the manager progressively winding down holdings and returning capital to its investors.
CONTACT
Map
Grösslingová 44
811 09 Bratislava
www.sih.sk
Documents
Media
News
DATA PROTECTION
MANDATORY DISCLOSURES
-----
CB Investment Management | Slovak Investment Holding, a. s.
CB Investment Management
Slovak Investment Holding is an investor in the fund managed by CB Investment Management, which holds full responsibility for the fund's management and the execution of its investment strategy. The fund was established as a fixed-term investment vehicle with an anticipated duration of 10 years, commencing its operations in 2020 and concluding its acti
… [1715 more characters]
```
</details>

→ `Bash` — Find SIH fund page slugs in raw HTML
```sh
cd [redacted: local path] && grep -o 'investicie-cez-financnych-sprostredkovatelov/[a-z0-9-]*' pages/*.raw | sort -u | head -50; wc -c pages/133267c21d330abe.raw
```

<details><summary>result</summary>

```
pages/66a13966adb885ef.raw:investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia
pages/806d18bfc9d3015c.raw:investicie-cez-financnych-sprostredkovatelov/vision-ventures-kapitalova-investicia
pages/9a2c569d52fa534b.raw:investicie-cez-financnych-sprostredkovatelov/cb-investment-management-kapitalova-investicia
       0 pages/133267c21d330abe.raw
```
</details>

→ `Bash` — Probe SIH fund page slugs and sitemap
```sh
cd [redacted: local path] && PY=[redacted: local path] for s in zero-gravity-capital 0100-ventures neulogy-ventures g-force venture-to-future-fund zgc-fund-i zero-gravity-capital-kapitalova-investicia 0100-ventures-kapitalova-investicia neulogy-ventures-kapitalova-investicia; do u="https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/$s"; case $s in *kapitalova*) ;; *) u="$u-kapitalova-investicia";; esac; $PY bin/get.py "$u"; done; $PY bin/get.py https://www.sih.sk/en/investicie https://www.sih.sk/sitemap.xml https://www.sih.sk/en
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/zero-gravity-capital-kapitalova-investicia  len=1033
[redacted: local path]  404 text/html; charset=UTF-8 https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/0100-ventures-kapitalova-investicia  len=192
[redacted: local path]  200 text/html; charset=UTF-8 https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/neulogy-ventures-kapitalova-investicia  len=1100
[redacted: local path]  404 text/html; charset=UTF-8 https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/g-force-kapitalova-investicia  len=192
[redacted: local path]  404 text/html; charset=UTF-8 https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/venture-to-future-fund-kapitalova-investicia  len=192
[redacted: local path]  404 text/html; charset=UTF-8 https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/zgc-fund-i-kapitalova-investicia  len=192
[redacted: local path]  200 text/html; charset=UTF-8 https://www.sih.sk/en/investicie/investicie
… [1868 more characters]
```
</details>

→ `Bash` — Show SIH ZGC/Neulogy pages and sitemap
```sh
cd [redacted: local path] && cat pages/4e078baf8636cd2c.txt | head -4; cat pages/1c6a4904e69cc3ee.txt | head -4; cat pages/643440da8a96024e.raw | head -c 1500; echo; grep -o 'href="[^"]*kapitalov[^"]*"' pages/8e53afed91025b1c.raw | sort -u | head -40
```

<details><summary>result</summary>

```
Zero Gravity Capital | Slovak Investment Holding, a. s.
Zero Gravity Capital
Slovak Investment Holding is an investor in the fund managed by Zero Gravity Capital, which carries full responsibility for its governance and the implementation of its investment strategy. The fund was established as a fixed-term investment vehicle with an expected 10-year term, initiating its activities in 2020 and closing its investment window in December 2023.
Throughout the investment period, capital was directed primarily toward early-stage startups, focusing on companies within five years of their launch, as well as growth-oriented micro and small enterprises. The fund's allocations enhanced the development of innovative solutions and catalysed new entrepreneurial activities in Slovakia.
Neulogy Ventures | Slovak Investment Holding, a. s.
Neulogy Ventures
Slovak Investment Holding is an investor in a Luxembourg-based fund managed by Neulogy Ventures, which has full responsibility for the fund's management and the implementation of its investment strategy. The fund comprises two investment compartments supporting start-ups and growth-oriented small and medium-sized enterprises (SMEs), one of which also includes private investors. The fund's investment period ran from 2014 to 2016.
During the investment period, capital was deployed to early-stage start-ups as well as SMEs with strong growth and expansion potential. The investments supported the development of innovative projects, strengthened th
… [1137 more characters]
```
</details>

→ `Bash` — Query ESMA upreg solr for Neulogy
```sh
cd [redacted: local path] && curl -sL --max-time 30 -A "Mozilla/5.0" 'https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=ae_entityName:*Neulogy*&wt=json&rows=10' | head -c 3000
```

<details><summary>result</summary>

```
{
  "responseHeader":{
    "status":0,
    "QTime":121,
    "params":{
      "q":"ae_entityName:*Neulogy*",
      "rows":"10",
      "wt":"json"}},
  "response":{"numFound":0,"start":0,"numFoundExact":true,"docs":[]
  }}
```
</details>

→ `Bash` — Inspect ESMA upreg fields and facets
```sh
cd [redacted: local path] && curl -sL --max-time 30 -A "Mozilla/5.0" 'https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=*:*&wt=json&rows=2&fq=ae_homeMemberState:SK' | head -c 3000; echo; curl -sL --max-time 30 -A "Mozilla/5.0" 'https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=*:*&wt=json&rows=0&facet=true&facet.field=ae_competentAuthority&facet.field=ae_entityTypeCode&facet.limit=60' | head -c 4000
```

<details><summary>result</summary>

```
{
  "responseHeader":{
    "status":0,
    "QTime":60,
    "params":{
      "q":"*:*",
      "fq":"ae_homeMemberState:SK",
      "rows":"2",
      "wt":"json"}},
  "response":{"numFound":0,"start":0,"numFoundExact":true,"docs":[]
  }}

{
  "responseHeader":{
    "status":0,
    "QTime":9,
    "params":{
      "q":"*:*",
      "facet.limit":"60",
      "facet.field":["ae_competentAuthority",
        "ae_entityTypeCode"],
      "rows":"0",
      "wt":"json",
      "facet":"true"}},
  "response":{"numFound":101697,"start":0,"numFoundExact":true,"docs":[]
  },
  "facet_counts":{
    "facet_queries":{},
    "facet_fields":{
      "ae_competentAuthority":[
        "federal financial supervisory authority (bafin)",2796,
        "commission de surveillance du secteur financier (cssf)",1210,
        "autorité des marchés financiers (amf)",1197,
        "comisión nacional del mercado de valores (cnmv)",1140,
        "netherlands authority for the financial markets (afm)",673,
        "austrian financial market authority (fma)",653,
        "polish financial supervisory authority (knf)",623,
        "banca d'italia",598,
        "central bank of ireland (cbi)",575,
        "finansinspektionen (fi)",467,
        "cyprus securities and exchange commission (cysec)",424,
        "autorité de contrôle prudentiel et de résolution (acpr)",386,
        "finanstilsynet",372,
        "finanssivalvonta (fsa)",338,
        "norwegian financial supervisory authority",287,
        "malta financial se
… [1731 more characters]
```
</details>

→ `Bash` — List SK AIFM and EuVECA entries in ESMA register
```sh
cd [redacted: local path] && curl -sL --max-time 30 -A "Mozilla/5.0" 'https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=ae_competentAuthority:"national bank of slovakia (nbs)"&wt=json&rows=100&fl=ae_entityName,ae_entityTypeCode,ae_nationalCode,ae_lei,id' --data-urlencode x=1 -G | .venv/bin/python -c 1 2>/dev/null; curl -sL --max-time 30 -A "Mozilla/5.0" -G 'https://registers.esma.europa.eu/solr/esma_registers_upreg/select' --data-urlencode 'q=ae_competentAuthority:"national bank of slovakia (nbs)" AND ae_entityTypeCode:(aif OR evc)' --data-urlencode 'wt=json' --data-urlencode 'rows=200' > esma_sk.json; [redacted: local path] -c "
import json;d=json.load(open('esma_sk.json'));print(d['response']['numFound'])
print(sorted(d['response']['docs'][0].keys()))
for x in d['response']['docs']: print(x.get('ae_entityTypeCode'),'|',x.get('ae_entityName'),'|',x.get('ae_nationalCode') or x.get('ae_lei'),'|',x.get('id'))
"
```

<details><summary>result</summary>

```
16
['_root_', '_version_', 'ae_authorisationNotificationDate', 'ae_authorisationNotificationDateStr', 'ae_authorisationWithdrawalEndDateStr', 'ae_branchAddress', 'ae_comment', 'ae_commercialName', 'ae_competentAuthority', 'ae_dbId', 'ae_entityName', 'ae_entityTypeCode', 'ae_entityTypeLabel', 'ae_headOfficeAddress', 'ae_headOfficeLei', 'ae_homeMemberState', 'ae_hostMemberState', 'ae_lastUpdate', 'ae_lastUpdateStr', 'ae_legalform', 'ae_lei', 'ae_officeType', 'ae_status', 'ae_website', 'collectorParent', 'entity_type', 'id', 'no_of_funds', 'timestamp', 'type_s']
EVC | G-Force, s. r. o. |  | ae42928
EVC | Occam Investments s. r. o. | 097900CAKA0000144796 | ae48769
AIF | Sandberg Capital, správ. spol., a.s. | 254900UIM8PBV7CBUI90 | ae10847
AIF | Avanea, správ. spol., a.s. |  | ae44491
AIF | PARTNERS ASSET MANAGEMENT, správ. spol., a. s. | 097900CAFU0000238738 | ae42013
AIF | HB Reavis Investment Management správ. spol., a. s. | 097900BJDN0000190169 | ae24213
AIF | VOSEM Capital, správ. spol., a. s. | 097900CAKA0000231320 | ae49618
AIF | Tatra Asset Management, správ. spol., a.s. | 31570020000000005803 | ae16904
AIF | Asset Management Slovenskej sporiteľne, správ. spol., a.s. |  | ae16901
AIF | IAD Investments, správ. spol., a. s. | 315700PVRM5D3U301460 | ae10848
AIF | J&T INVESTIČNÁ SPOLOČNOSŤ, správ. spol., a.s. | 097900CAKA0000038581 | ae42729
AIF | Slovak Asset Management, správ. spol., a.s. | 097900BIJF0000169556 | ae35839
AIF | Erste Asset Management GmbH, pobočka Slovenská r
… [248 more characters]
```
</details>

→ `Bash` — Show G-Force ESMA doc and list CNB entries
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY -c "
import json;d=json.load(open('esma_sk.json'))
print(json.dumps([x for x in d['response']['docs'] if x['id']=='ae42928'][0],ensure_ascii=False,indent=1))"; curl -sL --max-time 30 -A "Mozilla/5.0" -G 'https://registers.esma.europa.eu/solr/esma_registers_upreg/select' --data-urlencode 'q=ae_competentAuthority:"czech national bank (cnb)"' --data-urlencode 'wt=json' --data-urlencode 'rows=300' > esma_cz.json; $PY -c "
import json;d=json.load(open('esma_cz.json'));print(d['response']['numFound'])
for x in d['response']['docs']: print(x.get('ae_entityTypeCode'),'|',x.get('ae_entityName'),'|',x.get('ae_status'),'|',x.get('id'))
"
```

<details><summary>result</summary>

```
{
 "id": "ae42928",
 "ae_entityTypeCode": "EVC",
 "ae_lastUpdate": "2021-10-28T00:00:00Z",
 "ae_lastUpdateStr": "28/10/2021",
 "ae_lei": "",
 "ae_headOfficeLei": "",
 "ae_entityName": "G-Force, s. r. o.",
 "collectorParent": [
  "G-Force, s. r. o."
 ],
 "ae_officeType": "Head office",
 "ae_competentAuthority": "National Bank of Slovakia (NBS)",
 "ae_homeMemberState": "SLOVAKIA",
 "ae_hostMemberState": "",
 "ae_headOfficeAddress": "Pekárska 14, 91701 Trnava, Slovakia",
 "ae_branchAddress": "",
 "ae_comment": "",
 "ae_status": "Active",
 "ae_authorisationNotificationDate": "2021-08-16T00:00:00Z",
 "ae_authorisationNotificationDateStr": "16/08/2021",
 "ae_authorisationWithdrawalEndDateStr": "",
 "entity_type": "ae",
 "type_s": "parent",
 "ae_entityTypeLabel": "EVC",
 "_root_": "ae42928",
 "ae_dbId": 42928,
 "ae_website": "",
 "ae_commercialName": "",
 "ae_legalform": "",
 "timestamp": "2026-04-09T13:40:22.297Z",
 "no_of_funds": "2",
 "_version_": 1878709635198746624
}
158
MIF | Czech Asset Investments, a.s. | Active | ae2974
MIF | ATLANTIK finanční trhy, a.s. | Active | ae2966
MIF | BH Securities a.s. | Active | ae2969
MIF | AVANT Capital a.s. | Active | ae2965
MIF | Citfin - Finanční trhy, a.s. | Active | ae2972
MIF | AKCENTA CZ a.s. | Active | ae2963
MIF | Československá obchodní banka, a. s. | Active | ae2983
MIF | CYRRUS, a.s. | Active | ae2978
MIF | Česká spořitelna, a.s. | Active | ae2981
MIF | CYRRUS CORPORATE FINANCE, a.s. | Active | ae2979
MIF | Česká exportní banka, a.
… [8647 more characters]
```
</details>

→ `Bash` — Inspect ČNB JERRS intro page
```sh
cd [redacted: local path] && curl -sL --max-time 30 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36" 'https://apl.cnb.cz/apljerrsdad/JERRS.WEB07.INTRO_PAGE?p_lang=cz' -o jerrs_intro.html -w "%{http_code} %{url_effective}\n"; grep -o -i 'href="[^"]*"' jerrs_intro.html | head -40; grep -o -i '<form[^>]*>' jerrs_intro.html; grep -o -i 'name="[^"]*"' jerrs_intro.html | sort -u | head -30
```

<details><summary>result</summary>

```
200 https://jerrs.cnb.cz//apljerrsdad/JERRS.WEB07.INTRO_PAGE?p_lang=cz
href="JERRS.WEB07.WR_CASCADE_STYLE_F?p_lang=cz"
href="http://www.cnb.cz"
href="JERRS.WEB07.INTRO_PAGE?p_lang=en"
href="JERRS.WEB07.INTRO_PAGE?p_lang=cz"
href="JERRS.WEB09.DIRECT_FIND?p_lang=cz"
href="JERRS.WEB15.BASIC_LISTINGS?p_lang=cz"
href="JERRS.WEB24.SUBJECTS_COUNTS?p_lang=cz"
href="JERRS.WEB30.CAS_RADA_DRUHA_STAT?p_lang=cz"
href="JERRS.WEB31.STAT_VZNIK_ZANIK_SVR?p_lang=cz"
href="JERRS.WEB32.CRAD_VZNIK_ZANIK_SVR?p_lang=cz"
href="mailto:[redacted: email address]"
href="https://www.cnb.cz/cs/dohled-financni-trh/seznamy/webove-sluzby-ws-jerrs/"
href="https://www.cnb.cz/cnb/prohlaseni-o-pristupnosti/jerrs/index.html"
name="author"
name="copyright"
name="description"
name="keywords"
name="Last-Modified"
name="resource-type"
name="robots"
```
</details>

→ `Bash` — Inspect JERRS search and listings pages
```sh
cd [redacted: local path] && UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"; curl -sL --max-time 30 -A "$UA" 'https://jerrs.cnb.cz/apljerrsdad/JERRS.WEB09.DIRECT_FIND?p_lang=cz' -o jerrs_find.html; grep -o -i '<form[^>]*>\|<input[^>]*>\|<select[^>]*>' jerrs_find.html | head -20; curl -sL --max-time 30 -A "$UA" 'https://jerrs.cnb.cz/apljerrsdad/JERRS.WEB15.BASIC_LISTINGS?p_lang=cz' -o jerrs_list.html; [redacted: local path] -c "
import sys;sys.path.insert(0,'[redacted: local path]')
from investordb.fetch import html_to_text;print(html_to_text(open('jerrs_list.html','rb').read())[:3000])"; grep -o 'href="[^"]*"' jerrs_list.html | head -60
```

<details><summary>result</summary>

```
<form name="e_mailova_adresa" id="ID_EMAIL_FORM" method="post" enctype="application/x-www-form-urlencoded" action="JERRS.WEB45.CHECK_NEW_SES_WR_RD_COOKIE" onsubmit="return validace_vstupnich_hodnot()">
<input id="LANG_ID" name="p_lang" type="hidden" value="cz">
<input id="LANG_ID" name="p_ID" type="hidden" value="94059750">
<input type="text" class="biggerInput" title = "Opište kód" name="p_OPIS" id="OPIS" size="10" maxlength="10" value="">
<input class="jerrsButton" type="button" alt="Předání parametrů" title="Předání opsaného kódu k dalšímu zpracování" value="Potvrdit" onclick="odeslani_vstupnich_hodnot()">
<input type="submit" value="" style="position: absolute; left: -500px; top: -500px; width:0px; height:0px; border:none; padding: 0px; font-size: 0px;" tabindex="999">
login stranka
Seznamy regulovaných a registrovaných subjektů finančního trhu
Pro pokračování je nutné zadat CAPTCHA kód
.
Pro zadaní kódu CAPTCHA musí být v prohlížeči povoleny cookies.
Opište kód:
Zavřít
href="JERRS.WEB07.WR_CASCADE_STYLE_F?p_lang=cz"
href="http://www.cnb.cz"
href="#"
href="#"
href="#"
href="#"
href="#"
href="#"
href="#"
href="#"
href="#"
href="#"
```
</details>

→ `Bash` — Check ČNB WS-JERRS web service docs
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.cnb.cz/cs/dohled-financni-trh/seznamy/webove-sluzby-ws-jerrs/ >/dev/null; $PY bin/grep.py https://www.cnb.cz/cs/dohled-financni-trh/seznamy/webove-sluzby-ws-jerrs/ "https?://\S+|rest|json|xml" 120 | head -40; grep -o 'href="[^"]*"' pages/$(ls -t pages | head -1 | cut -d. -f1).raw | grep -i -E "jerrs|ws|api|xml|json" | head
```

<details><summary>result</summary>

```
... Obchodní systémy, vypořádání, evidence a ochrana trhu Emise, nabídky převzetí a vytěsnění Směnárny Legalizace výnosů z trestné činnosti Obchodování s OTC deriváty, sekuritizace a crowdfunding Prodeje na krátko Ozdravné postupy a řešení krize Oc ...

...  služby a každá je určena pro získání jiných údajů. Pro všechny 3 webové služby platí stejný postup, kdy tazatel odešle XML soubor s požadovanými údaji a obdrží odpověď s požadovanými informacemi ve formátu XML. Oba soubory XML musí odpovídat  ...

... tejný postup, kdy tazatel odešle XML soubor s požadovanými údaji a obdrží odpověď s požadovanými informacemi ve formátu XML. Oba soubory XML musí odpovídat požadované XSD specifikaci. Všechny webové služby jsou realizovány jako synchronní, při ...

...  tazatel odešle XML soubor s požadovanými údaji a obdrží odpověď s požadovanými informacemi ve formátu XML. Oba soubory XML musí odpovídat požadované XSD specifikaci. Všechny webové služby jsou realizovány jako synchronní, přičemž je určena ma ...

...  autoritou uvedenou na seznamu služeb vytvářejících důvěru, zveřejněném na webových stránkách Evropské komise na adrese https://webgate.ec.europa.eu/tl-browser . Pro získání přístupu k webovým službám je nutné zaslat na adresu [redacted: email address] elektronicky podepsanou žádost o přís ...

...  trvání a zániku oprávnění, informace o povolených činnostech a informace o vybraných vazbách na jiné subjekty. Příklad XML pro zaslání dotazu: getSubjekt.xml (xml, 1 kB) Příklad XML s odpovědí
… [3334 more characters]
```
</details>

→ `Bash` — Probe NBS entity register search
```sh
cd [redacted: local path] && UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"; curl -sL --max-time 30 -A "$UA" 'https://subjekty.nbs.sk/?qq=Neulogy' -o nbs1.html -w "%{http_code} %{url_effective}\n"; [redacted: local path] -c "
import sys;sys.path.insert(0,'[redacted: local path]')
from investordb.fetch import html_to_text;print(html_to_text(open('nbs1.html','rb').read())[:2500])"; grep -o 'href="[^"]*"' nbs1.html | head -40
```

<details><summary>result</summary>

```
200 https://subjekty.nbs.sk/sk/?qq=Neulogy
Subjekty fin. trhu
Upozornenie: Používate zastaralú verziu prehliadača, stránku nie je možné správne načítať.
Subjekty finančného trhu
Vyhľadať
BANKOVNÍCTVO, PLATOBNÉ SLUŽBY A ELEKTRONICKÉ PENIAZE
POISŤOVNÍCTVO
TRH CENNÝCH PAPIEROV
KOLEKTÍVNE INVESTOVANIE
DÔCHODKOVÉ SPORENIE
FINANČNÉ SPROSTREDKOVANIE A PORADENSTVO
TRH KRYPTOAKTÍV
SPRÁVCOVIA ÚVEROV, NEBANKOVÍ VERITELIA
DEVÍZOVÉ MIESTA
href="/static/fa/css/all.min.css"
href="/static/datatables.min.css"
href="/static/Bootstrap-4-4.6.0/css/bootstrap.css"
href="/static/icon/favicon.ico"
href="/static/jquery-ui/jquery-ui.min.css"
href="/static/nbs.css"
href="/static/subjekty.css"
href="https://www.nbs.sk"
href="/info"
href="https://www.nbs.sk/sk/o-narodnej-banke/kontakty"
href="javascript:void(0)"
href="/"
href="https://www.nbs.sk/sk/disclaimer-sk"
href="https://www.nbs.sk/sk/vyhlasenie-o-pristupnosti"
href="https://www.nbs.sk/sk/ochrana-osobnych-udajov"
```
</details>

→ `Bash` — Find NBS register AJAX endpoints
```sh
cd [redacted: local path] && grep -o -E '(url|ajax|fetch|\$\.get|\$\.post)[^;]{0,200}' nbs1.html | head -20; grep -o '<script[^>]*src="[^"]*"' nbs1.html
```

<details><summary>result</summary>

```
url_new_tab(url) {
url, '_blank')
<script src="/static/popper.js-1.0.4/popper.js"
<script type="text/javascript" src="/static/datatables.min.js"
<script src="/static/jquery-ui/jquery-ui.min.js"
<script src="/static/jquery-ui/i18n/datepicker-sk.js"
<script type="text/javascript" src="/static/jquery.cookies.js"
<script type="text/javascript" src="/static/nbs.js"
```
</details>

→ `Bash` — Inspect NBS register JS for endpoints
```sh
cd [redacted: local path] && curl -sL --max-time 30 -A "Mozilla/5.0" https://subjekty.nbs.sk/static/nbs.js | grep -o -E "(url|href|location)[^;]{0,160}" | head -30; grep -o -E 'onclick="[^"]{0,150}"|data-[a-z]+="[^"]{0,80}"' nbs1.html | sort -u | head -30
```

<details><summary>result</summary>

```
data-sektor="1005"
data-sektor="1059"
data-sektor="1105"
data-sektor="1120"
data-sektor="1170"
data-sektor="1179"
data-sektor="1414"
data-sektor="930"
data-sektor="985"
onclick="set_language()"
```
</details>

→ `Bash` — Read inline scripts in NBS register page
```sh
cd [redacted: local path] && grep -o -E '<script[^>]*>[^<]{0,3000}' nbs1.html | grep -v '^<script[^>]*src' | head -c 4000; grep -B2 -A2 'data-sektor="1105"' nbs1.html | head
```

<details><summary>result</summary>

```
<script>
<script>
<script>

            <div class="col-sm-4 px-1">
            <div class="p-2 panel panel-default text-center clearfix sektor-panel sektor-panel5" data-sektor="1105">
              <div class="p-4 panel-heading sektor-panel sektor-panel5" data-sektor="1105">
              <h4>DÔCHODKOVÉ SPORENIE</h4>
              </div>
```
</details>

→ `Bash` — Print NBS inline scripts
```sh
cd [redacted: local path] && [redacted: local path] - <<'EOF'
import re
h=open('nbs1.html',encoding='utf-8',errors='replace').read()
for m in re.finditer(r'<script>(.*?)</script>',h,re.S):
    s=m.group(1)
    print(s[:2500]); print('=====')
EOF
```

<details><summary>result</summary>

```
    function center_screen () {
        var wh = window.innerHeight
        var dh = $( 'div.container' ).height()
        if (dh < wh) {
            $( 'div.container' ).css('margin-top', (wh-dh)/3 + 'px');
        } else {
            $( 'div.container' ).css('margin-top','0px');
        }
    }

    $( window ).resize(center_screen);
    center_screen();

    $(document).ready( function () {
        $("div.sektor-panel").click( function () {
            window.location.href = '/?s=' + $(this).data('sektor');
        } );

    });



=====

    function supports_canvas() {
        return !!document.createElement('canvas').getContext;
    }
    function open_url_new_tab(url) {
      var win = window.open(url, '_blank');
      win.focus();
    }
    if (!supports_canvas()) {
        document.getElementById("ObsBrows").style.display = "inline";
    }
    $('#searchButton').on('click', function (e) {
        $("#searchForm").submit();
    });

=====

    function set_language() {
        const langPattern = /^\/([a-z]{2})\//;
        $('input[name="next"]').val($('input[name="next"]').val().replace(langPattern, '/'+$('input[name="language"]').val()+'/'));
        $('#set_lang_frm').submit();
    };


    $(document).ready( function () {

    });

=====
```
</details>

→ `Bash` — Open NBS collective investment sector
```sh
cd [redacted: local path] && grep -o '<form[^>]*>' nbs1.html; grep -o '<input[^>]*>' nbs1.html | head; UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"; curl -sL --max-time 30 -A "$UA" 'https://subjekty.nbs.sk/sk/?s=1059' -o nbs2.html; [redacted: local path] -c "
import sys;sys.path.insert(0,'[redacted: local path]')
from investordb.fetch import html_to_text;print(html_to_text(open('nbs2.html','rb').read())[:3000])"; grep -o 'href="[^"]*"' nbs2.html | grep -v static | head -40
```

<details><summary>result</summary>

```
<form id="set_lang_frm" action="/sk/set_language/"  method="post">
<form id="set_other_options">
<form id="searchForm" class="d-flex w-100" method="GET" action='/search'>
<input type="hidden" name="csrfmiddlewaretoken" value="jobT3BifUYFcGdNFk2YPmae5c66RMlpKPTdXFBHKeNKBp2Kyw7x9JPiXjHPVFxia">
<input name="next" type="hidden" value="/sk/?qq=Neulogy">
<input name="language" type="hidden" value="en"/>
<input type="text" class="form-control" placeholder="IČO, obchodné meno alebo iné označenie subjektu. Minimálne 3 znaky." aria-label="Search" aria-describedby="basic-addon2" name="q" value="">
Subjekty fin. trhu
Upozornenie: Používate zastaralú verziu prehliadača, stránku nie je možné správne načítať.
Subjekty finančného trhu
Vyhľadať
Banky, e-peniaze
Poisťovne
Trh cenných papierov
Kolektívne investovanie
Dôchodkové sporenie
Sprostredkovatelia
Trh kryptoaktív
Správcovia úverov, veritelia
Devízové miesta
Podľa oprávnenia na činnosť
Počet
Správcovské spoločnosti a zahraničné správcovské spoločnosti
368
Registrované subjekty
39
Subjekty so zaniknutým oprávnením na činnosť
18
Podľa investičnej stratégie
Počet
Slovenské fondy
92
Zahraničné fondy
1040
Subjekty so zaniknutým oprávnením na činnosť
708
Podľa územnej pôsobnosti
Počet
Správcovské spoločnosti a samosprávne investičné fondy
368
href="https://www.nbs.sk"
href="/info"
href="https://www.nbs.sk/sk/o-narodnej-banke/kontakty"
href="javascript:void(0)"
href="/"
href="#cctg1061"
href="#cctg1069"
href="#cctg1074"
href="#cctg1088"
href="#
… [160 more characters]
```
</details>

→ `Bash` — Search NBS register for Slovak managers
```sh
cd [redacted: local path] && UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"; for q in Neulogy "Vision Ventures" "0100" "Zero Gravity" "G-Force" "CB Investment" "Limerock" "Venture to Future" "Baryon" "Monogram"; do curl -sL --max-time 30 -A "$UA" -G 'https://subjekty.nbs.sk/search' --data-urlencode "q=$q" -o nbs_s.html -w "$q: %{http_code} %{url_effective}\n"; [redacted: local path] -c "
import sys,re;sys.path.insert(0,'[redacted: local path]')
from investordb.fetch import html_to_text;t=html_to_text(open('nbs_s.html','rb').read());i=t.find('Vyhľadať');print(t[i:i+700].replace(chr(10),' | '))"; grep -o 'href="/entity/[^"]*"\|href="[^"]*detail[^"]*"' nbs_s.html | head -5; done
```

<details><summary>result</summary>

```
Neulogy: 200 https://subjekty.nbs.sk/sk/search?q=Neulogy
Vyhľadať | Nájdené subjekty | ID | Meno | Adresa | Štát
Vision Ventures: 200 https://subjekty.nbs.sk/sk/search?q=Vision+Ventures
Vyhľadať | Nájdené subjekty | ID | Meno | Adresa | Štát
0100: 200 https://subjekty.nbs.sk/sk/search?q=0100
Vyhľadať | Nájdené subjekty | ID | Meno | Adresa | Štát
Zero Gravity: 200 https://subjekty.nbs.sk/sk/search?q=Zero+Gravity
Vyhľadať | Nájdené subjekty | ID | Meno | Adresa | Štát
G-Force: 200 https://subjekty.nbs.sk/sk/search?q=G-Force
Vyhľadať | Nájdené subjekty | ID | Meno | Adresa | Štát
CB Investment: 200 https://subjekty.nbs.sk/sk/search?q=CB+Investment
Vyhľadať | Nájdené subjekty | ID | Meno | Adresa | Štát
Limerock: 200 https://subjekty.nbs.sk/sk/search?q=Limerock
Vyhľadať | Nájdené subjekty | ID | Meno | Adresa | Štát
Venture to Future: 200 https://subjekty.nbs.sk/sk/search?q=Venture+to+Future
Vyhľadať | Nájdené subjekty | ID | Meno | Adresa | Štát
Baryon: 200 https://subjekty.nbs.sk/sk/search?q=Baryon
Vyhľadať | Nájdené subjekty | ID | Meno | Adresa | Štát
Monogram: 200 https://subjekty.nbs.sk/sk/search?q=Monogram
Vyhľadať | Nájdené subjekty | ID | Meno | Adresa | Štát
```
</details>

→ `Bash` — Look for data-table AJAX in NBS search page
```sh
cd [redacted: local path] && [redacted: local path] - <<'EOF'
import re
h=open('nbs_s.html',encoding='utf-8',errors='replace').read()
for m in re.finditer(r'<script>(.*?)</script>',h,re.S):
    s=m.group(1)
    if 'ajax' in s or 'DataTable' in s or 'url' in s: print(s[:3000]); print('=====')
i=h.find('Nájdené'); print(h[i:i+2500])
EOF
```

<details><summary>result</summary>

```
$(document).ready(function() {

    var occupancy = {
        "po": undefined,
        "fo": undefined
    }

    function selectPane() {
        if (occupancy.po !== undefined && occupancy.fo !== undefined) {
            if(occupancy.po === 0 && occupancy.fo > 0) {
                $("#contact-tab").trigger("click");
            }
            // else if (occupancy.fo === 0 && occupancy.po > 0){
            // 	$("#profile-tab").trigger("click");
            // }
        }
    }

    var sTable = $('#Subjekty2895758300').dataTable({
        "aDataSort": true,
        "order": [[ 0, "asc" ]],
        "processing": true,
        "serverSide": true,
        "stateSave": true,
        "searching": false,
        "initComplete": function(settings, json){
            occupancy.po = json.data.length;
            selectPane();
        },

        "language": {
            "url": "/static/i18n/sk.json"
        },

        "ajax": {
            "url" : "/sk/subjekty",
            "data" : {
                "mq" : "Monogram",
                "et" : "l",
            },
            "dataSrc": function ( json ) {

                if (json.data.length==1) {
                    link_re = /data-link="(\d+)"/.exec(json.data[0][0])
                    window.location = '/entity/' + link_re[1] + '/';
                }

                return json.data;
            }
        }
    });

    $('#Subjekty2895758300 tbody').on('click', 'tr', function () {
        if ($(this).find('.dataTables_empty').length) {
            return;
        }
        if ($('td', this).eq(0).find('div').length) {
            window.location = '/entity/' + $('td', this).eq(0).find('d
… [2950 more characters]
```
</details>

→ `Bash` — Query NBS register AJAX for Slovak managers
```sh
cd [redacted: local path] && UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"; for q in Neulogy "Vision Ventures" "0100 Ventures" "Zero Gravity" "G-Force" "CB Investment" "Limerock" "Venture to Future" "Baryon" "Monogram" "Slovak Asset" "365.fintech" "IPM" "Fond inov"; do echo "== $q"; curl -sL --max-time 30 -A "$UA" -H "X-Requested-With: XMLHttpRequest" -G 'https://subjekty.nbs.sk/sk/subjekty' --data-urlencode "mq=$q" --data-urlencode "et=l" --data-urlencode "draw=1" --data-urlencode "start=0" --data-urlencode "length=20" | head -c 900; echo; done
```

<details><summary>result</summary>

```
== Neulogy
{"draw": 1, "recordsTotal": 0, "recordsFiltered": 0, "data": [], "result": "ok"}
== Vision Ventures
{"draw": 1, "recordsTotal": 3, "recordsFiltered": 3, "data": [["<div data-link=\"5484\">52568288</div>", "Vision Ventures, s.r.o.", "Bottova 2/A, 81109 Bratislava", "Slovensko"], ["<div data-link=\"21986\">52656438</div>", "Vision Ventures Growth I, s. r. o.", "Bottova 2A, 81109 Bratislava - mestsk\u00e1 \u010das\u0165 Star\u00e9 Mesto", "Slovensko"], ["<div data-link=\"310775\"></div>", "N-Vision Ventures SCSp", "", "Luxembursko"]], "result": "ok"}
== 0100 Ventures
{"draw": 1, "recordsTotal": 0, "recordsFiltered": 0, "data": [], "result": "ok"}
== Zero Gravity
{"draw": 1, "recordsTotal": 1, "recordsFiltered": 1, "data": [["<div data-link=\"5486\">52651894</div>", "Zero Gravity Capital s.r.o.", "Staromestsk\u00e1 7830/3, Bratislava - mestsk\u00e1 \u010das\u0165 Star\u00e9 Mesto 811 03", "Slovensko"]], "result": "ok"}
== G-Force
{"draw": 1, "recordsTotal": 2, "recordsFiltered": 2, "data": [["<div data-link=\"5492\">53527798</div>", "G-Force, s.r.o.", "Pek\u00e1rska 14, 91701 Trnava", "Slovensko"], ["<div data-link=\"21994\">53588398</div>", "G-Force Fund, j.s.a.", "Pek\u00e1renska 14, 917 01 Trnava", "Slovensko"]], "result": "ok"}
== CB Investment
{"draw": 1, "recordsTotal": 7, "recordsFiltered": 7, "data": [["<div data-link=\"1734\"></div>", "CB Richard Ellis Indirect Investment Services Limited", "Kingsley House, Wimpole Street, London, W1G 0RE", "Spojen\u00e9 kr\u0
… [3813 more characters]
```
</details>

→ `Bash` — Fetch NBS entity pages for Slovak managers
```sh
cd [redacted: local path] && PY=[redacted: local path] UA="Mozilla/5.0"; for q in 47367610 "NEULOGY" 50209728 44071574 51301547 "Slovenská sporiteľňa" "Seed Starter"; do echo "== $q"; curl -sL --max-time 30 -A "$UA" -G 'https://subjekty.nbs.sk/sk/subjekty' --data-urlencode "mq=$q" --data-urlencode "et=l" --data-urlencode "draw=1" --data-urlencode "start=0" --data-urlencode "length=20" | head -c 500; echo; done; for id in 5484 5486 5492 5483 308293 5190 276769; do $PY bin/get.py https://subjekty.nbs.sk/entity/$id/; done
```

<details><summary>result</summary>

```
== 47367610
{"draw": 1, "recordsTotal": 0, "recordsFiltered": 0, "data": [], "result": "ok"}
== NEULOGY
{"draw": 1, "recordsTotal": 0, "recordsFiltered": 0, "data": [], "result": "ok"}
== 50209728
{"draw": 1, "recordsTotal": 0, "recordsFiltered": 0, "data": [], "result": "ok"}
== 44071574
{"draw": 1, "recordsTotal": 0, "recordsFiltered": 0, "data": [], "result": "ok"}
== 51301547
{"draw": 1, "recordsTotal": 0, "recordsFiltered": 0, "data": [], "result": "ok"}
== Slovenská sporiteľňa
{"draw": 1, "recordsTotal": 1, "recordsFiltered": 1, "data": [["<div data-link=\"9\">00151653</div>", "Slovensk\u00e1 sporite\u013e\u0148a, a.s.", "Tom\u00e1\u0161ikova 48, 83237 Bratislava", "Slovensko"]], "result": "ok"}
== Seed Starter
{"draw": 1, "recordsTotal": 0, "recordsFiltered": 0, "data": [], "result": "ok"}
[redacted: local path]  200 text/html; charset=utf-8 https://subjekty.nbs.sk/sk/entity/5484/  len=620
[redacted: local path]  200 text/html; charset=utf-8 https://subjekty.nbs.sk/sk/entity/5486/  len=645
[redacted: local path]  200 text/html; charset=utf-8 https://subjekty.nbs.sk/sk/entity/5492/  len=715
[redacted: local path]  200 text/html; charset=utf-8 https://subjekty.nbs.sk/sk/entity/5483/  len=621
[redacted: local path]  200 text/html; chars
… [361 more characters]
```
</details>

→ `Bash` — Show NBS entity page texts
```sh
cd [redacted: local path] && for k in 46a16af73d600c6f 241414900591d17d 1922f20bf144dd22 10e1d2671750211f e2fe271fdaaa0117 c52153f034a1fc5a 20b7c2454e691c7b; do tr '\n' '|' < pages/$k.txt; echo; echo; done
```

<details><summary>result</summary>

```
Subjekty fin. trhu|Upozornenie: Používate zastaralú verziu prehliadača, stránku nie je možné správne načítať.|Subjekty finančného trhu|Vyhľadať|Vision Ventures, s.r.o.|99.99.99|–|99.99.99|IČO:|52568288|99.99.99|–|99.99.99|Sídlo:|Bottova 2/A, 81109 Bratislava|09.11.21|–|99.99.99|Štát:|Slovensko|99.99.99|–|99.99.99|Rozbaliť|/|Zbaliť|Pôsobenie na finančnom trhu|99.99.99|–|99.99.99|registrovaný správca alternatívnych investičných fondov|11.11.19|–|99.99.99|Registračné číslo:|0020|11.11.19|–|99.99.99|Orgán dohľadu:|Národná banka Slovenska|11.11.19|–|99.99.99|fondy|Vision Ventures Growth I, s. r. o.|11.11.19|–|99.99.99

Subjekty fin. trhu|Upozornenie: Používate zastaralú verziu prehliadača, stránku nie je možné správne načítať.|Subjekty finančného trhu|Vyhľadať|Zero Gravity Capital s.r.o.|99.99.99|–|99.99.99|IČO:|52651894|99.99.99|–|99.99.99|Sídlo:|Staromestská 7830/3, Bratislava - mestská časť Staré Mesto 811 03|99.99.99|–|99.99.99|Štát:|Slovensko|99.99.99|–|99.99.99|Rozbaliť|/|Zbaliť|Pôsobenie na finančnom trhu|99.99.99|–|99.99.99|registrovaný správca alternatívnych investičných fondov|13.02.20|–|99.99.99|Registračné číslo:|0022|13.02.20|–|99.99.99|Orgán dohľadu:|Národná banka Slovenska|13.02.20|–|99.99.99|fondy|ZGC Fund I., s.r.o.|13.02.20|–|99.99.99

Subjekty fin. trhu|Upozornenie: Používate zastaralú verziu prehliadača, stránku nie je možné správne načítať.|Subjekty finančného trhu|Vyhľadať|G-Force, s.r.o.|99.99.99|–|99.99.99|IČO:|53527798|99.99.99|–|99.99.99|LEI:|097900CAKA00
… [3469 more characters]
```
</details>

→ `ToolSearch`

<details><summary>result</summary>

```

```
</details>

→ `WebSearch` nrinvesticni.cz fondy rizikového kapitálu portfolio Lighthouse Ventures Nation 1 Credo

<details><summary>result</summary>

```
Web search results for query: "nrinvesticni.cz fondy rizikového kapitálu portfolio Lighthouse Ventures Nation 1 Credo"

Links: [{"title":"Venture capital in the Czech Republic","url":"https://en.wikipedia.org/wiki/Venture_capital_in_the_Czech_Republic"},{"title":"OP PIK bude ve spolupráci s EIF podporovat začínající inovativní společnosti","url":"https://www.businessinfo.cz/clanky/op-pik-bude-ve-spolupraci-s-eif-podporovat-zacinajici-inovativni-spolecnosti/"},{"title":"stat pomuze startupum penize budou rozdelovat dva nove fondy","url":"https://forbes.cz/stat-pomuze-startupum-penize-budou-rozdelovat-dva-nove-fondy/"},{"title":"investori pri chuti ceske fondy maji nabito a letos planuji i exity","url":"https://forbes.cz/investori-pri-chuti-ceske-fondy-maji-nabito-a-letos-planuji-i-exity/"},{"title":"lighthouse ventures","url":"https://privateequitylist.com/investor/lighthouse-ventures"},{"title":"nejde o zdroj penez ale jak fondy podporuji startupy v rozvoji i pres krizi investujeme dal rika zalesak z lighthouse ventures","url":"https://cc.cz/nejde-o-zdroj-penez-ale-jak-fondy-podporuji-startupy-v-rozvoji-i-pres-krizi-investujeme-dal-rika-zalesak-z-lighthouse-ventures/"},{"title":"118548 lighthouse ventures","url":"https://my.motherbase.ai/startup/118548-lighthouse-ventures"},{"title":"nejde o zdroj penez ale jak fondy podporuji startupy v rozvoji i pres krizi investujeme dal rika zalesak z lighthouse ventures","url":"https://cc.cz/2020/04/nejde-o-zdroj-penez-ale-jak-fondy-podp
… [1700 more characters]
```
</details>

→ `WebSearch` eif.org Czech Republic "Lighthouse" seed fund ESIF fund of funds OP PIK Nation 1

<details><summary>result</summary>

```
Web search results for query: "eif.org Czech Republic "Lighthouse" seed fund ESIF fund of funds OP PIK Nation 1"

Links: [{"title":"lighthouse ventures","url":"https://privateequitylist.com/investor/lighthouse-ventures"},{"title":"Lighthouse Ventures","url":"https://privateequitylist.com/investors/lighthouse-ventures"},{"title":"118548 lighthouse ventures","url":"https://my.motherbase.ai/startup/118548-lighthouse-ventures"},{"title":"118548 lighthouse ventures","url":"https://my.motherbase.ai/company/118548-lighthouse-ventures"},{"title":"118548 lighthouse ventures","url":"https://my.motherbase.ai/startup/118548-lighthouse-ventures/?page=2"},{"title":"OP PIK bude ve spolupráci s EIF podporovat začínající inovativní společnosti","url":"https://www.businessinfo.cz/clanky/op-pik-bude-ve-spolupraci-s-eif-podporovat-zacinajici-inovativni-spolecnosti/"},{"title":"czfof call for eoi","url":"https://www.eif.org/what_we_do/resources/esif-fund-of-funds-czech-republic/call/czfof_call_for_eoi.pdf"},{"title":"Lighthouse Ventures","url":"https://venturecapitalarchive.com/venture-funds/lighthouse-ventures-lhv-vc"},{"title":"What we do","url":"https://www.eif.org/what_we_do/resources/esif-fund-of-funds-czech-republic/index.htm"},{"title":"lighthouse seed fund prague","url":"https://www.euacc.ai/investors/lighthouse-seed-fund-prague"}]

The search turned up a consistent picture of the Czech ESIF Fund of Funds (CZFoF) and its link to Lighthouse, though most of the material comes from secondary
… [1940 more characters]
```
</details>

→ `Bash` — Fetch EIF CZ FoF, businessinfo and Lighthouse pages
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.eif.org/what_we_do/resources/esif-fund-of-funds-czech-republic/index.htm https://www.businessinfo.cz/clanky/op-pik-bude-ve-spolupraci-s-eif-podporovat-zacinajici-inovativni-spolecnosti/ https://lhv.vc/ https://www.nrinvesticni.cz/; $PY bin/grep.py https://www.eif.org/what_we_do/resources/esif-fund-of-funds-czech-republic/index.htm "Lighthouse|Nation|selected|intermediar" 200; $PY bin/grep.py https://www.businessinfo.cz/clanky/op-pik-bude-ve-spolupraci-s-eif-podporovat-zacinajici-inovativni-spolecnosti/ "Lighthouse|Nation 1" 250; $PY bin/grep.py https://lhv.vc/ "fund of funds|ESIF|European Investment|Ministry" 200
```

<details><summary>result</summary>

```
[redacted: local path]  404 text/html;charset=utf-8 https://www.eif.org/what_we_do/resources/esif-fund-of-funds-czech-republic/index.htm  len=145
[redacted: local path]  403 text/html; charset=UTF-8 https://www.businessinfo.cz/clanky/op-pik-bude-ve-spolupraci-s-eif-podporovat-zacinajici-inovativni-spolecnosti/  len=16
[redacted: local path]  200 text/html; charset=UTF-8 https://lhv.vc/  len=4503
[redacted: local path]  200 text/html; charset=UTF-8 https://www.nrinvesticni.cz/  len=12478
[0 matches, meta=['404 text/html;charset=utf-8 https://www.eif.org/what_we_do/resources/esif-fund-of-funds-czech-republic/index.htm']]
[0 matches, meta=['403 text/html; charset=UTF-8 https://www.businessinfo.cz/clanky/op-pik-bude-ve-spolupraci-s-eif-podporovat-zacinajici-inovativni-spolecnosti/']]
... rience.” Michal Zálešák Managing Partner Contact us contact lhv.vc Office Evropská 2758/11 160 00, Prague 6 See map Follow us Lighthouse Seed Fund benefits from the support and financing of the Czech ESIF Fund of Funds (CZFoF). The Czech ESIF Fund of Funds is an initiative created by cooperation between the Ministry of Industry and Trade of the Czech Republic and EIF and financed under the European Re ...

... e.” Michal Zálešák Managing Partner Contact us contact lhv.vc Office Evropská 2758/11 160 00, Pragu
… [1641 more characters]
```
</details>

→ `Bash` — Look for fund lists on the NRI site
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/grep.py https://www.nrinvesticni.cz/ "fond|DEPO|ventures" 120 | head -30; grep -o 'href="[^"]*"' pages/e51a2dbaea8450c5.raw | sort -u | grep -v -E "\.css|\.js|\.png|\.svg" | head -60
```

<details><summary>result</summary>

```
... NR investiční, a.s., osoba rizikového kapitálu | Národní rozvojová investiční, a.s., osoba rizikového kapitálu Vyhledat Fond dostupného bydlení ČR Podpora přístupu malých a středních podniků k rizikovému financování IPO Fond 2025+ Poskytování n ...

... o kapitálu Vyhledat Fond dostupného bydlení ČR Podpora přístupu malých a středních podniků k rizikovému financování IPO Fond 2025+ Poskytování návratné podpory formou zvýhodněného juniorního financování projektů modernizace zastaralých, prostor ...

...  financování projektů modernizace zastaralých, prostorově a technicky nevyhovujících objektů, budov a areálů Brownfield fond MPO Investice rizikového kapitálu do startupů s ukrajinskými, gruzínskými či moldavskými zakladateli rozvíjejícími své  ...

... rizikového kapitálu do startupů s ukrajinskými, gruzínskými či moldavskými zakladateli rozvíjejícími své podnikání v ČR Fond Ukrajina Možnost z fondu získat prostředky na investování do firem z Česka i z širšího regionu Trojmoří Inovační fond T ...

... tartupů s ukrajinskými, gruzínskými či moldavskými zakladateli rozvíjejícími své podnikání v ČR Fond Ukrajina Možnost z fondu získat prostředky na investování do firem z Česka i z širšího regionu Trojmoří Inovační fond Trojmoří Mezinárodní fond ...

... R Fond Ukrajina Možnost z fondu získat prostředky na investování do firem z Česka i z širšího regionu Trojmoří Inovační fond Trojmoří Mezinárodní fond rizikového kapitálu, do kterého je svým vkladem zapojeno 24 evropských člen
… [6929 more characters]
```
</details>

→ `Bash` — Fetch NRI Fond Ukrajina and NRF pages
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.nrinvesticni.cz/nri-dokoncila-vyber-venture-kapitaloveho-fondu-pro-program-fond-ukrajina/ https://www.nrinvesticni.cz/fond-ukrajina/ https://www.narodnirozvojovyfond.cz/ ; $PY bin/grep.py https://www.nrinvesticni.cz/nri-dokoncila-vyber-venture-kapitaloveho-fondu-pro-program-fond-ukrajina/ "DEPO" 250 | head -12; $PY bin/grep.py https://www.nrinvesticni.cz/fond-ukrajina/ "DEPO" 200 | head -6; $PY bin/grep.py https://www.narodnirozvojovyfond.cz/ "portfol|fond[ůy]|Reflex|Credo|Rockaway|Tensor|Purple" 120 | head -20
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://www.nrinvesticni.cz/nri-dokoncila-vyber-venture-kapitaloveho-fondu-pro-program-fond-ukrajina/  len=4598
[redacted: local path]  200 text/html; charset=UTF-8 https://www.nrinvesticni.cz/fond-ukrajina/  len=2341
[redacted: local path]  526 text/plain; charset=UTF-8 https://www.narodnirozvojovyfond.cz/  len=16
...  pro program Fond Ukrajina investice rizikový kapitál Ukrajina 26.08.2026 Národní rozvojová investiční (NRI) úspěšně dokončila výběr správce fondu rizikového kapitálu v rámci programu Fond Ukrajina. Vybraným finančním zprostředkovatelem se stal fond DEPO Ventures One SCSp, spravovaný lucemburským fondem rizikového kapitálu DEPO Ventures Sàrl, podporujícím rozvoj startupů. NRI je dceřinou společností Národní rozvojové banky, která se zaměřuje na kapitálové a kvazikapitálové nástroje podporující strat ...

... árodní rozvojová investiční (NRI) úspěšně dokončila výběr správce fondu rizikového kapitálu v rámci programu Fond Ukrajina. Vybraným finančním zprostředkovatelem se stal fond DEPO Ventures One SCSp, spravovaný lucemburským fondem rizikového kapitálu DEPO Ventures Sàrl, podporujícím rozvoj startupů. NRI je dceřinou společností Národní rozvojové banky, která se zaměřuje na kapitálové a kvazikapitálové nástroje podporující strategický rozvoj české ekonomiky. Do vybra
… [2553 more characters]
```
</details>

→ `Bash` — Search ESMA register for all target names
```sh
cd [redacted: local path] && for q in Credo Presto Reflex Tilia Kaya KAYA Lighthouse ZAKA Purple Rockaway Tensor Nation DEPO Miton Inven Biotech Soulmates StartupYard "Y Soft" Startguide GAIN BHM "Czech Founders" Orbit Impulse KOOPEO "Air Ventures" Springtide UP21 RockawayX Baryon Neulogy Vision "0100" "Zero Gravity" "Monogram" "IPM" "LRJ" "GROWWS" "J&T Ventures" "365"; do r=$(curl -sL --max-time 30 -A "Mozilla/5.0" -G 'https://registers.esma.europa.eu/solr/esma_registers_upreg/select' --data-urlencode "q=ae_entityName:*${q// /\\ }*" --data-urlencode 'wt=json' --data-urlencode 'rows=20' --data-urlencode 'fl=id,ae_entityName,ae_entityTypeCode,ae_competentAuthority,ae_status' | [redacted: local path] -c "
import json,sys;d=json.load(sys.stdin)['response'];print(d['numFound'], [(x['ae_entityName'],x['ae_entityTypeCode'],x['ae_competentAuthority'][:12],x['ae_status'],x['id']) for x in d['docs'][:8]])"); echo "$q: $r"; done 2>&1 | grep -v ": 0 \[\]"
```

<details><summary>result</summary>

```
Credo: 4 [('CREDO Vermögensmanagement GmbH', 'MIF', 'Federal Fina', 'Active', 'ae6689'), ('CREDOS d.o.o.', 'MIF', 'Croatian Fin', 'Active', 'ae13327'), ('CREDOFUNDING', 'CSP', 'Autorité des', 'Active', 'ae48093'), ('CREDO PARTNERS AS', 'AIF', 'Norwegian Fi', 'Active', 'ae18139')]
Presto: 1 [('F3 Presto HVD CV Fund AB', 'AIF', 'Finansinspek', '', 'ae50078')]
Kaya: 2 [('Kaya Capital Management B.V.', 'MIF', 'Netherlands ', 'Active', 'ae4933'), ('Kaya Capital Funds B.V.', 'AIF', 'Netherlands ', 'Active', 'ae36889')]
KAYA: 2 [('Kaya Capital Management B.V.', 'MIF', 'Netherlands ', 'Active', 'ae4933'), ('Kaya Capital Funds B.V.', 'AIF', 'Netherlands ', 'Active', 'ae36889')]
Lighthouse: 1 [('Lighthouse Capital Management Ltd', 'AIF', 'Cyprus Secur', 'Active', 'ae23487')]
Nation: 181 [('AIPM Azur International Portfolio Management AG', 'MIF', 'Finanzmarkta', 'Inactive', 'ae22'), ('JPMorgan Chase bank, National Association', 'MIF', 'Autorité de ', 'Inactive', 'ae986'), ('LYXOR INTERNATIONAL ASSET MANAGEMENT', 'UCI', 'Autorité des', 'Inactive', 'ae1512'), ('Western union international bank GmbH', 'MIF', 'Austrian Fin', 'Inactive', 'ae1312'), ('NATIXIS INVESTMENT MANAGERS INTERNATIONAL', 'UCI', 'Autorité des', 'Active', 'ae1612'), ('International Investment Platform, o.c.p., a.s.', 'MIF', 'National Ban', 'Active', 'ae1848'), ('DEKA INTERNATIONAL S.A.', 'UCI', 'Commission d', 'Active', 'ae2828'), ('CAPITAL INTERNATIONAL MANAGEMENT COMPANY', 'UCI', 'Commission d', 'Active', 'ae2730')]
DE
… [2936 more characters]
```
</details>

→ `Bash` — Search SEC IAPD for target firms
```sh
cd [redacted: local path] && for q in "Credo Ventures" "Presto Ventures" "Reflex Capital" "Kaya" "Rockaway" "RockawayX" "Tensor Ventures" "ZAKA" "Purple Ventures" "Soulmates" "Lighthouse Ventures" "J&T Ventures" "Springtide" "Tachles" "Baryon" "Orbit Capital" "Air Ventures" "Czech Founders"; do r=$(curl -s --max-time 30 -A "Mozilla/5.0" -G "https://api.adviserinfo.sec.gov/search/firm" --data-urlencode "query=$q" --data-urlencode "hl=true" --data-urlencode "nrows=5" --data-urlencode "start=0" --data-urlencode "wt=json" | [redacted: local path] -c "
import json,sys
try:
  d=json.load(sys.stdin)['hits'];print(d['total'],[ (h['_source'].get('firm_name'),h['_source'].get('firm_source_id'),h['_source'].get('firm_ia_address_details','')[:80]) for h in d['hits'][:4]])
except Exception as e: print('err',e)"); echo "$q: $r"; done
```

<details><summary>result</summary>

```
Credo Ventures: 0 []
Presto Ventures: 0 []
Reflex Capital: 1 [('REFLEXIVE CAPITAL MANAGEMENT LP', '327416', '{"officeAddress": {"street1": "1160 BATTERY STREET EAST", "street2": "SUITES 100')]
Kaya: 4 [('BLUE KAYAK PARTNERS', '148258', '{"officeAddress": {"city": "FRANKLIN", "state": "TN", "country": "United States"'), ('KAYAN SECURITIES, INC.', '156175', ''), ('KAYAK CAPITAL MANAGEMENT INC.', '306023', '{"officeAddress": {"street1": "2311 JUNIPER ROAD NW", "city": "CALGARY, ALBERTA"'), ('KAYAK INVESTMENT PARTNERS LLC', '166116', '{"officeAddress": {"city": "SAN FRANCISCO", "state": "CA", "country": "United St')]
Rockaway: 0 []
RockawayX: 0 []
Tensor Ventures: 0 []
ZAKA: 2 [('ZAKARA CAPITAL, LLC', '337211', '{"officeAddress": {"street1": "300 PARK AVENUE", "street2": "5TH FLOOR", "city":'), ('ZAKARI CAPITAL MANAGEMENT LLC', '319176', '{"officeAddress": {"city": "MORGAN HILL", "state": "CA", "country": "United Stat')]
Purple Ventures: 0 []
Soulmates: 0 []
Lighthouse Ventures: 2 [('LIGHTHOUSE NETWORK VENTURES LLC', '342115', '{"officeAddress": {"street1": "1717 E CARY STREET", "city": "RICHMOND", "state":'), ('XYPN SAPPHIRE', '285967', '{"officeAddress": {"street1": "24 E. MAIN STREET", "city": "BOZEMAN", "state": "')]
J&T Ventures: 10 [('JDA VENTURES CORPORATION', '104340', ''), ('TRITONPOINT WEALTH, LLC', '328398', '{"officeAddress": {"street1": "5404 WISCONSIN AVE", "street2": "STE. 330", "city'), ('THE MCFOLLING FINANCIAL GROUP', '157779', '{"officeAddress": {"city": "APOLL
… [1425 more characters]
```
</details>

→ `Bash` — Fetch candidate portfolio pages for CZ VCs
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.prestoventures.com/ https://www.prestoventures.com/portfolio https://www.reflexcapital.com/ https://www.reflexcapital.com/portfolio https://www.jtventures.cz/ https://www.jtventures.cz/portfolio https://lhv.vc/portfolio/ https://www.zaka.vc/portfolio/ https://www.purple-ventures.com/ https://www.purple-ventures.com/portfolio https://rockawayventures.com/ https://www.miton.cz/portfolio https://www.miton.cz/ https://www.soulmates.ventures/ https://www.soulmatesventures.com/portfolio/ https://startupyard.com/portfolio/ https://www.credoventures.com/portfolio https://www.ysoftventures.com/ https://www.seedstarter.cz/ 2>&1 | grep -v REPLACEMENT
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=utf-8 https://www.prestoventures.com/  len=8024
[redacted: local path]  200 text/html; charset=utf-8 https://www.prestoventures.com/portfolio  len=6363
[redacted: local path]  200 text/html; charset=UTF-8 https://www.reflexcapital.com/  len=4396
[redacted: local path]  200 text/html; charset=UTF-8 https://www.reflexcapital.com/portfolio/  len=10317
[redacted: local path]  200 text/html; charset=utf-8 https://www.jtventures.cz/  len=1786
[redacted: local path]  200 text/html; charset=utf-8 https://www.jtventures.cz/portfolio  len=1658
[redacted: local path]  200 text/html; charset=UTF-8 https://lhv.vc/portfolio/  len=3053
[redacted: local path]  200 text/html; charset=UTF-8 https://zaka.vc/portfolio/  len=12795
[redacted: local path]  200 text/html; charset=UTF-8 https://www.purple-ventures.com/  len=47251
[redacted: local path]  200 text/html; charset=utf-8 https://purple-team.notion.site/6e69e7fb82594b6ab6a4d677522ca881?v=dd5d21e2b10e464e8ceadb32317c03e1  le
… [1263 more characters]
```
</details>

→ `Bash` — Show portfolio pages (Presto, Reflex, J&T, Lighthouse)
```sh
cd [redacted: local path] && cat > bin/show.py <<'EOF'
import sys
sys.path.insert(0, "[redacted: local path]")
from get import get
txt, meta = get(sys.argv[1])
t = txt.read_text()
a = int(sys.argv[2]) if len(sys.argv) > 2 else 0
b = int(sys.argv[3]) if len(sys.argv) > 3 else 2500
print(t.replace("\n", " | ")[a:b])
EOF
PY=[redacted: local path] for u in https://www.prestoventures.com/portfolio https://www.reflexcapital.com/portfolio https://www.jtventures.cz/portfolio https://lhv.vc/portfolio/; do echo "## $u"; $PY bin/show.py $u 0 1800; echo; done
```

<details><summary>result</summary>

```
## https://www.prestoventures.com/portfolio
Presto Ventures | Portfolio | Portfolio | Team | Founders | Horizons | News | Contact | Portfolio | Team | Founders | Horizons | News | Contact | Portfolio. | Projects. | Presto. | Filters | Reset All | 0 | results of | 0 | items | ORIGIN | Reset Filter | Belgium | Czechia | Estonia | Georgia | Greece | Kyrgyzstan | Lithuania | Latvia | Poland | Serbia | Slovakia | Tajikistan | Ukraine | IndustrY | Reset Filter | AI & Big Data | AR & VR | Consumer services | Cybersecurity & Infrastructure | Database | Deeptech | DevOps | E-commerce | Energy | Enterprise Software | eSport & Gaming | FinTech | Food | Hospitality | HRTech | Manufacturing | MarTech & AdTech | Metaverse | PropTech | RetailTech | Supply Chain | Sustainability | Transportation | Business Model | Reset Filter | Text Link | Hardware | Text Link | B2C | Text Link | Social Network | Text Link | Web3 | Text Link | B2B SaaS | Text Link | Marketplace | B2B SaaS | B2C | Hardware | Marketplace | Social Network | Web3 | Status | Reset Filter | Current | Exited | Thank you! Your submission has been received! | Oops! Something went wrong while submitting the form. | Company | ORIGIN | Year | Status | ABOUT | WEB | Required Nest Link | Adam | Czechia | 2022 | Current | Next-day interior painting services in 15+ countries | Required Nest Link | Behavio | Czechia | 2021 | Current | Ad-testing platform for maximum marketing effectiveness | Required Nest Link | Blindspot Tech | Czechia | 2
… [5861 more characters]
```
</details>

→ `Bash` — Inspect Lighthouse homepage and portfolio raw
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://lhv.vc/ 0 2500; echo; grep -o -i 'portfolio[^"]\{0,80\}' pages/a77d3485d3172791.raw | sort -u | head -20; grep -o -E 'wp-json[^"]{0,100}|admin-ajax[^"]{0,60}' pages/a77d3485d3172791.raw | sort -u | head
```

<details><summary>result</summary>

```
Lighthouse Ventures | % | Lighthouse Ventures is an early-stage venture capital, focused on technology projects with global vision | We bring inspiring | ideas to life | Learn more | B2B Software of various verticals, Fintech, AI | Investment focus | Apply now | From €200k to €1m | Investment in a single startup | Apply now | Idea / Seed | Preferred investment stage | Apply now | Europe and US | Geographies we invest in | Apply now | 2024 | Start year of most recent Fund II | Apply now | Previous | Next | Lighthouse Ventures | is an early-stage venture capital, focused on technology projects with global vision. | Our mission at Lighthouse Ventures is to nurture inspiring ideas throughout their critical early stage, financially as well as professionally, with an international team of | partners | bringing together expertise in entrepreneurship, startup mentoring, mergers and acquisitions, media and marketing, technology and operations, as well as a strong business network in the Europe and abroad. We also maintain a network of experienced mentors for the benefit of our portfolio companies. | Lighthouse Ventures invests in European and US based startups. It benefits from synergies and co-operation with leading start-up hubs, tech-partners and tech-universities. | Get in touch | Portfolio | Companies | See all | Partnerships | See all | Reviews | We provide entrepreneurs not only with funding, but also with professional support, bringing together expertise that our partners have
… [1172 more characters]
```
</details>

→ `Bash` — List Lighthouse WordPress post types
```sh
cd [redacted: local path] && curl -sL --max-time 30 -A "Mozilla/5.0" https://lhv.vc/wp-json/wp/v2/types | [redacted: local path] -c "import json,sys;d=json.load(sys.stdin);print({k:v.get('rest_base') for k,v in d.items()})"
```

<details><summary>result</summary>

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import json,sys;d=json.load(sys.stdin);print({k:v.get('rest_base') for k,v in d.items()})
                                                    ^^^^^
AttributeError: 'str' object has no attribute 'get'
```
</details>

→ `Bash` — Inspect Lighthouse API and ajax actions
```sh
cd [redacted: local path] && curl -sL --max-time 30 -A "Mozilla/5.0" https://lhv.vc/wp-json/wp/v2/types | head -c 600; echo; grep -o "admin-ajax.php'[^<]\{0,600\}" pages/a77d3485d3172791.raw | head -3; grep -o 'action[^,]\{0,80\}' pages/a77d3485d3172791.raw | sort -u | head
```

<details><summary>result</summary>

```
{"code":"itsec_rest_api_access_restricted","message":"You do not have sufficient permission to access this endpoint. Access to REST API requests is restricted by iThemes Security settings.","data":{"status":401}}
admin-ajax.php',
action_close_header cli_action_button" >Accept All</a></div></div></span></div><div id
action_close_header_reject {
action_close_header_reject cli_action_button"  data-cli_action="reject">Reject All</a>
action_close_header_reject:hover {
action_close_header_reject"  class="medium cli-plugin-button cli-plugin-main-button co
action="" method="post">
action="accept_all"  class="wt-cli-element medium cli-plugin-button wt-cli-accept-all-
action="accept" class="wt-cli-privacy-btn cli_setting_save_button wt-cli-privacy-accep
actions">
```
</details>

→ `Bash` — Look for portfolio company links in Lighthouse HTML
```sh
cd [redacted: local path] && grep -o -i -E '.{100}(ahoy|hermetiq|merchantee|ranketta).{100}' pages/a77d3485d3172791.raw pages/e0299fc3b17817db.raw | head -5; grep -o 'https://lhv.vc/[a-z0-9_/-]*' pages/a77d3485d3172791.raw | sort -u | head -40
```

<details><summary>result</summary>

```
https://lhv.vc/
https://lhv.vc/about-us/
https://lhv.vc/acceleration/
https://lhv.vc/apply-now/
https://lhv.vc/cookies-policy/
https://lhv.vc/faq/
https://lhv.vc/news-and-events/
https://lhv.vc/partnerships/
https://lhv.vc/portfolio/
https://lhv.vc/privacy-policy/
https://lhv.vc/project/beatpulselabs/
https://lhv.vc/project/boost-space/
https://lhv.vc/project/cytokine/
https://lhv.vc/project/dayswaps/
https://lhv.vc/project/decisionrules/
https://lhv.vc/project/deepmark/
https://lhv.vc/project/deplace-ai/
https://lhv.vc/project/dookan/
https://lhv.vc/project/edmund-ai/
https://lhv.vc/project/faceup/
https://lhv.vc/project/factoree/
https://lhv.vc/project/financial-antivirus/
https://lhv.vc/project/fleetfox/
https://lhv.vc/project/foxdeli/
https://lhv.vc/project/hermetiq/
https://lhv.vc/project/investown/
https://lhv.vc/project/jobsider/
https://lhv.vc/project/kernolab/
https://lhv.vc/project/localazy/
https://lhv.vc/project/malcom-finance/
https://lhv.vc/project/merchantee/
https://lhv.vc/project/midbrain/
https://lhv.vc/project/ng-aviation/
https://lhv.vc/project/nutritionpro/
https://lhv.vc/project/outfindo/
https://lhv.vc/project/pekat-vision-2/
https://lhv.vc/project/persoo/
https://lhv.vc/project/phantasma-labs/
https://lhv.vc/project/prodeen/
https://lhv.vc/project/product-fruits/
```
</details>

→ `Bash` — Inspect markup around a Lighthouse project link
```sh
cd [redacted: local path] && grep -o -E '.{300}project/boost-space/.{300}' pages/a77d3485d3172791.raw | head -2
```

<details><summary>result</summary>

```
(Bash completed with no output)
```
</details>

→ `Bash` — Print context around project link
```sh
cd [redacted: local path] && [redacted: local path] -c "
h=open('pages/a77d3485d3172791.raw',encoding='utf-8',errors='replace').read()
i=h.find('project/boost-space/');print(h[i-600:i+400])"
```

<details><summary>result</summary>

```
ipt></noscript></noscript>


        <img  data-src="https://lhv.vc/wp-content/uploads/2019/11/persoo.png" class="img-hor post-loop-grid-img lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" /><noscript><img class="img-hor post-loop-grid-img" src="https://lhv.vc/wp-content/uploads/2019/11/persoo.png" /></noscript>
        </a></div><hr style='display:block;width:100%;'><div><a>
    </a>
</div>


                    <div class="post-loop-grid-item splazy-item post-loop-grid-item-project i5952">
    <a class="post-loop-grid-item-inner scheme-sec" href="https://lhv.vc/project/boost-space/">
                    <img style="position:absolute;top:0;left:0;width:50%;z-index:9;"  data-src="//lhv.vc/wp-content/themes/lighthouse/img/content/lhv-fund-2.png" class="lazyload" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="><noscript><img style="position:absolute;top:0;left:0;width:50%;z-index:9;"  data-src="//lhv.vc/wp-content/themes/lighthouse/img/cont
```
</details>

→ `Bash` — List Wayback snapshots of EIF Czech fund lists
```sh
curl -s --max-time 60 -A "investordb/0.1" "https://web.archive.org/cdx/search/cdx?url=eif.org/files/attachments/czechia-equity-fundmanagers.pdf&output=json&filter=statuscode:200&fl=timestamp,original,digest" | head -40; curl -s --max-time 60 -A "investordb/0.1" "https://web.archive.org/cdx/search/cdx?url=eif.org/what_we_do/where/cz*&output=json&filter=statuscode:200&fl=timestamp,original&collapse=urlkey&limit=50" | head -40
```

<details><summary>result</summary>

```
[]
[["timestamp","original"],
["20151003012509","http://www.eif.org/what_we_do/where/cz/"],
["20251006131956","https://www.eif.org/what_we_do/where/cz/eif-in-czechia.png"],
["20151215144718","http://www.eif.org/what_we_do/where/cz/index.htm"]]
```
</details>

→ `Bash` — Search Wayback for older EIF Czech/Slovak lists
```sh
curl -s --max-time 60 -A "investordb/0.1" "https://web.archive.org/cdx/search/cdx?url=eif.org/attachments/*czech*&output=json&filter=statuscode:200&fl=timestamp,original&collapse=urlkey&limit=50" | head -30; curl -s --max-time 60 -A "investordb/0.1" "https://web.archive.org/cdx/search/cdx?url=eif.org/files/attachments/*&output=json&filter=statuscode:200&fl=timestamp,original&collapse=urlkey&limit=2000" | grep -i -E "czech|slovak|fundmanager|fund-manager|equity" | head -30
```

<details><summary>result</summary>

```
[]
["20260105002527","https://www.eif.org/files/attachments/belgium-equity-fundmanagers.pdf"],
["20260314153450","https://www.eif.org/files/attachments/checklist-equity-investment-proposal-form.pdf"],
["20260429192024","https://www.eif.org/files/attachments/eif-equity-fundmanagers-all-countries-dec-2025.pdf"],
["20260624065230","https://www.eif.org/files/attachments/eif-equity-fundmanagers-all-countries-jun-2026.pdf"],
["20251219132339","https://www.eif.org/files/attachments/eif-equity-fundmanagers-all-countries-sep-2025.pdf"],
["20260105005152","https://www.eif.org/files/attachments/france-equity-fundmanagers.pdf"],
["20260105010556","https://www.eif.org/files/attachments/germany-equity-fundmanagers.pdf"],
["20260218005627","https://www.eif.org/files/attachments/greece-equity-fundmanagers.pdf"],
["20260104230237","https://www.eif.org/files/attachments/italy-equity-fundmanagers.pdf"],
["20260105000335","https://www.eif.org/files/attachments/luxembourg-equity-fundmanagers.pdf"],
["20260105003518","https://www.eif.org/files/attachments/netherlands-equity-fundmanagers.pdf"],
["20260618014704","https://www.eif.org/files/attachments/norway-equity-fundmanagers.pdf"],
["20260427120838","https://www.eif.org/files/attachments/slovenia-equity-fundmanagers.pdf"],
["20260104230826","https://www.eif.org/files/attachments/spain-equity-fundmanagers.pdf"]]
```
</details>

→ `Bash` — Fetch EIF all-country fund manager lists
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.eif.org/files/attachments/eif-equity-fundmanagers-all-countries-sep-2026.pdf https://www.eif.org/files/attachments/eif-equity-fundmanagers-all-countries-jun-2026.pdf 2>&1 | tail -2
```

<details><summary>result</summary>

```
[redacted: local path]  200 application/pdf https://www.eif.org/files/attachments/eif-equity-fundmanagers-all-countries-sep-2026.pdf  len=113503
[redacted: local path]  200 application/pdf https://www.eif.org/files/attachments/eif-equity-fundmanagers-all-countries-jun-2026.pdf  len=124631
```
</details>

→ `Bash` — Grep EIF all-country list for target managers
```sh
cd [redacted: local path] && grep -n -i -E "credo|presto|reflex|tilia|kaya|lighthouse|zaka|purple|rockaway|tensor|nation ?1|depo |miton|inven|biotech|i&i|soulmates|startupyard|y soft|startguide|gain ven|bhm|czech founders|orbit|impulse|koopeo|air ventures|springtide|up21|baryon|neulogy|vision ven|0100|zero gravity|g-force|cb investment|cb growth|limerock|venture to future|seed starter|365|monogram|ipm |lrj|j&t|as at" pages/8584d53fdf2b47cb.txt | head -40
```

<details><summary>result</summary>

```
56:Invenio Partners Fund II SCSp Invenio Partners OOD Bulgaria COSME-EFG;EIF;JER-009 BULGARIA Multi-Country Private Equity Generalist Lower-Mid Market Fund 13/12/2026 http://empowercapital.net/
83:Tilia Impact Ventures Fund II Tilia Impact Partners Czech Republic IEU - Equity - LP Agriculture, Food, natural capital preservation and
88:Multi-Country Venture Capital ICT Early Stage Fund Fund 01/08/2028 https://tiliaimpactventures.cz/en/
92:Tensor Co-Investment Fund SCSp Tensor Advisory s.r.o Czech Republic RRF Czech Republic Artificial Intelligence (AI);Blockchain and Distributed
99:Kaya 5 SCSp KAYA Advisory s.r.o. Czech Republic EIF;RCR Artificial Intelligence (AI);Defense;Energy and built-
102:Multi-Country Venture Capital ICT Pre-Seed/Seed Fund Fund 11/06/2030 https://www.kaya.vc/
103:Orbit Growth Debt II OGD Advisory s.r.o. Czech Republic 3SIIF;FTP;IEU - DDF - LP Debt and hybrid debt-equity funds Multi-Country Private Debt ICT Private Credit Fund Fund 27/05/2029 https://orbitcapital.com/
145:as at 30 September 2026 - All countries -
149:Inventure Fund IV Ky Onventure Oy Finland EIF;IEU - Equity - PP;RCR Other Digital Multi-Country Venture Capital ICT Early Stage Fund Fund 28/01/2027 http://inventure.fi/about-us/
303:as at 30 September 2026 - All countries -
485:as at 30 September 2026 - All countries -
670:as at 30 September 2026 - All countries -
793:Claris Biotech II Claris Ventures SGR SpA Italy EIF;IEU - Equity - LP;RCR Life science and health Multi-Country Ventur
… [668 more characters]
```
</details>

→ `WebSearch` Czech ESIF Fund of Funds Lighthouse Ventures Nation 1 EIF signs

<details><summary>result</summary>

```
Web search results for query: "Czech ESIF Fund of Funds Lighthouse Ventures Nation 1 EIF signs"

Links: [{"title":"EIF in my country","url":"https://www.eif.org/supporting-smes/eif-near-me/czechia"},{"title":"RRF Czech Republic Fund of Funds","url":"https://www.eif.org/equity-products/all/rrf-czech-republic"},{"title":"EIF in the Czech Republic - EIF in my country","url":"https://engage.eif.org/eif-in-my-country/eif-in-the-czech-republic"},{"title":"Czechia and EIF launch €55 million fund of funds for digital technologies backed by Recovery and Resilience Facility","url":"https://www.eif.org/press/all/czech-republicand-eif-launch-55-million-fund-of-funds-for-digital-technologies-backed-by-recovery-and-resilience-facility"},{"title":"Homepage","url":"https://www.eif.org/"},{"title":"Launch of New Fund of Funds to Support European Tech Champions","url":"https://www.eif.org/what_we_do/news/2023/launch-of-new-fund-of-funds-to-support-european-tech-champions.htm"},{"title":"New Czech fund backs AI and deep-tech innovation with €50m for research commercialisation","url":"https://www.eif.org/press/all/first-czech-technology-transfer-fund-focused-on-ai-applications-to-invest-nearly-eur50-million-in-research-commercialisation"},{"title":"EIF Three Seas Initiative to boost growth-stage companies in central-eastern Europe","url":"https://eif.org/what_we_do/equity/news/2024/central-and-eastern-europes-growth-stage-companies-get-boost-as-polish-and-czech-promotional-institutions-become-fi
… [1695 more characters]
```
</details>

→ `Bash` — Show ZAKA, Rockaway, Miton, Soulmates pages
```sh
cd [redacted: local path] && PY=[redacted: local path] for u in https://www.zaka.vc/portfolio/ https://rockawayventures.com/ https://www.miton.cz/portfolio https://www.soulmatesventures.com/portfolio/; do echo "## $u"; $PY bin/show.py $u 0 1500; echo; done
```

<details><summary>result</summary>

```
## https://www.zaka.vc/portfolio/
Portfolio Archive - ZAKA VC | Skip to content | Home | About | Team | Portfolio | Co-Investors | News | Jobs | Contact | Submit pitch deck | Submit pitch deck | Home | About | Team | Portfolio | Co-Investors | News | Jobs | Contact | E-mail is copied | Portfolio | Our global | investment activity | Check out all the cities | WonderTx / Aerogen Systems / FinalDose / PerfectBit / Human Archive / AxionOrbital Space / CellType / Sygaldry Technologies / HexemBio / Ateios Systems / Mews / Zephyr Fusion / DeepSeq.AI / Kangaroo Biomedical / Cirrus Therapeutics / Kano Therapeutics / Lunabill / Verne Robotics / Avelis Health / b-12 / Nephrogen / Bullseye Biosciences / Alixia Therapeutics / Adentris / Bluejay / Mbodi AI / Inversion Semiconductor / Momentous Therapeutics / | WonderTx / Aerogen Systems / FinalDose / PerfectBit / Human Archive / AxionOrbital Space / CellType / Sygaldry Technologies / HexemBio / Ateios Systems / Mews / Zephyr Fusion / DeepSeq.AI / Kangaroo Biomedical / Cirrus Therapeutics / Kano Therapeutics / Lunabill / Verne Robotics / Avelis Health / b-12 / Nephrogen / Bullseye Biosciences / Alixia Therapeutics / Adentris / Bluejay / Mbodi AI / Inversion Semiconductor / Momentous Therapeutics / | Promakhos / Superlinked / Creasallis / ExoMatter / Sutro / Yenmo / edgetrace / Lime Therapeutics / SharpGrid / Eigen Therapeutics / Webel / Olio Labs / SpectreXR / KiraGen / InGel Therapeutics / Salu / Vetstor / MediSearch / ParcelBio / ExcepGen
… [4655 more characters]
```
</details>

→ `Bash` — Look for portfolio lists on Rockaway and Soulmates
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/grep.py https://rockawayventures.com/ "portfolio" 300 | head -20; $PY bin/show.py https://www.soulmatesventures.com/portfolio/ 1500 5000
```

<details><summary>result</summary>

```
[0 matches, meta=['200 text/html; charset=UTF-8 https://rockawayventures.com/']]
ome-share financing and a data-driven underwriting platform that ensures fair, scalable, and performance-aligned outcomes. | Energy | Modular Virtual Power Plant platform for connecting and managing energy assets such as renewable energy sources fostering sustainable energy transition and profitability. | Education | Twin Science empowers children with STEM and AI skills to prepare them for the sustainable jobs of the future, driving innovation in education and fostering a new generation of environmentally conscious leaders. | Education | Youni transforms global education by effortlessly linking students with universities worldwide through its advanced AI-driven platform. | Healthcare | Signapse employs an AI-powered Sign Language Avatar to enable instant and seamless communication for the deaf through real-time Sign Language translation. | Others | AI-powered fintech boosting SME growth with sustainable financing and real-time insights. | Healthcare | Kardi AI connects your heart to a cardiologist from home, saving over 200 lives by 2023 with real-time insights. | Energy | Climate-tech boosting financial and operational efficiency by improved decision-making for the energy industry supporting the green transition. | Food & AG | Sustainable, natural supplements to boost health and performance. | Circular Economy | Global digital twin platform to navigate your business on any device wherever you a
… [2081 more characters]
```
</details>

→ `Bash` — List Rockaway Ventures site links
```sh
cd [redacted: local path] && grep -o 'href="https://rockawayventures.com/[^"]*"' pages/be381f0492e00b84.raw | sort -u | head -30
```

<details><summary>result</summary>

```
href="https://rockawayventures.com/"
href="https://rockawayventures.com/app/themes/rockaway-portfolio/resources/img/skin/green/favicon.ico"
href="https://rockawayventures.com/app/themes/rockaway-portfolio/resources/img/sprite.svg#linkedin"
href="https://rockawayventures.com/app/themes/rockaway-portfolio/resources/img/sprite.svg#twitter"
href="https://rockawayventures.com/app/themes/rockaway-portfolio/resources/img/testimonial-slider-sprite.svg#arrow-left"
href="https://rockawayventures.com/app/themes/rockaway-portfolio/resources/img/testimonial-slider-sprite.svg#arrow-right"
href="https://rockawayventures.com/contact/"
href="https://rockawayventures.com/for-founders/"
href="https://rockawayventures.com/for-investors/"
href="https://rockawayventures.com/news/"
href="https://rockawayventures.com/rockaway-ventures-at-kviff-united-europe-tech-villa-as-a-launchpad-for-ideas-and-collaboration/"
href="https://rockawayventures.com/rockaway-ventures-leads-4-2m-seed-round-in-czech-ai-startup-filuta-ai/"
href="https://rockawayventures.com/team/"
```
</details>

→ `Bash` — Fetch Rockaway Ventures investor/news pages
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://rockawayventures.com/for-investors/ https://rockawayventures.com/portfolio/ https://rockawayventures.com/news/ https://www.rockawaycapital.com/ ; $PY bin/grep.py https://rockawayventures.com/for-investors/ "portfolio" 400 | head; $PY bin/show.py https://rockawayventures.com/news/ 0 2500
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://rockawayventures.com/for-investors/  len=14559
[redacted: local path]  200 text/html; charset=UTF-8 https://rockawayventures.com/for-founders-old/portfolio-old/  len=13443
[redacted: local path]  200 text/html; charset=UTF-8 https://rockawayventures.com/news/  len=25508
[redacted: local path]  200 text/html; charset=utf-8 https://www.rockawaycapital.com/cs  len=9784
... For Investors | Rockaway Ventures CAPITALIZE ON INNOVATION We are experienced venture capitalists with a successful track record of investing in high-potential startups. Our portfolio of past investments includes several high-profile exits, and we have already generated returns of more than 140% of the invested capital from our previous VC investments. We are also proud to have a unicorn in our portfolio, and we have a clear vision to generate total returns of more than 4x MoM multiple and 35%+ IRR. Since 2022, we are investing from a new dedicated VC fund, and we are committe ...

... For Investors | Rockaway Ventures CAPITALIZE ON INNOVATION We are experienced venture capitalists with a successful track record of investing in high-potential startups. Our portfolio of past investments includes several high-profile exits, and we have already generated returns of
… [3946 more characters]
```
</details>

→ `Bash` — Find portfolio section on Rockaway for-investors page
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/grep.py https://rockawayventures.com/for-investors/ "OUR PORTFOLIO|Portfolio companies|Show website [A-Z][A-Za-z.]+ " 150 | head -30
```

<details><summary>result</summary>

```
... away Ventures CAPITALIZE ON INNOVATION We are experienced venture capitalists with a successful track record of investing in high-potential startups. Our portfolio of past investments includes several high-profile exits, and we have already generated returns of more than 140% of the invested capital from our pre ...

...  we have already generated returns of more than 140% of the invested capital from our previous VC investments. We are also proud to have a unicorn in our portfolio, and we have a clear vision to generate total returns of more than 4x MoM multiple and 35%+ IRR. Since 2022, we are investing from a new dedicated VC ...

... iciency. With applications in gaming, defense, and automotive, Filuta AI is setting new standards for intelligent automation in complex environments. Show website CulturePulse Deep tech company that uses AI to simulate and predict human behavior in real time. By combining insights from psychology, linguistics, and machine le ...

... markets. Their technology is used in sectors such as media, policy, and crisis communication, enabling smarter decisions through behavioral modeling. Show website Cruxo Cruxo.io is a data-driven platform that simplifies and optimizes retail media management for e-commerce businesses. It enables automated campaign mana ...

... and Czech Founders VC, Cruxo has secured funding to expand internationally. Key clients include major e-shops like Dr. Max, Astratex, and Lékárna.cz. Show website Valpas Valpas is a Fin
… [3451 more characters]
```
</details>

→ `Bash` — Show Rockaway old portfolio page
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://rockawayventures.com/portfolio/ 0 1500
```

<details><summary>result</summary>

```
Portfolio &#8211; old | Rockaway Ventures | Portfolio | €6,7M | invested | 5 | projects | Rockaway Ventures Portfolio | Filuta AI | Filuta AI is a Czech startup pioneering Composite AI for game testing and beyond. Their platform combines symbolic and subsymbolic AI to create autonomous, engine-agnostic agents that perform QA tasks at unprecedented scale and efficiency. With applications in gaming, defense, and automotive, Filuta AI is setting new standards for intelligent automation in complex environments. | Show website | CulturePulse | Deep tech company that uses AI to simulate and predict human behavior in real time. By combining insights from psychology, linguistics, and machine learning, their platform helps companies and institutions understand cultural dynamics and audience responses across markets. Their technology is used in sectors such as media, policy, and crisis communication, enabling smarter decisions through behavioral modeling. | Show website | Cruxo | Cruxo.io is a data-driven platform that simplifies and optimizes retail media management for e-commerce businesses. It enables automated campaign management at scale, maximizing on-site ad revenue and enhancing ad relevance for customers. Backed by Rockaway Ventures and Czech Founders VC, Cruxo has secured funding to expand internationally. Key clients include major e-shops like Dr. Max, Astratex, and Lékárna.cz. | Show website | Valpas | Valpas is a Finnish startup that integrates IoT technology into hospital
```
</details>

→ `Bash` — Show Credo, Y Soft, Seed Starter pages
```sh
cd [redacted: local path] && PY=[redacted: local path] for u in https://www.credoventures.com/portfolio https://www.ysoftventures.com/ https://www.seedstarter.cz/; do echo "## $u"; $PY bin/show.py $u 0 2200; echo; done; grep -o 'href="[^"]*"' pages/7e23b1a8d5683be5.raw | grep -i -E "portfol|startup|compan" | sort -u | head
```

<details><summary>result</summary>

```
## https://www.credoventures.com/portfolio
Portfolio | Credo | Portfolio | , | Team | , | Manifesto | , | Newsroom | Contact | Po | r | t | f | ol | io | Po | r | t | f | ol | io | Po | r | t | f | ol | io | Po | r | t | f | ol | io | (Pre-seeds) | 84 | 84 | 84 | 84 | Selection | Since 2009 | Highlights | We believe in founders across the CEE region and CEE diaspora communities. Backing them to build global, category-defining companies. From Pre-Seed. | Exited | Exited | Exited | Exited | Exited | Exited | Exited | Exited | Exited | All | RIP | RIP | RIP | RIP | Bugprove | RIP | Bugprove | RIP | Bugprove | RIP | Goodlegal | RIP | Goodlegal | RIP | Goodlegal | RIP | Assetario | RIP | Assetario | RIP | Assetario | RIP | Talkbase | RIP | Talkbase | RIP | Talkbase | RIP | Munch.so | RIP | Munch.so | RIP | Munch.so | RIP | RIP | RIP | Stock Story | Stock Story | Stock Story | Exited | Exited | Exited | Exited | Exited | Exited | Exited | Manta | Exited | Manta | Exited | Manta | Exited | Waymark | Exited | Waymark | Exited | Waymark | Exited | Exited | Exited | Exited | Exited | Exited | Exited | Exited | Exited | Exited | SignAll | Exited | SignAll | Exited | SignAll | Exited | GoAvio | Exited | GoAvio | Exited | GoAvio | Exited | Represent | Exited | Represent | Exited | Represent | Exited | Exited | Exited | Exited | Exited | Exited | Exited | Apiary | Exited | Apiary | Exited | Apiary | Exited | DataFeedWatch | Exited | DataFeedWatch | Exited | DataFeedWatch | Exited | Klick2C
… [5081 more characters]
```
</details>

→ `Bash` — Check Y Soft and Seed Starter portfolio markup
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/grep.py https://www.ysoftventures.com/ "portfolio" 300 | head -12; grep -o -i 'alt="[^"]*"' pages/8995d79dd8581eab.raw | sort -u | head -30; grep -o 'href="[^"]*"' pages/8995d79dd8581eab.raw | sort -u | head -30
```

<details><summary>result</summary>

```
...  Virtual Reality In augmented and virtual reality (AR and VR), we are keen on B2B-oriented solutions that take a different angle on challenges brought by Smart Office, Smart Factory, or Retail 2.0 trends. Since B2C doesn't float our boat, we are not looking for consumer-facing AR/VR applications. A Portfolio We're Proud Of Hear From Our Ventures Here's a look at how our portfolio companies are leading the charge in transformative technology, as told through their experiences and successes. Sewio Watch Sewio's success story unfold. "Our participation with Y Soft Ventures started in 2015. Now, we are suc ...

... n on B2B-oriented solutions that take a different angle on challenges brought by Smart Office, Smart Factory, or Retail 2.0 trends. Since B2C doesn't float our boat, we are not looking for consumer-facing AR/VR applications. A Portfolio We're Proud Of Hear From Our Ventures Here's a look at how our portfolio companies are leading the charge in transformative technology, as told through their experiences and successes. Sewio Watch Sewio's success story unfold. "Our participation with Y Soft Ventures started in 2015. Now, we are successfully operating in over 40 countries around the world. Thanks to pers ...

... ures team as a guide for startup entrepreneurs about employee shares in the Czech Republic. It answers questions such as, "Why should I start an employee equity program? How should it be implemented? How can I talk about it with my colleagues?" While it was
… [1571 more characters]
```
</details>

→ `Bash` — Find Y Soft portfolio company names
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/grep.py https://www.ysoftventures.com/ "success story unfold" 60; grep -o -i -E 'data-[a-z-]*(portfolio|url|src)[a-z-]*="[^"]{0,120}"|/content/[^"]*portfol[^"]*' pages/8995d79dd8581eab.raw | sort -u | head
```

<details><summary>result</summary>

```
... hrough their experiences and successes. Sewio Watch Sewio's success story unfold. "Our participation with Y Soft Ventures started in 2015. N ...

... ow Sentien Sewio’s Journey with Y Soft Ventures Watch their success story unfold. Here's How We Can Help You We deliver real value by guidin ...

[2 matches, meta=['200 text/html; charset=UTF-8 https://www.ysoft.com/ventures']]
```
</details>

→ `Bash` — Show Y Soft portfolio section text
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/grep.py https://www.ysoftventures.com/ "Sentien" 700 | head -5
```

<details><summary>result</summary>

```
... through their experiences and successes. Sewio Watch Sewio's success story unfold. "Our participation with Y Soft Ventures started in 2015. Now, we are successfully operating in over 40 countries around the world. Thanks to personal consultations with Y Soft managers, we have professionally entered a demanding industry segment." Milan Simek, Founder, Sewio Networks Get to know Sewio NenoVision Watch NenoVision's story. "Y Soft came to be our investor in 2019. At that time they supported us, not just financially, but also with their experience during our board meetings. They came to be a strong partner in our manufacturing and supply chain." Jan Neuman, CEO, NenoVision Get to know NenoVision Sentien Watch Sentien's story unfold. "We started to collaborate with Y Soft when we wanted to scale our production, and go from development to mass manufacturing. We always felt like it was a partnership, we always felt understood. We felt that they know where we're coming from." Imrich Valach, CEO, Sentien Get to know Sentien Sewio’s Journey with Y Soft Ventures Watch their success story unfold. Here's How We Can Help You We deliver real value by guiding startups in key business areas even before the investment closes. Strategic Management Y Soft senior leaders are here to help you tackle any strategic challenge you might face. You can meet them during quarterly board meetings or through one-on-o ...

... experiences and successes. Sewio Watch Sewio's success story unfold. "Our parti
… [2749 more characters]
```
</details>

→ `Bash` — List StartupYard site links
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://startupyard.com/ >/dev/null; grep -o 'href="https://startupyard.com/[^"]*"' pages/$( $PY -c "import hashlib;print(hashlib.sha1(b'https://startupyard.com/').hexdigest()[:16])").raw | sort -u | head -40
```

<details><summary>result</summary>

```
href="https://startupyard.com/apply-to-startupyard-remote-lab/"
href="https://startupyard.com/blog/"
href="https://startupyard.com/category/accelerator/"
href="https://startupyard.com/category/financing/"
href="https://startupyard.com/category/interviews/"
href="https://startupyard.com/category/marketing/"
href="https://startupyard.com/category/news/"
href="https://startupyard.com/category/personal/"
href="https://startupyard.com/category/starting-a-business/"
href="https://startupyard.com/category/startup-tools/"
href="https://startupyard.com/category/startup/"
href="https://startupyard.com/faq/"
href="https://startupyard.com/feed/"
href="https://startupyard.com/for-investors/"
href="https://startupyard.com/for-startups/"
href="https://startupyard.com/frequently-asked-questions-about-startupyard/"
href="https://startupyard.com/mentors/"
href="https://startupyard.com/new-homepage/"
href="https://startupyard.com/wp-content/uploads/2024/09/cropped-SY-icon-180x180.png"
href="https://startupyard.com/wp-content/uploads/2024/09/cropped-SY-icon-192x192.png"
href="https://startupyard.com/wp-content/uploads/2024/09/cropped-SY-icon-32x32.png"
href="https://startupyard.com/wp-json/"
href="https://startupyard.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fstartupyard.com%2F"
href="https://startupyard.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fstartupyard.com%2F&#038;format=xml"
href="https://startupyard.com/wp-json/wp/v2/pages/176735043"
href="https://startupyard.com/xmlrpc.php?rsd"

… [41 more characters]
```
</details>

→ `Bash` — Look for StartupYard portfolio list
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://startupyard.com/for-investors/ https://startupyard.com/startups/ https://startupyard.com/our-startups/; $PY bin/grep.py https://startupyard.com/for-investors/ "portfolio|alumni|startups such as|including" 250 | head -12; $PY bin/grep.py https://startupyard.com/ "portfolio|alumni" 200 | head -8
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://startupyard.com/for-investors/  len=8629
[redacted: local path]  200 text/html; charset=UTF-8 https://startupyard.com/startups-embrace-think-pricing/  len=16874
[redacted: local path]  404 text/html; charset=UTF-8 https://startupyard.com/our-startups/  len=4074
... Partner, Credo Ventures “Working with StartupYard puts us at the ground level of new ideas and emerging technologies. It’s already brought us great investments, like Gjirafa.com” Dusan Zabrodsky Rockaway Capital Previous Next REQUEST THE STARTUPYARD PORTFOLIO Looking to invest in a startup? Receive our portfolio of companies currently fund-raising. Enter your email to receive it. Enter your email address * Meet Our Shareholders At StartupYard, we are proud to be backed by a distinguished group of investo ...

...  us at the ground level of new ideas and emerging technologies. It’s already brought us great investments, like Gjirafa.com” Dusan Zabrodsky Rockaway Capital Previous Next REQUEST THE STARTUPYARD PORTFOLIO Looking to invest in a startup? Receive our portfolio of companies currently fund-raising. Enter your email to receive it. Enter your email address * Meet Our Shareholders At StartupYard, we are proud to be backed by a distinguished group of investors who share our passion for innovation, technology, a
… [2572 more characters]
```
</details>

→ `Bash` — Show StartupYard news category
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://startupyard.com/category/news/ >/dev/null; $PY bin/show.py https://startupyard.com/category/news/ 0 3000
```

<details><summary>result</summary>

```
StartupYard News Archives - StartupYard | Meet Teamsharq: The Platform That Puts a Full Computer in Every Student’s Browser | June 15, 2026 | / | in | Interviews | , | StartupYard News | / | by | StartupYard | Read more | http://startupyard.com/wp-content/uploads/2026/03/SY_accelerator_dark-15-years-2.png | 0 | 0 | StartupYard | http://startupyard.com/wp-content/uploads/2026/03/SY_accelerator_dark-15-years-2.png | StartupYard | 2026-06-15 13:22:38 | 2026-06-16 12:54:42 | Meet Teamsharq: The Platform That Puts a Full Computer in Every Student’s Browser | Meet CaseLens: The AI Specialized in Complex Disputes | April 30, 2026 | / | in | Interviews | , | StartupYard News | / | by | StartupYard | Read more | https://startupyard.com/wp-content/uploads/2026/04/CaseLens-Team-EPIC-Office.png | 560 | 1024 | StartupYard | http://startupyard.com/wp-content/uploads/2026/03/SY_accelerator_dark-15-years-2.png | StartupYard | 2026-04-30 14:55:11 | 2026-06-15 13:24:49 | Meet CaseLens: The AI Specialized in Complex Disputes | The Next Wave Begins: StartupYard Announces Batch 15 | September 11, 2025 | / | in | Financing | , | StartupYard News | / | by | StartupYard | Read more | https://startupyard.com/wp-content/uploads/2025/09/pokerstack_a_high_definition_group_photography_of_happy_white_3f38f0b0-4100-4378-99b3-c22f8accc865_1.png | 768 | 1536 | StartupYard | http://startupyard.com/wp-content/uploads/2026/03/SY_accelerator_dark-15-years-2.png | StartupYard | 2025-09-11 16:20:49 | 2025-09-19 06
… [1500 more characters]
```
</details>

→ `Bash` — Fetch StartupYard Batch 15 announcement
```sh
cd [redacted: local path] && PY=[redacted: local path] grep -o 'href="https://startupyard.com/[^"]*batch-15[^"]*"' pages/*.raw | head -2; U=$(grep -oh 'https://startupyard.com/[^"]*batch-15[^"]*' pages/*.raw | head -1); echo $U; $PY bin/get.py "$U"; $PY bin/grep.py "$U" "SmartGuide|invest|Batch 15 (startups|companies|teams)" 250 | head -20
```

<details><summary>result</summary>

```
pages/bd384667f3613f39.raw:href="https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/"
pages/bd384667f3613f39.raw:href="https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/"
https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/' data-rel='slide-1' class='slide-image' title='The Next Wave Begins: StartupYard Announces Batch 15'><img decoding=
[redacted: local path]  000  https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/' data-rel='slide-1' class='slide-image' title='The Next Wave Begins: StartupYard Announces Batch 15'><img decoding=  len=0
[0 matches, meta=["000  https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/' data-rel='slide-1' class='slide-image' title='The Next Wave Begins: StartupYard Announces Batch 15'><img decoding="]]
```
</details>

→ `Bash` — Fetch Batch 15 post and look for SmartGuide
```sh
cd [redacted: local path] && PY=[redacted: local path] U=https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/; $PY bin/get.py "$U"; $PY bin/grep.py "$U" "SmartGuide" 400 | head -6
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/  len=8862
[0 matches, meta=['200 text/html; charset=UTF-8 https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/']]
```
</details>

→ `Bash` — Show Batch 15 post text
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/ 0 5000
```

<details><summary>result</summary>

```
The Next Wave Begins: StartupYard Announces Batch 15 - StartupYard | The Next Wave Begins: StartupYard Announces Batch 15 | Where first-time founders from CEE earn legitimacy and launch bold ideas. | Since 2011, StartupYard has been the launchpad for some of Central Europe’s most ambitious startups | , from Rossum to Gjirafa, Carebot, SwapIn and FeedYou, to name a few. Over 120 startups later, with more than €100M raised by our alumni, we’re opening our 15th batch, this time with a sharp focus on AI and hard-to-replicate deep tech solutions. | What’s New in Batch 15 | For the first time, founders can access an optional €25,000 cash investment alongside the hands-on acceleration StartupYard is known for. This isn’t just about capital,  it’s the beginning of a journey where every step is personalized. | No generic group workshops. No cookie-cutter curriculum. Instead, tailored guidance designed around you and your company. Fully remote. | Who This Is For | Batch 15 is built for the first-time founder from CEE who is thinking globally from day one | . If you’re working on a problem that feels too complex, too ambitious, or too early for others, this is where you belong. | We’re industry-agnostic, but we look for solutions that are hard to replicate. Whether you’re building applied AI for healthcare, finance, manufacturing, cybersecurity, or something no one has imagined yet, | StartupYard is where those bold ideas get traction | . | Why StartupYard | StartupYard is | by tech ent
… [3500 more characters]
```
</details>

→ `Bash` — Look for portfolio names on Purple homepage
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/grep.py https://www.purple-ventures.com/ "portfolio" 300 | head -8
```

<details><summary>result</summary>

```
... cratch, achieved 3+ exits, and grown to global fintech group, thus we know how to add relevant value to founders. Expertise We can be of value in product, GTM, PR, hiring, strategy, or simply as a trusted friend along your journey. Eco-system Potential synergies with our network of global firms and portfolio companies. Our startups Meet the startups we partner with. 1/24 Fether Labs uses proprietary ultrasonic tendon sensing to translate natural hand gestures into low-latency control of digital and robotic systems. Its vision is to become the post-touch interface used by a billion people. https://www.f ...

... y and business, he brings experience from both corporate and startup environments. Prior to joining Purple Ventures, Matej worked at Deloitte helping companies develop effective AI strategies. His passion lies in applying technology to solve real-world challenges with meaningful impact. His project portfolio includes collaborating with Google to help 80,000+ students with distance learning, developing NLP applications for Alzheimer’s patients, creating ML solutions for cardiovascular disease prediction, and building Flutter applications for startups. Currently based in Prague, Matej is completing his u ...

...  in Utrecht, Matyáš is starting his studies in Netherlands. Before, he lived in the France, gained a well-rounded perspective on investment, data analytics, and international business. At Purple Ventures, you can find Matyáš doing everything from research, a
… [974 more characters]
```
</details>

→ `Bash` — Show Purple startups section
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/grep.py https://www.purple-ventures.com/ "Meet the startups we partner with" 1500 | head -3
```

<details><summary>result</summary>

```
... is to build a great global team and business from scratch. We believe in collaboration , enjoying the journey and the results, together with the founders, angel investors and other VCs. Our investment strategy We invest with conviction. Pre-seed & Seed investment rounds €250k to €400k initial ticket size, later follow-ons 4-7 years investment horizon Minority equity stake founders own, drive and manage the startup Happy co-investing and leading with angels and other VCs, leading up to 50% of rounds Our approach What we look for. Human Does the team have humbleness, sense of fair play, drive, and AI-first mindset? Market Is the total addressable market big enough? Does the team have unique industry insights? Competent Do founders have the competence to grow the firm globally? Product Does the startup address a real need? Is the business model ready for an AI/AGI future? Timing Is it now the right time to enter a market? ROI Does it have potential for healthy return on investment? 1/4 Empathy We respect and support the founders in a friendly, honest, humble and fair manner. Experience We learned how hard it is to build international businesses from scratch, achieved 3+ exits, and grown to global fintech group, thus we know how to add relevant value to founders. Expertise We can be of value in product, GTM, PR, hiring, strategy, or simply as a trusted friend along your journey. Eco-system Potential synergies with our network of global firms and portfolio companies. Our start
… [1626 more characters]
```
</details>

→ `Bash` — Show sources of SK records needing existence
```sh
.venv/bin/python - <<'EOF'
import json
recs={r['id']:r for r in json.load(open('data/sample/parts/sk.json'))}
for rid in ['seed-starter-slovenskej-sporitelne','365-fintech','monogram-ventures','baryon-fund','lrj-capital','ipm-group']:
    r=recs[rid]
    for i in r.get('investments') or []:
        for s in i['sources']: print(rid,'|',i['company'],'|',s['url'],'|',s['quote'][:200])
    for k,f in r['fields'].items():
        if f:
            for s in f['sources']: print(rid,'| field',k,'|',s['url'],'|',s['quote'][:150])
EOF
```

<details><summary>result</summary>

```
seed-starter-slovenskej-sporitelne | Webout | https://www.omediach.com/internet/30236-seed-starter-slovenskej-sporitelne-investuje-400-tisic-eur-do-startupu-webout-ten-ziskava-spolu-1-65-miliona-eur-a-mieri-do-silicon-valley | Seed Starter Slovenskej sporiteľne investuje 400-tisíc eur do startupu Webout. Ten získava spolu 1,65 milióna eur a mieri do Silicon Valley
seed-starter-slovenskej-sporitelne | IntellCRE | https://www.slsp.sk/sk/aktuality/2025/9/17/zo-slovenska-rovno-na-najvacsi-realitny-trh-intellcre-ziskava-investiciu-od-seed-startera-slovenskej-sporitelne | teraz získava investíciu vo výške 400 000 eur od Seed Startera Slovenskej sporiteľne
seed-starter-slovenskej-sporitelne | IntellCRE | https://www.slsp.sk/sk/aktuality/2025/9/17/zo-slovenska-rovno-na-najvacsi-realitny-trh-intellcre-ziskava-investiciu-od-seed-startera-slovenskej-sporitelne | Celkovo ide už o šiesty zainvestovaný startup v portfóliu Seed Startera.
seed-starter-slovenskej-sporitelne | SmartHead | https://sita.sk/seed-starter-slovenskej-sporitelne-hlasi-prvu-investiciu-podporil-slovensky-startup-smarthead/ | Seed Starter Slovenskej sporiteľne získal 7 % podiel v slovenskom startupe SmartHead
seed-starter-slovenskej-sporitelne | field funds | https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/ | Pět milionů eur, tedy v přepočtu více než 123 milionů korun, si připravila Slovenská spořitelna na první fázi podpory startupů na Slovensku.
365-finte
… [1930 more characters]
```
</details>

→ `Bash` — Check SLSP and 365.fintech portfolio mentions
```sh
cd [redacted: local path] && PY=[redacted: local path] U=https://www.slsp.sk/sk/aktuality/2025/9/17/zo-slovenska-rovno-na-najvacsi-realitny-trh-intellcre-ziskava-investiciu-od-seed-startera-slovenskej-sporitelne; $PY bin/get.py $U https://365fintech.sk/ https://www.slsp.sk/sk/seed-starter https://www.slsp.sk/sk/biznis/seed-starter; $PY bin/grep.py $U "portfóli|startup[ey]? [A-Z]" 300 | head -8; $PY bin/grep.py https://365fintech.sk/ "portfolio" 400 | head -4
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=utf-8 https://www.slsp.sk/sk/aktuality/2025/9/17/zo-slovenska-rovno-na-najvacsi-realitny-trh-intellcre-ziskava-investiciu-od-seed-startera-slovenskej-sporitelne  len=5903
[redacted: local path]  200 text/html; charset=utf-8 https://365fintech.sk/  len=8655
[redacted: local path]  404 text/html; charset=utf-8 https://www.slsp.sk/sk/seed-starter  len=885
[redacted: local path]  404 text/html; charset=utf-8 https://www.slsp.sk/sk/biznis/seed-starter  len=885
...  realitný trh sveta – Spojené štáty. S jasnou víziou, silným produktom a odvahou ísť do rizika. Práve preto teraz získava investíciu vo výške 400 000 eur od Seed Startera Slovenskej sporiteľne, ktorá mu má pomôcť zrýchliť rast a otvoriť dvere k ďalšej expanzii. Celkovo ide už o šiesty zainvestovaný startup v portfóliu Seed Startera. Miesto dní iba sekundy. Iba toľko dnes trvá analýza, ktorá odporučí, či sa oplatí kúpiť nehnuteľnosť. A to vďaka platforme IntellCRE, ktorá funguje na báze umelej inteligencie a umožňuje investorom, agentom aj analytikom nájsť, analyzovať a realizovať obchody s nehnuteľnosť ...

... trh sveta – Spojené štáty. S jasnou víziou, silným produktom a odvahou ísť do rizika. Práve preto teraz získava investíciu vo výške 400 000 eur od Seed Startera Slovenskej sporit
… [3311 more characters]
```
</details>

→ `WebSearch` "Seed Starter" Slovenskej sporiteľne portfólio startupy SmartHead IntellCRE Webout

<details><summary>result</summary>

```
Web search results for query: ""Seed Starter" Slovenskej sporiteľne portfólio startupy SmartHead IntellCRE Webout"

Links: [{"title":"Michal a Karel získali 1,65 milióna eur. Teraz s revolučným nápadom mieria do Silicon Valley","url":"https://www.startitup.sk/?p=1207932"},{"title":"Seed Starter Slovenskej sporiteľne hlási prvú investíciu: podporil slovenský startup SmartHead","url":"https://sita.sk/seed-starter-slovenskej-sporitelne-hlasi-prvu-investiciu-podporil-slovensky-startup-smarthead/"},{"title":"slsp infografika 2025","url":"https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/Aktuality/slsp-infografika-2025.pdf"},{"title":"slsp infografika 1q 2026","url":"https://cdn.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/Aktuality/slsp-infografika-1q-2026.pdf"},{"title":"Šéf Slovenskej sporiteľne: Slovensko by malo skvalitniť školstvo. Naša ekonomika má zásadný problém","url":"https://www.startitup.sk/?p=676083"},{"title":"Investice do startupů po vzoru České spořitelny přebírá další země. Banka jim zatím poslala 180 milionů","url":"https://cc.cz/investice-do-startupu-po-vzoru-ceske-sporitelny-prebira-dalsi-zeme-banka-jim-zatim-poslala-180-milionu/"},{"title":"slsp infographic 2025 english","url":"https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/en/aktuality/slsp-infographic-2025-english.pdf"},{"title":"Investice do dobra. Startup, který pomáhá firmám s udržitelností, získal skoro 24 milionů","url":"https://cc.cz/investice-do-dobra-startup-ktery-pomaha-firm
… [1597 more characters]
```
</details>

→ `Bash` — Fetch SLSP infographic PDFs and find Seed Starter portfolio
```sh
cd [redacted: local path] && PY=[redacted: local path] U=https://cdn.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/Aktuality/slsp-infografika-1q-2026.pdf; $PY bin/get.py $U https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/en/aktuality/slsp-infographic-2025-english.pdf; $PY bin/grep.py $U "Seed Starter|Blockmate" 300 | head -5; $PY bin/grep.py https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/en/aktuality/slsp-infographic-2025-english.pdf "Seed Starter|Blockmate" 300 | head -4
```

<details><summary>result</summary>

```
[redacted: local path]  200 application/pdf https://cdn.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/Aktuality/slsp-infografika-1q-2026.pdf  len=2151
[redacted: local path]  200 application/pdf https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/en/aktuality/slsp-infographic-2025-english.pdf  len=2285
... čný partner Banka roka Magazín Global Finance udelil Slovenskej sporiteľni ocenenie Best Bank 2026. 200 rokov Najväčšia slovenská banka oslávila v 2025 okrúhle výročie založenia. 250-tisíc eur Startup Cultiwise, absolútny víťaz Startup Awards 2025, získal prísľub rokovať o investícii 250 000 eur od Seed Starter Slovenskej sporiteľne. Najlepšia CSR banka Ocenenie získala sporiteľňa od prestížneho maga- zínu Euromoney. Dostupnejšie bankovníctvo Slovenská sporiteľňa prináša do všetkých pobočiek tlmočenie do posunkového jazyka. Technológie umožňujú ľuďom spravovať svoje financie pohodlne a bez obmedzení. 151, ...

... le s aplikáciou George. Smart Banka 2025 George obhájil titul najlepšej bankovej apky na Slovensku. Sme odlišní od iných bánk 1. V rebríčku najzamestnávateľ sa opäť umiestnila ako najlepšia banka. 749 bankomatov vrátane 294 vkladomatov. Ide o najväčšiu sieť na Slovensku. 3,14 milióna eur investoval Seed Starter Slovenskej sporiteľne za 3 roky do siedmich sloven- ských startupov – Blockmate, Smart- Head, Vestberry, Eatster, Resitech, IntellCRE a Pointee. Potvrdi
… [1998 more characters]
```
</details>

→ `Bash` — Fetch Baryon Fund site
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://baryon.fund/ https://www.baryon.fund/portfolio; $PY bin/show.py https://baryon.fund/ 0 4000
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=utf-8 https://www.baryon.fund/  len=7621
[redacted: local path]  404 text/html; charset=utf-8 https://www.baryon.fund/portfolio  len=88
Baryon fund | team | mission | advisory board | portfolio | investment focus | Contact | Closer to the Frontline. Closer to the Founder. | We defend Europe by backing bold defence tech entrepreneurs | Our team | Since 2015, Martin has served as Co-Founder, Chairman, and Head of R&D at SEC Technologies, leading global business development and advancing complex R&D. An active angel investor since 2014, he has supported ventures in defence, biotech, and tech, including SliDo (acquired by Cisco), Staffino, and Zdroje Zeme. | Martin Vaľovský | Serial angel investor and entrepreneur | Since 2015, Martin has served as Co-Founder, Chairman, and Head of R&D at SEC Technologies, leading global business development and advancing complex R&D. An active angel investor since 2014, he has supported ventures in defense, biotech, and tech, including SliDo (acquired by Cisco), Staffino, and Zdroje Zeme. | Since 2015, as co-founder and CEO of SEC Technologies, Michal has led international business development and established defence manufacturing in hardware, optics, and electronics. Previously, he worked in high-tech M&A at McKinsey & Company. He holds a PhD in signal processing from Vienna University of Technology, wit
… [2779 more characters]
```
</details>

→ `Bash` — Show rest of Baryon homepage
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://baryon.fund/ 4000 8000
```

<details><summary>result</summary>

```
gh-assurance cybersecurity to governments and defence | David Cullin | Former CTO of FLIR and former vice-president of Teledyne FLIR Defence Group | Susan E. Walton | Susan E. Walton is a globally recognized investment research leader and senior advisor with a powerful international network spanning finance, geopolitics, and national security | Oleksii Reznikov | Former Minister of Defence of Ukraine | Portfolio | Modular drone hardware platform. | Domain: UAV | Battlefield-proven UAV & fixed-wing developer. | Domain: UAV | Investment Focus | BARYON's investment focus is the air, sea, space, and the enabling technology beneath them, not a generalist dual-use thesis, but a deliberate focus on where we believe the greatest impact lies. | Securing the skies and shores of Europe, from its Eastern Flank to its Northern edge. | Contact us | For other inquiries, you can contact Michal Šimko directly via email at | [redacted: email address] | Please send your PDF pitch deck to us at | [redacted: email address] | Our team | Mission | Advisory board | Portfolio | Investment Focus | Contact | © 2024 Baryon | All rights reserved | Privacy Policy | Terms and Conditions | The European Commission’s Sustainable Action Plan has three objectives: (1) To reorient capital flows towards sustainable investment in order to achieve sustainable and inclusive growth; (2) To manage financial risks stemming from climate change, environmental degradation, and social issues; and (3) To foster transparency and long
… [2267 more characters]
```
</details>

→ `WebSearch` "Baryon Fund" OR "BARYON" defence fund investment 2026 Šimko Vaľovský

<details><summary>result</summary>

```
Web search results for query: ""Baryon Fund" OR "BARYON" defence fund investment 2026 Šimko Vaľovský"

Links: [{"title":"baryon fund","url":"https://superscout.co/investor/baryon-fund"},{"title":"Marek Macko","url":"https://sk.linkedin.com/in/marekmacko"},{"title":"Angels Partners logo","url":"https://angelspartners.com/firm/BaryonFund"},{"title":"Martin Valovsky","url":"https://sk.linkedin.com/in/martin-valovsky"},{"title":"www.openvc.app","url":"https://www.openvc.app/fund/Baryon%20Fund"},{"title":"ભારતમાં શ્રેષ્ઠ ડિફેન્સ સેક્ટર મ્યુચ્યુઅલ ફંડ 2026","url":"https://www.5paisa.com/gujarati/blog/defence-sector-mutual-funds-india"},{"title":"Michal Simko","url":"https://sk.linkedin.com/in/michal-simko-b89b0117"},{"title":"best defence mutual funds in india for april 2026 aditya birla sl fund hdfc defence fund and more","url":"https://www.angelone.in/news/hindi/mutual-funds/best-defence-mutual-funds-in-india-for-april-2026-aditya-birla-sl-fund-hdfc-defence-fund-and-more"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/na-obranu-by-mali-ist-dve-percenta-hd/912274-clanok.html"}]

The search didn't turn up a specific 2026 investment by Baryon Fund involving Šimko or Vaľovský. The results describe the fund and its people, plus one 2026 event appearance.

- **Profile:** Investor listings describe Baryon as an early-stage VC firm, investing in defence-tech and dual-use scaleups. Its typical check size is $500,000 to $5,000,0
… [1241 more characters]
```
</details>

→ `WebSearch` Seed Starter České spořitelny portfolio investice 2025 2026 startup Born Digital Daytrip

<details><summary>result</summary>

```
Web search results for query: "Seed Starter České spořitelny portfolio investice 2025 2026 startup Born Digital Daytrip"

Links: [{"title":"Slovenská spořitelna bude investovat do startupů po vzoru České. Připravených má přes 120 milionů","url":"https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"},{"title":"Trh je plný rychle umírajících projektů a plýtvá se penězi, říká Medek z České spořitelny, která to chce změnit","url":"https://cc.cz/trh-je-plny-rychle-umirajicich-projektu-a-plytva-se-penezi-rika-medek-z-ceske-sporitelny-ktera-to-chce-zmenit/"},{"title":"Investice do startupů po vzoru České spořitelny přebírá další země. Banka jim zatím poslala 180 milionů","url":"https://cc.cz/investice-do-startupu-po-vzoru-ceske-sporitelny-prebira-dalsi-zeme-banka-jim-zatim-poslala-180-milionu/"},{"title":"Česká spořitelna chce, aby investoři více vydělávali. Investuje do slovenského startupu, který to řeší","url":"https://cc.cz/ceska-sporitelna-chce-aby-investori-vice-vydelavali-investuje-do-slovenskeho-startupu-ktery-to-resi/"},{"title":"Česká spořitelna rozběhla investice do startupů. Na Bootcampu jim ukáže, kde dělají největší chyby","url":"https://cc.cz/ceska-sporitelna-rozbehla-investice-do-startupu-na-bootcampu-jim-ukaze-kde-delaji-nejvetsi-chyby/"},{"title":"Seed starter","url":"https://cc.cz/tag/seed-starter/"},{"title":"Přidání názoru","url":"https://www.mesec.cz/aktuality/ceska-sporitelna-spousti-investicni-progra
… [1620 more characters]
```
</details>

→ `Bash` — Fetch Caplight and CzechCrunch pages for Seed Starter deals
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.caplight.com/investor/seedstarter https://cc.cz/ceska-sporitelna-chce-aby-investori-vice-vydelavali-investuje-do-slovenskeho-startupu-ktery-to-resi/; $PY bin/grep.py https://www.caplight.com/investor/seedstarter "20(2[3-6])" 120 | head -30
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=utf-8 https://www.caplight.com/investor/seedstarter  len=2736
[redacted: local path]  200 text/html; charset=UTF-8 https://cc.cz/ceska-sporitelna-chce-aby-investori-vice-vydelavali-investuje-do-slovenskeho-startupu-ktery-to-resi/  len=8388
... . Portfolio Companies 5 Website seedstarter.cz Investments Seed Starter investments Company Date Stage Lead Definic Jun 2026 Seed Co-investor Repsense Dec 2025 Seed Lead Vestberry Mar 2025 Seed Lead Born Digital Dec 2023 Seed Co-investor Blockm ...

... dstarter.cz Investments Seed Starter investments Company Date Stage Lead Definic Jun 2026 Seed Co-investor Repsense Dec 2025 Seed Lead Vestberry Mar 2025 Seed Lead Born Digital Dec 2023 Seed Co-investor Blockmate Sep 2023 Seed Lead Sector & Sta ...

... Starter investments Company Date Stage Lead Definic Jun 2026 Seed Co-investor Repsense Dec 2025 Seed Lead Vestberry Mar 2025 Seed Lead Born Digital Dec 2023 Seed Co-investor Blockmate Sep 2023 Seed Lead Sector & Stage Mix Industry, funding stag ...

...  Stage Lead Definic Jun 2026 Seed Co-investor Repsense Dec 2025 Seed Lead Vestberry Mar 2025 Seed Lead Born Digital Dec 2023 Seed Co-investor Blockmate Sep 2023 Seed Lead Sector & Stage Mix Industry, funding stage, and valuation band breakdowns ...

... -investor Repsense Dec 2025 Seed Lead Vestberry Mar 2025 Seed Lead Born Digital Dec 2023 Seed Co-
… [1265 more characters]
```
</details>

→ `WebSearch` Repsense investment "Seed Starter" Česká spořitelna

→ `WebSearch` Vestberry funding round 2025 "Seed Starter" Česká spořitelna press release

<details><summary>result</summary>

```
Web search results for query: "Vestberry funding round 2025 "Seed Starter" Česká spořitelna press release"

Links: [{"title":"Slovak fintech Vestberry secures €2.2M to improve VC fund management in the US","url":"https://en.ain.ua/2025/03/14/slovak-fintech-vestberry-secures-eur22m"},{"title":"18F41C70 A422 4B46 89FF 021491BDC513","url":"https://funding.tech.eu/companies/18F41C70-A422-4B46-89FF-021491BDC513"},{"title":"seed 2025 03","url":"https://seedtable.com/companies/vestberry/funding-rounds/seed-2025-03"},{"title":"startup vestberry ziskal 22 milionu eur pomuze to jeho expanzi do usa","url":"https://cc.cz/live/startup-vestberry-ziskal-22-milionu-eur-pomuze-to-jeho-expanzi-do-usa/"},{"title":"Total Raised","url":"https://www.cbinsights.com/company/vestberry/financials"},{"title":"top of page","url":"https://www.symsite.sk/single-post/slovak-fintech-vestberry-raised-2-2m-from-investors"},{"title":"Subscribe to Our Newsletter","url":"https://www.thesaasnews.com/news/vestberry-raises-2-2-million-in-funding/"},{"title":"Česká spořitelna chce, aby investoři více vydělávali. Investuje do slovenského startupu, který to řeší","url":"https://cc.cz/ceska-sporitelna-chce-aby-investori-vice-vydelavali-investuje-do-slovenskeho-startupu-ktery-to-resi/"},{"title":"488CB289 2EF6 4B49 ABEE 2D8BD829386B","url":"https://funding.tech.eu/deals/488CB289-2EF6-4B49-ABEE-2D8BD829386B"}]

The March 2025 round was €2.2 million (about 55 million CZK), led by Seed Starter, the venture program of Česká
… [1387 more characters]
```
</details>

<details><summary>result</summary>

```
Web search results for query: "Repsense investment "Seed Starter" Česká spořitelna"

Links: [{"title":"Nové peníze oznámil „Havel“, nástroj na analýzu dezinformací, který roste i z Prahy. Pracuje mimo jiné pro NATO","url":"https://www.lupa.cz/aktuality/nove-penize-oznamil-havel-nastroj-na-analyzu-dezinformaci-ktery-roste-i-z-prahy-pracuje-mimo-jine-pro-nato/"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/lithuanian-startup-repsense-raises-2m-to-accelerate-european-expansion"},{"title":"analyzuji dezinformace pro nato litevcum ted tensor ventures a seed starter posilaji milion eur","url":"https://forbes.cz/analyzuji-dezinformace-pro-nato-litevcum-ted-tensor-ventures-a-seed-starter-posilaji-milion-eur/"},{"title":"Jejich nástroj Havel pomáhá i v NATO. Do Litevců teď investují Tensor Ventures a Česká spořitelna","url":"https://cc.cz/jejich-nastroj-havel-pomaha-i-v-nato-do-litevcu-ted-investuji-tensor-ventures-a-ceska-sporitelna/"},{"title":"Petr Kopeček","url":"https://cz.linkedin.com/in/petrkopecek1"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/seed-starter-ceske-sportielny"},{"title":"triniti jurex advised lead investors on eur 2 mln investment into repsense","url":"https://triniti.eu/experience/triniti-jurex-advised-lead-investors-on-eur-2-mln-investment-into-repsense/"},{"title":"triniti.eu","url":"https://triniti.eu/?p=36282"},{"title":"Česká spořitelna","url":"https://www.finmag.cz/tema/ceska-sporitelna"},{"titl
… [2159 more characters]
```
</details>

→ `Bash` — Inspect Seed Starter portfolio logos markup
```sh
cd [redacted: local path] && grep -o -i -E '(data-[a-z-]+|src|href|alt|title)="[^"]*(portfol|logo|startup)[^"]*"' pages/8995d79dd8581eab.raw | head -20; grep -c -i "img" pages/8995d79dd8581eab.raw; grep -o -i 'cdn[^"]*\.\(png\|svg\|jpg\)' pages/8995d79dd8581eab.raw | sort -u | head -30
```

<details><summary>result</summary>

```
data-cid="portfolio"
3
cdn.erstegroup.com/content/dam/common/brand/icons/do-not-use-anymore/bright-blue/icon-calendar-clock.svg
cdn.erstegroup.com/content/dam/common/brand/icons/do-not-use-anymore/bright-blue/icon-currency-euro-money.svg
cdn.erstegroup.com/content/dam/common/brand/icons/do-not-use-anymore/bright-blue/icon-file-text-list.svg
cdn.erstegroup.com/content/dam/common/brand/icons/do-not-use-anymore/bright-blue/icon-travel-map-earth.svg
cdn.erstegroup.com/content/dam/cz/csas/kariera_csas_cz/obrazky/[redacted: email address]
cdn.erstegroup.com/content/dam/cz/csas/www_csas_cz/obrazky/ikony/favicon-touch.png
cdn.erstegroup.com/content/dam/cz/csas/www_csas_cz/obrazky/ikony/ico-facebook.svg
cdn.erstegroup.com/content/dam/cz/csas/www_csas_cz/obrazky/ikony/ico-linkedin.svg
cdn.erstegroup.com/content/dam/cz/csas/www_seedstarter_cz/seedstarter/CZ-SeedStarter_Logo_screen_white_new.svg
cdn.erstegroup.com/content/dam/cz/csas/www_seedstarter_cz/seedstarter/globe.png
cdn.erstegroup.com/content/dam/cz/csas/www_seedstarter_cz/seedstarter/linkedin.png
cdn.erstegroup.com/content/dam/cz/csas/www_seedstarter_cz/seedstarter/seedstarter-logo.svg
cdn.erstegroup.com/content/dam/cz/csas/www_seedstarter_cz/seedstarter/streamline-icon-interface-file-text@48x48.SVG
cdn.erstegroup.com/content/dam/cz/csas/www_seedstarter_cz/seedstarter/streamline-icon-interface-hand-gestures-praying-hands.svg
cdn.erstegroup.com/content/dam/cz/csas/www_seedstarter_cz/seedstarter/streamline-i
… [1775 more characters]
```
</details>

→ `WebSearch` csas.cz tisková zpráva Seed Starter investuje portfolio startupů Investown Signi Wflow Born Digital Vestberry

<details><summary>result</summary>

```
Web search results for query: "csas.cz tisková zpráva Seed Starter investuje portfolio startupů Investown Signi Wflow Born Digital Vestberry"

Links: [{"title":"Hlavní obsah","url":"https://seznamzpravy.cz/clanek/ekonomika-byznys-rozhovory-inkubator-neni-jen-pro-novorozence-sporitelna-jde-s-tim-svym-do-rumunska-239108"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/239108"},{"title":"Přidání názoru","url":"https://www.mesec.cz/aktuality/ceska-sporitelna-spousti-investicni-program-seed-starter-orientovany-na-start-upy/pridat"},{"title":"seed starter","url":"https://insights.munich-startup.de/companies/seed_starter"},{"title":"Rozhovor: Jak může začínajícím startupům pomoci Česká spořitelna?","url":"https://www.finance.cz/541902-seed-starter-cs"},{"title":"Rozhovor: Jak může začínajícím startupům pomoci Česká spořitelna?","url":"https://www.finance.cz/clanky/541902-seed-starter-cs/"},{"title":"startupy jejich reseni by mela zajimat i korporaty veri tomas milota ze seed starter cs","url":"https://forbes.cz/startupy-jejich-reseni-by-mela-zajimat-i-korporaty-veri-tomas-milota-ze-seed-starter-cs/"},{"title":"Rozhovor: Jak může začínajícím startupům pomoci Česká spořitelna?","url":"https://www.finance.cz/541902-rozhovor-jak-muze-zacinajicim-startupum-pomoci-ceska-sporitelna"},{"title":"Seed Starter ČS","url":"https://unicorn-nest.com/funds/seed-starter-cs/"}]

I didn't find the official csas.cz press release. The results are press and databases that mention the S
… [1345 more characters]
```
</details>

→ `WebSearch` "Seed Starter" site:csas.cz

<details><summary>result</summary>

```
Web search results for query: ""Seed Starter" site:csas.cz"

Links: [{"title":"Seed Starter Toolkit","url":"https://www.lindenhurstlibrary.org/library-things/seed-starter-tool-kit"},{"title":"9+ Easy How to Seed Starter Tips & Tricks","url":"https://checklist.atameken.kz/?p=2210"},{"title":"New Seed-Starters Handbook","url":"https://ecologycenter.org/library/library-entries/new-seed-starters-handbook/"},{"title":"Plant starter","url":"https://patents.justia.com/patent/4051625"},{"title":"44712 lee valley windowsill seed starter","url":"https://www.leevalley.com/en-gb/shop/garden/planting/propagation/seed-starting/44712-lee-valley-windowsill-seed-starter"},{"title":"Specials & Offers","url":"https://homedepot.com/b/Outdoors-Garden-Center-Plant-Seeds-Seed-Starters/Cell-Flats/N-5yc1vZc8qsZ1z175s1"},{"title":"← Zpět na Tech News","url":"https://www.marigold.cz/tech-news-archive/2025-12-03/letpot-launches-ss-pro-smart-seed-starter-on-kicks"},{"title":"#1 Home Improvement Retailer","url":"https://homedepot.com/p/Vermont-Organics-Reclamation-Soil-10-Qt-Organic-Seed-Starter-OSS10QT/204894890"},{"title":"wattersgardencenter.com","url":"https://wattersgardencenter.com/?p=4682"}]

The search returned no results from csas.cz. The site filter doesn't seem to have been applied, so every hit came from other domains.

The only Czech-language result is from marigold.cz, a tech news site, not csas.cz. It reports that LetPot has launched its SS-Pro Smart Seed Starter on Kickstarter, which is a
… [543 more characters]
```
</details>

→ `Bash` — Search ORSR for Vestberry
```sh
cd [redacted: local path] && UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"; curl -sL --max-time 30 -A "$UA" "https://www.orsr.sk/hladaj_subjekt.asp?OBMENO=Vestberry&PF=0&R=on" -o orsr_v.html; iconv -f windows-1250 -t utf-8 orsr_v.html | grep -o 'vypis.asp?ID=[0-9]*&SID=[0-9]*&P=[0-9]' | sort -u
```

<details><summary>result</summary>

```
(Bash completed with no output)
```
</details>

→ `Bash` — Retry ORSR search for Vestberry
```sh
cd [redacted: local path] && head -c 1500 orsr_v.html | iconv -f windows-1250 -t utf-8; UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"; curl -sL --max-time 30 -A "$UA" "https://www.orsr.sk/hladaj_subjekt.asp?OBMENO=VESTBERRY&PF=0&SID=0&R=on" | iconv -f windows-1250 -t utf-8 | grep -o 'vypis.asp[^"]*' | head
```

<details><summary>result</summary>

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang ="sk">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1250">
<meta http-equiv="Content-Language" content="sk">
<META NAME="Authors" CONTENT="Harman, Trník, Balog, Gáborčík, Rácik D">
<meta name="Description" content="Obchodný register Slovenskej Republiky na Internete - vyhľadávanie podľa obchodného mena subjektu.">
<title>Obchodný register SR - Výsledky vyhľadávania podľa obchodného mena subjektu</title>
<link rel="stylesheet" href="inc/styleS.css" type="text/css">
</head>
<body bgcolor="#FFFFFF" text="#000000" link="#000066">
<table border="0" width="100%" cellpadding="3" cellspacing="0">
<tr>
        <td width="100">
                <a href="default.asp"><img border="0" src="images/znak50.gif" alt="Hlavná stránka" title="Hlavná stránka" width="60" height="70"></a>
        </td>
        <td>
                <div align="center" class="min">
                <a href="https://www.justice.gov.sk" class="link">MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY</a>
                </div>
                <h2 align="center" class="reg">OBCHODNÝ REGISTER<br><span class="int">NA INTERNETE</span></h2>
        <br>
        <div align="center" class="min">
        <a href="default.asp" class="link">
            Slovensky<img src="images\slovak_flag_8.jpg" alt="Slovensky" title="Slovensky" width="24" height="14" border="0"></a> |
                <!-- <a href="default.asp?lan=en" cvypi
… [337 more characters]
```
</details>

→ `Bash` — Fetch Vestberry ORSR extracts, find investors
```sh
cd [redacted: local path] && PY=[redacted: local path] for id in 641731 773692 439172; do U="https://www.orsr.sk/vypis.asp?ID=$id&SID=2&P=0"; $PY bin/get.py "$U" >/dev/null; echo "== $id"; $PY bin/show.py "$U" 0 300; echo; $PY bin/grep.py "$U" "Seed Starter|Venture to Future|ZGC|Zero Gravity|0100" 200 | head -8; done
```

<details><summary>result</summary>

```
== 641731
Výpis z obchodného registra SR | MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY | OBCHODNÝ REGISTER | NA INTERNETE | Slovensky | | | English | Výpis z Obchodného registra Mestského súdu Bratislava III | Tento výpis má len informatívny charakter a nie je použiteľný pre právne úkony! | Zobraziť na n

[0 matches, meta=['200 text/html https://www.orsr.sk/vypis.asp?ID=641731&SID=2&P=0']]
== 773692
Výpis z obchodného registra SR | MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY | OBCHODNÝ REGISTER | NA INTERNETE | Slovensky | | | English | Výpis z Obchodného registra Mestského súdu Bratislava III | Tento výpis má len informatívny charakter a nie je použiteľný pre právne úkony! | Zobraziť na n

[0 matches, meta=['200 text/html https://www.orsr.sk/vypis.asp?ID=773692&SID=2&P=0']]
== 439172
Výpis z obchodného registra SR | MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY | OBCHODNÝ REGISTER | NA INTERNETE | Slovensky | | | English | Výpis z Obchodného registra Mestského súdu Bratislava III | Tento výpis má len informatívny charakter a nie je použiteľný pre právne úkony! | Zobraziť na n

[0 matches, meta=['200 text/html https://www.orsr.sk/vypis.asp?ID=439172&SID=2&P=0']]
```
</details>

→ `Bash` — Show company names and shareholders from ORSR
```sh
cd [redacted: local path] && PY=[redacted: local path] for id in 641731 773692 439172; do U="https://www.orsr.sk/vypis.asp?ID=$id&SID=2&P=0"; echo "== $id"; $PY bin/grep.py "$U" "Obchodné meno|Spoločníci|Akcionár" 400 | head -6; done
```

<details><summary>result</summary>

```
== 641731
... Výpis z obchodného registra SR MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY OBCHODNÝ REGISTER NA INTERNETE Slovensky | English Výpis z Obchodného registra Mestského súdu Bratislava III Tento výpis má len informatívny charakter a nie je použiteľný pre právne úkony! Zobraziť na novej verzii portálu Oddiel: Sja Vložka číslo: 238/B Obchodné meno: Vestberry Holding, j. s. a. (od: 08.11.2022) Sídlo: Staré Grunty 18 Bratislava - mestská časť Karlova Ves 841 04 (od: 17.04.2024) IČO: 54 903 742 (od: 08.11.2022) Deň zápisu: 08.11.2022 (od: 08.11.2022) Právna forma: Jednoduchá spoločnosť na akcie (od: 08.11.2022) Predmet podnikania (činnosti): počítačové služby a služby súvisiace s počítačovým spracovaním údajov (od: 08.11.2022) výskum a vývoj  ...

[1 matches, meta=['200 text/html https://www.orsr.sk/vypis.asp?ID=641731&SID=2&P=0']]
== 773692
... Výpis z obchodného registra SR MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY OBCHODNÝ REGISTER NA INTERNETE Slovensky | English Výpis z Obchodného registra Mestského súdu Bratislava III Tento výpis má len informatívny charakter a nie je použiteľný pre právne úkony! Zobraziť na novej verzii portálu Oddiel: Sja Vložka číslo: 489/B Obchodné meno: Vestberry Team, j. s. a. (od: 15.09.2026) Sídlo: Staré Grunty 6347/18 Bratislava - mestská časť Karlova Ves 841 04 (od: 15.09.2026) IČO: 57 898 987 (od: 15.09.2026) Deň zápisu: 15.09.2026 (od: 15.09.2026) Právna forma: Jednoduchá spoločnosť na akcie (od: 15.09.2026) Predmet podnikani
… [2699 more characters]
```
</details>

→ `Bash` — Probe Seed Starter portfolio URLs and Vestberry news
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.seedstarter.cz/en/portfolio https://www.seedstarter.cz/cs/portfolio https://www.seedstarter.cz/cs/home https://www.vestberry.com/blog https://www.vestberry.com/news 2>&1 | grep -v REPLACE; $PY bin/grep.py https://www.seedstarter.cz/cs/home "Born|Vestberry|Blockmate|Pointee|Investown" 100 | tail -3
```

<details><summary>result</summary>

```
[redacted: local path]  404 text/html; charset=utf-8 https://www.seedstarter.cz/en/portfolio  len=154
[redacted: local path]  404 text/html; charset=utf-8 https://www.seedstarter.cz/cs/portfolio  len=111
[redacted: local path]  404 text/html; charset=utf-8 https://www.seedstarter.cz/cs/home  len=111
[redacted: local path]  200 text/html; charset=utf-8 https://vestberry.com/blog  len=3917
[redacted: local path]  404 text/html; charset=utf-8 https://vestberry.com/news  len=93
[0 matches, meta=['404 text/html; charset=utf-8 https://www.seedstarter.cz/cs/home']]
```
</details>

→ `Bash` — Look for Vestberry funding post
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://vestberry.com/blog 0 2500; grep -o 'href="[^"]*"' pages/e975c4c2411f26d8.raw | grep -i -E "fund|rais|seed|invest|2-2|million" | head
```

<details><summary>result</summary>

```
Vestberry Blog | VC Insights & Portfolio Management | Blog | Vestberry Resources | Category | Heading | Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros elementum tristique. Duis cursus, mi quis viverra ornare, eros dolor interdum nulla, ut commodo diam libero vitae erat. Aenean faucibus nibh et justo cursus id rutrum lorem imperdiet. Nunc ut sem vitae risus tristique posuere. | Author | 3 | 3 | min read | Product updates | Introducing Tony: Vestberry's AI for Venture Capital | June 1, 2026 | · | 8 | min read | Events | From Intuition to Infrastructure: How European VCs Are Building Data‑Driven Operating Models | January 31, 2026 | · | 8 | min read | Latest news | Stay up to date with the latest news and updates from Vestberry | All | Product updates | Events | Industry Insights | Thank you! Your submission has been received! | Oops! Something went wrong while submitting the form. | Industry Insights | Should Your VC Fund Vibe-Code Its Own Portfolio Monitoring Software in 2026? | Vibe-coding a portfolio dashboard takes a weekend. Running a fund on one is a different question. A build-vs-buy guide for VC CFOs, GPs, and portfolio managers. | Vestberry | August 4, 2026 | 8 | min read | Industry Insights | Vestberry vs. Excel: When Spreadsheets Stop Working for VC Fund Data | Lost files, no audit trail, version chaos: why VC funds outgrow Excel, when it's time to switch, and how a single source of truth changes decisions. | Vestberry | July
… [1169 more characters]
```
</details>

→ `Bash` — Fetch Startguide site pages
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://startguide.cz/en/ https://startguide.cz/ https://startguide.cz/en/portfolio/ https://startguide.cz/portfolio/; $PY bin/show.py https://startguide.cz/en/ 0 3000
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=utf-8 https://startguide.cz/en/  len=3864
[redacted: local path]  200 text/html; charset=utf-8 https://startguide.cz/  len=3878
[redacted: local path]  200 text/html; charset=utf-8 https://startguide.cz/en/portfolio/  len=3878
[redacted: local path]  200 text/html; charset=utf-8 https://startguide.cz/portfolio/  len=3878
STARTGUIDE – We’ll guide you onto the right path | We empower digital startups | to create value and drive positive change. | Enterprenerues investing in early‑stage digital startups in the CEE region. We are bringing hands‑on unique value. | Discover the way | Contact us | About us | STARTGUIDE is a | venture capital fund | that invests with a hands‑on approach, bringing | added value | to investors, startups, and partners. | STARTGUIDE's unique approach combines financial investment with | strategic mentorship and network access | . | At STARTGUIDE, we bring | more than just capital to the table | . Our hands-on approach includes deep collaboration with startup founders on strategy, product-market fit, and scaling their business to achieve market leadership. | Our investment philosophy goes beyond financial returns, prioritizing innovation, execution, and growth | . | We are a financial investor but for selected startups a
… [2062 more characters]
```
</details>

→ `Bash` — Check Startguide portfolio mentions and links
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://startguide.cz/en/ 3000 4000; grep -o -i -E 'alt="[^"]+"|carebot|ringil' pages/b0ea236560707852.raw | sort | uniq -c | head -20; grep -o 'href="[^"]*"' pages/b0ea236560707852.raw | sort -u | head -30
```

<details><summary>result</summary>

```
ams, Up to 35% of our fund includes female founders | , who are driving digital transformation and AI innovation. We believe these areas have substantial potential for growth and disruption. We seek to partner with startups capable of executing effectively, utilizing breakthrough technologies, and delivering market-driven solutions that revolutionize industries and enhance quality of life. | Which helps business and people to be more effective | Market‑Driven | Solutions | DIGITAL | TRANSFORMATION | / AI INNOVATIONS | Which breaks new ground in standard industries | Transformation‑Driven | Solutions | Which make customer’s life easier | Users‑Driven | Solutions | Contact | Are you a startup? Are you a fund? | Please make an appointment with us so that we can start our journey together. | [redacted: email address] | Address | Start Guide, s.r.o., Opletalova 1015/55, Nové Město, 110 00 Praha 1 | Identification number | : 28418425 | Back to top | This website does not use cookies. | Copyright
href="/_nuxt/BcMqlqRe.js"
href="/_nuxt/BDw61n7h.js"
href="/_nuxt/BiNNMZ9q.js"
href="/_nuxt/C19QRmIg.js"
href="/_nuxt/d0TfLoZs.js"
href="/_nuxt/Footer.DiWGtssM.css"
href="/_nuxt/jdRToexg.js"
href="/_nuxt/v3LzWKjp.js"
href="/"
href="/en/_payload.json?_b=84c36fa3-dc9e-4fa0-9c1d-3d0f4176685c"
href="/en/"
href="/en/#about"
href="/en/#contact"
href="/en/#investment"
href="/en/sgone/"
href="/en/sgone/#references"
href="/en/sgtwo/"
href="/en/sgtwo/#team"
href="/images/favicon.png"
href="#"
href="#about
… [108 more characters]
```
</details>

→ `Bash` — Fetch Startguide SG ONE fund page
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://startguide.cz/en/sgone/ https://startguide.cz/en/sgtwo/; $PY bin/show.py https://startguide.cz/en/sgone/ 0 4000
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=utf-8 https://startguide.cz/en/sgone/  len=4575
[redacted: local path]  200 text/html; charset=utf-8 https://startguide.cz/en/sgtwo/  len=4546
SGOne Fund | STARTGUIDE | Every success begins with the first step. | Let’s do it together. | Send an inquiry | A Fresh Fund for Fresh Ideas | EUR 6 000 000 | The fund is set up for EUR 6 mil. We‘ve already committed 30 %. | 7 YEARS | This is a 7‑year fund. We expect to meet the fund target in the next 18 months. | CEE REGION | We are mainly looking for projects in the CEE region. | We are primarily focused on the B2C segment, but also have companies in the B2B, smart tech or healthcare industry. | Conditions: | Ticket size is USD 50‑200,000 | | | Share size 1‑15 % | | | Length of stay 3‑7 years | We’ll Help You Get to the Top | We’re a bridge between angel investors and VC fund opportunities. | The new fund opens on 1 June 2022 and is looking for EUR 6 mil. | The closing date for investments is 1 May 2023; the fund will be open or 7 years. | In the end, we will have 50+ carefully selected projects. | We are investing cca EUR 100k in each project in the early stages. | We focus on projects in the CEE region, but already support projects across the EU. | Contact us if you would like to explore more of our vision and see our results. | Send an inquiry | Find an Experienced Guide to Lead the Way |
… [2786 more characters]
```
</details>

→ `Bash` — Check SG Two page for portfolio names
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/grep.py https://startguide.cz/en/sgtwo/ "Portfolio|Founder of" 200 | head -6
```

<details><summary>result</summary>

```
...  Transactions 20+ years in asset management Board roles at Conseq & QI investiční společnost Track record across acquisitions and exits Experience spanning both public and private markets Financial & Portfolio Management As board member of multiple investment companies was previously part of multiple investment funds, with experience in setting up the funds, operationally managing it, evaluating investment ...

[1 matches, meta=['200 text/html; charset=utf-8 https://startguide.cz/en/sgtwo/']]
```
</details>

→ `WebSearch` "GAIN Ventures" Praha investice startup Carebot

<details><summary>result</summary>

```
Web search results for query: ""GAIN Ventures" Praha investice startup Carebot"

Links: [{"title":"Česká umělá inteligence analyzuje rentgeny plic a míří do Evropy. Carebot zároveň získal investici","url":"https://cc.cz/ceska-umela-inteligence-analyzuje-rentgeny-plic-a-miri-do-evropy-carebot-zaroven-ziskal-investici/"},{"title":"cesko je maly rybnicek carebot ziskal novou investici a rozjizdi globalni ambice","url":"https://forbes.cz/cesko-je-maly-rybnicek-carebot-ziskal-novou-investici-a-rozjizdi-globalni-ambice/"},{"title":"Carebot pomáhá svou AI zachraňovat životy po světě. Nyní představuje řešení pro mamografii","url":"https://cnn.iprima.cz/carebot-pomaha-svou-ai-zachranovat-zivoty-po-celem-svete-nyni-predstavuje-reseni-pro-mamografii-518071"},{"title":"cesky carebot ziskal dosud nejvetsi investici a predstavil nove ai reseni","url":"https://forbes.cz/cesky-carebot-ziskal-dosud-nejvetsi-investici-a-predstavil-nove-ai-reseni/"},{"title":"Tvořili spolu hudbu, pak rozjeli startup, který odhaluje rakovinu. Teď zaujali „kočkopsa“ Matěje Turka","url":"https://cc.cz/tvorili-spolu-hudbu-pak-rozjeli-startup-ktery-odhaluje-rakovinu-ted-zaujali-kockopsa-mateje-turka/"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/carebot-receives-czk-15m-investment"},{"title":"cesky carebot ziskal dosud nejvetsi investici a predstavil nove ai reseni 2","url":"https://forbes.cz/email/cesky-carebot-ziskal-dosud-nejvetsi-investici-a-predstavil-nove-ai-reseni-2/"},{"title":"cz.lin
… [1688 more characters]
```
</details>

→ `WebSearch` BHM group Tomáš Krsek startupy portfolio Yieldigo Sharry Carebot BHM Ventures web

<details><summary>result</summary>

```
Web search results for query: "BHM group Tomáš Krsek startupy portfolio Yieldigo Sharry Carebot BHM Ventures web"

Links: [{"title":"Český miliardář chce v Evropě inovovat zdravotnictví. Už proto nakoupil německé, polské i britské firmy","url":"https://cc.cz/cesky-miliardar-chce-v-evrope-inovovat-zdravotnictvi-uz-proto-nakoupil-nemecke-polske-i-britske-firmy/"},{"title":"beze změny","url":"https://forbes.cz/lists/nc24/tomas-krsek/"},{"title":"Miliardář Krsek a Rubeš investují desítky milionů korun do českého startupu Feedyou","url":"https://cc.cz/miliardar-krsek-a-rubes-investuji-desitky-milionu-korun-do-ceskeho-startupu-feedyou/"},{"title":"Hlavní obsah","url":"https://seznamzpravy.cz/clanek/ekonomika-firmy-skupina-miliardare-krska-ma-na-nakupy-pripravene-miliardy-korun-254526"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/254526"},{"title":"Milionár Tomáš Kršek vstupuje do startupu, ktorý pomáha lekárom odhaliť rakovinu už v rannom štádiu","url":"https://www.startitup.sk/milionar-tomas-krsek-vstupuje-do-startupu-ktory-pomaha-lekarom-odhalit-rakovinu-uz-v-rannom-stadiu/"},{"title":"miliardar krsek ziskal podil ve startupu ktery pomoci ai odhaluje rakovinu","url":"https://www.newstream.cz/zpravy-z-firem/miliardar-krsek-ziskal-podil-ve-startupu-ktery-pomoci-ai-odhaluje-rakovinu"},{"title":"Milionár Tomáš Kršek vstupuje do startupu, ktorý pomáha lekárom odhaliť rakovinu už v rannom štádiu","url":"https://www.startitup.sk/?p=1113451"},{"title":"12 mld. korun
… [1634 more characters]
```
</details>

→ `Bash` — Probe candidate BHM group websites
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.bhmgroup.cz/ https://bhm.group/ https://www.bhm-group.com/ https://www.bhmgroup.eu/ 2>&1 | grep -v REPLACE
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://www.bhmgroup.eu/  len=2877
[redacted: local path]  000  https://bhm.group/  len=0
[redacted: local path]  302 text/html; charset=UTF-8 https://yfdabv8.com/?dn=www.bhm-group.com&accid=710956738&spfwd=1&spmsg=nschttp%3A504  len=0
[redacted: local path]  200 text/html; charset=UTF-8 https://www.bhmgroup.eu/  len=2877
```
</details>

→ `Bash` — Show BHM group site text and links
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://www.bhmgroup.cz/ 0 2900; grep -o 'href="[^"]*"' pages/6e7423d72acee1aa.raw | sort -u | grep -v -E "\.(css|js|png|svg|ico)" | head -30
```

<details><summary>result</summary>

```
ÚVOD - BHM Group | ÚVOD | O NÁS | LIDÉ | PORTFOLIO | PRESS ROOM | KARIÉRA | KONTAKTY | Naším posláním je investovat do firem a pomáhat je budovat tak, aby přinášely skutečnou hodnotu celé společnosti. Vytváříme produkty a služby, které lidem opravdu pomáhají — a protože nás to baví, děláme to s radostí! | Naším posláním je investovat do firem a pomáhat je budovat tak, aby přinášely skutečnou hodnotu celé společnosti. Vytváříme produkty a služby, které lidem opravdu pomáhají — a protože nás to baví, děláme to s radostí! | Strategické investice | BHM group je evropská investiční skupina, která řídí desítky společností napříč Evropou a aktivně podporuje jejich růst, inovace a expanzi na globální trhy. Nejsme jen investor — jsme strategický partner, který vytváří dlouhodobou hodnotu a otevírá nové příležitosti. | Zdravotnické technologie | BHM group investuje po celé Evropě do firem, které vyvíjejí a vyrábějí špičková řešení v oblasti zdravotnických technologií. Inovace, kvalita a budoucnost zdravotní péče — to je naše DNA. | www.reinsberg.com | Laboratorní technologie | BHM group spolupracuje s firmami, které poskytují mimořádná řešení v oblasti laboratorní infrastruktury. Preciznost, inovace a nejmodernější technologie — to je to, co nás pohání. | www.koettermanngroup.com | Obnovitelné zdroje | BHM group se v energetickém průmyslu soustředí na obnovitelné zdroje energie, akumulaci energie a vodíkové technologie. Udržitelnost, inovace a čistá energie — to je naše vize. | www.bhm
… [2353 more characters]
```
</details>

→ `Bash` — Fetch BHM tech-startup portfolio and BHM Ventures site
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py "https://www.bhmgroup.eu/portfolio?industry=tech-startups" https://www.bhmventures.eu/ https://www.bhmgroup.eu/novinky; $PY bin/show.py "https://www.bhmgroup.eu/portfolio?industry=tech-startups" 0 3000; echo; $PY bin/show.py https://www.bhmventures.eu/ 0 3000
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://www.bhmgroup.eu/portfolio?industry=tech-startups  len=5402
[redacted: local path]  000  https://www.bhmventures.eu/  len=0
[redacted: local path]  200 text/html; charset=UTF-8 https://www.bhmgroup.eu/novinky  len=3853
PORTFOLIO - BHM Group | ÚVOD | O NÁS | LIDÉ | PORTFOLIO | PRESS ROOM | KARIÉRA | KONTAKTY | NAŠE PORTFOLIO | BHM group spravuje aktiva v hodnotě 1 miliardy eur, působí ve více než 20 evropských zemích a zaměstnává přes 2000 lidí po celé Evropě. Skupina aktivně řídí více než 30 investic napříč různými odvětvími. Zde si můžete vyhledat více informací o portfoliu společnosti a projektech, do kterých investuje. | Filtrovat podle: | Všechny obory | MedTech | CleanTech | Renewables | Tech Startups | Hospitality | Residentials | Logistics | Ostatní | Všechny země | Czech Republic | Denmark | Estonia | Finland | Germany | Lithuania | Poland | Slovakia | Spain | Switzerland | United Kingdom | Tech Startups | Carebot | Tech Startups | Carebot | Carebot, český zdravotnicko-technologický startup, vyvinul software využívající umělou inteligenci k lokalizaci nálezů na rentgenových snímcích. Tento software propojuje znalosti expertů a lékařů. Primárně cílí na evropská zdravotnická zařízení, zejména nemocnice a radiologická oddělení. | Navštívit webové stránky | Zpět na přehle
… [1923 more characters]
```
</details>

→ `Bash` — Show rest of BHM tech-startups portfolio
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py "https://www.bhmgroup.eu/portfolio?industry=tech-startups" 3000 5500
```

<details><summary>result</summary>

```
inuté doplňky strany přirozeně zvyšují energii a zlepšují mentální výkon hráčů na té nejvyšší úrovni. | Navštívit webové stránky | Zpět na přehled portfolia | Tech Startups | Oddin | Tech Startups | Oddin | Oddin pomocí umělé inteligence předpovídá v reálném čase vývoj e-sportovních turnajů. Software predikuje herní události na základě dat z analýzy obrazu a pokročilé matematiky. Predikce dodává nejvýznamnějším světovým e-sportovním společnostem a mezinárodním sázkovým kancelářím. | Navštívit webové stránky | Zpět na přehled portfolia | Tech Startups | Persoo | Tech Startups | Persoo | Persoo je personalizační nástroj pro středně velké e-prodejce, který zvyšuje příjmy z elektronického obchodování bez dalších mediálních výdajů. Pomocí pokročilých matematických metod učení pomáhá Persoo personalizovat zákaznickou zkušenost. | Navštívit webové stránky | Zpět na přehled portfolia | Tech Startups | Ready Player Me | Tech Startups | Ready Player Me | Společnost Ready Player Me poskytuje vývojářům snadno integrovatelné nástroje pro tvorbu avatarů a vývojářské nástroje, které svým uživatelům poskytují vysoce personalizované postavy, které pomáhají zvýšit zapojení jejich uživatelů. Tyto avatary lze použít při virtuálních schůzkách, školení VR, hraní her nebo v metaversu. | Navštívit webové stránky | Zpět na přehled portfolia | Tech Startups | Sharry | Tech Startups | Sharry | Sharry je etablovaným hráčem na evropském PropTech trhu. Kancelářským budovám poskytuje technologie, které jej
… [999 more characters]
```
</details>

→ `Bash` — Check Carebot justice.cz extract for BHM/GAIN/Startguide
```sh
cd [redacted: local path] && PY=[redacted: local path] U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1124329&typ=UPLNY"; $PY bin/get.py "$U"; $PY bin/grep.py "$U" "BHM|GAIN|START GUIDE|Krsek|Kršek" 250 | head -12
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1124329&typ=UPLNY  len=14781
... ceno: 100 % Obchodní podíl: 1850/100000 Druh podílu: základní podíl zapsáno 19. prosince 2025 vymazáno 26. června 2026 Podíl: Vklad: 281 ,- Kč Splaceno: 100 % Obchodní podíl: 1791/100000 Druh podílu: základní podíl zapsáno 26. června 2026 Společník: START GUIDE ONE, a.s. , IČ: 173 23 126 Opletalova 1015/55, Nové Město, 110 00 Praha 1 zapsáno 18. března 2025 Podíl: Vklad: 744 ,- Kč Splaceno: 100 % Obchodní podíl: 4,91 % Druh podílu: základní podíl zapsáno 18. března 2025 vymazáno 19. prosince 2025 Podíl: Vk ...

... 35 655 Ovocný trh 1096/8, Staré Město, 110 00 Praha 1 zapsáno 18. března 2025 vymazáno 4. srpna 2025 Podíl: Vklad: 696 ,- Kč Splaceno: 100 % Obchodní podíl: 4,59 % Druh podílu: základní podíl zapsáno 18. března 2025 vymazáno 4. srpna 2025 Společník: GAIN Ventures s.r.o. , IČ: 056 90 935 Na strži 2102/61a, Krč, 140 00 Praha 4 zapsáno 18. března 2025 Podíl: Vklad: 455 ,- Kč Splaceno: 100 % Obchodní podíl: 3 % Druh podílu: základní podíl zapsáno 18. března 2025 vymazáno 19. prosince 2025 Podíl: Vklad:  ...

[2 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1124329&typ=UPLNY']]
```
</details>

→ `Bash` — List Carebot shareholders with entry dates
```sh
cd [redacted: local path] && PY=[redacted: local path] U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1124329&typ=UPLNY"; $PY bin/grep.py "$U" "Společník: [^,]{3,60}, IČ: [0-9 ]+[^z]{0,120}zapsáno [0-9]+\. [a-zěščřžýáíéůú]+ 20[0-9]{2}" 0 | head -30
```

<details><summary>result</summary>

```
... Společník: Dynumerics a.s. , IČ: 079 90 804 Pražská 1088/55a, 679 61 Letovice zapsáno 19. července 2021 ...

... Společník: Pilulka Lab s.r.o. , IČ: 287 33 347 Drahobejlova 1073/36, Libeň, 190 00 Praha 9 zapsáno 1. prosince 2021 ...

... Společník: Pilulka Lab s.r.o. , IČ: 287 33 347 Českomoravská 2408/1a, Libeň, 190 00 Praha 9 zapsáno 27. dubna 2023 ...

... Společník: Tahoe Invest a.s. , IČ: 085 35 655 Ovocný trh 1096/8, Staré Město, 110 00 Praha 1 zapsáno 18. března 2025 ...

... Společník: GAIN Ventures s.r.o. , IČ: 056 90 935 Na strži 2102/61a, Krč, 140 00 Praha 4 zapsáno 18. března 2025 ...

... Společník: Mediclinic a.s. , IČ: 279 18 335 Minská 84/97, Žabovřesky, 616 00 Brno zapsáno 18. března 2025 ...

... Společník: PAPER Media s.r.o. , IČ: 217 06 590 Revoluční 1082/8, Nové Město, 110 00 Praha 1 zapsáno 18. března 2025 ...

[7 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1124329&typ=UPLNY']]
```
</details>

→ `Bash` — Check Yieldigo and Sharry extracts for BHM entities
```sh
cd [redacted: local path] && PY=[redacted: local path] for U in "https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=949426&typ=UPLNY" "https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=940334&typ=UPLNY"; do $PY bin/get.py "$U" >/dev/null; echo "== $U"; $PY bin/grep.py "$U" "BHM|Bohemia" 300 | head -8; done
```

<details><summary>result</summary>

```
== https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=949426&typ=UPLNY
... 1984 Čapkova 1690/6, 251 01 Říčany Společník vlastní 1.500 základních podílů, a to podílů č. 5.001 až č. 6.500. zapsáno 31. října 2016 vymazáno 2. února 2017 Podíl: Vklad: 1 500 ,- Kč Splaceno: 100 % Obchodní podíl: 15 % Druh podílu: základní zapsáno 31. října 2016 vymazáno 2. února 2017 Společník: Bohemia Venture Capital a.s. , IČ: 054 55 464 Ovocný trh 573/12, Staré Město, 110 00 Praha 1 Společník vlastní 1.750 preferenčních podílů, a to podílů č. 6.501 až č. 8.250. zapsáno 31. října 2016 vymazáno 13. října 2019 Podíl: Vklad: 1 750 ,- Kč Splaceno: 100 % Obchodní podíl: 17,5 % Druh podílu: preferenč ...

... .2. písm. c) a 8.2. písm. d) společenské smlouvy, (ii) zvláštní hlasovací práva na valné hromadě podle článku 10.5 písm. c) společenské smlouvy, a (iii) právo udělit souhlas k vybraným jednáním jednatele dle článku 11.10 společenské smlouvy zapsáno 21. ledna 2022 vymazáno 22. května 2025 Společník: BHM Ventures a.s. , IČ: 054 55 464 Ovocný trh 1096/8, Staré Město, 110 00 Praha 1 Společník vlastní 1.750 preferenčních podílů S č. 6.501 až č. 8.250. zapsáno 22. května 2025 Podíl: Vklad: 1 750 ,- Kč Splaceno: 100 % Obchodní podíl: 1750/12129 Druh podílu: 1 750 preferenčních podílů S, tj. podílů se kt ...

[2 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=949426&typ=UPLNY']]
== https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?s
… [1385 more characters]
```
</details>

→ `Bash` — Check BHM-Carebot article details
```sh
cd [redacted: local path] && PY=[redacted: local path] U=https://www.startitup.sk/milionar-tomas-krsek-vstupuje-do-startupu-ktory-pomaha-lekarom-odhalit-rakovinu-uz-v-rannom-stadiu/; $PY bin/get.py $U; $PY bin/grep.py $U "BHM|Mediclinic|podiel|20[0-9]{2}" 200 | head -8
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://www.startitup.sk/milionar-tomas-krsek-vstupuje-do-startupu-ktory-pomaha-lekarom-odhalit-rakovinu-uz-v-rannom-stadiu/  len=8786
... u dostať aj ľudia, ktorí u nej nie sú poistení Výsledky vyhľadávania Tagy Milionár Tomáš Kršek vstupuje do startupu, ktorý pomáha lekárom odhaliť rakovinu už v rannom štádiu Linda Cebrová 20. augusta 2025 o 16:39 Tomáš Kršek investoval do českého startupu Carebot. Jeho AI ročne analyzuje viac než milión röntgenov. Rakovinu odhaľuje s 95 % presnosťou. BHM Group, freepik Linda Cebrová 20. augusta 2025 o ...

... u už v rannom štádiu Linda Cebrová 20. augusta 2025 o 16:39 Tomáš Kršek investoval do českého startupu Carebot. Jeho AI ročne analyzuje viac než milión röntgenov. Rakovinu odhaľuje s 95 % presnosťou. BHM Group, freepik Linda Cebrová 20. augusta 2025 o 16:39 Uložiť Uložené Zdieľať Investičná skupina BHM Group , ktorú založil milionár Tomáš Kršek a riadi ju managing director Jan Černý, získala 4,6-perc ...

... a 2025 o 16:39 Tomáš Kršek investoval do českého startupu Carebot. Jeho AI ročne analyzuje viac než milión röntgenov. Rakovinu odhaľuje s 95 % presnosťou. BHM Group, freepik Linda Cebrová 20. augusta 2025 o 16:39 Uložiť Uložené Zdieľať Investičná skupina BHM Group , ktorú založil milionár Tomáš Kršek a riadi ju managing director Jan Černý, získala 4,6-percentný podiel v českom medtech startupe Carebot ...

... pu Carebot. Jeho AI
… [388 more characters]
```
</details>

→ `Bash` — Find who entered Carebot in August 2025
```sh
cd [redacted: local path] && PY=[redacted: local path] U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1124329&typ=UPLNY"; $PY bin/grep.py "$U" "Společník: [^|]{0,200}?zapsáno (4\. srpna 2025|1[0-9]\. srpna 2025)" 50 | head; $PY bin/grep.py "$U" "4,6|Vklad: 696" 300 | head -4
```

<details><summary>result</summary>

```
... uh podílu: základní podíl zapsáno 26. června 2026 Společník: ERGOAPEX LIMITED 3032 Limassol, Karaiskaki, CITY HOUSE 6, Kyperská republika zapsáno 4. srpna 2025 Podíl: Vklad: 696 ,- Kč Splaceno: 100 % Obchodní  ...

[1 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1124329&typ=UPLNY']]
... ce 2025 vymazáno 26. června 2026 Podíl: Vklad: 777 ,- Kč Splaceno: 100 % Obchodní podíl: 4961/100000 Druh podílu: základní podíl zapsáno 26. června 2026 Společník: Tahoe Invest a.s. , IČ: 085 35 655 Ovocný trh 1096/8, Staré Město, 110 00 Praha 1 zapsáno 18. března 2025 vymazáno 4. srpna 2025 Podíl: Vklad: 696 ,- Kč Splaceno: 100 % Obchodní podíl: 4,59 % Druh podílu: základní podíl zapsáno 18. března 2025 vymazáno 4. srpna 2025 Společník: GAIN Ventures s.r.o. , IČ: 056 90 935 Na strži 2102/61a, Krč, 140 00 Praha 4 zapsáno 18. března 2025 Podíl: Vklad: 455 ,- Kč Splaceno: 100 % Obchodní podíl: 3 % Druh po ...

... ladní podíl zapsáno 19. prosince 2025 vymazáno 26. června 2026 Podíl: Vklad: 732 ,- Kč Splaceno: 100 % Obchodní podíl: 4675/100000 Druh podílu: základní podíl zapsáno 26. června 2026 Společník: ERGOAPEX LIMITED 3032 Limassol, Karaiskaki, CITY HOUSE 6, Kyperská republika zapsáno 4. srpna 2025 Podíl: Vklad: 696 ,- Kč Splaceno: 100 % Obchodní podíl: 4,59 % Druh podílu: základní podíl zapsáno 4. srpna 2025 vymazáno 19. prosince 2025 Podíl: Vklad: 1 327 ,- Kč Splaceno: 100 % Obchodní podíl: 8750/100000 Druh podílu: základní p
… [88 more characters]
```
</details>

→ `Bash` — Fetch Czech Founders site and Lighthouse news
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://lhv.vc/news-and-events/page/2/ https://czechfounders.vc/ https://czechfounders.vc/portfolio https://czechfounders.vc/news; $PY bin/grep.py https://lhv.vc/news-and-events/page/2/ "Czech Founders" 300 | head -4; $PY bin/show.py https://czechfounders.vc/ 0 2500
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://lhv.vc/news-and-events/page/2/  len=4907
[redacted: local path]  200 text/html; charset=utf-8 https://czechfounders.vc/  len=5585
[redacted: local path]  404 text/html; charset=utf-8 https://czechfounders.vc/portfolio  len=0
[redacted: local path]  404 text/html; charset=utf-8 https://czechfounders.vc/news  len=0
[0 matches, meta=['200 text/html; charset=UTF-8 https://lhv.vc/news-and-events/page/2/']]
Czech Founders VC | 🥷 | Czech Founders VC | 📩 | [redacted: email address] | 🎉 | The Founders community just grew international and got united.  🎊 | We’ve launched | United Founders! | We help build the next generation | of Central European unicorns by: | 😍 | Attracting | Attracting world-class | investors and mentors | 💸 | Investing | Investing in exceptional founders | with global ambitions | 🧑🏼‍🎓 | Learning | Enabling early-stage founders to learn from the best peers | 💡 | Apply for investment | ⛰️ | Apply for Sherpa acceleration | Our focus | This is what we typically invest in. | Pre-seed | Pre-seed tickets.  Typically €50-350k. | Strong founders | Winning teams willing to put everything into the game. | Go to market | Clear go-to-market strategy with a strong executive | team | . | CEE Region | Based in Central or Eastern Europe
… [1658 more characters]
```
</details>

→ `WebSearch` "Czech Founders" pre-seed round 2025 OR 2026 startup raises led by Czech Founders VC

<details><summary>result</summary>

```
Web search results for query: ""Czech Founders" pre-seed round 2025 OR 2026 startup raises led by Czech Founders VC"

Links: [{"title":"22227 cytowski partners advises filuta ai on usd 2 5 million pre seed financing","url":"https://ceelegalmatters.com/by-practice/22227-cytowski-partners-advises-filuta-ai-on-usd-2-5-million-pre-seed-financing"},{"title":"22227 cytowski partners advises filuta ai on usd 2 5 million pre seed financing","url":"https://ceelegalmatters.com/czech-republic/22227-cytowski-partners-advises-filuta-ai-on-usd-2-5-million-pre-seed-financing"},{"title":"czechfounders vc","url":"https://superscout.co/investor/czechfounders-vc"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/czech-founders-vc"},{"title":"Úspěšní čeští startupisté budou pomáhat novým nadějím. Vybrali na to mezi sebou čtvrt miliardy","url":"https://cc.cz/uspesni-cesti-startupiste-budou-pomahat-novym-nadejim-vybrali-na-to-mezi-sebou-ctvrt-miliardy/"},{"title":"10 Prague angel investors funding Czech pre-seed startups in 2026","url":"https://www.ellty.com/investors/prague-angel-investors"},{"title":"Z garáže k veľkému biznisu: Slovákom stačí len dobrý nápad, na podporu môžu získať stovky tisíc eur","url":"https://www.startitup.sk/z-garaze-k-velkemu-biznisu-slovakom-staci-len-dobry-napad-na-podporu-mozu-ziskat-stovky-tisic-eur/"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/czechfounde
… [1720 more characters]
```
</details>

→ `Bash` — Search justice.cz for Czech Founders portfolio companies
```sh
cd [redacted: local path] && UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"; for n in Lemondia "Carta Genum" Maxfusion Edmund Merchantee Daitable Yedem Lignufy AdSpawn Circuparts; do echo "== $n"; curl -sL --max-time 30 -A "$UA" -G "https://or.justice.cz/ias/ui/rejstrik-\$firma" --data-urlencode "nazev=$n" | grep -o 'subjektId=[0-9]*' | sort -u | head -3; done
```

<details><summary>result</summary>

```
== Lemondia
subjektId=1209281
== Carta Genum
subjektId=1274044
== Maxfusion
subjektId=1302395
== Edmund
subjektId=1199826
subjektId=14298
subjektId=148704
== Merchantee
subjektId=1200590
== Daitable
== Yedem
subjektId=1040865
== Lignufy
subjektId=1221616
== AdSpawn
== Circuparts
subjektId=1240518
```
</details>

→ `Bash` — Fetch justice.cz extracts and find Czech Founders entries
```sh
cd [redacted: local path] && PY=[redacted: local path] for id in 1209281 1274044 1302395 1199826 1200590 1040865 1221616 1240518; do U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=$id&typ=UPLNY"; $PY bin/get.py "$U" >/dev/null; echo "== $id $($PY bin/show.py "$U" 0 2000 | grep -o 'Obchodní firma: | [^|]*' | head -1)"; $PY bin/grep.py "$U" "Společník: (Czech Founders|CZECH FOUNDERS|United Founders|UNITED FOUNDERS)[^|]{0,200}?zapsáno [0-9]+\. [a-zěščřžýáíéůú]+ 20[0-9]{2}" 0 | head -4; done
```

<details><summary>result</summary>

```
== 1209281 Obchodní firma: | Lemondia s.r.o.
[0 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1209281&typ=UPLNY']]
== 1274044 Obchodní firma: | Carta Genum Analytics s.r.o.
[0 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1274044&typ=UPLNY']]
== 1302395 Obchodní firma: | Maxfusion AI s.r.o.
[0 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1302395&typ=UPLNY']]
== 1199826 Obchodní firma: | EDIMA solutions, s.r.o.
... Společník: Czech Founders Ventures s.r.o., osoba rizikového kapitálu , IČ: 170 51 835 Salvátorská 931/8, Staré Město, 110 00 Praha 1 zapsáno 25. března 2026 ...

[1 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1199826&typ=UPLNY']]
== 1200590 Obchodní firma: | Merchantee s.r.o.
[0 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1200590&typ=UPLNY']]
== 1040865 Obchodní firma: | HitchMe s.r.o.
[0 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1040865&typ=UPLNY']]
== 1221616 Obchodní firma: | Lignufy s.r.o.
[0 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1221616&typ=UPLNY']]
== 1240518 Obchodní firma: | CircuParts s.r.o.
[0 matches, meta=['200
… [108 more characters]
```
</details>

→ `Bash` — Inspect EDIMA solutions extract
```sh
cd [redacted: local path] && PY=[redacted: local path] U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1199826&typ=UPLNY"; $PY bin/grep.py "$U" "Edmund|Czech Founders|Předmět|Datum vzniku" 300 | head -8
```

<details><summary>result</summary>

```
... Veřejný rejstřík a Sbírka listin - Ministerstvo spravedlnosti České republiky Nový portál pro obchodní rejstřík a evidenci sveřenských fondů, který běží v ověřovacím provozu, se aktuálně upravuje. Úplný výpis z obchodního rejstříku Edmund s.r.o. , C 92247 vedená u Krajského soudu v Ostravě Vytisknout Úplný výpis z obchodního rejstříku, vedeného Krajským soudem v Ostravě oddíl C , vložka 92247 Datum vzniku a zápisu: 30. března 2023 Spisová značka: C 92247 vedená u Krajského soudu v Ostravě zapsáno 30. března 2023 Obchodní firma: EDIM ...

... chodní rejstřík a evidenci sveřenských fondů, který běží v ověřovacím provozu, se aktuálně upravuje. Úplný výpis z obchodního rejstříku Edmund s.r.o. , C 92247 vedená u Krajského soudu v Ostravě Vytisknout Úplný výpis z obchodního rejstříku, vedeného Krajským soudem v Ostravě oddíl C , vložka 92247 Datum vzniku a zápisu: 30. března 2023 Spisová značka: C 92247 vedená u Krajského soudu v Ostravě zapsáno 30. března 2023 Obchodní firma: EDIMA solutions, s.r.o. zapsáno 30. března 2023 vymazáno 26. února 2025 Edmund s.r.o. zapsáno 26. února 2025 Sídlo: Havlíčkova 233, Místek, 738 01 Frýdek-Místek zapsáno 30. b ...

... ý výpis z obchodního rejstříku, vedeného Krajským soudem v Ostravě oddíl C , vložka 92247 Datum vzniku a zápisu: 30. března 2023 Spisová značka: C 92247 vedená u Krajského soudu v Ostravě zapsáno 30. března 2023 Obchodní firma: EDIMA solutions, s.r.o. zapsáno 30. března 2023 vymazáno 26. února 2025 Edmund s.r.o. zapsáno 26.
… [901 more characters]
```
</details>

→ `Bash` — Confirm Czech Founders entry in Edmund extract
```sh
cd [redacted: local path] && PY=[redacted: local path] U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1199826&typ=UPLNY"; $PY bin/grep.py "$U" "Czech Founders" 350; $PY bin/q.py "$U" "Společník: Czech Founders Ventures s.r.o., osoba rizikového kapitálu , IČ: 170 51 835 Salvátorská 931/8, Staré Město, 110 00 Praha 1 zapsáno 25. března 2026"
```

<details><summary>result</summary>

```
... Obchodní podíl: 1825000/9093055 Druh podílu: Základní zapsáno 25. března 2026 Společník: TOMÁŠ PALOVSKÝ , dat. nar. 23. března 1999 Kpt. Nálepky 3512, Frýdek, 738 01 Frýdek-Místek zapsáno 30. března 2023 vymazáno 24. dubna 2024 Podíl: Vklad: 5 000 ,- Kč Splaceno: 100 % Obchodní podíl: 10 % zapsáno 30. března 2023 vymazáno 24. dubna 2024 Společník: Czech Founders Ventures s.r.o., osoba rizikového kapitálu , IČ: 170 51 835 Salvátorská 931/8, Staré Město, 110 00 Praha 1 zapsáno 25. března 2026 Podíl: Vklad: 7 534,24 Kč Splaceno: 100 % Obchodní podíl: 753424/9093055 Druh podílu: Preferenční podíl se kterým jsou spojena práva a povinnosti dle článku 6 až 9 společenské smlouvy zapsáno 25. března 2026 Společník: ...

[1 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1199826&typ=UPLNY']]
OK ws-exact | norm OK
```
</details>

→ `WebSearch` "Orbit Capital" growth equity investment 2025 OR 2026 Prague leads round

<details><summary>result</summary>

```
Web search results for query: ""Orbit Capital" growth equity investment 2025 OR 2026 Prague leads round"

Links: [{"title":"Orbit Capital Overview","url":"https://pitchbook.com/profiles/investor/434354-77"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/articles/orbit-capital-raises-107-m-for-growth-debt"},{"title":"CEE VC SUMMIT 2026","url":"https://www.vestbee.com/blog/articles/orbit-capital-launches-100-m-fund"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/orbit-capital-secures-70m-for-tech-growth"},{"title":"> ## Content Index","url":"https://www.therecursive.com/polish-orbit-capital-closes-eur107m-growth-debt-fund-ii-to-expand-venture-debt-for-cee-scaleups.md"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/articles/orbit-capital-launches-100-m-fund"},{"title":"Orbit inks more than €100m for venture debt fund","url":"https://alternativecreditinvestor.com/2026/07/02/orbit-inks-more-than-e100m-for-venture-debt-fund/"},{"title":"EIF Pledges €20 Million to Fuel Expansion of CEE-Based Innovative SMEs via Orbit Growth Debt II Fund","url":"https://www.eif.org/InvestEU/news/2025/eif-pledges-eur20-million-to-fuel-expansion-of-cee-based-innovative-smes-via-orbit-growth-debt-ii-fund"},{"title":"Prague's Orbit Capital Closes Second Growth Debt Fund at €107 Million","url":"https://www.startupresearcher.com/news/prague-s-orbit-capital-closes-second-growth-debt-fund-at-107-million"},{"title":"orbit capit
… [1281 more characters]
```
</details>

→ `Bash` — Inspect Orbit Capital site source
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://orbitcapital.com/ https://www.orbitcapital.com/portfolio; ls -la pages/$($PY -c "import hashlib;print(hashlib.sha1(b'https://orbitcapital.com/').hexdigest()[:16])").raw; grep -o -i -E '"(name|title|company)":"[^"]{2,40}"' pages/$($PY -c "import hashlib;print(hashlib.sha1(b'https://orbitcapital.com/').hexdigest()[:16])").raw | sort -u | head -40; grep -o 'src="[^"]*\.js"' pages/$($PY -c "import hashlib;print(hashlib.sha1(b'https://orbitcapital.com/').hexdigest()[:16])").raw | head
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=utf-8 https://orbitcapital.com/  len=54
[redacted: local path]  404 text/html; charset=utf-8 https://orbitcapital.com/portfolio  len=13
-rw-r--r--  1 [user]  staff  31599 11 Oct  06:31 pages/f6452aac9c3c773a.raw
"title":"Orbit Capital"
src="https://app.analyzati.com/js/script.js"
src="/_nuxt/DeXhN4Yd.js"
```
</details>

→ `Bash` — Find Orbit site routes and data endpoints
```sh
cd [redacted: local path] && grep -o '_payload[^"]*\|/api/[^"]*' pages/f6452aac9c3c773a.raw | sort -u | head; curl -sL --max-time 30 -A "Mozilla/5.0" https://orbitcapital.com/_nuxt/DeXhN4Yd.js | grep -o -E '"/[a-z-]+(/[a-z-]+)?"' | sort -u | head -40
```

<details><summary>result</summary>

```
_payload.json?a868da23-4e3a-4d30-bb12-199f832554ec
"/debt"
"/equity"
"/team"
```
</details>

→ `Bash` — Fetch Orbit equity/debt pages and payloads
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://orbitcapital.com/equity https://orbitcapital.com/debt; $PY bin/show.py https://orbitcapital.com/equity 0 3000; for p in equity debt; do curl -sL --max-time 30 -A "Mozilla/5.0" "https://orbitcapital.com/$p/_payload.json" | head -c 1500; echo; done
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=utf-8 https://orbitcapital.com/equity/  len=372
[redacted: local path]  200 text/html; charset=utf-8 https://orbitcapital.com/debt/  len=528
Orbit Capital Growth Equity | We | are | here | to | grow | innovative | scale | ‑ups. | Experience. | Ambition. | Rigor. | Orbit Capital Team | Radovan | Nesrsta | Partner | Wiktor | Namysl | Partner | Pavel | Mucha | IC Member | Lukas | Valek | CFO/COO | Michala | Vondrakova | Legal Officer | Tim | Polas | Financial Associate | Zosia | Kludka | Communications | Kamila | Himkova | Office Manager | Florian | Rickal | Fund Administration | ← | BACK | l>
[{"data":1,"prerenderedAt":3},["ShallowReactive",2],{},1784843665780]
[{"data":1,"prerenderedAt":3},["ShallowReactive",2],{},1784843665780]
```
</details>

→ `WebSearch` Sloneek Orbit Capital 2026 financing

<details><summary>result</summary>

```
Web search results for query: "Sloneek Orbit Capital 2026 financing"

Links: [{"title":"Join Vestbee Summer Pitch CEE","url":"https://vestbee.com/insights/articles/orbit-capital-raises-107-m-for-growth-debt"},{"title":"> ## Content Index","url":"https://www.therecursive.com/polish-orbit-capital-closes-eur107m-growth-debt-fund-ii-to-expand-venture-debt-for-cee-scaleups.md"},{"title":"parsers.vc","url":"https://parsers.vc/fund/vff.sk/"},{"title":"Back to Orbit Capital","url":"https://seedtable.com/investors/orbit-capital/portfolio"},{"title":"Orbit Capital closes €107M venture debt fund for CEE scaleups","url":"https://tech.eu/2026/07/02/orbit-capital-closes-eur107m-venture-debt-fund-for-cee-scaleups/"},{"title":"orbit capital","url":"https://seedtable.com/investors/orbit-capital"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/orbit-capital"},{"title":"polish orbit capital closes eur107m growth debt fund ii to expand venture debt for cee scaleups","url":"https://therecursive.com/polish-orbit-capital-closes-eur107m-growth-debt-fund-ii-to-expand-venture-debt-for-cee-scaleups/"},{"title":"Prague's Orbit Capital Closes Second Growth Debt Fund at €107 Million","url":"https://www.startupresearcher.com/news/prague-s-orbit-capital-closes-second-growth-debt-fund-at-107-million"}]

Sloneek's 2026 round was led mainly by Orbit Capital, and Orbit separately closed a new venture debt fund that same year.

- **Slone
… [1248 more characters]
```
</details>

→ `WebSearch` "Impulse Ventures" Ondřej Tomek investice startup 2024 2025

<details><summary>result</summary>

```
Web search results for query: ""Impulse Ventures" Ondřej Tomek investice startup 2024 2025"

Links: [{"title":"rok 2025 ve startupech technologicke firmy si vyskakuji cesi si veri jako globalni hraci a nejasna odpoved na otazku jestli se stehovat ze zeme","url":"https://www.lupa.cz/clanky/rok-2025-ve-startupech-technologicke-firmy-si-vyskakuji-cesi-si-veri-jako-globalni-hraci-a-nejasna-odpoved-na-otazku-jestli-se-stehovat-ze-zeme/"},{"title":"mame pro startupy ve stredni evrope ctyri miliardy korun hlasi novy cesky fond stoji za nim ondrej tomek a spol","url":"https://cc.cz/mame-pro-startupy-ve-stredni-evrope-ctyri-miliardy-korun-hlasi-novy-cesky-fond-stoji-za-nim-ondrej-tomek-a-spol/"},{"title":"dalsi desitky milionu od tomka vstup do brazilie dataddo nabira na sile","url":"https://forbes.cz/dalsi-desitky-milionu-od-tomka-vstup-do-brazilie-dataddo-nabira-na-sile/"},{"title":"Miliardář Tomek investuje do správy dat. Hodnota startupu Dataddo dosáhla půl miliardy","url":"https://www.e15.cz/byznys/startupy/miliardar-tomek-investuje-do-spravy-dat-hodnota-startupu-dataddo-dosahla-pul-miliardy-1384619"},{"title":"České Dataddo má čtvrtou investici od miliardáře Ondřeje Tomka. Datový startup se rozpíná po světě","url":"https://cc.cz/ceske-dataddo-ma-ctvrtou-investici-od-miliardare-ondreje-tomka-z-datoveho-startupu-se-stava-globalni-hrac/"},{"title":"Hlavní obsah","url":"https://www.seznamzpravy.cz/clanek/novy-cesky-fond-nabizi-ctyri-miliardy-pro-technologicke-nadsence-118740"},{"tit
… [2448 more characters]
```
</details>

→ `Bash` — Check Dataddo/Safetica/Shoptet registers for Impulse
```sh
cd [redacted: local path] && PY=[redacted: local path] UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"; for n in Dataddo Safetica Shoptet; do id=$(curl -sL --max-time 30 -A "$UA" -G "https://or.justice.cz/ias/ui/rejstrik-\$firma" --data-urlencode "nazev=$n" | grep -o 'subjektId=[0-9]*' | sort -u | head -1 | cut -d= -f2); U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=$id&typ=UPLNY"; $PY bin/get.py "$U" >/dev/null; echo "== $n $id"; $PY bin/grep.py "$U" "Impulse[^|]{0,250}?zapsáno [0-9]+\. [a-zěščřžýáíéůú]+ 20[0-9]{2}( vymazáno [0-9]+\. [a-zěščřžýáíéůú]+ 20[0-9]{2})?" 0 | head -8; done
```

<details><summary>result</summary>

```
== Dataddo 895711
... Impulse Ventures DD, s.r.o. , IČ: 088 66 716 U Nesypky 1255/3, Smíchov, 150 00 Praha 5 zapsáno 3. února 2020 vymazáno 1. července 2020 ...

[1 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=895711&typ=UPLNY']]
== Safetica 26844
... Impulse Capital, a.s. , IČ: 052 36 941 U Nesypky 1255/3, Smíchov, 150 00 Praha 5 zapsáno 21. února 2020 vymazáno 1. května 2022 ...

[1 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=26844&typ=UPLNY']]
== Shoptet 369286
... Impulse Capital, s.r.o. , IČ: 052 36 941 U Nesypky 1255/3, Smíchov, 150 00 Praha 5 zapsáno 15. září 2016 vymazáno 3. ledna 2020 ...

... Impulse Capital, a.s. , IČ: 052 36 941 U Nesypky 1255/3, Smíchov, 150 00 Praha 5 zapsáno 3. ledna 2020 vymazáno 1. července 2020 ...

... Impulse Capital, a.s. , IČ: 052 36 941 Pod dráhou 1637/6, Holešovice, 170 00 Praha 7 zapsáno 16. července 2024 vymazáno 29. září 2025 ...

[3 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=369286&typ=UPLNY']]
```
</details>

→ `Bash` — Date Dataddo-Tomek articles and recent Dataddo shareholders
```sh
cd [redacted: local path] && PY=[redacted: local path] for U in https://forbes.cz/dalsi-desitky-milionu-od-tomka-vstup-do-brazilie-dataddo-nabira-na-sile/ https://cc.cz/ceske-dataddo-ma-ctvrtou-investici-od-miliardare-ondreje-tomka-z-datoveho-startupu-se-stava-globalni-hrac/; do $PY bin/get.py $U >/dev/null; $PY bin/grep.py $U "Impulse|20[12][0-9]" 120 | head -5; done; U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=895711&typ=UPLNY"; $PY bin/grep.py "$U" "Společník: [^|]{0,120}?zapsáno [0-9]+\. [a-zěščřžýáíéůú]+ 20(2[3-6])" 0 | head
```

<details><summary>result</summary>

```
... eciály Woman Podcasty Newslettery Eventy Forbes Select Akcie Kryptoměny Nemovitosti Peníze Vše z investic Těší mě Říjen 2026 Zjistěte více! Automotive Doprava E-commerce Energetika Obchod Potraviny Stavebnictví Strojírenství Obranný průmysl Zdr ...

...  Energetika Obchod Potraviny Stavebnictví Strojírenství Obranný průmysl Zdraví Zemědělství Vše z průmyslu Těší mě Říjen 2026 Zjistěte více! Architektura Cestování Ekonomika Filantropie Gastro Kultura Politika Práce Sport Udržitelnost Umění & de ...

... tropie Gastro Kultura Politika Práce Sport Udržitelnost Umění & design Vzdělávání Woman Vše ze společnosti Iva Listopad 2025 Zjistěte více! Fintech Inovace Startupy Umělá inteligence Věda Vše z technologií Kam zmizí Česko? Září 2026 Zjistěte ví ...
... ského startupu Dataddo - CzechCrunch Přejít k obsahu | Přejít k hlavnímu menu | Přejít k vyhledávání Startupy – 20. 12. 2023 – 1 min čtení České Dataddo má čtvrtou investici od miliardáře Ondřeje Tomka. Datový startup se rozpíná po světě Přes t ...

... má čtvrtou investici od miliardáře Ondřeje Tomka. Datový startup se rozpíná po světě Přes třicet milionů korun od fondu Impulse Ventures chce Dataddo využít zejména na další škálování přes marketing. Peter Brejčák 0 Zobrazit komentáře Sdílet Foto: ...

... á také na latinskoamerických trzích. Pražský startup Dataddo teď uzavřel své čtvrté investiční kolo, a to opět od fondu Impulse Ventures. Fond spravuje prostředky Ondřeje Tomka, jenž po prodeji portálu Centrum.cz mimo jiné i
… [157 more characters]
```
</details>

→ `Bash` — Look for Dataddo own funding announcements
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.dataddo.com/blog https://www.dataddo.com/press https://www.dataddo.com/about-us 2>&1 | grep -v REPLACE; for u in https://www.dataddo.com/blog https://www.dataddo.com/press https://www.dataddo.com/about-us; do $PY bin/grep.py $u "Impulse|funding|raise" 150 | head -4; done
```

<details><summary>result</summary>

```
[redacted: local path]  404 text/html https://www.dataddo.com/blog  len=5786
[redacted: local path]  404 text/html https://www.dataddo.com/press  len=5786
[redacted: local path]  404 text/html https://www.dataddo.com/about-us  len=5786
[0 matches, meta=['404 text/html https://www.dataddo.com/blog']]
[0 matches, meta=['404 text/html https://www.dataddo.com/press']]
[0 matches, meta=['404 text/html https://www.dataddo.com/about-us']]
```
</details>

→ `WebSearch` dataddo.com Impulse Ventures investment announcement Dataddo raises

<details><summary>result</summary>

```
Web search results for query: "dataddo.com Impulse Ventures investment announcement Dataddo raises"

Links: [{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/dataddo/financials"},{"title":"Fond Ondřeje Tomka investuje další milion dolarů do startupu Dataddo","url":"https://www.lupa.cz/aktuality/fond-ondreje-tomka-investuje-dalsi-milion-dolaru-do-startupu-dataddo/"},{"title":"dalsi desitky milionu od tomka vstup do brazilie dataddo nabira na sile","url":"https://forbes.cz/dalsi-desitky-milionu-od-tomka-vstup-do-brazilie-dataddo-nabira-na-sile/"},{"title":"Miliardář Tomek investuje do správy dat. Hodnota startupu Dataddo dosáhla půl miliardy","url":"https://www.e15.cz/byznys/startupy/miliardar-tomek-investuje-do-spravy-dat-hodnota-startupu-dataddo-dosahla-pul-miliardy-1384619"},{"title":"Miliardář Ondřej Tomek investuje do Dataddo již potřetí. Český datový startup nově využívá i Twitter","url":"https://cc.cz/miliardar-ondrej-tomek-investuje-do-dataddo-jiz-potreti-cesky-datovy-startup-nove-vyuziva-i-twitter/"},{"title":"Data jedou. Český startup Dataddo rychle roste a ještě více ho nakopnou další miliony od fondu Ondřeje Tomka","url":"https://cc.cz/data-jedou-cesky-startup-dataddo-rychle-roste-a-jeste-vice-ho-nakopnou-dalsi-miliony-od-fondu-ondreje-tomka/"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/dataddo"},{"title":"Dataddo Overview","url":"https://pitchbook.com/profiles/company/303308-92"},{"title":"proc zacinat v cesku kdyz muze
… [1887 more characters]
```
</details>

→ `Bash` — Check KOOPEO portfolio companies in justice.cz
```sh
cd [redacted: local path] && PY=[redacted: local path] UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"; for n in Precisimo Trifft KeyGuru "KOOPEO"; do ids=$(curl -sL --max-time 30 -A "$UA" -G "https://or.justice.cz/ias/ui/rejstrik-\$firma" --data-urlencode "nazev=$n" | grep -o 'subjektId=[0-9]*' | sort -u | head -3 | cut -d= -f2); for id in $ids; do U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=$id&typ=UPLNY"; $PY bin/get.py "$U" >/dev/null; echo "== $n $id $($PY bin/show.py "$U" 0 2500 | grep -o 'Obchodní firma: | [^|]*' | head -1)"; $PY bin/grep.py "$U" "KOOPEO[^|]{0,200}?zapsáno [0-9]+\. [a-zěščřžýáíéůú]+ 20[0-9]{2}( vymazáno [0-9]+\. [a-zěščřžýáíéůú]+ 20[0-9]{2})?" 0 | head -4; done; done
```

<details><summary>result</summary>

```
== KeyGuru 1030518 Obchodní firma: | Keyguru s.r.o.
[0 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1030518&typ=UPLNY']]
== KOOPEO 940591 Obchodní firma: | KOOPEO Ventures SE
... KOOPEO Ventures SE zapsáno 27. července 2016 ...

[1 matches, meta=['200 text/html;charset=UTF-8 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=940591&typ=UPLNY']]
```
</details>

→ `Bash` — Show KOOPEO Ventures SE register extract
```sh
cd [redacted: local path] && PY=[redacted: local path] U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=940591&typ=UPLNY"; $PY bin/show.py "$U" 0 3500
```

<details><summary>result</summary>

```
Veřejný rejstřík a Sbírka listin - Ministerstvo spravedlnosti České republiky | Nový portál pro obchodní rejstřík a evidenci sveřenských fondů, který běží v ověřovacím provozu, se aktuálně upravuje. | Úplný výpis | z | obchodního rejstříku | KOOPEO Ventures SE | , | H | 564 | vedená u | Krajského soudu v Brně | Vytisknout | Úplný výpis | z | obchodního rejstříku, vedeného | Krajským soudem v Brně | oddíl | H | , vložka | 564 | Datum vzniku a zápisu: | 27. července 2016 | Spisová značka: | H 564 vedená u Krajského soudu v Brně | zapsáno 27. července 2016 | Obchodní firma: | KOOPEO Ventures SE | zapsáno 27. července 2016 | Sídlo: | Solniční 243/17, Brno-město, 602 00  Brno | zapsáno 27. července 2016 | Identifikační číslo: | 052 | 69 | 113 | zapsáno 27. července 2016 | Právní forma: | Evropská společnost | zapsáno 27. července 2016 | Předmět podnikání: | Pronájem nemovitých věcí, bytů a nebytových prostor. | zapsáno 27. července 2016 | Výroba, obchod a služby neuvedené v přílohách 1 až 3 živnostenského zákona. | zapsáno 1. srpna 2019 | Statutární orgán - představenstvo: | člen představenstva: | VLADIMÍR ŠŤASTNÝ | , dat. nar. | 7. listopadu 1985 | 03222  Liptovský Trnovec 248, Slovenská republika | Den vzniku funkce: | 27. července 2016 | Den vzniku členství: | 27. července 2016 | zapsáno 27. července 2016 | vymazáno 10. ledna 2017 | člen představenstva: | VLADIMÍR ŠŤASTNÝ | , dat. nar. | 7. listopadu 1985 | 03222 Liptovský Trnovec 248, Slovenská republika | Den vzniku členství:
… [2000 more characters]
```
</details>

→ `Bash` — Probe Air Ventures sites and AIR VENTURES s.r.o. register
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://airventures.co/ https://www.airventures.co/ https://airventures.vc/ https://www.airventures.cz/ 2>&1 | grep -v REPLACE; UA="Mozilla/5.0"; id=$(curl -sL --max-time 30 -A "$UA" -G "https://or.justice.cz/ias/ui/rejstrik-\$firma" --data-urlencode "ico=04999851" | grep -o 'subjektId=[0-9]*' | sort -u | head -1 | cut -d= -f2); echo $id; U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=$id&typ=UPLNY"; $PY bin/get.py "$U" >/dev/null; $PY bin/show.py "$U" 0 1800
```

<details><summary>result</summary>

```
[redacted: local path]  000  https://airventures.co/  len=0
[redacted: local path]  000  https://www.airventures.co/  len=0
[redacted: local path]  200 text/html https://airventures.vc/  len=30
[redacted: local path]  000  https://www.airventures.cz/  len=0
931251
Veřejný rejstřík a Sbírka listin - Ministerstvo spravedlnosti České republiky | Nový portál pro obchodní rejstřík a evidenci sveřenských fondů, který běží v ověřovacím provozu, se aktuálně upravuje. | Úplný výpis | z | obchodního rejstříku | AIR VENTURES s.r.o. | , | C | 256839 | vedená u | Městského soudu v Praze | Vytisknout | Úplný výpis | z | obchodního rejstříku, vedeného | Městským soudem v Praze | oddíl | C | , vložka | 256839 | Datum vzniku a zápisu: | 19. dubna 2016 | Spisová značka: | C 256839 vedená u Městského soudu v Praze | zapsáno 19. dubna 2016 | Obchodní firma: | AIR VENTURES s.r.o. | zapsáno 19. dubna 2016 | Sídlo: | Drtinova 557/10, Smíchov, 150 00  Praha 5 | zapsáno 19. dubna 2016 | vymazáno 28. ledna 2021 | Pařížská 68/9, Josefov, 110 00  Praha 1 | zapsáno 28. ledna 2021 | vymazáno 15. října 2024 | Rohanské nábřeží 678/25, Karlín, 186 00  Praha 8 | zapsáno 15. října 2024 | Identifikační číslo: | 049 | 99 | 851 | zapsáno 19. dubna 2016 | Právní forma: | Společnost s ručením omezeným | zapsáno 19. dubna 2016
… [757 more characters]
```
</details>

→ `Bash` — Show airventures.vc and rest of AIR VENTURES extract
```sh
cd [redacted: local path] && cat pages/da36962a1c0c59b8.txt; echo; head -c 800 pages/da36962a1c0c59b8.raw; echo; PY=[redacted: local path] U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=931251&typ=UPLNY"; $PY bin/show.py "$U" 1800 3500
```

<details><summary>result</summary>

```
This site is under development
<!DOCTYPE HTML>
<html>

    <head>
        <title>This site is under development</title>
        <style>
            #ad_frame{ height:800px; width:100%; }
            body{ margin:0; border: 0; padding: 0; }
        </style>
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
        <script type="text/javascript" language="JavaScript">
            var url = 'http://www.searchvity.com/?dn='
                + document.domain + '&pid=9PO1MNIJ3';

            $(document).ready(function() {
                $('#ad_frame').attr('src', url);
            });
        </script>
    </head>
    <body>
        <iframe id="ad_frame" src="http://www.searchvity.com/"
            frameborder="0" scrolling="no">

            <div id="container">
                <h1>
1  Zvolen, Hollého 2, Slovenská republika | Den vzniku funkce: | 25. července 2018 | zapsáno 27. července 2018 | Počet členů: | 1 | zapsáno 19. dubna 2016 | vymazáno 27. července 2018 | 2 | zapsáno 27. července 2018 | Způsob jednání: | Jednatel zastupuje společnost samostatně. | zapsáno 19. dubna 2016 | vymazáno 27. července 2018 | Za společnost jednají vždy dva jednatelé společně | zapsáno 27. července 2018 | Společníci: | Společník: | MN Holding s.r.o. | , IČ: | 037 75 925 | Jednořadá 451/4, Bubeneč, 160 00  Praha 6 | zapsáno 19. dubna 2016 | vymazáno 25. května 2016 | Podíl: | Vklad: | 10 000 | ,- Kč | Splaceno: | 100 | % | Obchodní podíl: | 1/3 | Druh podí
… [1032 more characters]
```
</details>

→ `WebSearch` "Air Ventures" Pavlečka OR Kristeľ OR Kristel investice startup

<details><summary>result</summary>

```
Web search results for query: ""Air Ventures" Pavlečka OR Kristeľ OR Kristel investice startup"

Links: [{"title":"Z garáže k veľkému biznisu: Slovákom stačí len dobrý nápad, na podporu môžu získať stovky tisíc eur","url":"https://www.startitup.sk/z-garaze-k-velkemu-biznisu-slovakom-staci-len-dobry-napad-na-podporu-mozu-ziskat-stovky-tisic-eur/"},{"title":"prusovy tiskarny jako nova skodovka dovedu si to predstavit rika investor","url":"https://forbes.cz/prusovy-tiskarny-jako-nova-skodovka-dovedu-si-to-predstavit-rika-investor/"},{"title":"Vaclav Pavlecka","url":"https://startupyard.com/startups/vaclav-pavlecka"},{"title":"luma.com","url":"https://luma.com/i0dvx836"},{"title":"Vaclav Pavlecka","url":"https://cz.linkedin.com/in/vaclavpavlecka"},{"title":"www.ft.tul.cz","url":"https://www.ft.tul.cz/fakultni-novinky/226/download/152"},{"title":"Václav Pavlečka","url":"https://www.resite.org/speakers/vaclav-pavlecka"},{"title":"luma.com","url":"https://luma.com/i0dvx836?locale=cs"},{"title":"AirVentures Overview","url":"https://pitchbook.com/profiles/investor/489928-60"},{"title":"Venture Capital","url":"https://altss.com/profile/air-ventures"}]

Air Ventures is a small Prague venture fund, and both Pavlečka and Kristeľ have been tied to it.

- **Founding and focus:** PitchBook says Air Ventures is a venture capital firm based in Prague, Czech Republic, founded in 2016. Altss describes it as investing in technology startups across various industries.
- **Pavlečka:** Forbes Czech
… [1239 more characters]
```
</details>

→ `Bash` — Check Air Ventures holdings in justice.cz
```sh
cd [redacted: local path] && PY=[redacted: local path] UA="Mozilla/5.0"; for n in Kimba "Feel Goods" Jiant; do ids=$(curl -sL --max-time 30 -A "$UA" -G "https://or.justice.cz/ias/ui/rejstrik-\$firma" --data-urlencode "nazev=$n" | grep -o 'subjektId=[0-9]*' | sort -u | head -4 | cut -d= -f2); for id in $ids; do U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=$id&typ=UPLNY"; $PY bin/get.py "$U" >/dev/null; echo "== $n $id $($PY bin/show.py "$U" 0 2500 | grep -o 'Obchodní firma: | [^|]*' | head -1)"; $PY bin/grep.py "$U" "AIR VENTURES[^|]{0,200}?zapsáno [0-9]+\. [a-zěščřžýáíéůú]+ 20[0-9]{2}( vymazáno [0-9]+\. [a-zěščřžýáíéůú]+ 20[0-9]{2})?" 0 | head -3; done; done
```

<details><summary>result</summary>

```
== Kimba 123977
450173
[0 matches, meta=['450173&typ=UPLNY', '000  https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=123977', '450173&typ=UPLNY']]
```
</details>

→ `WebSearch` "Springtide Ventures" investice 2023 OR 2024 OR 2025 KKCG startup kolo

<details><summary>result</summary>

```
Web search results for query: ""Springtide Ventures" investice 2023 OR 2024 OR 2025 KKCG startup kolo"

Links: [{"title":"komarek investuje do umele inteligence kkcg posila do izraelskeho startupu 65 milionu korun","url":"https://forbes.cz/komarek-investuje-do-umele-inteligence-kkcg-posila-do-izraelskeho-startupu-65-milionu-korun/"},{"title":"Miliardář Karel Komárek dál loví v Izraeli. Investuje do startupu pro ochranu firemních dat a dokumentů","url":"https://cc.cz/miliardar-karel-komarek-dal-lovi-v-izraeli-investuje-do-startupu-pro-ochranu-firemnich-dat-a-dokumentu/"},{"title":"Komárkův fond Springtide Ventures investuje do izraelského startupu Cognni","url":"https://www.e15.cz/byznys/komarkuv-fond-springtide-ventures-investuje-do-izraelskeho-startupu-cognni-1384434"},{"title":"Příběh druhého nejbohatšího Čecha v Izraeli rezonuje. Komárka tu chtějí napodobit, hlásí fond Springtide","url":"https://cc.cz/pribeh-druheho-nejbohatsiho-cecha-v-izraeli-rezonuje-komarka-tu-chteji-napodobit-hlasi-fond-springtide/"},{"title":"server o českém Internetu","url":"https://www.lupa.cz/n/springtide/"},{"title":"Pražský kapitálový fond chce investovat až 1,6 miliard korun do středoevropských startupů","url":"https://cc.cz/prazsky-kapitalovy-fond-chce-investovat-az-16-miliard-korun-do-stredoevropskych-startupu/"},{"title":"Springtide Ventures","url":"https://app.dealroom.co/investors/springtide_ventures"},{"title":"pocitame s uspechem kazde nasi firmy rika manazer komarkova vc fondu","url":"h
… [1789 more characters]
```
</details>

→ `Bash` — Fetch KKCG Springtide page and Lupa tag
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.kkcg.com/en/springtide-ventures https://kkcg.apploud.cz/en/springtide-ventures https://www.lupa.cz/n/springtide/ 2>&1 | grep -v REPLACE; $PY bin/show.py https://www.kkcg.com/en/springtide-ventures 0 2500; echo; $PY bin/show.py https://www.lupa.cz/n/springtide/ 0 100; $PY bin/grep.py https://www.lupa.cz/n/springtide/ "Springtide" 200 | head -8
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=utf-8 https://kkcg.com/en/our-businesses/energy  len=3665
[redacted: local path]  000  https://kkcg.apploud.cz/en/springtide-ventures  len=0
[redacted: local path]  200 text/html; charset=utf-8 https://www.lupa.cz/n/springtide/  len=2675
Energy | Energy and energy infrastructure is a core pillar of KKCG’s business. Decades of operating critical energy assets have provided KKCG with the deep operational and commercial know-how to grow our companies across the broader value chain. | Strengthening the energy value chain | We implement environmentally-friendly practices which contribute to energy self-sufficiency from traditional and renewable sources. | MND Group | MND Group is building on its century-plus expertise in oil and gas to reimagine how the energy industry meets the needs of the 21st century.  Alongside its extensive operations in exploration, oil and natural gas production, drilling, storage and distribution, MND Group is also active in renewable energy.  Active in the Czech Republic, Austria, Ukraine and Germany, the group is a key player in Europe. | Explore MND Group | Diverse fields of business | Energy Sources | With its traditional focus on oil and natural gas exploration, MND has rapidly evolved to meet the energy demands of the 21st century in recent years. MND sees stron
… [2830 more characters]
```
</details>

→ `Bash` — Find Lupa Springtide article link
```sh
cd [redacted: local path] && grep -o 'href="[^"]*komarek-investuje-250[^"]*"' pages/4dc72454fc33d13e.raw | head -1
```

<details><summary>result</summary>

```
href="/aktuality/komarek-investuje-250-milionu-do-dvou-izraelskych-sitovych-a-bezpecnostnich-startupu/"
```
</details>

→ `Bash` — Read Lupa article on Springtide 2022 deals
```sh
cd [redacted: local path] && PY=[redacted: local path] U=https://www.lupa.cz/aktuality/komarek-investuje-250-milionu-do-dvou-izraelskych-sitovych-a-bezpecnostnich-startupu/; $PY bin/get.py $U >/dev/null; $PY bin/grep.py $U "Springtide působí jako vedoucí fond" 400 | head -2; $PY bin/grep.py $U "27\. ?4\. ?2022|dubna 2022" 80 | head -3
```

<details><summary>result</summary>

```
... lských síťových a bezpečnostních startupů Jan Sedlák 27. 4. 2022 přidejte názor Sdílet Sdílejte na Facebooku Sdílejte na síti X Autor: Depositphotos – Spectral Ilustrační obrázek Přidat mezi oblíbené zdroje na Googlu Český fond Springtide Ventures spadající do skupiny KKCG Karla Komárka investoval 250 milionů korun do dvou izraelských startupů zaměřených na kybernetickou bezpečnost a správu sítí. Springtide působí jako vedoucí fond v rámci investic do Source Defense a NetOp.Cloud . První jmenovaný startup v rámci series B posbíral 27 milionů dolarů. Druhý v kole seed dosáhl na 4,5 milionu dolarů. KKCG dle svých slov jako vedoucí investor získala “významné podíly” a v případě Source Defense také místo v představenstvu. Obsadil ho technický ředitel Springtide Karel Tušek . KKCG má se zkušenostmi v Izraeli zkušenosti, napříkla ...

... e 250 milionů do dvou izraelských síťových a bezpečnostních startupů Jan Sedlák 27. 4. 2022 přidejte názor Sdílet Sdílejte na Facebooku Sdílejte na síti X Autor: Depositph ...

[1 matches, meta=['200 text/html; charset=utf-8 https://www.lupa.cz/aktuality/komarek-investuje-250-milionu-do-dvou-izraelskych-sitovych-a-bezpecnostnich-startupu/']]
```
</details>

→ `WebSearch` UP21 Karlín inkubátor Janeček Šubert investice startup podíl STAR21 fond

<details><summary>result</summary>

```
Web search results for query: "UP21 Karlín inkubátor Janeček Šubert investice startup podíl STAR21 fond"

Links: [{"title":"UP21 Karla Janečka a Víta Šuberta spustí nový investiční fond. Do každého startupu vloží až 1,5 milionu eur","url":"https://cc.cz/up21-karla-janecka-a-vita-suberta-spusti-novy-investicni-fond-do-kazdeho-startupu-vlozi-az-15-milionu-eur/"},{"title":"Karel Janeček","url":"https://cc.cz/tag/karel-janecek/"},{"title":"podcast up21 subert","url":"https://forbes.cz/podcast-up21-subert/"},{"title":"cc.cz","url":"https://cc.cz/tag/star21/"},{"title":"rict si o penize je umeni nejvetsi chyby ktere pri tom founderi opakuji","url":"https://forbes.cz/rict-si-o-penize-je-umeni-nejvetsi-chyby-ktere-pri-tom-founderi-opakuji/"},{"title":"cc.cz","url":"https://cc.cz/tag/up21/"},{"title":"Miliardář Karel Janeček spouští v Karlíně startupový inkubátor s palebnou silou 700 milionů","url":"https://cc.cz/miliardar-karel-janecek-spousti-startupovy-inkubator-s-palebnou-silou-700-milionu/"},{"title":"Miliardář Karel Janeček spouští v Karlíně startupový inkubátor s palebnou silou 700 milionů","url":"https://cc.cz/2016/04/miliardar-karel-janecek-spousti-startupovy-inkubator-s-palebnou-silou-700-milionu/"},{"title":"Karel Janeček: Fungování společnosti se musí změnit. Klíčovou roli sehrají startupy i technologie","url":"https://cc.cz/2019/04/karel-janecek-fungovani-spolecnosti-se-musi-zmenit-klicovou-roli-sehraji-startupy-i-technologie/"},{"title":"Download Our List of The Top 100
… [1489 more characters]
```
</details>

→ `Bash` — Check UP21 news dates and register entities
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://cc.cz/tag/up21/ >/dev/null; $PY bin/show.py https://cc.cz/tag/up21/ 0 3000; UA="Mozilla/5.0"; for n in UP21 GistinUp "UP 21"; do echo "== $n"; curl -sL --max-time 30 -A "$UA" -G "https://or.justice.cz/ias/ui/rejstrik-\$firma" --data-urlencode "nazev=$n" | grep -o 'subjektId=[0-9]*' | sort -u | head -5 | tr '\n' ' '; echo; done
```

<details><summary>result</summary>

```
UP21 - CzechCrunch | Přejít k obsahu | | | Přejít k hlavnímu menu | | | Přejít k vyhledávání | UP21 | Insider | České Spaceflow nabírá na digitalizaci budov 41 milionů korun. Investici vedou Credo Ventures, připojil se i UP21 | 06. 8. 2019 | – | Ondřej Holzman | Digitalizace budov je ve světě nemovitostí velké téma. Také budovy, kancelářské prostory a další objekty se začínají stávat chytrými a s nasazováním technologií pomáhá… | Insider | Umělá inteligence i big data. Startupové trendy podle Martina Rozhoně, Ondřeje Fryce či Credo Ventures | 31. 7. 2019 | – | Václav Bedřich | Umělá inteligence, strojové učení, big data, proptech nebo fintech. Výčet několika oborů, do kterých se ve velkém pouštějí nové startupy s cílem uspět na… | UP21 Karla Janečka a Víta Šuberta spustí nový investiční fond. Do každého startupu vloží až 1,5 milionu eur | 18. 3. 2019 | – | Václav Bedřich | Karlínský startupový inkubátor UP21, za kterým stojí miliardář Karel Janeček a Vít Šubert, se po čtyřech letech fungování a 18 startupech v portfoliu pouští… | Martin Vápeník z UP21: Financování startupů je snazší než kdy dřív. S investory si vylaďte očekávání | 20. 2. 2019 | – | Martin Vápeník | Startupový trh se těší velké popularitě i mezi investory, kteří se dříve zaměřovali spíše na tradiční odvětví. Proto mají začínající projekty možnosti financování jako… | Martin Vápeník z UP21: Začínající startupy neumí odhadnout náklady a dojít si pro radu. To jim škodí | 09. 1. 2019 | – | Martin Vápeník | Podhodn
… [1567 more characters]
```
</details>

→ `Bash` — Show UP21 register hit
```sh
cd [redacted: local path] && PY=[redacted: local path] U="https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1212208&typ=UPLNY"; $PY bin/get.py "$U" >/dev/null; $PY bin/show.py "$U" 0 1500
```

<details><summary>result</summary>

```
Veřejný rejstřík a Sbírka listin - Ministerstvo spravedlnosti České republiky | Nový portál pro obchodní rejstřík a evidenci sveřenských fondů, který běží v ověřovacím provozu, se aktuálně upravuje. | Úplný výpis | z | obchodního rejstříku | UP 211 s.r.o. | , | C | 389283 | vedená u | Městského soudu v Praze | Vytisknout | Úplný výpis | z | obchodního rejstříku, vedeného | Městským soudem v Praze | oddíl | C | , vložka | 389283 | Datum vzniku a zápisu: | 16. srpna 2023 | Spisová značka: | C 389283 vedená u Městského soudu v Praze | zapsáno 16. srpna 2023 | Obchodní firma: | UP 211 s.r.o. | zapsáno 16. srpna 2023 | Sídlo: | Varšavská 715/36, Vinohrady, 120 00  Praha 2 | zapsáno 16. srpna 2023 | Identifikační číslo: | 196 | 20 | 021 | zapsáno 16. srpna 2023 | Právní forma: | Společnost s ručením omezeným | zapsáno 16. srpna 2023 | Předmět podnikání: | Výroba, obchod a služby neuvedené v přílohách 1 až 3 živnostenského zákona | - zprostředkování obchodu a služeb | - velkoobchod a maloobchod | - údržba motorových vozidel a jejich příslušenství | - pronájem a půjčování věcí movitých | - poradenská a konzultační činnost, zpracování odborných studií a posudků | - reklamní činnost, marketing, mediální zastoupení | zapsáno 16. srpna 2023 | Statutární orgán: | Jednatel: | RAFAŁ NOGA | , dat. nar. | 28. září 1988 | 30-698  Krakov, Adama Krzyżanowskiego 14B, Polská republika | Den vzniku funkce: | 16. srpna 2023 | zapsáno 16. srpna 2023 | Počet členů: | 1 | zapsáno 16. srpna 2023 | Způso
```
</details>

→ `Bash` — Fetch RockawayX site pages
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://rockawayx.com/ https://rockawayx.com/portfolio https://rockawayx.com/venture https://rockawayx.com/news 2>&1 | grep -v REPLACE; $PY bin/show.py https://rockawayx.com/ 0 2500
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=utf-8 https://rockawayx.com/  len=2809
[redacted: local path]  404 text/html; charset=utf-8 https://rockawayx.com/portfolio  len=85
[redacted: local path]  404 text/html; charset=utf-8 https://rockawayx.com/venture  len=85
[redacted: local path]  404 text/html; charset=utf-8 https://rockawayx.com/news  len=85
RockawayX | Wheel Picker - Rockaway X | // We run blockchains and provide liquidity to fuel protocols. | // We run blockchains and provide liquidity to fuel protocols. | Introducing Catapult: RockawayX's Accelerator Providing Incubation, Liquidity and Curation to RWAs. | // Investments | Venture and yield strategies | Engineering the future with bold founders | // Liquidity | On-chain capital solutions | Solver powering intent-based protocols | // Infrastructure | Validators and mainnet-ready hardware | Accelerating the Solana network since 2020 | The best | investors | are | builders | . We actively | collaborate | with our portfolio projects. | // Investments | Long-held convictions, and the network to show for it | We invest in early-stage projects, then build alongside them. We were seed backers of Solana and continue to expand, with 15+ of the ecosystem’s leading projects in our portfolio. Our engineers contribute on-chain code dai
… [1550 more characters]
```
</details>

→ `WebSearch` RockawayX leads seed round 2025 OR 2026 equity startup raises

<details><summary>result</summary>

```
Web search results for query: "RockawayX leads seed round 2025 OR 2026 equity startup raises"

Links: [{"title":"Portfolio Companies","url":"https://seedtable.com/investors/rockawayx"},{"title":"RockawayX Research","url":"https://f4.fund/firms/rockawayx"},{"title":"adam bilko","url":"https://www.vcsheet.com/who/adam-bilko"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/rockaway-blockchain"},{"title":"globallegalchronicle.com","url":"https://globallegalchronicle.com/?p=232784"},{"title":"superscout.co","url":"https://superscout.co/investor/rockawayx"},{"title":"viktor fischer","url":"https://www.vcsheet.com/who/viktor-fischer"},{"title":"www.cbinsights.com","url":"https://www.cbinsights.com/company/rockawayx/financials"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/investor/rockawayx"}]

I found no 2025 or 2026 seed round led by RockawayX in these results. The closest matches are a 2024 seed deal, a 2026 Series A, and 2025–2026 seed rounds where it only co-invested.

- **Schuman Financial (seed lead, likely 2024):** A cited article says Schuman Financial has closed a €7 million seed round led by RockawayX. The article's image path points to December 2024, so this is probably older than your window.
- **2026 Series A rounds (lead, not seed):** One tracker lists RockawayX as lead on OnReMay May 2026 Series A and BetHog in April 2026 at Series A.
- **2025–2026 seed rounds (co
… [1031 more characters]
```
</details>

→ `Bash` — Look for Schuman Financial funding announcement
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://schuman.io/ https://www.schuman.io/blog https://schuman.io/news 2>&1 | grep -v REPLACE; for u in https://schuman.io/ https://www.schuman.io/blog https://schuman.io/news; do $PY bin/grep.py $u "RockawayX|seed" 200 | head -3; done
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://schuman.io/  len=5228
[redacted: local path]  200 text/html; charset=UTF-8 https://schuman.io/blog/  len=8313
[redacted: local path]  404 text/html; charset=UTF-8 https://schuman.io/news  len=2014
[0 matches, meta=['200 text/html; charset=UTF-8 https://schuman.io/']]
[0 matches, meta=['200 text/html; charset=UTF-8 https://schuman.io/blog/']]
[0 matches, meta=['404 text/html; charset=UTF-8 https://schuman.io/news']]
```
</details>

→ `WebSearch` Schuman Financial €7 million seed RockawayX EURØP stablecoin announcement

<details><summary>result</summary>

```
Web search results for query: "Schuman Financial €7 million seed RockawayX EURØP stablecoin announcement"

Links: [{"title":"schuman financial euro backed stablecoin mica","url":"https://cointelegraph.com/news/schuman-financial-euro-backed-stablecoin-mica"},{"title":"Schuman Financial debuts EURØP, a MiCA-compliant euro stablecoin","url":"https://www.theblock.co/amp/post/328075/schuman-financial-debuts-europ-a-mica-compliant-euro-stablecoin"},{"title":"Financial and Business News","url":"https://financemagnates.com/cryptocurrency/ex-binance-executives-launch-eurp-stablecoin-secure-7-million-round/amp"},{"title":"Schuman Financial debuts EURØP, a MiCA-compliant euro stablecoin","url":"https://www.theblock.co/post/328075/schuman-financial-debuts-europ-a-mica-compliant-euro-stablecoin"},{"title":"Deal Ticker: Kellerhals Carrard Supports Schuman Financial in its EUR 7M Seed Funding","url":"https://kellerhals-carrard.ch/de/deals/deal-ticker-kellerhals-carrard-supports-schuman-financial-in-its-eur-7m-seed-funding"},{"title":"Ex-Binance Executives Launch EURØP Stablecoin, Secure €7 Million Round","url":"https://www.financemagnates.com/cryptocurrency/ex-binance-executives-launch-eurp-stablecoin-secure-7-million-round/"},{"title":"Ex-Binance Executives Launch Euro-Backed Stablecoin Ahead of MiCA Deadline","url":"https://www.unlock-bc.com/?p=133282"},{"title":"Companies & Deals","url":"https://www.unlock-bc.com/en/ex-binance-executives-launch-euro-backed-stablecoin-ahead-of-mica-deadli
… [1917 more characters]
```
</details>

→ `Bash` — Check Schuman blog for funding post
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://schuman.io/blog/ 0 1500; grep -o 'href="https://schuman.io/[^"]*"' pages/6fd3d210647766e7.raw | sort -u | grep -i -E "seed|fund|rais|million|launch" | head
```

<details><summary>result</summary>

```
Schuman Financial | EURØP | Blog | Open Menu | X | LinkedIn | Latest News | European digital-finance firms, joined by Nasdaq-listed etoro, launch Eurøpe Consortium to expand euro-denominated onchain finance | October 5, 2026 | European digital-finance firms, joined by Nasdaq-listed etoro, launch Eurøpe Consortium to expand euro-denominated onchain finance | Schuman Financial, etoro and leading European digital-finance firms have launched the Eurøpe Consortium, an industry coalition focused on expanding adoption of euro-denominated onchain finance | Read More | https://schuman.io/wp-content/uploads/2026/10/europe-consortium-blog-hero-2400x1260-1.png | 2400 | 1260 | Schuman Financial | EURØP | Schuman Financial | EURØP | https://schuman.io/wp-content/uploads/2026/10/europe-consortium-blog-hero-2400x1260-1.png | October 5, 2026 | October 5, 2026 | Schuman Financial Joins Plexo’s Founding Cohort to Bring Regulated Euro Rails to Global Stablecoin Payments | September 1, 2026 | Schuman Financial Joins Plexo’s Founding Cohort to Bring Regulated Euro Rails to Global Stablecoin Payments | Schuman Financial has joined the founding cohort of Plexo, the coordination network for institutional stablecoin clearing, alongside Hercle, TradeVu, Echo Money, Kii Global, Zynta, Zuba and 18 other licensed financial institutions. | Read More | https://schuman.io/wp-content/uploads/2026/09/Blog.png | 1920 | 1080 | Schuman Financial | EURØP | Schuman Financial | EURØP | https://schuman.io/wp-content/
… [78 more characters]
```
</details>

→ `Bash` — List RockawayX site links
```sh
cd [redacted: local path] && PY=[redacted: local path] grep -o 'href="[^"]*"' pages/5dc59d87e9258968.raw | sort -u | grep -v -E "\.(css|js|png|svg|ico|woff)" | head -30
```

<details><summary>result</summary>

```
href="/"
href="/careers"
href="/catapult"
href="/contact"
href="/funds"
href="/infrastructure"
href="/insights"
href="/insights/crypto-market-update-july-2026"
href="/insights/introducing-catapult"
href="/insights/rockawayx-acquires-crypto-focused-hedge-fund-firm-relayer-capital-and-launches-liquid-opportunities-fund"
href="/investments"
href="/liquidity"
href="/privacy-policy"
href="/team"
href="/vaults"
href="${firstInfiniteUrl}"
href="${lastInfiniteUrl}"
href="${source[i].url || "
href="https://cdn.prod.website-files.com"
href="https://fonts.googleapis.com"
href="https://fonts.gstatic.com"
href="https://www.linkedin.com/company/rockawayx/"
href="https://x.com/RockawayX"
```
</details>

→ `Bash` — Fetch RockawayX investments, insights, funds pages
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://rockawayx.com/investments https://rockawayx.com/insights https://rockawayx.com/funds; $PY bin/show.py https://rockawayx.com/investments 0 3000; echo; $PY bin/grep.py https://rockawayx.com/insights "lead|seed|round|invest" 120 | head -10
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=utf-8 https://rockawayx.com/investments  len=530
[redacted: local path]  200 text/html; charset=utf-8 https://rockawayx.com/insights  len=2097
[redacted: local path]  200 text/html; charset=utf-8 https://rockawayx.com/funds  len=3631
Investments | RockawayX | Building Projects Together | // We don’t throw money at founders and call it a day. We join your team in the trenches. | Sign-up for our newsletter | Your email address | I  agree to receive correspondence from RockawayX and have read the | privacy policy. | Thank you for signing up for our newsletter. | Oops! Something went wrong while submitting the form. | Home | Investments | Liquidity | Infrastructure | Team | Insights | Funds | Careers | Contact us | © 2026 Blockad s.r.o. | RockawayX (previously Rockaway Blockchain Fund) | Privacy

... Insights | RockawayX RockawayX Media Research Investments News Liquidity Vault Curation Infra Events ‍ ‍ Investments Introducing Catapult September 24, 2026 ‍ ‍ News Rockaw ...

... Insights | RockawayX RockawayX Media Research Investments News Liquidity Vault Curation Infra Events ‍ ‍ Investments Introducing Catapult September 24, 2026 ‍ ‍ News RockawayX acquires crypto-focused hedge fund firm, Relayer Capita ...

... 16, 2026 ‍ ‍ Research Crypto Market Update - June 2026 July 13, 2026 ‍ ‍ Vault
… [682 more characters]
```
</details>

→ `Bash` — Fetch RockawayX BetHog and OnRe posts
```sh
cd [redacted: local path] && PY=[redacted: local path] grep -o 'href="/insights/[^"]*"' pages/3553802b5e238896.raw | sort -u | grep -i -E "bethog|onre|invest" ; for s in our-investment-in-bethog-an-ai-native-gaming-platform rockawayx-and-forward-industries-co-lead-strategic-investment-in-onre; do $PY bin/get.py https://rockawayx.com/insights/$s; done
```

<details><summary>result</summary>

```
href="/insights/bringing-onres-onyc-to-ethereum-with-onre-core-vault"
href="/insights/onre-brings-reinsurance-yield-to-ethereum-through-accountable-vault"
href="/insights/our-investment-in-bethog-an-ai-native-gaming-platform"
href="/insights/rockawayx-and-forward-industries-co-lead-strategic-investment-in-onre"
href="/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure"
[redacted: local path]  200 text/html; charset=utf-8 https://rockawayx.com/insights/our-investment-in-bethog-an-ai-native-gaming-platform  len=8214
[redacted: local path]  200 text/html; charset=utf-8 https://rockawayx.com/insights/rockawayx-and-forward-industries-co-lead-strategic-investment-in-onre  len=6198
```
</details>

→ `Bash` — Show BetHog and OnRe post text
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://rockawayx.com/insights/our-investment-in-bethog-an-ai-native-gaming-platform 0 1600; echo; $PY bin/show.py https://rockawayx.com/insights/rockawayx-and-forward-industries-co-lead-strategic-investment-in-onre 0 1500
```

<details><summary>result</summary>

```
Our Investment in BetHog: An AI-Native Gaming Platform | Our Investment in BetHog: An AI-Native Gaming Platform | Bart Hillerich | News | Investments | Our firm's mandate is to back category-defining businesses that leverage crypto rails to reshape real-world markets. | Over the past year, we've done that largely across the onchain yield stack of DeFi protocols, infrastructure, and tokenization-focused teams. Today, we're extending into real-money gaming, an adjacent category representing one of the largest and most durable consumer markets in the world. | We're excited to announce our investment in | BetHog | , a consumer platform pioneering AI-driven experiences in real-money gaming. | A Product-Led Thesis in a Marketing-Led Category | Real-money gaming is one of the largest, most durable online consumer categories. It's also a category that has been missing product-led innovation. Historically, incumbents have competed on marketing spend and bonus economics, instead of the experiences users actually interact with. And they tend to run the same third-party games with different branding, invest disproportionately in acquisition over product, and offer minimal differentiation at the player layer. | We see this as an asymmetric opportunity. | If a team inverted the ratio and invested in a genuinely differentiated product instead of working to outspend competitors on marketing, it could compound on lower CAC, higher retention, and organic growth. And if that team focused on ble
… [1602 more characters]
```
</details>

→ `Bash` — List RockawayX insights and dates in posts
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://rockawayx.com/insights 0 2100; echo; $PY bin/grep.py https://rockawayx.com/insights/rockawayx-and-forward-industries-co-lead-strategic-investment-in-onre "2026" 80 | head -3; $PY bin/grep.py https://rockawayx.com/insights/our-investment-in-bethog-an-ai-native-gaming-platform "2026|Series|round|led" 100 | head -4
```

<details><summary>result</summary>

```
Insights | RockawayX | RockawayX Media | Research | Investments | News | Liquidity | Vault Curation | Infra | Events | ‍ | ‍ | Investments | Introducing Catapult | September 24, 2026 | ‍ | ‍ | News | RockawayX acquires crypto-focused hedge fund firm, Relayer Capital, and launches Liquid Opportunities Fund | August 25, 2026 | ‍ | ‍ | Research | Crypto Market Update - July 2026 | August 19, 2026 | ‍ | ‍ | Vault Curation | Case Study: How RockawayX Helped Fill Tori Finance’s $50M Ecosystem Vault Within Days | July 16, 2026 | ‍ | ‍ | Research | Crypto Market Update - June 2026 | July 13, 2026 | ‍ | ‍ | Vault Curation | RockawayX Tori Ecosystem Vault: Investment Thesis & Risk Disclosure | June 15, 2026 | ‍ | ‍ | Vault Curation | Introducing the RockawayX-Curated Huma USDC Main Vault on Morpho | June 11, 2026 | ‍ | ‍ | Research | Crypto Market Update - May 2026 | June 10, 2026 | ‍ | ‍ | Vault Curation | OnRe Brings Reinsurance Yield to Ethereum Through Accountable Vault | June 9, 2026 | ‍ | ‍ | Vault Curation | RockawayX: Curating Capital Flows | June 4, 2026 | ‍ | ‍ | Vault Curation | Bringing OnRe’s ONyc to Ethereum With OnRe Core Vault | June 3, 2026 | ‍ | ‍ | News | Welcoming David Shang to RockawayX | May 26, 2026 | ‍ | ‍ | Research | Crypto Market Update - April 2026 | May 21, 2026 | ‍ | ‍ | Liquidity | The Liquidity Problem Holding Back RWA Growth | May 19, 2026 | ‍ | ‍ | Vault Curation | RockawayX Vault Curation: An Overview of Products & Capabilities | May 19, 2026 | ‍ | ‍
… [1373 more characters]
```
</details>

→ `Bash` — Show RockawayX funds page
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://rockawayx.com/funds 0 3700
```

<details><summary>result</summary>

```
Funds | Proven Track-Record | // Our funds offer investors varied exposure to the fast growing digital asset space. | RockawayX Liquid Opportunities Fund | [Active] | A fundamentals-driven, directional long/short fund, actively managed to take advantage of crypto market volatility. | Focus on liquid tokens and listed crypto-related equities. Thesis-driven underwriting, complemented by crypto-native analysis of market structure, liquidity, flows, technicals, and sentiment positioning. | //Fund type | Open ended | //Liquidity | Monthly | //Management Fee | 2.0% p.a. | //Performance Fee | 20% | //Fund Administrator | NAV Consulting | //Subscriptions | Monthly — min. USD 500,000 | //Redemptions | Quarterly with 30 days' notice, 1-year soft lock-up (5% fee for redemptions in under 1-year) | //Jurisdiction | Cayman Island | //Regulator | CIMA | //Liquidity Protections | 1 Year Soft Lockup (5% early withdrawal fee) | //Currency | USD | //Requirements | For qualified investors only | //Approved for distribution | Global | Request further information | RockawayX Market Neutral Fund | [Active] | This fund provides capital to digital asset protocols and companies. The strategy has been operated since April 2022 and has delivered 42.59% absolute return inception to date, net of fees. The fund provides monthly liquidity. The team’s unique combination of traditional credit investing acumen and engineering expertise allow it to implement its mandate within a growing opportunity set, and mai
… [2199 more characters]
```
</details>

→ `Bash` — Check CVCA member detail page and membership quotes
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://cvca.cz/en/credo-ventures-2/ >/dev/null; $PY bin/grep.py https://cvca.cz/en/credo-ventures-2/ "Full members|Associate" 100 | head -3; $PY bin/grep.py https://www.cvca.cz/en/members/ "(Credo Ventures|Depo Ventures|i&i Biotech Investments|Inven Capital|KAYA  ?VC|Nation1|Orbit Capital|Tensor Ventures) dk [0-9. ]+ Full members" 0
```

<details><summary>result</summary>

```
[0 matches, meta=['200 text/html; charset=UTF-8 https://cvca.cz/en/credo-ventures-2/']]
... Credo Ventures dk 14. 1. 2020 Full members ...

... Depo Ventures dk 23. 1. 2020 Full members ...

... i&i Biotech Investments dk 18. 1. 2020 Full members ...

... Inven Capital dk 14. 1. 2020 Full members ...

... KAYA VC dk 16. 10. 2020 Full members ...

... Nation1 dk 14. 1. 2020 Full members ...

... Orbit Capital dk 12. 1. 2020 Full members ...

... Tensor Ventures dk 20. 6. 2023 Full members ...

[8 matches, meta=['200 text/html; charset=UTF-8 https://cvca.cz/en/membership/']]
```
</details>

→ `Bash` — Find Spaceflow/UP21 article URLs
```sh
cd [redacted: local path] && PY=[redacted: local path] U=$(grep -o 'href="https://cc.cz/[^"]*spaceflow[^"]*"' pages/$($PY -c "import hashlib;print(hashlib.sha1(b'https://cc.cz/tag/up21/').hexdigest()[:16])").raw | head -3); echo "$U"
```

<details><summary>result</summary>

```
href="https://cc.cz/cesti-spaceflow-nabiraji-na-digitalizaci-budov-41-milionu-korun-investici-vedou-credo-ventures-pripojil-se-i-up21/"
href="https://cc.cz/cesti-spaceflow-nabiraji-na-digitalizaci-budov-41-milionu-korun-investici-vedou-credo-ventures-pripojil-se-i-up21/"
href="https://cc.cz/cesky-proptech-startup-spaceflow-ziskal-od-inkubatoru-up21-investici-v-jednotkach-milionu-kc/"
```
</details>

→ `Bash` — Read Spaceflow 2019 round article
```sh
cd [redacted: local path] && PY=[redacted: local path] U=https://cc.cz/cesti-spaceflow-nabiraji-na-digitalizaci-budov-41-milionu-korun-investici-vedou-credo-ventures-pripojil-se-i-up21/; $PY bin/get.py $U; $PY bin/grep.py $U "UP21" 200 | head -4; $PY bin/grep.py $U "6\. ?8\. ?2019|2019" 60 | head -2
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://cc.cz/cesti-spaceflow-nabiraji-na-digitalizaci-budov-41-milionu-korun-investici-vedou-credo-ventures-pripojil-se-i-up21/  len=9432
... České Spaceflow nabírá na digitalizaci budov 41 milionů korun. Investici vedou Credo Ventures, připojil se i UP21 - CzechCrunch Přejít k obsahu | Přejít k hlavnímu menu | Přejít k vyhledávání Insider – 06. 8. 2019 – 2 min čtení České Spaceflow nabírá na digitalizaci budov 41 milionů korun. Investici vedou Credo  ...

... obsahu | Přejít k hlavnímu menu | Přejít k vyhledávání Insider – 06. 8. 2019 – 2 min čtení České Spaceflow nabírá na digitalizaci budov 41 milionů korun. Investici vedou Credo Ventures, připojil se i UP21 Ondřej Holzman 0 Zobrazit komentáře Sdílet Insider Foto: Spaceflow Lukáš Balík, spoluzakladatel a CEO Spaceflow Sdílet Uložit 0 0 Zobrazit komentáře Baví vás články CzechCrunche? Vídejte je na Googlu ...

...  | Přejít k hlavnímu menu | Přejít k vyhledávání Insider – 06. 8. 2019 – 2 min čtení České Spaceflow nabírá na digitalizaci budov  ...
```
</details>

→ `Bash` — Show BHM and Czech Founders records in full
```sh
.venv/bin/python - <<'EOF'
import json
recs={r['id']:r for r in json.load(open('data/sample/parts/cz.json'))}
for rid in ['bhm-ventures','czech-founders-vc']:
    print(json.dumps(recs[rid],ensure_ascii=False,indent=1))
print(list(recs['credo-ventures'].keys()), list(recs['credo-ventures']['fields'].keys()))
print(list(recs['air-ventures'].keys()), recs['air-ventures'].get('legal_entities'))
EOF
```

<details><summary>result</summary>

```
{
 "id": "bhm-ventures",
 "name": "BHM Ventures (BHM group)",
 "aliases": [
  "BHM Group"
 ],
 "type": "private_investor",
 "hq": {
  "country": "CZ",
  "city": "Praha"
 },
 "website": null,
 "legal_entities": [
  {
   "name": "BHM Ventures a.s.",
   "role": "manager",
   "id_type": "ICO",
   "id": "05455464",
   "register_url": "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/05455464"
  }
 ],
 "decision": {
  "status": "uncertain",
  "rules": [
   "I2",
   "I3"
  ],
  "note": "Startup arm of Tomáš Krsek's BHM group. Entered as shareholder of Yieldigo and Sharry Europe on the same day (22 May 2025), which may be an internal transfer from BHM Ventures I/II rather than new investments. Website bhm.cz belongs to an unrelated driving school."
 },
 "fields": {},
 "investments": [
  {
   "company": "Yieldigo",
   "date": "2025-05-22",
   "date_kind": "registry_entry",
   "round_size": null,
   "sources": [
    {
     "url": "https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=949426&typ=UPLNY",
     "tier": "A",
     "publisher": "Obchodní rejstřík (justice.cz)",
     "published": "2025-05-22",
     "accessed": "2026-10-11",
     "quote": "Společník: BHM Ventures a.s. , IČ: 054 55 464 Ovocný trh 1096/8, Staré Město, 110 00 Praha 1"
    }
   ]
  },
  {
   "company": "Sharry",
   "date": "2025-05-22",
   "date_kind": "registry_entry",
   "round_size": null,
   "sources": [
    {
     "url": "https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjek
… [2933 more characters]
```
</details>

→ `Bash` — Extract exact portfolio quote spans
```sh
mkdir -p [redacted: local path] && cat > [redacted: local path] <<'EOF'
"""span.py URL START END -> print exact ws-normalised substring from first START to the end of the next END."""
import sys
sys.path.insert(0, "[redacted: local path]")
from get import get
from q import ws
def span(url, start, end):
    t = ws(get(url)[0].read_text())
    i = t.find(start)
    if i < 0: return None
    j = t.find(end, i + len(start) - len(end) if end in start else i)
    if j < 0: return None
    return t[i:j + len(end)]
if __name__ == "__main__":
    s = span(*sys.argv[1:4])
    print(len(s) if s else None); print(s)
EOF
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://cvca.cz/en/membership/ >/dev/null; $PY bin/span.py https://www.prestoventures.com/portfolio "Adam Czechia 2022" "Blindspot Tech"; $PY bin/span.py https://www.reflexcapital.com/portfolio "MADMONQ founders" "Dotidot founders"; $PY bin/span.py https://www.purple-ventures.com/ "TASS Vision brings" "Vetstor creates"; $PY bin/span.py https://www.soulmatesventures.com
… [488 more characters]
```

<details><summary>result</summary>

```
216
Adam Czechia 2022 Current Next-day interior painting services in 15+ countries Required Nest Link Behavio Czechia 2021 Current Ad-testing platform for maximum marketing effectiveness Required Nest Link Blindspot Tech
122
MADMONQ founders More Story Our Heroes Petr Svoboda Shopsys founder More Story Our Heroes Ondra and Pavel Dotidot founders
681
TASS Vision brings "Google Analytics" into brick-and-mortar stores, using edge AI cameras to track customer journeys, optimize shelves, and measure campaign performance – all without sending data to the cloud. With deployments in 2,000+ stores across 10 countries and partnerships with 100+ brands, the traction is undeniable www.tassvision.ai PV 2 | Invested in 2025 Clearly combines video sessions with licensed therapists, 24/7 AI companions, and standalone AI therapy to deliver accessible and effective psychological care for both individuals and businesses. www.clearly.help PV 2 | Invested in 2025 In collaboration with veterinarians and with the help of AI, Vetstor creates
385
Twin Science empowers children with STEM and AI skills to prepare them for the sustainable jobs of the future, driving innovation in education and fostering a new generation of environmentally conscious leaders. Education Youni transforms global education by effortlessly linking students with universities worldwide through its advanced AI-driven platform. Healthcare Signapse employs
661
Get to know Sewio NenoVision Watch NenoVision's story. "Y Soft came to b
… [2997 more characters]
```
</details>

→ `Bash` — Find shortest clean 3-company span on Rockaway page
```sh
cd [redacted: local path] && [redacted: local path] - <<'EOF'
import sys,re
sys.path.insert(0,'bin')
from get import get
from q import ws
t=ws(get('https://rockawayventures.com/for-investors/')[0].read_text())
idx=[m.start() for m in re.finditer(r'Show website ', t)]
names=[]
for i in idx:
    nm=t[i+13:i+13+30].split(' ')[0]
    names.append((i,nm))
best=None
for k in range(len(names)-2):
    a=names[k][0]; c=names[k+2][0]+13+len(names[k+2][1])
    s=t[a:c]
    if '​' in s: continue
    if best is None or len(s)<len(best): best=s
print(len(best)); print(best)
EOF
```

<details><summary>result</summary>

```
449
Show website Exited 2018 uLekare.cz uLekare.cz is the largest Czech on-line medical clinic and a pioneer in the field of telemedicine, and aims to streamline and improve Czech healthcare. A team of more than 300 doctors, including dozens of specialists, serves an average of 2500 users per month. Exited back to the founders in 2018. Show website Exited 2018 Dreadlocks Dreadlocks is a gaming studio for console and mobile games. Show website Exited
```
</details>

→ `Bash` — Extract CulturePulse-to-Valpas span
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/span.py https://rockawayventures.com/for-investors/ "Show website CulturePulse" "Show website Valpas" | python3 -c "import sys;s=sys.stdin.read();print(s);print('ZW' if '​' in s else 'clean')"
```

<details><summary>result</summary>

```
896
Show website CulturePulse Deep tech company that uses AI to simulate and predict human behavior in real time. By combining insights from psychology, linguistics, and machine learning, their platform helps companies and institutions understand cultural dynamics and audience responses across markets. Their technology is used in sectors such as media, policy, and crisis communication, enabling smarter decisions through behavioral modeling. Show website Cruxo Cruxo.io is a data-driven platform that simplifies and optimizes retail media management for e-commerce businesses. It enables automated campaign management at scale, maximizing on-site ad revenue and enhancing ad relevance for customers. Backed by Rockaway Ventures and Czech Founders VC, Cruxo has secured funding to expand internationally. Key clients include major e-shops like Dr. Max, Astratex, and Lékárna.cz. Show website Valpas

clean
```
</details>

→ `Bash` — Check publisher conventions for EIF/SLOVCA/SIH sources
```sh
grep -h -B3 -A3 'eif.org/files' data/sample/parts/*.json | grep -E '"(publisher|published|quote)"' | head -12; grep -h -A4 'slovca.sk' data/sample/parts/sk.json | grep -E 'publisher|published' | head -4; grep -h -A4 'sih.sk/en' data/sample/parts/*.json | grep -E 'publisher|published|tier' | head -4
```

<details><summary>result</summary>

```
            "publisher": "European Investment Fund",
            "published": null,
            "publisher": "European Investment Fund",
            "published": null,
            "publisher": "European Investment Fund",
            "published": null,
            "quote": "Tensor Ventures GP S.à r.l. & Tensor Ventures Fund I SCSp"
            "publisher": "European Investment Fund",
            "published": null,
            "publisher": "European Investment Fund",
            "published": null,
            "publisher": "SLOVCA",
            "published": null,
            "publisher": "SLOVCA",
            "published": null,
            "tier": "B",
            "publisher": "Slovak Investment Holding",
            "published": "2024-05-28",
```
</details>

**Agent:**

Now I'll fetch the ESMA records and build the full existence spec.

→ `Bash` — Fetch ESMA register records for Inven and G-Force
```sh
cd [redacted: local path] && PY=[redacted: local path] for id in ae15502 ae42928; do $PY bin/get.py "https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=id:$id&wt=json"; done; $PY bin/show.py "https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=id:ae15502&wt=json" 0 1500
```

<details><summary>result</summary>

```
[redacted: local path]  200 application/json;charset=utf-8 https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=id:ae15502&wt=json  len=1387
[redacted: local path]  200 application/json;charset=utf-8 https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=id:ae42928&wt=json  len=1348
{ |   "responseHeader":{ |     "status":0, |     "QTime":62, |     "params":{ |       "q":"id:ae15502", |       "wt":"json"}}, |   "response":{"numFound":1,"start":0,"numFoundExact":true,"docs":[ |       { |         "id":"ae15502", |         "ae_entityTypeCode":"AIF", |         "ae_lastUpdate":"2025-03-14T00:00:00Z", |         "ae_lastUpdateStr":"14/03/2025", |         "ae_lei":"8945003C8OZTS2ORXY18", |         "ae_headOfficeLei":"", |         "ae_entityName":"Inven Capital, SICAV, a.s.", |         "collectorParent":["Inven Capital, SICAV, a.s."], |         "ae_officeType":"Head office", |         "ae_competentAuthority":"Czech National Bank (CNB)", |         "ae_homeMemberState":"CZECHIA", |         "ae_hostMemberState":"", |         "ae_headOfficeAddress":"Pod křížkem 1773/2, Braník, 147 00 Praha 4", |         "ae_branchAddress":"", |         "ae_comment":"", |         "ae_status":"Active", |         "ae_authorisationNotificationDate":"2016-09-01T00:00:00Z", |         "ae_authorisationNotificationDateStr":"01/09/2016", |         "ae_authorisationWithdrawalEndDateStr":"", |
… [374 more characters]
```
</details>

→ `Bash` — Build and verify existence evidence spec
```sh
cat > [redacted: local path] <<'EOF'
"""Build existence fields with verified verbatim quotes -> spec/existence.json"""
import json, sys
sys.path.insert(0, "[redacted: local path]")
from span import span
from q import check

ACC = "2026-10-11"
CVCA = "https://cvca.cz/en/membership/"
SLOVCA = "https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html"
EIF_CZ = "https://www.eif.org/files/attachments/czechia-equity-fundmanagers.pdf"
EIF_SK = "https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf"
SIH = "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/"
NBS = "https://subjekty.nbs.sk/sk/entity/"
ESMA = "https://registers.esma.europa.eu/solr/esma_registers_upreg/select?q=id:{}&wt=json"

def S(url, tier, publisher, quote=None, start=None, end=None, published=None):
    if quote is None:
        quote = span(url, start, end)
        assert quote, (url, start, end)
    return {"url": url, "tier": tier, "publisher": publisher, "published": published,
            "accessed": ACC, "quote": quote}

def cvca(name):
    return S(CVCA, "B", "CVCA", start=name + " dk ", end="Full members
… [8490 more characters]
```

<details><summary>result</summary>

```
Exit code 1
Traceback (most recent call last):
  File "[redacted: local path]", line 86, in <module>
    E["reflex-capital"] = [("portfolio_page", S("https://www.reflexcapital.com/portfolio/", "B", "Reflex Capital", start="MADMONQ founders", end="Dotidot founders"))]
                                              ~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "[redacted: local path]", line 19, in S
    assert quote, (url, start, end)
           ^^^^^
AssertionError: ('https://www.reflexcapital.com/portfolio/', 'MADMONQ founders', 'Dotidot founders')
```
</details>

→ `Bash` — Recheck final URLs for Reflex, ZAKA, Y Soft
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/get.py https://www.reflexcapital.com/portfolio/; $PY bin/show.py https://www.reflexcapital.com/portfolio/ 0 600; $PY bin/get.py https://zaka.vc/portfolio/; $PY bin/get.py https://www.ysoft.com/ventures
```

<details><summary>result</summary>

```
[redacted: local path]  200 text/html; charset=UTF-8 https://www.reflexcapital.com/portfolio/  len=10317
OUR INVESTMENTS × Reflex Capital | Reflex Capital | Menu | OUR INVESTMENTS | Power Team | In media | Contact | Blog | OUR INVESTMENTS | We invest into people. It’s the founders, who carry the biggest responsibility. Their courage, abilities, and ambition to change the world is what we bet on. | Our Heroes | Scott Schreiman | Co-founder & CEO Samepage | More Story | Our Heroes | Jakub and Honza | Founders Apify | More Story | Our Heroes | Petr and Ondra | Smartlook founders | More Story | Our Heroes | Honza | Contember founder | More Story | Our Heroes | Lukas, Stanislav, Michael | signageOS fo
[redacted: local path]  200 text/html; charset=UTF-8 https://zaka.vc/portfolio/  len=12795
[redacted: local path]  200 text/html; charset=UTF-8 https://www.ysoft.com/ventures  len=8795
```
</details>

→ `Bash` — Show Reflex Capital homepage text
```sh
cd [redacted: local path] && PY=[redacted: local path] $PY bin/show.py https://www.reflexcapital.com/ 0 4400
```

<details><summary>result</summary>

```
Reflex Capital | Reflex Capital | Menu | OUR INVESTMENTS | Power Team | In media | Contact | Blog | WHY REFLEX? | Doing business may resemble a jungle survival. You better be prepared and have the right reflexes! It’s also useful to have someone with real experience around. We at Reflex Capital are entrepreneurs, just like you. We built our own companies, negotiated with investors, and took part in plenty of transactions. | €150M invested | TRUSTING DNA | We managed our own companies and sought investments ourselves. We're partners, not bankers. We share the same DNA. | TRUSTING SMILES | We'll stand by you in good times and bad. It's not always easy, but everything is easier with a smile. Stress is not a good driver. | TRUSTING PEOPLE | Rather than business models, personalities of the founders play key role in our investments. We have to feel we are on the same vibe! | TRUSTING GUTS | We believe in the power of making decisions based on instincts. Those who stand still for too long are out of the game. We act on what we feel is right. | OUR FOUNDERS | These are the people that have convinced us, and we convinced them. These are our founders. And we'll do our utmost for their success. | Jakub a Honza | zakladatelé Apify | Vladimir and Dusan | Rene Morkos | CEO Alice Technologies | Daniel, Radek, Nicolas | SENS founders | Alexander and Simon | byways founders | Karin | Digitoo founder | Ondra and Pavel | Dotidot founders | David and Samuel | Shrooly founders | Václav, Oskar, J
… [2899 more characters]
```
</details>

→ `Bash` — Test stability of Reflex page ordering
```sh
cd [redacted: local path] && PY=[redacted: local path] for i in 1 2; do $PY bin/get.py -f https://www.reflexcapital.com/ >/dev/null; $PY bin/show.py https://www.reflexcapital.com/ 1050 1300; echo; done; for i in 1 2; do $PY bin/get.py -f https://www.reflexcapital.com/portfolio/ >/dev/null; $PY bin/show.py https://www.reflexcapital.com/portfolio/ 300 450; echo; done
```

<details><summary>result</summary>

```
. | OUR FOUNDERS | These are the people that have convinced us, and we convinced them. These are our founders. And we'll do our utmost for their success. | Max Verteletskyi | Co-founder & CEO Spaceti | Alexander Leichter | Founder & CEO BYRD | Karel

. | OUR FOUNDERS | These are the people that have convinced us, and we convinced them. These are our founders. And we'll do our utmost for their success. | Ondrej and Jiri | VOS.health founders | Karel and Lada | Product Fruits founders | Jakub | Flo

Heroes | Vlastimil, Jan | Leadspicker founders | More Story | Our Heroes | Václav, Oskar, Jiří a Artem | More Story | Our Heroes | Veronika Allister |

Heroes | Ondrej and Jiri | VOS.health founders | More Story | Our Heroes | Vit Jezek | Founder & CEO Rekola | More Story | Our Heroes | Zdenek and Pav
```
</details>

→ `Bash` — Check stability of Reflex in-media section
```sh
cd [redacted: local path] && PY=[redacted: local path] for i in 1 2 3; do $PY bin/get.py -f https://www.reflexcapital.com/ >/dev/null; $PY bin/span.py https://www.reflexcapital.com/ "IN MEDIA" "Keboola raises \$4.5M" | tail -1 | md5; done
```

<details><summary>result</summary>

```
c585cc8a6648924389f63881c9bd2273
c585cc8a6648924389f63881c9bd2273
c585cc8a6648924389f63881c9bd2273
```
</details>

→ `Bash` — Rebuild existence spec with Reflex fix
```sh
cd [redacted: local path] && [redacted: local path] - <<'EOF'
p='bin/build_existence.py'
s=open(p).read()
s=s.replace('''E["reflex-capital"] = [("portfolio_page", S("https://www.reflexcapital.com/portfolio/", "B", "Reflex Capital", start="MADMONQ founders", end="Dotidot founders"))]''',
'''E["reflex-capital"] = [("portfolio_page", S("https://www.reflexcapital.com/", "B", "Reflex Capital", start="Sony, signage OS partner", end="Productboard Raises $125 Million in New Round"))]''')
open(p,'w').write(s)
EOF
PY=[redacted: local path] $PY bin/build_existence.py
```

<details><summary>result</summary>

```
33 records; BAD: []
neulogy-ventures ['fund_of_funds_commitment', 'association_full_member'] [74, 95, 182]
vision-ventures ['regulator_register', 'fund_of_funds_commitment', 'association_full_member'] [336, 79, 238]
venture-to-future-fund ['regulator_register', 'association_full_member'] [103, 222]
zero-one-hundred ['regulator_register', 'fund_of_funds_commitment'] [376, 84]
g-force ['regulator_register'] [551]
cb-investment-management ['regulator_register', 'fund_of_funds_commitment'] [349, 88]
seed-starter-slovenskej-sporitelne ['portfolio_page'] [195]
fond-inovacii-a-technologii ['regulator_register', 'association_full_member'] [419, 103]
limerock ['regulator_register', 'fund_of_funds_commitment'] [508, 123]
365-fintech ['portfolio_page'] [249]
credo-ventures ['association_full_member'] [42]
presto-ventures ['portfolio_page'] [216]
reflex-capital ['portfolio_page'] [209]
jt-ventures ['portfolio_page'] [45]
tilia-impact-ventures ['fund_of_funds_commitment'] [84]
kaya-vc ['fund_of_funds_commitment', 'association_full_member'] [55, 36]
lighthouse-ventures ['fund_of_funds_commitment'] [101]
zaka-vc ['portfolio_page'] [53]
purple-ventures ['portfolio_page'] [681]
rockaway-ventures ['portfolio_page'] [896]
tensor-ventures ['fund_of_funds_commitment', 'association_full_member'] [86, 43]
nation-1 ['association_full_member'] [35]
depo-ventures ['fund_of_funds_commitment', 'association_full_member'] [158, 41]
miton ['portfolio_page'] [36]
inven-capital ['regulator_register', 'associ
… [395 more characters]
```
</details>

→ `Bash` — Re-fetch all existence URLs and recheck quotes
```sh
cd [redacted: local path] && cat > bin/recheck.py <<'EOF'
import json, sys
sys.path.insert(0, "[redacted: local path]")
from get import get
from q import check
spec = json.load(open(sys.argv[1]))
urls = set()
items = []
for rid, v in spec.items():
    srcs = v["sources"] if "sources" in v else [s for inv in v.get("investments", []) for s in inv["sources"]]
    for s in srcs:
        urls.add(s["url"]); items.append((rid, s))
for u in sorted(urls):
    get(u, force=True)
bad = [(rid, s["url"], s["quote"][:60]) for rid, s in items if not all(check(s["url"], s["quote"]))]
print(len(items), "quotes rechecked after re-fetch; failures:", bad)
EOF
[redacted: local path] bin/recheck.py spec/existence.json 2>&1 | grep -v REPLACEMENT
```

<details><summary>result</summary>

```
47 quotes rechecked after re-fetch; failures: []
```
</details>

→ `Bash` — Verify quotes for new investment entries
```sh
cd [redacted: local path] && PY=[redacted: local path]
$PY bin/q.py https://rockawayx.com/insights "RockawayX and Forward Industries Co-Lead Strategic Investment in OnRe May 5, 2026"
$PY bin/q.py https://rockawayx.com/insights "Our Investment in BetHog: An AI-Native Gaming Platform April 22, 2026"
$PY bin/q.py https://rockawayx.com/insights/rockawayx-and-forward-industries-co-lead-strategic-investment-in-onre "The two firms co-led OnRe's \$5 million Series A round."
$PY bin/q.py https://rockawayx.com/insights/our-investment-in-bethog-an-ai-native-gaming-platform "We're excited to announce our investment in BetHog , a consumer platform pioneering AI-driven experiences in real-money gaming."
$PY bin/q.py https://cc.cz/ceske-dataddo-ma-ctvrtou-investici-od-miliardare-ondreje-tomka-z-datoveho-startupu-se-stava-globalni-hrac/ "Pražský startup Dataddo teď uzavřel své čtvrté investiční kolo, a to opět od fondu Impulse Ventures."
$PY bin/q.py https://cc.cz/ceske-dataddo-ma-ctvrtou-investici-od-miliardare-ondreje-tomka-z-datoveho-startupu-se-stava-globalni-hrac/ "Startupy – 20. 12. 2023"
$PY bin/q.py https://www.lupa.cz/aktuality/k
… [2044 more characters]
```

<details><summary>result</summary>

```
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
OK ws-exact | norm OK
```
</details>

→ `Bash` — Record baseline counts and back up part files
```sh
.venv/bin/python -c "
import json,collections
r=json.load(open('data/sample/investors.json'));print(len(r),collections.Counter(x['decision']['status'] for x in r))
for c in ['sk','cz']:
  p=json.load(open(f'data/sample/parts/{c}.json'));print(c,len(p),collections.Counter(x['decision']['status'] for x in p))
" ; cp data/sample/parts/sk.json data/sample/parts/cz.json data/sample/parts/sk-decisions.md data/sample/parts/cz-decisions.md [redacted: local path] && ls [redacted: local path]
```

<details><summary>result</summary>

```
91 Counter({'out_of_scope': 26, 'included': 25, 'excluded': 20, 'uncertain': 13, 'dormant': 7})
sk 49 Counter({'excluded': 19, 'out_of_scope': 16, 'included': 7, 'dormant': 6, 'uncertain': 1})
cz 53 Counter({'out_of_scope': 21, 'included': 18, 'uncertain': 12, 'dormant': 1, 'excluded': 1})
cz-decisions.md
cz.json
existence.json
sk-decisions.md
sk.json
```
</details>

→ `Bash` — Detect JSON formatting of part files
```sh
head -c 300 data/sample/parts/sk.json; echo; head -c 200 data/sample/parts/cz.json; echo; tail -c 50 data/sample/parts/cz.json | od -c | tail -3; .venv/bin/python -c "
import json
for c in ['sk','cz']:
  s=open(f'data/sample/parts/{c}.json').read(); d=json.loads(s)
  for ind in (1,2,4):
    print(c, ind, json.dumps(d,ensure_ascii=False,indent=ind)+'\n'==s, json.dumps(d,ensure_ascii=False,indent=ind)==s)
"
```

<details><summary>result</summary>

```
[
  {
    "id": "neulogy-ventures",
    "name": "Neulogy Ventures",
    "aliases": [
      "Neulogy Ventures, a. s.",
      "Neulogy VC",
      "Slovak Venture Fund S.C.A., SICAR"
    ],
    "type": "vc",
    "hq": {
      "country": "SK",
      "city": "Bratislava"
    },
    "website": "https://ww
[
  {
    "id": "credo-ventures",
    "name": "Credo Ventures",
    "type": "vc",
    "hq": {
      "country": "CZ",
      "city": "Praha"
    },
    "website": "https://www.credoventures.com/",
    "
0000040    t   m   e   n   t   s   "   :       [   ]  \n           }  \n
0000060    ]  \n
0000062
sk 1 False False
sk 2 True False
sk 4 False False
cz 1 False False
cz 2 True False
cz 4 False False
```
</details>

→ `Bash` — Apply existence, decisions and investments to part files
```sh
cat > [redacted: local path] <<'EOF'
import json
from pathlib import Path

ROOT = Path("[redacted: local path]")
EX = json.load(open("[redacted: local path]"))
ACC = "2026-10-11"
JUS = "Obchodní rejstřík (justice.cz)"

def src(url, tier, publisher, quote, published=None):
    return {"url": url, "tier": tier, "publisher": publisher, "published": published, "accessed": ACC, "quote": quote}

def inv(company, date, kind, sources, round_size=None):
    return {"company": company, "date": date, "date_kind": kind, "round_size": round_size, "sources": sources}

NO_EXIST = " No I2 evidence (regulator register, fund-of-funds commitment, full association membership or a portfolio page naming 3+ companies) was found, so existence is left empty."

DECISIONS = {
 "startguide": ("included", ["I1", "I2", "I3", "I4"],
  "Was uncertain. Prague VC (Start Guide, s.r.o., fund START GUIDE ONE, a.s.). I2 via its own SG One fund page, which names portfolio companies DTS, BikeFair and Ringil. I3: START GUIDE ONE entered Carebot s.r.o. on 18 Mar 2025 and Ringil on 3 Jul 2024 (justice.cz)."),
 "g
… [11931 more characters]
```

<details><summary>result</summary>

```
unused existence specs: set()
('sk', 'neulogy-ventures', 'included', 'included', True)
('sk', 'vision-ventures', 'included', 'included', True)
('sk', 'venture-to-future-fund', 'included', 'included', True)
('sk', 'zero-one-hundred', 'included', 'included', True)
('sk', 'g-force', 'included', 'included', True)
('sk', 'cb-investment-management', 'included', 'included', True)
('sk', 'seed-starter-slovenskej-sporitelne', 'included', 'included', True)
('sk', 'baryon-fund', 'uncertain', 'uncertain', False)
('sk', 'lrj-capital', 'dormant', 'dormant', False)
('sk', 'ipm-group', 'dormant', 'dormant', False)
('sk', 'fond-inovacii-a-technologii', 'dormant', 'dormant', True)
('sk', 'limerock', 'dormant', 'dormant', True)
('sk', '365-fintech', 'dormant', 'dormant', True)
('sk', 'monogram-ventures', 'dormant', 'dormant', False)
('cz', 'credo-ventures', 'included', 'included', True)
('cz', 'presto-ventures', 'included', 'included', True)
('cz', 'reflex-capital', 'included', 'included', True)
('cz', 'jt-ventures', 'included', 'included', True)
('cz', 'tilia-impact-ventures', 'included', 'included', True)
('cz', 'kaya-vc', 'included', 'included', True)
('cz', 'lighthouse-ventures', 'included', 'included', True)
('cz', 'zaka-vc', 'included', 'included', True)
('cz', 'purple-ventures', 'included', 'included', True)
('cz', 'rockaway-ventures', 'included', 'included', True)
('cz', 'tensor-ventures', 'included', 'included', True)
('cz', 'nation-1', 'included', 'included', True)
('cz', 'depo-ventur
… [1026 more characters]
```
</details>

→ `Bash` — Update changed decision lines in cz-decisions.md
```sh
.venv/bin/python - <<'EOF'
from pathlib import Path
p=Path('data/sample/parts/cz-decisions.md')
s=p.read_text().splitlines()
new={
"- STARTGUIDE —":"- STARTGUIDE — included — I1, I2, I3, I4 — Was uncertain. Prague VC; own SG One page names portfolio companies DTS, BikeFair and Ringil (I2); START GUIDE ONE entered Carebot on 18 Mar 2025 (justice.cz).",
"- GAIN Ventures —":"- GAIN Ventures — excluded — I2 — Was uncertain. Single known holding (Carebot, Mar 2025); no website, portfolio, licence, membership or fund-of-funds commitment, so investing is not shown to be a core activity.",
"- BHM Ventures (BHM group) —":"- BHM Ventures (BHM group) — uncertain — I3 — I2 now shown by the group's portfolio page (13 tech startups); the May 2025 register lines are a rename of Bohemia Venture Capital (same IČ), and the Aug 2025 Carebot stake is held by vehicles not named BHM, so recency rests on press only.",
"- Czech Founders VC —":"- Czech Founders VC — included — I1, I2, I3, I4 — Was uncertain. Self-published portfolio of 30+ startups; fund entered Edmund s.r.o. on 25 Mar 2026 (justice.cz).",
"- KOOPEO Ventures —":"- KOOPEO Ventures — excluded — I2 — Was uncertain. Registered for property ren
… [1350 more characters]
```

<details><summary>result</summary>

```
set()
data/sample/parts/sk-decisions.md:5:Counts: included 7, uncertain 1, dormant 6, excluded 35.
27,30c27,30
< - STARTGUIDE — uncertain — I2 — Prague fund with Tier A holdings in Carebot (Mar 2025) and Ringil (Jul 2024), but no licence, membership or 3+ portfolio found.
< - GAIN Ventures — uncertain — I2 — Prague vehicle that entered Carebot (Mar 2025); no website or portfolio, so investing as a core activity is unproven.
< - BHM Ventures (BHM group) — uncertain — I2, I3 — Tomáš Krsek's startup vehicle; two same-day register entries (May 2025) may be internal transfers, so recency and I2 are unproven.
< - Czech Founders VC — uncertain — I3 — Founder-backed pre-seed fund with a 30+ portfolio; latest Tier A evidence (SharpGrid, Aug 2023) is just outside 36 months.
---
> - STARTGUIDE — included — I1, I2, I3, I4 — Was uncertain. Prague VC; own SG One page names portfolio companies DTS, BikeFair and Ringil (I2); START GUIDE ONE entered Carebot on 18 Mar 2025 (justice.cz).
> - GAIN Ventures — excluded — I2 — Was uncertain. Single known holding (Carebot, Mar 2025); no website, portfolio, licence, membership or fund-of-funds commitment, so investing is not shown to be a core activity.
> - BHM Ventures (BHM group) — uncertain — I3 — I2 now shown by the group's portfolio page (13 tech startups); the May 2025 register lines are a rename of Bohemia Venture Capital (same IČ), and the Aug 2025 Carebot stake is held by vehicles not named BHM, so recency rests on press only.
> - Czech Foun
… [1774 more characters]
```
</details>

**Agent:**

Now merge and validate.

→ `Bash` — Merge parts and validate records
```sh
.venv/bin/python scripts/merge_parts.py && .venv/bin/python -m investordb validate --today 2026-10-11 | tail -15
```

<details><summary>result</summary>

```
Credo Ventures: kept CZ, dropped out_of_scope from SK
Presto Ventures: kept CZ, dropped out_of_scope from SK
J&T Ventures: kept CZ, dropped out_of_scope from SK
ZAKA VC: kept CZ, dropped out_of_scope from SK
N1 (Nation 1): kept CZ, dropped out_of_scope from SK
ARX Equity Partners: kept CZ, dropped out_of_scope from SK
CVI: kept SK, dropped out_of_scope from CZ
Enterprise Investors: kept SK, dropped out_of_scope from CZ
Genesis Capital: kept CZ, dropped out_of_scope from SK
Jet Investment: kept CZ, dropped out_of_scope from SK
Sandberg Capital: kept SK, dropped out_of_scope from CZ
102 part records -> 91 investors in data/sample/investors.json
91 records, 0 errors, 0 warnings
```
</details>

→ `Bash` — Run fetch and verify on merged records
```sh
(.venv/bin/python -m investordb fetch 2>&1 | tail -8) && (.venv/bin/python -m investordb verify 2>&1 | tail -20)
```

<details><summary>result</summary>

```
[2/8] live     200 https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=1199826&typ=UPLNY
[3/8] live     200 https://cc.cz/ceske-dataddo-ma-ctvrtou-investici-od-miliardare-ondreje-tomka-z-datoveho-startupu-se-stava-globalni-hrac/
[4/8] live     200 https://rockawayx.com/insights
[5/8] live     200 https://rockawayx.com/insights/rockawayx-and-forward-industries-co-lead-strategic-investment-in-onre
[6/8] live     200 https://rockawayx.com/insights/our-investment-in-bethog-an-ai-native-gaming-platform
[7/8] live     200 https://www.lupa.cz/aktuality/komarek-investuje-250-milionu-do-dvou-izraelskych-sitovych-a-bezpecnostnich-startupu/
[8/8] live     200 https://cc.cz/cesti-spaceflow-nabiraji-na-digitalizaci-budov-41-milionu-korun-investici-vedou-credo-ventures-pripojil-se-i-up21/
done: 8 live, 0 from Wayback, 0 failed
250 checks over 64 records, 134 URLs
quote: 250/250 pass (100.0 %) - exact 250, fuzzy 0, missing 0, unreachable 0
value: n/a 104, ok 106, partial 30, value_not_in_quote 10
tier A: 44/44 quotes pass
tier B: 180/180 quotes pass
tier C: 26/26 quotes pass
claims (all verified quotes together): n/a 103, ok 104, partial 15
wrote data/sample/verification.csv
```
</details>

→ `Bash` — Inspect verification rows for changed records
```sh
head -1 data/sample/verification.csv; grep -E "^(czech-founders-vc|rockawayx|impulse-ventures|springtide-ventures|up21|bhm-ventures)," data/sample/verification.csv | cut -c1-260
```

<details><summary>result</summary>

```
record_id,record_name,target,kind,label,source_index,url,tier,publisher,quote_status,similarity,value_status,value_detail,claim_value_status,fetch_used,http_status,final_url
bhm-ventures,BHM Ventures (BHM group),investments[0],investment,Carebot,0,https://www.startitup.sk/milionar-tomas-krsek-vstupuje-do-startupu-ktory-pomaha-lekarom-odhalit-rakovinu-uz-v-rannom-stadiu/,C,Startitup,exact,1.0,ok,date=2025-08-20:published,ok,live,20
bhm-ventures,BHM Ventures (BHM group),investments[1],investment,Sharry,0,https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=940334&typ=UPLNY,A,Obchodní rejstřík (justice.cz),exact,1.0,ok,date=2019-02-21:ok; company_not_in_quote,ok,live,200,https://
bhm-ventures,BHM Ventures (BHM group),investments[2],investment,Yieldigo,0,https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=949426&typ=UPLNY,A,Obchodní rejstřík (justice.cz),exact,1.0,ok,date=2016-10-31:ok; company_not_in_quote,ok,live,200,https:
bhm-ventures,BHM Ventures (BHM group),investments[2],investment,Yieldigo,1,https://or.justice.cz/ias/ui/rejstrik-firma.vysledky?subjektId=949426&typ=UPLNY,A,Obchodní rejstřík (justice.cz),exact,1.0,value_not_in_quote,date=2016-10-31:missing; company_not_in_quo
czech-founders-vc,Czech Founders VC,fields.stages,stages,stages,0,https://czechfounders.vc/,B,Czech Founders VC,exact,1.0,n/a,,n/a,live,200,https://czechfounders.vc/
czech-founders-vc,Czech Founders VC,fields.geography,geography,geography,0,https://czechfounders.vc/,B,Czech Found
… [2606 more characters]
```
</details>

→ `Bash` — Drop rename source, re-merge, validate, verify, decide
```sh
.venv/bin/python - <<'EOF'
import json
p='data/sample/parts/cz.json'
recs=json.load(open(p))
for r in recs:
    if r['id']=='bhm-ventures':
        for inv in r['investments']:
            if inv['company']=='Yieldigo':
                inv['sources']=[s for s in inv['sources'] if 'BHM Ventures a.s.' not in s['quote']]
                print(len(inv['sources']))
open(p,'w').write(json.dumps(recs,ensure_ascii=False,indent=2)+'\n')
EOF
.venv/bin/python scripts/merge_parts.py | tail -1 && .venv/bin/python -m investordb validate --today 2026-10-11 | tail -1 && .venv/bin/python -m investordb verify 2>&1 | sed -n 2,3p && .venv/bin/python -m investordb decide --ref-date 2026-10-11
```

<details><summary>result</summary>

```
1
102 part records -> 91 investors in data/sample/investors.json
91 records, 0 errors, 0 warnings
quote: 249/249 pass (100.0 %) - exact 249, fuzzy 0, missing 0, unreachable 0
value: n/a 104, ok 106, partial 30, value_not_in_quote 9
reference date 2026-10-11, window 36 months; DISAGREE 16, agree 39, human_only 36
  DISAGREE   365-fintech: stored dormant [E4] vs computed uncertain [I3?] - no dated investment with a Tier A/B source
  human_only abris-capital: stored out_of_scope [S1] vs computed uncertain [I3?] - no dated investment with a Tier A/B source
  human_only aceon-accelerator: stored excluded [E9] vs computed uncertain [I1?;I2?] - accelerator: keep out of ticket statistics; no registry identifier; no registration/FoF evidence and only 1 sourced portfolio companies
  DISAGREE   arca-capital-slovakia: stored excluded [E4] vs computed uncertain [I3?] - no dated investment with a Tier A/B source
  human_only arx-equity-partners: stored out_of_scope [S1] vs computed uncertain [I3?] - no dated investment with a Tier A/B source
  DISAGREE   bic-bratislava: stored excluded [E4] vs computed uncertain [I3?] - no dated investment with a Tier A/B source
  human_only cb-espri-impact-one: stored excluded [E9] vs computed uncertain [I3?] - no dated investment with a Tier A/B source
  human_only cvi: stored excluded [E3] vs computed uncertain [I3?] - no dated investment with a Tier A/B source
  human_only energy-venture-pals: stored out_of_scope [S1] vs computed uncertain [I3?] - no d
… [5980 more characters]
```
</details>

→ `Bash` — Compare engine disagreements before and after on parts
```sh
.venv/bin/python - <<'EOF'
import json, sys
from datetime import date
sys.path.insert(0,'src')
from investordb.rules import decide, load_negative_list, agreement
neg=load_negative_list('data/negative_list.csv')
W='[redacted: local path]'
for label, base in (('before', W), ('after','data/sample/parts/')):
    dis=[]
    for c in ('sk','cz'):
        for r in json.load(open(base+f'{c}.json')):
            d=decide(r,neg,date(2026,10,11))
            a=agreement(r,d)
            if a=='DISAGREE': dis.append((c,r['id'],r['decision']['status'],d.status))
    print(label, len(dis)); [print('  ',x) for x in dis]
EOF
```

<details><summary>result</summary>

```
before 29
   ('sk', 'venture-to-future-fund', 'included', 'uncertain')
   ('sk', 'zero-one-hundred', 'included', 'uncertain')
   ('sk', 'g-force', 'included', 'uncertain')
   ('sk', 'cb-investment-management', 'included', 'uncertain')
   ('sk', 'seed-starter-slovenskej-sporitelne', 'included', 'uncertain')
   ('sk', 'ipm-group', 'dormant', 'uncertain')
   ('sk', 'fond-inovacii-a-technologii', 'dormant', 'uncertain')
   ('sk', 'limerock', 'dormant', 'uncertain')
   ('sk', '365-fintech', 'dormant', 'uncertain')
   ('sk', 'monogram-ventures', 'dormant', 'uncertain')
   ('sk', 'kpas', 'excluded', 'uncertain')
   ('sk', 'launcher', 'excluded', 'uncertain')
   ('sk', 'bic-bratislava', 'excluded', 'uncertain')
   ('sk', 'arca-capital-slovakia', 'excluded', 'uncertain')
   ('sk', 'pro-partners-holding', 'excluded', 'uncertain')
   ('sk', 'swiss-re-bratislava', 'excluded', 'uncertain')
   ('sk', 'prva-kapitalova', 'excluded', 'uncertain')
   ('sk', 'gapfunding', 'excluded', 'uncertain')
   ('sk', 'monopoly-ventures', 'excluded', 'uncertain')
   ('cz', 'reflex-capital', 'included', 'uncertain')
   ('cz', 'zaka-vc', 'included', 'uncertain')
   ('cz', 'rockaway-ventures', 'included', 'uncertain')
   ('cz', 'nation-1', 'included', 'uncertain')
   ('cz', 'miton', 'included', 'uncertain')
   ('cz', 'inven-capital', 'included', 'uncertain')
   ('cz', 'ii-biotech-fund', 'included', 'uncertain')
   ('cz', 'soulmates-ventures', 'included', 'uncertain')
   ('cz', 'startupyard', 'included', 'unce
… [918 more characters]
```
</details>

→ `Bash` — Check whether grading uses the existence field
```sh
sed -n 40,70p src/investordb/grade.py; grep -n "existence" src/investordb/review.py | head -5
```

<details><summary>result</summary>

```
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
75:            # existence: show the strongest source we have for the record
86:            c = _claim(rec, "existence", "", "existence", text, all_src[:1] + all_src[1:4],
8
… [125 more characters]
```
</details>

→ `Bash` — Compute final status and existence counts
```sh
.venv/bin/python - <<'EOF'
import json, collections
r=json.load(open('data/sample/investors.json'));print('merged', len(r), dict(collections.Counter(x['decision']['status'] for x in r)))
kinds=collections.Counter(); n=0; tot=0; nulls=[]
for c in ['sk','cz']:
    p=json.load(open(f'data/sample/parts/{c}.json'));print(c, dict(collections.Counter(x['decision']['status'] for x in p)))
    for x in p:
        if x['decision']['status'] in ('included','uncertain','dormant'):
            tot+=1
            e=(x.get('fields') or {}).get('existence')
            if e: n+=1; kinds.update(e['value'])
            else: nulls.append((x['id'],x['decision']['status']))
print('target records',tot,'with existence',n, dict(kinds)); print('null:',nulls)
EOF
```

<details><summary>result</summary>

```
merged 91 {'dormant': 9, 'out_of_scope': 26, 'excluded': 22, 'uncertain': 7, 'included': 27}
sk {'included': 7, 'uncertain': 1, 'dormant': 6, 'excluded': 19, 'out_of_scope': 16}
cz {'included': 20, 'uncertain': 6, 'dormant': 3, 'excluded': 3, 'out_of_scope': 21}
target records 43 with existence 33 {'fund_of_funds_commitment': 11, 'association_full_member': 12, 'regulator_register': 8, 'portfolio_page': 15}
null: [('baryon-fund', 'uncertain'), ('lrj-capital', 'dormant'), ('ipm-group', 'dormant'), ('monogram-ventures', 'dormant'), ('cs-seed-starter', 'uncertain'), ('impulse-ventures', 'uncertain'), ('air-ventures', 'uncertain'), ('springtide-ventures', 'dormant'), ('up21', 'dormant'), ('rockawayx', 'uncertain')]
```
</details>

**Agent:**

[redacted: name]

**Enrichment report: investor-db pilot (CZ/SK), ref-date 2026-10-11**

All four commands ran clean. Validate gave 91 records, 0 errors and 0 warnings. Fetch got all 8 new URLs live, verify passed 249/249 quotes (all exact), and decide finished as below. One limitation: fetch, verify and grade never read `fields.existence`, because `FIELD_NAMES` in `records.py` doesn't include it. I checked all 47 existence quotes myself instead: each is a whitespace-normalised substring of the raw page text, and each still matched after a forced re-fetch. Only `rules.py` reads the field.

**Status counts, before → after**

| | included | uncertain | dormant | excluded | out_of_scope |
|---|---|---|---|---|---|
| merged (91 records) | 25 → 27 | 13 → 7 | 7 → 9 | 20 → 22 | 26 → 26 |
| sk.json | 7 → 7 | 1 → 1 | 6 → 6 | 19 → 19 | 16 → 16 |
| cz.json | 18 → 20 | 12 → 6 | 1 → 3 | 1 → 3 | 21 → 21 |

**Existence evidence**

After the re-decisions, 43 records are included, uncertain or dormant. 33 of them now have `fields.existence`; some have more than one kind.

| Kind | Records | Sources used |
|---|---|---|
| portfolio_page | 15 | own sites, Tier B |
| association_full_member | 12 | 8 from the CVCA "Full members" section, 4 from SLOVCA ordinary members |
| fund_of_funds_commitment | 11 | 10 Tier A: EIF Sep-2026 PDFs, SIH fund pages, the NRI Fond Ukrajina page for DEPO. 1 Tier B (Lighthouse, below) |
| regulator_register | 8 | 7 NBS entity pages, 1 ESMA register record for Inven |

- **Lighthouse:** its only evidence is the fund's own statement of Czech ESIF FoF backing, so the source is Tier B. Its portfolio page shows logos only.
- **Tilia:** CVCA lists it as an "Honorary Member", so I used its EIF listing instead of CVCA.
- **ČNB JERRS:** behind a CAPTCHA, so I couldn't use it. Its web service needs a signed access request. There were no SEC IAPD hits for any record.
- **No evidence found (existence left null, said in each note):** Baryon, ČS Seed Starter, Impulse, Air Ventures, RockawayX, LRJ, IPM, Monogram, Springtide, UP21.

**Decision changes (CZ only)**

- **STARTGUIDE: uncertain → included.** Its SG One page names DTS, BikeFair and Ringil. START GUIDE ONE entered Carebot on 18 Mar 2025 (Tier A).
- **Czech Founders VC: uncertain → included.** Its fund entered Edmund s.r.o. on 25 Mar 2026 (justice.cz). Its own portfolio page lists 30+ startups.
- **GAIN Ventures: uncertain → excluded (I2).** Carebot is its only known holding; there's no website, portfolio, licence or membership.
- **KOOPEO Ventures: uncertain → excluded (I2).** The SE is registered for property rental, the domain is parked and no deal was found.
- **Springtide: uncertain → dormant (E4).** Last deal was Source Defense / NetOp.Cloud on 27 Apr 2022 (media).
- **UP21: uncertain → dormant (E4).** Last deal was Spaceflow on 6 Aug 2019 (media). No registry entity found.
- **BHM Ventures: stays uncertain, rules I2+I3 → I3.**
  - I2 is now shown: the group's portfolio page lists 13 startups.
  - The stored "22 May 2025" Yieldigo and Sharry entries were not new deals. BHM Ventures a.s. has the same IČ as Bohemia Venture Capital a.s., which already held those stakes. I re-dated them to the original entries (2016 and 2019).
  - The Aug 2025 Carebot stake is held by Tahoe Invest, then ERGOAPEX (Cyprus). Neither is named BHM in the register.
- **Air Ventures: stays uncertain, rules I1+I3 → I2+I3.** The entity is now resolved: AIR VENTURES s.r.o., run by the Czech Founders partners. Recent deals appear only in PitchBook.
- **RockawayX: stays uncertain, rules I3 → I2.** Its own posts show dated deals (OnRe Series A May 2026, BetHog Apr 2026). But most of the business is validators, liquidity and a liquid hedge fund (close to E7), and there's no portfolio page.
- **Unchanged uncertain, with notes refreshed:**
  - Orbit: recent 2026 deals are venture debt and it's unknown whether they carry warrants.
  - Impulse: Dataddo, Dec 2023, Tier C only.
  - ČS Seed Starter: portfolio shown as logos only; Born Digital keeps it in the I3 window only until 24 Nov 2026.
  - Baryon: two portfolio companies, management seat unknown.

**Remaining decide disagreements: 16 (down from 29)**

- **Five dormant records** (365.fintech, FIT, Limerock, Monogram, IPM): engine says uncertain.
  - The engine is right about the data: E4 needs a dated last investment and these records have none.
  - The stored "dormant" is still the right human call. The fix is to add an old dated (even Tier C) deal to each.
  - IPM is a special case: its InoBat 2024 row (Tier B, which the note excludes as the group's own project) makes the engine pass I3. Either drop that row or accept the disagreement.
- **Eleven excluded records**, where I think the stored decision is right:
  - GAIN and KOOPEO (I2): the engine reaches the same finding but can only output uncertain for a failed I rule.
  - Prvá kapitálová, Gapfunding and Monopoly Ventures (I1), and Swiss Re (I2): same pattern.
  - KPAS (E1): the engine doesn't know an angel network routes money; it isn't on the negative list.
  - Launcher, BIC, Arca and Pro Partners (all "excluded E4"): pre-existing records I didn't touch. They contradict PLAN, which keeps E4 entities in the dormant list. I2 or I3 would be the better rule for a firm that never invested.

Files are in `[redacted: local path]`:
- sk.json
- cz.json
- cz-decisions.md

Working files (fetch and quote-check helpers, the existence spec, pre-edit backups) are in `[redacted: local path]`.

