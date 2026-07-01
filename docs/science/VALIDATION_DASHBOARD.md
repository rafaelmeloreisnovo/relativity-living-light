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

## Latent thesis registry

| Artifact | Role |
|---|---|
| `data/real_sources/rll_latent_theses_registry.yml` | registry of claim-gated latent theses |
| `docs/science/RLL_LATENT_THESES_AND_RECENT_DATA_CROSSWALK.md` | formal crosswalk from recent-data context to hypotheses/tests |
| `tools/validate_latent_theses_registry.py` | registry validator |
| `tests/test_latent_theses_registry.py` | CI coverage |

Rule: latent theses are test programs, not validation claims.

---

## Required data gap registry

| Artifact | Role |
|---|---|
| `data/real_sources/rll_required_data_gap_registry.yml` | route-level missing-data and missing-artifact registry |
| `docs/science/RLL_REQUIRED_DATA_GAPS_IMPLEMENTATION.md` | implementation note for gaps and required evidence |
| `tools/validate_required_data_gap_registry.py` | registry validator |
| `tests/test_required_data_gap_registry.py` | CI coverage |

Rule: a registered gap is a required next input, not proof that the input is already present.

---

## Counts

```text
routes_total: 7 including cosmology_background
active_seed_routes: 6
computed_seed_routes: 5+
raw_data_complete_routes: 0
claim_allowed_true_routes: 0
latent_theses_registered: 6
latent_theses_claim_allowed_true: 0
required_data_gaps_registered: 8
required_data_gap_claim_allowed_true: 0
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
7. latent thesis registry with falsifiers and baselines
8. required data gap registry with route-level missing inputs
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
7. latent theses still require route-specific data, metrics and falsifier execution
8. P0 gaps still require materialized inputs or executable artifacts
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

The repository now has a working validation scaffold, multiple seed-level artifacts, a latent-thesis registry and a required-data gap registry. It is still claim-gated: stronger claims require materialized data, checksums, baselines, error models and executed falsifier metrics.
