# Claim-state ledger — Four-axis flow ports

| ID | Statement | Class | State | Evidence/Falsifier |
|---|---|---|---|---|
| `FLOW-E-001` | Four opposed axes produce eight distinct meridian ports. | `[E]` | `PASS` | Direct enumeration: `4×2=8`. |
| `FLOW-E-002` | Every opposed pair has midpoint `C` and length `2r`. | `[E]` | `PASS` | Coordinate substitution. |
| `FLOW-E-003` | Every port lies on the meridian circle. | `[E]` | `PASS` | `||P-C||=r`. |
| `FLOW-E-004` | The aperture tangent is perpendicular to the radial normal. | `[E]` | `PASS` | `n·t=0`. |
| `FLOW-E-005` | The tangent-line distance from the center equals `r`. | `[E]` | `PASS` | Point-line distance. |
| `FLOW-E-006` | The eight directions cover axial and square-diagonal neighbors. | `[E/C]` | `PASS/REFERENCE` | Declared stencil and exact set comparison. |
| `FLOW-E-007` | Unit diagonal directions have components `±1/sqrt(2)`. | `[E]` | `PASS` | Euclidean normalization. |
| `FLOW-E-008` | Sweeping each port around `u` preserves the meridian radius. | `[E]` | `PASS` | Substitution in the torus meridian equation. |
| `FLOW-C-009` | Ports function as matrix gates or channel labels. | `[C]` | `REFERENCE` | Computational convention, not a natural-law claim. |
| `FLOW-H-010` | The ports generate a physical Venturi effect. | `[H]` | `TOKEN_VAZIO` | Requires aperture area, pressure, density, viscosity, flow and boundary data. |
| `FLOW-H-011` | The ports generate a physical vortex. | `[H]` | `TOKEN_VAZIO` | Requires velocity field, circulation/vorticity, units and measurements. |
| `FLOW-H-012` | Eight geometric ports imply eight physical jets. | `[H]` | `PROHIBITED_BY_SCOPE` | Geometry alone cannot determine a physical flow topology. |

```text
exact_geometry_state = PASS
physical_claims_state = TOKEN_VAZIO
claim_allowed = false
```
