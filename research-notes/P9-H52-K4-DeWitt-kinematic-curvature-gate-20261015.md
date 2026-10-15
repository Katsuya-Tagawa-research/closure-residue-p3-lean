# H52 — Exact K4 Response-Metric Chart, DeWitt Signature and the Missing Spatial-Curvature Gate

**2026-10-15 | P3–P11 Mathematical Bridge / P9 GR-I handoff**, stacked on H51 Draft PR #70. This note develops a NEW, **strictly conditional kinematic bridge** from P9's already established finite \(K_4\) edge metric to the **ADM three-metric kinetic supermetric** and gives a sharp counterexample to inferring spatial curvature or Einstein dynamics from one finite cell. All results are ordinary differential geometry / exact finite rational matrix algebra under explicitly added assumptions, NOT a derivation of physical gravity, P6 physical source, a P7/P8 soldering or a CR-exclusive effect. No frozen manuscripts/main changes, Lean kernel formalization, human peer review, or hardware experiment.

## 1. Six K4 edge weights provide exactly six local 3-metric coordinates

Let
\[
S=\mathbf1^\perp\subset\mathbb R^4,\quad r_{ab}=e_a-e_b,
\quad A_w=\sum_{a<b}w_{ab}r_{ab}r_{ab}^{\mathsf T},
\qquad g_w=16(A_w|_S)^{-1}.
\]
Use **exactly** the P7/P8 orientation/normalization convention for S; the orientation is irrelevant to the symmetric metric, but its scaling is not. Take the nonorthonormal basis
\[
f_0=e_0-e_3,\quad f_1=e_1-e_3,\quad f_2=e_2-e_3,
\quad T=(f_0,f_1,f_2),\quad
G=T^{\mathsf T}T=
\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix}.
\]
Define the six edge covectors \(v_{ab}=T^{\mathsf T}r_{ab}\) and the covariant quadratic-form matrix \(B_w=\sum_{a<b}w_{ab}v_{ab}v_{ab}^{\mathsf T}\). **Do not invert B and call it the metric without correcting the nonorthonormal basis:** the correct matrix of the covariant metric tensor on S is
\[
\boxed{\ g_w=16\,G\,B_w^{-1}G.\ }
\]
Indeed the represented endomorphism \(A_w|_S\) is \(G^{-1}B_w\), and \(g_w(T_i,T_j)=16[G\,B_w^{-1}G]_{ij}\). At uniform \(w_{ab}=1\), \(A_w|_S=4I_S\), \(B_\star=4G\), and
\[
\boxed{g_\star=4G, \text{ i.e. }g_\star=4\langle\cdot,\cdot\rangle_S=h,}
\]
matching P7's declared normalization at the uniform cell.

For edge order \((01,02,03,12,13,23)\) and symmetric-matrix coordinate order \((B_{11},B_{22},B_{33},B_{12},B_{13},B_{23})\), the 6×6 linear map \(w\mapsto B_w\) is
\[
M=\begin{pmatrix}
1&1&4&0&1&1\\
1&0&1&1&4&1\\
0&1&1&1&1&4\\
-1&0&2&0&2&1\\
0&-1&2&0&1&2\\
0&0&1&-1&2&2
\end{pmatrix},
\qquad\boxed{\det M=-256\ne0}.
\]
Therefore the six weights uniquely coordinate **all six** symmetric 3×3 quadratic-form directions. For **strictly positive** w, B is positive definite because the K4 edge vectors span S. The inverse-metric construction is smooth and invertible on the resulting open positive edge cone, with exact differential
\[
\boxed{\delta g
=-16\,G\,B_w^{-1}
\left(\sum_{a<b}\delta w_{ab}v_{ab}v_{ab}^{\mathsf T}\right)
B_w^{-1}G.}
\]
At the uniform cell, \(\delta g_\star=-\delta B\), hence the six weights form a **local diffeomorphic chart onto an open subset of \(\operatorname{SPD}(3)\)**.

**Do not exaggerate surjectivity.** The strict **positive-edge** image is a *proper* open subset of all positive-definite metrics. An exact counterexample: choose \(w_{01}=-1/10\) and all other five weights 1. Then
\[
B=\begin{pmatrix}69/10&51/10&4\\51/10&69/10&4\\4&4&8\end{pmatrix}\succ0,
\quad
g=\begin{pmatrix}94/9&14/9&4\\14/9&94/9&4\\4&4&8\end{pmatrix}\succ0.
\]
Its edge weights are uniquely recovered from B, so **no alternative all-positive edge weights represent that same g** in this fixed cell chart. This does not invalidate the required local chart near positive uniform weights.

