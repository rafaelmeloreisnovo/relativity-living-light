# Plano A→B→C→D — AGN/JWST para Paper e Fechamento do Modelo

Este documento consolida o plano em 4 etapas para transformar a trilha atual do repositório em submissão científica com validação estatística e predições discriminantes.

## A) Paper científico publicável

### Título sugerido
**Intergalactic Quasar Feedback and Early Supermassive Black Hole Growth: an effective cosmological extension constrained by H(z) and fσ₈(z)**

### Estrutura recomendada
1. **Introdução** — sucesso de ΛCDM, lacunas em SMBHs precoces e motivação de termo efetivo com teste observacional.
2. **Dados** — H(z), fσ₈(z), e extensão opcional para SN Ia/lensing/CMB shift.
3. **Modelo** — extensão mínima em expansão ou crescimento com baixo número de parâmetros.
4. **Inferência** — ajuste por χ² com comparação via AIC/BIC.
5. **Resultados** — comparação direta RLL/ΛCDM, degenerescências e sensibilidade dos parâmetros.
6. **Discussão** — conexão com feedback de quasar/AGN, SMBH super-Eddington e predições ambientais.
7. **Conclusão** — ganhos reais, limitações e próximo “teste mortal”.

## B) Modelo fechado (mínimo)

### Caminho 1: extensão na expansão
\[
H^2(z)=H_0^2\left[\Omega_m(1+z)^3+\Omega_r(1+z)^4+\Omega_\Lambda+\Omega_f(z)\right]
\]
\[
\Omega_f(z)=\beta\exp\left[-\frac{(z-z_p)^2}{2w^2}\right]
\]

### Caminho 2: extensão no crescimento
\[
f\sigma_8(z)=\Omega_m(z)^\gamma\sigma_{8,0}S(z),\quad S(z)=1-\alpha\exp\left[-\frac{(z-z_p)^2}{2w^2}\right]
\]

### Critério de fechamento
- consistência física/estabilidade;
- **k ≤ 5** como alvo;
- ganho estatístico vs ΛCDM (ΔAIC < 0 ou ΔBIC ~ 0);
- pelo menos uma predição observável nova.

## C) Análise máxima (estado da arte)

- **SMBH cedo demais:** avaliar super-Eddington e sementes pesadas/colapso direto.
- **Feedback além da hospedeira:** mapear impacto em IGM/CGM, SFR e crescimento estrutural (S8/fσ8).
- **Limite metodológico:** separar física bariônica não-linear de “nova física” e evitar sobreajuste.

## D) Até onde pode chegar

- **Cenário forte:** menos parâmetros + melhor AIC/BIC + predição ambiental testável.
- **Cenário médio:** pipeline reprodutível como ferramenta comparativa.
- **Cenário fraco:** excesso de parâmetros sem predição nova.

## Execução prática no repositório

1. Ingerir/atualizar dados reais em `data/real/`.
2. Rodar o pipeline de validação real (`docs/rll_validation_real.py`).
3. Publicar comparação final em `results/model_comparison.csv` (arquivo-alvo para versão de paper).
4. Atualizar discussão e conclusão no manuscrito principal (`main.tex` e/ou `docs/PAPER_CORRIGIDO.tex`).

