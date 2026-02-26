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

---

### Quadro técnico — Dicionário Matemática → Observável

| Operador/Função matemática | Definição no modelo | Variável observacional associada | Tipo de dado/sonda |
|---|---|---|---|
| `E(z)` ou `H(z)` | `E(z)=H(z)/H₀` e `H(z)=H₀E(z)` na equação de background. | `H(z)` | BAO radial e cosmic chronometers (idade diferencial). |
| distância angular integrada | Distância angular obtida por integral de linha de visada no background (`D_A(z)` via integral de `1/H(z)`). | `D_A(z)` | BAO angular e lentes fortes/fracas (escala geométrica). |
| função de crescimento efetiva | Crescimento linear efetivo da estrutura reportado como `fσ₈(z)`. | `fσ₈(z)` | RSD (redshift-space distortions) em levantamentos espectroscópicos. |
| potencial/projeção de lente | Projeção do potencial gravitacional ao longo da linha de visada, observada como convergência. | `κ` | Weak lensing/cosmic shear e mapas de massa em clusters. |

> Notação alinhada ao glossário: `E(z)`, `H(z)`, `D_A(z)`, `fσ₈(z)` e `κ` seguem convenção canônica do capítulo 33.

