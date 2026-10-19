# P11–AX08 — Non-Circular Generative Axioms and Independence Audit

2026-10-19, stacked on P11–AX07 Draft PR #145. Separate from SPS-H113–H123, which retain the physical static-source STOP.

## Reproduce

\`\`\`sh
python -m pip install sympy==1.14.0
python research/p11/ax08-noncircular-generativity-20261019/P11_AX08_independence_audit.py
\`\`\`

Expected 604/604 exact finite assertions. The analytic theorem proves identical *all finite A-only outcome words* for any independent hidden spectator CPTP dynamics; SymPy checks every binary word through length six. An independently prepared/read B qubit distinguishes the two explicit hidden channels. An unmarked U(d)-equivariant rank-one pointer cannot be selected.

**G1:** finite/relative operational predictions. **G2:** physical source/observer completeness OPEN. **G3:** F-generative completeness OPEN. No human peer review or Lean mechanization of the full theorem; no P6 physics PASS, P9 GR or P3 original commutator-residue equivalence.
