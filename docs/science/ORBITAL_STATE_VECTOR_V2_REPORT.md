# Orbital State Vector V2 Report

Status: orbital state-vector v2 generated
Claim level: `claim_allowed=false`

## Formulae

```text
h_vector = |r x v|
h_seed = sqrt(mu*a*(1-e^2))
relative_residual = (h_vector - h_seed) / h_seed
```

## First row result

| Field | Value |
|---|---:|
| h_vector_km2_s | 5476002166.230221 |
| h_seed_formula_km2_s | 5475990916.542538 |
| residual_km2_s | 11249.687683105469 |
| relative_residual | 2.0543656581169718e-06 |

## Safe conclusion

Orbital v2 computes a real vector residual from raw state vectors, but final scientific claims remain blocked.
