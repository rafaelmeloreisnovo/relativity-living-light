# Descobertas Emergentes (RLL)

Este documento consolida **14 descobertas numeradas** com trilha de manutenção explícita entre hipótese, código e artefatos.
Strings de localização canônicas: `run_all.py` (pipeline fim-a-fim), `likelihood.py` (ajuste estatístico), `growth.py` (fσ8).

## 1. Consistência global de ajuste entre RLL e ΛCDM permanece praticamente degenerada no χ² agregado
- **Evidência:** `results/RLL_chi2_results.csv` (linha `DELTA_RLL_minus_LCDM`, coluna `chi2 = -0.002`).
- **Risco:** interpretativo (confundir diferença numérica mínima com “vitória” inequívoca).
- **Teste de falsificação:** recalcular a tabela de comparação com bootstrap dos observáveis; reprova se o sinal de `DELTA_RLL_minus_LCDM` mudar de forma instável (>40% das reamostragens).
- **Prioridade:** P0
- **Ponte com código:** `data/pipelines/structure_d/likelihood.py` + `chi2()`, `chi2_with_covariance()`, `aic()`, `bic()`.
- **Ponte com resultados:** `results/RLL_chi2_results.csv`, `figs/paper/corner_plot_unified_highres.png`.

## 2. Penalização de complexidade favorece ΛCDM quando RLL adiciona parâmetros livres
- **Evidência:** `results/RLL_chi2_results.csv` (`k=7` para RLL vs `k=4` para LCDM; ΔAIC≈+5.998 para RLL).
- **Risco:** científico (overfitting por parametrização adicional sem ganho explicativo proporcional).
- **Teste de falsificação:** congelar subconjuntos de parâmetros extras (`Os0`, `zt`, `wt`) e recomputar AIC/BIC; reprova se RLL não melhorar AIC/BIC com `k` reduzido.
- **Prioridade:** P0
- **Ponte com código:** `data/pipelines/structure_d/run_all.py` + `fit_params_rll`, `fit_params_lcdm`.
- **Ponte com resultados:** `results/RLL_chi2_results.csv`, `figs/paper/post_1d_Os.png`.

## 3. Uso de covariância está incompleto em blocos-chave, elevando risco de viés no ajuste
- **Evidência:** `results/structure_d/covariance_usage.csv` (arquivo contém apenas cabeçalho, sem blocos preenchidos).
- **Risco:** técnico/científico (incertezas subestimadas por fallback diagonal ou ausência de bloco).
- **Teste de falsificação:** preencher `covariance_usage.csv` com todos os blocos esperados (`SNe`, `BAO`, `fσ8`, `lenses`, `Hz`); reprova se qualquer bloco permanecer `not_used` sem justificativa metodológica.
- **Prioridade:** P0
- **Ponte com código:** `data/pipelines/structure_d/run_all.py` + geração de `covariance_usage.csv` e `_chi2_from_entry()`.
- **Ponte com resultados:** `results/structure_d/covariance_usage.csv`, `figs/paper/unified_mu_residuals.png`.

## 4. Pipeline fim-a-fim definido, mas resultado principal `model_comparison.csv` não está materializado no snapshot atual
- **Evidência:** ausência de `results/structure_d/model_comparison.csv` apesar da documentação operacional.
- **Risco:** técnico (quebra de reprodutibilidade ponta-a-ponta por artefato faltante).
- **Teste de falsificação:** executar `run_all.py` com configuração padrão; reprova se `results/structure_d/model_comparison.csv` não for gerado.
- **Prioridade:** P0
- **Ponte com código:** `data/pipelines/structure_d/run_all.py` + `main()` / `evaluate_model()`.
- **Ponte com resultados:** `results/structure_d/README.md`, `figs/paper/fig_pipeline.png`.

## 5. Componente de crescimento fσ8 já possui ponte explícita para realimentação AGN
- **Evidência:** `growth.py` aplica `suppression_factor()` quando `use_feedback=True`.
- **Risco:** científico (atribuir supressão de crescimento ao mecanismo errado sem validação cruzada).
- **Teste de falsificação:** comparar curva com `use_feedback=False` e `True`; reprova se a variante com feedback não produzir supressão mensurável em torno de `z_peak`.
- **Prioridade:** P1
- **Ponte com código:** `data/pipelines/structure_d/growth.py` + `f_sigma8_proxy()`.
- **Ponte com resultados:** `figs/paper/unified_growth_fs8.png`, `results/RLL_chi2_results.csv`.

