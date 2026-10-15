# H61 — P9.70 Response: Microscopic Polarization, Acoustic Metric Matching, DeWitt Signature and Off-Shell Constraint Gates

**2026-10-15 | P3–P11 Mathematical Bridge → P9 GR-I / P9.70.** This note responds to the P9.70 research handoff. H61 is an independent finite mathematical audit of selected necessary gates; P9.70's separate SymPy evidence and its asserted conditional IR matter calculation are **reported inputs, not wholly independently re-audited here**. Stacked on H60 Draft PR #79. No frozen manuscripts or main modifications. No experimental confirmation, human peer review or Lean kernel formalization.

## Research provenance/status matrix

| Theme | Mathematical outcome | Physical/GR provenance |
|---|---|---|
| B1 generic U(4) torus invariant polarization | Exact stronger NO-GO at the diagonal basepoint | No independent CR/P6 selector |
| B1 SU(2) coherence readout | Conditional local 2D (q,p) chart and reference-sensitive selector | Control accessibility, phase reference, independent calibration OPEN |
| B2 3D scalar H-H principal symbol | Exact conditional tensor equality **A K^{ij}=g^{ij}** | Independent P7/P8 physical solder and source susceptibilities OPEN |
| B3 positive kinetic vs DeWitt | Exact real-congruence inertia NO-GO: (6+,0-) cannot become (5+,1-) | Negative geometrical direction source OPEN |
| B4 standard coupled off-shell ADM+matter algebra | Conditional known canonical closure under standard hypotheses | Not CR-generated; P9 full off-shell HDA/Einstein dynamics OPEN |

## B1. Strong torus-invariant real-Lagrangian NO-GO

Choose the **H59 comparator**, not the actual P9.64 micro-source:

\[
\rho_*=\operatorname{diag}(1,2,3,4)/10,\qquad
\mathcal O=U(4)\cdot\rho_*,\quad
T_{\rho_*}\mathcal O=\bigoplus_{a<b}V_{ab}.
\]

