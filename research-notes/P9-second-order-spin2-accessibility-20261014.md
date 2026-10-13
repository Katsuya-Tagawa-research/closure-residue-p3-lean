# P9 second-order spin-2 accessibility: exact mathematical proof obligations

Status: mathematical lemmas and conditional mechanisms; **NOT** a Lean-certified statement about P6/P7/P8 physics. 2026-10-14.

## 1. Canonical quadratic tensor map

Let `W=R^3` with Euclidean inner product `h`. Define the symmetric bilinear equivariant map

```math
Q(u,v)_{ij} = u_i v_j + v_i u_j - (2/3) h(u,v) h_{ij}.
```

It takes values in `S^2_0(W^*)` (the spin-2 irreducible 5-dimensional representation).

For `xi=e_3` the TT projection is

```math
Pi_TT(Q(e1,e1)) = diag(1,-1,0),
Pi_TT(Q(e1,e2)) = E12 + E21.
```

These are independent and span the TT plane. SO(3)-equivariance implies the rank-two statement for every nonzero spatial covector `xi` **as a map on all quadratic input pairs**, not as a claim about reachable P6 controls.

More precisely, the polarization of a quadratic response `R(u)=Q(u,u)` gives `Q(u,v)`. If the physically available measurement only probes one restricted parameter trajectory, the induced accessible span can have rank <2 even when the universal bilinear map is surjective.

## 2. Fundamental descent obstruction for P6 response quotient

Let `T=T_x C`, `A=D Sigma_x:T -> O`, `K=ker A`, and `W=T/K`.

A symmetric bilinear second response `H:T x T -> O_2` defines `Hbar:W x W -> O_2` by `Hbar([u],[v])=H(u,v)` **if and only if**

```math
H(k,v)=0 for every k in K and every v in T.
```

Necessity: `[k]=0`. Sufficiency: replacing `u` by `u+k` and `v` by `v+l` leaves `H` invariant by bilinearity and the null property.

The condition does not follow from `D Sigma(k)=0`. Thus one cannot automatically build a spin-2 response by applying `Sym^2` to the first-order response quotient.

Explicit counterexample: `Sigma(x,y)=(x,y^2)` at the origin, on affine coordinates. The first differential kills `e_y`, but the second differential has `D^2 Sigma(e_y,e_y)=(0,2) !=0`. This is a second-order awakening of a first-order silent direction. For a non-affine control manifold, Hessian and covariance require a specified connection or a well-defined second-jet formulation.

A more general second-order accessibility object must therefore use the **full second response jet** (or a separately defined second-order quotient) rather than assuming descent onto `Sym^2 W`.

## 3. Conditional rank-two theorem to hand to P9

Assume:
- A physically defined local second response tensor `H_x` or second response jet, with a well-specified observer/connection convention;
- a physically accessible vector subrepresentation `V_x = 3` with two independently controllable transverse directions for each `xi !=0`;
- SO(3)-equivariance at an isotropic background;
- a nonzero spin-2 coefficient `c_x !=0` in the projection of the second response to `S^2_0`, i.e., on the accessible `Sym^2(V_x)` inputs, `H_x^{(2)}(u,v)=c_x Q(u,v)`, up to fixed representation identifications.

Then `rank(Pi_TT(xi) o H_x^{(2)})=2` for every `xi != 0` on the accessible bilinear input space.

This is a **sufficient theorem with explicit assumptions**, not an output of the already-proved P6 first-order accessibility. To apply it physically, compute a nonzero, calibrated `c_x` directly from the P6 dynamics, and confirm that the actual controls can independently excite the two required transverse bilinear directions.

## 4. No-Go boundary

The 1+3 linear response no-go from PR #33 remains valid under its isotropy/linearity/representation assumptions; the quadratic 3 x 3 -> 5 map does not contradict it.

The mere tensor product decomposition `3 x 3 = 1 + 3 + 5` is not proof of a physical nonzero coefficient. A vanishing coefficient `c_x=0`, inaccessible controls, or a second-jet descent failure prevent an inference of two gravitational-wave polarizations.

## Next formalization order

1. Finish the exact finite TT symbol and scalar+vector quarter-turn No-Go Lean CIs.
2. Independently code the finite `Q` formula, TT projections of `Q(e1,e1)`, `Q(e1,e2)`, and their linearly independent witnesses.
3. Formalize the bilinear quotient descent iff condition and explicit `Sigma(x,y)=(x,y²)` counterexample, without claiming the full physical P6 second jet has been constructed.
4. Only then inspect actual P6/P7/P8 calibrated dynamics for an accessible nonzero spin-2 coefficient. If absent, report a conditional No-Go rather than P9 spin-2 success.
