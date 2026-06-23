# RLL perturbation layer

Status: first background-coupled linear kernel is implemented.

## Implemented files

```text
src/rll/class_rll_background.c
src/rll/rll_perturbation_kernel.py
scripts/run_cmb_power_backend.py
```

## What is available now

The C background provides the exact RLL background. The Python kernel uses the same background equations to integrate the linear matter growth equation:

```text
delta_xx + [2 + dlnH/dlna] delta_x - 1.5 Omega_m(a) delta = 0
```

with `x = ln(a)`.

The backend now reports:

```text
rll_background_and_linear_kernel_available
```

## Output command

```bash
python src/rll/rll_perturbation_kernel.py
```

Outputs:

```text
results/rll_perturbation_kernel.csv
results/rll_perturbation_kernel_summary.json
```

## What this closes

```text
background_exact = available
linear_growth_kernel = available
```

## What remains open

```text
cmb_cl_exact = TOKEN_VAZIO
nonlinear_pk_exact = TOKEN_VAZIO
full_boltzmann_hierarchy = TOKEN_VAZIO
```

Reason: exact CMB Cl and exact nonlinear P(k) require a full Boltzmann and nonlinear matter module, not only a background and scale-independent growth kernel.

## Next engineering target

Wire `src/rll/class_rll_background.c` and the perturbation equations into a forked CLASS/CAMB backend so that RLL has native transfer functions, CMB Cl and P(k,z).
