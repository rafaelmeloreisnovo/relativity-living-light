# Frentes práticas: CLASS/CAMB vs extrator observacional em ln(1+z)

## Escopo
Comparação operacional das duas frentes para a fase atual do DHA, considerando custo, risco e ganho de evidência empírica.

## Frente A — Injeção no CLASS/CAMB
- **Entrega:** modificação das equações de evolução/transferência para incluir termo oscilatório DHA.
- **Vantagem:** conecta o modelo à cadeia cosmológica padrão de alto rigor teórico.
- **Risco atual:** maior custo de implementação e validação, com latência maior para primeiro resultado falsificável.

## Frente B — Extrator observacional em ln(1+z)
- **Entrega:** pipeline de ajuste de resíduo log-periódico em catálogos LSS.
- **Vantagem:** produz sinal mensurável rapidamente e permite testar consistência de \(\omega\) com dados.
- **Risco atual:** depende de controle de sistemáticos e qualidade dos catálogos usados.

## Sequência sugerida de execução
1. **Executar primeiro a Frente B** para obter detecção/limite empírico inicial de \(A_0\) e \(\omega\).
2. Usar esse resultado para **informar priors** da implementação em CLASS/CAMB (Frente A).
3. Fechar ciclo com comparação cruzada entre previsão de transferência e resíduo observado.

## Critérios de sucesso mínimos
- \(|\omega_{fit} - \omega_{teoria}|\) dentro da incerteza 1–2\(\sigma\).
- \(\Delta\)BIC favorável ao termo DHA ou limites superiores robustos para \(A_0\).
- Reprodutibilidade por workflow CI e artefatos versionados.
