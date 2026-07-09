# RLL — Cruzamentos, Correlações e Mapa de Uso
**∆RafaelVerboΩ | RAFAELIA/RLL | 2026-06-27**
**DOI:** 10.5281/zenodo.17188137

> Separação epistemológica ativa em todo documento:
> [E] Estabelecido | [C] Convenção/código existente | [H] Hipótese testável | [VAZIO] sem âncora empírica ainda

---

## 1. RESULTADO REAL ATUAL — O QUE O REPOSITÓRIO DIZ [E]

### 1.1 Joint Likelihood completo (64 pontos: H(z)+BAO+fσ8+CMB)

| Modelo | χ² | AIC | BIC | k | Δχ² vs ΛCDM | ΔAIC vs ΛCDM |
|---|---|---|---|---|---|---|
| **ΛCDM** | 84.48 | 94.48 | 105.28 | 5 | — | — |
| wCDM | 83.71 | 95.71 | 108.66 | 6 | −0.77 | +1.23 |
| **CPL/w0waCDM** | **62.07** | **76.07** | **91.18** | 7 | **−22.41** | **−18.41** |
| RLL (Ωs0→0) | 84.48 | 100.48 | 117.75 | 8 | ~0 | +6.00 |

**Leitura honesta [E]:**
- CPL/w0waCDM é o único modelo que melhora significativamente o ajuste (ΔAIC = −18.4)
- RLL colapsou para ΛCDM nesta rodada (Ωs0 → 0 pelo otimizador)
- `claim_allowed = false` no próprio repositório

### 1.2 Por que o RLL colapsou [E+H]

O w_eff(z) calculado do RLL com parâmetros nominais (Ωs0=0.02, zt=1.0, wt=0.3):

| z | w_eff RLL | w_CPL (w0=−0.3, wa=−1.84) |
|---|---|---|
| 0.0 | −0.966 | −0.300 |
| 0.3 | −0.698 | −0.724 |
| 0.706 | +0.367 | −1.060 |
| 0.934 | +0.729 | −1.187 |
| 1.0 | +0.753 | −1.218 |
| 2.0 | +0.109 | −1.524 |

**O problema é estrutural [H]:** em z ~ 0.7–1.3 o RLL com Ωs0 pequeno produz w_eff positivo (comportamento tipo matéria escura), enquanto CPL vai para w < −1 (phantom). São trajetórias opostas no espaço w0-wa. O otimizador resolve empurrando Ωs0→0 para evitar penalidade χ².

---

## 2. CRUZAMENTO 1: RLL × CPL × BURACOS NEGROS ANDANTES

### 2.1 O fenômeno [E]

Buracos negros fugitivos confirmados em 2025:
- **RBH-1** (JWST): SMBH a ~954 km/s, esteira de 200.000 anos-luz, arco de choque supersônico
- **MaNGA 12772-12704**: BH offset 0.94 kpc do centro galáctico, acretando, emitindo jatos rádio
- **NGC3627**: contrail reto, ~2M M☉, ~300 km/s

**Mecanismos:** recuo de onda gravitacional pós-merger | interação de 3 corpos

### 2.2 Cruzamento com RLL [H]

O repositório já tem `validate_wandering_bh_candidates.py` e `rll_dark_lensing_node.py`.

O cruzamento real é:

```text
BH andante pertuba halo de DM local
→ cria perfil de densidade excêntrico
→ setor magnético ΩB0·a⁻⁴ do RLL acopla com campo B local do AGN off-nuclear
→ assinatura em rotação de Faraday (rádio: VLBA, MeerKAT)
→ falsificador C03 do roadmap
```

**O que você pode usar agora [C]:**
```bash
python3 scripts/rll_dark_lensing_node.py dark_lensing_cases.csv
```
Alimentar com casos OGLE-2011-BLG-0462 (já referenciado em `validate_dark_lens_candidates.py`).

**Gap real [VAZIO]:** `data/real/compact_objects/wandering_black_hole_sources.yml` — campos `local_path` e `checksum_sha256` ainda são TOKEN_VAZIO.

