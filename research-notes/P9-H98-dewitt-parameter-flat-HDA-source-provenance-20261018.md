# H98 — DeWitt Parameter Selection Requires Off-Shell Dynamics: Exact K4 Cotangent Kinematics and a Flat-Metric H–H Anomaly

**2026-10-18 | P9 GR-I, G4 ↔ G5 / P3–P11 Mathematical Bridge, Route A.**

**Base:** H97 Draft PR #116, **100/100 CI PASS**. This step leaves the genuine H75 CPTP original P3 finite residue, source observations, main and frozen P1–P8 unchanged. It does not add fictitious physical controls, assume a source-created canonical momentum or insert Einstein's equations and call them derived. Its *ADM field comparator* is explicitly **independently supplied standard gravitational physics**, not a property of the H75 source.

## 1. The G4 question sharpened: why precisely the DeWitt trace coefficient 1/2?

At a 3-dimensional spatial metric \(g\), one-parameter ultralocal canonical gravitational kinetic forms are
\[
\mathcal K_\lambda[g,\pi]
=\frac1{\sqrt g}\left(\pi^{ij}\pi^{kl}g_{ik}g_{jl}
-\lambda (g_{ij}\pi^{ij})^2\right),\qquad\lambda\in\mathbb R.
\tag{H98-K}
\]
At \(g=I\), on the six independent entries of the *symmetric contravariant momentum density*,
\[
D_\lambda=\operatorname{diag}_{3\times3}\!\left(I_3-\lambda{\bf1}{\bf1}^\top\right)\oplus2I_3.
\]
Its eigenvalues are
\[
\boxed{1,1,1-3\lambda,2,2,2.}
\tag{H98-EIG}
\]
Hence \(D_\lambda\) is positive definite for \(\lambda<1/3\), degenerate at \(\lambda=1/3\), and Lorentzian in the *DeWitt superspace-kinetic sense* with inertia \((5+,1-)\) for **every** \(\lambda>1/3\). Positivity of the *spatial* three-metric (including the response metric supplied conditionally by K4) does not determine even this sign, much less the unique ADM value \(\lambda=1/2\).

For the conformal momentum \(\pi=a g^{-1}\) in 3 spatial dimensions,
\[
\sqrt g\,\mathcal K_\lambda(g,a g^{-1})= (3-9\lambda)a^2.
\]
For any nonzero traceless symmetric momentum, the first positive term is strictly positive and its \(\lambda\)-dependent trace term vanishes. This separation is source-independent ADM algebra, and does not presume that a real microscopic gravitational Hamiltonian already exists.

## 2. H98.1 — Conditional K4 metric chart *does* admit an exact cotangent lift, but its momenta are not source-derived (EXACT conditional kinematics)

Take the actual original H75 positive flag-1 readouts of four **separately prepared** microscopic positive qutrit inputs,
\[
r=(0,16/25,16/25,4/25).
\]
H85, after independently supplying K4 cell labeling, four-cell spatial solder, endpoint-only additive selection and weight-budget normalization W=27, gives the **strictly positive candidate edge weights**
\[
w_{\rm add}=(4,4,1,8,5,5).
\]
All four positive H75 readouts and original signed P3 \(R_3\ne0\) are kept exactly; this note does NOT derive or uniquely select these physical graph-coupling assumptions from P3.

Use the fixed nonorthonormal basis \(B=(e_0-e_3,e_1-e_3,e_2-e_3)\) of \(S={\bf1}^\perp\subset\mathbb R^4\), \(G_0=B^\top B\), and
\[
C(w)=B^\top L_w B,\qquad
g(w)=16\,G_0\,C(w)^{-1}G_0.
\tag{H98-G}
\]
This is the matrix of the original H85 positive response metric \(16L_w^+\) in the **same** B basis, not a new or independent metric.

