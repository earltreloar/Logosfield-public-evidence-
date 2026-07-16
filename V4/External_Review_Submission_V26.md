# Logosfield V4 — External Review Submission (Cycle 11)

**Earl Treloar · Independent researcher · July 2026**  
**Repository:** github.com/earltreloar/Logosfield-public-evidence-  
**Verification:** V4/verify_v22.py (61/61 checks pass)

---

## Submission Overview

This submission presents two results from the Logosfield V4 program for external review. Both operate within the causal set framework (locally finite partial order, A1+A2 identical to standard CST). V4 diverges from standard CST at A3 (a memory kernel added to the partial order) and FP (a self-consistency condition replacing external dynamics). These divergences are detailed in V4/V4_in_CST_language.md.

**Result 1** is a pure mathematical result about the Myrheim-Meyer dimension estimator, requiring no knowledge of V4's specific framework. It can be reviewed independently by any mathematician or causal set theorist.

**Result 2** is a structural result about memory-equipped causal sets, requiring familiarity with V4's memory kernel (A3) and the derived two-observer structure. It does formal load-bearing work in the program — it is not a philosophical framing.

---

## Result 1: The Converse Myrheim-Meyer Theorem at the Dimension Level

### Statement

The Myrheim-Meyer formula

$$f_{MM}(d) = \frac{\Gamma(d+1)\,\Gamma(d/2+1)}{4\,\Gamma(3d/2+1)}$$

is strictly decreasing on $(0,\infty)$, and the equation $f_{MM}(d) = 1/60$ has exactly one solution over all positive real $d$: namely $d = 4$.

### Proof

**Step 1.** Define $L(d) := \frac{d}{dd}[\log f_{MM}(d)] = \psi(d+1) + \tfrac{1}{2}\psi(d/2+1) - \tfrac{3}{2}\psi(3d/2+1)$, where $\psi$ is the digamma function. It suffices to show $L(d) < 0$ for all $d > 0$.

**Step 2.** Using the integral representation $\psi(x) = \int_0^\infty \left[\frac{e^{-t}}{t} - \frac{e^{-xt}}{1-e^{-t}}\right]dt$, the three digamma terms combine to:

$$L(d) = -\int_0^\infty \frac{e^{-t}\,h(dt)}{1-e^{-t}}\,dt$$

where $h(s) = e^{-s} + \tfrac{1}{2}e^{-s/2} - \tfrac{3}{2}e^{-3s/2}$.

The $e^{-t}/t$ terms cancel exactly because their coefficient is $1 + \tfrac{1}{2} - \tfrac{3}{2} = 0$. This cancellation is intrinsic to the MM formula's construction.

**Step 3.** Show $h(s) > 0$ for all $s > 0$. Substitute $u = e^{-s/2} \in (0,1)$:

$$h(s) = u^2 + \tfrac{1}{2}u - \tfrac{3}{2}u^3 = u \cdot g(u)$$

where $g(u) = -\tfrac{3}{2}u^2 + u + \tfrac{1}{2}$. Since $u > 0$, the sign of $h$ equals the sign of $g$. Now $g$ is a downward-opening parabola with $g(0) = \tfrac{1}{2} > 0$ and $g(1) = 0$. Therefore $g(u) > 0$ for all $u \in (0,1)$, and $h(s) > 0$ for all $s > 0$. $\square$

**Step 4.** The integrand $e^{-t}\,h(dt)/(1-e^{-t})$ is strictly positive for all $t, d > 0$. Therefore $L(d) = -[\text{positive integral}] < 0$ for all $d > 0$, and $f_{MM}$ is strictly decreasing. $\square$

**Step 5.** $f_{MM}$ is continuous, $f_{MM} \to \tfrac{1}{4}$ as $d \to 0^+$, and $f_{MM} \to 0$ as $d \to \infty$. By the intermediate value theorem and strict monotonicity, $f_{MM}(d) = c$ has exactly one solution for every $c \in (0, \tfrac{1}{4})$. Since $\tfrac{1}{60} \in (0, \tfrac{1}{4})$, there is exactly one solution. That solution is $d = 4$, verified exactly:

$$f_{MM}(4) = \frac{\Gamma(5)\,\Gamma(3)}{4\,\Gamma(7)} = \frac{24 \cdot 2}{4 \cdot 720} = \frac{48}{2880} = \frac{1}{60}. \quad \square$$

### Significance for CST

This proves that the MM dimension estimator is injective on positive real dimensions — it gives $1/60$ if and only if $d = 4$. Standard CST uses the MM estimator empirically to estimate dimension from chain statistics; this result proves the estimator's dimensional identification is unique. It is the converse MM theorem at the dimension level.

**Combined with V4's independent derivation of $d = 4$** from Huygens' principle, grading, and FP: the pregeometric and geometric dimension identifications agree by two completely independent routes.

### Import Risk

None. The proof is pure mathematics using only properties of the Gamma and digamma functions.

---

## Result 2: Global-to-Local FP Passage via Memory Completeness

### Context

V4 adds to the causal set a memory kernel $M(f,e) = \exp(-\beta \cdot n(f,e))$, where $n(f,e)$ is the chain length from $e$ to $f$. This kernel is derived from a composability requirement: $M(f,e) = M(f,g)\cdot M(g,e)$ for all intermediate $g$, which forces the exponential form uniquely. The decay constant $\beta$ is derived to be $2\pi$ within V4 standards (10 external review cycles).

