# Mechanism 16 — sigma_8 Response (V2 Canonical)
# Active public child branch of CDDR path
# Last updated: May 29, 2026

## Status

Active. Child branch of the frozen public CDDR path. V2 Canonical.

Not presented as an independently calibrated proof. Tests whether the same fixed V2 structure produces a consistent downstream sigma_8 response without branch-specific retuning.

---

## V2 Physical Mechanism

The sigma_8 suppression arises through two V2 channels:

**Channel 1 — Phi stress-energy:**
  H^2 = (8 pi G / 3)(rho_m + rho_Phi)
  rho_Phi = 1/2 Phi_dot^2 + V(Phi)
  Result: -1.13% sigma_8 suppression

**Channel 2 — Y(Phi) G_eff modification:**
  G_eff/G ~= 1 + c_y * Phi / M_Pl
  delta' + (2 + d ln H/dx) delta' - (3/2) Omega_m(a)(G_eff/G) delta = 0
  Result: -6.82% at G_eff/G = 0.98

**Combined (SuperGrok prototype):** -3% to -8% (DES/KiDS consistent)

Constrained range: -1% to -8% — NOT tunable, set by frozen parameters.
Point prediction requires c_y/c_g measurement from second observable.

---

## Connection to CDDR (V2 joint prediction)

The unique V2 signature:
  |eta-1| / |Delta_sigma_8/sigma_8| ~ 0.13 to 0.25

LCDM: undefined. Single-effect models: 0 or infinity.
This ratio is the observable fingerprint. Testable jointly by Euclid/Rubin 2027-2029.

CDDR formula (V2):
  eta(z=0.5) - 1 = -0.0569 * epsilon_g + 0.2384 * epsilon_y

epsilon_y ~ -0.021 gives sigma_8 suppression of -6.69%.

---

## Current Public Bridge

Weak-response bridge (conservative default):
  sigma8 = sigma8_ref * (1 + k * (eta - 1))
  sigma8_ref = 0.8121 (DESI+CMB)
  default k = 0.0

The k=0 default is intentionally conservative. The V2 derivation above gives the theoretically motivated response. These will converge as c_y/c_g is separately measured.

---

## Forward Predictions

| Prediction         | Confidence | Testable by       |
|--------------------|------------|-------------------|
| sigma_8 -4% to -8% | MEDIUM     | Euclid, Rubin     |
| Signature ratio    | MEDIUM     | Joint survey      |
| G_eff/G ~ 0.98    | MEDIUM     | CMB lensing       |