Each real root plane \(V_{ab}=\mathrm{span}_{\mathbb R}\{X_{ab}^{\#},(iS_{ab})^{\#}\}\) has real dimension 2 and KKS restriction \(\omega|_{V_{ab}}\ne0\), proportional to \(2(\lambda_a-\lambda_b)\). The diagonal stabilizer torus \(U(1)^4\) acts on \(V_{ab}\) through its nontrivial weight \(\theta_a-\theta_b\).

**Theorem H61.1 (strong real invariant-isotropic obstruction).** For the full diagonal torus at this generic diagonal basepoint, the only invariant **real isotropic** linear subspace of \(T_{\rho_*}\mathcal O\) is zero. In particular there cannot exist a torus-invariant real Lagrangian six-plane.

*Proof without invoking generic uniqueness of all torus weights.* The single diagonal generator \(h=\operatorname{diag}(0,1,4,10)\) already has six distinct nonzero absolute root frequencies \((1,4,10,3,9,6)\). Let its induced real skew generator be \(J\), rotation by frequency \(f_e\) on each \(V_e\). Then \(J^2\) has six distinct real eigenvalues \(-f_e^2\), with explicit rational polynomial projectors

\[
P_e(J^2)=\prod_{j\ne e}\frac{J^2+f_j^2 I}{f_j^2-f_e^2}.
\]

Any real subspace invariant under the torus is invariant under \(J\), hence under each \(P_e\), and decomposes as its intersections with the six root planes. Within a root plane a nonzero real \(J\)-invariant subspace must equal the entire real 2-plane, since its real rotation generator has no real eigenline. But that entire plane has nonzero restricted KKS form, contradicting isotropy. Hence the invariant isotropic subspace is zero. The standalone exact Fraction checker verifies all six projectors, their rank two, orthogonality/sum, and nonzero KKS blocks. The universal subspace conclusion is this algebraic argument, **not** brute-force enumeration of infinitely many subspaces.

**Scope:** The result is at the comparator diagonal basepoint with the entire specified diagonal stabilizer left unbroken. It does not forbid noninvariant real local Lagrangian charts, explicit phase-reference breaking, differently degenerate orbits, additional physical structure or reduced/other group actions. It does not establish a CR-dependent polarization selector.

### Conditional reference-sensitive SU(2) chart

On a separate U(2) spin-sphere sector, write

\[
\rho=\begin{pmatrix}c+p&a+ib\\a-ib&c-p\end{pmatrix},
\quad a^2+b^2+p^2=r^2,\quad r>0.
\]

On a patch \(a^2+b^2>0\), the coherent reference defines \(q=\arg(a+ib)\) locally (choose its orientation consistently with the KKS convention), with local canonical \((q,p)\). The measured channels

\[
(X,Y,Z)=(2a,2b,2p)
\]

have differential rank two with respect to \((q,p)\). An exact rational witness \(c=1/2,r=1/4,p=3/20,a=1/5,b=0\) has a nonzero (Y,Z)-Jacobian minor \(4/5\). Without a **declared external coherent phase reference**, \(q\) changes under the relative U(1) diagonal action and no preferred zero-phase is selected. The existence of the map from actual P6 causal response fingerprint \(\Sigma\) to these three calibrated channels remains OPEN. This local chart does not evade H59's compact/global KKS flux obstruction. It also uses a non-diagonal reference point: at the H59 diagonal basepoint coherence vanishes and \(q\) is undefined.

**B1 program gate:** Construct a physically sourced response-reference object \(R\) with transformation behavior and declared observer/control implementation, and show a selector \(\mathcal P(\Sigma,R)\) is (a) local, smooth on a specified chart; (b) symplectically Lagrangian; (c) operationally accessible under actual P6 conditions; and (d) transformed equivariantly under permitted symmetries. If \(R\) is added by hand, label the result CONDITIONAL rather than CR-derived.

## B2. Acoustic tensor matching, not speed-only matching

Take a three-dimensional local scalar effective Hamiltonian in a fixed chart,

\[
H_m[N]=\tfrac12\int d^3x\,N\big(A(x)P^2+K^{ij}(x)\partial_iq\partial_jq\big),\quad A>0,\quad K=K^T>0,
\]

with \(\{q(x),P(y)\}=\delta(x-y)\). Coefficients are treated as field-independent during the **matter-matter** bracket; metric dependence is allowed, but neither depends on q or P. Under compact support/appropriate boundary conditions,

\[
\begin{split}
\frac{\delta H_m[N]}{\delta q}&=-\partial_i(NK^{ij}\partial_jq),\\
\frac{\delta H_m[N]}{\delta P}&=NAP.
\end{split}
\]

Consequently

\[
\boxed{
\{H_m[N],H_m[M]\}
=\int d^3x\,P\partial_iq\,AK^{ij}(N\partial_jM-M\partial_jN)
=:D_m[v],
\quad v^i=AK^{ij}(N\partial_jM-M\partial_jN).
}
\]

The symmetric lapse product \(NM\), including derivatives of q and K, cancels on antisymmetrization. The **necessary and sufficient coefficient condition** for equality of this matter H-H shift with the standard ADM spatial metric for all q,P,N,M on an open chart is

\[
\boxed{AK^{ij}=g_{\mathrm{physical}}^{ij}\quad\text{(full 3×3 tensor, six components).}}
\]

The 1D flat P9.70 case \(K=2\kappa r^2\), \(g^{xx}=1\) reduces to \(2A\kappa r^2=1\) under the reported normalization. Matching only \(\omega^2=c^2 k^2\) along one line does **not** certify the tensor condition. The exact verifier matches an offdiagonal anisotropic rational SPD metric and exhibits an isotropic mismatch.

**Full spatial covariance is a separate condition.** For the standard minimally coupled scalar with scalar q, momentum density P and dynamical SPD metric g, choose density-correct couplings

\[
A(g)=1/\sqrt{g},\qquad K^{ij}(g)=\sqrt{g}\,g^{ij},
\]

or any physically justified matching with the correct spatial density transformation laws. The product equality alone, with an externally fixed spatial background, does **not** prove D-H/D-D covariance, nor does it independently source g from P7/P8 or determine A and K from original CR.

## B3. Provenance of one negative DeWitt direction

Let the microscopic six-momentum Hessian \(C(q)\) be positive definite. A smooth **real configuration-preserving canonical transformation** has momenta related by an invertible linear Jacobian at each configuration (up to q-dependent shifts). The transformed quadratic momentum Hessian is a real congruence \(J^TCJ\), therefore its inertia stays \((6+,0-)\).

**Theorem H61.2 (positive-source signature obstruction).** Under the preceding premises, no such transformation, including H52's invertible K₄ six-edge-to-metric coordinate map, turns \(C>0\) into the inverse DeWitt kinetic Hessian with signature \((5+,1-)\). Simple restriction to a real momentum subspace or minimization of a positive quadratic also cannot introduce a negative kinetic direction.

At \(g=I\), with six independent symmetric momentum coordinates
\(p=(\pi_{11},\pi_{22},\pi_{33},\pi_{12},\pi_{13},\pi_{23})\),

\[
Q_{\rm DW}(p)
=p_1^2+p_2^2+p_3^2+2(p_4^2+p_5^2+p_6^2)
-\tfrac12(p_1+p_2+p_3)^2.
\]

Its tracelike vector \((1,1,1,0,0,0)\) has value \(-3/2\); two tracefree diagonal directions and all three offdiagonal directions are positive and together give the exact inertia \((5+,1-)\). The verifier also checks a nontrivial positive microscopic Hessian and its exact H52 K₄ Jacobian congruence remains positive. This negative conformal *supermetric* direction is not, by itself, a claim of a physical ghost: lapse constraints and gauge reduction matter.

**Routes left open, none derived by H61:** (i) an independently sourced indefinite geometric kinetic sector; (ii) an extended system with non-positive sector plus first-class constraints and consistent reduction; (iii) a mechanism fundamentally beyond real configuration-preserving canonical congruence. Complex coordinate tricks, an arbitrary sign reversal or just declaring DeWitt by hand are not physical provenance.

## B4. Coupled ADM+matter brackets: CONDITIONAL canonical consistency versus CR generation

Let

\[
\mathcal H=\mathcal H_{\rm ADM}(g,\pi)+
\frac{P^2}{2\sqrt g}+\frac{\sqrt g}{2}g^{ij}\partial_iq\partial_jq+\sqrt g V(q),
\]

\[
\mathcal D_i=\mathcal D_i^{\rm ADM}+P\partial_iq.
\]

**If** the standard ADM gravitational phase space, Hamiltonian/diffeomorphism constraints, minimally coupled scalar with proper density weights, canonical brackets, regularity and appropriate boundary conditions are *assumed*, then the familiar off-shell constraint algebra is

\[
\begin{aligned}
\{D[v],D[w]\}&=D[[v,w]],\\
\{D[v],H[N]\}&=H[\mathcal L_vN],\\
\{H[N],H[M]\}&=D[g^{ij}(N\partial_jM-M\partial_jN)].
\end{aligned}
\]

Sign conventions for the first two brackets may reverse with the chosen generator convention; fix them globally when implementing.

**Important mixed-bracket audit:** For standard minimally coupled scalar matter with no dependence on gravitational momentum \(\pi\) or metric derivatives, the anti-symmetrized gravity-matter H-H cross-term cancels pointwise because it is proportional to \(NM-MN\). This statement has extra hypotheses and is *not automatic* for CR-induced derivative-coupled effective matter, kinetic mixing, nonlocal memory terms or anomalous boundary contributions. The matter-matter calculation in B2 is an off-shell algebraic identity, not the full coupled B4 closure.

**Independent-CR provenance remains completely OPEN:** a CR-generated physical KKS polarization; metric and susceptibility values; negative DeWitt supermetric direction; lapse/shift as first-class multipliers; nonuniform-field canonical brackets with spatial delta distributions; mixed constraint cancellation; correctly treated boundaries; and Einstein-Hilbert/Einstein dynamics. Reusing assumed ADM dynamics would prove only conditional compatibility, never emergence.

## Exact finite verification

Run

`python3 P3/P9H61PolarizationMetricDeWittGatesExactCheck.py`

to independently check all six torus-frequency spectral projectors and the rank-12 KKS tangent, conditional coherent-response local rank, full anisotropic \(AK^{ij}=g^{ij}\) coefficient comparison, K₄ positive Hessian congruence and explicit five-plus/one-minus DeWitt witnesses. The general theorems and B2 functional derivative are established in the analytic proofs above; the finite code is a reproducible rational audit, not a substitute for proving continuum field-theory HDA or observational/physical-origin gates.

## H62 recommended next

Prioritize **B1 response selector provenance**: formalize the set of P6-allowed observable/coherent channels, their residual U(1)^4 stabilizers, and the exact access/no-go criterion for a local Lagrangian splitting on the actual P9.70 micro-sector. Simultaneously ask P9.70 for the concrete physical micro-orbit, source controls and \(A,K^{ij}\) derivation. Defer any claim of B4 full off-shell HDA until B1 and B3 provenance gates have genuine microscopic candidates. Keep H61 Draft/unmerged, P9 Minimum Success unmet.
