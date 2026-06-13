# Raw Data Manifest Status

Status: raw-data custody status  
Claim level: `claim_allowed=false`

Total records: **8**  
Raw files present: **2**  
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
| `RAW_JPL_HORIZONS_MARS_OBSERVER_2006_SAMPLE` | `orbital_shape_angular_momentum` | `true` | `true` | `observer_ephemeris_delta_deldot_profile` |
| `RAW_JPL_HORIZONS_MARS_VECTORS_2006_SAMPLE` | `orbital_shape_angular_momentum` | `true` | `true` | `state_vector_vs_reference_h_residual` |

---

## Meaning

The raw-data custody layer now contains two local raw files:

```text
1. Mars observer ephemeris sample
2. Mars heliocentric Cartesian state-vector sample
```

The second file is the first raw vector dataset used by orbital v2.

---

## Safe conclusion

Raw data custody now contains two local JPL Horizons samples with SHA256. Orbital v2 has a raw vector residual, but scientific claims remain blocked until baselines and uncertainty models exist.
