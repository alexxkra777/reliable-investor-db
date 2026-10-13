# Implementation and review process

This is a retrospective account of the completed work, not a conversation transcript. Agent instructions and tool records are in `../ai-log/`.

## Scope and evidence contract

The initial scope was Slovak venture investors. It expanded to Czech and Slovak candidates because the Slovak included population was too small for a useful field-accuracy sample. The unit is the manager rather than each legal fund vehicle. Public primary sources support stored facts; commercial directories are discovery aids. Unknown values remain null. Each fact carries a URL, access date and verbatim quotation. Inclusion, exclusion, dormancy and pilot-scope decisions are distinct.

## Work stages

1. Define the population, inclusion rules, reliability assumptions and worldwide cost model in `../PLAN.md`.
2. Assign separate source-landscape, candidate-collection and pipeline tasks with explicit output contracts and source requirements.
3. Assemble 91 candidate records. Validate the schema, cache source pages, check quotations and values, recompute decisions and grade evidence. These lexical and rule checks have stated semantic limits.
4. Obtain a blind review from a different model family and adjudicate disagreements. This caught status errors and did not replace a human sample review.
5. Preserve the original stratified 60-claim sample. Prepare detailed findings; two human reviewers manually check each sampled claim against its sources and confirm labels.
6. Correct the two unsupported facts: Inven committed capital was mislabelled AUM; an exact IntellCRE announcement date was supported only by its URL. Keep the historical wrong labels and 58/60 result instead of rewriting history.
7. Strengthen evidence checking and verification invalidation, rerun validation, and preserve review provenance alongside the historical claims hash.

## Result and limits

The manual sample result is 96.7% (95% Wilson interval 88.6–99.1%). Current cached quote matches are 299/299, while complete automated value support is 48/124. These measure different things. Global population and cost estimates remain estimates, not a completed worldwide crawl. Final local validation passed 117 tests, Ruff and the schema check for all 91 records.

The author reviewed the completed package before publication. The original model outputs, disagreements and corrected records remain inspectable. Conversation records are translated and edited with that fact disclosed; native `/export` coverage is described in `../ai-log/README.md`.
