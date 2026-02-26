# 09. Hipóteses — Setor Magnético e Plasmático

[⬅️ Capítulo anterior](./08_hipoteses_hipotese_central.md) | [📚 Sumário do livro](./README.md) | [Capítulo próximo ➡️](./10_hipoteses_entropia_margens.md)

Detalha hipóteses físicas adicionais para setor magnético e setor plasmático no background.


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
## Hipótese de acoplamento magneto-coerente

### Modelo de acoplamento magneto-coerente (forma operacional)

A hipótese estende a normalização de superposição fotônica por um termo dependente do setor magnético, seguindo a forma já registrada em `docs/BOOSTERS.md`:

```
Ω_s0 → Ω_s0·[1+α_B(Ω_B0 a⁻⁴)^β]
```

Interpretação operacional dos parâmetros:

- `α_B`: amplitude da força efetiva de acoplamento entre o setor magnético e o setor de coerência fotônica. Quando `α_B→0`, recupera-se o caso sem modulação magneto-coerente.
- `β`: índice de regime da resposta ao termo magnético:
  - `0<β<1` (**sublinear**): resposta amortecida/saturante; aumentos em `Ω_B0 a⁻⁴` produzem incrementos relativamente menores no acoplamento efetivo.
  - `β≈1` (**linear**): resposta proporcional direta à energia magnética efetiva.
  - `β>1` (**superlinear**): resposta amplificada; pequenas variações no setor magnético podem gerar modulação mais forte de `Ω_s0`.

Hipótese de validade por domínio:

- **Background cosmológico**: usa-se a forma média efetiva, com contribuição principal na contabilidade energética e em `H(z)`.
- **Ambiente de halo/cluster**: a mesma estrutura funcional é interpretada como aproximação fenomenológica para plasma magnetizado, cisalhamento e turbulência locais, onde a modulação de coerência tende a ser mais relevante.

## Papel do plasma (T, P) na dinâmica

### Termo plasmático e interpretação observável

No nível de background, a contribuição plasmática é modelada por:

```
ρ_plasma(a)=Ω_P0 ρ_c0 a⁻⁴
```

Em termos microfísicos e magneto-térmicos, usa-se:

```
ρ_plasma=(3/2)nk_B T/c² + B²/(2μ₀c²)
```

Conexão com proxies observacionais:

- **Temperatura (`T`)**: mapeia energia térmica do meio (raios X em clusters) e informa o termo `(3/2)nk_B T/c²`.
- **Faraday (RM)**: traça magnetização integrada em linha de visada (`n_e B_∥`) e auxilia a ancorar a parcela magnética `B²/(2μ₀c²)`.
- **Pressão efetiva (`P_eff`)**: combina pressão térmica e magnetização/turbulência, com impacto no termo gravitacional efetivo `ρ+3p/c²`.

A pressão térmica não é apenas correção hidrodinâmica local: ela entra na fonte gravitacional efetiva via combinação `ρ+3p/c²`, reforçando a curvatura efetiva quando `T` e `P` aumentam. Em linha com `docs/VELOCIDADE_SOM.md`, o efeito dominante no regime discutido é sobre o background e sobre a transição coerência/decoerência; não há crescimento próprio por instabilidade de Jeans do componente neste domínio de parâmetros.

## Decoerência e regime radiativo

Quando temperatura, turbulência e atividade do plasma aumentam, o ambiente favorece perda de coerência local do setor fotônico, deslocando a dinâmica para o ramo atrativo. Esse deslocamento não implica abandonar o comportamento radiativo global: a contribuição média ainda mantém lei tipo `a⁻⁴` no background para os setores magnético/plasmático.

Assim, distingue-se explicitamente:
- efeito global cosmológico (termos médios escalando como `a⁻⁴`);
- efeito local em estrutura (halos/aglomerados), onde magnetização, cisalhamento e turbulência modulam a coerência e a resposta gravitacional efetiva.

## Observáveis e assinaturas testáveis

### Cadeia de impacto em observáveis

Organiza-se a inferência em uma cadeia operacional de três níveis:

1. **Expansão `H(z)` → crescimento `fσ₈(z)`**: mudanças no orçamento efetivo alteram o histórico de expansão e, indiretamente, a taxa de crescimento de estruturas.
2. **Potencial projetado → `κ/γ` (lensing)**: a resposta no potencial integrado ao longo da linha de visada afeta convergência e cisalhamento, com foco em sistemas de halo/aglomerado.
3. **Potencial local/gradiente efetivo → curvas de rotação**: no regime galáctico, a modulação do gradiente potencial impacta velocidades orbitais inferidas.

A hipótese gera alvos observacionais diretos e indiretos:

- **Lensing em clusters (`κ`, `γ`)**: sensível à distribuição efetiva de massa/pressão quando há contribuição magneto-plasmática.
- **Rotação/Faraday**: proxy observacional de campo magnético de linha de visada e do estado do plasma magnetizado.
- **Crescimento `fσ₈(z)`**: impacto principalmente indireto, via alteração de `H(z)` e das frações efetivas dos componentes no orçamento cosmológico.

A validação segue o plano estatístico de `docs/PLANO_AD_AGN_JWST.md`: comparação por χ², penalização por complexidade (AIC/BIC) e formulação de previsões falsificáveis para separar ganho físico real de sobreajuste fenomenológico.

Capítulos de validação diretamente conectados:

- [`book/18_validacao_crescimento_fs8.md`](./18_validacao_crescimento_fs8.md)
- [`book/19_validacao_lentes_aglomerados.md`](./19_validacao_lentes_aglomerados.md)
- [`book/20_validacao_rotacao_galaxias.md`](./20_validacao_rotacao_galaxias.md)
- [`book/24_resultados_figuras_painel.md`](./24_resultados_figuras_painel.md)

## Falsificabilidade mínima

Sinais que favorecem efeito físico (vs. degenerescência puramente paramétrica):

- **Consistência cruzada entre sondas**: mesma região viável de (`α_B`, `β`, `Ω_P0`) ajusta simultaneamente `fσ₈(z)`, lentes em clusters e curvas de rotação, sem tensão estatística relevante.
- **Escalonamento ambiente-dependente previsto**: ganho de sinal em halos/aglomerados magnetizados (alto RM, alta `T`) superior ao observado em ambientes pouco magnetizados.
- **Correlação com proxies físicos independentes**: tendência monotônica entre desvio residual e estimadores de magnetização/pressão, além do que seria esperado por ruído e seleção.

Sinais que sugerem degenerescência paramétrica:

- melhora apenas global de ajuste sem padrão físico em função de `T`, RM ou pressão;
- necessidade de regiões mutuamente incompatíveis de parâmetros para diferentes observáveis;
- desaparecimento do ganho quando se impõe priors físicos em plasma/magnetização.

---
