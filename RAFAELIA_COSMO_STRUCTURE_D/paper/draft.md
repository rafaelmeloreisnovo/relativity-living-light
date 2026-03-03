# Draft (paper skeleton)

> Governança de evidências: novas claims só entram neste draft com rastreabilidade prévia em `paper/evidence_traceability.md`.

## Abstract
Este trabalho testa, no escopo de dados de expansão e crescimento usados no fluxo legado do Structure D, se uma extensão fenomenológica do tipo RLL-like+AGN melhora a descrição observacional em relação ao ΛCDM. Usamos o conjunto conjunto de observações com \(N=45\) pontos (\(H(z)\) e \(f\sigma_8(z)\)) e comparamos dois modelos: (i) ΛCDM com \(k=4\) parâmetros livres e (ii) RLL-like+AGN com \(k=7\). O ajuste é feito por máxima verossimilhança Gaussiana, reportado via \(\chi^2\), AIC e BIC. O melhor \(\chi^2\) numérico é praticamente idêntico entre modelos (123.681 para ΛCDM e 123.679 para RLL-like+AGN; \(\Delta\chi^2=-0.002\) em favor do modelo estendido), porém a penalização por complexidade domina: \(\Delta\mathrm{AIC}=+5.998\) e \(\Delta\mathrm{BIC}=+11.418\) (RLL-like+AGN menos favorecido). Conclusão quantitativa: com estes dados e esta configuração, a evidência de informação favorece ΛCDM de forma moderada (AIC) a forte (BIC), sem ganho estatístico relevante em \(\chi^2\).

## Introduction
- ΛCDM successes
- H0/S8 tensions (context)
- Role of baryonic/AGN feedback
- Proposed effective extension (RLL_like + AGN)

## Methods
### Dados e modelos comparados
Foram usados os dados agregados do fluxo legado com \(N=45\) observações totais e duas famílias de predição:
- **ΛCDM**: parâmetros livres \(\{H_0,\Omega_m,\Omega_\Lambda,\Omega_b h^2\}\), total \(k=4\).
- **RLL-like+AGN**: parâmetros livres \(\{H_0,\Omega_m,\Omega_\Lambda,\Omega_{s0},z_t,w_t,\Omega_b h^2\}\), total \(k=7\).

Parâmetros tratados como fixos na prática de comparação desta versão: \(N\) (tamanho amostral), forma funcional dos modelos e a política de ruído Gaussiano por ponto (sem termo extra de hiper-ruído livre no ajuste reportado).

### Função de verossimilhança
Assumimos likelihood Gaussiana independente por ponto para os blocos usados no resultado legado:
\[
\chi^2(\theta)=\sum_i\left(\frac{x_i^{\mathrm{obs}}-x_i^{\mathrm{mod}}(\theta)}{\sigma_i}\right)^2,
\qquad
\ln\mathcal{L}(\theta)=-\frac{1}{2}\chi^2(\theta)+\mathrm{const}.
\]
O estimador pontual é o conjunto \(\hat\theta\) que minimiza \(\chi^2\).

### Critérios de seleção de modelo
Foram aplicados os três critérios abaixo:
- \(\mathrm{AIC}=\chi^2+2k\)
- \(\mathrm{BIC}=\chi^2+k\ln N\)
- Evidência Bayesiana por \(\ln B\) (**quando disponível**); nesta versão de resultados legados, \(\ln B\) não foi publicado junto da tabela final comparativa.

Convenção de diferença: \(\Delta\mathrm{AIC}=\mathrm{AIC}_{\mathrm{RLL}}-\mathrm{AIC}_{\Lambda\mathrm{CDM}}\) e \(\Delta\mathrm{BIC}=\mathrm{BIC}_{\mathrm{RLL}}-\mathrm{BIC}_{\Lambda\mathrm{CDM}}\). Valores positivos penalizam o modelo estendido.

### Política de covariância
Política declarada para o pipeline: usar covariância completa quando disponível e fallback diagonal por \(\sigma_i\) quando não houver matriz completa para um bloco observacional; no recorte legado usado na tabela final, a forma efetiva é diagonal por ponto, compatível com a definição explícita de \(\chi^2\) acima.

## Results
Tabela final numérica (sem arredondamento interpretativo extra):

