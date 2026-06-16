# ZPhi Summary — V3 Canonical
# Logosfield / ODCCT Framework

This file is a compact technical summary. For full derivations and gap-by-gap status, see `THEORY.md`.

---

## 1. Memory-Covariant Derivative

```
D_mem,mu psi(x) = integral_{M^-(x)} K(x,x'; beta,gamma) * U(x,x') * D_mu' psi(x') sqrt(-g') d^4x'
K(x,x'; beta,gamma) = gamma*beta * exp(-beta*(t-t')) * Theta(t-t')
```

- `M^-(x)`: causal past of x
- `U(x,x')`: parallel transport / Wilson line operator
- Conservative limit: `gamma -> 0` recovers `D_mu` exactly.

The kernel is derived, not postulated, from integrating out an auxiliary field `chi` satisfying `(d/dt+beta)*chi = beta*sqrt(gamma)*psi + xi(t)` (Gap 10). `gamma -> 0` is a controlled decoupling limit of this auxiliary system.

## 2. Coupling completion (supersedes V2 linear EFT layer)

```
f(Phi/M_Pl) = g(Phi/M_Pl) = h(Phi/M_Pl) = 1 + O(gamma) * (Phi/M_Pl)^2
```

Derived from conformal weight counting + a Z_2 symmetry inherent to `D_mem`'s bilinear structure. No free EFT coefficients (`c_g`, `c_y` from V2 are removed — they conflicted with precision measurements by ~8 orders of magnitude).

## 3. Scalar potential

```
V(Phi) = (1/2)*gamma*beta^2*Phi^2 + (gamma^2/16*pi^2)*Phi^4
```

Minimum at `Phi=0`. `Phi_ref != 0` (needed for any cosmological signal) is not derived from `V(Phi)` alone — Gap 8, open.

## 4. Parameters (current default — Pair 1)

```
alpha = 1            [postulated]
beta  = 2*pi          [IDENTIFIED — Matsubara lead]
gamma = 0.003122      [IDENTIFIED — baryogenesis line + Matsubara]
```

See `THEORY.md` Section 4 for the full derivation-attempt history, including ruled-out paths.

## 5. Force Coupling Table

```
gamma_EM    = 0 exactly         [DERIVED]
gamma_g    -> 0                  [DERIVED]
gamma_weak ~ 408 at 1 fm         [DERIVED, 0.12% match to M_W*r]
gamma_strong: sign only          [IDENTIFIED (sign) + OPEN (magnitude)]
```

## 6. Closed/substantially-closed results

- Gap 3 (Cassini / alpha variation): closed, 50+ orders of margin
- Gap 7 (Horndeski / GW speed): closed, c_T=c exactly
- Gap 10 (auxiliary field / causal kernel): substantially addressed
- Gap 11 (conformal protection, gauge+Yukawa above EW): substantially closed
- Gap 12 (baryogenesis / c_W): substantially closed, c_W=0.9832
- Gap 13 (below-EW continuity): substantially resolved

## 7. Open

- Gap 4/9 (first-principles derivation of gamma, beta): open — see THEORY.md Section 4 for what has been tried and ruled out
- Gap 8 (Phi_ref): open, not blocking the above, but blocking CDDR/sigma8 (suspended)
- gamma_strong magnitude at Lambda_QCD: open

## 8. Suspended

- CDDR (Etherington distance duality)
- Mechanism 16 sigma8 response
- Galaxy rotation mechanism

All three require `Phi != 0` in a cosmological background, which is not currently derived (Gap 8).
