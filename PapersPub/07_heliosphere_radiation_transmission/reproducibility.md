# Reproducibility — Heliosfera: Transmissão de Radiação

**Status:** `planned`

## Ambiente mínimo

- Registrar sistema operacional, versão de Python/compilador, dependências e seeds.
- Preferir comandos determinísticos e arquivos versionados.
- Preservar logs em `results/` ou artefatos dedicados antes de promover status.

## Comandos previstos

```bash
# Inventário de fontes até 5 níveis, sem mover conteúdo
find RAFAELIA_COSMO_STRUCTURE_D/paper newadd docs -maxdepth 5 -type f | sort

# Auditoria de status das trilhas PapersPub
find PapersPub -maxdepth 2 -name draft.md -o -name data_manifest.md -o -name reproducibility.md | sort
```

## FAILSAFE

- Não atualizar status para `analysis_run` sem comando, saída, dataset e métrica.
- Não aceitar resultado sem baseline comparável quando a claim envolver superioridade.
- Não apagar artefatos legados durante preparação do paper.

## FAILOVER

- Se dataset real estiver indisponível, marcar como `planned` ou `data_ingested` parcial e não inferir validação real.
- Se pipeline principal falhar, registrar fallback e diferença metodológica antes de usar resultados.

## ROLLBACK

- Para qualquer migração futura, manter origem e destino documentados no `data_manifest.md`.
- Reverter promoção de status se testes, checksums ou métricas não forem reproduzíveis.

## Mitigação de risco científico

Resultados negativos, penalização por complexidade, p-valores desfavoráveis, vieses residuais e lacunas de dados devem aparecer no draft antes de submissão.
