# RAFAELIA · Cosmology Structure (D) — legado compatível

Este diretório foi mantido apenas por compatibilidade.
A execução oficial do Structure D está centralizada em:

- `data/pipelines/structure_d/` (código)
- `data/inputs/structure_d/` (entradas)
- `results/structure_d/` (saídas)

## Execução oficial
```bash
python -m data.pipelines.structure_d.make_example_data
python -m data.pipelines.structure_d.run_all
```

## Status do `rll_pipeline/`
`rll_pipeline/` agora é apenas wrapper fino (reexport/import) para `data.pipelines.structure_d`.
## Pastas
- `core/` : equações e documentação formal
- `data/` : CSVs (reais ou exemplo)
- `rll_pipeline/` : scripts (expansão, crescimento, feedback, likelihood)
- `results/` : outputs (tabelas e plots)
- `paper/` : rascunho de artigo (esqueleto)

## Restrições de domínio dos parâmetros (pipeline)
- `chi2(obs, mod, sigma)` em `rll_pipeline/likelihood.py` exige `sigma` finito e estritamente positivo (`sigma > 0`) em todos os elementos.
- `gaussian_window(z, z_peak, width)` em `rll_pipeline/feedback_agn.py` exige `width` finito e estritamente positivo (`width > 0`).
- Entradas fora dessas condições geram `ValueError` para bloquear combinações fisicamente/matematicamente inválidas.
