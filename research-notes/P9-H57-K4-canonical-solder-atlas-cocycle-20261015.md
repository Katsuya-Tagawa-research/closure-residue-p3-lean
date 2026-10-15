# H57 — A Conditional K₄ Canonical Atlas: Solder Transitions, Symplectic Cocycles, Spatial Derivative Compensation, and Boundaries

**2026-10-15 | P3–P11 Mathematical Bridge → P9 GR-I; stacked on H56 Draft PR #75.**

This is a **conditional local chart/atlas audit of already given ADM canonical geometry**, not an origin theorem for physical spacetime/Einstein gravity and not the answer to P9.64's separate microphysical KKS→ADM problem. H56 parent had **69/69 CI PASS** at the start of H57. All K₄ internal-to-spatial solder choices, the smooth 3D manifold, the full ADM action/canonical symplectic structure, allowed chart-transition gauge group and acceptable boundary support are **independent assumptions**. No frozen manuscripts or main edited, no Lean kernel/human peer review/laboratory data.

## 1. The exact K₄ atlas transition formula

On the fixed physical spatial coordinates, introduce a *chosen* family of physical solder frames parameterized by orientation-preserving \(Q\in GL^+(3,\mathbb R)\). In the chosen nonorthonormal \(S=\mathbf1^\perp\subset\mathbb R^4\) reference frame \(f_i=e_i-e_3\), put
\[
G=f^\top f=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix},\quad
B(w)=\sum_{e\in E(K_4)}w_eV_e,\quad V_e=v_ev_e^\top,\quad
g_0(w)=16GB(w)^{-1}G.
\]
Take chart A with metric \(g_A(w)=g_0(w)\). For *another independently permitted solder* \(Q\), chart B is \(g_B(v)=Q^\top g_0(v)Q\). Equating their **physical metric components in the same fixed coordinate chart**, \(g_A(w)=g_B(v)\), gives
\[
g_0(v)=Q^{-\top}g_0(w)Q^{-1},
\quad
\boxed{B(v)=L_Q B(w)L_Q^\top,\qquad L_Q=GQG^{-1}.}
\]
Since \(w\mapsto B(w)\) is a 6-dimensional **linear isomorphism**, there exists one uniquely determined **linear** six-weight transition
\[
\boxed{v=T_Qw,\qquad
T_Q=M^{-1}\operatorname{SymCong}(L_Q)M,\quad
\det T_Q=(\det Q)^4}
\]
in which \(M\) is H52's 6×6 edge-to-symmetric-tensor matrix, and \(\operatorname{SymCong}(L)\) sends a symmetric matrix \(B\) to \(LBL^\top\). The determinant formula follows from the standard third symmetric-power-of-determinant rule in \(\operatorname{Sym}^2\mathbb R^3\). In a constant determinant-one shear, \(\det T_Q=1\).

**This linearity is special and useful:** although \(g_0(w)\) is nonlinear in \(w\), the transition is linear because the *inverse metric* \(B=16Gg^{-1}G\) is linear in the six edge weights. Nothing about this formula shows that every mathematically possible \(GL^+\) solder is **physically realizable** or derived from finite CR.

## 2. Genuine positive-overlap atlas and a true exit from one positive cone

Consider \(Q_s=\begin{pmatrix}1&s&0\\0&1&0\\0&0&1\end{pmatrix}\).

At \(s=1/10\), a uniform positive B-chart weight \(v=(1,\ldots,1)\) corresponds in chart A to
\[
\boxed{w=T_{Q_{1/10}}^{-1}v
=\left(\frac{13}{10},\frac9{10},\frac{103}{100},1,\frac7{10},\frac{11}{10}\right)>0.}
\]
Conversely A-uniform weights map into B-positive weights
\[
\boxed{T_{Q_{1/10}}(1,\ldots,1)
=\left(\frac7{10},\frac{11}{10},\frac{103}{100},1,\frac{13}{10},\frac9{10}\right)>0.}
\]
Thus the two positive K₄ charts share a **nonempty open overlap**, not merely a boundary coincidence.

