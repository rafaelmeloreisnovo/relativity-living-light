# Data Gap Scan and Structure Linkage Ledger

Status: operational data-gap ledger  
Scope: RLL cosmology, structure formation, residual gravity, compact objects, wandering black holes, lensing, gravitational-wave catalogs  
Claim level: conservative; no validation claim without dataset ingestion and reproducible metrics

---

## 1. Purpose

This document defines the missing-data scan needed to connect the recent RLL hypothesis modules to real observable structures.

It links each missing concept to:

- required dataset;
- required observable;
- required source ledger;
- required pipeline structure;
- expected validation script;
- claim status.

This file exists to prevent conceptual gaps from becoming unsupported claims.

---

## 2. Absolute rule

No claim is allowed from conceptual structure alone.

Every future statement must be classified as:

```text
FATO_VERIFICADO
HIPOTESE
LACUNA
TOKEN_VAZIO
BLOQUEADO
ERRO
RISCO
ACAO_RECOMENDADA
```

If the dataset is not ingested, hashed, cited, and connected to a metric, the status remains:

```text
blocked / TOKEN_VAZIO / LACUNA
```

---

## 3. Data-gap map

| Module | Missing data | Required observable | Structure to create/connect | Status |
|---|---|---|---|---|
| wandering black holes | candidate catalog | lensing / dynamics / accretion limits | `data/real/compact_objects/wandering_black_hole_sources.yml` | TOKEN_VAZIO |
| silent black holes | multiwavelength non-detections + mass evidence | X-ray/radio/IR/optical limits + dynamics | `data/real/compact_objects/silent_black_hole_candidates.yml` | TOKEN_VAZIO |
| dark lenses | lensing event/candidate catalogs | microlensing, astrometric lensing, weak/strong lensing | `data/real/lensing/dark_lens_sources.yml` | TOKEN_VAZIO |
| historical slingshot impulse | trajectory traceback data | proper motion, radial velocity, origin reconstruction | `data/real/kinematics/hypervelocity_sources.yml` | TOKEN_VAZIO |
| recoiling black holes | offset AGN / BH recoil candidates | spatial offset, velocity offset, host model | `data/real/compact_objects/recoiling_bh_sources.yml` | TOKEN_VAZIO |
| residual gravitational structures | disrupted galaxies / streams / orphan halos | streams, velocity dispersion, lensing mass | `data/real/structure/residual_gravity_sources.yml` | TOKEN_VAZIO |
| compact remnant boundary | NS/BH mass catalogs | mass, radius, EOS constraints, GW event masses | `data/real/compact_objects/remnant_boundary_sources.yml` | TOKEN_VAZIO |
| lower mass gap | compact-object events in 2.5-5 Msun range | GW posterior masses / EM constraints | `data/real/compact_objects/lower_mass_gap_sources.yml` | TOKEN_VAZIO |
| pair-instability gap | high-mass BH catalogs | BH mass, metallicity, channel | `data/real/compact_objects/pair_instability_gap_sources.yml` | TOKEN_VAZIO |
| early SMBH seeds | high-z AGN / quasar / JWST sources | redshift, BH mass, host properties | `data/real/high_z_smbh/high_z_seed_sources.yml` | TOKEN_VAZIO |
| cosmological connection | DESI/Planck/Pantheon/fsigma8 integrated covariance | covariance-aware model comparison | existing cosmology validation pipeline | blocked |

---

## 4. Required repository structure

Recommended directories:

```text
data/real/compact_objects/
data/real/lensing/
data/real/kinematics/
data/real/structure/
data/real/high_z_smbh/
data/results/compact_objects/
data/results/lensing/
data/results/structure/
scripts/data_scan/
scripts/validation/
```

Recommended docs:

```text
docs/science/WANDERING_BLACK_HOLES_AND_LENSING_GAPS.md
docs/science/GRAVITATIONAL_RESIDUAL_MEMORY_AND_COMPACT_GAPS.md
docs/science/DATA_GAP_SCAN_AND_STRUCTURE_LINKAGE.md
```

---

## 5. Minimal source-ledger schema

Every source ledger must include:

