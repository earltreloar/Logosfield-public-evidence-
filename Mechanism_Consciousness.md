# Mechanism — Consciousness Domain (V2 Canonical)
# Point 1 — Logosfield / ODCCT Framework
# Last updated: May 29, 2026
# Status: Formally developed; F_self not yet computable; psychedelic extension directional only

---

## Core Model

```
R = gamma * F_omega * N_eff * F_self
```

where:
- **R**: conscious integration measure
- **gamma = 0.005**: memory coupling (frozen, same as all sectors)
- **F_omega**: frequency-domain memory efficiency
- **N_eff**: effective spatial integration (architecture-dependent)
- **F_self**: self-referential modeling capacity

### F_omega (universal)

```
F_omega = beta^2 / (beta^2 + 1) ~= 0.975
```

Universal across sectors. Does not vary per mechanism.

### N_eff (spatial architecture)

```
N_eff = (L / r_coh) * f_sync
```

- L: characteristic system size
- r_coh = 4.43 cm (neural sector, 40 Hz)
- f_sync: synchronization fraction of active neural volume

### F_self (self-referential modeling)

```
F_self = lambda_N * lambda_G * lambda_T
```

- lambda_N: NMDA receptor gate (-> 0 under ketamine)
- lambda_G: GABAergic gate (-> 0 under propofol)
- lambda_T: Thalamic broadcast gate (-> 0 under dexmedetomidine)

F_self in [0,1]. Not yet formally computable from first principles.
Formal derivation blocked pending Z(Phi) formalization completion.

Proposed information-theoretic form:
  F_self = I(Psi_int; Psi) / H(Psi)

---

## 2D Consciousness Threshold

A system is conscious if and only if:
  R > C*  AND  F_self > F_self*

Two independent thresholds. Both must be satisfied.
This is not a single scalar threshold — it is a two-dimensional criterion.

---

## State Map (Full — Anesthetic + Psychedelic)

| State                | N_eff       | F_self   | R        | Description               |
|----------------------|-------------|----------|----------|---------------------------|
| Awake                | high        | ~= 1     | high     | Conscious                 |
| MDMA                 | increased   | ~= 1     | highest  | Max R — unique class      |
| Low-dose psilocybin  | increased   | moderate | elevated | Expanded awareness        |
| High-dose psilocybin | very high   | -> 0     | -> 0     | Ego dissolution           |
| DMT breakthrough     | maximum     | -> 0     | -> 0     | Ego death, max N_eff      |
| Salvia               | disrupted   | -> 0     | -> 0     | Fragmented                |
| Ketamine             | high        | -> 0     | -> 0     | Dissociative (lambda_N=0) |
| Dexmedetomidine      | elevated    | low      | low      | Sedated (lambda_T low)    |
| Propofol/sevoflurane | -> 0        | -> 0     | -> 0     | Unconscious (lambda_G=0)  |
| Deep sleep           | -> 0        | -> 0     | -> 0     | Unconscious               |

**Two distinct paths to R -> 0:**
1. N_eff collapse (anesthesia, deep sleep)
2. F_self collapse with N_eff preserved (psychedelic ego death, dissociatives)

This distinction is unique to the V2 two-dimensional framework.
Prior single-threshold models cannot reproduce it.

---

## Psychedelic Class Analysis (V2 — Directional)

### Classic psychedelics (5-HT2A agonists — psilocybin, LSD, mescaline)
- N_eff increases (cortical desynchronization -> broader integration)
- F_self decreases (default mode network suppression)
- R trajectory depends on dose: moderate dose elevates R; high dose collapses it via F_self

### MDMA
- N_eff increases
- F_self preserved (DMN not suppressed; interoceptive + social circuits enhanced)
- R reaches maximum — the only pharmacological class where both N_eff and F_self rise simultaneously
- Therapeutic efficacy for PTSD explained: memory reconsolidation under maximum R, not ego dissolution

### Ketamine / PCP (NMDA antagonists)
- lambda_N -> 0, therefore F_self -> 0
- N_eff may remain high (thalamocortical activity not fully suppressed)
- R -> 0 despite cortical activity — dissociation without global suppression

### Dexmedetomidine (alpha-2 agonist)
- Thalamic broadcast suppressed: lambda_T low
- F_self low, R low
- Paradox: elevated cortical N_eff but no conscious integration — explained by thalamic gate

### Propofol / sevoflurane (GABA-A potentiation)
- lambda_G -> 0
- Global suppression of N_eff and F_self
- R -> 0

**Therapeutic efficacy prediction (V2):**
- MDMA best for PTSD: maximum R during reconsolidation
- Psilocybin best for depression: N_eff reorganization, not ego dissolution depth
- Framework explains differential efficacy from first principles
- REBUS model (Carhart-Harris) is structurally compatible with V2

---

## Neural Sector Scale Parameters

| Parameter | Value  | Derivation                       |
|-----------|--------|----------------------------------|
| r_coh     | 4.43 cm | v_slow / omega_char (40 Hz)     |
| r_ref     | 27.9 cm | v_fast / omega_char (40 Hz)     |
| tau_K     | 4.0 ms  | 1 / omega_char                  |
| beta      | ~= 2pi  | v_fast / v_slow (working assumption) |
| tau_mem   | 25 ms   | gamma-band cycle (neural check) |

v_fast = axonal conduction velocity
v_slow = dendritic/synaptic integration velocity

---

## Forward Predictions

| Prediction                        | Confidence  | Testable by              |
|-----------------------------------|-------------|--------------------------|
| 2D threshold (R, F_self)          | LOW-MEDIUM  | Anesthesia depth data    |
| MDMA uniquely maximizes R         | MEDIUM      | EEG + pharmacology       |
| Ketamine: high N_eff, zero F_self | MEDIUM      | EEG + NMDA assay         |
| Psilocybin: N_eff reorganization  | MEDIUM      | fMRI + clinical outcome  |
| Dexmedetomidine: thalamic gate    | MEDIUM      | Thalamic recording data  |

---

## Confidence Statement

Consciousness predictions have LOWER confidence than physical predictions
(CDDR, sigma_8, BH QNM). The model is internally consistent and makes
novel testable distinctions, but F_self is not yet computable from first
principles. Psychedelic extension is directional only.

DMT entity contact: speculative. Do not present externally.
Formal development deferred until F_self is formally computable.

---

## Status

**Point 1 — CLOSED (framework complete)**

The two-dimensional threshold, state map, psychedelic extension, and
mechanistic F_self decomposition are all developed. F_self formal
derivation (Gap 5) and full psychedelic formalization are deferred
pending computational tools.

