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

## Numerical anchors

```text
ideal-gas steam reference     1.6996519706 m³ per kg at 373.15 K / 1 atm
electron/proton FE/FG         2.2686614330e39
Q_T at Md/MBH=0.10            2.2360679775  (backreaction gate)
Q_T at Md/MBH=0.25            0.8944271910  (instability candidate)
T_orb at 20 rg, 10 Msun       0.0276813661 s
T_orb at 20 rg, 4.3e6 Msun    11902.9874443 s
```

## Verification

Local isolated execution:

```text
PYTHONPATH=src python -m pytest -q tests/test_strong_gravity_calibration.py
16 passed
```

GitHub Actions execution:

```text
Run structural and strong-gravity tests       success
Reproduce committed numeric calibration       success
```

The workflow runs the previous 16 structural tests plus the new 16 calibration tests and compares the regenerated JSON byte-for-byte with the committed result.

## Extension commit ledger

| Order | Commit | Function |
|---:|---|---|
| 1 | `c658d5f6bf3d909dc9892f2e207acd899ad8ea37` | unit-aware strong-gravity operators and recurrence |
| 2 | `5a86295df55f8a3797ff8029ac1fbe56dfe3449f` | 16 calibration and boundary tests |
| 3 | `f93b944ea3ebc8c79a99ab14c1e2bc1810d0e99d` | deterministic numerical runner |
| 4 | `7268680b96e7267f77cde528609b0f572f8a3905` | committed numerical sweep |
| 5 | `25d63be20e0348e0b56c94e5a7369fbfa72c91b9` | heuristic and artifact registry |
| 6 | `5fa2894d0c72734b08f4d3c8bcb3a4756cf84cb0` | scientific calibration documentation |
| 7 | `3aa1874dcfe3704317b3b24b1d81e8d99dc44a08` | initial delivery index |
| 8 | `c961e012e40dc7ebeba8cf79ae1b5ea5bb6a53fa` | B08/B09 operational integration |
| 9 | `9b8d31be943f7b73abd446bb8c14534902f5ba79` | combined tests and numerical reproduction CI |

This file is the final traceability commit for the extension.

## Epistemic boundary

The implementation formalizes and calibrates the session's analogies. It does not claim that atomic gravity dominates electromagnetic binding, that electrolysis literally occurs without an electrolyte/electrodes, that the reference ring is a GRMHD solution, or that an RLL-specific coupling has been detected.

`F_ok`: mechanisms, scales, recurrence, numerical anchors and CI are explicit.  
`F_gap`: source-specific fields, composition, cross sections, covariance and observational targets remain `TOKEN_VAZIO`.  
`F_next`: replace the reference ring with a declared self-gravitating GRMHD/GRPIC source manifest before fitting any physical parameter.
