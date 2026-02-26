# Framework — Resumo Canônico (Micro-tabela)

Status: canônico vigente  
Escopo: padronização terminológica para README, livro e snippets.

## Micro-tabela de termos canônicos (uso obrigatório)

| Termo canônico | Forma curta | Definição operacional | Observação de uso |
|---|---|---|---|
| **superposição fotônica** | setor de superposição | Componente dinâmica unificada que evolui entre regimes efetivos cosmológicos. | Termo principal; evitar “superposição escura” sem qualificação. |
| **coerência (f(z))** | coerência | Fração logística do setor de superposição: \(f(z)=1/(1+\exp((z-z_t)/w_t))\). | Usar para o ramo tipo DE do setor de superposição. |
| **decoerência ((1−f(z)))** | decoerência | Fração complementar do setor de superposição: \((1-f(z))\). | Usar para o ramo tipo DM do setor de superposição. |
| **setor magnético** | magnético | Contribuição física associada a \(\Omega_{B0}\), \(\rho_B\), \(B\), \(\alpha_B\), \(\beta\). | Evitar “campo magnético” isolado em títulos/legendas canônicas. |
| **setor plasmático** | plasmático | Contribuição física associada a \(\Omega_{P0}\), \(\rho_P\), \(n\), \(T\). | Evitar “plasma” isolado em títulos/legendas canônicas. |
| **transição DE→DM do setor de superposição** | DE→DM | Passagem efetiva entre regime dominado por coerência para regime dominado por decoerência. | Sempre explicitar que a transição pertence ao setor de superposição. |

## Política de sinônimos legados

- Termos históricos/sinônimos (ex.: “superposição escura”, “campo magnético”, “plasma”) só podem aparecer quando marcados como **sinônimo legado** ou **histórico**.
- Em exemplos, figuras e legendas, priorizar sempre a forma canônica da tabela acima.
# Framework — Resumo Canônico

Este documento centraliza a formulação canônica do framework Relativity Living Light (RLL).

## Equação unificada (forma de referência)

```text
E²(a) = Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ +
        Ω_s0[f(a) + (1-f)a⁻³] +
        Ω_B0 a⁻⁴ +
        Ω_P0 a⁻⁴
```

com transição suave:

```text
f(z) = 1 / (1 + exp((z - z_t)/w_t))
```

## Interpretação canônica

- Ω_r, Ω_m, Ω_Λ: termos clássicos de radiação, matéria e constante cosmológica.
- Ω_s0: setor de superposição fotônica com transição dinâmica entre componente tipo energia escura e componente tipo matéria.
- Ω_B0, Ω_P0: contribuições adicionais de campo magnético e plasma.
- z_t e w_t: parâmetros que controlam posição e largura da transição.

## Regra editorial

A equação/interpretação canônica deve ser referenciada por link a este arquivo nos demais documentos, evitando duplicação de versões locais.
