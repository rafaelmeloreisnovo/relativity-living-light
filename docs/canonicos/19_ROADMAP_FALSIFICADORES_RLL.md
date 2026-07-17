# 19 — Roadmap e Falsificadores RLL

**Status:** canônico complementar  
**Origem:** extraído de `docs/canonicos/BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md`  
**Função:** transformar caminhos futuros em tarefas públicas verificáveis.  
**Última sincronização:** 2026-07-17 — integração estrutural e literatura 2025–2026.

---

## 1. Regra central

Um caminho de validação só é forte se tiver:

```text
claim → source → equation → dataset → compatibility
      → covariance → baseline → falsifier → result → allowed language
```

## 2. Conjunto adversarial

O RLL não deve ser comparado apenas com ΛCDM ou w0waCDM.

\[
\mathcal A_{\rm RLL}=
\{
\Lambda{\rm CDM},
w_0w_a,
{\rm GEDE},
{\rm Anton\! -\! Schmidt},
{\rm viscous},
{\rm interacting},
{\rm EFT/MG},
{\rm standard\ plasma},
{\rm axion/photon}
\}
\]

Os adversários são particionados por domínio. Modelos de fundo, perturbação,
propagação e polarização não devem ser misturados como se respondessem à mesma
pergunta física.

## 3. Caminhos prioritários

| ID | Domínio | Prioridade | Observável | Dataset/Fonte |
|---|---|---:|---|---|
| C00 | proveniência/compatibilidade | P0 | hashes, η(z), F_AP, método | registries + BAO + SNe |
| C01 | background cosmológico | P0 | f(z) ↔ w(z) | DESI DR2 + Pantheon+/DES-SN + Planck |
| C02 | baselines transitórios | P0 | evidência e resíduos | CPL, GEDE, Anton–Schmidt |
| C03 | matéria escura / estrutura | alta | core→cusp / halo | SIDM sims; DES Y6 |
| C04 | interação/dissipação | alta | Q, ξ, crescimento | DESI + CMB + SNe + fσ8 |
| C05 | tensão H0 | alta | H0 local vs CMB | SH0ES + Planck + DESI |
| C07 | gravidade alternativa | alta | μ(k,a), Σ(k,a), GW | H(z)+BAO+SNe+CMB+lensing |
| C09 | fóton/plasma | alta | DM, RM, ν-exponent | CHIME/FRB + DESI Legacy |
| C10 | magneto-óptico | média | EB, TB, V-mode | ACT/Planck/WMAP + nulls |

## 4. Tarefas documentais

- manter `BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md` como documento-mãe;
- usar `docs/science/RLL_OPERATIONAL_INTEGRATION_HOUSE_20260717.md` como casa de execução;
- manter fontes recentes em `data/registries/rll_recent_primary_sources_2026.json`;
- registrar ramos e gates em `data/registries/rll_operational_integration_registry.json`;
- verificar identificadores bibliográficos, versões, tabelas/equações e checksums;
- separar relevância conceitual, equivalência matemática e evidência observacional;
- preservar infinito matemático/potencial/físico/computacional/evolutivo e `TOKEN_VAZIO`.

## 5. Estado das tarefas computacionais

| Tarefa | Estado em 2026-07-17 | Evidência / próximo gate |
|---|---|---|
| verossimilhança conjunta H(z)+BAO+fσ8+CMB | ✅ implementada | consolidar com a rota FASE 20 |
| MCMC e evidência Bayesiana | ✅ executadas com limitação | cadeia, priors e reprodução permanecem |
| covariância DESI | ✅ implementada em rota separada | unificar com MCMC/nested |
| Pantheon+ no posterior | ⚠️ parcial | falta STAT+SYS completa na mesma rota |
| operadores f(z), ρs(z), w_eff(z) | ✅ executáveis | `src/rll/structural_integration.py` |
| gate η(z) de dualidade | ✅ operador; ⚠️ pipeline pendente | integrar às distâncias reais e mocks |
| gate F_AP | ✅ operador; ⚠️ relatório pendente | gerar por tracer e comparar métodos |
| interação Q=βHρ | ✅ operador mínimo; hipótese aberta | definir ρ_ref, gauge e perturbações |
| viscosidade p_eff=p−3Hξ | ✅ operador mínimo; hipótese aberta | declarar unidades, termodinâmica e estabilidade |
| FRB residual ν^-2 | ✅ operador mínimo; hipótese aberta | materializar catálogo localizado e null model |
| magneto-óptico | ⚠️ registro formal | falta modelo de campo, Faraday e instrumento |
| backend CLASS/CAMB | `TOKEN_VAZIO` | fechar perturbações antes de integrar |
| CMB TT/TE/EE e lensing | `TOKEN_VAZIO` | priors comprimidos não substituem espectros |
| crescimento não linear / N-body | `TOKEN_VAZIO` | requer setor físico fechado |

## 6. Falsificadores mínimos

O RLL perde força se:

- um baseline comparável explicar os resíduos com maior evidência ou menor penalidade;
- a conclusão desaparecer sob covariância, catálogo de SNe ou prior defensável;
- BAO e SNe forem combinados apesar de um gate de compatibilidade reprovado;
- o resultado depender de reconstrução enviesada ou de calibração não declarada;
- a assinatura FRB não diferir do plasma padrão \(\nu^{-2}\);
- a rotação de polarização não sobreviver a Faraday e calibração instrumental;
- interação/viscosidade produzirem instabilidade ou violarem conservação;
- a forma de fundo não possuir extensão perturbativa consistente;
- anterioridade, fonte ou cadeia de transformação não forem auditáveis.

## 7. Ordem de execução corrigida

```text
G0  congelar fontes, hashes, inclusão/exclusão e TOKEN_VAZIO
G1  testar η(z), F_AP, calibração e sensibilidade de reconstrução
G2  executar torneio ΛCDM/w0wa/GEDE/Anton-Schmidt/viscoso/interagente/RLL
G3  unificar full-covariance + SN STAT+SYS + MCMC/nested
G3  impor convergência, priors, nuisances e manifesto
G4  escolher fluido/campo/gravidade/propagação
G4  derivar conservação, som, perturbações e estabilidade
G5  recuperar ΛCDM em CLASS/CAMB antes de ativar RLL
G6  testar FRB e polarização em pipelines independentes do fundo
G7  inflação, BBN abundâncias, N-body, H0/S8 e revisão externa
```

## 8. Integridade

Resultado desfavorável deve ser preservado. Ciência legítima registra falha,
limite, dependência de dataset e vazio.

Dados observacionais brutos são imutáveis. Ajustes de unidade, ordem, máscara,
covariância ou calibração geram artefato derivado, comando, razão e hash.

A existência de um paper vizinho não valida o RLL; apenas define um baseline,
uma tradução física possível ou um falsificador melhor.

---

*Falsificador é aliado: ele protege o que for real.*
