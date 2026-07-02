# RAFAELIA Symbol Table

## Status

`symbol_table / mathematical_operational_core / claim_boundary`

## Purpose

This document defines the minimal symbol table for the RAFAELIA formal core.

It reduces ambiguity before implementation, simulation or scientific interpretation.

## Claim boundary

```text
claim_allowed=false
symbol_table=true
scientific_validation=false
physics_claim=false
neuroscience_claim=false
quantum_hardware_claim=false
```

This table does not validate RAFAELIA as physics, neuroscience, consciousness theory, cosmology or hardware. It only clarifies symbols, roles, domains and proof obligations for future implementation.

## Canonical source

```text
data/formulas/RAFAELIA_FORMAL_UNIFIED_CORE.md
```

## Symbols

| Symbol | Role | Suggested domain | Layer | Notes |
|---|---|---|---|---|
| `i` | node index | integer node id | graph | Identifies a site in the lattice/graph. |
| `j` | neighbor index | integer node id | graph | Used inside neighborhood sums. |
| `t` | discrete time index | integer `t >= 0` | dynamics | Simulation step, not continuous time unless separately derived. |
| `T_i(t)` | local state | real finite scalar | state | May be signed unless later constrained. Entropy uses `abs(T_i)` for safety. |
| `Delta T_i` | state increment | real finite scalar | dynamics | Update contribution at node `i`. |
| `N(i)` | neighborhood | set/list of node ids | graph | Hexagonal interpretation expects six neighbors when fully populated. |
| `C_ij` | anti-loop/path cutter | `{0, 1}` | structure | `0` blocks an edge relation; `1` allows it. |
| `F_i` | local flow | real finite scalar | dynamics | Sum of neighbor differences with path cutter. |
| `D_i` | adaptive diffusivity/viscosity | real finite scalar | dynamics/control | Can become negative only under declared anti-diffusive regime. |
| `D_0` | base diffusivity | real scalar, usually nonnegative | control | Global feedback may update it. |
| `D_neg` | negative-regime coefficient | real scalar `< 0` | critical regime | Must be negative and dominant enough to permit `D_i < 0`. |
| `P_i` | plasticity state | real finite scalar | adaptive | Hebb-like memory/plasticity variable. |
| `eta` | plasticity gain | real scalar | adaptive | Should be bounded before simulation. |
| `lambda` | plasticity decay | real scalar, usually `>= 0` | adaptive | Decay term; avoid conflict with programming language keyword as `lambda_decay`. |
| `L_i` | discrete logarithmic derivative proxy | real finite scalar | adaptive | Requires epsilon guard. |
| `epsilon` | numerical guard | positive real | numerical safety | Prevents division/log zero failures. |
| `I_i` | integral memory | real finite scalar | control | Accumulates deviation from base state. |
| `T_base` | base/reference state | real scalar | control | Used by integral memory. |
| `T_target` | target state | real scalar | control | Used by error term. |
| `e_i` | control error | real finite scalar | control | `T_i - T_target`. |
| `Theta_i` | adaptive threshold/control | real finite scalar | control | Must not be confused with phase. |
| `Theta_0` | base threshold | real scalar | control | Baseline threshold. |
| `K_p` | proportional gain | real scalar | control | PID-like reduced term. |
| `K_i` | integral gain | real scalar | control | PID-like reduced term. |
| `phi_i` | internal spiral phase | real scalar modulo convention pending | structure | Must not be confused with threshold/control. |
| `omega` | phase gain/frequency | real scalar | structure | Controls phase update speed. |
| `M_i` | synaptic/adaptive modulation | `[-1, 1]` by tanh | adaptive | Modulates diffusivity update. |
| `w_0..w_3` | modulation weights | real scalars | adaptive | Need ranges before simulation. |
| `A_i` | anti-diffusion increment | nonnegative real when active | critical regime | `alpha * abs(F_i) * indicator(D_i < 0)`. |
| `alpha` | anti-diffusion gain | real scalar, usually `>= 0` | critical regime | Needs stability bounds. |
| `p_i` | entropy weight | `[0, 1]` | global feedback | Use `abs(T_i)/(sum(abs(T))+epsilon)`. |
| `S_H` | global entropy | nonnegative real | global feedback | Avoid using `H` to prevent collision with Heaviside. |
| `calH(x)` | Heaviside step | `{0, 1}` | control | Use `calH` or `Heaviside`, not `H`, to avoid entropy collision. |
| `1_{D_i<0}` | indicator | `{0, 1}` | critical regime | Activates anti-diffusion term. |

## Symbol collisions resolved

```text
Theta_i = adaptive threshold/control
phi_i = internal spiral phase
S_H = entropy
calH = Heaviside step
lambda_decay = implementation-safe name for lambda
```

## Implementation constraints

```text
1. All states must remain finite.
2. epsilon must be positive.
3. graph edges must reference existing nodes.
4. D_neg must be explicitly negative.
5. entropy must use safe normalization if T_i can be signed.
6. anti-diffusion must be declared as critical/unstable regime, not hidden inside diffusion.
7. no simulation result can promote physics/neuroscience/cosmology claims without baseline, metric, uncertainty and contradiction check.
```

## Minimum implementation gates

```text
1. Parse symbol table.
2. Implement toy graph/lattice update.
3. Add finite-output tests.
4. Add edge/reference validation.
5. Add parameter bounds.
6. Add baseline pure-diffusion comparison.
7. Add synthetic-only boundary.
8. Record seed, config, output, checksum and claim boundary.
```

## Allowed statement

```text
RAFAELIA has a clarified mathematical-operational symbol table suitable for implementation and testing.
```

## Blocked statements

```text
RAFAELIA is validated physics.
RAFAELIA proves neuroscience or consciousness.
RAFAELIA proves quantum hardware.
RAFAELIA has passed stability analysis.
RAFAELIA has external experimental validation.
```
