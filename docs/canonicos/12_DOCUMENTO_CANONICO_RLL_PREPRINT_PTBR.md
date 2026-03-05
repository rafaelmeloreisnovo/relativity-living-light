# Documento Canônico RLL (Pré-print PT-BR)
## Relativity Living Light — Definições Fechadas, Predições Falsificáveis e Protocolo de Validação

**Versão:** 1.1 (canônica)
**Status:** pré-print interno para submissão
**Escopo:** definição formal mínima, contrato observacional e matriz Claim → Evidence → Test
**Norma-base:** [`docs/canonicos/CONVENCOES_GLOBAIS_RLL.md`](CONVENCOES_GLOBAIS_RLL.md)

---

## Resumo

Este documento consolida o estado canônico do programa **Relativity Living Light (RLL)** como um framework cosmológico alternativo, formalizado e executável, pronto para inferência com dados reais [INT-001][INT-002]. O núcleo do modelo introduz um setor efetivo de superposição com transição logística em redshift, com comportamento assintótico de matéria em alto redshift e de energia escura em baixo redshift [INT-003]. O texto fixa notação, hipóteses e limites, estabelece um contrato observacional com predições falsificáveis, e define a trilha operacional para comparação quantitativa com ΛCDM/CPL via χ², AIC, BIC e fator de Bayes [INT-004][EXT-001]. O objetivo central é reduzir ambiguidade semântica, separar claramente o que já está demonstrado (autoria, formalismo, computabilidade) do que ainda depende de validação observacional (evidência estatística forte e robustez sob sistemáticos), e preparar uma base reprodutível para submissão acadêmica [INT-005].

**Palavras-chave:** cosmologia observacional, DE efetiva, transição logística, inferência bayesiana, falsificabilidade.

### Convenção canônica de citação por claim técnica

- **Markdown (documentos canônicos):** usar chaves explícitas no corpo do texto, no formato `[INT-###]` (fonte interna) e `[EXT-###]` (fonte externa).
- **LaTeX (preprint):** usar chaves bibliográficas em `\cite{...}` (ex.: `\cite{desi2025}`, `\cite{trotta2008}`).
- **Regra de auditoria:** toda afirmação factual/técnica deve carregar ao menos uma chave.

---

## 1. Introdução e escopo

### 1.1 Formato canônico de citação de claims técnicas

- **Markdown (documentos canônicos):** usar chaves explícitas no corpo do texto, no formato `[INT-XXX]` para fontes internas e `[EXT-XXX]` para fontes externas.
- **LaTeX (paper acadêmico):** usar `\cite{chave}` com chave bibliográfica unificada (ex.: `\cite{desi2025}`, `\cite{okada2026}`).
- **Regra editorial:** toda afirmação factual/testável deve portar ao menos uma chave de referência.

O RLL é tratado aqui como um pacote integrado de quatro camadas:

1. **Hipótese cosmológica formal** (equações, parâmetros, regimes) [INT-002][INT-003];
2. **Pipeline computacional** (execução reproduzível e artefatos CSV) [INT-006];
3. **Dossiê documental** (argumentação físico-matemática) [INT-001];
4. **Predições falsificáveis** (critério de ciência empírica) [INT-004].

Este documento não reivindica confirmação final de nova física. Em vez disso, fixa uma posição metodológica rigorosa:

- **o que já está estabelecido**: anterioridade documental, coerência formal e executabilidade [INT-005][INT-006];
- **o que ainda precisa ser decidido por dados**: desempenho relativo frente a ΛCDM/CPL sob inferência completa com covariâncias e análise bayesiana [EXT-001][EXT-004].

---

## 2. Definições canônicas fechadas

### 2.1 Expansão de fundo

Adota-se a forma efetiva [INT-002]:

```math
E^2(a)=\Omega_r a^{-4}+\Omega_m a^{-3}+\Omega_\Lambda
+\Omega_{s0}\left[f(a)+(1-f(a))a^{-3}\right]
+\Omega_{B0}a^{-4}+\Omega_{P0}a^{-4}
```

onde `E(a)=H(a)/H0` [INT-002].

Definição operacional alinhada ao formalismo canônico de notação e decomposição por componentes cosmológicos. [INT-001]

### 2.2 Função de transição

```math
f(z)=\frac{1}{1+\exp\left((z-z_t)/w_t\right)},\quad w_t>0
```