At \(s=1/2\) the B-uniform positive weight has A-coordinates
\[
\boxed{T_{Q_{1/2}}^{-1}(1,\ldots,1)
=\left(\frac52,\frac12,\frac74,1,-\frac12,\frac32\right).}
\]
This point remains a positive-definite physical metric but falls **outside the strict positive-edge A-chart**; B still describes it with six positive weights, provided this different solder is admitted as a valid physical frame. A **pure K₄ site permutation** only permutes the six edge weights and cannot remove this negative value. Hence a physically meaningful extended atlas requires solder/frame freedom **beyond merely relabeling the four K₄ vertices**, or a different proven parameterization. This does not mean such new solder gauge freedom is automatically present in original P3/P7/P8.

## 3. Three-chart cocycle and full canonical cotangent atlas

On the common positive overlap choose A (\(s=0\)), B (\(s=1/10\)), C (\(s=-1/10\)), with transitions \(T_{AB}\), \(T_{BC}\), \(T_{AC}\). Exact matrix algebra gives
\[
\boxed{T_{BC}T_{AB}=T_{AC}.}
\]
For any pre-existing ADM momenta \(\pi^{ij}\) and associated local positive chart-cotangent variables
\(p_{A,e}=\pi^{ij}\partial_{w_e}g_{A,ij}\), define
\[
\boxed{p_B=T_{AB}^{-\top}p_A,\qquad
\sum_ep_{A,e}\,\delta w_e
=\sum_ep_{B,e}\,\delta v_e.}
\]
The exact checker verifies the full 6×6 inverse-Jacobian identities, the canonical Poisson brackets
\[
\boxed{\{v_e,p_{B,f}\}=\delta_{ef},\quad
\{v_e,v_f\}=0,\quad
\{p_{B,e},p_{B,f}\}=0,}
\]
and arbitrary rational linear-functional brackets in A and B. These are **ordinary cotangent-lift symplectic transition maps**: they preserve the locally assumed canonical 2-form, not a result showing an original P3/P4 KKS form is actually the ADM form.

The momentum transitions also obey the cocycle \(p_C=T_{BC}^{-\top}p_B=T_{AC}^{-\top}p_A\). Physical ADM constraint functions expressed in the same physical \((g,\pi)\) therefore agree across chart overlap, **provided** all space/time derivatives of the solder are transformed and the external standard ADM field phase space/boundary conditions are the same.

## 4. Spatially varying soldering: do not mistake edge fields for six scalars

If \(Q=Q(x)\), then \(T=T_{Q(x)}\), so
\[
\boxed{\partial_i v=T\,\partial_i w+(\partial_iT)\,w.}
\]
The physical metric identity is \(g_A(w(x))=Q(x)^\top g_0(v(x))Q(x)\); its spatial derivative contains the **indispensable solder terms**
\[
\boxed{\partial_i g_A=
Q^\top\bigl(Dg_0(v)\,\partial_iv\bigr)Q
+(\partial_iQ)^\top g_0(v)Q
+Q^\top g_0(v)(\partial_iQ).}
\]
For a nonconstant \(Q_s(x)\) with \(s(0)=1/10\), \(\partial_1s=1/20\) and **constant physical A-weights** \(w=(1,\ldots,1)\), the B-weights have
\[
\boxed{
\partial_1 v
=\left(-\frac3{20},\frac1{20},\frac3{100},0,
\frac3{20},-\frac1{20}\right)\ne0.}
\]
The naive derivative using \(Dg_0(v)\partial_1v\) alone is NONZERO, even though the actual physical metric \(g_A\) is constant! The complementary two solder-derivative terms cancel it **exactly** in rational arithmetic. This is a concrete obstruction to treating six local K₄ weight coordinates as independently transforming spatial scalars under changes of frame.

For a genuinely nonflat 3D field, choose A-weights \(w_e(x)=1-x^\top Gx\) near the origin and the same nonconstant solder \(Q_{1/10+x_1/20}\). Define B-weights \(v(x)=T_{Q(x)}w(x)\). At all sampled neighboring points the full physical metrics **agree exactly**; hence their centered first/second jets, Levi-Civita, Ricci tensor, Einstein tensor and scalar \(R_h^{(3)}\) agree EXACTLY for \(h=1/10,1/20,1/40\). The original conformal example has continuum \(R(0)=-3\); the stencil agrees across both charts with H53's exact \(R_h(c,h)\) formula. Under correctly compensated solder/frame changes, the ADM potential and HDA structure function \(g^{ij}\) therefore agree, not just their scalar densities at one cell.

