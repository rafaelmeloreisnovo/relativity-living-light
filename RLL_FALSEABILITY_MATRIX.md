# RLL Falseability Matrix (RLL × GR/ΛCDM)

> Status: **test program**, not proof claim.

## Core falsifiable residual

\[
\epsilon_{RLL}(\mathcal{O}, z, t) = \mathcal{O}_{obs}(z,t) - \mathcal{O}_{GR+\Lambda CDM}(z,t)
\]

Where \(\mathcal{O}\in\{H(z), D_L(z), \mu(z), f\sigma_8(z), C_\ell^{lens}, h(f)\}\).

The RLL hypothesis is only physically meaningful when it predicts **sign, amplitude, scale, and uncertainty** for \(\epsilon_{RLL}\).

## External data baselines (public)

- DESI BAO DR2 / collaboration releases (BAO distances and expansion constraints).
- Planck 2018 legacy CMB parameters.
- Pantheon+ SN Ia distance moduli.
- JWST/COSMOS-Web lensing and large-scale structure mapping products.
- LIGO/Virgo/KAGRA GW strain catalogs.
- QGEM literature for laboratory entanglement-by-gravity protocols.

## Matrix

| Vector | Observable(s) | Public baseline | RLL required prediction | Falsification condition |
|---|---|---|---|---|
| Precision expansion | \(H(z)\) | DESI BAO + cosmic chronometers | \(H_{RLL}(z)\) with posterior | Worse fit than ΛCDM after AIC/BIC penalty |
| Luminosity distance | \(D_L(z), \mu(z)\) | Pantheon+ | Residual law \(\Delta\mu_{RLL}(z)\) | \(\chi^2\) degradation without complexity gain |
| Dynamic DE | \(w(z)\) | DESI+Planck+SNe combined constraints | \(w_{RLL}(z)\) mapped to effective EOS | Excluded credible intervals |
| CMB anchor | \(\Omega_m, H_0, r_s\)-linked projections | Planck 2018 | Consistent projected parameter region | Breaks CMB consistency envelope |
| Growth | \(f\sigma_8(z)\) | RSD (DESI/eBOSS/Euclid path) | Growth curve under same priors | Incompatible structure growth trend |
| Weak lensing | \(\gamma(\theta),\kappa(\theta), C_\ell^{lens}\) | COSMOS-Web, DES, HSC, Euclid | Shear/convergence residual pattern | No coherent non-GR residual after errors |
| Wandering BH lensing | \(\theta_{obs}(t)\) astrometric residual | HST/Gaia/JWST follow-up streams | Temporal residual \(\epsilon^{lens}_{RLL}(t)\) | GR moving-lens model fully explains signal |
| Gravitational waves | \(h(f)\) | LIGO/Virgo/KAGRA catalogs | Phase/amplitude/dispersion signature | Predicted signature absent |
| Quantum gravity lab | Entanglement witness | QGEM protocol literature | Directional effect on entanglement | Experimental outcome contradicts forecast |

## Implementation bridge in this repo

- Programmatic comparator: `rll_vs_lcdm.py`
- Outputs (default): `results/rll_vs_lcdm_summary.json`, `results/rll_vs_lcdm_predictions.csv`
- Initial local inputs:
  - `data/real/Hz_data_real.csv`
  - `data/real/BAO_data_real.csv`

## Method discipline

1. Keep GR/ΛCDM as null model.
2. Fit RLL extension with explicit extra parameters.
3. Compare using fair complexity penalty (AIC/BIC).
4. Publish residuals and error bars, not narrative claims.

