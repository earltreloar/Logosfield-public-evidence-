# 00_THEORY.md — Redirected to V4

> **This file documents V3 theory (superseded). The current framework is V4.**
> See `/V4/Logosfield_V4_Vision_17_Final_Q4b_Baryon.docx` for the current master document.
> See `README.md` for the current program overview.

The V3 technical summary below is preserved as historical record only.
All V3 results are superseded by V4. V4 is a genuinely pregeometric framework —
it does not presuppose the spacetime and gauge structure it claims to generate.

---

## V3 Technical Summary (Historical — Superseded)

# 00_THEORY.md

## Logosfield / ODCCT: current public technical summary (V3 Canonical)

The Logosfield is presented in this repository as a **non-local scalar field framework** built around a memory-covariant derivative, intended to test whether one fixed underlying structure can produce repeatable, non-random signals across multiple observables without branch-specific retuning.

This repository does **not** claim a completed discovery. It presents a **Level 2 framework** — internally consistent, recovering known physics in the conservative limit, not independently replicated — with explicit gap tracking and honest classification of every result as DERIVED, IDENTIFIED, SPECULATIVE, SUSPENDED, OPEN, or RULED OUT.

---

## 1. Core model stance

### General Relativity
General Relativity's gravitational sector is **minimal Horndeski**, derived (not assumed) from diffeomorphism invariance:

```
G2 = X - V(Phi)
G3 = 0
G4 = M_Pl^2 / 2   (constant)
G5 = 0
```

This forces `c_T = c` exactly. GW170817 is satisfied automatically. [DERIVED — Gap 7, CLOSED]

### Standard Model
Standard Model operator content is preserved. The Logosfield enters only through the memory-covariant derivative acting on matter fields, with couplings determined by each sector's own symmetry — not through an independent free EFT layer.

---

## 2. The memory-covariant derivative

```
D_mem,mu psi(x) = integral_{M^-(x)} K(x,x'; beta,gamma) * U(x,x') * D_mu' psi(x') sqrt(-g') d^4x'
K(tau) = gamma * beta * exp(-beta*tau) * Theta(tau)
```

- `M^-(x)`: causal past of x
- `U(x,x')`: parallel transport / Wilson line
- Conservative limit: `gamma -> 0` recovers the standard covariant derivative `D_mu` exactly.

### Auxiliary field origin (Gap 10) [DERIVED, numerically verified]

The kernel is not postulated in isolation. It follows from integrating out an auxiliary field `chi`:

```
(d/dt + beta) * chi = beta * sqrt(gamma) * psi + xi(t)
```

