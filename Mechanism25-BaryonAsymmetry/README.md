# Mechanism 25 — Status Note (V3)
# Original file: Mechanism25-BaryonAsymmetry (V2 Canonical, unchanged below this note)

**This note was added during the V3 update. The original V2 content follows unchanged below for historical reference.**

## V3 status: NOT RECONCILED — flagged, not superseded outright

This mechanism's V2 content should be read with three corrections in mind:

1. **Uses superseded parameters.** It is written at `gamma = 0.005`, the V2 working value. The current default is `gamma ~= 0.003122` (V3 Pair 1 — see `00_THEORY.md` Section 4).

2. **Cites suspended results as cross-domain consistency evidence.** The file's "Cross-domain consistency" claim explicitly invokes "sigma_8 suppression" and "CDDR signal" as corroborating the same frozen parameters. Both of those are now **SUSPENDED** (see README status table, `05_Cosmology.md`). This specific cross-domain consistency argument no longer holds as stated.

3. **Describes a different mechanism than the archive's actual Gap 12 derivation.** This file's CP-violating phase comes from `D_mem` acting directly on fermion fields during reheating (`delta_CP ~ gamma*alpha`). The framework's actual derived baryogenesis result (Gap 12, substantially closed) instead derives the CP phase from a chiral SU(2)_L Wilson line with temporal asymmetry, and computes the Weinberg operator Wilson coefficient `c_W = 0.9832` via a Polyakov loop argument — see `00_THEORY.md` Section 8. **These two mechanisms have not been reconciled.** It is not yet established whether they are compatible, equivalent under some limit, or in conflict.

This mechanism is not formally superseded (unlike the linear EFT completion), because no audit has yet determined whether its core claim is right, wrong, or a restatement of the same physics in different language. It is flagged here as **requiring reconciliation with the Gap 12 derivation** before its predicted `eta ~= 6.1e-10` can be cited as a current, validated result of the framework.

**Confidence, as self-assessed in the original file: MEDIUM (mechanism clear from V2 structure; numerical verification pending).** This self-assessment predates the Gap 12 work and should not be read as confirming consistency with it.

---

## Original V2 content (unchanged)

### Mechanism 25 — Baryon Asymmetry Generation via Logosfield Memory Bias (V2 Canonical)
# Last updated: May 29, 2026

The Logosfield naturally resolves the baryon asymmetry problem without
additional particles or fine-tuned resonances beyond the minimal scalar extension.

---

## V2 Physical Mechanism

In V2, the memory-covariant derivative D_mem,mu acts on matter fields psi
(quarks, leptons) during reheating. This is distinct from the V1 formulation
which used a nonlocal S_mem bilinear on Phi itself.

**V2 operator acting on matter:**
```
D_mem,mu psi(x) = integral K(x,x; beta,gamma) * U(x,x) * D_mu psi(x) d^4x
K = gamma*beta * exp(-beta*(t-t)) * Theta(t-t)
```

With gamma = 0.005, beta ~= 2pi.

During reheating (T ~ 10^12 - 10^15 GeV), D_mem,mu acting on fermionic
matter fields introduces a chiral phase preference through the retarded
kernel structure. The kernel is asymmetric in time (Theta(t-t) enforces
causality), producing an effective CP-violating phase:

  delta_CP ~ gamma * alpha ~ 0.005

This biases weak-scale sphaleron processes toward matter channels by
~10^-9 without explicit heavy mediators.

---

## Sakharov Conditions Satisfied

1. **B violation**: Via electroweak sphalerons (active above T_EW)
2. **C/CP violation**: Intrinsic to the asymmetric memory kernel acting
   on fermion fields — the retarded structure is inherently time-asymmetric
3. **Departure from equilibrium**: Rapid reheating + field damping drives
   out-of-equilibrium dynamics

---

## Predicted Asymmetry

  eta = n_B / n_gamma ~= 6.1 x 10^-10

Matches CMB observation for locked parameters
{alpha=1, beta~=2pi, gamma=0.005}.

Cross-domain consistency: same frozen parameters that give sigma_8
suppression, CDDR signal, and SMBH seeding also produce the correct
baryon asymmetry. No retuning per mechanism.

---

## Key Feature

No primordial antimatter excess to hide. The asymmetry is seeded from
the memory kernel's inherent temporal directionality (the Theta function),
preserving CPT overall while favoring baryons from the outset.

---

## Status

Directional derivation complete. Formal derivation to publication
standard requires full numerical integration of the V2 kernel acting
on fermionic fields during reheating. Not part of the current locked
public challenge path (CDDR + Mechanism 16).

Confidence: MEDIUM (mechanism clear from V2 structure; numerical
verification pending).

