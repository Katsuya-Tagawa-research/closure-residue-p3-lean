# SPS-H123 — Native-source completeness and finite certification gate

This follows the independent P11 Static Primitive Selection (SPS) series, stacked after Draft PR #137 (SPS-H122). It is separate from unrelated H75-memory P11-H113 PR #132.

Run `python -m pip install sympy==1.14.0` and `python research/p11/sps-h123-20261019/P3P11_SPS_H123_native_completeness_audit.py`.

Mathematical result: four proposed H37 preparation/readout pairs produce exactly `A=-2 I4` at identity baseline. A conservative Hilbert–Schmidt norm bound keeps that matrix invertible under the *known fixed* H37 baseline for `t=1/100`. All algebraic checks use exact SymPy rationals. A separate hypothetical fifth, unmarked diagonal port cannot be ruled out by four marked-port experiments.

**OPEN:** physical source exhaustiveness, phase/readout calibration, native actuator provenance, P6 experimental gate, unique AX-ORIGIN from F, P9 Einstein dynamics, and P11 Generative Completeness. Finite CI does not constitute experimental evidence, Lean formalization or independent human peer review.