## 6. Parâmetro `width` controla largura da supressão e pode colapsar identificabilidade
- **Evidência:** em `growth.py`, `width` entra diretamente em `suppression_factor(z, alpha, z_peak, width)`.
- **Risco:** interpretativo/técnico (degenerescência entre `alpha`, `z_peak`, `width`).
- **Teste de falsificação:** varrer grade 3D (`alpha`,`z_peak`,`width`) e inspecionar contornos de χ²; reprova se múltiplos vales equivalentes impedirem identificação prática.
- **Prioridade:** P1
- **Ponte com código:** `data/pipelines/structure_d/growth.py` + parâmetros de `f_sigma8_proxy()`.
- **Ponte com resultados:** `figs/paper/post_2d_zt_wt.png`, `figs/paper/post_2d_Os_wt.png`.

## 7. Controle de integridade estatística já rejeita `sigma<=0` e covariância malformada
- **Evidência:** validações em `likelihood.py` (`_validated_sigma_array`, `_validated_covariance_matrix`).
- **Risco:** técnico (falhas silenciosas se validação for contornada por dados externos).
- **Teste de falsificação:** injetar caso de teste com diagonal não positiva; reprova se `chi2_with_covariance()` não lançar `ValueError`.
- **Prioridade:** P1
- **Ponte com código:** `data/pipelines/structure_d/likelihood.py` + `_validated_sigma_array()`, `_validated_covariance_matrix()`.
- **Ponte com resultados:** `results/structure_d/covariance_usage.csv`, `figs/paper/mock_H_fit.png`.

## 8. Fórmula de BIC depende de `N` e é sensível ao total de observáveis ativos
- **Evidência:** `bic(chi2_val, k, N)=chi2+k*log(N)` em `likelihood.py`; `N` é acumulado em `run_all.py`.
- **Risco:** interpretativo (comparar BIC de execuções com conjuntos de dados diferentes como se fossem equivalentes).
- **Teste de falsificação:** repetir ajuste removendo um dataset ativo; reprova se comparação de BIC for usada sem normalização de `N`.
- **Prioridade:** P1
- **Ponte com código:** `data/pipelines/structure_d/likelihood.py` + `bic()`; `data/pipelines/structure_d/run_all.py` + `total_observables`.
- **Ponte com resultados:** `results/RLL_chi2_results.csv`, `figs/paper/fig_degeneracy.png`.

## 9. Conjunto opcional de duas radiações amplia escopo físico sem integração obrigatória
- **Evidência:** `results/two_radiation_model_preview.csv` existe como artefato opcional do fluxo.
- **Risco:** científico (misturar análise principal e preview opcional sem separação de narrativa).
- **Teste de falsificação:** rodar baseline sem `--with-two-rad`; reprova se conclusões principais dependerem do preview opcional.
- **Prioridade:** P2
- **Ponte com código:** `run_all.py` (pipeline fim-a-fim via wrapper `scripts/run_repro_all.sh`).
- **Ponte com resultados:** `results/two_radiation_model_preview.csv`, `figs/paper/unified_fractions.png`.

## 10. Cadeia de evidências em H(z) está visualmente consolidada em figura canônica
- **Evidência:** `figs/paper/unified_H_ratio.png` e `figs/paper/H_ratio_vs_z.png`.
- **Risco:** interpretativo (overtrust em inspeção visual sem métrica complementar).
- **Teste de falsificação:** calcular erro quadrático médio por faixa de redshift; reprova se qualquer faixa crítica tiver degradação sistemática >10% contra baseline.
- **Prioridade:** P2
- **Ponte com código:** `data/pipelines/structure_d/run_all.py` + ramificação dataset `hz`.
- **Ponte com resultados:** `figs/paper/unified_H_ratio.png`, `figs/paper/H_ratio_vs_z.png`.

## 11. Resíduos de distância (SNe Ia) sugerem utilidade diagnóstica de regimes de transição
- **Evidência:** `figs/paper/unified_mu_residuals.png` e `figs/paper/mu_residuals.png`.
- **Risco:** científico (atribuir padrão residual a física nova sem controlar sistemáticas de calibração).
- **Teste de falsificação:** rodar ajuste com subconjuntos de SNe por survey; reprova se padrão residual não for robusto entre subconjuntos.
- **Prioridade:** P2
- **Ponte com código:** `data/pipelines/structure_d/likelihood.py` + `chi2()`/`chi2_with_covariance()`.
- **Ponte com resultados:** `figs/paper/unified_mu_residuals.png`, `results/RLL_chi2_results.csv`.

## 12. Lensing em clusters permanece como validador externo do setor de superposição
- **Evidência:** `figs/paper/cluster_lensing_SIS_unified.png`.
- **Risco:** interpretativo (generalização indevida de poucos casos de cluster).
- **Teste de falsificação:** aplicar mesma parametrização em amostra cega adicional; reprova se erros de massa/lente excederem 2σ em maioria da amostra.
- **Prioridade:** P2
- **Ponte com código:** `run_all.py` (integração final de métricas comparativas).
- **Ponte com resultados:** `figs/paper/cluster_lensing_SIS_unified.png`, `results/RLL_chi2_results.csv`.

