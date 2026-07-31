# Cânone 29 — Logística Fotônica e Espectrometria Ubíqua Cosmológica

**Status:** contrato observacional público, seguro e falsificável  
**Versão:** 1.0.0  
**Data:** 2026-07-30  
**Função:** integrar espectroscopia, espectrometria, fotometria, polarimetria e visualização multi-faixa ao pipeline RLL sem promover interpretação autoral a mecanismo físico.

---

## 1. Invariante

\[
\boxed{
\text{céu físico}
\neq
\text{radiação emitida}
\neq
\text{radiação recebida}
\neq
\text{dado calibrado}
\neq
\text{imagem renderizada}
\neq
\text{interpretação}
}
\]

Uma visualização cosmológica é o fim de uma cadeia de transformação. Cores, contraste, composição RGB e suavização pertencem à renderização; não são automaticamente propriedades visíveis do objeto.

## 2. Cadeia logística fotônica

```text
emissor/processo
→ meio local da fonte
→ propagação cosmológica
→ absorção/espalhamento/lenteamento
→ abertura e óptica do instrumento
→ detector
→ calibração
→ reconstrução
→ fusão multi-faixa
→ visualização
→ interpretação
→ claim gate
```

Para uma fonte em redshift cosmológico, a observação pertence ao cone de luz passado. O objeto pode ter evoluído durante o tempo de viagem da radiação; o dado recebido registra radiação que chegou agora, associada a um estado anterior da fonte.

## 3. Objeto observacional mínimo

A unidade canônica é:

\[
\mathcal O =
\left(
\mathbf S,\,
\xi,\,
x,y,\,
t,\,
z,\,
R,\,
\sigma,\,
C,\,
M,\,
P
\right)
\]

onde:

- \(\mathbf S=(I,Q,U,V)\): vetor de Stokes quando polarimetria existir;
- \(\xi\): eixo espectral — comprimento de onda, frequência, energia ou canal;
- \(x,y\): coordenadas espaciais;
- \(t\): época e duração da observação;
- \(z\): redshift observado ou inferido, com método declarado;
- \(R\): resposta instrumental, incluindo bandpass, PSF e LSF quando aplicável;
- \(\sigma\): incerteza estatística;
- \(C\): covariância e sistemáticos;
- \(M\): máscara/qualidade;
- \(P\): proveniência, licença, versão, hash e transformação.

A ausência de qualquer campo necessário deve produzir `TOKEN_VAZIO`, não preenchimento inventado.

## 4. Faixas fotônicas

As fronteiras entre faixas são convencionais e aproximadas. O registro público em `data/observational/cosmological_photonic_bands.v1.json` é a fonte executável desta taxonomia.

| Faixa | Exemplos de observáveis | Processos/fontes típicos | Uso cosmológico/astrofísico |
|---|---|---|---|
| Rádio | contínuo, linhas, polarização, rotação de Faraday, timing | sincrotron, gás frio, elétrons em campos magnéticos, pulsares/FRBs | H I 21 cm, gás, magnetismo, estrutura em grande escala, transientes |
| Micro-ondas/submilimétrico | espectro térmico, anisotropia, polarização | CMB, poeira fria, efeito Sunyaev–Zeldovich, linhas moleculares | universo primordial, clusters, matéria bariônica e geometria |
| Infravermelho | SED, linhas moleculares/atômicas, contínuo térmico | poeira, estrelas frias, galáxias de alto redshift | formação estelar, galáxias antigas, linhas ópticas redshiftadas |
| Visível | absorção/emissão, redshift, cinemática, polarização | estrelas, nebulosas, galáxias, supernovas | distâncias, composição, velocidades, lentes, SNe Ia |
| Ultravioleta | linhas de alta ionização, absorção do meio intergaláctico | estrelas quentes, gás ionizado, remanescentes | reionização, Lyα, meio intergaláctico e formação estelar |
| Raios X | contínuo térmico/não térmico, linhas, timing, polarização | plasma quente, AGN, discos de acreção, clusters | massa de clusters, gás quente, metais, crescimento de estruturas |
| Raios gama | espectro não térmico, linhas, timing | GRBs, jatos, decaimentos/aniquilação, interações de raios cósmicos | universo extremo, transientes e restrições indiretas de física fundamental |

