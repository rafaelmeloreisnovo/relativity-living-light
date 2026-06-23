# Verificacao de Estabilidade - RLL logistic sector

Modulo: `docs/ESTABILIDADE_GHOST_CHECK.md`
Status: gate minimo executavel conectado a `scripts/check_rll_background.py`.

Este arquivo substitui a nota puramente conceitual por um criterio operacional minimo para o setor logistico RLL. O objetivo nao e declarar validacao completa de perturbacoes; e fechar a primeira barreira fisica: cinetica efetiva nao negativa, ausencia de cruzamento abaixo de w=-1 e velocidade de som prescrita dentro de [0,1].

## 1. Setor de fundo

A densidade efetiva do setor logistico e tratada como:

```text
rho_s(z) = Omega_s0 rho_c0 [ f(z) + (1-f(z))(1+z)^3 ]
p_s(z)   = - Omega_s0 rho_c0 f(z)
f(z)     = 1/(1+exp((z-z_t)/w_t)), with w_t > 0
```

Assim, a equacao de estado efetiva do fluido misto nao e simplesmente `-f`; ela e:

```text
w_eff(z) = p_s/rho_s = -f(z) / [ f(z) + (1-f(z))(1+z)^3 ]
```

Essa forma e importante porque garante que o limite de alto redshift seja matter-like (`w_eff -> 0`) e o limite de baixo redshift seja dark-energy-like (`w_eff -> -1`, sem cruzar abaixo de -1 para os parametros fisicos).

## 2. Criterio cinetico minimo

Para reconstruir o setor como campo escalar canonico:

```text
K(a) = (1+w_eff(a)) rho_s(a) / 2
V(a) = (1-w_eff(a)) rho_s(a) / 2
```

O primeiro gate fisico e:

```text
(1+w_eff) Omega_s(a) >= 0
```

O script calcula exatamente esse fator como `kinetic_gate`.

## 3. Velocidade de som

Ha duas leituras distintas:

1. Campo escalar canonico no referencial de repouso: `cs2 = 1`.
2. Fechamento fenomenologico suave usado no pipeline minimo: `cs2_proxy = f(z)`.

O gate executavel verifica que:

```text
0 <= cs2_proxy <= 1
```

A analise completa de perturbacoes, Boltzmann solver e `f_sigma8` permanece marcada como `TOKEN_VAZIO`.

## 4. Comando

```bash
python scripts/check_rll_background.py \
  --omega-m 0.315 \
  --omega-s0 0.059 \
  --zt 1.164 \
  --wt 0.405
```

Saida principal:

```text
results/rll_background_check.json
```

## 5. Resultado esperado para os parametros centrais

Para `Omega_m=0.315`, `Omega_s0=0.059`, `z_t=1.164`, `w_t=0.405`, em `0 <= z <= 5`, a execucao local retorna:

```json
{
  "kinetic_gate_non_negative": true,
  "w_eff_above_minus_one": true,
  "cs2_proxy_bounded": true,
  "growth_solver": "TOKEN_VAZIO"
}
```

## 6. Fronteira honesta

Este fechamento sobe o RLL de esboco fisico para gate minimo de consistencia de fundo. Ainda nao substitui:

- MCMC real;
- nested sampling;
- matriz completa de covariancia;
- crescimento de estrutura;
- equacoes de Boltzmann;
- comparacao CMB completa.
