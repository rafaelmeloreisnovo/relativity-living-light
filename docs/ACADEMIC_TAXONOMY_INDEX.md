# ACADEMIC_TAXONOMY_INDEX

Documento índice acadêmico com taxonomia mínima para rastrear formulações, hipóteses e estado observacional do modelo RLL.

## Links cruzados obrigatórios

- [docs/LAGRANGIANO_EFT.md](./LAGRANGIANO_EFT.md)
- [docs/PERTURBACOES_CRESCIMENTO.md](./PERTURBACOES_CRESCIMENTO.md)
- [docs/VELOCIDADE_SOM.md](./VELOCIDADE_SOM.md)
- [docs/ROADMAP_VALIDACAO.md](./ROADMAP_VALIDACAO.md)
- [docs/REFERENCES.md](./REFERENCES.md)

---

## Áreas temáticas

| ID único | Item | Referência de arquivo (path completo) | Status | Observável associado (quando houver) |
|---|---|---|---|---|
| AREA-001 | EFT do setor de superposição (consistência de campos, estabilidade e acoplamentos) | [`/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md`](./LAGRANGIANO_EFT.md) | parcial real | Birrefringência cosmológica / alinhamento de spins |
| AREA-002 | Crescimento estrutural linear com componente de superposição | [`/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md`](./PERTURBACOES_CRESCIMENTO.md) | parcial real | `fσ₈(z)` |
| AREA-003 | Dinâmica de velocidade do som do setor efetivo | [`/workspace/relativity-living-light/docs/VELOCIDADE_SOM.md`](./VELOCIDADE_SOM.md) | sintético | Estabilidade linear e espectro de crescimento |
| AREA-004 | Pipeline de validação observacional RLL vs ΛCDM | [`/workspace/relativity-living-light/docs/ROADMAP_VALIDACAO.md`](./ROADMAP_VALIDACAO.md) | parcial real | `μ(z)`, `χ²`, `AIC`, `BIC` |
| AREA-005 | Base bibliográfica e mapeamento de precedentes teóricos/observacionais | [`/workspace/relativity-living-light/docs/REFERENCES.md`](./REFERENCES.md) | real validado | — |

---

## Fórmulas/expressões principais

| ID único | Item | Referência de arquivo (path completo) | Status | Observável associado (quando houver) |
|---|---|---|---|---|
| FORM-001 | Ação EFT total: `S = ∫ d⁴x √(−g) [ R/(16πG) + L_m + L_r + L_sup ]` | [`/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md`](./LAGRANGIANO_EFT.md) | parcial real | Consistência dinâmica global (indireto em `H(z)`) |
| FORM-002 | Lagrangiana canônica: `L_sup = −(1/2) g^{μν}∂_μφ∂_νφ − V(φ) + L_acoplamentos` | [`/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md`](./LAGRANGIANO_EFT.md) | parcial real | Assinatura de estabilidade e propagação |
| FORM-002A | Cutoff scale EFT: `Λ = O(10⁻³ eV)` para o setor de energia escura, ou `Λ ≈ 10³ eV` se acoplado a matéria escura. Justificativa: a expansão em derivadas de `H` converge para redshifts `z < 5`. | [`/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md`](./LAGRANGIANO_EFT.md) | parcial real | Domínio de validade EFT |
| FORM-003 | Evolução de crescimento linear: `D'' + [2 + d(lnH)/d(lna)]D' − (3/2)Ω_m(a)D = 0` | [`/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md`](./PERTURBACOES_CRESCIMENTO.md) | parcial real | `fσ₈(z)` |
| FORM-004 | Taxa observável de crescimento: `fσ₈(z) = f(z)·σ₈(0)·D(z)/D(0)` | [`/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md`](./PERTURBACOES_CRESCIMENTO.md) | parcial real | `fσ₈(z)` |
| FORM-005 | Regime canônico de som no escalar: `c_s² = 1` (com distinção de fluido efetivo) | [`/workspace/relativity-living-light/docs/VELOCIDADE_SOM.md`](./VELOCIDADE_SOM.md) | sintético | Critério `c_s² > 0` e estabilidade |

