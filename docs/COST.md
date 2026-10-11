# What it would cost to cover the world

Short answer: **about $20–40k of model and infrastructure spend plus 350–770 analyst hours for the
first build of ~12–20k verified organisations, then roughly $3–6k and 40–60 hours per quarter to
keep it fresh.** Pilot usage below is historical; production costs and human hours are planning assumptions, not measured delivery costs or analyst time.

## 1. What the pilot actually used

Token counters were recomputed from the original research-agent JSONL responses on 2026-10-11.
Streaming fragments are deduplicated by response `message.id`, taking the last usage block
(the complete response); synthetic error responses are excluded. All priced responses identify
`claude-opus-5-5`, global inference and standard service. Cache writes are entirely 5-minute writes.

[Official Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), checked
2026-10-11: $4/MTok uncached input, $5/MTok 5-minute cache writes, $8/MTok 1-hour cache writes,
**$0.20/MTok cache reads**, $20/MTok output. Calculation:
`(4*input + 5*write_5m + 8*write_1h + 0.20*cache_read + 20*output) / 1,000,000`.

These are **imputed API list-price token costs**, not invoices or actual subscription payments.
The pilot used subscriptions. The total below covers the four listed collection agents only;
it excludes the orchestrator, pipeline engineering, final audit, independent reviews, tools and
infrastructure. No complete project bill or subscription allocation was measured.

| Step | Model calls | Tool calls | Cache reads (MTok) | Output (kTok) | Imputed token cost |
|---|---:|---:|---:|---:|---:|
| Slovak candidates, first pass | 129 | 239 | 23.111 | 78.549 | $7.82 |
| Slovak records with verbatim quotes | 125 | 126 | 25.099 | 111.514 | $10.53 |
| Czech records with verbatim quotes | 140 | 150 | 30.560 | 127.815 | $11.94 |
| Existence evidence + re-deciding uncertain records | 185 | 186 | 45.785 | 110.688 | $13.42 |
| **Data collection total** | **579** | **701** | **124.555** | **428.566** | **$43.70** |
| One-off: source landscape and universe sizing | 61 | 116 | 6.874 | 56.200 | $3.49 |
| Blind second review of 45 records (other model family) | — | — | — | — | Not included; historical report states ~288k tokens |

Exact raw counters underlying the rounded table (all 1-hour writes are zero):

| Step | Uncached input | 5m writes | Cache reads | Output | Original agent log ID |
|---|---:|---:|---:|---:|---|
| Slovak candidates, first pass | 258 | 324174 | 23111424 | 78549 | `a56118ade50469af1` |
| Slovak records with verbatim quotes | 250 | 655295 | 25098778 | 111514 | `ae9344859411d2483` |
| Czech records with verbatim quotes | 280 | 653829 | 30559840 | 127815 | `a7cea1c8756749d5d` |
| Existence evidence + re-deciding uncertain records | 370 | 409956 | 45784647 | 110688 | `a7c9068e4184f1a94` |
| One-off: source landscape and universe sizing | 122 | 198850 | 6873646 | 56200 | `a3ac17bd55c8ff68c` |

The previous $60.93 estimate used an incorrect $0.40 cache-read price **and** first-fragment
output counters (3.8/12.4/11.5/16.8 kTok rather than complete outputs). It is superseded, not an
actual historical bill. Repricing only rounded cache totals would miss the output-counter error.
The corrected exact collection total before rounding is $43.7031598; source landscape is $3.4934672.

Volume: about **110 candidates screened → 91 records** (after merging duplicates across the two
countries) **→ 28 included**, 10 uncertain, 6 dormant, 21 excluded, 26 real investors outside the
pilot slice.

| Unit cost (pilot, as run) | |
|---|---|
| per screened candidate | **≈ $0.40** |
| per record kept in the database (any status) | ≈ $0.48 |
| per stored included VC (not an automatic confidence grade) | ≈ $1.56 |

Two things make the pilot more expensive than production would be:
- **Cache reads are about 98% of the collection tokens.** Each agent worked through dozens of candidates in one
  long context, so every step re-read everything before it. A production pipeline runs one small
  context per candidate.
