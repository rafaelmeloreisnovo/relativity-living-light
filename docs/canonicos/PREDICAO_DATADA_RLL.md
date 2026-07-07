# Predições Datadas do Modelo RLL

**Data de registro**: 2026-07-07 | **Fase**: FASE 11  
**Status epistêmico**: [C] predições registradas antes de dados futuros mencionados  
**Marcação**: [E] Estabelecido · [C] Convenção · [H] Hipótese · [VAZIO] sem âncora empírica

> **Propósito**: Para que uma hipótese científica seja falsificável, suas predições devem ser
> registradas com data *anterior* aos dados que as testariam. Este documento cumpre essa função
> para o modelo RLL. Conhecimento de corte usado: DESI DR2 (arXiv:2503.14738, dados publicados
> 2025), Pantheon+SH0ES (arXiv:2202.04077). Dados de Euclid, DESI DR3, e Rubin/LSST ainda
> não publicados na data de registro.

---

## P-RLL-01: Cruzamento w_eff = 0 do Setor em z ≈ 0.5 [H — disfavorecida por DR2]

**Predição** (setor padrão): Se o setor RLL padrão descreve o universo, observações de
w_eff do componente de energia escura deverão mostrar **cruzamento w=0 em z ≈ 0.5**,
seguido de w_eff **positivo (w > 0) em z ∈ (0.5, 1.5)** — assinatura única, sem equivalente
em ΛCDM, w0waCDM, ou k-essência.

**Contexto**: O setor RLL padrão interpola entre DE (w=−1) e matéria (w=0), com transição em
z_t ≈ 1.0. O w_eff do setor cruza zero em z ≈ 0.45 (calculado numericamente em FASE 10).

**Dados que testariam** [VAZIO P0]:
- DESI DR3 (~2027): w(z) via BAO em z = 0.3–1.5 com σ_w < 0.05
- Euclid DR1 (~2026–2027): weak lensing + BAO com cobertura a z~1.5
- LSST/Rubin (~2027+): SNe Ia a z > 1, sensível a evolução de w_eff

**Status perante DESI DR2** [E]: CPL best-fit (w0=-0.838, wa=-0.62) mantém w(z) sempre
negativo até z=2. Isso **contradiz P-RLL-01** com dados atuais. Porém:
- A contradição é do w_eff do *setor isolado* vs. CPL global
- O χ²_BAO=93.81 com parâmetros nominais mostra que o E(z) total pode ser compatível
- Setor com Ωs0 pequeno (~2%) tem impacto reduzido no w_eff total

**Condição de falsificação** [C]: Se DESI DR3 confirmar w(z) < 0 em todo z ∈ (0.3, 1.5)
com precisão σ_w < 0.05 *e* o melhor ajuste RLL exigir w_eff > 0 no mesmo intervalo,
então P-RLL-01 é FALSIFICADA em nível >3σ.

**Condição de suporte** [H]: Se futuros dados mostrarem w(z) > 0 em z ≈ 0.7–1.3
(sem precedente em modelos atuais), P-RLL-01 seria **fortemente corroborada**.

**Valor epistêmico**: P-RLL-01 é a predição mais distinguível do RLL — nenhum outro modelo
padrão prediz w_eff positivo na era de dominância de energia escura.

---

## P-RLL-02: Transição de Fase em z_t ≈ 1.0 [H — aguarda MCMC]

**Predição**: O modelo RLL prevê uma transição de fase do setor de energia escura centrada em
z_t ≈ 1.0, com largura de transição Δz ≈ 3·w_t ≈ 0.9 (z de 0.1 a 1.9).

**Assinatura observacional esperada**: inflexão na taxa de variação de E(z) = H(z)/H₀ em
z ≈ 1.0 — mais pronunciada que ΛCDM, onde E(z) é monotônica suave.

**Dados que testariam**:
- Moresco 2023 H(z): 33 pontos via cronômetros cósmicos, sensível à curvatura de H(z)
- DESI BAO: sensibilidade à curvatura de D_H(z) = c/(H(z)·r_d) em z~0.5–1.5
- SKA (~2028+): H(z) via HI absorção, z = 0–3

**Status atual** [C]: z_t = 1.0 é parâmetro livre sem derivação de primeiros princípios
(TOKEN_VAZIO P1). Scan Pantheon+ sugeriu valores menores — aguarda MCMC joint (TOKEN_VAZIO G1).

**Condição de falsificação** [C]: Se MCMC joint com Pantheon+ + DESI excluir z_t ∈ (0.5, 1.5)
em 2σ, então P-RLL-02 é testada — mas depende de G1 (pipeline manual pendente).

**Condição de suporte** [H]: z_t melhor ajuste cair em (0.8, 1.2) com σ_{z_t} < 0.2.

---

