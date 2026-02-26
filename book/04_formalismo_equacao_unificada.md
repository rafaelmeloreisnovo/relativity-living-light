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
## Derivação da forma estendida

**Base formal:** [`../newadd/01_MATHEMATICS.md`](../newadd/01_MATHEMATICS.md), [`../newadd/02_PHYSICS.md`](../newadd/02_PHYSICS.md), [`../newadd/04_GEOMETRY.md`](../newadd/04_GEOMETRY.md).

`E²(a)=Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ + Ω_s0 [f(a)+(1-f(a))a⁻³] + Ω_B0 a⁻⁴ + Ω_P0 a⁻⁴`, com `E(a)=H(a)/H₀` e `a=1/(1+z)`.
1. **Equação de Friedmann padrão (background FRW plano):**
   
   `H²(a)=H₀²[Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ]`.

2. **Definição da taxa de expansão normalizada:**

   `E(a)=H(a)/H₀`, portanto

   `E²(a)=Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ`.

3. **Substituição explícita dos componentes padrão:**

   - radiação: `Ω_r a⁻⁴`;
   - matéria não-relativística: `Ω_m a⁻³`;
   - constante cosmológica: `Ω_Λ`.

4. **Inserção do setor de superposição com transição logística** (detalhes em [`05_formalismo_funcao_transicao.md`](./05_formalismo_funcao_transicao.md)):

   `Ω_s0[f(a)+(1-f(a))a⁻³]`,

   com

   `f(z)=1/(1+exp((z-z_t)/w_t))` e `a=1/(1+z)`.

5. **Inserção dos termos booster magnético/plasmático** (hipóteses do setor em [`09_hipoteses_setor_magnetico_plasmatico.md`](./09_hipoteses_setor_magnetico_plasmatico.md)):

## Fundamentos matemáticos operacionais

### Função logística de transição
   `Ω_B0 a⁻⁴ + Ω_P0 a⁻⁴`.

6. **Forma final normalizada:**

Operacionalmente, `z_t` fixa o redshift central em que a transição DE→DM do setor de superposição é máxima, enquanto `w_t` regula a largura efetiva dessa janela de transição (abrupta para `w_t` pequeno, suave para `w_t` maior).

### Propriedades matemáticas

- **Monotonicidade (para `w_t>0`)**: na convenção operacional do capítulo, `df/dz>0` para a fração coerente efetiva ao longo da varredura de redshift adotada.
- **Assíntotas**: `f→1` para `z >> z_t` e `f→0` para `z << z_t`.
- **Escala característica da transição**: `w_t` controla a espessura da janela de transição em redshift; valores menores comprimem a troca de regime, valores maiores alargam a transição.

### Parametrização e implicações físicas

- `Ω_s0` define a amplitude atual do setor de superposição e, portanto, o peso do termo híbrido no background `E(a)`.
- `z_t` desloca a época de crossover entre comportamento tipo energia escura (coerente) e tipo matéria escura (decoerente), alterando `H(z)` e integrais de distância.
- `w_t` controla quão rápida é a troca entre os regimes, impactando suavidade em `H(z)`, `Δμ(z)` e no acoplamento com crescimento estrutural (`fσ₈`).
- `Ω_B0` e `Ω_P0` entram como correções `a⁻⁴` no background, com efeito potencial em observáveis de precisão (expansão em alto redshift, calibração de distância e lensing).

### Definições dos parâmetros
   `E²(a)=Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ + Ω_s0[f(a)+(1-f(a))a⁻³] + Ω_B0 a⁻⁴ + Ω_P0 a⁻⁴`.

## Definição formal dos parâmetros

- `Ω_r`: fração de densidade de radiação no presente (`a=1`); evolução de background `ρ_r(a)∝a⁻⁴`.
- `Ω_m`: fração de densidade de matéria não-relativística no presente; evolução `ρ_m(a)∝a⁻³`.
- `Ω_Λ`: fração associada ao termo tipo constante cosmológica; `ρ_Λ(a)=constante`.
- `Ω_s0`: fração atual do setor de superposição; contribui como mistura `f(a)` (comportamento tipo DE) e `(1-f(a))a⁻³` (comportamento tipo DM).
- `Ω_B0`: fração efetiva atual do booster magnético; no background entra como correção radiativa `a⁻⁴`.
- `Ω_P0`: fração efetiva atual do booster plasmático; no background entra como correção radiativa `a⁻⁴`.

