# RAFAELIA `sqrt3_2` Kernel — geometria, projeção e decaimento

Status: **invariante operacional testável / núcleo técnico restrito**.

Este documento formaliza o uso de

```text
h = sqrt(3) / 2 ≈ 0.8660254037844386
```

como constante de engenharia para contextos em que há simetria de 30°/60°/120°, malha triangular/hexagonal, projeção vetorial ou contração recursiva. A regra epistemológica é deliberadamente conservadora: `sqrt(3)/2` organiza muitos mecanismos, mas não substitui prova, medição, distribuição estatística ou fórmula de domínio.

## Contrato do kernel

| Campo | Definição |
|---|---|
| Nome canônico | `RAFAELIA_H_KERNEL` |
| Constante | `h = sqrt(3)/2` |
| Fixed-point Q16.16 | `H_Q16 = round(h * 65536) = 56756` |
| Inverso | `2/sqrt(3) ≈ 1.1547005383792517` |
| Potência estrutural | `h^2 = 3/4` |
| Meia-vida discreta | `ln(0.5)/ln(h) ≈ 4.81884167930642 ciclos` |
| Queda para 10% | `ln(0.1)/ln(h) ≈ 16.00784555930218 ciclos` |
| Queda para 1% | `ln(0.01)/ln(h) ≈ 32.01569111860436 ciclos` |
| Soma geométrica | `1/(1-h) ≈ 7.464101615137752` |

## Limites de verdade

- **Forte:** altura de triângulo equilátero unitário, espaçamento vertical de grade triangular/hexagonal, senos/cossenos de 30° e 60°, projeção angular e filtros de contração.
- **Médio:** suavização operacional de risco, estoque, cache, latência e memória quando o fator de amortecimento é uma escolha de projeto explícita.
- **Fraco/perigoso:** tratar `sqrt(3)/2` como `1σ`, z-score de 95%, densidade total de empacotamento ou prova universal sem derivação intermediária.

A densidade ótima de empacotamento de círculos em 2D é `pi/(2*sqrt(3)) ≈ 0.9068996821171089`; `sqrt(3)/2` entra na geometria da célula, não como a densidade final.

## Módulo 1 — `geometry_hex_grid`

**Entrada:** `row`, `col`, `side`.

**Fórmula:**

```text
x = side * (col + 0.5 * (row & 1))
y = side * h * row
```

**Saída:** coordenada axial/offset para malha triangular ou visualização hexagonal 2D.

**Teste mínimo:** com `side=1`, a diferença vertical entre duas linhas adjacentes é `h`.

**Limite:** é geometria euclidiana plana; projeções esféricas, mapas geodésicos e grids com distorção exigem correção.

## Módulo 2 — `recursive_decay_filter`

**Entrada:** estado acumulado `R_n` e entrada `Entrada_n`.

**Fórmula-mãe:**

```text
R_{n+1} = Entrada_n + h * R_n
```

**Caso homogêneo:**

```text
F_n = F_0 * h^n
```

**Saída:** memória com decaimento suave, estável e mensurável.

**Teste mínimo:** `h^2` deve ser `0.75`; a soma infinita deve tender a `1/(1-h)` quando `|h| < 1`.

**Limite:** sem normalização, uma entrada constante `1` converge para `7.464101615...`; use `(1-h)*Entrada_n + h*R_n` quando a saída deva permanecer na escala da entrada.

## Módulo 3 — `signal_6fold_projection`

**Entrada:** vetor ou amostra angular em eixos 30°/60°/120°.

**Fórmula:**

```text
cos(30°) = sin(60°) = h
sin(30°) = cos(60°) = 0.5
```

**Tabela fixed-point Q16.16:**

```text
H_Q16    = 56756
HALF_Q16 = 32768
project_q16(x) = (x * H_Q16) >> 16
```

**Saída:** projeções direcionais para filtros 6-fold, decomposição angular, FFT em simetrias hexagonais e kernels freestanding.

**Limite:** fixed-point acumula erro de arredondamento; caminhos críticos devem declarar escala e saturação.

## Módulo 4 — `regression_angle_map`

**Entrada:** coeficiente `R²` ou ângulo entre vetor observado e vetor projetado.

**Fórmula:**

```text
R² = cos²(theta)
sqrt(1 - R²) = sin(theta)
```

Quando `theta = 60°`, `sin(theta) = h` e `R² = 0.25`.

**Saída:** leitura geométrica de projeção/erro, sem converter diretamente em probabilidade normal.

**Limite:** `sqrt(3)/2` não é `1σ`; `1σ` normal cobre cerca de 68.27%, enquanto `h` é uma razão trigonométrica.

## Módulo 5 — `risk_buffer_smoother`

**Entrada:** demanda/risco bruto e buffer anterior.

**Fórmula operacional:**

```text
Buffer_{novo} = Demanda + h * Buffer_{anterior}
Risco_{filtrado} = Risco_{bruto} * h^ciclos_estaveis
```

**Saída:** amortecimento de ruído para filas, cache, estoque adaptativo, watchdog e latência.