Parâmetros [INT-003]:

- `z_t`: redshift de transição;
- `w_t`: largura da transição;
- `Ω_s0`: amplitude atual do setor de superposição.

Forma logística adotada para garantir transição suave e parametrizável entre regimes dinâmicos. [INT-002]

### 2.3 Equação de estado do setor de superposição

```math
w_{\mathrm{sup}}(z)=
-\frac{f(z)}{f(z)+(1-f(z))(1+z)^3}
```

A aproximação `w_sup≈-f(z)` é permitida apenas para leitura rápida e nunca substitui a forma completa em inferência [INT-003].

O uso de forma completa em inferência evita viés de aproximação no cálculo de observáveis derivados. [EXT-003]

### 2.4 Limites assintóticos oficiais

Com `w_t>0` [INT-003]:

- `z\gg z_t`  ⇒ `f(z)→0`  ⇒ setor sup com comportamento tipo matéria (`w_sup→0`);
- `z\ll z_t`  ⇒ `f(z)→1`  ⇒ setor sup com comportamento tipo DE (`w_sup→-1`).

Este mapeamento é **obrigatório** para todo material derivado [INT-003].
Esses limites são a referência oficial para consistência entre implementação numérica, texto e validação observacional. [INT-003]

Este mapeamento é **obrigatório** para todo material derivado.

---

## 3. Interpretação física operacional

A leitura operacional do RLL é de um setor efetivo que muda de regime sem descontinuidades [INT-002][INT-003]:

- no universo tardio, contribui para aceleração efetiva [INT-003];
- no universo antigo, escala de forma próxima a matéria [INT-003].

Consequências metodológicas:

1. O modelo pode reproduzir o pano de fundo de expansão sem introduzir salto não físico [INT-003];
2. O setor adiciona estrutura testável em observáveis de crescimento e distâncias [INT-004];
3. A distinção entre explicação e ajuste deve ser feita por comparação estatística explícita [EXT-001][EXT-004].
1. O modelo pode reproduzir o pano de fundo de expansão sem introduzir salto não físico;
2. O setor adiciona estrutura testável em observáveis de crescimento e distâncias. [EXT-004]
3. A distinção entre explicação e ajuste deve ser feita por comparação estatística explícita. [EXT-005]

---

## 4. O que o RLL já demonstra hoje

### 4.1 Autoria e anterioridade

Existe trilha documental e de versionamento suficiente para estabelecer anterioridade de formulação (equação, interpretação e implementação) [INT-001][INT-005].

### 4.2 Coerência formal

O formalismo contém definição explícita de variáveis, sinais, limites e parâmetros inferíveis [INT-002][INT-003]. Isso distingue teoria implementável de narrativa não testável [INT-005].

### 4.3 Computabilidade

O repositório possui pipeline, dados em CSV e saídas quantitativas reproduzíveis, permitindo comparação com cenários de referência [INT-006].

---

## 5. O que ainda não está provado

Este documento explicita limites de afirmação para evitar sobreinterpretação:

- não está provado que o RLL venceu ΛCDM de forma conclusiva [INT-006];
- não está provada confirmação observacional de nova física [EXT-001][EXT-004];
- não está encerrada a robustez frente a sistemáticos, covariâncias completas e escolhas de prior [EXT-001][EXT-004].

Portanto, o status correto é: **framework formal e executável em fase de validação observacional comparativa** [INT-006].

---

## 6. Observáveis-alvo e protocolo de comparação

### 6.1 Observáveis principais

- `H(z)` (cronômetros cósmicos) [EXT-004];
- BAO (escalas de distância) [EXT-001];
- SN Ia (`μ(z)`) [EXT-004];
- crescimento (`fσ8(z)`) [INT-004];
- forma de `P(k)` em regime compatível com aproximações adotadas [INT-004].

### 6.2 Métricas mínimas de decisão

- ajuste: `χ²` [INT-006];
- penalização por complexidade: `AIC`, `BIC` [INT-006];
- evidência relativa: `ln B` (fator de Bayes) [EXT-001].
- `H(z)` (cronômetros cósmicos);
- BAO (escalas de distância). [EXT-006]
- SN Ia (`μ(z)`). [EXT-007]
- crescimento (`fσ8(z)`). [EXT-008]
- forma de `P(k)` em regime compatível com aproximações adotadas. [EXT-009]

