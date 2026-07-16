# Logosfield V4 — In Causal Set Theory Language

**A translation document for external engagement**  
Earl Treloar · July 2026 · V4 Vision 26

---

## Purpose

This document maps V4's primitives and results onto standard causal set theory (CST) terminology. It is intended for causal set theorists engaging with V4 for the first time, and for clarifying exactly where V4 diverges from the standard CST program.

---

## What V4 Shares With Standard CST

**The underlying structure is identical.**

Standard CST (Bombelli, Lee, Myrheim, Sorkin 1987) is built on a locally finite partial order: a set C with a transitive, irreflexive, locally finite relation ≺. V4's A1 (events) and A2 (partial order with covering relations) are exactly CST's causal set. V4's grading is CST's height function. V4's covering relations are CST's links.

**A1 + A2 = CST-1 exactly. No divergence here.**

The Hauptvermutung (HV) — that the causal set faithfully embeds in a Lorentzian manifold, with cardinality approximating spacetime volume — is shared. V4 has not proved HV. PATH 2 (the converse Myrheim-Meyer theorem) is V4's systematic attempt. Layer 1 of PATH 2 is complete; Layers 2 and 3 are open.

---

## Where V4 Diverges From Standard CST

V4 diverges from CST at three points: A3, FP, and the two-observer structure.

### Divergence 1 — A3: The Memory Kernel

Standard CST has no memory relation. The dynamics (classical sequential growth or quantum measure) selects which causal sets are physically realized, but does not assign a two-point function to the partial order itself.

V4 adds a distinguished two-point function to the causal set:

**M(f,e) = exp(−β·n(f,e))**

where n(f,e) is the length of the longest chain from e to f (equivalently, the height difference in the Hasse diagram). This is called the memory kernel. It assigns to every causal relation (f,e) a weight that decays exponentially with chain length.

**In CST language:** V4 adds an exponential two-point function to the causal set, with decay constant β. This function is not the Green's function of any field on the causal set — it is a structural weighting of the partial order itself. It is derived from a composability requirement: M(f,e) = M(f,g)·M(g,e) for all intermediate g, which forces the exponential form uniquely.

### Divergence 2 — FP: Self-Consistency Replaces External Dynamics

Standard CST uses an external dynamics to generate or select causal sets:
- Classical sequential growth (Rideout-Sorkin): causal sets grow by sequential element addition with transition probabilities
- Quantum measure / path sum: a sum over causal sets weighted by a quantum amplitude

Both approaches apply an external rule to the space of causal sets.

V4 replaces external dynamics with an internal self-consistency condition — the Founding Principle (FP):

> *All potential is realized before it began. It cannot over-realize that maximum.*

FP has two components:
- **FP-lower (existence):** The structure must realize all its generative potential
- **FP-upper (specificity):** The structure cannot exceed its own generative capacity

**In CST language:** FP is a fixed-point self-consistency condition on the causal set with memory kernel. The causal set is not grown by an external rule — it is the unique fixed point of its own realization criterion. The self-consistency condition is: exp(−β) = exp(−ρ·V_interval), where ρ is the event density and V_interval is the causal interval volume.

This replaces the CSG transition probabilities or quantum amplitude with a single uniqueness requirement. V4 asks: is there a causal set with memory kernel that is so self-consistent that it determines its own parameters? The answer is yes, and the parameters are derived.

**This is V4's most fundamental divergence from CST.** CST's dynamics generates many causal sets; V4's FP selects the unique self-consistent one. These are compatible at the structural level — both operate on locally finite partial orders — but differ fundamentally in approach.

### Divergence 3 — Two-Observer Structure

Standard CST has no formal observer structure. The HV is a mathematical statement about the relationship between the causal set and the embedding manifold, not about observers.

V4 has a derived two-observer structure:

**Logos-observer:** Outside the partial order. Sees the complete structure simultaneously. The perspective from which FP is stated.

**Inside observer:** Created into the mechanism. Registers only its causal past through the memory kernel M(f,e). Has access only to what the kernel delivers at each event.

**In CST language:** The inside observer is the causal past of a single element, equipped with the memory kernel as a weighting function. The Logos-observer is the global causal set viewed from outside. In standard CST, this distinction is mathematical convenience. In V4, the inside observer is structurally load-bearing: it is the mechanism through which FP-lower is satisfied (V4 Vision 25). The memory kernel is not an external two-point function — it is the inside observer's registration of its own causal past.

---

## Derived Results in CST Language

| V4 Result | CST Translation | Status |
|-----------|----------------|--------|
| d=4 [DERIVED] | Spacetime dimension is derived, not input | [DERIVED — fully closed] |
| β=2π [DERIVED] | Exponential decay constant of memory kernel is derived | [DERIVED — 10 review cycles] |
| τ=1 [DERIVED] | Link length (covering relation step) is the unique unit | [DERIVED] |
| β>0 [DERIVED] | Memory kernel decays (does not amplify) — forced by finite entropy | [DERIVED] |
| FP-minimal [DERIVED] | Fixed-point condition is the minimal sufficient selector | [DERIVED] |
| PATH2-L1 [DERIVED] | f_MM(d)=1/60 forces d=4 uniquely — analytic proof | [DERIVED] |
| ρ=24/π [IDENTIFIED] | Sprinkling density is constrained by self-consistency | [IDENTIFIED — HV conditional] |
| N_past=β [IDENTIFIED] | Expected past element count per memory cycle = 2π | [IDENTIFIED — HV conditional] |
| Flatness (R=0) [IDENTIFIED] | Memory completeness forces constant interval volume | [IDENTIFIED — HV conditional] |
| U(1)×SU(2) from A2 [IDENTIFIED] | Electroweak symmetry from lightcone cross-section in d=4 | [IDENTIFIED — HV conditional] |

