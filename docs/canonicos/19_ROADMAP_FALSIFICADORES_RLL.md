# 19 — Roadmap e Falsificadores RLL

**Status:** canônico complementar  
**Origem:** extraído de `docs/canonicos/BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md`  
**Função:** transformar caminhos futuros em tarefas públicas verificáveis.  
**Última sincronização:** 2026-07-17 — ver `docs/science/RLL_COSMOLOGY_GAP_AUDIT_20260717.md`.

---

## 1. Regra central

Um caminho de validação só é forte se tiver:

```text
claim → dataset → métrica → baseline → falsificador → resultado versionado
```

## 2. Adversário principal

O adversário científico principal do RLL é **w0waCDM**, não apenas ΛCDM.

## 3. Caminhos prioritários

| ID | Domínio | Prioridade | Observável | Dataset/Fonte |
|---|---|---:|---|---|
| C01 | background cosmológico | pré-requisito | f(z) ↔ w(z) | DESI DR2 + Pantheon+ + Planck |
| C03 | matéria escura / estrutura | alta | core→cusp / halo | SIDM sims; DES Y6 |
| C05 | tensão H0 | alta | H0 local vs CMB | SH0ES + Planck + DESI |
| C07 | gravidade alternativa | alta | aceleração sem DE | H(z)+BAO+SNe |
| C09 | fóton/plasma | média | dispersão em plasma | CHIME/FRB |

## 4. Tarefas documentais

- dividir o documento-mãe em módulos canônicos;
- verificar identificadores bibliográficos;
- atualizar `docs/INDICE_MESTRE.md`;
- registrar pendências em checklist;
- manter `BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md` como documento-mãe;
- separar infinito matemático, potencial, físico, computacional, evolutivo e `TOKEN_VAZIO` pelo protocolo `RLL_INFINITY_OPEN_EVOLUTION_PROTOCOL.md`.

## 5. Estado das tarefas computacionais

| Tarefa histórica | Estado em 2026-07-17 | Evidência / próximo gate |
|---|---|---|
| verossimilhança conjunta H(z)+BAO+fσ8+CMB | ✅ implementada | `data/pipelines/structure_d/joint_real_likelihood.py`; consolidar com a rota FASE 20 |
| MCMC e evidência Bayesiana | ✅ executadas com limitação | `scripts/rll_fase20_mcmc_bayes.py`; cadeia curta e sensibilidade a prior permanecem |
| covariância BAO 2×2 por tracer | ✅ implementada na FASE 20 | migrar o sampler canônico para a matriz DESI completa 13×13 já materializada |
| covariância DESI completa | ✅ implementada em rota separada | `data/real/desi_dr2_bao_covariance.csv`; unificar com MCMC/nested |
| Pantheon+ no posterior | ⚠️ parcial | FASE 20 usa erros diagonais; falta STAT+SYS completa na mesma rota |
| r_d derivado/calibrado | ✅ implementado | preservar estudo de sistemáticos e política única entre modelos |
| mapeamento f(z) → w_eff(a) → w0wa | ⚠️ parcial | cálculo existe; falta fechamento físico/perturbativo e relatório canônico único |
| relatório automático com hashes e commit | ⚠️ parcial | múltiplos manifestos existem; falta uma única cadeia de posterior publication-grade |
| backend CLASS/CAMB | `TOKEN_VAZIO` | fechar perturbações, estabilidade e interface antes de integrar |
| CMB TT/TE/EE e lensing | `TOKEN_VAZIO` | priors comprimidos existem, espectros completos não |
| crescimento não linear / N-body | `TOKEN_VAZIO` | requer modelo perturbativo e setor físico fechado |

### Regra de atualização

Uma tarefa não volta a `TOKEN_VAZIO` apenas porque existe uma rota melhor desejável. Use:

- `implementada` quando código e artefato existem;
- `parcial` quando a rota existe, mas a covariância, convergência, backend ou sistemática é incompleta;
- `TOKEN_VAZIO` somente quando a evidência operacional requerida não existe.

## 6. Falsificadores mínimos

O RLL perde força se:

- w0waCDM explicar os mesmos resíduos com menor penalidade AIC/BIC;
- a assinatura magnética/plasmática não produzir diferença observável;
- parâmetros RLL exigirem ajuste fino sem ganho preditivo;
- resultados desaparecerem ao usar covariância correta;
- a anterioridade não for comprovável por commit, tag, DOI ou artefato datado;
- o resultado depender de uma rota estatística mais fraca quando uma rota canônica mais completa estiver disponível;
- a cadeia não convergir ou a conclusão mudar materialmente sob priors defensáveis.

## 7. Ordem de execução corrigida

```text
P0  unificar full-covariance + Pantheon STAT+SYS + MCMC/nested
P0  impor convergência e sensibilidade a priors
P1  definir setor RLL como fluido/campo/gravidade/propagação
P1  derivar conservação, som, perturbações e estabilidade
P2  integrar CLASS/CAMB e recuperar ΛCDM antes de ativar RLL
P2  gerar CMB/lensing/P(k) e likelihoods correspondentes
P3  inflação, BBN abundâncias, N-body, H0/S8 e CHIME/FRB
```

## 8. Integridade

Resultado desfavorável deve ser preservado. Ciência legítima registra falha, limite e vazio.

O protocolo de infinito/open evolution não promove resultados cosmológicos. Ele apenas garante que ciclos exploratórios sejam finitos, detectem repetição, preservem contradições e emitam `TOKEN_VAZIO` quando a evidência for insuficiente.

---

*Falsificador é aliado: ele protege o que for real.*
