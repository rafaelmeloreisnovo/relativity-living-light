# RAFAELIA RLL — Six Sigma Source Ledger 2026-06-25

Origem: `rll_adequacao_six_sigma.zip`
SHA-256 do zip: `4b7fcf35f584f6d5edce265503dc6c2efdc9101886d4b9e29d6fc1d8e186052c`
Tamanho do zip: `31079` bytes
Conteúdo descompactado declarado: `65220` bytes

> Este ledger fixa a origem do pacote antes da aplicação em código. A aplicação integral deve ocorrer em PR separado, com diff por arquivo e testes.

## Conteúdo do zip

| Caminho interno | Bytes | Destino recomendado |
|---|---:|---|
| `rll_adequacao/src/rll_model.py` | 9440 | `src/rll_model.py` ou módulo equivalente |
| `rll_adequacao/governance/CITATION.cff` | 2457 | `governance/CITATION.cff` ou `CITATION.cff` |
| `rll_adequacao/governance/LICENSE_CODE.md` | 2388 | `governance/LICENSE_CODE.md` |
| `rll_adequacao/apply_adequacao.sh` | 6242 | `scripts/apply_adequacao.sh` com revisão manual |
| `rll_adequacao/scripts/chi2_bao_cov.py` | 14209 | `scripts/chi2_bao_cov.py` |
| `rll_adequacao/data/FETCH_INSTRUCTIONS.md` | 4151 | `data/FETCH_INSTRUCTIONS.md` |
| `rll_adequacao/data/data2_README.md` | 2329 | `data/data2_README.md` |
| `rll_adequacao/CHECKLIST_MESTRE_ADEQUACAO.md` | 9248 | `docs/CHECKLIST_MESTRE_ADEQUACAO.md` |
| `rll_adequacao/raiz/REFORM_LOG.md` | 2761 | `docs/REFORM_LOG.md` |
| `rll_adequacao/raiz/GOVERNANCE_REORG_DRAFT.md` | 6602 | `docs/GOVERNANCE_REORG_DRAFT.md` |
| `rll_adequacao/raiz/newadd_README.md` | 2471 | `docs/newadd_README.md` |
| `rll_adequacao/docs/INDICE_MESTRE_PATCH.md` | 2922 | `docs/INDICE_MESTRE_PATCH.md` |

## Claim gate

```text
[DOC] manifesto/ledger/checklist
[DATA] fetch instructions e data README
[COD-CANDIDATE] rll_model.py, chi2_bao_cov.py, apply_adequacao.sh
[EXP-REQUIRED] qualquer resultado numérico novo
```

## Ordem segura de aplicação

1. Documentos de governança e índice.
2. Instruções de dados.
3. Script estatístico com fixtures pequenas.
4. Modelo RLL com testes existentes.
5. Só depois atualizar README/citação/licença se não houver conflito.

## Retroalimentação

```text
F_ok: origem do zip fixada por hash e conteúdo interno enumerado.
F_gap: ainda não aplicado código numérico para evitar sobrescrita sem diff.
F_next: PR parcial para docs/data; PR separado para scripts/src com testes.
```
