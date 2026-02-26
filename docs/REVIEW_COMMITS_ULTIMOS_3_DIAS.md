# Revisão técnica — últimos 3 dias de commits

Data da revisão: 2026-02-26
Escopo: histórico `git log --since='3 days ago'` no branch atual.

## Resumo executivo
- O período teve volume muito alto de integração: 93 commits não-merge e 119 merges.
- Predominaram mudanças em documentação e padronização de convenções (glossário, FAQ, trilha PhD, índices).
- No código, os dois blocos centrais foram:
  1. validação de domínio em `chi2` e janela gaussiana;
  2. consolidação do pipeline `structure_d` com wrappers de compatibilidade.

## Commits técnicos principais (código)

### 1) `f0e701f` — Add domain validation for sigma and gaussian width
Arquivos impactados no código:
- `data/pipelines/structure_d/likelihood.py`
- `data/pipelines/structure_d/feedback_agn.py`
- espelhos equivalentes em `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/`

Avaliação:
- Ponto forte: bloqueia estados numéricos inválidos (`sigma<=0`, `width<=0` ou não-finito), reduzindo propagação silenciosa de `NaN/inf`.
- Risco residual: a validação ainda está duplicada entre árvore canônica e árvore compatível.

### 2) `5ee2b4d` — Consolidate Structure D pipeline into canonical module wrappers
Arquivos impactados no código:
- `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/run_all.py`
- `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/models.py`
- `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/__init__.py`
- equivalentes em `to_Add/...`

Avaliação:
- Ponto forte: reduz divergência funcional ao redirecionar execução para módulo canônico (`data.pipelines.structure_d`).
- Ponto de atenção: parte da árvore `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/` segue com implementações próprias (não-wrapper), o que ainda permite drift entre diretórios.

## Estado atual do código (inspeção)

### Válidações adicionadas
- `chi2` usa `_validated_sigma_array` para rejeitar sigma não-finito ou não-positivo.
- `gaussian_window` usa `_validated_width` para rejeitar largura inválida.

### Consolidação parcial de wrappers
- `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/run_all.py` é wrapper para `data.pipelines.structure_d.run_all`.
- `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/models.py` é wrapper para `data.pipelines.structure_d.models`.
- `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/__init__.py` é wrapper para `data.pipelines.structure_d`.
- Porém `RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/likelihood.py` e `feedback_agn.py` ainda carregam implementação local.

## Resultado da análise
- O repositório evoluiu bem em robustez numérica no pipeline cosmológico.
- A consolidação de diretórios foi iniciada corretamente, mas ainda não está 100% homogênea.
- O maior risco técnico imediato não é algoritmo: é manutenção por duplicação parcial de código entre árvores.

## Ações recomendadas (curtas)
1. Finalizar canonização: transformar também `likelihood.py`, `feedback_agn.py`, `growth.py`, `cosmo.py` em wrappers no diretório compatível.
2. Definir regra explícita de “source of truth” no README raiz para evitar novos forks internos.
3. Adicionar teste mínimo automatizado para os erros esperados:
   - `chi2(..., sigma=[...,0,...])` deve lançar `ValueError`;
   - `gaussian_window(..., width=0)` deve lançar `ValueError`.

## Comandos usados na revisão
- `git log --since='3 days ago' --date=iso --pretty=format:'%h|%ad|%an|%s'`
- `git log --since='3 days ago' --no-merges --pretty=format:'%h|%ad|%s' --date=short`
- `git log --since='3 days ago' --no-merges --numstat --pretty=format:'@@@ %h %s' | awk ...`
- `git show --stat --name-only --pretty=fuller f0e701f`
- `git show --stat --name-only --pretty=fuller 5ee2b4d`
- `python -m data.pipelines.structure_d.make_example_data`
- `python -m data.pipelines.structure_d.run_all`
