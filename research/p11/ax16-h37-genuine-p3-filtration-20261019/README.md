# P11 AX16 — Authentic H37 Original P3 Residue (2026-10-19)

This Draft stacks on AX15 PR #153 and preserves frozen P3. Exact finite evidence: H37 resolvent CPTP channel Phi=(id−L)^−1 has **genuine P3 H1 rank4, R2=D5^0 rank4**, first nonzero residue at depth2. For deterministic fixed-time CPTP Phi_t=exp(tL), an **exact nonzero t^26 Taylor determinant** proves R2=D5^0 for every sufficiently small t>0. For this model R2 and AX14 K have the **same diagonal image**, but are not identical objects or universally linked.

Run (Python 3.11, SymPy 1.14):

    python research/p11/ax16-h37-genuine-p3-filtration-20261019/P11_AX16_H37_genuine_P3_filtration_audit.py

Expected **59/59 exact assertions**. This test generates its own JSON report. Dedicated path-scoped GitHub Actions runs the test and verifies G2/G3 **OPEN** flags.

All physical provenance/independent readout, P6 experimental validation, general P3/AX14 identity, F generation, P9 GR, G2/G3 remain OPEN. No human peer review, no Lean proof of the new analytic general statements.
