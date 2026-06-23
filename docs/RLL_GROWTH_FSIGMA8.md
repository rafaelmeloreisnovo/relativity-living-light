# RLL Growth Gate - linear f_sigma8

Status: solver linear executavel conectado a `scripts/check_rll_growth.py` e ao CSV real `data/real/cosmology/fsigma8_growth.csv`.

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

O CSV real default e:

```text
data/real/cosmology/fsigma8_growth.csv
```

Saidas:

```text
results/rll_growth_fsigma8_summary.json
results/rll_growth_fsigma8_predictions.csv
```

## 4. Resultado materializado localmente

Com `Omega_m=0.315`, `Omega_s0=0.059`, `z_t=1.164`, `w_t=0.405`, `sigma8_0=0.811` e 7 pontos reais em diagonal simples:

```text
lcdm: chi2_fsigma8 = 5.3737848935179695
w0wa: chi2_fsigma8 = 5.3737848935179695
rll : chi2_fsigma8 = 4.280773157819194
```

Leitura honesta: neste gate diagonal minimo, RLL fica melhor que LCDM/w0wa nos parametros pontuais escolhidos, mas isso ainda nao e evidencia bayesiana nem MCMC.

## 5. Com dado real alternativo

O arquivo CSV pode ter colunas:

```text
z,fsigma8,sigma
```

ou equivalentes:

```text
redshift,value,error
z,fs8,sigma
```

Comando:

```bash
python scripts/check_rll_growth.py \
  --model all \
  --data data/real/cosmology/fsigma8_growth.csv
```

Quando `--data` e informado, o script calcula `chi2_fsigma8` para cada modelo.

## 6. Fronteira honesta

Este bloco e valido como gate linear de fundo. Ele ainda nao e:

- Boltzmann solver completo;
- CMB likelihood;
- nonlinear power spectrum;
- Halofit/HMcode direto;
- baryonic feedback;
- tratamento de covariancia completa de surveys.

Esses pontos sao tratados no adaptador `scripts/run_cmb_power_backend.py` e permanecem `TOKEN_VAZIO` para RLL exato ate haver modulo customizado em CAMB/CLASS.

## 7. Valor cientifico imediato

Antes, `f_sigma8` era uma lacuna. Agora existe uma previsao computavel e testavel para `LCDM`, `w0wa` e `RLL`, ligada a dados observacionais reais e com `chi2_fsigma8` gerado.
