# Agent: Slovak records with verbatim quotes

Claude Code sub-agent log, exported from `agent-ae9344859411d2483.jsonl`.
Tool outputs longer than 1,500 characters are shortened.

## Brief

You are a data analyst on an investor-database project in /Users/[redacted]/homeW/ai-dev-test/investor-db. Read PLAN.md (rules I1–I4, E1–E10, evidence tiers A/B/C), schema/investor.schema.json and tests/fixtures/investors.json (format example) first.

Task: turn the Slovak VC research in research/sk-vc-candidates.json (49 candidates, written by a colleague) into records that follow the schema EXACTLY, and write them to data/sample/parts/sk.json (JSON array, pretty-printed, UTF-8). Also write data/sample/parts/sk-decisions.md: one line per candidate "name — status — rule IDs — one-sentence reason".

Hard requirements:
1. **Every `quote` must be VERBATIM text that appears on the page at `url`.** The colleague's quotes are sometimes paraphrased by the fetch tool — do not trust them. WebFetch returns a model-written summary, NOT the page text, so never copy quotes from WebFetch output. Instead fetch raw pages with `curl -sL -A "Mozilla/5.0 ..." <url>` (or python urllib), extract visible text (python: strip script/style, html.unescape), and copy the sentence from that text. For PDFs use `pdftotext` if available or python pypdf from /Users/[redacted]/homeW/ai-dev-test/investor-db/.venv/bin/python. After writing each quote, confirm it with a grep on the extracted text. If a page can't be fetched raw (403, JS-only), find another source or set that field to null — never keep an unverifiable quote. Keep the quote short (one sentence or table row) but containing the value (number/date/sector words).
2. For the Slovak business register use the helper `[tmp]` (`python3 orsr.py search "<name>"`, `python3 orsr.py vypis "<url>"`). ORSR shareholder entries ("Spoločníci" … "(od: dd.mm.yyyy)") are Tier A evidence of an investment and its date; the ORSR extract URL + the exact line is the quote. finstat.sk returns 403 — don't use it.
3. Resolve the 7 "uncertain" candidates (0100 VC Fund II, ZAKA VC, G-Force, CB Investment Management, Baryon Fund, LRJ Capital, IPM Group) into included / excluded / dormant with rule IDs, with extra searching where needed. "uncertain" is allowed only if you truly can't decide — explain why.
4. Re-check the 3 includes (Neulogy Ventures, Vision Ventures, Venture to Future Fund): try hard to find a dated investment within 36 months before 2026-10-11 (I3) — ORSR shareholder entries of portfolio companies are the best route. Neulogy: check if any portfolio company added Neulogy's fund vehicle as shareholder since Oct 2023.
5. For excluded records you don't need full fields: id, name, type, hq, website, decision (status + rules + note), and at least one source proving the reason in the most relevant field or investment (e.g., a platform: a quote saying it is a crowdfunding platform). Put that proof in `fields.sectors` only if it fits; otherwise add it as decision evidence in `decision.note` with the URL. Keep it schema-valid.
6. `type` uses the schema enum. Money as numbers + currency. Dates ISO. `accessed` = 2026-10-11. Use null for unknown, never guess.
7. Validate: `cd /Users/[redacted]/homeW/ai-dev-test/investor-db && .venv/bin/python -m investordb validate --file data/sample/parts/sk.json` if that option exists; otherwise validate with python jsonschema against schema/investor.schema.json yourself (each record against the `record` definition). Fix every error.

Rules: all file content in English (Slovak/Czech quotes stay verbatim). Don't mention AI/tools in files. Don't run git. Don't touch files other than data/sample/parts/sk.json and sk-decisions.md. Don't use the Playwright MCP browser. No signups, no forms.

Final message (English): counts by status, list of included with their latest dated investment, how many quotes you verified by grep vs. dropped, and the weakest 5 records.

**Agent:**

Начинаю с чтения PLAN.md, схемы и примера.

→ `Bash` — Read plan and list project files
```sh
ls -la && cat PLAN.md && ls data data/sample data/sample/parts research tests/fixtures 2>&1
```

<details><summary>result</summary>

```
Exit code 1
total 48
drwxr-xr-x  14 [user]  staff    448 11 окт.  01:29 .
drwxr-xr-x   4 [user]  staff    128 11 окт.  01:07 ..
drwxr-xr-x  12 [user]  staff    384 11 окт.  01:36 .git
-rw-r--r--   1 [user]  staff     72 11 окт.  01:27 .gitignore
drwxr-xr-x   5 [user]  staff    160 11 окт.  01:29 .ruff_cache
drwxr-xr-x   7 [user]  staff    224 11 окт.  01:27 .venv
drwxr-xr-x   4 [user]  staff    128 11 окт.  01:29 data
drwxr-xr-x   2 [user]  staff     64 11 окт.  01:27 eval
-rw-r--r--   1 [user]  staff  12330 11 окт.  01:23 PLAN.md
-rw-r--r--   1 [user]  staff    788 11 окт.  01:27 pyproject.toml
drwxr-xr-x   5 [user]  staff    160 11 окт.  01:34 research
drwxr-xr-x   3 [user]  staff     96 11 окт.  01:28 schema
drwxr-xr-x   4 [user]  staff    128 11 окт.  01:29 src
drwxr-xr-x   3 [user]  staff     96 11 окт.  01:27 tests
# Plan: a reliable database of investors

The point of this database is trust. A record is only worth something if a reader can click
through to a public page and see for themselves that the entity invests, in what, how much,
and since when. So the plan is built around evidence first and coverage second.

Research behind the numbers below: [`research/sources-and-universe.md`](research/sources-and-universe.md).

---

## 1. What counts as an investor

**Unit of a record = the investing organisation (manager), or a person investing in their own name.**
Not the fund vehicle, not the SPV, not the brand. A manager with five funds is one record with
five funds attached. This matt
… [8539 more characters]
```
</details>

→ `Bash` — Read the truncated middle of PLAN
```sh
sed -n 60,140p PLAN.md
```

<details><summary>result</summary>

```
## 2. Data model

```
Investor (manager or person)  1 ─── n  Fund  1 ─── n  Vehicle
   │
   ├── n  Investment (portfolio company, date, round, evidence)
   └── every field = { value, source_url, source_type, tier, published, accessed, quote }
```

- **Every value carries its own provenance.** Not "sources: [5 links]" at the bottom of a row, but
  the exact URL and an exact quote for that one field. A reviewer can check any single number
  in under a minute.
- `quote` is a verbatim sentence from the source. It is what makes automated checking possible (3.2).
- Money is stored as amount + currency + `as_of`. Fund size and AUM are different fields:
  `fund_size` (one fund's commitments) vs `aum` (manager total as stated). They are not added up
  silently, because their definitions differ.
- `ticket_min/ticket_max` = what the investor says on its own site, or what the fund-of-funds
  terms say; derived ticket estimates from round sizes are stored separately as `ticket_observed`.
- `confidence` is computed per record from the evidence tiers (3.3), not set by hand.

Schema: [`schema/investor.schema.json`](schema/investor.schema.json).

---

## 3. How authenticity and classification are verified

### 3.1 Evidence tiers

| Tier | Sources | Proves |
|---|---|---|
| **A — legal filings** | Regulators (SEC ADV/Form D, ESMA, ČNB, NBS), business registers with shareholder entries (ORSR, justice.cz, Companies House), fund-of-funds commitments from EIF/SIH/NRB | That the entity exists as a 
… [3604 more characters]
```
</details>

→ `Bash` — Read schema, fixture and source tree
```sh
cat schema/investor.schema.json && cat tests/fixtures/investors.json && ls -R src data/reference && cat pyproject.toml
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
… [15916 more characters]
```
</details>

→ `Bash` — Read E6-E10 rules, CLI and fetch helpers
```sh
sed -n 40,60p PLAN.md && cat src/investordb/cli.py src/investordb/fetch.py | head -200 && cat data/negative_list.csv | head -50
```

<details><summary>result</summary>

