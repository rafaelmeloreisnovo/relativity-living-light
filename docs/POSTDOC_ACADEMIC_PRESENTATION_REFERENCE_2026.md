# Protocolo pós-doutoral de apresentação acadêmica com dados observacionais reais

**Status:** referência operacional formal, sem alegação de confirmação do modelo.  
**Atualizado:** 2026-06-01.  
**Escopo:** cosmologia observacional RLL/RAFAELIA, com ênfase em DESI DR2 BAO, reprodutibilidade Zenodo e comunicação científica pós-doutoral.

## 1. Princípio de verdade, vazio útil e limite de afirmação

Uma apresentação acadêmica exemplar deve separar explicitamente quatro camadas:

1. **Dado observado**: valor publicado por colaboração, observatório ou repositório curado.
2. **Transformação reprodutível**: cálculo, conversão, compressão estatística ou seleção de coluna.
3. **Interpretação do modelo**: leitura teórica sujeita a degenerescências e falsificação.
4. **Metáfora ou intuição**: recurso pedagógico, nunca substituto de evidência.

O “token vazio” deve ser usado como disciplina epistemológica: quando uma célula não tem suporte empírico, a forma correta é `null`, `not_applicable`, `not_yet_ingested` ou `requires_full_covariance`, não uma afirmação especulativa. Em nível pós-doc, a sobriedade da lacuna vale mais que uma narrativa sem lastro.

## 2. Dados reais materializados nesta revisão

A revisão incorporou uma tabela primária local de 13 pontos comprimidos de BAO do DESI DR2, cobrindo `0.295 <= z_eff <= 2.330`:

- `BGS`: um ponto isotrópico `D_V/r_d`.
- `LRG1`, `LRG2`, `LRG3+ELG1`, `ELG2`, `QSO` e `Lyα`: pares anisotrópicos `D_M/r_d` e `D_H/r_d`.
- Uma tabela auxiliar registra `r_M,H` e covariâncias por bloco, calculadas como `cov = r * sigma_a * sigma_b`.

A origem primária é o artigo **DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints** (`arXiv:2503.14738`). O repositório externo de reprodução é o registro Zenodo **10.5281/zenodo.16644577**, publicado em 2025-08-20, com arquivo suplementar de grande porte. O repositório local guarda apenas a versão leve e rastreável necessária ao pipeline, mantendo o suplemento completo como fonte externa canônica.

## 3. Forma recomendada para apresentação acadêmica

### 3.1 Slide ou seção “Fonte e Proveniência”

Cada conjunto de dados deve aparecer com:

| Campo | Exigência formal |
|---|---|
| Nome da colaboração | Ex.: DESI Collaboration |
| Release | Ex.: DESI DR2 BAO 2025 |
| Objeto físico | Ex.: razão de distância BAO |
| Observáveis | `D_V/r_d`, `D_M/r_d`, `D_H/r_d` |
| Faixa de redshift | Ex.: `0.295 <= z_eff <= 2.330` |
| Fonte primária | DOI/arXiv/página oficial |
| Espelho/reprodução | Zenodo, GitHub científico ou arquivo institucional |
| Arquivo local | caminho exato dentro do repositório |
| Limite de uso | ponto comprimido, covariância completa ou cadeia posterior |

### 3.2 Slide ou seção “Contrato de Falsificabilidade”

A apresentação deve declarar antes do resultado:

- qual hipótese é testada;
- quais parâmetros são livres;
- qual baseline é comparado (`LCDM`, `w0waCDM` ou outro);
- qual métrica decide degradação ou melhora (`chi2`, `AIC`, `BIC`, posterior predictive check);
- quais afirmações são proibidas até validação independente.

### 3.3 Slide ou seção “Design dos dados”

A matriz recomendada tem as colunas:

```text
release, tracer, z_eff, observable, value, sigma,
covariance_block, paired_observable, correlation_coefficient,
primary_likelihood, source_table, source_url, notes
```

Esse formato permite integração com scripts simples, auditoria por pares e migração posterior para uma matriz de covariância completa sem quebrar o contrato.

