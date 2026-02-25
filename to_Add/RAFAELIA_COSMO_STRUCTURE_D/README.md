# RAFAELIA · Cosmology Structure (D)
Estrutura forte para integrar:
- Expansão cosmológica (H(z))
- Crescimento estrutural (fσ8)
- Feedback AGN/quasar (supressão ambiental)
- Validação estatística (χ², AIC, BIC)

> Gerado em 2026-02-21.

## Como rodar (rápido)
1) Instale dependências:
```bash
python -m venv .venv
. .venv/bin/activate  # Linux/Mac
# ou: .venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

2) Gere dados exemplo e rode validação:
```bash
python -m code.make_example_data
python -m code.run_all
```

## Pastas
- `core/` : equações e documentação formal
- `data/` : CSVs (reais ou exemplo)
- `code/` : scripts (expansão, crescimento, feedback, likelihood)
- `results/` : outputs (tabelas e plots)
- `paper/` : rascunho de artigo (esqueleto)
