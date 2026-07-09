# Apêndice 01 — Reconstrução do potencial escalar RLL

Status: **BLOQUEADO PELO GATE ESTATÍSTICO**.

Pela regra de prioridade desta rodada, a reconstrução microfísica completa só seria promovida se o gate estatístico inicial favorecesse RLL. O gate executado em 2026-07-01 retornou ΔAIC = `+27.9163419675` e ΔBIC = `+33.1999423146` para `RLL - ΛCDM`; portanto este apêndice registra apenas o contrato algébrico mínimo e marca os produtos de ajuste como `[VAZIO]`.

## Contrato algébrico preservado

Para um campo escalar canônico:

```text
rho_phi = 1/2 phidot^2 + V(phi)
p_phi   = 1/2 phidot^2 - V(phi)
H^2(a)  = H0^2 E^2(a)
E^2(a)  = Omega_m0 a^-3 + Omega_r0 a^-4 + Omega_Lambda0 + alpha f(a) S(a)
S(a)    = 1 / (1 + exp[-k(a-a_t)])
```

A reconstrução inversa em unidades reduzidas usa:

```text
V(a) = (3 H(a)^2 / kappa^2) * [1 + (1/3) d ln H / d ln a]
```

e, para ramo canônico não fantasma, exige `phidot^2 >= 0` e trajetória monotônica `phi(a)` antes de inverter numericamente `a(phi)`.

## Produtos não promovidos

- `[VAZIO]` Gráfico `V(phi)` vs. `phi`.
- `[VAZIO]` Prova dinâmica de que a logística emerge de solução de campo e não de parametrização empírica.
- `[VAZIO]` Inferência de domínio de parâmetros observacionalmente aceito para `alpha > 0`.

## Motivo

Publicar uma curva suave tipo “rocha escalonada” após um gate AIC/BIC desfavorável criaria falsa robustez. A microfísica permanece uma hipótese formal até novo gate multissonda completo.
