# Convenções Globais Canônicas — Relativity Living Light (RLL)

**Status:** norma canônica obrigatória para documentação derivada.

## 1) Definições canônicas

### 1.1 Função logística de transição

A forma canônica é:

```math
f(z)=\frac{1}{1+\exp\left((z-z_t)/w_t\right)},\quad w_t>0
```

Convenção operacional:
- `f(z)` controla a fração tipo DE do setor de superposição;
- `(1-f(z))` controla a fração tipo DM do mesmo setor.

### 1.2 Equação de estado do setor de superposição (`w_sup`)

Definição canônica completa:

```math
w_{\mathrm{sup}}(z)=\frac{p_{\mathrm{sup}}}{\rho_{\mathrm{sup}}}
=-\frac{f(z)}{f(z)+(1-f(z))(1+z)^3}
```

Aproximação de uso rápido (apenas quando explicitamente indicado no texto):

```math
w_{\mathrm{sup}}(z)\approx -f(z)
```

### 1.3 Equação de estado total (`w_total`)

Definição canônica:

```math
w_{\mathrm{total}}(z)=\frac{p_{\mathrm{tot}}}{\rho_{\mathrm{tot}}}
```

Com decomposição padrão:

```math
w_{\mathrm{total}}(z)=\sum_i \Omega_i(z)\,w_i(z)
```

onde `i` inclui os setores padrão e o setor de superposição.

## 2) Convenção de sinais

- Pressão tipo energia escura: `p<0`.
- Pressão tipo matéria fria: `p\approx 0`.
- Para o setor de superposição, usar:
  - `p_sup = -\rho_c\,\Omega_{s0}\,f(z)`;
  - `\rho_sup = \rho_c\,\Omega_{s0}\,[f(z)+(1-f(z))(1+z)^3]`.
- Portanto, `w_sup\in[-1,0]` no regime físico canônico.

## 3) Limites assintóticos esperados

Dada a forma logística acima:

- `z\gg z_t`  =>  `f(z)\to 0`  =>  setor de superposição tende a comportamento tipo matéria (`w_sup\to 0`).
- `z\ll z_t`  =>  `f(z)\to 1`  =>  setor de superposição tende a comportamento tipo energia escura (`w_sup\to -1`).

Regra editorial curta:
- **Canônico:** `f=1 → DE` e `f=0 → DM`.
- Qualquer texto com mapeamento invertido deve ser marcado como histórico, hipótese alternativa ou corrigido.

## 4) Escopo de aplicação

Esta norma deve ser referenciada no topo de documentos derivados (README, `newadd/*`, FAQs, comparativos e materiais de síntese) para evitar deriva semântica entre versões.
