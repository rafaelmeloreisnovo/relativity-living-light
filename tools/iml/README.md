# IML pipeline (Actions + Artifact)

Executa um pipeline dinâmico inspirado no modelo toroidal/atrator e gera um artefato JSON com:

- Série temporal de `C_t`, `H_t`, `phi_t`
- Estado toroidal `s in [0,1)^7`
- Bloco de teste de falsificabilidade auto-adaptado

## Execução local

```bash
python tools/iml/iml_pipeline.py --input data/iml/daise_input.example.json --output artifacts/iml/iml_artifact.json --steps 42
```

## Execução no GitHub Actions

- Workflow: `.github/workflows/iml_artifact.yml`
- Trigger: `workflow_dispatch`
- Saída: artefato `iml-artifact`
