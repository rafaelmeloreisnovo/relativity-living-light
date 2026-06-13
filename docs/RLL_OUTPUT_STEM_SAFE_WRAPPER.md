# RLL — Output Stem Safe Wrapper

**Status:** rota segura implementada para execuções versionadas do Structure-D joint likelihood.  
**Escopo:** documenta `scripts/run_structure_d_joint_likelihood.py`; não altera dados, fórmulas, resultados canônicos ou claim policy.

---

## 1. O que foi fechado

A lacuna `TOKEN_VAZIO_CLI_OUTPUT_STEM` tinha o risco de uma execução robusta escrever no stem canônico:

```text
results/structure_d/joint_real_likelihood.json
```

Foi criado um wrapper seguro:

```text
scripts/run_structure_d_joint_likelihood.py
```

Ele chama internamente:

```python
run_joint_likelihood(output_stem=...)
```

sem alterar o pipeline científico.

---

## 2. Como usar via variável de ambiente

```bash
STRUCTURE_D_JOINT_OUTPUT_STEM="joint_real_likelihood_seed_1_maxiter_100" \
STRUCTURE_D_JOINT_SEED=1 \
STRUCTURE_D_JOINT_MAXITER=100 \
python scripts/run_structure_d_joint_likelihood.py
```

Saídas esperadas:

```text
results/structure_d/joint_real_likelihood_seed_1_maxiter_100.csv
results/structure_d/joint_real_likelihood_seed_1_maxiter_100.json
results/structure_d/joint_real_likelihood_seed_1_maxiter_100_covariance_manifest.json
```

---

## 3. Como usar via argumento CLI

```bash
STRUCTURE_D_JOINT_SEED=1 \
STRUCTURE_D_JOINT_MAXITER=100 \
python scripts/run_structure_d_joint_likelihood.py \
  --output-stem joint_real_likelihood_seed_1_maxiter_100
```

O argumento CLI tem precedência sobre `STRUCTURE_D_JOINT_OUTPUT_STEM`.

---

## 4. Trava de segurança

O wrapper rejeita stems que contenham:

- vazio;
- `/`;
- `\\`;
- `.` ou `..`;
- path traversal;
- extensões `.json`, `.csv` ou `.tsv`.

Isso força o output a permanecer como stem simples dentro de:

```text
results/structure_d/
```

---

## 5. Testes adicionados

Arquivo:

```text
tests/test_structure_d_output_stem_wrapper.py
```

Cobre:

- stem válido;
- rejeição de caminhos e extensões;
- default canônico quando variável ausente;
- leitura de `STRUCTURE_D_JOINT_OUTPUT_STEM`;
- precedência do argumento CLI sobre variável de ambiente.

---

## 6. Comando robust-fit recomendado atualizado

```bash
for seed in 1 2 3 4 5 6 7 8 9 10; do
  STRUCTURE_D_JOINT_SEED=$seed \
  STRUCTURE_D_JOINT_MAXITER=100 \
  python scripts/run_structure_d_joint_likelihood.py \
    --output-stem "joint_real_likelihood_seed_${seed}_maxiter_100"
done
```

---

## 7. Limites preservados

Esta rota:

- não altera `data/real/**`;
- não altera fórmulas cosmológicas;
- não altera bounds/priors;
- não altera resultados canônicos existentes;
- não muda `claim_allowed=false`;
- não declara vitória RLL;
- apenas habilita saída versionada segura.

---

## 8. Estado do gate

```text
TOKEN_VAZIO_CLI_OUTPUT_STEM = mitigado por wrapper seguro
robust_fit_execution_allowed = condicionado a testes PASS e uso do wrapper
claim_allowed = false
```

---

## 9. R3

```text
F_ok   = rota segura de output stem implementada e documentada.
F_gap  = testes ainda precisam ser executados em CI/local; robust fit ainda não foi rodado.
F_next = atualizar issue #401 com evidência de implementação e depois preparar wrapper de matriz seeds 1..10.
```
