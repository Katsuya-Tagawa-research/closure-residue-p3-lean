# H75 GT–K4 operational metric descent — independent Bridge audit (2026-10-20)

A standalone auxiliary audit **stacked on H82 PR #101**, without assigning a new H or P11–AX number. Main and frozen manuscripts remain untouched.

## Three strictly separated claims

**1. Original native 15-record NO-GO — source-reported.** The supplied fixed U(3)×U(3) orbit pair has identical native measurements but different engineered GT–K4 metrics according to the independent original auditor. This package *independently checks its positive trace-one block-isospectral orbit premises*, but does **not** independently recompute all 15 native observables, six GT values or the SPD metric formula. This is not a new native-15 verification.

**2. Additional operation distinguishes the counterpair.** The unchanged H75 microscopic CPTP source and H81 flag-conditioned SWAP, followed by H75 real Cayley V(0,1/3) and positive site-1 POVM, separate the pair: (sigma minus rho) contrast = -(350208+12288 sqrt(57))/2403125. Executing source reset before any control instead erases the pair. 52 exact SymPy assertions pass in the included script. The executable access is an added AX-OA condition, not derived from F.

**3. Enlarged global 36-record access — conditional.** Four pre-reset programs (I, flag feedback F_fb, V_A then F_fb, W then F_fb then V_B then W then F_fb), the same H75 source, three post-reset choices (I, V_A, V(1/4,1/3)) and site POVMs Q0,Q1,Q2 provide a linear map from Herm(3)⊕Herm(3) (real dimension 18) to R^36. A selected 18x18 rational submatrix has nonzero modular determinant **39156989 mod 1000000007**, so rank is exactly 18 and any *already selected* metric on the fixed KKS orbit factors through these enriched records. The original native-15 NO-GO is unchanged. The longer P3 pre-reset word is independently **not** hardware-certified. This does not establish metric selection, physical KKS→ADM, or generative completeness.

## Reproduction

```bash
python -m pip install sympy==1.14.0
python research/bridge/h75-operational-metric-descent-20261020/H75_Access_Descent_Exact_Audit.py
python research/bridge/h75-operational-metric-descent-20261020/H75_Global_Access_Modular_Verify.py
# Regenerates all 36 rows from the exact H75/H81 operators (more expensive):
python research/bridge/h75-operational-metric-descent-20261020/H75_Global_Access_Exact_Audit.py
```

Two fast CI checks (52-item pair audit and independent CSV modular determinant) run on push and PR; the 69-item full generator and exact result ledgers are committed for independent reproduction. Exact SymPy tests are not a formal Lean theorem, physical experiment or human review.

**Status:** Pairwise access EXACT for specified finite model; global D1 descent CONDITIONAL EXACT with full 36-access; smooth/stable reconstructions conditional on metric regularity and calibration; source/port/scheduling physical certification, frozen P6 provenance, F generation G2/G3, P7/P8 soldering, KKS→ADM and off-shell Einstein dynamics all OPEN.

Baseline: [H75 PR #94](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/94), [H81 PR #100](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/100), [H82 PR #101](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/101).
