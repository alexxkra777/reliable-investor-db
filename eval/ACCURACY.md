# Accuracy report

Built by `python -m investordb eval` on 2026-10-11.

## Human review

**No review labels found** (eval/labels.csv). Only the automated metrics below were computed; they say whether sources still contain the quoted text, not whether the claims are right. Run `review-pack`, review `eval/review.html`, export `eval/labels.csv` and run `eval` again.

## Recall against reference lists

| List | Entities | Covered | Recall (95 % CI) | Decisions of covered |
|---|---:|---:|---|---|
| cvca-full-members | 27 | 27 | 100.0 % (87.5-100.0) | excluded 1, included 8, out_of_scope 17, uncertain 1 |


## Automated checks

| Check | Value (95 % CI) |
|---|---|
| Quote found on page, all sources | 100.0 % (98.7-100.0) |
| Quote found on page, reachable sources only | 100.0 % (98.7-100.0) |
| Quote found, Tier A | 100.0 % (94.2-100.0) |
| Quote found, Tier B | 100.0 % (98.2-100.0) |
| Quote found, Tier C | 100.0 % (87.9-100.0) |
| Claims whose numbers/dates are all in their quotes | 87.0 % (79.9-91.8) |
| Claims with at least part of the value in the quotes | 99.2 % (95.5-99.9) |
| Number/date present, per single source | 73.2 % (65.5-79.6) |
| Stored decision = rule engine (decidable cases) | 74.6 % (61.7-84.2) |

Rule engine vs stored decisions: DISAGREE 14, agree 41, human_only 36. `human_only` = a decision the engine can't make (pilot scope, or a rule it has no data for).

Quote statuses: exact 300.

Confidence grades: A 26, B 2, C 63.

## Method

- Claims are sampled with `review-pack` (stratified by claim type: existence, each field, investments; proportional allocation with at least 3 per stratum, fixed seed). Overall accuracy is the plain sample share and leans towards the smaller strata.
- Inclusion precision uses existence claims of records whose stored decision is `included`. Investment claims are judged on company and date.
- **Strict** counts "Can't verify" as wrong, because a value whose source doesn't back it breaks the provenance promise. **Lenient** drops those claims.
- Intervals are 95 % Wilson score intervals.
- Recall: a reference entity is covered if a record with the same normalised name, alias or legal entity name exists, whatever its decision.
- Automated checks: `verify` looks for each stored quote on the cached page (normalised text, exact or fuzzy >= 0.85 with matching numbers) and for the claimed number/date inside the quote.