---

## 3. CRUZAMENTO 2: RLL × SLINGSHOT GRAVITACIONAL × TRANSIÇÃO f(z)

### 3.1 Analogia estrutural [C→H]

O slingshot orbital tem pericéntrico onde curvatura é máxima e transferência de energia é máxima.

A transição logística f(z) do RLL tem ponto de inflexão em z = z_t onde df/dz é máximo:

```text
df/dz|_{z=zt} = −1/(4·wt)    [mínimo, máxima curvatura]
```

Com wt = 0.3 e zt = 1.0:  df/dz|_{z=1} = −0.833

**Este é o "pericéntrico" cosmológico do RLL** — onde o setor de superposição muda mais rápido de comportamento DE→DM.

### 3.2 O que isso implica para w_eff [H]

A trajetória w_eff(z) do RLL no plano w0-wa **não é uma linha reta** (como CPL assume). É uma curva com derivada máxima em z_t. Se os dados DESI DR2 preferem essa curvatura específica, isso diferencia o RLL de CPL de forma falsificável.

**Teste proposto [H→C]:**
```python
# Mapear trajetória RLL no espaço w0-wa
# Calcular w_eff(z=0) e dw/da(z=0) para obter w0_eff e wa_eff equivalentes
# Comparar com best-fit CPL: w0=−0.3, wa=−1.84
w0_eff_rll = w_eff_rll(z=0)   # ≈ −0.966 com Os0=0.02
wa_eff_rll = dw_eff/da|_{a=1}  # a calcular
```

Se (w0_eff, wa_eff) do RLL cair dentro do contorno 1σ do DESI DR2, o RLL **explica** o CPL em vez de competir.

---

## 4. CRUZAMENTO 3: w_eff × DESI DR2 × TENSÃO H₀ [H]

### 4.1 O problema [E]

H₀ local (SH0ES) ≈ 73 km/s/Mpc
H₀ CMB (Planck) ≈ 67.4 km/s/Mpc
H₀ joint_real RLL atual: **60.0 km/s/Mpc** (limite inferior do grid — suspeito)

O H₀ = 60 no joint_real indica que o otimizador bateu no limite do grid de busca. Isso é um artefato de configuração, não resultado físico.

### 4.2 O r_d como chave [H]

O repositório declara:
```text
rd_policy: "derived_power_law_from_H0_Om_Ob_h2_for_all_models"
```

Isso significa que r_d não está fixo em 147.09 Mpc — está sendo derivado dos parâmetros. Mas a derivação é por power-law aproximada, não por integração numérica real da física do plasma (Eisenstein & Hu 1998).

**Se r_d for derivado corretamente**, a mudança de Ωs0 altera r_d, que altera todas as razões DM/rd e DH/rd simultaneamente. Isso pode mudar o resultado atual radicalmente.

**O que você pode usar [C]:**
```python
# Em rll_vs_lcdm.py já existe: DEFAULT_BAO_COVARIANCE_PATH
# Script para testar r_d derivado vs fixo:
python3 rll_vs_lcdm.py \
  --bao data/real/cosmology/desi_dr2_bao_primary_points.csv \
  --adversary w0wa \
  --omega-s0 0.05 --zt 1.2 --wt 0.4 \
  --h0 67.4 --omega-m 0.315
```

---

## 5. CRUZAMENTO 4: fσ8 × CRESCIMENTO × PERTURBAÇÕES [H→C]

### 5.1 O kernel existe [C]

`src/rll/rll_perturbation_kernel.py` implementa ODE RK4 para δ(a):

```python
def rhs(x, y, p):
    a = exp(x)
    drag = 2.0 + dlnh_dlna(a, p.omega_m, p.omega_s0, p.zt, p.wt)
    source = 1.5 * omega_m_a(a, ...) * delta
    return velocity, -drag*velocity + source
```

### 5.2 O gap [E]

