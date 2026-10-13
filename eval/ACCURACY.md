# Accuracy report

Built by `python -m investordb eval` on 2026-10-11.

Review tables describe the original 60-claim sample before corrections. Two human reviewers manually checked all 60 sampled claims against their sources and confirmed the final labels on 11 October 2026. Findings were prepared with AI assistance; model checks and human source verification are separate stages. Automated checks describe the corrected current records and reuse the 11 October page cache. See CORRECTIONS.md for qualifications.

Reviewer: two human reviewers; confirmed on 2026-10-11.

## Human source-by-source review

60 of 60 sampled claims labelled.

| Metric | Labelled | Correct | Wrong | Can't verify | Strict (95 % CI) | Lenient (95 % CI) |
|---|---:|---:|---:|---:|---|---|
| Inclusion precision | 6 | 6 | 0 | 0 | 100.0 % (61.0-100.0) | 100.0 % (61.0-100.0) |
| Field: aum | 4 | 3 | 1 | 0 | 75.0 % (30.1-95.4) | 75.0 % (30.1-95.4) |
| Field: existence | 7 | 7 | 0 | 0 | 100.0 % (64.6-100.0) | 100.0 % (64.6-100.0) |
| Field: funds | 5 | 5 | 0 | 0 | 100.0 % (56.5-100.0) | 100.0 % (56.5-100.0) |
| Field: geography | 6 | 6 | 0 | 0 | 100.0 % (61.0-100.0) | 100.0 % (61.0-100.0) |
| Field: sectors | 6 | 6 | 0 | 0 | 100.0 % (61.0-100.0) | 100.0 % (61.0-100.0) |
| Field: stages | 6 | 6 | 0 | 0 | 100.0 % (61.0-100.0) | 100.0 % (61.0-100.0) |
| Field: ticket | 6 | 6 | 0 | 0 | 100.0 % (61.0-100.0) | 100.0 % (61.0-100.0) |
| Investment date | 14 | 13 | 1 | 0 | 92.9 % (68.5-98.7) | 92.9 % (68.5-98.7) |
| **All claims** | 60 | 58 | 2 | 0 | 96.7 % (88.6-99.1) | 96.7 % (88.6-99.1) |

## Historical original model review

The same sample judged by a separate model run that read each source page in full (not only the quote) and the whole record. It is not a substitute for the human review: it comes from the same model family that collected the data, so its mistakes can line up with the collectors' mistakes.

60 of 60 sampled claims labelled.

| Metric | Labelled | Correct | Wrong | Can't verify | Strict (95 % CI) | Lenient (95 % CI) |
|---|---:|---:|---:|---:|---|---|
| Inclusion precision | 6 | 6 | 0 | 0 | 100.0 % (61.0-100.0) | 100.0 % (61.0-100.0) |
| Field: aum | 4 | 4 | 0 | 0 | 100.0 % (51.0-100.0) | 100.0 % (51.0-100.0) |
| Field: existence | 7 | 7 | 0 | 0 | 100.0 % (64.6-100.0) | 100.0 % (64.6-100.0) |
| Field: funds | 5 | 5 | 0 | 0 | 100.0 % (56.5-100.0) | 100.0 % (56.5-100.0) |
| Field: geography | 6 | 6 | 0 | 0 | 100.0 % (61.0-100.0) | 100.0 % (61.0-100.0) |
| Field: sectors | 6 | 6 | 0 | 0 | 100.0 % (61.0-100.0) | 100.0 % (61.0-100.0) |
| Field: stages | 6 | 6 | 0 | 0 | 100.0 % (61.0-100.0) | 100.0 % (61.0-100.0) |
| Field: ticket | 6 | 6 | 0 | 0 | 100.0 % (61.0-100.0) | 100.0 % (61.0-100.0) |
| Investment date | 14 | 14 | 0 | 0 | 100.0 % (78.5-100.0) | 100.0 % (78.5-100.0) |
| **All claims** | 60 | 60 | 0 | 0 | 100.0 % (94.0-100.0) | 100.0 % (94.0-100.0) |

Author-confirmed and model labels agree on 58 of 60 claims (96.7 % (88.6-99.1)). Claims they disagree on: inven-capital/field/aum, seed-starter-slovenskej-sporitelne/investment/1.

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
| Claims with complete checked value support (company/number/date) | 38.7 % (30.6-47.5) |
| Claims not classified as wholly unsupported (includes partial) | 99.2 % (95.6-99.9) |
| Number/date present, per single source | 52.0 % (44.0-60.0) |
| Stored decision = rule engine (decidable cases) | 74.6 % (61.7-84.2) |

Rule engine vs stored decisions: DISAGREE 14, agree 41, human_only 36. `human_only` = a decision the engine can't make (pilot scope, or a rule it has no data for).

Quote statuses: exact 299.

Confidence grades: A 3, C 88.

## Method

- Claims are sampled with `review-pack` (stratified by claim type: existence, each field, investments; proportional allocation with at least 3 per stratum, fixed seed). Overall accuracy is the plain sample share and leans towards the smaller strata.
- Inclusion precision uses existence claims of records whose stored decision is `included`. Investment claims are judged on company and date.
- **Strict** counts "Can't verify" as wrong, because a value whose source doesn't back it breaks the provenance promise. **Lenient** drops those claims.
- Intervals are 95 % Wilson score intervals.
- Recall: a reference entity is covered if a record with the same normalised name, alias or legal entity name exists, whatever its decision.
- Automated checks: `verify` looks for each stored quote on the cached page (normalised text, exact or fuzzy >= 0.85 with matching numbers) and for the claimed number/date inside the quote.
