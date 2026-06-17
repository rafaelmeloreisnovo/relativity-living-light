# Real Seed Validation v0 Index

Status: generated seed-validation index  
Claim level: seed-level calculation only; no final scientific claim

> These outputs are seed-level calculations only. They do not validate final scientific claims.

---

## Outputs

| Output | Module | Status | Claim allowed |
|---|---|---|---:|
| `data/results/compact_objects/remnant_boundary_validation.json` | `compact_remnant_boundary` | `seed_metric_ready_claim_blocked` | `false` |
| `data/results/compact_objects/wandering_bh_validation.json` | `wandering_black_holes_dark_lens` | `seed_metric_ready_claim_blocked` | `false` |
| `data/results/kinematics/historical_impulse_validation.json` | `historical_impulse_slingshot` | `seed_metric_ready_claim_blocked` | `false` |
| `data/results/high_z_smbh/seed_validation.json` | `high_z_smbh_seeds` | `seed_metric_ready_claim_blocked` | `false` |

---

## What changed

The repository now has materialized v0 artifacts for each real observational seed module:

1. Compact remnant / lower mass gap.
2. Wandering or silent black hole / dark lens.
3. Historical impulse / slingshot trajectory memory.
4. High-redshift SMBH seed-growth constraint.

---

## Safe conclusion

The repository now has first-pass calculations for each real observational seed module, but raw catalogs, checksums, posterior files, full error models, and baseline comparisons are still required.

```text
seed data + v0 calculation = readiness artifact
seed data + v0 calculation ≠ final validation claim
```

---

## Likely workflow failure explanation

If the GitHub Actions run failed in strict mode, that failure is expected while any ledger still contains `TOKEN_VAZIO`, missing raw catalog data, or blocked claim status.

If the run produced no versioned artifacts, that is because GitHub Actions uploads artifacts to the run, but does not automatically commit generated files back to the repository.

This file materializes the seed-validation output trail in the repository.
