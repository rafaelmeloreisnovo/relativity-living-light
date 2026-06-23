# RLL perturbation layer

Status: background-coupled linear kernel plus transfer bridge contract.

## Implemented files

```text
src/rll/class_rll_background.c
src/rll/rll_perturbation_kernel.py
src/rll/rll_transfer_bridge_contract.json
scripts/run_cmb_power_backend.py
```

## What is available now

The C background provides the exact RLL background. The Python kernel uses the same background equations to integrate the linear matter growth equation:

```text
delta_xx + [2 + dlnH/dlna] delta_x - 1.5 Omega_m(a) delta = 0
```

with `x = ln(a)`.

The transfer contract defines the bridge outputs:

```text
z
k_hmpc
D_z
T_k_z
P_linear_bridge
```

The backend now reports:

```text
rll_background_kernel_transfer_contract_available
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

The transfer bridge contract is:

```text
src/rll/rll_transfer_bridge_contract.json
```

## What this closes

```text
background_exact = available
linear_growth_kernel = available
transfer_bridge_contract = available
```

## What remains open

```text
cmb_cl_exact = TOKEN_VAZIO
nonlinear_pk_exact = TOKEN_VAZIO
full_boltzmann_hierarchy = TOKEN_VAZIO
```

Reason: exact CMB Cl and exact nonlinear P(k) require a full Boltzmann and nonlinear matter module, not only a background, scale-independent growth kernel and transfer contract.

## Next engineering target

Replace the contract placeholder with native CLASS/CAMB transfer functions so that RLL has backend-generated transfer tables, CMB Cl and P(k,z).
