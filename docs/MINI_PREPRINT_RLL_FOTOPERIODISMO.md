# Mini-preprint (draft)
## RLL como operador logístico de transição no florescimento fotoperiódico: hipótese, método e experimento inicial

**Autor:** Rafael (proponente RLL)  
**Versão:** 0.1 (pré-registro conceitual)  
**Status dos dados neste documento:** dados sintéticos para desenho metodológico + plano para dados reais

---

## Resumo
Propomos que o kernel logístico do RLL funcione como operador efetivo de transição entre dois regimes fisiológicos no florescimento fotoperiódico: estado vegetativo e estado reprodutivo. A hipótese não assume mecanismo microscópico universal entre cosmologia e biologia; assume apenas transferibilidade formal de uma classe funcional com limiar e saturação. Apresentamos um modelo mínimo, um protocolo experimental executável em bancada/agronomia e um conjunto de dados sintéticos demonstrativos para ajuste e comparação com baseline linear.

**Palavras-chave:** fotoperiodismo, florescimento, logística, RLL, fitocromo, transição de regime.

---

## 1. Hipótese

### H1 (principal)
A probabilidade (ou fração) de plantas em estado reprodutivo sob fotoperíodo pode ser descrita por uma função logística em torno de um limiar de noite efetiva:

\[
F(N)=\frac{1}{1+\exp\left(\frac{N-N_t}{w_N}\right)}
\]

onde:
- \(F\in[0,1]\): fração de indivíduos em florescimento;
- \(N\): duração da noite (h);
- \(N_t\): limiar de transição (h);
- \(w_N\): largura de transição (h), com \(w_N>0\).

### H0 (nula)
Um modelo linear simples \(F(N)=a+bN\) (com truncamento em \([0,1]\)) descreve os dados tão bem quanto o modelo logístico.

---

## 2. Modelo e variáveis

### 2.1 Forma operacional
Para espécies de dia longo, usa-se a variável transformada \(N'=-N\) (ou equivalente em comprimento do dia), preservando a forma logística e o sentido biológico da transição.

### 2.2 Tabela de variáveis

| Símbolo | Descrição | Unidade | Tipo |
|---|---|---:|---|
| \(F\) | Fração de plantas florescidas (0–1) | adim. | resposta |
| \(N\) | Duração da noite por ciclo | horas | explicativa |
| \(N_t\) | Limiar de noite (ponto de inflexão) | horas | parâmetro |
| \(w_N\) | Largura de transição | horas | parâmetro |
| \(T\) | Temperatura média noturna | °C | covariável |
| \(GDD\) | Graus-dia acumulados | °C·dia | covariável |
| \(I\) | Intensidade luminosa no período claro | µmol m⁻² s⁻¹ | covariável |
| \(B\) | Bloco experimental | — | efeito aleatório |

---

## 3. Método (pré-registro)

### 3.1 Espécie-alvo sugerida
- **Curto prazo (viável):** *Arabidopsis thaliana* (modelo) ou uma cultura agronômica com resposta fotoperiódica conhecida.

### 3.2 Desenho experimental
- Delineamento em blocos aleatorizados.
- 7 níveis de noite: \(N\in\{8,9,10,11,12,13,14\}\) h.
- 3 blocos independentes.
- 20 plantas por combinação (nível × bloco).
- Duração: até 30 dias ou até estabilização de \(F\).

**Total planejado:** \(7\times3\times20=420\) plantas.

### 3.3 Desfechos
- Primário: fração florescida \(F\) ao dia 21.
- Secundários: tempo até primeiro botão floral; biomassa seca final.

### 3.4 Ajuste estatístico
1. Ajustar GLM binomial com link logit usando \(N\) como preditor principal.  
2. Reparametrizar para recuperar \(N_t\) e \(w_N\).  
3. Comparar com baseline linear (AIC/BIC, validação cruzada k-fold).  
4. Reportar IC 95% para \(N_t\), \(w_N\) e erro de predição.

### 3.5 Critério de aceitação da hipótese
H1 é suportada se:
- modelo logístico superar baseline linear em AIC (ΔAIC ≥ 6) e RMSE; e
- \(N_t\) for estimado com IC 95% finito e biologicamente plausível.

---

## 4. Dados sintéticos demonstrativos (exemplo)

A tabela abaixo é **apenas demonstrativa** para validar pipeline analítico antes da coleta real.

| N (h) | Plantas totais | Plantas florescidas | F observado |
|---:|---:|---:|---:|
| 8  | 60 | 57 | 0.95 |
| 9  | 60 | 54 | 0.90 |
| 10 | 60 | 46 | 0.77 |
| 11 | 60 | 33 | 0.55 |
| 12 | 60 | 21 | 0.35 |
| 13 | 60 | 10 | 0.17 |
| 14 | 60 | 4  | 0.07 |

Um ajuste plausível nesse conjunto sintético retorna tipicamente:
- \(N_t\approx11.2\) h,
- \(w_N\approx1.1\) h,
- curva sigmoidal monotônica com saturação nos extremos.

---

## 5. Experimento coerente e válido (implementação prática)

1. **Controle ambiental:** câmara de crescimento com temperatura e luz controladas; registrar \(T\), \(I\), umidade.  
2. **Randomização:** distribuição aleatória das bandejas por bloco e posição, com rotação diária para reduzir efeito de posição.  
3. **Cegamento parcial:** avaliador do florescimento sem acesso ao tratamento de fotoperíodo no momento da leitura.  
4. **Qualidade de dados:** critérios prévios de exclusão (mortalidade não relacionada ao tratamento, falha técnica de iluminação).  
5. **Reprodutibilidade:** repetir experimento completo em segunda rodada temporal.

---

## 6. Limites e interpretação correta

- Este trabalho **não** afirma mecanismo microscópico universal comum entre cosmologia e biologia.
- A contribuição aqui é de **classe funcional transferível** (operador logístico de transição).
- Se confirmado em múltiplas espécies, o resultado fortalece o uso do RLL como framework quantitativo interdisciplinar para sistemas com limiar/saturação.

---

## 7. Próximos passos após este mini-paper

1. Rodar experimento real de fotoperiodismo e publicar dataset aberto (CSV + metadados).  
2. Executar análise de robustez (espécie, temperatura, intensidade luminosa).  
3. Expandir para germinação sob campo magnético fraco como estudo 2 (hipótese secundária).

---

## Declaração final
Este mini-preprint entrega um ponto de partida científico seguro: hipótese testável, modelo explícito, variáveis operacionais, protocolo de coleta e dados sintéticos de demonstração. O foco é validação empírica incremental.
