# RLL — Workflow de execução completa com dados reais

Este documento registra o caminho operacional para acionar a coleta, auditoria e validação real por GitHub Actions sem transformar lacuna em dado sintético.

## Workflow canônico

- Arquivo: `.github/workflows/real-data-complete-execution.yml`
- Nome no GitHub Actions: `Real Data Complete Execution`
- Acionamento: `workflow_dispatch`, manual, com parâmetros explícitos.

## Como usar

1. Abrir a aba **Actions** do repositório.
2. Selecionar **Real Data Complete Execution**.
3. Clicar em **Run workflow**.
4. Escolher o modo:
   - `audit_only`: confere contratos, fontes registradas e relatórios sem baixar Pantheon+.
   - `materialize`: baixa entradas oficiais permitidas, especialmente Pantheon+SH0ES.
   - `validate`: valida usando os dados reais já materializados.
   - `full`: materializa, audita e valida em uma execução.
5. Manter `strict_real_data=true` para impedir preenchimento falso quando um arquivo real obrigatório estiver ausente.
6. Manter `commit_light_artifacts=false` quando não quiser que a CI faça commit automático de relatórios leves.


## Gate automático de contrato real-data

Além do workflow manual completo, o repositório possui o gate `.github/workflows/real-data-contract-ci.yml` (`Real Data Contract CI`) para PRs e pushes que alterem workflows, scripts, inventário, dados reais ou testes. Esse gate instala `requirements.txt`, valida `tools/docs_inventory.py --check`, executa `scripts/compute_rll_real_pipeline.py --data-source repo`, verifica o manifesto gerado e faz upload do artifact `real-data-contract-<run_id>` com `MANIFEST.json`, `COMPUTE_REPORT.md` e tabelas processadas.

Comandos locais equivalentes ao gate:

```bash
python3 tools/docs_inventory.py --check
python3 scripts/compute_rll_real_pipeline.py --output-dir /tmp/rll-real-run --real-data-dir data/real --data-source repo
python -m pytest -q tests/test_compute_rll_real_pipeline_contract.py tests/test_desi_dr2_bao_materialized.py
```

## Dados reais e fonte primária

O workflow chama `scripts/download_real_cosmology_inputs.sh` para Pantheon+SH0ES quando a materialização está habilitada. Esse script baixa somente os arquivos oficiais do repositório público `PantheonPlusSH0ES/DataRelease` e grava checksums em `data/real/downloaded_real_cosmology_inputs.sha256`.

## Failsafe, failover e rollback

- `strict_real_data=true` faz a execução falhar quando uma entrada real obrigatória falta.
- Os artefatos da execução são escritos primeiro em `artifacts/real-data-complete/`.
- O upload de artifact preserva logs, manifesto e checksums mesmo quando uma etapa falha.
- O commit automático é opcional e limitado a relatórios leves em `results/pipeline-runs/<run_id>`.
- Arquivos `mock`, `synthetic`, `example`, `placeholder` ou similares não são promovidos como dado real.

## Saídas esperadas

O artifact `real-data-complete-<run_id>` contém:

- `EXECUTION_PLAN.md`
- `PIPELINE_REPORT.md`
- `MANIFEST.json`
- `CHECKSUMS.sha256`
- `reports/real_data_policy_check.log`
- `reports/pantheon_inputs.json`, quando a verificação Pantheon+ é executada
- `reports/real_source_signature_verification.md`
- `reports/real_data_materialization_audit.md`
- `reports/structure_d_real_validation.log`, quando a validação Structure-D é executada
- `reports/run_real_pantheon_validation.log`, quando a validação Pantheon+ é executada

## Limite científico

O workflow preserva o limite de alegação do repositório: `No superiority claim unless real-data metrics pass predefined thresholds.` Isso significa que a CI pode materializar dados, calcular métricas e gerar relatórios, mas não deve declarar superioridade científica sem passar por critérios pré-definidos e auditáveis.
