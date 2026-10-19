# SPS-H121 — Infinitesimal Choi Noise Tangent and Native-Source Separation

**2026-10-19 • P3–P11 Mathematical Bridge / P11 AX-ORIGIN.** This is the independent SPS numbering series; it is not the H75-memory P11 H113 in PR #132. Stacks on SPS-H120 Draft PR #135.

**Result:** exact finite-dimensional GKSL/Choi structure and 78 SymPy assertions on finite witnesses. **Not** an original proof of the 1976 GKSL theorem, a physical P6 source certificate, or P11 Generative Completeness.

## 1. Canonical conditional Choi tangent (exact, known GKSL consequence)

Let Phi_t=exp(t L) be a norm-continuous finite-dimensional CPTP semigroup. Use the **unnormalized** output-first Choi matrix J(T)=sum_ij T(E_ij) tensor E_ij, and column-stacked vec. Put Q=I_{d²}-|I>><<I|/d and

  C_L = Q (d/dt J(Phi_t)|_{t=0}) Q = Q J(L) Q.

For a GKSL representation

  L(rho) = -i[H,rho] + sum_alpha [A_alpha rho A_alpha† - {A_alpha† A_alpha,rho}/2],

write A_alpha^0=A_alpha - tr(A_alpha) I/d. Then

  **C_L = sum_alpha |A_alpha^0>><<A_alpha^0| >= 0**,

and its range, after unvec, is precisely the complex traceless Lindblad span N(L)=span_C{A_alpha^0}, invariant under changes of Lindblad representation.

*Proof:* The gain terms contribute outer products of vec(A_alpha). All loss and Hamiltonian terms have Choi form |B>><<I| + |I>><<B| and vanish after double Q compression. Q vec(A)=vec(A^0). For B the matrix of traceless vec(A) columns, Ran(B B†)=Ran(B), giving the range identity. The rank of C_L is a minimal **traceless noise** multiplicity, not a count of native actuators or actual physical baths.

In finite dimensions the Choi map is linear, so Q J(Phi_t) Q = t C_L + O(t²), with matrix-norm convergence. Pure Hamiltonian evolution has C_L=0 even with nonzero H.

## 2. Recovering canonical Hamiltonian (exact, *full generator* required)

Fix a Hilbert–Schmidt orthonormal basis F_a of traceless d-by-d operators, and set C_ab = <<F_a|C_L|F_b>>. Define the canonical dissipator D_C(rho)=sum_ab C_ab [F_a rho F_b† - {F_b†F_a,rho}/2]. Then

  **L - D_C = -i[H_can, .]**,

with unique H_can modulo real scalar identity. Proof: scalar jump shifts can be absorbed into H, leaving a traceless Lindblad list whose coefficient Gram matrix is exactly C_ab. The difference between two Hermitian H inducing the same commutator lies in the center R I.

Important gauge identity: A->A+cI changes the dissipator by -i[deltaH,.] with deltaH=(i/2)(conj(c)A-c A†); compensate H->H-deltaH to keep L unchanged. Thus individual displayed jumps and Hamiltonian can change while the **canonical gauge-fixed** extracted H remains unique.

## 3. Exact finite witnesses

**Two levels:** H=X/5+Z/7 and traceless jumps Z/2 and E_01/3. Exact symbolic audit verifies rank(C_L)=2, positive Gram identity, representation invariance under jump mixing and scalar shifts, and recovered canonical H coefficients (X,Y,Z)=(1/5,0,1/7). It checks O(t²) projected Choi expansion.

**Actual fixed H37 five-site generator:** L=-i[H_H37,.] +(2/3)(Delta_D-id), with jump representation sqrt(2/3) p_i, i=0…4. Therefore

  **N(L_H37)=D_5^0 = {diag(z_0…z_4):sum z_i=0}, dim_C=4**.

The independently *declared mathematical* native real-exchange K_e=E_{e,e+1}-E_{e+1,e} span four real off-diagonal directions. Their complex span intersects D_5^0 trivially. Equal dimension 4 is not equal microscopic provenance, physically realizable coherent control, or P6 Xi accessibility.

**Native-control non-identification:** Two hypothetical experimental completions with the same full baseline L can have native coherent controls span_R{iX} versus span_R{iX,iZ}, respectively. Nothing in the common baseline Choi first derivative or recovered canonical H resolves that externally supplied one-pulse control inventory. This is a weak-model category counterexample, not a claim about any actual H37 hardware.

## 4. Scope table

| Claim | Status |
|---|---|
| Canonical compressed derivative >=0 and traceless noise support | EXACT / standard GKSL |
| Canonical H modulo scalar from full L and fixed HS gauge | EXACT / conditional |
| H37 dephasing noise dim_C=4, transverse to marked native coherent controls | EXACT / finite algebra |
| Native independent coherent control list from L alone | NO-GO in weak marked expansion class |
| F-derived AX-ORIGIN, physical J_N and native controls, P6 hardware gate | OPEN |
| CR-exclusive GKSL prediction, P9 Einstein/ADM/HDA, P11 Completeness | OPEN |

**Stop rule:** Do not rename N(L) or H_can as the independently selected static primitive set S_static, or report source physics PASS merely because this exact finite CI succeeds. Next SPS-H122, if undertaken, must require an independently calibrated *infinitesimal control family*, or state the source-provenance STOP.

## Reproducibility

Run with Python 3.11 and SymPy 1.14: python research/p11/sps-h121-20261019/P3P11_SPS_H121_infinitesimal_choi_audit.py. Expected **78/78 exact assertions**, generated results JSON, rank 2 on the two-level witness and rank 4 on H37. Analytic proof is in this document, not formally checked in Lean; no hardware experiment or independent human specialist review.

### Literature / priority boundary
V. Gorini, A. Kossakowski, E. C. G. Sudarshan, *Completely positive dynamical semigroups of N-level systems*, J. Math. Phys. 17, 821–825 (1976), DOI 10.1063/1.522979. G. Lindblad, *On the generators of quantum dynamical semigroups*, Commun. Math. Phys. 48, 119–130 (1976), DOI 10.1007/BF01608499.
