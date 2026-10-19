# P11–AX03 Canonical Observer Projection and Selection No-Go

Stacked on P11–AX02 Draft PR #140, separate from SPS-H113–H123 source-identifiability work. Existing main and frozen P1–P8 are unchanged.

Reproduce: Python 3.11 + SymPy 1.14
\`\`\`sh
python research/p11/ax03-observer-projection-20261019/P11_AX03_canonical_observer_audit.py
\`\`\`
Expect **119 exact finite assertions** PASS and generated JSON.

Result: a given unital *-subalgebra A has a unique trace-preserving UCP expectation E_A. Channel-only full unitary covariance cannot pick proper nonscalar pointer algebra for an isotropic channel. Original H37's fixed-point algebra is **CI5**, whereas its marked D5 has dimension5 and is not dynamically invariant; explicit first-order coherence and second-order population returns are verified.

**OPEN:** F-derived observer algebra, original P3 R_k identification, physical P6 source, P9 gravity and P11 generative completeness. No independent human review or Lean formal proof.
