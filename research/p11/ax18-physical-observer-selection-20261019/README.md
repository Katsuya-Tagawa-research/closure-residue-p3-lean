# P11–AX18 — Physical observer selection and noncircular source gate
Stacks on AX17 Draft PR #155, independent of the unfinished SPS native-source evidence.

## Reproduction
Python 3.11 + SymPy 1.14:
\`\`\`sh
python -m pip install sympy==1.14.0
python research/p11/ax18-physical-observer-selection-20261019/P11_AX18_pointer_source_audit.py
\`\`\`
Expected **336/336** exact finite checks, with all physical and F-generative source flags OPEN.

Positive theorem: in known exact dimension d, d preparations and d-outcome POVM with identity probability table force a rank-one pointer PVM up to a global Hilbert frame. With independent fixed-frame preparations, a bounded confusion matrix gives a Hilbert–Schmidt effect bound. Counterexamples retain the same table in d+1, same effects with different instruments, and uncalibrated X/Y phase.

Not an experimental device certificate, proof of exhaustive physical controls, original P3 R_k automatically from hardware, or P11 Generative Completeness. No human review or Lean formalization of general theorem.
