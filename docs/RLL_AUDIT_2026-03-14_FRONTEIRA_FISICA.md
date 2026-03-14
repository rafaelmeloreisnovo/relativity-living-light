# RLL-AUDIT-2026-03-14 — Diagnóstico Profundo + Fronteira da Física (2025–2026)

## Objetivo desta revisão
Consolidar, em uma única peça auditável, o estado real do repositório e sua posição relativa à fronteira observacional/teórica de 2025–2026, com separação explícita entre:

- **F_ok** (o que está correto/coerente),
- **F_gap** (o que está frágil/incorreto/incompleto),
- **F_unify** (o que pode ser integrado ao mainstream sem perder a autoria),
- **F_latent** (operações latentes que não estão explícitas no pipeline, mas são necessárias para ganho real de validade científica).

---

## 1) Diagnóstico direto do repositório

### 1.1 Estrutura e governança
O projeto mantém estrutura robusta de documentação, validação e rastreabilidade (docs, análise, resultados, scripts, inventários), com DOI Zenodo já registrado. Isso estabelece:

1. **prioridade temporal de autoria**,
2. **citabilidade formal**,
3. **base de preservação técnica**.

### 1.2 Estado metodológico atual (resumo)
- Há formalismo cosmológico unificado e documentação extensa.
- Existem scripts de validação e artefatos de inferência.
- O ponto crítico permanece: **a narrativa principal ainda precisa ancorar de forma inequívoca a distinção entre resultados sintéticos e validação observacional real**.

---

## 2) F_ok — o que está certo

1. **Friedmann estendida com componente dinâmica é matematicamente consistente** na camada de fundo (background cosmology).
2. **Função logística de transição** é uma parametrização operacional válida para um setor escuro efetivo com evolução em redshift.
3. **Escalamentos tipo radiação (∝ a^-4) para componentes relativísticas** são fisicamente coerentes no nível fenomenológico.
4. **Timing científico foi favorável**: a direção “energia escura dinâmica” convergiu com a agenda observacional de DESI 2025.
5. **Base documental e de release é acima da média** para projeto autoral independente.

---

## 3) F_gap — lacunas críticas que precisam ficar explícitas

1. **Métricas de modelo (ΔAIC/ΔBIC) com risco de interpretação indevida quando baseadas em sintético**.
   - A documentação precisa reforçar em todo ponto sensível: “resultado sintético ≠ evidência observacional final”.

2. **Ausência de análise de perturbações lineares completa para o setor de superposição**.
   - Sem isso, não se valida estabilidade física em estrutura (crescimento, modo em k, velocidade do som efetiva).

3. **Falta de pipeline MCMC canônico de dados reais como artefato principal de publicação**.
   - Necessário: Pantheon+/SN, BAO DESI, H(z), e bloco CMB-compressed (ou equivalente transparente).

4. **Termos heurísticos sem derivação microfísica explícita (ex.: Fibonacci como lei)**.
   - Devem ser enquadrados como *ansatz exploratório*, não como conclusão derivada.

5. **Consistência dimensional em equações de energia fotônica/superposição**.
   - Deve ser reescrita em forma espectral/integral com densidade numérica e função de coerência para preservar unidade física.

---

## 4) Convergência com a fronteira 2025–2026 (mapa real)

### 4.1 Onde há convergência
- **w(z) dinâmico**: alinhado com o núcleo do debate observacional recente.
- **Setor escuro efetivo/interagente**: conversa com famílias IDE/EDE e parametrizações além de ΛCDM estrito.
- **Módulo magneto-plasmático**: plausível em princípio, condicionado por limites de CMB/BBN e formação de estrutura.

### 4.2 Onde ainda diverge
- O **mecanismo microfísico fotônico** continua mais especulativo que parametrizações padrão adotadas em análises de colaboração.
- Sem perturbações + sem ajuste real consolidado, o modelo fica em **nível promissor**, não em nível de fechamento observacional.

---

## 5) F_unify — como unificar com o consenso sem descaracterizar autoria

