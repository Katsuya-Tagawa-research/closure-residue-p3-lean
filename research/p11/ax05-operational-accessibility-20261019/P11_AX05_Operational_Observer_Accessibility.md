# P11–AX05 — Operational Observer Accessibility and the Generative Source Gate

**2026-10-19 | P11 axiomatization | Draft research.** Stacks on AX04 PR #142. SPS-H113–H123's primitive-source STOP continues to apply. Status: standard finite quantum observability theorems, exact qubit and H37 witnesses, **109 exact SymPy assertions**, independent physical measurement instruments **NOT CERTIFIED**, P11 Generative Completeness **OPEN**.

## AX05.1 Conditional finite operational observability theorem

**Declare the protocol before analyzing the target.** Fix terminal POVM settings with effects M_a, each summing to I, and a **marked** finite alphabet of known CPTP channels Phi_b. Allow **finite control-channel words followed by one terminal measurement on a fresh state preparation**. The family does **not** automatically include mid-circuit selective measurement, feedback, ancilla/environment access, unmarked physical controls or arbitrary algebraic products.

Writing Psi_b=Phi_b† for the UCP Heisenberg maps, define
\[
 O_{\rm op}=\operatorname{span}_{\mathbb C}
 \{\Psi_{b_1}\cdots\Psi_{b_k}(M_a):k\ge0\}.
\]
**Exact finite closure:** Starting from O_0=span{M_a}, set
\[
 O_{k+1}=O_k+\sum_b\Psi_b(O_k).
\]
The increasing chain stabilizes in at most d²−dim_C O_0 strict steps and is the *minimal invariant linear space* containing the POVM effects. It is self-adjoint and contains I, but need **not** be an algebra. Linear combinations of measured effect expectations are data post-processing **across separate runs**; such combinations are not assumed to be native physical POVM elements.

**Indistinguishability/complete readout:** Two density matrices rho,sigma give identical outcome probabilities for every allowed word iff Tr[A(rho−sigma)]=0 for every A in O_op. Arbitrary state determination is mathematically possible iff O_op=M_d(C). For a proper self-adjoint operator system, choose nonzero traceless Hermitian Z orthogonal to it; I/d ±epsilon Z for sufficiently small epsilon are two different legitimate, indistinguishable states. This theorem says nothing about whether a requested initial state is independently preparable in a laboratory.

## AX05.2 A qubit counterexample to interpreting AX04 *-algebra generation as readout access

Take only terminal X-basis POVM (I±X)/2 and a marked repeatable unitary U=diag(1,i) **before** the detector. With Psi=Ad_U†, Psi(X)=−Y, Psi(Y)=X. Then

\[
 O_{\rm op}=\operatorname{span}\{I,X,Y\},\quad\dim_{\mathbb C}=3,
 \qquad C^*(O_{\rm op})=M_2(\mathbb C),\quad\dim_{\mathbb C}=4.
\]
The product XY=iZ generates the missing algebra direction, but a product of abstract observables is not a native terminal detector. The two *different* input states rho_±=(I±Z)/2 produce identical terminal-X outcome probabilities after **every** permitted U^k; the difference Z is orthogonal to O_op. If a **separately calibrated** Z-basis terminal POVM is added, the measurement span becomes all M2. The contrast is exact and within a fixed specified protocol alphabet. Allowing intermediate adaptive measurements or other channels changes the protocol and may alter the conclusion.

## AX05.3 H37 positive conditional witness: ideal time-resolved population POVMs span all M5

Use the fixed H37 five-site GKSL semigroup generator
\[
 L(\rho)=-i[H,\rho]+\tfrac23(\Delta_D(\rho)-\rho),\quad
 H=\tfrac12\sum_{e=0}^3 (E_{e,e+1}+E_{e+1,e})
 +\operatorname{diag}(0,\tfrac17,-\tfrac19,\tfrac2{11},-\tfrac3{13}).
\]
Assume all five population effects p_i are independently **marked** available readouts and every freely chosen known duration t in a nonempty open interval is permitted as a repeatable operation with ideal timing and fixed calibrated dynamics. Put T=L† and
O^(k)=span_C{T^j p_i:0≤j≤k,0≤i≤4}.

