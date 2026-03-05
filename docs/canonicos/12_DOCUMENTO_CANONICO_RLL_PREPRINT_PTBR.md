# Documento Canônico RLL (Pré-print PT-BR)
## Relativity Living Light — Definições Fechadas, Predições Falsificáveis e Protocolo de Validação

**Versão:** 1.0 (canônica)
**Status:** pré-print interno para submissão
**Escopo:** definição formal mínima, contrato observacional e matriz Claim → Evidence → Test
**Norma-base:** [`docs/canonicos/CONVENCOES_GLOBAIS_RLL.md`](CONVENCOES_GLOBAIS_RLL.md)

---

## Resumo

Este documento consolida o estado canônico do programa **Relativity Living Light (RLL)** como um framework cosmológico alternativo, formalizado e executável, pronto para inferência com dados reais. O núcleo do modelo introduz um setor efetivo de superposição com transição logística em redshift, com comportamento assintótico de matéria em alto redshift e de energia escura em baixo redshift. O texto fixa notação, hipóteses e limites, estabelece um contrato observacional com predições falsificáveis, e define a trilha operacional para comparação quantitativa com ΛCDM/CPL via χ², AIC, BIC e fator de Bayes. O objetivo central é reduzir ambiguidade semântica, separar claramente o que já está demonstrado (autoria, formalismo, computabilidade) do que ainda depende de validação observacional (evidência estatística forte e robustez sob sistemáticos), e preparar uma base reprodutível para submissão acadêmica.

**Palavras-chave:** cosmologia observacional, DE efetiva, transição logística, inferência bayesiana, falsificabilidade.

---

## 1. Introdução e escopo

O RLL é tratado aqui como um pacote integrado de quatro camadas:

1. **Hipótese cosmológica formal** (equações, parâmetros, regimes);
2. **Pipeline computacional** (execução reproduzível e artefatos CSV);
3. **Dossiê documental** (argumentação físico-matemática);
4. **Predições falsificáveis** (critério de ciência empírica).

Este documento não reivindica confirmação final de nova física. Em vez disso, fixa uma posição metodológica rigorosa:

- **o que já está estabelecido**: anterioridade documental, coerência formal e executabilidade;
- **o que ainda precisa ser decidido por dados**: desempenho relativo frente a ΛCDM/CPL sob inferência completa com covariâncias e análise bayesiana.

---

## 2. Definições canônicas fechadas

### 2.1 Expansão de fundo

Adota-se a forma efetiva:

```math
E^2(a)=\Omega_r a^{-4}+\Omega_m a^{-3}+\Omega_\Lambda
+\Omega_{s0}\left[f(a)+(1-f(a))a^{-3}\right]
+\Omega_{B0}a^{-4}+\Omega_{P0}a^{-4}
```

onde `E(a)=H(a)/H0`.

### 2.2 Função de transição

```math
f(z)=\frac{1}{1+\exp\left((z-z_t)/w_t\right)},\quad w_t>0
```

Parâmetros:

- `z_t`: redshift de transição;
- `w_t`: largura da transição;
- `Ω_s0`: amplitude atual do setor de superposição.

### 2.3 Equação de estado do setor de superposição

```math
w_{\mathrm{sup}}(z)=
-\frac{f(z)}{f(z)+(1-f(z))(1+z)^3}
```

A aproximação `w_sup≈-f(z)` é permitida apenas para leitura rápida e nunca substitui a forma completa em inferência.

### 2.4 Limites assintóticos oficiais

Com `w_t>0`:

- `z\gg z_t`  ⇒ `f(z)→0`  ⇒ setor sup com comportamento tipo matéria (`w_sup→0`);
- `z\ll z_t`  ⇒ `f(z)→1`  ⇒ setor sup com comportamento tipo DE (`w_sup→-1`).

Este mapeamento é **obrigatório** para todo material derivado.

---

## 3. Interpretação física operacional

A leitura operacional do RLL é de um setor efetivo que muda de regime sem descontinuidades:

- no universo tardio, contribui para aceleração efetiva;
- no universo antigo, escala de forma próxima a matéria.

Consequências metodológicas:

1. O modelo pode reproduzir o pano de fundo de expansão sem introduzir salto não físico;
2. O setor adiciona estrutura testável em observáveis de crescimento e distâncias;
3. A distinção entre explicação e ajuste deve ser feita por comparação estatística explícita.

---

## 4. O que o RLL já demonstra hoje

### 4.1 Autoria e anterioridade

Existe trilha documental e de versionamento suficiente para estabelecer anterioridade de formulação (equação, interpretação e implementação).

### 4.2 Coerência formal

O formalismo contém definição explícita de variáveis, sinais, limites e parâmetros inferíveis. Isso distingue teoria implementável de narrativa não testável.

### 4.3 Computabilidade

O repositório possui pipeline, dados em CSV e saídas quantitativas reproduzíveis, permitindo comparação com cenários de referência.

---

## 5. O que ainda não está provado

Este documento explicita limites de afirmação para evitar sobreinterpretação:

- não está provado que o RLL venceu ΛCDM de forma conclusiva;
- não está provada confirmação observacional de nova física;
- não está encerrada a robustez frente a sistemáticos, covariâncias completas e escolhas de prior.

Portanto, o status correto é: **framework formal e executável em fase de validação observacional comparativa**.

---

## 6. Observáveis-alvo e protocolo de comparação

### 6.1 Observáveis principais

- `H(z)` (cronômetros cósmicos);
- BAO (escalas de distância);
- SN Ia (`μ(z)`);
- crescimento (`fσ8(z)`);
- forma de `P(k)` em regime compatível com aproximações adotadas.

