# Canonical Route Checklist

Status: canonical route checklist  
Claim level: `claim_allowed=false`

Source control file:

```text
data/real/bootstrap/canonical_route_checklist.yml
```

---

## Meaning

This is a checkbox view of route readiness. It separates:

```text
what already exists
what is still TOKEN_VAZIO or incomplete
what can be packaged as artifact
what remains blocked from claim
```

---

## Global artifact export

- [x] supports combined ZIP artifact
- [x] supports separated route artifacts
- [x] claim boundary preserved
- [ ] all routes review-ready

---

## P0 routes

### Raw data custody governance

- [x] raw or seed present
- [x] sha256 present
- [ ] schema present
- [ ] tests present
- [x] CI present
- [ ] baseline present
- [ ] uncertainty present
- [ ] negative ledger updated after latest raw status
- [x] report present
- [ ] ready for review

Artifacts:

```text
data/raw/RAW_DATA_MANIFEST.yml
data/results/bootstrap/raw_data_manifest_status.json
data/results/bootstrap/raw_data_manifest_status.tsv
docs/science/RAW_DATA_MANIFEST_STATUS.md
docs/science/RAW_DATA_MANIFEST_GUIDE.md
```

### Orbital shape angular momentum

- [x] raw or seed present
- [x] sha256 present
- [ ] schema present
- [ ] tests present
- [x] CI present
- [ ] baseline present
- [ ] uncertainty present
- [ ] negative ledger updated after orbital v2
- [x] report present
- [ ] ready for review

Artifacts:

```text
data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv
data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv
data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml
data/results/orbital_dynamics/orbital_state_vector_v2_validation.json
docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md
```

### Compact remnant boundary

- [x] raw or seed present
- [ ] sha256 present
- [ ] schema present
- [ ] tests present
- [ ] CI present
- [ ] baseline present
- [ ] uncertainty present
- [x] negative ledger updated
- [x] report present
- [ ] ready for review

---

## P1 routes

### High-z SMBH seeds

- [x] raw or seed present
- [ ] sha256 present
- [ ] schema present
- [ ] tests present
- [ ] CI present
- [ ] baseline present
- [ ] uncertainty present
- [x] negative ledger updated
- [ ] report present
- [ ] ready for review

### Wandering dark compact mass

- [x] raw or seed present
- [ ] sha256 present
- [ ] schema present
- [ ] tests present
- [ ] CI present
- [ ] baseline present
- [ ] uncertainty present
- [x] negative ledger updated
- [ ] report present
- [ ] ready for review

### Publication and product packaging

- [x] raw or seed present
- [ ] sha256 present
- [ ] schema present
- [ ] tests present
- [ ] CI present
- [ ] baseline present
- [ ] uncertainty present
- [ ] negative ledger updated
- [x] report present
- [ ] ready for review

---

## Safe conclusion

This checklist is operational. It does not authorize scientific claims. Its job is to show what can be packaged, what is incomplete, and what must remain blocked.
