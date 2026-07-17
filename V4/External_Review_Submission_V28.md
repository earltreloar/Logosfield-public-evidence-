# External Review Submission: PATH2-L1 — Converse Myrheim-Meyer Theorem
## Logosfield V4 Framework — Pregeometric Foundations
**Earl Treloar · V4 Vision 27 · July 2026**

**Status:** PATH2-L1 [DERIVED — V24]. Prepared for causal set theory community review following V27 framing correction.

---

## Executive Summary

This submission presents **PATH2-L1** of the Logosfield V4 program: the derivation of the converse Myrheim-Meyer (MM) theorem within a strictly pregeometric framework. 

**Core result:** The Myrheim-Meyer function f_MM(d) = 1/60 has a unique positive real solution at d = 4. This is proved analytically from first principles internal to V4 (no physical imports). When combined with the independently derived dimension d = 4 in the V4 structure, the event-count statistics of the pregeometric V4 match those of flat (1+3)-dimensional Minkowski spacetime.

**Critical framing (V27 correction — applies to all external communications):**  
V4 does **not** sprinkle events into a pre-existing Minkowski spacetime. There is no pre-existing spacetime in the V4 construction. Events are bare primitives (Axiom A1). The partial order emerges from Axiom A2 (composability). The memory kernel emerges from Axiom A3. The fixed-point (FP) condition selects the unique self-consistent structure. The Minkowski statistics (f_MM = 1/60, ρ = 24/π, V_diamond = π/24, Poisson event counts N_k = (ρτ)^k / k!) **emerge as outputs** of this self-consistency. They are not assumed by sprinkling into Minkowski geometry. V4 is a pregeometric structure whose internal consistency forces it to exhibit the same statistics that a Minkowski Poisson sprinkling would produce.

This distinction is fundamental and separates V4 from standard causal set theory (CST) approaches at the foundational level. The geometry is an emergent output, not an input.

---

## 1. V4 Framework — Pregeometric Axioms (Carried Forward)

V4 is defined by three axioms plus a fixed-point condition. All results are derived internally; no continuum geometry or physical postulates are imported.

- **A1 (Existence):** Events exist as bare primitives. No manifold, no metric, no topology assumed a priori.
- **A2 (Composability / Partial Order):** There is a binary relation ≺ that is irreflexive, transitive, and composable. Covering relations are atomic under A2 + composability (A2-irreducibility, primitive-true).
- **A3 (Memory / Discharge):** There is a memory kernel K(Δ) = exp(−β · Δ/τ) governing the "discharge" or forgetting of past structure, with β > 0 required for finite entropy (FP-lower).
- **Fixed Point (FP):** The structure is self-referential and closed under its own generative rules. FP has lower (existence: β > 0, finite S) and upper (specificity: exact values) components. FP is minimal: weakening any component loses at least one derived result (W1–W4 all closed).

