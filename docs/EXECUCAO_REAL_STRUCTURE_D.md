# Execução real (Structure-D): comando, artefatos, AIC/BIC e troubleshooting

Este guia descreve a execução da validação real do pipeline `structure_d` usando o perfil de dados reais definido em `data/pipelines/structure_d/datasets_config.json` e o script `data/pipelines/structure_d/run_all_real.py`.

## 1) Comando de execução real

Use a execução como módulo Python a partir da raiz do repositório:

```bash
python -m data.pipelines.structure_d.run_all_real
```

Opcionalmente, para forçar explicitamente o perfil real:

```bash
STRUCTURE_D_PROFILE=structure_d_real_validation \
python -m data.pipelines.structure_d.run_all_real
```

### Ajuste de custo computacional (opcional)

O script usa otimização por `differential_evolution`. É possível reduzir/elevar iterações via variáveis de ambiente:

```bash
STRUCTURE_D_MAXITER_LCDM=120 STRUCTURE_D_MAXITER_RLL=150 \
python -m data.pipelines.structure_d.run_all_real
```

## 2) Artefatos esperados

Ao finalizar, o script grava:

- `results/structure_d/model_comparison_real.csv`

E imprime no terminal:

- tabela com colunas de comparação (`model`, `chi2`, `AIC`, `BIC`, `N`, `k`, etc.);
- linha final `Wrote: .../results/structure_d/model_comparison_real.csv`.

## 3) Interpretação de AIC/BIC nesta execução

No `run_all_real.py`, os modelos comparados são:

- `LCDM` com `k = 4` parâmetros;
- `RLL_like+AGN` com `k = 7` parâmetros.

O total observacional usado no cálculo é:

- `N = len(real_hz) + len(real_bao) + len(real_cmb_shift)`.

As fórmulas (definidas em `likelihood.py`) são:

- `AIC = chi2 + 2k`
- `BIC = chi2 + k ln(N)`

### Leitura prática

- Menor AIC/BIC indica melhor compromisso entre ajuste e complexidade.
- `RLL_like+AGN` precisa reduzir `chi2` o suficiente para compensar a penalidade de `k` maior.
- Compare preferencialmente modelos rodados no mesmo conjunto de dados (mesmo `N` e mesmo perfil ativo).

## 4) Relação com `datasets_config.json`

A execução real depende do profile:

- `structure_d_real_validation`

com datasets ativos:

- `real_hz`
- `real_bao`
- `real_cmb_shift`

Esses itens vêm de `data/pipelines/structure_d/datasets_config.json`, incluindo caminhos e mapeamento de colunas/chaves.

## 5) Troubleshooting de dependências

Se ocorrer erro de import (ex.: `ModuleNotFoundError`), instale dependências mínimas na venv ativa:

```bash
python -m pip install -r requirements.txt
```

Problemas comuns:

- `No module named numpy/scipy/pandas`:
  - instale com `pip install -r requirements.txt`.
- erro ao usar import relativo (`from .data_access import ...`) ao executar arquivo diretamente:
  - execute como módulo (`python -m data.pipelines.structure_d.run_all_real`), não como caminho de arquivo.
- ausência de artefato em `results/structure_d/`:
  - verifique se a execução iniciou na raiz do repositório;
  - confirme permissões de escrita no diretório `results/`;
  - confira se o profile ativo inclui `real_hz`, `real_bao` e `real_cmb_shift`.

## 6) Referências diretas

- Configuração de datasets e profiles: `data/pipelines/structure_d/datasets_config.json`
- Execução real e escrita do CSV final: `data/pipelines/structure_d/run_all_real.py`
