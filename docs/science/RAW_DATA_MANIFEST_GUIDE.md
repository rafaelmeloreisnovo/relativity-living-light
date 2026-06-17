# Raw Data Manifest Guide

Status: operational guide  
Claim level: `claim_allowed=false`

---

## Purpose

The raw data manifest turns future downloaded or manually added datasets into auditable custody records.

A seed record becomes stronger only when it gains:

```text
source_url
access_date_utc
license_or_terms
source_version
local_path
sha256
bytes
raw_data_local=true
```

Even then, scientific claims still require:

```text
metric
baseline
uncertainty/error model
machine output
negative-results update if needed
```

---

## Main manifest

```text
data/raw/RAW_DATA_MANIFEST.yml
```

---

## Status artifacts

```text
data/results/bootstrap/raw_data_manifest_status.json
data/results/bootstrap/raw_data_manifest_status.tsv
docs/science/RAW_DATA_MANIFEST_STATUS.md
```

---

## Helper command

```bash
python scripts/data_scan/build_raw_data_manifest_status.py
```

---

## First priority raw slots

```text
RAW_PENDING_GW190814_POSTERIOR
RAW_PENDING_GW230529_POSTERIOR
RAW_PENDING_EARTH_STATE_VECTOR
RAW_PENDING_MARS_STATE_VECTOR
RAW_PENDING_GAIA_BH1_ASTROMETRY
RAW_PENDING_UHZ1_HIGHZ_CONTEXT
```

---

## Safe conclusion

This guide defines custody. It does not authorize claims. `claim_allowed` remains false until the full evidence chain exists.
