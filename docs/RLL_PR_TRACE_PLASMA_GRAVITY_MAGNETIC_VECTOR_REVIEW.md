# RLL PR Trace — Plasma Gravity and Magnetic Vectorization Review

## Purpose

This document follows Rafael's instruction to inspect the early repository trail instead of treating the current branch as the whole history.

Focus:

```text
plasma gravity + magnetic vectorization + photonic/logistic sector
```

The goal is to preserve the historical trail from PR #1 and PR #2, compare it with careful physics language, and identify what must be formalized next.

## PR trace checked

### PR #1 — repository restructuring and equation preservation

PR #1 was merged and did not erase the original trail. It reorganized the repository into `docs`, `data`, and `figs`, preserved files, and introduced/centralized the unified RLL equation in `README_MASTER.md`.

The PR #1 body states that the project was reorganized with zero file deletion and that notebooks/figures were preserved. It also explicitly showed the unified equation:

```text
E²(a) = Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ
      + Ω_s0[f(a) + (1-f)a⁻³]
      + Ω_B0 a⁻⁴
      + Ω_P0 a⁻⁴
```

Meaning in the PR trail:

- `Ω_s0` = photonic superposition / dark-sector transition term;
- `Ω_B0` = magnetic field term;
- `Ω_P0` = plasma term;
- `f(a)`/`f(z)` = transition/logistic gate.

PR #1 also preserved many figure paths, including expansion plots, transition plots, growth plots, posterior plots, rotation curves and cluster lensing panels.

### PR #2 — photonic/plasma/magnetic cosmology connection

PR #2 was also merged and created the photonic/nonlocality analysis package. The body of PR #2 explicitly connects:

```text
laboratory photonic nonlocality -> cosmological photonic superposition -> unified dark sector explanation
```

It repeats the same extended Friedmann expression and lists testable predictions:

- H(z) deviations;
- distance modulus residuals;
- modified fσ8 evolution;
- cluster lensing + Faraday rotation correlations;
- photonic halo profiles / SPARC rotation curves.

This confirms Rafael's point: the plasma/magnetic/photonic logic is not absent from the trail. It exists from the early PR sequence and was not deleted.

## Physics reading — what can be said carefully

### 1. Plasma does gravitate, but not magically

Literal physics:

```text
plasma has mass-energy + pressure + kinetic energy + electromagnetic field energy
```

In general relativity, the source of curvature is the stress-energy tensor. Therefore plasma contributes gravitationally through its total energy-momentum content.

Safe statement:

```text
Plasma contributes to gravity through mass-energy, pressure, flows and electromagnetic field energy.
```

Unsafe statement:

```text
Plasma alone replaces gravity or creates a separate gravitational force outside stress-energy/GR/Newtonian mass distribution.
```

### 2. Magnetism can vectorize plasma dynamics

Literal plasma/MHD physics:

```text
Lorentz force density: f = ρ_e E + J × B
```

For magnetized plasma, magnetic pressure and magnetic tension make the dynamics directional. Collapse, flow, confinement, lensing environment, current sheets and density structures can become anisotropic relative to the magnetic field.

Safe statement:

```text
Magnetic fields can vectorize/orient plasma motion and pressure anisotropy.
```

Unsafe statement:

```text
Magnetic fields vectorize gravity itself as a new fundamental force.
```

More precise RLL-compatible sentence:

```text
Magnetism vectorizes the plasma/coherence sector; the resulting anisotropic mass-energy distribution can alter gravitational potential, lensing or collapse signatures.
```

### 3. Plasma + magnetism can change lensing/propagation signatures

Papers on magnetized compact objects in plasma and plasma lensing show that plasma parameters and magnetic fields can affect observed deflection, magnification, splitting and time delay of light propagation.

Safe statement:

```text
Plasma and magnetic fields can modify electromagnetic propagation and lensing observables, and can be degenerate with gravitational lensing in some effective descriptions.
```

Unsafe statement:

```text
All gravitational lensing is plasma lensing.
```

### 4. Self-gravitating magnetized plasma has anisotropic collapse