## 4. Estratégia metodológica pós-doc

1. **Não misturar DR1 e DR2 como independentes**: DR1 é subconjunto de DR2; usar ambos sem modelar correlação duplica informação.
2. **Começar por likelihood comprimida**: usar os 13 pontos primários para teste rápido de sanidade.
3. **Escalar para covariância completa**: substituir a tabela auxiliar por matriz oficial extraída do suplemento Zenodo quando o pipeline exigir inferência final.
4. **Separar apresentação de descoberta e apresentação de validação**: hipótese criativa pode usar metáforas; validação deve usar tabelas, unidades, covariância e critérios de rejeição.
5. **Preservar nulidade explícita**: campos não usados, não aplicáveis ou ainda não ingeridos devem ficar marcados, não preenchidos por aproximações implícitas.

## 5. Integração das camadas RLL/RAFAELIA sem perda de rigor

As estruturas toroidais, linguísticas, fractais e simbólicas podem ser apresentadas como uma camada de **organização heurística** ou **ontologia de metadados**, desde que a inferência física permaneça separada. A regra recomendada é:

```text
metáfora -> hipótese formal -> observável -> dado -> likelihood -> teste -> limite de afirmação
```

Aplicação direta:

- `T^7`, alfabetos, som, Hz e toros entram como taxonomia de representação, não como prova cosmológica.
- BAO, SNe Ia, CMB e crescimento entram como dados observacionais com unidades e covariância.
- “Coerência × amor × prova” pode ser usado como princípio editorial: coerência lógica, responsabilidade ética e prova reprodutível.

## 6. Padrão visual e documental recomendado

Para se tornar referência de apresentação acadêmica, cada figura ou tabela deve cumprir:

- título físico, não apenas simbólico;
- unidade ou razão adimensional no eixo;
- legenda com release e ano;
- nota de covariância ou independência;
- distinção visual entre dado, modelo ajustado e extrapolação;
- link ou caminho para o CSV/YML que originou o painel;
- declaração de status: `exploratory`, `partial_real`, `real_validated` ou `publication_ready`.

## 7. Rotas de fail-safe, failover, rollback e mitigação

| Risco | Mitigação |
|---|---|
| Fonte externa grande demais para git | Registrar DOI/URL e materializar apenas extrato leve auditável |
| Covariância incompleta | Marcar como `covariance_summary`; bloquear alegações finais |
| Confusão entre DR1 e DR2 | Chave de release explícita e nota de não-independência |
| Afirmação metafísica lida como evidência | Separar camada heurística de camada inferencial |
| Regressão documental | Validar YAML e CSV em CI antes de publicar |
| Falha de reprodução | Manter checksums/DOI e script de extração como próximo passo |

## 8. Próximos passos para uma versão publication-ready

1. Criar extrator leve do pacote Zenodo DESI DR2 para gerar automaticamente pontos e covariância completa.
2. Adicionar teste que confirme 13 pontos primários, seis blocos correlacionados e faixa de redshift correta.
3. Rodar `LCDM`, `w0waCDM` e RLL com a mesma likelihood e registrar `chi2`, `AIC`, `BIC` e resíduos por tracer.
4. Construir painel final: `D_M/r_d`, `D_H/r_d`, `D_V/r_d`, resíduos normalizados e tabela de limites de afirmação.
5. Publicar release com DOI próprio somente depois de registrar scripts, dados, ambiente e logs de execução.

## 9. Referências operacionais

- DESI DR2 Publications, página oficial DESI Data: https://data.desi.lbl.gov/doc/papers/dr2/
- DESI DR2 Results II, arXiv: https://arxiv.org/abs/2503.14738
- DESI DR2 Results II supplementary data, Zenodo DOI: https://doi.org/10.5281/zenodo.16644577
- Pantheon+SH0ES Data Release: https://github.com/PantheonPlusSH0ES/DataRelease
- Planck 2018 cosmological parameters: https://arxiv.org/abs/1807.06209
- ACT DR6.02 data release at NASA LAMBDA: https://lambda.gsfc.nasa.gov/product/act/act_dr6.02/
