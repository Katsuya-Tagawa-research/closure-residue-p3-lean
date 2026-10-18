# H88 — Coherence Completion of a Finite KKS Observer: Local Twelve-Response Poisson Closure vs Global Fifteen-Observable Lie–Poisson Closure

**2026-10-18 | P3–P11 Mathematical Bridge / P9 GR-I / Route A (Constructive).**

**Base:** H87 Draft PR #106, **100/100 GitHub Actions PASS**. Original H75 six-dimensional CPTP micro source and original P3 signed residue are unchanged. The separate nondegenerate **four-level U(4) KKS comparator** is **not** thereby derived from H75, P6 or F; the physical observability of all coherence channels is an **additional apparatus hypothesis**.

## H88.1 — Completion of six x-responses by six conjugate y-responses (EXACT LOCAL)

Fix \(\rho_\star=\mathrm{diag}(\lambda_0,\lambda_1,\lambda_2,\lambda_3)\) with
\[
\lambda=(2/5,3/10,1/5,1/10),\qquad \dim_\mathbb R \mathcal O_{\rho_\star}=12.
\]
For each unordered pair \(a<b\), let
\[
X_{ab}=E_{ab}+E_{ba},\quad
Y_{ab}=-i(E_{ab}-E_{ba}),\quad
x_{ab}=\mathrm{Tr}(\rho X_{ab}),\quad
y_{ab}=\mathrm{Tr}(\rho Y_{ab}).
\]
In the H87 convention \(\{f_A,f_B\}=-i\mathrm{Tr}(\rho[A,B])\),
\[
\{x_{ab},y_{cd}\}(\rho_\star)
=2(\lambda_a-\lambda_b)\delta_{(ab),(cd)},\qquad
\{x_{ab},x_{cd}\}(\rho_\star)=
\{y_{ab},y_{cd}\}(\rho_\star)=0.
\]
All six gaps are nonzero. Equivalently the derivative of
\[
\boxed{\Xi:\mathcal O_{\rho_\star}\to\mathbb R^{12},
\quad \Xi(\rho)=(x_{01},\ldots,x_{23};y_{01},\ldots,y_{23})}
\tag{H88-XI}
\]
has rank 12 at \(\rho_\star\). Since the orbit is a smooth 12-manifold, the inverse function theorem implies **a neighborhood \(\mathcal U\) of \(\rho_\star\)** on which \(\Xi\) is a diffeomorphism onto an open set of \(\mathbb R^{12}\). Pulling back the KKS bivector by the inverse produces a **genuine nondegenerate local Poisson structure** on the full twelve-response image. Thus **the chosen H87 x-only nonprojectability is repaired locally by supplying all six y channels**.

This is not a statement that the twelve raw observables have constant canonical Poisson brackets: away from the basepoint \(\{x_{01},x_{12}\}=y_{02}\), among other nontrivial brackets. The first-order normalized pair \(q_{ab}=x_{ab},\ p_{ab}=y_{ab}/[2(\lambda_a-\lambda_b)]\) is canonical **at the basepoint** but not over an open neighborhood. Local nonlinear Darboux corrections exist, but the instrument/readout meaning of the corrected variables requires an additional proof.

## H88.2 — Reconstructing missing diagonal population locally from spectrum invariants (EXACT ANALYTIC)

