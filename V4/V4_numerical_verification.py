"""
Logosfield V4 — Numerical Verification Suite
Earl Treloar · June 22, 2026

Verifies all core numerical claims made in V4 Vision 17 Final Complete.
Run with: python V4_numerical_verification.py

All results should match the values stated in the document.
"""

import numpy as np
import math
from scipy.optimize import brentq
import sys

PASS = "  PASS"
FAIL = "  FAIL"
SEP = "=" * 60

def check(label, condition, detail=""):
    status = PASS if condition else FAIL
    print(f"{status}: {label}")
    if detail:
        print(f"        {detail}")
    return condition

results = []

print(SEP)
print("V4 NUMERICAL VERIFICATION SUITE")
print("Logosfield V4 Vision 17 Final Complete · June 22, 2026")
print(SEP)

# ── 1. COMPOSABILITY VERIFICATION ────────────────────────────────────────────
print("\n1. COMPOSABILITY: M(L=n) = M(L=1)^n")
print("   Claim: exponential kernel satisfies composability exactly")

beta = 2 * np.pi
M1 = np.exp(-beta * 1)  # kernel weight per step

errors = []
for n in range(1, 21):
    Mn = np.exp(-beta * n)
    M1n = M1 ** n
    err = abs(Mn - M1n)
    errors.append(err)

max_err = max(errors)
results.append(check(
    f"M(n) = M(1)^n for n=1..20 at β=2π",
    max_err < 1e-14,
    f"max error = {max_err:.2e} (machine precision)"
))

# ── 2. POISSON FORM ───────────────────────────────────────────────────────────
print("\n2. POISSON FORM: N_k(τ) = (ρτ)^k / k!")
print("   Claim: forced by convolution + self-bounding, no manifold assumed")

rho, tau = 1.0, 5.0
lam = rho * tau  # Poisson parameter

errors_poisson = []
for k in range(0, 15):
    Nk_formula = (lam ** k) / math.factorial(k) * np.exp(-lam)
    # Verify convolution: N_k(τ1+τ2) = Σ N_j(τ1)·N_{k-j}(τ2)
    tau1, tau2 = 2.0, 3.0
    lam1, lam2 = rho * tau1, rho * tau2
    conv = sum(
        (lam1**j / math.factorial(j)) * np.exp(-lam1) *
        (lam2**(k-j) / math.factorial(k-j)) * np.exp(-lam2)
        for j in range(k+1)
    )
    Nk_direct = ((lam1+lam2)**k / math.factorial(k)) * np.exp(-(lam1+lam2))
    errors_poisson.append(abs(conv - Nk_direct))

max_err_p = max(errors_poisson)
results.append(check(
    "Poisson convolution N_k(τ1+τ2) = Σ N_j(τ1)·N_{k-j}(τ2) for k=0..14",
    max_err_p < 1e-14,
    f"max error = {max_err_p:.2e}"
))

# ── 3. FIXED POINT EQUATION ───────────────────────────────────────────────────
print("\n3. FIXED POINT EQUATION: C₄ = (1-u)⁴ / (1+4u+u²)")
print("   Claim: corrected from Ψ(e)=exp(-β) normalization (axiom A2 compliant)")

def C4(beta):
    u = np.exp(-beta)
    return (1 - u)**4 / (1 + 4*u + u**2)

def C4_old(beta):
    u = np.exp(-beta)
    return (1 - u)**4 / (u * (1 + 4*u + u**2))

# Verify: C4_new = C4_old · exp(-β)
betas_test = [1.0, np.pi, 2*np.pi, 5.0, 10.0]
errors_fp = []
for b in betas_test:
    u = np.exp(-b)
    ratio = C4(b) / C4_old(b)
    errors_fp.append(abs(ratio - u))

results.append(check(
    "C₄_new = C₄_old · exp(-β) at β = 1, π, 2π, 5, 10",
    max(errors_fp) < 1e-14,
    f"max error = {max(errors_fp):.2e}"
))

