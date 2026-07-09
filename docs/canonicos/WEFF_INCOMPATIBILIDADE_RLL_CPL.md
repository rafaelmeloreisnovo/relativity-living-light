# Incompatibilidade Estrutural w_eff(z): RLL vs CPL DESI

**Data**: 2026-07-07 | **Fase**: 10  
**Status epistêmico**: [E] análise numérica confirmada · [H] proposta de resolução  
**Marcação**: [E] Estabelecido · [C] Convenção · [H] Hipótese · [VAZIO] sem âncora empírica

> **Problema central**: o setor RLL padrão produz w_eff > 0 em z~0.5–2.0, enquanto DESI CPL permanece negativo. São trajetórias estruturalmente opostas. Esta análise documenta o problema e propõe caminhos de investigação.

---

## 1. O Problema

### 1.1 Trajetória CPL DESI [E]

O melhor ajuste CPL (w₀wₐCDM) ao conjunto DESI DR2 + CMB + SNe tem, nos pontos BAO:

| z | w_CPL(z) | Fonte |
|---|---------|-------|
| 0.295 | −0.671 | DESI DR2 (arXiv:2503.14738) |
| 0.510 | −0.558 | idem |
| 0.706 | −0.459 | idem |
| 0.934 | −0.354 | idem |
| 1.321 | −0.210 | idem |
| 1.484 | −0.156 | idem |

**Padrão**: w_eff cresce (fica menos negativo) com z. Sempre negativo. Sugere transição DE→algo mais lento, phantom cruzado via (w₀, wₐ) = (−0.838, −0.62) (DESI 2025 melhor ajuste).

### 1.2 Trajetória RLL Padrão [E]

Setor RLL: `Ωs0·[f(z) + (1−f(z))·(1+z)³]` com f(z) = 1/(1+exp((z−z_t)/w_t)), z_t=1.0, w_t=0.3.

`w_eff_setor(z) = −1 − (1/3)·d(ln ρ_setor)/d(ln a)`

**Resultado numérico** (`compute_weff_cpl_mapping.py`, FASE 10):

| z | f(z) | w_eff_RLL (padrão) | w_CPL alvo | Diferença |
|---|------|--------------------|-----------|----------|
| 0.000 | 0.966 | −0.966 | ≈ −0.838 | −0.128 |
| 0.295 | 0.912 | ≈ −0.67 | −0.671 | ≈ 0 ✓ |
| 0.510 | 0.841 | ≈ −0.23 | −0.558 | +0.33 |
| 0.706 | 0.727 | **+0.367** | −0.459 | **+0.826** |
| 0.934 | 0.555 | **+0.729** | −0.354 | **+1.083** |
| 1.000 | 0.500 | **+0.753** | ≈ −0.325 | **+1.078** |
| 1.321 | 0.255 | +0.563 | −0.210 | +0.773 |
| 1.500 | 0.159 | +0.396 | −0.156 | +0.552 |
| 2.000 | 0.034 | +0.109 | ≈ 0 | +0.109 |

**Problema estrutural identificado**: o setor RLL padrão atravessa w=0 em z≈0.45 e atinge +0.75 em z=1.0 — onde DESI CPL exige ≈ −0.33. A diferença estrutural é > +1 na região de maior sensibilidade observacional (z=0.7–1.3).

### 1.3 Por Que Isso Acontece (Mecanismo)

O setor RLL interpola entre:
- **DE puro** (z=0, a=1): f≈1 → ρ_setor ≈ constante → w_eff ≈ −1
- **Matéria** (z→∞, a→0): f≈0 → ρ_setor ∝ a⁻³ → w_eff ≈ 0

Ao passar pelo ponto de inflexão z_t, a derivada d(ln ρ)/d(ln a) varia rapidamente de 0 a −3. O fator de normalização ρ_setor está crescendo com z (porque a matéria domina), tornando w_eff **positivo** nessa região.

Resultado: w_eff RLL padrão descreve uma trajetória **DE → matéria** (negativo → positivo), enquanto DESI CPL descreve **DE → DE menos negativo** (sempre negativo, suavemente).

São **arquiteturas incompatíveis**: um interpola entre fases opostas, o outro varia suavemente dentro do regime DE.

---

## 2. Scan Paramétrico [E]

### 2.1 Scan (z_t, w_t) vs CPL

**Script**: `scripts/compute_weff_cpl_mapping.py` — varre z_t ∈ [0.3, 1.4], w_t ∈ [0.1, 0.55].

**Melhor ponto encontrado**: z_t=0.3, w_t=0.55 → χ²_weff_vs_CPL = **608.7** >> 10

