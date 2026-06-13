# Raw Data Manifest Status

Status: raw-data custody status  
Claim level: `claim_allowed=false`

Total records: **6**  
Raw files present: **0**  
Raw files missing: **6**

---

## Custody slots

| Raw ID | Route | File present | SHA matches | Next metric |
|---|---|---:|---:|---|
| `RAW_PENDING_GW190814_POSTERIOR` | `compact_remnant_boundary` | `false` | `false` | `mass_gap_overlap_probability` |
| `RAW_PENDING_GW230529_POSTERIOR` | `compact_remnant_boundary` | `false` | `false` | `mass_gap_overlap_probability` |
| `RAW_PENDING_EARTH_STATE_VECTOR` | `orbital_shape_angular_momentum` | `false` | `false` | `state_vector_vs_reference_h_residual` |
| `RAW_PENDING_MARS_STATE_VECTOR` | `orbital_shape_angular_momentum` | `false` | `false` | `state_vector_vs_reference_h_residual` |
| `RAW_PENDING_GAIA_BH1_ASTROMETRY` | `wandering_dark_compact_mass` | `false` | `false` | `astrometric_dark_mass_consistency` |
| `RAW_PENDING_UHZ1_HIGHZ_CONTEXT` | `high_z_smbh_seeds` | `false` | `false` | `Eddington_growth_feasibility_grid` |

---

## Meaning

This is the first raw-data custody layer.

It does not contain the raw datasets yet. It creates named slots where raw files can be placed, hashed, and tied to a scientific route.

---

## Safe conclusion

Raw data custody is scaffolded. Missing files remain TOKEN_VAZIO and cannot support claims.
