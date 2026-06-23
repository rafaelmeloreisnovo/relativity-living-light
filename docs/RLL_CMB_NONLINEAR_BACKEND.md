# RLL CMB and nonlinear matter backend

Status: adaptador executavel para engines externas reais.

O arquivo principal e:

```bash
python scripts/run_cmb_power_backend.py --engine auto --model lcdm --nonlinear
```

## 1. O que este bloco faz

O script tenta usar engines cientificas reais:

```text
CAMB
CLASS/classy
```

Quando uma delas esta instalada, o script calcula:

- espectros CMB `Cl` ate `lmax`;
- espectro de materia `P(k,z)`;
- modo nao linear via Halofit/HMcode quando o backend oferece suporte.

## 2. Comandos

LCDM com espectro nao linear:

```bash
python scripts/run_cmb_power_backend.py \
  --engine auto \
  --model lcdm \
  --nonlinear
```

w0wa com espectro nao linear:

```bash
python scripts/run_cmb_power_backend.py \
  --engine auto \
  --model w0wa \
  --w0 -1.0 \
  --wa 0.0 \
  --nonlinear
```

RLL exato:

```bash
python scripts/run_cmb_power_backend.py \
  --engine auto \
  --model rll \
  --nonlinear
```

Para `rll`, o script registra `TOKEN_VAZIO` se o backend for stock CAMB/CLASS, porque o setor logistico RLL exige modulo de background e perturbacoes customizado. Isso e intencional: evita tratar uma aproximacao w0wa como se fosse RLL exato.

## 3. Saida

```text
results/cmb_power_backend_summary.json
```

## 4. Fronteira honesta

Este arquivo fecha o caminho operacional para CMB e espectro nao linear via engine real. Ele nao declara que o RLL exato ja foi portado para CAMB/CLASS.

O que esta pronto:

- adaptador executavel;
- tentativa automatica CAMB -> CLASS;
- CMB e P(k) nao linear para LCDM/w0wa quando backend existe;
- bloqueio honesto para RLL exato em backend stock.

O que permanece `TOKEN_VAZIO`:

- modulo RLL customizado em CAMB/CLASS;
- perturbacoes RLL exatas;
- likelihood Planck/ACT/SPT completa;
- covariancia completa de lensing e CMB.

## 5. Referencias de metodo

- CAMB/CLASS sao engines padrao de Boltzmann para CMB e materia.
- Halofit e HMcode sao aproximacoes/implementacoes usadas para espectro de materia nao linear.
- O repo usa este adaptador para nao reinventar, de forma fragil, uma engine que ja existe e e revisada pela comunidade.