```yaml
source_record:
  id: TOKEN_VAZIO
  module: TOKEN_VAZIO
  dataset_name: TOKEN_VAZIO
  provider: TOKEN_VAZIO
  url_or_reference: TOKEN_VAZIO
  access_date_utc: TOKEN_VAZIO
  license_or_terms: TOKEN_VAZIO
  data_type: observational | catalog | paper | simulation | derived | TOKEN_VAZIO
  raw_data_available: false
  local_path: TOKEN_VAZIO
  checksum_sha256: TOKEN_VAZIO
  observables:
    - TOKEN_VAZIO
  required_columns:
    - TOKEN_VAZIO
  baseline_models:
    - TOKEN_VAZIO
  validation_metric: TOKEN_VAZIO
  claim_allowed: false
  status: TOKEN_VAZIO
```

---

## 6. Minimal validation linkage

Each data source must be linked to at least one validation pathway:

| Data type | Required validation |
|---|---|
| microlensing | mass posterior, lens-source geometry, event timescale, alternative models |
| astrometric lensing | source position shift, parallax/proper motion, lens mass model |
| strong lensing | image configuration, time delays, mass model, luminous counterpart search |
| weak lensing | shear catalog, redshift distribution, mass reconstruction |
| hypervelocity star | 6D phase-space if possible, traceback, origin probability |
| recoiling AGN/BH | spatial offset, velocity offset, host-galaxy model, merger alternative |
| compact remnant | mass posterior, object class, EOS or BH baseline |
| gravitational wave | posterior masses/spins, event ID, waveform model, catalog version |
| high-z SMBH | redshift, BH mass estimate, luminosity/accretion assumptions, host constraints |
| disrupted galaxy | stream morphology, kinematics, mass model, simulation comparison |

---

## 7. Pipeline scan requirements

Future automation must perform:

```text
1. locate source ledgers
2. validate YAML syntax
3. validate required fields
4. check local paths
5. compute or verify SHA256
6. classify TOKEN_VAZIO/LACUNA/BLOQUEADO
7. link each source to one module
8. link each module to one required observable
9. link each observable to one validation script
10. write machine-readable summary
```

Expected output:

```text
data/results/data_gap_scan_summary.json
data/results/data_gap_scan_ledger.tsv
docs/science/DATA_GAP_SCAN_REPORT.md
```

---

## 8. Script stubs to add later

Recommended scripts:

```text
scripts/data_scan/scan_source_ledgers.py
scripts/data_scan/validate_gap_schema.py
scripts/data_scan/build_data_gap_report.py
scripts/validation/validate_wandering_bh_candidates.py
scripts/validation/validate_dark_lens_candidates.py
scripts/validation/validate_compact_remnant_boundary.py
scripts/validation/validate_residual_gravity_structures.py
```

These scripts should not invent missing data. They should fail closed when source records remain empty.

---

## 9. Claim boundary by module

| Module | Claim allowed now? | Reason |
|---|---|---|
| wandering black holes | false | no catalog wired |
| silent black holes | false | no multiwavelength + dynamical evidence wired |
| dark lenses | false | no lensing candidate ledger wired |
| historical impulse | false | no traceback dataset wired |
| residual gravitational structures | false | no stream/lensing/kinematics catalog wired |
| compact remnant boundary | false | no mass catalog ingestion wired |
| cosmological RLL superiority | false | current visible BAO + H(z) artifacts favor LCDM by AIC/BIC |

Allowed now:

```text
RLL may define these as hypothesis modules and data-gap structures.
```

Not allowed now:

```text
RLL has validated these modules observationally.
```

---

## 10. Next action order

1. Create source ledgers with TOKEN_VAZIO protected.
2. Add schema validator for source ledgers.
3. Add scan script to produce JSON/TSV report.
4. Ingest one real catalog at a time.
5. Only then add model-comparison metrics.
6. Keep all claims blocked until metrics exist.

---

## 11. Safe conclusion

The missing work is not only to gather more data. The missing work is to link each data class to the exact RLL structure it is meant to test.

Therefore:

```text
data without structure = archive only
structure without data = hypothesis only
data + structure + metric + baseline = testable science
```

---

## Retrofeedback

F_ok: missing data classes are now mapped to required RLL structures.  
F_gap: source ledgers still need real dataset records and checksums.  
F_next: create YAML ledgers for compact objects, residual gravity, lensing, and kinematics.
