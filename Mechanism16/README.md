# Mechanism 16 — sigma8 response (current public child branch)

## Status

Mechanism 16 is currently treated as a **child branch of the frozen public CDDR path**.

It is not presented here as an independently calibrated proof. Its purpose is to test whether the same fixed public cosmology structure can produce a consistent downstream response without branch-specific retuning.

---

## Current public interpretation

The current public path does **not** treat Mechanism 16 as a strong standalone derivation from a separately measured coupling sector.

Instead, it is interpreted as a **weak-response downstream branch** of the same narrowed frozen path that anchors the current CDDR result.

In that sense, Mechanism 16 is currently part of a minimal two-test structure:

1. CDDR
2. sigma8 response

---

## Current public bridge

The current public implementation uses a **weak-response bridge** rather than the older stronger square-root-style bridge.

Public default:

- `sigma8_ref = 0.8121`
- default response coefficient: `k = 0.0`

Operationally:

```text
sigma8 = sigma8_ref * (1 + k * (eta - 1))
