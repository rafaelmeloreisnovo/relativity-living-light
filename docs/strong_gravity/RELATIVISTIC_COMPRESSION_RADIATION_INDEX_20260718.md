# Relativistic compression and radiation integration index — 2026-07-18

## Authority

`instituto-Rafael/relativity-living-light`

## Integrated artifacts

```text
data/pipelines/strong_gravity/relativistic_compression_radiation_bridge.py
data/contracts/relativistic_compression_radiation_bridge.v1.json
data/results/strong_gravity/relativistic_compression_radiation_baseline.json
tests/strong_gravity/test_relativistic_compression_radiation_bridge.py
docs/strong_gravity/RELATIVISTIC_COMPRESSION_RADIATION_BRIDGE.md
data/formulas/FORMULAS_ARTIFACTS_MANIFEST.json
```

## Physics separation

```text
compression work             = -p Theta
magnetic pressure            = B^2/(2 mu0)
radiation pressure           = coupling * flux/c
photon thrust                = coupling * power/c
radiative acceleration       = opacity * flux/c
gravity acceleration         = GM/r^2
Eddington benchmark          = 4 pi GMc/opacity
electron degeneracy pressure = non-relativistic reference only
```

## Semantic corrections

- microscopic collision means scattering/interaction, not literal hard-sphere contact;
- Pauli exclusion concerns quantum-state occupation, not a universal geometric no-overlap statement;
- compression does not automatically create subparticles;
- a reached energy reference does not prove a reaction occurred;
- electron spin does not automatically create a macroscopic magnetic field;
- field lines are representations of the electromagnetic field, not material strings;
- electromagnetic and radiation energy contribute to stress-energy, but the scalar proxy is not an Einstein-equation solution;
- photon momentum can oppose inflow or help drive an outflow.

## Validation boundary

```text
local focused tests          = 15 PASS (pre-commit execution)
GRMHD solution               = false
quantum kinetic solution     = false
spin hydrodynamics solution  = false
Einstein backreaction        = false
nuclear network              = false
laboratory validation        = false
astrophysical validation     = false
RLL cosmology validation     = false
claim_allowed                = false
```

No new workflow YAML was introduced.