### 6.2 Métricas mínimas de decisão

- ajuste: `χ²`;
- penalização por complexidade: `AIC`, `BIC`. [EXT-010]
- evidência relativa: `ln B` (fator de Bayes). [EXT-005]

### 6.3 Critério de reporting

Toda conclusão comparativa deve publicar simultaneamente [INT-006]:

1. melhor ajuste pontual;
2. incertezas marginais dos parâmetros;
3. impacto de sistemáticos/priores. [EXT-005]
4. sensibilidade a subconjuntos de dados;
5. tabela final de decisão com mesma base observacional para todos os modelos.

---

## 7. Predições falsificáveis (versão 1.0)

As predições abaixo são proposições de teste e podem ser refutadas por dados [INT-004]:

1. **Transição detectável em baixa-média época cósmica**: ajuste favorece `z_t` finito em vez de limite degenerado (`z_t→∞`) [INT-004].
2. **Largura não nula de transição**: posterior favorece `w_t>0` com suporte incompatível com transição abrupta extrema [INT-004].
3. **Assinatura em crescimento**: `fσ8(z)` apresenta desvio sistemático mensurável frente ao ΛCDM em faixa intermediária de redshift [INT-004].
4. **Consistência cruzada expansão-crescimento**: conjunto combinado (`H(z)+BAO+SN+fσ8`) mantém região de parâmetros compatível sem tensionamento interno severo [EXT-001][EXT-004].
5. **Competitividade informacional**: RLL atinge desempenho comparável ou superior em `AIC/BIC` e `ln B` dentro do mesmo dataset e mesmas hipóteses de prior [INT-006][EXT-001].
1. **Transição detectável em baixa-média época cósmica**: ajuste favorece `z_t` finito em vez de limite degenerado (`z_t→∞`). [INT-004]
2. **Largura não nula de transição**: posterior favorece `w_t>0` com suporte incompatível com transição abrupta extrema. [INT-005]
3. **Assinatura em crescimento**: `fσ8(z)` apresenta desvio sistemático mensurável frente ao ΛCDM em faixa intermediária de redshift. [EXT-008]
4. **Consistência cruzada expansão-crescimento**: conjunto combinado (`H(z)+BAO+SN+fσ8`) mantém região de parâmetros compatível sem tensionamento interno severo. [EXT-011]
5. **Competitividade informacional**: RLL atinge desempenho comparável ou superior em `AIC/BIC` e `ln B` dentro do mesmo dataset e mesmas hipóteses de prior. [EXT-005]

Se essas condições não ocorrerem sob análise robusta, o modelo deve ser considerado parcialmente ou totalmente falsificado no escopo testado [INT-004].

---

## 8. Inventário de ativo científico (declaração curta)

Declaração canônica permitida, sem extrapolação:

> “O RLL é um framework cosmológico alternativo, formalizado e implementado, com pipeline reproduzível e predições falsificáveis, pronto para validação quantitativa com dados reais.” [INT-005][INT-006]

Declaração operacional de próximo passo:

> “A etapa decisiva é inferência conjunta com dados reais e comparação bayesiana transparente contra ΛCDM/CPL.” [EXT-001][EXT-004]

---

## 9. Tabela Claim → Evidence → Test

| Claim (afirmação) | Evidence (já disponível) | Test (faltante para fechamento) |
|---|---|---|
| RLL é formal [INT-002] | Equações fechadas, convenções de sinal e limites assintóticos definidos [INT-003] | Revisão externa e checagem independente de consistência |
| RLL é executável [INT-006] | Pipeline e outputs em CSV/versionamento [INT-006] | Execução unificada “1 comando” com relatório final automatizado |
| RLL é comparável ao padrão [INT-006] | Métricas preliminares de ajuste em trilhas internas [INT-006] | Inferência conjunta com dados reais e covariância completa [EXT-001][EXT-004] |
| RLL é falsificável [INT-004] | Predições explícitas sobre transição, crescimento e decisão estatística [INT-004] | Confronto com releases observacionais atualizados (DESI/SN/BAO) [EXT-001][EXT-004] |
| RLL pode ser competitivo [INT-004] | Estrutura paramétrica com interpretação física e custo computacional manejável [INT-004] | `ln B` com análise de robustez (priors/sistemáticos/subamostras) [EXT-001] |

---

## 10. Protocolo de reprodutibilidade mínima

### 10.1 Entradas mínimas

