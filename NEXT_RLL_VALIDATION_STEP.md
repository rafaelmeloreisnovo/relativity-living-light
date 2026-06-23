# Proximo salto RLL

Objetivo: executar uma validacao real minima com baseline LCDM, adversario w0waCDM, setor logistico RLL e gate linear de crescimento `f_sigma8`, mantendo a fronteira entre avaliacao pontual, aproximacao por BIC e evidencia completa futura.

## Dados esperados

- `data/real/Hz_data_real.csv`
- `data/real/cosmology/desi_dr2_bao_primary_points.csv`
- `data/real/cosmology/desi_dr2_bao_covariance_summary.csv`
- opcional: `data/real/cosmology/fsigma8_growth.csv`

## Comando direto - fundo Hz+BAO

```bash
python rll_vs_lcdm.py \
  --adversary both \
  --with-bayes \
  --with-growth \
  --bao data/real/cosmology/desi_dr2_bao_primary_points.csv \
  --bao-covariance data/real/cosmology/desi_dr2_bao_covariance_summary.csv
```

## Comando direto - crescimento linear f_sigma8

```bash
python scripts/check_rll_growth.py --model all
```

Com dados reais de crescimento:

```bash
python scripts/check_rll_growth.py \
  --model all \
  --data data/real/cosmology/fsigma8_growth.csv
```

## Comando via CLI

```bash
rll run --data real --model rll --adversary w0waCDM --with-bayes --with-growth
```

## Saidas esperadas

- `results/rll_model_comparison_summary.json`
- `results/rll_model_comparison_predictions.csv`
- `results/rll_growth_fsigma8_summary.json`
- `results/rll_growth_fsigma8_predictions.csv`

## Leitura minima

- chi2 por modelo
- AIC
- BIC
- numero de parametros
- `delta_aic_rll_minus_w0wa`
- `delta_bic_rll_minus_w0wa`
- fator aproximado por BIC, se `--with-bayes` for usado
- `D(z)`, `f_growth(z)` e `f_sigma8(z)` pelo solver linear
- `chi2_fsigma8` quando o CSV real de crescimento for informado

## Fronteira honesta

- `--with-bayes` usa aproximacao BIC/Schwarz, nao nested sampling.
- `scripts/check_rll_growth.py` calcula crescimento linear em fundo GR suave, nao Boltzmann/CMB completo.
- nonlinear power spectrum, Halofit, baryonic feedback e covariancia completa de surveys permanecem `TOKEN_VAZIO`.
- MCMC e otimizacao robusta seguem como etapa posterior.
