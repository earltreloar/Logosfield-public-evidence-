# Reproduce the Logosfield V2 Public Path
# Last updated: May 29, 2026

This repository maintains a **narrowed frozen V2 public test path**.

The active public path currently includes only:
1. CDDR (anchor)
2. Mechanism 16 — sigma_8 response (child branch)

---

## Requirements

Recommended environment:
- Python 3.10+
- NumPy, Pandas, Matplotlib

---

## Active Reproduction Commands

Run CDDR:
    python run.py --mode cddr

Run Mechanism 16:
    python run.py --mode mech16

Or via Makefile:
    make mech16

---

## Expected Outputs

**CDDR run should:**
- Compute eta(z) = D_L / ((1+z)^2 D_A)
- Print eta mean and std
- V2 prediction: eta(z=0.5) - 1 = -0.0569*epsilon_g + 0.2384*epsilon_y

**Mechanism 16 run should:**
- Compute downstream sigma_8 response
- Print sigma_8 value and benchmark comparison
- V2 prediction: -3% to -8% suppression range

**Joint signature to compute:**
  |eta-1| / |Delta_sigma_8/sigma_8| ~ 0.13 to 0.25

This ratio is the unique V2 fingerprint. Please report it explicitly.

---

## V2 Framework Notes

The V2 Canonical framework uses the memory-covariant derivative:

  D_mem,mu psi(x) = integral K(x,x; beta,gamma) * U(x,x) * D_mu psi(x) d^4x
  K = gamma*beta * exp(-beta*(t-t)) * Theta(t-t)

Conservative limit: gamma -> 0 recovers D_mu exactly.

Frozen parameters:
  alpha = 1
  beta ~= 2pi  (working assumption)
  gamma = 0.005

EFT coefficients (constrained, not tunable per mechanism):
  c_g: epsilon_g > 0.088 for Euclid threshold
  c_y: epsilon_y ~ -0.021 for sigma_8 tension target

---

## Other Mechanisms

Additional mechanisms are in the repository but are not part of the
current locked public test path:

| Mechanism | Domain              | Status              |
|-----------|---------------------|---------------------|
| 15        | Ly-alpha escape z=13 | Provisional         |
| 17        | H0 reconciliation   | Under review        |
| 21        | SMBH seeding        | Feasibility shown   |
| 25        | Baryon asymmetry    | Directional         |
| Consciousness | Neural domain   | Framework complete  |

---

## Current Cautions

This repository does **not** currently claim:
- Confirmed discovery of a new force
- Validated galaxy rotation curve solutions
- Full empirical separation of c_g and c_y
- Inheritance of all mechanisms from the frozen path

Bayesian position: 10-15% posterior.
Definitive test: Euclid/Rubin 2027-2029.

---

## Key Files

README.md — project overview
THEORY.md — canonical V2 model summary (Sections 10-11 critical)
ZPhi_Summary.md — full V2 technical derivation
EFT couplings — V2 operator structure
CHALLENGE.md — replication challenge
Cosmology — CDDR and sigma_8 modules
Mechanism_Consciousness.md — consciousness domain (Point 1)
run.py — public execution runner

