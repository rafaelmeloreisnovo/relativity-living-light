# RLL Energy-Momentum Bridge - SGP/FNext

Status: operational note, not a superiority claim.

Publication language: RLL is a candidate effective dynamic-transition cosmology under real-data evaluation.

Claim boundary: No superiority claim unless real-data metrics pass predefined thresholds.

## Core correction

Converted rest mass does not stop gravitating. Rest mass changes form into radiation, kinetic flow, heat, pressure and field-mediated redistribution. In relativistic language, the bridge is not mass disappearing, but energy-momentum changing form.

```text
E_transition = delta_m * c^2

T_eff = T_matter + T_radiation + T_thermal + T_flow + T_field
```

## Attractor transition

The "lost attractor" is represented as:

```text
A_lost = rho_before - rho_rest_after
```

It must reappear as:

```text
A_transition = rho_radiation + rho_kinetic + rho_thermal + P/c^2 + rho_field
```

The operational gap is:

```text
F_gap = A_lost - A_transition
```

If `F_gap` is near zero, the transition accounting is coherent. If not, the missing term must be measured, not invented.

## SGP

SGP means Sopro/Gradiente/Pressao:

```text
SGP = grad(P_radiation) + grad(P_thermal) + div(F_gamma)
```

Temperature and radiation are different forms of energy and must be treated as part of the effective energy-momentum budget.

## FNext

FNext is the next validation gate:

```text
FNext = delta_chi2 + delta_AIC + delta_BIC + F_gap
```

This term does not claim superiority. It only records whether the new bridge improves real-data comparison under predefined thresholds.

## Pipeline binding

The repository-level implementation is intentionally conservative:

1. real-data model comparisons provide `delta_chi2`, `delta_AIC` and `delta_BIC`;
2. transition-ledger rows provide measured density/pressure terms for `F_gap`;
3. if no transition ledger is present, `F_gap` remains `null` and `FNext.score` remains `null`;
4. missing bridge terms are reported as an observable gap, never filled by tuning or invented constants.

The current joint real-data pipeline writes this gate into `results/structure_d/joint_real_likelihood.json` under the `fnext` key.

## Operational rule

Do not claim:

- RLL proves LambdaCDM wrong
- RLL is superior
- RLL is confirmed

Allowed statement:

RLL tests whether dynamic transitions between rest mass, radiation, pressure, thermal energy, flow and fields can account for residual observable structure.
