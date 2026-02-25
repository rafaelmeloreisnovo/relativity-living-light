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
\Omega_{\mathrm{feedback}}(z)=\Omega_{\mathrm{rad,ativo}}(z)+\Omega_{\mathrm{MHD}}(z)+\Omega_{\mathrm{ion}}(z)
\]

com decomposição mínima:

\[
\Omega_{\mathrm{rad,ativo}}(z)=\beta_{\mathrm{rad}}\,\exp\left[-\frac{(z-z_{\mathrm{rad}})^2}{2w_{\mathrm{rad}}^2}\right],\qquad
\Omega_{\mathrm{MHD}}(z)=\beta_{\mathrm{MHD}}\,\exp\left[-\frac{(z-z_{\mathrm{MHD}})^2}{2w_{\mathrm{MHD}}^2}\right],
\]

\[
\Omega_{\mathrm{ion}}(z)=\beta_{\mathrm{ion}}\,\exp\left[-\frac{(z-z_{\mathrm{ion}})^2}{2w_{\mathrm{ion}}^2}\right]
\]

**Versão fenomenológica compacta (opcional, para comparação AIC/BIC):**

\[
\Omega_f(z)=\beta\,\exp\left[-\frac{(z-z_p)^2}{2w^2}\right]
\]

### B1.1 Mapeamento físico de parâmetros

- \(\beta_{\mathrm{rad}},\beta_{\mathrm{MHD}},\beta_{\mathrm{ion}}\): amplitudes efetivas de cada canal de feedback no budget de energia cosmológica; \(\beta>0\) tende a **aquecimento/injeção** (supressão de SFR), enquanto \(\beta<0\) representa canal efetivo de **resfriamento/compensação** (potencial alívio de supressão).
- \(z_{\mathrm{rad}},z_{\mathrm{MHD}},z_{\mathrm{ion}}\): redshift central de atuação dominante de cada processo (janela temporal de maior acoplamento físico).
- \(w_{\mathrm{rad}},w_{\mathrm{MHD}},w_{\mathrm{ion}}\): largura da janela em redshift; valores maiores implicam efeito distribuído por intervalo mais amplo, valores menores concentram o impacto em episódio curto.
- Na forma compacta, \((\beta,z_p,w)\) representam, respectivamente, amplitude líquida, época central e duração efetiva do feedback agregado.

**Nota de consistência dimensional e normalização:** todas as contribuições \(\Omega_i(z)\) são definidas como frações de densidade normalizadas por \(\rho_{\mathrm{crit},0}=3H_0^2/(8\pi G)\), garantindo que cada termo no colchete de \(H^2(z)/H_0^2\) seja adimensional. Exigir \(H^2(z)>0\) em todo o intervalo analisado preserva a consistência física do fechamento.

### B2. Caminho 2 (modificação no crescimento; recomendado)

Mantém H(z) de ΛCDM e altera diretamente o observável de crescimento:

\[
f\sigma_8(z)=\Omega_m(z)^\gamma\,\sigma_{8,0}\,S(z)
\]

\[
S(z)=1-\alpha\,\exp\left[-\frac{(z-z_p)^2}{2w^2}\right]
\]

### Mapeamento físico de parâmetros

- **Amplitude \(\beta\)** (no Caminho 1): intensidade efetiva do canal físico que entra como termo extra em \(H^2(z)/H_0^2\).
- **Amplitude \(\alpha\)** (no Caminho 2): intensidade efetiva do canal físico que modula diretamente o observável de crescimento \(f\sigma_8\).
- **Largura em redshift \(w\)**: extensão temporal (em tempo cósmico mapeado por \(z\)) ou intervalo efetivo no qual o canal atua de forma relevante.
- **Centro \(z_p\)**: época central do evento de feedback, onde o acoplamento fenomenológico atinge efeito máximo.
- **Convenção de sinal (modelo efetivo):**
  - no Caminho 1, \(\beta>0\) aumenta \(H^2\) (acelera expansão efetiva no intervalo de ação), enquanto \(\beta<0\) reduz \(H^2\);
  - no Caminho 2, com \(S(z)=1-\alpha G(z)\), \(\alpha>0\) reduz \(S(z)\) e suprime crescimento/formação estelar efetiva, enquanto \(\alpha<0\) amplia \(S(z)\) e favorece crescimento.

**Nota curta de consistência:** todos os \(\Omega_i(z)\) usados dentro de \(H^2(z)/H_0^2\) devem ser adimensionais; parâmetros de amplitude devem ser normalizados para manter \(H^2(z)/H_0^2\) adimensional; e a positividade de \(H^2(z)\) deve ser preservada no intervalo de redshift analisado.
- **Amplitude \(\beta\) em \(\Omega_f(z)\):** controla a intensidade efetiva do canal físico de injeção energética no background cosmológico (quanto maior \(|\beta|\), maior a contribuição do canal).
- **Amplitude \(\alpha\) em \(S(z)\):** controla a intensidade efetiva do canal físico de modulação do crescimento estrutural/formação estelar (quanto maior \(|\alpha|\), mais forte o efeito no observável de crescimento).
- **Largura em redshift \(w\):** representa a extensão temporal (intervalo efetivo em redshift) da ação do canal; valores maiores de \(w\) implicam feedback distribuído por uma faixa mais ampla de épocas.
- **Centro da janela \(z_p\):** define a época central do feedback, isto é, o redshift no qual o canal atinge efeito máximo em módulo.
- **Convenção de sinal (modelo efetivo):**
  - no caminho de expansão, \(\beta>0\) tende a aumentar \(H^2(z)\) (reforça a taxa de expansão efetiva local), enquanto \(\beta<0\) tende a reduzir \(H^2(z)\);
  - no caminho de crescimento, com \(S(z)=1-\alpha G(z)\) e \(G(z)>0\), \(\alpha>0\) suprime crescimento/formação estelar efetiva (reduz \(f\sigma_8\)), enquanto \(\alpha<0\) amplifica crescimento efetivo (aumenta \(f\sigma_8\)).

