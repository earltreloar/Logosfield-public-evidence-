# Logosfield — Public Evidence & Reproducibility

Public research repository for the Logosfield program and its reproducibility artifacts.

This repository currently presents a **narrowed, frozen public test path** rather than a broad claim of completed discovery. The goal is to determine whether one fixed Logosfield structure can survive contact with data across multiple observables without branch-specific retuning.

## Technical entry point

For the current canonical technical summary of the model, frozen parameters, coupling interpretation, and active public test path, see [THEORY.md](THEORY.md).

## Why this repository exists

The Logosfield program explores whether a single fixed underlying structure can produce repeatable, non-random coherence across otherwise disconnected physical domains.

This repository is organized around three principles:

1. **Freeze the core**
2. **Test with public data**
3. **Prune failed branches instead of rescuing them**

The current public emphasis is therefore on the strongest surviving reproducible path, not on maximizing the number of claimed mechanisms.

---

## Current model stance

### Minimal GR
General Relativity is kept in its minimal Einstein–Hilbert form.

- No `f(Phi) R`
- No `xi Phi^2 R`
- No conformal or disformal metric dressing

### Standard Model preserved
Standard Model operator content is left intact. Logosfield enters, if enabled, only through universal effective dressings.

### Logosfield identity
The current working reduction treats the Logosfield as an effective scalar sector `Phi` with a retarded exponential memory kernel and locked core parameters:

- `alpha = 1`
- `beta ~= 2 pi`
- `gamma = 0.005`

These locked core parameters are part of the public freeze policy and are not retuned per mechanism.

---

## Frozen EFT completion (public working form)

This repository uses a minimal EFT-style completion whose purpose is to make “couples to the four forces” explicit in a conservative and attackable way while avoiding parameter sprawl.

### Interaction sector
Only two universal coefficients are admitted in the current public EFT layer:

- `c_g`
- `c_y`

Universal dressing functions:

- `Z(Phi) = 1 + c_g * Phi / M_Pl`
- `Y(Phi) = 1 + c_y * Phi / M_Pl`

Interpretation:

- Gauge-sector response is carried through `Z(Phi)`
- Yukawa / mass-sector response is carried through `Y(Phi)`

### Important public caution
The current narrowed cosmology path does **not** yet separately measure `c_g` and `c_y`.

At present, the public two-test path only constrains an **effective cosmology response combination**, not fully separated couplings.

That effective response should be treated operationally as something like:

- `epsilon_g = c_g * Phi_ref / M_Pl`
- `epsilon_y = c_y * Phi_ref / M_Pl`
- `epsilon_C = A_g * epsilon_g + A_y * epsilon_y`

where only the downstream effective cosmology response is presently constrained in the public path.

---

## Freeze policy

This repository is only credible if coupling freedom remains minimal and global.

The public freeze rules are:

- only two EFT coefficients are admitted in the current layer: `c_g` and `c_y`
- universality is enforced
- no split coefficients by gauge group
- no per-fermion Yukawa coefficients
- no branch-specific rescue parameters
- fit once or bound once, then freeze globally
- if a branch fails under the frozen public structure, it is demoted rather than patched ad hoc

---

## Legacy compatibility

All previously released legacy mechanisms remain preserved under the default legacy setting:

- `c_g = 0`
- `c_y = 0`

This means:

- legacy results remain legacy results
- nonzero EFT-mode couplings must be labeled explicitly
- legacy success does **not** automatically validate later nonzero-coupling claims

---

## Current verified public path

The repository currently maintains a **frozen two-test public path**.

### Active Test 1
**CDDR diagnostic**  
Distance-duality / Etherington-style diagnostic used as the current anchor branch.

### Active Test 2
**Mechanism 16 sigma8 response**  
Treated only as a child branch of the same cosmology path.

### Public status
- CDDR: provisional pass
- Mechanism 16: provisional pass under the patched weak-response default
- Direct force branches: not current flagship claims
- Mechanism 17: under review / not part of the frozen public path
- SMBH feasibility: separate lane unless a shared bridge is explicitly derived and survives

---

## What is not currently being claimed

This repository does **not** currently claim:

- confirmed new-force discovery
- completed fifth-force validation
- separated empirical measurement of `c_g` and `c_y`
- a validated direct rotation-curve force detection
- a validated universal bridge from the current CDDR path into every other mechanism

This repository should be read as a **narrowed candidate-framework and reproducibility program**, not a completed coronation of the theory.

---

## Reproducibility

The current public reproduction priority is the frozen two-test path only.

### Run CDDR
```bash
python run.py --mode cddr


python run.py --mode mech16
