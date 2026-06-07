# Synthetic vs real data boundary for RLL validation

## Operational rule

**Synthetic for code truth. Real observational data for world truth.** RLL remains: "RLL is a candidate effective dynamic-transition cosmology under real-data evaluation."

The mandatory claim boundary for every scientific artifact is:

> No superiority claim unless real-data metrics pass predefined thresholds.

## Allowed roles for synthetic data

Synthetic data may be retained for:

- unit tests and regression tests;
- example notebooks and sanity checks;
- numerical stability checks;
- fixture-driven failover and rollback tests.

Synthetic data must not support scientific conclusions, public model-comparison metrics, cosmological superiority language, or claims about the physical world.

## Required locations and labels

The repository boundary is explicit:

- `data/synthetic/` for synthetic inputs and generated sanity datasets;
- `data/real/` for materialized observational inputs;
- `results/synthetic/` for synthetic sanity or regression outputs;
- `results/real/` for real observational outputs outside specialized pipelines;
- `results/structure_d/` for Structure-D real-validation outputs;
- `tests/fixtures/` for test-only fixtures.

Every JSON artifact must declare `dataset_type` with one of:

- `real_observational`;
- `synthetic_sanity_check`;
- `synthetic_regression_test`;
- `mixed_forbidden`;
- `unknown_forbidden`.

If `dataset_type` is not `real_observational`, the artifact must carry `claim_allowed: false`.

## Real-data provenance requirements

Real-data artifacts should record source, unit, SHA256 for each local file, DOI or URL when available, license or license note when available, command, git commit hash, Python version, and relevant package versions.

## TOKEN_VAZIO policy

`TOKEN_VAZIO` means an explicit empty or null slot is preferred to inferred or invented content. Missing observational data must be represented as `null`, `not_measured`, `unknown_forbidden`, or another explicit blocker. Filling gaps by inference can make an artifact look more complete than the evidence permits; therefore, explicit absence is a scientific integrity feature, not a failure.

## Current audit note

Synthetic or mock material is still present in legacy and example paths, including `data/posterior_unified_synth.csv`, mock figure names under `figs/`, and fixture-like examples in tests. Those are acceptable only as code-truth assets. Real validation outputs must not depend on `data/synthetic/`, `results/synthetic/`, or `tests/fixtures/`.
