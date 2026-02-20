# Roadmap de Validação — Relativity Living Light
## Da prova de conceito à publicação científica

**Versão:** 2.0 | **Data:** Fevereiro 2026  
**TRL atual:** 3 (dados sintéticos) → **TRL alvo:** 6 (validação com dados reais)

---

## Prioridade 1 — Consistência interna (1–2 semanas)

**Objetivo:** Eliminar inconsistências documentais que prejudicam credibilidade imediata.

**Ações:**
- Atualizar todos os documentos que citam Ω_s0 ≈ 0.72, z_t ≈ 0.65, w_t ≈ −0.97 para os valores reais do CSV (Ω_s0 = 0.059, z_t = 1.164, w_t = 0.405)
- Remover do README e do preprint LaTeX a tabela de parâmetros com valores inconsistentes
- Adicionar disclaimer explícito de "dados sintéticos" em todos os resultados quantitativos
- Separar o repositório em branch `scientific` (técnico) e manter o conteúdo simbólico em `manifesto`

**Entregável:** README_CIENTIFICO.md + PAPER_CORRIGIDO.tex (já gerados neste pacote)

---

## Prioridade 2 — Validação parcial com dados reais (2–4 semanas)

**Objetivo:** Primeiro teste do modelo contra dados observacionais públicos.

**Dataset:** BOSS DR12 fσ₈(z) — 6 pontos com erros, público em `github.com/sdss/boss`

**Ações:**
1. Implementar `codigo/crescimento_estrutural.py` (já incluído neste pacote)
2. Resolver a equação D''(a) com os parâmetros centrais do modelo
3. Comparar fσ₈(z) do RLL com dados BOSS e com ΛCDM
4. Reportar ΔAIC/ΔBIC (mesmo que com χ² parcial, é o primeiro resultado com dados reais)

**Previsão quantitativa:** Desvio RLL vs ΛCDM em fσ₈ de −2% a −4% em z ∈ [0.3, 0.8], marginal para BOSS mas detectável por DESI

**Entregável:** Figura `fs8_comparison.png` + tabela de χ² parcial

---

## Prioridade 3 — Dados reais de supernovas (4–8 semanas)

**Objetivo:** Substituição total dos dados sintéticos por Pantheon+.

**Dataset:** Pantheon+ — 1701 SNe Ia, completo com matriz de covariância  
**URL:** `github.com/PantheonPlusSH0ES/DataRelease`

**Ações:**
1. Adaptar `codigo/panteon_likelihood.py` para carregar CSV Pantheon+
2. Definir likelihood de módulo de distância com covariância completa:  
   `χ² = (μ_obs − μ_model)^T · C^{−1} · (μ_obs − μ_model)`
3. Rodar MCMC (emcee ou dynesty) com prior flat nos parâmetros
4. Reportar posterior real, ΔAIC e ΔBIC vs. ΛCDM

**Critério de sucesso:** ΔAIC > 0 (modelo favorecido), ou rejeição honesta se ΔAIC < 0

**Entregável:** Novo `posterior_real_pantheon.csv` + corner plot + atualização do paper

---

## Prioridade 4 — Adição de BAO — DESI DR2 (8–12 semanas)

**Objetivo:** Análise combinada SNe Ia + BAO, o conjunto mais poderoso para w(z).

**Dataset:** DESI DR2 BAO — H(z)·r_d, D_M(z)/r_d, público  
**URL:** `data.desi.lbl.gov`

**Ações:**
1. Implementar likelihood de BAO com covariância DESI
2. Calcular distância de co-mover D_M(z) e H(z) do modelo RLL
3. Constraint conjunta: Pantheon+ + DESI BAO no mesmo MCMC
4. Comparar resultado com ΛCDM e com CPL (w₀wₐCDM)

**Nota:** A parametrização CPL é o benchmark padrão do DESI. O modelo RLL deve ser comparado explicitamente com ela para ser avaliado pela comunidade.

---

## Prioridade 5 — Extensão anisotrópica (paralelo, 1–3 meses)

**Objetivo:** Testar f(z,θ,φ) contra anomalia de dipolo de Böhme et al. (2025).

**Ações:**
1. Implementar grid HEALPix com f(z,θ,φ) usando código em `teoria/EXTENSAO_ANISOTROPICA.md`
2. Extrair direção preferencial de Böhme et al.
3. Ajustar (A_z, A_w) para reproduzir amplitude de 5.4σ
4. Verificar consistência com mapa de CMB Planck

**Por que prioritário:** Este é o teste mais original do modelo — não existem outros trabalhos que parametrizem o dipolo CMB via transição DE↔DM direcional. Resultado positivo seria publicável em Physical Review Letters.

---

## Prioridade 6 — Verificação de estabilidade (paralelo, 2 semanas)

**Objetivo:** Confirmar ausência de ghosts e taquiões.

**Ações:**
1. Executar `check_stability()` de `teoria/ESTABILIDADE_GHOST_CHECK.md` para todo o posterior
2. Verificar cs² > 0 com prescrição física cs² = f(z)
3. Confirmar w_eff ≥ −1 (sem phantom crossing) para 95% do espaço de parâmetros

---

## Prioridade 7 — Preprint arXiv (após Prioridades 2–4)

**Objetivo:** Publicação científica reconhecida com dados reais.

**Estrutura do paper:**
1. Abstract com resultado principal (ΔAIC vs ΛCDM com dados reais)
2. Modelo (Eq. Friedmann, f(z), w_eff)
3. Dados: Pantheon+ + DESI BAO + BOSS fσ₈
4. Resultados: posterior, comparação modelos, figura H_ratio e fσ₈
5. Conexão com DESI dinâmico e Minnesota PRL 2026
6. Extensão anisotrópica (se Prioridade 5 concluída)
7. Conclusão com roadmap Euclid/CMB-S4

**Destino:** arXiv astro-ph.CO → submissão JCAP ou Universe

---

## Cronograma Resumido

```
Semanas 1-2:   Prioridade 1 (consistência documental)       [já parcialmente feito]
Semanas 2-4:   Prioridade 2 (BOSS fσ₈ com dados reais)
Semanas 4-8:   Prioridade 3 (Pantheon+)
Paralelo:      Prioridade 6 (estabilidade)
Meses 2-3:     Prioridade 4 (DESI BAO)
Paralelo:      Prioridade 5 (extensão anisotrópica)
Mês 3-4:       Prioridade 7 (preprint arXiv)
```

---

## Recursos Necessários

**Computação:** MCMC com Pantheon+ (1701 pontos) + DESI BAO (~50 pontos) converge em 4–8h em CPU padrão com emcee (200 walkers × 5000 steps). Sem necessidade de GPU ou cluster.

**Dependências Python:**
```
numpy, scipy, emcee (ou dynesty), astropy,
matplotlib, corner, healpy (para anisotropia)
```

**Dados públicos:** Todos os datasets necessários são de acesso livre.
