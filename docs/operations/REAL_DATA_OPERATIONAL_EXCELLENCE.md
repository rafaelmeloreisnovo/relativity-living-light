# Real Data Operational Excellence

## Status

`governance_record / source_registered`

## Purpose

This document defines operational practices for adding, checking and using real data in the repository without inflating claims.

## Golden rule

Real public source registration is not the same as local real-data validation.

A source becomes operationally usable only after it has provenance, access date, local artifact path, checksum, ingestion command, schema validation, metric output, baseline or adversary, and claim boundary.

## Directory practice

Use stable layers:

```text
data/real/                         real-data registry and manifests
data/real/cosmology/               cosmology real-data sources
data/real/cosmology/<source_id>/   source-specific downloaded or materialized artifacts
artifacts/real-data/               generated validation outputs, not source truth
docs/operations/                   operational procedures and policies
docs/real_data/                    source-specific documentation and reports
```

## States

| State | Meaning |
|---|---|
| `SOURCE_REGISTERED` | Public real source is identified but not locally ingested. |
| `INGESTION_READY` | Download command, expected schema and destination exist. |
| `INGESTED_UNVERIFIED` | Local artifact exists but hash/schema/metrics are incomplete. |
| `INGESTED_VERIFIED` | Local artifact, hash and schema checks pass. |
| `METRIC_READY` | A reproducible metric has been computed. |
| `BASELINE_COMPARED` | Metric has been compared against baseline or adversary. |
| `REAL_VALIDATED_LIMITED` | A limited, bounded claim may be made. |
| `CLAIM_BLOCKED` | Required evidence is missing or contradictory. |

## Required metadata per source

Each real-data source must record:

- source identifier;
- public URL or DOI;
- access date;
- license or usage note when available;
- local artifact path;
- checksum;
- ingestion command;
- expected schema;
- validation command;
- metric command;
- baseline or adversary;
- uncertainty or covariance policy;
- claim boundary;
- next action.

## Good practices

1. Keep raw source artifacts separate from derived outputs.
2. Never overwrite raw artifacts without a new checksum record.
3. Do not mix mock and real data in the same output directory.
4. Prefer small manifests over large opaque commits.
5. Use deterministic scripts for ingestion and validation.
6. Treat missing checksum as `TOKEN_VAZIO`.
7. Treat missing covariance policy as `REAL_VALIDATED_BLOCKED`.
8. Treat successful parsing as metadata readiness, not validation.
9. Treat baseline comparison as mandatory before any superiority language.
10. Keep claim language weaker than the evidence.

## Review checklist

Before merging real-data additions, verify:

- the source is public or legally usable;
- source path and local path are both declared;
- checksum is present or explicitly marked `TOKEN_VAZIO`;
- ingestion does not require secrets unless documented;
- mock outputs are not mixed with real outputs;
- validation script exists;
- metric and baseline are declared;
- claim boundary is explicit;
- README or report states what is not proven.

## Boundary

This operational layer improves readiness. It does not prove RLL, does not validate cosmology, and does not authorize superiority claims.

## Canonical cosmology source manifest

The canonical manifest for committed cosmology real-data inputs is:

```text
data/real/cosmology/observational_sources_manifest.json
```

Operational consumers must reference canonical real inputs by `source_id`, `sha256`, `local_path`, and `dataset_type` instead of copying free-form status strings. `data/pipelines/structure_d/datasets_config.json` is the Structure-D consumer of these fields, and `data/inputs/cosmology_joint/joint_real_inputs_manifest.json` consumes the same source identifiers for the joint real likelihood route.

Real observational entries must pass the path boundary enforced by `data.pipelines.structure_d.synthetic_real_boundary.validate_real_dataset_manifest_entry`: any real dataset path containing `synthetic`, `mock`, `demo`, `fixture`, or `example` is invalid. Explicit test fixtures may be marked as regression fixtures, but they are classified as `synthetic_regression_test` and remain blocked from real validation.

## Synthetic preservation rule

Synthetic artifacts are allowed only under these preservation zones:

```text
data/synthetic/
results/synthetic/
tests/fixtures/
```

Legacy synthetic artifacts outside those zones are tolerated only when they are registered in:

```text
data/synthetic/LEGACY_SYNTHETIC_MANIFEST.json
```

Those exceptions must keep `scientific_use_allowed: false` and a synthetic dataset type. They are compatibility records, not real-data sources, and must not be promoted into real validation manifests.
