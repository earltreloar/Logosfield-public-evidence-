# Master Archive Index — V3 Canonical
# Logosfield / ODCCT Framework
# Supersedes: Master_Archive_Index_2026_05_29_V2.md (retained for historical reference)

---

## FRAMEWORK IDENTITY

Name: Logosfield / ODCCT Framework
Version: V3 Canonical
Repository: https://github.com/earltreloar/Logosfield-public-evidence-
Status: Level 2 — internally consistent, recovers known physics in conservative limit, not independently replicated.

---

## WHAT CHANGED FROM V2

1. **Linear EFT completion removed.** `Z(Phi)=1+c_g*Phi/M_Pl`, `Y(Phi)=1+c_y*Phi/M_Pl` conflicted with precision measurements by ~8 orders of magnitude. Replaced by a derived, conformally-protected completion: `f=g=h=1+O(gamma)*(Phi/M_Pl)^2`.
2. **CDDR and Mechanism 16 (sigma8) suspended.** Both depended on the removed linear completion. They require `Phi_ref != 0`, which is not derivable from the now-derived scalar potential `V(Phi)` alone (its minimum is at `Phi=0`). This is Gap 8, open.
3. **Parameters updated.** `gamma` moved from the August-2025 working value of `0.005` to `~0.003122`, identified via a baryogenesis-line + Matsubara-frequency argument and verified to preserve every closed result's margin under a full recalculation pass.
4. **Auxiliary field derivation of the kernel (Gap 10).** The memory kernel is no longer a bare postulate — it is derived from integrating out an auxiliary field `chi`. `gamma -> 0` is now a controlled decoupling limit.
5. **Force Coupling Table strong-sector entry corrected.** Previously mislabeled DERIVED; corrected to IDENTIFIED (sign of running, from asymptotic freedom) + OPEN (magnitude at the confinement scale).
6. **Scalar potential `V(Phi)` derived** from conformal weight counting + a Z_2 symmetry identified in the memory kernel's bilinear structure.
7. **Gap 7 (Horndeski mapping)** carried forward unchanged from V2 — still closed, `c_T=c` exactly.

---

## CURRENT PARAMETERS

| Parameter | Value | Status |
|---|---|---|
| `alpha` | 1 | Postulated |
| `beta` | `2*pi` | IDENTIFIED (Matsubara lead) |
| `gamma` | `0.003122` | IDENTIFIED (baryogenesis line + Matsubara) |

See `THEORY.md` Section 4 for the full derivation-attempt history, including every ruled-out path (naive-equipartition error, joint loop-factor closure, strong-CP kernel-topology route, c_W self-consistency route).

---

## GAP STATUS SUMMARY

| Gap | Subject | Status |
|---|---|---|
| 3 | Cassini / alpha variation | CLOSED — 50+ orders margin |
| 4 | First-principles gamma | OPEN — see derivation-attempt history |
| 7 | Horndeski mapping / GW speed | CLOSED |
| 8 | Phi_ref | OPEN — not blocking closed gaps; blocks suspended predictions |
| 9 | First-principles beta | Dissolves into Gap 4 |
| 10 | Auxiliary field / causal kernel | Substantially addressed |
| 11 | Conformal protection (above EW) | Substantially closed |
| 12 | Baryogenesis / Weinberg operator | Substantially closed |
| 13 | Below-EW continuity | Substantially resolved |
| — | gamma_strong magnitude | OPEN |

---

## SUSPENDED PREDICTIONS

- CDDR (Etherington distance-duality)
- Mechanism 16 sigma8 response
- Galaxy rotation mechanism

All three require Gap 8 resolution before they can be meaningfully rederived and tested.

---

## NAVIGATION

- `THEORY.md` — full technical detail and derivation history (start here)
- `README.md` — project overview
- `CHALLENGE.md` — current active replication targets
- `REPRODUCE.md` — reproduction instructions and status table
- `CITATIONS.md` — citation guidance
- `EFT_couplings.md`, `Cosmology.md`, `ZPhi_Summary.md` — sector-specific detail
- `Master_Archive_Index_2026_05_29_V2.md` — prior version, retained for historical reference
