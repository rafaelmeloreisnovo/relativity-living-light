# RADIATION TRANSMISSION VALIDATION (RLL/MCRP)

Status: **Parcial real em preparação**.

## Objetivo
Validar a decomposição \(\Phi_{\mathrm{eff}}=\Phi_{\mathrm{ext}}\cdot T_M\) com dados heliosféricos, cósmicos e orbitais.

## Fontes de dados
- OMNI (solar wind + IMF).
- NMDB (raios cósmicos).
- GOES energetic particles.
- SPENVIS AE9/AP9 (modelagem de ambiente em LEO).

## Pipeline operacional
1. Obter OMNI (IMF, Bz, vento solar, densidade, pressão dinâmica, Kp, Dst, AE, F10.7, prótons).
2. Obter NMDB (contagens, GLE, Forbush).
3. Obter GOES energetic particles (prótons/elétrons por energia).
4. Rodar ou documentar execução SPENVIS AE9/AP9 para órbitas LEO-alvo.
5. Estimar \(\Phi_{\mathrm{ext}}(E,t,\Omega)\) com forçamento heliosférico/cósmico.
6. Estimar \(T_M(E,\Omega;M(t),m(t),SW)\) regional com camada geomagnética.
7. Derivar \(\Phi_{\mathrm{eff}}\) por energia e janela temporal.
8. Comparar com eventos de satélite públicos (quando disponíveis).

## Métricas sugeridas
- RMS espectral e temporal por canal de energia.
- Skill score de eventos (picos, quedas e eventos extremos).
- Defasagem ótima entre forçamento heliosférico e resposta efetiva.
- IC por bootstrap e análise de sensibilidade.

## Critérios de interpretação
- Não reivindicar validação final sem cadeia de processamento reprodutível.
- Não reduzir o problema a um único índice (ex.: só Kp ou só Dst).
- Distinguir claramente: hipótese física, dado bruto, transformação de modelo, métrica observável.
- Registrar cadeia de custódia em `data/real/heliophysics/README.md`.
