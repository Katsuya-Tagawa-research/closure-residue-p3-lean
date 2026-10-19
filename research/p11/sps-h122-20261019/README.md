# SPS-H122 — Native control-jet certification
Independent Static Primitive Selection series stacked on SPS-H121 PR #136, not the separate P11 H113 study of PR #132.

Reproduce with Python 3.11 and SymPy 1.14:
\`\`\`sh
python -m pip install sympy==1.14.0
python research/p11/sps-h122-20261019/P3P11_SPS_H122_native_control_jet_audit.py
\`\`\`

Expected finite audit: **65/65 exact assertions PASS**; qubit full observability rank3 vs diagonal-population-only rank0, H37 four marked full-process jets rank4. **Physical native-source catalogue, P6 hardware, P11 Completeness and P9 GR remain OPEN.** No code change to main or frozen P1–P8. The rank theorem is standard system-identification algebra and no novel theorem-priority claim is made.
