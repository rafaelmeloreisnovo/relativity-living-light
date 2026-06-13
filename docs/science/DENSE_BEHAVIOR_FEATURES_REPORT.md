# Dense Behavior Features Report

Status: seed-derived feature layer  
Claim level: `claim_allowed=false`

This report turns mapped seed records into a denser feature matrix for later raw-data validation.

---

## Inputs

```text
data/results/bootstrap/real_seed_ingestion_plan.json
data/results/orbital_dynamics/angular_momentum_shape_validation.json
data/results/bootstrap/token_vazio_priority_ledger.json
data/results/negative_results_ledger.json
```

## Outputs

```text
data/results/bootstrap/dense_behavior_features.json
data/results/bootstrap/dense_behavior_features.tsv
docs/science/DENSE_BEHAVIOR_FEATURES_REPORT.md
```

---

## Behavior classes

| Class | Count |
|---|---:|
| `reference_motion_profile` | 4 |
| `high_value_next_measure` | 7 |
| `seed_metric_ready_claim_blocked` | 4 |
| `negative_result_guarded` | 4 |

---

## Highest readiness seed-stage items

| Record | Route | Class | Score | Next math target |
|---|---|---|---:|---|
| `REAL_ORBIT_EARTH_HELIOCENTRIC_SHAPE_AM_V1` | `orbital_shape_angular_momentum` | `reference_motion_profile` | 0.65 | `state_vector_vs_reference_h_residual` |
| `REAL_ORBIT_MOON_GEOCENTRIC_SHAPE_AM_V1` | `orbital_shape_angular_momentum` | `reference_motion_profile` | 0.65 | `state_vector_vs_reference_h_residual` |
| `REAL_ORBIT_MARS_HELIOCENTRIC_SHAPE_AM_V1` | `orbital_shape_angular_momentum` | `reference_motion_profile` | 0.65 | `state_vector_vs_reference_h_residual` |
| `REAL_ORBIT_JUPITER_HELIOCENTRIC_SHAPE_AM_V1` | `orbital_shape_angular_momentum` | `reference_motion_profile` | 0.65 | `state_vector_vs_reference_h_residual` |
| `REAL_SEED_GW230529_181500` | `compact_remnant_boundary` | `high_value_next_measure` | 0.55 | `mass_gap_overlap_probability` |
| `REAL_SEED_PSR_J0740_6620` | `compact_remnant_boundary` | `high_value_next_measure` | 0.55 | `mass_gap_overlap_probability` |
| `REAL_SEED_GW190814` | `compact_remnant_boundary` | `high_value_next_measure` | 0.55 | `mass_gap_overlap_probability` |
| `REAL_SEED_PSR_J0952_0607` | `compact_remnant_boundary` | `high_value_next_measure` | 0.55 | `mass_gap_overlap_probability` |

---

## Orbital dense features now available

```text
specific_orbital_angular_momentum_km2_s
mean_orbital_speed_proxy_km_s
spin_angular_momentum_proxy_kg_m2_s
total_orbital_angular_momentum_proxy_kg_m2_s
spin_orbit_ratio_proxy
flattening
j2
```

Next math targets:

```text
state_vector_vs_reference_h_residual
spin_orbit_ratio_series
shape_gravity_residual
torque_proxy_over_time
```

---

## Safe conclusion

This layer increases data density and identifies next mathematical targets. It remains seed-stage only until raw data, checksum, uncertainty, and baselines are added.
