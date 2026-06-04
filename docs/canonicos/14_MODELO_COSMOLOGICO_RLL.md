# 14 — Modelo Cosmológico RLL

**Status:** canônico complementar  
**Origem:** extraído de `docs/canonicos/BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md`  
**Função:** registrar a equação-mãe, hipóteses, adversários científicos e condições de falsificação.

---

## 1. Equação-mãe canônica [C/H]

```math
E^2(a) = \Omega_r a^{-4} + \Omega_m a^{-3} + \Omega_\Lambda
+ \Omega_{s0}\,[f(a) + (1-f(a))a^{-3}]
+ \Omega_{B0}a^{-4} + \Omega_{P0}a^{-4}
```

## 2. Transição logística

```math
f(z) = \frac{1}{1 + \exp((z - z_t)/w_t)}, \qquad a = \frac{1}{1+z}
```

Leitura operacional:

- baixo redshift: setor de superposição se comporta como energia escura;
- alto redshift: setor migra para ramo tipo matéria;
- `ΩB0` e `ΩP0` representam setores magnético e plasmático, nulos no baseline quando não usados.

## 3. Impressão digital do RLL [H]

A hipótese distintiva é acoplar coerência do setor escuro ao ambiente magnético:

```math
\Omega_{s0} \to \Omega_{s0}\,[1 + \alpha_B(\Omega_{B0}a^{-4})^\beta]
```

O ponto testável é verificar se ambientes magnéticos distintos deixam assinatura observacional que não seja absorvida por w0waCDM genérico.

## 4. Equação de estado efetiva

Com:

```math
g(a)=f(a)+(1-f(a))a^{-3}
```

então:

```math
w_{\rm eff}(a) = -1 - \frac{1}{3}\frac{d\ln g}{d\ln a}
```

com:

```math
g'(a)=f'(a)(1-a^{-3})-3(1-f(a))a^{-4}
```

## 5. Adversário científico correto

O adversário principal do RLL não é apenas ΛCDM puro, mas **w0waCDM**, porque DESI DR2 e combinações com CMB/SNe favorecem testes de energia escura dinâmica.

## 6. Estado honesto atual

Com dados reais e erros diagonais no recorte atual descrito no documento-mãe:

```text
ΛCDM: χ²/dof ≈ 0.94
RLL : χ²/dof ≈ 1.12
Δχ² = −5.5
```

Leitura: RLL é computável, testável e não-falsificado no recorte, mas não supera ΛCDM nos parâmetros atuais. Isso preserva a integridade científica do projeto.

## 7. Falsificadores prioritários

- ajuste conjunto H(z)+BAO+fσ8+CMB;
- comparação direta contra w0waCDM;
- covariância BAO 2×2 por tracer;
- r_d derivado dos parâmetros;
- teste de assinatura magnética local/global.

---

*RLL = hipótese testável, não reivindicação absoluta.*