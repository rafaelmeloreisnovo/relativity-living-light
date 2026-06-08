# Test fixtures

Fixtures are test-only data and must never be classified as `real_observational`.

Fixtures may emulate real schemas, failure modes, rollback states, or incomplete ledgers, but they remain `synthetic_regression_test` and must keep `claim_allowed: false` when serialized as JSON.

If a fixture-like artifact still lives outside `tests/fixtures/` for compatibility, it must be cataloged in `data/synthetic/LEGACY_SYNTHETIC_MANIFEST.json` with `scientific_use_allowed: false`.
