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
python -m rll_pipeline.make_example_data
python -m rll_pipeline.run_all
```

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