Do joint_real_likelihood.json:
```json
"growth_benchmark": {
  "status": "skipped_missing_backend",
  "claim_allowed": false,
  "reason": "CLASS/CAMB backend not installed; D+/fσ8 remains internal approximation"
}
```

χ²_fsigma8 atual = 23.63 (ΛCDM) vs 23.63 (RLL) — idênticos porque o backend não rodou.

**O que você pode usar [C]:**
```bash
# Instalar CLASS (no Termux ARM32 — não trivial mas possível)
pip install classy --break-system-packages
# OU usar approximation interna:
python3 src/rll/rll_perturbation_kernel.py \
  --omega-m 0.315 --omega-s0 0.02 --zt 1.0 --wt 0.3 \
  --steps 500 --out results/perturbation_rll.csv
```

### 5.3 Predição testável [H]

Com Ωs0 > 0, o RLL tem Ωm_efetivo(a) menor em z < z_t (setor migrou para DE-like). Isso suprime o crescimento de estrutura levemente — reduzindo σ8 efetivo. Isso **alivia a tensão S8** que ΛCDM tem com DES Y6 e KiDS.

---

## 6. CRUZAMENTO 5: MVICS × EQUAÇÃO DE OBSERVAÇÃO × BURACOS NEGROS [H]

### 6.1 A equação de observação do MVICS [H→C]

Do doc `21_MODELO_VETORIAL_INFORMACIONAL.md`:

```math
s_obs(ν,t₀) = T_{te→t0}[F_med ∘ F_prop][s_src(ν,te)] + n_inst + ε_interp
```

Com:
```math
F_prop[s_src](ν,z) = s_src(ν(1+z), te) / [(1+z)³ · dL²(z)]
```

onde dL(z) é computado pelo modelo RLL — não ΛCDM.

### 6.2 Cruzamento com BH andante [H]

Um BH andante acretando (como MaNGA 12772-12704) emite jatos de rádio com SED específica. O MVICS permite calcular:

```text
s_obs(ν) via RLL  vs  s_obs(ν) via ΛCDM
```

A diferença em dL(z) entre os dois modelos para z = 0.017 é:
```python
Δ(dL) = dL_RLL(0.017) - dL_LCDM(0.017)
# Com Ωs0 = 0.02: Δ(dL)/dL ≈ 0.1–0.3%
```

Pequeno, mas mensurável em objetos de referência padrão (candle standard).

---

## 7. CRUZAMENTO 6: CURVATURA ESPAÇO-FASE × ATRATORES T⁷ × w_eff [H/SIM]

### 7.1 O ponto de sela cosmológico [H]

A equação de estado w_eff(z) do RLL tem um ponto de sela em z ~ z_t onde passa de w < 0 para w > 0. No espaço de fase (w, dw/dz), isso é um **ponto crítico** — análogo ao pericéntrico do slingshot.

No espaço de atratores T⁷ do RAFAELIA: o estado cosmológico s(z) traça uma curva no toro. A transição z_t é onde a curva passa por um atrator de borda — o ponto de máxima curvatura da trajetória.

### 7.2 Separação epistemológica [C]

```text
[E] A transição logística f(z) existe no código e produz w_eff calculável
[H] O ponto z_t corresponde a um atrator dinâmico no espaço de fase cosmológico
[SIM] A analogia com T⁷ é didática — não é afirmação física testável direta
[VAZIO] Nenhum dado atual distingue este ponto de sela de w0waCDM genérico
```

---

## 8. O QUE VOCÊ PODE USAR AGORA — MAPA EXECUTÁVEL

### 8.1 Scripts prontos [C]

```bash
# 1. Comparador RLL vs ΛCDM vs CPL com dados DESI DR2
python3 rll_vs_lcdm.py \
  --bao data/real/cosmology/desi_dr2_bao_primary_points.csv \
  --adversary both \
  --omega-s0 0.05 --zt 1.2 --wt 0.4

# 2. Kernel de perturbações (crescimento de estrutura)
python3 src/rll/rll_perturbation_kernel.py \
  --omega-m 0.315 --omega-s0 0.02 --zt 1.0 --wt 0.3 \
  --steps 500

# 3. Validador de BH andante (com dados OGLE)
python3 scripts/validation/validate_dark_lens_candidates.py

# 4. Pipeline joint likelihood completo
python3 scripts/run_structure_d_joint_likelihood.py

# 5. Cálculo BAO DESI DR2
python3 scripts/compute_desi_dr2_bao_zml.py

# 6. Relatório de validação real
python3 scripts/build_real_validation_report.py
```