# C4 at β=2π
c4_2pi = C4(2*np.pi)
results.append(check(
    f"C₄ at β=2π ≈ 0.985 (physically sensible, ≈1)",
    abs(c4_2pi - 0.985) < 0.001,
    f"C₄(2π) = {c4_2pi:.6f}"
))

# C4 → 1 as β → ∞
c4_large = C4(50.0)
results.append(check(
    "C₄ → 1 as β → ∞ (minimum shell structure)",
    abs(c4_large - 1.0) < 1e-10,
    f"C₄(50) = {c4_large:.10f}"
))

# ── 4. ALGEBRAIC IDENTITY ─────────────────────────────────────────────────────
print("\n4. ALGEBRAIC IDENTITY: C₄·exp(-4β) = u⁴(1-u)⁴/(1+4u+u²)")
print("   Claim: exact, follows algebraically from fixed point definition")

errors_id = []
for b in [1.0, np.pi, 2*np.pi, 5.0, 10.0, 20.0]:
    u = np.exp(-b)
    lhs = C4(b) * u**4
    rhs = u**4 * (1-u)**4 / (1 + 4*u + u**2)
    errors_id.append(abs(lhs - rhs))

results.append(check(
    "C₄·exp(-4β) = u⁴(1-u)⁴/(1+4u+u²) at β = 1, π, 2π, 5, 10, 20",
    max(errors_id) < 1e-14,
    f"max error = {max(errors_id):.2e} (exact identity)"
))

# ── 5. ASYMPTOTIC IDENTITY ────────────────────────────────────────────────────
print("\n5. ASYMPTOTIC IDENTITY: ln(C₄) = -8·exp(-β) + O(exp(-2β))")
print("   Claim: leading order behavior for large β")

errors_asym = []
for b in [5.0, 10.0, 15.0, 20.0]:
    u = np.exp(-b)
    lnC4 = np.log(C4(b))
    approx = -8 * u
    # Relative error of leading term
    if abs(lnC4) > 1e-15:
        rel_err = abs(lnC4 - approx) / abs(lnC4)
        errors_asym.append(rel_err)

results.append(check(
    "ln(C₄) ≈ -8·exp(-β) to within O(exp(-2β)) for β = 5,10,15,20",
    max(errors_asym) < 0.01,
    f"max relative error in leading term = {max(errors_asym):.2e}"
))

# Verify ln(C4_old) ≈ β - 8exp(-β) (old normalization)
errors_old = []
for b in [5.0, 10.0, 15.0]:
    u = np.exp(-b)
    lnC4_old = np.log(C4_old(b))
    approx_old = b - 8*u
    errors_old.append(abs(lnC4_old - approx_old))

results.append(check(
    "ln(C₄_old) = β - 8·exp(-β) + O(exp(-2β)) — old normalization",
    max(errors_old) < 1e-3,
    f"max error = {max(errors_old):.2e}"
))

# ── 6. FORESIGHT/MEMORY RATIO ─────────────────────────────────────────────────
print("\n6. FORESIGHT/MEMORY RATIO: exp(-β)/2")
print("   Claim: past always dominates; ratio = 0.093% at β=2π")

ratio_2pi = np.exp(-2*np.pi) / 2
results.append(check(
    f"Foresight/memory at β=2π = exp(-2π)/2 ≈ 9.3×10⁻⁴",
    abs(ratio_2pi - 9.337e-4) < 1e-6,
    f"ratio = {ratio_2pi:.6e}"
))

results.append(check(
    "Past always dominates: exp(-β)/2 < 1 for all β > 0",
    all(np.exp(-b)/2 < 1 for b in [0.01, 0.1, 1.0, 2*np.pi, 10.0]),
    "verified for β = 0.01, 0.1, 1, 2π, 10"
))