## 2. Pulling back the DeWitt 3-metric kinetic quadratic form

On symmetric variations \(H,K\in T_g\operatorname{SPD}(3)\), define the standard ADM kinetic DeWitt-type bilinear form, **up to its overall positive density factor**,
\[
\boxed{\mathscr D_g(H,K)
=\operatorname{tr}(g^{-1}H g^{-1}K)
-\operatorname{tr}(g^{-1}H)\operatorname{tr}(g^{-1}K).}
\]
It has **signature \(5+\), \(1-\)** in three spatial dimensions: decompose \(H=H_0+(\tau/3)g\) with \(\operatorname{tr}(g^{-1}H_0)=0\). Then
\[
\mathscr D_g(H,H)=\operatorname{tr}[(g^{-1}H_0)^2]
-\frac23\tau^2.
\]
The traceless sector is 5-dimensional positive, the conformal trace sector 1-dimensional negative. Because \(Dg_w\) is an isomorphism, this same inertia holds after pulling back to six K4 edge-weight variations.

At the uniform cell, the **exact rational pulled-back matrix** in edge order \((01,02,03,12,13,23)\) is
\[
\boxed{
\mathscr D^{\mathrm{edge}}_\star=
\begin{pmatrix}
0&-3/16&-3/16&-3/16&-3/16&-1/4\\
-3/16&0&-3/16&-3/16&-1/4&-3/16\\
-3/16&-3/16&0&-1/4&-3/16&-3/16\\
-3/16&-3/16&-1/4&0&-3/16&-3/16\\
-3/16&-1/4&-3/16&-3/16&0&-3/16\\
-1/4&-3/16&-3/16&-3/16&-3/16&0
\end{pmatrix}.}
\]
Its characteristic roots/multiplicities are
\[
\boxed{\operatorname{spec}\mathscr D^{\mathrm{edge}}_\star
=\{-1,\ \tfrac18,\tfrac18,\ \tfrac14,\tfrac14,\tfrac14\},\quad
\det \mathscr D^{\mathrm{edge}}_\star=-1/4096.}
\]
The sign decomposition can also be checked without spectral computation: the uniform conformal variation \(\delta w_{ab}=1\) gives \(H=-g\) and \(\mathscr D_g(H,H)=-6\), whereas the trace-free variation \(\delta w_{01}=1,\delta w_{23}=-1\) yields \(\mathscr D_g(H,H)=1/2>0\). The 6×6 exact eigenspace rank checks certify the full inertia.

**Interpretation restraint:** the single negative direction is the **conformal mode in the space of spatial metrics**, NOT the timelike dimension of a physical 1+3 Lorentzian spacetime. This is *conditional ADM kinematics*, not a deduction of a causal cone, constraint algebra or Einstein equations from P3/P6.

## 3. An exact homogeneous ADM kinetic expression under separately specified foliation

**Add** (do not claim to derive) a smooth one-dimensional time parameter \(t\), a positive lapse \(N(t)\), a vanishing shift, a smooth positive **homogeneous** weight \(w(t)\) on all six K4 edges and a prescribed spatial volume coordinate chart that identifies an orthonormal frame on S with a spatial slice. Then
\[
g_{ij}(t)=\frac4{w(t)}\delta_{ij},\qquad
K_{ij}=\frac1{2N}\dot g_{ij},
\]
and the ADM kinetic Lagrangian density is
\[
\mathcal L_{\rm kin}
=N\sqrt{\det g}\,\left(K_{ij}K^{ij}-K^2\right)
=\frac{\sqrt{\det g}}{4N}\mathscr D_g(\dot g,\dot g).
\]
Substitution gives the exact **ultralocal/homogeneous** formula
\[
\boxed{\mathcal L_{\rm kin}
=-\frac{12\,\dot w^2}{N\,w^{7/2}}.}
\]
The exact checker validates this with multiple rational configurations where \(\sqrt w\) is rational and checks the general tensor identity separately.

This equality shows the K4 weight coordinate can **parametrize the standard ADM kinetic term after adding independent foliation/lapse/shift/field assumptions**. It does **not** show that the quantum generation map produces the ADM action or that \(w(t)\) must physically obey Einstein equations. This sector is spatially homogeneous/flat with zero intrinsic scalar 3-curvature, before introducing spatially varying fields.

