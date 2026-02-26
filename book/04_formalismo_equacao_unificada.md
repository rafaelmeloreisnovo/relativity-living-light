# 04. Formalismo — Equação Unificada

[⬅️ Capítulo anterior](./03_fundamentos_preservacao_integridade.md) | [📚 Sumário do livro](./README.md) | [Capítulo próximo ➡️](./05_formalismo_funcao_transicao.md)

Apresenta a extensão tipo Friedmann com superposição dinâmica e termos adicionais.


## Termos canônicos aplicados neste ponto de entrada

Referência: [`docs/canonicos/FRAMEWORK_RESUMO_CANONICO.md`](../docs/canonicos/FRAMEWORK_RESUMO_CANONICO.md).

- **superposição fotônica** (termo principal)
- **coerência (f(z))**
- **decoerência ((1−f(z)))**
- **setor magnético**
- **setor plasmático**
- **transição DE→DM do setor de superposição**
## Bloco canônico do framework

- Referência canônica: [`../docs/canonicos/FRAMEWORK_RESUMO_CANONICO.md`](../docs/canonicos/FRAMEWORK_RESUMO_CANONICO.md)
- Instrução editorial: não duplicar versão local da equação/interpretação.

## Conteúdo incorporado (itens soltos/localizados)
Documentos e artefatos relacionados incorporados nesta etapa:
## Equação de Friedmann estendida (forma normalizada)

`E²(a)=Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ + Ω_s0 [f(a)+(1-f(a))a⁻³] + Ω_B0 a⁻⁴ + Ω_P0 a⁻⁴`, com `E(a)=H(a)/H₀` e `a=1/(1+z)`.

## Função de transição logística

`f(z)=1/(1+exp((z-z_t)/w_t))`, que controla a fração coerente do setor de superposição.

### Definições dos parâmetros

- `Ω_s0`: densidade atual do setor de superposição (amplitude do componente híbrido DE/DM).
- `z_t`: redshift de transição/coerência.
- `w_t`: largura da transição (quão abrupta/suave).
- `Ω_B0`: densidade efetiva do booster magnético (escala radiativa `a⁻⁴`).
- `Ω_P0`: densidade efetiva do booster plasmático (também `a⁻⁴` no background).

## Limites físicos e interpretação

- `z >> z_t`: `f→1`, regime coerente, `w_eff,sup≈-1` (componente tipo energia escura).
- `z << z_t`: `f→0`, regime colapsado, termo `a⁻³` domina (componente tipo matéria escura).
- `Ω_B0` e `Ω_P0` agem como correções subdominantes do background, relevantes em observáveis de precisão.

## Conexão observacional

A validação fenomenológica usa como alvos principais `H(z)`, `Δμ(z)`, `fσ₈(z)` e lensing, com nomenclatura alinhada a `docs/CONCEPTUAL_FRAMEWORK.md`, `docs/Relativity_Living_Light.md` e `docs/LAGRANGIANO_EFT.md`.


## Referências técnicas e bibliográficas

- Planck Collaboration (2020). *Planck 2018 results. VI. Cosmological parameters*. A&A 641, A6. DOI:10.1051/0004-6361/201833910.
- Linder, E. V. (2003). *Exploring the expansion history of the universe*. PRL 90, 091301.
- Bellini, E., & Sawicki, I. (2015). *Maximal Freedom at Minimum Cost: Linear Large-Scale Structure in General Modifications of Gravity*. JCAP 2015, 050.
- Bartelmann, M., & Schneider, P. (2001). *Weak gravitational lensing*. Physics Reports, 340(4-5), 291-472.
- DES Collaboration (2022). *Dark Energy Survey Year 3 results: cosmological constraints from galaxy clustering and weak lensing*. PRD 105, 023520.

**Fontes de consolidação no repositório:** `newadd/03_Descricao_Academica_PhD_Completa.md` (seção “Bibliografia Consolidada”), `docs/REFERENCES.md` e `book/39_apendice_referencias_fontes.md`.

---
