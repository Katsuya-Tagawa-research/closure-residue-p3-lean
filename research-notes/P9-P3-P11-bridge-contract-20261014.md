# P9 ⇄ P3–P11 mathematical bridge: conditional proof contract

Date: 2026-10-14. This is a **research specification and mathematical argument**, **not** a Lean-certified theorem except for the two finite lemmas in `P3/P9TTFiniteSymbol.lean` if dedicated CI passes.

## A. Observable-to-tensor bridge

Let `R_x := T_x C / ker(D Sigma_x)` be the finite observer response quotient, with its representation of the stabilizer of the local observer.

Let `(S_x,h_x)` denote the P7 3-dimensional Euclidean spatial response fiber. A spatial, observer-covariant linear tensor bridge is a field of equivariant maps

```math
 B_x : R_x -> Sym^2(S_x^*).
```

With the spatial coframe `e_mu^a`, its covariant (observer-dependent) 4D-tensor representative may be written

```math
 delta g_{mu nu}(r) = e_mu^a e_nu^b B_x(r)_{ab}.
```

This is only a spatial symmetric-2-tensor map; constructing every component of an unconstrained 4D metric perturbation is a separate obligation. Covariance includes transforming the observer/coframe data, rather than silently fixing a preferred Lorentz frame.

The required equivariant representation is

```math
 Sym^2(S_x^*) = 1 (+) 5.
```

A response quotient with *only* `1 (+) 3` cannot carry a nonzero equivariant linear map onto `5`. The current P6/P7 vector reclosure therefore **does not by itself provide** a linear spin-2 observable-to-tensor bridge. A new spin-2 sector, higher response jets, a non-isotropic background, or a demonstrated nonlinear mechanism is needed. The mere representation identity `3 x 3 = 1 + 3 + 5` is not an accessibility proof.

## B. Two-polarization accessibility

For a nonzero spatial covector `xi` define the orthogonal transverse projector

```math
 P_i^j(xi) = delta_i^j - xi_i xi^j / |xi|^2.
```

In dimension three, the spatial TT projector is

```math
 (Pi_TT(xi) q)_ij =
 (P_i^k P_j^l - (1/2) P_ij P^{kl}) q_kl.
```

For `xi=e3`, using tensor coordinate ordering
`(q11,q22,q33,q12,q13,q23)`, the rank-2 representative is

```math
 T = [[1,-1,0,0,0,0],
      [0, 0,0,1,0,0]].
```

Its two coordinates represent the plus and cross polarizations. The conformal+diffeomorphism principal symbol in gauge parameter order `(v1,v2,v3,f)` is

```math
 G = [[0,0,0,2],
      [0,0,0,2],
      [0,0,2,2],
      [0,0,0,0],
      [1,0,0,0],
      [0,1,0,0]].
```

Elementary linear algebra: `rank(T)=2`, `rank(G)=4`, `T*G=0`, and `ker(T)=im(G)`. The TT quotient is therefore 2-dimensional. The kernel equality and rank(G) are **not** claimed as Lean-certified by the current two-lemma module.

**Actual CR accessibility:** For a response-to-tensor principal symbol
`sigma(B)_xi : R_x -> Sym^2(S_x^*)`, define

```math
 A_xi = Pi_TT(xi) o sigma(B)_xi.
```

The P9 target is `rank(A_xi)=2` for **every** `xi != 0`; `rank(T)=2` alone does not imply that target.

### Isotropic 1+3 no-go

Under the stabilizer `SO(2)_xi`, a scalar+vector input has weights `0,0,+/-1`, whereas the TT fiber has helicity `+/-2`. For a covariant linear symbol `A_xi` at an isotropic background, an `SO(2)_xi` intertwiner between these spaces vanishes. Thus

```math
 R_x = 1 (+) 3  ==>  A_xi = 0
```

under these assumptions. This obstruction does not cover new spin-2 response inputs, anisotropic backgrounds, or nonlinear observables.

### Conditional sufficient mechanism

If `R_x` has an accessible `5 = Sym^2_0(S_x^*)` summand, and `B_x` restricted to it is `c_x id` (up to a chosen equivariant identification), with `c_x != 0`, then
`rank(Pi_TT(xi) o B_x)=2` for every `xi != 0`. Proving that the **physical CR response quotient actually has such a summand and map** is outstanding.

## C. Finite CR / P1 near-identity compatibility

Let `V=M_N(C)` (finite dimensional), let `D <= V` be the designated diagonal seed space and let `L` be the P1 generator. Define

```math
 K_L = span{ L^j d : d in D, j >= 0 }.
 K_Delta = span{ Phi_Delta^j d : d in D, j >= 0 }.
 A_Delta = (Phi_Delta - I)/Delta.
```

**Conditional theorem (mathematical proof):** Assume `A_Delta -> L` in operator norm and `Phi_Delta K_L <= K_L` for all sufficiently small positive `Delta`. Then `K_Delta=K_L` for every sufficiently small `Delta>0`.

*Proof:* For nonzero `Delta`, the binomial relations between
`Phi_Delta=I+Delta A_Delta` and `A_Delta=(Phi_Delta-I)/Delta` imply
`K_Delta=span{A_Delta^j D:j>=0}`.
The invariant-subspace assumption gives `K_Delta <= K_L`.
Choose finitely many vectors `L^{j_a}d_a` that form a basis of `K_L`.
The corresponding `A_Delta^{j_a}d_a` converge to those basis vectors and remain linearly independent for sufficiently small positive `Delta`.
Thus `dim K_Delta>=dim K_L`, proving equality.

For the **exact semigroup** `Phi_Delta=exp(Delta L)` the invariance assumption follows automatically because `K_L` is `L`-invariant. This is a finite-dimensional continuous-to-discrete *saturated reachable-space* compatibility result. It does **not** identify each finite-depth filtered subspace at every `k`, nor all higher CR defect/return operators without further work.

If the P3 hidden subspace is defined by the fixed linear off-diagonal projector `Q=I-delta` as `Q K`, equality of saturated reachable spaces implies equality of the corresponding hidden images.

**Failure without invariance:** Let `X` be Pauli X,
`U_Delta=exp(-i Delta^2 X)`,
`Phi_Delta(M)=U_Delta M U_Delta^dagger`.
Each `Phi_Delta` is CPTP and
`(Phi_Delta-I)/Delta -> 0`, hence `L=0` satisfies the P1 first-order near-identity condition. But `Phi_Delta(Z)` develops a nonzero Y component for every sufficiently small positive `Delta`. Thus `K_Delta` strictly contains the diagonal seed space while `K_L=D`. This disproves any unconditional closure preservation theorem based only on the first-order P1 hypothesis.

Also, the fixed involution `Phi(M)=U M U^dagger` in P3 PR #28 is not itself a family tending to identity as `Delta->0`; an explicit continuous family and limit compatibility proof must be constructed rather than assumed.

## Freeze/verification gates

1. Independent finite symbol rank and gauge annihilation Lean CI, no `sorryAx`.
2. Gauge rank/TT quotient kernel equality Lean proof.
3. Construct equivariant `B_x` from *actual* P6/P7/P8 response data.
4. Determine `rank(A_xi)` for every nonzero `xi`; publish a no-go if it is generically zero.
5. Formalize saturated closure compatibility and counterexample in finite Lean.
6. Only after these gates consider transferring conditional spin-2 accessibility assumptions into P9 dynamics.

No Einstein equations, propagating gravitational-wave dynamics, universal generative completeness or finite-to-infinite theorem is established by this note.
