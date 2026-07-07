# 09 — Pantheon+SH0ES: Resultado Real contra o Modelo RLL

**Classificação epistêmica**: [E] Evidência direta — cálculo executado contra dado observacional real  
**Gap fechado**: G0 (Pantheon+ ausente do pipeline RLL)  
**Data de execução**: 2026-07-06  
**Branch de integração**: `claude/rll-cronologia-auditoria-qyvn83`

---

## 1. Dataset

**Pantheon+SH0ES** — lançamento público oficial: `PantheonPlusSH0ES/DataRelease` (GitHub)

| Campo | Valor |
|-------|-------|
| Arquivo | `validacao_real/data/pantheon_data.dat` |
| Total SNe | 1701 |
| Calibradores Cepheid excluídos (`IS_CALIBRATOR==1`) | 77 |
| **Amostra cosmológica** | **1624** |
| Colunas usadas | `zHD` (col 3), `MU_SH0ES` (col 11), `MU_SH0ES_ERR_DIAG` (col 12), `IS_CALIBRATOR` (col 14) |
| Referência | arXiv:2202.04077 (Brout et al. 2022) |

**Regra SH0ES**: os 77 calibradores Cepheid servem para ancorar H₀ via escada de distâncias; são excluídos do fit cosmológico z-μ puro para evitar circularidade.

---

## 2. Metodologia

### 2.1 Modelos Testados

| Modelo | Parâmetros livres | k |
|--------|-----------------|---|
| ΛCDM | H₀, Ωm | 2 |
| CPL / w0waCDM | H₀, Ωm, w₀, wₐ | 4 |
| RLL original | H₀, Ωm, w₀, wₐ | 4 |
| RLL Opção A | H₀, Ωm, w₀, wₐ | 4 |

### 2.2 Função de Transição

**RLL original**: `f(z) = 1 / (1 + exp(-sharpness × (z − z_t)))`  
com `z_t = 0.5`, `sharpness = 5.0` (fixos)

**RLL Opção A**: `g(z) = 1 − f(z)` (transição invertida)

### 2.3 Distância de Luminosidade

Integração trapezoidal cumulativa vetorizada sobre grade `z ∈ [0, 3]` (4000 pontos):
```
d_L(z) = (c/H₀) × (1+z) × ∫₀ᶻ dz'/E(z')
μ_th(z) = 5 log₁₀(d_L) + 25
```

### 2.4 Fit

Otimizador: **Nelder-Mead** (scipy.optimize.minimize)  
Tolerâncias: `xatol=1e-6`, `fatol=1e-6`, `maxiter=5000`

### 2.5 Scripts

```
scripts/pantheon/load_pantheon.py       — loader do dataset
scripts/pantheon/models_pantheon.py     — E(z), dL, chi2, fit_model
scripts/pantheon/run_rll_vs_pantheon.py — pipeline principal (4 fits)
```

Cópias originais do usuário: `validacao_real/data/`

---

## 3. Resultado [E]

### Tabela Principal

| Modelo | H₀ | Ωm | w₀ | wₐ | χ² | χ²/dof | AIC |
|--------|-----|-----|-----|-----|-----|--------|-----|
| ΛCDM | 73.064 | 0.3460 | − | − | 710.808 | 0.4382 | 714.808 |
| CPL | 73.018 | 0.1401 | −0.7572 | +0.7036 | 710.390 | 0.4385 | 718.390 |
| RLL original | 72.970 | 0.2989 | −0.9037 | +0.0729 | 710.613 | 0.4387 | 718.613 |
| RLL Opção A | 72.970 | 0.2989 | −0.8307 | −0.0729 | 710.613 | 0.4387 | 718.613 |

**Razão χ²(RLL original) / χ²(RLL Opção A) = 1.0000**

dof = N − k = 1624 − k

---

## 4. Interpretação Epistêmica

### 4.1 Competitividade [E]

Todos os modelos são praticamente equivalentes em χ²:
- Δχ²(ΛCDM − CPL) = +0.418 → diferença insignificante
- Δχ²(ΛCDM − RLL) = −0.195 → RLL marginalmente pior que ΛCDM em χ²
- ΔAIC(RLL − ΛCDM) = +3.81 → penalidade pelos 2 parâmetros extras (esperada)

**Conclusão [E]**: o dataset Pantheon+ SNe Ia **não distingue** entre ΛCDM, CPL e RLL ao nível de χ². Todos os modelos com 4 parâmetros têm AIC ~4 unidades acima do ΛCDM (penalidade puramente por k, não por pior fit).

### 4.2 Degenerescência RLL original ↔ Opção A [E]

**Ratio = 1.0000**: as funções `f(z)` e `1 − f(z)` produzem **resultado idêntico** contra Pantheon+. Isto ocorre porque o otimizador absorve a inversão reparametrizando wₐ:
- RLL original: w₀=−0.9037, wₐ=+0.0729 → ŵ (z alto) = −0.9037 + 0.0729 = −0.8308
- RLL Opção A: w₀=−0.8307, wₐ=−0.0729 → ŵ (z alto) = −0.8307 − 0.0729 = −0.9036

Os valores trocam de posição: z baixo ↔ z alto, mas o fit de distância de luminosidade não é sensível à qual direção a transição aponta quando wₐ é pequeno.

**Implicação [H]**: A distinção entre `f(z)` e `1 − f(z)` requer dataset sensível à **evolução temporal de w(z)**, não apenas à distância integrada — candidatos: BAO + CMB combinados, onde a estrutura de fase importa.

### 4.3 wa_eff vs DESI [H]

- RLL Pantheon+: wₐ = +0.073 (muito pequeno, próximo de ΛCDM)
- DESI CPL best-fit: wₐ ≈ −0.62 (phantom no passado)
- **Incompatibilidade**: os dois datasets apontam para wₐ em direções opostas quando o modelo CPL é usado

Isso não é uma refutação do RLL, mas documenta que a parametrização de equação de estado do RLL (via transição logística) responde diferentemente aos dois datasets. **TOKEN_VAZIO**: análise joint (Pantheon+ + BAO DESI simultâneos) pendente.

### 4.4 Status na Tupla I_RLL

| Elemento | Antes | Após Fase 4 |
|----------|-------|-------------|
| D (dados reais) | ✅ CSV BAO | ✅ + Pantheon+ 1624 SNe |
| T (testes) | ⚠️ parcial | ⚠️ + 4 fits Nelder-Mead executados |
| `claim_allowed` | false | **false** (S sistemáticos ainda [VAZIO]) |

---

## 5. Gaps Remanescentes após Fase 4

| Gap | Prioridade | Descrição |
|-----|-----------|-----------|
| Análise joint Pantheon+ + BAO | P1 | Fit simultâneo com covariância cruzada |
| Covariância sistemática Pantheon+ | P1 | `pantheon_covsys.zip` não integrado — systematics off-diagonal |
| wa incompatibilidade DESI | P1 | wₐ(Pantheon)=+0.07 vs wₐ(DESI)=−0.62 — não resolvido |
| Moresco H(z) χ² | P2 | Ainda [VAZIO] |
| Planck priors joint | P2 | Ainda [VAZIO] |

---

## 6. Arquivo de Resultado

```
results/pantheon_plus_resultado_real.txt
```

Conteúdo exato gerado pelo script `run_rll_vs_pantheon.py` em 2026-07-06.
