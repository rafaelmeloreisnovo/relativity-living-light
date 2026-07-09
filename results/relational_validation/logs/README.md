# Relational Validation Logs

## Status

`logs_root / relational_validation / append_only_preferred`

## Purpose

This directory stores logs linked to relational-validation packages.

A log is acceptable only when it can be linked to:

```text
claim_id
relation_graph_id
command or workflow
input/source paths
artifact output paths
metric names
baseline/adversary
claim boundary
```

## Rule

```text
Logs record execution context.
Logs do not prove claims by themselves.
Logs become useful when they converge with artifacts, metrics, baselines and contradiction checks.
```

## Naming convention

```text
YYYYMMDDTHHMMSSZ_<claim_id>_<relation_graph_id>.log
```

If the exact time is unavailable, use:

```text
TOKEN_VAZIO_TIME_<claim_id>_<relation_graph_id>.log
```

## Minimal log header

```text
claim_id:
relation_graph_id:
command_or_workflow:
source_paths:
artifact_paths:
metric_names:
baseline_or_adversary:
claim_allowed:false
claim_boundary:
```
