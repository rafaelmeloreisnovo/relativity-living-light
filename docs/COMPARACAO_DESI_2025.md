# Comparação com Literatura Acadêmica 2025–2026

**Norma canônica de convenções globais:** [docs/canonicos/CONVENCOES_GLOBAIS_RLL.md](canonicos/CONVENCOES_GLOBAIS_RLL.md)

## Relativity Living Light × Resultados Observacionais Recentes

**Versão:** 2.0 | **Última atualização:** Fevereiro 2026

---

## Sumário Executivo

O modelo Relativity Living Light foi formulado em Fevereiro 2025, com commits datados no GitHub. Três resultados observacionais publicados entre Novembro 2025 e Janeiro 2026 apresentam convergência de ideia com aspectos específicos do modelo. Esta seção documenta as conexões de forma factualmente precisa, distinguindo convergência de ideias da prioridade acadêmica formal (que requer publicação peer-reviewed).

---

## 1. DESI DR2 — Energia Escura Dinâmica

**Referência:** DESI Collaboration. *Evidence for Dynamic Dark Energy*. Nature Astronomy, Dezembro 2025.  
**Significância:** 2.8–4.2σ para w(z) ≠ constante (combinação BAO+CMB+SNe).

### Conexão com RLL

O DESI reportou que a densidade de energia escura varia com o redshift, com w(z) abaixo de −1 em baixo redshift e tendendo para valores menos negativos em redshift maior. Esta é exatamente a trajetória descrita pelo w_eff(z) do modelo RLL.

```
DESI:  w(z) ≠ −1 com 2.8–4.2σ, variação monotônica identificada
RLL:   w_eff(z) = −f(z) ∈ [−1, 0], transição em z_t ≈ 1.16
```

**Distinção importante:** O DESI usa parametrização CPL (w₀, wₐ) que é linear em a. O RLL usa transição logística que é mais flexível. O mapeamento entre os dois não é trivial mas é testável. Os parâmetros CPL favorecidos pelo DESI (w₀ ≈ −0.7, wₐ ≈ −1.0) são qualitativamente compatíveis com a trajetória RLL mas o teste quantitativo direto requer cálculo explícito.

---

## 2. Okada et al. — Matéria Escura Quente → Fria

**Referência:** Okada et al. (U. Minnesota + Paris-Saclay). *Dark Matter Can Be Born Hot and Cool Down*. Physical Review Letters 136, Janeiro 2026.  
**Conceito central:** Matéria escura não precisa ser fria desde o Big Bang; pode nascer relativística e transicionar para não-relativística.

### Conexão com RLL

O modelo RLL, via função f(z), produz exatamente esse comportamento para a componente de superposição:

```
RLL (z >> z_t): ρ_sup ∝ a^{−4}  →  comportamento relativístico (quente), w ≈ 1/3
RLL (z << z_t): ρ_sup ∝ a^{−3}  →  comportamento pressureless (frio), w ≈ 0
```

### Distinção de contribuição

Minnesota descreve o conceito qualitativamente. O RLL fornece uma parametrização analítica explícita (Ω_s0, z_t, w_t) integrada na equação de Friedmann com código MCMC pronto. A precedência de commit do GitHub (Fevereiro 2025) é factualmente anterior ao artigo de Janeiro 2026, embora não constitua prioridade científica reconhecida sem peer review.

---

## 3. Nature Communications — Não-localidade Fotônica

**Referência:** DOI s41467-025-63981-3. *Nonlocality-enabled photonic analogies of parallel spaces*. Nature Communications, 2025.  
**Resultado:** Experimento em laboratório demonstra correlações não-locais em sistemas fotônicos, simulando analogias de espaços paralelos.

### Conexão com RLL

O mecanismo físico proposto para o componente de superposição é que estados fotônicos não-locais seriam a origem microscópica da transição DE↔DM cosmológica. O artigo da Nature Communications fornece evidência experimental de que fótons podem exibir estados não-locais estendidos em escala laboratorial.

### Avaliação honesta

A extensão do fenômeno laboratorial (escala mm–m) para efeitos cosmológicos (escala Gpc) requer um mecanismo de escala não estabelecido. Esta conexão permanece especulativa e não constitui suporte observacional para o modelo. Seria necessária uma derivação rigorosa de como o fenômeno quântico em escala de laboratório propaga para a equação de Friedmann.

---

## 4. Böhme et al. — Dipolo de 5.4σ

**Referência:** Böhme et al. (2025). Assimetria direcional no CMB, 5.4σ.  
**Resultado:** Quebra de isotropia estatisticamente significativa na distribuição de estruturas.

### Conexão com RLL

A extensão anisotrópica f(z,θ,φ) proposta em `teoria/EXTENSAO_ANISOTROPICA.md` é o único framework no repositório que pode endereçar diretamente esta observação. Nenhum outro modelo de transição DE↔DM disponível na literatura parametriza explicitamente o dipolo via variação direcional da transição.

**Status:** Proposta formulada, implementação numérica pendente. Este é o teste de maior impacto potencial do conjunto.

---

## 5. Tabela Comparativa Consolidada

| Observação | Convergência de ideia | Conexão quantitativa | Status |
|------------|----------------------|---------------------|--------|
| DESI DR2 — w(z) dinâmico | Alta | Requer mapeamento CPL↔RLL | ⚠️ A calcular |
| Okada PRL 2026 — DM quente→fria | Alta | Analiticamente reproduzido por f(z) | ✅ Consistente |
| Nature Comms — não-localidade | Hipotética | Sem derivação de escala | 🔍 Especulativo |
| Böhme — dipolo 5.4σ | Alta | Extensão f(z,θ,φ) em desenvolvimento | ⚠️ A implementar |

