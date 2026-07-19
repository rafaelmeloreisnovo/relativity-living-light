# Appendix C — Four opposed flow axes and axial/diagonal matrix ports

**Status:** `mathematical appendix | exact_geometry=PASS | physical_claims=TOKEN_VAZIO`  
**Author:** Rafael Melo Reis (∆RafaelVerboΩ)  
**Canonical context:** *From the Observed Void to Recurrence*

## C.1 Scope

This appendix formalizes a refinement of the torus-meridian construction. Instead of treating the upper and lower points as the only distinguished positions, the model introduces **four opposed axes through one common center**:

1. vertical;
2. horizontal;
3. rising diagonal;
4. falling diagonal.

Each axis has two opposite mouths. The construction therefore contains eight ports:

\[
4\text{ axes}\times 2\text{ mouths}=8\text{ ports}.
\]

The term *port* denotes a geometric/computational gate. It does not by itself denote a physical nozzle, jet or vortex core.

## C.2 Meridian center and port positions

Let the meridian circle of the ring torus have center

\[
C=(R,0)
\]

and minor radius `r>0`. For an angle `theta`, define

\[
P(\theta)=C+r(\cos\theta,\sin\theta).
\]

| Port | Axis | Angle |
|---|---|---:|
| upper | vertical | `90°` |
| lower | vertical | `270°` |
| right | horizontal | `0°` |
| left | horizontal | `180°` |
| upper-right | rising diagonal | `45°` |
| lower-left | rising diagonal | `225°` |
| upper-left | falling diagonal | `135°` |
| lower-right | falling diagonal | `315°` |

The four axes are diameters, not isolated rays.

## C.3 Opposed-pair invariants

For every axis with opposed ports `P+` and `P-`,

\[
\frac{P_++P_-}{2}=C
\]

and

\[
\|P_+-P_-\|=2r.
\]

Thus all four channels share the same center and the same diameter.

## C.4 Axial and diagonal matrix projection

The corresponding matrix directions are

\[
\mathcal N_8=\{(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)\}.
\]

The axial directions already have unit Euclidean length. The diagonal steps require normalization:

\[
\widehat d_{\mathrm{diag}}=\frac1{\sqrt2}(\pm1,\pm1).
\]

Therefore the diagonal projection has the same unit radial length as the upper, lower and lateral projections.

This is a declared computational convention linking an eight-neighbor matrix stencil to the meridian geometry.

## C.5 Radial and tangential bases

At `P(theta)`, define the outward radial unit vector

\[
\widehat n(\theta)=(\cos\theta,\sin\theta)
\]

and the counterclockwise tangent

\[
\widehat t(\theta)=(-\sin\theta,\cos\theta).
\]

Then

\[
\widehat n\cdot\widehat t=0.
\]

The tangent aperture line is

\[
\widehat n(\theta)\cdot X=\widehat n(\theta)\cdot P(\theta).
\]

Its perpendicular distance from `C` is exactly `r`, so it is tangent to the meridian circle at one point.

This vector form is preferred to slope-only formulas because the left and right mouths have vertical tangent lines, for which a finite slope is undefined.

## C.6 Relation to the quadratic/Bhaskara layer

For nonvertical tangent candidates written as

\[
z=m\rho+b,
\]

substitution into

\[
(\rho-R)^2+z^2=r^2
\]

produces a quadratic equation. Tangency is identified by

\[
\Delta=0.
\]

The vector aperture equation generalizes this construction to all eight ports, including vertical tangents. The earlier `30°` tangent family and the present `45°` diagonal family are different constraints:

- `30°` belongs to the triangle/tangent construction;
- `45°` belongs to the square-diagonal/matrix projection.

Their coexistence does not imply identity.

## C.7 Toroidal sweep

Interpreting a port as meridian coordinates

\[
P=(\rho_P,z_P),
\]

its sweep around the toroidal angle `u` is

\[
X_P(u)=(\rho_P\cos u,\rho_P\sin u,z_P).
\]

Each meridian port therefore generates one ring. The four axes generate eight projected rings.

For each swept point,

\[
\sqrt{\left(\sqrt{x^2+y^2}-R\right)^2+z^2}=r.
\]

Thus the sweep preserves the meridian-circle radius exactly.

## C.8 Computational interpretation

The construction supports:

- an axial/diagonal eight-neighbor stencil;
- paired inlet/outlet labels;
- radial and tangential feature vectors;
- symmetric routing through a common center;
- four opposed channel identifiers;
- eight toroidal ring projections;
- deterministic masks and relation kernels.

The construction does not choose a direction of actual transport. Inward and outward vectors are both recorded so a later model may define source, sink, pulse or alternating phase without rewriting the geometry.

## C.9 Physical boundary

The exact geometry does not establish a physical Venturi or vortex mechanism. Such a model requires at least:

- aperture area and shape;
- pressure field;
- density;
- viscosity;
- flow rate;
- circulation or vorticity;
- governing equations;
- initial and boundary conditions;
- dimensional units;
- numerical or experimental data;
- uncertainty and falsifiers.

Therefore:

```text
exact_geometry_state = PASS
physical_claims_state = TOKEN_VAZIO
claim_allowed = false
```

## C.10 Reproduction

Run:

```bash
python3 PapersPub/08_multiscale_validation_methods/scripts/validate_four_axis_flow_ports.py
```

Expected:

```text
12/12 checks PASS
4 axes
8 ports
exact_geometry_state = PASS
physical_claims_state = TOKEN_VAZIO
```

## C.11 Canonical invariant

\[
\boxed{
\text{one center}+\text{vertical}+\text{horizontal}+\text{two diagonals}
=\text{four opposed axes}
=\text{eight projected ports}
}
\]

The result extends the matrix projection page without converting geometric symmetry into an unsupported physical claim.