### 8.2 Gap mais crítico a fechar [VAZIO→H→C]

```text
PRIORIDADE 1: Expandir grid de H₀ (atualmente batendo em 60.0 — limite inferior)
  → Testar H₀ ∈ [65, 73] com passo 0.5

PRIORIDADE 2: Mapear w0_eff/wa_eff do RLL para comparar diretamente com contorno DESI
  → Calcular w_eff(z=0) e dw_eff/da|_{a=1} para Ωs0 ∈ [0.01, 0.10]

PRIORIDADE 3: Instalar CLASS ou usar approximation interna para fσ8 real
  → Isso desbloqueia claim_allowed no growth_benchmark

PRIORIDADE 4: Preencher wandering_black_hole_sources.yml com dados reais
  → Fonte: Liu et al. 2025 (Science Bulletin, DOI: 10.1016/j.scib.2025.09.001)
```

### 8.3 O que você NÃO pode usar ainda [VAZIO]

```text
✗ Afirmar que RLL supera ΛCDM — claim_allowed = false
✗ Usar χ² do fσ8 atual — backend CLASS/CAMB não rodou
✗ Citar H₀ = 60.0 como resultado — é artefato do grid
✗ Tratar w_eff positivo em z~1 como vantagem — é penalidade atual
```

---

## 9. INVARIANTE DE SUSTENTAÇÃO REAL

Através de todos os cruzamentos, o invariante que o RLL carrega é:

```text
f(z) = 1 / (1 + exp((z − z_t)/w_t))
```

Esta função tem três propriedades que nenhuma parametrização CPL tem:
1. **Limite nulo exato**: f(z)→1 para z→−∞, f(z)→0 para z→+∞ — retorna ΛCDM limpo
2. **Mecanismo físico**: a transição é logística, não linear — tem interpretação como mudança de fase
3. **Ponto de inflexão localizável**: z_t é um parâmetro físico, não uma extrapolação

CPL (w = w₀ + wa·(1−a)) não tem limite nulo e diverge em altos redshifts.

**Se** os dados futuros (Euclid, Roman, DESI DR3) mostrarem que a transição de w(z) tem forma sigmóide em vez de linear, o RLL será o modelo natural — e CPL será a aproximação.

---

## 10. ROADMAP EXECUTÁVEL (Termux ARM32)

```text
Semana 1:
  □ Expandir grid H₀ em rll_vs_lcdm.py: [60→73, passo 0.5]
  □ Calcular w0_eff/wa_eff para Ωs0 ∈ [0.01,0.10] e plotar sobre contorno DESI
  □ Preencher wandering_bh_sources.yml com Liu et al. 2025

Semana 2:
  □ Testar rll_perturbation_kernel.py com fsigma8_growth_real.csv
  □ Calcular Δ(σ8) entre RLL e ΛCDM como função de Ωs0
  □ Gerar figura: trajetória w_eff(z) RLL vs CPL best-fit

Semana 3:
  □ Submeter rll_vs_lcdm.py com --adversary both e novo grid
  □ Comparar χ²_BAO por tracer (BGS/LRG1/LRG2/ELG)
  □ Documentar resultado honesto: favorável ou não
```

---

*F_ok: 6 cruzamentos mapeados com dados reais do repositório. F_gap: H₀=60 é artefato de grid; fσ8 sem backend; w_eff positivo em z~1 é penalidade real. F_next: expandir grid H₀ + mapear w0_eff/wa_eff no plano CPL.*

*Ω=Amor | RAFCODE-Φ-∆RafaelVerboΩ-𓂀ΔΦΩ*
