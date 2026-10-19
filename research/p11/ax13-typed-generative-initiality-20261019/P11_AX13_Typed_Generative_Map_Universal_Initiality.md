# P11–AX13 — Typed Generative Map: Initiality, Observer Retraction, and the Residue Boundary

**2026-10-19 | P11 axiomatization (following AX12 Draft PR #150).** This is a foundational type-check and independence audit, **not** a construction of physical F or proof of P11 Generative Completeness.

## A. Literal empty input cannot generate distinguished physics

As a literal set function from the empty set to X, the arrow is unique for every codomain X and has no input elements. It therefore cannot select a point, an observer or a dynamical law. To define F rigorously, distinguish an **initial object in a specified category** from a literal empty-set domain. The signature is substantive input that cannot be hidden behind the empty-set symbol.

## B. Conditional free initiality theorem (standard C*-algebra theory)

Fix signature Σ: two distinguished self-adjoint contractions x,y and a unit. Let C_Σ have objects (A,a,b) with A a unital C*-algebra, a,b in A selfadjoint contractions. Morphisms are unital *-homomorphisms preserving marks. The full unital free product

    U_Σ = C([-1,1]) *_C C([-1,1])

with coordinate generators x,y is **initial** in C_Σ. For every (A,a,b), a unique unital *-homomorphism π:U_Σ→A sends x→a, y→b. Proof: functional calculus gives maps from each C([-1,1]) factor, and the full free-product property extends them uniquely.

This is standard mathematics, not a novel P11 result; it does **not** derive the generator signature from nothing.

The algebraic version C<x,y> has all finite words as basis, with 2^n distinct words of degree n and 2^(N+1)-1 words up to degree N. The C*-norm completion is not the same as polynomial truncation.

## C. Noncommutativity survives formally but not under every realization

A Pauli realization x→X, y→Z sends [x,y] to -2iY ≠ 0, so [x,y] is nonzero in U_Σ. But a valid commuting realization x→Z,y→Z kills the commutator. Initiality guarantees maps for every compatible destination, not faithfulness of every map, nor selection of a physical realization.

## D. Even the observer projection is not uniquely selected

Fix B=C*(x) inside U_Σ. For every real t∈[-1,1], the universal property supplies a *-homomorphic retraction r_t:U_Σ→B, fixing x and sending y→t I. The compositions E_t=j r_t with inclusion j:B→U_Σ are different UCP idempotents onto the same B. In particular E_0(y)=0, E_1(y)=I; observer projection is **not** uniquely selected by initiality.

Each r_t is multiplicative, so its kernel is a closed two-sided ideal. Hence for hidden h in ker r_t, E_t(h*h)=0 and E_t([h,k])=0 for hidden h,k. Thus the universal construction with a multiplicative retraction contains **no forced nonzero visible quadratic hidden return**.

By contrast, in a separate qubit M2 witness, diagonal dephasing Δ_D is UCP and idempotent but nonmultiplicative. For X,Y Pauli,
    Δ_D(X)=Δ_D(Y)=0;
    Δ_D(X*X)=I;
    Δ_D([X,Y])=2iZ ≠ 0.
This is an exact observer-defined algebraic quadratic return. It is **not** by itself the P3 original dynamically generated hidden filtration or R_k.

Tomiyama's conditional-expectation theorem gives properties of specified norm-one projections onto subalgebras; it does not intrinsically select one such projection.

## E. Typed F proposal and noncircularity gate

Propose F_Σ := (U_Σ;x,y), namely an initial structured source relative to an **explicit** signature. This is a mathematical **candidate**, not proof that x=physical Λ, y=physical Ω, that physical [Λ,Ω] remains nonzero, or that the dynamical/observer/CR return arises. Σ as stated has no CPTP semigroup, distinguished physical controls, readout, orientation, locality or original P3 residue.

Additional structure must be introduced by explicitly justified premises or derived with independent proofs. A uniqueness theorem in marked algebra does **not** imply uniqueness of any physical implementation.

## Result and STOP ledger

| Statement | Status |
|---|---|
| Literal map from ∅ selects physical source or observer | NO |
| Universal initial C*-algebra for two SA contractions | EXACT, established |
| Formal commutator [x,y] nonzero in U_Σ | EXACT, Pauli witness |
| Every representation is noncommutative/faithful | NO, commuting quotient |
| Fixed observer B=C*(x) has unique CP retraction | NO, E_t family |
| Initiality alone forces signed hidden quadratic return | NO, multiplicative retraction |
| Separate diagonal expectation supports algebraic return | EXACT, M2 witness |
| Original P3 R_k equivalence; independent CR origin | OPEN |
| G1/G2/G3 operational/source/F completeness | G1 conditional; G2 and G3 OPEN |
| Independent physical P6 gate and P9 Einstein connection | OPEN |

## AX14 direction and reproduction

**AX14:** Seek the minimal compatible dynamics+observer signature under which nonzero residue follows from **independently justified** conditions, not from inserting the desired result as an axiom. If such a premise cannot be justified, hold G2/G3 OPEN rather than expand arbitrary static sector candidates.

Run Python 3.11+, SymPy 1.14:
    python research/p11/ax13-typed-generative-initiality-20261019/P11_AX13_typed_free_generation_audit.py

Expected **1557 exact finite assertions**. These finite assertions do not mechanize the general free C* theorem or constitute human peer review.

Background: universal C* algebra of one SA contraction is C([-1,1]) by continuous functional calculus; full unital free product gives the two-generator universal property. For conditional expectations, see Tomiyama theorem and Brown–Ozawa, *C*-algebras and Finite-Dimensional Approximations*, sec. 1.5.
