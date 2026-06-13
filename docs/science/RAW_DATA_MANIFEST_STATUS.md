# Raw Data Manifest Status

Status: raw-data custody status  
Claim level: `claim_allowed=false`

Total records: **7**  
Raw files present: **1**  
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

---

## Meaning

This is the first raw-data custody layer with one local raw file now present.

The first local raw file is a NASA/JPL Horizons Mars observer-ephemeris sample. It is useful for custody, provenance, parser, and observer-ephemeris feature tests.

It is not yet the state-vector dataset required for orbital v2.

---

## Safe conclusion

Raw data custody now contains one local raw file with SHA256. Scientific claims remain blocked until route-specific raw vectors, baselines, and uncertainty models exist.
