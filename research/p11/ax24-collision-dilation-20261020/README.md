# P11 AX24 — finite collision dilation and provenance gate

2026-10-20. Stacked Draft on AX23 PR #161, main unchanged.

An exact finite controlled-environment dilation of the pure-dephasing step q id + (1-q) Delta_D, fine-collision Strang convergence to H37 -i[H,.]+(2/3)(Delta_D-id), and the first-order dissipator obstruction for a fixed bounded finite bath Hamiltonian are documented with **263 exact SymPy assertions**.

This is standard conditional open-systems mathematics, not independent F origin, hardware certification, new Lean formalization, or human review. G2/G3 stay OPEN.

Reproduce:

```sh
python -m pip install sympy==1.14.0
python P11_AX24_collision_source_audit.py
```