- dados de expansão e distâncias em `data/real/` [INT-006];
- definições canônicas em `docs/canonicos/` [INT-002];
- scripts de pipeline em `data/pipelines/structure_d/` e scripts de validação em `docs/` [INT-006].

### 10.2 Saída mínima obrigatória

Um pacote final (CSV + tabela markdown) contendo [INT-006]:

- `χ²`, `AIC`, `BIC`, `ln B`;
- melhor ajuste e incertezas (`z_t`, `w_t`, `Ω_s0`, parâmetros de fundo);
- diagnóstico de sensibilidade a prior e subconjuntos.

### 10.3 Requisito de auditoria

Toda execução deve registrar hash de dados de entrada, commit git, timestamp e versão dos scripts [INT-006].

---

## 11. Maturidade tecnológica científica (TRL científico)

Classificação operacional:

- **TRL2:** conceito e estrutura teórica formulados [INT-001][INT-002];
- **TRL3:** prova computacional e geração de artefatos [INT-006];
- **TRL4:** validação quantitativa com dados reais e comparação rigorosa [EXT-001][EXT-004].
- **TRL2:** conceito e estrutura teórica formulados;
- **TRL3:** prova computacional e geração de artefatos. [INT-006]
- **TRL4:** validação quantitativa com dados reais e comparação rigorosa. [INT-007]

Estado atual deste documento: **entre TRL3 e transição para TRL4** [INT-006].

---

## 12. Roadmap objetivo (curto prazo)

1. consolidar execução unificada de inferência (1 comando) [INT-006];
2. publicar tabela comparativa final com mesma base observacional [EXT-001][EXT-004];
3. emitir nota técnica de robustez (sistemáticos + priors) [EXT-001];
4. preparar submissão em formato de preprint com anexos reprodutíveis [INT-005].

---

## 13. Conclusão

O RLL já ultrapassa o estágio de ideia abstrata: há formalismo, implementação e capacidade de teste [INT-005][INT-006]. A contribuição científica imediata é um programa falsificável com infraestrutura de validação em curso [INT-004]. A contribuição pendente — e decisiva — é estatística: demonstrar, no mesmo regime de dados e critérios, se o modelo é apenas viável ou efetivamente preferível [EXT-001][EXT-004].

Em termos canônicos, a síntese correta é:

- **força atual:** autoria + coerência + executabilidade [INT-001][INT-002][INT-006];
- **lacuna crítica:** veredito observacional-bayesiano completo [EXT-001][EXT-004];
- **próximo marco:** inferência conjunta reprodutível com decisão quantitativa transparente [INT-006][EXT-001].

---

## Referências internas canônicas

- [`docs/canonicos/CONVENCOES_GLOBAIS_RLL.md`](CONVENCOES_GLOBAIS_RLL.md)
- [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](09_GLOSSARIO_COMPLETO.md)
- [`docs/ROADMAP_VALIDACAO.md`](../ROADMAP_VALIDACAO.md)
- [`docs/COMPARACAO_DESI_2025.md`](../COMPARACAO_DESI_2025.md)
- [`docs/Results.md`](../Results.md)
- [`README.md`](../../README.md)

## Bibliografia unificada canônica (chaves)

### Chaves internas (`INT-XXX`)

- **[INT-001]** `docs/canonicos/11_DOCUMENTO_PRIORIDADE.md`
- **[INT-002]** `docs/canonicos/CONVENCOES_GLOBAIS_RLL.md`
- **[INT-003]** `docs/FORMULAS_CANONICAS_INDEX.md`
- **[INT-004]** `docs/canonicos/06_COMPARACOES_DETALHADAS.md`
- **[INT-005]** `docs/canonicos/FRAMEWORK_RESUMO_CANONICO.md`
- **[INT-006]** `docs/Results.md`

### Chaves externas (`EXT-XXX`)

- **[EXT-001]** DESI Collaboration (2025), *Evidence for Dynamic Dark Energy from Large-Scale Structure*.
- **[EXT-002]** Okada et al. (2026), *Dark Matter Can Be Born Hot and Cool Down*.
- **[EXT-003]** Böhme et al. (2025), *5.4σ dipole anomaly in CMB*.
- **[EXT-004]** Brout et al. (2022), *Pantheon+ Analysis: Cosmological Constraints*.

## Mapa de claims → referências

