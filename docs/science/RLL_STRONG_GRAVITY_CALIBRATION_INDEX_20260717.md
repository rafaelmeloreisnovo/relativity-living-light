# RLL Strong-Gravity Calibration Index — 2026-07-17

**Branch:** `agent/rll-operational-integration-house-20260717`  
**PR:** `#563`  
**Claim state:** `claim_allowed=false`

## Delivery order

1. `src/rll/strong_gravity_calibration.py`
2. `tests/test_strong_gravity_calibration.py`
3. `scripts/run_strong_gravity_calibration.py`
4. `results/strong_gravity_calibration/session_reference_sweep_20260717.json`
5. `data/registries/rll_strong_gravity_calibration_registry.json`
6. `docs/science/RLL_STRONG_GRAVITY_HEURISTIC_CALIBRATION_20260717.md`
7. `data/registries/rll_operational_integration_registry.json`
8. `.github/workflows/rll-structural-integration.yml`

## Implemented branch extension

```text
B08 strong-gravity magnetokinetic conversion
B09 gravitational-electrodissociative recurrent calibration
```

## Verification target

```text
PYTHONPATH=src python -m pytest -q \
  tests/test_structural_integration.py \
  tests/test_strong_gravity_calibration.py

32 tests expected
```

The numerical artifact is regenerated in CI and compared byte-for-byte with the committed JSON.

## Epistemic boundary

The implementation formalizes and calibrates the session's analogies. It does not claim that atomic gravity dominates electromagnetic binding, that electrolysis literally occurs without an electrolyte/electrodes, or that an RLL-specific coupling has been detected.