`laser` não é uma faixa do espectro eletromagnético. É uma fonte coerente e uma tecnologia que pode ser usada em calibração, metrologia, óptica adaptativa ou sensoriamento.

## 5. Modos de medição

A ubiquidade não é apenas cobrir sete faixas. Deve cobrir também os modos:

1. **fotometria:** fluxo integrado por bandpass;
2. **espectroscopia/espectrometria:** fluxo resolvido no eixo espectral;
3. **polarimetria:** \(I,Q,U,V\);
4. **espectropolarimetria:** espectro de polarização;
5. **imagem espectral/IFU:** \(I(x,y,\xi)\);
6. **série temporal:** \(I(\xi,t)\) ou eventos por energia/tempo;
7. **interferometria:** amplitude, fase e visibilidades;
8. **SED multi-instrumento:** segmentos espectrais com épocas, resoluções e calibrações distintas;
9. **tomografia:** reconstruções por redshift, velocidade ou linha de visada;
10. **multi-mensageiro:** fótons combinados com ondas gravitacionais, neutrinos ou raios cósmicos — registrados separadamente porque não são espectrometria fotônica.

## 6. Propagação e observador

A radiação recebida pode diferir da emitida por:

- redshift cosmológico e peculiar;
- extinção e avermelhamento;
- absorção e emissão intervenientes;
- espalhamento;
- lenteamento gravitacional;
- dispersão;
- rotação de Faraday;
- variabilidade da fonte;
- tempo de viagem;
- seleção e sensibilidade do instrumento.

Logo:

\[
F_{\rm det} =
\mathcal R_{\rm inst}
\circ
\mathcal T_{\rm prop}
\left[F_{\rm emit}\right]
+
N
\]

com \(\mathcal T_{\rm prop}\) representando propagação e \(\mathcal R_{\rm inst}\) a resposta instrumental.

## 7. Visualização cosmológica

Toda imagem pública derivada deve declarar:

```yaml
source_dataset:
spectral_bands:
observation_dates:
instrument:
calibration_version:
units:
psf_lsf:
reprojection:
background_subtraction:
normalization:
transfer_function:
clipping:
smoothing:
channel_mapping:
color_space:
uncertainty_or_quality_mask:
provenance:
```

Regras:

- RGB é uma codificação de exibição, não um espectro físico completo;
- CMYK/pigmento pertence à reprodução impressa, não à detecção;
- imagens de falsa cor são válidas quando a transformação é explícita;
- combinar faixas sem equalizar PSF, grade, unidades e épocas pode criar estruturas inexistentes;
- canais saturados, limites superiores e não detecções não podem ser tratados como medições comuns;
- a imagem renderizada nunca substitui o FITS/VOTable ou o dado calibrado de origem.

## 8. Setor escuro: fronteira pública

Este cânone não identifica matéria escura com uma região emissora nem energia escura com um destino da luz.

```yaml
DARK_MATTER:
  direct_electromagnetic_spectrum: NOT_ESTABLISHED
  usual_inference:
    - gravitational_lensing
    - stellar_and_gas_dynamics
    - galaxy_clusters
    - CMB_and_large_scale_structure

DARK_ENERGY:
  photon_destination_model: NOT_ESTABLISHED
  usual_inference:
    - expansion_history
    - type_Ia_supernovae
    - BAO
    - CMB
    - structure_growth

AUTHORIAL_SOURCE_RECEIVER_ANALOGY:
  state: PRIVATE_OR_HYPOTHESIS
  operational_definition: TOKEN_VAZIO
  public_physical_claim_allowed: false
```

A espectroscopia pode restringir modelos do setor escuro por traçadores bariônicos, redshifts, velocidades, distâncias, clusters e crescimento de estrutura. Isso é inferência indireta e deve permanecer separado de detecção direta.

## 9. Integração com o pipeline RLL

Este contrato estende o pipeline canônico:

