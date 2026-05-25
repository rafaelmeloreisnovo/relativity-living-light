# Physics Benchmarks

This directory contains benchmark layers that support RLL analysis without changing the main cosmological validation pipeline.

## Available benchmark layers

- `../RLL_BH_FLUX_NOTE.md` - black-hole mass-flux formula extension.

## Black-hole flux benchmark

Run:

```bash
python3 scripts/bh_flux_calc.py --preset sgr-a-star
python3 scripts/bh_flux_calc.py --preset m87-star-low
python3 scripts/bh_flux_calc.py --preset quasar-demo
```

With weights:

```bash
python3 scripts/bh_flux_calc.py --preset m87-star-low --c-b 1.2 --c-pol 0.8 --theta-rad 1.1 --s-kerr 1.3
```

The output is JSON and includes:

- black-hole mass in kg;
- accretion rate in kg/s;
- Schwarzschild radius approximation;
- horizon-scale area;
- mass flux per horizon area;
- microscopic unit-equivalent count rate;
- normalized growth rate;
- base and weighted RLL BH flux index.

## Guardrail

These benchmarks are diagnostic and reproducibility helpers. They do not prove RLL cosmology, do not replace general relativity, and do not replace GRMHD simulations.
