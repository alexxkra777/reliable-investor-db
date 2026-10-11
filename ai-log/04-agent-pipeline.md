# Agent: verification pipeline

Claude Code sub-agent log, exported from `agent-a2a771182c9c15832.jsonl`.
Tool outputs longer than 1,500 characters are shortened.

## Brief

You are a senior Python engineer. Build the tooling for a small "reliable investor database" project in the existing git repo /Users/[redacted]/homeW/ai-dev-test/investor-db. First read PLAN.md there (it defines inclusion rules I1–I4, exclusion rules E1–E10, evidence tiers A/B/C, confidence grades, accuracy metrics). Do not edit PLAN.md or research/.

## Record format (implement exactly; this is the contract)
`data/sample/investors.json` = JSON array of records:
```json
{
  "id": "neulogy-ventures",
  "name": "Neulogy Ventures",
  "type": "vc",                       // vc|pe|cvc|family_office|angel|private_investor|accelerator|fund_of_funds|public_dfi|platform|adviser|other
  "hq": {"country": "SK", "city": "Bratislava"},
  "website": "https://...",
  "legal_entities": [{"name": "...", "role": "manager|fund|vehicle", "id_type": "ICO|LEI|CRD|CIK|company_number", "id": "...", "register_url": "..."}],
  "decision": {"status": "included|excluded|dormant|uncertain", "rules": ["I1","I2","I3","I4"] , "note": "..."},
  "fields": {
    "sectors":   {"value": ["software","deeptech"], "sources": [SOURCE...]},
    "stages":    {"value": ["seed","series_a"], "sources": [...]},
    "geography": {"value": ["SK","CZ","CEE"], "sources": [...]},
    "ticket":    {"value": {"min": 200000, "max": 2000000, "currency": "EUR"}, "sources": [...]},
    "funds":     {"value": [{"name": "...", "size": 30000000, "currency": "EUR", "vintage": 2021}], "sources": [...]},
    "aum":       {"value": {"amount": 100000000, "currency": "EUR", "as_of": "2025-06-30"}, "sources": [...]}
  },
  "investments": [
    {"company": "...", "date": "2025-03-12", "date_kind": "announced|registry_entry|portfolio_page", "round_size": {"amount": 1500000, "currency": "EUR"}, "sources": [SOURCE...]}
  ]
}
```
SOURCE = `{"url": "...", "tier": "A|B|C", "publisher": "...", "published": "YYYY-MM-DD|null", "accessed": "YYYY-MM-DD", "quote": "verbatim sentence from the page"}`.
Any field may be `null` (unknown). Values without sources are invalid unless null.
Write the JSON Schema to `schema/investor.schema.json` (draft 2020-12) and validate with `jsonschema`.

