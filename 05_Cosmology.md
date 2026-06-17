# Cosmology — V3 Canonical
# Logosfield / ODCCT Framework

---

## Status: SUSPENDED pending Gap 8 (Phi_ref)

The CDDR (Etherington distance-duality) and Mechanism 16 (sigma8 response) predictions in this file are **suspended**. They were previously computed (V2) using a linear EFT completion (`Z(Phi) = 1 + c_g*Phi/M_Pl`, `Y(Phi) = 1 + c_y*Phi/M_Pl`) that has since been removed after an audit found an eight-order-of-magnitude conflict with precision measurements (see `04_EFT_couplings.md` and `00_THEORY.md` Section 6).

The replacement, conformally-protected coupling form is:

```
f(Phi/M_Pl) = g(Phi/M_Pl) = h(Phi/M_Pl) = 1 + O(gamma) * (Phi/M_Pl)^2
```

This is quadratic in `Phi/M_Pl`, not linear, and reduces to exactly 1 at `Phi = 0`. The scalar potential has been derived:

```
V(Phi) = (1/2)*gamma*beta^2*Phi^2 + (gamma^2/16*pi^2)*Phi^4
```

Its classical minimum is at `Phi = 0` — meaning that without an external cosmological input (an initial condition setting `Phi_ref != 0`, not derivable from `V(Phi)` alone), the corrected couplings give **no observable deviation from GR/SM** in the cosmological sector. This is Gap 8, and it remains open.

**The formulas below are retained for historical/reproducibility reference only.** They do not currently represent an active prediction of the framework.

---

## CDDR (Etherington Distance Duality) — historical V2 formula, SUPERSEDED

```
eta(z) = D_L / [(1+z)^2 D_A]
```

V2 formula (depended on the now-removed linear EFT completion):

```
eta(z=0.5) - 1 = -0.0569 * epsilon_g + 0.2384 * epsilon_y
```

where `epsilon_g = c_g * Phi_ref/M_Pl`, `epsilon_y = c_y * Phi_ref/M_Pl`. Since `c_g`, `c_y` no longer exist as independent coefficients under the V3 conformal-protection completion, **this formula does not apply as written** and should not be used for new predictions. A V3-consistent CDDR prediction would need to be rederived using the quadratic coupling form and an independently-justified `Phi_ref`, neither of which is currently available.

## Mechanism 16 — sigma8 response — historical V2 formula, SUPERSEDED

Same status as CDDR above: the V2 sigma8 suppression formula depended on the linear `Y(Phi)` coupling and does not carry over to the V3 quadratic form without rederivation.

---

## What is NOT suspended

The structural results that do not depend on `Phi_ref` are unaffected by the above:

- Force Coupling Table (EM, gravity, weak sector couplings) — see `00_THEORY.md` Section 5
- Gap 3 (Cassini / alpha variation) — depends on the kernel parameters directly, not on `Phi_ref`
- Gap 7 (Horndeski / GW speed) — a symmetry statement, independent of `Phi`'s value
- Gap 12 (baryogenesis / c_W) — depends on `T* = gamma/beta`, not on `Phi_ref`

See `00_THEORY.md` for the full, current technical summary.
