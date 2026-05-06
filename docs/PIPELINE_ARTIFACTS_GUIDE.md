# PIPELINE_ARTIFACTS_GUIDE

## Workflow manual
1. Abra **GitHub Actions** no repositório.
2. Escolha **RLL Book Data Pipeline** (`.github/workflows/rll-book-data-pipeline.yml`).
3. Clique em **Run workflow**.
4. Selecione `book_scope`, `dataset_group`, `mode`, `flush_artifact`, `commit_artifacts` e `retention_days`.

## Escolha de `book_scope`
- `methodology`: trilha metodológica (caps. 11–14).
- `real_data`: nó de dados reais (cap. 13 + H(z), BAO e χ² inicial).
- `scripts`: mapeamento de notebooks/scripts reprodutíveis (cap. 14).
- `observational_validation`: rota observacional completa (caps. 15–24).
- `desi_boss`: camada DESI DR2/BOSS DR12/eBOSS DR16/Planck 2018 (cap. 21).
- `amas_mcrp`: ligação AMAS/SAA com MCRP sem afirmar validação total.
- `all`: agrega todos os blocos canônicos acima.

## Escolha de `dataset_group`
- `geomagnetic`: M(t), m(t), T_M.
- `heliophysics`: Φ_ext, SW, T_M, Φ_eff.
- `cosmology`: E²(a), f(z), w(z), comparação RLL vs ΛCDM/w0waCDM.
- `all`: executa os três grupos.

## Modos (`mode`)
- `metadata_only`: gera manifestos/rota/auditoria sem ingestão de dados pesados.
- `dry_run`: simula execução com trilha e contratos de saída.
- `fetch`: prepara/realiza ingestão controlada quando aplicável.
- `compute`: reservado para cálculo; o guardrail mantém status editorial sem promoção automática para “Real validado”.

## Download de artifact
- Acesse a execução do workflow.
- Em **Artifacts**, baixe `rll-book-pipeline-<run_id>-...`.
- O pacote inclui `RUN_UTC.txt`, `COMMIT_SHA.txt`, `CHECKSUMS.sha256`, manifestos e rota do livro.

## Quando usar `commit_artifacts`
Use `commit_artifacts=true` apenas quando precisar persistir resultados leves e rastreáveis em:
- `results/pipeline-runs/<github.run_id>/`

A rotina limita commit a `*.md`, `*.json`, `*.txt`, `*.sha256`.

## Por que não commitar dados brutos pesados
- Evita crescimento indevido do histórico Git.
- Preserva reprodutibilidade operacional com pipelines de ingestão versionados.
- Mantém `results/` para saídas pequenas persistentes e não para storage massivo.

## Como interpretar `CHECKSUMS.sha256`
- Cada linha é `sha256 arquivo`.
- Permite verificar integridade local após download.
- Permite comparar execuções e detectar mudanças de conteúdo.

## Ordem editorial guiada por `book/README.md`
- `book/README.md` é a trilha principal oficial.
- `book_scope` recorta blocos da trilha sem quebrar a ordem canônica.
- A execução respeita: `docs/` (entrada científica), `data/` (entrada/execução), `results/` (saída pequena), `data/pipelines/structure_d/` (módulos), `to_Add/` (histórico).
