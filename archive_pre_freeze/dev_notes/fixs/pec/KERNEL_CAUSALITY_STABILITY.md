# Kernel Causality & Stability (Retarded Exponential Memory)

This repository’s “Logosfield memory” term is implemented as a **retarded** (causal) exponential kernel.
This document defines the kernel precisely and states sufficient stability conditions for numerical runs.

## 1. Definition (causal / retarded)
Let Φ(t, x) be the Logosfield scalar. Define the memory functional:

M[Φ](t, x) = ∫_{-∞}^{t} exp[-β (t - t′)] Φ(t′, x) dt′

with β > 0. The upper limit t ensures **causality** (no dependence on future values).

Common normalized variant:
M_norm[Φ](t,x) = β ∫_{-∞}^{t} exp[-β (t - t′)] Φ(t′, x) dt′
so that for slowly varying Φ, M_norm ≈ Φ.

## 2. Local (auxiliary-variable) form
Define an auxiliary field χ(t,x) := ∫_{-∞}^{t} exp[-β (t - t′)] Φ(t′,x) dt′.
Then χ satisfies the first-order ODE:

∂_t χ = Φ - β χ    (β > 0)

This converts the nonlocal kernel into a **local** dynamical system (Φ, χ), which is preferred for
reproducibility and stability analysis.

## 3. Where it enters the action / EOM
In the minimal EFT completion, the memory contribution can enter the equation of motion schematically as:

□Φ + V'(Φ) + γ * F(χ, Φ, ∂Φ, …) = 0

where γ is the locked memory amplitude (γ = 0.005 in the frozen parameter set).

This repository uses the retarded form above; any deviation (advanced kernels, symmetric kernels) is disallowed.

## 4. Stability (sufficient conditions)
### 4.1 Kernel parameters
- β must satisfy β > 0 (ensures exponential decay, bounded memory).
- γ should be treated as a small coupling in EFT sense; for explicit solvers, require γ * Δt ≪ 1.

### 4.2 Discretization
Using the auxiliary form, a stable explicit update is:

χ_{n+1} = χ_n + Δt (Φ_n - β χ_n)

A sufficient stability condition for the χ update is:
Δt < 2/β

(Implicit or semi-implicit updates relax this.)

### 4.3 Sanity checks required in every run
Each mechanism run must report:
- β, γ, Δt (or equivalent step size), integrator choice
- Whether χ was used (local) or direct convolution (nonlocal)
- A short “boundedness check”: max|χ| and whether it remained finite across the run

## 5. Reproducibility contract
Any replication must:
- use the retarded kernel definition above (no future dependence),
- report the prereg hash and parameter hash,
- include null tests (rotations/shuffles/permutations as prereg’d).
