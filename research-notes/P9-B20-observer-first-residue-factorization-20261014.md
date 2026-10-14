# P9 B20 — Observer-resolved first residue and exact second-return factorization

**Date:** 2026-10-14. **Status:** exact rational-matrix finite audit candidate, not Lean-kernel formalization or proof of inherited P3/P6 physical reachability. Stacked Draft on B19 PR #39 (which is stacked on B18 #38 and B14 #37). Main and the frozen P3 core remain unchanged.

## Declared finite model and two observational levels

Let `D_4` be the diagonal subalgebra in `M_4(C)`. For each of the six K4 edges `e=(a,b)`, `a<b`, put `K_e=E_ab-E_ba` and `K(x)=Σ_e x_e K_e` for real controls `x ∈ R^6`. The generator is real antisymmetric, so `U_t(x)=exp(tK(x))` is orthogonal/unitary and `Φ_{t,x}(ρ)=U_t(x)ρU_t(x)^†` is CPTP for all real t.

For diagonal preparations `D(p)=diag(p)`, define the *full first-residue matrix response* `R_p(x)=[K(x),D(p)]` and the *population first-time response* `C_D R_p(x)=diag R_p(x)`. These are **different observation channels**:

```math
R_p(x)_{ab}=x_{ab}(p_b-p_a)\quad(a<b),\qquad
C_D R_p(x)=0.
```

The first relation makes the full coherent response a possible faithful first-residue observation, whereas the second says all six edge directions are silent for first-time *population-only* observation.

The two positive mixed preparations already used in B18/B19 are

```math
p_1=(3,3,1,1)/8,\qquad p_2=(3,1,3,1)/8.
```

For each edge e=(a,b), at least one preparation has `p_{j,b}-p_{j,a} ≠0`. Therefore choose that j and define the exact linear left inverse

```math
\ell_e(R_{p_1}(x),R_{p_2}(x))
=\frac{(R_{p_j}(x))_{ab}}{p_{j,b}-p_{j,a}}=x_e.
```

Consequently the joint **coherence-resolved first-time response** on these two preparations has rank exactly **6**. Each preparation alone has rank **4**, and the **population-only first-time response** has rank **0**. Thus the full first-residue map is *already faithful in this declared K4 model*, without demanding six different preparations. This does **not** assert that actual P6 first-residue observables include these coherences or controls.

## Algebraic quadratic return and factorization through the full residue

For the same declared dynamics,

```math
q_p(x)=\frac12\left.\partial_t^2\operatorname{diag}\Phi_{t,x}(D(p))\right|_{0}
=\frac12\operatorname{diag}[K(x),[K(x),D(p)]]
=-A_{x^2}p.
```

The mixed-edge terms for distinct e,f cancel on the diagonal. The **second control differential** of this already second-time-order response is

```math
D_x^2q_p(x)[u,v]=-2A_{u\odot v}p,
```

independently of x. Distinguish this from `∂_t²`: there are two distinct differentiation variables, *physical evolution time* and *external edge controls*.

With the P7 `h=4⟨,⟩` Hadamard frame and the B18 TT extraction, set

```math
y(x)=T(x_e^2)_e,\quad
T=\begin{pmatrix}
-1&1&0&0&1&-1\\
0&0&1&-1&0&0
\end{pmatrix}.
```

Writing `\mathcal R(x)=(R_{p_1}(x),R_{p_2}(x))` and using the explicit left inverse `\ell`, the B19 second-control response obeys the exact factorization

```math
D^2_xy(x)[u,v]
=2\sum_eT_e\ell_e(\mathcal R(u))\ell_e(\mathcal R(v)).
```

Therefore the B19 obstruction **is not an obstruction to descent through the full first-residue observer**: that map is injective and admits a bilinear factorization. Conversely, no nonzero second return can descend through the entirely silent population first-time response. At the nonzero uniform control point, the separate *first differential of the extracted quadratic TT readout*, `D_xy(x_\star)`, has rank 2 and still fails second-jet descent, as B19 proves. These are three distinct notions, not interchangeable.

## Finite permutation covariance and access limitations

For every `σ∈S4`, simultaneous conjugation `K↦Pσ KPσ^{-1}` and `D(p)↦Pσ D(p)Pσ^{-1}` commutes with the first commutator and diagonal second-return operations. All 24 permutations are audited against all six edge basis controls and the two preparations using exact fractions. **This is finite K4 permutation covariance**, not proof that the fixed-frame TT coordinates are invariant under the entire S4, not continuous SO(3) physical control symmetry, and not Lorentz covariance.

The script also checks `rank w↦(q_{p1},q_{p2})=5` and independent edge-amplitude sign ambiguity for the population-only readout, even though the coherence-resolved first-order response separates opposite signs.

## Interpretation / minimum gate for P3→P6→P9

This supplies a constructive **finite closure–residue-compatible unitary example** with a faithful coherent first-residue observable and a nontrivial diagonal quadratic return whose extracted TT coordinates factor through that faithful observable.

It **does not establish a morphism from the inherited P3 two-level unitary witness or calibrated P6 exchange+dephasing control tangent to the K4 six-dimensional control space**. In particular no independently calibrated six-edge P6 first-residue physical accessibility, observer permission to measure offdiagonal coherences, experimental signal/noise, SO(3)-equivariant dynamical spin-2 propagation, second-jet gauge descent in a physical quotient, continuum gluing, variational action, or Einstein equations have been derived. The standard GKSL comparator still prevents a claim of CR-specific necessity from the conductances alone.

The next meaningful structural gate is an *explicit admissible control embedding* `Z_{P6}^{physical}→span_R{K_e}` with its genuinely measured observer map, plus a verified rank condition and covariance properties, or a finite no-go if those assumptions cannot hold.

## Reproducibility

`P3/K4B20ObserverResidueExactCheck.py` uses only Python standard-library `fractions.Fraction`, matrix multiplication/commutators, exact rank elimination, and all 24 vertex permutations. All tested algebraic identities are exact; no sampling-based numerical tolerances. The symbolic formula for arbitrary controls follows by matrix-unit expansion and polarization, and the checker verifies it on edge basis, pairs, and additional rational combinations. GitHub Actions is the independent execution environment, not a human expert review.
