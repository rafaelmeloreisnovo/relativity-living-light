# Proximo salto RLL

Objetivo: executar uma validacao real minima com baseline LCDM, adversario w0waCDM e setor logistico RLL, mantendo a fronteira entre avaliacao pontual, aproximacao por BIC e evidencia completa futura.

## Dados esperados

- `data/real/Hz_data_real.csv`
- `data/real/cosmology/desi_dr2_bao_primary_points.csv`
- `data/real/cosmology/desi_dr2_bao_covariance_summary.csv`

## Comando direto

```bash
python rll_vs_lcdm.py \
  --adversary both \
  --with-bayes \
  --with-growth \
  --bao data/real/cosmology/desi_dr2_bao_primary_points.csv \
  --bao-covariance data/real/cosmology/desi_dr2_bao_covariance_summary.csv
```

## Comando via CLI

```bash
rll run --data real --model rll --adversary w0waCDM --with-bayes --with-growth
```

## Saidas esperadas

- `results/rll_model_comparison_summary.json`
- `results/rll_model_comparison_predictions.csv`

## Leitura minima

- chi2 por modelo
- AIC
- BIC
- numero de parametros
- `delta_aic_rll_minus_w0wa`
- `delta_bic_rll_minus_w0wa`
- fator aproximado por BIC, se `--with-bayes` for usado
- status `TOKEN_VAZIO` para crescimento de estrutura, se `--with-growth` for usado

## Fronteira honesta

- `--with-bayes` usa aproximacao BIC/Schwarz, nao nested sampling.
- `--with-growth` registra o gate f_sigma8, mas ainda nao calcula crescimento real.
- MCMC e otimizacao robusta seguem como etapa posterior.
