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
