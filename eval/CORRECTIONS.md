# Review provenance and corrections (2026-10-11)

## Historical assessment

`claims.csv` and `review.html` preserve the original 60-claim stratified sample of 264 claims.
`labels.csv` contains the labels confirmed after [redacted: name] and a colleague manually checked
all 60 sampled claims against their sources: 58 correct, 2 wrong, no unverifiable claims
(96.7%, 95% Wilson CI 88.6–99.1%). AI reviewers prepared findings and checked sources before
this human verification. The author explicitly confirmed the source-by-source human check on
11 October 2026. This sample review does not certify all 91 records. `labels-model.csv` remains
the unchanged original model review, including its two missed errors. Its historical 60/60
result is not the final accuracy result.

These labels judge the original snapshot, not the corrected dataset. The sample is not redrawn,
and the two wrong labels stay wrong after correction. The current claim population is 263 instead of 264 because Inven AUM is null; this was checked with `build_claims` without writing a new review pack. The historical sample and its denominator remain unchanged.

## Corrected facts

- **Inven Capital AUM:** `fields.aum` is null in the combined dataset and Czech source part.
  The homepage's EUR 500m describes institutional/corporate capital and total committed capital,
  not manager AUM. The original quote, URL, access date and distinction are retained in the
  record's decision note; no fund size or AUM definition was invented.
- **IntellCRE announcement date:** investment `date` and the two source `published` values are
  null in the combined dataset and Slovak source part. Full cached and live page text and raw
  HTML confirm the investment but do not independently state 17 September 2025. That date
  came only from the retained URL. The decision note records why the precision was removed.

Tensor/Wultra remains labelled correct only for the claimed **registry entry** date: unchanged
stakes transferred between Tensor vehicles. It is not independent evidence of a new cash
investment on that date. Likewise shareholder-entry dates need not be cash-transfer dates.

## Current automated results and limits

`validate`, `verify`, `decide`, `grade` and `eval` were rerun on corrected records. Quote verification
reused the 2026-10-11 cache, not a new download of every page. Matching text establishes lexical
support, not semantic truth of sector/stage classifications, AUM definitions or manager identity.
Grade A/B is a conservative automatic indicator, not a substitute for review of those meanings.
`decide` uses declared source tiers and stored dates/publication metadata rather than verification
results; its core-activity heuristic accepts any Tier A field. Consequently its decisions are not
fully verified semantic determinations. Disagreements and `human_only` cases remain explicit.

## Reproduction limits

The schema and current CLI accept null investment dates; no workaround or fabricated day is
needed. `eval` joins labels to the unchanged `claims.csv` by claim ID. The adjacent
`labels.metadata.json` records assessment type, author confirmation date and the SHA-256 hash
of that historical claims file. If the claims hash changes, evaluation fails before overwriting
reports. Rerunning `eval --labels eval/labels.csv` preserves the confirmed human source-review attribution,
historical-model heading and snapshot note automatically.

The legacy `human` JSON key names the labels input; `review_provenance` records how the labels
were produced and records the author-confirmed human source-by-source review.
The sidecar binds the historical claims file, not the current corrected records; it does not
establish accuracy of the corrected snapshot. Do not rerun `review-pack` over the historical
`claims.csv` or `review.html` to make the corrected dataset appear to score 100%. To create a
separate future sample, choose different `--claims` and `--html` output paths as shown in README.