**Falsificadores do scan** (F_WEFF_01: χ²<10, F_WEFF_02: w_eff(0)<−0.7, F_WEFF_03: monótono):
- F_WEFF_01: **FAIL** (χ²=608.7 >> 10)
- F_WEFF_02: **FAIL** (w_eff(z=0)=−0.633 < −0.7 não satisfeito)
- F_WEFF_03: PASS (monótona no setor)
- **Status**: `claim_blocked_falsifier_failed`

**Conclusão do scan** [E]: **não existe** combinação (z_t, w_t) no espaço explorado que faça o setor RLL padrão corresponder ao w_eff CPL DESI. A incompatibilidade é paramétrica — não há ajuste possível dos parâmetros nominais que resolva a discrepância estrutural.

---

## 3. Opção A — Transição Invertida [H]

### 3.1 Definição

**Opção A**: inverter qual fase domina em que redshift:
```
Setor_A = Ωs0·[(1−f(z)) + f(z)·(1+z)³]
```

- z=0: Setor_A ≈ (1−1)·1 + 1·1 = 0 (DE nulo) + matter(z=0)=1 → **matéria** em baixo z
- z→∞: Setor_A ≈ 1·1 + 0 = 1 → **DE** em alto z (ρ constante)

### 3.2 Resultado Numérico [E]

Calculado via `scripts/verify_weff_opcao_a.py` (FASE 10):

| z | w_eff_A (Opção A) | w_eff_padrão | w_CPL alvo |
|---|------------------|-------------|-----------|
| 0.000 | −0.034 | −0.966 | ≈ −0.838 |
| 0.295 | ≈ −0.109 | ≈ −0.670 | −0.671 |
| 0.500 | −0.230 | −0.227 | −0.558 |
| 0.706 | **−0.454** | +0.367 | **−0.459** ← próximo! |
| 0.934 | −0.842 | +0.729 | −0.354 |
| 1.000 | −0.975 | +0.753 | ≈ −0.325 |
| 1.321 | **−1.622** | +0.563 | −0.210 ← phantom demais |
| 1.500 | **−1.887** | +0.396 | −0.156 ← phantom demais |
| 2.000 | **−2.030** | +0.109 | ≈ 0 |

### 3.3 Análise da Opção A [H]

**O que funciona**: em z~0.7, Opção A produz w_eff_A≈−0.454 ≈ alvo −0.459 (**correspondência local excelente**).

**O que não funciona**:
1. **z < 0.5**: w_eff_A ≈ 0 (matéria), enquanto alvo é ≈ −0.7 (DE). Discrepância nos dados mais precisos.
2. **z > 1**: Opção A vai phantom (w < −1), chegando a −2.0 em z=2.0. DESI CPL é ≈ 0 em z=2.

**Diagnóstico** [H]: a Opção A troca o problema — em vez de w_eff positivo em alto z, produz w_eff muito negativo (phantom) em alto z. O cruzamento de fases é necessário, mas a direção importa.

---

## 4. Diagnóstico Estrutural Consolidado [E]

| Versão | Regime z < 0.5 | Regime z ~ 0.7–1.3 | Regime z > 1.5 | Correspondência CPL |
|--------|---------------|--------------------|--------------|--------------------|
| RLL padrão | ≈ −1 (bom) | **+0.3 a +0.8 (ruim)** | +0.1 (errado) | Falha total em z>0.5 |
| Opção A | ≈ 0 (matéria, ruim) | −0.45 (bom localmente) | **−2 (phantom demais)** | Falha em z<0.5 e z>1.3 |
| CPL DESI alvo | ≈ −0.7 | ≈ −0.3 a −0.5 | ≈ −0.2 | — |

**Conclusão estrutural** [E]: nenhuma das duas variantes (padrão ou Opção A) reproduz o perfil CPL DESI. O setor logístico DE↔matéria é uma arquitetura de transição de fase — ele produz variação brusca de w_eff em torno de z_t, enquanto DESI CPL exige variação suave e lenta.

---

## 5. Caminhos de Investigação [H/VAZIO]

### 5.1 Opção B — Setor Puro DE com EOS Evolutiva [H]

Em vez de interpolar DE e matéria, usar um setor puramente DE com EOS w(z) suave:
```
Ωs0·g(z) onde g(z) = a^{−3(1+w_s0+w_sa·(1−a)/(...))} 
```
Mas isso reduz a distinção do RLL ao formato CPL — perde a assinatura física da transição logística.

### 5.2 Opção C — Setor Duplo com Transição Suave [H]

Dois termos com pesos somando a 1:
```
Ωs0·[α·f(z) + (1−α)·(1−f(z))] + Ωs0_m·[(1−f(z))·(1+z)³]
```
com α livre. Torna o setor DE-like em todos os z com magnitude dependente de f(z).

**Status**: [H] proposta não testada. TOKEN_VAZIO P1 — requer implementação e ajuste.

