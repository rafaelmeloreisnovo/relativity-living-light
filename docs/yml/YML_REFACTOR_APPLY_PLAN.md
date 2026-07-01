# YML Refactor Apply Plan

## Status

`governance_record / action_plan`

## Objective

Apply safe corrections to workflows and YAML files without deleting history, without promoting synthetic material to real validation, and without changing scientific claims.

## Safe order

1. Fix the missing directory in `dha-fisher-ci.yml`.
2. Normalize workflow permissions when needed.
3. Add explicit timeouts to jobs that do not declare timeout.
4. Add concurrency guards to workflows without concurrency control.
5. Mark the validation paths file as canonical under `docs/pipelines`.
6. Keep root duplicates as legacy until consumers are checked.
7. Keep synthetic material explicitly blocked from real-data validation.
8. Run YAML parse checks.
9. Run workflow audit.
10. Run documentation inventory checks.

## Do not do in this change

- Do not delete raw authorial material.
- Do not rewrite scientific theory.
- Do not alter numerical results.
- Do not promote examples to real validation.
- Do not declare model superiority.
- Do not remove duplicate files without traceability.

## Success criteria

The plan succeeds if YAML files still parse, workflows remain isolated, referenced scripts exist, workflows have explicit safety settings, examples stay separated from real validation, traceability documents exist, and the inventory remains consistent.

## Boundary

This plan improves organization and traceability. It does not prove physical truth, model superiority, observational validation, peer acceptance, or execution of every real-data pipeline.
