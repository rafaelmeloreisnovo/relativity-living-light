# RAFAELIA · Cosmology Structure (D) — legado compatível

Este diretório existe apenas por compatibilidade.
A implementação autoritativa do Structure D está em:

- `data/pipelines/structure_d/` (código)
- `data/inputs/structure_d/` (entradas)
- `results/structure_d/` (saídas)

## Comandos oficiais
```bash
python -m data.pipelines.structure_d.make_example_data
python -m data.pipelines.structure_d.run_all
```

## Wrappers de compatibilidade
`RAFAELIA_COSMO_STRUCTURE_D/rll_pipeline/` contém somente wrappers finos.
Eles não carregam lógica autoritativa.