```text
Estágio 0 — matemática estrutural
Estágio 1A — fonte, licença, unidades e observável
Estágio 1B — resposta instrumental e propagação
Estágio 1C — calibração, máscara, incerteza e covariância
Estágio 1D — compatibilização multi-faixa
Estágio 2 — inferência e posterior
Estágio 3 — adversários, controles e falsificadores
Estágio 4 — relatório, visualização, manifesto e hashes
```

Ele não altera a equação cosmológica RLL nem transforma uma visualização em evidência do modelo.

## 10. Gates de fusão multi-faixa

Uma fusão é publicável somente se:

\[
G =
G_{\rm provenance}
\land
G_{\rm units}
\land
G_{\rm calibration}
\land
G_{\rm PSF}
\land
G_{\rm epoch}
\land
G_{\rm uncertainty}
\land
G_{\rm license}
\]

Falha em qualquer gate produz `TOKEN_VAZIO` ou bloqueio explícito.

## 11. Risco de publicação

### Seguro para repositório público

- taxonomia das faixas e modos;
- contrato de metadados;
- exemplos sintéticos claramente marcados;
- referências oficiais;
- código de validação sem dados privados;
- resultados negativos e limitações.

### Exige triagem antes de publicação

- dados observacionais redistribuídos;
- imagens derivadas de terceiros;
- resultados numéricos ainda não reproduzidos;
- detalhes de hipótese autoral potencialmente sensíveis a estratégia de publicação;
- qualquer associação entre setor escuro e fonte/receptor;
- composições de cor sem receita de renderização.

### Proibido no público

- dados pessoais;
- exports de conversa;
- credenciais, tokens e caminhos privados;
- dataset sem licença;
- claim físico promovido apenas por analogia;
- imagem processada apresentada como dado bruto.

## 12. Falsificadores

A logística é rejeitada ou rebaixada quando:

- o resultado muda materialmente com uma escolha arbitrária de paleta;
- uma estrutura desaparece após equalização de PSF;
- a conclusão depende de épocas incompatíveis;
- a linha não sobrevive à resposta instrumental e ao contínuo;
- a significância desaparece com sistemáticos/covariância;
- a associação multi-faixa não resiste a catálogo nulo ou embaralhamento;
- o efeito é reproduzido por seleção, saturação, máscara ou fundo;
- o claim do setor escuro não produz previsão diferente de ΛCDM, w0waCDM ou controles astrofísicos.

## 13. Referências normativas e científicas

- NASA, *Multiwavelength Astronomy*: https://imagine.gsfc.nasa.gov/science/toolbox/multiwavelength1.html
- NASA/ESA/CSA, *Spectroscopic Observations of Different Wavelengths*: https://science.nasa.gov/asset/webb/spectroscopic-observations-of-different-wavelengths-of-light-in-astronomy/
- ESA, *What is spectroscopy?*: https://www.esa.int/ESA_Multimedia/Images/2025/11/What_is_spectroscopy
- NASA, *Hubble Spectroscopy*: https://science.nasa.gov/mission/hubble/science/science-behind-the-discoveries/hubble-spectroscopy/
- IVOA, *Spectrum Data Model 1.2*: https://www.ivoa.net/documents/SpectrumDM/
- IAU FITS Working Group/NASA, *FITS Standard*: https://fits.gsfc.nasa.gov/fits_standard.html
- FITS WCS: https://fits.gsfc.nasa.gov/fits_wcs.html

## R3

```yaml
F_ok:
  - cadeia emissor-propagação-instrumento-renderização separada
  - sete faixas fotônicas e dez modos de medição registrados
  - schema, registro e validador executável previstos
  - risco público e claim gate do setor escuro definidos
F_gap:
  - datasets reais selecionados
  - respostas instrumentais por missão
  - política de licenças por arquivo
  - calibração cruzada e covariâncias reais
F_next:
  - ingerir um dataset oficial pequeno por faixa
  - produzir manifests e receipts
  - executar comparação de visualização com e sem harmonização
claim_allowed: false
```

---

*O telescópio não entrega o cosmos diretamente; entrega uma cadeia mensurável de sinais, filtros, incertezas e escolhas. A ciência começa quando cada transformação deixa recibo.*