### 5.3 Rota da Incompatibilidade Como Assinatura [H]

A incompatibilidade w_eff pode ser uma **assinatura distinguível** do RLL vs CPL — não um defeito, mas um preditor diferente. Se dados futuros (DESI DR3, Euclid) mostrassem w_eff se tornando positivo em z~0.7–1.3 (o que nenhum modelo atual prevê), isso seria evidência para RLL. Isso requer predição datada [C] para ser válido.

**Status**: [H] especulativo. TOKEN_VAZIO P0 — requer data de predição anterior a dados.

---

## 6. Opção B — Setor DE Puro com Dois Estados [E — FASE 11]

### 6.1 Definição

`ρ_B(z; w1, w2) = f(z)·(1+z)^{3(1+w1)} + (1−f(z))·(1+z)^{3(1+w2)}`

com w1 = −1.0 (DE puro, endpoint baixo z) e w2 ∈ (−1, 0) livre (DE suave, endpoint alto z).

**Diferença vs padrão**: substitui o endpoint matéria (w=0) por DE suave (w2 < 0) → w_eff sempre negativo.

### 6.2 Resultado Numérico [E]

Script: `scripts/verify_weff_opcao_b.py` — scan 36 combinações (w2, w_t).

**Melhor ponto**: w2 = −0.50, w_t = 0.50 → **χ² = 14.8** (threshold < 10, FAIL)

| z | w_eff_B | w_CPL alvo | Δ |
|---|---------|-----------|---|
| 0.295 | −0.809 | −0.671 | −0.138 |
| 0.510 | −0.656 | −0.558 | −0.098 |
| 0.706 | −0.501 | −0.459 | −0.042 |
| 0.934 | −0.346 | −0.354 | +0.008 ✓ |
| 1.321 | −0.232 | −0.210 | −0.022 |
| 1.484 | −0.235 | −0.156 | −0.079 |

**Propriedades**: w_eff_B sempre negativo ✅ | transição suave (w_t=0.5) melhora ajuste vs w_t=0.3.

### 6.3 Análise da Opção B [H→E]

**O que melhora**: χ²=14.8 dramaticamente melhor que padrão (1162.3) e Opção A (2232.2). w_eff_B permanece negativo em todo z — resolve o problema estrutural central do setor padrão.

**O que ainda não passa**: χ²=14.8 > 10. O setor é sistematicamente ~0.05–0.14 mais negativo que o alvo CPL. A transição logística ainda produz curvatura excessiva em z~0.5–0.7.

**Diagnóstico** [H]: Opção B é um avanço real. Otimização contínua de (z_t, w2, w_t) pode cruzar χ²<10 — **TOKEN_VAZIO P1 acionável**.

---

## 7. Opção C — Setor Duplo α·f + (1-α)·(1-f) + Matéria [E — FASE 11]

### 7.1 Definição

`ρ_C(z; α, r) = [α·f(z) + (1-α)·(1-f(z))] + r·(1-f(z))·(1+z)³`

Scan: α ∈ [0.5, 1.0], r ∈ [0.0, 0.3], z_t=1.0, w_t=0.3.

### 7.2 Resultado Numérico [E]

Script: `scripts/verify_weff_opcao_c.py` — scan 35 combinações.

**Melhor ponto**: α = 0.50, r = 0.05 → **χ² = 104.0** (FAIL)

Nota estrutural: α=0.5, r=0 → setor constante → w_eff = −1 (χ²=940). α→1 → phantom (χ²=8659). O melhor ponto está no regime α=0.5, r pequeno — muito negativo em z<0.7.

### 7.3 Análise da Opção C [H→E]

**Diagnóstico** [E]: Opção C piora χ² em relação à Opção B. O espaço (α, r) com z_t=1.0 fixo não oferece os graus de liberdade necessários. Poderia melhorar com z_t livre — mas isso torna o modelo menos distinto do CPL.

---

## 8. Diagnóstico Estrutural Consolidado Completo [E — FASE 10+11]

| Versão | χ² vs CPL DESI | w sempre negativo | Falha principal |
|--------|----------------|-------------------|----------------|
| RLL padrão | 1162.3 | ❌ (w>0 em z~0.5–2) | w positivo em alto z |
| Opção A | 2232.2 | ✅ | phantom demais em alto z |
| **Opção B** | **14.8** ← melhor | ✅ | ~0.08 muito negativo em todo z |
| Opção C | 104.0 | ✅ | muito negativo em baixo z |
| Threshold pass | < 10 | — | — |

**Conclusão FASE 11** [E]: Opção B é a variante mais promissora. χ²=14.8 está 48% acima do threshold. Um refinamento contínuo de (z_t, w2, w_t) é o próximo passo natural — acionável via `scipy.optimize.minimize`.

