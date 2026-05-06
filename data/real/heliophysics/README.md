# data/real/heliophysics

Status: **Parcial real em preparação**.

## Escopo
Repositório de custódia para dados de forçamento heliosférico, raios cósmicos e partículas energéticas.

## Fontes previstas
- OMNI (NASA/SPDF).
- GOES energetic particles.
- NMDB neutron monitor database.

## Registro obrigatório por fonte
- Fonte e versão do produto;
- URL/endpoint e política de licença;
- Variáveis usadas;
- Resolução temporal (ex.: 1 min, 1 h, diário);
- Janela temporal coberta;
- Data de acesso (UTC);
- Hash SHA-256 dos arquivos brutos;
- Método de download e script de processamento;
- Limitações conhecidas (lacunas, mudanças instrumentais, cobertura, flags de qualidade).

## Variáveis de referência
- OMNI: IMF, Bz, velocidade do vento solar, densidade, pressão dinâmica, Kp, Dst, AE, F10.7, fluxo de prótons.
- GOES: prótons e elétrons por canal de energia.
- NMDB: contagens por monitor, GLE, assinaturas de Forbush.

## Limitações esperadas
- Heterogeneidade de calibração entre instrumentos e épocas.
- Lacunas temporais e mudanças de versão de produto.
- Necessidade de alinhamento temporal para comparação com \(\Phi_{ext}\), \(T_M\) e \(\Phi_{eff}\).