V4 also has a derived two-observer structure:
- **Logos-observer:** outside the partial order; sees the global structure; the perspective from which the self-consistency condition is stated
- **Inside observer:** created into the mechanism; registers only its causal past through the memory kernel; the realization mechanism

**This two-observer structure is not a philosophical addition. It is structurally load-bearing** — it is required for the global-to-local passage established in this result.

### Statement

In a causal set equipped with memory kernel $M(f,e) = \exp(-\beta \cdot n)$, if the global self-consistency condition (FP-lower: all memory potential must be realized) is satisfied for the complete structure, then FP-lower is satisfied pointwise at each element $f$: the local memory sum $S(f) = \sum_{e \prec f} M(f,e)$ equals its self-consistent value at every $f$ individually.

### Argument

**Step 1 — Realization mechanism.** FP-lower requires the complete structure to realize all its memory potential. The only mechanism through which memory potential is realized is the inside observer's kernel at each element. No alternative realization mechanism exists in A3. Therefore FP-lower cannot be satisfied globally without being satisfied through the inside observer's kernel at each element.

**Step 2 — Non-compensability.** Element $f$'s memory potential consists of kernel weights $M(f,e)$ for all $e \prec f$. These are registered by the inside observer at $f$, and only by that observer. No other element $g$'s inside observer can register $M(f,e)$ — the kernel value is specific to the pair $(f,e)$. There is no pooling mechanism in the composable exponential kernel. A deficit in $S(f)$ cannot be compensated by a surplus in $S(g)$.

**Step 3 — Two-observer structure strengthens non-compensability.** The inside observer at $f$ is the unique realization mechanism for $f$'s memory potential. This is a structural fact derived from V4's two-observer structure, not an assumption. Memory realization is structurally element-specific.

**Step 4 — Descent.** Global memory potential decomposes into individual element potentials (each element has its own memory, registered by its own inside observer). Individual potentials are non-compensable (Steps 2-3). Therefore all individual potentials must be realized for global potential to be realized. Global FP-lower implies pointwise FP-lower: $S(f) = $ self-consistent value at every $f$.

Combined with FP-upper ($S(f)$ cannot exceed the self-consistent value), the local memory sum is exactly self-consistent at each element.

### Consequence (HV-conditional)

Pointwise $S(f) = \rho(f)\cdot\exp(-\beta)$ implies pointwise $N_\text{past}(f) = \beta$. Combined with the self-consistency condition $\rho\cdot V_\text{interval} = \beta$, this forces $V_\text{interval}(f)$ to be constant across the structure. A $d=4$ Lorentzian spacetime with everywhere-constant causal interval volume is flat ($R=0$). This consequence requires the geometric identification of $V_\text{interval}$ with the embedding manifold's causal interval volume — which is what the Hauptvermutung establishes.

**The argument does not prove HV. It constrains what HV must produce:** the only geometry compatible with V4's memory structure is flat Minkowski spacetime.

### Significance

This establishes that a global self-consistency condition on a memory-equipped causal set descends to local conditions at each element, using only the pair-specificity of the exponential kernel and the structural element-specificity of memory realization. This is a general result about memory-equipped causal sets.

The key advance over a naive ergodic argument: the ergodic argument requires large $N$ per causal interval (fails at $N \approx \beta = 2\pi \approx 6$, where Poisson fluctuations are ~40%). The memory completeness argument is scale-independent — it holds at every element regardless of how many elements are in its causal past.

### Import Risk

Low. Uses A3's composable structure and the derived two-observer distinction. Does not use $\rho = 24/\pi$ or HV.

---

## The Fluctuation Prediction

V4's self-consistency condition gives $\rho \cdot V_\text{diamond} = 1$ exactly (unit density: one element per causal diamond on average). Poisson fluctuations at $N = 1$ give 100% relative fluctuations at the single-diamond (Planck) scale.

At the scale of $k$ memory cycles ($k \cdot \beta$ elements):

$$\frac{\delta g}{g} \sim \frac{1}{\sqrt{k\beta}} = \frac{1}{\sqrt{2\pi k}}$$

This is a specific, computable prediction. Standard CST does not make this prediction because it does not derive $\rho$ from first principles. V4 derives $\rho = 24/\pi$ from self-consistency (HV-conditional), which fixes the fluctuation amplitude at all scales.

At macroscopic scales ($k \gg 1$), fluctuations are suppressed as $1/\sqrt{k}$ — statistical flatness is recovered.

---

## What the Review Should Assess

For **Result 1**: Is the proof correct? Is the result known in the CST literature? (We believe it is not, but are uncertain.) Does the structural cancellation — weights $\{1, \tfrac{1}{2}, -\tfrac{3}{2}\}$ summing to zero — have a known interpretation?

For **Result 2**: Is the non-compensability argument for the exponential kernel sound? Does the two-observer distinction (Logos vs. inside observer) constitute a genuine structural feature or a notational convenience? Is the conclusion — that global self-consistency implies pointwise self-consistency for memory-equipped causal sets — consistent with known results in the causal set literature?

For the **fluctuation prediction**: Is $1/\sqrt{2\pi k}$ at $k$ memory cycles a distinguishable prediction from standard causal set phenomenology? If $\rho = 24/\pi$ is confirmed by HV, is this prediction falsifiable in principle?

---

*V4 Vision 26 · July 2026 · Earl Treloar · Logosfield / ODCCT*  
*Repository: github.com/earltreloar/Logosfield-public-evidence-*