| Modelo | \(\chi^2\) | AIC | BIC | \(\Delta\)AIC vs ΛCDM | \(\Delta\)BIC vs ΛCDM | \(\ln B\) |
|---|---:|---:|---:|---:|---:|---:|
| ΛCDM | 123.681 | 131.681 | 138.908 | 0.000 | 0.000 | N/D |
| RLL-like+AGN | 123.679 | 137.679 | 150.326 | +5.998 | +11.418 | N/D |

Síntese objetiva do resultado:
- Melhora em \(\chi^2\): \(-0.002\) (numericamente desprezível para \(+3\) parâmetros).
- Penalização por complexidade: \(+5.998\) em AIC e \(+11.418\) em BIC.
- Decisão por critério de informação: ΛCDM preferido neste conjunto de dados.

### External validation

- **Objetivo:** validar o modelo em dois níveis explícitos e não intercambiáveis:
  1) **convergência qualitativa** (mesma direção física);
  2) **suporte quantitativo** (compatibilidade estatística com métricas comparáveis).
- **Ponte quantitativa com DESI/CPL:** incluir mapeamento explícito \(w_{RLL}(a)\rightarrow(w_0,w_a)\) usando expansão local em \(a=1\):
  - \(w_0=-f_0\)
  - \(w_a=-\left.dw/da\right|_{a=1}=-f_0(1-f_0)/w_t\)
- **Métricas comparáveis obrigatórias:** \(\chi^2_{\min}\), \(\Delta\)AIC, \(\Delta\)BIC, PPC e distância em sigma para \((w_0,w_a)\).
- **Critérios de rejeição objetivos (falsificação):**
  - \(\Delta\)AIC>10 e \(\Delta\)BIC>10;
  - p-valor global do ajuste < 0.01;
  - inconsistência >3σ no plano \((w_0,w_a)\) contra contornos externos;
  - viés residual \(|\langle r/\sigma\rangle|>2\) em ≥2 observáveis independentes.
- **Tabela de previsões falsificáveis:** incluir tabela por observável/dataset futuro (DESI DR3, Euclid, Roman, SKA, CMB-S4) com coluna “critério de falha”.
- **Referência de apoio:** alinhar esta subseção com `docs/COMPARACAO_DESI_2025.md` (seção “External validation”).

## Discussion
Limitações explícitas deste resultado:
1. A tabela final usada é de trilha legada; não inclui \(\ln B\) estimado para a mesma corrida comparativa.
2. O conjunto avaliado (\(N=45\)) é restrito ao recorte disponível no artefato legado e não cobre, nesta tabela, combinações completas com BAO, SNe, lentes e CMB shift no mesmo fit conjunto.
3. O ganho de ajuste do modelo estendido é muito pequeno frente ao custo paramétrico; isso aumenta risco de sobreajuste fenomenológico.

Testes de refutação previstos (critérios que invalidariam o modelo RLL-like+AGN no escopo deste estudo):
- **Refutação por parcimônia**: se em reexecução canônica com mesmos dados o modelo estendido mantiver \(\Delta\mathrm{AIC}>0\) e \(\Delta\mathrm{BIC}>0\), ele permanece desfavorecido por informação.
- **Refutação por robustez entre datasets**: se ao adicionar novos blocos observacionais padronizados (p.ex. BAO/SNe/lensing) o modelo não reduzir \(\chi^2\) o bastante para compensar \(\Delta k=3\), a hipótese de vantagem física efetiva é rejeitada.
- **Refutação por estabilidade de parâmetros**: se parâmetros extras \((\Omega_{s0},z_t,w_t)\) não se estabilizarem em intervalos estreitos sob variações de prior/configuração, a extensão é classificada como não identificável neste regime de dados.

## Conclusion
No escopo estrito da comparação numérica reportada aqui (dados legados com \(N=45\), dois modelos e métricas \(\chi^2\)/AIC/BIC), não há suporte estatístico para afirmar superioridade do modelo RLL-like+AGN sobre ΛCDM. A única afirmação sustentada pelos números é: o ajuste em \(\chi^2\) é praticamente igual, mas AIC e BIC penalizam o modelo estendido de forma relevante. Portanto, qualquer extrapolação para “nova física confirmada”, para outros conjuntos de dados ou para inferência cosmológica global está fora do escopo desta evidência específica.
