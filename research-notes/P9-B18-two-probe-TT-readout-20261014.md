# B18 — TT-only short-time K4 readout with two calibrated preparations

**Date:** 2026-10-14. **Scope:** finite rational linear-algebra calculation, not a Lean theorem and not a physical P3/P6-to-TT accessibility result. Stacked on draft B14/B17 PR #37, without modifying `main` or frozen P3.

## P7-compatible rational spatial frame

Let `S=1^perp ⊂ R^4`, `h=4⟨·,·⟩`. Define Euclidean orthonormal Hadamard vectors

```text
f1=( 1, 1,-1,-1)/2
f2=( 1,-1, 1,-1)/2
f3=( 1,-1,-1, 1)/2.
```

Then `e_i=f_i/2` is **h-orthonormal**. For `A_w=Σ w_ab r_ab r_ab^T`, define the h-tensor coordinates `q_ij=h(e_i,A_w e_j)=f_i^T A_w f_j`. At `xi=e3` the finite TT readout is

```text
TT_plus=q11-q22 = -w01+w02+w13-w23
TT_cross=q12    =  w03-w12.
```

This is a *coordinate projection* of the conductance tensor in a declared frame, not a proof of spin-2 propagation. A nonorthonormal K4 edge basis must not be inserted directly into the P9 TT symbol.

## Operational quadratic readout and a two-probe construction

For a diagonal prepared population `p`, the declared coherent family in PR #37 yields the half-Hessian `H_p=(1/2)diag Φ''(0)=-A_w p`. Choose strictly positive normalized mixtures

```text
u=(1,1,1,1)/4
p1=u+f1/4=(3,3,1,1)/8
p2=u+f2/4=(3,1,3,1)/8.
```

Since `A_w u=0`, the complete two-polarization readout follows **without reconstructing all six w**:

```text
TT_plus  = -4 [ f1·H_p1 - f2·H_p2 ]
TT_cross = -4 f1·H_p2.
```

These identities hold coefficientwise for all six independent edge rates over Q. The map from w to the eight population readouts has rank **5**, yet its row span contains both TT coordinates (rank two). The invisible weight mode `(1,1,-1,-1,1,1)` is TT-silent. Therefore 2 chosen mixed preparations suffice for *TT-only* readout while never determining the full six conductances.

## Why two localized preparations do not suffice

For each basis-state preparation E_bb, the short-time population Hessian has rank 3 and appending both TT rows raises the combined rank to 5. For any pair of different basis-state preparations, the readout has rank 5 **but appending TT raises it to 6**: TT is not determined. All six pairs are checked exactly. Three independent localized preparations remain sufficient to reconstruct all six rates as shown in PR #37.

Thus the minimum count depends on the *observation goal and preparation manifold*. The general two-preparation impossibility in PR #37 concerns full conductance tomography, not a two-dimensional TT-only functional.

## Scope and required next gate

The exact check `P3/K4B18TTReadoutExactCheck.py` uses only `fractions.Fraction`, rank elimination and coefficientwise identities. It assumes six **declared** K4 coherent edge amplitudes. It neither derives these controls from the inherited P3/P6 first-residue quotient, nor proves physical full SO(3) covariance, dynamical spin-2 accessibility, gauge descent, nonzero propagation, a continuum limit, or Einstein equations. The TT output here is a static algebraic projection at a chosen frame and covector.

The next CR bridge must independently specify which populations, calibrations and control directions the *actual* P6 observer can access, and verify equivariance and quotient descent; abstract rank alone is insufficient.
