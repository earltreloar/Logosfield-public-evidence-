# Logosfield / ODCCT Replication Challenge — V3
# Last updated: V3 update

The current public replication challenge tests whether the framework's **closed structural results** survive independent scrutiny — not the suspended cosmology predictions, which require further derivation before they can be meaningfully challenged.

---

## What changed from V2

V2's challenge was built around the CDDR and Mechanism 16 formulas, which depended on a linear EFT completion (`Z(Phi)`, `Y(Phi)` with free coefficients `c_g`, `c_y`) that has since been removed for conflicting with precision measurements by ~8 orders of magnitude. Those two predictions are now **SUSPENDED** pending Gap 8 (derivation of `Phi_ref`) — see `00_THEORY.md` Sections 9–10.

This is not a weakening of the challenge — it is a correction. Challenging a suspended, not-yet-rederived prediction would not be a meaningful test.

---

## Active challenge targets (V3)

### 1. Force Coupling Table — weak sector formula

**Claim:** `gamma(r) = M*r` (the exponent of a Proca/Yukawa propagator) gives `gamma_weak ~ 408` at `r = 1 fm`, matching `M_W * (1 fm)/(hbar*c)` to better than 0.2%.

**Challenge:** verify this numerical match independently, and check whether the same functional form can or cannot be extended to other known massive-boson sectors as a consistency check.

### 2. Gap 3 — Cassini / alpha variation margins

**Claim:** at the current default parameters (`beta=2*pi`, `gamma=0.003122`), the predicted PPN-gamma deviation and laboratory alpha-variation are suppressed by ~59 and ~116 orders of magnitude respectively below current bounds.

**Challenge:** independently verify the suppression-scaling argument (`(t_kernel/t_Hubble)` and its square) and check whether the margins remain large under reasonable variation of the parameter pair (see `00_THEORY.md` Section 4 for the range of internally-motivated candidate pairs).

### 3. Gap 7 — Horndeski mapping

**Claim:** diffeomorphism invariance forces `G3=G5=0`, `G4=M_Pl^2/2` (constant), giving `c_T=c` exactly.

**Challenge:** verify the mapping from the memory-covariant matter sector to this minimal-Horndeski gravity sector, and confirm no residual non-minimal coupling survives.

### 4. Gap 10 — auxiliary field derivation

**Claim:** the causal and symmetric memory kernels both arise from a single auxiliary field `chi` obeying `(d/dt+beta)*chi = beta*sqrt(gamma)*psi + xi(t)`; the symmetric kernel matches `chi`'s stationary correlator under a fluctuation-dissipation relation.

**Challenge:** reproduce the Monte Carlo Ornstein-Uhlenbeck verification of this correlator matching, and check the claimed retraction of an earlier ("kernel collapse") hypothesis.

---

## Suspended — not currently active challenge targets

- CDDR (Etherington distance-duality)
- Mechanism 16 (sigma8 response)
- Galaxy rotation mechanism

These require an independently-derived `Phi_ref != 0`, which the framework does not currently provide (Gap 8). Reproducing the historical V2 formulas for these (retained in `05_Cosmology.md` for reference) is not a meaningful test of the current framework, since those formulas depended on a coupling structure that has been removed.

---

## How to submit a challenge result

Provide code, environment, and outputs as in previous versions of this challenge (see `07_REPRODUCE.md`). Results should specify clearly which V3 claim (1–4 above) is being addressed.
