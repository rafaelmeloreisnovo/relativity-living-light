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

Resultado o acoplamento magneto-coerente modulando a amplitude efetiva de superposição em ambientes magnetizados é sustentado por [Faraday-Rotation-Review-2011, Planck2018, DESI-DR2-2025].

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

Resultado o papel termodinâmico do plasma na fonte gravitacional efetiva e na transição de coerência é sustentado por [Cluster-MHD-2024, Faraday-Rotation-Review-2011, Planck2018].

## Decoerência e regime radiativo

Quando temperatura, turbulência e atividade do plasma aumentam, o ambiente favorece perda de coerência local do setor fotônico, deslocando a dinâmica para o ramo atrativo. Esse deslocamento não implica abandonar o comportamento radiativo global: a contribuição média ainda mantém lei tipo `a⁻⁴` no background para os setores magnético/plasmático.

Assim, distingue-se explicitamente:
- efeito global cosmológico (termos médios escalando como `a⁻⁴`);
- efeito local em estrutura (halos/aglomerados), onde magnetização, cisalhamento e turbulência modulam a coerência e a resposta gravitacional efetiva.

## Observáveis e assinaturas testáveis

A hipótese gera alvos observacionais diretos e indiretos:

- **Lensing em clusters (`κ`, `γ`)**: sensível à distribuição efetiva de massa/pressão quando há contribuição magneto-plasmática.
- **Rotação/Faraday**: proxy observacional de campo magnético de linha de visada e do estado do plasma magnetizado.
- **Crescimento `fσ₈(z)`**: impacto principalmente indireto, via alteração de `H(z)` e das frações efetivas dos componentes no orçamento cosmológico.

A validação segue o plano estatístico de `docs/PLANO_AD_AGN_JWST.md`: comparação por χ², penalização por complexidade (AIC/BIC) e formulação de previsões falsificáveis para separar ganho físico real de sobreajuste fenomenológico.

Resultado as assinaturas observacionais combinadas em lensing, rotação/Faraday e `fσ₈(z)` como testes do setor magneto-plasmático são sustentadas por [Faraday-Rotation-Review-2011, DESI-DR2-2025, eBOSS-DR16-2021].

## Referências de rastreabilidade

- [Planck2018] Planck Collaboration (2018), *Planck 2018 results. VI. Cosmological parameters*.
- [DESI-DR2-2025] DESI Collaboration (2025), *Data Release 2 cosmological constraints*.
- [eBOSS-DR16-2021] eBOSS Collaboration (2021), *DR16 cosmological analyses*.
- [Faraday-Rotation-Review-2011] Govoni et al. (2011), *Magnetic fields in galaxy clusters and Faraday rotation review*.
- [Cluster-MHD-2024] Vazza et al. (2024), *Cluster plasma and MHD constraints in large-scale structure*.

---
