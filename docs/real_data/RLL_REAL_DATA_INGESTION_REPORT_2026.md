# RLL Real Data Ingestion Report — 2026

## Coerência × Amor × Prova
Este relatório materializa a primeira camada de dados reais auditáveis do RLL sem converter hipótese em conclusão.

- Manifesto: `data/real/rll_real_sources_manifest_2026.yml`
- CSV normalizado: `data/real/cosmology_observational_seed_2026.csv`
- Proveniência planejada: `data/real/cosmology_observational_seed_2026.provenance.json`
- Claim boundary: `No superiority claim unless real-data metrics pass predefined thresholds.`

## Saídas atuais
- Linhas totais no CSV: 4
- Pontos observacionais H(z): 3
- Fontes-resumo aguardando tabela/covariância: 1

## Pontos observacionais materializados

| source_id | z | observável | valor | erro - | erro + | unidade | referência |
|---|---:|---|---:|---:|---:|---|---|
| cc_borghi_2021_lega_c | 0.75 | H(z) | 98.8 | 33.6 | 33.6 | km/s/Mpc | arXiv:2110.04304 |
| cc_jiao_2022_lega_c_full_spectrum | 0.80 | H(z) | 113.1 | 19.188 | 32.773 | km/s/Mpc | arXiv:2205.05701 |
| cc_tomasetti_2025_clusters | 0.542 | H(z) | 66.0 | 31.780 | 82.037 | km/s/Mpc | arXiv:2512.02109 |

## Lacunas preservadas como dado
- DESI DR2 BAO foi registrado como fonte real, mas ainda exige tabela oficial de distâncias BAO e covariância antes de qualquer chi2.
- Pantheon+SH0ES foi registrado como entrada esperada do runner real, mas arquivos grandes oficiais devem ser materializados localmente em `data/pantheon/`.
- Planck 2018 foi preservado como referência/prior, não como dado bruto ingerido.

## Próximo passo executável
Rodar:

```bash
python scripts/ingest_real_cosmology_sources.py --check
```

Depois materializar Pantheon+ e executar:

```bash
python scripts/run_real_pantheon_validation.py
```
