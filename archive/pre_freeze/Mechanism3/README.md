# Mechanism #3 — Sacred-Site Alignment

**Goal**  
Quantify spatial coherence between ancient sacred-site coordinates and Logosfield resonance nodes.

**Data**  
Aggregated sacred-site catalog; shoreline/elevation/era covariates; global DEM.

**Method (locked/prereg)**  
Mean geodesic distance advantage vs matched nulls (shoreline/elevation/era-matched); permutation roll/jitter tests.

**Key result**  
Global **p ≈ 0.018**; **log10 BF ≈ 0.95** (conservative, prereg).

**Reproduce**  
- Runner: `python run.py --mechanism 3`  
- Bundle (when attached): `Mechanism3_SacredSites_Land_Validated_Results.zip`

**Outputs**  
Maps/overlays, null distributions, and `m3_summary.json` in `Mechanism3/outputs/`.