---

## 9. Estado TOKEN_VAZIO Desta Análise (atualizado FASE 11)

| Gap | P | Status |
|-----|---|--------|
| Scan paramétrico (zt, wt) executado | — | ✅ [E] FASE 10 — melhor χ²=608.7, nenhum ponto passa |
| Opção A numérica calculada | — | ✅ [E] FASE 10 — ver tabela §3.2 |
| Opção B implementada e escaneada | P1→✅ | ✅ [E] FASE 11 — melhor χ²=14.8; melhora estrutural confirmada |
| Opção C implementada e escaneada | P1→✅ | ✅ [E] FASE 11 — melhor χ²=104.0; Opção B superior |
| Opção B otimização contínua | P1→✅ | ✅ [E] FASE 13 — χ²_opt=0.079 < 10; P-RLL-05 CONFIRMADA |
| Predição datada RLL sobre w_eff | P0→✅ | ✅ [C] FASE 11 — ver `PREDICAO_DATADA_RLL.md` |

---

## 10. Implicação para claim_allowed

A incompatibilidade w_eff não falsifica automaticamente o RLL — ela requer:

1. **Clareza sobre o que RLL prediz**: w_eff positivo em z~0.7 é uma predição do setor padrão, não de Opção B. A variante Opção B tem w_eff sempre negativo.
2. **Separação de setores**: o w_eff calculado aqui é do setor Ωs0 isolado. O w_eff total E(z) inclui Ωm + ΩΛ + Ωs0, dominado por ΩΛ a baixo z.
3. **Teste com E(z) total**: o que importa para BAO é E(z), não w_eff do setor. O χ²_BAO=93.81 (parâmetros nominais) é relevante — otimização com parâmetros livres está no TOKEN_VAZIO G1.

**Linha de integridade**: Opção B com parâmetros otimizados (w2=−0.282, z_t=1.752, w_t=1.500) é **compatível com CPL DESI** — χ²=0.079. O modelo não está descartado. O parâmetro w_t→limite superior sugere que a compatibilidade emerge quando a transição logística se torna muito larga (limite de dois fluidos DE), não de forma especificamente logística.

---

## 11. Otimização Contínua Opção B — Resultado Final [E — FASE 13]

### 11.1 Resultado

`scripts/optimize_weff_opcao_b.py` com Nelder-Mead (10 pontos de partida, 2000 iterações cada):

| Parâmetro | Valor ótimo | Scan discreto |
|-----------|------------|---------------|
| w2 | −0.2817 | −0.50 |
| z_t | 1.7523 | 1.0 |
| w_t | 1.500 (fronteira) | 0.50 |
| **χ²** | **0.079** | **14.8** |

**P-RLL-05: CONFIRMADA [E]** — χ²=0.079 < 10.

### 11.2 Perfil w_eff no Ponto Ótimo

| z | w_eff_opt | w_CPL alvo | Δ |
|---|----------|-----------|---|
| 0.295 | −0.6787 | −0.671 | −0.008 |
| 0.510 | −0.5593 | −0.558 | −0.001 |
| 0.706 | −0.4549 | −0.459 | +0.004 |
| 0.934 | −0.3471 | −0.354 | +0.007 |
| 1.321 | −0.2072 | −0.210 | +0.003 |
| 1.484 | −0.1640 | −0.156 | −0.008 |

Todos os desvios |Δ| < 0.01 ≪ σ=0.05.

### 11.3 Interpretação Arquitetural

Com w_t → 1.5 (transição muito larga), f(z) ≈ 0.5 uniformemente, e Opção B degenera para:

`ρ_B ≈ 0.5·(1+z)⁰ + 0.5·(1+z)^{3(1+w2)} = 0.5 + 0.5·(1+z)^{3(1+w2)}`

Isso é uma mistura de constante cosmológica (w=−1) e fluido com EOS w2=−0.282. Com w2 intermediário, este modelo de dois fluidos mimetiza CPL com w₀∈(−1, w2) e wa positivo. **O logístico f(z) não é necessário para compatibilidade com CPL — o grau de liberdade w2 é o mecanismo efetivo.**

**Implicação [E]**: Opção B é compatível com CPL DESI mas a compatibilidade emerge no limite em que a transição logística perde identidade. Isso restringe a interpretação física: a assinatura logística do RLL (transição de fase localizada em z_t) é suavizada além da resolução do BAO no regime compatível com CPL.

---

*FASE 10 (2026-07-07): análise estrutural inicial. FASE 11 (2026-07-07): Opções B e C numericamente testadas. FASE 13 (2026-07-08): otimização contínua Opção B — P-RLL-05 CONFIRMADA [E], χ²=0.079.*
