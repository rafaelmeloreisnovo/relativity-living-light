# Validation Dashboard

Status: operational maturity dashboard  
Claim level: `claim_allowed=false`

This dashboard summarizes what exists, what is blocked, and what the next measurable action is.

---

## Route maturity table

| Route | Seed map | Computed artifact | Raw data | Checksum | Baseline | Error/covariance | Claim | Next action |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `compact_remnant_boundary` | yes | v0 | no | no | partial/planned | no | false | ingest LVK/GWOSC posterior samples and compute mass-gap overlap |
| `wandering_dark_compact_mass` | yes | v0 | no | no | planned | no | false | ingest Gaia/OGLE astrometry/RV/light-curve data |
| `residual_gravity_structures` | yes | weak/planned | no | no | planned | no | false | add validator and Gaia/stream membership metric |
| `historical_impulse_slingshot` | yes | v0 | no | no | planned | no | false | ingest HVS table and compute traceback probability |
| `high_z_smbh_seeds` | yes | v0 | no | no | planned | no | false | ingest JWST/Chandra context and model seed-growth baselines |
| `orbital_shape_angular_momentum` | yes | v1 | no | no | planned | no | false | ingest SPICE/JPL/Horizons vectors and compare to seed metrics |
| `cosmology_background` | partial | blocked/mixed | partial | partial | partial | partial | false | rebuild covariance-aware LCDM/wCDM/CPL comparison |

---

## Counts

```text
routes_total: 7 including cosmology_background
active_seed_routes: 6
computed_seed_routes: 5+
raw_data_complete_routes: 0
claim_allowed_true_routes: 0
```

---

## Current strongest assets

```text
1. claim boundary discipline
2. seed catalogs v0/v1/v2
3. CI artifacts for real seed validation and orbital v1
4. orchestration map
5. negative results ledger
6. TOKEN_VAZIO priority ledger
```

---

## Current biggest blockers

```text
1. raw data with sha256
2. formal schemas
3. automated tests
4. baselines per route
5. covariance/error models
6. cosmology_background remains blocked for final RLL claim
```

---

## Recommended next route

Priority route:

```text
compact_remnant_boundary
```

Reason:

```text
It has clear seeds, clear raw data path, clear metric, and a falsifiable baseline.
```

Next measurable metric:

```text
mass_gap_overlap_probability
```

---

## Safe conclusion

The repository now has a working validation scaffold and multiple seed-level artifacts. It is not yet a final scientific proof engine because raw data, checksums, baselines, and error models are still missing.
