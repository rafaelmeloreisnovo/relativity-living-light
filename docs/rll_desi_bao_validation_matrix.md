# RLL × DESI BAO Validation Matrix

## Objective
Define a reproducible path for comparing RLL candidates against ΛCDM and w0waCDM on DESI-centered expansion constraints.

## Models
- **RLL_0**: ΛCDM limit.
- **RLL_1**: transition-only sector \((\Omega_{s0}, z_t, w_t)\).
- **RLL_2**: transition + radiative effective terms \((\Omega_{B0},\Omega_{P0})\).

## BAO observables
- \(D_M(z)/r_d\)
- \(D_H(z)/r_d = c/(H(z)r_d)\)
- \(D_V(z)/r_d\)

## Statistical block
\[
\chi^2_{BAO}=(\vec{D}_{obs}-\vec{D}_{model})^T C^{-1}(\vec{D}_{obs}-\vec{D}_{model})
\]
\[
AIC=2K+\chi^2,\quad BIC=K\ln N+\chi^2.
\]

## Decision protocol
- Do not claim preference from Δχ² alone.
- Evaluate ΔAIC and ΔBIC jointly.
- Require no major degradation relative to CMB-based priors.

## Data pointers
- Config schema: [`data/real/cosmology/DESI_BAO_MATH_ARTIFACTS.yml`](../data/real/cosmology/DESI_BAO_MATH_ARTIFACTS.yml)
- Source catalog: [`data/observational_sources.yml`](../data/observational_sources.yml)