## 4. A sharp curvature No-Go even for smooth positive K4 weight fields

A finite cell provides a pointwise 3-metric, not derivatives on a physical manifold. To expose the missing ingredient mathematically, **independently add** a continuum spatial base \(\mathbb R^3\) with Euclidean coordinates \(x=(x_1,x_2,x_3)\), and for each real \(c\) choose smooth **strictly positive** K4 weight fields
\[
w_{ab}^{(c)}(x)=e^{-c|x|^2}
\quad\text{for every one of the six edges.}
\]
In an orthonormal S frame, the induced metric is
\[
\boxed{g_{ij}^{(c)}(x)=4e^{c|x|^2}\delta_{ij}.}
\]
At \(x=0\), **for all** c:
\[
w_{ab}^{(c)}(0)=1,\quad
g^{(c)}_{ij}(0)=4\delta_{ij},\quad
\partial_k g^{(c)}_{ij}(0)=0.
\]
Nevertheless the SECOND derivatives differ,
\[
\partial_k\partial_l g^{(c)}_{ij}(0)=8c\,\delta_{kl}\delta_{ij},
\]
and the standard 3D conformal-metric curvature formula (or direct normal-point Christoffel calculation) gives
\[
\boxed{R^{(3)}[g^{(c)}](0)=-3c.}
\]
In particular c=0 yields \(R^{(3)}(0)=0\), whereas c=1 yields \(-3\), **despite identical finite K4 cell values and first spatial jets**. Hence no assignment depending ONLY on one cell's \(w_{ab}\), its algebraic metric and its first spatial derivatives can universally determine the correct spatial-curvature potential \(\sqrt g R^{(3)}\). Additional field gluing, second spatial derivatives, manifold geometry and variation principles are indispensable.

This is not a no-go against **adding** an independently specified continuum field theory of the K4 weights: once such a field is granted, its curvature can of course be computed using its derivatives. The No-Go is about **automatic origin from pointwise finite-cell algebra**.

## 5. P9 handoff: exact achieved scope and explicit missing gates

| Component | H52 result | Safe P9 claim |
|---|---|---|
| Six finite response degrees of freedom | exact 6×6 determinant \(-256\), local metric chart | **PROVEN FINITE**, for declared K4 positive-weight sector |
| K4 metric variation | exact \(\delta g=-16GB^{-1}\delta B B^{-1}G\) | **PROVEN FINITE** |
| Pullback of DeWitt supermetric | eigenvalues \(-1,1/8,1/8,1/4,1/4,1/4\) at uniform; signature \(5+,1-\) | **PROVEN KINEMATIC** once standard ADM DeWitt form is specified |
| Homogeneous ADM kinetic density | \(-12\dot w^2/(Nw^{7/2})\) | **CONDITIONAL**, lapse/time/shift/spatial frame supplied externally |
| Spatial scalar curvature from local cell data | counterexample \(R(0)=-3c\) | **REFUTED automatic implication** |
| Physical 1+3 Lorentzian spacetime from microscopic P3/P6 | no result | **OPEN** |
| Diffeomorphism invariance, EH action and variation, Bianchi identities, ADM/HDA constraint closure, Einstein field equations | no result | **OPEN** |
| Standard-GKSL versus CR-exclusive signature | none | **OPEN / no-discriminator boundary H50** |

**H53 proposed gate:** choose the next missing component honestly: (a) an independently declared **spatial gluing/second-jet/connection** rule for smooth K4 weight fields, and an exact covariant spatial-curvature functional with boundary terms; (b) then an EH/ADM action under additional lapse/shift and matter/source postulates, verifying first-class HDA instead of asserting it; or (c) identify a physically motivated P7/P8 soldering that derives such a continuum base rather than assuming one. Treat all these as **additional postulates or independent proofs**, not results of H52 itself.

## Reproducibility

`P3/P9H52K4DeWittKinematicsCurvatureExactCheck.py` is self-contained (Python standard library `fractions.Fraction` only). It checks exact Gram/basis conventions, the \(-256\) linear map determinant, local metric inversion and six independent Jacobian directions, the positive-edge proper-cone witness, the 6×6 DeWitt eigenvalue multiplicities by exact ranks, two positive/negative tangent witnesses, ADM homogeneous rational kinetic identities and the smooth-curvature counterexample through exact origin jets. A dedicated GitHub Actions CI is included. This is NOT a Lean proof or expert-reviewed gravity result.
