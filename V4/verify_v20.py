"""
Logosfield V4 Vision 20 — Numerical Verification Suite
earltreloar/Logosfield-public-evidence- / V4/verify_v20.py

Independently verifies all core numerical claims from V20 session.
Run: python3 verify_v20.py

All results should pass. Any failure indicates a document error.
Last updated: July 14, 2026 (corrected MF-4 and S precision claims)
"""

import numpy as np
from scipy.special import gamma

PASS = "PASS"
FAIL = "FAIL"
results = []

def check(name, condition, computed=None, expected=None):
    status = PASS if condition else FAIL
    results.append((status, name))
    marker = "✓" if condition else "✗"
    print(f"  {marker} {name}")
    if computed is not None:
        print(f"      computed:  {computed}")
    if expected is not None:
        print(f"      expected:  {expected}")
    return condition

print("="*65)
print("LOGOSFIELD V4 VISION 20 — NUMERICAL VERIFICATION SUITE")
print("="*65)
print()

BETA = 2 * np.pi
TAU  = 1.0
D    = 4

# ── Section 1: Core parameters ────────────────────────────────────────────
print("SECTION 1: Core Derived Parameters")
print("-"*40)
check("β = 2π", np.isclose(BETA, 6.283185307179586),
      computed=BETA, expected=6.283185307179586)
check("τ = 1", TAU == 1.0)
check("d = 4", D == 4)
print()

# ── Section 2: T ──────────────────────────────────────────────────────────
print("SECTION 2: T = (24·exp(-2π)/π)^(1/4)")
print("-"*40)
T = (24 * np.exp(-BETA) / np.pi) ** 0.25
T_precise = 0.345602734970968   # corrected precise value
check("T value", np.isclose(T, 0.34560273, rtol=1e-6),
      computed=f"{T:.14f}", expected="0.34560273...")
check("T⁴ = 24·exp(-2π)/π",
      np.isclose(T**4, 24*np.exp(-BETA)/np.pi),
      computed=f"{T**4:.12f}", expected=f"{24*np.exp(-BETA)/np.pi:.12f}")
print()

# ── Section 3: Geometric quantities ──────────────────────────────────────
print("SECTION 3: Geometric Quantities")
print("-"*40)
V_diamond  = np.pi / 24
V_interval = np.pi**2 / 12
check("V_diamond = π/24",
      np.isclose(V_diamond, 0.13089969389957),
      computed=f"{V_diamond:.14f}")
check("V_interval = π²/12",
      np.isclose(V_interval, 0.82246703342411),
      computed=f"{V_interval:.14f}")
check("V_interval / V_diamond = β = 2π  [KEY — d=4 only]",
      np.isclose(V_interval / V_diamond, BETA),
      computed=f"{V_interval/V_diamond:.12f}", expected=f"β = {BETA:.12f}")
check("V_interval = β · V_diamond  [EXACT]",
      np.isclose(V_interval, BETA * V_diamond),
      computed=f"{V_interval:.12f}", expected=f"{BETA*V_diamond:.12f}")
print()

# ── Section 4: ρ = 24/π ───────────────────────────────────────────────────
print("SECTION 4: ρ = 24/π Self-Consistency Derivation")
print("-"*40)
rho = 24 / np.pi
check("ρ = 24/π = 7.6394...",
      np.isclose(rho, 7.639437268699651),
      computed=f"{rho:.12f}")
check("ρ · V_diamond = 1 exactly  [unit density]",
      np.isclose(rho * V_diamond, 1.0),
      computed=f"{rho * V_diamond:.15f}", expected="1.0")
check("Self-consistency: exp(-β) = exp(-ρ·V_interval)  [KEY]",
      np.isclose(np.exp(-BETA), np.exp(-rho * V_interval)),
      computed=f"{np.exp(-BETA):.12f}", expected=f"{np.exp(-rho*V_interval):.12f}")
check("ρ = β / V_interval",
      np.isclose(rho, BETA / V_interval),
      computed=f"{rho:.12f}", expected=f"{BETA/V_interval:.12f}")
print()

# ── Section 5: Discharge equation ─────────────────────────────────────────
print("SECTION 5: Discharge Equation")
print("-"*40)
check("exp(-β) = (π/24)·T⁴",
      np.isclose(np.exp(-BETA), (np.pi/24)*T**4),
      computed=f"{np.exp(-BETA):.12f}", expected=f"{(np.pi/24)*T**4:.12f}")
check("π/24 = V_diamond  [coefficient = diamond volume, d=4 only]",
      np.isclose(np.pi/24, V_diamond),
      computed=f"{np.pi/24:.12f}")
check("exp(-β) = V_diamond · T⁴",
      np.isclose(np.exp(-BETA), V_diamond * T**4),
      computed=f"{np.exp(-BETA):.12f}", expected=f"{V_diamond*T**4:.12f}")
print()

# ── Section 6: Entropy ────────────────────────────────────────────────────
print("SECTION 6: Entropy S at Unit Density")
print("-"*40)
S_exact  = rho * (np.exp(TAU * np.exp(-BETA)) - 1)
S_approx = rho * np.exp(-BETA)   # = T⁴ (leading order)
T4       = T**4
check("S = ρ·(exp(τ·exp(-β))-1) computes correctly",
      np.isclose(S_exact, 0.014279540, rtol=1e-5),
      computed=f"{S_exact:.10f}")
