# Logosfield / ODCCT — V3 Reproducibility Archive: Active Mechanisms, Suspended Cosmology Tests, and Gap Tracking

Public research repository for the Logosfield / ODCCT program and its reproducibility artifacts.

This repository presents a **Level 2 theoretical framework** — internally consistent, recovering known physics in its conservative limit, not independently replicated — with explicit gap tracking and honest classification of every claim. It is not presented as a completed discovery.

## V3 claim boundary

Under V3, this framework currently claims **structural consistency and constrained coupling behavior**, not empirical confirmation of a new field or force. Every public test below is classified by whether it survives the V3 coupling correction (see "What changed from V2"). CDDR and the sigma8 prediction do not currently survive as active predictions, because the cosmological reference value `Phi_ref` they require is not derived (Gap 8, open). This is a property of the current theory, not a temporary omission — see "Active vs. suspended test paths" immediately below for the full picture at a glance.

## Active vs. suspended test paths

| Path | Status | Why |
|---|---|---|
| Force Coupling Table (EM, gravity, weak) | Active — structural result | Independent of `Phi_ref`; derived from symmetry |
| Cassini / alpha-variation margins (Gap 3) | Active — constraint check | Survives conformal protection; large margin |
| Mechanism 15 (Ly-alpha escape, z=13) | Active / exploratory | See `Mechanism15/README.md` — flags a superseded mechanism description pending rederivation |
| Mechanism 17 (H0 reconciliation) | Active / under review | See `Mechanism17/README.md` — not part of the locked challenge path |
| CDDR (distance duality) | **Suspended** | Requires non-zero `Phi_ref`, not yet derived (Gap 8) |
| Mechanism 16 (sigma8 response) | **Suspended** | Relied on removed V2 linear EFT completion; no V3-consistent rederivation yet |
| Mechanism 21 (SMBH seeding/damping) | **Open / diagnostic** | High-z SMBH growth remains a target tension zone; prior relief tests were distribution-sensitive and do not yet constitute an active V3 prediction. Needs an explicit V3-compatible rerun using the frozen parameters and corrected coupling form before it can be called active. |

These branches are suspended because the corrected theory removes the mechanism that generated their previous signal. **They are not failures of the entire framework; they are failures of a now-retracted completion.**

## Technical entry point

For the canonical technical summary — the memory-covariant derivative, parameter status, Force Coupling Table, conformal protection, and which predictions are currently suspended — see [00_THEORY.md](00_THEORY.md).

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
SM operator content is preserved. The Logosfield enters only through the memory-covariant derivative `D_mem,mu`, with each sector's coupling fixed by that sector's own symmetry (see Force Coupling Table in 00_THEORY.md) — not through an independently free EFT layer.

### Parameters

| Parameter | Value | Status |
|---|---|---|
| `alpha` | 1 | Postulated |
| `beta` | `2*pi` | IDENTIFIED (Matsubara lead), not derived |
| `gamma` | `~0.003122` | IDENTIFIED (baryogenesis line + Matsubara), not derived |

The model has a frozen three-parameter structural core. These parameters are not retuned per mechanism. Current work tests whether that frozen core remains consistent across domains; first-principles derivation of `alpha`, `beta`, and `gamma` remains an open problem (Gap 4) and should not be described as solved.

**Note:** the parameter values changed from the V2 working values (`gamma = 0.005`) after a systematic consistency pass against the framework's surviving closed structural constraints. The new pair was checked against every closed result in the framework (Cassini, alpha variation, baryogenesis, conformal protection) and preserves every margin. Full reasoning is in 00_THEORY.md Section 4.

---

## What changed from V2

The previous public version of this repository used a linear EFT completion (`Z(Phi) = 1 + c_g*Phi/M_Pl`, `Y(Phi) = 1 + c_y*Phi/M_Pl`). That completion has been **removed**: an internal audit found an eight-order-of-magnitude conflict with precision measurements. It has been replaced by a **derived, conformally-protected** coupling form:

```
f(Phi/M_Pl) = g(Phi/M_Pl) = h(Phi/M_Pl) = 1 + O(gamma) * (Phi/M_Pl)^2
```

This is quadratic in `Phi/M_Pl`, not linear, and follows from conformal weight counting plus a Z_2 symmetry inherent to the memory kernel's bilinear structure — it is not an independently free EFT layer with fitted coefficients.

**Direct consequence:** the CDDR and Mechanism 16 (sigma8) formulas published under V2 depended on the now-removed linear completion and no longer apply as written. These predictions are now correctly labeled **SUSPENDED**, not "provisional pass." See the status table above.

---

## Force Coupling Table

| Sector | Result | Status |
|---|---|---|
| EM | `gamma_EM = 0` exactly | DERIVED (U(1) conformal invariance) |
| Gravity | `gamma_g -> 0` | DERIVED (diffeomorphism invariance) |
| Weak | `gamma_weak ~ 408` at 1 fm | DERIVED (Proca propagator, 0.12% match) |
| Strong | sign only (asymptotic freedom) | IDENTIFIED (sign) + OPEN (magnitude) |

The strong-sector magnitude was previously mislabeled DERIVED in V2. Corrected here — see 00_THEORY.md Section 5 for why the weak-sector formula is a category mismatch for the confining strong sector. This table is also reproduced in `00_THEORY.md` and `06_CHALLENGE.md` (where its weak-sector entry is an active challenge target).

---

## Freeze and honesty policy

- Core structural parameters (`alpha`, `beta`, `gamma`) are frozen at the values in 00_THEORY.md Section 4 and are not retuned per mechanism.
- Every claim is labeled DERIVED / IDENTIFIED / SPECULATIVE / SUSPENDED / OPEN / RULED OUT.
- Errors and retractions are documented explicitly in 00_THEORY.md rather than silently corrected.
- Negative results (ruled-out derivation attempts) are recorded on the same footing as positive ones.
- If a branch fails or becomes suspended under the frozen structure, it is labeled as such rather than patched ad hoc.

---

## What is not currently being claimed

This repository does **not** currently claim:

- a first-principles derivation of `alpha`, `beta`, or `gamma`
- confirmed new-force discovery or a validated fifth-force detection
- a working CDDR or sigma8 prediction (suspended, see status table above)
- a validated SMBH seeding/damping signature (open/diagnostic, see status table above)
- independent replication by any party outside this project

This repository should be read as a narrowed, honestly-labeled candidate framework and reproducibility program.

---

## Reproducibility

See [07_REPRODUCE.md](07_REPRODUCE.md) for current reproduction status. Because CDDR and Mechanism 16 are suspended, their runners remain in the repository for historical reference but are not currently part of an active validated public test path.

## Repository layout

- `00_THEORY.md` — canonical technical summary (start here)
- `06_CHALLENGE.md` — replication challenge, updated for V3 status
- `07_REPRODUCE.md` — reproduction instructions
- `08_CITATIONS.md` — how to cite this work
- `05_Cosmology.md`, `04_EFT_couplings.md`, `03_ZPhi_Summary.md` — sector-specific technical detail
- `Mechanism15/`, `Mechanism16/`, `Mechanism17/` — individual mechanism implementations
- `Mechanism21_SMBH_Seeding_Damping/` — SMBH seeding/damping exploration; status: open/diagnostic, see table above
- `Mechanism25-BaryonAsymmetry` — baryon asymmetry exploration; status not yet formally classified under V3
- `archive/` — historical record, including the V2 master archive index and pre-freeze mechanisms; not current evidentiary status
- `manuscript/` — *The Remembering Cosmos*, the originating manuscript

## License

See [LICENSE](LICENSE).
