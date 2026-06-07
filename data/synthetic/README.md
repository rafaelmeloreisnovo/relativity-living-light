# Synthetic data

Synthetic inputs belong here when they are used for code sanity, examples, numerical stability checks, or regression tests. They cannot support scientific claims.

## Required metadata

Serialized synthetic JSON artifacts should include:

- `dataset_type: synthetic_sanity_check` or `dataset_type: synthetic_regression_test`;
- `claim_allowed: false`;
- enough provenance to reproduce how the file was generated.

## Legacy manifest

`LEGACY_SYNTHETIC_MANIFEST.json` catalogs legacy synthetic/mock/demo/example/fixture artifacts that still live outside `data/synthetic/`, `results/synthetic/`, and `tests/fixtures/` for compatibility. These entries are documented in place rather than deleted, with proposed boundary paths for future migrations.

Every manifest entry has `scientific_use_allowed: false`. `code_test_use_allowed` only means the artifact can be used for tests or diagnostics; it does not grant scientific use.
