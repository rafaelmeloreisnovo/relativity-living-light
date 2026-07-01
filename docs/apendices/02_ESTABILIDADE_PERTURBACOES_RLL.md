# Apêndice 02 — Estabilidade das perturbações RLL

Status: **BLOQUEADO PELO GATE ESTATÍSTICO**.

A ação de segunda ordem relevante é:

```text
S2 = integral dt d^3x a^3 Q_s [ zdoteta^2 - (c_s^2/a^2) (grad zeta)^2 ]
```

O contrato físico é:

- `Q_s > 0`: ausência de ghosts.
- `0 < c_s^2 <= 1`: ausência de instabilidade de gradiente e causalidade efetiva.
- domínio em `a,k` restrito a parâmetros que passam no gate observacional.

Como o gate de 2026-07-01 rejeitou o RLL operacional contra ΛCDM por ΔAIC/ΔBIC positivos, não há domínio observacional aceito para promover uma prova global de estabilidade.

## Produtos não promovidos

- `[VAZIO]` Script SymPy/Mathematica final para `c_s^2(a,k)` e `Q_s(a)` calibrado por posterior real.
- `[VAZIO]` Plots globais de estabilidade dentro do horizonte.
- `[VAZIO]` Declaração “sem ghosts” válida para submissão.

## Nota RAW_TEXT_FIRST

O token vazio aqui é deliberado: estabilidade formal sem posterior observacional aceito não resolve a não-conformidade de submissão, apenas a desloca.