---

## Teorias e extensões

| ID único | Item | Referência de arquivo (path completo) | Status | Observável associado (quando houver) |
|---|---|---|---|---|
| TEORIA-001 | Quintessência do tipo thawing para mapear transição de estado efetivo | [`/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md`](./LAGRANGIANO_EFT.md) | parcial real | `w_eff(z)` e histórico de expansão |
| TEORIA-002 | Acoplamento magneto-coerente `L_mag ∝ F_{μν}F^{μν}(φ/M_Pl)` | [`/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md`](./LAGRANGIANO_EFT.md) | parcial real | Birrefringência / rotação de polarização |
| TEORIA-003 | Acoplamento com plasma `L_plasma ∝ n_e φ²/M_Pl²` | [`/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md`](./LAGRANGIANO_EFT.md) | sintético | Dependência ambiental em propagação |
| TEORIA-004 | Prescrição de pipeline observacional para comparação RLL–ΛCDM | [`/workspace/relativity-living-light/docs/ROADMAP_VALIDACAO.md`](./ROADMAP_VALIDACAO.md) | parcial real | `Δμ`, `χ²`, `AIC`, `BIC` |
| TEORIA-005 | Enquadramento comparativo com literatura de não-localidade, DE/DM e MG | [`/workspace/relativity-living-light/docs/REFERENCES.md`](./REFERENCES.md) | real validado | — |

---

## Hipóteses testáveis

| ID único | Item | Referência de arquivo (path completo) | Status | Observável associado (quando houver) |
|---|---|---|---|---|
| HYP-001 | O termo de superposição reduz `fσ₈(z)` em relação ao ΛCDM em redshifts intermediários | [`/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md`](./PERTURBACOES_CRESCIMENTO.md) | parcial real | `fσ₈(z)` (BOSS/Euclid/DESI) |
| HYP-002 | O acoplamento magneto-coerente gera sinal mensurável de birrefringência cosmológica | [`/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md`](./LAGRANGIANO_EFT.md) | parcial real | Polarização e rotação de plano |
| HYP-003 | A cadeia de validação Pantheon+ discrimina RLL vs ΛCDM por métricas de ajuste | [`/workspace/relativity-living-light/docs/ROADMAP_VALIDACAO.md`](./ROADMAP_VALIDACAO.md) | parcial real | `χ²`, `AIC`, `BIC`, resíduos `Δμ` |
| HYP-004 | Regimes efetivos de velocidade do som preservam estabilidade linear no setor escuro unificado | [`/workspace/relativity-living-light/docs/VELOCIDADE_SOM.md`](./VELOCIDADE_SOM.md) | sintético | Condição de estabilidade (`c_s²`) |
| HYP-005 | A construção EFT evita ghosts/taquiões no domínio de parâmetros adotado | [`/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md`](./LAGRANGIANO_EFT.md) | parcial real | Critérios de estabilidade teórica |

---

## Evidências observacionais e status