check("S ≈ ρ·exp(-β) = T⁴ to leading order",
      np.isclose(S_approx, T4),
      computed=f"ρ·exp(-β)={S_approx:.12f}, T⁴={T4:.12f}")
check("S ≈ T⁴: error < 2×10⁻⁵  [corrected from document]",
      abs(S_exact - T4) < 2e-5,
      computed=f"error = {abs(S_exact-T4):.3e}", expected="< 2e-5")
print()

# ── Section 7: MF-4 (corrected) ───────────────────────────────────────────
print("SECTION 7: MF-4 — Matter Density (CORRECTED)")
print("-"*40)
rho_matter = rho * np.exp(-BETA)
print("  NOTE: Original document contained error in MF-4 formulation.")
print("  Corrected relations:")
print()
check("ρ_matter = ρ·exp(-β) = T⁴  [CORRECT MF-4]",
      np.isclose(rho_matter, T4),
      computed=f"ρ_matter={rho_matter:.12f}, T⁴={T4:.12f}")
check("ρ_matter · V_diamond = exp(-β)  [correct geometric relation]",
      np.isclose(rho_matter * V_diamond, np.exp(-BETA)),
      computed=f"{rho_matter*V_diamond:.12f}", expected=f"{np.exp(-BETA):.12f}")
check("ρ_matter · V_diamond ≠ T⁴  [previous document error]",
      not np.isclose(rho_matter * V_diamond, T4),
      computed=f"ρ_matter·V_d={rho_matter*V_diamond:.6f} ≠ T⁴={T4:.6f}")
check("Matter fraction = exp(-β) = 0.1867%",
      np.isclose(np.exp(-BETA)*100, 0.18674, rtol=1e-3),
      computed=f"{np.exp(-BETA)*100:.5f}%")
print()

# ── Section 8: MM formula ─────────────────────────────────────────────────
print("SECTION 8: Myrheim-Meyer f_MM(4) = 1/60")
print("-"*40)
def f_mm(d):
    return gamma(d+1)*gamma(d/2+1)/(4*gamma(3*d/2+1))
check("f_MM(4) = 1/60",
      np.isclose(f_mm(4), 1/60),
      computed=f"{f_mm(4):.10f}", expected=f"1/60 = {1/60:.10f}")
print()

# ── Section 9: FF-4 SO(3) ────────────────────────────────────────────────
print("SECTION 9: FF-4 — SO(3) Generator Count from d=4")
print("-"*40)
def so_gen(n): return n*(n-1)//2
for d_t in [3,4,5,6]:
    n = d_t-1
    marker = " ← d=4 [DERIVED]" if d_t==4 else ""
    print(f"  d={d_t}: cross-section S^{d_t-2}, SO({n}), {so_gen(n)} generators{marker}")
check("SO(3) has 3 generators", so_gen(3)==3, computed=so_gen(3))
check("3 is unique to d=4 among d=2..6",
      so_gen(2)!=3 and so_gen(3)==3 and so_gen(4)!=3,
      computed=f"d=3→{so_gen(2)}, d=4→{so_gen(3)}, d=5→{so_gen(4)}")
print()

# ── Section 10: T interpretations ────────────────────────────────────────
print("SECTION 10: Consistent Interpretations of T")
print("-"*40)
T_discharge = (np.exp(-BETA)*24/np.pi)**0.25
T_volume    = (np.exp(-BETA)/V_diamond)**0.25
T_matter    = rho_matter**0.25   # CORRECTED: T = ρ_matter^(1/4)
check("T from discharge equation",
      np.isclose(T_discharge, T, rtol=1e-10), computed=f"{T_discharge:.12f}")
check("T from volume fraction (HV-1c)",
      np.isclose(T_volume, T, rtol=1e-10),    computed=f"{T_volume:.12f}")
check("T = ρ_matter^(1/4)  [CORRECTED MF-4]",
      np.isclose(T_matter, T, rtol=1e-10),    computed=f"{T_matter:.12f}")
check("All three T values identical",
      np.isclose(T_discharge, T_volume) and np.isclose(T_volume, T_matter),
      computed=f"max diff = {max(abs(T_discharge-T_volume),abs(T_volume-T_matter)):.2e}")
print()

# ── Summary ───────────────────────────────────────────────────────────────
print("="*65)
print("VERIFICATION SUMMARY")
print("="*65)
passed = sum(1 for s,_ in results if s==PASS)
failed = sum(1 for s,_ in results if s==FAIL)
print(f"  {passed}/{len(results)} checks passed")
if failed:
    print(f"  FAILED ({failed}):")
    for s,n in results:
        if s==FAIL: print(f"    ✗ {n}")
else:
    print("  All checks passed ✓")
print()
print("  Corrections applied vs. original V20 document:")
print("  1. MF-4: T⁴ = ρ_matter (not ρ_matter·V_diamond)")
print("     Correct: ρ_matter = T⁴; ρ_matter·V_diamond = exp(-β)")
print("  2. S≈T⁴ precision: error < 2e-5 (not < 1e-7 as originally stated)")
print()
print(f"  T (precise):    {T:.14f}")
print(f"  ρ:              {rho:.14f}")
print(f"  exp(-β):        {np.exp(-BETA):.14f}")
print(f"  V_diamond:      {V_diamond:.14f}")
print(f"  V_interval:     {V_interval:.14f}")
print(f"  V_int/V_dia:    {V_interval/V_diamond:.14f} = β = 2π")
print()
print("Logosfield V4 Vision 20 · earltreloar/Logosfield-public-evidence-")
