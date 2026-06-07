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

If `dataset_type` is not `real_observational`, the artifact must carry `claim_allowed: false`. Incomplete real artifacts also keep `claim_allowed: false` until all predefined real-data metrics and provenance requirements are satisfied.

## Legacy synthetic/mock manifest

Legacy synthetic, mock, demo, example, or fixture artifacts that still live outside the approved roots are cataloged in `data/synthetic/LEGACY_SYNTHETIC_MANIFEST.json`. The manifest records each original path, the proposed boundary path, artifact kind, dataset type, classification reason, code-test allowance, migration status, and SHA256 for stable local files.

The current safe migration pattern is **document first, do not delete**. A legacy path may remain in place only when it is present in the manifest and remains behind `scientific_use_allowed: false`. New synthetic/mock/demo/example/fixture artifacts outside `data/synthetic/`, `results/synthetic/`, or `tests/fixtures/` should be treated as boundary violations unless a compatibility exception is added with a clear reason.

## Real-validation input rule

Real validation code must not consume paths whose names or provenance indicate `synthetic`, `synth`, `mock`, `demo`, `example`, or `fixture`, except for explicit test-only fixtures classified as `synthetic_regression_test`. A path containing both real and synthetic indicators is `mixed_forbidden` and cannot support claims.

## Real-data provenance requirements

Real-data artifacts should record source, unit, SHA256 for each local file, DOI or URL when available, license or license note when available, command, git commit hash, Python version, and relevant package versions.

## TOKEN_VAZIO policy

`TOKEN_VAZIO` means an explicit empty or null slot is preferred to inferred or invented content. Missing observational data must be represented as `null`, `not_measured`, `unknown_forbidden`, or another explicit blocker. Filling gaps by inference can make an artifact look more complete than the evidence permits; therefore, explicit absence is a scientific integrity feature, not a failure.

### Remaining TOKEN_VAZIO/null gaps

- The energy-momentum observational ledger template keeps density fields such as kinetic, thermal, gravitational, and field energy as `null`/`measured: false` until traceable observations are supplied.
- Structure-D FNext diagnostics keep `F_gap: null`, `F_gap_uncertainty: null`, and `score: null` when the observational ledger is incomplete or no physical normalization exists.
- Current real artifacts keep `claim_allowed: false`; absent or incomplete metrics must not be filled with guessed values.

## Current audit note

Synthetic or mock material is still present in legacy and example paths, including `data/posterior_unified_synth.csv`, mock figure names under `figs/`, fixture-like examples under `data/rll_latentes/examples/`, and `results/dha/mock_catalog.csv`. Those are acceptable only as code-truth or illustrative assets when cataloged in the legacy manifest. Real validation outputs must not depend on `data/synthetic/`, `results/synthetic/`, `tests/fixtures/`, or any manifest-listed legacy synthetic path for scientific claims.
