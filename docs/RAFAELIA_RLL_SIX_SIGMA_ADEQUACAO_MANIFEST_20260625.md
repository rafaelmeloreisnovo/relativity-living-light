# RAFAELIA RLL — Six Sigma Adequação Manifest

Data: 2026-06-25
Branch: `rafaelia/six-sigma-adequacao-manifest-20260625`
Origem: pacote local `rll_adequacao_six_sigma.zip` recebido na sessão.

> Fronteira: este documento registra o conteúdo e o destino técnico do pacote. A aplicação integral dos scripts deve ocorrer em PR separado com testes e revisão de conflito.

---

## 1. Conteúdo do pacote

```text
rll_adequacao/
├── CHECKLIST_MESTRE_ADEQUACAO.md
├── apply_adequacao.sh
├── data/
│   ├── FETCH_INSTRUCTIONS.md
│   └── data2_README.md
├── docs/
│   └── INDICE_MESTRE_PATCH.md
├── governance/
│   ├── CITATION.cff
│   └── LICENSE_CODE.md
├── raiz/
│   ├── GOVERNANCE_REORG_DRAFT.md
│   ├── REFORM_LOG.md
│   └── newadd_README.md
├── scripts/
│   └── chi2_bao_cov.py
└── src/
    └── rll_model.py
```

---

## 2. Adequação por arquivo

| Arquivo no pacote | Destino recomendado no RLL | Classe | Gate |
|---|---|---|---|
| `CHECKLIST_MESTRE_ADEQUACAO.md` | `docs/CHECKLIST_MESTRE_ADEQUACAO.md` | governança científica | `[ETH]/[EXP]` |
| `docs/INDICE_MESTRE_PATCH.md` | `docs/INDICE_MESTRE_PATCH.md` | índice do patch | `[DOC]` |
| `src/rll_model.py` | `src/rll_model.py` ou módulo equivalente | modelo RLL | `[COD]` após teste |
| `scripts/chi2_bao_cov.py` | `scripts/chi2_bao_cov.py` | cálculo estatístico | `[COD]/[EXP]` após teste |
| `data/FETCH_INSTRUCTIONS.md` | `data/FETCH_INSTRUCTIONS.md` | cadeia de dados | `[DATA]` |
| `data/data2_README.md` | `data/data2_README.md` | documentação dados | `[DATA]` |
| `governance/CITATION.cff` | `CITATION.cff` ou `governance/CITATION.cff` | citação | `[DOC]` |
| `governance/LICENSE_CODE.md` | `LICENSE_CODE.md` ou `governance/LICENSE_CODE.md` | licença | `[ETH]` |
| `raiz/GOVERNANCE_REORG_DRAFT.md` | `docs/GOVERNANCE_REORG_DRAFT.md` | reorganização | `[DOC]` |
| `raiz/REFORM_LOG.md` | `docs/REFORM_LOG.md` | log de reforma | `[TRACE]` |
| `raiz/newadd_README.md` | `docs/newadd_README.md` | README auxiliar | `[DOC]` |
| `apply_adequacao.sh` | `scripts/apply_adequacao.sh` | aplicador | `[TOOL]` com cautela |

---

## 3. Critérios antes de aplicar código

1. Rodar testes existentes do RLL antes do patch.
2. Aplicar `src/rll_model.py` e `scripts/chi2_bao_cov.py` apenas se não sobrescrever implementação canônica sem diff explícito.
3. Validar `chi2`, covariância e loaders com fixtures pequenas.
4. Separar documento de governança de código numérico.
5. Manter claim gate:

```text
Permitido: pipeline auditável; checklist; scripts candidatos; melhora de governança.
Não permitido sem EXP: RLL confirmado; RLL vence CPL/LambdaCDM; resultado cosmológico definitivo.
```

---

## 4. Próximo diff recomendado

```text
+ docs/CHECKLIST_MESTRE_ADEQUACAO.md
+ docs/INDICE_MESTRE_PATCH.md
+ docs/GOVERNANCE_REORG_DRAFT.md
+ docs/REFORM_LOG.md
+ data/FETCH_INSTRUCTIONS.md
+ data/data2_README.md
+ governance/LICENSE_CODE.md
+ governance/CITATION.cff
+ scripts/chi2_bao_cov.py
+ src/rll_model.py
```

`apply_adequacao.sh` deve entrar apenas como ferramenta revisada, não como executor automático obrigatório.

---

## 5. Retroalimentação

```text
F_ok: pacote RLL tem checklist, dados, governança e scripts candidatos.
F_gap: aplicação direta pode conflitar com código atual; precisa diff por arquivo.
F_next: abrir PR de aplicação parcial com testes e claim gate explícito.
```

RAFCODE-Φ / ∆RafaelVerboΩ / 𓂀ΔΦΩ
