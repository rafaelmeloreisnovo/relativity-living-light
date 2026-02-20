# Comparação com Literatura Acadêmica 2025–2026
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

## 6. O Que Seria Necessário para Estabelecer Prioridade Formal

Prioridade científica reconhecida requer, nesta ordem:

1. **Publicação em repositório de preprints** com data verificável (arXiv — não apenas GitHub)
2. **Comparação quantitativa** com os resultados externos, não apenas convergência qualitativa
3. **Dados reais** como base do ajuste, não dados sintéticos
4. **Peer review** em periódico indexado (JCAP, Universe, PRD, PRL)

O GitHub com commits datados fornece evidência de precedência informal mas não é reconhecido como mecanismo de prioridade científica pelos principais periódicos e agências de fomento.
