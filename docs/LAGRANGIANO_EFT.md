# Lagrangiano Efetivo - EFT minima do setor logistico RLL

Modulo: `docs/LAGRANGIANO_EFT.md`
Status: reconstrucao canonica minima conectada ao gate executavel `scripts/check_rll_background.py`.

## 1. Objetivo

O RLL possui um setor logistico de fundo cosmologico. Para que ele seja mais que uma parametrizacao fenomenologica, e preciso mostrar que existe uma reconstrucao efetiva compativel com campo escalar canonico no regime de baixa energia.

A acao minima e:

```text
S = integral d4x sqrt(-g) [ R/(16 pi G) + L_m + L_r + L_phi ]
L_phi = -1/2 g^{mu nu} partial_mu phi partial_nu phi - V(phi)
```

Esta convencao usa assinatura `(-,+,+,+)`. Para campo homogeneo:

```text
rho_phi = K + V
p_phi   = K - V
K       = phi_dot^2 / 2
w       = p_phi/rho_phi
```

Logo:

```text
K(a) = (1+w(a)) rho_phi(a)/2
V(a) = (1-w(a)) rho_phi(a)/2
```

## 2. Setor logistico RLL

O fundo logistico e:

```text
f(z) = 1/(1+exp((z-z_t)/w_t)), w_t > 0
rho_s(z) = Omega_s0 rho_c0 [ f(z) + (1-f(z))(1+z)^3 ]
p_s(z)   = - Omega_s0 rho_c0 f(z)
```

Portanto:

```text
w_eff(z) = -f(z) / [ f(z) + (1-f(z))(1+z)^3 ]
```

Esta correcao e central: o setor misto tem denominador de densidade. Assim, no alto redshift o termo `(1+z)^3` domina e `w_eff -> 0`; no baixo redshift, `w_eff` aproxima o regime de energia escura.

## 3. Reconstrucao do campo

Defina:

```text
E2(z) = Omega_m(1+z)^3 + Omega_Lambda + Omega_s0 [ f + (1-f)(1+z)^3 ]
Omega_s(z) = Omega_s0 [ f + (1-f)(1+z)^3 ] / E2(z)
```

A derivada canonica em relacao a `ln a` e:

```text
d phi / d ln a = M_Pl sqrt( 3 Omega_s(a) [1+w_eff(a)] )
```

O potencial parametrico fica:

```text
V(a)/(rho_c0) = 1/2 [1-w_eff(a)] Omega_s(a) E2(a)
```

E a energia cinetica parametrica:

```text
K(a)/(rho_c0) = 1/2 [1+w_eff(a)] Omega_s(a) E2(a)
```

O gate minimo e simplesmente:

```text
[1+w_eff(a)] Omega_s(a) >= 0
```

Esse gate e calculado pelo script como `kinetic_gate`.

## 4. Velocidade de som

Para campo escalar canonico:

```text
cs2_rest = 1
```

Para o fechamento fenomenologico de fundo usado na checagem minima:

```text
cs2_proxy(z) = f(z)
```

Como `0 <= f(z) <= 1`, o proxy permanece limitado. Isso nao substitui o tratamento completo de perturbacoes.

## 5. Comando executavel

```bash
python scripts/check_rll_background.py \
  --omega-m 0.315 \
  --omega-s0 0.059 \
  --zt 1.164 \
  --wt 0.405
```

Saida:

```text
results/rll_background_check.json
```

## 6. O que esta fechado

- Lagrangiano canonico minimo definido.
- `w_eff` corrigido com denominador de densidade do fluido misto.
- Reconstrucao parametrica `K(a)` e `V(a)` definida.
- Gate cinetico executavel conectado ao script.
- Proxy de velocidade de som limitado por construcao.

## 7. O que permanece TOKEN_VAZIO

- Inversao numerica `a(phi)` para escrever `V(phi)` explicitamente.
- Correcoes de loop e naturalidade.
- Equacoes de Boltzmann.
- Crescimento de estrutura `f_sigma8`.
- Evidencia Bayesiana completa.

## 8. Criterio de falsificacao deste bloco

Este bloco falha se, dentro do intervalo de parametros posterior defensavel:

```text
w_eff < -1
ou
[1+w_eff] Omega_s < 0
ou
cs2_proxy fora de [0,1]
```

Se isso ocorrer, o setor logistico precisa ser revisado antes de qualquer claim cosmologico forte.
