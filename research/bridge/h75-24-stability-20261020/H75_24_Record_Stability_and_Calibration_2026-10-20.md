# H75/AX-OA — 24-Record Stability and Calibration Gate

**2026-10-20 | Independent P3–P11 Mathematical Bridge continuation | conditional finite result.**

## Boundary and relation to prior work

Stacked on Draft PR #166 (resource-subset rank audit), which is stacked on #165 (phase orientation) and #164 (global rank-18 enlarged-access certificate). Uses the **unchanged original H75/H81 six-level four-Kraus channel**, four pre-reset programs P0–P3, three post-reset programs T0–T2, and site-projector readouts. Input is only the **18-dimensional real linear space** Herm(3) ⊕ Herm(3) of flag-block-diagonal operators. Not an assertion about generic flag coherences, the original native-15 metric descent, laboratory implementability, P6 origin, F completeness, or KKS→ADM gravity.

For each unordered pair of site effects (i,j), form the 24×18 *real rational* probability-response matrix C_ij, using four P settings × three T settings × the two retained positive site projectors. In each 3×3 block take E_00,E_11,E_22, then the real and imaginary Hermitian generators E_jk+E_kj and i(E_jk-E_kj) in lexicographic pair order. This basis is **not Hilbert–Schmidt orthonormal**. The physical controls and Kraus operators are reproduced in the checker; no arbitrary replacement dynamics is introduced.

## Independently computed rank and numerical conditioning

| retained site pair | exact rational rank | approx. sigma_min | approx. kappa_2 | approx. norm(C^dagger)_2 |
|---|---:|---:|---:|---:|
| Q0,Q1 | 18 | 0.0691704520 | 65.6779008 | 14.4570401 |
| Q0,Q2 | 18 | 0.0575030074 | 74.7489091 | 17.3903948 |
| Q1,Q2 | 18 | 0.0445355709 | 102.6101947 | 22.4539616 |
| Q0,Q1,Q2 (36 effects) | 18 | 0.0863960273 | 56.7037587 | 11.5746063 |

These singular values/condition numbers are **coordinate-dependent numerical diagnostics**, not exact algebraic equalities, laboratory error measurements, or a global hardware optimality proof. In this specified three-choice catalog, Q0,Q1 is the best of the three 24-effect choices by sigma_min and kappa_2.

## EXACT rational spectral lower bounds

The checker constructs every entry of each C_ij as an exact SymPy rational and verifies positivity of *all 18 rational LDL pivots* of C_ij^T C_ij - a_ij^2 I_18:

- (Q0,Q1): a_01 = 3/50 = 0.06
- (Q0,Q2): a_02 = 1/20 = 0.05
- (Q1,Q2): a_12 = 1/25 = 0.04

Therefore **in the declared unnormalized coordinate Euclidean norm**:

sigma_min(C_01)>3/50,  sigma_min(C_02)>1/20,  sigma_min(C_12)>1/25.

This proves exact injectivity and a quantitative linear inverse bound, independently of floating-point SVD. If the actual calibrated 24×18 matrix equals C_01+Delta with ||Delta||_2 < 3/50, then by Weyl's singular-value perturbation inequality it remains injective. This is a **sufficient mathematical tolerance conditional on independent source and port calibration**. It does not certify that a physical error is this small or that unknown nonlinear model mismatch can be modeled by such a Delta.

For N independent Bernoulli shots **per effect**, model-correct state x, exactly known C_ij and least-squares estimator xhat, Hoeffding and the union bound yield with probability at least 1-delta:

||xhat-x||_2 ≤ sqrt(m)/sigma_min(C_ij) * sqrt(log(2m/delta)/(2N)), m=24.

At N=100000 and delta=0.05 the numerical bounds using floating-point sigma_min are approximately 0.4150 (Q0,Q1), 0.4992 (Q0,Q2), and 0.6446 (Q1,Q2), versus approximately 0.4188 for 36 records **at the same per-effect N**. The 24-record scheme uses 2.4 million trials against 3.6 million at that per-effect sampling level; this comparison does not account for different hardware acquisition costs/correlations, drift, or calibration noise. Using only the rigorous a_01=0.06 in place of sigma_min yields a conservative exact-parameter probability bound.

## Meaning for metric descent and physical provenance

Because every C_ij is injective on Herm(3)⊕Herm(3), any chosen GT–K4 metric g **where defined** on any included fixed block-unitary orbit factors uniquely through each C_ij on its image. If g has Lipschitz constant L_g in the declared source norm, the descended map has Lipschitz constant at most L_g/sigma_min(C_ij). Without an independent bound on L_g near metric-cone degeneracy, there is NO uniform numeric metric-error guarantee.

The original **native-15 GT–K4 descent NO-GO** is not rescinded: the 24 new outputs require external AX-OA control/readout assumptions. The flagship P9/P11 gates remain OPEN: preparability of a sufficiently complete positive-state family, full lengthy pre-reset schedule permission, independently anchored imaginary phase reference, Kraus/port/readout calibration, frozen P6 J_N provenance, source-derived physical soldering, KKS–ADM/DeWitt/off-shell HDA/Einstein, and generative completeness. This is a **strictly scoped calibration proof**, not a CR-specific experimental signature.

## Reproducibility

Run the local exact checker H75_24_Record_Stability_Exact.py with SymPy and NumPy. It regenerates source matrices, the complete 36×18 response, three 24×18 submatrices, rational ranks and LDL certificates, and separately prints floating-point SVD diagnostics. Numerical approximations do not underwrite the exact theorem.

**Status:** research Draft, unmerged, no human peer review or laboratory verification. Main and frozen/published P1–P8 unchanged.
