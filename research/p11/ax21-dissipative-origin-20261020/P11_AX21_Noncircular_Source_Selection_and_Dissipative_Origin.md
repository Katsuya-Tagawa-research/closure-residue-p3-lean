# P11–AX21 — Non-Circular Source Selection and the Origin of Dissipative Structure

**2026-10-20 (Japan). Status: Draft mathematics only. No human expert peer review, experimental native-source certification, or F-origin proof.**
Upstream AX20 PR #158: if a fully marked pure-dephasing GKSL generator is supplied, its HS-symmetric kernel recovers the observer algebra. AX21 audits whether the source generator can be selected from baseline physical admissibility conditions alone.

## Source-choice ambiguity at d=5

On M_5(C), let D be standard diagonal MASA, E its trace-preserving expectation, R=I-(2/5)11^T an exact orthogonal Householder matrix, D'=RDR^T, E'=Ad_R E Ad_R^T. For gamma>0, L0=gamma(E-I) and L1=gamma(E'-I) are distinct unital CPTP GKSL generators, both HS-selfadjoint, both pure-dephasing channels. Both contract purity:
d/dt Tr(rho_t²)=-2 gamma ||(I-E)rho_t||² <=0 (and analogously for E').
Their fixed algebras are D and D' respectively.

For a=diag(a1,...,a5), the (i,j) offdiagonal entry of R^T a R is
  -(2/5)(ai+aj)+(4/25) sum_k ak.
These equations for all distinct i,j force all ai equal (exact rational constraint rank 4); hence D∩D'=CI. The equally admissible convex average Lbar=(L0+L1)/2 obeys
  -<X,Lbar X>=(gamma/2)(||(I-E)X||²+||(I-E')X||²).
Thus ker Lbar=D∩D'=CI, no selected MASA. Admissible quantum dynamics and entropy/purity monotonicity by themselves do not select H37's specific D.

## Unitary-equivariant symmetry no-go (conditional on bare symmetric input)

For d>=2, no MASA D is invariant under all U(d) conjugations: a MASA contains a rank-one projection and its unitary orbit contains mutually noncommuting rank-one projections. Therefore no fully unitary-equivariant MASA selector exists from only data invariant under all U(d), such as (C^d, tr, I/d). This does NOT rule out independent symmetry-breaking physical inputs.

## A conditional B-to-observer recipe and a CR warning

Given an independently provided **nondegenerate** Hermitian pointer B and kappa>0, the standard GKSL generator
  L(X)=-i[H,X]-kappa[B,[B,X]]
has HS symmetric part -kappa ad_B². Its kernel is C*(B), a MASA. This is a valid conditional source-to-observer construction, **not** an explanation of the origin of B or H.

If B=H with simple spectrum, the selected energy MASA is invariant under L; for every t, Phi_t=e^(tL) preserves it. Hence P3's original hidden filtration and R_k are zero at **every depth**. Thus this naive Hamiltonian-intrinsic pointer choice would suppress the interesting CR return. Requiring [H,B]!=0 produces a nonzero first hidden derivative, but **does not by itself guarantee nonzero genuine P3 residue**: the qubit example B=Z, H=X/2, kappa=1/3 has hidden span CY for all times/depths and all P3 commutator residues zero.

## Decision

- Distinct admissible positive-rate pointer GKSL generators: exact countermodel.
- Mixed-pointer generator loses 5D fixed algebra: exact countermodel.
- Universal MASA selection from unitary-invariant bare input: symmetry NO-GO.
- Independently sourced simple-spectrum pointer B selects a MASA: exact standard conditional theorem.
- B=H forces nonzero P3 residue: FALSE.
- [H,B]!=0 alone forces nonzero P3 residue: FALSE.
- **G2** native source inventory/calibrations and physically exhaustive Hilbert space: OPEN.
- **G3** F noncircularly selects source generator/pointer/control: OPEN.

Scope: exact finite symbolic witness (SymPy 1.14), not generic physical-device verification or proof that all theories cannot select observers. Frozen P1–P8 and main remain unchanged. An independent symmetry-breaking mechanism, rather than circularly prescribing the desired pointer, is required for progress on G3.