- Framework RLL formalizado e executável → [INT-001], [INT-002], [INT-006]
- Setor de superposição com transição logística e limites assintóticos canônicos → [INT-002], [INT-003]
- Comparação quantitativa por χ²/AIC/BIC/ln B contra ΛCDM/CPL → [INT-006], [EXT-001]
- Observáveis-alvo `H(z)`, BAO, SN Ia e `fσ8(z)` para validação → [INT-004], [EXT-001], [EXT-004]
- Predições falsificáveis envolvendo `z_t`, `w_t` e assinatura em crescimento → [INT-004]
- Estado de maturidade entre TRL3 e transição para TRL4 → [INT-006], [EXT-001], [EXT-004]
---
## 14. Referências canônicas unificadas (chaves)

### Chaves internas (INT)

- **[INT-001]** `docs/canonicos/CONVENCOES_GLOBAIS_RLL.md` (notação e decomposição canônica).
- **[INT-002]** `docs/canonicos/10_FAQ_COMPLETO.md` (função logística e interpretação operacional).
- **[INT-003]** `docs/canonicos/CONVENCOES_GLOBAIS_RLL.md` (limites assintóticos obrigatórios).
- **[INT-004]** `docs/ROADMAP_VALIDACAO.md` (teste de detecção de `z_t` finito).
- **[INT-005]** `docs/ROADMAP_VALIDACAO.md` (teste de `w_t>0` e robustez de posterior).
- **[INT-006]** `docs/Results.md` (pipeline e artefatos computacionais reproduzíveis).
- **[INT-007]** `docs/ROADMAP_VALIDACAO.md` (plano de transição TRL3→TRL4 com dados reais).

### Chaves externas (EXT)

- **[EXT-003]** Lewis \\& Bridle (2002), *Physical Review D* 66:103511 (inferência cosmológica e riscos de aproximações em parâmetros derivados).
- **[EXT-004]** Okada et al. (2026), *PRL* 136 (transição hot→cold e impacto em observáveis de crescimento/expansão).
- **[EXT-005]** Trotta (2008), *Contemporary Physics* 49:71–104 (comparação bayesiana, `ln B` e robustez a prior).
- **[EXT-006]** DESI Collaboration (2024/2025), resultados BAO e constraints cosmológicos.
- **[EXT-007]** Brout et al. (2022), Pantheon+ (*ApJ*), constraints de SN Ia em `μ(z)`.
- **[EXT-008]** BOSS Collaboration / literatura `fσ8` para crescimento linear em redshift intermediário.
- **[EXT-009]** Planck Collaboration (2020), *A\&A* 641 A6 (forma de `P(k)` e consistência com parâmetros de fundo).
- **[EXT-010]** Akaike (1974) + Schwarz (1978): definições canônicas de `AIC`/`BIC`.
- **[EXT-011]** DESI + Pantheon+ + BOSS (análises combinadas para consistência cruzada expansão-crescimento).

---

## 15. Mapa de claims → referências

| Claim curto | Chave(s) |
|---|---|
| Decomposição canônica de `E^2(a)` | [INT-001] |
| Transição logística suave com (`z_t`, `w_t`, `Ω_s0`) | [INT-002] |
| Forma completa de `w_sup(z)` para inferência | [EXT-003] |
| Limites assintóticos oficiais (`w_sup→0/-1`) | [INT-003] |
| Estrutura testável em crescimento/distâncias | [EXT-004] |
| Comparação estatística explícita por evidência | [EXT-005] |
| BAO como observável primário | [EXT-006] |
| SN Ia (`μ(z)`) como observável primário | [EXT-007] |
| Crescimento via `fσ8(z)` como observável primário | [EXT-008] |
| Forma de `P(k)` em regime compatível | [EXT-009] |
| Métricas `AIC/BIC` para penalização de complexidade | [EXT-010] |
| `ln B` para evidência relativa | [EXT-005] |
| Predição: `z_t` finito é detectável | [INT-004] |
| Predição: `w_t>0` é testável e falsificável | [INT-005] |
| Predição: assinatura em `fσ8(z)` | [EXT-008] |
| Predição: consistência conjunta (`H(z)+BAO+SN+fσ8`) | [EXT-011] |
| Predição: competitividade por `AIC/BIC` e `ln B` | [EXT-005] |
| Status atual entre TRL3 e TRL4 | [INT-006], [INT-007] |

---