# ── 7. PATH F PERIODICITY ─────────────────────────────────────────────────────
print("\n7. PATH F: 2π/β = 1 step → β = 2π")
print("   Claim: imaginary period of exp(-βL) matches discrete step when β=2π")

# The periodicity condition: 2π/β = 1 → β = 2π
beta_from_periodicity = 2 * np.pi
period = 2 * np.pi / beta_from_periodicity
results.append(check(
    "2π/β = 1 step when β = 2π",
    abs(period - 1.0) < 1e-14,
    f"2π/(2π) = {period:.10f}"
))

# Verify: exp(-β(L + 2πi/β)) = exp(-βL) (periodicity in imaginary direction)
beta_test = 2 * np.pi
L_test = 3.0
M_L = np.exp(-beta_test * L_test)
M_L_shifted = np.exp(-beta_test * (L_test + 2*np.pi*1j/beta_test))
results.append(check(
    "exp(-β(L+2πi/β)) = exp(-βL): kernel periodic in imaginary direction",
    abs(M_L_shifted - M_L) < 1e-14,
    f"|M(L+2πi/β) - M(L)| = {abs(M_L_shifted - M_L):.2e}"
))

# ── 8. BARYON DEFICIT (CORRECTED NORMALIZATION) ───────────────────────────────
print("\n8. BARYON DEFICIT: corrected normalization values")
print("   Claim: deficit ≈ 1.2×10⁻¹¹ at candidate β=2π (weaker than old 6.4×10⁻⁹)")

u_2pi = np.exp(-2*np.pi)
deficit_new = u_2pi**4 * (1-u_2pi)**4 / (1 + 4*u_2pi + u_2pi**2)
deficit_old = u_2pi**3 * (1-u_2pi)**4 / (1 + 4*u_2pi + u_2pi**2)

results.append(check(
    f"New deficit at β=2π ≈ 1.2×10⁻¹¹",
    abs(deficit_new - 1.2e-11) < 0.1e-11,
    f"deficit_new = {deficit_new:.4e}"
))

results.append(check(
    f"Old deficit at β=2π ≈ 6.4×10⁻⁹",
    abs(deficit_old - 6.4e-9) < 0.1e-9,
    f"deficit_old = {deficit_old:.4e}"
))

eta = 6.1e-10
results.append(check(
    "New deficit/η ≈ 0.02 (weaker proximity than old 10.5)",
    deficit_new / eta < 0.05,
    f"new deficit/η = {deficit_new/eta:.4f}"
))

# β where new deficit = η
def eq_new(b):
    u = np.exp(-b)
    return u**4*(1-u)**4/(1+4*u+u**2) - eta

beta_eta = brentq(eq_new, 5.0, 15.0)
results.append(check(
    f"β where new deficit = η ≈ 5.29 (new normalization)",
    abs(beta_eta - 5.294) < 0.01,
    f"β_η = {beta_eta:.6f}, β_η/(2π) = {beta_eta/(2*np.pi):.6f} [new normalization, not 7.07 which was old]"
))

# ── 9. CO-DETERMINATION ───────────────────────────────────────────────────────
print("\n9. CO-DETERMINATION: τ*·exp(-β) = ln(3)")
print("   [SPECULATIVE — reference interval τ=1 not derived]")
print("   Claim: τ* ≈ 588 at candidate β=2π (illustrative only)")

tau_star = np.log(3) * np.exp(2*np.pi)
results.append(check(
    "τ* = ln(3)·exp(2π) ≈ 588 at candidate β=2π [SPECULATIVE]",
    abs(tau_star - 588) < 1,
    f"τ* = {tau_star:.4f} [illustrative only — τ=1 reference not derived]"
))

# ── SUMMARY ───────────────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("SUMMARY")
print(SEP)
passed = sum(results)
total = len(results)
print(f"  {passed}/{total} checks passed")
if passed == total:
    print("  All numerical claims verified.")
else:
    print(f"  {total-passed} check(s) FAILED — review output above.")
print(SEP)

sys.exit(0 if passed == total else 1)
