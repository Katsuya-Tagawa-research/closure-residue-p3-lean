# P11–AX11 minimal instruments and complex orientation

Stacked Draft on P11-AX10 PR #148. P11 axiomatization; no SPS-H113–H123 rewrite and no changes to frozen P1–P8.

Run with Python 3.11+ and SymPy 1.14:
    python -m pip install sympy==1.14.0
    python research/p11/ax11-minimal-orientation-20261019/P11_AX11_chiral_minimality_audit.py

Expected 803 exact assertions and generated JSON. The two four-outcome tetrahedral qubit instruments have reachable rank4, observable rank4, Hankel rank4; their full word languages coincide via simultaneous transpose, but unitary-conjugacy chirality has opposite sign. Only an independently fixed external Y phase reference makes that oriented distinction operational. Unmarked physical source catalogue, original P3 residue, P6 experimental gate, P9 gravity, F Generative Completeness remain OPEN. No Lean or human expert review of this theorem.
