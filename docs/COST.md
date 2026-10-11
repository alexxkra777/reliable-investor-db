# What it would cost to cover the world

Short answer: **about $20–40k of model and infrastructure spend plus 250–400 analyst hours for the
first build of ~12–20k verified organisations, then roughly $3–6k and 40–60 hours per quarter to
keep it fresh.** The numbers below come from what the CZ/SK pilot actually used, not from guesses
about tokens.

## 1. What the pilot actually used

Token usage was read from the session logs of each research agent (every API response carries its
own usage block). Priced at Claude Opus 5.5 list prices: $4 / MTok input, $5 cache write, $0.40
cache read, $20 output.

| Step | Model calls | Tool calls | Cache reads (MTok) | Output (kTok) | List-price cost |
|---|---|---|---|---|---|
| Slovak candidates, first pass | 129 | 239 | 23.1 | 3.8 | $10.94 |
| Slovak records with verbatim quotes | 126 | 126 | 25.1 | 12.4 | $13.57 |
| Czech records with verbatim quotes | 141 | 150 | 30.6 | 11.5 | $15.72 |
| Existence evidence + re-deciding uncertain records | 185 | 186 | 45.8 | 16.8 | $20.70 |
| **Data collection total** | | | | | **$60.93** |
| One-off: source landscape and universe sizing | 61 | 116 | 6.9 | 3.9 | $3.82 |
| Blind second review of 45 records (other model family) | — | — | — | — | ~288k tokens total |

Volume: about **110 candidates screened → 91 records** (after merging duplicates across the two
countries) **→ 28 included**, 10 uncertain, 6 dormant, 21 excluded, 26 real investors outside the
pilot slice.

| Unit cost (pilot, as run) | |
|---|---|
| per screened candidate | **≈ $0.55** |
| per record kept in the database (any status) | ≈ $0.67 |
| per verified, included VC | ≈ $2.20 |

Two things make the pilot more expensive than production would be:
- **Cache reads are 99 % of the tokens.** Each agent worked through dozens of candidates in one
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
| **Model + infra** | | **≈ $10k–30k**; at the pilot's unoptimised rate ($0.55 / candidate, no second review) the research line alone would be ~$22–33k, so **$20–40k is the safe budget** |

**People.** The pilot showed where human time goes:
- **Adjudicating disagreements.** The blind second review disagreed with the first pass on 9 % of
  kept records (4 of 45), and the rule engine flagged 15 more for a look. At 5–10 minutes each,
  ~10 % of 20k records → **170–330 hours**.
- **Measuring accuracy.** A 60-claim sample takes ~40 minutes. Meaningful numbers per country ×
  investor type need ~60–100 strata → **40–70 hours**.
- **Rules and source curation per new country** (registers, associations, local press): 2–4 hours
  each for ~60 countries that matter → **120–240 hours**, front-loaded.

So **250–400 analyst hours** for the first build (overlapping categories counted once). Elapsed
time with ~20 parallel workers on the model side is days, not weeks; the human side sets the pace
at roughly 4–6 weeks for one analyst plus one engineer.

**Keeping it fresh.** Quote checks and link checks are free to re-run monthly. Activity has to be
re-researched: about a quarter of records per quarter (the 36-month window moves, funds close,
new funds appear) → **$3–6k and 40–60 hours per quarter**. The pilot's lesson applies here: the
blind review found that "dormant" was the label most often wrong, so dormant records get a
targeted second search before they're published as dormant.

## 3. What would change the estimate

- **Angels in scope**: +15–40k records, but each is a person under GDPR (legitimate-interest
  assessment, Art. 14 notices, opt-outs). Budget legal work before compute.
- **Commercial data**: licensing a commercial database removes most of the discovery work but
  not the verification, and its terms usually forbid building a resellable database on top of it.
- **Accuracy target**: every extra point of precision costs mostly human time (adjudication), not
  model time. See [eval/ACCURACY.md](../eval/ACCURACY.md) for what the pilot reached.