```
### Exclusion rules (any one excludes)

| ID | Excluded | Why / how detected |
|---|---|---|
| **E1** | Crowdfunding / investment platforms (Crowdberry's platform, Crowdcube, Seedrs, Republic) | They route other people's money. Negative list = ESMA ECSP register (261 providers). If the platform also runs a fund, the **fund manager** can be included separately. |
| **E2** | Advisers: M&A boutiques, law firms, auditors, banks' corporate finance | Associate members of CVCA (57 of 84) and SLOVCA (31) are exactly this. NACE 69.10/69.20/70.22/64.19 filter + manual check. |
| **E3** | Lenders only (banks, leasing, venture debt funds without equity) | Debt is not equity investing. Venture debt that takes warrants → `vc` with a flag. |
| **E4** | Dormant: no dated investment in 36 months | Kept in a `dormant` list with `last_evidence_date`, so it can be re-activated. |
| **E5** | Announced but never launched funds | Needs a first close or first investment, not a press release about plans (example: the Czech Národní inovační fond was cancelled before investing). |
| **E6** | Grant agencies, subsidy programs, competitions | No equity. |
| **E7** | Pure listed-equity managers, hedge funds, retail asset managers | No private-company investing. ESMA AIFM register mixes them in (e.g. Tatra Asset Management, IAD Investments in SK). |
| **E8** | Single-business holding groups | Buying operating companies for their own group (strategic M&A) is not third-party investing. Included as `private_in
… [8156 more characters]
```
</details>

→ `Bash` — Inspect candidates research file
```sh
wc -c research/* && head -c 6000 research/sk-vc-candidates.json && echo && python3 -c "
import json;d=json.load(open('research/sk-vc-candidates.json'));print(type(d), len(d) if isinstance(d,list) else d.keys())"
```

<details><summary>result</summary>

```
   80698 research/sk-vc-candidates.json
   12673 research/sk-vc-candidates.md
   43511 research/sources-and-universe.md
  136882 total
[
  {
    "name": "Neulogy Ventures",
    "management_company": "Neulogy Ventures, a. s.",
    "fund_vehicles": [
      "Slovak Venture Fund S.C.A., SICAR (Luxembourg; EIF lists Neulogy Ventures a.s. as manager)"
    ],
    "ico": "47 367 610",
    "register_link": "https://www.orsr.sk/vypis.asp?ID=276162&SID=2&P=0",
    "website": "https://www.neulogy.vc/",
    "hq_city": "Bratislava",
    "proposed_type": "VC",
    "sectors": "ICT, energy/cleantech, medical diagnostics/medtech, B2B SaaS, cybersecurity (deeptech)",
    "stages": "seed, venture (early stage)",
    "geography": "Slovakia / CEE",
    "ticket_min_eur": 200000,
    "ticket_max_eur": 2500000,
    "fund_sizes": [
      {
        "value": "AUM EUR 26 million",
        "vintage": null,
        "source": "SLOVCA profile"
      },
      {
        "value": "SIH (NDF I) capital investment EUR 19.0 million",
        "vintage": "investment period 2014-2016",
        "source": "SIH page / search snippet"
      }
    ],
    "recent_investments": [
      {
        "company": "GA Drilling",
        "date": "2024-04-18",
        "round_size": "USD 15 million first close (Neulogy one of several investors)",
        "source": {
          "url": "https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/",
          "accessed": "2026-10-11",
          "publ
… [4651 more characters]
```
</details>

→ `Bash` — Read candidates markdown summary
```sh
cat research/sk-vc-candidates.md
```

<details><summary>result</summary>

```
# Slovak VC investors — pilot sample candidates

Accessed 2026-10-11. Full evidence (per-field sources, quotes, registry links) is in `sk-vc-candidates.json`.
49 candidates: **3 include / 7 uncertain / 39 exclude**.

**Where the candidates came from:** SLOVCA full and associate member lists, the EIF list "Slovakia equity fund managers" (as at 30.09.2026), SIH intermediary pages, Startitup/Forbes/CzechCrunch/e15/Vestbee funding news, and directory lists (papermark, incubatorlist, vestbee 2020, podnikajte 2016, ain.ua 2022). Evidence of investments comes from ORSR shareholder entries ("od: dd.mm.yyyy").

**Inclusion rule applied:** the management company or fund vehicle is managed from Slovakia, or the investor is Slovak-founded with a Slovak investment team; it invests equity directly; and it has at least one dated investment.
**Excluded:** PE/buyout funds, corporate VCs (CVC), banks, public fund-of-funds and co-investment vehicles, accelerators, crowdfunding platforms, angel networks, Czech/Polish funds, and funds that are closed or dormant.

**Notes:**
- Of the task's seed names, three could not be verified anywhere ("Prvá kapitálová", "Gapfunding", "Monopoly Ventures"); "Nation1" turned out to be the Czech fund Nation 1. No Slovak "Bitcoin-era" fund was found. The Swiss Re link points to a shared service centre, not a VC.
- Most Slovak VCs were set up in 2019 under the SIH/NDF II programme, and their investment windows ended in 2023 (Vision Ventures, Zero Gravity, CB IM). M
… [11076 more characters]
```
</details>

→ `Bash` — Read ORSR helper and scratchpad contents
```sh
cat [tmp] ls [tmp] [tmp] which pdftotext
```

<details><summary>result</summary>

```
#!/usr/bin/env python3
# usage: orsr.py search "name"   -> list of matches with vypis links
#        orsr.py vypis "<relative or abs url>" [full]  -> text of extract
import sys, re, urllib.request, urllib.parse, html, socket; socket.setdefaulttimeout(30)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"
BASE = "https://www.orsr.sk/"
def get(url):
    import time
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            raw = urllib.request.urlopen(req, timeout=60).read()
            return raw.decode("windows-1250", errors="replace")
        except Exception as e:
            err = e; time.sleep(3)
    print("FETCH FAILED", url, err); return ""
def text(h):
    h = re.sub(r"(?is)<script.*?</script>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</tr>|</p>|</div>", "\n", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h)
    lines = [re.sub(r"[ \t\xa0]+", " ", l).strip() for l in h.split("\n")]
    return "\n".join(l for l in lines if l)
cmd = sys.argv[1]
if cmd == "search":
    q = urllib.parse.quote(sys.argv[2].encode("windows-1250"))
    h = get(BASE + f"hladaj_subjekt.asp?OBMENO={q}&PF=0&R=on")
    rows = re.findall(r'(?is)<a href="(vypis\.asp\?ID=\d+&amp;SID=\d+&amp;P=0)" class = "link"[^>]*>(.*?)</a>', h); rows=[(n,l.replace("&amp;","&")) for l,n in rows]
    for name, link in rows:
        print(html.unescape(re.sub("<[^>]+>","",na
… [2745 more characters]
```
</details>

→ `Bash` — Read fetch text extraction and validator
```sh
sed -n 60,400p src/investordb/fetch.py; cat src/investordb/validate.py src/investordb/records.py
```

<details><summary>result</summary>

```
def cache_key(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()


def html_to_text(html: str | bytes) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(DROP_TAGS):
        tag.decompose()
    # keep block structure so sentences from different elements don't glue together
    text = soup.get_text(separator="\n")
    lines = (ln.strip() for ln in text.splitlines())
    return "\n".join(ln for ln in lines if ln)


def pdf_to_text(data: bytes) -> str:
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(data))
    return "\n".join((page.extract_text() or "") for page in reader.pages)


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
    host = ur
… [16014 more characters]
```
</details>

→ `Bash` — Dump compact view of first 10 candidates
```sh
mkdir -p [tmp] [tmp] && cd /Users/[redacted]/homeW/ai-dev-test/investor-db && python3 -c "
import json
d=json.load(open('research/sk-vc-candidates.json'))
print(sorted(set(k for c in d for k in c)))
for i,c in enumerate(d[:10]):
    print('=====',i,c['name'],'|',c.get('management_company'),'| ICO',c.get('ico'),'|',c.get('register_link'),'|',c.get('website'),'|',c.get('hq_city'),'|',c.get('proposed_type'),'|',c.get('decision'))
    for k in ['fund_vehicles','sectors','stages','geography','ticket_min_eur','ticket_max_eur','fund_sizes']:
        print(' ',k,':',json.dumps(c.get(k),ensure_ascii=False))
    for r in c.get('recent_investments') or []:
        print('  INV',r['company'],r['date'],r.get('round_size'),r['source']['url'],r.get('evidence_type'))
    for k,v in (c.get('sources') or {}).items():
        print('  SRC',k,[s['url'] for s in v])
    for q in c.get('evidence_quotes') or []: print('  Q',q)
    print('  REASON',c.get('reason'))
"
```

<details><summary>result</summary>

```
['decision', 'evidence_quotes', 'found_via', 'fund_sizes', 'fund_vehicles', 'geography', 'hq_city', 'ico', 'management_company', 'name', 'proposed_type', 'reason', 'recent_investments', 'register_link', 'sectors', 'sources', 'stages', 'ticket_max_eur', 'ticket_min_eur', 'website']
===== 0 Neulogy Ventures | Neulogy Ventures, a. s. | ICO 47 367 610 | https://www.orsr.sk/vypis.asp?ID=276162&SID=2&P=0 | https://www.neulogy.vc/ | Bratislava | VC | include
  fund_vehicles : ["Slovak Venture Fund S.C.A., SICAR (Luxembourg; EIF lists Neulogy Ventures a.s. as manager)"]
  sectors : "ICT, energy/cleantech, medical diagnostics/medtech, B2B SaaS, cybersecurity (deeptech)"
  stages : "seed, venture (early stage)"
  geography : "Slovakia / CEE"
  ticket_min_eur : 200000
  ticket_max_eur : 2500000
  fund_sizes : [{"value": "AUM EUR 26 million", "vintage": null, "source": "SLOVCA profile"}, {"value": "SIH (NDF I) capital investment EUR 19.0 million", "vintage": "investment period 2014-2016", "source": "SIH page / search snippet"}]
  INV GA Drilling 2024-04-18 USD 15 million first close (Neulogy one of several investors) https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/ press article
  INV StratifAI GmbH 2024-09-02 EUR 1.5 million pre-seed (co-led by Neulogy Ventures and MultiplexDX) https://www.trysignalbase.com/news/funding/stratifai-secures-1.5-million-in-pre-seed-funding-to-revolutionize-precision-oncology-with-ai-driven-biomarkers aggre
… [17991 more characters]
```
</details>

→ `Bash` — Dump compact view of candidates 10-29
```sh
python3 -c "
import json
d=json.load(open('research/sk-vc-candidates.json'))
for i,c in enumerate(d[10:30],10):
    print('=====',i,c['name'],'|',c.get('management_company'),'| ICO',c.get('ico'),'|',c.get('register_link'),'|',c.get('website'),'|',c.get('hq_city'),'|',c.get('proposed_type'),'|',c.get('decision'))
    for k in ['fund_vehicles','sectors','stages','ticket_min_eur','ticket_max_eur','fund_sizes']:
        v=c.get(k)
        if v: print(' ',k,':',json.dumps(v,ensure_ascii=False))
    for r in c.get('recent_investments') or []:
        print('  INV',r['company'],r['date'],r.get('round_size'),r['source']['url'],r.get('evidence_type'))
    for k,v in (c.get('sources') or {}).items():
        print('  SRC',k,[s['url'] for s in v])
    for q in c.get('evidence_quotes') or []: print('  Q',q)
"
```

<details><summary>result</summary>

```
===== 10 IPM Group / IPM Growth | IPM Group (Anglo-Slovak asset manager; Slovak entity not identified) | ICO 52 151 573 | https://www.orsr.sk/vypis.asp?ID=450600&SID=3&P=0 | https://ipmllp.com | London / Bratislava (offices also Seoul, San Francisco, Hong Kong) | growth VC / asset manager | uncertain
  fund_vehicles : ["IPM Growth s.r.o. (IČO 52 151 573, Banská Bystrica; shareholders IPM Group Holdings Limited (UK) and Global Connect Corporation SK)"]
  sectors : "InfraTech: mobility, AI-enabled infrastructure, energy"
  stages : "growth"
  ticket_min_eur : 25000
  INV Photoneo / Brightpick 2021-12-07 USD 21 million Series B (IPM led) https://www.automate.org/robotics/news/photoneo-raises-21-million-in-series-b/anc press release
  INV Matsuko 2019-10-11 ~EUR 1 million round led by IPM https://www.startitup.sk/kosicky-startup-matsuko-ziskal-takmer-milionovu-investiciu-obsadzuje-svetovy-trh/ press article
  SRC profile/ticket ['https://www.vestbee.com/vc-list/ipm-growth']
  SRC slovak entity ['https://www.orsr.sk/vypis.asp?ID=450600&SID=3&P=0']
  Q vestbee: ticket '€25K to €5M+'
  Q startitup 11.10.2019: 'anglicko-slovenský fond IPM spolu so súčasnými investormi z Neulogy Ventures'
===== 11 Impact Ventures, s. r. o. (Žilina) | Impact Ventures, s. r. o. | ICO 55 927 033 | https://www.orsr.sk/vypis.asp?ID=679020&SID=5&P=0 | None | Žilina | impact co-investment SPV | exclude
  INV Seerlinq s.r.o. 2026-09-08 not public https://www.orsr.sk/vypis.asp?ID=665401&SID=7&P=0 business regi
… [9827 more characters]
```
</details>

→ `Bash` — Dump compact view of candidates 30-48
```sh
python3 -c "
import json
d=json.load(open('research/sk-vc-candidates.json'))
for i,c in enumerate(d[30:],30):
    print('=====',i,c['name'],'|',c.get('management_company'),'| ICO',c.get('ico'),'|',c.get('register_link'),'|',c.get('website'),'|',c.get('hq_city'),'|',c.get('proposed_type'),'|',c.get('decision'))
    for k in ['fund_vehicles','ticket_min_eur','ticket_max_eur','fund_sizes']:
        v=c.get(k)
        if v: print(' ',k,':',json.dumps(v,ensure_ascii=False))
    for r in c.get('recent_investments') or []:
        print('  INV',r['company'],r['date'],r.get('round_size'),r['source']['url'],r.get('evidence_type'))
    for k,v in (c.get('sources') or {}).items():
        print('  SRC',k,[s['url'] for s in v])
    for q in c.get('evidence_quotes') or []: print('  Q',q)
"
```

<details><summary>result</summary>

```
===== 30 Monogram Ventures | MONOGRAM Ventures a. s. | ICO 44 071 574 | None | None | Bratislava | VC (dormant) | exclude
  SRC legal ['https://www.orsr.sk/vypis.asp?ID=124603&SID=2&P=0']
  SRC activity ['https://www.caplight.com/investor/monogram']
===== 31 Arca Capital Slovakia | None | ICO 35 868 856 | None | None | Bratislava | PE (parent in restructuring) | exclude
  SRC legal ['https://www.orsr.sk/vypis.asp?ID=39276&SID=2&P=0']
  SRC list ['https://www.podnikajte.sk/investor/private-equity-venture-fondy-sr']
===== 32 Pro Partners Holding | None | ICO 47 257 521 | None | None | Bratislava | investment holding (PE/real estate) | exclude
  SRC legal ['https://www.orsr.sk/vypis.asp?ID=325650&SID=2&P=0']
  SRC profile ['https://altss.com/profile/pro-partners-holding']
===== 33 Credo Ventures | None | ICO None | None | None | Prague | VC (Czech) | exclude
  SRC site ['https://www.credoventures.com/']
===== 34 Presto Ventures | None | ICO None | None | None | Prague | VC (Czech) | exclude
  SRC profile ['https://tech.eu/2022/06/23/presto-ventures-pulls-eur30-million-out-of-its-hat-with-second-fund-aimed-squarely-at-cee-region-startups/']
===== 35 J&T Ventures | None | ICO None | None | None | Prague | VC (Czech) | exclude
  SRC profile ['https://pitchbook.com/profiles/investor/157578-04']
===== 36 Nation 1 | None | ICO None | None | None | None | VC (Czech) | exclude
  SRC profile ['https://cc.cz/novy-cesky-investicni-fond-nation-1-ma-pro-startupy-500-milionu-korun-do-konce-ro
… [2371 more characters]
```
</details>

→ `Write` [tmp]

<details><summary>result</summary>

```
File created successfully at: [tmp] (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Test fetch helper on Neulogy ORSR extract
```sh
S=[tmp] cat > $S/pg <<'EOF'
#!/bin/sh
exec /Users/[redacted]/homeW/ai-dev-test/investor-db/.venv/bin/python [tmp] "$@"
EOF
chmod +x $S/pg; $S/pg get "https://www.orsr.sk/vypis.asp?ID=276162&SID=2&P=0" 3000
```

<details><summary>result</summary>

```
{"url": "https://www.orsr.sk/vypis.asp?ID=276162&SID=2&P=0", "status": 200, "final_url": "https://www.orsr.sk/vypis.asp?ID=276162&SID=2&P=0", "ctype": "text/html", "chars": 3200}
Výpis z obchodného registra SR
MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY
OBCHODNÝ REGISTER
NA INTERNETE
Slovensky
|
English
Výpis z Obchodného registra Mestského súdu Bratislava III
Tento výpis má len informatívny charakter a nie je použiteľný pre právne úkony!
Zobraziť na novej verzii portálu
Oddiel:
Sa
Vložka číslo:
5826/B
Obchodné meno:
Neulogy Ventures, a. s.
(od: 24.08.2013)
Sídlo:
Tallerova
4
Bratislava - mestská časť Staré Mesto
811 02
(od: 16.07.2016)
IČO:
47 367 610
(od: 24.08.2013)
Deň zápisu:
24.08.2013
(od: 24.08.2013)
Právna forma:
Akciová spoločnosť
(od: 24.08.2013)
Predmet podnikania (činnosti):
Činnosť podnikateľských, organizačných a ekonomických poradcov
(od: 24.08.2013)
Administratívne služby
(od: 24.08.2013)
Sprostredkovateľská činnosť v oblasti obchodu
(od: 24.08.2013)
Sprostredkovateľská činnosť v oblasti služieb
(od: 24.08.2013)
Kúpa tovaru na účely jeho predaja konečnému spotrebiteľovi (maloobchod) alebo iným prevádzkovateľom živnosti (veľkoobchod)
(od: 24.08.2013)
Prieskum trhu a verejnej mienky
(od: 24.08.2013)
Reklamné a marketingové služby
(od: 24.08.2013)
Prenájom hnuteľných vecí
(od: 24.08.2013)
Služby súvisiace s počítačovým spracovaním údajov
(od: 24.08.2013)
Vykonávanie mimoškolskej vzdelávacej činnosti
(od: 24.08.2013)
Štatutárny orgán:
predstavenstvo
(od: 24.
… [1679 more characters]
```
</details>

→ `Bash` — Fetch Neulogy homepage text
```sh
S=[tmp] $S/pg get "https://www.neulogy.vc/" 6000; 
```

<details><summary>result</summary>

```
{"url": "https://www.neulogy.vc/", "status": 200, "final_url": "https://neulogy.vc/", "ctype": "text/html; charset=UTF-8", "chars": 4796}
Neulogy VC - Neulogy VC
Skip to content
×
About us
Portfolio
News
Careers
17
Contact
Investors
About us
Portfolio
News
Careers
17
Contact
Investors
We help
entrepreneurs
build great
companies.
Contact us
Explore
We invest in real innovation, and don’t
just blindly follow the hype.
101
Founders
€135 million
Sales
10
Countries
Deeptech investments leveraging CEE engineering talent.
Moonshot ideas pushing the frontier in technology, climate and health.
About us
Meet with our top
companies
Medtech
Anvesana
Anvesana is leveraging RNAseq analysis platform to treat rare genetic disorders caused by gene dosage effects.
B2B SaaS
Cleantech
BeIT
BeiT is a unified platform for managing financial and operational processes in residential and commercial properties.
B2B SaaS
BiteBerry
BiteBerry uses AI to boost restaurant efficiency with a voice ordering system integrated into POS systems.
Marketplace
Medtech
Diagnose.me
Diagnose.me is a digital platform for medical diagnosis by international medical specialists.
Marketplace
Eyerim
Eyerim is a leading online eye-wear retailer in CEE.
Cybersec
Excalibur
Excalibur offers cyber security as a service with a range of enterprise-grade security solutions.
Cleantech
GA Drilling
GA Drilling develops technology for ultra-deep geothermal as the only viable large-scale baseload solution.
Cleantech
Infrastructure
Green
… [3434 more characters]
```
</details>

→ `Bash` — Fetch Neulogy portfolio and news pages
```sh
S=[tmp] $S/pg get "https://neulogy.vc/portfolio/" 5000; $S/pg get "https://neulogy.vc/news/" 5000
```

<details><summary>result</summary>

```
{"url": "https://neulogy.vc/portfolio/", "status": 200, "final_url": "https://neulogy.vc/portfolio/", "ctype": "text/html; charset=UTF-8", "chars": 3849}
Portfolio Archive - Neulogy VC
Skip to content
×
About us
Portfolio
News
Careers
17
Contact
Investors
About us
Portfolio
News
Careers
17
Contact
Investors
Porfolio of amazing
companies
Sort by industry
All
B2B SaaS
Cleantech
Cybersec
Infrastructure
Marketplace
Medtech
VR/XR
Medtech
Anvesana
Anvesana is leveraging RNAseq analysis platform to treat rare genetic disorders caused by gene dosage effects.
B2B SaaS
Cleantech
BeIT
BeiT is a unified platform for managing financial and operational processes in residential and commercial properties.
B2B SaaS
BiteBerry
BiteBerry uses AI to boost restaurant efficiency with a voice ordering system integrated into POS systems.
Marketplace
Medtech
Diagnose.me
Diagnose.me is a digital platform for medical diagnosis by international medical specialists.
Marketplace
Eyerim
Eyerim is a leading online eye-wear retailer in CEE.
Cybersec
Excalibur
Excalibur offers cyber security as a service with a range of enterprise-grade security solutions.
Cleantech
GA Drilling
GA Drilling develops technology for ultra-deep geothermal as the only viable large-scale baseload solution.
Cleantech
Infrastructure
GreenWay
GreenWay is a provider of charging infrastructure for e-vehicles in the CEE.
B2B SaaS
GroupSolver
GroupSolver is an online platform for market research and collective problem solving.
B2B SaaS
Exi
… [6138 more characters]
```
</details>

→ `Bash` — Check BiteBerry ORSR shareholders
```sh
S=[tmp] $S/pg get "https://www.orsr.sk/vypis.asp?ID=694090&SID=5&P=0" 200 >/dev/null; $S/pg grep "https://www.orsr.sk/vypis.asp?ID=694090&SID=5&P=0" "Spoločníci:.{0,1500}" 0
```

<details><summary>result</summary>

```
1 hits (status 200, 2914 chars)
--- Spoločníci: Core Capital s. r. o. IČO: 55 496 865 Tematínska 3231/2 Bratislava - mestská časť Petržalka 851 05 (od: 08.07.2023) Vision Ventures Growth I, s. r. o. IČO: 52 656 438 Bottova 2A Bratislava - mestská časť Staré Mesto 811 09 (od: 09.08.2023) AI Group s.r.o. IČO: 55 614 710 Bytčická 1139/89 Žilina 010 09 (od: 09.08.2023) Výška vkladu každého spoločníka: Core Capital s. r. o. Vklad: 14 520 EUR ( peňažný vklad ) Splatené: 14 520 EUR (od: 08.07.2023) Vision Ventures Growth I, s. r. o. Vklad: 2 254 EUR ( peňažný vklad ) Splatené: 2 254 EUR (od: 09.08.2023) AI Group s.r.o. Vklad: 750 EUR ( peňažný vklad ) Splatené: 750 EUR (od: 09.08.2023) Štatutárny orgán: konatelia (od: 10.05.2024) Ing. Viera Oravec Dátum narodenia: 21.03.1985 Vznik funkcie: 01.05.2024 (od: 10.05.2024) Ing. Dušan Koutný Dátum narodenia: 23.10.1984 Vznik funkcie: 01.05.2024 (od: 10.05.2024) Konanie menom spoločnosti: V mene spoločnosti koná a podpisuje každý konateľ samostatne. (od: 22.04.2023) Výška základného imania: 17 524 EUR Rozsah splatenia: 17 524 EUR (od: 09.08.2023) Dozorná rada: Ing. Gabriel Horváth Dátum narodenia: 22.02.1988 Vznik funkcie: 14.07.2023 (od: 09.08.2023) Mgr. Adriána Kubáňová Dátum narodenia: 03.07.1986 Vznik funkcie: 01.05.2024 (od: 26.07.2024) Ing. Ivan Kollárik Dátum narodenia: 30.12.1984 Vznik funkcie: 09.06.2026 (od: 25.06.2026) Dátum aktualizácie údajov: 08.10.2026 Dátum výpisu: 11.10.2026 Aktuálne zmeny | Elektronické služby Obchodného r
… [47 more characters]
```
</details>

→ `Bash` — ORSR brief for Neulogy portfolio companies
```sh
cd [tmp] for n in "BeIT" "Anvesana" "Staffino" "MultiplexDX"; do echo "######## $n"; python3 orsr.py brief "$n" 2>&1 | head -30; done
```

<details><summary>result</summary>

```
######## BeIT
== BE ITALIAN, s.r.o. | https://www.orsr.sk/vypis.asp?ID=17253&SID=4&P=0
IČO: 36 577 251 | Sídlo: Kamenárska 5, Spišská Nová Ves 052 01 | zápis: 09.03.2004
Spoločníci: Alberto Russo / (od: 09.03.2004) / Ľudovít Vrana / (od: 09.03.2004) / Jozef Szentkereszty / (od: 09.03.2004) / 
Vklady: Alberto Russo / Vklad: 3 319,391888 EUR Splatené: 3 319,391888 EUR / (od: 16.02.2010) / Ľudovít Vrana / Vklad: 1 659,695944 EUR Splatené: 1 659,695944 EUR / (od: 16.02.2010) / Jozef Szentkereszty / Vklad: 1 659,695944 EUR Splatené: 1 659,695944 EUR / (od: 16.02.2010) / 
== BeiT SK s.r.o.,organizačná zložka | https://www.orsr.sk/vypis.asp?ID=705960&SID=2&P=0
IČO: 56 571 925 | Sídlo: Ve Střešovičkách 45/40, Střešovice, Praha 6 169 00 | zápis: 09.11.2024
== BEIT, s.r.o. | https://www.orsr.sk/vypis.asp?ID=334659&SID=5&P=0
IČO: 48 305 367 | Sídlo: Univerzitná 8413/6, Žilina 010 08 | zápis: 23.09.2015
Spoločníci: Dr.h.c. prof. Ing. Jozef Živčák , PhD. / Dátum narodenia: 03.05.1958 / (od: 21.05.2022) / doc. Ing. Radovan Hudák , PhD. / Dátum narodenia: 22.09.1976 / (od: 08.11.2022) / 
Vklady: doc. Ing. Radovan Hudák , PhD. / Vklad: 2 376 EUR Splatené: 2 376 EUR / (od: 08.11.2022) / Dr.h.c. prof. Ing. Jozef Živčák , PhD. / Vklad: 7 524 EUR Splatené: 7 524 EUR / (od: 21.05.2022) / 
######## Anvesana
== Anvesana s. r. o. | https://www.orsr.sk/vypis.asp?ID=653887&SID=2&P=0
IČO: 55 252 176 | Sídlo: Ilkovičova 8, Bratislava - mestská časť Karlova Ves 841 04 | zápis: 23.02.2023
Spoločníci: Anve
… [2952 more characters]
```
</details>

→ `Bash` — Fetch EIF Slovakia fund managers PDF
```sh
S=[tmp] $S/pg get "https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf" 6000
```

<details><summary>result</summary>

```
{"url": "https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf", "status": 200, "final_url": "https://www.eif.org/files/attachments/slovakia-equity-fundmanagers.pdf", "ctype": "application/pdf", "chars": 611}
 Public #
Fund name Fund manager Team location Mandate(s) short name Target area Geographical focus Strategy Main sector Stage focus Investment strategy set up End of investment period Fund Manager website
Sandberg Investment Fund II SCSp Sandberg Capital, sprav. spol., a.s. Slovakia CEFoF;COSME-EFG;EIF Multi-Country Private Equity Generalist Lower-Mid Market Fund 12/01/2027 https://sandberg.capital/#hero
Slovak Venture Fund S.C.A., SICAR Neulogy Ventures a.s. Slovakia CEFoF;EGF Slovakia Venture Capital ICT Balanced Fund 14/03/2027 https://www.neulogy.vc/
EIF equity fund partners
as at 30 September 2026
```
</details>

→ `Bash` — Fetch SLOVCA and SIH pages for Neulogy
```sh
S=[tmp] $S/pg get "https://www.slovca.sk/sk/riadni-clenovia/neulogy-ventures.html" 5000; echo; $S/pg get "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/neulogy-ventures-kapitalova-investicia" 4000
```

<details><summary>result</summary>

```
{"url": "https://www.slovca.sk/sk/riadni-clenovia/neulogy-ventures.html", "status": 200, "final_url": "https://www.slovca.sk/sk/riadni-clenovia/neulogy-ventures.html", "ctype": "text/html; charset=UTF-8", "chars": 1754}
Neulogy Ventures / Slovak Venture Capital & Private Equity Association SLOVCA
Neulogy Ventures
Adresa: Tallerova 2/4, 81102 Bratislava, Slovensko
Tel: +421 2 2077 4437
Web:
www.neulogy.vc/sk
E-mail:
info@neulogy.vc
Typ investícií: Seed, Venture capital
Preferovaná výška jednej investície: 200,000 - 2.5 M EUR
Objem prostriedkov v správe: 26 M EUR
Preferované odvetvie: Informačné a komunikačné technológie, energetika a medicínska diagnostika
Geografické zameranie: SR
Počet transakcií v SR: 28
Portfóliové spoločnosti: Agent Balance, Boldburg, CropTech, diagnose.me, Erigones, Eyerim, Group Solver, Gruveo, Ingenio, Inhiro, Ixworx, Limewood, Meet n Learn, Mentegram, MultiplexDX, Orderlord, Piano Media, Profifox, RoomAssistant, RF Elements, SaferPass, SEAK, Shortlist, Streamstar, Vectary
Prílohy na stiahnutie
neulogy-ventures_logo.jpg
(veľkosť 22 KB, formát jpg)
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
Čerstvé správy!
Prihláste sa na odber noviniek SLOVCA a získajte informácie o private equity trhu v EU a na Slovensku ako aj najnovšie štatistiky o investovanom rozvojovom k
… [1904 more characters]
```
</details>

→ `Bash` — Grep Slovak Venture Fund entries in ORSR extracts
```sh
S=[tmp] for u in "https://www.orsr.sk/vypis.asp?ID=554899&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=705838&SID=2&P=0"; do $S/pg get "$u" 10 >/dev/null; $S/pg grep "$u" "Slovak Venture Fund.{0,160}" 0; $S/pg grep "$u" "Obchodné meno: .{0,60}" 0; done
```

<details><summary>result</summary>

```
2 hits (status 200, 3774 chars)
--- Slovak Venture Fund S.C.A., SICAR Avenue Emile Reuter 11 Luxembourg L-2420 Luxemburské veľkovojvodstvo Iné identifikačné číslo: B185175 (od: 17.01.2026) Výška vkladu každého spolo
--- Slovak Venture Fund S.C.A., SICAR Vklad: 750 EUR ( peňažný vklad ) Splatené: 750 EUR (od: 17.01.2026) Štatutárny orgán: konateľ (od: 09.09.2021) Pavol Čekan Dátum narodenia: 25.03
1 hits (status 200, 3774 chars)
--- Obchodné meno: MultiplexDX, s.r.o. (od: 14.01.2016) Sídlo: Ilkovičova 8 Bra
2 hits (status 200, 4300 chars)
--- Slovak Venture Fund S.C.A., SICAR Boulevard Royal 18 Luxemburg L-2449 Luxemburské veľkovojvodstvo Iné identifikačné číslo: B 185175 (od: 18.10.2024) Výška vkladu každého spoločník
--- Slovak Venture Fund S.C.A., SICAR Vklad: 9 648 EUR ( peňažný vklad ) Splatené: 9 648 EUR (od: 19.12.2025) QQ Capital SE Vklad: 4 543 EUR ( peňažný vklad ) Splatené: 4 543 EUR (od:
1 hits (status 200, 4300 chars)
--- Obchodné meno: STAFFINO s. r. o. (od: 13.02.2014) Sídlo: Teslova 26 Bratisl
```
</details>

→ `Bash` — Check ORSR history extracts for Slovak Venture Fund
```sh
S=[tmp] for u in "https://www.orsr.sk/vypis.asp?ID=554899&SID=2&P=1" "https://www.orsr.sk/vypis.asp?ID=705838&SID=2&P=1"; do $S/pg get "$u" 10 >/dev/null; $S/pg grep "$u" "Slovak Venture Fund.{0,160}" 0; $S/pg grep "$u" "Spoločníci:.{0,200}" 0;  done
```

<details><summary>result</summary>

```
5 hits (status 200, 7324 chars)
--- Slovak Venture Fund S.C.A., SICAR Avenue Emile Reuter 11 Luxemburg L-2420 Luxemburské veľkovojvodstvo (od: 11.02.2016 do: 27.09.2018) MultiplexDX, Inc. Greentree Drive 160 City of
--- Slovak Venture Fund S.C.A., SICAR Avenue Emile Reuter 11 Luxembourg L-2420 Luxemburské veľkovojvodstvo Iné identifikačné číslo: B185175 (od: 17.01.2026) Výška vkladu každého spolo
--- Slovak Venture Fund S.C.A., SICAR Vklad: 750 EUR ( peňažný vklad ) Splatené: 750 EUR (od: 17.01.2026) JUDr. Artúr Fried , LL.M. Vklad: 2 000 EUR Splatené: 2 000 EUR (od: 14.01.201
--- Slovak Venture Fund S.C.A., SICAR Vklad: 3 000 EUR Splatené: 3 000 EUR (od: 11.02.2016 do: 04.07.2017) MultiplexDX, Inc. Vklad: 2 000 EUR Splatené: 2 000 EUR (od: 11.02.2016 do: 0
--- Slovak Venture Fund S.C.A., SICAR Vklad: 2 000 EUR Splatené: 2 000 EUR (od: 05.07.2017 do: 27.09.2018) MultiplexDX, Inc. Vklad: 3 000 EUR Splatené: 3 000 EUR (od: 05.07.2017 do: 2
1 hits (status 200, 7324 chars)
--- Spoločníci: JUDr. Artúr Fried , LL.M. (od: 14.01.2016 do: 10.02.2016) A.K.F. Lawyers, s.r.o. Páričkova 23 Bratislava - mestská časť Ružinov 821 08 (od: 14.01.2016 do: 10.02.2016) Slovak Venture Fund S.C.A., SICA
6 hits (status 200, 9762 chars)
--- Slovak Venture Fund S.C.A., SICAR Avenue Emile Reuter 11 Luxemburg L-2420 Luxemburské veľkovojvodstvo (od: 04.08.2015 do: 02.08.2022) Mgr. Tomáš Rosputinský (od: 13.09.2016 do: 20
--- Slovak Venture Fund S.C.A., SICAR Avenue Emile Reuter 11 Luxemburg L-2420 Luxemb
… [1083 more characters]
```
</details>

→ `Bash` — Show Staffino contribution history
```sh
S=[tmp] $S/pg grep "https://www.orsr.sk/vypis.asp?ID=705838&SID=2&P=1" "Výška vkladu každého spoločníka:.{0,2500}" 0
```

<details><summary>result</summary>

```
1 hits (status 200, 9762 chars)
--- Výška vkladu každého spoločníka: Mgr. Tomáš Rosputinský ( peňažný vklad ) (od: 13.09.2016 do: 20.12.2019) Mgr. Tomáš Rosputinský ( peňažný vklad ) (od: 21.12.2019 do: 28.02.2022) Mgr. Tomáš Rosputinský Vklad: 9 570 EUR ( peňažný vklad ) Splatené: 9 570 EUR (od: 01.03.2022) Michal Liptaj ( peňažný vklad ) (od: 13.09.2016 do: 28.02.2022) Michal Liptaj Vklad: 987 EUR ( peňažný vklad ) Splatené: 987 EUR (od: 01.03.2022) Ivan Dvoran ( peňažný vklad ) (od: 23.05.2017 do: 28.02.2022) Ivan Dvoran Vklad: 8 763 EUR ( peňažný vklad ) Splatené: 8 763 EUR (od: 01.03.2022) Synap s.r.o. Vklad: 987 EUR ( peňažný vklad ) Splatené: 987 EUR (od: 01.09.2023) Slovak Venture Fund S.C.A., SICAR Vklad: 9 648 EUR ( peňažný vklad ) Splatené: 9 648 EUR (od: 19.12.2025) QQ Capital SE Vklad: 4 543 EUR ( peňažný vklad ) Splatené: 4 543 EUR (od: 19.12.2025) Martin Vaľovský Vklad: 1 384 EUR ( peňažný vklad ) Splatené: 1 384 EUR (od: 19.12.2025) Bc. Ivan Dvoran Vklad: 5 000 EUR ( peňažný vklad ) Splatené: 5 000 EUR (od: 13.02.2014 do: 18.09.2014) Mgr. Tomáš Rosputinský Vklad: 5 000 EUR ( peňažný vklad ) Splatené: 5 000 EUR (od: 13.02.2014 do: 18.09.2014) Bealalaw s. r. o. Vklad: 12 222 EUR ( peňažný vklad ) Splatené: 12 222 EUR (od: 13.02.2014 do: 18.09.2014) Bc. Ivan Dvoran Vklad: 5 064 EUR ( peňažný vklad ) Splatené: 5 064 EUR (od: 19.09.2014 do: 04.05.2015) Mgr. Tomáš Rosputinský Vklad: 5 064 EUR ( peňažný vklad ) Splatené: 5 064 EUR (od: 19.09.2014 do: 13.04.2015) Beal
… [1068 more characters]
```
</details>

→ `ToolSearch`

<details><summary>result</summary>

```

```
</details>

→ `WebSearch` StratifAI pre-seed Neulogy Ventures MultiplexDX 1.5 million

<details><summary>result</summary>

```
Web search results for query: "StratifAI pre-seed Neulogy Ventures MultiplexDX 1.5 million"

Links: [{"title":"Christian Mandl","url":"https://sk.linkedin.com/in/christianmandl"},{"title":"cekan pavol multiplexdx 202409 inc persons people chief 2001 28559","url":"https://www.life-sciences-europe.com/person/cekan-pavol-multiplexdx-202409-inc-persons-people-chief-2001-28559.html"},{"title":"www.360dx.com","url":"https://www.360dx.com/node/105971"},{"title":"www.genomeweb.com","url":"https://www.genomeweb.com/node/643801"},{"title":"Recently FundedEUR 1.5MTechnology, Information and Internet","url":"https://www.trysignalbase.com/news/funding/stratifai-secures-1.5-million-in-pre-seed-funding-to-revolutionize-precision-oncology-with-ai-driven-biomarkers"},{"title":"stratiffai gmbh 2023 dresden sachsen federal state germany 2001 54811","url":"https://www.life-sciences-europe.com/organisation/stratiffai-gmbh-2023-dresden-sachsen-federal-state-germany-2001-54811.html"},{"title":"app.foundernest.com","url":"https://app.foundernest.com/public/space/7678/companies/10190350?page=11"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/company/stratifai"},{"title":"Founded Year","url":"https://www.cbinsights.com/company/multiplexdx"},{"title":"nahbas omar stratifai 202509 stratiffai gmbh persons people 2001 28550","url":"https://www.life-sciences-europe.com/person/nahbas-omar-stratifai-202509-stratiffai-gmbh-persons-people-2001
… [1324 more characters]
```
</details>

→ `Bash` — Fetch StratifAI and GA Drilling sources
```sh
S=[tmp] for u in "https://www.360dx.com/node/105971" "https://www.genomeweb.com/node/643801" "https://www.trysignalbase.com/news/funding/stratifai-secures-1.5-million-in-pre-seed-funding-to-revolutionize-precision-oncology-with-ai-driven-biomarkers" "https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/"; do $S/pg get "$u" 10 | head -1; $S/pg grep "$u" "Neulogy.{0,100}" 150 | head -8; done
```

<details><summary>result</summary>

```
{"url": "https://www.360dx.com/node/105971", "status": 403, "final_url": "https://www.genomeweb.com/node/105971", "ctype": "text/html", "chars": 222}
0 hits (status 403, 222 chars)
{"url": "https://www.genomeweb.com/node/643801", "status": 403, "final_url": "https://www.genomeweb.com/node/643801", "ctype": "text/html", "chars": 222}
0 hits (status 403, 222 chars)
{"url": "https://www.trysignalbase.com/news/funding/stratifai-secures-1.5-million-in-pre-seed-funding-to-revolutionize-precision-oncology-with-ai-driven-biomarkers", "status": 200, "final_url": "https://www.trysignalbase.com/news/funding/stratifai-secures-1.5-million-in-pre-seed-funding-to-revolutionize-precision-oncology-with-ai-driven-biomarkers", "ctype": "text/html; charset=utf-8", "chars": 6533}
1 hits (status 200, 6533 chars)
--- K today 4 Nozomio United States Pre-seed $850.0K today 5 Lagos Company United States Pre-seed $500.0K today Trusted by 200+ sales teams Investors 5 N Neulogy Ventures M MultiplexDX International D Debiopharm A Arve Capital C Christoph Haarburger Unlock 3 more investors and reach their contacts directly. Start free trial Similar recently funded companies WIMR Medical Research AU Recently received $ 9.0M R
{"url": "https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/", "status": 200, "final_url": "https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/", "ctype": "text/html; charset=UTF-8", "char
… [865 more characters]
```
</details>

→ `Bash` — Get GA Drilling sentence and StratifAI page text
```sh
S=[tmp] u="https://www.thinkgeoenergy.com/ga-drilling-secures-15-million-funding-to-accelerate-deep-geothermal/"; $S/pg grep "$u" ".{0,400}Slovakia-based" 0; $S/pg grep "$u" "(April|2024).{0,80}" 40 | head -6; u2="https://www.trysignalbase.com/news/funding/stratifai-secures-1.5-million-in-pre-seed-funding-to-revolutionize-precision-oncology-with-ai-driven-biomarkers"; $S/pg text "$u2" 0 2500
```

<details><summary>result</summary>

```
1 hits (status 200, 7182 chars)
--- of successful tests, securing further investment to deliver deep geothermal faster and at deeper depths while remaining cost-effective. Investors include leading global drilling rig, services, and technology provider, Nabors , Christian Oldendorff’s new Family Office, alfa8 , the previous CEO of private equity firm EQT, Thomas von Koch, newly established geothermal fund Underground Ventures , and Slovakia-based
1 hits (status 200, 7182 chars)
--- unding to accelerate deep geothermal 18 April 2024 Carlo Cariaga View all articles | Contact GA Drilling has secured $15 million in investment to accelerate technolo
Signalbase
Signalbase B.V.
Amsterdam
The Netherlands
Stay in the Loop
Hey, we're building something special here. 👋
Join our mailing list to get updates on new features, funding signals, and insights about what actually works.
Only the good stuff, and only when it matters.
Yes, sign me up!
A low-key, occasional mailing list from our founder.
No pitching, no selling, just the learnings. You can unsubscribe at any time.
We never share your data and we hate spam.
News
VC Funding News
Mergers and Acquisitons
Top Recently Funded Startups
Resources
API Documentation
MCP Server
Signal-based guides
Glossary
Best Intent Data Providers in 2026
Best Funding Data Providers
Best Job Posting Data Providers
Best Job Change Tracking Tools
Best Data for Recruiting Agencies
Best Recruiting APIs
Connect with Us
Signal APIs
Intent Signals API
Recruiting D
… [1653 more characters]
```
</details>

→ `Bash` — Check Airvolute and Spinbotics ORSR history
```sh
S=[tmp] for u in "https://www.orsr.sk/vypis.asp?ID=548451&SID=7&P=1" "https://www.orsr.sk/vypis.asp?ID=527183&SID=4&P=1"; do $S/pg get "$u" 10 | head -1; $S/pg grep "$u" "Obchodné meno: .{0,60}" 0; $S/pg grep "$u" "(Vision Ventures Growth|Baryon).{0,190}" 0; done
```

<details><summary>result</summary>

```
{"url": "https://www.orsr.sk/vypis.asp?ID=548451&SID=7&P=1", "status": 200, "final_url": "https://www.orsr.sk/vypis.asp?ID=548451&SID=7&P=1", "ctype": "text/html", "chars": 6174}
1 hits (status 200, 6174 chars)
--- Obchodné meno: Airvolute s.r.o. (od: 07.04.2021) AE Drones, s.r.o. (od: 17.
6 hits (status 200, 6174 chars)
--- Vision ventures Growth l, s. r. o IČO: 52 656 438 Lomnická 906/2 Bratislava - mestská časť Devín 841 10 (od: 18.12.2020 do: 28.03.2025) Ing. Jozef Rodina , PhD. (od: 26.05.2023 do: 10.11.2025) Ing. Lukáš Palkovič
--- Vision Ventures Growth I, s. r. o. IČO: 52 656 438 Bottova 2A Bratislava - mestská časť Staré Mesto 811 09 (od: 29.03.2025) AV SPV 1 s.r.o. IČO: 56 428 863 Ota Holúska 9092/3B Bratislava - mestská časť Záhorská B
--- Baryon Fund SCSp Parc d'Activités 2-4 Capellen L-8308 Luxemburské veľkovojvodstvo Iné identifikačné číslo: B299800 (od: 09.01.2026) Výška vkladu každého spoločníka: AV SPV 1 s.r.o. Vklad: 3 427 EU
--- Vision Ventures Growth I, s. r. o. Vklad: 3 290 EUR ( peňažný vklad ) Splatené: 3 290 EUR (od: 09.01.2026) Baryon Fund SCSp Vklad: 2 569 EUR ( peňažný vklad ) Splatené: 2 569 EUR (od: 09.01.2026) Ing. Lukáš Palko
--- Vision ventures Growth l, s. r. o Vklad: 1 667 EUR Splatené: 1 667 EUR (od: 18.12.2020 do: 28.03.2025) Ing. Lukáš Palkovič , PhD. ( peňažný vklad ) (od: 26.05.2023 do: 28.03.2025) Ing. Lukáš Palkovič , PhD. Vklad
--- Vision Ventures Growth I, s. r. o. Vklad: 1 667 EUR ( peňažný vklad ) Splatené: 1 667 EUR (od: 29.03.202
… [1081 more characters]
```
</details>

→ `Bash` — Show Vision Ventures contributions in Airvolute
```sh
S=[tmp] u="https://www.orsr.sk/vypis.asp?ID=548451&SID=7&P=1"; $S/pg grep "$u" "Vision Ventures Growth I, s. r. o. Vklad.{0,110}" 0; u0="https://www.orsr.sk/vypis.asp?ID=548451&SID=7&P=0"; $S/pg get "$u0" 10 >/dev/null; $S/pg grep "$u0" "Spoločníci:.{0,900}" 0
```

<details><summary>result</summary>

```
2 hits (status 200, 6174 chars)
--- Vision Ventures Growth I, s. r. o. Vklad: 3 290 EUR ( peňažný vklad ) Splatené: 3 290 EUR (od: 09.01.2026) Baryon Fund SCSp Vklad: 2 569 EUR ( peňažný
--- Vision Ventures Growth I, s. r. o. Vklad: 1 667 EUR ( peňažný vklad ) Splatené: 1 667 EUR (od: 29.03.2025 do: 10.11.2025) Vision Ventures Growth I, s.
1 hits (status 200, 4078 chars)
--- Spoločníci: Vision Ventures Growth I, s. r. o. IČO: 52 656 438 Bottova 2A Bratislava - mestská časť Staré Mesto 811 09 (od: 29.03.2025) AV SPV 1 s.r.o. IČO: 56 428 863 Ota Holúska 9092/3B Bratislava - mestská časť Záhorská Bystrica 841 06 (od: 11.11.2025) AV SPV 2 s.r.o. IČO: 56 424 884 Nejedlého 1907/21 Bratislava - mestská časť Dúbravka 841 02 (od: 11.11.2025) AV SPV 3 s.r.o. IČO: 56 364 679 Sibírska 1612/20 Bratislava - mestská časť Nové Mesto 831 02 (od: 11.11.2025) Baryon Fund SCSp Parc d'Activités 2-4 Capellen L-8308 Luxemburské veľkovojvodstvo Iné identifikačné číslo: B299800 (od: 09.01.2026) Výška vkladu každého spoločníka: AV SPV 1 s.r.o. Vklad: 3 427 EUR ( peňažný vklad ) Splatené: 3 427 EUR (od: 11.11.2025) AV SPV 2 s.r.o. Vklad: 2 996 EUR ( peňažný vklad ) Splatené: 2 996 EUR (od: 11.11.2025) AV SPV 3 s.r.o. Vklad: 1 077 EUR ( peňažný vklad ) Splatené: 1 077 EUR (od: 11.11.2025) Vision
```
</details>

→ `Bash` — Check Spinbotics contributions and Vision Ventures site
```sh
S=[tmp] $S/pg grep "https://www.orsr.sk/vypis.asp?ID=527183&SID=4&P=1" "Vision Ventures Growth I, s. r. o. (Vklad|\().{0,120}" 0; $S/pg get "https://visionventures.vc/" 5000
```

<details><summary>result</summary>

```
2 hits (status 200, 4151 chars)
--- Vision Ventures Growth I, s. r. o. ( peňažný vklad ) (od: 07.05.2020 do: 01.02.2023) Vision Ventures Growth I, s. r. o. ( peňažný vklad ) (od: 02.02.2023 do
--- Vision Ventures Growth I, s. r. o. Vklad: 2 143 EUR ( peňažný vklad ) Splatené: 2 143 EUR (od: 18.04.2024) Ing. Peter Tkáč Vklad: 6 818 EUR ( peňažný vklad ) Sp
{"url": "https://visionventures.vc/", "status": 200, "final_url": "https://visionventures.vc/", "ctype": "text/html; charset=UTF-8", "chars": 11393}
Vision Ventures
Skip to content
Contact us
Supporting courageous and passionate entrepreneurs with
bold ambitions
to build a business on a global scale.
VC fund focused on pre-seed and seed investments in Slovakia.
See how we can help
We invest in Slovak's most ambitious start-ups:
26
Portfolio companies
Investment up to
1.6 million €
Investing in
Slovakia
About us
Vision Ventures
Vision Ventures is a VC investor focused on pre-seed and seed investments in Slovakia, providing investment up to EUR 1.6 million.
We support courageous and passionate entrepreneurs with bold ambitions to build a business on the global scale.
Our Vision & Mission
We’ll
help you grow
your idea exponentially.
Vision
The innovations and new technologies dynamically changing the world fascinate us.
We believe that these opportunities can make the world a better place for everyone.
Therefore, we want to search for unique companies and help them in their successful growth.
Mission
We seek and actively connec
… [4007 more characters]
```
</details>

→ `Bash` — Check Seerlinq ORSR shareholders
```sh
S=[tmp] u="https://www.orsr.sk/vypis.asp?ID=665401&SID=7&P=0"; $S/pg get "$u" 10 >/dev/null; $S/pg grep "$u" "Spoločníci:.{0,1800}" 0; u="https://www.orsr.sk/vypis.asp?ID=665401&SID=7&P=1"; $S/pg get "$u" 10 >/dev/null; $S/pg grep "$u" "(Vision|Impact Ventures|National Development).{0,150}" 0
```

<details><summary>result</summary>

```
1 hits (status 200, 5443 chars)
--- Spoločníci: Nikola Jajcay Dátum narodenia: 20.05.1990 (od: 28.12.2022) MUDr. Branislav Bezák Dátum narodenia: 11.01.1991 (od: 28.12.2022) PMX Solutions, občianske združenie IČO: 53 360 460 Medená 97/18 Bratislava - mestská časť Staré Mesto 811 02 (od: 28.12.2022) Traun s. r. o IČO: 54 512 255 Pod násypom 7/J Bratislava - mestská časť Lamač 841 03 (od: 28.12.2022) Vision Ventures Growth I, s. r. o. IČO: 52 656 438 Bottova 2A Bratislava - mestská časť Staré Mesto 811 09 (od: 14.07.2023) Impact Ventures, s. r. o. IČO: 55 927 033 Framborská ulica 283/58 Žilina 010 01 (od: 08.09.2026) LongTaal, s. r. o. IČO: 46 769 676 Staré grunty 61 Bratislava - mestská časť Karlova Ves 841 04 (od: 08.09.2026) National Development Fund II., a.s. IČO: 47 759 224 Grösslingová 44 Bratislava - mestská časť Staré Mesto 811 09 (od: 08.09.2026) Výška vkladu každého spoločníka: Nikola Jajcay Vklad: 756 EUR ( peňažný vklad ) Splatené: 756 EUR (od: 28.12.2022) MUDr. Branislav Bezák Vklad: 756 EUR ( peňažný vklad ) Splatené: 756 EUR (od: 28.12.2022) PMX Solutions, občianske združenie Vklad: 6 048 EUR ( peňažný vklad ) Splatené: 6 048 EUR (od: 28.12.2022) Traun s. r. o Vklad: 840 EUR ( peňažný vklad ) Splatené: 840 EUR (od: 28.12.2022) Vision Ventures Growth I, s. r. o. Vklad: 1 050 EUR ( peňažný vklad ) Splatené: 1 050 EUR (od: 14.07.2023) Impact Ventures, s. r. o. Vklad: 750 EUR ( peňažný vklad ) Splatené: 750 EUR (od: 08.09.2026) LongTaal, s. r. o. Vklad: 750 EUR ( peň
… [1050 more characters]
```
</details>

→ `Bash` — Fetch VFF ORSR extract and website
```sh
S=[tmp] u="https://www.orsr.sk/vypis.asp?ID=464212&SID=2&P=0"; $S/pg get "$u" 10|head -1; $S/pg text "$u" 0 3500 | tr '\n' ' ' | head -c 3500; echo; $S/pg get "https://vff.sk/" 6000
```

<details><summary>result</summary>

```
{"url": "https://www.orsr.sk/vypis.asp?ID=464212&SID=2&P=0", "status": 200, "final_url": "https://www.orsr.sk/vypis.asp?ID=464212&SID=2&P=0", "ctype": "text/html", "chars": 3406}
Výpis z obchodného registra SR MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY OBCHODNÝ REGISTER NA INTERNETE Slovensky | English Výpis z Obchodného registra Mestského súdu Bratislava III Tento výpis má len informatívny charakter a nie je použiteľný pre právne úkony! Zobraziť na novej verzii portálu Oddiel: Sa Vložka číslo: 6938/B Obchodné meno: Venture to Future Fund, a.s. (od: 07.05.2019) Sídlo: Grösslingová 44 Bratislava - mestská časť Staré Mesto 811 09 (od: 07.05.2019) IČO: 52 380 483 (od: 07.05.2019) Deň zápisu: 07.05.2019 (od: 07.05.2019) Právna forma: Akciová spoločnosť (od: 07.05.2019) Predmet podnikania (činnosti): Činnosť podnikateľských, organizačných a ekonomických poradcov (od: 07.05.2019) Poskytovanie úverov alebo pôžičiek z peňažných zdrojov získaných výlučne bez verejnej výzvy a bez verejnej ponuky majetkových hodnôt (od: 07.05.2019) 4 Sprostredkovanie poskytovania úverov alebo pôžičiek z peňažných zdrojov získaných výlučne bez verejnej výzvy a bez verejnej ponuky majetkových hodnôt (od: 07.05.2019) Administratívne služby (od: 07.05.2019) Sprostredkovateľská činnosť v oblasti obchodu, služieb, výroby (od: 07.05.2019) zhromažďovanie peňažných prostriedkov od investorov s cieľom investovať ich v súlade s určenou investičnou politikou v prospech osôb, ktorých peňažné prostriedky boli z
… [8110 more characters]
```
</details>

→ `Bash` — Fetch VFF deal and profile sources
```sh
S=[tmp] for u in "https://www.startitup.sk/z-brna-do-dubaja-novy-fond-nalial-miliony-do-startupu-ktory-vznikol-ako-studentsky-projekt-teraz-mieri-aj-na-slovensko/" "https://vestbee.com/insights/articles/talentiqa-raises-1-1-m" "https://www.e15.cz/byznys/fait-investuje-miliony-do-online-distribuce-autodilu-platformu-iag-podpori-i-slovaci-1424729" "https://www.sih.sk/en/aktuality/venture-to-future-fund-navysuje-kapital-o-15-3-miliona-eur-na-podporu-slovenskych-startupov" "https://www.slovca.sk/sk/riadni-clenovia/venture-to-future-fund.html"; do $S/pg get "$u" 10|head -1; $S/pg grep "$u" "Venture to Future.{0,150}" 200 | head -6; done
```

<details><summary>result</summary>

```
{"url": "https://www.startitup.sk/z-brna-do-dubaja-novy-fond-nalial-miliony-do-startupu-ktory-vznikol-ako-studentsky-projekt-teraz-mieri-aj-na-slovensko/", "status": 200, "final_url": "https://www.startitup.sk/z-brna-do-dubaja-novy-fond-nalial-miliony-do-startupu-ktory-vznikol-ako-studentsky-projekt-teraz-mieri-aj-na-slovensko/", "ctype": "text/html; charset=UTF-8", "chars": 10735}
1 hits (status 200, 10734 chars)
--- nvestícia za milióny dolárov JIC Ventures vstúpil do investičného kola Series A spoločnosti FaceUp v hodnote 5 miliónov dolárov. Kolo viedol chorvátsky fond Fil Rouge Capital. Pridali sa aj slovenský Venture to Future Fund, pražský Gi21 Capital a doterajší investori Jiří Hlavenka, Tilia Impact Ventures či Reflex Capital spolu s anjelskými investormi a zamestnancami firmy. Celkovo FaceUp počas svojej histórie získal už približne 9 miliónov dolárov. „S Janom a tímom FaceUp sme spolu od začiatku. Sledovať, ako zo študentského projektu vyrástlo komplexné riešenie p
{"url": "https://vestbee.com/insights/articles/talentiqa-raises-1-1-m", "status": 200, "final_url": "https://www.vestbee.com/insights/articles/talentiqa-raises-1-1-m", "ctype": "text/html;charset=utf-8", "chars": 5622}
2 hits (status 200, 5622 chars)
--- irm Talentiqa, which automates candidate pre-screening to streamline and accelerate hiring, has raised €1.1 million (CZK 25 million), with the investment equally split between Purple Ventures and the Venture to Future Fund, as Vestbee was told. Launched i
… [6634 more characters]
```
</details>

→ `Bash` — Find publication dates in VFF deal articles
```sh
S=[tmp] for u in "https://www.startitup.sk/z-brna-do-dubaja-novy-fond-nalial-miliony-do-startupu-ktory-vznikol-ako-studentsky-projekt-teraz-mieri-aj-na-slovensko/" "https://vestbee.com/insights/articles/talentiqa-raises-1-1-m" "https://www.e15.cz/byznys/fait-investuje-miliony-do-online-distribuce-autodilu-platformu-iag-podpori-i-slovaci-1424729"; do grep -oE '"datePublished"[^,]{0,40}|article:published_time" content="[^"]{0,30}|[0-9]{1,2}\. ?[0-9]{1,2}\. ?20[0-9]{2}' $S/cache/$(python3 -c "import hashlib,sys;print(hashlib.sha1(sys.argv[1].encode()).hexdigest())" "$u").raw | sort | uniq -c | head -5; $S/pg grep "$u" "(20(24|25|26)).{0,30}" 60 | head -4; done
```

<details><summary>result</summary>

```
   2 "datePublished":"2026-05-19T14:59:22+00:00"
   1 article:published_time" content="2026-05-19T14:59:22+00:00
4 hits (status 200, 10734 chars)
--- ojekt. Teraz mieri aj na Slovensko Jasmína Púčková 19. mája 2026 o 16:59 Študentský projekt z Brna dnes funguje vo viac ako 70 krajinách sveta. Nový fond 
--- id Špunar Archív/Fond JIC Ventures Jasmína Púčková 19. mája 2026 o 16:59 Uložiť Uložené Zdieľať Ešte pred pár rokmi išlo o študentský projekt , ktorý vzni
--- o Kiwi.com, Y Soft alebo Flowmon. Financial Times ju v roku 2026 zaradil medzi päťdesiat najlepších startupových hubov v Európe. Do nového fondu nevstúpil
   1 "datePublished":"2025-09-29T13:50:40.347Z"
5 hits (status 200, 5622 chars)
---  and corporates in Europe Join here Join here September 29, 2025 · 2 min read Joy Laoun News Editor, Vestbee Insights Czech-Slovak startup Talentiqa raise
--- the US. Deals #News #Czech Republic #Slovakia September 29, 2025 Latest news Oct 09 UK neurotech chip developer MintNeuro raises $5M. Czech JSK Investment
--- re Editor's pick Top CEE funding rounds closed in September 2026 Europe’s defence and dual-use investors The US loves longevity. Can Europe turn it into v
   1 "datePublished": "2025-05-22T12:29:00+02:00"
11 hits (status 200, 6124 chars)
--- Fait • Zdroj: E15 Michaela Szkanderová ČTK , koc 22. května 2025 · 12:29 Diskuze ( 1 ) Investiční skupina Jet Investment brněnského miliardáře Igora Faita
--- stupujících má ANO Komunální volby Aktualizováno Mapa voleb 2026 podle okr
… [239 more characters]
```
</details>

→ `Bash` — Check 2020 VFF article for manager
```sh
S=[tmp] u="https://www.startitup.sk/?p=358673"; $S/pg get "$u" 10|head -1; $S/pg grep "$u" "(sprav|Asset Management|40 mil).{0,200}" 150 | head -8
```

<details><summary>result</summary>

```
{"url": "https://www.startitup.sk/?p=358673", "status": 200, "final_url": "https://www.startitup.sk/slovenske-startupy-uz-nemusia-odchadzat-do-zahranicia-vznikol-jedinecny-fond-na-ich-podporu/", "ctype": "text/html; charset=UTF-8", "chars": 5977}
3 hits (status 200, 5977 chars)
--- ru Patrik Zengevald/SITA 11. februára 2020 o 14:07 Európska investičná banka, Ministerstvo financií a Slovak Investment Holding do neho zainvestovali 40 mil. eur. Fond bude pomáhať malým a stredným podnikom so silným rastovým potenciálom. TASR Patrik Zengevald/SITA 11. februára 2020 o 14:07 Uložiť Uložené Zdieľať Na Slovensku vznikol nový fond na podporu inovatívnych a technologických malých a stredných podnikov. Európska investičná banka (EIB), Ministerstvo financií SR a Slovak Investment Holding (SI
--- ických malých a stredných podnikov. Európska investičná banka (EIB), Ministerstvo financií SR a Slovak Investment Holding (SIH) do neho zainvestovali 40 mil. eur. Venture to Future Fund bude od marca tohto roku poskytovať slovenským spoločnostiam kapitálové a kvázi-kapitálové financovanie. Prihlás sa na odber notifikácií a najnovšie info dostaneš medzi prvými. ODOBERAŤ notifikácie zo Startitup vo svojom prehliadači Dostaň Startitup do svojich Google odporúčaní Pridať ako preferovaný zdroj Startitup, o
--- roj Startitup, odkaz sa otvorí v novom okne Ako ďalej informoval SIH, poskytovateľom bude nový fond pod licencovanou správcovskou spoločnosťou Slovak Asset Management, ktorá patrí do investičnej 
… [321 more characters]
```
</details>

→ `Bash` — Look up Slovak Asset Management in ORSR
```sh
cd [tmp] python3 orsr.py brief "Slovak Asset Management" | head -12
```

<details><summary>result</summary>

```
(Bash completed with no output)
```
</details>

→ `Bash` — Search ORSR for SIH-group entities
```sh
cd [tmp] python3 orsr.py search "Slovak Asset"; python3 orsr.py search "Slovak Investment Holding"
```

<details><summary>result</summary>

```
Slovak Assets s. r. o. | https://www.orsr.sk/vypis.asp?ID=545881&SID=2&P=0
Slovak Investment Holding, a. s. | https://www.orsr.sk/vypis.asp?ID=307221&SID=2&P=0
```
</details>

→ `Bash` — Fetch 0100.vc homepage
```sh
S=[tmp] $S/pg get "https://0100.vc/" 7000
```

<details><summary>result</summary>

```
{"url": "https://0100.vc/", "status": 200, "final_url": "https://www.0100.vc/", "ctype": "text/html; charset=utf-8", "chars": 11859}
Zero One Hundred | Main page
A venture capital company founded by builders, with a unique ecosystem, backing the best startups from Emerging Europe and the Middle East.
An entrepreneurial ecosystem which adds value
Future winners require more than mere capital. We love working with founders side by side, helping their visions come to life. We’re also bringing unmatched value through the companies we have built: leading players in the innovation, technology, and investment sectors.
In past 10 years our team
In past
12 years our team
Started
10 companies
Invested
in 34 companies
Exited
4 companies
Organized
70+ international conferences
Welcomed
20,000 entrepreneurs to our events
Brought
10,000 investors to our events
Hosted
4,000 technical talents and operators at our community events
Built
1 unique entrepreneurial ecosystem
Our portfolio
Leading the AI revolution in cardiovascular care
Visit website
Unlocking the full earning power of mobile games
Visit website
Redefining car ownership
Visit website
Tech-driven platform for planning, executing, and financing renovations
Visit website
Smartest partner for personal and business finance
Visit website
AI Real Estate Analysis and Marketing Platform
Visit website
AI behaviour and experimentation layer for enterprises
Visit website
Platform that simplifies HR, payroll, and attendance for SMEs
Visit web
… [5633 more characters]
```
</details>

→ `Bash` — Check 0100 legal footer and ORSR for 0100/ZGC entities
```sh
S=[tmp] $S/pg grep "https://0100.vc/" "This website and all its content.{0,300}" 0; for u in "https://www.orsr.sk/vypis.asp?ID=346365&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=498371&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=503429&SID=2&P=0"; do $S/pg get "$u" 10 >/dev/null; $S/pg grep "$u" "(Obchodné meno: .{0,80}|Sídlo: .{0,90}|IČO: .{0,30}|Spoločníci:.{0,600}|Akcionár:.{0,300})" 0; done
```

<details><summary>result</summary>

```
1 hits (status 200, 11858 chars)
--- This website and all its content belong exclusively to 0100 VC RAIF F.C.I.C. PLC., with a registered office at 5 Esperidon Street 2001, Strovolos, Nicosia, Cyprus. The Fund is only addressed to Well-Informed and/or Professional Investors (the “Eligible Investors”). Paul Jozefak Executive in Residence Paul has spent over thirty yea
6 hits (status 200, 6455 chars)
--- Obchodné meno: 0100 Ventures s. r. o. (od: 16.03.2016) Sídlo: Staré grunty 18 Bratislava - mest
--- IČO: 50 209 728 (od: 16.03.2016) De
--- Spoločníci: Mgr. Michal Paško Dátum narodenia: 21.08.1989 (od: 09.12.2022) Dušan Duffek Dátum narodenia: 25.06.1990 (od: 09.12.2022) Martin Joakim Flood Hauge Dátum narodenia: 26.08.1989 (od: 09.12.2022) Peter Klíma Dátum narodenia: 15.07.1962 (od: 09.12.2022) CHB PARTNERS GmbH Am Bahnhof, Ebni 3 Teufen AR 9053 Švajčiarska konfederácia Iné identifikačné číslo: CHE-108.469.826 (od: 09.12.2022) Pannonia Property Group a.s. IČO: 52 718 280 Tolstého 850/7 Bratislava - mestská časť Staré Mesto 811 02 (od: 09.12.2022) Lepaka s.r.o. IČO: 54 243 581 Nové Záhrady I/9 Bratislava - mestská časť Ružinov 821 05 (od: 
--- IČO: 48 324 779 Panenská 18 Bratisl
--- IČO: 51 687 682 Tramínová 12869/11 
--- IČO: 35 704 098 Alžbetina 41 Košice
3 hits (status 200, 2174 chars)
--- Obchodné meno: Zero Gravity Capital s.r.o. (od: 01.10.2019) Sídlo: Staré Grunty 18 Bratislava -
--- IČO: 52 651 894 (od: 01.10.2019) De
--- Spoločníci: 0100 Ventures s. r. o. IČO: 50 209
… [1353 more characters]
```
</details>

→ `Bash` — Check BinarBase ORSR for ZGC Fund I
```sh
S=[tmp] u="https://www.orsr.sk/vypis.asp?ID=621204&SID=2&P=1"; $S/pg get "$u" 10 >/dev/null; $S/pg grep "$u" "(Obchodné meno: .{0,60}|ZGC.{0,170})" 0; u="https://www.orsr.sk/vypis.asp?ID=621204&SID=2&P=0"; $S/pg get "$u" 10 >/dev/null; $S/pg grep "$u" "ZGC.{0,170}" 0
```

<details><summary>result</summary>

```
5 hits (status 200, 4881 chars)
--- Obchodné meno: BinarBase s. r. o. (od: 20.05.2022) Sídlo: Staré Grunty 6347
--- ZGC Fund I., s.r.o. IČO: 52 768 058 Staromestská 7830/3 Bratislava - mestská časť Staré Mesto 811 03 (od: 08.02.2023 do: 31.10.2024) Peter Augustín (od: 01.11.2024) ZGC Fund
--- ZGC Fund I., s.r.o. Vklad: 3 161 EUR ( peňažný vklad ) Splatené: 3 161 EUR (od: 01.11.2024) START GUIDE ONE, a.s. Vklad: 1 798 EUR ( peňažný vklad ) Splatené: 1 798 EUR (od:
--- ZGC Fund I., s.r.o. Vklad: 750 EUR ( peňažný vklad ) Splatené: 750 EUR (od: 08.02.2023 do: 02.08.2023) Tomáš Tiefenbach Vklad: 750 EUR ( peňažný vklad ) Splatené: 750 EUR (o
--- ZGC Fund I., s.r.o. Vklad: 3 000 EUR ( peňažný vklad ) Splatené: 3 000 EUR (od: 03.08.2023 do: 31.10.2024) Štatutárny orgán: konatelia (od: 20.05.2022) Daniel Janiga Vznik f
2 hits (status 200, 2839 chars)
--- ZGC Fund I., s.r.o. IČO: 52 768 058 Staré Grunty 18 Bratislava - mestská časť Staré Mesto 841 04 (od: 01.11.2024) START GUIDE ONE, a.s. Karla Engliše 3201/6 Praha 150 00 Čes
--- ZGC Fund I., s.r.o. Vklad: 3 161 EUR ( peňažný vklad ) Splatené: 3 161 EUR (od: 01.11.2024) START GUIDE ONE, a.s. Vklad: 1 798 EUR ( peňažný vklad ) Splatené: 1 798 EUR (od:
```
</details>

→ `Bash` — Fetch Reno and cc.cz 0100 articles
```sh
S=[tmp] u="https://www.wamda.com/2025/12/uae-reno-raises-4-million-equity-debt-round"; $S/pg get "$u" 10|head -1; $S/pg grep "$u" "Zero 100.{0,100}" 300 | head; u="https://cc.cz/podporili-nejvetsi-startupove-nadeje-na-slovensku-s-novym-fondem-maji-i-pro-ceske-firmy-15-miliardy/"; $S/pg get "$u" 10|head -1; $S/pg grep "$u" "(60 milion|23 milion|Kypr|Kyp|Dubaj).{0,200}" 200 | head
```

<details><summary>result</summary>

```
{"url": "https://www.wamda.com/2025/12/uae-reno-raises-4-million-equity-debt-round", "status": 200, "final_url": "https://www.wamda.com/2025/12/uae-reno-raises-4-million-equity-debt-round", "ctype": "text/html; charset=UTF-8", "chars": 8948}
2 hits (status 200, 8948 chars)
--- Thought Leadership Research Events Wamda Capital Partner projects About Contact عربي عربي UAE's Reno raises $4 million in equity-debt round News • 04 December, 2025 Edit Arabic UAE-based home renovation tech platform Reno has raised $4 million in equity and debt, led by Sanabil 500, Hub71, Plus VC, Zero 100 VC, FlyerOne Ventures, Sandstorm VC, AngelSpark and Swiss Founders Fund. Founded in 2024 by Marc Michel, Amr Hosny and Farah Karabeg, Reno is the all-in-one, end-to-end interior design and renovation platform for residential and commercial projects. With this investment, Reno plans to expand its footprint across the GCC, scale its technology capabilities, and continue refining the renovation expe
--- e supports the launch of Reno’s new app in early 2026, introducing real-time AI-powered design, instant budget estimates, and an intelligent materials engine that gives customers absolute clarity from the very first step of their renovation journey. The round was led by 500 Sanabil, Hub71, Plus VC, Zero 100 VC, FlyerOne Ventures, Sandstorm VC, AngelSpark and Swiss Founders Fund. The investment will fuel Reno’s expansion across the UAE and GCC, reinforcing its mission to simplify and streamline the renova
… [2990 more characters]
```
</details>

→ `Bash` — Fetch SIH pages for Zero Gravity and Vision Ventures
```sh
S=[tmp] for u in "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/zero-gravity-capital-kapitalova-investicia" "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/vision-ventures-kapitalova-investicia"; do $S/pg get "$u" 1500; done
```

<details><summary>result</summary>

```
{"url": "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/zero-gravity-capital-kapitalova-investicia", "status": 200, "final_url": "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/zero-gravity-capital-kapitalova-investicia", "ctype": "text/html; charset=UTF-8", "chars": 1033}
Zero Gravity Capital | Slovak Investment Holding, a. s.
Zero Gravity Capital
Slovak Investment Holding is an investor in the fund managed by Zero Gravity Capital, which carries full responsibility for its governance and the implementation of its investment strategy. The fund was established as a fixed-term investment vehicle with an expected 10-year term, initiating its activities in 2020 and closing its investment window in December 2023.
Throughout the investment period, capital was directed primarily toward early-stage startups, focusing on companies within five years of their launch, as well as growth-oriented micro and small enterprises. The fund's allocations enhanced the development of innovative solutions and catalysed new entrepreneurial activities in Slovakia.
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
{"url": "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/vision-ventures-kapitalova-investicia", "st
… [1251 more characters]
```
</details>

→ `Bash` — Fetch ZAKA VC homepage
```sh
S=[tmp] $S/pg get "https://zaka.vc/" 8000
```

<details><summary>result</summary>

```
{"url": "https://zaka.vc/", "status": 200, "final_url": "https://zaka.vc/", "ctype": "text/html; charset=UTF-8", "chars": 5041}
ZAKA - ZAKA VC
Skip to content
Home
About
Team
Portfolio
Co-Investors
News
Jobs
Contact
Submit pitch deck
Submit pitch deck
Home
About
Team
Portfolio
Co-Investors
News
Jobs
Contact
E-mail is copied
Founders backed by
entrepreneurs
We are a seed & pre-seed VC fund, investing mainly in the US and Europe. Especially looking for startups in the Health & Biotech and Industrial Tech verticals.
Read our story
97
Companies invested totally
5
Exits
1
Unicorn
17M
Current fund size
Fund size
Companies
Family office
5M
5M
invested
34
Fund 1
17M
8M
invested
46
One of the best Healthcare & Life Sciences portfolios in continental Europe.
Check it out!
Sillicon Valley, London, Prague, Bratislava
We seek entrepreneurs with global ambition wherever they are and support them by creating a bridge between North America and Europe.
Portfolio
Portfolio
Portfolio
There's already 97 companies across 5 continents that we believe in
San Francisco, CA
United States
WonderTx
Extrapolative AI to unlock first-in-class drugs
Anywhere
Is this you?
Ann Arbor, MI
United States
Aerogen Systems
Modernizing chip manufacturing infrastructure
London
United Kingdom
FinalDose
Programmable DNA drug destroying all cancers, unlocking 80% of targets
San Francisco, CA
United States
PerfectBit
Correct by construction training data for frontier AI labs
Mountain View, CA
United States
Human Archive

… [3669 more characters]
```
</details>

→ `Bash` — Fetch cc.cz ZAKA article and ORSR search
```sh
S=[tmp] u="https://cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milionu-korun/"; $S/pg get "$u" 10|head -1; $S/pg grep "$u" "(SICAV|sídl|San Francisc|Bratislav|15 milion|10,5|Kasper|Zálešák|slovens).{0,200}" 150 | head -12; cd ../shared; python3 orsr.py search "ZAKA"
```

<details><summary>result</summary>

```
Exit code 2
{"url": "https://cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milionu-korun/", "status": 200, "final_url": "https://cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milionu-korun/", "ctype": "text/html; charset=UTF-8", "chars": 8782}
6 hits (status 200, 8781 chars)
--- e je na Googlu častěji. Sledovat Upřednostnit Startupová Zaka VC vznikla jako rodinný fond, v němž své síly spojily rodiny úspěšných podnikatelů Jána Kaspera a Petera Zálešáka, kteří se svým týmem během čtyř let podpořili přes padesát nadějných startupů. Teď fond začíná novou kapitolu, v níž se poprvé otevřel také externím investorům, a cílí na celkovou částku 15 milionů eur (přibližně 380 milionů korun), z čehož již 10,5 milionu eur (265 milionů korun) nasbíral. V začátcích se Zaka soustředila hlavně
--- odpořili přes padesát nadějných startupů. Teď fond začíná novou kapitolu, v níž se poprvé otevřel také externím investorům, a cílí na celkovou částku 15 milionů eur (přibližně 380 milionů korun), z čehož již 10,5 milionu eur (265 milionů korun) nasbíral. V začátcích se Zaka soustředila hlavně na region střední a východní Evropy, postupně ale svůj záběr rozšířila také do dalších zemí včetně Velké Británie a Spojených států, kde podporuje hlavně startupy zdejších zakladatelů. Fond se řadí mezi vůbec nejakt
--- bec nejaktivnější svého druhu, jen loni podpořil přes dvacítku nadějných firem . Celkem jde o 55 startupů a proinvestovaných téměř 280 milionů 
… [2177 more characters]
```
</details>

→ `Bash` — Search ORSR for ZAKA and fetch startitup article
```sh
O=[tmp] python3 $O search "ZAKA"; python3 $O search "Zaka VC"; S=[tmp] u="https://www.startitup.sk/?p=1130105"; $S/pg get "$u" 10|head -1; $S/pg grep "$u" "(San Francisc|sídl|slovensk[ýé] fond|Búza|Bratislav).{0,200}" 150 | head -8
```

<details><summary>result</summary>

```
Za Kasárňou 1 s. r. o. | https://www.orsr.sk/vypis.asp?ID=697220&SID=2&P=0
ZAK - AGRA, s.r.o. | https://www.orsr.sk/vypis.asp?ID=345378&SID=7&P=0
ZAKA colours, s. r. o. | https://www.orsr.sk/vypis.asp?ID=770797&SID=7&P=0
ZAKA CONSTRUCTION, s. r. o. | https://www.orsr.sk/vypis.asp?ID=514871&SID=3&P=0
zaka kp, s. r. o. | https://www.orsr.sk/vypis.asp?ID=687946&SID=5&P=0
ZaKa Slovakia, s. r. o. | https://www.orsr.sk/vypis.asp?ID=347235&SID=2&P=0
ZAKA Startup 1 j.s.a. | https://www.orsr.sk/vypis.asp?ID=515739&SID=2&P=0
ZAKA Startup 10 j. s. a. | https://www.orsr.sk/vypis.asp?ID=646317&SID=2&P=0
ZAKA Startup 11 j. s. a. | https://www.orsr.sk/vypis.asp?ID=646303&SID=2&P=0
ZAKA Startup 12 j. s. a. | https://www.orsr.sk/vypis.asp?ID=646308&SID=2&P=0
ZAKA Startup 13 j. s. a. | https://www.orsr.sk/vypis.asp?ID=646314&SID=2&P=0
ZAKA Startup 14 j. s. a. | https://www.orsr.sk/vypis.asp?ID=646304&SID=2&P=0
ZAKA Startup 15 j. s. a. | https://www.orsr.sk/vypis.asp?ID=646305&SID=2&P=0
ZAKA Startup 16 j. s. a. | https://www.orsr.sk/vypis.asp?ID=645000&SID=2&P=0
ZAKA Startup 17 j. s. a. | https://www.orsr.sk/vypis.asp?ID=646307&SID=2&P=0
ZAKA Startup 18 j. s. a. | https://www.orsr.sk/vypis.asp?ID=646306&SID=2&P=0
ZAKA Startup 19 j. s. a. | https://www.orsr.sk/vypis.asp?ID=645001&SID=2&P=0
ZAKA Startup 2 j.s.a. | https://www.orsr.sk/vypis.asp?ID=526365&SID=2&P=0
ZAKA Startup 20 j. s. a. | https://www.orsr.sk/vypis.asp?ID=646301&SID=2&P=0
ZAKA Startup 3 j.s.a. | https://www.orsr.sk/vypis.asp?ID=5
… [3870 more characters]
```
</details>

→ `Bash` — Read ZAKA Startup j.s.a. ORSR extracts
```sh
S=[tmp] for u in "https://www.orsr.sk/vypis.asp?ID=515739&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=645000&SID=2&P=0"; do $S/pg get "$u" 10 >/dev/null; $S/pg text "$u" 400 2600 | tr '\n' ' '; echo; echo; done
```

<details><summary>result</summary>

```
á 4775/7 Bratislava - mestská časť Staré Mesto 811 02 (od: 16.05.2020) IČO: 52 994 490 (od: 16.05.2020) Deň zápisu: 16.05.2020 (od: 16.05.2020) Právna forma: Jednoduchá spoločnosť na akcie (od: 16.05.2020) Predmet podnikania (činnosti): Prenájom nehnuteľností bez poskytovania iných než základných služieb spojených s prenájmom (od: 16.05.2020) Výskum a vývoj v oblasti prírodných, technických, spoločenských a humanitných vied (od: 16.05.2020) Uskutočňovanie stavieb a ich zmien (od: 16.05.2020) Prípravné práce k realizácii stavby (od: 16.05.2020) Dokončovacie stavebné práce pri realizácii exteriérov a interiérov (od: 16.05.2020) Sprostredkovateľská činnosť v oblasti obchodu, služieb, výroby (od: 16.05.2020) Kúpa tovaru na účely jeho predaja konečnému spotrebiteľovi (maloobchod) alebo iným prevádzkovateľom živnosti (veľkoobchod) (od: 16.05.2020) Skladovanie a pomocné činnosti v doprave (od: 16.05.2020) Ubytovacie služby s poskytovaním prípravy a predaja jedál, nápojov a polotovarov ubytovaným hosťom v ubytovacích zariadeniach s kapacitou do 10 lôžok (od: 16.05.2020) Ubytovacie služby bez poskytovania pohostinských činností (od: 16.05.2020) Poskytovanie obslužných služieb pri kultúrnych a iných spoločenských podujatiach (od: 16.05.2020) Vydavateľská činnosť, polygrafická výroba a knihárske práce (od: 16.05.2020) Počítačové služby a služby súvisiace s počítačovým spracovaním údajov (od: 16.05.2020) Poskytovanie úverov alebo pôžičiek z peňažných zdrojov získaných výlučne bez verejne
… [3702 more characters]
```
</details>

→ `Bash` — Get ZAKA SPV statutory body and notes
```sh
S=[tmp] for u in "https://www.orsr.sk/vypis.asp?ID=515739&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=645000&SID=2&P=0"; do $S/pg grep "$u" "(Obchodné meno: .{0,50}|Sídlo: .{0,60}|Štatutárny orgán:.{0,300}|Akcionár.{0,200}|Ďalšie právne.{0,300})" 0; done
```

<details><summary>result</summary>

```
3 hits (status 200, 4881 chars)
--- Obchodné meno: ZAKA Startup 1 j.s.a. (od: 16.05.2020) Sídlo: Révo
--- Štatutárny orgán: predstavenstvo (od: 16.05.2020) Bc. Karolína Kasperová - Člen predstavenstva Dátum narodenia: 09.05.1995 Vznik funkcie: 04.10.2022 (od: 03.01.2023) Samuel Zálešák - Člen predstavenstva Dátum narodenia: 23.07.1998 Vznik funkcie: 03.04.2023 (od: 19.04.2023) Konanie menom spoločnosti: V mene spoločnos
--- Akcionár: ZAKA VC I, osoba rizikového kapitálu, a.s. Panská 854/2 Praha 1 - Nové Město 110 00 Česká republika (od: 28.02.2025) Dozorná rada: Ing. Daniel Báchor Dátum narodenia: 05.04.1990 Vznik funkcie: 16.05
2 hits (status 200, 5262 chars)
--- Obchodné meno: ZAKA Startup 16 j. s. a. (od: 16.08.2022) Sídlo: R
--- Štatutárny orgán: predstavenstvo (od: 16.08.2022) Bc. Karolína Kasperová - Predseda predstavenstva Dátum narodenia: 09.05.1995 Vznik funkcie: 09.02.2023 (od: 17.03.2023) Ján Kasper ml. - Člen predstavenstva Dátum narodenia: 25.07.1999 Vznik funkcie: 09.02.2023 (od: 17.03.2023) Konanie menom spoločnosti: V mene Spolo
```
</details>

→ `Bash` — Fetch ZAKA contact and about pages
```sh
S=[tmp] for u in "https://zaka.vc/contact/" "https://zaka.vc/about/"; do $S/pg get "$u" 10|head -1; $S/pg grep "$u" "(Bratislava|Prague|Praha|San Francisco|a\.s\.|s\.r\.o\.|Inc\.|LLC|IČ).{0,150}" 100 | head -8; done
```

<details><summary>result</summary>

```
{"url": "https://zaka.vc/contact/", "status": 404, "final_url": "https://zaka.vc/contact/", "ctype": "text/html; charset=UTF-8", "chars": 460}
1 hits (status 404, 460 chars)
--- You can return to our homepage by clicking here . Back to top hey@zaka.vc Silicon Valley / London / Prague / Bratislava Home About Team Portfolio Co-Investors News Jobs Privacy Policy hey@zaka.vc Back to top
{"url": "https://zaka.vc/about/", "status": 404, "final_url": "https://zaka.vc/about/", "ctype": "text/html; charset=UTF-8", "chars": 460}
1 hits (status 404, 460 chars)
--- You can return to our homepage by clicking here . Back to top hey@zaka.vc Silicon Valley / London / Prague / Bratislava Home About Team Portfolio Co-Investors News Jobs Privacy Policy hey@zaka.vc Back to top
```
</details>

→ `Bash` — List ZAKA site links
```sh
S=[tmp] grep -oE 'href="https://zaka.vc/[^"]*"' $S/cache/$(python3 -c "import hashlib;print(hashlib.sha1(b'https://zaka.vc/').hexdigest())").raw | sort -u | head -30
```

<details><summary>result</summary>

```
href="https://zaka.vc/"
href="https://zaka.vc/co-investors/"
href="https://zaka.vc/jobs/"
href="https://zaka.vc/mrna-is-still-made-the-1984-way-it-was-not-built-for-the-drugs-coming-next/"
href="https://zaka.vc/news/"
href="https://zaka.vc/our-story/"
href="https://zaka.vc/portfolio/"
href="https://zaka.vc/portfolio/#industry=80"
href="https://zaka.vc/portfolio/#portfolio"
href="https://zaka.vc/privacy-policy/"
href="https://zaka.vc/sensible-biotechnologies-raises-47m-why-we-backed-them-early-and-why-its-personal-for-us/"
href="https://zaka.vc/submit-pitchdeck/"
href="https://zaka.vc/team/"
href="https://zaka.vc/wp-content/themes/zaka/assets/img/favicon/android-icon-192x192.png"
href="https://zaka.vc/wp-content/themes/zaka/assets/img/favicon/apple-icon-114x114.png"
href="https://zaka.vc/wp-content/themes/zaka/assets/img/favicon/apple-icon-120x120.png"
href="https://zaka.vc/wp-content/themes/zaka/assets/img/favicon/apple-icon-144x144.png"
href="https://zaka.vc/wp-content/themes/zaka/assets/img/favicon/apple-icon-152x152.png"
href="https://zaka.vc/wp-content/themes/zaka/assets/img/favicon/apple-icon-180x180.png"
href="https://zaka.vc/wp-content/themes/zaka/assets/img/favicon/apple-icon-57x57.png"
href="https://zaka.vc/wp-content/themes/zaka/assets/img/favicon/apple-icon-60x60.png"
href="https://zaka.vc/wp-content/themes/zaka/assets/img/favicon/apple-icon-72x72.png"
href="https://zaka.vc/wp-content/themes/zaka/assets/img/favicon/apple-icon-76x76.png"
href="https://zaka.vc/wp-con
… [375 more characters]
```
</details>

→ `Bash` — Fetch ZAKA privacy, team and Sensible pages
```sh
S=[tmp] for u in "https://zaka.vc/privacy-policy/" "https://zaka.vc/team/" "https://zaka.vc/sensible-biotechnologies-raises-47m-why-we-backed-them-early-and-why-its-personal-for-us/"; do $S/pg get "$u" 10|head -1; $S/pg grep "$u" "(Bratislava|Praha|Prague|a\.s\.|IČO|ID No|registered|seed|first check|invested|backed).{0,180}" 120 | head -6; done
```

<details><summary>result</summary>

```
{"url": "https://zaka.vc/privacy-policy/", "status": 200, "final_url": "https://zaka.vc/privacy-policy/", "ctype": "text/html; charset=UTF-8", "chars": 11347}
4 hits (status 200, 11346 chars)
--- cy Policy Who we are The operator of the website and personal data is the company ZAKA VC I, osoba rizikového kapitálu, a.s., with its registered office at Italská 2581/67, 120 00 Prague 2, ID number: 215 14 992, registered in the Commercial Register of the Municipal Court Prague I, File no. B 28844 (“Operator”). The operator hereby provides you with information in accordance with Act no. 452/2021 Coll. on electronic com
--- ons regarding the protection of personal data, or cookies, contact us at hey@zaka.vc. Basic information about ZAKA VC I a.s.: ZAKA VC I, osoba rizikového kapitálu, a.s., ID: 215 14 992, with registered office at Panská 854/2, Nové Město, 110 00 Prague 1, registered in the commercial register maintained by the Municipal Court in Prague under file no. trade mark B 28844 (“ZAKA”), is an alternative fund by a so-called risk 
--- t Panská 854/2, Nové Město, 110 00 Prague 1, registered in the commercial register maintained by the Municipal Court in Prague under file no. trade mark B 28844 (“ZAKA”), is an alternative fund by a so-called risk capital entity registered with the Czech National Bank (“ČNB”), as a person entered in the list of persons carrying out property management comparable to management in the sense of § 15 paragraph 1 of Act no. 240
---  does not super
… [4407 more characters]
```
</details>

→ `Bash` — Read G-Force ORSR extracts
```sh
S=[tmp] for u in "https://www.orsr.sk/vypis.asp?ID=608015&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=659572&SID=2&P=0"; do $S/pg get "$u" 10 >/dev/null; $S/pg grep "$u" "(Obchodné meno: .{0,60}|Sídlo: .{0,80}|IČO: .{0,30}|Deň zápisu: .{0,15}|Spoločníci:.{0,700}|Akcionár.{0,300}|Predmet podnikania.{0,300})" 0; echo; done
```

<details><summary>result</summary>

```
4 hits (status 200, 3600 chars)
--- Obchodné meno: G-Force, s. r. o. (od: 12.01.2021) Sídlo: Mlynské nivy 5 Bra
--- IČO: 53 527 798 (od: 12.01.2021) De
--- Predmet podnikania (činnosti): Sprostredkovanie poskytovania úverov alebo pôžičiek z peňažných zdrojov získaných výlučne bez verejnej výzvy a bez verejnej ponuky majetkových hodnôt (od: 18.09.2021) Poskytovanie úverov alebo pôžičiek z peňažných zdrojov získaných výlučne bez verejnej výzvy a bez verejnej ponuky majetk
--- Spoločníci: Péter Küllöi Dátum narodenia: 10.03.1960 (od: 11.02.2022) Founders Factory Limited Northcliffe House, Young Street London W8 5EH Spojené kráľovstvo Veľkej Británie a Severného Írska Iné identifikačné číslo: 09564631 (od: 11.02.2022) GRANPOOL Hungary Kft. Aradi vértanúk tere 1. Esztergom 2500 Maďarsko Iné identifikačné číslo: 1109025457 (od: 11.02.2022) Global Connect Corporation SK s. r. o. IČO: 46 830 243 Landererova 12 Bratislava - mestská časť Staré Mesto 811 09 (od: 22.05.2025) BRAUN HOLDING, s. r. o. IČO: 44 443 200 Pribinova 4 Bratislava - mestská časť Staré Mesto 811 09 (od: 22.05.2025) Výška vkladu každého spoločníka: Péter Küllöi Vklad: 7 875 EUR ( peňažný vklad ) Splatené: 7 875 E

3 hits (status 200, 2845 chars)
--- Obchodné meno: G-Force Fund, j. s. a. (od: 16.02.2021) Sídlo: Mlynské nivy 
--- IČO: 53 588 398 (od: 16.02.2021) De
--- Predmet podnikania (činnosti): Činnosť podnikateľských, organizačných a ekonomických poradcov (od: 16.02.2021) Poskytovanie úverov alebo pôžičiek z peňa
… [166 more characters]
```
</details>

→ `WebSearch` "G-Force" climate fund Founders Factory Marian Gazdik investment 2025

<details><summary>result</summary>

```
Web search results for query: ""G-Force" climate fund Founders Factory Marian Gazdik investment 2025"

Links: [{"title":"investing in the climate revolution","url":"https://foundersfactory.substack.com/p/investing-in-the-climate-revolution"},{"title":"marian gazdik","url":"https://www.vcsheet.com/who/marian-gazdik"},{"title":"Header Hero logoHeader Hero logo","url":"https://foundersfactory.com/g-force/"},{"title":"founders factory g force launches sustainability seed program","url":"https://siliconcanals.com/founders-factory-g-force-launches-sustainability-seed-program/"},{"title":"climate tech what have we learned","url":"https://foundersfactory.substack.com/p/climate-tech-what-have-we-learned"},{"title":"Who we are","url":"https://g-force-fund-ii.seedrs.com"},{"title":"Seedrs Offers Investors Access to Green Fund by G Force","url":"https://www.crowdfundinsider.com/?p=214476"},{"title":"Seedrs Offers Investors Access to Green Fund by G Force","url":"https://www.crowdfundinsider.com/2023/10/214476-seedrs-offers-investors-access-to-green-fund-by-g-force/"},{"title":"G-Force team","url":"https://techcrunch.com/2021/09/06/founders-factory-and-g-force-launch-seed-program-for-climate-focused-startups/amp/"},{"title":"marian gazdik fd9fc","url":"https://www.vcsheet.com/who/marian-gazdik-fd9fc"}]

The search didn't turn up any 2025-specific investment news for Marian Gazdik or G-Force. Most results date from 2021 to 2023, so treat them as background rather than current activity.

- 
… [1352 more characters]
```
</details>

→ `Bash` — Fetch G-Force sources
```sh
S=[tmp] for u in "https://foundersfactory.com/g-force/" "https://g-force-fund-ii.seedrs.com" "https://www.crowdfundinsider.com/2023/10/214476-seedrs-offers-investors-access-to-green-fund-by-g-force/" "https://www.caplight.com/investor/g-force"; do $S/pg get "$u" 10|head -1; $S/pg grep "$u" "(Bratislava|Slovak|20 million|€20|invest(ed|ment) in|Enzidia|2025|2026).{0,160}" 120 | head -6; done
```

<details><summary>result</summary>

```
{"url": "https://foundersfactory.com/g-force/", "status": 200, "final_url": "https://foundersfactory.com/g-force/", "ctype": "text/html", "chars": 4586}
2 hits (status 200, 4586 chars)
--- -satellite data Environment ESG 360 ESG 360 / Pre-Seed The ESG platform designed for global value chains Sustainability Enzidia Enzidia / Pre-Seed Dramatically accelerating enzyme optimisation, paving the way for faster, more efficient, and more sustainable industrial bioprocesses. Bioindustry Brightly Brightly / Pre-Seed Creating high-integrity carbon credits for food recovery organisations, tied to avo
--- ights Subscribe to our newsletter Monthly stories and insights from leading founders, investors and our team. Sign up © 2026 Founders Factory Ltd. All rights reserved Code of conduct
{"url": "https://g-force-fund-ii.seedrs.com", "error": "SSLError(MaxRetryError(\"HTTPSConnectionPool(host='g-force-fund-ii.seedrs.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError(1, '[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] ssl/tls alert handshake failure (_ssl.c:1082)')))\"))", "status": 0, "ctype": "", "final_url": "https://g-force-fund-ii.seedrs.com/", "via": "curl", "chars": 0}
0 hits (status 0, 0 chars)
{"url": "https://www.crowdfundinsider.com/2023/10/214476-seedrs-offers-investors-access-to-green-fund-by-g-force/", "status": 200, "final_url": "https://www.crowdfundinsider.com/2023/10/214476-seedrs-offers-investors-access-to-green-fund-by-g-force/", "ctype": "text/html; chars
… [3939 more characters]
```
</details>

→ `Bash` — Fetch g-force.earth and Founders Factory G-Force page
```sh
S=[tmp] $S/pg get "https://g-force.earth/" 4000; $S/pg text "https://foundersfactory.com/g-force/" 0 2500
```

<details><summary>result</summary>

```
{"url": "https://g-force.earth/", "error": "ConnectionError(MaxRetryError('HTTPSConnectionPool(host=\\'g-force.earth\\', port=443): Max retries exceeded with url: / (Caused by NameResolutionError(\"HTTPSConnection(host=\\'g-force.earth\\', port=443): Failed to resolve \\'g-force.earth\\' ([Errno 8] nodename nor servname provided, or not known)\"))'))", "status": 0, "ctype": "", "final_url": "https://g-force.earth/", "via": "curl", "chars": 0}

G-Force Sustainability Seed Program - Founders Factory
Founders
Venture Studio
Accelerator
Venture Funds
Partners
Focus areas
Fintech
Industrials
Health
Deep Tech
Portfolio
Careers
Company
About us
Team
Our partners
Stories & Insights
Apply
ACCELERATOR - Climate
G-Force Climate Seed Program
Applications open
€250k investment • 6 months operational support • Remote
Apply now
program overview
Backing stellar founders who are helping to accelerate to a net zero future
We're bringing together the best minds to support entrepreneurs taking on this global climate challenge.
Our Climate Seed Program is a collaboration between Founders Factory and
G-Force
- including investors Boris Zeleny (serial entrepreneur and key figure behind AVG, sold to AVAST for $1.4bn), Marian Gazdik (Startup Grind), Peter Kulloi & Miklos Kobor.
Learn more
program overview
Backing stellar founders who are helping to accelerate to a net zero future
We're bringing together the best minds to support entrepreneurs taking on this global climate challenge.
Our Climate Seed 
… [1448 more characters]
```
</details>

→ `WebSearch` Enzidia pre-seed G-Force Founders Factory enzyme

<details><summary>result</summary>

```
Web search results for query: "Enzidia pre-seed G-Force Founders Factory enzyme"

Links: [{"title":"Production of enzyme products and raw feed materials using grain seeds","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6063431"},{"title":"investing in enzidia","url":"https://foundersfactory.com/articles/investing-in-enzidia/"},{"title":"thehub.io","url":"https://thehub.io/startups/enzidia"},{"title":"www.vcbacked.co","url":"https://www.vcbacked.co/company/enzidia"},{"title":"Total Funding","url":"https://www.crunchbase.com/organization/enzidia"},{"title":"startup-seeker.com","url":"https://startup-seeker.com/company/enzidia~com"},{"title":"www.premieralts.com","url":"https://www.premieralts.com/companies/enzidia"},{"title":"NEWCaplight raises a $16M Series A, led by BlackRock and Fin Capital →","url":"https://www.caplight.com/company/enzidia"},{"title":"US6063431A - Production of enzyme products and raw feed materials using grain seeds - Google Patents","url":"https://patents.google.com/patent/US6063431"}]

Enzidia is a Danish enzyme-engineering startup, and the results support a Founders Factory investment, but they don't clearly confirm the round details.

- **Company:** Enzidia builds a platform that speeds up enzyme optimization. It provides a high-throughput enzyme engineering platform for discovering and optimizing biocatalysts for biomanufacturing. It was founded in 2024 and is based in Denmark, with 1-10 employees.
- **Founders Factory:** A Fo
… [1018 more characters]
```
</details>

→ `Bash` — Fetch Founders Factory Enzidia article
```sh
S=[tmp] u="https://foundersfactory.com/articles/investing-in-enzidia/"; $S/pg get "$u" 10|head -1; $S/pg grep "$u" "(G-Force|March|2025|invest).{0,200}" 150 | head -8
```

<details><summary>result</summary>

```
{"url": "https://foundersfactory.com/articles/investing-in-enzidia/", "status": 200, "final_url": "https://foundersfactory.com/articles/investing-in-enzidia/", "ctype": "text/html", "chars": 4355}
6 hits (status 200, 4355 chars)
--- Investing in Enzidia—leading the bioeconomy revolution with enzymes - Founders Factory Founders Venture Studio Accelerator Venture Funds Partners Focus areas Fintech Industrials Health Deep Tech Portfolio Careers Company About us Team Our partners Stories & Insights Apply Share We’re excited to announce our latest G-Force climate investment— Enzidia . Th
--- Industrials Health Deep Tech Portfolio Careers Company About us Team Our partners Stories & Insights Apply Share We’re excited to announce our latest G-Force climate investment— Enzidia . The problem Enzymes are key to unlocking the radical transformation of the chemical manufacturing industry as they look to become cleaner, more renewable, and less carbon intensive. They are the backbone of numerous bio-industrial solutions, in manufacturing and chemistry (bio-based chemicals and bio-plastics), agricu
--- rdisk Foundation Center for Biosustainability. This research ultimately led him to build the technology platform behind Enzidia. Why we’re excited to invest Marian Gazdik , partner at G-Force: “Jinbei, Enzidia’s founder, is clearly mission driven and unapologetically ambitious with his unique approach of making the enzymes industry orders of magnitude more efficient. Enzidia isn’t just shapi
… [1385 more characters]
```
</details>

→ `Bash` — Find Enzidia article publication date
```sh
S=[tmp] f=$S/cache/$(python3 -c "import hashlib;print(hashlib.sha1(b'https://foundersfactory.com/articles/investing-in-enzidia/').hexdigest())").raw; grep -oE '(datePublished|published_time|dateCreated|"date")[^,]{0,50}|20(24|25)-[0-9]{2}-[0-9]{2}' $f | sort | uniq -c | head; grep -oE '[A-Z][a-z]+ [0-9]{1,2}, 202[45]|[0-9]{1,2} [A-Z][a-z]+ 202[45]' $f | head
```

<details><summary>result</summary>

```
(Bash completed with no output)
```
</details>

→ `Bash` — Check Wayback captures of Enzidia article
```sh
S=[tmp] curl -s "https://web.archive.org/cdx/search/cdx?url=foundersfactory.com/articles/investing-in-enzidia/&output=json&limit=5" -A "investordb/0.1"; echo; f=$S/cache/$(python3 -c "import hashlib;print(hashlib.sha1(b'https://foundersfactory.com/articles/investing-in-enzidia/').hexdigest())").raw; grep -oiE '(published|modified|updated)[^<]{0,80}' $f | head
```

<details><summary>result</summary>

```
[["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
["com,foundersfactory)/articles/investing-in-enzidia","20250327124335","https://foundersfactory.com/articles/investing-in-enzidia/","text/html","200","PC3TMSZ76VFVZL3OLSKUT2BTQBBGRNJ3","39300"],
["com,foundersfactory)/articles/investing-in-enzidia","20250719170755","https://foundersfactory.com/articles/investing-in-enzidia/","text/html","200","W5T6FCCBWLNJNYZEW4WSU2ZGYRNW2YKH","39339"],
["com,foundersfactory)/articles/investing-in-enzidia","20251110185910","https://foundersfactory.com/articles/investing-in-enzidia/","text/html","200","BL63XZE5E5RAKE2UAP5AP7GVZ23Q7HSQ","40076"]]
```
</details>

→ `Bash` — Fetch archived Enzidia article for date
```sh
S=[tmp] u="https://web.archive.org/web/20250327124335id_/https://foundersfactory.com/articles/investing-in-enzidia/"; $S/pg get "$u" 10 | head -1; $S/pg grep "$u" "(202[45]|latest G-Force).{0,120}" 80 | head; f=$S/cache/$(python3 -c "import hashlib,sys;print(hashlib.sha1(sys.argv[1].encode()).hexdigest())" "$u").raw; grep -oE '20(24|25)-[0-9]{2}-[0-9]{2}[T0-9:.+Z-]*' $f | sort | uniq -c | head
```

<details><summary>result</summary>

```
{"url": "https://web.archive.org/web/20250327124335id_/https://foundersfactory.com/articles/investing-in-enzidia/", "status": 429, "final_url": "https://web.archive.org/web/20250327124335id_/https://foundersfactory.com/articles/investing-in-enzidia/", "ctype": "text/html", "chars": 605}
0 hits (status 429, 603 chars)
```
</details>

→ `Bash` — Download archived Enzidia article with archive UA
```sh
S=[tmp] mkdir -p $S/dl; curl -s -A "investordb/0.1 (source verification; 1 req/s)" "https://web.archive.org/web/20250327124335id_/https://foundersfactory.com/articles/investing-in-enzidia/" -o $S/dl/enz.html; wc -c $S/dl/enz.html; grep -oE '20(24|25)-[0-9]{2}-[0-9]{2}[T0-9:.+Z-]*|[A-Z][a-z]+ [0-9]{1,2}(st|nd|rd|th)?,? 202[45]|[0-9]{1,2} [A-Z][a-z]+ 202[45]' $S/dl/enz.html | sort | uniq -c | head
```

<details><summary>result</summary>

```
  185968 [tmp]
   1 2025-02-20
   1 2025-03-11
   1 2025-03-17
   1 March 11th 2025
```
</details>

→ `Bash` — Show context of March 11th 2025 in archived page
```sh
S=[tmp] grep -oE '.{200}March 11th 2025.{100}' $S/dl/enz.html | sed 's/<[^>]*>/ /g'; grep -oE '.{80}2025-03-11.{80}' $S/dl/enz.html
```

<details><summary>result</summary>

```
58.large{font-size:0.9rem;}@media screen and (min-width:700px){.css-869e58.large{font-size:1.2rem;}}  Words   Founders Factory  March 11th 2025   /  3 min read    <p class="break-words ff-type overlayOverBkg ff-
db"><p class="font-foundersGrotesk css-15nqg53">factory news</p><time dateTime="2025-03-11 09:00" class="font-foundersGrotesk css-jibw2n"> — <!-- -->16 days ago</time></d
```
</details>

→ `Bash` — Use archive UA in helper and refetch snapshot
```sh
S=[tmp] sed -i '' 's/from investordb.fetch import HEADERS, extract_text  # noqa: E402/from investordb.fetch import HEADERS, _headers, extract_text  # noqa: E402/; s/r = requests.get(url, headers=HEADERS, timeout=40/r = requests.get(url, headers=_headers(url), timeout=40/' $S/bin/pg.py; grep -n "_headers" $S/bin/pg.py; u="https://web.archive.org/web/20250327124335id_/https://foundersfactory.com/articles/investing-in-enzidia/"; $S/pg get "$u" --force 10 | head -1; $S/pg grep "$u" "(March 11th 2025|latest G-Force).{0,80}" 80
```

<details><summary>result</summary>

```
22:from investordb.fetch import HEADERS, _headers, extract_text  # noqa: E402
46:            r = requests.get(url, headers=_headers(url), timeout=40, allow_redirects=True)
{"url": "https://web.archive.org/web/20250327124335id_/https://foundersfactory.com/articles/investing-in-enzidia/", "status": 200, "final_url": "https://web.archive.org/web/20250327124335id_/https://foundersfactory.com/articles/investing-in-enzidia/", "ctype": "text/html", "chars": 5076}
1 hits (status 200, 5075 chars)
--- n Enzidia—leading the bioeconomy revolution with enzymes Words Founders Factory March 11th 2025 / 3 min read We’re excited to announce our latest G-Force climate investment— Enzidia . The problem Enzymes are key to unlocking the radical transformation of
```
</details>

→ `Bash` — Fetch CBIM site and ORSR entries
```sh
S=[tmp] $S/pg get "https://www.cbim.sk/" 5000; O=[tmp] python3 $O brief "CB MDX" | head; python3 $O brief "CB Investment Management" | head -20
```

<details><summary>result</summary>

```
{"url": "https://www.cbim.sk/", "status": 200, "final_url": "https://www.cbim.sk/", "ctype": "text/html; charset=UTF-8", "chars": 2207}
CB Investment Management — Získajte kapitál a znalosti  | Venture Capital
top of page
Crowdberry
CB ESPRI
CB Property Investors
Login
Innovate. Challenge. Grow.
We help you gain capital and know-how for your success.
Submit your pitch
Want to hear more? Sign up for our newsletter.
What are you looking for?
We believe that thriving startups and SMEs are the backbone of Europe’s future prosperity. Our vision is to become a growth catalyst.
Our goal is
your success.
Experience
Capital
Network
Submit your pitch
About us
Since 2015, Crowdberry has been the driving force for investments in startups, SMEs, impact investing and real estate projects in Slovakia and Czechia. Our team has experience in finance management, investment banking and venture capital from all around the world.
​
CB Investment Management Growth One fund was founded in 2019 in order to help seed and pre-seed businesses based in Slovakia.
Meet the team
€23.2M
Fund size
32
Companies
2019
Founded
10
Years lifetime
+ 3 years extension
Venture Stories
DNA ERA
The Slovak biotechnology company specializes in direct genetic analysis of DNA. Its technology can detect 74 carrier diseases and 34 health risks, as well as predispositions for certain sports and optimal nutrition. In 2021, DNA ERA received investment worth 250,000 € from the CB Growth One fund managed by CB Investment Manageme
… [1467 more characters]
```
</details>

→ `Bash` — Search ORSR for CB Growth One fund vehicle
```sh
O=[tmp] for q in "CB Growth" "CB IM" "CB Investment Management Growth" "Growth One"; do echo "## $q"; python3 $O search "$q" | head -8; done
```

<details><summary>result</summary>

```
## CB Growth
CB Growth ONE s. r. o. | https://www.orsr.sk/vypis.asp?ID=497750&SID=2&P=0
## CB IM
NO MATCH
## CB Investment Management Growth
CB Investment Management s. r. o. | https://www.orsr.sk/vypis.asp?ID=482767&SID=2&P=0
## Growth One
NO MATCH
```
</details>

→ `Bash` — Check CBIM portfolio companies in ORSR
```sh
O=[tmp] for q in "3IPK" "Forvio" "altFINS" "DNA ERA"; do echo "## $q"; python3 $O brief "$q" 2>&1| grep -E "^==|IČO|CB Growth" | head -6; done; S=[tmp] u="https://www.orsr.sk/vypis.asp?ID=497750&SID=2&P=0"; $S/pg get "$u" 10 >/dev/null; $S/pg grep "$u" "(Obchodné meno: .{0,50}|Spoločníci:.{0,500})" 0
```

<details><summary>result</summary>

```
## 3IPK
== 3IPK Global s. r. o. | https://www.orsr.sk/vypis.asp?ID=624999&SID=7&P=0
IČO: 54 713 820 | Sídlo: Nitrianska 1835/1, Piešťany 921 01 | zápis: 01.07.2022
Spoločníci: 3IPK, a.s. IČO: 52 001 296 / Nitrianska 1835/1 / Piešťany 921 01 / (od: 01.07.2022) / 
== 3IPK, a.s. | https://www.orsr.sk/vypis.asp?ID=613307&SID=7&P=0
IČO: 52 001 296 | Sídlo: Nitrianska 1835/1, Piešťany 921 01 | zápis: 23.01.2019
## Forvio
== Forvio s. r. o. | https://www.orsr.sk/vypis.asp?ID=610947&SID=4&P=0
IČO: 54 337 739 | Sídlo: Štefániková 16, Košice - mestská časť Staré Mesto 040 01 | zápis: 19.01.2022
## altFINS
== Altfin, s.r.o. | https://www.orsr.sk/vypis.asp?ID=775984&SID=2&P=0
IČO: 48 176 044 | Sídlo: Námestie SNP 7184/22, Bratislava - mestská časť Staré Mesto 811 01 | zápis: 29.05.2015
== altFINS Incentive Systems, s. r. o. | https://www.orsr.sk/vypis.asp?ID=603306&SID=4&P=0
IČO: 54 143 021 | Sídlo: Južná Trieda 48, Košice - mestská časť Juh 040 01 | zápis: 14.10.2021
Spoločníci: altFINS, j. s. a. IČO: 51 781 646 / Námestie slobody 13 / Bratislava - mestská časť Staré Mesto 811 06 / (od: 14.10.2021) / 
== altFINS, j. s. a. | https://www.orsr.sk/vypis.asp?ID=434882&SID=2&P=0
## DNA ERA
== DNA ERA s. r. o. | https://www.orsr.sk/vypis.asp?ID=440332&SID=2&P=0
IČO: 51 860 830 | Sídlo: Karadžičova 8, Bratislava - mestská časť Ružinov 821 08 | zápis: 05.09.2018
2 hits (status 200, 2483 chars)
--- Obchodné meno: CB Growth ONE s. r. o. (od: 09.10.2019) Sídlo: Sta
--- Spoločníci: National Developm
… [482 more characters]
```
</details>

→ `Bash` — Look for CB Growth ONE entries in portfolio ORSR
```sh
S=[tmp] for u in "https://www.orsr.sk/vypis.asp?ID=610947&SID=4&P=1" "https://www.orsr.sk/vypis.asp?ID=440332&SID=2&P=1" "https://www.orsr.sk/vypis.asp?ID=613307&SID=7&P=1"; do $S/pg get "$u" 10 >/dev/null; echo "## $u"; $S/pg grep "$u" "CB Growth.{0,170}" 0; done
```

<details><summary>result</summary>

```
## https://www.orsr.sk/vypis.asp?ID=610947&SID=4&P=1
2 hits (status 200, 4537 chars)
--- CB Growth ONE s. r. o. IČO: 52 656 136 Staromestská 3 Bratislava - mestská časť Staré Mesto 811 03 (od: 10.06.2023 do: 24.06.2026) Smarter Ecommerce GmbH Peter-Behrens-Platz 9 Lin
--- CB Growth ONE s. r. o. Vklad: 1 669 EUR ( peňažný vklad ) Splatené: 1 669 EUR (od: 10.06.2023 do: 29.12.2023) CB Growth ONE s. r. o. Vklad: 2 145 EUR ( peňažný vklad ) Splatené: 2
## https://www.orsr.sk/vypis.asp?ID=440332&SID=2&P=1
7 hits (status 200, 10479 chars)
--- CB Growth ONE s. r. o. IČO: 52 656 136 Staromestská 3 Bratislava - mestská časť Staré Mesto 811 03 (od: 28.01.2021 do: 27.11.2024) Michaela Šišková (od: 07.07.2021 do: 24.06.2022)
--- CB Growth ONE s. r. o. Vklad: 1 250 EUR Splatené: 1 250 EUR (od: 28.01.2021 do: 20.06.2024) Jakub Šiška Vklad: 2 500 EUR Splatené: 2 500 EUR (od: 07.07.2021 do: 20.06.2024) Michae
--- CB Growth ONE s. r. o. Vklad: 1 250 EUR ( peňažný vklad ) Splatené: 1 250 EUR Záložné právo na obchodný podiel spoločníka Číslo záložnej zmluvy: 20240604 Dátum uzavretia záložnej 
--- CB Growth ONE s. r. o. Vklad: 1 250 EUR ( peňažný vklad ) Splatené: 1 250 EUR Záložné právo na obchodný podiel spoločníka Číslo záložnej zmluvy: 20240604 Dátum uzavretia záložnej 
--- CB Growth ONE s. r. o. Vklad: 1 250 EUR ( peňažný vklad ) Splatené: 1 250 EUR Záložné právo na obchodný podiel spoločníka Číslo záložnej zmluvy: 20241023 Dátum uzavretia záložnej 
--- CB Growth ONE s. r. o. Vklad: 1 333 E
… [411 more characters]
```
</details>

→ `Bash` — Show CB Growth ONE contribution chain in Forvio and DNA ERA
```sh
S=[tmp] u="https://www.orsr.sk/vypis.asp?ID=610947&SID=4&P=1"; $S/pg grep "$u" "CB Growth ONE s. r. o. Vklad.{0,250}" 0; u0="https://www.orsr.sk/vypis.asp?ID=610947&SID=4&P=0"; $S/pg get "$u0" 10 >/dev/null; $S/pg grep "$u0" "Spoločníci:.{0,700}" 0; u="https://www.orsr.sk/vypis.asp?ID=440332&SID=2&P=1"; $S/pg grep "$u" "CB Growth ONE s. r. o. Vklad: 1 333.{0,400}" 0 | head -3
```

<details><summary>result</summary>

```
1 hits (status 200, 4537 chars)
--- CB Growth ONE s. r. o. Vklad: 1 669 EUR ( peňažný vklad ) Splatené: 1 669 EUR (od: 10.06.2023 do: 29.12.2023) CB Growth ONE s. r. o. Vklad: 2 145 EUR ( peňažný vklad ) Splatené: 2 145 EUR (od: 30.12.2023 do: 24.06.2026) Štatutárny orgán: konatelia (od: 19.01.2022) Ing. Tomáš Pu
1 hits (status 200, 2573 chars)
--- Spoločníci: Smarter Ecommerce GmbH Peter-Behrens-Platz 9 Linz 4020 Rakúska republika Iné identifikačné číslo: FN 298859z (od: 25.06.2026) Výška vkladu každého spoločníka: Smarter Ecommerce GmbH Vklad: 7 145 EUR ( peňažný vklad ) Splatené: 7 145 EUR (od: 25.06.2026) Štatutárny orgán: konatelia (od: 19.01.2022) Ing. Tomáš Putnoky Dátum narodenia: 23.05.1988 Vznik funkcie: 19.01.2022 (od: 19.01.2023) Ing. Andrej Kozák Dátum narodenia: 31.01.1973 Vznik funkcie: 15.12.2022 (od: 19.01.2023) Konanie menom spoločnosti: Písomnosti zakladajúce práva a povinnosti spoločnosti podpisuje konateľ samostatne, a to tak, že k písanému alebo tlačenému obchodnému menu spoločnosti pripojí svoj vlastnoručný podpis. (od: 19.
1 hits (status 200, 10479 chars)
--- CB Growth ONE s. r. o. Vklad: 1 333 EUR ( peňažný vklad ) Splatené: 1 333 EUR Záložné právo na obchodný podiel spoločníka Číslo záložnej zmluvy: 20240604 Dátum uzavretia záložnej zmluvy: 4. 6. 2024 Záložný veriteľ: Diagnose.me a. s. IČO: 46 588 418 Zochova 6-8 * 811 03 * (od: 12.11.2024 do: 27.11.2024) CB Growth ONE s. r. o. Vklad: 1 333 EUR ( peňažný vklad ) Splatené: 1 333 EUR Záložné právo na o
… [35 more characters]
```
</details>

→ `Bash` — Find SIH intermediary pages list
```sh
S=[tmp] for slug in cb-investment-management-kapitalova-investicia crowdberry-kapitalova-investicia; do u="https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/$slug"; $S/pg get "$u" 700 | head -8; done; $S/pg get "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov" 10 | head -1; grep -oE 'investicie-cez-financnych-sprostredkovatelov/[a-z0-9-]+' $S/cache/$(python3 -c "import hashlib;print(hashlib.sha1(b'https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov').hexdigest())").raw | sort -u
```

<details><summary>result</summary>

```
{"url": "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/cb-investment-management-kapitalova-investicia", "status": 200, "final_url": "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/cb-investment-management-kapitalova-investicia", "ctype": "text/html; charset=UTF-8", "chars": 1123}
CB Investment Management | Slovak Investment Holding, a. s.
CB Investment Management
Slovak Investment Holding is an investor in the fund managed by CB Investment Management, which holds full responsibility for the fund's management and the execution of its investment strategy. The fund was established as a fixed-term investment vehicle with an anticipated duration of 10 years, commencing its operations in 2020 and concluding its active investment period in December 2023.
During its investment phase, capital was deployed into early-stage startups—specifically companies within five years of incorporation—as well as micro and small enterprises with robust growth potential. The fund's investmen
{"url": "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/crowdberry-kapitalova-investicia", "status": 404, "final_url": "https://www.sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/crowdberry-kapitalova-investicia", "ctype": "text/html; charset=UTF-8", "chars": 192}
Zadaná stránka neexistuje | Slovak Investment Holding, a. s.
Page not found.
CONTACT
Map
Grösslingová 44
811 09 Bratislava
www.sih.sk
Some c
… [324 more characters]
```
</details>

→ `WebSearch` Baryon Fund defence tech fund Michal Šimko Bratislava Prague

<details><summary>result</summary>

```
Web search results for query: "Baryon Fund defence tech fund Michal Šimko Bratislava Prague"

Links: [{"title":"www.openvc.app","url":"https://www.openvc.app/fund/Baryon%20Fund"},{"title":"Angels Partners logo","url":"https://angelspartners.com/firm/BaryonFund"},{"title":"Marek Macko","url":"https://sk.linkedin.com/in/marekmacko"},{"title":"Martin Valovsky","url":"https://sk.linkedin.com/in/martin-valovsky"},{"title":"baryon fund","url":"https://superscout.co/investor/baryon-fund"},{"title":"České firmy představily na Slovensku novinky v obranném průmyslu","url":"https://www.businessinfo.cz/clanky/ceske-firmy-predstavily-na-slovensku-novinky-v-obrannem-prumyslu/"},{"title":"CEE VC SUMMIT 2026","url":"https://www.vestbee.com/blog/articles/presto-ventures-launches-a-150-m-fund"},{"title":"Join Vestbee Summer Pitch CEE","url":"https://www.vestbee.com/insights/articles/presto-ventures-launches-a-150-m-fund"},{"title":"Michal Simko","url":"https://sk.linkedin.com/in/michal-simko-b89b0117"}]

The results describe Baryon Fund as an early-stage, defence-focused VC investor, but they disagree on its location and on whether it backs dual-use companies.

- **Location:** One directory lists its headquarters in Prague, Czech Republic. A LinkedIn profile for Martin Valovsky lists an experience entry at Baryon Investment Fund in Bratislava, so the team appears to have a Slovak presence too.
- **Focus:** Its own description says it invests in defence-tech and dual-use scaleups. SuperScout, h
… [972 more characters]
```
</details>

→ `Bash` — Probe Baryon Fund websites and profiles
```sh
S=[tmp] for u in "https://baryon.fund/" "https://www.baryonfund.com/" "https://baryonfund.com/" "https://www.baryon.vc/" "https://superscout.co/investor/baryon-fund" "https://www.openvc.app/fund/Baryon%20Fund" "https://finder.techleap.nl/news/feed/baryon-investment-fund-backs-slovak-drone-tech-startup-airvolute-1"; do $S/pg get "$u" 10 | head -1 | cut -c1-250; done
```

<details><summary>result</summary>

```
{"url": "https://baryon.fund/", "status": 200, "final_url": "https://www.baryon.fund/", "ctype": "text/html; charset=utf-8", "chars": 7621}
{"url": "https://www.baryonfund.com/", "error": "ConnectionError(MaxRetryError('HTTPSConnectionPool(host=\\'www.baryonfund.com\\', port=443): Max retries exceeded with url: / (Caused by NameResolutionError(\"HTTPSConnection(host=\\'www.baryonfund.com
{"url": "https://baryonfund.com/", "error": "ConnectionError(MaxRetryError('HTTPSConnectionPool(host=\\'baryonfund.com\\', port=443): Max retries exceeded with url: / (Caused by NameResolutionError(\"HTTPSConnection(host=\\'baryonfund.com\\', port=44
{"url": "https://www.baryon.vc/", "status": 200, "final_url": "https://www.baryon.vc/", "ctype": "text/html", "chars": 0}
{"url": "https://superscout.co/investor/baryon-fund", "status": 403, "final_url": "https://superscout.co/investor/baryon-fund", "ctype": "text/html; charset=UTF-8", "chars": 16}
{"url": "https://www.openvc.app/fund/Baryon%20Fund", "status": 200, "final_url": "https://www.openvc.app/fund/Baryon%20Fund", "ctype": "text/html; charset=UTF-8", "chars": 4731}
{"url": "https://finder.techleap.nl/news/feed/baryon-investment-fund-backs-slovak-drone-tech-startup-airvolute-1", "status": 403, "final_url": "https://finder.techleap.nl/news/feed/baryon-investment-fund-backs-slovak-drone-tech-startup-airvolute-1",
```
</details>

→ `Bash` — Read Baryon Fund site and OpenVC location
```sh
S=[tmp] $S/pg text "https://baryon.fund/" 0 7700; echo ======; $S/pg grep "https://www.openvc.app/fund/Baryon%20Fund" "(Prague|Bratislava|Czech|Slovak|HQ|Headquarter|located).{0,150}" 80 | head -5
```

<details><summary>result</summary>

```
Exit code 1
Baryon fund
team
mission
advisory board
portfolio
investment focus
Contact
Closer to the Frontline. Closer to the Founder.
We defend Europe by backing bold defence tech entrepreneurs
Our team
Since 2015, Martin has served as Co-Founder, Chairman, and Head of R&D at SEC Technologies, leading global business development and advancing complex R&D. An active angel investor since 2014, he has supported ventures in defence, biotech, and tech, including SliDo (acquired by Cisco), Staffino, and Zdroje Zeme.
Martin Vaľovský
Serial angel investor and entrepreneur
Since 2015, Martin has served as Co-Founder, Chairman, and Head of R&D at SEC Technologies, leading global business development and advancing complex R&D. An active angel investor since 2014, he has supported ventures in defense, biotech, and tech, including SliDo (acquired by Cisco), Staffino, and Zdroje Zeme.
Since 2015, as co-founder and CEO of SEC Technologies, Michal has led international business development and established defence manufacturing in hardware, optics, and electronics. Previously, he worked in high-tech M&A at McKinsey & Company. He holds a PhD in signal processing from Vienna University of Technology, with 30 peer-reviewed papers and over 1,100 citations.
Michal Šimko
Entrepreneur, ex-McKinsey with scientific background
Since 2015, as co-founder and CEO of SEC Technologies, Michal has led international business development and established defense manufacturing in hardware, optics, and electroni
… [6159 more characters]
```
</details>

→ `Bash` — Search ORSR for Baryon and read Baryon legal pages
```sh
O=[tmp] python3 $O brief "Baryon" | head -20; S=[tmp] for p in privacy-policy terms-and-conditions; do u="https://www.baryon.fund/$p"; $S/pg get "$u" 10 | head -1 | cut -c1-200; $S/pg grep "$u" "(S\.à r\.l|SCSp|Luxembourg|Bratislava|Praha|Prague|registered office|IČO|s\. ?r\. ?o).{0,160}" 120 | head -6; done
```

<details><summary>result</summary>

```
== Baryon Consult, s. r. o. | https://www.orsr.sk/vypis.asp?ID=266832&SID=2&P=0
IČO: 47 146 818 | Sídlo: Veterná 982/22, Malinovo 900 45 | zápis: 14.05.2013
Spoločníci: Ing. Marek Špirko / Dátum narodenia: 25.11.1975 / (od: 25.05.2022) / 
Vklady: Ing. Marek Špirko / Vklad: 5 000 EUR Splatené: 5 000 EUR / (od: 25.05.2022) / 
== BARYON s. r. o. | https://www.orsr.sk/vypis.asp?ID=33645&SID=2&P=0
IČO: 35 824 514 | Sídlo: Ružinovská 44, Bratislava 821 03 | zápis: 14.11.2001
Spoločníci: Mgr. Milan Klúčar / Dátum narodenia: 04.07.1970 / (od: 28.10.2022) / Ing. Peter Zámečník / Dátum narodenia: 10.07.1976 / (od: 28.10.2022) / 
Vklady: Mgr. Milan Klúčar / Vklad: 3 320 EUR Splatené: 3 320 EUR / (od: 28.10.2022) / Ing. Peter Zámečník / Vklad: 3 320 EUR Splatené: 3 320 EUR / (od: 28.10.2022) / 
{"url": "https://www.baryon.fund/privacy-policy", "status": 404, "final_url": "https://www.baryon.fund/privacy-policy", "ctype": "text/html; charset=utf-8", "chars": 88}
0 hits (status 404, 88 chars)
{"url": "https://www.baryon.fund/terms-and-conditions", "status": 404, "final_url": "https://www.baryon.fund/terms-and-conditions", "ctype": "text/html; charset=utf-8", "chars": 88}
0 hits (status 404, 88 chars)
```
</details>

→ `Bash` — List Baryon site links
```sh
S=[tmp] grep -oE 'href="[^"]+"' $S/cache/$(python3 -c "import hashlib;print(hashlib.sha1(b'https://baryon.fund/').hexdigest())").raw | sort -u | grep -vE '\.(png|jpg|svg|css|js|ico|webp)' | head -30
```

<details><summary>result</summary>

```
href="/"
href="/about"
href="/blog"
href="/contact"
href="/internal"
href="/old-home"
href="/projects"
href="#"
href="#advisory-board"
href="#contact"
href="#focus"
href="#mission"
href="#portfolio"
href="#team"
href="https://airlogix.io/en"
href="https://airvolute.com/"
href="https://cdn.prod.website-files.com"
href="https://fonts.googleapis.com"
href="https://fonts.gstatic.com"
href="https://sk.linkedin.com/in/martin-valovsky-564bb8303"
href="https://sk.linkedin.com/in/michal-simko-b89b0117?original_referer=https%3A%2F%2Fwww.google.com%2F"
href="https://www.linkedin.com/company/baryon-fund/"
href="https://www.linkedin.com/in/jasonball/"
href="https://www.linkedin.com/in/linerind/"
href="https://www.linkedin.com/in/marekmacko/"
href="https://www.linkedin.com/in/r%C3%B3bert-vass-169ab01a5/"
href="mailto:michal.simko@baryon.fund"
href="mailto:pitch@baryon.fund"
```
</details>

→ `Bash` — Read Baryon about, contact, blog pages
```sh
S=[tmp] for p in about contact blog; do u="https://www.baryon.fund/$p"; $S/pg get "$u" 10 | head -1 | cut -c1-200; $S/pg grep "$u" "(Luxembourg|Bratislava|Praha|Prague|Slovak|office|address|Airvolute|Airlogix|2025|2026).{0,160}" 100 | head -8; done
```

<details><summary>result</summary>

```
{"url": "https://www.baryon.fund/about", "status": 404, "final_url": "https://www.baryon.fund/about", "ctype": "text/html; charset=utf-8", "chars": 88}
0 hits (status 404, 88 chars)
{"url": "https://www.baryon.fund/contact", "status": 404, "final_url": "https://www.baryon.fund/contact", "ctype": "text/html; charset=utf-8", "chars": 88}
0 hits (status 404, 88 chars)
{"url": "https://www.baryon.fund/blog", "status": 404, "final_url": "https://www.baryon.fund/blog", "ctype": "text/html; charset=utf-8", "chars": 88}
0 hits (status 404, 88 chars)
```
</details>

→ `WebSearch` "GROWWS" SICAV LRJ Capital investícia

<details><summary>result</summary>

```
Web search results for query: ""GROWWS" SICAV LRJ Capital investícia"

Links: [{"title":"memorialc.public.lu","url":"https://memorialc.public.lu/memorial/2007/C/Pdf/c261916B.pdf"},{"title":"All Products","url":"https://www.troweprice.com/institutional/uk/en/products/sicav-iii.html"},{"title":"lrj capital fund","url":"https://www.crunchbase.com/organization/lrj-capital-fund"},{"title":"T. Rowe Price Global Growth Equity Net Zero Transition Fund","url":"https://troweprice.com/financial-intermediary/se/en/lp/esg/esg-reports.html"},{"title":"Discover our Range of Funds","url":"https://troweprice.com/financial-intermediary/be/en/home.html"},{"title":"T. Rowe Price Funds SICAV","url":"https://troweprice.com/institutional/at/en/lp/esg/esg-reports.html"},{"title":"troweprice.com","url":"https://troweprice.com/financial-intermediary/uk/en/home.html"},{"title":"memorialc.public.lu","url":"https://memorialc.public.lu/memorial/2007/C/Pdf/c1183166.pdf"},{"title":"esg reports","url":"https://troweprice.com/institutional/uk/en/lp/esg/esg-reports.html"},{"title":"LAZARD%20PATRIMOINE%20CROISSANCE Annual%20Report French%20(France)","url":"https://www.lazardassetmanagement.com/docs/-m0-/190819/LAZARD%20PATRIMOINE%20CROISSANCE_Annual%20Report_French%20(France).pdf"}]

I found no results for "GROWWS" as a SICAV or in connection with LRJ Capital, so I can't confirm any link between them.

The only LRJ Capital result describes it as a Slovak-focused venture investor. Its profile calls it a private 
… [661 more characters]
```
</details>

→ `WebSearch` "LRJ Capital" investícia startup 2024 OR 2025 OR 2026

<details><summary>result</summary>

```
Web search results for query: ""LRJ Capital" investícia startup 2024 OR 2025 OR 2026"

Links: [{"title":"LRJ Capital","url":"https://app.dealroom.co/companies/lrj_capital"},{"title":"Second Photo","url":"https://www.tryfundable.ai/investor/lrj-capital"},{"title":"rj venture capital","url":"https://superscout.co/investor/rj-venture-capital"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/lj-ventures"},{"title":"Predict your next investment","url":"https://www.cbinsights.com/investor/lr-capital"},{"title":"LRG Capital Group Plants Roots in Iowa","url":"https://www.businesswire.com/news/home/20210504005991/en/LRG-Capital-Group-Plants-Roots-in-Iowa"},{"title":"repositorio-api.insper.edu.br","url":"https://repositorio-api.insper.edu.br/server/api/core/bitstreams/f3c75580-0d9b-44e7-a1aa-1609a28a7bdf/content"},{"title":"LRG Capital Group Investor","url":"https://mindmaps.femtech.health/firms/43865"},{"title":"lrf ventures","url":"https://seedtable.com/investors/lrf-ventures"},{"title":"Assisted fundraising","url":"https://hub.waveup.com/funds/sector/vr-ar?page=10"}]

I found one profile for LRJ Capital, but no 2024–2026 investment news.

- **Profile:** Dealroom describes it as a private evergreen venture capital fund. It lists its HQ location as Larnaca Municipality, Cyprus.
- **Focus:** Fundable says the firm supports Slovak and Central/Eastern European startups, and it was founded in 2014. It lists 1-10 employees, with IT, security, and software
… [510 more characters]
```
</details>

→ `Bash` — Fetch LRJ Capital site and Finax article
```sh
S=[tmp] for u in "https://lrjcapital.com/" "https://www.lrj.capital/" "https://www.startitup.sk/slovensky-startup-ziskal-investiciu-15-miliona-eur/"; do $S/pg get "$u" 10 | head -1 | cut -c1-200; $S/pg grep "$u" "(LRJ|GROWWS).{0,200}" 100 | head -4; done
```

<details><summary>result</summary>

```
{"url": "https://lrjcapital.com/", "status": 200, "final_url": "https://www.hugedomains.com/domain_profile.cfm?d=lrjcapital.com", "ctype": "text/html; charset=utf-8", "chars": 5463}
3 hits (status 200, 5463 chars)
--- LrjCapital.com is for sale | HugeDomains Skip to main content Search +1-303-893-0552 LrjCapital.com Buy now: $1,995 ▸ Buy now Processing or ▸ Start payment plan Processing Only $83.13/mo. for 24 months See details 30-day money back guarantee Take immediate ownership Safe and secure shopping LrjCapital.
--- 24 months See details 30-day money back guarantee Take immediate ownership Safe and secure shopping LrjCapital.com This domain is for sale: $1,995 Buy now for $1,995 or pay $83.13 per month for 24 months ▸ Buy now Processing or ▸ Start payment plan Processing Make 24 monthly payments Pay 0% interest Start using the domain today. See details Make 24 monthly payments Pay 0% interest Start using the dom
--- ee domain $3,495 CapitalXs.com ▸ See domain $2,495 Quick stats Domain length 10 characters Keywords Lrj , Capital Base domain LrjCapital TLD extension .com LrjCapital.com ▸ Buy now ▸ Start Payment Plan Shop Home Categories Payment plans My account Safe and secure Money back guarantee Escrow.com NameBright.com Testimonials Helpful Tips Buying guide Case studies FAQs About us Overview Contact us Terms 
{"url": "https://www.lrj.capital/", "error": "ConnectionError(MaxRetryError('HTTPSConnectionPool(host=\\'www.lrj.capital\\', port=443): Max retries exceeded with 
… [1528 more characters]
```
</details>

→ `Bash` — Fetch IPM Growth ORSR and IPM website
```sh
S=[tmp] u="https://www.orsr.sk/vypis.asp?ID=450600&SID=3&P=0"; $S/pg get "$u" 10 >/dev/null; $S/pg grep "$u" "(Obchodné meno: .{0,60}|Sídlo: .{0,80}|IČO: .{0,30}|Spoločníci:.{0,500}|Predmet podnikania.{0,200})" 0; $S/pg get "https://ipmllp.com" 3000
```

<details><summary>result</summary>

```
4 hits (status 200, 2691 chars)
--- Obchodné meno: IPM Growth s.r.o. (od: 04.01.2019) Sídlo: Dolná 5 Banská Bys
--- IČO: 52 151 573 (od: 04.01.2019) De
--- Predmet podnikania (činnosti): Prenájom nehnuteľností, bytových a nebytových priestorov bez poskytovania iných než základných služieb spojených s nájmom (od: 04.01.2019) Kúpa tovaru na účely jeho predaja konečnému spot
--- Spoločníci: IPM Group Holdings Limited Augentius, Two London Bridge Londýn SE1 9RA Spojené kráľovstvo Veľkej Británie a Severného Írska Iné identifikačné číslo: 11719671 (od: 27.09.2022) Global Connect Corporation SK s. r. o. IČO: 46 830 243 Landererova 12 Bratislava - mestská časť Staré Mesto 811 09 (od: 27.09.2022) MaViL, s.r.o. IČO: 52 188 191 Nové záhrady IV 14 Bratislava - mestská časť Ružinov 821 05 (od: 27.09.2022) Výška vkladu každého spoločníka: IPM Group Holdings Limited Vklad: 11 250 EUR ( peňaž
{"url": "https://ipmllp.com", "status": 200, "final_url": "https://www.ipmllp.com/", "ctype": "text/html; charset=UTF-8", "chars": 660}
IPM
About us
Team
Contact
×
InfraPartners Management LLP
About us
Team
Contact
Infrastructure Investment Advisor
Read more
About us
InfraPartners Management LLP was established in 2014 by a team of experienced investment professionals in the infrastructure sector.
More about us
London
123 Pall Mall
London SW1Y 5EA
United Kingdom
E-MAIL
[email protected]
“IPM LLP” is a business name of InfraPartners Management LLP, a Limited Liability Partnership registered in England a
… [187 more characters]
```
</details>

→ `WebSearch` "IPM Growth" OR "IPM Group" investment startup Slovakia 2024 2025

<details><summary>result</summary>

```
Web search results for query: ""IPM Growth" OR "IPM Group" investment startup Slovakia 2024 2025"

Links: [{"title":"venture capital firms bratislava","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava.md"},{"title":"Blog9 Trailblazing Venture Capital Firms Powering Bratislava's Startup Surge","url":"https://www.papermark.com/blog/venture-capital-firms-bratislava"},{"title":"top of page","url":"https://www.symsite.sk/single-post/ipm-raised-200m-from-investors-across-various-projects"},{"title":"therecursive.com","url":"https://therecursive.com/?p=38848"},{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/inobat-secures-100m-in-series-c"},{"title":"REQUEST A DEMO","url":"https://www.emis.com/php/company-profile/SK/Ipm_Growth_SRO_en_16452171.html"},{"title":"top vc funds in slovakia to finance your startup","url":"https://vestbee.com/insights/articles/top-vc-funds-in-slovakia-to-finance-your-startup"},{"title":"Spravodajský portál Tlačovej agentúry Slovenskej republiky","url":"https://www.teraz.sk/ekonomika/peter-gajdos-sa-pripojil-k-ipm-do-tim/432852-clanok.html"},{"title":"Adrian Vyčítal","url":"https://itapa.sk/14255-en/speakers/adrian-vycital"}]

The search turned up several sources on IPM's investment activity in Slovakia, though they don't all agree and one is a weak source.

- **Investment track record:** IPM Group, led by Marián Boček, reportedly raised €200m from investors across various projects. Its flagship holding is a 25% stake
… [2353 more characters]
```
</details>

→ `Bash` — Fetch IPM coverage articles
```sh
S=[tmp] for u in "https://www.symsite.sk/single-post/ipm-raised-200m-from-investors-across-various-projects" "https://therecursive.com/?p=38848" "https://www.teraz.sk/ekonomika/peter-gajdos-sa-pripojil-k-ipm-do-tim/432852-clanok.html"; do $S/pg get "$u" 10 | head -1 | cut -c1-220; $S/pg grep "$u" "(IPM).{0,220}" 120 | head -5; done
```

<details><summary>result</summary>

```
{"url": "https://www.symsite.sk/single-post/ipm-raised-200m-from-investors-across-various-projects", "status": 200, "final_url": "https://www.symsite.sk/single-post/ipm-raised-200m-from-investors-across-various-projects"
3 hits (status 200, 1298 chars)
--- IPM raised €200m from investors across various projects top of page KONTAKT O NÁS IPM raised €200m from investors across various projects Feb 25 1 min read IPM investment group, led by Marián Boček, has raised €200m from investors across various projects. Its flagship investment is a €1.2bn battery factory under construction in Šurany by Chi
---  projects. Its flagship investment is a €1.2bn battery factory under construction in Šurany by China's Gotion, in which IPM holds a 25% stake. The group has also backed successful companies including Brightpick, Photoneo, Matsuko, Energy Storage Systems, SEC Technologies, and French LNG terminal Dunkerque. Less successful to date have been efforts in proprietary battery production, as InoBat is instead installing Gotion battery storage facilities, as well as 
--- ttery production, as InoBat is instead installing Gotion battery storage facilities, as well as chip development, where IPM is an investor in Tachyum. ( dennikN.sk ) Táto správa je z Ekonomiky DNES , denného prehľadu najdôležitejších ekonomických správ zo Slovenska. UKÁŽKA SKÚŠOBNÉ ZASIELANIE This news is from the Slovak Business News TODAY , one-page summary of all the important Slovak business news. FREE TRIAL RECENT ISSU
… [2267 more characters]
```
</details>

→ `WebSearch` InoBat Series C €100 million investors IPM Group press release

<details><summary>result</summary>

```
Web search results for query: "InoBat Series C €100 million investors IPM Group press release"

Links: [{"title":"Back to feed","url":"https://finder.techleap.nl/news/feed/inobat-secures-100m-in-series-c"},{"title":"InoBat Successfully Closes Its Series C Investment Round, the Largest Ever for a Slovak Technology Company","url":"https://www.batterypoweronline.com/view-press-releases/entry/5335/"},{"title":"InoBat Valuation, Funding & Investors","url":"https://multiples.vc/private-comps/inobat"},{"title":"therecursive.com","url":"https://therecursive.com/?p=38848"},{"title":"fr.businessam.be","url":"https://fr.businessam.be/?p=132713"},{"title":"top of page","url":"https://www.symsite.sk/single-post/inobat-raised-100m-from-investors"},{"title":"Slovak battery maker InoBat raises 100 million euros in latest funding round 48633940","url":"https://ca.marketscreener.com/quote/stock/RIO-TINTO-PLC-9590196/news/Slovak-battery-maker-InoBat-raises-100-million-euros-in-latest-funding-round-48633940/"},{"title":"Slovak battery maker InoBat raises 100 million euros in latest funding round","url":"https://batteryindustry.net/?p=40341"},{"title":"Slovak battery maker InoBat raises 100 million euros in latest funding round","url":"https://www.aol.com/news/slovak-battery-maker-inobat-raises-081430515.html"}]

I didn't find an IPM Group press release in the results. The closest primary source is InoBat's own announcement, which lists IPM Group among the investors.

- **Round and date:** InoBat
… [1352 more characters]
```
</details>

→ `Bash` — Fetch InoBat Series C press release
```sh
S=[tmp] u="https://www.batterypoweronline.com/view-press-releases/entry/5335/"; $S/pg get "$u" 10 | head -1 | cut -c1-220; $S/pg grep "$u" "(IPM Group|December|2024).{0,160}" 200 | head -4
```

<details><summary>result</summary>

```
{"url": "https://www.batterypoweronline.com/view-press-releases/entry/5335/", "status": 200, "final_url": "https://www.batterypoweronline.com/view-press-releases/entry/5335/", "ctype": "text/html; charset=UTF-8", "chars"
5 hits (status 200, 4573 chars)
--- ey Set to be Europe’s primary source of high performance NMC battery cells. Continued partnership with Gotion for LFP battery cells. Sets Ambitious Scaling Goals for 2025 Bratislava, Slovakia – 20/12/2024 – InoBat announces the finalisation of its investment round Series C, successfully raising €100m in equity. Investmentfrom strategic investors Amara Raja and Rio Tinto are complemented with significant contributions from SIH (Slovakia’s sovereign wealth fund), Lilium, Bromo Capital, IPM Group and Cielo Capital (InoBat’s founders). Gotion, the Chinese batter
--- aising €100m in equity. Investmentfrom strategic investors Amara Raja and Rio Tinto are complemented with significant contributions from SIH (Slovakia’s sovereign wealth fund), Lilium, Bromo Capital, IPM Group and Cielo Capital (InoBat’s founders). Gotion, the Chinese battery cell maker, backed by the Volkswagen Group, also cements its partnership with InoBat by becoming a cornerstone investor in the round. Chairman Dr Andy Palmer CMG: “Western Europe has been slow to react to the critical need for battery technology. Inobat has quietly gone about building both i
--- y has still a long way to go, but closing Series C and moving to a scaling agenda with Series D is a
… [464 more characters]
```
</details>

→ `Bash` — Fetch Photoneo Series B press release
```sh
S=[tmp] u="https://www.automate.org/robotics/news/photoneo-raises-21-million-in-series-b/anc"; $S/pg get "$u" 10 | head -1 | cut -c1-220; $S/pg grep "$u" "(IPM|Posted|2021).{0,200}" 150 | head -5
```

<details><summary>result</summary>

```
{"url": "https://www.automate.org/robotics/news/photoneo-raises-21-million-in-series-b/anc", "status": 200, "final_url": "https://www.automate.org/robotics/news/photoneo-raises-21-million-in-series-b/anc", "ctype": "text
4 hits (status 200, 7095 chars)
--- SLETTERS Subscribe to Newsletters Photoneo raises $21 million in Series B Member Updates · By Photoneo, now part of Zebra Technologies · December 08, 2021 · 3 min read Share: LinkedIn | Copy Link Bratislava, Slovakia, 7 December 2021 — Photoneo, the innovative smart automation powerhouse, today announced an investment of $21 million from AI Capital, IPM Group, Earlybird, Venture to Future Fund, and Credo Ventures as well as all investors who participated in previous investment rounds. The newly rais
--- onvincing them that Photoneo is primed to lead the next-generation automation of orders fulfillment,” says Jan Zizka. The investment round was led by IPM Group, a global asset manager focusing on technology companies, together with Venture to Future Fund, Earlybird, Credo Ventures, and investors who participated in earlier rounds as well. “Photoneo’s work and achievements are truly impressive. We believe in the company’s power to enhance logistics and transform the automation of e-commerce processe
--- stics and transform the automation of e-commerce processes with its groundbreaking and much-needed solutions,” says Marian Bocek, Managing Partner at IPM Group. “Photoneo is already a well-established leader of smart automatio
… [786 more characters]
```
</details>

→ `Bash` — Fetch Crowdberry and CB ESPRI sources
```sh
S=[tmp] for u in "https://www.crowdberry.eu/en" "https://cc.cz/lokalni-investovani-je-na-vzestupu-hlasi-crowdberry-pres-platformu-a-fondy-loni-proteklo-730-milionu/" "https://www.orsr.sk/vypis.asp?ID=596151&SID=2&P=0" "https://www.podnikajte.sk/financie-na-podnikanie/cb-espri-impact-one-novy-fond" "https://www.orsr.sk/vypis.asp?ID=618739&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=679020&SID=5&P=0"; do echo "#### $u"; $S/pg get "$u" 10 | head -1 | cut -c1-200; done
```

<details><summary>result</summary>

```
#### https://www.crowdberry.eu/en
(eval):1: no such file or directory: [tmp]
#### https://cc.cz/lokalni-investovani-je-na-vzestupu-hlasi-crowdberry-pres-platformu-a-fondy-loni-proteklo-730-milionu/
(eval):1: no such file or directory: [tmp]
#### https://www.orsr.sk/vypis.asp?ID=596151&SID=2&P=0
(eval):1: no such file or directory: [tmp]
#### https://www.podnikajte.sk/financie-na-podnikanie/cb-espri-impact-one-novy-fond
(eval):1: no such file or directory: [tmp]
#### https://www.orsr.sk/vypis.asp?ID=618739&SID=2&P=0
(eval):1: no such file or directory: [tmp]
#### https://www.orsr.sk/vypis.asp?ID=679020&SID=5&P=0
(eval):1: no such file or directory: [tmp]
```
</details>

→ `Bash` — Inspect scratch directory state
```sh
ls -la [tmp] [tmp] ls [tmp] | wc -l
```

<details><summary>result</summary>

```
ls: [tmp] No such file or directory
ls: [tmp] No such file or directory
ls: [tmp] No such file or directory
       0
```
</details>

→ `Bash` — Check what remains in scratchpad
```sh
ls [tmp] | head -50; ls [tmp]
```

<details><summary>result</summary>

```
Exit code 1
cache
tools
ls: [tmp] No such file or directory
```
</details>

→ `Bash` — Inspect new scratchpad contents
```sh
ls -la [tmp] [tmp] | head -30
```

<details><summary>result</summary>

```
[tmp]
total 1384
drwxr-xr-x  26 [user]  wheel     832 11 окт.  01:48 .
drwx------   4 [user]  wheel     128 11 окт.  01:48 ..
-rw-r--r--   1 [user]  wheel     420 11 окт.  01:48 0ce0f4af7e639183328251e61642d3a4d9706611.hdr
-rw-r--r--   1 [user]  wheel  115119 11 окт.  01:48 0ce0f4af7e639183328251e61642d3a4d9706611.raw
-rw-r--r--   1 [user]  wheel   13994 11 окт.  01:48 0ce0f4af7e639183328251e61642d3a4d9706611.txt
-rw-r--r--   1 [user]  wheel     420 11 окт.  01:48 10ff919b4d1ca89fa63813da7c2ea52322d7672b.hdr
-rw-r--r--   1 [user]  wheel   35849 11 окт.  01:48 10ff919b4d1ca89fa63813da7c2ea52322d7672b.raw
-rw-r--r--   1 [user]  wheel    4050 11 окт.  01:48 10ff919b4d1ca89fa63813da7c2ea52322d7672b.txt
-rw-r--r--   1 [user]  wheel     420 11 окт.  01:48 159ab3678e10fbbb8ce6d3e7a3a7a9db697717b7.hdr
-rw-r--r--   1 [user]  wheel   40581 11 окт.  01:48 159ab3678e10fbbb8ce6d3e7a3a7a9db697717b7.raw
-rw-r--r--   1 [user]  wheel    5211 11 окт.  01:48 159ab3678e10fbbb8ce6d3e7a3a7a9db697717b7.txt
-rw-r--r--   1 [user]  wheel     420 11 окт.  01:48 34bcf5d96cd7fcf0f130f821f7b3b2f19e3db6f3.hdr
-rw-r--r--   1 [user]  wheel   36490 11 окт.  01:48 34bcf5d96cd7fcf0f130f821f7b3b2f19e3db6f3.raw
-rw-r--r--   1 [user]  wheel    4292 11 окт.  01:48 34bcf5d96cd7fcf0f130f821f7b3b2f19e3db6f3.txt
-rw-r--r--   1 [user]  wheel     420 11 окт.  01:48 4faf30be25f8de9a54131f588b314ff67c7579de.hdr
-rw-r--r--   1 [user]  wheel  127393 11 окт
… [1106 more characters]
```
</details>

→ `Bash` — Recreate ORSR helper and wrapper in new dir
```sh
D=[tmp] mkdir -p $D/bin $D/cache $D/dl && cat > $D/bin/orsr.py <<'EOF'
#!/usr/bin/env python3
# usage: orsr.py search "name" | brief "name" [full] | vypis URL
import sys, re, urllib.request, urllib.parse, html, socket; socket.setdefaulttimeout(30)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"
BASE = "https://www.orsr.sk/"
def get(url):
    import time
    err = None
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, timeout=60).read().decode("windows-1250", errors="replace")
        except Exception as e:
            err = e; time.sleep(3)
    print("FETCH FAILED", url, err); return ""
def text(h):
    h = re.sub(r"(?is)<script.*?</script>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</tr>|</p>|</div>", "\n", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h)
    lines = [re.sub(r"[ \t\xa0]+", " ", l).strip() for l in h.split("\n")]
    return "\n".join(l for l in lines if l)
def rows_for(q):
    q = urllib
… [1311 more characters]
```

<details><summary>result</summary>

```
ok
```
</details>

→ `Write` [tmp]

<details><summary>result</summary>

```
File created successfully at: [tmp] (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Fetch excluded-candidate sources batch 1
```sh
D=[tmp] for u in "https://www.crowdberry.eu/en" "https://www.orsr.sk/vypis.asp?ID=596151&SID=2&P=0" "https://www.podnikajte.sk/financie-na-podnikanie/cb-espri-impact-one-novy-fond" "https://www.orsr.sk/vypis.asp?ID=618739&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=679020&SID=5&P=0" "https://www.orsr.sk/vypis.asp?ID=497651&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=526709&SID=2&P=0"; do echo "#### $u"; $D/pg get "$u" 10 | head -1 | cut -c1-160; done
```

<details><summary>result</summary>

```
#### https://www.crowdberry.eu/en
{"url": "https://www.crowdberry.eu/en", "status": 200, "final_url": "https://www.crowdberry.eu/en", "ctype": "text/html; charset=utf-8", "chars": 12925}
#### https://www.orsr.sk/vypis.asp?ID=596151&SID=2&P=0
{"url": "https://www.orsr.sk/vypis.asp?ID=596151&SID=2&P=0", "status": 200, "final_url": "https://www.orsr.sk/vypis.asp?ID=596151&SID=2&P=0", "ctype": "text/htm
#### https://www.podnikajte.sk/financie-na-podnikanie/cb-espri-impact-one-novy-fond
{"url": "https://www.podnikajte.sk/financie-na-podnikanie/cb-espri-impact-one-novy-fond", "status": 200, "final_url": "https://www.podnikajte.sk/financie-na-pod
#### https://www.orsr.sk/vypis.asp?ID=618739&SID=2&P=0
{"url": "https://www.orsr.sk/vypis.asp?ID=618739&SID=2&P=0", "status": 200, "final_url": "https://www.orsr.sk/vypis.asp?ID=618739&SID=2&P=0", "ctype": "text/htm
#### https://www.orsr.sk/vypis.asp?ID=679020&SID=5&P=0
{"url": "https://www.orsr.sk/vypis.asp?ID=679020&SID=5&P=0", "status": 200, "final_url": "https://www.orsr.sk/vypis.asp?ID=679020&SID=5&P=0", "ctype": "text/htm
#### https://www.orsr.sk/vypis.asp?ID=497651&SID=2&P=0
{"url": "https://www.orsr.sk/vypis.asp?ID=497651&SID=2&P=0", "status": 200, "final_url": "https://www.orsr.sk/vypis.asp?ID=497651&SID=2&P=0", "ctype": "text/htm
#### https://www.orsr.sk/vypis.asp?ID=526709&SID=2&P=0
{"url": "https://www.orsr.sk/vypis.asp?ID=526709&SID=2&P=0", "status": 200, "final_url": "https://www.orsr.sk/vypis.asp?ID=526709&SID=2&P=0", "ctype"
… [11 more characters]
```
</details>

→ `Bash` — Grep Crowdberry, CB ESPRI, Impact Ventures, Vision ORSR
```sh
D=[tmp] $D/pg grep "https://www.crowdberry.eu/en" "(platform|crowd|club).{0,150}" 60 | head -6; for u in "https://www.orsr.sk/vypis.asp?ID=596151&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=618739&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=679020&SID=5&P=0" "https://www.orsr.sk/vypis.asp?ID=497651&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=526709&SID=2&P=0"; do echo "#### $u"; $D/pg grep "$u" "(Obchodné meno: .{0,60}|IČO: .{0,14}|Spoločníci:.{0,450}|Akcionár:.{0,200})" 0; done; $D/pg grep "https://www.podnikajte.sk/financie-na-podnikanie/cb-espri-impact-one-novy-fond" "(10,5|sociáln|pôžič|úver|kapitál|500 000|10 000).{0,200}" 100 | head -6
```

<details><summary>result</summary>

```
17 hits (status 200, 12925 chars)
--- Investments in SMEs and real estate | Crowdberry - Crowdberry NOW AVAILABLE Investment opportunity Boataround. Learn more. Investment opportunity Boataround. Learn more. EN Investment opportunities Local. Vetted. Investments. Play a part in the success 
---  Play a part in the success of domestic brands. Invest with Crowdberry. Investment opportunities About Crowdberry Register in 5 minutes No opening fees Only verified opportunities ECSPR licensed ECSPR licensed 16,705 registered 16,705 registered from EUR 1,000 from EUR 1,000
--- total demand reaching almost double. Sensoneo More than 100 Crowdberry investors have invested a total of more than €2 million in Seonsone smart waste management. Previous slide Next slide All closed opportunities References The perspective of investors and founders on how p
--- owth Michal Meško CEO, Martinus I’ve been investing through Crowdberry practically since the beginning and it makes a lot of sense to me. I can see the direct impact of my investments and their power to influence the business environment in Slovakia. I can choose companies w
--- vá Co-founder, CURADEN Slovakia What I appreciate about the Crowdberry platform is that it does a lot of the work for me that an investor has to do when investing on their own. The Crowdberry team thoroughly vet the Slovak companies I put my money into, which makes the inves
#### https://www.orsr.sk/vypis.asp?ID=596151&SID=2&P=0
3 hits (status 200, 2360 chars)
-
… [5038 more characters]
```
</details>

→ `Bash` — Fetch excluded-candidate sources batch 2
```sh
D=[tmp] for u in "https://www.slovca.sk/sk/riadni-clenovia/sandberg-capital.html" "https://www.slovca.sk/sk/riadni-clenovia/eterus-capital.html" "https://www.eterus.sk/" "https://www.orsr.sk/vypis.asp?ID=653149&SID=2&P=0" "https://oaklins.com/ar/en/deals/110583" "https://sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia" "https://www.fondfit.sk/" "https://www.slovca.sk/sk/riadni-clenovia/fond-inovacii-a-technologii.html" "https://www.nhfond.sk/" "https://www.slovca.sk/sk/riadni-clenovia/narodny-holdingovy-fond-s-r-o.html"; do echo "#### $u"; $D/pg get "$u" 10 | head -1 | cut -c1-160; done
```

<details><summary>result</summary>

```
#### https://www.slovca.sk/sk/riadni-clenovia/sandberg-capital.html
{"url": "https://www.slovca.sk/sk/riadni-clenovia/sandberg-capital.html", "status": 200, "final_url": "https://www.slovca.sk/sk/riadni-clenovia/sandberg-capital
#### https://www.slovca.sk/sk/riadni-clenovia/eterus-capital.html
{"url": "https://www.slovca.sk/sk/riadni-clenovia/eterus-capital.html", "status": 200, "final_url": "https://www.slovca.sk/sk/riadni-clenovia/eterus-capital.htm
#### https://www.eterus.sk/
{"url": "https://www.eterus.sk/", "status": 200, "final_url": "https://eterus.sk/", "ctype": "text/html; charset=UTF-8", "chars": 8747}
#### https://www.orsr.sk/vypis.asp?ID=653149&SID=2&P=0
{"url": "https://www.orsr.sk/vypis.asp?ID=653149&SID=2&P=0", "status": 200, "final_url": "https://www.orsr.sk/vypis.asp?ID=653149&SID=2&P=0", "ctype": "text/htm
#### https://oaklins.com/ar/en/deals/110583
{"url": "https://oaklins.com/ar/en/deals/110583", "status": 200, "final_url": "https://www.oaklins.com/ar/en/deals/110583/", "ctype": "text/html; charset=UTF-8"
#### https://sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia
{"url": "https://sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia", "status": 200, "final_url": "ht
#### https://www.fondfit.sk/
{"url": "https://www.fondfit.sk/", "status": 200, "final_url": "https://www.fondfit.sk/", "ctype": "text/html; charset=UTF-8", "chars": 3892}
####
… [649 more characters]
```
</details>

→ `Bash` — Read SLOVCA profiles of PE/public members
```sh
D=[tmp] for u in "https://www.slovca.sk/sk/riadni-clenovia/sandberg-capital.html" "https://www.slovca.sk/sk/riadni-clenovia/eterus-capital.html" "https://www.slovca.sk/sk/riadni-clenovia/fond-inovacii-a-technologii.html" "https://www.slovca.sk/sk/riadni-clenovia/narodny-holdingovy-fond-s-r-o.html"; do echo "#### $u"; $D/pg text "$u" 0 700 | tr '\n' '|'; echo; done
```

<details><summary>result</summary>

```
#### https://www.slovca.sk/sk/riadni-clenovia/sandberg-capital.html
Sandberg Capital / Slovak Venture Capital & Private Equity Association SLOVCA|Sandberg Capital|Adresa: Dvořákovo Nábrežie 8, 81102 Bratislava, Slovakia|Email: dealflow@sandbergcapital.com|Web:|www.sandbergcapital.com|Preferovaná výška investície: €4M - €15M|Preferované odvetvia: IT, vzdelávanie, potraviny a poľnohospodárstvo. Firmy s opakovanými tržbami a esenciálnymi produktami a službami. Preferované zameranie na B2B.|Geografické zameranie: Slovensko, Česko, okolité krajiny CEE, Balkán.|Prílohy na stiahnutie|Sandberg logo new.png|(veľkosť 48 KB, formát png)|Riadni členovia|ARX Equity Partners|CVI|Enterprise Investors|Eterus Capital|Fond inovácií a technológií|Genesis Capital|Jet Investment|
#### https://www.slovca.sk/sk/riadni-clenovia/eterus-capital.html
Eterus Capital / Slovak Venture Capital & Private Equity Association SLOVCA|Eterus Capital|Adresa: Laurinská 18, 811 01 Bratislava, Slovensko|Mobil: +421 914 32 00 65|E-mail: Boris.Kostik@wood.com|Web:|www.eterus.sk|Typ investícií: Private equity|Preferovaná výška investície: 500 tis. Eur až 5 mil. Eur.|Preferované odvetvie: Odvetvia s vyššou pridanou hodnotou, investície do príležitostí v rozvojovom štádiu životného cyklu v odvetviach so silným rastovým potenciálom.|Geografické zameranie: Slovenská republika|Prílohy na stiahnutie|Eterus_Trademark_Tagline_Color_RGB.png|(veľkosť 11 KB, formát png)|Eterus_Presentation_2022.pdf|(veľkosť 607 KB, formát png)|Ri
… [1601 more characters]
```
</details>

→ `Bash` — Read FIT, NHF and Limerock SIH pages
```sh
D=[tmp] $D/pg text "https://www.fondfit.sk/" 0 1800 | tr '\n' '|'; echo; echo; $D/pg text "https://www.nhfond.sk/" 0 1800 | tr '\n' '|'; echo; echo; $D/pg text "https://sih.sk/en/investicie/investicie-cez-financnych-sprostredkovatelov/limerock-fund-manager-kapitalova-investicia" 0 1100
```

<details><summary>result</summary>

```
Fond Fit – Pomáhame inovatívnym nápadom|Hľadať:|Adresa|Trnavská cesta 100, 821 01 Bratislava|Email|info@fondfit.sk|Pomáhame inovatívnym nápadom|Informácia pre potenciálnych záujemcov o investície: Fond inovácií a technológií vstúpil v roku 2025 do post-investičnej fázy.|O NÁS|Rozvíjame podniky s úspešnými technológiami|Viac ako 10 rokov pomáhame slovenským podnikateľom premieňať ich podnikateľské zámery na realitu|Viac informácií|SLUŽBY|Poskytujeme tieto služby a podporu|Financovanie kapitálu|Poskytnutie kapitálu v prípade záujmu investora|Mentoring|Podporu pri tvorbe startupu pod vedením skúsených odborníkov|Analýza zámeru|Uskutočniteľnosť a rentabilita Vášho projektu|Pracovný proces|Náš pracovný postup – ako posudzujeme vaše projekty|Kontakt|1.|Kontaktujte nás|cez email a zašlite nám vyplnený formulár, ktorý si môžete stiahnuť tu|Formulár na stiahnutie|2.|Investičný zámer|Financovaný projekt musí spĺňať podmienky nášho investičného zamerania a podľa štádia jeho vývoja stanovíme našu investičnú stratégiu|3.|Projekt|Identifikácia základných východísk projektu a potrieb|4.|Investičný proces|Rokovania s partnermi o podmienkach vstupu investora a spolupráce|5.|Transkačná dokumentácia|Príprava a podpísanie transakčnej dokumentácie|6.|Vstup investora|Po skompletizovaní všetkých legislatívnych procesov dochádza k vstupu investora do spoločnosti|Projekty|Portfólio podporených podnikateľov|Elearn.Aero|IT technológie|Futureplastix|Výroba|Trigen|Technológie|,|Výroba|COGNEXA|IT technoló
… [3123 more characters]
```
</details>

→ `Bash` — Check NDF II/NHF ORSR and Seed Starter sources
```sh
D=[tmp] O="python3 $D/bin/orsr.py"; $O brief "National Development Fund II" | head -5; $O brief "Národný holdingový fond" | head -4; for u in "https://www.slsp.sk/sk/aktuality/2025/9/17/zo-slovenska-rovno-na-najvacsi-realitny-trh-intellcre-ziskava-investiciu-od-seed-startera-slovenskej-sporitelne" "https://www.omediach.com/internet/30236-seed-starter-slovenskej-sporitelne-investuje-400-tisic-eur-do-startupu-webout-ten-ziskava-spolu-1-65-miliona-eur-a-mieri-do-silicon-valley" "https://sita.sk/seed-starter-slovenskej-sporitelne-hlasi-prvu-investiciu-podporil-slovensky-startup-smarthead/" "https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/"; do echo "#### $u"; $D/pg get "$u" 10 | head -1 | cut -c1-120; $D/pg grep "$u" "(Seed Starter).{0,200}" 60 | head -3; done
```

<details><summary>result</summary>

```
(eval):1: no such file or directory: python3 [tmp]
(eval):1: no such file or directory: python3 [tmp]
#### https://www.slsp.sk/sk/aktuality/2025/9/17/zo-slovenska-rovno-na-najvacsi-realitny-trh-intellcre-ziskava-investiciu-od-seed-startera-slovenskej-sporitelne
{"url": "https://www.slsp.sk/sk/aktuality/2025/9/17/zo-slovenska-rovno-na-najvacsi-realitny-trh-intellcre-ziskava-invest
9 hits (status 200, 5900 chars)
--- o na najväčší realitný trh. IntellCRE získava investíciu od Seed Startera Slovenskej sporiteľne | Slovenská sporiteľňa Preskočiť navigáciu Späť na Aktuality Zo Slovenska rovno na najväčší realitný trh. IntellCRE získava investíciu od Seed Startera Slovenskej sporiteľne Kým väčšina startupov sa najskôr snaží uspieť doma, IntellCRE 
--- ráve preto teraz získava investíciu vo výške 400 000 eur od Seed Startera Slovenskej sporiteľne, ktorá mu má pomôcť zrýchliť rast a otvoriť dvere k ďalšej expanzii. Celkovo ide už o šiesty zainvestovaný startup v portfóliu Seed Startera. Miesto dní iba sekundy. Iba toľko dnes trvá analýza, ktorá odporučí, či sa oplatí kúpiť nehnut
#### https://www.omediach.com/internet/30236-seed-starter-slovenskej-sporitelne-investuje-400-tisic-eur-do-startupu-webout-ten-ziskava-spolu-1-65-miliona-eur-a-mieri-do-silicon-valley
{"url": "https://www.om
… [2571 more characters]
```
</details>

→ `Bash` — ORSR lookups for NDF II, NHF, banks
```sh
D=[tmp] python3 $D/bin/orsr.py brief "National Development Fund II" | head -4; python3 $D/bin/orsr.py brief "Národný holdingový fond" | head -4; python3 $D/bin/orsr.py search "Slovenská sporiteľňa"; python3 $D/bin/orsr.py search "365.fintech"; python3 $D/bin/orsr.py search "Tatra banka"; python3 $D/bin/orsr.py search "Všeobecná úverová banka"
```

<details><summary>result</summary>

```
== National Development Fund I., s. r. o. | https://www.orsr.sk/vypis.asp?ID=150565&SID=2&P=0
IČO: 44 690 487 | Sídlo: Grösslingová 2495/44, Bratislava - mestská časť Staré Mesto 811 09 | zápis: 21.03.2009
Spoločníci: Slovak Investment Holding, a. s. IČO: 47 759 097 / Grösslingová 44 / Bratislava - mestská časť Staré Mesto 811 09 / (od: 01.12.2021) / 
== National Development Fund II., a.s. | https://www.orsr.sk/vypis.asp?ID=306999&SID=2&P=0
== Národný holdingový fond s. r. o. | https://www.orsr.sk/vypis.asp?ID=10228&SID=2&P=0
IČO: 31 384 943 | Sídlo: Trnavská cesta 17065/100, Bratislava - mestská časť Ružinov 821 01 | zápis: 13.12.1994
Spoločníci: Slovak Business Agency IČO: 30 845 301 / Karadžičova 7773/2 / Bratislava - mestská časť Staré Mesto 811 09 / (od: 27.08.2025) / 
Slovenská sporiteľňa, a.s. | https://www.orsr.sk/vypis.asp?ID=19812&SID=2&P=0
365.fintech, a.s. | https://www.orsr.sk/vypis.asp?ID=410247&SID=2&P=0
Tatra banka, a.s. | https://www.orsr.sk/vypis.asp?ID=21634&SID=2&P=0
Všeobecná úverová banka, a.s.; skrátený názov: VÚB, a.s. | https://www.orsr.sk/vypis.asp?ID=21601&SID=2&P=0
```
</details>

→ `Bash` — Fetch ORSR extracts of public entities and banks
```sh
D=[tmp] for u in "https://www.orsr.sk/vypis.asp?ID=306999&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=19812&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=410247&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=21634&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=21601&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=10228&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=307221&SID=2&P=0"; do echo "#### $u"; $D/pg get "$u" 10 >/dev/null; $D/pg grep "$u" "(Obchodné meno: .{0,70}|IČO: .{0,14}|Akcionár:.{0,200}|Spoločníci:.{0,200}|Predmet podnikania \(činnosti\): .{0,220})" 0; done
```

<details><summary>result</summary>

```
#### https://www.orsr.sk/vypis.asp?ID=306999&SID=2&P=0
4 hits (status 200, 4839 chars)
--- Obchodné meno: National Development Fund II., a.s. (od: 24.07.2018) Sídlo: Grösslingo
--- IČO: 47 759 224 (od
--- Predmet podnikania (činnosti): činnosť podnikateľských, organizačných a ekonomických poradcov (od: 26.04.2014) poskytovanie úverov a/alebo pôžičiek z peňažných zdrojov získaných výlučne bez verejnej výzvy a bez verejnej ponuky majetkových hodnôt (od: 
--- Akcionár: Slovak Investment Holding, a. s. IČO: 47 759 097 Grösslingová 44 Bratislava - mestská časť Staré Mesto 811 09 (od: 28.12.2021) Ďalšie právne skutočnosti: Spoločnosť bola založená zakladateľskou listi
#### https://www.orsr.sk/vypis.asp?ID=19812&SID=2&P=0
8 hits (status 200, 25831 chars)
--- Obchodné meno: Slovenská sporiteľňa, a.s. (od: 05.11.2014) Sídlo: Tomášikova 48 Brati
--- IČO: 00 151 653 (od
--- Predmet podnikania (činnosti): Predmetom podnikania spoločnosti sú bankové činnosti: (od: 30.05.2002) prijímanie vkladov (od: 30.05.2002) poskytovanie úverov (od: 30.05.2002) obchodovanie na vlastný účet, 1. s finančnými nástrojmi peňažného trhu v slo
--- Akcionár: Erste Group Bank AG Am Belvedere 1 Viedeň A-1100 Rakúska republika (od: 17.08.2022) Ďalšie právne skutočnosti: Spoločnosť bola založená zakladateľskou listinou Fondu národného majetku SR so sídlom v 
--- IČO: 36 700 991 Tom
--- IČO: 35 849 665 Tom
--- IČO: 35 865 491 Tom
--- IČO: 35 812 419 Tom
#### https://www.orsr.sk/vypis.asp?ID=410247&SID=2&P=0
4 hits 
… [3199 more characters]
```
</details>

→ `Bash` — Fetch 365.fintech, SBA, KPAS, AceON, Launcher sources
```sh
D=[tmp] for u in "https://365fintech.sk/" "https://www.sbagency.sk/" "https://www.podnikajte.sk/investor/vznikol-klub-podnikatelskych-anjelov" "https://accace.com/winners-of-our-international-startup-accelerator" "https://www.startitup.sk/launcher-postavi-vas-projekt-na-nohy/"; do echo "#### $u"; $D/pg get "$u" 10 | head -1 | cut -c1-160; done
```

<details><summary>result</summary>

```
#### https://365fintech.sk/
{"url": "https://365fintech.sk/", "status": 200, "final_url": "https://365fintech.sk/", "ctype": "text/html; charset=utf-8", "chars": 8655}
#### https://www.sbagency.sk/
{"url": "https://www.sbagency.sk/", "status": 200, "final_url": "https://www.sbagency.sk/", "ctype": "text/html; charset=UTF-8", "chars": 3461}
#### https://www.podnikajte.sk/investor/vznikol-klub-podnikatelskych-anjelov
{"url": "https://www.podnikajte.sk/investor/vznikol-klub-podnikatelskych-anjelov", "status": 200, "final_url": "https://www.podnikajte.sk/investor/vznikol-klub-
#### https://accace.com/winners-of-our-international-startup-accelerator
{"url": "https://accace.com/winners-of-our-international-startup-accelerator", "status": 200, "final_url": "https://www.accace.com/winners-of-our-international-
#### https://www.startitup.sk/launcher-postavi-vas-projekt-na-nohy/
{"url": "https://www.startitup.sk/launcher-postavi-vas-projekt-na-nohy/", "status": 200, "final_url": "https://www.startitup.sk/launcher-postavi-vas-projekt-na-
```
</details>

→ `Bash` — Grep 365.fintech, SBA, KPAS pages
```sh
D=[tmp] $D/pg grep "https://365fintech.sk/" "(20(19|2[0-6])|invest|Velaris).{0,120}" 60 | head -10; $D/pg text "https://www.sbagency.sk/" 0 1200 | tr '\n' '|'; echo; $D/pg grep "https://www.podnikajte.sk/investor/vznikol-klub-podnikatelskych-anjelov" "(Klub podnikateľských anjelov|anjel).{0,200}" 60 | head -4
```

<details><summary>result</summary>

```
31 hits (status 200, 8653 chars)
--- opean Focus <#Fintech> 365.fintech We are a fintech venture investor focusing on innovative b2b or b2b2c FinTech, InsurTech and Big Data startups. We invest in European startups with global ambitions around seed stage. FIRST THING YOU SHOULD KNOW
--- Focus in on European Fintech We are based in CEE but we are investing anywhere in Europe where we see outstanding nascent fintech startups - from London to Riga. Our ultimate goal is to support our companies in scaling across the continent and gl
--- ross the continent and globally. Who Are We Looking For? We invest in and around seed stage in Europe. Our primary focus is on b2b and b2b2c fintech startups disrupting legacy infrastructure and distribution models and creating value for end cons
--- from simple onboarding to "live" compliance and AML checks. Velaris Velaris is a London based platform for customer success management and operations. Tapline Tapline is a trading platform that enables companies with recurring revenues to receive 
--- startup building the next generation credit card experience InvestSuite International B2B WealthTech startup, focused at helping institutions serve their clients better with a suite of modern digital investment solutions. Startup Wise Guys Startu
--- s serve their clients better with a suite of modern digital investment solutions. Startup Wise Guys Startup Wise Guys is the leading B2B startup accelerator in Europe. Dateio Dateio is building a scaleable c
… [3000 more characters]
```
</details>

→ `Bash` — Grep AceON and Launcher pages
```sh
D=[tmp] $D/pg grep "https://accace.com/winners-of-our-international-startup-accelerator" "(ZAKA|40|AceON|invest|Dec|2025).{0,160}" 80 | head -8; $D/pg grep "https://www.startitup.sk/launcher-postavi-vas-projekt-na-nohy/" "(Launcher).{0,200}" 60 | head -4; $D/pg grep "https://www.startitup.sk/launcher-postavi-vas-projekt-na-nohy/" "20[0-9]{2} o [0-9]" 60 | head -2
```

<details><summary>result</summary>

```
38 hits (status 200, 20262 chars)
--- From 49 countries to one cohort: AceOn Accelerator welcomes its most international batch yet | Press release - Accace Contact us Sign up for news eShop Search for Search for X Contact Form Notify Get in touch with us! Refer to this form if you have any questions and require add
--- scribe form sidebar Subscribe Sign up for news From 49 countries to one cohort: AceOn Accelerator welcomes its most international batch yet | Press release December 22, 2025 This article is also available in Czech Slovak Romanian AceON Accelerator has successfully completed its fifth international acceleration program, whic
--- m concluded with an online Demo Day, during which one startup received a direct investment from AceON. JST 3D: Italian startup earns AceON investment A total of 23 startups presented their projects to AceON’s investment committee during the virtual Demo Day. Among them, JST 3D stood out for its solution addressing a critical
--- nd MRI scans and the need for faster, highly accurate data interpretation. “Our decision to invest in JST 3D was driven by the strength of their core technology. Their AI can reveal anatomical details that are invisible to the human eye and translate standard CT scans into actionable 3D models, giving clinicians a powerfu
--- ve surgical planning and patient outcomes,” explains Peter Pašek, Co-founder of AceON Accelerator and Managing Director & Partner at Accace Slovakia , on why he considered JST 3D the stronge
… [1931 more characters]
```
</details>

→ `Bash` — Fetch ORSR for BIC, Monogram, Arca, Pro Partners, Eterus, Ethernum, Sandberg, Limerock, FIT
```sh
D=[tmp] for u in "https://www.orsr.sk/vypis.asp?ID=4814&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=124603&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=39276&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=325650&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=129737&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=653149&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=311602&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=307952&SID=2&P=0" "https://www.orsr.sk/vypis.asp?ID=260666&SID=2&P=0"; do echo "#### $u"; $D/pg get "$u" 10 >/dev/null; $D/pg grep "$u" "(Obchodné meno: .{0,70}|IČO: .{0,14}|Akcionár:.{0,160}|Spoločníci:.{0,250}|Predmet podnikania \(činnosti\): .{0,160}|Ďalšie právne skutočnosti:.{0,200})" 0 | head -7; done 2>&1 | cut -c1-400
```

<details><summary>result</summary>

```
#### https://www.orsr.sk/vypis.asp?ID=4814&SID=2&P=0
5 hits (status 200, 4014 chars)
--- Obchodné meno: B I C Bratislava spol. s r.o. (od: 30.12.1991) Sídlo: Zochova 5 Bratis
--- IČO: 30 840 007 (od
--- Predmet podnikania (činnosti): automatizované spracovanie údajov (od: 04.08.1994) sprostredkovanie obchodu a služieb (od: 04.08.1994) reklamná a propagačná činnosť (od: 04.08.1994) prenájom a
--- Spoločníci: Slovenská obchodná a priemyselná komora, zast. Bratislavskou regionálnou komorou IČO: 30 842 654 Jašíkova 6 Bratislava (od: 11.02.1999) Ing. Štefan Vrátny , PhD. Dátum narodenia: 21.11.1957 (od: 24.05.2022) Ing. Roman Linczényi Dátum narodenia: 09.1
--- Ďalšie právne skutočnosti: Spoločnosť s ručením obmedzeným bola založená spoločenskou zmluvou zo dňa 12.12.1991 podľa § 106a ods. l a § 106n ods. l Zák. č. 103/ 1990 Zb., ktorým sa mení a dopľňa Hospodársky zákonník. Starý spi
#### https://www.orsr.sk/vypis.asp?ID=124603&SID=2&P=0
4 hits (status 200, 3691 chars)
--- Obchodné meno: MONOGRAM Ventures a. s. (od: 08.04.2008) Sídlo: Ilkovičova 6276 Bratis
--- IČO: 44 071 574 (od
--- Predmet podnikania (činnosti): administratívne, organizačné a technické práce súvisiace s vyhľadávaním, triedením, spracúvaním a zoraďovaním informácií (od: 08.04.2008) školiaca činnosť v roz
--- Ďalšie právne skutočnosti: Spoločnosť bola založená zakladateľskou zmluvou spísanou formou notárskej zápisnice N 60/2008, Nz 10281/2008 dňa 11.03.2008 v zmysle príslušných ustanovení z.č. 513/1991 Zb. Obchod
… [4697 more characters]
```
</details>

→ `Bash` — Fetch excluded-candidate sources batch 3
```sh
D=[tmp] for u in "https://oaklins.com/ar/en/deals/110583" "https://www.eterus.sk/" "https://www.caplight.com/investor/monogram" "https://www.podnikajte.sk/investor/private-equity-venture-fondy-sr" "https://altss.com/profile/pro-partners-holding" "https://www.papermark.com/blog/venture-capital-firms-bratislava" "https://en.ain.ua/2022/10/26/sandberg-capital-acquires-green-fox-academy"; do echo "#### $u"; $D/pg get "$u" 10 | head -1 | cut -c1-140; done
```

<details><summary>result</summary>

```
#### https://oaklins.com/ar/en/deals/110583
{"url": "https://oaklins.com/ar/en/deals/110583", "status": 200, "final_url": "https://www.oaklins.com/ar/en/deals/110583/", "ctype": "text/
#### https://www.eterus.sk/
{"url": "https://www.eterus.sk/", "status": 200, "final_url": "https://eterus.sk/", "ctype": "text/html; charset=UTF-8", "chars": 8747}
#### https://www.caplight.com/investor/monogram
{"url": "https://www.caplight.com/investor/monogram", "status": 200, "final_url": "https://www.caplight.com/investor/monogram", "ctype": "te
#### https://www.podnikajte.sk/investor/private-equity-venture-fondy-sr
{"url": "https://www.podnikajte.sk/investor/private-equity-venture-fondy-sr", "status": 200, "final_url": "https://www.podnikajte.sk/investo
#### https://altss.com/profile/pro-partners-holding
{"url": "https://altss.com/profile/pro-partners-holding", "status": 200, "final_url": "https://altss.com/profile/pro-partners-holding", "cty
#### https://www.papermark.com/blog/venture-capital-firms-bratislava
{"url": "https://www.papermark.com/blog/venture-capital-firms-bratislava", "status": 200, "final_url": "https://www.papermark.com/blog/ventu
#### https://en.ain.ua/2022/10/26/sandberg-capital-acquires-green-fox-academy
{"url": "https://en.ain.ua/2022/10/26/sandberg-capital-acquires-green-fox-academy", "status": 200, "final_url": "https://en.ain.ua/2022/10/2
```
</details>

→ `Bash` — Grep evidence sentences in batch 3
```sh
D=[tmp] $D/pg grep "https://oaklins.com/ar/en/deals/110583" "(Ethernum|Eterus).{0,200}" 100 | head -3; $D/pg grep "https://www.eterus.sk/" "(Zameriavame|2 - 2,5|private equity|buy).{0,150}" 80 | head -4; $D/pg grep "https://www.caplight.com/investor/monogram" "(Piano|20[01][0-9]|Company Date).{0,150}" 60 | head -4; $D/pg grep "https://www.podnikajte.sk/investor/private-equity-venture-fondy-sr" "(Arca).{0,200}" 60 | head -3; $D/pg grep "https://altss.com/profile/pro-partners-holding" "(Pro Partners).{0,200}" 30 | head -3; $D/pg grep "https://www.papermark.com/blog/venture-capital-firms-bratislava" "(BIC).{0,250}" 30 | head -3
```

<details><summary>result</summary>

```
6 hits (status 200, 6434 chars)
--- Eterus Capital has partnered with Dr. Martin to expand its dental clinic network | Deals | Oaklins Argentina: Mid-market M&A and financial advice globally Argentina What we do Team Deals Industries Insights News Careers Contact About Oaklins Our locations en / es Go to deals Private Equity | Healthcare Et
--- ts News Careers Contact About Oaklins Our locations en / es Go to deals Private Equity | Healthcare Eterus Capital has partnered with Dr. Martin to expand its dental clinic network May 2024 — Dr. Martin Dental Clinic, a leading network of dental clinics in Slovakia, has received a significant investment from Eterus Capital and Ethernum Capital to support its expansion across the country. The group aims 
4 hits (status 200, 8747 chars)
--- Eterus Capital – Private equity: Investujeme do vášho rastu Skip to content Hľadám investora Private equity Portfólio V médiách Kontakt Slovenčina English × Hľadám investora Private equity Portfólio V médiách Kontakt Slovenčina English Investujeme do vášho rast
--- ch Kontakt Slovenčina English Investujeme do vášho rastu Do inovácií sme formou private equity investovali už viac než 40 mil. EUR. Hľadám investora Tomáš Červenka, CEO „Eterus Capital sme oslovili koncom roku 2021 a oceňujeme korektnú a promptnú komunikáciu v celom procese transakcie, fér ... ový prístup (najmä s ohľadom 
--- om na Slovensku. Neponúkame dlhové financovanie. Investičné možnosti a horizont Zameriavame sa na investície v rozm
… [2662 more characters]
```
</details>

→ `Bash` — Fetch foreign-fund and misc sources
```sh
D=[tmp] for u in "https://www.credoventures.com/" "https://tech.eu/2022/06/23/presto-ventures-pulls-eur30-million-out-of-its-hat-with-second-fund-aimed-squarely-at-cee-region-startups/" "https://pitchbook.com/profiles/investor/157578-04" "https://cc.cz/novy-cesky-investicni-fond-nation-1-ma-pro-startupy-500-milionu-korun-do-konce-roku-nabere-temer-miliardu/" "https://www.orsr.sk/vypis.asp?ID=640476&SID=8&P=0" "https://cc.cz/chceme-z-ceska-moderni-ekonomiku-ne-skanzen-rika-sef-jet-ventures-a-vyjmenovava-5-nejvetsich-prekazek/" "https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html" "https://www.slovca.sk/sk/riadni-clenovia/arx-equity-partners.html" "https://www.slovca.sk/sk/riadni-clenovia/cvi.html" "https://www.startitup.sk/od-cambridge-az-po-bratislavu-vznikol-novy-fond-na-podporu-europskych-talentov-chce-investovat-80-milionov-eur/" "https://pitchbook.com/profiles/investor/1405189-00" "https://spectator.sme.sk/business/c/swiss-re-adds-to-its-ssc-in-bratislava" "https://incubatorlist.com/top-vcs-in-slovakia"; do echo "#### $u"; $D/pg get "$u" 10 | head -1 | cut -c1-140; done
```

<details><summary>result</summary>

```
#### https://www.credoventures.com/
{"url": "https://www.credoventures.com/", "status": 200, "final_url": "https://www.credoventures.com/", "ctype": "text/html", "chars": 3919}
#### https://tech.eu/2022/06/23/presto-ventures-pulls-eur30-million-out-of-its-hat-with-second-fund-aimed-squarely-at-cee-region-startups/
{"url": "https://tech.eu/2022/06/23/presto-ventures-pulls-eur30-million-out-of-its-hat-with-second-fund-aimed-squarely-at-cee-region-startup
#### https://pitchbook.com/profiles/investor/157578-04
{"url": "https://pitchbook.com/profiles/investor/157578-04", "status": 403, "final_url": "https://pitchbook.com/profiles/investor/157578-04"
#### https://cc.cz/novy-cesky-investicni-fond-nation-1-ma-pro-startupy-500-milionu-korun-do-konce-roku-nabere-temer-miliardu/
{"url": "https://cc.cz/novy-cesky-investicni-fond-nation-1-ma-pro-startupy-500-milionu-korun-do-konce-roku-nabere-temer-miliardu/", "status"
#### https://www.orsr.sk/vypis.asp?ID=640476&SID=8&P=0
{"url": "https://www.orsr.sk/vypis.asp?ID=640476&SID=8&P=0", "status": 200, "final_url": "https://www.orsr.sk/vypis.asp?ID=640476&SID=8&P=0"
#### https://cc.cz/chceme-z-ceska-moderni-ekonomiku-ne-skanzen-rika-sef-jet-ventures-a-vyjmenovava-5-nejvetsich-prekazek/
{"url": "https://cc.cz/chceme-z-ceska-moderni-ekonomiku-ne-skanzen-rika-sef-jet-ventures-a-vyjmenovava-5-nejvetsich-prekazek/", "status": 20
#### https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html
{"url": "https://www.slovca.sk/sk/clenstvo/riadni-clenovia.ht
… [1380 more characters]
```
</details>

→ `Bash` — Grep Credo, Presto, Nation 1, Jet sources
```sh
D=[tmp] $D/pg grep "https://www.credoventures.com/" "(Prague|Kraków|Krakow|Warsaw|Bratislava).{0,120}" 80 | head -3; $D/pg grep "https://tech.eu/2022/06/23/presto-ventures-pulls-eur30-million-out-of-its-hat-with-second-fund-aimed-squarely-at-cee-region-startups/" "(Prague|Czech).{0,150}" 100 | head -3; $D/pg grep "https://cc.cz/novy-cesky-investicni-fond-nation-1-ma-pro-startupy-500-milionu-korun-do-konce-roku-nabere-temer-miliardu/" "(Nation 1).{0,150}" 60 | head -3; $D/pg grep "https://www.orsr.sk/vypis.asp?ID=640476&SID=8&P=0" "(Obchodné meno: .{0,50}|Jet.{0,160})" 0 | head -4
```

<details><summary>result</summary>

```
4 hits (status 200, 3684 chars)
--- – we want to hear from you. No deck required. No warm intro. ↓ Logo 16:39 , CET Prague Karlovo Náměstí 10 120 00, Prague Czech Republic 16:39 , CET Kraków Lubomirskiego 20 31-509 Kraków Poland ©2026 Credo Ventures. Contact (CV.) info@credoventures.com +420211153211 Follow LinkedIn, X I
--- – we want to hear from you. No deck required. No warm intro. ↓ Logo 16:39 , CET Prague Karlovo Náměstí 10 120 00, Prague Czech Republic 16:39 , CET Kraków Lubomirskiego 20 31-509 Kraków Poland ©2026 Credo Ventures. Contact (CV.) info@credoventures.com +420211153211 Follow LinkedIn, X P
1 hits (status 200, 6224 chars)
--- o just that. Dan Taylor 23 June 2022 1 Share Facebook Twitter Linkedin Share 1 Send email Copy link Prague-based Presto Ventures has announced the close of its second fund at a magnificent €30 million. Making no bones about it, the princes of Praha are looking to make seed and pre-seed round investments in no less than 40 B2B startups hailing from the CE
14 hits (status 200, 11009 chars)
--- Nový český investiční fond Nation 1 má pro startupy 500 milionů korun. Do konce roku nabere téměř miliardu - CzechCrunch Přejít k obsahu | Přejít k hlavnímu menu | Přejít k vyhledávání Venture – 02. 8. 2019 – 3 min čtení Nový český investiční fo
--- ture – 02. 8. 2019 – 3 min čtení Nový český investiční fond Nation 1 má pro startupy 500 milionů korun. Do konce roku nabere téměř miliardu Ondřej Holzman 0 Zobrazit komentáře Sdílet Insider Foto: Nation 1
… [511 more characters]
```
</details>

→ `Bash` — Read SLOVCA lists, United Founders, incubatorlist
```sh
D=[tmp] $D/pg text "https://www.slovca.sk/sk/clenstvo/riadni-clenovia.html" 0 1500 | tr '\n' '|'; echo; $D/pg text "https://www.slovca.sk/sk/riadni-clenovia/arx-equity-partners.html" 0 600 | tr '\n' '|'; echo; $D/pg text "https://www.slovca.sk/sk/riadni-clenovia/cvi.html" 0 700 | tr '\n' '|'; echo; $D/pg grep "https://www.startitup.sk/od-cambridge-az-po-bratislavu-vznikol-novy-fond-na-podporu-europskych-talentov-chce-investovat-80-milionov-eur/" "(United Founders|Cambridge|sídl).{0,200}" 60 | head -4; $D/pg grep "https://incubatorlist.com/top-vcs-in-slovakia" "(Monopoly).{0,200}" 100 | head -3
```

<details><summary>result</summary>

```
Riadni členovia / Slovak Venture Capital & Private Equity Association SLOVCA|Riadni členovia|ARX Equity Partners|CVI|Enterprise Investors|Eterus Capital|Fond inovácií a technológií|Genesis Capital|Jet Investment|Národný holdingový fond s.r.o.|Neulogy Ventures|Sandberg Capital|Venture to Future Fund|Vision Ventures|Členstvo|Riadni členovia|Pridružení členovia|Partnerskí členovia|Partneri|Etický kódex|Prihláška|Čerstvé správy!|Prihláste sa na odber noviniek SLOVCA a získajte informácie o private equity trhu v EU a na Slovensku ako aj najnovšie štatistiky o investovanom rozvojovom kapitáli.|Registrovať|Slovak Venture Capital & Private Equity Association SLOVCA|+421-2-21 201 010|slovca@slovca.sk|Štúrova 12/4, 811 02 Bratislava-Staré Mesto|Slovakia|O nás|SLOVCA dnes|Správna rada|Legal & Tax Committee|Stanovy|Členstvo|Riadni členovia|Pridružení členovia|Partnerskí členovia|Partneri|Etický kódex|Prihláška|Na stiahnutie|Štatistiky|Tlačové správy|Vzorové dokumenty|Novinky|Novinky ohľadom PE-VC|Podujatia|Web vytvoril|Fresh idea|. Dizajn Michaela Lipková.|
ARX Equity Partners / Slovak Venture Capital & Private Equity Association SLOVCA|ARX Equity Partners|Preferovaná výška investície : EUR 10-50 mil.|Objem prostriedkov v správe: EUR 300 mil. (total commitments since inception)|Preferované odvetvie: bez preference|Geografické zameranie: Central Europe|Kontakná osoba : Michal Aron|Email: aron@arxequity.com|Web:|https://arxequity.com/|Prílohy na stiahnutie|5-logo-File-arx_new--336x336.jpg|
… [2721 more characters]
```
</details>

→ `Bash` — Fetch Genesis, Enterprise, J&T, EVP sites
```sh
D=[tmp] $D/pg grep "https://www.startitup.sk/od-cambridge-az-po-bratislavu-vznikol-novy-fond-na-podporu-europskych-talentov-chce-investovat-80-milionov-eur/" "(Cambridge, |Paríž|Zürich|Berlín|kancel|pobočk).{0,200}" 120 | head -3; for u in "https://www.genesiscapital.cz/" "https://www.ei.com.pl/en/" "https://www.jtventures.cz/" "https://www.energyventurepals.com/" "https://evp.vc/"; do echo "#### $u"; $D/pg get "$u" 10 | head -1 | cut -c1-160; done
```

<details><summary>result</summary>

```
2 hits (status 200, 8604 chars)
--- né na starnutie populácie, kyberbezpečnosť, energetiku, vesmírne inovácie a agentovú umelú inteligenciu,“ hovorí Horký. Cambridge, Mníchov, Bratislava Fond má fyzické zastúpenie v hlavných technologických centrách Európy – od Cambridge, Paríža, Zürichu a Berlína, až po Bratislavu, kde je jedným z managing partnerov aj Václav Pavlečka, známy z Czech Founders VC. Ambíciou fondu je prepojiť roztrieštený európsky trh, vytvoriť funkčnú sieť medzi unive
--- jich partnerov a investorov sa fond dostane do priameho kontaktu s elitnými akademickými inštitúciami ako University of Cambridge, Oxford, Technická univerzita v Mníchove, ETH Zürich, ale aj Akadémia vied Českej republiky. To znamená, že výskum v laboratóriu nebude končiť v zásuvke, ale bude mať priamo prístup k mentorom, financovaniu a k trhu s viac ako 233 miliónmi obyvateľov. Tím s globálnymi skúsenosťami Za fondom nestojí len kapitál a vízia, 
#### https://www.genesiscapital.cz/
{"url": "https://www.genesiscapital.cz/", "error": "ConnectionError(ProtocolError('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer')))"
#### https://www.ei.com.pl/en/
{"url": "https://www.ei.com.pl/en/", "status": 200, "final_url": "https://www.ei.com.pl/en/", "ctype": "text/html; charset=UTF-8", "chars": 947}
#### https://www.jtventures.cz/
{"url": "https://www.jtventures.cz/", "status": 200, "final_url": "https://www.jtventures.cz/", "ctype": "text/html; charset=utf-8", "chars": 1786}
###
… [346 more characters]
```
</details>

→ `Bash` — Read Enterprise, J&T, EVP, Genesis pages
```sh
D=[tmp] $D/pg text "https://www.ei.com.pl/en/" 0 950 | tr '\n' '|'; echo; $D/pg text "https://www.jtventures.cz/" 0 1800 | tr '\n' '|'; echo; $D/pg text "https://evp.vc/" | tr '\n' '|'; echo; $D/pg get "https://www.genesiscapital.cz/" --force --curl 10 | head -1 | cut -c1-200
```

<details><summary>result</summary>

```
Enterprise Investors|We finance the development of|dynamically growing companies|About us|We are the most experienced private equity investor in Central and Eastern Europe.|Since 1990, we have been supporting the development of high-potential companies by providing the capital and expertise necessary to implement ambitious growth strategies.|Read more|News|October 06, 2026|18GYM and Stay Fit Gym join forces with backing from Enterprise Investors|Read more|July 01, 2026|Enterprise Investors returns to Lithuania with investment in Kredito unija "Saulėgrąža"|Read more|June 11, 2026|Enterprise Investors to sell MOYA owner Anwim to Stonepeak and Energy Equation Partners|Read more|March 16, 2026|EI re-enters the renewables sector with majority investment in Art Wind|Read more|Varso Tower|69 Chmielna Street, 34th floor|00-801 Warsaw|tel.: +48 22 458 85 00|About us|Team|Investments|News|Contact|LP login|GDPR information|clause|Get directions|
J&T Ventures|English|Náš přístup|Portfolio|Tým|Blog|Kontakt|J&T Ventures, budova J&T Banka|Sokolovská 700/113a (|5. patro|)|Praha 8 – Karlín, 186 00|Pošlete pitch deck|Podporujeme|CEE & SEE|foundery s globální ambicí|Tomáš Malovec|Born Digital|Jan Čurn|Apify|Petr Dvořák|Wultra|Petr Jahn|SprayVision|Marin Curkovic|AEOS (AdScanner)|Klára Losert|Talkbase|Tomáš Turek|Daytrip|Portfolio|€120M|Výše aktiv|31|Startupů|5|Exitů|Pošlete pitch deck|Zajímají nás|B2B|B2C|Marketplaces|Sector Agnostic|Potfolio startupů|Investiční kritéria|Region|CEE & SEE|& Balt
… [1777 more characters]
```
</details>

→ `Bash` — Fetch EIF Czech fund managers list
```sh
D=[tmp] u="https://www.eif.org/files/attachments/czech-republic-equity-fundmanagers.pdf"; $D/pg get "$u" 10 | head -1 | cut -c1-200; $D/pg grep "$u" "(Genesis|Nation 1|Credo|Presto|J&T|Energy Venture|Jet).{0,200}" 0 | head -8
```

<details><summary>result</summary>

```
{"url": "https://www.eif.org/files/attachments/czech-republic-equity-fundmanagers.pdf", "status": 404, "final_url": "https://www.eif.org/files/attachments/czech-republic-equity-fundmanagers.pdf", "cty
0 hits (status 404, 0 chars)
```
</details>

→ `WebSearch` EIF "equity fund partners" Czech Republic fund managers pdf eif.org attachments

<details><summary>result</summary>

```
Web search results for query: "EIF "equity fund partners" Czech Republic fund managers pdf eif.org attachments"

Links: [{"title":"czechia equity fundmanagers","url":"https://www.eif.org/files/attachments/czechia-equity-fundmanagers.pdf"},{"title":"czechia equity fundmanagers","url":"https://lb.eif.org/files/attachments/czechia-equity-fundmanagers.pdf"},{"title":"What we do","url":"https://www.eif.org/what_we_do/resources/rrf-czech-republic/index"},{"title":"What we do","url":"https://eif.org/what_we_do/resources/esif-fund-of-funds-czech-republic/index.htm"},{"title":"rrf czech republic","url":"https://www.eif.org/products/all/rrf-czech-republic"},{"title":"czech republic fund of funds","url":"https://eif.org/what_we_do/equity/news/2017/czech_republic_fund_of_funds.htm"},{"title":"80 million central europe fund of funds to support smes and small mid caps","url":"https://eif.org/what_we_do/equity/news/2018/80-million-central-europe-fund-of-funds-to-support-smes-and-small-mid-caps.htm"},{"title":"eif launches eur 80 million central europe fund funds support smes small mid caps","url":"https://dailynewshungary.com/eif-launches-eur-80-million-central-europe-fund-funds-support-smes-small-mid-caps/"},{"title":"What we do","url":"https://www.eif.org/what_we_do/equity/news/2023/czech-republicand-eif-launch-55-million-fund-of-funds-for-digital-technologies-backed-by-recovery-and-resilience-facility.htm"}]

The search turned up an EIF PDF that matches your query. It's titled "czechia e
… [863 more characters]
```
</details>

→ `Bash` — Fetch EIF Czechia fund managers PDF
```sh
D=[tmp] u="https://www.eif.org/files/attachments/czechia-equity-fundmanagers.pdf"; $D/pg get "$u" 10 | head -1 | cut -c1-200; $D/pg text "$u" 0 4000
```

<details><summary>result</summary>

```
{"url": "https://www.eif.org/files/attachments/czechia-equity-fundmanagers.pdf", "status": 200, "final_url": "https://www.eif.org/files/attachments/czechia-equity-fundmanagers.pdf", "ctype": "applicat
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
Multi-Country Venture Capital ICT Early Stage Fun
… [1067 more characters]
```
</details>

→ `WebSearch` "Energy Venture Pals" Prague fund

<details><summary>result</summary>

```
Web search results for query: ""Energy Venture Pals" Prague fund"

Links: [{"title":"Energy Venture Pals Overview","url":"https://pitchbook.com/profiles/investor/1405189-00"},{"title":"Energy Venture Pals (investor - Others)","url":"https://nordic9.com/companies/energy-venture-pals/"},{"title":"Inven Capital","url":"https://privateequitylist.com/investors/inven-capital"},{"title":"inven capital","url":"https://startupintros.com/orgs/inven-capital"},{"title":"nabidka soukromeho investicniho fondu","url":"https://biom.cz/cz/novinky/nabidka-soukromeho-investicniho-fondu"},{"title":"Energy Venture Capital Firms in Czech Republic2","url":"https://privateequitylist.com/investors/venture-capital/czech-republic/energy"},{"title":"Clifford Chance advises EIB on its first equity investment in the Czech Republic","url":"https://www.cliffordchance.com/news/news/2018/01/clifford-chance-advises-eib-on-its-first-equity-investment-.html"},{"title":"venture capital firms prague","url":"https://www.papermark.com/blog/venture-capital-firms-prague.md"},{"title":"cps fund","url":"https://village.ai/company/cps-fund"},{"title":"300+ investors in your industry, stage, and region Get","url":"https://shizune.co/investors/energy-vc-funds-czech-republic"}]

I found limited public information on Energy Venture Pals, and it looks like a small Prague-based investor.

- **Profile:** PitchBook lists the firm as an active venture investor with its office in Prague. Its profile shows its investor status as ac
… [862 more characters]
```
</details>

→ `Bash` — Fetch EVP Nordic9 profile and Webout article mention
```sh
D=[tmp] u="https://nordic9.com/companies/energy-venture-pals/"; $D/pg get "$u" 10 | head -1 | cut -c1-200; $D/pg grep "$u" "(Prague|Czech|Energy Venture Pals).{0,160}" 60 | head -4; $D/pg grep "https://www.omediach.com/internet/30236-seed-starter-slovenskej-sporitelne-investuje-400-tisic-eur-do-startupu-webout-ten-ziskava-spolu-1-65-miliona-eur-a-mieri-do-silicon-valley" "(Energy Venture Pals|pražsk|česk).{0,200}" 100 | head -3
```

<details><summary>result</summary>

```
{"url": "https://nordic9.com/companies/energy-venture-pals/", "status": 200, "final_url": "https://nordic9.com/companies/energy-venture-pals/", "ctype": "text/html; charset=utf-8", "chars": 3810}
12 hits (status 200, 3810 chars)
--- Energy Venture Pals (investor) - Nordic9.com Go Close × Sign in Sign up Menu × Intel Countries Rankings People discovery Investor fit Dry powder tracker Signals Graded investment deals Startup radar Stealth founders New funds Network track
---  investors All investment deals M&A and Secondary Get intel Energy Venture Pals (investor - Others) See something wrong or missing? Let us know Offices: Prague Average round investment: 1.93m USD Average number per year: 1.00 Distribution: 2026 (1) See the entire list Portfolio companies: Webout Se
--- io companies: Webout See the entire list Mostly invests in: Czech Republic (1) AI (1) Investments You need an account to access this feature. Log in or create one from here . Do you have a question? Talk to us . Investors with similar profile to Energy Venture Pals Name Criteria Sebas
8 hits (status 200, 9612 chars)
--- ieri do Silicon Valley Komentáre Hoaxy TV Rádio Tlač Internet Reklama Ďalšie Marketing Obchod Filmy Česko Koncesionárske Stručne Tlačové správy Seed Starter Slovenskej sporiteľne investuje 400-tisíc eur do startupu Webout. Ten získava spolu 1,65 milióna eur a mieri do Silicon Valley 08.06.2026 | Internet | PR | Slovenská sporiteľňa Zdroj: Webout Seed Starter Slovenskej sporiteľne vedie investič
… [416 more characters]
```
</details>

→ `WebSearch` Swiss Re Bratislava centre office employees Slovakia

<details><summary>result</summary>

```
Web search results for query: "Swiss Re Bratislava centre office employees Slovakia"

Links: [{"title":"www.profesia.sk","url":"https://www.profesia.sk/praca/swiss-re/O3760981"},{"title":"Можливість для людей з України","url":"https://www.profesia.sk/praca/swiss-re/O4527374"},{"title":"www.profesia.sk","url":"https://www.profesia.sk/praca/swiss-re/O3876540"},{"title":"11. May 2015 at 06:30","url":"https://spectator.sme.sk/business/c/swiss-re-adds-to-its-ssc-in-bratislava"},{"title":"Service Center Process Manager (Ref. No.: 87245)","url":"https://www.profesia.sk/praca/swiss-re/O3377785"},{"title":"2. April 2019 at 14:58","url":"https://spectator.sme.sk/business/c/the-lack-of-a-labour-force-is-a-myth-says-swiss-re-managing-director"},{"title":"Employer Branding Associate","url":"https://www.profesia.sk/praca/swiss-re/O3511911"},{"title":"Reinsurance Account Analyst","url":"https://www.profesia.sk/praca/swiss-re/O3485511"},{"title":"www.profesia.sk","url":"https://www.profesia.sk/en/work/swiss-re/O2769294"}]

Swiss Re's Bratislava centre has grown substantially, though the sources give different headcounts because they date from different years.

- **Early growth:** A 2015 Slovak Spectator article said the branch started eight years earlier with 25 employees and had become one of Slovakia's biggest shared service centres. At the end of 2014, it employed 800 experts offering support in finance, assets administration, investing and risk management. It also planned expansion of 40
… [1073 more characters]
```
</details>

→ `Bash` — Fetch Swiss Re job postings
```sh
D=[tmp] for u in "https://www.profesia.sk/praca/swiss-re/O3377785" "https://www.profesia.sk/praca/swiss-re/O3760981"; do $D/pg get "$u" 10 | head -1 | cut -c1-150; $D/pg grep "$u" "(Service Cent|branch|Bratislava).{0,160}" 60 | head -3; done
```

<details><summary>result</summary>

```
{"url": "https://www.profesia.sk/praca/swiss-re/O3377785", "status": 200, "final_url": "https://www.profesia.sk/praca/swiss-re/O3377785", "ctype": "te
8 hits (status 200, 6632 chars)
--- Service Center Process... - Swiss Re | PROFESIA.SK Úvodná stránka Hľadanie práce Service Center Process Manager × Ľutujeme, spoločnosť ponúkajúca danú pracovnú pozíciu ukončila zverejnenie ponuky na stránke. Ďakujeme za porozumenie.
--- a stránke. Ďakujeme za porozumenie. Zobraziť podobné ponuky Service Center Process Manager Place of work Mlynské nivy 12, Bratislava Contract type full-time Wage (gross) From 2 500 EUR/month Minimum base salary for this job from 2500 EUR gross/month/full time. Our offer to you may be higher 
{"url": "https://www.profesia.sk/praca/swiss-re/O3760981", "status": 200, "final_url": "https://www.profesia.sk/praca/swiss-re/O3760981", "ctype": "te
3 hits (status 200, 7870 chars)
--- iť podobné ponuky Reinsurance Account Analyst Place of work Bratislava Contract type full-time Wage (gross) Minimum base salary for this job from 1100 EUR gross/month/full time. Our offer to you may be higher based on your skills and experience and will include additional rewards and benef
--- orporations and public sector clients. Swiss Re's center in Bratislava opened 10 years ago and has already grown into one of the most important locations within the Group. What will you do? If you want to learn the core of reinsurance business, our department is the right place to start an
```
</details>

→ `Bash` — Check ORSR no-match search pages
```sh
D=[tmp] for u in "https://www.orsr.sk/hladaj_subjekt.asp?OBMENO=Prv%E1+kapit%E1lov%E1&PF=0&R=on" "https://www.orsr.sk/hladaj_subjekt.asp?OBMENO=Gapfunding&PF=0&R=on"; do $D/pg get "$u" 10 | head -1 | cut -c1-150; $D/pg text "$u" 0 1500 | tr '\n' '|' | cut -c1-900; echo; done
```

<details><summary>result</summary>

```
{"url": "https://www.orsr.sk/hladaj_subjekt.asp?OBMENO=Prv%E1+kapit%E1lov%E1&PF=0&R=on", "status": 200, "final_url": "https://www.orsr.sk/hladaj_subje
Obchodný register SR - Výsledky vyhľadávania podľa obchodného mena subjektu|MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY|OBCHODNÝ REGISTER|NA INTERNETE|Slovensky|||English|Výsledky vyhľadávania podľa obchodného mena subjektu|( vyhľadávanie len v aktuálnych záznamoch )|Obchodné meno začína:|prvakapitalova|Právna forma:|akákoľvek|Súd:|akýkoľvek|Stránka:|0 / 0|Záznamy:|0 - 0 / 0|Dátum:|11.10.2026|Kritériám vyhľadávania nezodpovedá žiadny záznam!|Aktuálne zmeny|||Elektronické služby Obchodného registra|||Vyhľadávanie podnikov v EÚ|Vyhľadávanie podľa :|obchodného mena|||identifikačného čísla|sídla|||spisovej značky|||priezviska a mena osoby|O obchodnom registri SR|||Návod na používanie ORI|||Kontakty na registrové súdy|Aktuality a oznamy|
{"url": "https://www.orsr.sk/hladaj_subjekt.asp?OBMENO=Gapfunding&PF=0&R=on", "status": 200, "final_url": "https://www.orsr.sk/hladaj_subjekt.asp?OBME
Obchodný register SR - Výsledky vyhľadávania podľa obchodného mena subjektu|MINISTERSTVO SPRAVODLIVOSTI SLOVENSKEJ REPUBLIKY|OBCHODNÝ REGISTER|NA INTERNETE|Slovensky|||English|Výsledky vyhľadávania podľa obchodného mena subjektu|( vyhľadávanie len v aktuálnych záznamoch )|Obchodné meno začína:|gapfunding|Právna forma:|akákoľvek|Súd:|akýkoľvek|Stránka:|0 / 0|Záznamy:|0 - 0 / 0|Dátum:|11.10.2026|Kritériám vyhľadávania nezodpovedá žiadny záznam!|Akt
… [293 more characters]
```
</details>

→ `Bash` — Get dates and quotes for SmartHead, cc.cz, Matsuko, vestbee
```sh
D=[tmp] $D/pg grep "https://sita.sk/seed-starter-slovenskej-sporitelne-hlasi-prvu-investiciu-podporil-slovensky-startup-smarthead/" "([0-9]{1,2}\. ?[0-9]{1,2}\. ?2023|[0-9]{1,2}\. (septembra|augusta|októbra) 2023).{0,40}" 40 | head -3; $D/pg grep "https://cc.cz/ceska-sporitelna-jde-podporovat-startupy-i-na-slovensko-pro-tamni-mlade-firmy-ma-pres-120-milionu/" "(– [0-9]{2}\. [0-9]{1,2}\. 20[0-9]{2}).{0,20}" 30 | head -2; u="https://www.startitup.sk/kosicky-startup-matsuko-ziskal-takmer-milionovu-investiciu-obsadzuje-svetovy-trh/"; $D/pg get "$u" 10 | head -1 | cut -c1-120; $D/pg grep "$u" "(IPM).{0,200}" 150 | head -2; u="https://www.vestbee.com/insights/articles/top-vc-funds-in-slovakia-to-finance-your-startup"; $D/pg get "$u" 10 | head -1 | cut -c1-120; $D/pg grep "$u" "(CB Investment|CBIM|LRJ|IPM).{0,300}" 30 | head -4
```

<details><summary>result</summary>

```
1 hits (status 200, 8146 chars)
--- oblasti udržateľnosti a ESG reportingu. 05. 09. 2023 14:00 - Aktualizované 05. 09. 2023 14:05 Informačný servis 4 min. čítania Foto:
1 hits (status 200, 9349 chars)
--- Přejít k vyhledávání Startupy – 08. 9. 2022 – 2 min čtení Slovenská spořitelna bude investova
{"url": "https://www.startitup.sk/kosicky-startup-matsuko-ziskal-takmer-milionovu-investiciu-obsadzuje-svetovy-trh/", "s
1 hits (status 200, 5780 chars)
--- orúčaní Pridať ako preferovaný zdroj Startitup, odkaz sa otvorí v novom okne V prvom A kole investície sú hlavnými investormi anglicko-slovenský fond IPM spolu so súčasnými investormi z Neulogy Ventures, Granpool Hungary a sli.do. Do financovania technologického startupu sa zapojili aj tzv. „anjelskí investori“ Šimon Šicko (Pixel Federation) alebo Miklos Kobor. Matsuko sa stala prvou firmou, do ktorej investovala slovenská úspešná firma sli.do. Firma ponúka aj technológiu, ktorá prepája stretnutia 
{"url": "https://www.vestbee.com/insights/articles/top-vc-funds-in-slovakia-to-finance-your-startup", "status": 200, "fi
6 hits (status 200, 12192 chars)
--- rful Medical , and Medannot . CB Investment Management Geography: Slovakia Preferred industries: Various industries Investment ticket: up to €1.6M Company stage: Seed The Bratislava-based CB Investment Management has under its management a fund focused on early stage Slovakian startups with international potential. Apart from capital, young and innovative companies are s
--- Data
… [726 more characters]
```
</details>

→ `Bash` — Check Matsuko and vestbee article dates
```sh
D=[tmp] $D/pg grep "https://www.startitup.sk/kosicky-startup-matsuko-ziskal-takmer-milionovu-investiciu-obsadzuje-svetovy-trh/" "[0-9]{1,2}\. [a-zá]+ 2019 o" 30 | head -2; $D/pg grep "https://www.vestbee.com/insights/articles/top-vc-funds-in-slovakia-to-finance-your-startup" "(20(19|20|21|22|23|24|25|26)) · .{0,20}|[A-Z][a-z]+ [0-9]{1,2}, 20[0-9]{2}" 20 | head -3; $D/pg grep "https://www.crowdberry.eu/en" "(ECSPR|licen).{0,120}" 60 | head -2
```

<details><summary>result</summary>

```
0 hits (status 200, 5780 chars)
2 hits (status 200, 12192 chars)
--- Join here Join here October 8, 2020 · 8 min read Konrad
--- e capital #Slovakia October 8, 2020 Latest news Oct 09 
1 hits (status 200, 12925 chars)
--- er in 5 minutes No opening fees Only verified opportunities ECSPR licensed ECSPR licensed 16,705 registered 16,705 registered from EUR 1,000 from EUR 1,000 Investments involve risk. Risk comes with return. Be sensible. Active investment opportun
```
</details>

→ `Bash` — Find Matsuko article date
```sh
D=[tmp] $D/pg grep "https://www.startitup.sk/kosicky-startup-matsuko-ziskal-takmer-milionovu-investiciu-obsadzuje-svetovy-trh/" "20(19|20) " 60 | head -3; f=$D/cache/$(python3 -c "import hashlib,sys;print(hashlib.sha1(sys.argv[1].encode()).hexdigest())" "https://www.startitup.sk/kosicky-startup-matsuko-ziskal-takmer-milionovu-investiciu-obsadzuje-svetovy-trh/").raw; grep -oE '"datePublished":"[^"]+"' $f | head -2
```

<details><summary>result</summary>

```
2 hits (status 200, 5780 chars)
--- vú investíciu, obsadzuje svetový trh Adam Sipos 11. októbra 2019 o 15:32 Košický startup Matsuko sa môže pochváliť novou inve
--- i aj známi Slováci. Facebook/Matsuko Adam Sipos 11. októbra 2019 o 15:32 Uložiť Uložené Zdieľať Košický startup Matsuko , kto
"datePublished":"2019-10-11T13:32:18+00:00"
"datePublished":"2019-10-11T13:32:18+00:00"
```
</details>

→ `Write` [tmp]

<details><summary>result</summary>

```
File created successfully at: [tmp] (file state is current in your context — no need to Read it back)
```
</details>

→ `Bash` — Build records and verify all quotes
```sh
D=[tmp] cd $D && sed -i '' 's|"type": "accelerator", "hq": {"country": "SK", "city": "Bratislava"}, "website": FF_G,|"type": "accelerator", "hq": {"country": "SK", "city": "Bratislava"}, "website": None,|' build.py && /Users/[redacted]/homeW/ai-dev-test/investor-db/.venv/bin/python build.py && $D/pg verifyall /Users/[redacted]/homeW/ai-dev-test/investor-db/data/sample/parts/sk.json $D/note_evidence.json
```

<details><summary>result</summary>

```
49 {'included': 7, 'uncertain': 1, 'dormant': 6, 'excluded': 35} 47
FAIL lrj-capital decision.note https://lrjcapital.com/ | LrjCapital.com is for sale
verified 115, failed 1
```
</details>

→ `Bash` — Check LRJ domain page text
```sh
D=[tmp] $D/pg grep "https://lrjcapital.com/" "for sale.{0,60}" 60 | head -3
```

<details><summary>result</summary>

```
0 hits (status 0, 0 chars)
```
</details>

→ `Bash` — Refetch LRJ domain and inspect redirects
```sh
D=[tmp] $D/pg get "https://lrjcapital.com/" --force 300; curl -sIL -m 30 -A "Mozilla/5.0" https://lrjcapital.com/ | grep -iE "^(HTTP|location)"
```

<details><summary>result</summary>

```
{"url": "https://lrjcapital.com/", "status": 200, "final_url": "https://www.hugedomains.com/domain_profile.cfm?d=lrjcapital.com", "ctype": "text/html; charset=utf-8", "chars": 5463}
LrjCapital.com is for sale | HugeDomains
Skip to main content
Search
+1-303-893-0552
LrjCapital.com
Buy now:
$1,995
▸ Buy now
Processing
or
▸ Start payment plan
Processing
Only $83.13/mo. for 24 months
See details
30-day money back guarantee
Take immediate ownership
Safe and secure shopping
LrjCapital.com
This domain is for sale:
$1,995
Buy now for
$1,995
or pay
$83.13
per month for 24 months
▸ Buy now
Processing
or
▸ Start payment plan
Processing
Make 24 monthly payments
Pay 0% interest
Start using the domain today.
See details
Make 24 monthly payments
Pay 0% interest
Start using the domain today.
See details
This domain is for sale:
$1,995
▸ Buy now
Processing
or
▸ Start payment plan
Processing
Only $83.13/mo. for 24 months
See details
Favorite
Questions? Talk to a domain expert:
1‑303‑893‑0552
Enjoy zero percent financing
Quick delivery of the domain
Safe and secure shopping
Since 2005, we've helped thousands of people get the perfect domain name
R
Fast great, reliable service. Helped us secure the domain quickly and transfer it our server.
- Robert Patterson, September 28, 2026
D
Great job. Easy process. Thorough follow through.
- David Hucks, September 25, 2026
T
Very quick, flexible and efficient.
- Timothy Morson, September 21, 2026
T
Great business. Easy purchase and transfer process.
- Th
… [193 more characters]
```
</details>

→ `Bash` — Re-verify quotes and run project validator
```sh
D=[tmp] $D/pg verifyall /Users/[redacted]/homeW/ai-dev-test/investor-db/data/sample/parts/sk.json $D/note_evidence.json; cd /Users/[redacted]/homeW/ai-dev-test/investor-db && .venv/bin/python -m investordb validate --records data/sample/parts/sk.json --today 2026-10-11
```

<details><summary>result</summary>

```
verified 116, failed 0
WARNING zaka-vc: excluded without an E rule
WARNING sandberg-capital: excluded without an E rule
WARNING eterus-capital: excluded without an E rule
WARNING ethernum-capital: excluded without an E rule
WARNING narodny-holdingovy-fond: excluded without an E rule
WARNING slovak-investment-holding: excluded without an E rule
WARNING credo-ventures: excluded without an E rule
WARNING presto-ventures: excluded without an E rule
WARNING jt-ventures: excluded without an E rule
WARNING nation-1: excluded without an E rule
WARNING jet-investment: excluded without an E rule
WARNING genesis-capital: excluded without an E rule
WARNING arx-equity-partners: excluded without an E rule
WARNING enterprise-investors: excluded without an E rule
WARNING united-founders: excluded without an E rule
WARNING energy-venture-pals: excluded without an E rule
WARNING swiss-re-bratislava: excluded without an E rule
WARNING prva-kapitalova: excluded without an E rule
WARNING gapfunding: excluded without an E rule
WARNING monopoly-ventures: excluded without an E rule
49 records, 0 errors, 20 warnings
```
</details>

→ `Bash` — Drop unsupported fund link and rebuild, show decisions
```sh
D=[tmp] cd $D && python3 - <<'EOF'
p='build.py'; s=open(p).read()
old='''              "Founders Factory March 11th 2025 / 3 min read We’re excited to announce our latest G-Force climate investment— Enzidia")],
            fund="G-Force Fund II"),'''
new='''              "Founders Factory March 11th 2025 / 3 min read We’re excited to announce our latest G-Force climate investment— Enzidia")]),'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
/Users/[redacted]/homeW/ai-dev-test/investor-db/.venv/bin/python build.py && cat /Users/[redacted]/homeW/ai-dev-test/investor-db/data/sample/parts/sk-decisions.md
```

<details><summary>result</summary>

```
49 {'included': 7, 'uncertain': 1, 'dormant': 6, 'excluded': 35} 47
# Slovak VC pilot — candidate decisions

Source: research/sk-vc-candidates.json (49 candidates). Accessed 2026-10-11. Records: data/sample/parts/sk.json.

Counts: included 7, uncertain 1, dormant 6, excluded 35.

Format: name — status — rule IDs — reason. For excluded records the rule is the one that excludes; 'none (out of pilot scope)' marks real investors that no E rule excludes but that are not Slovak-managed VC (foreign, PE, public). I1/I2 on an excluded or uncertain record means that inclusion rule fails or is unproven.

- Neulogy Ventures — included — I1, I2, I3, I4 — Slovak manager (ORSR, SLOVCA full member, EIF-listed); fund re-entered MultiplexDX on 17.01.2026 per ORSR (likely follow-on).
- Vision Ventures — included — I1, I2, I3, I4 — Slovak manager and fund vehicle (ORSR, SLOVCA full member); only a follow-on in Airvolute (ORSR 09.01.2026) after Oct 2023.
- Venture to Future Fund — included — I1, I2, I3, I4 — Bratislava fund (ORSR) investing directly; ORSR shareholder in MultiplexDX since 17.01.2026, FaceUp round 19.05.2026.
- Zero One Hundred (0100 Ventures) — included — I1, I2, I3, I4 — Was uncertain. Slovak parent and Fund I manager (ORSR); follow-on in BinarBase 01.11.2024 (ORSR), Fund II deal Reno 12/2025 (media); Cyprus Fund II flagged.
- G-Force — included — I1, I2, I3, I4 — Was uncertain. Bratislava manager and fund (ORSR); Enzidia announced 11.03.2025 by Founders Factory; typed accelerato
… [4845 more characters]
```
</details>

→ `Bash` — Final quote verification and schema validation
```sh
D=[tmp] $D/pg verifyall /Users/[redacted]/homeW/ai-dev-test/investor-db/data/sample/parts/sk.json $D/note_evidence.json | tail -2; cd /Users/[redacted]/homeW/ai-dev-test/investor-db && .venv/bin/python -m investordb validate --records data/sample/parts/sk.json --today 2026-10-11 | tail -1; .venv/bin/python -c "
import json,jsonschema
s=json.load(open('schema/investor.schema.json')); d=json.load(open('data/sample/parts/sk.json'))
v=jsonschema.Draft202012Validator(s, format_checker=jsonschema.Draft202012Validator.FORMAT_CHECKER); print('schema errors:', len(list(v.iter_errors(d))))
n=sum(len(f['sources']) for r in d for f in r['fields'].values() if f)+sum(len(i['sources']) for r in d for i in r['investments'] or []); print('stored quotes', n)"; ls -la data/sample/parts
```

<details><summary>result</summary>

```
verified 116, failed 0
49 records, 0 errors, 20 warnings
schema errors: 0
stored quotes 69
total 328
drwxr-xr-x  5 [user]  staff    160 11 окт.  01:57 .
drwxr-xr-x  3 [user]  staff     96 11 окт.  01:38 ..
-rw-r--r--  1 [user]  staff  72170 11 окт.  01:55 cz.json
-rw-r--r--  1 [user]  staff   6596 11 окт.  01:58 sk-decisions.md
-rw-r--r--  1 [user]  staff  85515 11 окт.  01:58 sk.json
```
</details>

**Agent:**

You've hit your session limit · resets 6am (Europe/Prague)

## Message from the orchestrator

The coordinator sent a message while you were working:
The usage limit reset — resume where you stopped (context intact). data/sample/parts/sk.json and sk-decisions.md already exist on disk — check what's done and continue. The orsr.py helper path in your brief was deleted by someone else's cleanup; if you need it, write your own small fetcher (ORSR pages are windows-1250 encoded; search URL: https://www.orsr.sk/hladaj_subjekt.asp?OBMENO=<urlencoded cp1250 name>&PF=0&R=on, extract links vypis.asp?ID=..&SID=..&P=0). Keep your working files under /Users/[redacted]/homeW/ai-dev-test/.work/sk/ and don't delete anything outside it. Final message in English.

Address this before completing your current task.

**Agent:**

The output files already on disk are the ones from my final build, made right before the reset. I'll move the working files to the location the coordinator asked for.

→ `Bash` — Copy working files to .work/sk and re-verify from there
```sh
D=[tmp] W=/Users/[redacted]/homeW/ai-dev-test/.work/sk; mkdir -p $W && cp -R $D/bin $D/build.py $D/note_evidence.json $D/cache $W/ && sed -i '' "s|$D|$W|g" $W/build.py && sed -i '' 's|EVID = Path(__file__).resolve().parent / "note_evidence.json"|EVID = Path(__file__).resolve().parent / "note_evidence.json"|' $W/build.py && printf '#!/bin/sh\nexec /Users/[redacted]/homeW/ai-dev-test/investor-db/.venv/bin/python %s/bin/pg.py "$@"\n' $W > $W/pg && chmod +x $W/pg && $W/pg verifyall /Users/[redacted]/homeW/ai-dev-test/investor-db/data/sample/parts/sk.json $W/note_evidence.json | tail -1; ls $W
```

<details><summary>result</summary>

```
verified 116, failed 0
bin
build.py
cache
note_evidence.json
pg
```
</details>

**Agent:**

[redacted: name]

All 49 candidates are in `data/sample/parts/sk.json` and `sk-decisions.md`. The validator shows 0 errors and 20 warnings. Every one of the 116 quotes was confirmed word for word on the raw page text (whitespace normalised).

**Counts:** 7 included, 1 uncertain, 6 dormant, 35 excluded.

**Included, with latest dated investment:**

| Investor | Latest dated investment | Evidence |
|---|---|---|
| Neulogy Ventures | MultiplexDX, s.r.o., 2026-01-17. Its fund (Slovak Venture Fund S.C.A., SICAR) came back as shareholder after leaving in 2018, so probably a follow-on. | ORSR, Tier A |
| Vision Ventures | Airvolute follow-on, 2026-01-09: stake raised from 1 667 to 3 290 EUR. | ORSR, Tier A |
| Venture to Future Fund | FaceUp, 2026-05-19 (press). Also MultiplexDX, 2026-01-17. | Press; ORSR, Tier A |
| Zero One Hundred (0100 Ventures) | Reno (UAE), 2025-12-04, press only. BinarBase follow-on, 2024-11-01. | Press; ORSR, Tier A |
| G-Force (typed `accelerator`) | Enzidia, 2025-03-11. | Founders Factory page, Wayback copy |
| CB Investment Management | Forvio follow-on, 2023-12-30. | ORSR, Tier A |
| Seed Starter Slovenskej sporiteľne (`cvc`) | Webout, 2026-06-08. | Bank's own press release |

**Notes on the three original includes:**
- **Neulogy:** its fund is not a new shareholder in any portfolio company since Oct 2023. The only post-2023 registry entry is the MultiplexDX re-entry (most likely a follow-on). Staffino's 18.10.2024 entry is only the fund's address changing, so I didn't count it.
- **Vision Ventures:** the 29.03.2025 Airvolute and 18.04.2024 Spinbotics dates in the research are also address changes. Its own site says new investments ended in 2023, and the fund is now selling down its holdings. It passes the recency rule (I3) on follow-ons only.
- **VFF:** a 2020 SIH article names Slovak Asset Management as its manager, and I couldn't find that name in ORSR. So the record stays at fund level.

**The 7 uncertain candidates:**
- **0100 VC Fund II → included.** I merged it with Zero Gravity Capital into one manager record; Zero Gravity is excluded as a rolled-up vehicle (E9).
- **G-Force → included**, as an accelerator.
- **CB Investment Management → included.**
- **ZAKA VC → excluded.** The fund is Czech (registered with the Czech National Bank, Prague); its Bratislava SPVs are owned by that Czech fund.
- **LRJ Capital → dormant (E4).** Last deal 2019, and its website domain is for sale.
- **IPM Group → dormant (E4).** Last third-party deal was Photoneo in 2021. I didn't count its InoBat 2024 money because IPM itself started InoBat.
- **Baryon Fund → still uncertain.** It has an ORSR-proven deal (Airvolute, 2026-01-09), but its manager's seat is unknown and its site lists only 2 portfolio companies (I2 unproven).

**Decisions that need your call:**
- **Seed Starter changed from exclude to include.** The PLAN has no rule that excludes corporate VC. The catch: its parent is a bank, and the PLAN defines `cvc` as the arm of a non-financial company.
- **20 excluded records have no E rule, which is what the 20 validator warnings are.** 16 are foreign, PE or public investors that no E rule excludes; they're marked "out of pilot scope". The other four are excluded on a failed inclusion rule (I1 or I2), which the validator also flags. The schema doesn't allow a scope rule ID. If you want these warnings gone, the PLAN needs a scope rule.

**Quotes:** 69 quotes in fields and investments, plus 47 in decision notes; all 116 confirmed, none failed. Of the colleague's quotes and sources, I dropped or replaced about 12:
- The SLOVCA profile paraphrase and the Trustmatic X post: replaced with exact text from the SLOVCA page and neulogy.vc/news.
- SIH's "EUR 19.0 million" for Neulogy: not on the current page, so dropped.
- StratifAI: aggregator only, and the currency contradicts the round.
- ZAKA's "minimum ticket 130K": it is the minimum for fund investors, not a startup ticket.
- The €11.6m figure for Vision Ventures: an SIH allocation, not the fund size.
- The Caplight deals for G-Force and CB Investment Management: aggregator only.
- The incubatorlist ticket for G-Force: dropped.
- Pages that return 403 or don't load (pitchbook, techleap, spectator.sme.sk, tatrabanka, genesis): replaced with the EIF Czech list, Nordic9, profesia.sk and ORSR, or dropped.

**Weakest 5 records:**
1. **Vision Ventures:** recency rests only on a share increase in a fund that is selling down its holdings.
2. **CB Investment Management:** recency rests on the 30.12.2023 follow-on, which falls out of the 36-month window on 30.12.2026. Its ticket comes from a 2020 secondary source.
3. **IPM Group:** dormant only because I chose not to count InoBat. Counting it would make the record included.
4. **Seed Starter:** a bank programme typed as corporate VC.
5. **Zero One Hundred:** the newest deal rests on a press match of "Zero 100 VC", and Fund II sits in Cyprus.

My working files (build script, fetcher, page cache) are in `/Users/[redacted]/homeW/ai-dev-test/.work/sk/`; I re-ran the quote check from there and all 116 still pass. Another session's cleanup wiped my first scratch folder mid-task, so I rewrote the tools. The second copy in the scratchpad (`skvc-agent/`) is still there because you said not to delete anything outside `.work/sk`. I touched nothing else, including `cz.json`, and ran no git.

Files:
- `/Users/[redacted]/homeW/ai-dev-test/investor-db/data/sample/parts/sk.json`
- `/Users/[redacted]/homeW/ai-dev-test/investor-db/data/sample/parts/sk-decisions.md`

