# Plano A→B→C→D — Organização de Dados, Documentos e Roteiro Científico
## Relativity Living Light (RLL) com foco em JWST/AGN/SMBH precoce

**Objetivo:** consolidar em um único artefato o esqueleto de paper (A), o fechamento de modelo (B), a análise máxima (C) e os cenários de alcance (D), com trilha prática de execução e organização documental.

---

## 1) Escopo consolidado (o que foi incluído)

Este documento incorpora de forma estruturada:

- Plano em 4 etapas (A→B→C→D).
- Formulações mínimas para extensão cosmológica efetiva.
- Critérios estatísticos de discriminação (χ², AIC, BIC).
- Lista de âncoras observacionais recentes (JWST/quasares/super-Eddington/LRDs) para fundamentação narrativa e teste observacional.
- Procedimento operacional para transformar o plano em paper com resultados reproduzíveis.

---

## 2) Etapa A — Paper científico publicável (estrutura)

### Título sugerido

**Intergalactic Quasar Feedback and Early Supermassive Black Hole Growth: an effective cosmological extension constrained by H(z) and fσ₈(z)**

### Abstract-base (editável)

Observações recentes do JWST apontam, simultaneamente, sinais de supressão de formação estelar em galáxias vizinhas de quasares em escalas ~Mpc e evidências de crescimento acelerado de SMBHs no universo primordial, incluindo cenários consistentes com episódios super-Eddington. Motivado por esse quadro, adotamos uma extensão efetiva fenomenológica com janela em redshift para representar injeção energética associada a AGN/quasares e avaliamos seu desempenho frente a H(z) e fσ₈(z). O contraste estatístico com ΛCDM é feito via χ², AIC e BIC, com ênfase em degenerescências e penalidade por contagem de parâmetros. Mostramos como o modelo pode gerar predições discriminantes em crescimento estrutural e em ambientes de quasar, úteis para testes com dados atuais e próximos levantamentos.

### Estrutura de seções do paper

1. **Introdução**
   - contexto ΛCDM e escopo de tensões relevantes;
   - motivação física: SMBH precoce + feedback além da hospedeira;
   - proposta: extensão efetiva com predição observável e controle de overfit.
2. **Dados**
   - H(z) (compilações/chronometers);
   - fσ₈(z) (RSD);
   - opcionais em versões futuras: SN Ia, lensing e CMB-compressed likelihoods.
3. **Modelo**
   - definição explícita do termo efetivo;
   - parametrização mínima e interpretação física de cada parâmetro.
4. **Inferência e seleção de modelo**
   - χ², AIC, BIC;
   - análise de degenerescências e robustez.
5. **Resultados**
   - tabelas comparativas RLL-efetivo vs ΛCDM;
   - sensibilidade a janela de redshift e amplitude do termo de feedback.
6. **Discussão física**
   - conexão com AGN feedback/super-Eddington/LRDs;
   - previsões para clustering, lensing e supressão de SFR em vizinhança de quasares.
7. **Conclusão**
   - ganhos e limites;
   - teste observacional prioritário para falsificabilidade.

---

## 3) Etapa B — Modelo fechado (mínimo e testável)

### B1. Caminho 1 (modificação na expansão)

\[
H^2(z)=H_0^2\left[\Omega_m(1+z)^3+\Omega_r(1+z)^4+\Omega_\Lambda+\Omega_f(z)\right]
\]

\[
\Omega_f(z)=\beta\,\exp\left[-\frac{(z-z_p)^2}{2w^2}\right]
\]

### B2. Caminho 2 (modificação no crescimento; recomendado)

Mantém H(z) de ΛCDM e altera diretamente o observável de crescimento:

\[
f\sigma_8(z)=\Omega_m(z)^\gamma\,\sigma_{8,0}\,S(z)
\]

\[
S(z)=1-\alpha\,\exp\left[-\frac{(z-z_p)^2}{2w^2}\right]
\]

### B3. Critérios formais de fechamento

Um “modelo fechado” aqui deve satisfazer:

- **Consistência física:** positividade de H²(z), comportamento regular no intervalo de redshift analisado e ausência de patologias óbvias no regime efetivo.
- **Parcimônia:** idealmente \(k \leq 5\).
- **Competitividade estatística:** ΔAIC < 0 (preferível) e ΔBIC não severamente penalizado.
- **Predição discriminante:** pelo menos uma assinatura observável além do ajuste retrospectivo.

### B4. Fechamento observacional do termo de feedback

Para o fechamento observacional, adotar duas parametrizações concorrentes do termo de feedback e compará-las no mesmo pipeline estatístico.

