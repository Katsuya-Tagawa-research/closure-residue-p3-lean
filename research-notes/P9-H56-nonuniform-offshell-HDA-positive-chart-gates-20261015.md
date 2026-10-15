# H56 — Positive K₄ Canonical Chart and Nonuniform Off-Shell ADM Constraint Algebra

**2026-10-15 | P3–P11 Mathematical Bridge / P9 GR-I, separate from the independently progressing P9.64 KKS↔ADM origin audit.** Stacked on [H55 Draft PR #74](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/74) whose all 68 CI workflows were PASS at H56 start.

**Central boundary:** H56 tests the transport of **ordinary externally supplied ADM canonical theory**, *not* the microphysical origin of its symplectic form, constraints, action, physical spacetime or HDA from original P3/P4. The KKS→ADM symplectic origin is appropriately retained for P9.64 and is not solved in the H56 geometry/canonical-chart code. No original manuscripts or main edited, no human peer review, Lean formalization or experiments.

## 1. Imported verified assumptions and exact scope

Accept H52–H55 as **conditional finite/geometry results** with exact restrictions:

1. The internal \(S=\mathbf1^\perp\subset\mathbb R^4\), frame \(f_i=e_i-e_3\), Gram \(G\), K₄ edges \(v_e\), and local SPD metric \(g(w)=16 G B(w)^{-1}G\), \(B(w)=\sum_e w_ev_ev_e^\top\); **six positive edge weights** define a local positive chart in SPD3 with invertible Jacobian \(J^A{}_e(w)=\partial q^A/\partial w_e\).
2. The physically soldered \(C^4\) three-dimensional smooth spatial manifold, gluing across neighboring K₄ cells, ADM 3+1 foliation, lapse \(N>0\), shift \(\xi^i\), ADM gravitational action and canonical Poisson brackets are **additional declarations**. H52–H54 did NOT derive them from CR; H55 pulled back standard ADM algebra into a local chart.
3. All smeared constraints below use smooth **compactly supported lapses/vector fields** on an open spatial patch with uniformly positive weights, or independently specified physical boundary conditions and boundary Hamiltonians that make integrations by parts legitimate. The examples are rational Taylor **jets at a point**, NOT replacement of the full spatial field-theory functional bracket by 3×3 matrix commutators.

## 2. H56.1: positive-edge cone not preserved by fixed-solder spatial shears

In the nonorthonormal spatial K₄ frame
\[
G=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix},\quad
w_\star=(1,1,1,1,1,1),\quad g_\star=4G
=\begin{pmatrix}8&4&4\\4&8&4\\4&4&8\end{pmatrix}.
\]
Take the orientation-preserving invertible spatial coordinate shear
\[
Q=\begin{pmatrix}1&\frac12&0\\0&1&0\\0&0&1\end{pmatrix},
\quad\det Q=1,\quad g'=Q^\top g_\star Q.
\]
The corresponding SPD metric is positive. **However**, if one insists on re-expressing the raw sheared coordinate metric components \(g'\) using the **SAME fixed physical K₄ solder/frame**, the exactly inverted edge weights are
\[
\boxed{w'(g')=\left(\frac52,\frac12,\frac74,1,-\frac12,\frac32\right),}
\]
so the fifth edge weight is **negative** even though \(g'\succ0\), \(\det g'=\det g_\star=256\), and all original six \(w_e=1\) were positive. The map \(w\mapsto g(w)\) remains invertible on its full algebraic SPD-admissible extension, but the **strictly positive** domain is a proper chart patch, not invariant under arbitrary spatial GL+ coordinate changes at fixed solder.