The retarded Green's function of this equation, after integrating out `chi`, reproduces the causal kernel exactly. `gamma -> 0` is therefore a controlled decoupling limit (gamma is literally a coupling constant), not an ad hoc truncation. The same `chi`, carrying its own noise `xi`, has a stationary correlator that reproduces the symmetric kernel `K_full = gamma*beta*exp(-beta|t-t'|)` — verified numerically via Monte Carlo OU simulation. `Theta(t-t')` is inherited from the microcausality of the `chi`-`psi` embedding, not independently postulated.

An earlier hypothesis (that the symmetric kernel collapses into the causal kernel as `gamma -> 0`) was tested and found incorrect; it has been retracted. K and K_full are different objects — response function and correlation function of the same field, related by a fluctuation-dissipation relation.

---

## 3. Parameters

| Parameter | Value | Status |
|---|---|---|
| `alpha` | 1 | Postulated — not yet seriously examined |
| `beta` | `2*pi` | IDENTIFIED — Matsubara frequency lead at Planck temperature; not derived |
| `gamma` | `~0.003122` | IDENTIFIED — see Section 4 below; supersedes earlier working value of 0.005 |

None of the three core parameters has a first-principles derivation. This is the framework's most significant open problem (Gap 4 / Gap 9).

---

## 4. Parameter derivation attempts — honest status

The original working values (`gamma = 0.005`, `beta = 2*pi`, `alpha = 1`) were chosen in August 2025 to get the framework off the ground and were never derived from the framework's own structure. A systematic reverse-engineering pass was conducted to ask what the *validated* structure itself demands.

### The baryogenesis line [IDENTIFIED]

`T* = gamma/beta * M_Pl` coincides with the seesaw/leptogenesis scale `M_R ~ 1.21e15 GeV`. Requiring `T* = M_R` exactly defines a **line**, not a point: `gamma = (M_R/M_Pl) * beta`, valid for `beta` in `(0, ~14)` (from the requirement that Phi's mass stay sub-Planckian).

### Working pair ("Pair 1") — current default

Combining the baryogenesis line with the Matsubara frequency lead for `beta` (`beta = 2*pi`, the lowest non-trivial Matsubara mode at Planck temperature):

```
beta  = 2*pi       = 6.2832
gamma = (M_R/M_Pl)*beta = 0.003122
```

This gives `T*/M_R = 1.000` exactly, `m_Phi = 0.351 * M_Pl` (comfortably sub-Planckian), `c_W = 0.9832`. This pair was checked against every prior quantitative result in the framework (Gaps 3, 7, 10, 11, 12, 13) and found to preserve every margin — no qualitative result depends sensitively on the exact value of gamma. **This is the current default working pair, adopted after a full recalculation pass.**

### Second candidate pair ("Pair 2") — boundary case, also viable

An independent route applies the correct fluctuation-dissipation relation (matching spectral densities, not naive equipartition) to the auxiliary field `chi` at Planck temperature `T=1`, giving `D = 2` exactly. Combined with Gap 10's matching condition `D = 2*gamma*beta^2`, this gives `gamma = 1/beta^2` — which is algebraically equivalent to `m_Phi = M_Pl` exactly, for any `beta`. Combined with the baryogenesis line: `beta = 12.625`, `gamma = 0.00627`. This sits exactly at the boundary of EFT validity (Phi's mass exactly at the Planck mass) — a legitimate but boundary-saturating result, flagged for continued scrutiny.

### What has been ruled out

- **Naive equipartition applied to chi's relaxation equation** — incorrect, because chi's equation is first-order/dissipative with no canonical momentum; this error was caught after producing a super-Planckian (`m_Phi = 6.7 * M_Pl`) and therefore unphysical pair.
- **Joint loop-factor self-consistency** (tree-level mass = one-loop correction) — shown to require either `beta = 0.5` or `gamma = 8*pi^2`, neither of which matches the framework. Structurally unresolvable by loop calculation.
- **Strong-CP suppression via kernel-topology overlap (Route 3)** — the kernel operates at the Planck scale while QCD topology operates at the confinement scale, a 19-order-of-magnitude mismatch. The actual kernel-topology overlap gives negligible suppression; the specific mechanism does not work with current parameters.
- **`c_W` self-consistency as an independent constraint (Path 4)** — ruled out for a structural reason: `c_W` is derived entirely from `T* = gamma/beta`, so it can only ever constrain the ratio, never gamma and beta separately. Not merely unexplored — shown not to work.
- **"Self-bounding closure" claiming `beta ~ 2*pi` from internal consistency alone** — proposed externally, not yet accepted. The risk is circularity: `beta = 2*pi` was the original input assumption throughout the framework's history, and a calculation that reproduces it from a closure condition built around the same topological factor may simply be rediscovering its own input. Pending an explicit, fully shown coarse-graining calculation.

---

## 5. Force Coupling Table

The framework's central claim is that the four forces are not separately glued onto the Logosfield substrate, but emerge as symmetry-filtered branchings from the same `D_mem` structure, with each sector's memory coupling fixed by that sector's own symmetry — not by fitting.

| Sector | Coupling | Status |
|---|---|---|
| Electromagnetism | `gamma_EM = 0` exactly | DERIVED — U(1) conformal invariance |
| Gravity | `gamma_g -> 0` | DERIVED — diffeomorphism invariance (Gap 7) |
| Weak | `gamma_weak ~ 408` at 1 fm | DERIVED — Proca propagator formula `gamma(r) = M*r`, matches M_W*r to 0.12% |
| Strong | sign: negative beta function (asymptotic freedom) | IDENTIFIED (sign) + OPEN (magnitude at Lambda_QCD) |

The strong-sector entry was previously mislabeled DERIVED in earlier versions of this repository. Only the *sign* of the running (asymptotic freedom) is derived; the *magnitude* at the confinement scale is not, because the `gamma(r)=M*r` formula is a category mismatch for a confining (non-Yukawa) potential. This has been corrected.

---

## 6. Conformal protection [DERIVED]

Conformal weight counting forces:

```
f(Phi/M_Pl) = 1 + O(gamma) * (Phi/M_Pl)^2     [gauge kinetic sector]
g(Phi/M_Pl) = 1 + O(gamma) * (Phi/M_Pl)^2     [Yukawa sector, above EW scale]
h(Phi/M_Pl) = 1 + O(gamma) * (Phi/M_Pl)^2     [below EW scale]
```

This **supersedes** the earlier `Z(Phi) = 1 + c_g*Phi/M_Pl`, `Y(Phi) = 1 + c_y*Phi/M_Pl` linear EFT completion used in V2 of this repository. That linear completion was removed after an audit found an eight-order-of-magnitude conflict with precision electroweak/equivalence-principle measurements. The corrected, conformally-protected form is quadratic in `Phi/M_Pl`, not linear — this follows from a Z_2 symmetry (`Phi -> -Phi`) identified in `D_mem`'s bilinear coupling structure (the kernel always couples `Phi(t)*K*Phi(t')`, which is automatically even).

The quadratic form, combined with the small value of gamma, gives enormous observational margins (50+ orders of magnitude on Cassini PPN-gamma and laboratory alpha-variation bounds) rather than a near-miss. See Section 7.

---

## 7. Gap 3 — Cassini / alpha variation [DERIVED, CLOSED]

```
delta_alpha/alpha = gamma * (t_Pl/t_Hub)^2 / beta^2   ~  1.2e-126   (bound: 1e-9;  margin ~8e116)
delta_gamma_PPN    = gamma * (t_Pl/t_Hub)   / beta     ~  6.2e-65   (bound: 2.3e-5; margin ~4e59)
```

Both spatial alpha variation (zero, from translation invariance of the pure kernel) and the Cassini PPN-gamma bound are satisfied with structural headroom, not fine-tuning. Values shown at the current default pair (Section 4).

---

## 8. Gap 12 — Baryogenesis / Weinberg operator [substantially closed]

```
c_W = 1 - C2 * alpha_2(T*) = 0.9832     [DERIVED — Polyakov loop argument]
```

`T* = M_R` exactly (by construction of the default working pair). The Davidson-Ibarra bound is satisfied with a margin of roughly 180,000x. This is **consistency with** standard leptogenesis given external Yukawa inputs, not an independent derivation of the baryon asymmetry — the framework does not derive the required CP-violating phase from first principles.

---

## 9. V(Phi) — the scalar potential [DERIVED + IDENTIFIED]

```
V(Phi) = (1/2) * gamma * beta^2 * Phi^2 + (gamma^2 / 16*pi^2) * Phi^4
```

The quartic term's coefficient is conformally invariant (the unique conformally-invariant potential term in 4D); the quadratic term is the minimal conformal-symmetry-breaking term, motivated by a Z_2 symmetry inherited from `D_mem`'s bilinear structure (not an external assumption). The mass term comes from integrating out the chi portal: `m_Phi = beta*sqrt(gamma)*M_Pl`.

`V(Phi)` has its minimum at `Phi = 0` (no spontaneous symmetry breaking). This is consistent with every closed gap above. It means `Phi_ref` (the reference value used in the conformal-protection corrections) is not fixed by `V(Phi)` alone — it would require a cosmological initial condition external to the potential. This is Gap 8, and it remains open. Gap 8 is **not blocking** for any of the closed results above; it only matters for the suspended predictions below.

---

## 10. Suspended predictions — CDDR, sigma8, galaxy rotation

CDDR (Etherington distance-duality) and the Mechanism 16 sigma8 response were previously reported in this repository as "provisional pass" results, computed using the now-superseded linear `Z(Phi)/Y(Phi)` EFT completion. That completion has been removed (Section 6). The replacement, conformally-protected coupling form gives a *quadratic*, not linear, dependence on `Phi/M_Pl` — meaning the original CDDR and sigma8 formulas in this repository no longer apply as written.

More fundamentally: these predictions require `Phi != 0` in some cosmological background to produce any observable signal at all, since `f = g = h = 1` exactly at `Phi = 0`. Section 9 shows `V(Phi)`'s classical minimum is at `Phi = 0`, and `Phi_ref` is not yet derived (Gap 8). **CDDR, the sigma8 response, and the galaxy-rotation mechanism are therefore SUSPENDED, not provisionally passing**, pending resolution of Gap 8. This is a correction from earlier versions of this repository.

---

## 11. What is not currently being claimed

This repository does **not** currently claim:

- a completed derivation of `alpha`, `beta`, or `gamma`
- confirmed new-force discovery
- a validated fifth-force or direct rotation-curve detection
- a working CDDR or sigma8 prediction (see Section 10 — suspended)
- independent replication of any result by a party outside this project

---

## 12. How to navigate the repo

- `README.md` — project overview
- `06_CHALLENGE.md` — active replication challenge
- `07_REPRODUCE.md` — reproduction instructions
- `05_Cosmology.md` — cosmology-sector structure (now reflecting suspended status)
- `04_EFT_couplings.md` — coupling definitions, V3 conformal-protection form
- `03_ZPhi_Summary.md` — compact technical summary
- `Mechanism15/`, `Mechanism16/`, `Mechanism17/` — individual mechanism implementations (status varies; see each README)
- `archive/pre_freeze/` — historical record, not current evidentiary status

---

## 13. Current public posture

- freeze the core structure, keep gap tracking explicit
- label every result DERIVED / IDENTIFIED / SPECULATIVE / SUSPENDED / OPEN / RULED OUT
- document errors and retractions explicitly rather than silently correcting them
- prioritize honest negative results (ruled-out paths) on the same footing as positive ones
- do not claim more than what survives scrutiny

This file is the canonical technical snapshot of the current public Logosfield/ODCCT path (V3).
