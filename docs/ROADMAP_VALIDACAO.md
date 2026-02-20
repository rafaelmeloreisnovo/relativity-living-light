# ROADMAP_VALIDACAO — Pipeline oficial de prova observacional

Este guia operacional define o fluxo executável para validação observacional com Pantheon+, comparação RLL vs ΛCDM e exportação padronizada de resultados.

## Status dos Dados

- **Sintético:** ambiente de teste com arquivos simulados e validação de pipeline.
- **Parcial real:** ingestão de dados reais em andamento com cobertura parcial dos observáveis.
- **Real validado:** pipeline concluído com dados reais, artefatos finais e relatório validado.

**Nível atual deste roadmap:** `Parcial real` (fase operacional de ingestão e validação).

---

## 1) Obtenção dos arquivos Pantheon+

Fonte oficial:
- https://github.com/PantheonPlusSH0ES/DataRelease

Arquivos mínimos exigidos:
- `lcparam_full_long_zhel.txt`
- `sys_full_long.txt` (opcional, porém recomendado)

Exemplo de preparação local:

```bash
mkdir -p data/pantheon
# baixar manualmente os dois arquivos do DataRelease
# e copiar para data/pantheon/
```

## 2) Estrutura esperada em `data/pantheon/`

Estrutura canônica:

```text
data/
└── pantheon/
    ├── lcparam_full_long_zhel.txt
    └── sys_full_long.txt
```

Regras:
- `lcparam_full_long_zhel.txt` deve conter cabeçalho com nomes de colunas.
- `sys_full_long.txt`, quando presente, deve ter exatamente `N×N` elementos, onde `N` é o número de SNe de `lcparam_full_long_zhel.txt`.

## 3) Colunas aceitas (entrada Pantheon+)

O pipeline aceita aliases para robustez de versão:

- Redshift (obrigatória): `zhel` **ou** `zcmb`
- Módulo de distância observado (obrigatória): `mb` **ou** `mu` **ou** `m_b_corr`
- Erro do módulo (obrigatória): `dmb` **ou** `dmu` **ou** `mb_err`

Se nenhuma coluna de um grupo for encontrada, a execução falha com mensagem explícita.

## 4) Validações executáveis

Validações implementadas em `docs/panteon_likelihood.py`:

1. Arquivo principal existe (`lcparam_full_long_zhel.txt`).
2. Colunas obrigatórias resolvidas pelos nomes aceitos.
3. `z`, `mu_obs`, `mu_err` sem NaN/inf.
4. `mu_err > 0` para todos os pontos.
5. Se `sys_full_long.txt` existir, tamanho compatível com `N×N`.
6. Inversão da covariância total (`C_stat + C_sys`) sem erro.

## 5) Execução do pipeline (etapa de validação)

Com os arquivos no lugar:

```bash
python docs/panteon_likelihood.py
```

Saídas esperadas (quando a etapa `Real validado` for concluída):
- ajuste de melhor valor para RLL e ΛCDM
- χ², AIC, BIC
- deltas comparativos RLL-ΛCDM
- artefatos canônicos em `data/results/`
- figura comparativa em `figs/paper/` (se `matplotlib` estiver disponível)

## 6) Formato canônico de saída

### 6.1 Resultados numéricos (`data/results/`)

`data/results/pantheon_comparativo_rll_vs_lcdm.csv`
- selo de origem esperado: `real`
- colunas:
  - `modelo`
  - `chi2`
  - `AIC`
  - `BIC`
  - `delta_AIC_vs_LCDM`
  - `delta_BIC_vs_LCDM`

`data/results/pantheon_fit_summary.json`
- selo de origem esperado: `real`
- campos principais:
  - `pipeline`
  - `timestamp_utc`
  - `n_obs`
  - `rll.best_fit` + `rll.chi2` + `rll.AIC` + `rll.BIC`
  - `lcdm.best_fit` + `lcdm.chi2` + `lcdm.AIC` + `lcdm.BIC`
  - `comparativo` (tabela equivalente ao CSV)

### 6.2 Figuras de paper (`figs/paper/`)

Figura padrão desta etapa (selo de origem esperado: `real`):
- `figs/paper/pantheon_rll_vs_lcdm_delta_mu.png`

Regra de nomenclatura sugerida:
- `<dataset>_<comparacao>_<observavel>.png`

## 7) Checklist de término

- [ ] `data/pantheon/` contém os arquivos exigidos
- [ ] execução sem erro do comando principal
- [ ] CSV e JSON presentes em `data/results/`
- [ ] figura presente em `figs/paper/` (ou anotação de ausência de `matplotlib`)
- [ ] valores de χ²/AIC/BIC registrados no relatório técnico/paper

---

Este documento é a referência operacional para a etapa de prova observacional no repositório.