- **It ran on the top model, interactively.** Extraction from a fetched page is a much easier job
  than open-ended research and runs fine on a cheaper model through the batch API (−50 %).

## 2. How the cost scales

**How many candidates.** From [research/sources-and-universe.md](../research/sources-and-universe.md):
12–20k verifiable organisations worldwide (VC, PE, family offices that invest directly, named large
private investors). The pilot kept roughly one in three screened candidates as an investor in the
target slice and one in two as an investor of some kind. So the world needs **~40–60k candidates
screened**, mostly from SEC ADV/Form D, ESMA registers, EIF and national fund-of-funds lists,
association member lists and press feeds. Angels (15–40k named) are left out here; they're a
separate, GDPR-heavy decision.

**Cost per candidate in production.**

| Stage | How | Per candidate |
|---|---|---|
| Discovery + de-duplication | Bulk files (SEC, ESMA, GLEIF) and lists, deterministic code | ~$0 |
| Fetch + text extraction | own fetcher, polite rate limits, Wayback fallback | ~$0 (infra) |
| Research + extraction with verbatim quotes | one short agent run per candidate, mid-tier model, ~10 tool calls | $0.10–0.25 |
| Automatic checks (quote on page, value in quote, rules, recency) | the `investordb` pipeline in this repo | ~$0 |
| Independent second review of kept records | a different model, blind | $0.10–0.20 |

| Line item | Basis | First build |
|---|---|---|
| Research + extraction | 40–60k × $0.10–0.25 | $4k–15k |
| Second review | 15–25k kept × $0.10–0.20 | $1.5k–5k |
| Headroom for re-runs, hard cases on the top model, prompt iteration | ~50 % on the two lines above | $3k–10k |
| Fetching infrastructure (small VM, storage, occasional proxy for blocked sites) | 2 months | $0.5k–1k |
| **Model + infra** | | **≈ $10k–30k**; at the pilot's unoptimised imputed rate ($0.40 / candidate, no second review) the research line alone would be ~$16–24k, so **$20–40k is the safe budget** |

**People (planning scenario, not measured analyst time).** The pilot exposed these work categories; timing assumptions below have not been benchmarked:
- **Adjudicating disagreements.** The blind second review caught status errors in 4 of 45
  kept records (9%); the current rule engine flags 14 disagreements and leaves 36 cases outside its automatic decisions. These are different signals, not additive counts. At 5–10 minutes each,
  ~10 % of 20k records → **170–330 hours**.
- **Measuring accuracy.** Assume 60–120 minutes for a 60-claim sample (1–2 minutes per claim), not the previously unmeasured 40-minute claim. At 60–100 country/type strata this gives **60–200 hours**. Hard-to-access or ambiguous sources can exceed this allowance.
- **Rules and source curation per new country** (registers, associations, local press): 2–4 hours
  each for ~60 countries that matter → **120–240 hours**, front-loaded.

The three ranges sum to **350–770 analyst hours** (170–330 + 60–200 + 120–240), with no assumed overlap discount. At 40 hours per week this is about **9–20 analyst weeks**, before engineering work. Model concurrency may shorten compute time, but elapsed delivery time was not measured in the pilot.

**Keeping it fresh.** Quote checks and link checks use no model calls; fetching still consumes infrastructure and may require maintenance. Activity has to be
re-researched: about a quarter of records per quarter (the 36-month window moves, funds close,
new funds appear) → **$3–6k and 40–60 hours per quarter**, an unbenchmarked planning allowance rather than measured maintenance time. The pilot's lesson applies here: the
blind review found that "dormant" was the label most often wrong, so dormant records get a
targeted second search before they're published as dormant.

## 3. What would change the estimate

- **Angels in scope**: +15–40k records, but each is a person under GDPR (legitimate-interest
  assessment, Art. 14 notices, opt-outs). Budget legal work before compute.
- **Commercial data**: licensing a commercial database removes most of the discovery work but
  not the verification, and its terms usually forbid building a resellable database on top of it.
- **Accuracy target**: every extra point of precision costs mostly human time (adjudication), not
  model time. See [eval/ACCURACY.md](../eval/ACCURACY.md) for what the pilot reached.