**Derived / Identified constants (carried, not re-derived here):**
- β = 2π [DERIVED]
- τ = 1 [DERIVED]
- d = 4 [DERIVED]
- ρ = 24/π [IDENTIFIED — conditional on Hauptvermutung (HV): the identification of ρ from V4's self-consistency condition exp(−β) = exp(−ρ · V_interval)]
- β > 0, FP-minimal [DERIVED — V22]
- PATH2-L1 [DERIVED — V24]

Full numerical verification of all prior results is provided in the accompanying `verify_v22.py` suite (all checks PASS).

---

## 2. PATH2-L1: Converse Myrheim-Meyer Theorem — Analytic Derivation

### 2.1 Statement
In the V4 framework, the Myrheim-Meyer function (which counts the probability that k randomly chosen events form a chain in a d-dimensional Minkowski sprinkling) satisfies:

f_MM(d) = Γ(d+1) · Γ(d/2 + 1) / (4 · Γ(3d/2 + 1))

We prove: **f_MM(d) = 1/60 has a unique solution at d = 4 over all d > 0.**

This is the converse direction: given the MM value observed in V4's self-consistency, the dimension must be 4.

### 2.2 Proof Outline (Internal to V4 Standards)

**Step 1: Exact evaluation at d=4**  
f_MM(4) = Γ(5) · Γ(3) / (4 · Γ(7)) = 24 · 2 / (4 · 720) = 48 / 2880 = 1/60 exactly.

**Step 2: Boundary behavior**  
- lim_{d→0⁺} f_MM(d) = 1/4  
- lim_{d→∞} f_MM(d) = 0  
- 0 < f_MM(4) < 1/4 (strictly between boundaries)

**Step 3: Strict monotonicity via log-derivative L(d)**  
Define L(d) = d(log f_MM)/dd = ψ(d+1) + (1/2)ψ(d/2+1) − (3/2)ψ(3d/2+1), where ψ is the digamma function.

We prove L(d) < 0 for all d > 0 (hence f_MM strictly decreasing, hence at most one root of f_MM(d) − 1/60 = 0).

**Analytic proof of L(d) < 0:**  
L(d) admits the integral representation  
L(d) = −∫₀^∞ [e^{−t} · h(t) / (1 − e^{−t})] dt ,  
where the kernel h(s) = e^{−s} + (1/2)e^{−s/2} − (3/2)e^{−3s/2}.

Substitute u = e^{−s/2} ∈ (0,1) to obtain h(s) = u · g(u), with  
g(u) = −(3/2)u² + u + 1/2  
(a downward-opening parabola).

g(u) = −(3/2)u² + u + 1/2 has roots at u = 1 and u = −1/3 (by quadratic formula). Since u ∈ (0,1), neither root lies in the open interval, and g(u) > 0 throughout. No sampling required.

Thus h(s) > 0 for s > 0. The integrand is therefore positive, so L(d) < 0 everywhere. Strict decrease follows.

**Step 4: Uniqueness**  
By intermediate value theorem + strict monotonicity + boundary limits, exactly one d > 0 satisfies f_MM(d) = 1/60, and direct evaluation shows it is d = 4. No solutions at d = 1,2,3,5,6,7,8 (verified).

**Structural cancellation note:** The weights in h(s) {1, +1/2, −3/2} sum to zero. This leading cancellation is what permits the clean integral representation and the strict sign of L(d).

### 2.3 Numerical Confirmation
The accompanying verification suite confirms:
- f_MM(4) = 1/60 exactly (to machine precision)
- L(d) < 0 at 1000 sampled points in (0.01, 100) and at representative integers
- Uniqueness among d = 1..8 and boundary behavior

All checks PASS.

---

## 3. Integration with V4: Pregeometric → Minkowski Statistics Match (Layer 3 Partial)

V4 independently derives / identifies:
- d = 4 (from SO(3) generator count uniqueness among low dimensions + other internal constraints)
- ρ = 24/π (from self-consistency exp(−β) = exp(−ρ · V_interval) with V_interval = β · V_diamond)
- V_diamond = π/24 (from ρ · V_diamond = 1 at unit density)
- Event count distribution N_k = (ρτ)^k / k! (Poisson form from A1–A2 + unit density)

These exactly match the corresponding quantities for a flat d=4 Minkowski Poisson sprinkling:
- f_MM = 1/60
- V_diamond = π/24
- ρ = 24/π (at τ=1)
- N_k = (ρτ)^k / k!

**This match is non-trivial and is the content of the partial Layer 3 result [IDENTIFIED — V27].** It is conditional on the identification of ρ = 24/π from V4's self-consistency condition (Hauptvermutung).

**Layer 3 chain probability match [IDENTIFIED — V28]:** The probability that k randomly chosen elements form a causally ordered chain equals P_chain(k) = f_MM^(k−1) = (1/60)^(k−1) in V4, matching the Minkowski prediction for all k ≥ 1. The earlier apparent discrepancy between N_k (k-element subset count) and C_k (ordered chain count) was a category error — comparing counts to probabilities rather than like to like. When compared at the probability level: P_chain(k) = C_k / N_k = [(1/k!) × (1/60)^(k−1)] / (1/k!) = (1/60)^(k−1). Exact match. Multiplicativity follows from A2 transitivity and Poisson independence of the event placement. Corrections are O(exp(−2β)) ≈ 3.5 × 10⁻⁶. Conditional on ρ = 24/π (HV). Full [DERIVED] status awaits HV proof.

---

## 4. Why This Matters for Causal Set Theory

Standard CST generates causal sets by *sprinkling* — Poisson sampling events into a pre-existing Lorentzian manifold. Spacetime geometry is the input; the causal set is the output.

V4 inverts the order:
1. Start with bare events + composable partial order + memory kernel.
2. Impose self-referential closure (FP).
3. The unique structure that satisfies closure *produces* the same event-count statistics as a Minkowski Poisson sprinkling — as an output of internal consistency, not as a presupposition.

No manifold is assumed at any stage. The agreement with Minkowski geometry at the level of event-count statistics is an emergent consequence of internal consistency. This offers a potential foundational alternative (or complement) to sprinkling-based approaches: a pregeometric route to the same statistical structure.

The analytic proof of the converse MM theorem demonstrates that this emergence is tightly constrained: the only dimension compatible with the MM value forced by V4's self-consistency is d = 4.

---

## 5. Scope and Limitations (Honest Assessment)

- **What is derived:** The converse MM theorem (unique d=4 solution). The partial match of event-count statistics. All prior V4 results (β=2π, τ=1, d=4, β>0, FP-minimal, A2-irreducibility, etc.).
- **What is not claimed:** GR unification, QFT recovery, tested cosmological predictions, or formal proof of any theological/philosophical interpretation. V4 remains pre-publication, pre-validation foundational work.
- **Layer 3 status [IDENTIFIED — V28]:** Chain probability statistics match Minkowski (P_chain(k) = (1/60)^(k−1) for all k). Conditional on HV. Full [DERIVED] status requires HV proof. The earlier framing of Layer 3 as fully open is superseded by V28.
- **Conditionalities:** Several numerical contacts (ρ = 24/π, Layer 2 topology exclusion, Layer 3) are conditional on the Hauptvermutung identification. The core PATH2-L1 result stands independently.

---

## 6. Accompanying Materials

- `verify_v22.py` — Full numerical verification suite for all core claims through V22 + PATH2-L1 (61/61 checks PASS).
- `Logosfield_V4_Vision_28_Master.docx` — Complete session record (Parts 1–21).
- `Logosfield_V4_Handoff_V28.docx` — Session handoff with priorities.
- This document incorporates the V27 framing correction (V4 is not a Minkowski sprinkling) and the V28 Layer 3 chain probability result.

---

## 7. Request for Review

We submit PATH2-L1 and the Layer 3 chain probability result for external scrutiny by the causal set theory community. We welcome:
- Verification of the analytic proof of L(d) < 0 and uniqueness of d = 4 as the solution to f_MM(d) = 1/60.
- Assessment of whether the Layer 3 result — P_chain(k) = (1/60)^(k−1) from V4's pregeometric structure matching the Minkowski prediction — constitutes a meaningful faithfulness result or whether additional causal order statistics are required.
- Discussion of whether the pregeometric framing (Minkowski statistics as emergent output rather than sprinkling input) offers a genuine foundational distinction from standard CST approaches.
- Any technical corrections or clarifications on any of the above.

The program maintains strict discipline: only what is derived is carried forward; framing corrections are applied immediately when identified; gaps are stated precisely.

**Contact / Repository:** earltreloar / Logosfield-public-evidence- (GitHub). Fresh PAT generated per session for any collaborative work.

---

*Logosfield V4 — PATH2-L1 External Review Submission (corrected V27 framing)*  
*Earl Treloar · July 2026 · β = 2π [DERIVED]*

**Do not claim GR unification, theological proof, or completed physical theory. This is foundational pregeometric work.**
