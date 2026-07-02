# Relational Validation Artifacts

## Status

`artifacts_root / relational_validation / evidence_package_policy`

## Purpose

This directory stores artifacts produced by relational-validation checks.

Accepted artifacts include:

```text
metric tables
model comparison tables
manifest files
checksums
relation graphs
summary reports
negative ledgers
contradiction checks
review packets
```

## Rule

```text
An artifact is evidence only inside a declared relation package.
A relation package must link source, log, artifact, metric, baseline, uncertainty status and claim boundary.
```

## Naming convention

```text
YYYYMMDD_<claim_id>_<relation_graph_id>_<artifact_kind>.<ext>
```

## Minimal artifact manifest

Each artifact package should include or reference:

```text
claim_id
relation_graph_id
source_paths
log_paths
artifact_paths
sha256
metric_names
baseline_or_adversary
uncertainty_or_covariance_status
contradiction_check
claim_allowed
claim_blocked
next_gate
```

## Promotion guard

```text
No artifact in this directory can promote a claim unless the ledger state is updated and the required evidence package is complete.
```