This does **not** contradict coordinate covariance of the physical metric. The true same physical tensor in the **original spatial chart** is recovered by \(g=(Q^{-1})^\top g'Q^{-1}\), whose unique K₄ weights are all positive again. Equivalently, the physical solder/frame must co-transform with the physical coordinate basis. These are distinct procedures; treating K₄ edge numbers as six invariant scalar fields while fixing their tensor-index solder silently is not a diffeomorphism-covariant construction.

At the infinitesimal level, the Lie derivative \(\mathcal L_\xi g\) induces
\[
\boxed{\delta_\xi w
=J(w)^{-1}\operatorname{symvec}(\mathcal L_\xi g).}
\]
For every strictly positive \(w\), infinitesimal transformations of sufficiently small parameter remain locally in that open chart; a finite transformation may cross its boundary. Physical global covariance requires local chart transitions and/or solder transformations, and a proof of their consistency. The exact checker verifies the shear, all six recovered weights, the inverse Jacobian action and preservation of the K₄ canonical one-form \(\pi^{ij}\delta g_{ij}=p_e\delta w_e\).

## 3. Off-shell HDA: the precise claim and its algebraic proof

Adopt as **external** the standard ADM constraints on a soldered smooth 3-dimensional spatial slice with no boundary flux for the declared smearing functions:
\[
\mathcal H_\perp
=\frac1{\sqrt g}(\pi^{ij}\pi_{ij}-\tfrac12\pi^2)
-\sqrt g R^{(3)},\qquad
\mathcal H_i=-2g_{ik}\nabla_j\pi^{jk},
\]
where \(\pi^{jk}\) is a **symmetric contravariant density of weight one**. Define \(H[N]=\int N\mathcal H_\perp\) and \(D[\xi]=\int \xi^i\mathcal H_i\).

**Standard ADM HDA with the explicitly chosen sign convention**:
\[
\boxed{
\begin{aligned}
\{D[\xi],D[\eta]\}&=D[[\xi,\eta]],\\
\{D[\xi],H[N]\}&=H[\xi^i\partial_i N],\\
\{H[N],H[M]\}&=D[\beta],\\
\beta^i&=g^{ij}(N\partial_jM-M\partial_jN).
\end{aligned}
}
\]
The metric-dependent structure function \(g^{ij}(w(x))\) and field-dependent \(\beta\) are **essential**; this is a hypersurface-deformation **algebroid** relation, not a Lie algebra of constant structure constants and not an ordinary commutator of finite \(K_4\) matrices. The HDA is an **off-shell** identity on the ADM phase space, including fields where \(\mathcal H_\perp\ne0\) and \(\mathcal H_i\ne0\).

For the only subtle Hamiltonian-Hamiltonian bracket, variation of the lapse-smeared curvature potential gives the Hessian-of-lapse term
\[
\frac{\delta H[N]}{\delta g_{ij}}\Big|_{\partial N}
=\sqrt g\left(g^{ij}\Delta N-\nabla^i\nabla^jN\right),
\quad
\frac{\delta H[M]}{\delta\pi^{ij}}
=\frac{2M}{\sqrt g}
\left(\pi_{ij}-\frac12\pi g_{ij}\right).
\]
Antisymmetrizing \(\{H[N],H[M]\}\) cancels the **ultralocal** kinetic/metric terms, leaving
\[
\boxed{
\mathfrak B[N,M]
=2\pi^{ij}\left(N\nabla_i\nabla_jM-M\nabla_i\nabla_jN\right).
}
\]
With \(\alpha_j=N\partial_jM-M\partial_jN\) and \(\beta^i=g^{ij}\alpha_j\), using the density-weight-one identity
\[
\nabla_i\pi^{ij}=\partial_i\pi^{ij}+\Gamma^j{}_{ik}\pi^{ik}
\]
one obtains the **exact LOCAL equality**
\[
\boxed{
\mathfrak B[N,M]
=\beta^i\mathcal H_i+\partial_i\bigl(2\pi^{ij}\alpha_j\bigr).
}
\]
The current divergence is NONZERO in general **at a point**; only after integration with legitimate support/boundary conditions does the last term vanish and the canonical smeared H-H HDA bracket follow. The proof uses neither \(\mathcal H_\perp=0\) nor \(\mathcal H_i=0\): it is genuinely off-shell.

The exact rational tester takes **nonuniform spatial weight gradients and Hessians**, nonzero Christoffels and curvature, nonuniform symmetric momentum-density gradients, two independent lapses with nonzero values/gradients/Hessians, and finds
\[
\boxed{
\mathfrak B=\frac{150139237}{93562560},\qquad
\beta^i\mathcal H_i=\frac{4413193}{3132864},\qquad
\partial_i(2\pi^{ij}\alpha_j)=\frac{56099}{286195}.
}
\]
These three fractions satisfy the exact local identity (and are individually nonzero); the Hamiltonian and momentum constraints are also **not** set to zero.

Further exact tests:
- **Diffeomorphism–momentum closure:** for independent affine vector fields on a nonuniform metric two-jet, \([\mathcal L_\xi,\mathcal L_\eta]g=\mathcal L_{[\xi,\eta]}g\).
- **Diffeomorphism–Hamiltonian covariance:** the kinetic Hamiltonian density transforms as a **weight-one spatial scalar density**, \(\delta_\xi\mathcal H_{\rm kin}=\xi^i\partial_i\mathcal H_{\rm kin}+\mathcal H_{\rm kin}\partial_i\xi^i\), while the curvature potential has the same tensor-density transformation under H53's independently soldered smooth metric.
- **Nonuniform K₄ shift generator:** \(p_e\delta_\xi w_e=\pi^{ij}(\mathcal L_\xi g)_{ij}\), and the exact local momentum-density identity includes the boundary current \(\partial_j(2\pi^{ji}g_{ik}\xi^k)\).

Therefore the **full off-shell HDA is available, conditionally, on the positive-chart patch of the standard ADM continuum phase space** because H55's invertible K₄ cotangent lift preserves the canonical symplectic form. This is not a newly independent derivation of HDA from original CR dynamics. Only the H-H local Hessian mechanism and selected D-D/D-H transformation properties are **separately cross-checked** in exact finite rational jets here, not an exhaustive finite enumeration of arbitrary smooth fields or a new Lean formal proof of all functional Poisson brackets.

## 4. P9.64 parallelism: precise microphysical KKS→ADM map gates

P9 separately pursues **P9.64 — KKS symplectic structure to ADM canonical structure**. H56 neither changes nor presumes the result of P9.64. Its contribution is a necessary condition ledger for any such origin claim.

Let \((\mathcal O,\omega_{\rm KKS})\) be the independently defined (pre)symplectic microscopic coadjoint orbit and \((\mathcal P_{\rm ADM},\Omega_{\rm ADM})\) a declared physically relevant ADM canonical phase-space sector. A candidate microscopic map \(F:\mathcal O\to\mathcal P_{\rm ADM}\) purporting to transport the actual canonical geometry must explicitly address:

1. **Symplectic relation:** \(F^*\Omega_{\rm ADM}=\omega_{\rm KKS}\) on its defined domain, or an explicitly documented reduction/constraint procedure if the forms are presymplectic. Checking equality of dimension counts, Hessians, antisymmetric matrices, or the H52 DeWitt *symmetric* supermetric is NOT this condition.
2. **Differential rank:** for a genuinely symplectic finite-dimensional \(\mathcal O\), pullback equality into a symplectic target requires \(DF\) injective. If claiming a local symplectomorphism onto an open full 12-dimensional ADM \((g_{ij},\pi^{ij})\) fiber, the source must have rank 12 and \(DF\) must be invertible. A lower-dimensional symplectic source may embed into a **constrained submanifold**, but cannot parametrize the full open ADM canonical fiber.
3. **Physical solder/covariance:** the map must be independent of post-fit observations and compatible with spatial chart changes, \(S\leftrightarrow TM\) soldering, the six-weight cone transitions and physically allowed control/intervention families.
4. **Dynamics and constraints:** pulling back \(\Omega_{\rm ADM}\) is necessary but not sufficient to derive the ADM Hamiltonian/EH action or its first-class HDA. Prove a dynamical intertwiner or independently generated Hamiltonian and correct lapse/shift/matter/boundary condition laws, *without re-importing standard ADM as an unexplained premise*.
5. **Field-theoretic limit:** explain how local finite KKS orbits assemble into a spatial continuum with delta-function canonical brackets, constraints, consistent spatial gluing and compatible gauge identifications. A single K₄ cell and finite matrix KKS form alone do not carry continuum derivatives.

These are conditional **necessary audits, not assertions about what P9.64 has already proved**. The present H56 local positive-cone shear obstruction is relevant to #3: a proposed microphysical solder cannot identify the same fixed positive-edge coordinates under every spatial diffeomorphism without chart/solder transitions.

## 5. H56 research conclusion, scope, and handoff

**PROVEN within declared external ADM premises:** (a) local positive K₄ cone not globally invariant at fixed solder, with a concrete determinant-one spatial shear counterexample; (b) exact cotangent/metric Lie derivative and local canonical 1-form compatibility; (c) explicit **nonuniform off-shell** H-H bracket density equals momentum constraint density plus total divergence and gives the smeared bracket on legitimate support; (d) D-D Lie closure and D-H kinetic weight-one covariance checked in nonuniform rational jets; (e) ADM full HDA transports via the canonical map on its local positive chart.

**NOT proven/NOT claimed:** HDA generated from CR/KKS, valid global six-scalar K₄ weights under arbitrary diffeomorphisms, independent 3+1 spacetime emergence from finite P3/P4, the actual microscopic P9.64 symplectic map, a nonstandard quantum/Einstein prediction, physical experimental validation or journal referee acceptance.

**H57 candidate:** under the same explicit conditional ADM hypotheses, establish a functional-domain/atlas criterion for solder-compatible transitions across the K₄ positive cone, with corner/boundary currents and off-shell bracket closure (when transitions are canonical). Then independently compare to P9.64's microscopic KKS candidate, without claiming its outcome in advance. If no independently physical solder/map can be constructed, retain H56 as a precise *conditional coordinate equivalence* rather than declare generative Einstein gravity.

## Reproducibility

`P3/P9H56NonuniformOffshellK4HDAExactCheck.py` uses standard-library Fraction rational arithmetic and previously audited H52/H53/H55 metric and canonical maps. It verifies the shear edge weights, the nonuniform off-shell density identity with exact rational fractions and nonzero constraints, Lie brackets and density covariance, and boundary-current terms. Dedicated stacked Draft PR CI; no frozen manuscript/main edits, human review or new Lean kernel.
