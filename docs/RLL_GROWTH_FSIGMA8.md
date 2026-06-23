# RLL Growth Gate - linear f_sigma8

Status: solver linear executavel conectado a `scripts/check_rll_growth.py`.

Este modulo fecha o primeiro nivel de crescimento de estrutura para o RLL: fator de crescimento linear `D(a)`, taxa `f=dlnD/dlna` e observavel `f_sigma8(z)`.

## 1. Equacao usada

O solver integra, em `x=ln a`:

```text
D_xx + [2 + dlnH/dlna] D_x - 1.5 Omega_m(a) D = 0
```

com condicao inicial em regime de materia:

```text
D(a_ini)=a_ini
D_x(a_ini)=a_ini
```

A normalizacao final e:

```text
D(a=1)=1
f(a)=D_x/D
f_sigma8(z)=f(z) sigma8_0 D(z)
```

## 2. Modelos comparados

O script calcula os tres fundos:

```text
lcdm
w0wa
rll
```

O RLL usa o mesmo setor logistico aplicado no gate de fundo:

```text
E2_RLL = Omega_m a^-3 + Omega_Lambda + Omega_s0 [ f + (1-f)a^-3 ]
f(z)=1/(1+exp((z-z_t)/w_t))
```

## 3. Comando principal

```bash
python scripts/check_rll_growth.py --model all
```

Saidas:

```text
results/rll_growth_fsigma8_summary.json
results/rll_growth_fsigma8_predictions.csv
```

## 4. Com dado real opcional

O arquivo CSV pode ter colunas:

```text
z,fsigma8,sigma
```

ou equivalentes:

```text
redshift,value,error
```

Comando:

```bash
python scripts/check_rll_growth.py \
  --model all \
  --data data/real/cosmology/fsigma8_growth.csv
```

Quando `--data` e informado, o script calcula `chi2_fsigma8` para cada modelo.

## 5. Resultado de sanidade local

Com `Omega_m=0.315`, `sigma8_0=0.811` e parametros centrais do RLL, a validacao local mostra:

```text
LCDM: f(z=0) aproximadamente 0.527
RLL : f(z=0) aproximadamente 0.525
```

Esse intervalo e coerente com crescimento linear de fundo em GR para `Omega_m` proximo de 0.315.

## 6. Fronteira honesta

Este bloco e valido como gate linear de fundo. Ele ainda nao e:

- Boltzmann solver completo;
- CMB likelihood;
- nonlinear power spectrum;
- Halofit;
- baryonic feedback;
- tratamento de covariancia completa de surveys.

Esses pontos permanecem `TOKEN_VAZIO` ate implementacao especifica.

## 7. Valor cientifico imediato

Antes, `f_sigma8` era uma lacuna. Agora existe uma previsao computavel e testavel para `LCDM`, `w0wa` e `RLL`. Isso transforma crescimento de estrutura de promessa textual em gate falsificavel minimo.