## 13. Curvas de rotação reforçam consistência fenomenológica além do regime puramente cosmológico
- **Evidência:** `figs/paper/rotcurve_NGC_2403.png` e `figs/paper/rotation_curves_sup.png`.
- **Risco:** científico (extrapolação cosmologia→escala galáctica sem ponte dinâmica completa).
- **Teste de falsificação:** comparar predição em galáxias fora do conjunto de calibração; reprova se erro relativo mediano de velocidade circular superar 15%.
- **Prioridade:** P3
- **Ponte com código:** `growth.py` (consistência de crescimento/estrutura) + `run_all.py` (orquestração).
- **Ponte com resultados:** `figs/paper/rotcurve_NGC_2403.png`, `figs/paper/rotation_curves_sup.png`.

## 14. Documentação já indica trilha de reprodução única, útil para auditoria de descobertas
- **Evidência:** comando canônico `bash scripts/run_repro_all.sh` documentado no master.
- **Risco:** técnico (drift entre documentação e comportamento real do pipeline).
- **Teste de falsificação:** executar script em ambiente limpo e verificar presença dos artefatos declarados; reprova se faltar qualquer arquivo obrigatório sem erro explícito.
- **Prioridade:** P0
- **Ponte com código:** `run_all.py` (executado indiretamente pelo script de reprodução).
- **Ponte com resultados:** `results/RLL_chi2_results.csv`, `figs/paper/RLL_validacao_real.png`.

---

## Matriz de cobertura final

| Descoberta | módulo | resultado | teste de falsificação | prioridade |
|---|---|---|---|---|
| 1 | `likelihood.py` (`chi2`, `chi2_with_covariance`) | `results/RLL_chi2_results.csv`, `figs/paper/corner_plot_unified_highres.png` | bootstrap de `DELTA_RLL_minus_LCDM` | P0 |
| 2 | `run_all.py` (`fit_params_rll`, `fit_params_lcdm`) | `results/RLL_chi2_results.csv`, `figs/paper/post_1d_Os.png` | congelar parâmetros extras e recomputar AIC/BIC | P0 |
| 3 | `run_all.py` (`_chi2_from_entry`, escrita de covariância) | `results/structure_d/covariance_usage.csv`, `figs/paper/unified_mu_residuals.png` | exigir blocos SNe/BAO/fσ8/lenses/Hz completos | P0 |
| 4 | `run_all.py` (`main`, `evaluate_model`) | `results/structure_d/README.md`, `figs/paper/fig_pipeline.png` | gerar `model_comparison.csv` em execução padrão | P0 |
| 5 | `growth.py` (`f_sigma8_proxy`) | `figs/paper/unified_growth_fs8.png`, `results/RLL_chi2_results.csv` | comparar `use_feedback=False/True` | P1 |
| 6 | `growth.py` (`width`, `z_peak`, `alpha`) | `figs/paper/post_2d_zt_wt.png`, `figs/paper/post_2d_Os_wt.png` | varredura 3D de degenerescência | P1 |
| 7 | `likelihood.py` (validações de sigma/covariância) | `results/structure_d/covariance_usage.csv`, `figs/paper/mock_H_fit.png` | injetar covariância inválida e esperar `ValueError` | P1 |
| 8 | `likelihood.py` (`bic`) + `run_all.py` (`total_observables`) | `results/RLL_chi2_results.csv`, `figs/paper/fig_degeneracy.png` | recomputar BIC com dataset reduzido | P1 |
| 9 | `run_all.py` (pipeline via `run_repro_all.sh`) | `results/two_radiation_model_preview.csv`, `figs/paper/unified_fractions.png` | validar independência do baseline sem `--with-two-rad` | P2 |
| 10 | `run_all.py` (bloco `hz`) | `figs/paper/unified_H_ratio.png`, `figs/paper/H_ratio_vs_z.png` | erro por faixa de redshift | P2 |
| 11 | `likelihood.py` (`chi2`, `chi2_with_covariance`) | `figs/paper/unified_mu_residuals.png`, `results/RLL_chi2_results.csv` | robustez por subsets de SNe | P2 |
| 12 | `run_all.py` (integração comparativa) | `figs/paper/cluster_lensing_SIS_unified.png`, `results/RLL_chi2_results.csv` | amostra cega adicional de clusters | P2 |
| 13 | `growth.py` + `run_all.py` | `figs/paper/rotcurve_NGC_2403.png`, `figs/paper/rotation_curves_sup.png` | validação em galáxias fora da calibração | P3 |
| 14 | `run_all.py` (reprodução fim-a-fim) | `results/RLL_chi2_results.csv`, `figs/paper/RLL_validacao_real.png` | execução limpa + checklist de artefatos | P0 |
