# P11–AX09: Universal Observable Realization (relative, linear)

This is the independent P11 axiomatization track stacked on AX08 Draft PR #146, not the SPS H113–H123 native-source selection series. No changes to main or frozen P1–P8.

Run with Python 3.11+, SymPy 1.14:

\`\`\`sh
python -m pip install sympy==1.14.0
python research/p11/ax09-universal-observable-realization-20261019/P11_AX09_hankel_universal_audit.py
\`\`\`

Expected: **203 exact assertions PASS**. The chosen 2-level quantum instrument has minimal observable Hankel rank2. A linear non-unitary similarity and an unobservable extra coordinate preserve its word probabilities. Independent hidden-qubit channels id_B/Ad_Z_B have the same full A-only word series but differ physically.

The positive relative minimality/uniqueness theorem is standard rational-series/weighted-automata mathematics, not a novel intrinsic law for F. A full physical source or observer effect is not selected by the word series; **G2/G3, P6 hardware and P9 gravity remain OPEN**. No human peer review or Lean mechanization.
