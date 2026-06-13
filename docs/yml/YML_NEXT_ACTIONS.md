# YML NEXT ACTIONS

PRs mínimos, seguros e auditáveis. Ordenados por relação valor/risco.

## Aplicado neste PR
- [x] Documentação de auditoria (`docs/yml/`).
- [x] `permissions: contents: read` nos 7 workflows sem bloco de permissões.
- [x] `timeout-minutes` em todos os jobs.
- [x] `concurrency` nos workflows que não tinham.
- [x] Gate `yml-syntax-validation.yml` (parser real em PR/push).

## ACAO_RECOMENDADA (próximos PRs, não feitos aqui)

1. **Dedupe `CAMINHOS_VALIDACAO_NOVOS.yml`** — raiz é byte-idêntica a
   `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml` (sha256
   `7c95cdf16a6b…`). Manter a versão em `docs/pipelines/...` (a referenciada
   pelos workflows) e substituir a raiz por um stub/symlink ou removê-la.
   Risco: baixo, mas é arquivo versionado → decisão do mantenedor.

2. **Pin de actions por SHA** — trocar `actions/checkout@v4`,
   `actions/setup-python@v5`, `actions/upload-artifact@v4` por hashes
   imutáveis + comentário com a tag. Supply-chain hardening.

3. **Renomear `mock_catalog.csv`** em `dha-fisher-ci.yml` para
   `ci_smoke_catalog.csv` (reduz ambiguidade real/synthetic).

4. **Padronizar `mode`** dos pipelines com a escada canônica
   `metadata_only → dry_run → fetch → compute → report → full` (hoje há
   pequenas variações entre `rll-data-pipeline` e `rll-real-data-orchestrator`).

5. **CI da validação cosmológica** — promover `validacao_real` (chi2/AIC/BIC)
   a um job de PR com publicação de `validation_summary.json` como artefato,
   para que ΛCDM-vs-RLL seja medido a cada mudança.

## F_next (PR mínimo seguinte)
Dedupe do `CAMINHOS_VALIDACAO_NOVOS.yml` (item 1) — um único arquivo tocado,
diff trivial, totalmente reversível.
