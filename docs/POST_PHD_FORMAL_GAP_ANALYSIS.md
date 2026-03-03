# Análise de Lacunas — RLL para padrão pós-PhD formal/profissional

**Escopo:** transformar o repositório em referência intelectual, estrutural e acadêmica com padrão de submissão internacional (arXiv + journal + reprodutibilidade auditável).

---

## 1) Diagnóstico objetivo (estado atual)

### Pontos fortes já presentes
- Governança documental forte (índices, inventários, preservação histórica e trilha canônica).
- Núcleo científico explícito (`PAPER_CORRIGIDO.tex`, `RESULTADOS_CORRIGIDOS.md`, scripts em `docs/`).
- Artefatos de dados e figuras já consolidados para etapa sintética.

### Lacunas críticas para nível pós-PhD formal
1. **Validação observacional real ainda não fechada** (Pantheon+/BAO/RSD/CMB com métricas publicáveis).
2. **Conflito de narrativa entre "estado atual" e "blueprint"** em partes da documentação.
3. **Higiene de release incompleta** (duplicatas, organização de figuras, consistência de claims de segurança).
4. **Pacote de reprodutibilidade ainda parcial** (execução ponta-a-ponta com saída canônica e rastreável).
5. **Plano de publicação não operacionalizado** (alvos, critérios de aceite, checklist de submissão e resposta a parecer).

---

## 2) Critérios mínimos de “padrão pós-PhD”

Para ser referência formal, o projeto precisa cumprir simultaneamente:

- **C1 — Evidência observacional:** comparação RLL vs ΛCDM com `χ²`, `AIC`, `BIC` e (idealmente) Bayes factor.
- **C2 — Reprodutibilidade executável:** um comando principal que gera tabelas/figuras finais a partir de dados reais.
- **C3 — Integridade e rastreabilidade:** inventário único de artefatos, hashes e versão de cada resultado.
- **C4 — Consistência editorial:** uma trilha oficial única (sem ambiguidade com material de blueprint/histórico).
- **C5 — Publicação profissional:** pacote pronto para arXiv + journal (texto, figuras, apêndices, dados, software citation, limitações).

---

## 3) Gap matrix (falta vs ação concreta)

| Pilar | Lacuna atual | Evidência de prontidão | Ação de fechamento |
|---|---|---|---|
| Observacional | Pipeline real incompleto | `panteon_likelihood.py` é template | Fechar ingestão Pantheon+, rodar ajuste e gerar tabela RLL vs ΛCDM com métricas |
| Método estatístico | Forte no sintético, fraco no real | CSV/posterior sintético e forecast Fisher | Consolidar bloco único de inferência com saída `results/` versionada |
| Reprodutibilidade | Scripts existem, mas fluxo ainda não unificado | `requirements.txt`, scripts de crescimento/Fisher/Pantheon | Criar rotina de execução ponta-a-ponta + validação automática de arquivos |
| Arquitetura documental | Excelente, porém com sobreposição de trilhas | índice mestre e canônicos bem definidos | Marcar explicitamente “canônico”, “blueprint” e “arquivo histórico” |
| Qualidade editorial | Material autoral extenso pode poluir trilha técnica | separação já iniciada | manter trilha técnica isolada para paper e revisão por pares |
| Segurança/integridade | claims desatualizados em alguns pontos | checklist de integridade já existe | sincronizar SECURITY com estado real e inventário efetivo |

---

## 4) Roadmap de profissionalização (execução direta)

### Fase A — 0 a 14 dias (fechar prova observacional mínima)
1. Rodar Pantheon+ real com trilha documentada de ingestão.
2. Gerar `χ²`, `AIC`, `BIC` para RLL e ΛCDM.
3. Exportar tabela final em `data/results/` e figuras em `figs/paper/`.
4. Atualizar `RESULTADOS_CORRIGIDOS.md` com bloco “dados reais v1”.

**Entrega da fase:** primeira evidência observacional publicável.

### Fase B — 15 a 30 dias (blindagem de reprodutibilidade)
1. Criar script único de execução científica (ex.: `run_validation.sh` ou equivalente Python) para gerar artefatos finais.
2. Incluir validações automáticas de inputs/outputs (existência, formato, checksum básico).
3. Padronizar um comando canônico único de execução ponta-a-ponta: `scripts/run_repro_all.sh` (com variantes `--bayes` e `--with-two-rad`).
4. Fixar convenção de versionamento de resultados (data + hash + commit).

**Entrega da fase:** pipeline auditável de ponta a ponta.

### Fase C — 30 a 60 dias (pacote de submissão formal)
1. Congelar versão do preprint técnico com escopo estritamente científico.
2. Incluir seção explícita de limitações e riscos de interpretação.
3. Preparar pacote de submissão: carta de cobertura, contribuição, reprodutibilidade, disponibilidade de dados/código.

**Entrega da fase:** pacote pronto para arXiv + journal alvo.

---

## 5) Estrutura editorial recomendada (para referência intelectual)

- **Trilha A (canônica técnica):** paper, métodos, resultados, validação, reprodutibilidade.
- **Trilha B (blueprint/P&D):** hipóteses estendidas, arquitetura futura, estudos exploratórios.
- **Trilha C (arquivo autoral/histórico):** manifesto, evolução narrativa, memória institucional.

Regra operacional: **toda afirmação científica no paper deve apontar para dado, script ou figura reproduzível.**

---

## 6) Checklist de prontidão para “referência acadêmica”

Marcar como concluído apenas com evidência verificável:

- [ ] Comparativo observacional RLL vs ΛCDM com métricas (`χ²`, `AIC`, `BIC`, Bayes factor quando disponível).
- [ ] Scripts executam sem ambiguidade de caminho e geram artefatos em diretórios canônicos.
- [ ] Documento de segurança/integridade coerente com o estado real dos arquivos.
- [ ] Duplicatas removidas ou justificadas com política explícita.
- [ ] Preprint técnico sem mistura com material não científico no corpo principal.
- [ ] Release com DOI/metadata consistente entre `CITATION.cff`, Zenodo e paper.

---

## 7) Conclusão objetiva

O projeto já está **forte em coerência documental e em prototipagem científica**. O salto para padrão pós-PhD formal depende principalmente de **fechar a prova observacional real com métricas comparativas** e **travar um pipeline reprodutível auditável**. Com isso, o repositório passa de “excelente estrutura + forte sintético” para “evidência acadêmica competitiva e profissional”.
