# RLL — Triângulos × Coroas Circulares × Toro × Malhas Angulares 840 — Bridge V1

**Data:** 2026-09-22  
**Estado:** \`FORMAL_GEOMETRY_BRIDGE / CLAIM_BOUNDARY_ACTIVE\`  
**Autor/proponente:** RAFAEL MELO REIS  
**Integração:** RLL governado  
**claim_allowed:** \`false\` para mecanismo físico, vórtice, cosmologia ou equivalência esfera↔toro.

## 0. Proveniência

Esta integração cruza a sessão atual com autoridades já existentes:

- RLL: \`docs/invariants/sqrt3_2_kernel.md\` — blob \`76d075edfc84886d95db5d6d9d897ef4457f0512\`;
- Matemática: \`PITAGORAS_BHASKARA_ISOSCELES_POINCARE_CROSSWALK_V1.md\` — blob \`d89ecf1ac8964d1d778e3c35289f629bacab8564\`;
- Matemática: \`CROWN_15_30_45_PI12_PI5_GEODESIC_REFLECTION_CROSSWALK_V1.md\` — blob \`0db1e191481a425f0f3c3f07a3f010a5a613245d\`;
- Matemática: \`2026-08-18_omega7_modular_geodesic_toroidal_focus.md\` — blob \`8dd0f19a10fff0b1edba7a7ca3d1c297bfc9e62e\`;
- Papers: \`crown_geodesic_reflection_geometry_v1/paper.md\` — blob \`2dc8b992073c786c253545e620960b1810232eff\`;
- Papers: \`poincare_torus_mobile_v1/paper.md\` — blob \`8d9144e922c45d599e90d90470c21201d208ea5f\`;
- Papers: \`radial_partition_5_6_7_8_geometry_v1/paper.md\` — formalização corrente do grid 5–6–7–8.

Regra:
\[
\text{IDENTIDADE EXATA}\neq
\text{MODELO GEOMÉTRICO}\neq
\text{CODIFICAÇÃO MODULAR}\neq
\text{MECANISMO FÍSICO}.
\]

## 1. Kernel equilátero

\[
h=\frac{\sqrt3}{2},\qquad h^2=\frac34.
\]

Na seção circular do tubo toroidal, para \(v=30^\circ\):

\[
r\cos v=\frac{\sqrt3}{2}r,\qquad
r\sin v=\frac12r.
\]

Portanto o mesmo kernel trigonométrico do meio-triângulo equilátero parametriza uma posição da seção circular do toro.

Isso é reutilização de identidade trigonométrica, não identidade ontológica entre triângulo e toro.

## 2. Toro padrão

\[
T(u,v)=
((R+r\cos v)\cos u,\,
(R+r\cos v)\sin u,\,
r\sin v),
\quad R>r>0.
\]

Há dois ciclos independentes:

\[
u\in S^1,\qquad v\in S^1.
\]

O ciclo \(u\) percorre o círculo maior; \(v\) percorre a seção circular do tubo.

### Seis posições equiláteras no ciclo menor

\[
v_k=\frac{k\pi}{3},\qquad k=0,\ldots,5.
\]

As coordenadas meridianas são:

\[
(\rho_k,z_k)=
(R+r\cos v_k,\;r\sin v_k).
\]

Elas formam um hexágono regular na seção circular local do tubo.

Ao deixar \(u\) variar em \([0,2\pi)\) com \(v=v_k\) fixo, cada vértice gera um círculo toroidal. Assim:

\[
\text{hexágono da seção}
\longrightarrow
6\text{ círculos toroidais}.
\]

## 3. Projeção ortográfica do toro no plano xy

A coordenada radial projetada satisfaz:

\[
R-r\le \rho\le R+r.
\]

Logo a projeção é a coroa:

\[
\mathcal A_T=
\{(\rho,\theta):R-r\le \rho\le R+r\}.
\]

Sua área:

\[
A_{\rm crown}
=
\pi[(R+r)^2-(R-r)^2]
=
\boxed{4\pi Rr}.
\]

A área da superfície do toro padrão é:

\[
A_T=4\pi^2Rr.
\]

Portanto:

\[
\boxed{A_T=\pi A_{\rm crown}}.
\]

Isto é uma relação métrica exata para o toro padrão e sua projeção ortográfica equatorial.

## 4. Coroa produzida pelo giro de um polígono regular

Para um \(n\)-gono regular de circunraio \(a\), seu inraio é:

\[
a_n=a\cos\frac{\pi}{n}.
\]

A união de todas as bordas rotacionadas preenche a coroa:

\[
a\cos\frac{\pi}{n}\le \rho\le a.
\]

A fração da área do disco externo ocupada por essa coroa é:

\[
\boxed{
\frac{A_{\rm ann,n}}{\pi a^2}
=
\sin^2\frac{\pi}{n}
}.
\]

Casos:

\[
n=3\Rightarrow\frac34,
\quad
n=4\Rightarrow\frac12,
\quad
n=6\Rightarrow\frac14,
\quad
n=8\Rightarrow\frac{2-\sqrt2}{4}.
\]

## 5. Coroa planar → casca toroidal

Revolvendo essa coroa em torno de um eixo externo a distância \(R>a\), Pappus fornece:

\[
V_{\rm shell,n}=2\pi R\,A_{\rm ann,n}.
\]

O toro sólido de tubo circular de raio \(a\) possui:

\[
V_T=2\pi^2Ra^2.
\]

Logo:

\[
\boxed{
\frac{V_{\rm shell,n}}{V_T}
=
\sin^2\frac{\pi}{n}
}.
\]

A fração de área da coroa planar é preservada como fração volumétrica da casca toroidal porque ambas as regiões de seção têm centroide no mesmo centro de revolução.

## 6. Seis triângulos → seção hexagonal → aproximação toroidal

Um hexágono regular inscrito em círculo de raio \(r\) contém seis equiláteros e possui:

\[
A_6=\frac{3\sqrt3}{2}r^2.
\]

Revolvido em torno de eixo externo a distância \(R\):

\[
V_6=2\pi R A_6
=
3\sqrt3\,\pi Rr^2.
\]

Comparando ao toro circular:

\[
V_T=2\pi^2Rr^2,
\]

temos:

\[
\boxed{
\frac{V_6}{V_T}
=
\frac{3\sqrt3}{2\pi}
\approx0.8269933431
}.
\]

Generalização para seção \(n\)-gonal inscrita:

\[
\boxed{
\frac{V_n}{V_T}
=
\frac{n\sin(2\pi/n)}{2\pi}
}
\]

e:

\[
\lim_{n\to\infty}\frac{V_n}{V_T}=1.
\]

## 7. Tangentes paralelas da seção meridiana

Seção:

\[
(\rho-R)^2+z^2=r^2.
\]

Reta:

\[
z=m\rho+b.
\]

Para uma família de inclinação \(m\), as duas tangentes são:

\[
b_\pm=-mR\pm r\sqrt{1+m^2}.
\]

A distância perpendicular entre elas é:

\[
\boxed{d_\parallel=2r}.
\]

Para:

\[
m=\pm\tan30^\circ=\pm\frac1{\sqrt3},
\]

obtêm-se as famílias espelhadas já presentes no corpus PBIP/coroa/toro.

## 8. Seis setores iguais no plano → três pares volumétricos iguais no toro

Considere uma casca de seção anular local:

\[
r_i\le s\le r_o
\]

e um setor angular de abertura \(\alpha\), centrado em \(v_0\). Ao revolvê-lo no toro:

\[
\boxed{
V(v_0,\alpha)=
\pi R\alpha(r_o^2-r_i^2)
+
\frac{4\pi}{3}(r_o^3-r_i^3)
\cos v_0\sin\frac{\alpha}{2}
}.
\]

Para seis setores:

\[
\alpha=\frac{\pi}{3}.
\]

Eles têm áreas planares iguais, mas os volumes toroidais são diferentes por causa do fator \(R+s\cos v\).

Para setores opostos:

\[
v_0\leftrightarrow v_0+\pi,
\]

os termos em \(\cos v_0\) cancelam. Portanto:

\[
\boxed{
V(v_0)+V(v_0+\pi)
=
\frac13 V_{\rm shell,total}
}.
\]

Assim:

\[
6\text{ setores iguais no plano}
\not\Rightarrow
6\text{ volumes iguais no toro},
\]

mas:

\[
\boxed{
3\text{ pares opostos}
\Rightarrow
3\text{ volumes iguais}.
}
\]

## 9. Relógios 30° × 45° no toro

O predecessor toroidal discreto usa:

\[
\Delta u=30^\circ,\qquad
\Delta v=45^\circ.
\]

Os ciclos possuem 12 e 8 estados:

\[
\boxed{\operatorname{lcm}(12,8)=24}.
\]

A família equilátera de \(60^\circ\) aparece como subgrade:

\[
Z_6\hookrightarrow Z_{12}.
\]

A família quadrado/octogonal fornece o passo de \(45^\circ\).

## 10. Grid 5–6–7–8

\[
\boxed{\operatorname{lcm}(5,6,7,8)=840}.
\]

Microângulo:

\[
\delta\theta=\frac{360^\circ}{840}
=\frac37^\circ
=\frac{\pi}{420}.
\]

Pesos dos setores:

\[
168,\quad140,\quad120,\quad105.
\]

Sob fase comum:

\[
\boxed{26\text{ raios nominais}\to22\text{ direções distintas}}.
\]

Após identificação antipodal:

\[
\boxed{16\text{ orientações de retas completas}}.
\]

Materializando as retas completas concorrentes:

\[
\boxed{16\text{ retas}\to32\text{ semirretas/setores}}.
\]

## 11. Segundo 840 já existente no corpus

O carrier modular documentado:

\[
\mathbb Z_{24}\times
\mathbb Z_{10}\times
\mathbb Z_{42}
\]

possui período síncrono:

\[
\boxed{
\operatorname{lcm}(24,10,42)=840
}.
\]

Portanto os dois objetos compartilham ordem cíclica 840:

\[
\mathbb Z_{840}
\cong
\langle(1,1,1)\rangle
\subset
\mathbb Z_{24}\times\mathbb Z_{10}\times\mathbb Z_{42}.
\]

Mas:

\[
\boxed{
\text{840 angular}\neq
\text{840 modular sem mapa semântico declarado}.
}
\]

Um isomorfismo abstrato de grupos cíclicos não fornece automaticamente identidade de significado.

## 12. Fronteira esfera ↔ toro

\[
\chi(S^2)=2,
\qquad
\chi(T^2)=0.
\]

Logo não existe homeomorfismo global:

\[
S^2\not\cong T^2.
\]

Pontes permitidas precisam declarar uma operação como:

\[
\text{SEAM},
\text{CUT},
\text{QUOTIENT},
\text{LOCAL\_CHART},
\text{PROJECTION}
\]

e metadados de distorção.

## 13. Gates

- G01: \(h^2=3/4\).
- G02: seção toroidal em \(30^\circ\) recupera \((\sqrt3/2,1/2)\).
- G03: projeção \(xy\) do toro padrão é coroa \(R-r\le\rho\le R+r\).
- G04: \(A_T/A_{\rm crown}=\pi\).
- G05: coroa de giro poligonal tem fração \(\sin^2(\pi/n)\).
- G06: casca toroidal correspondente preserva a mesma fração.
- G07: seção hexagonal dá \(V_6/V_T=3\sqrt3/(2\pi)\).
- G08: tangentes paralelas de uma família estão separadas por \(2r\).
- G09: três pares opostos dos seis setores têm um terço do volume cada.
- G10: relógios \(30^\circ\times45^\circ\) fecham em 24.
- G11: \(\operatorname{lcm}(5,6,7,8)=840\).
- G12: união radial 5–6–7–8 tem 22 direções sob fase comum.
- G13: identificação antipodal produz 16 orientações de reta.
- G14: 16 retas concorrentes produzem 32 semirretas/setores.
- G15: \(\operatorname{lcm}(24,10,42)=840\).

## 14. Claim boundary

\`\`\`text
TRIANGLE_KERNEL != TORUS
PLANAR_ANNULUS != TORUS_SURFACE
SAME_VOLUME_FRACTION != SAME_OBJECT
PLANAR_HEXAGRAM != SPHERICAL_GEODESIC_HEXAGRAM
SPHERE != TORUS
840_ANGULAR != 840_MODULAR_SEMANTICALLY
FORMAL_TORUS_GEOMETRY != PHYSICAL_VORTEX
\`\`\`

## 15. R3

**F_ok**
- ponte triângulo/equilátero ↔ seção circular toroidal tipada;
- coroa projetada do toro e relação \(A_T=\pi A_{\rm crown}\);
- operador polígono→coroa→casca toroidal;
- aproximação hexagonal do toro;
- tangentes paralelas e distância \(2r\);
- seis setores → três pares volumétricos iguais;
- 30°×45° → período 24;
- dois fechamentos 840 separados por semântica.

**F_gap**
- mapa semântico canônico entre os dois 840;
- mapa hexagrama plano→geodésica esférica;
- qualquer modelo físico de vórtice;
- ponte global esfera↔toro é bloqueada por topologia;
- dados físicos não foram introduzidos.

**F_next**
1. integrar o verificador determinístico;
2. adicionar sweep \(u\times v\) dos seis pontos/triângulos;
3. calcular interseções das famílias tangentes/cordas;
4. testar órbitas 30°/45°/60°/72°;
5. somente depois avaliar pontes físicas com variáveis, unidades e dados.
