# RLL — Pre-Robust-Fit PR Checklist

**Status:** checklist obrigatório antes de qualquer PR que habilite execução robusta.  
**Escopo:** impedir sobrescrita, overclaim e mistura entre smoke e robust fit.

---

## 1. Objetivo

Antes de rodar seeds múltiplas ou `maxiter>=100`, o repositório precisa garantir que cada execução produza artefatos versionados.

A prioridade é fechar:

```text
TOKEN_VAZIO_CLI_OUTPUT_STEM
```

---

## 2. Checklist de segurança

### A. Código / execução

- [ ] `main()` aceita `STRUCTURE_D_JOINT_OUTPUT_STEM` ou argumento CLI.
- [ ] execução padrão continua escrevendo `joint_real_likelihood` apenas quando explicitamente desejado.
- [ ] robust fit usa stem versionado por seed e maxiter.
- [ ] nenhum robust fit sobrescreve `results/structure_d/joint_real_likelihood.json`.
- [ ] atomic write e backup continuam ativos.
- [ ] outputs incluem seed, maxiter e created_utc.

### B. Resultados

- [ ] cada seed gera `.json`, `.csv` e `_covariance_manifest.json` próprios.
- [ ] outputs robustos ficam em diretório ou stem reconhecível.
- [ ] tabela agregada não substitui tabela canônica smoke.
- [ ] resultados robustos carregam `claim_allowed=false` até gates completos.

### C. Testes

- [ ] `python -m py_compile` passa.
- [ ] testes existentes passam.
- [ ] novo teste verifica que `STRUCTURE_D_JOINT_OUTPUT_STEM` altera o caminho de saída.
- [ ] novo teste verifica que execução robusta não toca no JSON canônico.

### D. Documentação

- [ ] `docs/RLL_OUTPUT_STEM_CLI_GAP.md` é atualizado ou referenciado.
- [ ] `docs/RLL_ROBUST_FIT_CHECKLIST.md` é atualizado se o comando mudar.
- [ ] `docs/RLL_NEXT_SAFE_ACTIONS_INDEX.md` move o item da fila B para executável.
- [ ] PR declara que não altera dados brutos.
- [ ] PR declara que não altera fórmula cosmológica.
- [ ] PR declara que não altera claim policy.

---

## 3. Critérios de aceite do PR

Um PR que fecha `TOKEN_VAZIO_CLI_OUTPUT_STEM` deve provar:

```text
STRUCTURE_D_JOINT_OUTPUT_STEM=joint_real_likelihood_test_seed_1
python data/pipelines/structure_d/joint_real_likelihood.py
```

produz:

```text
results/structure_d/joint_real_likelihood_test_seed_1.json
results/structure_d/joint_real_likelihood_test_seed_1.csv
results/structure_d/joint_real_likelihood_test_seed_1_covariance_manifest.json
```

sem modificar:

```text
results/structure_d/joint_real_likelihood.json
results/structure_d/joint_real_likelihood.csv
results/structure_d/joint_real_likelihood_covariance_manifest.json
```

---

## 4. PR body sugerido

```markdown
### Motivation
- Close `TOKEN_VAZIO_CLI_OUTPUT_STEM` before robust-fit execution.
- Prevent accidental overwrite of canonical smoke artifacts.
- Enable seed/maxiter-versioned outputs for future robust fits.

### Changes
- Add output stem support via environment variable or CLI.
- Preserve default behavior unless output stem is explicitly set.
- Add/adjust tests for versioned output paths.
- Update documentation references.

### Safety
- Does not alter `data/real/**`.
- Does not alter cosmological formulas.
- Does not alter canonical results.
- Does not change `claim_allowed=false`.

### Testing
- `python -m py_compile ...`
- `pytest ...`
- Manual smoke with temporary output stem.
```

---

## 5. Bloqueios

Não rodar robust fit se qualquer item abaixo estiver ausente:

- output versionado;
- seed registrada;
- maxiter registrado;
- caminho de saída não-canônico;
- testes mínimos;
- documentação de claim boundary.

---

## 6. R3

```text
F_ok   = checklist PR pré-robust-fit criado; critérios de aceite definidos.
F_gap  = PR/código ainda não implementado; robust fit segue bloqueado.
F_next = criar issue de acompanhamento para fechar output stem e habilitar robust fit seguro.
```
