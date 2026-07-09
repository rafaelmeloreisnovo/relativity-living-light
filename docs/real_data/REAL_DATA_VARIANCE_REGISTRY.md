# Real Data Variance Registry

## Status

`documentation_only / structural_check / claim_boundary`

## Purpose

This document records the minimal real-data variance registries added under:

```text
data/real/cosmology/variance_policy_registry_minimal.csv
data/real/cosmology/dataset_routes_minimal.csv
```

The registries connect already committed real-data routes to explicit uncertainty or covariance policies.

## Validator

The structural validator is:

```text
tools/validate_real_dataset_variance_registry.py
```

It checks that the minimal registries exist, are non-empty, contain required columns, and that route policies are represented in the variance registry.

## Claim boundary

This registry and validator do not validate RLL, do not compare models, and do not promote any result.

They only make the data/variance layer easier to audit before model-comparison or likelihood steps.

## Current registered routes

| Route | Axis | Policy |
|---|---|---|
| `hz` | expansion | diagonal |
| `bao` | BAO | covariance summary |
| `growth` | growth | diagonal |
| `cmb` | CMB shift | compressed |

## Next coherent step

Wire the validator into a lightweight CI check after confirming it passes in the repository environment.
