# First Raw Data Ingestion Report

Status: first raw-data file locally versioned  
Claim level: `claim_allowed=false`

---

## Raw file added

```text
data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_observer_2006_sample.csv
```

Metadata:

```text
data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_observer_2006_sample.meta.yml
```

---

## Source

Provider:

```text
NASA/JPL Horizons API
```

Query role:

```text
Mars observer ephemeris from geocentric observer context, 2006-Jan-01 to 2006-Jan-05 sample rows
```

---

## Custody

```text
sha256: 9c8a018c46865766ae00a42340341207b7fe4ae974ca9ec3ccaca257a3eca6e8
bytes: 1146
raw_data_local: true
claim_allowed: false
```

---

## What this raw data contains

```text
date_utc
RA/DEC
apparent magnitude
surface brightness
observer-target range delta
range-rate deldot
solar elongation angle
Sun-target-observer angle
constellation
```

---

## What it does not yet contain

```text
Cartesian state vectors r and v
h_vector = |r x v|
SPICE kernel
gravity harmonics
shape model
uncertainty/covariance model
baseline comparison
```

---

## Meaning

This is the first real raw-data ingestion into the repository custody layer. It proves the pipeline can now hold a local raw file with source metadata and SHA256.

It does not yet complete orbital v2. For orbital v2, the next required raw dataset is a Horizons/SPICE state-vector table.

---

## Safe conclusion

The repository has moved from zero raw files to one raw file under custody. Scientific claims remain blocked until the required state-vector/baseline/error chain exists.
