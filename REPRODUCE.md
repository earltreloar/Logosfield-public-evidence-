# Reproduce the current public Logosfield path

This repository maintains a **narrowed frozen public test path**.

The active public path currently includes only:

1. CDDR
2. Mechanism 16

Other materials in the repository remain part of the broader project record but are not all equal in current evidentiary status.

---

## Requirements

Recommended environment:

- Python 3.10+
- NumPy
- Pandas
- Matplotlib

Install additional packages if needed in your local environment before running.

---

## Active reproduction commands

Run the current public tests using the repository runner.

Run CDDR:

    python run.py --mode cddr

Run Mechanism 16:

    python run.py --mode mech16

---

## Expected outputs

CDDR run should:

- compute the η (Etherington distance-duality) diagnostic
- print summary statistics

Mechanism 16 run should:

- compute the downstream σ₈ response
- print the resulting benchmark comparison

---

## Philosophy of the current path

The public path is intentionally narrow.

The goal is not to maximize the number of mechanisms claimed.  
The goal is to determine whether a **single frozen structure survives contact with multiple observables without branch-specific retuning**.

This means:

- the core parameters are frozen
- couplings are interpreted minimally
- the current public path is limited to CDDR and Mechanism 16

---

## Current cautions

This repository does **not** currently claim:

- confirmed discovery of a new force
- validated galaxy rotation curve solutions
- full empirical separation of coupling sectors
- inheritance of all historical mechanisms from the present frozen path

The repository should therefore be read as a **candidate-framework reproducibility track**, not a completed discovery claim.

---

## Key files

README.md — project overview  
THEORY.md — canonical model summary  
CHALLENGE.md — replication challenge  
run.py — public execution runner  
tools/ — data processing utilities  
Mechanism16/ — σ₈ response branch implementation

---

## Historical material

Other mechanisms and historical experiments remain preserved in the repository for continuity and reference. They should not automatically be interpreted as part of the **current locked public test path**.
