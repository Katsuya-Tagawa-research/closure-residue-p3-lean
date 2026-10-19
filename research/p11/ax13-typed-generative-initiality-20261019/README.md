# P11–AX13: Typed F / Initiality / Observer-source STOP

Stacked on AX12 Draft PR #150, independent of SPS research and frozen P1–P8. **Initiality relative to a supplied generator signature is not physical F completeness.**

Reproduce (Python 3.11 and SymPy 1.14):

    python research/p11/ax13-typed-generative-initiality-20261019/P11_AX13_typed_free_generation_audit.py

Expected: **1557 exact SymPy checks PASS**. Check free polynomial words, two distinct UCP retractions onto a fixed observer subalgebra, commuting/noncommuting representations, and separate M2 nonmultiplicative positive quadratic return.

OPEN: physical generator/observer selection, native control inventory, P3 R_k matching, P6 experimental gate, P9 GR, P11 Generative Completeness. No formal Lean proof or human peer review of the general initiality statement.
