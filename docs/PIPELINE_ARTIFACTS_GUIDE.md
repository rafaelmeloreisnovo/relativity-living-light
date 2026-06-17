# PIPELINE_ARTIFACTS_GUIDE

## Workflow orquestrador único
- Workflow: `.github/workflows/rll-real-data-orchestrator.yml`.
- Entrada manual por `workflow_dispatch` com combo boxes (`pipeline_scope`, `dataset_group`, `mode`, `book_scope`, `retention_days`) e checkboxes de fontes reais.

## Modos
- `metadata_only`: gera metadados e reports sem baixar payload pesado.
- `fetch`: baixa fontes leves e registra fontes pesadas como `pending_manual_or_large_download`.
- `compute`: calcula quando dados suficientes existem; ausências ficam `pending_data`.
- `plots`: gera PNGs a partir de tabelas existentes ou painel `pending_data`.
- `full`: executa fetch + compute + plots.

## Artifact e download
- Baixe em GitHub Actions > run > Artifacts.
- O pacote inclui `MANIFEST.json`, `DATA_SOURCES.md`, `FETCH_REPORT.md`, `COMPUTE_REPORT.md`, `CLAIM_REFERENCE_AUDIT.md`, `CHECKSUMS.sha256`.

## commit_light_artifacts
- Use quando precisar persistir somente arquivos leves em `results/pipeline-runs/<run_id>/`.
- Nunca comitar dados brutos pesados para evitar inflar histórico Git e violar trilha de custódia operacional.

## CHECKSUMS.sha256
- Formato: `sha256  arquivo`.
- Verifica integridade e cadeia de custódia dos arquivos do artifact.

## Taxonomia de status
- `real_data`: arquivo baixado de fonte oficial com hash.
- `fallback_local`: CSV local usado explicitamente como fallback/cache.
- `compute_stub`: cálculo ainda incompleto com TODO técnico explícito.
- `pending_data`: dado ausente; sem resultado fingido.
- `validated_result`: só após dados reais processados + métricas + reprodutibilidade.
