# AMAS / South Atlantic Magnetic Anomaly (SAA) — Caso Observacional RLL/MCRP

Status: **Parcial real em preparação**.

## Escopo
Este documento descreve a AMAS/SAA como caso observacional local para teste da camada geomagnética do RLL/MCRP.

## Princípios de interpretação
- AMAS/SAA **não** constitui prova isolada do RLL.
- A análise deve separar hipótese, dado, modelo e métrica.
- Qualquer reivindicação de validação real exige dados baixados/processados com cadeia de custódia.

## Integração com pipelines
- Matriz de dados: `docs/VALIDATION_DATA_MATRIX_RLL_MCRP.md`.
- Pipeline geomagnético: `docs/pipelines/GEOMAGNETIC_VALIDATION_PIPELINE.md`.
- Pipeline de transmissão/radiação: `docs/pipelines/RADIATION_TRANSMISSION_VALIDATION.md`.
# Anomalia Magnética do Atlântico Sul como Caso Observacional para o RLL/MCRP

## 1) Status epistemológico
- **Este documento não prova o RLL.**
- **Este documento propõe a AMAS/SAA como caso observacional parcial** para testar a camada Magnetismo–Radiação–Plasma.
- A matéria do G1 (publicada em **2026-05-05**) é referência jornalística inicial e **não** fonte científica primária.
- As afirmações técnicas abaixo devem ser rastreadas a fontes científicas primárias e institucionais, com data de origem e versão quando aplicável.

## 2) Resumo técnico
A Anomalia Magnética do Atlântico Sul (AMAS/SAA) é uma região de menor intensidade do campo geomagnético total sobre a América do Sul e o Atlântico Sul. Essa redução regional de blindagem magnética geomagnética está associada a maior penetração de partículas energéticas em altitudes orbitais baixas, com impacto em satélites e instrumentação (erros, resets, SEU e degradação por dose). A AMAS é relevante para o acoplamento entre geodínamo, termos não dipolares/multipolares do campo terrestre, dinâmica da magnetosfera e ambiente de radiação em LEO.

## 3) Conexão com o MCRP
Referência de modelo: `docs/MODELO_COSMOLOGICO_UNIFICADO_MAGNETISMO_RADIACAO_PLASMA.md`.

No encadeamento formal **Galáxia → Heliosfera → Magnetosfera → Atmosfera → Observáveis**, a AMAS pode ser tratada como caso local/regional em que:
- `M(t)` varia regionalmente (intensidade efetiva do campo em superfície/altitude);
- a transmissão magnetosférica `T_M` aumenta para subconjuntos de energias/rigidezes;
- `Φ_eff` pode crescer localmente em órbitas LEO que cruzam a AMAS;
- `Q_ion` pode variar por altitude/orbita e por estado geoespacial;
- observáveis tecnológicos incluem falhas de satélite, ruído instrumental, resets, *single event upsets* (SEU) e dose acumulada.

## 4) Formalização mínima
\[
\Phi_{eff}(E,t,\Omega)=\Phi_{ext}(E,t,\Omega)\cdot T_M(E,\Omega;M(t),m(t),SW)
\]

Onde:
- `Φ_ext`: fluxo externo de partículas/radiação (galáctico, solar, cinturões);
- `T_M`: função de transmissão modulada pelo campo magnético e geometria orbital;
- `M(t)`: intensidade efetiva do campo geomagnético;
- `m(t)`: estrutura/orientação multipolar (incluindo evolução secular);
- `SW`: estado do vento solar/forçamento heliosférico.

## 5) Interpretação física cautelosa
- Campo magnético mais fraco **não** implica ausência total de proteção.
- A AMAS **não** é um “buraco” literal no campo magnético.
- A AMAS **não** prova causalidade cosmológica ampla.
- A AMAS é evidência robusta de que variações geomagnéticas regionais têm consequências tecnológicas mensuráveis.
- A hipótese RLL/MCRP deve ser testada contra dados, com critérios falsificáveis e comparação de modelos.

