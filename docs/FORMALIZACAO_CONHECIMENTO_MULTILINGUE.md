# Sistema Geométrico Unificado + Execução Reprodutível

Este documento substitui a versão anterior e entrega o que faltava: **formalização geométrica única** + **script executável** + **workflow YAML** sem entrega manual de binários.

## Núcleo formal

- Intervalo: \(\Delta = R-r\)
- Escala radial: \(\lambda=R/r\)
- Invariante: \(I=R^2-r^2\)

Geradores:
- Extrusão: \(\mathcal{E}(S,h)=S\times[0,h]\)
- Rotação: \(\mathcal{R}(S)\)
- Empilhamento discreto: \(\mathcal{S}_n=\sum_{k=0}^{n}S_k\)

Unificação:
\[
\text{Forma} = \{\mathcal{R},\mathcal{E},\mathcal{S}\}\circ\{T,Q,C\}
\]

## Objetos cobertos

\(\{\)triângulo equilátero, quadrado, círculo, cubo, esfera, tetraedro, bipirâmide, toro\(\}\).

## Entregáveis técnicos

1. `scripts/unified_geometry_system.py`
   - Gera métricas fechadas (área/volume) das formas.
   - Preserva \(\Delta,\lambda,I\) como núcleo do toro.
   - Exporta apenas texto estruturado (`CSV` e `JSON`).

2. `.github/workflows/unified-geometry.yml`
   - Executa o script automaticamente.
   - Publica artefatos textuais por GitHub Actions.

## Política de artefatos

- Sem entrega manual de binários neste fluxo.
- Repositório mantém código + YAML + artefatos textuais.
- Outputs para consumo ficam como artifacts da pipeline.
