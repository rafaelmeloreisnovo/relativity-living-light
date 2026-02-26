# Índice Canônico de Artefatos Textuais (`results/`)

Este arquivo é a referência canônica dos artefatos textuais em `results/`.

| caminho | formato | descrição | colunas/schema | script gerador | comando de reprodução | data/versão |
|---|---|---|---|---|---|---|
| `results/RLL_chi2_results.csv` | csv | Tabela histórica de métricas χ² para comparações RLL em trilhas legadas/versionadas. | `model,chi2,AIC,BIC` (estrutura tabular de métricas por modelo). | `news/archive_legacy/1/*` (origem histórica; sem script único versionado neste caminho). | Não canônico (artefato legado já versionado). | `legacy` |
| `results/two_radiation_model_preview.csv` | csv | Prévia tabular do modelo de duas radiações para inspeção rápida de parâmetros/resultados. | Estrutura tabular CSV (colunas definidas no próprio arquivo). | Fluxo documental/técnico de duas radiações (sem script único dedicado em `data/pipelines/structure_d/`). | Não canônico (artefato versionado para referência). | `preview` |
| `results/structure_d/model_comparison.csv` | csv | Comparação entre modelos (ex.: LCDM vs RLL_like+AGN) com χ²/AIC/BIC e metadados da corrida. | `model,chi2,AIC,BIC,N,k,fit_params,fixed_params,datasets_used,run_name` | `data/pipelines/structure_d/run_all.py` | `python -m data.pipelines.structure_d.run_all` | `run_name` em `data/pipelines/structure_d/datasets_config.json` |
| `results/structure_d/covariance_usage.csv` | csv | Resumo por bloco observacional do modo de covariância usado (cheia, fallback diagonal, não usado). | `model,block,covariance_mode,has_full_covariance,has_diagonal_sigma` | `data/pipelines/structure_d/run_all.py` | `python -m data.pipelines.structure_d.run_all` | `run_name` em `data/pipelines/structure_d/datasets_config.json` |
| `results/OUTPUTS_TEXTUAIS_INDEX.md` | md | Índice canônico humano dos artefatos textuais de `results/`. | Tabela Markdown com metadados de reprodução e esquema. | Curadoria manual versionada no repositório. | `cat results/OUTPUTS_TEXTUAIS_INDEX.md` | `v1` |
| `results/manifest.json` | json | Manifesto de máquina com os mesmos metadados deste índice para automações/auditoria. | JSON objeto: `version`, `canonical_index`, `textual_artifacts[]`. | Curadoria manual versionada no repositório. | `cat results/manifest.json` | `v1` |