**Nota curta de consistência:** todos os \(\Omega_i(z)\) usados em \(H^2(z)/H_0^2\) devem ser adimensionais; parâmetros de amplitude devem ser normalizados para manter \(H^2(z)/H_0^2\) adimensional; e deve-se preservar a positividade de \(H^2(z)\) no intervalo de redshift analisado.

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


## Consistência com BOOSTERS/EFT

Para garantir consistência entre a parametrização fenomenológica e a base física já definida, adotamos uma decomposição operacional em que `Ω_r` permanece como componente radiativa padrão de fundo, enquanto `Ω_feedback(z)` captura exclusivamente contribuição ativa e localizada em redshift associada a episódios AGN/quasar. Termos legados de BOOSTERS e operadores EFT com suporte funcional equivalente devem ser fixados, recalibrados ou desligados por corrida, de modo a impedir dupla contagem e preservar interpretabilidade estatística.

Esta seção é vinculante para todas as corridas e deve ser aplicada em conjunto com `docs/BOOSTERS.md` (termos de plasma/magnetismo e superposição já definidos) e `docs/LAGRANGIANO_EFT.md` (acoplamentos efetivos e operadores do setor EFT).

### 1) Partição de energia (baseline vs ativo)

- `Ω_r` padrão permanece como baseline radiativo de referência (fótons + neutrinos efetivos do cenário base), sem incorporar automaticamente componentes de feedback localizado.
- `Ω_feedback(z)` representa apenas contribuição ativa e localizada em redshift (janela gaussiana/logística ou equivalente), destinada a capturar injeção AGN/quasar em faixa `z` controlada por parâmetros de amplitude, centro e largura.
- Regra de não sobreposição: qualquer termo com suporte temporal/local equivalente ao de `Ω_feedback(z)` não pode permanecer simultaneamente livre no baseline.

### 2) Mapeamento com BOOSTERS

- Termos de `Ω_B0` (magnético) e `Ω_P0` (plasma), formalizados em `docs/BOOSTERS.md`, devem ser tratados em exatamente uma das modalidades abaixo por corrida:
  - **Modalidade Fundo (background):** contribuição contínua (ex.: escala radiativa `a^-4`) permanece no baseline, e `Ω_feedback(z)` modela apenas excesso transitório.
  - **Modalidade Janela Ativa:** parte/total desses efeitos entra em `Ω_feedback(z)`, e o termo contínuo legado correspondente é congelado ou desligado para evitar duplicação.
- O booster de superposição (`Ω_s0`) deve obedecer ao mesmo princípio de exclusão quando houver parametrização efetiva equivalente na janela ativa.

### 3) Mapeamento com EFT

Com base em `docs/LAGRANGIANO_EFT.md`, adotar as regras operacionais:

- Acoplamentos EFT que geram correção suave e global do fundo permanecem no baseline (parâmetros fixos ou com prior estreito).
- Acoplamentos EFT que induzem resposta transitória associada a AGN/quasar devem migrar para `Ω_feedback(z)` (ou termo equivalente único), desligando duplicatas fenomenológicas.
- Exigência de rastreabilidade 1:1: cada operador/acoplamento EFT ativo deve mapear para um único bloco observável no pipeline (fundo **ou** feedback localizado).

### 4) Matriz operacional por corrida (obrigatória)

| Tipo de corrida | Ω_r padrão | Ω_feedback(z) | Termos legados (BOOSTERS/EFT) | Ação anti-duplicação |
|---|---|---|---|---|
| **Corrida A (ΛCDM baseline)** | Fixo padrão | `0` | Desligados | Manter apenas componentes de referência sem termos ativos equivalentes |
| **Corrida B (feedback puro)** | Fixo padrão | Livre (amplitude/centro/largura) | Equivalentes desligados | Remover do baseline qualquer termo com kernel colinear à janela ativa |
| **Corrida C (boosters físicos)** | Fixo padrão | `0` (ou restrito a residual) | Boosters físicos ligados no fundo; EFT duplicativo desligado | Preservar termos contínuos físicos e bloquear versões transitórias redundantes |
| **Corrida D (híbrida controlada)** | Fixo padrão | Livre sob controle | Subset físico não redundante ativo; duplicativos fixados com prior estreito | Registrar justificativa explícita para cada termo mantido e cada termo desligado |

### 5) Regras de fixar/recalibrar/desligar (checklist)

Antes de cada ajuste, aplicar obrigatoriamente:

- [ ] **Fixar:** parâmetros de baseline bem estabelecidos (`Ω_r`, calibrações de referência) para evitar absorção indevida do sinal.
- [ ] **Recalibrar:** somente termos que alteram a normalização global sem replicar a forma de janela em `z`.
- [ ] **Desligar:** qualquer termo legado cujo kernel temporal/funcional seja colinear com `Ω_feedback(z)` na faixa analisada.
- [ ] **Diagnóstico de degenerescência:** se houver correlação posterior alta entre amplitude de feedback e termo legado, desligar o legado ou impor prior informativo.

### 6) Critério de aceitação da seção

- “Nenhuma corrida é válida se dois blocos ativos modelarem o mesmo efeito físico na mesma janela de redshift.”
- “Comparações AIC/BIC só são reportadas entre modelos com contagem efetiva de parâmetros não redundantes.”


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
