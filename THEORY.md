# THEORY.md

## Logosfield: current public technical summary

The Logosfield is currently presented in this repository as a **minimal GR-compatible effective sector** intended to test whether one fixed underlying structure can produce repeatable, non-random signals across multiple observables without branch-specific retuning.

This repository does **not** currently present Logosfield as a completed discovery claim. It presents a **frozen candidate framework** with a narrowed public test path.

---

## 1. Core model stance

### General Relativity
General Relativity is kept in minimal Einstein–Hilbert form.

- no `f(Phi) R`
- no `xi Phi^2 R`
- no conformal/disformal metric dressing in the current public form

### Standard Model
Standard Model operator content is preserved.

The public EFT layer does not replace the Standard Model. It adds only minimal universal dressing functions.

---

## 2. Logosfield working reduction

The current working reduction treats the Logosfield as an effective scalar sector `Phi` with a retarded exponential memory structure and locked core parameters:

- `alpha = 1`
- `beta ~= 2 pi`
- `gamma = 0.005`

These parameters are frozen in the current public path and are not retuned per mechanism.

---

## 3. Minimal EFT completion

The current public EFT layer admits only two universal coefficients:

- `c_g`
- `c_y`

with universal dressing functions

- `Z(Phi) = 1 + c_g * Phi / M_Pl`
- `Y(Phi) = 1 + c_y * Phi / M_Pl`

Interpretation:

- `Z(Phi)` carries gauge-sector response
- `Y(Phi)` carries Yukawa / mass-sector response

The purpose of this layer is to make the coupling structure explicit while avoiding parameter sprawl.

---

## 4. What is actually constrained in the current public path

The current narrowed public test path does **not** yet empirically separate `c_g` and `c_y`.

Instead, it should be interpreted as constraining an **effective cosmology response combination**, for example:

- `epsilon_g = c_g * Phi_ref / M_Pl`
- `epsilon_y = c_y * Phi_ref / M_Pl`
- `epsilon_C = A_g * epsilon_g + A_y * epsilon_y`

Only this downstream effective response is currently constrained by the active public path.

---

## 5. Freeze policy

The current public framework uses these rules:

- only two EFT coefficients are admitted: `c_g`, `c_y`
- universality is enforced
- no branch-specific rescue coefficients
- fit once or bound once, then freeze globally
- failed branches are demoted rather than patched ad hoc

Legacy results remain legacy results under:

- `c_g = 0`
- `c_y = 0`

Nonzero EFT-mode claims must therefore be interpreted separately from legacy-mode results.

---

## 6. Active public test path

The current public path is intentionally narrow.

### Test 1: CDDR
Distance-duality / Etherington-style diagnostic used as the current anchor branch.

### Test 2: Mechanism 16
Sigma8 response treated only as a child branch of the same frozen cosmology path.

These are the only currently active public tests in the minimal locked path.

---

## 7. What is not currently being claimed

This repository does **not** currently claim:

- confirmed new-force discovery
- validated fifth-force detection
- validated direct rotation-curve force signal
- separate empirical measurement of `c_g` and `c_y`
- universal successful bridge from the active path into every other mechanism

Other mechanisms may remain scientifically relevant, but they are not all part of the current locked public challenge path.

---

## 8. How to navigate the repo

Main theory and reproduction entry points:

- `README.md` — public project overview
- `CHALLENGE.md` — active replication challenge
- `REPRODUCE.md` — reproduction instructions
- `Cosmology` — cosmology-side structure
- `EFT couplings` — coupling definitions and current EFT stance
- `run.py` — public runner
- `tools/cddr_runner_fullcov.py` — CDDR runner
- `Mechanism16/` — current child-branch implementation

Historical or broader materials remain part of the project record but are not all equal in current evidentiary status.

---

## 9. Current public posture

The repository’s current public posture is:

- freeze the core
- keep the path narrow
- prioritize reproducibility
- demote overstated branches
- only build outward from tests that survive under the same fixed structure

This file should be read as the canonical technical snapshot of the current public Logosfield path.
