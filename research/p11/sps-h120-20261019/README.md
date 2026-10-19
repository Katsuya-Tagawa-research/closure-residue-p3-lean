# P11-SPS H120: Choi-Canonical Operational Source

Stacks on **SPS-H119 Draft PR #134**; separate from unrelated H75/P11 H113 (#132). This H120 PR adds one mathematical proof note, one exact SymPy verifier and one path-scoped CI. It does not edit P1–P8, original Lean core, P9 studies, Notion, Zenodo or main.

Reproduce:
\`\`\`sh
python -m pip install sympy==1.14.0
python research/p11/sps-h120-20261019/P3P11_SPS_H120_choi_source_audit.py
\`\`\`
Expected: **51 exact checks PASS** and a generated JSON report.

Result: the Choi support is a canonical, tensor/composition-respecting **operational channel Kraus space**. It forgets physical actuation and may lose generator locality; it does not select the unique **native static source** or establish the P6 physical gate.

**OPEN:** source-native correspondence; AX-ORIGIN from F; P11 completeness; P9 Einstein dynamics. Finite CI and standard quantum-channel algebra are not an experimentally sourced primitive, novel Choi theorem, Lean proof or human peer review.
