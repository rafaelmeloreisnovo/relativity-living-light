# Validação real RLL

Este diretório contém o bundle executável de validação real que antes estava
misturado em `.github/workflows`. A separação é intencional:

- `.github/workflows` fica reservado a workflows executáveis do GitHub Actions.
- `validacao_real/` contém scripts, contratos YAML de dados, fallbacks embutidos
  e artefatos gerados pela validação RLL vs LCDM.
- `docs/pipelines/validation_paths/` contém metodologia e arquivos de apoio que
  não devem ser interpretados pelo GitHub como workflows.

## Fluxo padrão

```bash
cd validacao_real
python3 fetch_real_data.py
python3 compute_validation.py
python3 make_figures.py
python3 render_report.py
```

## Artefatos

- `fetched/`: dados materializados e manifesto de proveniência.
- `results/`: métricas, predições, relatório renderizado e figuras.
- `legacy_artifacts/`: artefatos históricos preservados ao remover a fricção do
  diretório `.github/workflows`.

## Princípio operacional

A validação não declara descoberta. Ela materializa dados públicos/fallbacks,
calcula métricas explícitas e registra critérios de falsificação. Se a execução
falhar, o erro deve permanecer visível para fail-safe/failover/rollback.