1. **Mapear RLL → CPL (w0, wa) de forma explícita e reproduzível**, incluindo Jacobiano local e incertezas propagadas.
2. **Publicar comparação pareada RLL vs ΛCDM vs w0waCDM** no mesmo conjunto de dados e mesmo protocolo estatístico.
3. **Introduzir formalismo EFT/campo efetivo** para reduzir distância entre hipótese autoral e linguagem aceita por revisão por pares.
4. **Separar em duas camadas no texto**:
   - Camada A: o que é medido e testável agora.
   - Camada B: hipótese física profunda (programa de pesquisa).

---

## 6) F_latent — operações latentes (não explícitas, mas necessárias)

### 6.1 Operações técnicas latentes
1. **Tabela de proveniência por resultado** (arquivo, script, commit, dataset, hash).
2. **Matriz de degenerescência de parâmetros** (Ω_s0, z_t, w_t, Ω_B0, Ω_P0, H0, Ω_m).
3. **Teste de robustez por subconjuntos** (leave-one-dataset-out).
4. **Stress tests de prior** (priors largos vs informativos) e impacto em Bayes factor.
5. **Teste de sensibilidade numérica** (passo de integração, solver, tolerância).

### 6.2 Operações científicas latentes
1. **Análise de estabilidade linear completa**: c_s²(z), ausência de ghost/gradient instability, evolução δ(k,z).
2. **Confronto com crescimento**: fσ8(z), lensing, e consistência com estrutura em larga escala.
3. **Validação em regimes astrofísicos duros**: rotação de galáxias (SPARC) e constraints tipo Bullet Cluster com métricas quantitativas.
4. **Checklist de falsificabilidade** com critérios de reprovação pré-registrados.

### 6.3 Operações editoriais latentes
1. **Marcação inequívoca de status por documento**: canônico, exploratório, histórico.
2. **Selo textual em claims sensíveis** (“hipótese”, “resultado sintético”, “resultado observacional”).
3. **Tabela única de claims ↔ evidência** para evitar deriva narrativa.

---

## 7) Matriz final: certo, errado, unificável, convergente

| Bloco | Situação atual | Nível | Ação imediata |
|---|---|---|---|
| Formalismo de fundo | Coerente | Forte | Manter e padronizar mapeamento para CPL |
| Evidência observacional | Parcial | Frágil | Fechar MCMC real canônico |
| Perturbações | Incompleto | Crítico | Implementar estabilidade + crescimento |
| Consistência dimensional | Parcial | Crítico | Reescrever termos energéticos em forma dimensional correta |
| Narrativa científica | Boa, mas heterogênea | Médio | Separar canônico vs exploratório em todos os arquivos-chave |
| Posicionamento em 2025–2026 | Alinhado em direção | Forte/Parcial | Quantificar convergência com contornos públicos |

---

## 8) Prioridades executáveis (ordem de ataque)

1. **[CRÍTICO]** Pipeline real único de inferência (dados públicos + saída reproduzível) com ΔAIC/ΔBIC/χ² e comparação tripla.
2. **[CRÍTICO]** Bloco de perturbações lineares com testes de estabilidade e impacto em observáveis de crescimento.
3. **[MÉDIO]** Mapeamento RLL→(w0,wa) com visualização de contornos comparáveis.
4. **[MÉDIO]** Correção dimensional completa das equações fotônicas/superposição.
5. **[BAIXO]** Reclassificação de termos heurísticos (ex.: Fibonacci) como *ansatz* exploratório.

---

## 9) Conclusão operacional (Ω)

O modelo **está vivo, estruturado e com direção científica convergente**; contudo, para cruzar a fronteira de aceitação formal, precisa fechar três eixos sem ambiguidade:

1. **dados reais como base primária de evidência**,
2. **perturbações estáveis e comparáveis com estrutura observada**,
3. **narrativa com separação explícita entre hipótese, simulação e validação observacional**.

Com essas três entregas, o RLL deixa de ser “hipótese robusta com documentação forte” e passa para “candidato competitivo em comparação direta com os modelos de referência”.