## P-RLL-03: Ωs0 como Perturbação Sub-dominante [H — aguarda MCMC]

**Predição**: O setor RLL contribui com fração pequena Ωs0 ≲ 0.05 da densidade crítica hoje,
atuando como perturbação sobre a base ΛCDM. Isso implica:
- χ²_BAO_RLL ≈ χ²_BAO_ΛCDM ± 5 (setor pequeno → impacto limitado no BAO)
- Assinatura detectável apenas via análise residual de E(z) ou w(z) do setor

**Status atual** [C]: Ωs0 = 0.02–0.05 por convenção (TOKEN_VAZIO P1). χ²_BAO_nominal=93.81
vs. χ²_ΛCDM_esperado ~100–150 — consistente com Ωs0 pequeno mas não conclusivo.

**Condição de falsificação**: MCMC joint (G1) com limite superior Ωs0 < 0.01 ou > 0.15.

---

## P-RLL-04: Degeneração Padrão/Opção A em Dados de Distância [E — VERIFICADA FASE 4]

**Predição original** [H]: Os setores f(z) e (1−f(z)) devem ser degenerados em dados de
distância luminosa, pois ambos têm ρ_setor(0) = 1 e diferem apenas na trajetória.

**Status**: **VERIFICADO** [E] em FASE 4 (Pantheon+SH0ES, 1701 SNe):
- χ²_RLL_original = χ²_RLL_optionA = 710.613 (idênticos ao 4º decimal)
- Ratio = 1.0000 exato
- Conclusão: degeneração f ↔ (1−f) confirmada em dados de distância [E]

**Implicação**: Para distinguir padrão de Opção A, precisam-se dados sensíveis ao *sinal*
de w_eff, não apenas à magnitude de D_L(z). Dados de crescimento de estrutura (σ8(z)) seriam
sensíveis à diferença.

---

## P-RLL-05: Opção B Cruzará χ²<10 com Otimização Contínua [H — predição testável]

**Predição**: A Opção B (setor DE puro, w1=−1, w2 livre) com otimização contínua de
(z_t, w2, w_t) atingirá χ²_DESI < 10, demonstrando compatibilidade estrutural com CPL.

**Evidência atual** [E]: Scan discreto (FASE 11) encontrou melhor χ²=14.8 (w2=−0.5, w_t=0.5).
O gradiente positivo sugere que otimização no entorno desse ponto pode cruzar o threshold.

**Como testar**: `scipy.optimize.minimize(chi2_opcao_b, x0=[1.0, -0.5, 0.5], method='Nelder-Mead')`

**Condição de falsificação**: Se χ² ótimo continuar > 10 após otimização completa,
confirma incompatibilidade estrutural mesmo da Opção B.

**Condição de suporte**: Se χ² < 10 é atingido, Opção B é **compatível com CPL DESI** —
resultado positivo relevante para o modelo.

---

## Sumário de Predições Registradas em 2026-07-07

| ID | Predição central | Dados necessários | Status atual | Prioridade |
|----|-----------------|-------------------|-------------|-----------|
| P-RLL-01 | w_eff > 0 em z~0.7–1.3 (padrão) | DESI DR3, Euclid | ⚠️ disfavorecida por DR2 | P0 |
| P-RLL-02 | Inflexão E(z) em z~1.0 | MCMC joint (G1) | ⏳ aguarda G1 | P0 |
| P-RLL-03 | Ωs0 < 0.05 | MCMC joint (G1) | ⏳ aguarda G1 | P1 |
| P-RLL-04 | Degeneração padrão/Opção A | Pantheon+ [E] | ✅ confirmado | — |
| P-RLL-05 | Opção B cruzará χ²<10 (otimização) | scipy.minimize local | ⏳ pendente | P1 |

---

## Nota sobre Validade Epistemológica

Para que uma predição seja cientificamente válida, deve ser registrada **antes** dos dados.

- P-RLL-01/02/03/05: registradas em 2026-07-07, após DESI DR2 mas **antes** de DESI DR3 e Euclid DR1
- P-RLL-04: retroativa (verificada, não predita) — conta como verificação [E], não predição
- P-RLL-01 já testada *parcialmente* por DESI DR2: resultado desfavorável documentado honestamente

A predição P-RLL-01 tem valor epistemológico especial: é **distinta de qualquer outro modelo**
cosmológico padrão. Se confirmada por dados futuros, seria evidência extraordinária para o RLL.

---

*Documento criado em FASE 11 (2026-07-07). Predições registradas antes de dados de DESI DR3 e Euclid.*
*Referências cruzadas: `WEFF_INCOMPATIBILIDADE_RLL_CPL.md`, `08_ARVORE_CONCEITUAL_RLL.md`, `CONTRATO_FALSIFICADORES_RLL.md`.*
