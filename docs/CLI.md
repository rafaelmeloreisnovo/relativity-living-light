# CLI do Relativity Living Light (`rll`)

## Instalação

No diretório raiz do repositório:

```bash
pip install -e .
```

Isso instala o comando `rll` definido em `pyproject.toml`.

## Subcomando `run`

Executa os fluxos já existentes sem duplicar lógica, apenas roteando para scripts atuais.

### Exemplo solicitado

```bash
rll run --data real --model rll --with-bayes --with-covariance
```

### Opções

- `--data synthetic|real`
- `--model rll|lcdm|both`
- `--with-bayes`
- `--with-covariance`

## Mapeamento para fluxos atuais

- `--data synthetic` 
  - Roteia para: `data/pipelines/structure_d/run_all.py`
- `--data real` sem flags adicionais
  - Roteia para: `docs/rll_validation_real.py`
- `--data real` com `--with-bayes` e/ou `--with-covariance`
  - Roteia para: `docs/panteon_likelihood.py`

## Observações

- O pipeline Pantheon+ espera insumos em `data/pantheon/` (detalhes em `docs/ROADMAP_VALIDACAO.md`).
- O parâmetro `--model` é mantido para compatibilidade de interface; os fluxos atuais executam comparação RLL vs ΛCDM de forma conjunta.
