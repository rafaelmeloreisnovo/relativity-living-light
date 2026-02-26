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

A hipótese estende a normalização de superposição fotônica por um termo dependente do setor magnético, seguindo a forma já registrada em `docs/BOOSTERS.md`:

```
Ω_s0 → Ω_s0·[1+α_B(Ω_B0 a⁻⁴)^β]
```

Neste acoplamento, `α_B` representa a força efetiva da interação entre campo magnético e setor de coerência fotônica, enquanto `β` controla a não-linearidade da resposta (saturação, amplificação sublinear ou superlinear conforme o regime). O cenário físico associado é de halos e aglomerados com plasma magnetizado onde o campo `B` modula a manutenção da coerência fotônica, alterando a fração efetiva entre ramo expansivo e ramo atrativo.

## Papel do plasma (T, P) na dinâmica

No nível de background, a contribuição plasmática é modelada por:

```
ρ_plasma(a)=Ω_P0 ρ_c0 a⁻⁴
```

Em termos microfísicos e magneto-térmicos, usa-se:

```
ρ_plasma=(3/2)nk_B T/c² + B²/(2μ₀c²)
```

A pressão térmica não é apenas correção hidrodinâmica local: ela entra na fonte gravitacional efetiva via combinação `ρ+3p/c²`, reforçando a curvatura efetiva quando `T` e `P` aumentam. Em linha com `docs/VELOCIDADE_SOM.md`, o efeito dominante no regime discutido é sobre o background e sobre a transição coerência/decoerência; não há crescimento próprio por instabilidade de Jeans do componente neste domínio de parâmetros.

## Decoerência e regime radiativo

Quando temperatura, turbulência e atividade do plasma aumentam, o ambiente favorece perda de coerência local do setor fotônico, deslocando a dinâmica para o ramo atrativo. Esse deslocamento não implica abandonar o comportamento radiativo global: a contribuição média ainda mantém lei tipo `a⁻⁴` no background para os setores magnético/plasmático.

Assim, distingue-se explicitamente:
- efeito global cosmológico (termos médios escalando como `a⁻⁴`);
- efeito local em estrutura (halos/aglomerados), onde magnetização, cisalhamento e turbulência modulam a coerência e a resposta gravitacional efetiva.

## Geometria e estrutura de campo

Esta seção adota, para o setor magneto-plasmático, a formulação geométrica de base documentada em [`newadd/04_GEOMETRY.md`](../newadd/04_GEOMETRY.md), em particular os elementos toroidais, integrais de circulação e vínculos topológicos usados para descrever coerência de campo.

### Geometria toroidal e coordenadas

O setor é representado em geometria toroidal com decomposição angular em coordenadas poloidal (`θ`) e toroidal (`φ`), além de um parâmetro radial efetivo (`r`) para cascas de fluxo magnetizado. No regime de halos e aglomerados, essa parametrização separa:

- variação ao longo das linhas fechadas do toro (direção toroidal);
- variação transversal de curvatura/encurvamento de linha de campo (direção poloidal);
- estratificação radial de densidade de plasma, pressão e intensidade magnética.

Com isso, `B(r,θ,φ)` e os campos termodinâmicos associados (`T`, `P`, `n`) entram no modelo de forma anisotrópica controlada, preservando a leitura física de circulação local e acoplamento com a coerência fotônica.

### Integrais de coerência

Para quantificar coerência de campo em domínio toroidal, introduzem-se integrais/funcionais de circulação e fluxo efetivo, inspirados na base geométrica (`∮`, `∫`) de `newadd/04_GEOMETRY.md`:

- integral de circulação coerente ao longo de curva fechada de campo (`C`): `I_C = ∮_C ω`;
- integral de fluxo em superfície seccional (`Σ`): `Φ_Σ = ∫_Σ dω`;
- funcional escalar de coerência média `𝒞[z]`, usado para modular os termos efetivos do setor magneto-coerente.

No modelo efetivo, essas quantidades entram como operadores de peso sobre o acoplamento `Ω_s0·[1+α_B(Ω_B0 a⁻⁴)^β]`, permitindo distinguir regiões com alta coerência geométrica (menor decoerência local) de regiões turbulentas (maior transferência para o ramo atrativo).

### Simetria geométrica e termos observáveis

Assume-se simetria axial/toroidal como caso de referência, com anisotropias permitidas como perturbações controladas por magnetização, cisalhamento e turbulência plasmática. Essa estrutura de simetria organiza a projeção para observáveis:

- **lensing `κ`**: responde à redistribuição geométrica de densidade/pressão efetiva e à quebra local de isotropia no potencial projetado;
- **crescimento `fσ₈`**: sensível ao histórico de coerência/decoerência e ao impacto indireto da geometria magneto-plasmática na taxa de expansão;
- **`H(z)`**: recebe correções de background via normalização efetiva dos setores, com assinatura dependente de como as integrais de coerência pesam os termos magnetizados ao longo de `z`.

Em termos práticos, a simetria define quais termos são permitidos no ansatz fenomenológico e quais padrões de anisotropia devem aparecer de forma correlacionada entre lensing, crescimento e expansão.

## Observáveis e assinaturas testáveis

A hipótese gera alvos observacionais diretos e indiretos:

- **Lensing em clusters (`κ`, `γ`)**: sensível à distribuição efetiva de massa/pressão quando há contribuição magneto-plasmática.
- **Rotação/Faraday**: proxy observacional de campo magnético de linha de visada e do estado do plasma magnetizado.
- **Crescimento `fσ₈(z)`**: impacto principalmente indireto, via alteração de `H(z)` e das frações efetivas dos componentes no orçamento cosmológico.

A validação segue o plano estatístico de `docs/PLANO_AD_AGN_JWST.md`: comparação por χ², penalização por complexidade (AIC/BIC) e formulação de previsões falsificáveis para separar ganho físico real de sobreajuste fenomenológico.

---
