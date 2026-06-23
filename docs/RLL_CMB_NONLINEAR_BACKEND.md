# RLL CMB and nonlinear matter backend

Status: adapter plus exact RLL background source.

## Implemented now

The exact RLL background source is present at:

`src/rll/class_rll_background.c`

It provides:

- `f(z)`
- `rho_factor`
- `E2`
- `H_over_H0`
- `w_eff`
- `Omega_m_a`
- `Omega_s_a`
- `dlnH_dlna`

The backend adapter `scripts/run_cmb_power_backend.py` now reports:

`rll_exact_background_available`

for `--model rll`.

## What this means

The RLL background is no longer an empty placeholder. It is implemented as a C source that can be wired into a CLASS or CAMB custom background layer.

## Still open

- exact perturbation equations
- exact CMB Cl for RLL
- exact nonlinear P(k) for RLL
- full CMB likelihood layer

These remain `TOKEN_VAZIO` until the perturbation and likelihood layer is added.

## Existing backend route

For `lcdm` and `w0wa`, the adapter continues to delegate to CAMB or CLASS/classy when those packages are installed.
