# replications/verify_hashes.py
import json, hashlib, os, glob

MANIFEST = os.path.join(os.path.dirname(__file__), "hashes.json")

def sha256sum(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def find_candidates(fn: str):
    """Try common patterns (handles spaces and '(1)' variants)."""
    base = os.path.basename(fn)
    pats = [
        fn,
        base,
        base.replace(" (", " *").replace(")", "*"),
        fn.replace(" (", " *").replace(")", "*"),
    ]
    seen = []
    for p in pats:
        for m in glob.glob(p):
            if os.path.exists(m) and m not in seen:
                seen.append(m)
    return seen

def main():
    if not os.path.exists(MANIFEST):
        raise SystemExit(f"Manifest not found: {MANIFEST}")

    with open(MANIFEST) as f:
        expected = json.load(f)

    ok = bad = miss = 0
    print("Using manifest:", MANIFEST)
    for fn, ref in expected.items():
        cands = find_candidates(fn)
        if not cands:
            print(f"[WARN] missing: {fn}")
            miss += 1
            continue
        path = cands[0]
        got = sha256sum(path)
        if got == ref:
            print(f"[OK]   {fn}  ✓")
            ok += 1
        else:
            print(f"[MISMATCH] {fn}")
            print(f" expected: {ref}")
            print(f" got:      {got}")
            bad += 1

    print(f"\nSummary: ok={ok}, mismatched={bad}, missing={miss}")

if __name__ == "__main__":
    main()
