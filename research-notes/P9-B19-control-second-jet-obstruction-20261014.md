# P9 B19 — A concrete second-jet quotient obstruction in the finite K4 population response

**2026-10-14.** Exact rational finite-dimensional audit candidate, stacked on B18 Draft PR #38 (itself on B14/B17 Draft PR #37). No changes to `main` or frozen P3. This is not a Lean formalization, CR-provenance theorem, continuum spin-2 propagation theorem, or Einstein dynamics.

## Declared physical model, distinguished observers, and response

For the six K4 edge controls `K_e=E_ab-E_ba`, take `K(x)=Σ_e x_e K_e`, `U_t(x)=exp(tK(x))`, `Φ_{t,x}(ρ)=U_t(x)ρU_t(x)^†`. This is a unitary CPTP family for each real x. The diagonal population first **time** derivative vanishes, while for every diagonal preparation `p` the half-second **time** derivative is
```math
q_p(x):=\frac12\left.\partial_t^2\operatorname{diag}\Phi_{t,x}(\operatorname{diag}p)\right|_{t=0}
=-A_{x^2}p.
```

With the calibrated positive mixed preparations from B18, `p1=(3,3,1,1)/8` and `p2=(3,1,3,1)/8`, extract the two finite TT-coordinate functionals via
```math
y_+(x)=-4(f_1\cdot q_{p1}(x)-f_2\cdot q_{p2}(x)),\qquad
y_\times(x)=-4 f_1\cdot q_{p2}(x).
```
Here `f1=(1,1,-1,-1)/2` and `f2=(1,-1,1,-1)/2` are Euclidean-orthonormal in `S=1^perp`, with `e_i=f_i/2` h-orthonormal for P7 `h=4 dot`.

Exactly, with edge order `01,02,03,12,13,23`,
```math
y(x)=T(x_{01}^2,x_{02}^2,x_{03}^2,x_{12}^2,x_{13}^2,x_{23}^2)^T,\quad
T=\begin{pmatrix}
-1&1&0&0&1&-1\\
0&0&1&-1&0&0
\end{pmatrix}.
```
The script checks the extraction against both population-preparation response matrices coefficientwise.

## First and second *control* jets (not time jets)

At any control basepoint `x0`, set `A=D_x y(x0)` and `H=D_x^2 y(x0)`. Explicitly
```math
A(u)=2\sum_e x_{0,e}T_e u_e,\qquad
H(u,v)=2\sum_e T_e u_e v_e\in\mathbb Q^2.
```
This is a mathematically concrete illustration of the PR #35 first-quotient descent obstruction, in the fully specified finite K4 model (not merely a toy scalar example).

At `x0=0`, `A=0` but `H\ne0`. More strongly, the **bilinear radical** is zero:
```math
\operatorname{rad}H
=\{u:H(u,v)=0\ \forall v\}=\{0\}.
```
Indeed for each edge `e`, `H(u,e_e)=2u_eT_e`, and *every column `T_e` is nonzero*. The map `u\mapsto[v\mapsto H(u,v)]` is therefore injective (flattened rational matrix rank 6). The two scalar outputs can distinguish six independent tangent control directions when one is allowed to pair them against calibrated second-direction probes. This **does not imply injectivity of the quadratic map y(x)**, which is insensitive to each individual `x_e\mapsto -x_e`.

At the nonzero uniform-amplitude point `xstar=(1,1,1,1,1,1)`, `rank A=2`, hence `dim ker A=4`. Explicitly,
```math
k=(1,1,0,0,0,0)\in\ker A,\qquad
H(k,e_{01})=(-2,0)\ne0.
```
Thus `H` **cannot** descend bilinearly through `A` on both inputs: if `H(u,v)=\overline H(Au,Av)`, then `H(k,v)=0` for all v, contradiction. In fact the radical-zero result shows this failure at **every** basepoint because `rank A\le2<6`.

The genuine second-jet refinement of the first-order observational quotient must preserve information in the radical complement; one defensible algebraic candidate is `V/(\ker A\cap\operatorname{rad}H)` in this fixed-vector-space model. Here it equals V. It is *not* automatically the P6 operational quotient; that requires specifying measurable two-control cross-derivatives, their calibration and gauge invariance.

## Crucial nonclaims

1. `A=D_x y(x0)` above is the first derivative **of the TT-extracted quadratic population readout with respect to x**. It is not the first-time derivative of populations (that derivative vanishes), nor the full-superoperator P6 response. These observer levels must not be conflated.
2. All six K4 controls are **declared** in the chosen unitary example; inherited P3/P6 physical first-residue access, independent calibration of e_e perturbations, and operational quotient descent have not been shown.
3. `T` is a finite TT *coordinate projection at a fixed frame and covector*; the six-dimensional control chart is not an SO(3) representation with established dynamical covariance. There is no propagating graviton or Einstein equation.
4. Bilinear radical zero is a property of mixed control response probes, not proof that two static scalar measurements recover six unknown rates. The latter remains impossible at fixed x under the B18 conditions.

## Reproducibility

`P3/K4B19SecondJetRefinementExactCheck.py` runs on Python standard-library `fractions.Fraction` and checks the full rational coefficient matrix, positive prepared states, rank two first control response at uniformity, rank six Hessian flattening, explicit kernel/second-jet witness, quadratic finite-difference equality, and a sign-indistinguishable control pair. Dedicated GitHub Actions CI audits this file, separately from Lean formalization.
