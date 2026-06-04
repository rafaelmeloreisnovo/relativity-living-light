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

## 7) Verossimilhança conjunta de quatro eixos reais

Para a conta pedida como próximo passo científico — `H(z) + DESI DR2 BAO + fσ8 + CMB shift` no mesmo vetor de parâmetros — use o novo consumidor local-first:

```bash
python -m data.pipelines.structure_d.joint_real_likelihood
```

### Entradas usadas

As rotas de alimentação estão fixadas em `data/inputs/cosmology_joint/joint_real_inputs_manifest.json` e apontam para:

- `data/real/Hz_data_real.csv`
- `data/real/cosmology/desi_dr2_bao_primary_points.csv`
- `data/real/cosmology/desi_dr2_bao_covariance_summary.csv`
- `data/real/cosmology/fsigma8_growth_real.csv`
- `data/real/CMB_shift_real.json`

### O que mudou em relação ao script real anterior

- O BAO DESI DR2 usa `DV/rd`, `DM/rd` e `DH/rd`, em vez de reduzir tudo a `DV/rs`.
- A matriz de covariância DESI é materializada como uma matriz `13×13` a partir dos erros diagonais e dos blocos `DM/DH` correlacionados já presentes no repositório. O ponto isotrópico BGS permanece diagonal porque não há par `DM/DH` para ele na tabela primária local.
- `r_d` é derivado dos parâmetros `H0`, `Ωm` e `Ωb h²` por uma aproximação calibrada leve, em vez de ficar fixo como constante global.
- O bloco de crescimento `fσ8` entra junto com expansão, BAO e CMB no mesmo `χ²`.
- Os resultados são escritos com substituição atômica e backup `*.bak` quando já existe saída anterior.

### Artefatos esperados

- `results/structure_d/joint_real_likelihood.csv`
- `results/structure_d/joint_real_likelihood.json`
- `results/structure_d/joint_real_likelihood_covariance_manifest.json`

### Interpretação disciplinada

A saída deve ser lida como comparação operacional por `χ²`, AIC e BIC. Ela não autoriza, sozinha, afirmar superioridade do RLL sobre ΛCDM. Se o ajuste RLL reduzir `χ²`, a redução ainda precisa compensar a penalidade dos parâmetros extras em AIC/BIC e sobreviver a testes com produtos externos completos quando eles forem materializados.

## 8) Varredura sintético → real, failover e rollback

Antes de uma execução científica, rode a auditoria de materialização para garantir que datasets de fixture/sintéticos estejam roteados para uma contraparte real ou explicitamente marcados como inventário pendente:

```bash
python tools/real_data_materialization_audit.py
```

A auditoria varre a configuração `Structure-D` e arquivos em `data/` até cinco níveis de caminho procurando marcadores como `synthetic`, `synth`, `mock`, `example`, `fixture` e `local_input`. Ela não apaga fixtures: elas permanecem como rollback/regressão, enquanto rotas produtivas devem apontar para `data/real/**` ou URL externa documentada.

Artefatos esperados:

- `results/audit/real_data_materialization_audit.csv`
- `results/audit/real_data_materialization_audit.json`
- `results/audit/real_data_materialization_audit.md`

Na versão atual, as rotas configuradas cobertas são:

- `hz` e `hz_cov_synth` → `real_hz` (`data/real/Hz_data_real.csv`)
- `fsigma8` e `fsigma8_cov_synth` → `real_fsigma8` (`data/real/cosmology/fsigma8_growth_real.csv`)
- `real_bao` legado → `real_desi_dr2_bao` (`data/real/cosmology/desi_dr2_bao_primary_points.csv`)

Se uma rota real falhar, a política é **não preencher com número inventado**: manter o fixture como fallback de teste, marcar a rota como pendente e restaurar o `*.bak` do artefato se a escrita anterior tiver sido substituída.