Exact symbolic rational-Hermitian 25-dimensional calculation gives

\[
\boxed{\dim O^{(0..7)}=(5,9,13,17,21,23,25,25).}
\]

This is a **linear** dynamic observability filtration, as distinct from AX04's *multiplicative* one-step C*(D_5,T(D_5))=M5. Since e^{tT} is analytic and the T-Krylov space is finite, its time orbit over **any open time interval** has the same span as {T^k p_i}: containment follows from Cayley–Hamilton; the reverse follows because any functional annihilating every sampled time orbit is identically zero as an analytic function and therefore annihilates every derivative. Thus at most 25 suitable effect/time pairs exist in principle whose statistics separate arbitrary states.

**Scope:** Existence of mathematical times does not supply calibrated times, device coherence, initial-state preparation, phase reference, SPAM errors or a robust tomography conditioning bound. It is fully consistent with standard GKSL quantum mechanics. It does **not** certify the P6 native coherent tangent J_N, signed hidden edge-current hardware readout, a CR-exclusive response gap, or source selection from F.

## AX05.4 Noncircular physical observer gate (proposed, not passed)

1. **Independent POVM/instrument source:** detector identity, effect matrices, outcome labels, efficiencies, phase and pointer reference fixed before target responses.
2. **Allowed operations:** independently marked native control/channel family, ordering, timing, free versus adaptive instrument protocols, environment/ancilla access.
3. **Preparation:** a demonstrably available set of states with sufficient independent linear span for the desired comparison.
4. **Operational design matrix:** experimentally calibrated ranks, uncertainties, drift and condition numbers; symbolic exact rank is not an actual physical certification.
5. **Prediction gap:** prospective, matched standard-GKSL comparator versus P6/CR physical prediction on **the same instrument alphabet**, independently locked before data.
6. **Reviewability:** device model, source documentation, protocol versions, raw data hashes and independent operator/experimental verification.

## Honest proof-gate ledger

| Claim | Status |
|---|---|
| Finite word-effect observability space and indistinguishability criterion | **EXACT** (established linear observability) |
| Generated *-algebra implies operational full tomography | **NO**; qubit 3 vs 4 counterexample |
| H37 fixed mathematical semigroup + ideal time-resolved marked population effects spans M5 | **EXACT conditional**; Krylov ranks 5,9,13,17,21,23,25 |
| Real device can implement the assumed channels/times/POVMs and calibrate rank/conditioning | **OPEN** |
| H37 physical P6 coherent-source provenance and CR-exclusive readout | **OPEN** |
| Observable word-space equals original P3 generated hidden filtration/residue R_k | **OPEN** |
| Observer effect choice is generated uniquely by F | **OPEN** |
| P9 Einstein/ADM/HDA and P11 Generative Completeness | **OPEN** |

**Prior-art boundary:** D. D'Alessandro, *On quantum state observability and measurement*, J. Phys. A 36 (2003), 9721, DOI 10.1088/0305-4470/36/37/310; N. Yamamoto, K. Tsumura, S. Hara, *Local reachability and local observability of quantum control dynamics*, Trans. SICE 40 (2004), 1078–1087, DOI 10.9746/sicetr1965.40.1078. The general observability machinery is standard. The AX05 contribution is a **specific H37 finite exact calculation and program-specific logical boundary audit**.

Reproduce with SymPy 1.14: python research/p11/ax05-operational-accessibility-20261019/P11_AX05_operational_accessibility_audit.py. General analytic statements are proved here but not Lean-mechanized; finite CI does not constitute human review or experimental certification.

**Next gate AX06:** require independently sourced instrument/protocol families or give an explicit conditional categorical axiom; do not create arbitrary new J5 sectors or upgrade mathematical accessibility to experimental P6 PASS.