## Hipóteses e domínio de validade

- **Homogeneidade/isotropia:** a construção assume background FRW (média cosmológica), sem resolver estruturas locais individualmente.
- **Regime efetivo fenomenológico:** os termos adicionais (`Ω_s0`, `Ω_B0`, `Ω_P0`) são parametrizações efetivas para confrontação observacional no nível de expansão.
- **Validade em background:** a equação é usada para `H(z)` e integrais cosmológicas associadas, não como descrição microscópica completa do setor escuro.
- **Separação de efeitos locais:** efeitos astrofísicos locais, não-lineares ou dependentes de ambiente devem ser tratados fora desta parametrização de background.

## Limites assintóticos

- **`a→0` (alto redshift):** os termos `a⁻⁴` dominam (`Ω_r`, `Ω_B0`, `Ω_P0`). Assim, o efeito relativo de `Ω_B0`/`Ω_P0` é naturalmente mais visível no regime primordial e em observáveis sensíveis à expansão radiativa.
- **`a→1` (época atual):** cada `Ω_i` representa diretamente sua fração efetiva no presente; a interpretação é feita por balanço entre `Ω_m`, `Ω_Λ`, `Ω_s0` e correções `Ω_B0`, `Ω_P0`.
- **`z≫z_t` (antes da transição):** `f→1`, o setor de superposição aproxima comportamento tipo DE.
- **`z≪z_t` (após a transição):** `f→0`, prevalece a parcela `a⁻³` do setor de superposição, com caráter tipo DM.

Para o impacto empírico desses regimes nas curvas comparativas e painéis de resultados, ver [`24_resultados_figuras_painel.md`](./24_resultados_figuras_painel.md).

## Conexão observacional

**Fontes técnicas:** [`../newadd/01_MATHEMATICS.md`](../newadd/01_MATHEMATICS.md), [`../newadd/02_PHYSICS.md`](../newadd/02_PHYSICS.md), [`../newadd/04_GEOMETRY.md`](../newadd/04_GEOMETRY.md).

A validação fenomenológica usa como alvos principais `H(z)`, `Δμ(z)`, `fσ₈(z)` e lensing, com nomenclatura alinhada a `docs/CONCEPTUAL_FRAMEWORK.md`, `docs/Relativity_Living_Light.md` e `docs/LAGRANGIANO_EFT.md`.

## Ver também

- [Hipóteses magneto-plasmáticas](./09_hipoteses_setor_magnetico_plasmatico.md)
- [Validação DESI/BOSS](./21_validacao_desi_boss.md)
- [Validação JWST/AGN/SMBH](./22_validacao_jwst_agn_smbh.md)
- [Painel analítico de resultados](./24_resultados_figuras_painel.md)

---

## Referências e convenções terminológicas
- Convenção editorial: usar exclusivamente as formas **DESI DR2**, **BOSS DR12** e **pós-PhD** (quando houver menção à etapa pós-doutoral).
### Quadro técnico — Dicionário Matemática → Observável

| Operador/Função matemática | Definição no modelo | Variável observacional associada | Tipo de dado/sonda |
|---|---|---|---|
| `E(z)` ou `H(z)` | `E(z)=H(z)/H₀` e `H(z)=H₀E(z)` na equação de background. | `H(z)` | BAO radial e cosmic chronometers (idade diferencial). |
| distância angular integrada | Distância angular obtida por integral de linha de visada no background (`D_A(z)` via integral de `1/H(z)`). | `D_A(z)` | BAO angular e lentes fortes/fracas (escala geométrica). |
| função de crescimento efetiva | Crescimento linear efetivo da estrutura reportado como `fσ₈(z)`. | `fσ₈(z)` | RSD (redshift-space distortions) em levantamentos espectroscópicos. |
| potencial/projeção de lente | Projeção do potencial gravitacional ao longo da linha de visada, observada como convergência. | `κ` | Weak lensing/cosmic shear e mapas de massa em clusters. |

> Notação alinhada ao glossário: `E(z)`, `H(z)`, `D_A(z)`, `fσ₈(z)` e `κ` seguem convenção canônica do capítulo 33.