---

## 6. External validation (mapeamento quantitativo)

Esta seção conecta explicitamente a formulação do `RAFAELIA_COSMO_STRUCTURE_D/paper/draft.md` com os resultados externos, separando o que é **convergência qualitativa** do que conta como **suporte quantitativo**.

### 6.1 Mapeamento explícito CPL ↔ parametrização RLL

Para comparação no mesmo espaço de parâmetros da literatura (DESI), definimos o mapeamento local em torno de `a=1`:

\[
w_{RLL}(a) = -f(a),\quad f(a)=\frac{1}{1+\exp\left(\frac{z(a)-z_t}{w_t}\right)},\quad z(a)=a^{-1}-1
\]

\[
w_{CPL}(a)=w_0+w_a(1-a)
\]

Correspondência operacional (1ª ordem em Taylor):

- \(w_0 \equiv w_{RLL}(a=1) = -f_0\)
- \(w_a \equiv -\left.\frac{dw_{RLL}}{da}\right|_{a=1} = -\left.\frac{df}{da}\right|_{a=1}\)
- com \(\frac{df}{dz}=-\frac{f(1-f)}{w_t}\) e \(\frac{dz}{da}=-a^{-2}\), então:

\[
w_a = -\frac{f_0(1-f_0)}{w_t}
\]

Métricas comparáveis no mesmo protocolo de ajuste:

- \(\chi^2_{\min}\) total e por dataset
- \(\Delta\mathrm{AIC}\), \(\Delta\mathrm{BIC}\) vs \(\Lambda\)CDM e vs CPL livre
- tensão em parâmetros via distância em sigma (ex.: \(|w_0^{RLL\to CPL}-w_0^{DESI}|/\sigma_{w_0}\))
- PPC (posterior predictive checks) para BAO, SN e crescimento \(f\sigma_8\)

### 6.2 Critérios objetivos de rejeição (falsificação)

Um ajuste RLL é classificado como **rejeitado** se qualquer critério abaixo ocorrer:

1. **Penalização de informação:** \(\Delta\mathrm{AIC}>10\) e \(\Delta\mathrm{BIC}>10\) contra o melhor modelo concorrente no mesmo conjunto de dados.
2. **Mau ajuste absoluto:** p-valor global do \(\chi^2\) < 0.01.
3. **Discrepância paramétrica externa:** mapeamento RLL→CPL incompatível em >3σ com contornos DESI (para \(w_0,w_a\)).
4. **Resíduo sistemático observacional:** média dos resíduos normalizados por bin de redshift com viés \(|\langle r/\sigma\rangle|>2\) em dois ou mais observáveis independentes.

### 6.3 Separação metodológica: qualitativo vs quantitativo

| Nível de evidência | Definição operacional | Exemplo neste contexto |
|---|---|---|
| Convergência qualitativa | Mesma direção física/heurística sem equivalência estatística formal | “w(z) dinâmico” em DESI e transição logística em RLL |
| Suporte quantitativo | Compatibilidade numérica com incertezas + métricas de ajuste | RLL→CPL dentro de 1–2σ e \(\Delta\mathrm{AIC}\le 2\) |

Regra editorial para o paper: afirmações de prioridade/conexão devem indicar explicitamente em qual nível estão.

### 6.4 Tabela de previsões falsificáveis (observável/dataset futuro)

| Observável | Dataset futuro-alvo | Previsão RLL falsificável | Critério de falha |
|---|---|---|---|
| \(w_0,w_a\) efetivos (via mapeamento) | DESI DR3 + SN de alta-z | Região mapeada RLL→CPL sobrepõe 68% CL do ajuste conjunto | Sem sobreposição em 95% CL |
| Curvatura de \(H(z)\) em \(0.8<z<1.6\) | DESI DR3 BAO + Roman SN | Inflexão compatível com transição em torno de \(z_t\sim 1\) | Modelo requer \(z_t\) fora do intervalo 0.5–2.0 para ajustar dados |
| Crescimento \(f\sigma_8(z)\) | Euclid + DESI full-shape | Desvio sistemático controlado por \(\Omega_{s0}\) sem degradação de \(\chi^2\) global | \(\Delta\chi^2>9\) (≈3σ para 1 dof efetivo) contra \(\Lambda\)CDM/CPL |
| Dipolo anisotrópico em expansão/crescimento | SKA + CMB-S4 + catálogos all-sky | Sinal dipolar coerente com extensão \(f(z,\theta,\phi)\) e eixo estável entre probes | Eixos incompatíveis >3σ ou amplitude consistente com zero em todos os probes |

Integração no texto principal: esta seção deve ser usada como contraparte quantitativa direta da seção “External validation” em `RAFAELIA_COSMO_STRUCTURE_D/paper/draft.md`.

---

## 7. O Que Seria Necessário para Estabelecer Prioridade Formal

Prioridade científica reconhecida requer, nesta ordem:

1. **Publicação em repositório de preprints** com data verificável (arXiv — não apenas GitHub)
2. **Comparação quantitativa** com os resultados externos, não apenas convergência qualitativa
3. **Dados reais** como base do ajuste, não dados sintéticos
4. **Peer review** em periódico indexado (JCAP, Universe, PRD, PRL)

O GitHub com commits datados fornece evidência de precedência informal mas não é reconhecido como mecanismo de prioridade científica pelos principais periódicos e agências de fomento.
