# Mechanism #2 — Density–Lensing (κ) Coherence

**Goal**  
Measure correlation between Logosfield density overlays and DES-Y3 κ mass maps.

**Data**  
DES-Y3 Kaiser–Squires convergence maps; matched Logosfield density rasters and masks.

**Method (locked/prereg)**  
Real-space w(θ) and harmonic Cℓ spectra with **≥1000 permutation nulls**; mask-aware resampling.

**Key result**  
Bayes factor **log10 BF ≈ 101** (strong support); rotation/shuffle nulls collapse ≈0.50.

**Reproduce**  
- Release bundle: `Mechanism2_Validated_Results.zip`  
- Or runner: `python run.py --mechanism 2`

**Outputs**  
`m2_outputs/` with power/cross-spectra, null histograms, and JSON summary.
