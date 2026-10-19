# P11–AX03 — Canonical Observer Projection and Non-Circular Selection

**2026-10-19 | P11 axiomatization | stacked on AX02 Draft PR #140.** Distinct from the SPS-H113…H123 physical primitive selection branch. Results are conditional standard operator-algebra mathematics, an exact symmetry-based nonselection theorem, and an explicit H37 observer-versus-fixed-point calculation. No claim of F generative completeness, P6 hardware source, P9 Einstein equations or a new Choi–Effros theorem.

## AX03.1 A canonical trace-preserving observer expectation once its range is independently marked (EXACT; established)

Let A⊆M_d(C) be an **already-specified unital *-subalgebra** and τ=Tr/d. There is a unique **trace-preserving UCP idempotent** E_A:M_d→A whose range is A:

  **E_A=P_A^HS=∫_{U(A')} U(.)U† dμ(U).**

Here A' is the commutant and U(A') its unitary group. The Haar average is UCP, trace-preserving, idempotent, and fixes the double commutant (A')'=A. It is therefore the Hilbert–Schmidt orthogonal projection onto A. To prove uniqueness, any UCP idempotent with range A fixes each a∈A; a, a†a and aa† are all fixed, so the multiplicative-domain theorem makes the map A-bimodular. Trace preservation implies Tr(a†E(X))=Tr(a†X), so it is the Hilbert–Schmidt projection.

Special cases:
- Marked diagonal D_d yields E_D=Δ_D=diagonal-torus twirl (faithful).
- A=CI yields E_CI(X)=Tr(X)I/d.
- Both are canonical **relative to distinct prior choices of observer algebra**.

This is not AX02's most general Choi–Effros projection: its range may not be an algebra under ambient multiplication and its map may not be trace preserving. Choosing a trace-preserving expectation onto a **specified *-subalgebra** is stronger.

## AX03.2 Channel-only, full-unitary covariance cannot choose a proper nontrivial pointer algebra (THEOREM)

Take Φ_p(X)=pX+(1-p)Tr(X)I/d with 0<p<1 and d≥2. This channel is invariant under every unitary conjugation. Let S be a deterministic U(d)-equivariant assignment of an observer **unital *-subalgebra** from the channel alone. Equivariance plus input invariance forces S(Φ_p) to be invariant under all unitary conjugations. Only CI and M_d have this property.

Proof: if an invariant *-algebra contains any nonscalar self-adjoint operator, it contains a nontrivial spectral projection P. By U(d) invariance it contains the orbit of all rank-r projections with r=rank P, 1≤r<d. The complex span of this orbit is M_d: differences generate all traceless Hermitian matrices, and the orbit average gives rI/d. Thus the algebra is full.

Hence **no unitary-covariant, channel-only selection of a proper non-scalar pointer algebra on isotropic data**. This is a bounded No-Go, not a prohibition on scalar/full selectors or on additional externally sourced preparation/readout information.

In d=2, D_Z=span{I,Z} and D_X=span{I,X} are distinct proper MASAs compatible with the same isotropic channel; their canonical expectations Δ_Z and Δ_X differ. Complete covariance of the **input-output pair** is compatible with both and does not establish which physical pointer was used.

## AX03.3 Original H37: dynamic fixed algebra is CI5, while marked pointer algebra is D5

For H37's exact five-site connected nearest-neighbor Hamiltonian (each hopping 1/2) and dephasing gamma=2/3, write Heisenberg generator

  L*(A)=i[H,A]+gamma(Δ_D(A)-A).

For Hilbert–Schmidt inner product,

  **Re⟨A,L*(A)⟩ = -gamma||(I-Δ_D)A||².**

Thus any fixed point L*(A)=0 is diagonal. The connected nonzero hopping graph and [H,A]=0 then force all diagonal entries equal. Therefore

  **Fix(L*)=CI5**, complex dim **1**;

while the independently specified marked pointer algebra D5 has complex dimension **5**. A perfectly canonical dynamical fixed-point rule is therefore **not** a selection of H37's intended nontrivial site observer.

The marked diagonal algebra D5 is not invariant under H37 dynamics: L*(p0)=i[H,p0] is offdiagonal. Thus populations alone are not in general autonomous Markov outputs for arbitrary coherent inputs.

For Schrödinger L and p0=E00, Y01=-iE01+iE10,

  Δ_D(Y01)=0,  **Δ_D L(Y01)=p0-p1**,

  **Δ_D L(p0)=0,   Δ_D L²(p0)=(p1-p0)/2.**

The first is a hidden-phase-to-population **first-order** return. The second gives

  Δ_D exp(tL)(p0)=p0+(t²/4)(p1-p0)+O(t³).

These are exact finite H37 matrix equalities. They exhibit failure of exact population-only Markov closure and delayed observable effects, **not an automatic equality with P3's original generated hidden filtration and quadratic signed R_k**. They do not certify native hardware controls.

## AX03.4 Three logically independent tasks

1. **A provided:** E_A uniquely follows from A plus normalized trace and the conditional expectation assumptions. (EXACT, standard)
2. **Phi provided:** various dynamical algebras such as Fix(Phi†) can be selected under conditions, but neither the isotropic selection theorem nor H37 forces a nontrivial pointer D5 from a channel alone. (EXACT bounded obstruction)
3. **F or CR core provided:** why a physically appropriate observer algebra A is selected, how it relates to P3 residues/P6 hardware, and whether it is compositionally universal. (OPEN)

A defensible next AX04 task: if an independently calibrated effect family {M_a} is given, analyze A_obs=C*(M_a), its associated E_A, and the **separate** invariance/Markov condition E_A Phi=E_A Phi E_A. Never use the target response to reverse-engineer effects or declare source completeness.

## Audit and prior art
Run P11_AX03_canonical_observer_audit.py; expected 119 exact SymPy assertions, covering d=2,3,5 conditional expectations, finite Z3^n twirling, isotropic depholarizing observer alternatives, H37 fixed algebra proof witness and order-1/order-2 returns. The general all-d theorems are mathematical arguments here, not Lean formalizations; CI checks finite examples only.

References: M. Takesaki, *Conditional expectations in von Neumann algebras*, J. Funct. Anal. 9 (1972), 306–321, DOI 10.1016/0022-1236(72)90004-3; I. Nechita and S.-J. Park, *Random Covariant Quantum Channels*, Ann. Henri Poincaré (2025), DOI 10.1007/s00023-025-01558-y; finite-QMS fixed point algebra theory. No human peer review of AX03 has been performed.
