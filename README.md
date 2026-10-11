# Reliable investor database — plan, pilot and measured accuracy

Assignment A: a database of investors in companies (VC, PE, family offices, angels, large private
investors) where every record is a real investor, and every value says where it comes from.

The approach in one line: **every value carries a verbatim quote and a URL, and a script re-opens
the page and checks the quote is there and contains the number.** Language models do the reading;
code checks them; a second model re-checks blind; the author reviews an AI-assisted assessment.

| Deliverable | Where |
|---|---|
| Plan: who is in, who is out, how it's verified, how many exist, how reliable | [PLAN.md](PLAN.md) |
| Evidence behind the plan (sources, counts from SEC/ESMA/GLEIF bulk files, failure modes) | [research/sources-and-universe.md](research/sources-and-universe.md) |
| Pilot data: VC investors managed from Czechia and Slovakia, a source and quote for every value | [data/sample/investors.json](data/sample/investors.json), flat: [investors.csv](data/sample/investors.csv) |
| Every decision with the rule that made it | [data/sample/parts/sk-decisions.md](data/sample/parts/sk-decisions.md), [cz-decisions.md](data/sample/parts/cz-decisions.md) |
| Accuracy: author-reviewed assessment, recall, automated checks | [eval/ACCURACY.md](eval/ACCURACY.md); [all 60 findings](eval/REVIEW.md) |
| Blind second review and how disagreements were settled | [eval/second-opinion/](eval/second-opinion/) |
| Cost of scaling to the world, from measured pilot usage | [docs/COST.md](docs/COST.md) |
| Verification pipeline (Python) | [src/investordb/](src/investordb/), tests in [tests/](tests/) |
| Conversation exports | [ai-log/](ai-log/) |

## Results at a glance

**Pilot scope:** venture capital investors managed from Slovakia and Czechia (Slovakia was the
original slice; it gave only 7 included investors, too few to measure anything, so Czechia was added).