| ID único | Evidência | Referência de arquivo (path completo) | Status | Observável associado (quando houver) |
|---|---|---|---|---|
| EVID-001 | Compilação de referência para não-localidade fotônica (base conceitual laboratorial) | [`/workspace/relativity-living-light/docs/REFERENCES.md`](./REFERENCES.md) | real validado | Correlações não-locais / testes tipo Bell |
| EVID-002 | Tabela de dados RSD (BOSS DR12 e complementares) para crescimento | [`/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md`](./PERTURBACOES_CRESCIMENTO.md) | parcial real | `fσ₈(z)` |
| EVID-003 | Estado do pipeline Pantheon+ com trilha explícita de ingestão e artefatos esperados | [`/workspace/relativity-living-light/docs/ROADMAP_VALIDACAO.md`](./ROADMAP_VALIDACAO.md) | parcial real | `μ(z)`, `χ²`, `AIC`, `BIC` |
| EVID-004 | Constraints contextuais para acoplamento magnético (limites citados no framework) | [`/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md`](./LAGRANGIANO_EFT.md) | parcial real | Limite em `α_B` |
| EVID-005 | Consolidação final por evidência integrada (expansão + crescimento + consistência EFT) | [`/workspace/relativity-living-light/docs/ROADMAP_VALIDACAO.md`](./ROADMAP_VALIDACAO.md) + [`/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md`](./PERTURBACOES_CRESCIMENTO.md) + [`/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md`](./LAGRANGIANO_EFT.md) | sintético | Combinação multissonda |
- [LAGRANGIANO_EFT](./LAGRANGIANO_EFT.md)
- [PERTURBACOES_CRESCIMENTO](./PERTURBACOES_CRESCIMENTO.md)
- [VELOCIDADE_SOM](./VELOCIDADE_SOM.md)
- [ROADMAP_VALIDACAO](./ROADMAP_VALIDACAO.md)
- [REFERENCES](./REFERENCES.md)

---

## 1) Áreas temáticas

| ID único | Item | Referência de arquivo (path completo) | Status | Observável associado |
|---|---|---|---|---|
| AREA-001 | EFT do setor de superposição (consistência de campos, estabilidade e acoplamentos) | `/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md` | parcial real | Birrefringência cosmológica / alinhamento de spins |
| AREA-002 | Crescimento estrutural linear com componente de superposição | `/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md` | parcial real | `fσ₈(z)` |
| AREA-003 | Dinâmica de velocidade do som do setor efetivo | `/workspace/relativity-living-light/docs/VELOCIDADE_SOM.md` | sintético | Estabilidade linear e espectro de crescimento |
| AREA-004 | Pipeline de validação observacional RLL vs ΛCDM | `/workspace/relativity-living-light/docs/ROADMAP_VALIDACAO.md` | parcial real | `μ(z)`, `χ²`, `AIC`, `BIC` |
| AREA-005 | Base bibliográfica e mapeamento de precedentes teóricos/observacionais | `/workspace/relativity-living-light/docs/REFERENCES.md` | real validado | Não aplicável |

---

## 2) Fórmulas/expressões principais

| ID único | Item | Referência de arquivo (path completo) | Status | Observável associado |
|---|---|---|---|---|
| FORM-001 | Ação EFT total: `S = ∫ d⁴x √(−g) [ R/(16πG) + L_m + L_r + L_sup ]` | `/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md` | parcial real | Consistência dinâmica global (indireto em `H(z)`) |
| FORM-002 | Lagrangiana canônica: `L_sup = −(1/2) g^{μν}∂_μφ∂_νφ − V(φ) + L_acoplamentos` | `/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md` | parcial real | Assinatura de estabilidade e propagação |
| FORM-002A | Cutoff scale EFT: `Λ = O(10⁻³ eV)` para o setor de energia escura, ou `Λ ≈ 10³ eV` se acoplado a matéria escura. Justificativa: a expansão em derivadas de `H` converge para redshifts `z < 5`. | `/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md` | parcial real | Domínio de validade EFT |
| FORM-003 | Evolução de crescimento linear: `D'' + [2 + d(lnH)/d(lna)]D' − (3/2)Ω_m(a)D = 0` | `/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md` | parcial real | `fσ₈(z)` |
| FORM-004 | Taxa observável de crescimento: `fσ₈(z) = f(z)·σ₈(0)·D(z)/D(0)` | `/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md` | parcial real | `fσ₈(z)` |
| FORM-005 | Regime canônico de som no escalar: `c_s² = 1` (com distinção de fluido efetivo) | `/workspace/relativity-living-light/docs/VELOCIDADE_SOM.md` | sintético | Critério `c_s² > 0` e estabilidade |

---

## 3) Teorias e extensões

