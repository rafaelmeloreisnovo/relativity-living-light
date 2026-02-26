# Resultados – Relativity Living Light

## Referência principal (posterior unificado sintético)

Parâmetros derivados de `data/posterior_unified_synth.csv` usando estatística **ponderada** pela coluna `weight`.

| Parâmetro | Média ponderada | Desvio padrão ponderado | Mediana ponderada | Intervalo 16%–84% |
|---|---:|---:|---:|---:|
| Ω_s0 | 0.0592 | 0.0113 | 0.0589 | [0.0481, 0.0707] |
| z_t | 1.1478 | 0.2915 | 1.1642 | [0.8824, 1.4300] |
| w_t | 0.3999 | 0.1180 | 0.4048 | [0.2710, 0.5337] |

### Diagnóstico de amostragem (posterior)

- N total de amostras: `25000`
- N efetivo (`N_eff = 1/Σw²`): `2320.75`

## Bloco legacy/exploratório

> **Legacy / exploratório (não usar como referência principal):**
>
> - z_t ≈ 0.68 ± 0.05  
> - w_t ≈ 0.20 ± 0.04

## Fonte dos números

- Arquivo-fonte: `data/posterior_unified_synth.csv`
- Commit (última atualização do arquivo): `8d49cba562a5b2b8a993de0e94d0b8b057e539fb`
- Data do commit: `Sun Oct 19 15:21:22 2025 +0000`
- Geração desta tabela: estatísticas calculadas diretamente do CSV local nesta revisão.

## Política de artefatos e regeneração de gráficos

- Este documento e os arquivos em `results/*.csv` e `results/*.json` são a fonte canônica do core versionado.
- Gráficos e infográficos devem ser gerados localmente a partir dos dados textuais e publicados como artefatos externos (release/DOI), sem versionar binários no núcleo.

Comandos de referência para regeneração fora do core:

```bash
python data/pipelines/structure_d/run_all.py
python docs/rll_validation_real.py
python docs/crescimento_estrutural.py
```

