# Reproduce the Logosfield/ODCCT Public Path — V3
# Last updated: V3 update

This repository's previous (V2) reproduction path centered on CDDR and Mechanism 16 (sigma8). **Both are now suspended** (see `THEORY.md` Section 10 and `Cosmology.md`) because they depended on a linear EFT completion that has since been removed for conflicting with precision measurements.

This does not mean there is nothing to reproduce. It means the reproduction priority has shifted to the framework's closed structural results, which do not depend on the suspended cosmology layer.

---

## What you can currently reproduce

### 1. Weak-sector Force Coupling Table check

Verify `gamma(r) = M*r` gives `gamma_weak ~ 408` at `r = 1 fm`:

```python
M_W = 80.4       # GeV
hbar_c = 0.1973  # GeV*fm
r_fm = 1.0
gamma_weak = M_W * (r_fm / hbar_c)
print(gamma_weak)  # expect ~407.5
```

### 2. Gap 3 — Cassini / alpha variation margins

See `tools/cddr_runner_fullcov.py` for the historical CDDR runner (now superseded — retained for reference). A standalone margin-check script for Gap 3 is planned; in the meantime the formulas are given explicitly in `THEORY.md` Section 7 and can be reproduced directly:

```
delta_alpha/alpha = gamma * (t_Pl/t_Hub)^2 / beta^2
delta_gamma_PPN    = gamma * (t_Pl/t_Hub)   / beta
```

with `gamma = 0.003122`, `beta = 2*pi` (current default parameters, `THEORY.md` Section 4).

### 3. Gap 10 — auxiliary field kernel verification

The Ornstein-Uhlenbeck Monte Carlo check (causal kernel response vs. symmetric kernel correlator matching) referenced in `THEORY.md` Section 2 can be reproduced with a standard OU-process simulation at `beta=2*pi`, `gamma=0.003122` (or the original `gamma=0.005` used in the initial check) and comparing the simulated stationary autocorrelation against `K_full(tau) = gamma*beta*exp(-beta*tau)`.

---

## Historical (suspended) reproduction commands — retained for reference only

```bash
python run.py --mode cddr     # SUSPENDED — uses removed linear EFT completion
python run.py --mode mech16   # SUSPENDED — uses removed linear EFT completion
```

These commands still execute against the historical formulas in `Cosmology.md` but do **not** represent a current, active prediction of the V3 framework. Results from these runners should not be cited as validating or testing the current framework without first confirming whether the linear-completion-dependent formulas have been superseded by a V3-consistent rederivation (not yet available).

---

## Requirements

- Python 3.10+
- NumPy, Pandas, Matplotlib

## Status summary

| Test | V2 status | V3 status |
|---|---|---|
| CDDR | provisional pass | SUSPENDED (Gap 8) |
| Mechanism 16 (sigma8) | provisional pass | SUSPENDED (Gap 8) |
| Weak-sector coupling formula | not previously tested | reproducible, DERIVED |
| Gap 3 margins | present, different parameter pair | reproducible, DERIVED, margins improve under V3 parameters |
| Gap 10 kernel verification | not previously documented | reproducible, DERIVED |
