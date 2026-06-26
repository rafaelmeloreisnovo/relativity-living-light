# fsigma8 growth sample

Path: `data/real/cosmology/fsigma8_growth.csv`

Columns:

```text
z,fsigma8,sigma,survey,reference,notes
```

This is a minimal real growth-rate sample for the RLL `chi2_fsigma8` gate. The current run uses the diagonal `sigma` column only.

Included groups:

- 6dFGS: z=0.067
- BOSS DR12 consensus: z=0.38, 0.51, 0.61
- BOSS DR11 CMASS: z=0.57
- eBOSS DR16 LRG/ELG Fourier: z=0.70, 0.845

Boundary:

- full covariance is `TOKEN_VAZIO`
- survey cross-covariances are not yet represented
- for paper-grade runs, replace or augment with official covariance blocks

Command:

```bash
python scripts/check_rll_growth.py --model all
```