## Package `investordb` (Python 3.12+, src layout, pyproject.toml, deps: requests, beautifulsoup4, jsonschema, pypdf; dev: pytest, ruff). CLI `python -m investordb <cmd>`:
1. `validate` — schema validation + consistency checks (ticket min ≤ max ≤ largest fund size; investment dates not in the future and ≥ fund vintage when linked; currencies present; every non-null field has ≥1 source; ids unique).
2. `fetch` — download every distinct source URL into `data/cache/` (gitignored) with polite rate limit (1 req/s per host), a realistic browser User-Agent, timeout 20 s, 2 retries; store status, final URL, content type, fetched_at, sha256 in `data/cache/index.json`. HTML → visible text (strip script/style/nav); PDF → text via pypdf. If a page fails, try the Wayback Machine availability API (`https://archive.org/wayback/available?url=`) and fetch the snapshot; record which one was used.
3. `verify` — for every (record, field/investment, source) check that `quote` appears in the fetched text. Normalise both sides: Unicode NFKD + strip diacritics, casefold, unify quotes/dashes/nbsp, collapse whitespace, normalise number formatting ("1 500 000", "1,5 mil." etc. — keep it reasonable, don't overengineer). Result per check: `exact`, `fuzzy` (best sliding-window similarity ≥ 0.85 using difflib on a window around the best token match — keep it fast), `missing`, `unreachable`. Also check the claimed value is supported: for numbers/dates, the number or date (in common formats incl. Slovak/Czech month names and dd.mm.yyyy) should appear within the quote; flag `value_not_in_quote` otherwise. Write `data/sample/verification.csv` (one row per check) and a summary to stdout.
4. `decide` — deterministic rule engine that recomputes decision suggestions from the data (I3 recency: latest investment within 36 months of a reference date, default today; E-rules from `type` and a negative list file `data/negative_list.csv` (name, reason, rule)). It must NOT overwrite the human decision; it writes `data/sample/decision_check.csv` showing stored vs computed decision and highlights disagreements.
5. `grade` — confidence A/B/C per record per PLAN 3.3, using source tiers and verify results (a source whose quote is `missing`/`unreachable` does not count). Writes into `data/sample/investors.graded.json` and `data/sample/investors.csv` (flat, one row per investor, with semicolon-joined values and the primary source URL per column, plus `last_investment_date`, `confidence`).
6. `review-pack --n 60 --seed 7` — builds a self-contained static `eval/review.html` for a human reviewer: a stratified random sample of claims (existence/type per record + field values + investments), each showing the claim, the quote, a clickable source link, and buttons Correct / Wrong / Can't verify + optional note. State in localStorage (wrapped in try/catch); "Export CSV" button downloads `labels.csv` (claim_id, label, note, reviewed_at). Mobile friendly, clean, no external dependencies. Also writes `eval/claims.csv` (the sampled claims with ids).
7. `eval --labels eval/labels.csv` — computes inclusion precision, per-field accuracy, investment-date accuracy, overall claim accuracy, each with 95 % Wilson intervals; recall against `data/reference/*.csv` reference lists (columns: name, source_url; matching by normalised name + aliases in records) — counted as covered if the entity is in investors.json with any decision; writes `eval/ACCURACY.md` (tables + short method note) and `eval/metrics.json`. If labels file is missing, compute only the automated metrics (verify pass rates) and say so.

Tests (pytest) for: normalisation and quote matching (incl. Slovak diacritics, nbsp, number formats), Wilson interval, rule engine (recency boundary, platform exclusion), schema validation of a small fixture, grade logic. Keep fixtures in tests/fixtures. No network in tests.

Use a tiny fixture dataset (2–3 fake records clearly named "Example Ventures" etc.) ONLY inside tests/fixtures — do not create data/sample/investors.json (real data comes from someone else). Create `data/negative_list.csv` with a header and a few real well-known entries (Crowdcube, Seedrs, Republic, Crowdberry platform — reason, rule E1). Create `.gitignore` (data/cache/, __pycache__, .venv, .pytest_cache, *.egg-info).

Engineering rules:
- Use a venv in .venv (`python3 -m venv .venv`), install with pip -e .[dev]. Make `pytest` and `ruff check` pass.
- Code comments in English, short, plain, human — only where useful. No docstring essays.
- Nothing anywhere may mention AI, LLM, Claude, GPT, Codex, "generated" or agents (code, comments, commit messages).
- Make small logical git commits as you go (schema, fetch, verify, rules, grade, review pack, eval, tests). Plain English messages, no trailers, no Co-Authored-By. Do not change git config. Do not push.
- Do not write README.md. Do not touch files outside this repo.

Final message: list of commands, test results (paste pytest summary line), and known limitations.

→ `Bash` — Inspect repo state and Python versions
```sh
git status && git log --oneline | head -20 && ls -la && find . -path ./.git -prune -o -type f -print | head -50 && python3 --version && which python3.12 python3.13 python3.14
```

<details><summary>result</summary>

```
Exit code 1
Текущая ветка: main
нечего коммитить, нет изменений в рабочем каталоге
9112125 Add plan: inclusion rules, evidence tiers, verification
3a42a0e Add research notes on public sources and universe size
total 32
drwxr-xr-x   5 [user]  staff    160 11 окт.  01:23 .
drwxr-xr-x   4 [user]  staff    128 11 окт.  01:07 ..
drwxr-xr-x  12 [user]  staff    384 11 окт.  01:24 .git
-rw-r--r--   1 [user]  staff  12330 11 окт.  01:23 PLAN.md
drwxr-xr-x   3 [user]  staff     96 11 окт.  01:21 research
./PLAN.md
./research/sources-and-universe.md
Python 3.14.7
python3.12 not found
python3.13 not found
/opt/homebrew/bin/python3.14
```
</details>

→ `Bash` — Read plan and git author info
```sh
cat PLAN.md && wc -l research/sources-and-universe.md && git log --format='%an <%ae> | %s' && git config user.name; git config user.email
```

<details><summary>result</summary>

```
# Plan: a reliable database of investors

The point of this database is trust. A record is only worth something if a reader can click
through to a public page and see for themselves that the entity invests, in what, how much,
and since when. So the plan is built around evidence first and coverage second.

Research behind the numbers below: [`research/sources-and-universe.md`](research/sources-and-universe.md).

---

## 1. What counts as an investor

**Unit of a record = the investing organisation (manager), or a person investing in their own name.**
Not the fund vehicle, not the SPV, not the brand. A manager with five funds is one record with
five funds attached. This matters a lot: 64 % of "venture capital fund" issuers in the last
four quarters of SEC Form D filings are one-deal SPVs or series vehicles. Counting vehicles
would triple the database with noise.

### Types

| Type | Definition used here |
|---|---|
| `vc` | Manages third-party or own capital and takes minority equity / convertible stakes in young private companies (pre-seed to growth). |
| `pe` | Buyout, growth or mezzanine investor in established private companies, usually majority or significant minority stakes. |
| `cvc` | Investment arm of a non-financial corporation that invests in third-party startups. |
| `family_office` | Single or multi-family office that makes **direct** investments into private companies (not only allocates to funds or manages a portfolio of listed securities). |
| `angel` | Natural 
… [11067 more characters]
```
</details>

**Agent:**

Coordinator rule noted: only explicit `git add <paths>`, check `git status` before each commit. Setting up the environment now.

→ `Bash` — Check git hooks and create venv with deps
```sh
git config --get core.hooksPath; ls .git/hooks | grep -v sample; git config --global --get core.hooksPath; python3 -m venv .venv && .venv/bin/pip install -q --upgrade pip && .venv/bin/pip install -q requests beautifulsoup4 jsonschema pypdf pytest ruff setuptools && .venv/bin/pip list 2>/dev/null | grep -iE 'requests|beautifulsoup4|jsonschema|pypdf|pytest|ruff'
```

<details><summary>result</summary>

```
beautifulsoup4            4.15.0
jsonschema                4.26.0
jsonschema-specifications 2025.9.1
pypdf                     6.20.0
pytest                    9.1.1
requests                  2.34.2
ruff                      0.17.0
```
</details>

**Agent:**

Now the scaffold and schema.

→ `Bash` — Create gitignore and pyproject
```sh
mkdir -p /Users/[redacted]/homeW/ai-dev-test/investor-db/{schema,src/investordb,tests/fixtures,data/reference,eval} && cd /Users/[redacted]/homeW/ai-dev-test/investor-db && cat > .gitignore <<'EOF'
data/cache/
__pycache__/
.venv/
.pytest_cache/
*.egg-info/
.ruff_cache/
EOF
cat > pyproject.toml <<'EOF'
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "investordb"
version = "0.1.0"
description = "Tooling for an evidence-first investor database: validation, source fetching, quote checks, rules, grading, review and accuracy reports."
requires-python = ">=3.12"
dependencies = [
    "requests>=2.31",
    "beautifulsoup4>=4.12",
    "jsonschema>=4.21",
    "pypdf>=4.0",
]

[project.optional-dependencies]
dev = ["pytest>=8", "ruff>=0.5"]

[project.scripts]
investordb = "investordb.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
line-length = 100
target-version = "py312"
src = ["src", "tests"]

[tool.ruff.lint]
select = ["E", "F", "W", "I", "B", "UP", "SIM"]
EOF
```

<details><summary>result</summary>

```
(Bash completed with no output)
```
</details>

→ `Write` /Users/[redacted]/homeW/ai-dev-test/investor-db/schema/investor.schema.json

<details><summary>result</summary>

```
File created successfully at: /Users/[redacted]/homeW/ai-dev-test/investor-db/schema/investor.schema.json (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Create package init and records helpers
```sh
cd /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb && cat > __init__.py <<'EOF'
__version__ = "0.1.0"
EOF
cat > __main__.py <<'EOF'
from investordb.cli import main

raise SystemExit(main())
EOF
cat > records.py <<'EOF'
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
        raise DataError(f"{p} must con
… [1171 more characters]
```

<details><summary>result</summary>

```
(Bash completed with no output)
```
</details>

→ `Write` /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/validate.py

<details><summary>result</summary>

```
File created successfully at: /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/validate.py (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Simplify record label helper
```sh
cd /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb && python3 - <<'EOF'
p='validate.py'
s=open(p).read()
s=s.replace('''def _where(rec: dict, i: int) -> str:
    return rec.get("id") or f"#{i}" if isinstance(rec, dict) else f"#{i}"''','''def _where(rec: dict, i: int) -> str:
    return rec.get("id") or f"#{i}"''')
open(p,'w').write(s)
EOF
```

<details><summary>result</summary>

```
(Bash completed with no output)
```
</details>

**Agent:**

Now the CLI (lazy imports so each command can land in its own commit).

→ `Write` /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/cli.py

<details><summary>result</summary>

```
File created successfully at: /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/cli.py (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Add negative list, fixture, install package, run validate
```sh
cat > data/negative_list.csv <<'EOF'
name,reason,rule
Crowdcube,Equity crowdfunding platform; routes investors' money into companies,E1
Seedrs,Equity crowdfunding platform (now part of Republic Europe),E1
Republic,Investment and crowdfunding platform,E1
Crowdberry,"Crowdberry's investment platform; its fund manager, if any, is assessed as a separate record",E1
EOF
cat > tests/fixtures/investors.json <<'EOF'
[
  {
    "id": "example-ventures",
    "name": "Example Ventures",
    "aliases": ["Example Ventures a.s."],
    "type": "vc",
    "hq": {"country": "SK", "city": "Bratislava"},
    "website": "https://example.com/",
    "legal_entities": [
      {"name": "Example Ventures a.s.", "role": "manager", "id_type": "ICO", "id": "12345678",
       "register_url": "https://example.com/register/12345678"}
    ],
    "decision": {"status": "included", "rules": ["I1", "I2", "I3", "I4"], "note": "Fixture record."},
    "fields": {
      "sectors": {"value": ["software", "deeptech"], "sources": [
        {"url": "https://example.com/about", "tier": "B", "publisher": "Example Ventures",
         "published": null, "accessed": "2026-10-01",
         "quote": "We back software and deep-tech fo
… [3251 more characters]
```

<details><summary>result</summary>

```
ERROR   schema example-ventures: fields/aum: None is valid under each of {'allOf': [{'$ref': '#/$defs/field'}, {'properties': {'value': {'$ref': '#/$defs/aum'}}}]}, {'type': 'null'}
ERROR   schema example-ventures: fields/stages: None is valid under each of {'allOf': [{'$ref': '#/$defs/field'}, {'properties': {'value': {'$ref': '#/$defs/stringList'}}}]}, {'type': 'null'}
3 records, 2 errors, 0 warnings
exit=1
error: records file not found: data/sample/investors.json
exit=2
```
</details>

→ `Bash` — Fix schema null handling and re-validate fixture
```sh
.venv/bin/python - <<'EOF'
import json
p='schema/investor.schema.json'
s=json.load(open(p))
props=s['$defs']['record']['properties']['fields']['properties']
for k,v in props.items():
    one=v.pop('oneOf')
    v['allOf']=one[1]['allOf']
s['$defs']['field']['description']="A sourced value, or null when unknown. Field definitions add a constraint on 'value' on top of this."
txt=json.dumps(s,indent=2,ensure_ascii=False)+"\n"
open(p,'w').write(txt)
EOF
.venv/bin/python -m investordb validate --records tests/fixtures/investors.json --today 2026-10-11; echo exit=$?
```

<details><summary>result</summary>

```
3 records, 0 errors, 0 warnings
exit=0
```
</details>

→ `Bash` — Check validate error messages on broken data
```sh
.venv/bin/python - <<'EOF'
import json, copy
from investordb.validate import validate
recs=json.load(open('tests/fixtures/investors.json'))
r=copy.deepcopy(recs)
r[0]['fields']['ticket']['sources']=[]
r[0]['fields']['ticket']['value']['max']=50000000
r[0]['investments'][0]['date']='2027-01-01'
r[1]['id']='example-ventures'
r[2]['fields']['sectors']={"value":["x"]}
rep=validate(r)
print("\n".join(rep.errors)); print(rep.warnings)
EOF
```

<details><summary>result</summary>

```
schema example-ventures: fields/ticket: [] should be non-empty
schema demo-capital: fields/sectors: {'value': ['x']} is not of type 'null'
example-ventures: fields.ticket has a value but no sources
example-ventures: ticket max 50000000 EUR > largest fund size 30000000 EUR
example-ventures: investments[0] (Alpha Robotics) date 2027-01-01 is in the future
example-ventures: duplicate id (also record #0)
demo-capital: fields.sectors has a value but no sources
[]
```
</details>

→ `Bash` — Improve oneOf error messages
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/validate.py'
s=open(p).read()
s=s.replace('''        if err.context:
            best = min(err.context, key=lambda e: -len(e.absolute_path))
            msg = best.message''','''        if err.context:
            best = best_match(err.context)
            msg = best.message
            if best.absolute_path != err.absolute_path:
                msg = f"{'/'.join(str(p) for p in best.relative_path)}: {msg}"''')
s=s.replace("from jsonschema import Draft202012Validator\n","from jsonschema import Draft202012Validator\nfrom jsonschema.exceptions import best_match\n")
open(p,'w').write(s)
EOF
.venv/bin/python - <<'EOF'
import json, copy
from investordb.validate import validate
recs=json.load(open('tests/fixtures/investors.json'))
r=copy.deepcopy(recs)
r[0]['fields']['ticket']['value']['currency']='eur'
r[2]['fields']['sectors']={"value":["x"]}
r[2]['investments'][0]['sources'][0]['tier']='D'
print("\n".join(validate(r).errors))
EOF
```

<details><summary>result</summary>

```
schema example-ventures: fields/ticket/value/currency: 'eur' does not match '^[A-Z]{3}$'
schema demo-capital: fields/sectors: {'value': ['x']} is not of type 'null'
schema demo-capital: investments: [{'company': 'Gamma Labs', 'date': '2019-11-20', 'date_kind': 'announced', 'round_size': None, 'sources': [{'url': 'https://example.com/news/gamma', 'tier': 'D', 'publisher': 'Example Daily', 'published': '2019-11-20', 'accessed': '2026-10-01', 'quote': 'Demo Capital invested in Gamma Labs on 20 November 2019.'}]}] is not of type 'null'
demo-capital: fields.sectors has a value but no sources
```
</details>

→ `Bash` — Pick deepest schema error and run ruff
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/validate.py'
s=open(p).read()
old_start=s.index("def schema_errors")
old_end=s.index("def consistency")
new='''def _deepest(err):
    # oneOf/allOf hide the useful message somewhere inside err.context
    if not err.context:
        return err
    cands = [_deepest(e) for e in err.context]
    return max(cands, key=lambda e: (len(e.absolute_path), e.validator != "type"))


def schema_errors(records, validator: Draft202012Validator) -> list[str]:
    out = []
    for top in sorted(validator.iter_errors(records), key=lambda e: list(e.absolute_path)):
        err = _deepest(top)
        path = list(err.absolute_path)
        where = "/".join(str(p) for p in path) or "(root)"
        if path and isinstance(path[0], int) and isinstance(records[path[0]], dict):
            rid = records[path[0]].get("id")
            if rid:
                where = f"{rid}: " + "/".join(str(p) for p in path[1:])
        out.append(f"schema {where}: {err.message}")
    return out


'''
s=s[:old_start]+new+s[old_end:]
s=s.replace("from jsonschema.exceptions import best_match\n","")
open(p,'w').write(s)
EOF
.venv/bin/python - <<'EOF'
import json, copy
from invest
… [348 more characters]
```

<details><summary>result</summary>

```
Exit code 1
schema example-ventures: fields/ticket/value/currency: 'eur' does not match '^[A-Z]{3}$'
schema demo-capital: fields/sectors: 'sources' is a required property
schema demo-capital: hq/country: 'Slovakia' does not match '^[A-Z]{2}$'
schema demo-capital: investments/0/sources/0/tier: 'D' is not one of ['A', 'B', 'C']
demo-capital: fields.sectors has a value but no sources
SIM300 [*] Yoda condition detected
   --> src/investordb/validate.py:142:41
    |
140 |         rules = set(dec.get("rules") or [])
141 |         status = dec.get("status")
142 |         if status == "included" and not INCLUSION_RULES <= rules:
    |                                         ^^^^^^^^^^^^^^^^^^^^^^^^
143 |             missing = ", ".join(sorted(INCLUSION_RULES - rules))
144 |             rep.warnings.append(f"{rid}: included but rules miss {missing}")
    |
help: Rewrite as `rules >= INCLUSION_RULES`
    |
141 |         status = dec.get("status")
    -         if status == "included" and not INCLUSION_RULES <= rules:
142 +         if status == "included" and not rules >= INCLUSION_RULES:
143 |             missing = ", ".join(sorted(INCLUSION_RULES - rules))
    |

Found 1 error.
[*] 1 fixable with `--fix`.
```
</details>

→ `Bash` — Fix lint and check status
```sh
sed -i '' 's/if status == "included" and not INCLUSION_RULES <= rules:/if status == "included" and INCLUSION_RULES - rules:/' src/investordb/validate.py && .venv/bin/ruff check src && .venv/bin/ruff format --check src | tail -3; git status --short
```

<details><summary>result</summary>

```
All checks passed!
    |

3 files would be reformatted, 2 files already formatted
?? .gitignore
?? data/
?? pyproject.toml
?? schema/
?? src/
?? tests/
[This command modified 1 file you've previously read: src/investordb/validate.py. Call Read before editing.]
```
</details>

→ `Bash` — Commit skeleton/schema and validate separately
```sh
git add .gitignore pyproject.toml schema/investor.schema.json src/investordb/__init__.py src/investordb/__main__.py src/investordb/cli.py src/investordb/records.py && git status --short && git commit -q -m "Add package skeleton and investor record schema" && git add src/investordb/validate.py && git status --short && git commit -q -m "Add validate command: schema and consistency checks" && git log --oneline | head -3
```

<details><summary>result</summary>

```
A  .gitignore
A  pyproject.toml
A  schema/investor.schema.json
A  src/investordb/__init__.py
A  src/investordb/__main__.py
A  src/investordb/cli.py
A  src/investordb/records.py
?? data/
?? src/investordb/validate.py
?? tests/
A  src/investordb/validate.py
?? data/
?? tests/
169c011 Add validate command: schema and consistency checks
631ac55 Add package skeleton and investor record schema
9112125 Add plan: inclusion rules, evidence tiers, verification
```
</details>

→ `Write` /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/fetch.py

<details><summary>result</summary>

```
File created successfully at: /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/fetch.py (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Smoke-test fetch against a few live URLs
```sh
S=[tmp] && mkdir -p $S && .venv/bin/python - <<EOF
import json
src=lambda u:{"url":u,"tier":"B","publisher":"x","published":None,"accessed":"2026-10-01","quote":"Example Domain"}
recs=[{"id":"t","name":"T","type":"vc","decision":{"status":"included","rules":[]},"fields":{"sectors":{"value":["a"],"sources":[src("https://example.com/"),src("https://www.python.org/this-page-does-not-exist-xyz"),src("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"),src("https://www.slovca.sk/en/")]}}}]
json.dump(recs,open("$S/recs.json","w"))
EOF
time .venv/bin/python -m investordb fetch --records $S/recs.json --cache $S/cache && .venv/bin/python -c "
import json;d=json.load(open('$S/cache/index.json'))
for u,e in d.items(): print({k:e.get(k) for k in ('status','used','final_url','content_type','text_chars','wayback_url','redirected_to_homepage')})
" && head -c 300 $S/cache/files/*.txt
```

<details><summary>result</summary>

```
4 distinct URLs, 0 already cached, fetching 4
[1/4] live     200 https://example.com/
[2/4] FAILED   404 https://www.python.org/this-page-does-not-exist-xyz
[3/4] FAILED   403 https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf
[4/4] live     200 https://www.slovca.sk/en/
done: 2 live, 0 from Wayback, 2 failed
.venv/bin/python -m investordb fetch --records $S/recs.json --cache $S/cache  0,18s user 0,04s system 4% cpu 5,436 total
{'status': 200, 'used': 'live', 'final_url': 'https://example.com/', 'content_type': 'text/html; charset=utf-8', 'text_chars': 171, 'wayback_url': None, 'redirected_to_homepage': False}
{'status': 404, 'used': None, 'final_url': 'https://www.python.org/this-page-does-not-exist-xyz', 'content_type': 'text/html; charset=utf-8', 'text_chars': None, 'wayback_url': None, 'redirected_to_homepage': False}
{'status': 200, 'used': 'live', 'final_url': 'https://www.slovca.sk/en/', 'content_type': 'text/html; charset=UTF-8', 'text_chars': 2782, 'wayback_url': None, 'redirected_to_homepage': False}
{'status': 403, 'used': None, 'final_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf', 'content_type': 'text/html; charset=UTF-8', 'text_chars': None, 'wayback_url': None, 'redirected_to_homepage': False}
==> [tmp] <==
Slovak Venture Capital & Private Equity Association SLOVCA
Slovak V
… [555 more characters]
```
</details>

→ `Bash` — Probe Wayback availability API responses
```sh
curl -s -m 30 -A "Mozilla/5.0" "https://archive.org/wayback/available?url=https%3A%2F%2Fwww.w3.org%2FWAI%2FER%2Ftests%2Fxhtml%2Ftestfiles%2Fresources%2Fpdf%2Fdummy.pdf"; echo; curl -s -m 30 "https://archive.org/wayback/available?url=www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"; echo; curl -s -m 30 "https://archive.org/wayback/available?url=example.com"
```

<details><summary>result</summary>

```
{"url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", "archived_snapshots": {}}
{"url": "www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", "archived_snapshots": {}}
{"url": "example.com", "archived_snapshots": {"closest": {"status": "200", "available": true, "url": "http://web.archive.org/web/20261010051639/https://...%20or%20mailto:jobs@example.com/", "timestamp": "20261010051639"}}}
```
</details>

→ `Bash` — Test PDF extraction and Wayback fallback live
```sh
S=[tmp] && curl -s -m 30 "https://archive.org/wayback/available?url=http://www.geocities.com/" ; echo; .venv/bin/python - <<EOF
import json
src=lambda u:{"url":u,"tier":"B","publisher":"x","published":None,"accessed":"2026-10-01","quote":"x"}
recs=[{"id":"t","name":"T","type":"vc","decision":{"status":"included","rules":[]},"fields":{"sectors":{"value":["a"],"sources":[src("https://pdfobject.com/pdf/sample.pdf"),src("http://www.geocities.com/")]}}}]
json.dump(recs,open("$S/recs2.json","w"))
EOF
.venv/bin/python -m investordb fetch --records $S/recs2.json --cache $S/cache2 && .venv/bin/python -c "
import json;d=json.load(open('$S/cache2/index.json'))
for u,e in d.items(): print({k:e.get(k) for k in ('status','used','final_url','content_type','text_chars','wayback_url','error','redirected_to_homepage')})
" && head -c 200 $S/cache2/files/*.txt
```

<details><summary>result</summary>

```
{"url": "http://www.geocities.com/", "archived_snapshots": {}}
2 distinct URLs, 0 already cached, fetching 2
[1/2] live     200 https://pdfobject.com/pdf/sample.pdf
[2/2] live     200 http://www.geocities.com/
done: 2 live, 0 from Wayback, 0 failed
{'status': 200, 'used': 'live', 'final_url': 'https://www.yahoo.com/', 'content_type': 'text/html; charset=utf-8', 'text_chars': 2720, 'wayback_url': None, 'error': None, 'redirected_to_homepage': False}
{'status': 200, 'used': 'live', 'final_url': 'https://pdfobject.com/pdf/sample.pdf', 'content_type': 'application/pdf', 'text_chars': 2876, 'wayback_url': None, 'error': None, 'redirected_to_homepage': False}
==> [tmp] <==
Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Videos
Search Query for Search the web
Search with Yahoo Scout
Search the web
Skip to features bar
Skip to left column
Skip to main
Ski
==> [tmp] <==
Sample PDFThis is a simple PDF ﬁle. Fun fun fun.
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus facilisis odio sed mi. 
Curabitur suscipit. Nullam vel nisi. Etiam semper ipsum u
```
</details>

→ `Bash` — Exercise Wayback snapshot fetch path live
```sh
.venv/bin/python - <<'EOF'
import requests
from investordb.fetch import wayback_snapshot, HostThrottle, _get, extract_text
s=requests.Session(); t=HostThrottle()
snap=wayback_snapshot(s,t,"https://example.com/")
print(snap)
r,e=_get(s,t,snap); print(r.status_code if r is not None else e, r.headers.get("Content-Type") if r is not None else "")
if r is not None: print(extract_text(r.headers.get("Content-Type",""), r.content)[:200])
EOF
```

<details><summary>result</summary>

```
http://web.archive.org/web/20261010051639id_/https://...%20or%20mailto:jobs@example.com/
429 text/html
Your request is being blocked because our system has flagged it as suspected abusive bot traffic that is degrading the performance of the Wayback Machine.
We recognize this might be a false positive d
```
</details>

→ `Bash` — Check which User-Agent Wayback accepts
```sh
for ua in "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36" "investordb/0.1 (research)" "curl/8"; do curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -m 30 -A "$ua" -L "https://web.archive.org/web/2024id_/https://example.com/"; sleep 2; done; curl -s -m 30 "https://archive.org/wayback/available?url=https://www.python.org/about/"
```

<details><summary>result</summary>

```
200 https://web.archive.org/web/20241231233104id_/http://www.example.com/
200 https://web.archive.org/web/20241231233104id_/http://www.example.com/
200 https://web.archive.org/web/20241231233104id_/http://www.example.com/
{"url": "https://www.python.org/about/", "archived_snapshots": {}}
```
</details>

→ `Bash` — Test CDX API and requests headers against Wayback
```sh
curl -s -m 40 "https://web.archive.org/cdx/search/cdx?url=https://www.python.org/about/&output=json&limit=-1&filter=statuscode:200&fl=timestamp,original"; echo; cd /Users/[redacted]/homeW/ai-dev-test/investor-db && .venv/bin/python - <<'EOF'
import requests
from investordb.fetch import HEADERS
for u in ["http://web.archive.org/web/2024id_/https://example.com/","https://web.archive.org/web/2024id_/https://example.com/"]:
    r=requests.get(u,headers=HEADERS,timeout=20); print(r.status_code, r.url)
    r=requests.get(u,headers={"User-Agent":HEADERS["User-Agent"]},timeout=20); print(r.status_code, r.url)
EOF
```

<details><summary>result</summary>

```
[["timestamp","original"],
["20261009194646","https://www.python.org/about/"]]

429 http://web.archive.org/web/2024id_/https://example.com/
429 http://web.archive.org/web/2024id_/https://example.com/
429 https://web.archive.org/web/20241231233104id_/http://www.example.com/
429 https://web.archive.org/web/20241231233104id_/http://www.example.com/
```
</details>

→ `Bash` — Compare curl vs requests on Wayback
```sh
curl -s -o /dev/null -w "%{http_code}\n" -m 30 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36" "https://web.archive.org/web/20241231233104id_/http://www.example.com/"; cd /Users/[redacted]/homeW/ai-dev-test/investor-db && .venv/bin/python -c "
import requests
r=requests.get('https://web.archive.org/web/20241231233104id_/http://www.example.com/',headers={'User-Agent':'curl/8.7.1','Accept':'*/*'},timeout=20); print(r.status_code)
r=requests.get('https://web.archive.org/web/20241231233104id_/http://www.example.com/',headers={'User-Agent':'investordb/0.1 (+https://github.com/[redacted: account])'},timeout=20); print(r.status_code)
"
```

<details><summary>result</summary>

```
200
200
200
```
</details>

→ `Bash` — Add CDX fallback and archive UA, retest Wayback
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/fetch.py'
s=open(p).read()
s=s.replace('''WAYBACK_API = "https://archive.org/wayback/available?url="
''','''WAYBACK_API = "https://archive.org/wayback/available?url="
WAYBACK_CDX = "https://web.archive.org/cdx/search/cdx"
# archive.org flags a browser UA coming from a non-browser client as a bot (HTTP 429),
# so it gets a plain tool UA instead
ARCHIVE_UA = "investordb/0.1 (source verification; 1 req/s)"
''')
s=s.replace('''def _get(session, throttle: HostThrottle, url: str):
    last_exc = None
    for attempt in range(RETRIES + 1):
        throttle.wait(url)
        try:
            r = session.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)''','''def _headers(url: str) -> dict:
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
    
… [3300 more characters]
```

<details><summary>result</summary>

```
3 distinct URLs, 0 already cached, fetching 3
[1/3] FAILED   404 https://www.python.org/about/this-old-page-is-gone
[2/3] wayback  403 https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf
[3/3] live     200 http://www.geocities.com/
done: 1 live, 1 from Wayback, 1 failed
http://www.geocities.com/ {'status': 200, 'used': 'live', 'content_type': 'text/html; charset=utf-8', 'text_chars': 2759, 'wayback_url': None, 'wayback_lookup': None, 'wayback_error': None, 'redirected_offsite': True}
https://www.python.org/about/this-old-page-is-gone {'status': 404, 'used': None, 'content_type': 'text/html; charset=utf-8', 'text_chars': None, 'wayback_url': None, 'wayback_lookup': None, 'wayback_error': None, 'redirected_offsite': False}
https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf {'status': 403, 'used': 'wayback', 'content_type': 'text/html; charset=UTF-8', 'text_chars': 14, 'wayback_url': 'https://web.archive.org/web/20260930040145id_/https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf', 'wayback_lookup': 'availability', 'wayback_error': None, 'redirected_offsite': False}
```
</details>

→ `Bash` — Lint and commit fetch module
```sh
.venv/bin/ruff check src && git add src/investordb/fetch.py && git status --short && git commit -q -m "Add fetch command: polite downloader with text extraction and Wayback fallback" && git log --oneline | head -4
```

<details><summary>result</summary>

```
All checks passed!
A  src/investordb/fetch.py
?? data/
?? tests/
d39b4f1 Add fetch command: polite downloader with text extraction and Wayback fallback
169c011 Add validate command: schema and consistency checks
631ac55 Add package skeleton and investor record schema
9112125 Add plan: inclusion rules, evidence tiers, verification
```
</details>

**Agent:**

[redacted: name]

Работа не закончена: лимит аккаунта дошёл до 98 %, поэтому я остановился после трёх коммитов из примерно девяти. Переписка переезжает. Чекпоинт вне репозитория не писал, потому что задача запрещает трогать файлы за его пределами. Состояние для продолжения — ниже.

**Готово и закоммичено** в `/Users/[redacted]/homeW/ai-dev-test/investor-db`, автор [redacted: name], без трейлеров:
- `631ac55` — заготовка пакета: `pyproject.toml`, `.gitignore`, JSON Schema `schema/investor.schema.json`, `src/investordb/{__init__,__main__,cli,records}.py`. В `cli.py` уже описаны все 7 команд, модули подключаются только при вызове команды.
- `169c011` — `validate.py`: проверка по схеме (показывает самую точную ошибку внутри oneOf) и проверки согласованности: уникальность id, тикет min ≤ max ≤ самый крупный фонд, даты не в будущем и не раньше года запуска фонда, указана валюта, у каждого значения есть источник, решение сходится со своими правилами. На фикстуре: 0 ошибок; на испорченных данных ловит всё, что должна.
- `d39b4f1` — `fetch.py`: пауза 1 с на хост, User-Agent браузера, таймаут 20 с, 2 повтора, `index.json` со статусом, итоговым URL, типом, временем загрузки и sha256. HTML и PDF переводятся в текст. Отмечается, если ссылка увела на главную или на другой сайт. Проверил на живых адресах: HTML и PDF скачиваются, текст извлекается.

**Две находки по Wayback, обе учтены в коде:**
1. API доступности часто отвечает пустым ответом, хотя снимок есть (так было с python.org/about). Поэтому добавлен запасной путь через CDX API. В индекс пишется, какой из путей сработал.
2. web.archive.org отвечает 429 («бот»), когда с python-клиента приходит User-Agent браузера. Для archive.org поставил простой UA инструмента — с ним 200.

Через Wayback живьём отработал один случай: w3.org отдал 403, снимок нашёлся. Но в индексе у этого снимка `text_chars: 14` и тип `text/html` вместо PDF. Скорее всего, скачался не PDF, а какая-то заглушка; я этого не разбирал. При продолжении надо открыть сохранённый файл или проверить на другом мёртвом URL.

**Лежит на диске, но не закоммичено:**
- `data/negative_list.csv` — Crowdcube, Seedrs, Republic, Crowdberry, правило E1.
- `tests/fixtures/investors.json` — Example Ventures, Sample Crowd, Demo Capital.

**Осталось сделать** (по коммиту на пункт):
1. `textnorm.py` и `verify.py` — нормализация и поиск цитаты (точное совпадение / нечёткое ≥ 0.85 / нет / недоступно), проверка, что значение есть в цитате, включая словацкие и чешские названия месяцев. Задуманный статус `via_published` — когда дата совпадает с датой публикации источника.
2. `rules.py` (decide) — E-правила по типу и по negative list, окно I3 в 36 месяцев с включённой границей, столбец согласия со статусами `agree / disagree / human_only`.
3. `grade.py` — источник засчитывается, только если цитата найдена и значение не помечено `value_not_in_quote`. Плюс `investors.graded.json` и плоский `investors.csv`.
4. `review.py` — пропорциональная стратифицированная выборка, минимум 3 на слой, плюс `review.html` и `claims.csv`.
5. `evaluate.py` — интервалы Уилсона; «не могу проверить» считается ошибкой, рядом нестрогий вариант; полнота по `data/reference/*.csv`.
6. Тесты и итоговые прогоны `pytest` и `ruff check`.

**Мелочи:**
- `pytest` ещё не запускался, тестов пока нет.
- В схему сверх контракта добавлены необязательные `aliases`, `ticket_observed` и `investment.fund`. Без них не работают сверка с эталонными списками и проверка года запуска фонда.
- Правило координатора выполнялось: только `git add` с явными путями и `git status` перед каждым коммитом. В `research/` ничего не попало.
- Фоновых процессов не запускал. Временный кэш тестовых загрузок лежит в scratchpad.

## Message from the orchestrator

The coordinator sent a message while you were working:
Resume your task exactly where you stopped (you have your context). State on disk: commits 631ac55 (skeleton+schema), 169c011 (validate), d39b4f1 (fetch) are in; data/negative_list.csv and tests/fixtures/investors.json exist but are uncommitted — commit them with the next relevant commit. Remaining: textnorm+verify, rules (decide), grade, review-pack, eval, tests, final pytest + ruff run. Also look into the Wayback fallback case where a snapshot returned only 14 text chars as text/html instead of the PDF — likely the snapshot page is the Wayback frame; use the `id_` raw URL form (web.archive.org/web/<ts>id_/<url>) to get the original bytes. Same rules as before: explicit `git add <paths>` only, no AI mentions anywhere, all file content in English, don't touch research/. Note: someone else will soon write data/sample/investors*.json — don't create or edit those files. Don't use the Playwright MCP browser at all. Final message in English: commands, pytest summary line, limitations.

Address this before completing your current task.

→ `Bash` — Check repo state and inspect the short Wayback snapshot
```sh
git status --short && git log --oneline | head -5 && S=[tmp] && ls $S/cache3/files/ && for f in $S/cache3/files/*.raw; do echo "== $f"; head -c 600 "$f"; echo; done
```

<details><summary>result</summary>

```
?? data/
?? tests/
5dc4f6b Add Slovak VC candidate research with registry evidence
d39b4f1 Add fetch command: polite downloader with text extraction and Wayback fallback
169c011 Add validate command: schema and consistency checks
631ac55 Add package skeleton and investor record schema
9112125 Add plan: inclusion rules, evidence tiers, verification
613583c6309e71de22ee2838b0f59fd77bacd241.raw
613583c6309e71de22ee2838b0f59fd77bacd241.txt
c6720d71ee6e9f0034512b7fed99787027f23f70.raw
c6720d71ee6e9f0034512b7fed99787027f23f70.txt
== [tmp]
<!DOCTYPE html><html data-dpl-id="sha-85c0fc9" class="uds-color-mode-light" lang="en-US" style="color-scheme:light"><head><meta charSet="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><link rel="preload" as="image" href="https://s.yimg.com/lo/mysterio/api/5b9b2c4ccf9c16c00ed84c4a27446a414d79d0675c7d495eeb5d1c8b067eeb06/lightyear_networkapi/smartcrop_w124_h124_faces%3Bquality_90%3Bformat_webp/https%3A%2F%2Fmedia.zenfs.com%2Fen%2Fpeople_218%2Ffae9f97a18932bea93ed84614423fad3.jpg"/><link rel="preload" as="image" href="https://s.yimg.com/lo/mysterio/api/122718c1fec798
== [tmp]
%PDF-1.4
%äüöß
2 0 obj
<</Length 3 0 R/Filter/FlateDecode>>
stream
x�=��
1E
… [501 more characters]
```
</details>

→ `Bash` — Confirm snapshot text and locate content_type handling
```sh
S=[tmp] cat $S/cache3/files/c6720d71ee6e9f0034512b7fed99787027f23f70.txt; echo; cd /Users/[redacted]/homeW/ai-dev-test/investor-db && git show --stat 5dc4f6b | head -12; grep -n "content_type" src/investordb/fetch.py
```

<details><summary>result</summary>

```
Dummy PDF file
commit 5dc4f6b0083fe55513babff4a5a82751a3659e1f
Author: [redacted: name] <[redacted: email]>
Date:   Sun Oct 11 01:35:54 2026 +0200

    Add Slovak VC candidate research with registry evidence

 research/sk-vc-candidates.json | 2453 ++++++++++++++++++++++++++++++++++++++++
 research/sk-vc-candidates.md   |   68 ++
 2 files changed, 2521 insertions(+)
81:def is_pdf(content_type: str, data: bytes) -> bool:
82:    return "pdf" in (content_type or "").lower() or data[:5] == b"%PDF-"
85:def extract_text(content_type: str, data: bytes) -> str:
86:    if is_pdf(content_type, data):
88:    if "html" in (content_type or "").lower() or data.lstrip()[:1] == b"<":
169:                     content_type=r.headers.get("Content-Type", ""))
174:        entry.update(status=None, final_url=None, content_type=None, error=err)
178:        used, body, ctype = "live", r.content, entry["content_type"]
192:        used, body, ctype = "live", r.content, entry["content_type"]
```
</details>

→ `Bash` — Record stored body URL and content type in index
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/fetch.py'
s=open(p).read()
old='''    entry["used"] = used
    if body is not None:'''
new='''    entry["used"] = used
    # status/final_url/content_type above describe the live request; these describe
    # the bytes actually stored (live page or snapshot)
    entry["body_url"] = (entry["final_url"] if used == "live"
                         else entry.get("wayback_url") if used == "wayback" else None)
    entry["body_content_type"] = ctype
    if body is not None:'''
assert old in s
s=s.replace(old,new)
open(p,'w').write(s)
EOF
.venv/bin/ruff check src && sed -n 160,215p src/investordb/fetch.py
```

<details><summary>result</summary>

```
All checks passed!


def fetch_one(session, throttle: HostThrottle, url: str, files_dir: Path,
              use_wayback: bool = True) -> dict:
    entry: dict = {"url": url, "fetched_at": datetime.now(UTC).isoformat(timespec="seconds")}
    r, err = _get(session, throttle, url)
    live_ok = False
    if r is not None:
        entry.update(status=r.status_code, final_url=r.url,
                     content_type=r.headers.get("Content-Type", ""))
        entry["redirected_to_homepage"] = looks_like_homepage_redirect(url, r.url)
        entry["redirected_offsite"] = _site(url) != _site(r.url)
        live_ok = r.status_code < 400 and not entry["redirected_to_homepage"]
    else:
        entry.update(status=None, final_url=None, content_type=None, error=err)

    used, body, ctype = None, None, None
    if live_ok:
        used, body, ctype = "live", r.content, entry["content_type"]
    elif use_wayback:
        snap, how = wayback_snapshot(session, throttle, url)
        entry["wayback_url"] = snap
        entry["wayback_lookup"] = how
        if snap:
            wr, werr = _get(session, throttle, snap)
            if wr is not None and wr.status_code < 400:
                used, body, ctype = "wayback", wr.content, wr.headers.get("Content-Type", "")
                entry["wayback_status"] = wr.status_code
            else:
                entry["wayback_error"] = werr or f"HTTP {wr.status_code}"
    if used is None and r is not None and r.status_code < 400:
        # soft fa
… [1126 more characters]
```
</details>

→ `Bash` — Commit fetch index fix
```sh
git add src/investordb/fetch.py && git status --short && git commit -q -m "Record URL and content type of the stored body in the fetch index" && git log --oneline | head -1
```

<details><summary>result</summary>

```
M  src/investordb/fetch.py
?? data/
?? tests/
42f6e55 Record URL and content type of the stored body in the fetch index
```
</details>

→ `Write` /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/textnorm.py

<details><summary>result</summary>

```
File created successfully at: /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/textnorm.py (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Sanity-check normalisation, numbers, dates, quote matching
```sh
.venv/bin/python - <<'EOF'
from datetime import date
from investordb.textnorm import *
print(normalize("Dňa 12. marca 2025 sme investovali 1,5 mil. € do „Alpha“ — 1 500 000 eur, 1.500.000 Kč, 1,500,000 USD, 12.03.2025"))
for q in ["€2 mil.", "1,5 mil. eur", "€200 000", "EUR 30m", "30 miliónov eur", "$1.5bn", "200k", "fond 2021"]:
    print(q, numbers_in(normalize(q)))
t=normalize("Dňa 12. marca 2025 sme investovali. On March 12, 2025 we closed. 01.06.2023 zapísaný. in červnu 2023")
for d in [date(2025,3,12), date(2023,6,1), date(2023,6,15), date(2024,1,1)]:
    print(d, date_match(d,t))
page=normalize("Some intro text. Our first tickets range from €200 000 to €2 million for seed rounds. More text here.")
print(match_quote("Our first tickets range from €200,000 to €2 million for seed rounds.", None, page))
print(match_quote("Our first tickets range from €200 000 to €2 million for seed round", None, page))
print(match_quote("Our tickets range from €250 000 to €3 million for all rounds.", None, page))
print(match_quote("Totally unrelated sentence about cats and dogs.", None, page))
EOF
```

<details><summary>result</summary>

```
dna 12. marca 2025 sme investovali 1.5 mil. € do "alpha" - 1500000 eur, 1500000 kc, 1500000 usd, 12.03.2025
€2 mil. [2.0, 2000000.0]
1,5 mil. eur [1.5, 1500000.0]
€200 000 [200000.0]
EUR 30m [30.0, 30000000.0]
30 miliónov eur [30.0, 30000000.0]
$1.5bn [1.5, 1500000000.0]
200k [200.0, 200000.0]
fond 2021 [2021.0]
2025-03-12 full
2023-06-01 full
2023-06-15 month
2024-01-01 
('exact', 1.0)
('exact', 1.0)
('fuzzy', 0.867)
('missing', 0.0)
```
</details>

→ `Bash` — Reject fuzzy matches whose numbers differ
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/textnorm.py'
s=open(p).read()
s=s.replace('''def best_fuzzy(quote: str, text: str, max_anchors: int = 4, max_hits: int = 40) -> float:''','''def best_fuzzy(quote: str, text: str, max_anchors: int = 4,
               max_hits: int = 40) -> tuple[float, str]:''')
s=s.replace('''    if not quote or not text:
        return 0.0
    tokens''','''    if not quote or not text:
        return 0.0, ""
    tokens''')
s=s.replace('''    best = 0.0
    seen: set[int] = set()''','''    best, best_window = 0.0, ""
    seen: set[int] = set()''')
s=s.replace('''                best = max(best, sm.ratio())
            if best >= 0.999:
                return best
    return best''','''                r = sm.ratio()
                if r > best:
                    best, best_window = r, window
            if best >= 0.999:
                return best, best_window
    return best, best_window''')
s=s.replace('''    score = best_fuzzy(nq, nt)
    return ("fuzzy" if score >= FUZZY_THRESHOLD else "missing"), round(score, 3)''','''    score, window = best_fuzzy(nq, nt)
    if score < FUZZY_THRESHOLD:
        return "missing", round(score, 3)
    # a near-ident
… [835 more characters]
```

<details><summary>result</summary>

```
24:_DIGITS = re.compile(r"\d+(?:\.\d+)?")
103:    page_nums = set(_DIGITS.findall(window))
104:    if any(n not in page_nums for n in _DIGITS.findall(nq)):
('missing', 0.867)
('fuzzy', 0.942)
```
</details>

→ `Bash` — Widen window used for number comparison
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/textnorm.py'
s=open(p).read()
old='''                if r > best:
                    best, best_window = r, window'''
new='''                if r > best:
                    # keep a bit of slack so numbers at the edges are not cut in half
                    best, best_window = r, text[max(0, ws - 10):ws + int(n * 1.2) + 10]'''
assert old in s
s=s.replace(old,new)
open(p,'w').write(s)
EOF
.venv/bin/ruff check src
```

<details><summary>result</summary>

```
Exit code 1
SIM110 Use `return any(abs(x - value) <= max(0.5, rel_tol * abs(value)) for x in numbers_in(text))` instead of `for` loop
   --> src/investordb/textnorm.py:145:5
    |
144 |   def number_in(value: float, text: str, rel_tol: float = 0.01) -> bool:
145 | /     for x in numbers_in(text):
146 | |         if abs(x - value) <= max(0.5, rel_tol * abs(value)):
147 | |             return True
148 | |     return False
    | |________________^
help: Replace with `return any(abs(x - value) <= max(0.5, rel_tol * abs(value)) for x in numbers_in(text))`
    |
144 | def number_in(value: float, text: str, rel_tol: float = 0.01) -> bool:
    -     for x in numbers_in(text):
    -         if abs(x - value) <= max(0.5, rel_tol * abs(value)):
    -             return True
    -     return False
145 +     return any(abs(x - value) <= max(0.5, rel_tol * abs(value)) for x in numbers_in(text))
146 |
    |
note: This is an unsafe fix and may change runtime behavior

Found 1 error.
1 unsafe fix available with `--fix --unsafe-fixes`.
```
</details>

→ `Bash` — Fix lint in textnorm
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/textnorm.py'
s=open(p).read()
s=s.replace('''    for x in numbers_in(text):
        if abs(x - value) <= max(0.5, rel_tol * abs(value)):
            return True
    return False''','''    tol = max(0.5, rel_tol * abs(value))
    return any(abs(x - value) <= tol for x in numbers_in(text))''')
s=s.replace('''def _join_thousands(m: re.Match) -> str:
    sep = m.group(3)
    groups = m.group(2)
    # "12, 300" style with comma+space never reaches here; a single space or dot is a separator
    return m.group(1) + groups.replace(sep, "")''','''def _join_thousands(m: re.Match) -> str:
    return m.group(1) + m.group(2).replace(m.group(3), "")''')
open(p,'w').write(s)
EOF
.venv/bin/ruff check src
```

<details><summary>result</summary>

```
All checks passed!
```
</details>

→ `Write` /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/verify.py

<details><summary>result</summary>

```
File created successfully at: /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/verify.py (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Build offline fixture cache and run verify on it
```sh
mkdir -p tests/fixtures/cache/files && .venv/bin/python - <<'EOF'
import json, hashlib
from pathlib import Path
from investordb.fetch import cache_key
base=Path("tests/fixtures/cache")
pages={
 "https://example.com/about": ("live", "About us\nWe back software and deep‑tech founders from Central Europe.\nOur first tickets range from €200 000 to €2 mil.\nContact"),
 "https://example.org/fof/portfolio": ("wayback", "Portfolio\nExample Fund I closed at 30 mil. EUR in 2021.\nOther funds"),
 "https://example.com/news/alpha": ("live", "News\nDňa 12. marca 2025 sme investovali 1,5 mil. eur do Alpha Robotics.\nRead more"),
 "https://example.org/registry/beta": ("live", "Výpis\nSpoločník: Example Ventures a.s., zapísaný 01.06.2023.\n"),
}
index={}
for url,(used,text) in pages.items():
    k=cache_key(url)
    (base/"files"/f"{k}.txt").write_text(text,encoding="utf-8")
    index[url]={"url":url,"status":200 if used=="live" else 404,"final_url":url,"content_type":"text/html",
      "fetched_at":"2026-10-01T10:00:00+00:00","sha256":hashlib.sha256(text.encode()).hexdigest(),"used":used,
      "body_url":url,"body_content_type":"text/html","text_file":f"files/{k}.txt","text_chars":len(text)}
u="h
… [609 more characters]
```

<details><summary>result</summary>

```
7 checks over 2 records, 5 URLs
quote: 6/7 pass (85.7 %) - exact 6, fuzzy 0, missing 0, unreachable 1
value: n/a 2, ok 5
tier A: 2/2 quotes pass
tier B: 4/4 quotes pass
tier C: 0/1 quotes pass
problems (first 20):
  demo-capital investments[0] #0: unreachable/ok https://example.com/news/gamma
wrote [tmp]
record_id,record_name,target,kind,label,source_index,url,tier,publisher,quote_status,similarity,value_status,value_detail,fetch_used,http_status,final_url
example-ventures,Example Ventures,fields.sectors,sectors,sectors,0,https://example.com/about,B,Example Ventures,exact,1.0,n/a,,live,200,https://example.com/about
example-ventures,Example Ventures,fields.geography,geography,geography,0,https://example.com/about,B,Example Ventures,exact,1.0,n/a,,live,200,https://example.com/about
example-ventures,Example Ventures,fields.ticket,ticket,ticket,0,https://example.com/about,B,Example Ventures,exact,1.0,ok,min=200000:ok; max=2000000:ok,live,200,https://example.com/about
example-ventures,Example Ventures,fields.funds,funds,funds,0,https://example.org/fof/portfolio,A,Example Fund of Funds,exact,1.0,ok,size[Example Fund I]=30000000:ok; vintage[Example Fund I]=2021:ok,wayback,404,https://example.org/fof/portfolio
example-ventures,Example Ventures,investments[0],investment,Alpha Robotics,0,https://example.com/news/alpha,B,Example Ventures,exact,1.0,ok,date=2025-03-12:ok; round=1500000:ok,
… [451 more characters]
```
</details>

→ `Bash` — Commit textnorm and verify
```sh
.venv/bin/ruff check src && git add src/investordb/textnorm.py && git status --short && git commit -q -m "Add text normalisation and quote matching" && git add src/investordb/verify.py && git status --short && git commit -q -m "Add verify command: quote and value checks against cached pages" && git log --oneline | head -2
```

<details><summary>result</summary>

```
All checks passed!
A  src/investordb/textnorm.py
?? data/
?? src/investordb/verify.py
?? tests/
A  src/investordb/verify.py
?? data/
?? tests/
f37cdd8 Add verify command: quote and value checks against cached pages
be4e03f Add text normalisation and quote matching
```
</details>

→ `Bash` — Add organisation name key helper and try it
```sh
cat >> src/investordb/textnorm.py <<'EOF'


# --- names ---------------------------------------------------------------------

_LEGAL_FORMS = {
    "sro", "spol", "as", "ks", "vos", "se", "ltd", "limited", "llc", "lp", "llp", "gmbh", "ag",
    "sa", "sas", "bv", "nv", "plc", "inc", "corp", "co", "sicav", "zrt", "kft", "spzoo", "oy",
    "ab", "the",
}


def name_key(name: str) -> str:
    """Loose key for matching organisation names across lists ("Neulogy Ventures a.s." ==
    "NEULOGY VENTURES")."""
    s = strip_diacritics(name.translate(_CHAR_MAP)).casefold().replace("&", " and ")
    s = re.sub(r"\b([a-z])\.(?=[a-z]\.)", r"\1", s)  # s.r.o. -> sr.o. -> handled below
    s = re.sub(r"[.,'\"()\-/]", "", s)  # s.r.o. -> sro, a.s. -> as
    tokens = [t for t in s.split() if t not in _LEGAL_FORMS]
    return " ".join(tokens)
EOF
.venv/bin/python -c "
from investordb.textnorm import name_key as k
for n in ['Neulogy Ventures a.s.','NEULOGY VENTURES','Crowdberry','Zero Gravity Capital, s. r. o.','Slovak Investment Holding, a.s.','Bros & Co','Seed Starter s.r.o.','Limerock Fund Manager, správ. spol., a.s.']: print(repr(n), '->', repr(k(n)))
"
```

<details><summary>result</summary>

```
'Neulogy Ventures a.s.' -> 'neulogy ventures'
'NEULOGY VENTURES' -> 'neulogy ventures'
'Crowdberry' -> 'crowdberry'
'Zero Gravity Capital, s. r. o.' -> 'zero gravity capital s r o'
'Slovak Investment Holding, a.s.' -> 'slovak investment holding'
'Bros & Co' -> 'bros and'
'Seed Starter s.r.o.' -> 'seed starter'
'Limerock Fund Manager, správ. spol., a.s.' -> 'limerock fund manager sprav'
```
</details>

→ `Bash` — Improve legal form stripping in name key
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/textnorm.py'
s=open(p).read()
s=s.replace('''    s = re.sub(r"\\b([a-z])\\.(?=[a-z]\\.)", r"\\1", s)  # s.r.o. -> sr.o. -> handled below
    s = re.sub(r"[.,'\\"()\\-/]", "", s)  # s.r.o. -> sro, a.s. -> as
    tokens = [t for t in s.split() if t not in _LEGAL_FORMS]
    return " ".join(tokens)''','''    s = re.sub(r"[.,'\\"()\\-/]", " ", s)
    # glue runs of single letters back together: "s r o" -> "sro", "a s" -> "as"
    s = re.sub(r"\\b[a-z](?: [a-z]\\b)+", lambda m: m.group(0).replace(" ", ""), s)
    tokens = [t for t in s.split() if t not in _LEGAL_FORMS]
    return " ".join(tokens)''')
s=s.replace('''"sas", "bv", "nv", "plc", "inc", "corp", "co", "sicav",''','''"sas", "bv", "nv", "plc", "inc", "corp", "sicav", "sprav",''')
open(p,'w').write(s)
EOF
.venv/bin/python -c "
from investordb.textnorm import name_key as k
for n in ['Neulogy Ventures a.s.','Zero Gravity Capital, s. r. o.','Slovak Investment Holding, a.s.','Bros & Co','Seed Starter s.r.o.','Limerock Fund Manager, správ. spol., a.s.','Vision Ventures k.s.','Index Ventures','A B Capital']: print(repr(n), '->', repr(k(n)))
"
```

<details><summary>result</summary>

```
'Neulogy Ventures a.s.' -> 'neulogy ventures'
'Zero Gravity Capital, s. r. o.' -> 'zero gravity capital s r o'
'Slovak Investment Holding, a.s.' -> 'slovak investment holding'
'Bros & Co' -> 'bros and co'
'Seed Starter s.r.o.' -> 'seed starter'
'Limerock Fund Manager, správ. spol., a.s.' -> 'limerock fund manager'
'Vision Ventures k.s.' -> 'vision ventures'
'Index Ventures' -> 'index ventures'
'A B Capital' -> 'capital'
```
</details>

→ `Bash` — Glue only known spaced legal forms
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/textnorm.py'
s=open(p).read()
old=s[s.index('    # glue runs of single letters'):s.index('    tokens = [t for t in s.split() if t not in _LEGAL_FORMS]')]
new='''    s = " ".join(s.split())
    # "s. r. o." ends up as "s r o"; glue the usual spaced forms back together
    s = re.sub(r"\\b(?:s r o|a s|k s|v o s)\\b", lambda m: m.group(0).replace(" ", ""), s)
'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
sed -n '/^def name_key/,$p' src/investordb/textnorm.py; .venv/bin/python -c "
from investordb.textnorm import name_key as k
for n in ['Zero Gravity Capital, s. r. o.','Bros & Co','A B Capital','Neulogy Ventures a. s.','Example Ventures']: print(repr(n), '->', repr(k(n)))
"
```

<details><summary>result</summary>

```
def name_key(name: str) -> str:
    """Loose key for matching organisation names across lists ("Neulogy Ventures a.s." ==
    "NEULOGY VENTURES")."""
    s = strip_diacritics(name.translate(_CHAR_MAP)).casefold().replace("&", " and ")
    s = re.sub(r"[.,'\"()\-/]", " ", s)
    s = " ".join(s.split())
    # "s. r. o." ends up as "s r o"; glue the usual spaced forms back together
    s = re.sub(r"\b(?:s r o|a s|k s|v o s)\b", lambda m: m.group(0).replace(" ", ""), s)
    tokens = [t for t in s.split() if t not in _LEGAL_FORMS]
    return " ".join(tokens)
'Zero Gravity Capital, s. r. o.' -> 'zero gravity capital'
'Bros & Co' -> 'bros and co'
'A B Capital' -> 'a b capital'
'Neulogy Ventures a. s.' -> 'neulogy ventures'
'Example Ventures' -> 'example ventures'
```
</details>

→ `Write` /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/rules.py

<details><summary>result</summary>

```
File created successfully at: /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/rules.py (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Run decide on fixture and check month math
```sh
S=[tmp] .venv/bin/python -m investordb decide --records tests/fixtures/investors.json --ref-date 2026-10-11 --out $S/dc.csv && cat $S/dc.csv && .venv/bin/python -c "
from datetime import date
from investordb.rules import months_back, months_between
print(months_back(date(2026,10,11),36), months_back(date(2028,2,29),36), months_back(date(2026,5,31),1), months_between(date(2023,10,11),date(2026,10,11)), months_between(date(2023,10,12),date(2026,10,11)))
" && .venv/bin/ruff check src
```

<details><summary>result</summary>

```
Exit code 1
reference date 2026-10-11, window 36 months; DISAGREE 1, agree 2
  DISAGREE   demo-capital: stored dormant [E4] vs computed uncertain [I3?] - no dated investment with a Tier A/B source
wrote [tmp] (stored decisions were not changed)
record_id,name,type,stored_status,stored_rules,computed_status,computed_rules,agreement,last_ab_investment,months_since,reasons
example-ventures,Example Ventures,vc,included,I1;I2;I3;I4,included,I1;I2;I3;I4,agree,2025-03-12,18,Tier A source for funds
sample-crowd,Sample Crowd,platform,excluded,E1,excluded,E1,agree,,,type is platform (routes other people's money)
demo-capital,Demo Capital,vc,dormant,E4,uncertain,I3?,DISAGREE,,,no dated investment with a Tier A/B source
2023-10-11 2025-02-28 2026-04-30 36 35
E501 Line too long (103 > 100)
  --> src/investordb/rules.py:93:101
   |
91 |     if len(companies) >= 3:
92 |         return True, f"{len(companies)} portfolio companies with Tier A/B sources"
93 |     return False, f"no registration/FoF evidence and only {len(companies)} sourced portfolio companies"
   |                                                                                                     ^^^

Found 1 error.
```
</details>

→ `Bash` — Treat old evidence of any tier as dormant
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/rules.py'
s=open(p).read()
s=s.replace('''    return False, f"no registration/FoF evidence and only {len(companies)} sourced portfolio companies"''','''    return False, (f"no registration/FoF evidence and only {len(companies)} "
                   "sourced portfolio companies")''')
s=s.replace('''def last_ab_investment(rec: dict) -> date | None:
    dates = []
    for inv in rec.get("investments") or []:
        d = parse_date(inv.get("date"))
        if d and any(s.get("tier") in ("A", "B") for s in inv.get("sources") or []):
            dates.append(d)
    return max(dates) if dates else None''','''def last_investment(rec: dict, tiers=("A", "B")) -> date | None:
    dates = []
    for inv in rec.get("investments") or []:
        d = parse_date(inv.get("date"))
        if d and any(s.get("tier") in tiers for s in inv.get("sources") or []):
            dates.append(d)
    return max(dates) if dates else None''')
s=s.replace('''    last = last_ab_investment(rec)''','''    last = last_investment(rec)''')
old=s[s.index('    cutoff = months_back(ref, window_months)'):s.index('    failed = []')]
new='''    cutoff = months_back(ref, window_mo
… [866 more characters]
```

<details><summary>result</summary>

```
reference date 2026-10-11, window 36 months; agree 3
wrote [tmp] (stored decisions were not changed)
All checks passed!
```
</details>

→ `Bash` — Commit rule engine and negative list
```sh
git add src/investordb/textnorm.py src/investordb/rules.py data/negative_list.csv && git status --short && git commit -q -m "Add decide command: rule engine for I3 recency and E-rule exclusions" && git log --oneline | head -1
```

<details><summary>result</summary>

```
A  data/negative_list.csv
A  src/investordb/rules.py
M  src/investordb/textnorm.py
?? data/reference/
?? tests/
162da7c Add decide command: rule engine for I3 recency and E-rule exclusions
```
</details>

→ `Bash` — Inspect untracked data/reference contents
```sh
ls -la data/reference data/ eval/ && head -5 data/reference/* 2>/dev/null
```

<details><summary>result</summary>

```
data/:
total 8
drwxr-xr-x   5 [user]  staff  160 11 окт.  01:38 .
drwxr-xr-x  14 [user]  staff  448 11 окт.  01:29 ..
-rw-r--r--   1 [user]  staff  326 11 окт.  01:29 negative_list.csv
drwxr-xr-x   3 [user]  staff   96 11 окт.  01:38 reference
drwxr-xr-x   3 [user]  staff   96 11 окт.  01:38 sample

data/reference:
total 8
drwxr-xr-x  3 [user]  staff    96 11 окт.  01:38 .
drwxr-xr-x  5 [user]  staff   160 11 окт.  01:38 ..
-rw-r--r--  1 [user]  staff  1592 11 окт.  01:38 cvca-full-members.csv

eval/:
total 0
drwxr-xr-x   2 [user]  staff   64 11 окт.  01:27 .
drwxr-xr-x  14 [user]  staff  448 11 окт.  01:29 ..
name,source_url
Abris Capital,https://cvca.cz/en/abris-capital-2/
ARX Equity Partners,https://cvca.cz/en/arx-equity-partners-2/
Credo Ventures,https://cvca.cz/en/credo-ventures-2/
CVI,https://cvca.cz/en/cvi-2/
```
</details>

→ `Write` /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/grade.py

<details><summary>result</summary>

```
File created successfully at: /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/grade.py (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Run grade on fixture
```sh
S=[tmp] .venv/bin/python -m investordb grade --records tests/fixtures/investors.json --verification $S/verification.csv --out-json $S/g.json --out-csv $S/g.csv && cat $S/g.csv && .venv/bin/python -c "
import json; print([ (r['id'], r['grade']) for r in json.load(open('$S/g.json'))])" && .venv/bin/ruff check src
```

<details><summary>result</summary>

```
3 records graded: A 1, B 0, C 2
wrote [tmp] and [tmp]
id,name,type,hq_country,hq_city,website,legal_entities,decision_status,decision_rules,sectors,sectors_source,stages,stages_source,geography,geography_source,ticket_min,ticket_max,ticket_currency,ticket_source,funds,funds_source,aum_amount,aum_currency,aum_as_of,aum_source,investments_count,last_investment_date,last_investment_company,last_investment_source,confidence,confidence_reason
example-ventures,Example Ventures,vc,SK,Bratislava,https://example.com/,ICO:12345678,included,I1;I2;I3;I4,software;deeptech,https://example.com/about,,,SK;CZ,https://example.com/about,200000,2000000,EUR,https://example.com/about,"Example Fund I (30000000 EUR, 2021)",https://example.org/fof/portfolio,,,,,2,2025-03-12,Alpha Robotics,https://example.com/news/alpha,A,"existence by Tier A, dated investment by Tier A"
sample-crowd,Sample Crowd,platform,CZ,Praha,https://example.net/,,excluded,E1,,,,,,,,,,,,,,,,,0,,,,C,"no dated investment proven by Tier A/B; existence not proven (no Tier A, 0 A/B companies)"
demo-capital,Demo Capital,vc,SK,Košice,,ICO:87654321,dormant,E4,,,,,,,,,,,,,,,,,1,,,,C,"no dated investment proven by Tier A/B; existence not proven (no Tier A, 0 A/B companies)"
[('example-ventures', {'confidence': 'A', 'reason': 'existence by Tier A, dated investment by T
… [1015 more characters]
```
</details>

→ `Bash` — Commit grade module
```sh
git add src/investordb/grade.py && git status --short && git commit -q -m "Add grade command: confidence per record and flat CSV export" && git log --oneline | head -1
```

<details><summary>result</summary>

```
A  src/investordb/grade.py
?? data/reference/
?? tests/
d559fef Add grade command: confidence per record and flat CSV export
```
</details>

→ `Write` /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/review.py

<details><summary>result</summary>

```
File created successfully at: /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/review.py (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Build review pack from fixture and syntax-check JS
```sh
S=[tmp] .venv/bin/python -m investordb review-pack --records tests/fixtures/investors.json --n 60 --seed 7 --html $S/review.html --claims $S/claims.csv && cat $S/claims.csv && which node && .venv/bin/python - <<EOF
import re
h=open("$S/review.html").read()
js=re.search(r"<script>(.*)</script>", h, re.S).group(1)
open("$S/review.js","w").write(js)
EOF
node --check $S/review.js && echo JS_OK; .venv/bin/ruff check src
```

<details><summary>result</summary>

```
Exit code 1
8 claims in total, sampled 8 (seed 7): existence 1, field:sectors 1, field:geography 1, field:ticket 1, field:funds 1, investment 3
wrote [tmp] and [tmp]
claim_id,record_id,record_name,decision_status,kind,field,stratum,claim,quote,url,tier,publisher,published,other_urls,stratum_size
example-ventures/field/sectors,example-ventures,Example Ventures,included,field,sectors,field:sectors,"Sectors of Example Ventures: software, deeptech",We back software and deep-tech founders from Central Europe.,https://example.com/about,B,Example Ventures,,,1
example-ventures/field/geography,example-ventures,Example Ventures,included,field,geography,field:geography,"Geography of Example Ventures: SK, CZ",We back software and deep-tech founders from Central Europe.,https://example.com/about,B,Example Ventures,,,1
example-ventures/investment/1,example-ventures,Example Ventures,included,investment,,investment,Example Ventures invested in Beta Health on 2023-06-01 (registry_entry).,"Spoločník: Example Ventures a.s., zapísaný 01.06.2023.",https://example.org/registry/beta,A,Example Registry,2023-06-01,,3
demo-capital/investment/0,demo-capital,Demo Capital,dormant,investment,,investment,Demo Capital invested in Gamma Labs on 2019-11-20 (announced).,Demo Capital invested in Gamma Labs on 20 November 2019.,ht
… [3553 more characters]
```
</details>

→ `Bash` — Fix lint and dedupe extra source links
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/review.py'
s=open(p).read()
for k,(bg,fg) in {"correct":("ok-bg","ok"),"wrong":("bad-bg","bad"),"cant_verify":("unk-bg","unk")}.items():
    old=f'button.{k}[aria-pressed="true"] {{ background: var(--{bg}); color: var(--{fg}); border-color: var(--{fg}); }}'
    new=f'button.{k}[aria-pressed="true"] {{\n  background: var(--{bg}); color: var(--{fg}); border-color: var(--{fg}); }}'
    assert old in s; s=s.replace(old,new)
old='''            c["other_urls"] = ";".join(u for u in [c["other_urls"], *extra] if u)'''
new='''            urls = [*c["other_urls"].split(";"), *extra]
            c["other_urls"] = ";".join(dict.fromkeys(u for u in urls if u and u != c["url"]))'''
assert old in s; s=s.replace(old,new)
old='''    others = [s.get("url") for s in sources if s is not p and s.get("url")]'''
new='''    others = list(dict.fromkeys(s.get("url") for s in sources
                                if s is not p and s.get("url") and s.get("url") != p.get("url")))'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
.venv/bin/ruff check src && S=[tmp] && .ve
… [177 more characters]
```

<details><summary>result</summary>

```
All checks passed!
example-ventures/existence,example-ventures,Example Ventures,included,existence,,existence,"Example Ventures is a real investor of type 'vc' that still invests (HQ Bratislava, SK; ICO 12345678).",Example Fund I closed at 30 mil. EUR in 2021.,https://example.org/fof/portfolio,A,Example Fund of Funds,2021-05-10,https://example.org/registry/beta;https://example.com/about;https://example.com/;https://example.com/register/12345678,1
```
</details>

→ `Bash` — Render review page headless to check output
```sh
S=[tmp] C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; ls "$C" >/dev/null && mkdir -p $S/chrome-prof && "$C" --headless=new --disable-gpu --no-first-run --user-data-dir=$S/chrome-prof --dump-dom "file://$S/review.html" 2>/dev/null | grep -o 'class="card[^"]*"' | wc -l; "$C" --headless=new --disable-gpu --no-first-run --user-data-dir=$S/chrome-prof --window-size=390,1400 --screenshot=$S/mobile.png "file://$S/review.html" 2>/dev/null; "$C" --headless=new --disable-gpu --no-first-run --user-data-dir=$S/chrome-prof --force-dark-mode --blink-settings=preferredColorScheme=0 --window-size=1100,900 --screenshot=$S/desktop.png "file://$S/review.html" 2>/dev/null; ls -la $S/*.png
```

<details><summary>result</summary>

```
Command did not complete within its 120s timeout and was moved to the background (ID: bto7gtm12). Output is being written to: [tmp] You will be notified when it completes. To check interim output, use Read on that file path.
```
</details>

→ `Bash` — Check headless Chrome progress
```sh
cat [tmp] ls -la [tmp] 2>&1; pgrep -fl "chrome-prof" | head
```

<details><summary>result</summary>

```
(eval):1: no matches found: [tmp]
39906 /bin/zsh -c source /Users/[redacted]/.claude-account2/shell-snapshots/snapshot-zsh-1791675347633-vt1zsd.sh 2>/dev/null || true && setopt NO_EXTENDED_GLOB NO_BARE_GLOB_QUAL 2>/dev/null || true && { \builtin unalias -- 'unsetenv'; \builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'S=[tmp] C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; ls "$C" >/dev/null && mkdir -p $S/chrome-prof && "$C" --headless=new --disable-gpu --no-first-run --user-data-dir=$S/chrome-prof --dump-dom "file://$S/review.html" 2>/dev/null | grep -o '"'"'class="card[^"]*"'"'"' | wc -l; "$C" --headless=new --disable-gpu --no-first-run --user-data-dir=$S/chrome-prof --window-size=390,1400 --screenshot=$S/mobile.png "file://$S/review.html" 2>/dev/null; "$C" --headless=new --disable-gpu --no-first-run --user-data-dir=$S/chrome-prof --force-dark-mode --blink-settings=preferredColorScheme=0 --window-size=1100,900 --screenshot=$S/desktop.png "file://$S/review.html" 2>/dev/null; ls -la $S/*.png' < /dev/null && pwd -P >| /tmp/claude-9efc-cwd
39909 /Applications/Google Chrome.app/Contents/MacOS/Google Chrome --headless=new --disable-gpu --no-first-run --user-data-dir=[tmp] --dump-dom file:///private
… [3554 more characters]
```
</details>

→ `Bash` — Stop hung headless Chrome and look for jsdom
```sh
pkill -f "scratchpad/chrome-prof"; sleep 1; pgrep -fl "chrome-prof" | wc -l; rm -rf [tmp] npm ls -g 2>/dev/null | grep -i jsdom; ls /opt/homebrew/lib/node_modules 2>/dev/null
```

<details><summary>result</summary>

```
       5
@openai
ccusage
npm
vercel
```
</details>

→ `Bash` — Force-kill leftover headless Chrome
```sh
pgrep -fl "chrome-prof" | awk '{print $1}' | xargs -r kill -9 2>/dev/null; sleep 1; pgrep -f "chrome-prof" | wc -l
```

<details><summary>result</summary>

```
       0
```
</details>

→ `Bash` — Exercise review page script with a small DOM stub
```sh
S=[tmp] cd /Users/[redacted]/homeW/ai-dev-test/investor-db && .venv/bin/python - <<EOF
import re
h=open("$S/review.html").read()
open("$S/review.js","w").write(re.search(r"<script>(.*)</script>", h, re.S).group(1))
EOF
cat > $S/domstub.js <<'EOF'
const fs = require("fs");
function El(tag){ this.tagName=tag; this.children=[]; this.listeners={}; this.attrs={}; this._text=""; this.className=""; this.hidden=false; this.value="all"; }
El.prototype.appendChild=function(c){ this.children.push(c); return c; };
Object.defineProperty(El.prototype,"textContent",{get(){return this._text+this.children.map(c=>c.textContent).join("");},set(v){this._text=v;this.children=[];}});
El.prototype.addEventListener=function(t,f){ (this.listeners[t]=this.listeners[t]||[]).push(f); };
El.prototype.setAttribute=function(k,v){ this.attrs[k]=v; };
El.prototype.click=function(){ (this.listeners.click||[]).forEach(f=>f()); if(this.tagName==="a"&&this.download) global.downloaded=this; };
El.prototype.remove=function(){};
const ids={}; ["progress","filter","export","list","storage-warn"].forEach(i=>ids[i]=new El(i==="filter"?"select":"div")
… [1444 more characters]
```

<details><summary>result</summary>

```
cards: 8 | 0 / 8 reviewed
after: 3 / 8 reviewed | card0 class: card correct
todo shown: 5
download: labels.csv
claim_id,label,note,reviewed_at
example-ventures/field/sectors,correct,,<ts>
example-ventures/field/geography,wrong,,<ts>
example-ventures/investment/1,cant_verify,"page 404, ""moved""",<ts>
```
</details>

→ `Bash` — Commit review pack
```sh
git add src/investordb/review.py && git status --short && git commit -q -m "Add review-pack command: stratified claim sample and static review page" && git log --oneline | head -1
```

<details><summary>result</summary>

```
A  src/investordb/review.py
?? data/reference/
?? tests/
f291367 Add review-pack command: stratified claim sample and static review page
```
</details>

→ `Bash` — Add Wilson interval helper
```sh
cat > src/investordb/stats.py <<'EOF'
import math

Z95 = 1.959963984540054


def wilson(k: int, n: int, z: float = Z95) -> tuple[float, float] | None:
    """Wilson score interval for k successes out of n. None when n == 0."""
    if n <= 0:
        return None
    if not 0 <= k <= n:
        raise ValueError(f"k={k} must be within 0..{n}")
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return max(0.0, centre - half), min(1.0, centre + half)


def rate(k: int, n: int) -> dict:
    ci = wilson(k, n)
    return {
        "k": k, "n": n,
        "value": round(k / n, 4) if n else None,
        "ci95": [round(ci[0], 4), round(ci[1], 4)] if ci else None,
    }
EOF
.venv/bin/python -c "
from investordb.stats import wilson
print(wilson(0,10), wilson(10,10), wilson(5,10), wilson(81,100))"
```

<details><summary>result</summary>

```
(0.0, 0.2775327998628892) (0.7224672001371107, 0.9999999999999999) (0.236593090512564, 0.7634069094874361) (0.7222115462093562, 0.8748524849023126)
```
</details>

→ `Write` /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/evaluate.py

<details><summary>result</summary>

```
File created successfully at: /Users/[redacted]/homeW/ai-dev-test/investor-db/src/investordb/evaluate.py (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Run eval with and without labels on fixture data
```sh
S=[tmp] && mkdir -p tests/fixtures/reference && cat > tests/fixtures/reference/example-association.csv <<'EOF'
name,source_url
EXAMPLE VENTURES a.s.,https://example.org/members/example-ventures
Demo Capital,https://example.org/members/demo-capital
Missing Partners,https://example.org/members/missing-partners
EOF
cat > $S/labels.csv <<'EOF'
claim_id,label,note,reviewed_at
example-ventures/existence,correct,,2026-10-11T10:00:00Z
example-ventures/field/ticket,correct,,2026-10-11T10:01:00Z
example-ventures/field/sectors,wrong,"says deep-tech only",2026-10-11T10:02:00Z
example-ventures/investment/0,correct,,2026-10-11T10:03:00Z
demo-capital/investment/0,cant_verify,404,2026-10-11T10:04:00Z
bogus/claim,correct,,
EOF
.venv/bin/python -m investordb eval --records tests/fixtures/investors.json --claims $S/claims.csv --labels $S/labels.csv --reference tests/fixtures/reference --verification $S/verification.csv --decision-check $S/dc.csv --graded $S/g.json --out-md $S/ACCURACY.md --out-json $S/metrics.json && cat $S/ACCURACY.md && echo ---- && .venv/bin/python -m investordb eval --records tests/fixtures/investors.j
… [260 more characters]
```

<details><summary>result</summary>

```
labelled 5/8; overall strict 60.0 % (23.1-88.2); inclusion precision strict 100.0 % (20.6-100.0)
recall example-association: 2/3 66.7 % (20.8-93.8)
quote pass rate 85.7 % (48.7-97.4)
wrote [tmp] and [tmp]
# Accuracy report

Built by `python -m investordb eval` on 2026-10-11.

## Human review

5 of 8 sampled claims labelled.

| Metric | Labelled | Correct | Wrong | Can't verify | Strict (95 % CI) | Lenient (95 % CI) |
|---|---:|---:|---:|---:|---|---|
| Inclusion precision | 1 | 1 | 0 | 0 | 100.0 % (20.6-100.0) | 100.0 % (20.6-100.0) |
| Field: sectors | 1 | 0 | 1 | 0 | 0.0 % (0.0-79.3) | 0.0 % (0.0-79.3) |
| Field: ticket | 1 | 1 | 0 | 0 | 100.0 % (20.6-100.0) | 100.0 % (20.6-100.0) |
| Investment date | 2 | 1 | 0 | 1 | 50.0 % (9.4-90.5) | 100.0 % (20.6-100.0) |
| **All claims** | 5 | 3 | 1 | 1 | 60.0 % (23.1-88.2) | 75.0 % (30.1-95.4) |

Ignored label rows: bogus/claim: not in claims.csv

## Recall against reference lists

| List | Entities | Covered | Recall (95 % CI) | Decisions of covered |
|---|---:|---:|---|---|
| example-association | 3 | 2 | 66.7 % (20.8-93.8) | dormant 1, included 1 |

Not covered from `example-association`: Missing Partners.

## Automated checks

| Check | Value (95 % CI) |
|---|---|
| Quote found on page, all sources | 85.7 % (48.7-97.4) |
| Quote found on page, reacha
… [2330 more characters]
```
</details>

→ `Bash` — Commit eval and stats
```sh
git add src/investordb/stats.py src/investordb/evaluate.py && git status --short && git commit -q -m "Add eval command: accuracy, recall and automated check metrics with Wilson intervals" && git log --oneline | head -1
```

<details><summary>result</summary>

```
A  src/investordb/evaluate.py
A  src/investordb/stats.py
?? data/reference/
?? tests/
202c58b Add eval command: accuracy, recall and automated check metrics with Wilson intervals
```
</details>

→ `Bash` — Write conftest and normalisation tests, run them
```sh
cd /Users/[redacted]/homeW/ai-dev-test/investor-db/tests && cat > conftest.py <<'EOF'
import copy
import json
from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES


@pytest.fixture
def records() -> list[dict]:
    return json.loads((FIXTURES / "investors.json").read_text(encoding="utf-8"))


@pytest.fixture
def example(records) -> dict:
    return copy.deepcopy(records[0])
EOF
cat > test_textnorm.py <<'EOF'
from datetime import date

import pytest

from investordb.textnorm import (
    date_match,
    match_quote,
    name_key,
    normalize,
    number_in,
    numbers_in,
)


def test_normalize_strips_slovak_diacritics_and_case():
    assert normalize("Spoločník: ŽILINA, Ľubomír, Ďurčo, Šťastný") == (
        "spolocnik: zilina, lubomir, durco, stastny"
    )


def test_normalize_unifies_spaces_quotes_and_dashes():
    raw = "„Fond“ – ‘seed’ stage —\tfinal\n\nround"
    assert normalize(raw) == "\"fond\" - 'seed' stage - final round"


@pytest.mark.parametrize("raw", ["1 500 000", "1 500 000", "1.500.000", "1,500,000",
                                 "1 500 000"])
def test_normalize_tho
… [3557 more characters]
```

<details><summary>result</summary>

```
........................................                                 [100%]
40 passed in 0.02s
```
</details>

→ `Bash` — Add locative month names and rerun tests
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/textnorm.py'
s=open(p).read()
old=s[s.index("MONTHS = {"):s.index("}\n\n\ndef _names")+1]
new='''MONTHS = {
    1: ["january", "jan", "januar", "januara", "januari", "leden", "ledna", "lednu"],
    2: ["february", "feb", "februar", "februara", "februari", "unor", "unora", "unoru"],
    3: ["march", "mar", "marec", "marca", "marci", "brezen", "brezna", "breznu"],
    4: ["april", "apr", "aprila", "aprili", "duben", "dubna", "dubnu"],
    5: ["may", "maj", "maja", "maji", "kveten", "kvetna", "kvetnu"],
    6: ["june", "jun", "juna", "juni", "cerven", "cervna", "cervnu"],
    7: ["july", "jul", "jula", "juli", "cervenec", "cervence", "cervenci"],
    8: ["august", "aug", "augusta", "auguste", "srpen", "srpna", "srpnu"],
    9: ["september", "sep", "sept", "septembra", "septembri", "zari"],
    10: ["october", "oct", "oktober", "oktobra", "oktobri", "rijen", "rijna", "rijnu"],
    11: ["november", "nov", "novembra", "novembri", "listopad", "listopadu"],
    12: ["december", "dec", "decembra", "decembri", "prosinec", "prosince", "prosinci"],
}'''
s=s.replace(old,new)
s=s.replace("# month names after normalize() (no diacritics, casefolded): En
… [386 more characters]
```

<details><summary>result</summary>

```
........................................                                 [100%]
40 passed in 0.02s
```
</details>

→ `Bash` — Write stats, rules and schema tests and run
```sh
cd /Users/[redacted]/homeW/ai-dev-test/investor-db/tests && cat > test_stats.py <<'EOF'
import pytest

from investordb.stats import rate, wilson


@pytest.mark.parametrize("k,n,lo,hi", [
    (0, 10, 0.0, 0.2775),
    (10, 10, 0.7225, 1.0),
    (5, 10, 0.2366, 0.7634),
    (81, 100, 0.7222, 0.8749),
    (1, 1, 0.2065, 1.0),
])
def test_wilson_known_values(k, n, lo, hi):
    a, b = wilson(k, n)
    assert a == pytest.approx(lo, abs=1e-4)
    assert b == pytest.approx(hi, abs=1e-4)


def test_wilson_bounds_and_edge_cases():
    assert wilson(0, 0) is None
    with pytest.raises(ValueError):
        wilson(3, 2)
    for n in (1, 7, 60):
        for k in range(n + 1):
            lo, hi = wilson(k, n)
            assert 0.0 <= lo <= k / n <= hi <= 1.0


def test_rate():
    assert rate(3, 4)["value"] == 0.75
    assert rate(0, 0) == {"k": 0, "n": 0, "value": None, "ci95": None}
EOF
cat > test_rules.py <<'EOF'
import copy
from datetime import date

import pytest

from investordb.rules import (
    agreement,
    decide,
    load_negative_list,
    months_back,
    months_between,
)

REF = date(2026, 10, 11)


def with_last_investment(rec: dict, d: str, tier: str = "B") -> dict:
    rec = copy
… [5717 more characters]
```

<details><summary>result</summary>

```
validator = Draft202012Validator(schema={'$defs': {'aum': {'additionalProperties': False, 'properties': {'amount': {'minimum': 0, ...ormat_checker=<FormatChecker checkers=['date', 'email', 'idn-email', 'idn-hostname', 'ipv4', 'ipv6', 'regex', 'uuid']>)

    def test_consistency_checks(records, validator):
        bad = copy.deepcopy(records)
        bad[0]["fields"]["ticket"]["value"].update(min=3_000_000, max=50_000_000)
        bad[0]["investments"][0]["date"] = "2027-01-01"
        bad[0]["investments"][1].update(date="2020-01-01", fund="Example Fund I")
        bad[2]["id"] = "example-ventures"
        errors = "\n".join(validate(bad, validator, today=TODAY).errors)
>       assert "min 3000000 > max 50000000" in errors
E       assert 'min 3000000 > max 50000000' in "example-ventures: ticket max 50000000 EUR > largest fund size 30000000 EUR\nexample-ventures: investments[0] (Alpha R...ta Health) date 2020-01-01 is before vintage 2021 of 'Example Fund I'\nexample-ventures: duplicate id (also record #0)"

tests/test_schema.py:54: AssertionError
______________________ test_wilson_bounds_and_edge_cases _______________________

    def test_wilson_bounds_and_edge_cases():
        assert wilson(0, 0) is None
        with pytest.raises(ValueError):
            wilson(3, 2)
        for n in (1, 7, 60):
            for k in range(n + 1):
                lo, hi = wilson(k, n)
>               assert 0.0 <= lo <= k / n <= hi <= 1.0
E               assert 5.551115123125783e-17 <= (0 / 
… [314 more characters]
```
</details>

→ `Bash` — Fix Wilson edge bounds and schema test
```sh
.venv/bin/python - <<'EOF'
p='src/investordb/stats.py'
s=open(p).read()
s=s.replace('''    return max(0.0, centre - half), min(1.0, centre + half)''','''    # at k == 0 or k == n the bound is exactly 0 or 1; don't let float noise say otherwise
    lo = 0.0 if k == 0 else max(0.0, centre - half)
    hi = 1.0 if k == n else min(1.0, centre + half)
    return lo, hi''')
open(p,'w').write(s)
p='tests/test_schema.py'
s=open(p).read()
s=s.replace('''update(min=3_000_000, max=50_000_000)''','''update(min=40_000_000, max=35_000_000)''')
s=s.replace('''    assert "min 3000000 > max 50000000" in errors
    assert "> largest fund size 30000000" in errors''','''    assert "min 40000000 > max 35000000" in errors
    assert "max 35000000 EUR > largest fund size 30000000" in errors''')
open(p,'w').write(s)
EOF
.venv/bin/pytest -q tests 2>&1 | tail -3
```

<details><summary>result</summary>

```
........................................................................ [100%]
72 passed in 0.13s
```
</details>

**Agent:**

Now grade, verify, fetch (offline, fake session) and review/eval tests.

→ `Bash` — Write verify, grade and fetch tests and run
```sh
cd /Users/[redacted]/homeW/ai-dev-test/investor-db/tests && cat > test_verify.py <<'EOF'
from investordb.fetch import load_index
from investordb.records import iter_targets
from investordb.verify import check_records, value_facts, value_status


def test_verify_against_fixture_cache(records, fixtures_dir):
    cache = fixtures_dir / "cache"
    rows = check_records(records, load_index(cache), cache)
    by = {(r["record_id"], r["target"]): r for r in rows}
    assert len(rows) == 7
    assert by[("example-ventures", "fields.ticket")]["quote_status"] == "exact"
    assert by[("example-ventures", "fields.ticket")]["value_status"] == "ok"
    assert by[("example-ventures", "fields.funds")]["fetch_used"] == "wayback"
    assert by[("example-ventures", "investments[0]")]["value_detail"] == (
        "date=2025-03-12:ok; round=1500000:ok")
    assert by[("demo-capital", "investments[0]")]["quote_status"] == "unreachable"


def test_value_not_in_quote(example):
    t = next(t for t in iter_targets(example) if t.kind == "ticket")
    src = t.sources[0]
    facts = value_facts(t, src, "our tickets are small")
    assert value_status(facts) == "value_not_in_quote"
    facts = value_facts(t, src, 
… [8499 more characters]
```

<details><summary>result</summary>

```
........................................................................ [ 79%]
...................                                                      [100%]
91 passed in 0.25s
```
</details>

→ `Bash` — Write review and eval tests and run all
```sh
cd /Users/[redacted]/homeW/ai-dev-test/investor-db/tests && cat > test_review_eval.py <<'EOF'
import csv
import json
import re

from investordb.evaluate import human_metrics, read_labels, recall, run_eval
from investordb.review import allocate, build_claims, render_html, sample_claims


def test_claims_skip_excluded_records(records):
    claims = build_claims(records)
    assert not any(c["record_id"] == "sample-crowd" for c in claims)
    kinds = {c["claim_id"]: c["kind"] for c in claims}
    assert kinds["example-ventures/existence"] == "existence"
    assert kinds["example-ventures/field/ticket"] == "field"
    assert kinds["demo-capital/investment/0"] == "investment"
    # dormant records get no existence claim (inclusion precision is about included ones)
    assert "demo-capital/existence" not in kinds


def test_allocate_proportional_with_floor():
    sizes = {"existence": 50, "field:ticket": 10, "field:aum": 2, "investment": 200}
    alloc = allocate(sizes, 60)
    assert sum(alloc.values()) == 60
    assert alloc["field:aum"] == 2  # whole stratum, it's below the floor
    assert alloc["field:ticket"] >= 3
    assert alloc["investment"] > alloc["existence"] > alloc["field:ticket
… [3024 more characters]
```

<details><summary>result</summary>

```
........................................................................ [ 72%]
...........................                                              [100%]
99 passed in 0.16s
```
</details>

→ `Bash` — Add CLI smoke test, run pytest and ruff
```sh
cat >> tests/test_schema.py <<'EOF'


def test_cli_validate(fixtures_dir, tmp_path, capsys):
    from investordb.cli import main

    assert main(["validate", "--records", str(fixtures_dir / "investors.json"),
                 "--today", "2026-10-11"]) == 0
    assert "3 records, 0 errors" in capsys.readouterr().out
    assert main(["validate", "--records", str(tmp_path / "nope.json")]) == 2
EOF
.venv/bin/pytest -q tests 2>&1 | tail -2 && .venv/bin/ruff check . ; git status --short
```

<details><summary>result</summary>

```
............................                                             [100%]
100 passed in 0.15s
E501 Line too long (101 > 100)
  --> tests/test_textnorm.py:84:101
   |
82 | def test_fuzzy_with_changed_numbers_is_missing():
83 |     page = "Our first tickets range from €200 000 to €2 million for seed rounds."
84 |     status, sim = match_quote("Our first tickets range from €250 000 to €3 million for seed rounds.",
   |                                                                                                     ^
85 |                               page)
86 |     assert status == "missing" and sim >= 0.85
   |

Found 1 error.
 M src/investordb/stats.py
 M src/investordb/textnorm.py
?? data/reference/
?? tests/
```
</details>

→ `Bash` — Fix lint, commit source tweaks and tests
```sh
.venv/bin/python - <<'EOF'
p='tests/test_textnorm.py'
s=open(p).read()
s=s.replace('''    status, sim = match_quote("Our first tickets range from €250 000 to €3 million for seed rounds.",
                              page)''','''    quote = "Our first tickets range from €250 000 to €3 million for seed rounds."
    status, sim = match_quote(quote, page)''')
open(p,'w').write(s)
EOF
.venv/bin/ruff check . && .venv/bin/pytest -q tests 2>&1 | tail -1 && git add src/investordb/stats.py src/investordb/textnorm.py && git status --short && git commit -q -m "Add Slovak and Czech locative month names, exact Wilson bounds at 0 and n" && git add tests/conftest.py tests/test_textnorm.py tests/test_stats.py tests/test_rules.py tests/test_schema.py tests/test_verify.py tests/test_grade.py tests/test_fetch.py tests/test_review_eval.py tests/fixtures/investors.json tests/fixtures/cache tests/fixtures/reference/example-association.csv && git status --short && git commit -q -m "Add tests with offline fixtures for all commands" && git log --oneline | head -3
```

<details><summary>result</summary>

```
All checks passed!
100 passed in 0.14s
M  src/investordb/stats.py
M  src/investordb/textnorm.py
?? data/reference/
?? tests/
A  tests/conftest.py
A  tests/fixtures/cache/files/30cb4692eb7d68fde690b47a282b63aa707667c4.txt
A  tests/fixtures/cache/files/92658756ff41351598434cb67f74146e5274ec7b.txt
A  tests/fixtures/cache/files/96c12942ac53a1240b100c5b1f128ce3c43ca175.txt
A  tests/fixtures/cache/files/e32df979f3154c23febe32682381d43e8ef87d07.txt
A  tests/fixtures/cache/index.json
A  tests/fixtures/investors.json
A  tests/fixtures/reference/example-association.csv
A  tests/test_fetch.py
A  tests/test_grade.py
A  tests/test_review_eval.py
A  tests/test_rules.py
A  tests/test_schema.py
A  tests/test_stats.py
A  tests/test_textnorm.py
A  tests/test_verify.py
?? data/reference/
9279305 Add tests with offline fixtures for all commands
fcf4875 Add Slovak and Czech locative month names, exact Wilson bounds at 0 and n
202c58b Add eval command: accuracy, recall and automated check metrics with Wilson intervals
```
</details>

→ `Bash` — Check for real sample data
```sh
ls -la data/sample/ research/ && git status --short
```

<details><summary>result</summary>

```
data/sample/:
total 0
drwxr-xr-x  3 [user]  staff   96 11 окт.  01:38 .
drwxr-xr-x  5 [user]  staff  160 11 окт.  01:38 ..
drwxr-xr-x  2 [user]  staff   64 11 окт.  01:38 parts

research/:
total 280
drwxr-xr-x   5 [user]  staff    160 11 окт.  01:34 .
drwxr-xr-x  15 [user]  staff    480 11 окт.  01:45 ..
-rw-r--r--   1 [user]  staff  80698 11 окт.  01:34 sk-vc-candidates.json
-rw-r--r--   1 [user]  staff  12673 11 окт.  01:34 sk-vc-candidates.md
-rw-r--r--   1 [user]  staff  43511 11 окт.  01:21 sources-and-universe.md
?? data/reference/
```
</details>

→ `Bash` — Scan tracked files and commits for forbidden words
```sh
git ls-files | grep -v -E '^(PLAN.md|research/)' | xargs grep -n -i -E '\bai\b|llm|claude|gpt|codex|generat|agent|anthropic|openai' ; echo "grep exit=$?"; git log --format='%an <%ae>%n%B' 631ac55^..HEAD | grep -i -E 'co-authored|agent|claude|generat|\bai\b' ; echo "log grep exit=$?"; .venv/bin/python -m investordb --help
```

<details><summary>result</summary>

```
src/investordb/fetch.py:19:    "User-Agent": BROWSER_UA,
src/investordb/fetch.py:107:        return {**HEADERS, "User-Agent": ARCHIVE_UA}
src/investordb/textnorm.py:124:        if re.fullmatch(pat, word):
tests/test_fetch.py:87:    assert "Mozilla" in session.calls[0][2]["User-Agent"]
tests/test_fetch.py:88:    assert "Mozilla" not in session.calls[1][2]["User-Agent"]
grep exit=0
log grep exit=1
usage: investordb [-h]
                  {validate,fetch,verify,decide,grade,review-pack,eval} ...

Investor database tooling

positional arguments:
  {validate,fetch,verify,decide,grade,review-pack,eval}
    validate            schema + consistency checks
    fetch               download every source URL into the cache
    verify              check quotes and values against fetched pages
    decide              recompute decisions and compare with stored ones
    grade               confidence A/B/C per record
    review-pack         build the static review page
    eval                accuracy metrics from review labels

options:
  -h, --help            show this help message and exit
```
</details>

→ `Bash` — Run full pipeline on fixtures via CLI
```sh
S=[tmp] && mkdir -p $S && F=tests/fixtures && P=".venv/bin/python -m investordb" && $P validate --records $F/investors.json && $P verify --records $F/investors.json --cache $F/cache --out $S/verification.csv | tail -2 && $P decide --records $F/investors.json --out $S/dc.csv --ref-date 2026-10-11 | head -1 && $P grade --records $F/investors.json --verification $S/verification.csv --out-json $S/g.json --out-csv $S/g.csv | head -1 && $P review-pack --records $F/investors.json --html $S/review.html --claims $S/claims.csv | head -1 && $P eval --records $F/investors.json --claims $S/claims.csv --labels $S/labels.csv --reference $F/reference --verification $S/verification.csv --decision-check $S/dc.csv --graded $S/g.json --out-md $S/A.md --out-json $S/m.json && git status --short
```

<details><summary>result</summary>

```
Exit code 127
(eval):1: no such file or directory: .venv/bin/python -m investordb
```
</details>

→ `Bash` — Run full pipeline on fixtures via CLI
```sh
S=[tmp] && F=tests/fixtures && P() { .venv/bin/python -m investordb "$@"; } && P validate --records $F/investors.json && P verify --records $F/investors.json --cache $F/cache --out $S/verification.csv | tail -2 && P decide --records $F/investors.json --out $S/dc.csv --ref-date 2026-10-11 | head -1 && P grade --records $F/investors.json --verification $S/verification.csv --out-json $S/g.json --out-csv $S/g.csv | head -1 && P review-pack --records $F/investors.json --html $S/review.html --claims $S/claims.csv | head -1 && P eval --records $F/investors.json --claims $S/claims.csv --labels $S/labels.csv --reference $F/reference --verification $S/verification.csv --decision-check $S/dc.csv --graded $S/g.json --out-md $S/A.md --out-json $S/m.json && git status --short
```

<details><summary>result</summary>

```
3 records, 0 errors, 0 warnings
  demo-capital investments[0] #0: unreachable/ok https://example.com/news/gamma
wrote [tmp]
reference date 2026-10-11, window 36 months; agree 3
3 records graded: A 1, B 0, C 2
8 claims in total, sampled 8 (seed 7): existence 1, field:sectors 1, field:geography 1, field:ticket 1, field:funds 1, investment 3
note: [tmp] not found - computing automated metrics only
recall example-association: 2/3 66.7 % (20.8-93.8)
quote pass rate 85.7 % (48.7-97.4)
wrote [tmp] and [tmp]
?? data/reference/
```
</details>

→ `Bash` — Final test and lint run, list commits, clean scratch
```sh
.venv/bin/pytest 2>&1 | tail -1 && .venv/bin/ruff check . && git log --format='%h %an | %s' 9112125..HEAD && rm -rf [tmp] && pgrep -fl "Google Chrome --headless" | wc -l && git status --short
```

<details><summary>result</summary>

```
============================= 100 passed in 0.13s ==============================
All checks passed!
9279305 [redacted: name] | Add tests with offline fixtures for all commands
fcf4875 [redacted: name] | Add Slovak and Czech locative month names, exact Wilson bounds at 0 and n
202c58b [redacted: name] | Add eval command: accuracy, recall and automated check metrics with Wilson intervals
f291367 [redacted: name] | Add review-pack command: stratified claim sample and static review page
d559fef [redacted: name] | Add grade command: confidence per record and flat CSV export
162da7c [redacted: name] | Add decide command: rule engine for I3 recency and E-rule exclusions
f37cdd8 [redacted: name] | Add verify command: quote and value checks against cached pages
be4e03f [redacted: name] | Add text normalisation and quote matching
42f6e55 [redacted: name] | Record URL and content type of the stored body in the fetch index
5dc4f6b [redacted: name] | Add Slovak VC candidate research with registry evidence
d39b4f1 [redacted: name] | Add fetch command: polite downloader with text extraction and Wayback fallback
169c011 [redacted: name] | Add validate command: schema and consistency checks
631ac55 [redacted: name] | Add package skeleton and investor record schema
       0
?? data/reference/
```
</details>

**Agent:**

[redacted: name]

All seven commands are built and committed in `/Users/[redacted]/homeW/ai-dev-test/investor-db`. `pytest` and `ruff check` both pass. Everything has only been run on the fixture records, because `data/sample/investors.json` doesn't exist yet.

**pytest:** `============================= 100 passed in 0.13s ==============================`
**ruff check .:** `All checks passed!`

**Commands**
```
python3 -m venv .venv && .venv/bin/pip install -e '.[dev]'
python -m investordb validate   [--records data/sample/investors.json] [--today YYYY-MM-DD]
python -m investordb fetch      [--cache data/cache] [--force] [--no-wayback] [--limit N]
python -m investordb verify     [--out data/sample/verification.csv]
python -m investordb decide     [--ref-date YYYY-MM-DD] [--months 36] [--negative-list data/negative_list.csv]
python -m investordb grade      [--ignore-verify]   # -> investors.graded.json + investors.csv
python -m investordb review-pack --n 60 --seed 7    # -> eval/review.html + eval/claims.csv
python -m investordb eval --labels eval/labels.csv  # -> eval/ACCURACY.md + eval/metrics.json
.venv/bin/pytest && .venv/bin/ruff check .
```

**Commits:** 12 small commits, from `631ac55` (skeleton and schema) to `9279305` (tests). Author is [redacted: name], with no trailers. I committed using explicit paths only and checked `git status` each time. One commit in between, `5dc4f6b`, is someone else's (research). `research/`, `PLAN.md`, `data/reference/cvca-full-members.csv` and `data/sample/` were not touched or committed.

**The 14-character Wayback case:** the snapshot was fine. The code already fetched the raw `id_/` form, and that PDF's entire text really is "Dummy PDF file". What made it look wrong was the index: `content_type` showed the failed live response (a 403 HTML page). The index now also stores `body_url` and `body_content_type` for the bytes actually saved (commit `42f6e55`).

**Decisions you might not expect**
- **Fuzzy matches with different numbers fail.** A quote that is at least 85 % similar to the page but whose numbers differ is marked `missing`, not `fuzzy`. A plausible sentence with a wrong number is the main failure this check exists to catch.
- **Grading is stricter than the spec.** A source also stops counting if its quote doesn't contain the claimed number or date (`value_not_in_quote`), not only if the quote is missing or unreachable.
- **Wayback has a second route.** When the availability API returns nothing, `fetch` also asks the CDX API, which records snapshots the availability API often misses.
- **archive.org gets its own User-Agent.** It answered 429 to a browser UA sent from Python, so it gets a plain tool UA; every other site gets the browser UA. The HTTP header name `User-Agent` is the only match for the word "agent" in the repo.
- **Three optional fields added to the schema:** `aliases` (needed for recall), `ticket_observed` (from PLAN §2) and `investment.fund` (needed for the vintage check).
- **Dormant vs uncertain:** old evidence of any tier makes a record `dormant` (E4). A recent investment shown only by Tier C sources makes it `uncertain`.
- **Disagreements on human-only rules are labelled `human_only`.** Stored exclusions resting on rules the engine can't compute (E3, E5–E10, or E2 when the type isn't `adviser`) show as `human_only` instead of `DISAGREE`.
- **Strict and lenient accuracy:** strict counts "Can't verify" as wrong, as PLAN 3.5 requires; lenient leaves those claims out. Both are reported.

**Known limitations**
- **Not run on real data.** Real sources weren't fetched in bulk; `fetch` was only tried on a handful of live URLs (HTML, PDF, Wayback via the availability API). The CDX fallback is covered only by tests with a fake session.
- **The availability API is unreliable.** It returned nothing for pages that are archived, which is why the CDX fallback exists.
- **Some sites block the fetcher.** Pages behind Cloudflare or JavaScript (e.g. w3.org returned 403) will show up as `unreachable` unless a snapshot exists. There is no headless-browser fetching.
- **Review page visuals unchecked.** Headless Chrome hung and I killed it; Playwright was off-limits. The page's script logic (render, labelling, filter, CSV export with escaping) was run under Node with a small DOM stub, and the JS syntax is checked.
- **Value checks are basic.** Only numbers and dates are compared. Sectors, stages and geography get `n/a`. Number parsing treats a 3-digit group as thousands, so an English "1,500" is read as 1500. Scale words such as "m" or "b" can rarely misfire.
- **Existence at Tier A needs a sourced value.** It requires a verified Tier A source on some field or investment. A `legal_entities` entry alone doesn't count, because it has no quote to check.
- **Recall matching is exact.** It compares normalised names (legal forms such as s.r.o./a.s. stripped) with no fuzzy matching. Rebrands need `aliases`.
- **Overall accuracy leans towards small strata.** Allocation is proportional with at least 3 per stratum, and overall accuracy is the plain sample share with no reweighting.
- **Running `grade` writes into `data/sample/`.** It creates `data/sample/investors.graded.json` and `investors.csv`, which the person writing `data/sample/investors*.json` may also touch. I only ran it with outputs in a scratch folder.

I removed my scratch files; no processes are left running.

