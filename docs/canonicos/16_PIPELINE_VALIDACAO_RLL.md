# 16 — Pipeline de Validação RLL

**Status:** canônico complementar  
**Origem:** extraído de `docs/canonicos/BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md`  
**Função:** registrar a estrutura executável, funções-núcleo e critérios mínimos de reprodutibilidade.

---

## 1. Estrutura esperada

```text
relativity-living-light/
├── .github/workflows/
│   ├── validacao_real.yml
│   └── cosmology_validation.yml
├── validacao_real/
│   ├── sources.yml
│   ├── fetch_real_data.py
│   ├── compute_validation.py
│   ├── make_figures.py
│   ├── render_report.py
│   ├── data/
│   │   ├── desi_dr2_bao.yml
│   │   └── hz_cosmic_chronometers.yml
│   └── caminhos/
│       ├── CAMINHOS_VALIDACAO_NOVOS.yml
│       └── TEXTO_DESCRITIVO_ANALITICO_TECNICO.md
├── scripts/compute_validation.py
└── orquestrador/
    └── rafaelia_orquestrador.py
```

## 2. Funções-núcleo

```python
Ez_LCDM(z, Om, Or=8.6e-5)
Ez_w0wa(z, Om, w0, wa, Or=8.6e-5)
Ez_RLL(z, Om, Os0, zt, wt, OB0=0.0, OP0=0.0, Or=8.6e-5)
DM_over_rd(z, Ez, H0, rd)
DH_over_rd(z, Ez, H0, rd)
DV_over_rd(z, Ez, H0, rd)
chi2_bao(Ez, H0, rd, data)
aic(chi2, k)
aicc(chi2, k, n)
bic(chi2, k, n)
w_eff_RLL(a, zt, wt)
```

## 3. Critérios mínimos de validação

Toda execução de validação deve registrar:

- commit de referência;
- versão dos dados;
- parâmetros usados;
- matriz de covariância ou justificativa de diagonalização;
- número de observáveis;
- número de parâmetros livres;
- resultados de χ², AIC, AICc e BIC;
- interpretação com limites claros.

## 4. Regra de não-alucinação computacional

Se o pipeline não encontrou dado, matriz, arquivo ou referência, o relatório deve retornar `[VAZIO]`, não preencher automaticamente com número inventado.

## 5. Ambiente Termux ARM32

Para ambiente ARM32/Termux, preferência por pacotes do sistema:

```bash
pkg install python-numpy python-matplotlib
```

Evitar `pip install matplotlib` quando houver risco de falha de compilação local.

## 6. Saída esperada

O pipeline deve produzir:

- relatório `.md`;
- tabelas `.csv` ou `.yml`;
- figuras `.png` ou `.svg`;
- manifesto de execução;
- hashes de integridade.

---

*Pipeline é prova de trabalho, não ornamento.*