1. **Fenomenológica (gaussiana atual)**

   Mantém a forma gaussiana já definida:

   \[
   S(z)=1-\alpha\,\exp\left[-\frac{(z-z_p)^2}{2w^2}\right]
   \]

   (ou equivalente em \(\Omega_f(z)\), conforme o caminho escolhido).

2. **Semi-física com proxy de densidade de luminosidade AGN \(\rho_{L,AGN}(z)\)**

   Substituir o termo puramente gaussiano por uma forma guiada por \(\rho_{L,AGN}(z)\), por exemplo:

   \[
   S(z)=1-\alpha_s\left[\frac{\rho_{L,AGN}(z)}{\rho_{L,AGN}(z_\star)}\right]^\eta
   \]

   com \(\alpha_s\), \(\eta\) e parâmetros auxiliares de normalização/escala definidos para manter estabilidade numérica e interpretação física no intervalo de redshift analisado.

**Priors (forma semi-física):** declarar explicitamente que os parâmetros da parametrização semi-física usam priors informados por literatura, com intervalos amplos (fracos), para evitar super-restrição artificial.

**Comparação entre parametrizações:** reportar \(\Delta\mathrm{AIC}\) e \(\Delta\mathrm{BIC}\) entre as formas fenomenológica e semi-física, além da comparação com \(\Lambda\)CDM, para decisão de parcimônia vs. ganho de ajuste.

---

## 4) Etapa C — Análise máxima (estado da arte observacional)

### C1. Frentes físicas prioritárias

- episódios de acreção super-Eddington em fases curtas;
- cenários de sementes pesadas/colapso direto;
- interpretação de LRDs como possíveis fases de SMBH jovem.

### C2. Ponte com cosmologia observável

Se houver supressão de formação estelar em vizinhas de quasares, esperar:

- aquecimento de IGM/CGM;
- redução de gás frio;
- impacto indireto em histórico de crescimento e métricas como fσ₈/S8.

### C3. Limite metodológico atual

- separar feedback bariônico não linear de “nova física” em nível de background;
- evitar confundir melhora estatística local com explicação causal robusta.

---

## 5) Etapa D — Cenários de alcance

- **D1 (forte):** redução de parâmetros + ganho em AIC/BIC + predição observável ambiental.
- **D2 (médio):** sem vitória sobre ΛCDM, mas com pipeline reprodutível de alto valor científico.
- **D3 (fraco):** excesso de parâmetros e ausência de predição nova (risco de overfit).

---

## 6) Organização prática de dados e documentos (implementação imediata)

### 6.1 Estrutura mínima sugerida

- `data/` → dados de entrada e tabelas observacionais.
- `docs/` → narrativa científica, formulação, metodologia, discussão e roadmap.
- `results/` (a criar no próximo ciclo de execução) → saídas numéricas reproduzíveis (`model_comparison.csv`, best-fit, resíduos, etc.).

### 6.2 Convenção de nomes para ciclo A→B→C→D

- `data/Hz.csv` → série de expansão.
- `data/fsigma8.csv` → série de crescimento.
- `results/model_comparison.csv` → tabela principal de seleção de modelo.
- `docs/PLANO_ABCD_JWST_AGN_SMBH.md` → referência mestra do plano.

### 6.3 Checklist operacional

1. validar formato de `Hz.csv` e `fsigma8.csv` (colunas, unidades, metadados de origem);
2. executar pipeline de ajuste/inferência;
3. exportar `model_comparison.csv` com χ², AIC, BIC e k por modelo;
   - garantir uma linha para a parametrização **fenomenológica** e uma linha para a parametrização **semi-física**;
4. preencher versão final do paper com números e tabelas;
5. registrar release documental com hash/data dos artefatos.

---

## 7) Âncoras observacionais para fundamentação da narrativa (curadoria)

Para a versão de submissão, manter seção de referências dedicada a:

- resultados JWST sobre ambientes de quasar e supressão em vizinhança;
- evidências e debate sobre crescimento super-Eddington no universo primordial;
- literatura recente sobre LRDs e SMBHs em redshifts altos;
- comunicados/instrument papers relevantes (JWST/ESA) sobre SMBHs ativos muito cedo.

> Observação editorial: na versão final, inserir citações bibliográficas completas (autor, periódico, ano, DOI/arXiv quando aplicável) no arquivo canônico de referências.

---

## 8) Resultado desta consolidação

Este arquivo passa a ser o **ponto único** para transformar o material estratégico já definido em um fluxo técnico executável e publicável, preservando coerência entre:

- hipótese física,
- modelagem efetiva,
- validação estatística,
- e predição observacional falsificável.