For every strictly positive six-vector \(w\), the mapping \(w\mapsto C(w)\) is a linear isomorphism \(\mathbb R^6\to\operatorname{Sym}(3)\), \(C(w)\) is strictly positive, and inversion/congruence give a local positive-metric diffeomorphism. With \(z=\operatorname{vec}_6[g]\), the exact Jacobian is
\[
\boxed{
\frac{\partial g}{\partial w_e}
=-16\,G_0 C^{-1}(B^\top r_er_e^\top B)C^{-1}G_0,
\quad r_e=e_i-e_j.
}
\tag{H98-J}
\]
At the actual H85 positive selected \(w_{\rm add}\), with coordinates ordered \(z=(g_{11},g_{22},g_{33},g_{12},g_{13},g_{23})\), the exact six-by-six rational Jacobian A has
\[
\boxed{\det A=-\frac{16777216}{2251875390625}\ne0.}
\tag{H98-DET}
\]
An **externally declared** canonical cotangent phase-space pair \((w,p_w)\in T^*\mathbb R^6\) therefore has the exact symplectic cotangent lift
\[
\boxed{
z=g(w),\qquad
p_z=A(w)^{-T}p_w,\qquad
\sum_e p_{w,e}dw_e=\sum_\alpha p_{z,\alpha}dz_\alpha.
}
\tag{H98-COT}
\]
This is an explicit **conditional G3 kinematic** result, beyond a mere dimension or Darboux coincidence: the pulled-back canonical 1-form agrees exactly (hence symplectic 2-form), including nonlinear w-dependence on a positive neighborhood.

**However:** the six \(p_w\) have been declared as independent external cotangent variables, **not produced by H75 CPTP data**. The covariance of this chart under arbitrary spatial diffeomorphisms, its physical 3+1 field extension, KKS-to-ADM *physical* momenta and source Hamiltonian remain OPEN. The label A4 source selector does not fix them.

In particular the *same* source-selected positive \(g(w)\) can be paired with \(\lambda=0\) (positive kinetic Hessian) or \(\lambda=1/2\) (one negative conformal mode). Thus original H75 flag observations and K4 positive metric alone never distinguish a DeWitt kinetic coefficient.

## 3. H98.2 — Nonuniform off-shell H–H at a flat canonical metric fixes λ=1/2 (EXACT conditional ADM comparator)

Now **separately supply** the ordinary continuum spatial ADM Poisson brackets
\[
\{g_{ij}(x),\pi^{kl}(y)\}
=\delta_{(i}^k\delta_{j)}^l\delta(x-y),
\]
three-dimensional smooth fields, spatial scalar curvature \(R[g]\) and standard lapse smearing (without a GR/CR origin claim). Let
\[
\mathcal H_\lambda=\mathcal K_\lambda-\sqrt g\,R[g],
\quad H_\lambda[N]=\int N\mathcal H_\lambda,
\quad
D[V]=\int V^i(-2g_{ij}\nabla_k\pi^{jk}).
\tag{H98-FIELD}
\]
At \(g_{ij}=\delta_{ij}\), **off-shell with arbitrary smooth nonconstant \(\pi^{ij}(x),N(x),M(x)\)** and zero boundary contributions, a direct functional-derivative calculation gives
\[
\begin{aligned}
\{H_\lambda[N],H_\lambda[M]\}\big|_{g=I}
&=\int (N\partial_iM-M\partial_iN)
\Bigl[-2\partial_j\pi^{ij}
+2(1-2\lambda)\partial^i(\pi^j{}_j)\Bigr]\,d^3x\\
&=\boxed{
D[N\nabla M-M\nabla N]\big|_{g=I}
+2(1-2\lambda)\int
(N\partial_iM-M\partial_iN)\partial^i\pi\,d^3x}.
\end{aligned}
\tag{H98-HH}
\]
Here both local pure-kinetic terms cancel upon antisymmetrizing the lapses; the nontrivial derivative-lapse term comes from the **independently assumed curvature potential** \(-\sqrt gR\). This is **not** a full arbitrary-metric HDA theorem, only an exact flat-background off-shell necessary condition.