### The momentum constraint boundary current is a PHYSICAL tensor-density quantity

For a fixed spatial vector field \(\xi^k\), the standard integration-by-parts current is
\[
\boxed{J^j=2\pi^{ji}g_{ik}\xi^k.}
\]
If charts A and B represent the **same physical coordinate metric \(g\) and momentum density \(\pi\)**, then \(J^j\), lapse-induced \(\beta^i=g^{ij}(N\partial_jM-M\partial_jN)\), and the valid boundary flux condition agree. If one uses raw B-weights as six spatial scalars and drops \(\partial_iT\) or \(\partial_iQ\), the derived curvature/constraint currents may instead be spurious.

These are geometric/canonical compatibility tests in the **already granted standard ADM** continuum, not a standalone original CR construction of constraint boundary Hamiltonians or the full HDA.

## 5. Time-dependent soldering adds an explicit Hamiltonian connection

For an **externally time-dependent** solder \(Q(t,x)\), the spatial canonical 2-form still transforms correctly at each fixed time, but the canonical ACTION must account for the moving chart. With \(v=T(t,x)w\), \(p_B=T^{-\top}p_A\),
\[
\dot v=T\dot w+\dot T\,w,\quad
p_A\dot w=p_B\dot v-p_B\,\dot T\,T^{-1}v.
\]
Thus the correct transformed canonical Hamiltonian **density** is
\[
\boxed{\mathcal H_B=\mathcal H_A
+p_B^\top\dot T\,T^{-1}v.}
\]
A missing frame-connection term produces an artificial time dependence even when the physical ADM metric and momentum are unchanged. The checker verifies a nonzero rational example. This is a coordinate/gauge correction in an externally time-dependent canonical atlas, NOT the physical ADM Hamiltonian emerging from microscopic CR.

## 6. Exact scope relative to P9.64 KKS→ADM

**Established conditional mathematics:** linear six-weight transition from shared physical metric under a declared \(GL^+\) solder, nontrivial two-chart positive overlap, explicit one-chart exit and S₄ relabeling obstruction, exact three-chart cocycle, cotangent Poisson bracket invariance, spatial derivative/solder cancellation, nonflat curvature-stencil agreement, boundary-current consistency and time-dependent frame connection.

**Still OPEN:** original P3/P4/P7/P8 *physical authorization* of a non-permutation solder group; global manifold atlas existence, chart transition consistency with causal observer and physically permitted interventions; an independently specified microscopic \((\mathcal O,\omega_{\rm KKS})\) and map \(F\) with \(F^*\Omega_{\rm ADM}=\omega_{\rm KKS}\), correct rank/field limit/constraint intertwiner, and an actual CR-generated action/EH/Einstein equations. P9.64 is separately testing that microscopic map. H57 is a **necessary target-geometry atlas specification**, not its solution.

**H58 gate:** classify admissible solder transitions that preserve the K₄ positive-edge cone **without** changing physical frame, or prove an explicit restricted group/cocycle of physical microscopic KKS charts that maps to the ADM canonical atlas. Make any claimed physical \(GL^+\) gauge principle an independent theorem/axiom, not a convenient mathematical reparameterization. Also audit compact-support/boundary charges under nontrivial spatially varying, time-dependent chart transitions if a noncompact ADM region is contemplated.

## Reproducibility

`P3/P9H57K4CanonicalSolderAtlasExactCheck.py` uses exact standard-library Fraction arithmetic plus H52/H53/H55 audited local metric and cotangent functions. Every check is exact, including nonzero positive-overlap rational witnesses, Poisson brackets, two chart-space boundary/curvature consistency checks and frame-connection identity. New dedicated GitHub Actions CI on a Draft stacked PR; human journal review, Lean formalization and actual experimental validation not performed.
