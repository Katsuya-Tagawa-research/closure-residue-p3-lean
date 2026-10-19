# P11–AX02 — Observable Quotient Algebra and Quadratic-Return Compatibility

**2026-10-19 • P11 axiomatization** (separate from SPS-H113–H123). Follows AX01 Draft PR #139; no physical-source, P6, GR or Generative Completeness claim.

## 1. Ordinary product descent: exact iff-ideal theorem and full-matrix No-Go

For an associative complex algebra A and linear subspace N, the prescription (a+N)(b+N)=ab+N is representative-independent **iff N is a two-sided ideal**. Proof: replacing a by a+n (and likewise b) forces nb and an to lie in N. The converse is immediate by expanding (a+n)(b+m).

M_d(C) is a simple algebra: if a two-sided ideal contains x with x_ij≠0, E_ki x E_jl=x_ij E_kl belongs to that ideal, for arbitrary k,l. Consequently, a nonzero proper hidden N in M_d **does not admit the inherited full-matrix quotient product**. This does not forbid other observed operator-algebra structures.

For qubit diagonal dephasing Δ_D, N=span_C{E01,E10} is invisible linearly, but
Δ_D(E01E10)=p0, Δ_D(E10E01)=p1, Δ_D([E01,E10])=p0-p1≠0.
This is an exact **algebraic quadratic return**, not an identification of N with the original P3 dynamically generated hidden filtration.

## 2. The conditional Choi–Effros remedy (established 1977 theorem)

If E:A→A is a **unital completely positive idempotent**, E²=E, then R=Ran E is a C*-algebra in its inherited operator-system order, adjoint and **Choi–Effros product**

  a ∘_E b := E(ab),  a,b ∈ R.

This is the established **Choi–Effros theorem**, not a novel P11 theorem. It is a **new product on the range**, not a product on arbitrary representatives of A/ker E induced by ambient multiplication.

Citation: M.-D. Choi and E. G. Effros, “Injectivity and operator spaces,” J. Functional Analysis 24(2), 156–209 (1977), DOI **10.1016/0022-1236(77)90052-0**.

### Exact M3 UCP witness: range is not ambient algebra, but CE-algebra M2

Define α:M3→M2 to be compression to the first two levels and define ι:M2→M3 by
ι(A)=diag(A,tr(A)/2), with the upper 2×2 block A. Both are unital CP; αι=id. Thus E=ια is a UCP idempotent.

Explicit Heisenberg Kraus: V0=p0+p1, V1=E02/sqrt(2), V2=E12/sqrt(2), so
E(X)=Σ Vj† X Vj and ΣVj†Vj=I3.

R=ι(M2) has complex dimension 4 and is not closed under ordinary matrix multiplication: z=ι(diag(1,-1))=diag(1,-1,0) belongs to R, while z²=diag(1,1,0) does not. Yet **z∘_E z=I3** and, generally,
ι(A)∘_E ι(B)=ι(AB).
Therefore (R,∘_E) is exactly *-isomorphic to M2. The ambient kernel has dim_C 5 and is not an ideal.

### Compatible UCP dynamics

For U=[[0,1],[1,0]], put T=ι∘Ad_U∘α. This UCP map obeys ET=TE=T. On (R,∘_E), the restricted dynamics is the *-automorphism ι(A)↦ι(UAU†). All four matrix-unit multiplication identities, 64 associativity triples, and finite Kraus unitality are checked symbolically.

More generally if E is UCP idempotent and T is UCP satisfying **ET=ETE**, then E T|R induces a UCP *linear* dynamical map of the CE operator system. This is not necessarily a *-homomorphism; the swap above satisfies the stronger condition by construction. Compatibility is an **extra condition**, not a consequence of arbitrary AX01 linear closure.

## 3. Quadratic return and the faithfulness gate

For x∈ker E, Kadison–Schwarz gives

  Γ_E(x) := E(x†x) ≥ E(x)†E(x)=0.

If E is **faithful** (E(x†x)=0 implies x=0), then Γ_E(x)≠0 for every nonzero hidden x. Diagonal dephasing Δ_D is faithful and Δ_D(E01†E01)=p1.

**CP alone is insufficient:** in the M3 witness, nonzero x=E02 is hidden but
E(x†x)=E(p2)=0.
Meanwhile the hidden y=E20 has E(y†y)=E(p0)=ι(E00)≠0, and
E([E02,E20])=ι(E00)≠0.
A hidden direction may have zero positive ordered-square return, nonzero reverse-square return, or nonzero signed commutator return. These witnesses are algebraic/observer-defined and **not** the original P3 R_k without further proof.

## 4. Exact compatibility with AX01's nonsplit CPTP hidden extension

The column-stochastic AX01 model is

  P = [[1,1/2,1/4],[0,1/2,1/4],[0,0,1/2]],
  C = [[1,1,0],[0,0,1]],
  B = [[1,1/2],[0,1/2]], with CP=BC.

Its Heisenberg observed algebra A_vis={diag(a,a,b)} is a **genuine unital commutative subalgebra** preserved by the dual of the original CPTP measure-and-prepare channel. Visible dynamics acts as Bᵀ on (a,b), so positive Markov closure is exact. Yet the **microscopic state-space extension does not split**: the section-independent residue coefficient difference remains -1/4 (AX01). Positive observer-algebra dynamics and a nonsplit microscopic extension coexist without contradiction.

Do not silently identify the two-outcome **classical** output with a unique full M2 output-qubit channel, or the state-space section obstruction with a P3 commutator residue.

## 5. P11 proof-gate ledger

| Result | Status |
|---|---|
| Ordinary product descends iff invisible kernel is two-sided ideal | EXACT |
| Nontrivial proper M_d ordinary quotient with inherited multiplication | NO-GO |
| UCP projection gives CE product C*-algebra | EXACT **established literature**, conditional on E |
| Non-ambient M3 CE M2 example and compatible UCP dynamics | EXACT finite witnesses |
| Positive Γ_E; nonzero for every nonzero hidden under faithfulness | EXACT |
| Positive Γ_E nonzero for every nonzero hidden with mere CP | NO-GO |
| AX01 observable classical algebra and nonsplit state extension coexist | EXACT finite witness |
| E canonically and noncircularly selected by F or finite P3 CR core | OPEN |
| CE Γ_E rigorously identified with original P3 filtration residue R_k | OPEN |
| P6 physical gate/native-source provenance, P9 Einstein/ADM/HDA, P11 Generative Completeness | OPEN |

## Reproducibility and limits

Run \`python research/p11/ax02-observable-quotient-algebra-20261019/P11_AX02_observable_quotient_algebra_audit.py\` (SymPy 1.14.0). Expected **204/204 exact symbolic assertions** and generated JSON. The general Choi–Effros theorem is cited, not Lean-mechanized here; CI checks finite examples, not physical hardware or peer review. Next AX03 should seek an **independently justified selection rule** for the CP observer E and rigorous contact with original P3 R_k; merely choosing E to force a desired quadratic residue is circular.
