# Apêndice 03 — Resultado estatístico e gate MCMC RLL

Status: **FALSEAMENTO OPERACIONAL NESTA RODADA**.

## RAW_TEXT_FIRST / Token Vazio

Este documento registra primeiro o resultado bruto executável. Não inventa chains, best-fits ou corner plots. Onde o pedido exigia MCMC completo com DESI DR2, Pantheon+ e Planck, mas o repositório materializa apenas um subconjunto operacional leve para o gate atual, o item fica marcado como `[VAZIO]` até a ingestão completa dos catálogos e covariâncias oficiais.

## Comando executado

```bash
python scripts/compute_rll_real_pipeline.py --output-dir artifacts/rll-real-run-20260701 --data-source repo
```

## Dados usados pelo gate executável

- `data/real/Hz_data_real.csv`: 33 pontos H(z), SHA256 `1194fe2066dc3d92b4870cfb03d2cdbe2a316deae2e1355943f7f2ccca6d52b6`.
- `data/real/BAO_data_real.csv`: 10 pontos BAO, SHA256 `1decb159dd8c276e356e1f2ca45028da0079302a0b7b279797d8e40aab0c9527`.
- `data/real/CMB_shift_real.json`: referência Planck2018, SHA256 `f658dafa16b57a4522bdf59c243d8693e20efe9936e2815720fed7ed6d637cdc`.

## Tabela de comparação

| Modelo | χ² | N real | k | AIC | BIC |
|---|---:|---:|---:|---:|---:|
| ΛCDM | 216.5765289143 | 43 | 2 | 220.5765289143 | 224.0989291457 |
| RLL | 238.4928708818 | 43 | 5 | 248.4928708818 | 257.2988714603 |

Deltas com a convenção pedida, `RLL - ΛCDM`:

- Δχ² = `+21.9163419675`.
- ΔAIC = `+27.9163419675`.
- ΔBIC = `+33.1999423146`.

## Veredito

Como ΔAIC e ΔBIC são positivos, o RLL **não vence** o baseline neste gate. Pela regra de execução definida para esta auditoria, as Tarefas 1, 2 e a promoção MCMC completa ficam bloqueadas. O estado honesto é:

> RLL reprovado no gate estatístico operacional de 2026-07-01; não promover para submissão PRD/JCAP como modelo favorecido até novo ajuste com catálogos completos, covariâncias oficiais e baseline w0waCDM/CPL reproduzível.

## Itens explicitamente não materializados

- `[VAZIO]` Chains Cobaya/MontePython completas em `data/outputs/mcmc_rll/`.
- `[VAZIO]` Corner plot de posterior real.
- `[VAZIO]` Best-fits 1σ/3σ para `α, k, a_t, Ω_m, H0` derivados de MCMC completo.
- `[VAZIO]` Comparação final contra w0waCDM/CPL com a mesma likelihood multissonda.

## Próxima ação falsificável

1. Materializar DESI DR2 BAO com covariância oficial completa, Pantheon+ com matriz estatística+sistemática e priors/likelihood Planck.
2. Rodar Cobaya/MontePython com os mesmos nuisance parameters para RLL e w0waCDM.
3. Publicar também o resultado negativo se os deltas permanecerem positivos.
