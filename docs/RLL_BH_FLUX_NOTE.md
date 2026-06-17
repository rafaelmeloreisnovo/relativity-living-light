# RLL BH Flux Note

Status: benchmark and formula-extension note. This is not a cosmological proof and does not replace GR, Kerr geometry, GRMHD, or observational fitting.

## 1. What changes in RLL

This note adds an explicit black-hole mass-flux layer to the total RLL structure.

Previous compact form:

```text
RLL ~= field -> coherence -> observable
```

Expanded form:

```text
RLL_total = RLL_cosmo + RLL_field + RLL_BH_flux
```

The new layer is:

```text
RLL_BH_flux = f(M_bh, Mdot, A_H, spin, magnetic_field, polarization, radiation)
```

The main correction is that black-hole impact is not modeled from the mass of a single microscopic unit. It is modeled from total mass flow.

```text
Mdot = dM/dt
```

## 2. Core measurable quantities

```text
M_kg = M_bh_solar * M_sun
Mdot_kg_s = Mdot_solar_year * M_sun / year_seconds
r_s = 2 * G * M_kg / c^2
A_H = 4 * pi * r_s^2
Phi_M = Mdot_kg_s / A_H
Ndot = Mdot_kg_s / m_unit
growth_s = Mdot_kg_s / M_kg
```

Where:

- M_bh is black-hole mass.
- Mdot is accretion mass-flow rate.
- A_H is the horizon-scale area approximation.
- Phi_M is horizon-normalized mass flux.
- m_unit is a chosen microscopic reference mass.
- Ndot is the unit-equivalent count rate.

## 3. Diagnostic index

A conservative scalar diagnostic can be written as:

```text
I_RLL_BH = log10(1 + Ndot) * log10(1 + Phi_M) * C_B * C_pol * Theta_rad * S_Kerr
```

Where:

- C_B is magnetic-field coherence or strength normalization.
- C_pol is polarization coherence or ordered-polarization fraction.
- Theta_rad is radiative coupling or luminosity normalization.
- S_Kerr is a spin/horizon correction placeholder.

This index is not a physical law. It is a diagnostic wrapper that organizes measured and inferred quantities into one reproducible benchmark.

## 4. Difference from current models

Current black-hole modeling normally uses GR/Kerr geometry, GRMHD simulations, radiative transfer, and direct or indirect observables such as images, polarization, spectra, luminosity, variability, and jets.

RLL_BH_flux does not replace these models. It differs by adding a transverse bookkeeping layer:

```text
mass flow -> horizon flux -> microscopic-equivalent count -> field/polarization/radiation weights
```

So the differential claim is modest but useful:

```text
RLL adds a reproducible mass-flow diagnostic that can compare Sgr A*, M87*, and quasar-scale systems with the same output schema.
```

## 5. Relation to the Rydberg butterfly reference

The Rydberg butterfly molecule is not a direct black-hole driver. It can only be used as one possible microscopic mass unit.

```text
m_butterfly ~= 3e-25 kg
Ndot_butterfly_equivalent = Mdot_BH / m_butterfly
```

Correct framing:

```text
not: one molecule changes a black hole
yes: measured accretion flow can be expressed as microscopic unit-equivalent count rate
```

## 6. Safe statement for academic use

RLL includes a black-hole mass-flux benchmark that converts accretion rates into kg/s, horizon-normalized flux, normalized growth rate, and microscopic unit-equivalent count rate, optionally weighted by magnetic-field, polarization, radiation, and spin factors.

This supports benchmark comparison, not proof of a new cosmology.

## 7. Bibliography

- Event Horizon Telescope Collaboration. First M87 Event Horizon Telescope Results. VII. Polarization of the Ring. Astrophysical Journal Letters, 2021.
- Event Horizon Telescope Collaboration. First M87 Event Horizon Telescope Results. VIII. Magnetic Field Structure near The Event Horizon. Astrophysical Journal Letters, 2021.
- Event Horizon Telescope Collaboration. First Sagittarius A* Event Horizon Telescope Results. V. Testing Astrophysical Models of the Galactic Center Black Hole. Astrophysical Journal Letters, 2024.
- Event Horizon Telescope Collaboration. First Sagittarius A* Event Horizon Telescope Results. VII. Polarization of the Ring. Astrophysical Journal Letters, 2024.
- Shakura, N. I. and Sunyaev, R. A. Black holes in binary systems. Observational appearance. Astronomy and Astrophysics, 1973.
- Novikov, I. D. and Thorne, K. S. Astrophysics of black holes. In Black Holes, Les Houches, 1973.
- Bardeen, J. M., Press, W. H., and Teukolsky, S. A. Rotating black holes: locally nonrotating frames, energy extraction, and scalar synchrotron radiation. Astrophysical Journal, 1972.
- Blandford, R. D. and Znajek, R. L. Electromagnetic extraction of energy from Kerr black holes. Monthly Notices of the Royal Astronomical Society, 1977.
- Narayan, R. and Yi, I. Advection-dominated accretion: a self-similar solution. Astrophysical Journal Letters, 1994.
- Abramowicz, M. A. and Fragile, P. C. Foundations of black hole accretion disk theory. Living Reviews in Relativity, 2013.

## 8. Claim boundary

Allowed:

```text
RLL_BH_flux is a benchmark layer for mass-flow diagnostics around black holes.
```

Not allowed:

```text
RLL_BH_flux proves RLL cosmology.
RLL_BH_flux replaces GR or GRMHD.
A Rydberg molecule directly changes black-hole dynamics.
```
