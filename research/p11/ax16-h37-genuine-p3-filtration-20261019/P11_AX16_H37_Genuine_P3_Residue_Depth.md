# P11–AX16 — Authentic H37 P3 Filtration and Exact Quadratic Residue Depth

**19 October 2026.** Stacked on AX15 Draft PR #153. This note uses the *frozen, original P3 definition* rather than an AX14-projected-return substitute. All results are finite, conditional on the explicitly declared H37 GKSL generator. P6 native physical provenance, original P3-to-F independence, P9 Einstein/ADM/HDA and P11 G2/G3 **remain OPEN**.

## A. Correct provenance: original P3, not a renamed K

Let D_5⊂M_5(C) be diagonal, E=Δ_D, Q=I−E. The original P3 defines, for an **actual CPTP map** Phi,

  M_k = span_C{D_5, Phi(D_5), ..., Phi^k(D_5)},
  H_k = Q M_k,
  R_k = span_C{ E([z,w†]): z∈H_i, w∈H_j, i+j≤k } ⊆ D_5^0.

By H_0=0, R_0=R_1=0, so R_2 is the earliest possible nonzero depth. The separate AX14 **linear operator** K=E L Q L E has a different type from P3's **subspace** R_k. AX15 contains exact models showing their nonzero indicators do not imply each other in general.

## B. The fixed exact H37 model

On M_5(C), fix H = 1/2 Σ_{j=0}^3(E_{j,j+1}+E_{j+1,j})+diag(0,1/7,−1/9,2/11,−3/13), γ=2/3, and the standard dephasing GKSL generator

  L(A)=−i[H,A]+γ(E(A)−A).

Use the Hermitian operator basis {p_i, X_ij=E_ij+E_ji, Y_ij=−i E_ij+i E_ji} (25 real basis elements). Its Liouville generator matrix is **exactly rational**, allowing rational matrix inversion and rational Taylor coefficients. The real Hermitian calculation extends complex-linearly to the required P3 spans.

## C. A concrete genuine rational CPTP sampled channel

Define Phi_R=(id−L)^−1. It is **CPTP**, because

  Phi_R = ∫_0^∞ e^(−s) exp(sL) ds

is a normalized positive mixture of genuine CPTP semigroup channels. It is NOT falsely identified with exp(t0 L) at one deterministic sample time.

Compute the actual H_1 of original P3 using h_i=Q Phi_R(p_i), i=0,…,4. The exact 25×25 rational inverse gives

  dim_C H_1=4,
  R_0=R_1=0,
  R_2=span_C{E([h_i,h_j†]): i<j}=D_5^0,
  dim_C R_2=4.

All deeper R_k remain equal D_5^0 by monotonicity. Original P3's quadratic incremental dimension at k=2 is q_2=4; total QDMR is 4.

For h_a=Σ_{i<j} (x_{a,ij} X_ij+y_{a,ij} Y_ij), the diagonal signed commutator is exactly

  E([h_a,h_b])=2i Σ_{i<j}(x_{a,ij} y_{b,ij}−y_{a,ij} x_{b,ij})(p_i−p_j).

The script uses this **actual** P3 commutator formula, rational rank 4 and a full-matrix commutator cross-check; it does not inject arbitrary edge operators into the filtration.

## D. Genuine fixed-time exponential CPTP channel and a nonzero Taylor certificate

Let Phi_t=exp(tL), and define h_a(t)=Q Phi_t(p_a). For each pair a<b, define the REAL diagonal coefficient vector v_ab(t)=diag(E([h_a(t),h_b(t)]))/(2i), whose coordinates sum to zero. All entries are analytic functions in t.

For four pairs (0,1), (1,2), (2,3), (0,3), a rational Taylor expansion verifies:

- The first three v_ab have first nonzero terms at t^6.
- The final v_03 has first nonzero term at t^8.
- The determinant of the first four diagonal coordinates has **exact** first nonzero coefficient

  det(v_01,v_12,v_23,v_03) = −31890017/2655477015413839626240000 * t^26 + O(t^27).

For the unnormalized physical diagonal commutators multiply the determinant by (2i)^4=16. The nonzero coefficient proves analytically that R_2(Phi_t,D_5)=D_5^0 for **every sufficiently small positive sampling time t**. Likewise, Q Phi_t(D_5) has dimension 4 for every sufficiently small positive t since its first-order jet QL(D_5) has rank 4.

By analyticity, rank 4 holds for all t>0 **except possibly a discrete set** of exceptional sampling times. It is not claimed that the rank is 4 for every real t, and no concrete hardware timing range is certified.

## E. Precise relationship to AX14

For the **same fixed H37** L, the separate projected dynamical return K=E L Q L E has rank 4 and image D_5^0 (weighted path-Laplacian image). Thus for the certified resolvent channel and the certified small-t semigroup samples,

  R_2 = im K = D_5^0.

This is **equality of images only**: K and R_2 remain differently typed objects, and the AX15 pair of No-Go models shows no universal implication or identity.

## F. Claims not obtained

- NOT an independent physical P6 source for native X/Y controls, signed current readout, two-stage CPTP gate, or observer/phase/orientation provenance.
- NOT a CR-exclusive prediction against the standard GKSL comparator (the current model IS standard GKSL).
- NOT a derivation of L or Δ_D from the generative map F.
- NOT an Einstein equation, ADM/HDA closure, continuum, or full Generative Completeness.
- NOT a human-reviewed theorem or fully Lean-formalized new analytic lemma.

Frozen P1–P8 and the P3 source are unmodified. AX15 remains valid as a universal nonidentity demonstration; AX16 is a **positive special-model image bridge**.

## Audit

Run with SymPy 1.14.0:

  python research/p11/ax16-h37-genuine-p3-filtration-20261019/P11_AX16_H37_genuine_P3_filtration_audit.py

Expected **59/59 exact checks** and generated JSON preserving all OPEN flags. The Laplace-mixture CP argument and the analytic nonzero-Taylor-coefficient existence argument are in this note; CI verifies their finite algebraic certificates, not physical hardware and not the general theorem in Lean.

**Next:** perturbation and observer-dependence audit (AX17), not more arbitrary static J5 native-control assumptions.