For all arbitrary such momenta/lapses, recovering the **standard** undeformed ADM H–H bracket with the same standard momentum generator requires
\[
\boxed{\lambda=1/2.}
\tag{H98-SELECT}
\]
Thus the continuum curvature/constraint closure input can **select** the unique Einstein/ADM coefficient within this independently postulated λ-family—where positive spatial metric, A4 spatial source geometry, and even the DeWitt sign \((5+,1-)\) alone cannot.

An exact all-rational nonuniform witness on \(x\in[0,1]\) (and unit transverse 2-torus) uses
\[
N=x(1-x),\quad M=x^2(1-x),\quad
\pi^{ij}(x)=f(x)\delta^{ij},\quad f=x^2(1-x).
\]
With vanishing needed boundary contributions and \(w=N M'-M N'\),
\[
\int_0^1 f'(x)\,w(x)\,dx=\frac1{210},
\quad D[w\partial_x]=-\frac1{105},
\]
and
\[
\boxed{
\{H_\lambda[N],H_\lambda[M]\}\big|_{g=I}
=\frac{2-6\lambda}{105},\qquad
\{H_\lambda[N],H_\lambda[M]\}-D[w\partial_x]
=\frac{1-2\lambda}{35}.
}
\tag{H98-WITNESS}
\]
At \(\lambda=0\) the H–H bracket is \(2/105\) but D is \(-1/105\); at \(\lambda=1/2\) the anomaly vanishes. This is a **nonuniform OFF-SHELL counterexample**, not minisuperspace and not just comparing kinetic signatures.

The exact checker builds rational polynomials, differentiates/integrates them with Fraction arithmetic, reproduces \(\lambda=0,1/3,1/2,2/3\) values, and independently computes the directly differentiated H–H cross-bracket and its integrated-by-parts momentum/anomaly decomposition. The proof rests on **explicit imported ADM continuum geometric functional derivatives** and extends this witness algebraically to the λ-family; it is not a generated Einstein constraint algebra.

## 4. P9 G4/G5 and P11 handoff

**G4:** The original H75 source through H85 positive K4 chart supplies spatial response geometry only after extra topology/solder/selector data. Even its exact *conditional* 6+6 **cotangent lift** provides no *physical source-generated momenta*. A DeWitt kinetic term with the negative trace coefficient cannot be inferred from Fisher positivity, from spatial response alone or from matching KKS orbit dimension.

**G5:** Once independent **continuum ADM canonical variables, scalar curvature potential, and standard momentum constraint** have been imported, the flat nonuniform off-shell H–H bracket *conditionally* fixes the coefficient \(\lambda=1/2\). It does not prove the P3 CR-generated sector carries the imported curvature potential, spatial derivative bracket or diffeomorphism constraints, and it is not by itself the complete off-shell full HDA at arbitrary metrics. Existing H56/H83 broader **conditional** ADM comparator work remains separate.

**P11:** The generative gap is sharper than a missing numerical coefficient. A true F axiom or constructive theorem must produce **source-justified canonical field momenta, their symplectic Poisson brackets, the curvature/spatial derivative potential, and the physical constraint closure**. If these are all inserted externally, reproducing \(\lambda=1/2\) is standard ADM algebra rather than generating Einstein gravity.

**Proof ledger:** H75 actual flag readouts and exact P3 source **EXACT**; K4 positive conditional metric and exact Jacobian/cotangent lift **CONDITIONAL EXACT** (external A4 graph, edge selector and six canonical momenta); λ kinetic eigenvalues/inertia **EXACT standard ADM algebra**; flat nonuniform H–H anomalous term and selection \(\lambda=1/2\) **EXACT conditional standard canonical GR comparator**; physically generated DeWitt action, arbitrary-metric off-shell HDA, Einstein equations and F completeness **OPEN**.

**Stopping rule:** Do NOT relabel this ADM comparator as an H75-generated gravitational Hamiltonian. The next viable advance must prove the **source-origin of a canonical momenta/curvature-potential mechanism**, or formally state a new independent AX-CAN/AX-DYN/AX-SP axiom in P11. Main and frozen P1–P8 remain untouched; independent AI arithmetic/CI is not human referee review or a Lean kernel theorem.