| | |
|---|---|
| Candidates screened | ~110 |
| Records (one per manager, after merging duplicates) | **91** |
| Included / uncertain / dormant / excluded / real investors outside the VC slice | 28 / 10 / 6 / 21 / 26 |
| Quotes checked against cached page text | **299 of 299 found** (Tier A 62, B 209, C 28) |
| Claims with complete checked value support | **48 / 124 (38.7%)**; investment company names are also required, asserted publication dates do not count |
| Recall against the CVCA full-member list | **27 / 27** |
| Blind second review (other model family) agreed "is a real investor" | 44 / 45 after adjudication (43 / 45 before) |
| Status errors the second review caught in the first pass | 4 of 45 (all "dormant" firms that had recent deals) |
| Claim accuracy on the historical 60-claim sample, author-reviewed AI-assisted assessment | **58 / 60 (96.7%)**, 95% CI 88.6–99.1%; [method below](#author-reviewed-ai-assisted-assessment) |
| Imputed API token cost of four pilot collection agents (not subscription payments) | **$43.70 ≈ $0.40** per screened candidate; [exact counters and scope](docs/COST.md) |

## How a record is made and checked

```
discover ──> research agent ──> record with quotes ──> fetch every source ──> quote on page?
(lists,      (one candidate,     (schema-valid JSON)    (polite, cached,       value in quote?
 registers,   verbatim quotes                            Wayback fallback)      rules engine
 press)       from raw HTML)                                                    confidence grade
                                                                        │
                       blind second review (other model) ──> adjudicate ──> assisted sample ──> ACCURACY
```

```sh
python3 -m venv .venv && .venv/bin/pip install -e '.[dev]'
.venv/bin/python -m investordb validate          # schema + consistency
.venv/bin/python -m investordb fetch             # download every source once
.venv/bin/python -m investordb verify            # is each quote on its page, are the values in it
.venv/bin/python -m investordb decide            # recompute decisions from the rules, compare
.venv/bin/python -m investordb grade             # confidence A/B/C, flat CSV
.venv/bin/python -m investordb review-pack --html eval/review-current.html --claims eval/claims-current.csv  # optional NEW snapshot
.venv/bin/python -m investordb eval --labels eval/labels.csv
.venv/bin/pytest                                 # 117 tests
```

## Decisions I made where the brief was open

- **Unit of a record is the manager, not the fund.** 64 % of "VC funds" in a year of SEC Form D
  filings are single-deal SPVs; counting vehicles would triple the database with noise.
- **"Really invests" means a dated investment in the last 36 months** from a legal filing or a
  first-party source, not "has a website that says VC". 36 months because CEE funds often do 2–5
  deals a year.
- **Pilot scope status.** A PE firm in a VC pilot is a real investor, just not in this slice. It gets
  `out_of_scope` instead of `excluded`, so the pilot's precision isn't flattered by easy rejections.
- **Commercial databases (Crunchbase, Dealroom, PitchBook) are only used to find names.** Their
  terms forbid building a database from them, so every stored fact points to a free primary source.
- **Angels are left out of the pilot.** They are private individuals under GDPR; the plan keeps only
  people with a public investor persona and needs a legal basis before collection.

## Author-reviewed AI-assisted assessment

The fixed historical sample of **60 claims out of 264** remains in [eval/claims.csv](eval/claims.csv)
and [eval/review.html](eval/review.html). AI reviewers read full source pages and records, recorded
English notes, and identified two unsupported claims. The author reviewed the findings and confirmed
[eval/labels.csv](eval/labels.csv). This is **author-reviewed AI-assisted assessment**, not a claim
that the author or a colleague independently opened all 60 source pages.

| Review of the historical snapshot | Correct | Wrong | Can't verify | Accuracy (strict, 95% CI) |
|---|---:|---:|---:|---|
| Author-reviewed AI-assisted assessment | 58 | 2 | 0 | 96.7% (88.6–99.1) |
| Historical original model review, preserved unchanged | 60 | 0 | 0 | 100% (94.0–100) |

The current dataset corrects Inven's unsupported AUM and IntellCRE's unsupported exact date.
Those corrections do not relabel the historical sample as correct or establish accuracy of the
corrected snapshot. [Corrections and reproduction limits](eval/CORRECTIONS.md) distinguish these
snapshots and explain the CLI's legacy `human` terminology. Do not rerun `review-pack` over the
historical files. Per-field results: [eval/ACCURACY.md](eval/ACCURACY.md).

Automatic quote matching checks textual support, not semantic correctness of sectors, stages or
fund definitions. The current grades are **A 3, B 0, C 88**; 28 stored included decisions are not
28 automatically verified records. Grades do not by themselves prove manager identity or the meaning of a financial metric.
`decide` uses declared tiers and stored metadata; its core-activity heuristic accepts any Tier A
field and does not consume quote-verification results. It is not a semantic validator.
The rule engine agrees with 41 of 55 decidable cases, disagrees
with 14, and leaves 36 for review. Cached pages were fetched on 2026-10-11; this pass reused that
cache rather than fetching every page again.

## What's missing

- **One country pair.** Everything in the plan is designed for the world; only CZ/SK was built and measured.
- **Czech regulator data (ČNB JERRS)** sits behind a CAPTCHA and a certificate-based API, so Czech
  existence evidence comes from CVCA, EIF and fund-of-funds pages instead.
- **Family offices and large private investors** are planned and sized but not piloted — they need
  different sources (registry shareholder entries, rich lists for seeding only).
- **No scheduled refresh** yet; the monthly re-check is a cron job over the existing commands.

## How I worked with AI

See [the appendix](#appendix-how-i-worked-with-ai).

---

## Appendix: how I worked with AI

**Setup.** One orchestrating Claude Code session did the planning, wrote every brief, reviewed
every result and made all decisions. The research and build work went to sub-agents with written
briefs, each in a fresh context. Codex (a different model family) wrote parts of the code and did the
blind second review, so the two reviewers don't share the same blind spots. Two Claude
subscriptions plus Codex were rotated when a 5-hour usage limit ran out; the conversation moved with
its full context and interrupted agents were resumed.

**What every brief contained.** The goal and the deliverable file, the exact data contract (schema
or API payloads), hard rules ("every number needs a URL and an access date", "never invent a
figure, write *not found*", "quotes must be copied from the raw page text"), what not to touch
(other agents' folders, git config, deploys), "no `git add -A`", and the shape of the final report
(counts, weakest records, what couldn't be verified). Full briefs are at the top of each agent's
log in [ai-log/](ai-log/).

**How the output was checked — I didn't trust reports, I re-ran things.**
- Every agent report was compared with the actual files and commits (git log, file timestamps,
  re-running the tests myself).
- Numbers: automatic quote check against the live page for every value; the claimed number/date
  must be inside the quote; a rule engine recomputes every decision and lists disagreements.
- A blind second review by another model on everything that was kept, then adjudication of each
  disagreement with the evidence re-fetched.
- AI reviewers assess the historical stratified sample; the author reviews the findings and confirms labels. The reported number describes that assisted assessment.
- Before every commit: grep for tool names and AI mentions in code and commit messages, and a look
  at screenshots for anything visual.

**Agents in this repo.**

| Agent | Brief in one line | Output |
|---|---|---|
| Source landscape | Which free public sources prove an entity invests; size the universe from cited or computed numbers | `research/sources-and-universe.md` |
| Slovak candidates | Enumerate every Slovak VC candidate, including the ones that only look like VCs, with dated deals | `research/sk-vc-candidates.*` |
| Pipeline engineer | Build `validate / fetch / verify / decide / grade / review-pack / eval` against a fixed record contract, with tests | `src/investordb/`, `tests/` |
| Slovak records, Czech records | Turn candidates into schema records; every quote verbatim from raw HTML and grep-confirmed | `data/sample/parts/*.json` |
| Existence evidence | Add evidence for rule I2, re-decide uncertain records | same files |
| Blind second review (Codex) | Only names, countries, websites; decide independently | `eval/second-opinion/codex.json` |

**Where the AI got it wrong (and how it was caught).**
- **Paraphrased "quotes".** The first candidate pass copied quotes from a web-fetch tool that returns
  a model-written summary, not the page. Spot-checking against raw HTML showed it. From then on
  quotes come only from raw page text; `fetch` downloads the pages and `verify` checks the cache, failing a quote that isn't
  there — including a near-identical sentence with a different number, monetary scale or currency. Publication metadata alone does not verify an investment date.
- **Wrong dates from the registry.** The first pass read two shareholder-register entries as new
  investments; the second pass found they were only the fund's change of address.
- **"Dormant" was the most common wrong label.** The blind second review found recent deals for
  4 of 45 kept records that the first pass had marked dormant or dead (Y Soft Ventures, Springtide,
  365.fintech, KOOPEO). Settled in `eval/second-opinion/adjudication.md`; the plan now requires a
  targeted second search before a record is called dormant.
- **My own seed list was wrong.** The candidate list in the first brief contained names
  that don't exist or are Czech; the agent was told not to trust it and refuted them.
- **A field the pipeline didn't read.** I added `fields.existence` to the schema but not to the
  list of fields the pipeline iterates; the enrichment agent noticed that verify/grade ignored it.
- **Over-matching in my own script.** A bulk change of "out of scope" records matched the word
  "scope" in three unrelated notes; caught by reading the printed list, reverted.
- **Misleading metrics on the first run.** Recall showed 24/27 because of name variants and a
  reference row with a label in the name; value support was counted per source instead of per
  claim. Both fixed in code, with tests, before reporting numbers.
- **Instructions leaking between contexts.** A research agent wrote its notes in Russian because it
  picked up my personal assistant settings; the brief didn't say "write in English". Caught when
  reading the file before committing; fixed, and every later brief states the language.
- **Shared resources.** One agent's "clean up my scratch files" deleted other agents' files in a
  shared temp folder (including a brief); a research agent's browser navigation took over a tab I
  was using. Fix: every agent gets its own work folder and its own headless browser.