---

## What V4 Derives That CST Takes As Input

Standard CST inputs:
- Spacetime dimension d (estimated by MM estimator, not derived)
- Sprinkling density ρ (free parameter)
- No dynamics selector (multiple competing approaches)

V4 derives:
- d=4 uniquely (from Huygens + grading + FP)
- β=2π (memory decay constant, from T-P commensurability + FP)
- ρ=24/π (from self-consistency, HV conditional)
- The unique self-consistent selector (FP, derived as minimal sufficient)

**The core claim in CST language:** If a causal set is equipped with an exponential memory kernel M(f,e)=exp(−β·n) and required to be uniquely self-consistent under FP, then the dimension is forced to be 4, the decay constant is forced to be 2π, and the sprinkling density is constrained to 24/π. These are not inputs — they are outputs of the self-consistency requirement.

---

## The Planck-Scale Fluctuation Prediction

At background density ρ=24/π with β=2π, the expected number of elements per causal diamond is N = ρ·V_diamond = 1. Poisson fluctuations at N=1 give standard deviation σ = 1, i.e., 100% fluctuations at the single-diamond scale.

At the scale of one complete memory cycle (N_past = β ≈ 6.28 elements), fluctuations are σ/N = 1/√β ≈ 40%.

**In CST language:** V4 predicts that metric fluctuations at the Planck scale are of order 1/√(2π) ≈ 40% — significantly larger than what is typically assumed in causal set phenomenology. At macroscopic scales (many memory cycles), the fluctuations average out to statistical flatness.

**Distinguishing feature:** Standard causal set phenomenology (following Sorkin's work on the cosmological constant and causal set diffusion) typically assumes Poisson fluctuations at the Planck scale but does not derive a specific fluctuation amplitude from the sprinkling density. V4's self-consistency condition gives a specific prediction: ρ=24/π, N_diamond=1, σ/N=1/√β at the memory-cycle scale.

---

## The Two Results Ready for External Review

### Result 1 — PATH2-L1 (V4 Vision 24)

**Statement:** f_MM(d) = Γ(d+1)·Γ(d/2+1)/(4·Γ(3d/2+1)) is strictly decreasing on (0,∞), and f_MM(d)=1/60 has exactly one solution: d=4.

**Proof sketch:** The log-derivative L(d) = ψ(d+1) + (1/2)ψ(d/2+1) − (3/2)ψ(3d/2+1) equals −∫₀^∞ e^{−t}h(dt)/(1−e^{−t})dt where h(s)=e^{−s}+(1/2)e^{−s/2}−(3/2)e^{−3s/2}. Substituting u=e^{−s/2}: h=u·g(u) where g(u)=−(3/2)u²+u+1/2>0 on (0,1). Therefore L(d)<0 for all d>0. IVT gives unique solution at d=4.

**Why this matters for CST:** This proves that the MM dimension estimator, applied to any causal set in any dimension, gives f_MM=1/60 if and only if d=4. This is the converse MM theorem at the dimension level — a result that CST has used empirically but not proved analytically.

**Import risk:** None. Pure mathematics. No physical assumptions.

### Result 2 — Global-to-Local FP Passage (V4 Vision 25)

**Statement:** In V4's memory structure, FP-lower applied globally implies FP-lower applied pointwise at each element, because memory registration is pair-specific and non-compensable across elements.

**Argument:** (1) The only realization mechanism for FP-lower is the inside observer's memory kernel at each element. (2) M(f,e) is pair-specific — S(f) deficit at f cannot be compensated by S(g) surplus at g because no pooling mechanism exists in A3. (3) The two-observer structure (Logos-observer global, inside observer local) makes realization structurally element-specific. (4) Therefore global FP-lower implies pointwise FP-lower: S(f) = self-consistent value at every element f.

**Why this matters for CST:** This shows that a self-consistency requirement on a causal set with memory kernel descends from global to local without additional assumptions — using only the pair-specificity of the kernel and the structural distinction between global and local observers. This is a general result about memory-equipped causal sets, not specific to V4's parameters.

**Import risk:** Low. Uses A3 structure and the derived two-observer distinction. Does not use ρ=24/π or HV.

---

## Open Questions in CST Language

- **HV (Hauptvermutung):** Does the V4 causal set faithfully embed in (1+3)d Minkowski spacetime? PATH 2 Layers 2 and 3 are the current approach. Layer 1 complete.
- **De Sitter ruling:** Is de Sitter spacetime excluded by the memory completeness flatness result? De Sitter has R>0; the flatness result forces R=0 (HV-conditional). Need to confirm de Sitter is covered by the curved R≠0 case.
- **Compact topology ruling:** Does the derived Poisson chain distribution rule out compact topologies at any compactification scale?
- **Quantum behavior:** Does quantum mechanics emerge from the phase structure of k-chains in the V4 causal set? PATH 8 — not yet attempted.

---

## How to Engage With V4

The full session record (V17-V25) is at: `github.com/earltreloar/Logosfield-public-evidence-`

Verification script (Python): `V4/verify_v22.py` — 61/61 checks pass.

Current master document: `V4/Logosfield_V4_Vision_25_Master.docx`

The most reviewable standalone result is PATH2-L1 — a five-step analytic proof with no physical assumptions, verifiable by any mathematician familiar with the Gamma and digamma functions.

---

*V4 Vision 26 · July 2026 · Earl Treloar · Logosfield / ODCCT*
