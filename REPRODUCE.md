# Reproduce Logosfield Results

## One‑click (Docker)
```bash
docker build -t logosfield -f common/Dockerfile .
# Example: run Mechanism 14 with prereg
docker run -e PREREG=/prereg/14/2025-10-09/prereg.yaml -v $PWD:/work logosfield
```

## Makefile
```bash
# Example for Mechanism 14
cd Mechanism14 && make reproduce bundle MECH=14 DATE=2025-10-09 PREREG=../prereg/14/2025-10-09/prereg.yaml
```

## Colab
Open the appropriate `RUNME.ipynb` (placeholder) or runner script, upload the `prereg.yaml` when prompted, and run all.
