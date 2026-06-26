# RAFAELIA Falsification Gate

This document defines a claim-control method for converting symbolic intuition into testable documentation.

```text
SIM -> HIP -> MAT -> COD -> EXP -> ETH
```

## Layers

- SIM: metaphor, myth, fable, symbolic image.
- HIP: explicit hypothesis.
- MAT: mathematical relation or model.
- COD: executable code, deterministic artifact, checksum, CI output, or reproducible pipeline.
- EXP: empirical or documentary validation.
- ETH: claim boundary and consequence.

## Core rule

```text
Intuition points.
Falsification cleans.
Experiment decides.
```

Use these tags consistently:

```text
[COD] measured or established
[HIP] possible but not proven
[SIM] symbolic layer
[GAP] missing evidence
[TOKEN_VAZIO] protected absence; do not invent
```

## False-positive controls

Check explicitly:

```text
correlation != causation
repetition != root cause
symbolic similarity != physical identity
mathematical possibility != physical realization
AI coherence != proof
anomaly != theory
```

## Hidden-variable policy

For simple reference systems, temperature and pressure may be enough. For complex plasma/cosmology systems, document additional variables:

```text
T, P, density, B-vector, E-vector, current, ionization, geometry, metric, radiation, covariance, boundary conditions
```

Recommended terms:

```text
MHD = magnetohydrodynamics
GRMHD = general relativistic magnetohydrodynamics
self-gravitating plasma
plasma in gravitational field
```

## Basal-buffer principle

A stable model is not only basal. It needs buffer and return.

```text
coherence = basal range + buffer capacity + return path
```

For RLL this means checking not only best fit, but also:

```text
seed variation
prior variation
dataset ablation
parameter freeze/unfreeze
covariance perturbation
optimizer maxiter increase
```

## RLL claim gate

Allowed when only a pipeline exists:

```text
RLL is implemented as a testable model.
RLL was compared under dataset X and criteria Y.
Current run shows result Z.
```

Not allowed without evidence:

```text
RLL is confirmed.
RLL universally beats LCDM/CPL.
RLL proves new physics.
```

Required outputs:

```text
chi2
AIC/AICc
BIC
dataset description
covariance handling
parameter bounds
seeds
maxiter
failure modes
```

## Counterexample search

Every strong claim must ask:

```text
What would make this false?
What null model explains the same result cheaper?
What dataset breaks the claim?
Does the model collapse to a simpler model?
```

## AI boundary

AI can organize, calculate, review, generate counterexamples, and document. AI must not be treated as oracle, proof source, citation substitute, or experiment.

## One-line doctrine

```text
A beautiful pattern becomes science only after it survives a hostile documented test.
```