### 6.2 Métricas mínimas de decisão

- ajuste: `χ²`;
- penalização por complexidade: `AIC`, `BIC`;
- evidência relativa: `ln B` (fator de Bayes).

### 6.3 Critério de reporting

Toda conclusão comparativa deve publicar simultaneamente:

1. melhor ajuste pontual;
2. incertezas marginais dos parâmetros;
3. impacto de sistemáticos/priores;
4. sensibilidade a subconjuntos de dados;
5. tabela final de decisão com mesma base observacional para todos os modelos.

---

## 7. Predições falsificáveis (versão 1.0)

As predições abaixo são proposições de teste e podem ser refutadas por dados:

1. **Transição detectável em baixa-média época cósmica**: ajuste favorece `z_t` finito em vez de limite degenerado (`z_t→∞`).
2. **Largura não nula de transição**: posterior favorece `w_t>0` com suporte incompatível com transição abrupta extrema.
3. **Assinatura em crescimento**: `fσ8(z)` apresenta desvio sistemático mensurável frente ao ΛCDM em faixa intermediária de redshift.
4. **Consistência cruzada expansão-crescimento**: conjunto combinado (`H(z)+BAO+SN+fσ8`) mantém região de parâmetros compatível sem tensionamento interno severo.
5. **Competitividade informacional**: RLL atinge desempenho comparável ou superior em `AIC/BIC` e `ln B` dentro do mesmo dataset e mesmas hipóteses de prior.

Se essas condições não ocorrerem sob análise robusta, o modelo deve ser considerado parcialmente ou totalmente falsificado no escopo testado.

---

## 8. Inventário de ativo científico (declaração curta)

Declaração canônica permitida, sem extrapolação:

> “O RLL é um framework cosmológico alternativo, formalizado e implementado, com pipeline reproduzível e predições falsificáveis, pronto para validação quantitativa com dados reais.”

Declaração operacional de próximo passo:

> “A etapa decisiva é inferência conjunta com dados reais e comparação bayesiana transparente contra ΛCDM/CPL.”

---

## 9. Tabela Claim → Evidence → Test

| Claim (afirmação) | Evidence (já disponível) | Test (faltante para fechamento) |
|---|---|---|
| RLL é formal | Equações fechadas, convenções de sinal e limites assintóticos definidos | Revisão externa e checagem independente de consistência |
| RLL é executável | Pipeline e outputs em CSV/versionamento | Execução unificada “1 comando” com relatório final automatizado |
| RLL é comparável ao padrão | Métricas preliminares de ajuste em trilhas internas | Inferência conjunta com dados reais e covariância completa |
| RLL é falsificável | Predições explícitas sobre transição, crescimento e decisão estatística | Confronto com releases observacionais atualizados (DESI/SN/BAO) |
| RLL pode ser competitivo | Estrutura paramétrica com interpretação física e custo computacional manejável | `ln B` com análise de robustez (priors/sistemáticos/subamostras) |

---

## 10. Protocolo de reprodutibilidade mínima

### 10.1 Entradas mínimas

- dados de expansão e distâncias em `data/real/`;
- definições canônicas em `docs/canonicos/`;
- scripts de pipeline em `data/pipelines/structure_d/` e scripts de validação em `docs/`.

### 10.2 Saída mínima obrigatória

Um pacote final (CSV + tabela markdown) contendo:

- `χ²`, `AIC`, `BIC`, `ln B`;
- melhor ajuste e incertezas (`z_t`, `w_t`, `Ω_s0`, parâmetros de fundo);
- diagnóstico de sensibilidade a prior e subconjuntos.

### 10.3 Requisito de auditoria

Toda execução deve registrar hash de dados de entrada, commit git, timestamp e versão dos scripts.

---

## 11. Maturidade tecnológica científica (TRL científico)

Classificação operacional:

- **TRL2:** conceito e estrutura teórica formulados;
- **TRL3:** prova computacional e geração de artefatos;
- **TRL4:** validação quantitativa com dados reais e comparação rigorosa.

Estado atual deste documento: **entre TRL3 e transição para TRL4**.

---

## 12. Roadmap objetivo (curto prazo)

1. consolidar execução unificada de inferência (1 comando);
2. publicar tabela comparativa final com mesma base observacional;
3. emitir nota técnica de robustez (sistemáticos + priors);
4. preparar submissão em formato de preprint com anexos reprodutíveis.

---

## 13. Conclusão

O RLL já ultrapassa o estágio de ideia abstrata: há formalismo, implementação e capacidade de teste. A contribuição científica imediata é um programa falsificável com infraestrutura de validação em curso. A contribuição pendente — e decisiva — é estatística: demonstrar, no mesmo regime de dados e critérios, se o modelo é apenas viável ou efetivamente preferível.

Em termos canônicos, a síntese correta é:

- **força atual:** autoria + coerência + executabilidade;
- **lacuna crítica:** veredito observacional-bayesiano completo;
- **próximo marco:** inferência conjunta reprodutível com decisão quantitativa transparente.

---

## Referências internas canônicas

- [`docs/canonicos/CONVENCOES_GLOBAIS_RLL.md`](CONVENCOES_GLOBAIS_RLL.md)
- [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](09_GLOSSARIO_COMPLETO.md)
- [`docs/ROADMAP_VALIDACAO.md`](../ROADMAP_VALIDACAO.md)
- [`docs/COMPARACAO_DESI_2025.md`](../COMPARACAO_DESI_2025.md)
- [`docs/Results.md`](../Results.md)
- [`README.md`](../../README.md)