| ID único | Item | Referência de arquivo (path completo) | Status | Observável associado |
|---|---|---|---|---|
| TEORIA-001 | Quintessência do tipo thawing para mapear transição de estado efetivo | `/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md` | parcial real | `w_eff(z)` e histórico de expansão |
| TEORIA-002 | Acoplamento magneto-coerente `L_mag ∝ F_{μν}F^{μν}(φ/M_Pl)` | `/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md` | parcial real | Birrefringência / rotação de polarização |
| TEORIA-003 | Acoplamento com plasma `L_plasma ∝ n_e φ²/M_Pl²` | `/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md` | sintético | Dependência ambiental em propagação |
| TEORIA-004 | Prescrição de pipeline observacional para comparação RLL–ΛCDM | `/workspace/relativity-living-light/docs/ROADMAP_VALIDACAO.md` | parcial real | `Δμ`, `χ²`, `AIC`, `BIC` |
| TEORIA-005 | Enquadramento comparativo com literatura de não-localidade, DE/DM e MG | `/workspace/relativity-living-light/docs/REFERENCES.md` | real validado | Não aplicável |

---

## 4) Hipóteses testáveis

| ID único | Item | Referência de arquivo (path completo) | Status | Observável associado |
|---|---|---|---|---|
| HYP-001 | O termo de superposição reduz `fσ₈(z)` em relação ao ΛCDM em redshifts intermediários | `/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md` | parcial real | `fσ₈(z)` (BOSS/Euclid/DESI) |
| HYP-002 | O acoplamento magneto-coerente gera sinal mensurável de birrefringência cosmológica | `/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md` | parcial real | Polarização e rotação de plano |
| HYP-003 | A cadeia de validação Pantheon+ discrimina RLL vs ΛCDM por métricas de ajuste | `/workspace/relativity-living-light/docs/ROADMAP_VALIDACAO.md` | parcial real | `χ²`, `AIC`, `BIC`, resíduos `Δμ` |
| HYP-004 | Regimes efetivos de velocidade do som preservam estabilidade linear no setor escuro unificado | `/workspace/relativity-living-light/docs/VELOCIDADE_SOM.md` | sintético | Condição de estabilidade (`c_s²`) |
| HYP-005 | A construção EFT evita ghosts/taquiões no domínio de parâmetros adotado | `/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md` | parcial real | Critérios de estabilidade teórica |

---

## 5) Evidências observacionais e status

| ID único | Evidência | Referência de arquivo (path completo) | Status | Observável associado |
|---|---|---|---|---|
| EVID-001 | Compilação de referência para não-localidade fotônica (base conceitual laboratorial) | `/workspace/relativity-living-light/docs/REFERENCES.md` | real validado | Correlações não-locais / testes tipo Bell |
| EVID-002 | Tabela de dados RSD (BOSS DR12 e complementares) para crescimento | `/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md` | parcial real | `fσ₈(z)` |
| EVID-003 | Estado do pipeline Pantheon+ com trilha explícita de ingestão e artefatos esperados | `/workspace/relativity-living-light/docs/ROADMAP_VALIDACAO.md` | parcial real | `μ(z)`, `χ²`, `AIC`, `BIC` |
| EVID-004 | Constraints contextuais para acoplamento magnético (limites citados no framework) | `/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md` | parcial real | Limite em `α_B` |
| EVID-005 | Consolidação final por evidência integrada (expansão + crescimento + consistência EFT) | `/workspace/relativity-living-light/docs/ROADMAP_VALIDACAO.md` + `/workspace/relativity-living-light/docs/PERTURBACOES_CRESCIMENTO.md` + `/workspace/relativity-living-light/docs/LAGRANGIANO_EFT.md` | sintético | Combinação multissonda |

---

## Nota de uso

Este índice é um mapa de rastreabilidade acadêmica. Atualizar IDs e status sempre que um item migrar de `sintético` → `parcial real` → `real validado`.
