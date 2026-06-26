# RLL — Output Stem CLI Gap

**Status:** lacuna operacional identificada antes de executar robust fit.  
**Escopo:** impedir sobrescrita acidental dos artefatos canônicos em `results/structure_d/`.

---

## 1. Fato observado

O pipeline possui a função:

```python
run_joint_likelihood(output_stem: str = "joint_real_likelihood")
```

Essa função escreve os arquivos com base em `output_stem`:

```text
results/structure_d/{output_stem}.csv
results/structure_d/{output_stem}.json
results/structure_d/{output_stem}_covariance_manifest.json
```

Porém o `main()` atual chama:

```python
payload = run_joint_likelihood()
```

Sem ler uma variável como `STRUCTURE_D_JOINT_OUTPUT_STEM` e sem aceitar argumento CLI.

---

## 2. Risco

Se uma bateria robusta for executada diretamente com:

```bash
STRUCTURE_D_JOINT_MAXITER=100 python data/pipelines/structure_d/joint_real_likelihood.py
```

ela tende a escrever no `output_stem` padrão:

```text
joint_real_likelihood
```

Isso pode sobrescrever ou substituir os artefatos canônicos atuais:

```text
results/structure_d/joint_real_likelihood.csv
results/structure_d/joint_real_likelihood.json
results/structure_d/joint_real_likelihood_covariance_manifest.json
```

Mesmo com escrita atômica e backups, isso cria risco de confusão entre:

- smoke atual;
- robust fit;
- seeds diferentes;
- maxiter diferente;
- resultados canônicos;
- resultados experimentais.

---

## 3. Classificação RAFAELIA

```text
estado = TOKEN_VAZIO_CLI_OUTPUT_STEM
objeto = output stem versionado para execuções robustas
risco_se_ignorar = sobrescrita ou mistura de artefatos smoke e robust fit
valor_da_lacuna = protege rastreabilidade e impede falso claim por arquivo reusado
claim_allowed = false
```

---

## 4. Correção recomendada

Antes de executar robust fit, criar PR específico para uma destas opções:

### Opção A — variável de ambiente

```python
output_stem = os.environ.get("STRUCTURE_D_JOINT_OUTPUT_STEM", "joint_real_likelihood")
payload = run_joint_likelihood(output_stem=output_stem)
```

### Opção B — argumento CLI

```bash
python data/pipelines/structure_d/joint_real_likelihood.py \
  --output-stem joint_real_likelihood_seed_1_maxiter_100
```

### Opção C — wrapper robusto separado

Criar script:

```text
scripts/run_structure_d_robust_fit_matrix.py
```

Responsável por:

- iterar seeds;
- definir maxiter;
- gerar output stem versionado;
- nunca sobrescrever canônico;
- consolidar tabela agregada.

---

## 5. Regra de bloqueio

Enquanto o output stem versionado não estiver implementado ou garantido por wrapper:

```text
robust_fit_execution_allowed = false
```

Permitido apenas:

- documentação;
- plano de execução;
- checklist;
- dry-run conceitual;
- criação de issue/PR de correção.

---

## 6. Critério de aceite

A lacuna é fechada quando houver pelo menos um caminho operacional comprovado para gerar arquivos como:

```text
results/structure_d/joint_real_likelihood_seed_1_maxiter_100.json
results/structure_d/joint_real_likelihood_seed_2_maxiter_100.json
...
results/structure_d/joint_real_likelihood_seed_10_maxiter_100.json
```

sem alterar o canônico:

```text
results/structure_d/joint_real_likelihood.json
```

---

## 7. R3

```text
F_ok   = lacuna de output_stem identificada antes de qualquer robust fit.
F_gap  = ainda falta PR/código/wrapper para output versionado.
F_next = criar matriz de ablação e manifesto de figuras/tabelas para preparar o paper sem executar fit.
```
