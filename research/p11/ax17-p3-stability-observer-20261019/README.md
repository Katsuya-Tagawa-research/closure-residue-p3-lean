# P11–AX17: Genuine P3 Residue Structural Stability and Observer Dependence

Stacked Draft on P11–AX16 PR #154. No edits to frozen papers or main.

Run with Python 3.11+, SymPy 1.14:
    python research/p11/ax17-p3-stability-observer-20261019/P11_AX17_p3_perturbation_observer_audit.py

Expected **111/111 exact checks**. H37 resolvent R2 rank4 survives nearby physically admissible GKSL parameters; a decoupled model has rank0. Under *the same* qubit CPTP dynamics, Z MASA first nonzero genuine P3 residue is R3 while the Hamiltonian-axis MASA has none. Simultaneous gauge conjugacy preserves ranks. Do not confuse this with F's physical observer generation or P6 native source certification: G2 and G3 remain OPEN.
