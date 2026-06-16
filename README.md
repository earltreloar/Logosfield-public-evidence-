# Logosfield / ODCCT — Public Evidence & Reproducibility (V3)

Public research repository for the Logosfield / ODCCT program and its reproducibility artifacts.

This repository presents a **Level 2 theoretical framework** — internally consistent, recovering known physics in its conservative limit, not independently replicated — with explicit gap tracking and honest classification of every claim. It is not presented as a completed discovery.

## Technical entry point

For the canonical technical summary — the memory-covariant derivative, parameter status, Force Coupling Table, conformal protection, and which predictions are currently suspended — see [THEORY.md](THEORY.md).

## Why this repository exists

The Logosfield/ODCCT program explores whether a single non-local scalar field structure, built around a memory-covariant derivative, can produce repeatable signals across multiple physical domains without retuning per domain. The program is organized around three principles:

1. **Freeze the structural core; track gaps explicitly**
2. **Test against public data wherever possible**
3. **Demote or suspend failed/incomplete branches rather than patching them ad hoc**

---

## Current model stance (V3)

### Gravity
General Relativity's gravitational sector is **derived as minimal Horndeski** from diffeomorphism invariance:

```
G2 = X - V(Phi),  G3 = 0,  G4 = M_Pl^2/2 (constant),  G5 = 0
```

`c_T = c` exactly. GW170817 is satisfied automatically. [DERIVED]

### Standard Model
SM operator content is preserved. The Logosfield enters only through the memory-covariant derivative `D_mem,mu`, with each sector's coupling fixed by that sector's own symmetry (see Force Coupling Table in THEORY.md) — not through an independently free EFT layer.

### Parameters

| Parameter | Value | Status |
|---|---|---|
| `alpha` | 1 | Postulated |
| `beta` | `2*pi` | IDENTIFIED (Matsubara lead), not derived |
| `gamma` | `~0.003122` | IDENTIFIED (baryogenesis line + Matsubara), not derived |

**Note:** the parameter values changed from the V2 working values (`gamma = 0.005`) after a systematic reverse-engineering pass against the framework's own validated structure. The new pair was checked against every closed result in the framework (Cassini, alpha variation, baryogenesis, conformal protection) and preserves every margin. Full reasoning is in THEORY.md Section 4.

---

## What changed from V2

The previous public version of this repository used a linear EFT completion (`Z(Phi) = 1 + c_g*Phi/M_Pl`, `Y(Phi) = 1 + c_y*Phi/M_Pl`). That completion has been **removed**: an internal audit found an eight-order-of-magnitude conflict with precision measurements. It has been replaced by a **derived, conformally-protected** coupling form:

```
f(Phi/M_Pl) = g(Phi/M_Pl) = h(Phi/M_Pl) = 1 + O(gamma) * (Phi/M_Pl)^2
```

This is quadratic in `Phi/M_Pl`, not linear, and follows from conformal weight counting plus a Z_2 symmetry inherent to the memory kernel's bilinear structure — it is not an independently free EFT layer with fitted coefficients.

**Direct consequence:** the CDDR and Mechanism 16 (sigma8) formulas published under V2 depended on the now-removed linear completion and no longer apply as written. These predictions are now correctly labeled **SUSPENDED**, not "provisional pass." See "Current status of public tests" below.

---

## Force Coupling Table

| Sector | Result | Status |
|---|---|---|
| EM | `gamma_EM = 0` exactly | DERIVED (U(1) conformal invariance) |
| Gravity | `gamma_g -> 0` | DERIVED (diffeomorphism invariance) |
| Weak | `gamma_weak ~ 408` at 1 fm | DERIVED (Proca propagator, 0.12% match) |
| Strong | sign only (asymptotic freedom) | IDENTIFIED (sign) + OPEN (magnitude) |

The strong-sector magnitude was previously mislabeled DERIVED in V2. Corrected here — see THEORY.md Section 5 for why the weak-sector formula is a category mismatch for the confining strong sector.

---

## Current status of public tests

### CDDR and Mechanism 16 (sigma8) — SUSPENDED

These predictions require `Phi != 0` in some cosmological background to produce any observable signal (the corrected couplings give `f=g=h=1` exactly at `Phi=0`). The scalar potential `V(Phi)` has been derived and its classical minimum is at `Phi=0` — meaning the reference value `Phi_ref` needed for these predictions is not determined by the framework alone and requires an external cosmological input not yet derived (Gap 8). **These tests are suspended pending that derivation**, not passing under a provisional formula. This is a correction from the V2 state of this repository, which reported "provisional pass" using formulas tied to the now-removed linear EFT completion.

### What remains active

- The structural results in the Force Coupling Table (EM, gravity, weak) and the Cassini/alpha-variation margins (Gap 3) hold independent of `Phi_ref` and are not affected by the suspension above.
- Mechanism-specific files (`Mechanism15/`, `Mechanism17/`) retain their own independent status; see each mechanism's README.

---

## Freeze and honesty policy

- Core structural parameters (`alpha`, `beta`, `gamma`) are frozen at the values in THEORY.md Section 4 and are not retuned per mechanism.
- Every claim is labeled DERIVED / IDENTIFIED / SPECULATIVE / SUSPENDED / OPEN / RULED OUT.
- Errors and retractions are documented explicitly in THEORY.md rather than silently corrected.
- Negative results (ruled-out derivation attempts) are recorded on the same footing as positive ones.
- If a branch fails or becomes suspended under the frozen structure, it is labeled as such rather than patched ad hoc.

---

## What is not currently being claimed

This repository does **not** currently claim:

- a first-principles derivation of `alpha`, `beta`, or `gamma`
- confirmed new-force discovery or a validated fifth-force detection
- a working CDDR or sigma8 prediction (suspended, see above)
- independent replication by any party outside this project

This repository should be read as a narrowed, honestly-labeled candidate framework and reproducibility program.

---

## Reproducibility

See [REPRODUCE.md](REPRODUCE.md) for current reproduction status. Because CDDR and Mechanism 16 are suspended, their runners remain in the repository for historical reference but are not currently part of an active validated public test path.

## Repository layout

- `THEORY.md` — canonical technical summary (start here)
- `CHALLENGE.md` — replication challenge, updated for V3 status
- `REPRODUCE.md` — reproduction instructions
- `CITATIONS.md` — how to cite this work
- `Cosmology`, `EFT couplings`, `ZPhi_Summary.md` — sector-specific technical detail
- `Mechanism15/`, `Mechanism16/`, `Mechanism17/` — individual mechanism implementations
- `archive_pre_freeze/` — historical record, not current evidentiary status
- `manuscript/` — *The Remembering Cosmos*, the originating manuscript

## License

See [LICENSE](LICENSE).
