# P9.24 / H24 — Original P3 nonzero residue to internal diagonal-gauge holonomy

**2026-10-14.** Independent rational-Gaussian finite audit candidate, stacked on H21–H23 Draft PR #41. Main and frozen P3 unchanged. No Lean formalization, no assertion of *physical* P6 inheritance, Levi-Civita/Regge curvature, or Einstein dynamics.

## 1. A genuine phase-sensitive CPTP example

Use the exact unitary
```math
U=\frac13\begin{pmatrix}1-2i&-2i\\-2i&1+2i\end{pmatrix},
\quad \Phi(A)=UAU^\dagger,\quad D=\{\mathrm{diag}(a,b):a,b\in\mathbb C\}.
```
It satisfies U†U=I exactly. Thus Phi is a single-Kraus CPTP channel. With Z=diag(1,-1) and Q=1-Delta_D, define actual P3 Krylov-hidden operators z1=Q Phi(Z), z2=Q Phi²(Z). Direct exact computation gives
```math
z_1=\begin{pmatrix}0&(8+4i)/9\\(8-4i)/9&0\end{pmatrix},\qquad
z_2=\begin{pmatrix}0&(32-56i)/81\\(32+56i)/81&0\end{pmatrix}.
```
Both are Hermitian. They are complex-linearly independent: their two-coordinate offdiagonal determinant is `128i/81`. Hence H1=span_C{z1}, H2=all offdiagonal M2(C). Applying **P3's original** quadratic-residue definition `R_k=span{Delta_D([z,w*]):z∈H_i,w∈H_j,i+j≤k}` yields
```math
R_2=\{0\},\quad
\Delta_D([z_1,z_2^\dagger])=\frac{128i}{81}Z\ne0,\quad
R_3=D_2^0,\quad R_k=D_2^0\ (k\ge 3).
```
Here the first nonzero return is at **P3 depth k=3**, not k=2; index i+j is 1+2. This is an exact finite constructive counterpart to the all-depth-zero orthogonal model in H21.

## 2. A conditional algebraic bridge to internal observer-relative gauge holonomy

Choose anti-Hermitian coherent generators K1=i z1 and K2=i z2. The exact bracket is
```math
[K_1,K_2]=-\Delta_D([z_1,z_2^\dagger])
=-\frac{128i}{81}Z= B\ne0.
```
B is diagonal anti-Hermitian, so it **annihilates the diagonal observational algebra by commutation**, although the P3 residue itself is nonzero. With both controls and their commutators admissible, their generated real Lie algebra is su(2). In this Lie algebra, the silent diagonal-gauge subspace N=R iZ is **not an ideal**: `[B,K1]` is nonzero offdiagonal. This is an explicit nonideal ideal-test witness, in contrast to H21's entire-population-first-time silent kernel N=so(4).

The vector-space splitting `u(2)=h⊕m`, with `h=iD_2` and `m=` anti-Hermitian offdiagonal matrices, has `[m,m]⊆h` and `[h,m]⊆m`. Thus the horizontal bracket has a **vertical / observer-relative gauge** component. Under the explicitly chosen canonical reductive homogeneous-space connection of U(2)/T², this component supplies an internal connection-curvature coefficient (subject to connection sign convention). **It is not a Levi-Civita or physical spacetime curvature tensor**. Moreover, diagonal phase transformations are unobservable only relative to diagonal population readout, not relative to arbitrary coherent measurements.

P6 Eq. (6) uses Xi(J)=(1-Delta_D)(J-J†). For a **declared** complex microscopic sector containing J1=i z1/2 and J2=i z2/2, Xi(Jj)=Kj exactly, making these controls *formally compatible with* the First-Residue Accessibility algebraic selection condition. It does **not** show that the independently fixed, inherited microscopic P6 sector J_N actually contains these Jj, that their control pulses are physically calibrated, or that the chosen gauge quotient is compatible with all observables.

## 3. CPTP pulse holonomy and observational order

Every exact pulse exp(eps Kj) is unitary. Define
```math
U_{\square}(\varepsilon)=
e^{\varepsilon K_1}e^{\varepsilon K_2}
e^{-\varepsilon K_1}e^{-\varepsilon K_2}
=I+\varepsilon^2 B+O(\varepsilon^3).
```
Because B is **diagonal**, for any diagonal initial density matrix its leading order eps² conjugation response vanishes. For E00, the actual first offdiagonal density-matrix term is order eps³ (nonzero). Its population variation first appears at order eps⁶:
```math
\operatorname{diag}(U_{\square}E_{00}U_{\square}^\dagger)
-(1,0)
=\frac{183762944}{43046721}\varepsilon^6(-1,1)
+O(\varepsilon^7).
```
For a coherent preparation `rho+=(I+X)/2`, its offdiagonal density-matrix readout instead has leading eps² coefficient
```math
[ B,\rho_+ ]_{01}=-\frac{128i}{81}.
```
These orders differ sharply from the H22 **real-orthogonal K4** loop (coherence eps² and population eps⁴ for E00). A nonzero P3 residue may create a vertical holonomy that is invisible to the diagonal observation algebra through the leading commutator order. All of this is standard unitary quantum mechanics, **not a CR-specific prediction**.

## 4. P9.24 decision and boundaries

The strictly established *finite* chain is
```text
actual P3 Krylov-hidden z1,z2
  -> nonzero original diagonal quadratic residue
  -> chosen controls K_j = i z_j
  -> nonzero internal diagonal (vertical) Lie commutator
  -> chosen homogeneous-space connection holonomy
  -> observer-dependent pulse readout orders.
```
The arrows involving **chosen controls and internal connection** are *conditional identifications*, not general P3/P6 functorial constructions. Real physical CR control access, first-response fingerprint, independent calibration and gauge closure must still be shown. Crucially, *no canonical morphism* from this observer-relative internal gauge curvature to P7/P8 Lorentzian/Levi-Civita/Regge curvature has been supplied.

The H21 failure (orthogonal models with holonomy but zero original P3 residue) and the present H24 example (nonzero original P3 residue but leading holonomy purely diagonal gauge) jointly show why a curvature-transport theorem needs phase sensitivity, observer compatibility, and explicit soldering.

B14 physical six-edge CR provenance, B15 standard GKSL comparator and B17 actual response-conjugate force stay open. P9 Minimum Success and Einstein dynamics remain unachieved.

## Verification

`P3/P9H24PhaseSensitiveResidueGaugeExactCheck.py` uses Python standard-library `fractions.Fraction` with an explicit rational-Gaussian class, finite 2x2 complex matrices, exact commutators, and polynomial matrix series through eps^6. Dedicated GitHub Actions runs this checker. Finite symbolic coefficient checks do **not** establish a general infinite-dimensional or physically soldered theorem.
