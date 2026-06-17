# 15 — Dados Externos Reais RLL

**Status:** canônico complementar  
**Origem:** extraído de `docs/canonicos/BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md`  
**Função:** listar pacotes observacionais usados ou pendentes para validação.

---

## 1. Regra de uso dos dados

Todos os dados externos devem vir de fonte primária ou repositório oficial. Quando houver dúvida de identificador, ano, versão, matriz de covariância ou valor numérico, marcar como `[VAZIO]` até verificação.

## 2. Pacotes cosmológicos principais

### 2.1 DESI DR2 BAO [E]

- Tracers: BGS, LRG, ELG, QSO, Lyα.
- Observáveis: `DV/rd`, `DM/rd`, `DH/rd`.
- Total indicado no documento-mãe: 13 observáveis.
- Caveat: matriz completa inter-tracer deve ser verificada em fonte oficial.

### 2.2 CMB Planck distance priors [E]

- Variáveis: `R`, `lA`, `ωb`, `ns`.
- Usar matriz de correlação quando disponível.
- Caveat: confirmar identificador e tabela antes de citação formal.

### 2.3 Cronômetros cósmicos H(z) [E]

- Base: pontos de expansão H(z) por idade diferencial de galáxias.
- Usar covariância sistemática quando disponível.
- Caveat: pipeline deve explicitar quais pontos foram usados e quais foram excluídos.

### 2.4 fσ8 crescimento de estrutura [E]

- Usado para testar crescimento, não apenas background cosmológico.
- Caveat: baixo-z e correlações devem ser confirmados em portal primário.

## 3. Métricas de comparação

```text
χ² = rᵀ·C⁻¹·r
AIC  = χ²_min + 2k
AICc = AIC + 2k(k+1)/(n−k−1)
BIC  = χ²_min + k·ln(n)
```

A comparação deve registrar:

- número de dados `n`;
- número de parâmetros `k`;
- matriz de covariância usada;
- versão dos dados;
- commit do pipeline;
- data da execução.

## 4. Resultado-base registrado

O documento-mãe registra que, com dados reais e erros diagonais no recorte z∈[0,2.4], o ΛCDM fica levemente preferido sobre RLL nos parâmetros atuais.

Essa informação deve ser preservada como integridade científica, não apagada.

## 5. Pendências marcadas como [VAZIO]

- matriz 13×13 DESI em bloco completo;
- covariância sistemática completa dos cronômetros cósmicos;
- valores baixo-z de fσ8 e correlações;
- identificação primária de todas as referências usadas na camada neuro/física/linguística.

---

*Dados reais primeiro; inferência depois.*