# Real Seed Validation v0 Index

Status: generated seed-validation index

> These outputs are seed-level calculations only. They do not validate final scientific claims.

| Output | Module | Status | Claim allowed |
|---|---|---|---:|
| `data/results/compact_objects/remnant_boundary_validation.json` | `compact_remnant_boundary` | `seed_metric_ready_claim_blocked` | `false` |
| `data/results/compact_objects/wandering_bh_validation.json` | `wandering_black_holes_dark_lens` | `seed_metric_ready_claim_blocked` | `false` |
| `data/results/compact_objects/wandering_bh_source_readiness.json` | `wandering_black_holes_and_lensing_gaps` | `blocked_missing_observational_data` | `false` |
| `data/results/kinematics/historical_impulse_validation.json` | `historical_impulse_slingshot` | `seed_metric_ready_claim_blocked` | `false` |
| `data/results/high_z_smbh/seed_validation.json` | `high_z_smbh_seeds` | `seed_metric_ready_claim_blocked` | `false` |
| `data/results/structure/residual_gravity_validation.json` | `gravitational_residual_memory_and_compact_gaps` | `blocked_missing_observational_data` | `false` |

---

## What changed

The repository now has materialized v0 artifacts for each real observational seed module, including the wandering-BH readiness scan added for source-level claim gating.

1. Compact remnant / lower mass gap.
2. Wandering or silent black hole / dark lens.
3. Wandering/recoiling black-hole source readiness.
4. Historical impulse / slingshot trajectory memory.
5. High-redshift SMBH seed-growth constraint.
6. Residual gravity / compact gaps readiness.

---

## Safe conclusion

The repository now has first-pass calculations for each real observational seed module, but raw catalogs, checksums, posterior files, full error models, and baseline comparisons are still required.

```text
seed data + v0 calculation = readiness artifact
seed data + v0 calculation ≠ final validation claim
```

---

## Likely workflow failure explanation

If a strict workflow fails while any ledger still contains `TOKEN_VAZIO`, missing raw catalog data, or blocked claim status, that failure is expected and protects the repository from unsupported claims.

If CI uploads artifacts but does not commit generated files, materialize the canonical JSON/CSV/MD outputs locally and commit them with the corresponding validation command in the PR body.