**Limite:** não substitui fórmulas clássicas como `SS = z * sigma * sqrt(LT)`; é heurística de suavização quando calibrada e auditada.

## Rotas reversas e rollback

Contração e reconstrução formam um par explícito:

```text
forward:  x_{n+1} = h * x_n
reverse:  x_{n-1} = x_n * (2/sqrt(3))
```

Para FAILSAFE/FAILOVER/ROLLBACK, registre sempre:

1. escala (`float64`, Q16.16, Q32.32 ou inteiro nativo);
2. número de ciclos aplicados;
3. saturação/overflow esperado;
4. tolerância numérica;
5. estado anterior quando reversão aproximada for necessária.

## Retroalimentação

- **F_ok:** `sqrt(3)/2` é invariante direto em geometria 30°/60°/hexagonal e operador válido de contração com `|h| < 1`.
- **F_gap:** não deve ser confundido com `1σ`, z-score, densidade total de empacotamento ou prova universal sem fórmula intermediária.
- **F_next:** implementar kernels de baixo nível sem heap para Q16.16/Q32.32, com testes de saturação, rollback e comparação contra `float64`.

## Extensão matemática — complexos, Eisenstein e simetria de ordem 6

A leitura matemática mais forte além do triângulo é a rotação complexa:

```text
e^(i*pi/3) = cos(60°) + i*sin(60°) = 1/2 + i*sqrt(3)/2
```

Esse ponto é vértice do hexágono unitário e base para raízes da unidade de ordem 6, análise harmônica, rotações discretas, números de Eisenstein e reticulado triangular no plano complexo. Uma base executável equivalente é:

```text
a = (1, 0)
b = (1/2, sqrt(3)/2)
(x, y) = m*a + n*b
```

Essa forma conecta álgebra, redes triangulares, discretização de superfícies, autômatos celulares hexagonais e códigos geométricos sem exigir interpretação cosmológica forte.

## Extensão cosmológica — pivô diagnóstico, não constante fundamental

Em cosmologia, `sqrt(3)/2` deve entrar como operador, pivô, malha ou hipótese testável. Ele não é registrado aqui como constante cosmológica fundamental.

O pivô operacional proposto é:

```text
a_h = sqrt(3)/2
z_h = 1/a_h - 1 = 2/sqrt(3) - 1 ≈ 0.15470053837925168
```

Uso permitido:

```text
H_LCDM(z_h)
H_CPL(z_h)
H_RLL(z_h)
Delta_chi2 = chi2_LCDM - chi2_modelo_com_pivo_h
```

Interpretação:

- se `Delta_chi2 > 0`, o modelo com pivô reduziu o chi-quadrado no conjunto testado;
- se `Delta_chi2 < 0`, piorou;
- se empata dentro da tolerância estatística, o pivô é apenas linguagem geométrica/diagnóstica, não descoberta.

O modelo base `LambdaCDM` plano de 6 parâmetros permanece uma referência observacional robusta; dados DESI DR2/BAO e combinações com CMB/SNe podem tensionar a hipótese de energia escura constante em parametrizações dinâmicas, mas isso não transforma `sqrt(3)/2` em constante física universal. Portanto, o status correto é `TOKEN_VAZIO` para qualquer alegação de nova física até comparação reprodutível com BAO, supernovas, CMB e resíduos.

Fontes de fronteira usadas para esta extensão:

- Planck Collaboration, `Planck 2018 results. VI. Cosmological parameters`, arXiv:1807.06209, A&A 641 A6 (2020): https://arxiv.org/abs/1807.06209
- DESI Collaboration, `DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints`, arXiv:2503.14738, Phys. Rev. D 112, 083515 (2025): https://arxiv.org/abs/2503.14738
- DESI DR2 guide page, March 19 2025: https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/

## Implementação freestanding Q16.16

O primeiro kernel executável foi colocado no runtime C freestanding:

```text
core/lowlevel_runtime/include/pantheon_freestanding.h
core/lowlevel_runtime/c/pantheon_freestanding.c
```

API inicial:

```text
rll_sqrt3_2_project_q16(x_q16)
rll_sqrt3_2_reverse_q16(x_q16)
rll_sqrt3_2_decay_q16(state_q16, input_q16)
rll_sqrt3_2_hex_grid_q16(row, col, side_q16)
rll_sqrt3_2_cosmo_pivot_q16()
rll_sqrt3_2_spiral_step_q16(step, radius0_q16)
```

Garantias do escopo atual:

- sem `malloc`, sem heap e sem GC;
- sem dependência de `stdlib`, `stdio` ou `string.h` no módulo freestanding;
- fixed-point Q16.16 explícito;
- rota de rollback aproximada por `2/sqrt(3)`;
- pivô cosmológico exportado como diagnóstico (`a_h`, `z_h`), não como constante fundamental.
- evolução espiral discreta por setores de 60° com raio `r_n = r_0*(sqrt(3)/2)^n` e altura de triângulo equilátero `h_n = r_n*sqrt(3)/2`, sem trigonometria runtime nem heap.