Let \(\rho\) be an Hermitian \(4\times4\) matrix and write
\[
\rho_{ab}=\tfrac12(x_{ab}-i y_{ab})\quad(a<b),\qquad
d_a=\rho_{aa},\quad \sum_a d_a=1.
\]
The four fixed **Casimir/spectral equations**
\[
\boxed{\mathrm{Tr}(\rho^k)=c_k:=\sum_a\lambda_a^k,\quad k=1,2,3,4}
\tag{H88-C}
\]
constrain the four unknown diagonals \(d_a\) as functions of the twelve real offdiagonal coordinates. Their diagonal Jacobian at \((d,\Xi)=(\lambda,0)\) is
\[
\mathcal V_{ka}=k\lambda_a^{\,k-1},\quad
\boxed{\det \mathcal V=24\prod_{a<b}(\lambda_b-\lambda_a)=\frac9{31250}\ne0.}
\tag{H88-V}
\]
Hence by the real-analytic inverse function theorem there exists a unique real-analytic diagonal reconstruction \(d_a=d_a(x,y)\) in a neighborhood of the *declared eigenvalue ordering* \(\lambda\) (and the nearby fixed-orbit sheet). A concrete second-order expansion is
\[
\boxed{
d_a=\lambda_a-\sum_{b\ne a}
\frac{|\rho_{ab}|^2}{\lambda_a-\lambda_b}
+O(\Vert(x,y)\Vert^3).
}
\tag{H88-2}
\]
The sign and denominator are fixed by the second-order spectral perturbation formula; the exact rational truncated-polynomial checker verifies that this expansion preserves **all four** power-sum Casimirs through degree two, for a generic independently chosen nonzero Gaussian-rational offdiagonal perturbation, not merely one root plane. This formula is **local**; one must not use it globally or where eigenvalue gaps vanish.

Consequently the missing diagonal coordinates and the 12-variable local nonlinear KKS brackets can be evaluated from \((x,y)\) and the fixed spectrum **locally**. Example:
\[
\boxed{\{x_{ab},y_{ab}\}=2(d_a(x,y)-d_b(x,y)),}
\]
so the bracket is a nonlinear function of all twelve response coordinates; it is *not* a new independent scalar given by the original P3 residue.

## H88.3 — The twelve offdiagonal responses do NOT define a global autonomous Poisson quotient (EXACT GLOBAL NO-GO)

Let \(P_{01}\) swap basis sites \(0,1\). The two positive legitimate states
\[
\rho_\star=\operatorname{diag}(2/5,3/10,1/5,1/10),\quad
\rho_{\rm swap}=P_{01}\rho_\star P_{01}^\dagger
=\operatorname{diag}(3/10,2/5,1/5,1/10)
\]
belong to the same nondegenerate U(4) orbit and have **all twelve offdiagonal x/y readouts zero**. Nevertheless,
\[
\boxed{
\{x_{01},y_{01}\}(\rho_\star)=+1/5,\quad
\{x_{01},y_{01}\}(\rho_{\rm swap})=-1/5.
}
\tag{H88-G}
\]
Thus the full twelve-response map \(\Xi\) cannot be a **globally Poisson** projection on the entire orbit; it is neither globally injective nor bracket-projectable. All \(4!=24\) permutation-diagonal states map to the same offdiagonal origin, with potentially different KKS bracket matrices. This does not contradict the local inverse near one ordered diagonal state.

**Scope:** not a proof that no different twelve-function global separating map exists, nor a claim that global symplectic topology disappears after adding three diagonal readouts. Global compact-orbit-vs-exact-ADM-cotangent obstruction H59 remains.

## H88.4 — A globally CLOSED fifteen-observable Lie–Poisson certificate (EXACT)

Add three traceless diagonal directions
\[
Z_a=E_{aa}-E_{33}\quad(a=0,1,2),
\quad z_a(\rho)=\mathrm{Tr}(\rho Z_a).
\]
Then the 15 Hermitian traceless matrices
\[
\boxed{\mathcal B=\{X_{ab},Y_{ab}\ (a<b);\ Z_0,Z_1,Z_2\}}
\tag{H88-B}
\]
span the entire real vector space of traceless Hermitian \(4\times4\) matrices, and are closed under the Hermitian Lie bracket \(-i[A,B]\). In particular,
\[
\{x_{ab},y_{ab}\}=2(d_a-d_b),\quad
\{x_{01},x_{12}\}=y_{02},
\]
and every right-hand side is a **real linear combination** of the same 15 expectation coordinates. The trace-one affine matrix \(\rho\) is uniquely reconstructed from 12 coherences and three diagonal population differences. The ambient 15-dimensional affine density space carries the standard linear Lie–Poisson bracket; the fixed-spectrum coadjoint orbit is its twelve-dimensional symplectic leaf, characterized (within the positive density domain) by the **three additional independent Casimirs** \(\mathrm{Tr}\rho^2,\mathrm{Tr}\rho^3,\mathrm{Tr}\rho^4\). Therefore 15 readouts suffice for **global linear bracket closure** and full quantum-state tomography of a four-level register; no claim that 15 is a universally minimal globally sufficient observer number on one fixed orbit is made.

