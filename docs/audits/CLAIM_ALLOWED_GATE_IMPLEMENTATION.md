# Claim Allowed Gate Implementation

## Status

`audit_note / p0_gate_added / claim_boundary`

## Scope

This note records the implementation of a repository-level structural guard for `claim_allowed=true` entries in machine-readable artifacts.

## Implemented files

```text
tools/validate_claim_allowed_gate.py
tests/test_claim_allowed_gate.py
```

## What the gate checks

The validator scans JSON/YAML artifacts under:

```text
data/
results/
docs/yml/
schemas/
```

If a parsed mapping contains `claim_allowed: true`, the mapping must also contain non-empty evidence groups for:

```text
source
checksum
metric
baseline
uncertainty/error/covariance
execution/reproducibility command
claim boundary/falsifier
```

## Claim boundary

This gate does not validate RLL, execute cosmology, prove mathematics, select a model, determine market value or create legal/institutional acceptance.

It only blocks silent promotion of machine-readable claims without minimum evidence metadata.

## Why this matters

The P0 gap was:

```text
claim_allowed gate
```

The implemented gate converts that gap into an executable structural check. It does not close scientific validation; it prevents unsupported promotion.

## Still pending

```text
CI workflow connection may still be added or adjusted separately.
Scientific routes still require materialized data, checksums, baselines, metrics, uncertainty models and executed falsifiers.
```