## 6) Dados recomendados (com data de origem)
1. **IGRF-14 (IAGA/NOAA/NCEI)** — release 2024, válido 2025.0–2030.0; coeficientes de Gauss e SV.
2. **World Magnetic Model (WMM2025, NOAA/NCEI + BGS)** — data de origem 2024-12, válido 2025.0–2030.0.
3. **ESA Swarm** — missão lançada em 2013-11; séries temporais do campo e produtos derivados SAA.
4. **NASA (SAA e ambiente de radiação orbital)** — páginas técnicas e relatórios de missão sobre impactos em eletrônica embarcada.
5. Dados de partículas em LEO, dose/radiação em satélites e telemetria de eventos de anomalia (quando públicos).
6. Mapas de intensidade total do campo, histórico temporal da AMAS e evolução dos coeficientes de Gauss.
7. Dados paleomagnéticos e literatura de geodínamo (incluindo *reversed flux patches* no limite núcleo-manto, CMB).

## 7) Métricas e testes falsificáveis
### Testes
- Comparar evolução temporal da AMAS entre observações (Swarm) e modelos IGRF/WMM.
- Mapear variação de intensidade `B` sobre Atlântico Sul em janelas temporais fixas.
- Correlacionar posição/intensidade da AMAS com eventos de satélite (quando dados públicos existirem).
- Estimar `T_M` regional para órbitas LEO representativas.
- Estimar mudanças em `Φ_eff` em função de altitude, inclinação orbital e fase solar.
- Comparar predições MCRP com dados observacionais reais e com modelo-base sem extensão.

### Métricas
- Erro RMS entre modelo e mapas observados;
- correlação temporal (Pearson/Spearman, conforme distribuição);
- AIC/BIC para modelo-base vs. modelo estendido;
- validação por blocos temporais (*blocked time-series validation*);
- incerteza por Monte Carlo e/ou inferência Bayesiana.

## 8) Limites
- A AMAS é fenômeno geofísico local/regional.
- O RLL é estrutura cosmológica/fenomenológica ampla.
- A ponte AMAS↔RLL deve passar pela camada MCRP, não por afirmação direta.
- Sem dados reais com validação estatística, o status permanece: **Parcial real em preparação**.
- A referência jornalística não deve ser tratada como prova final.

## 9) Cadeia de custódia científica
Para cada dado usado no caso AMAS, registrar obrigatoriamente:
- fonte;
- URL/DOI;
- **data de origem** do dado/produto;
- data de acesso;
- versão;
- hash (se arquivo baixado);
- licença;
- método de processamento;
- script usado;
- saída gerada;
- limitações.

## 10) Fontes primárias e institucionais iniciais
- G1 (referência jornalística inicial, 2026-05-05):
  - https://g1.globo.com/ciencia/noticia/2026/05/05/estudo-desvenda-como-surgiu-a-anomalia-magnetica-que-coloca-em-risco-satelites-sobre-o-atlantico-sul.ghtml
- ESA Swarm (SAA e enfraquecimento regional):
  - https://www.esa.int/Applications/Observing_the_Earth/Swarm/Swarm_probes_weakening_of_Earth_s_magnetic_field
- NASA SAA (impacto em operações orbitais):
  - https://www.nasa.gov/missions/icon/nasa-researchers-track-slowly-splitting-dent-in-earths-magnetic-field/
- NOAA/NCEI (geomagnetismo; WMM):
  - https://www.ncei.noaa.gov/products/world-magnetic-model
- IGRF (IAGA V-MOD):
  - https://www.iaga-aiga.org/igrf/
- Revisado por pares (exemplo sobre persistência não dipolar/SAA):
  - https://www.nature.com/articles/s41467-024-53688-2

## 11) Frase final
**“A AMAS é um caso observacional forte para testar a camada Magnetismo–Radiação–Plasma do RLL, pois conecta campo magnético, radiação, tecnologia orbital e risco mensurável. Ela não valida o RLL por si só; ela fornece uma oportunidade concreta de falsificação, calibração e comparação com dados reais.”**