All 15 expectations can be represented **mathematically** with valid positive effects: for \(X,Y\), use \(Q_{A,+}=(I_4+A)/2\), with eigenvalues \(0,1/2,1\); for diagonal populations use \(P_a=E_{aa}\), \(a=0,1,2\), plus unit trace. These are positive-POVM descriptions, not evidence that such coherent multi-site instruments are actually accessible in the **physical** H75/P6 control catalog. The retained 15-observable certificate may itself be **physically unimplementable** without additional calibrated phase references.

## H88.5 — What this DOES and DOES NOT give to P9 GR-I

- **EXACT LOCAL:** the 12 conjugate x/y coherences form a local Poisson chart on the nondegenerate four-level KKS orbit. A local nonlinear Darboux canonical transformation exists by symplectic Darboux's theorem. With a separately fixed SPD3/K4 solder one can **choose** six canonical configuration variables and construct a cotangent-lift momentum map as in H87; this is local abstract geometry only.
- **EXACT GLOBAL:** the entire 12-coordinate offdiag projection is not globally Poisson-projectable; adding three diagonal population observables yields a 15-observable global **linear** Lie–Poisson closure.
- **CONDITIONAL OPERATIONAL:** physically measuring \(y_{ab}\) and diagonal population differences requires independent coherent phase references, instruments, control scheduling and certified sample preparation; H81 AX-OA still applies.
- **OPEN:** neither the 15-dimensional closure nor the fixed-spectrum Casimirs select **which six** of the 12 are physical ADM \(g_{ij}\), why their conjugate partners equal ADM \(\pi^{ij}\), how this arises from the unchanged H75/P3 microscopic source, how K4 weights/spatial adjacency/solder are generated, why ADM's DeWitt \((5+,1-)\) Hamiltonian is selected, or the full nonuniform off-shell H–H/H–D/D–D algebra and Einstein equations.

Full local KKS Poisson closure is **NOT** the same as Einstein dynamics. Global closure of su4 does not cure H59's compact-orbit symplectic topology obstacle.

## H88.6 — P11 generative-completeness handoff and next proof gate

H87's observer quotient failure is **repairable at three distinct mathematical costs**:
1. **Local nonlinear completion:** six additional conjugate y responses, plus fixed nondegenerate spectral data, yield a local rank-12 Poisson chart.
2. **Global linear algebraic completion:** all 12 x/y coherences **and** three diagonal population observables yield a 15-dimensional Lie–Poisson state representation.
3. **Physical AX-OA completion:** experimentally accessible instruments and phase standards for those added readouts; **independent apparatus premises**, not a consequence of the original P3 shadow-residue alone.

**P11 OPEN obligation:** an actual generative map \(F\) would need to *derive* a particular physically accessible Poisson-reclosing observer (or prove equivalence to such a representation), not merely cite abstract closure of su4. A proposed mathematically closed observable expansion is not automatically a true physical observer.

**Recommendation:** After exact CI verification and a scoped H88 audit, hand off the central research emphasis to (a) actual source-proven KKS canonical interfaces and constrained dynamics for P9, and (b) explicit F/AX-OA axioms for P11. Avoid endless new rank/completion models in the absence of new physical source conditions.

**Verification:** dependency-free exact Gaussian/Fraction checker (using the retained verified H87 matrix engine) audits twelve derivative ranks and commutators, Vandermonde determinant, global same-readout/different-Poisson witnesses, 225 full su4 basis-closure brackets, 15 positive-POVM state tomography, and generic degree-two Casimir reconstruction. CI includes inherited H80–H87 exact programs. Draft/unmerged; no human peer review, new Lean theorem, actual experimental measurement or independently generated Einstein equations.