The literature on self-gravitating magnetized plasma discusses anisotropic Jeans-like collapse: magnetic pressure can alter the critical scale and directionality of collapse.

Safe statement:

```text
Self-gravitating plasma embedded in a magnetic field can collapse anisotropically; the magnetic field affects the geometry and thresholds of instability.
```

This is close to Rafael's phrase:

```text
plasma exerce força de gravidade e pode ser vetorizado pelo magnetismo
```

but the formal version should be:

```text
plasma contributes to gravitational collapse through mass-energy; magnetism vectorizes the plasma dynamics and can make collapse/pressure/lensing anisotropic.
```

## RLL mapping

### Internal equation path

The early RLL equation already contains the three required slots:

```text
Ω_s0  -> photonic/coherence sector
Ω_B0  -> magnetic contribution/modulator
Ω_P0  -> plasma contribution/modulator
```

### Required formal split

To avoid overloading one equation, RLL should split the mechanism into layers:

1. **Background layer**
   ```text
   E²(a) = Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ + Ω_s0[f+(1-f)a⁻³] + Ω_B0 a⁻⁴ + Ω_P0 a⁻⁴
   ```

2. **Plasma-gravity layer**
   ```text
   ρ_eff = ρ_plasma + u_EM/c² + pressure/flow corrections
   ∇²Φ_eff = 4πG ρ_eff   [Newtonian/weak-field effective version]
   ```

3. **Magnetic-vector layer**
   ```text
   f_Lorentz = ρ_e E + J × B
   p_B = B²/(2 μ0)
   tension_B ~ (B·∇)B/μ0
   ```

4. **Anisotropic collapse/lensing layer**
   ```text
   magnetic pressure/tension -> anisotropic density/pressure distribution -> modified collapse/lensing/propagation signatures
   ```

5. **Claim gate**
   ```text
   if no data + no loader + no covariance + no test:
       claim_status = TOKEN_VAZIO
   ```

## What PR #1/#2 prove and do not prove

### Prove as repository history

- The plasma/magnetic/photonic terms existed from the early trail.
- The repository was reorganized without intentionally deleting that trail.
- The early equation already used `Ω_B0` and `Ω_P0`.
- The early figure set included H(z), transition, growth, lensing and rotation panels.
- PR #2 explicitly connected photonic/nonlocality concepts with plasma/magnetism, lensing/Faraday and SPARC-style tests.

### Do not prove as physics

- They do not prove RLL is correct.
- They do not prove plasma replaces gravity.
- They do not prove ordinary photons are dark matter.
- They do not prove magnetic fields create gravity as a new vector force.
- They do not replace the need for stress-energy, perturbation equations, loaders, likelihood and covariance.

## External literature alignment

### Strong adjacent support

- self-gravitating magnetized plasma can have anisotropic collapse;
- magnetic pressure/tension can set preferred directions in plasma dynamics;
- electromagnetic fields contribute to stress-energy;
- plasma and magnetic fields can affect lensing/propagation signatures;
- dark-sector MHD/dark-plasma models are active research directions.

### Boundary

These papers support the *shape* of the mechanism:

```text
mass-energy plasma + magnetic anisotropy + gravitational/lensing response
```

They do not validate the full RLL model.

## Recommended next implementation files

1. `docs/RLL_PLASMA_GRAVITY_FORMALIZATION.md`
2. `docs/RLL_MAGNETIC_VECTORIZATION_GLOSSARY.md`
3. `docs/RLL_PR1_PR2_HISTORICAL_TRACE.md`
4. `data/results/rll_pr_trace_plasma_magnetic.json`
5. `scripts/emit_rll_pr_trace_plasma_magnetic.py`

## Close

`F_ok`: PR #1 and PR #2 confirm the historical trail: plasma, magnetism, photonic superposition, figures and observables were present early.  
`F_gap`: the current rigorous pipeline has not fully formalized plasma-gravity and magnetic-vector layers.  
`F_next`: promote the historical trail into equations, glossary, data loaders, figure provenance and claim gates without overstating the physics.
