# GEOMAGNETIC VALIDATION PIPELINE (RLL/MCRP)

Status: **Parcial real em preparação**.

## Objetivo
Validar a camada geomagnética do RLL/MCRP sem extrapolar conclusão além dos dados observacionais disponíveis, focando AMAS/SAA como caso local.

## Entradas
- IGRF14.
- WMM2025.
- ESA Swarm (2014–2025).

## Saídas
- Diretório alvo: `results/geomagnetic/`.
- Mapas e séries temporais de `F, X, Y, Z` para região AMAS.
- Métricas de deriva, área e erro.

## Pipeline operacional
1. Baixar IGRF14/WMM2025/Swarm com registro de versão e hash.
2. Harmonizar grades, época e convenções de coordenadas.
3. Calcular mapas `F, X, Y, Z` para recorte AMAS.
4. Reconstruir evolução temporal 2014–2025.
5. Medir área sob limiar de intensidade (nT).
6. Estimar deslocamento do mínimo (lat/lon e km/ano).
7. Comparar com produtos ESA/Swarm e literatura associada.
8. Salvar artefatos e metadados em `results/geomagnetic/`.

## Métricas obrigatórias
- RMS error entre reconstrução e referência observacional.
- Drift do mínimo da anomalia (km/ano).
- Variação secular local (nT/ano).
- Área sob limiar de intensidade (km² ou área normalizada).
- Intervalo de confiança (bootstrap/janela temporal/modelo).

## Contratos de qualidade
- Separar hipótese, dado, modelo, métrica em cada relatório.
- Não inferir “prova” do RLL pela AMAS isoladamente.
- Não marcar como validação real completa sem execução reproduzível dos downloads e processamento.
- Preservar cadeia de custódia em `data/real/geomagnetic/README.md`.
