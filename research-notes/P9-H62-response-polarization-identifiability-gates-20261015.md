# H62 — P9.70/71 Response Polarization: Phase-Silence, Conditional Metric Selection and Stiffness Identifiability Gates

**2026-10-15 | P3–P11 Mathematical Bridge → P9 GR-I / P9.72.** Stacked on H61 Draft PR #80. Inputs are the P9-supplied four-level reference density, control/readout definitions and conditional coherence metric. H62 independently verifies exact finite statements **without** asserting the actual P3 hidden flow/P6 fingerprint implements these instruments. Neither H62 nor P9.70 establishes P9 Minimum Success. Research Draft, not merged; human peer review, Lean proof, and experiment absent.

## 0. Three distinct choices that should not be called the same “polarization”

On an SU(2)/U(1) orbit of nonzero spin radius r, away from its poles, local KKS coordinates \((q,p)\) obey \(\{q,p\}=1\). Distinguish:

1. **Lagrangian foliation** \(L=\ker dp=\mathrm{span}\{\partial_q\}\): each regular \(p\)-level is a one-dimensional Lagrangian leaf. It is already fixed by the **given** population moment map and is U(1)-invariant. No response metric is necessary to select this foliation. This does **not** contradict H61's torus-invariant **linear six-plane** No-Go at the **diagonal full U(4) basepoint**, which has different domain and isotropy assumptions.
2. **Horizontal/conjugate completion** \(H\), transverse to the leaves, hence a choice of local canonical angular coordinate up to shear \(q\mapsto q+f(p)\): an additional positive response metric may select \(H=L^{\perp_G}\), but only if it is physically constructed and declared.
3. **Absolute phase origin/reference** \(q=0\): neither \(p\) nor a U(1)-invariant isotropic metric singles out an origin. The residual constant \(q\mapsto q+\alpha\) is a genuine reference freedom. A calibrated X/Y frame can fix it **relative to an apparatus**, not derive an absolute CR phase.

In 2D every one-dimensional leaf is Lagrangian automatically. An argument about 2D canonical shear uniqueness must **not** be overclaimed as a full 12D KKS polarization selector or as Einstein-compatible ADM coordinates.

## 1. P9.70/71 microscopic input and full diagonal-basepoint control response

Take \(\rho_0=\mathrm{diag}(0.4,0.3,0.2,0.1)\). Define \(X_{ab}=E_{ab}+E_{ba}\), \(Y_{ab}=-i(E_{ab}-E_{ba})\), \(Z_{ab}=(E_{aa}-E_{bb})/2\); admissible controls *for this mathematical comparator* are \(H_c=\sum_{a<b}(u_{ab}X_{ab}+v_{ab}Y_{ab})\).

At the diagonal reference and with convention \(\dot{\langle O\rangle}=i\langle[H_c,O]\rangle\), each edge gives

\[
\frac{\partial\dot{\langle X_{ab}\rangle}}{\partial v_{ab}}
=2(\lambda_a-\lambda_b),\quad
\frac{\partial\dot{\langle Y_{ab}\rangle}}{\partial u_{ab}}
=-2(\lambda_a-\lambda_b).
\]

The full six-edge 12×12 first-control-jet Jacobian has full real rank 12 because every gap is nonzero. This is **control identification at a declared diagonal state with already calibrated X/Y axes**. It neither measures the phase of a coherent state nor constructs a polarization from P3/P6 data.

## 2. H62.1 — X/Y first-control-jet phase-silence theorem

Use P9's 1–2 level U(2) orbit, so its inherited eigenvalues are \(0.3,0.2\), with \(c=1/4\), \(r=1/20\). On the regular patch \(|p|<r\),

\[
\rho^{(12)}=\begin{pmatrix}c+p&R e^{-iq}\\R e^{iq}&c-p\end{pmatrix},
\quad R=\sqrt{r^2-p^2},
\quad \langle X\rangle=2R\cos q,\quad
\langle Y\rangle=2R\sin q,\quad
\langle Z\rangle=p.
\]

For \(H_c=uX+vY\), the exact **instantaneous** first-control-jet response is

\[
\boxed{\Sigma_{XY}^{(1)}(q,p)=
\frac{\partial(\dot{\langle X\rangle},\dot{\langle Y\rangle})}
{\partial(u,v)}
=\begin{pmatrix}0&4p\\-4p&0\end{pmatrix}},
\qquad \partial_q\Sigma_{XY}^{(1)}=0.
\]

This is a **strict phase-information No-Go for this specified two-channel, zero-time control-response fingerprint**. Even at coherent states with \(R>0\), every \(q\) with the same \(p\) produces the same \(\Sigma_{XY}^{(1)}\). The abstract fact that the 12×12 control Jacobian is invertible at \(\rho_0\) does not evade this distinction.

**Explicit rational witness:** \(p=3/100\), \(R=1/25\), \(r=1/20\) on the genuine U(2) suborbit of P9's four-level diagonal \(\rho_0\). Phase \(q=0\) corresponds to coherence \(R\), while phase \(q=\pi/2\) corresponds to coherence \(-iR\). Their X/Y control responses are equal; their coherent states are different. No approximation is used.

### H62.2 — an additional Z control-response channel restores q sensitivity, conditionally

Keeping the same calibrated \(X,Y\) controls, the extra response is

\[
\frac{\partial\dot{\langle Z\rangle}}{\partial(u,v)}
=(2R\sin q,\,-2R\cos q).
\]

Thus the full three-output response \(\Sigma_{XYZ}^{(1)}\), at \(R>0\) with known \(p,r\), determines \(\cos q,\sin q\) **relative to** the declared X/Y control orientation. In the rational witness above the two phase choices yield \((0,-2/25)\) and \((2/25,0)\). The absolute phase origin remains externally calibrated; the physical realizability and independent background/noise calibration under P6 are NOT proven.

This does **not** assert that the published/previous P6 response fingerprint \(\Sigma\) actually contains this Z response, or that its observer closure, allowed instruments and control-independent dephasing satisfy the same assumptions.

## 3. H62.3 — positive readout metric selects horizontal shear only under independently fixed calibration

P9 proposed

\[
G=w(d\langle X\rangle^2+d\langle Y\rangle^2)+w_Z d\langle Z\rangle^2,
\qquad w,w_Z>0.
\]

Importantly, this is the **pullback metric of the expectation readout map** \(R_{\rm obs}(\rho)=(\langle X\rangle,\langle Y\rangle,\langle Z\rangle)\) with an *externally chosen positive quadratic weighting*. It is **not automatically** the pullback of the original P6 causal-response fingerprint \(\Sigma\): an explicit, rank-controlled identification must be supplied.

In local coordinates,

\[
G_{qq}=4w(r^2-p^2)>0,\quad
G_{pq}=0,\quad
G_{pp}=w_Z+\frac{4wp^2}{r^2-p^2}>0.
\]

The symplectic shears \(\tilde q=q+f(p)\), \(\tilde p=p\) preserve \(dq\wedge dp\). A general metric transforms as \(G_{p\tilde q}=G_{pq}-G_{qq}f'(p)\). Consequently, for the specified isotropic fixed X/Y frame,

\[
\boxed{G_{p\tilde q}=0\iff f'(p)=0.}
\]

This **fixes horizontal transport/angle shear up to constant** for this declared metric, not the origin of \(q\), the metric itself, the full-orbit polarization, the microscopic Hamiltonian, or the physical observer algebra.

**Sharp dependence on weighting/reference (two exact counterexamples):**

- **Anisotropic X/Y readout:** \(G=w_XdX^2+w_YdY^2+w_Zdp^2\), \(w_X\ne w_Y\), gives \(G_{pq}=4p(w_X-w_Y)\sin q\cos q\). At the *same* \(p=3/100\), \(r=1/20\), \(w_X=1,w_Y=2\), \(G_{pq}/G_{qq}=0\) at \(q=0\), while it is \(-25/4\) at \(q=\pi/4\). No single \(p\)-only shear \(f'(p)\) makes **both** orthogonal. Equal X/Y weights are substantive extra structure, not implied by KKS nondegeneracy.
- **State-dependent rotated calibration frame:** choose \(\chi(p)=2p\), \(X'=2R\cos(q-\chi(p))\), \(Y'=2R\sin(q-\chi(p))\). Equal positive weights **in this other frame** induce \(G=G_{pp}^{(0)}dp^2+G_{qq}(dq-2dp)^2\). Its orthogonal canonical angle is \(\tilde q=q-2p\), **not** the original \(q\), though the KKS form and \(p\) remain identical. This is a different declared measurement family, not an unphysical contradiction. The frame choice must be fixed by real physical data.

Every positive metric on a 2D patch can locally define a horizontal complement, but no *particular* metric or calibration-frame dependence follows from P3 hidden-flow merely because such a complement exists.

## 4. H62.4 — 4-site phase gauge and loop-observable boundary

For the six oriented K4 coherence phases, diagonal site rephasing shifts edge phase \(q_{ab}\) by \(\theta_a-\theta_b\). The incidence map \(B:\mathbb R^6\to\mathbb R^4\) has rank 3, so independent relative phase gauges form a 3D space and (where all relevant coherences are nonzero) three independent cycle phase combinations are gauge invariant. Three triangles through site zero furnish an exact basis.

All six externally calibrated X/Y axes remove relative site-rephasing freedom, leaving the common center U(1) as an apparatus-preserving diagonal subgroup. This *does not* create an absolute CR phase: the calibration was additional input. On P9's **single** coherent U(2) edge, there is no cycle; its only edge phase changes under the relative U(1), so no gauge-invariant intrinsic angular zero can be obtained from that edge alone. These are precise finite gauge facts, not an assertion that cyclic Wilson-type response phases cannot be physically measured with expanded instruments.

## 5. H62.5 — first-control-jet cannot identify microscopic stiffness (limited no-go)

For a controlled Hamiltonian \(H(u,v)=H_0+uX+vY\), with state \(\rho\) fixed at the observation instant,

\[
\frac{\partial}{\partial u}\left.
\frac{d}{dt}\langle O\rangle\right|_{t=0}
=i\mathrm{Tr}\,\rho[X,O],
\]

which is independent of *any* additive background \(H_0\), including distinct neighbor gradient interactions and independently selected local stiffnesses. Therefore **this instantaneous first-control-jet cannot determine the physical values of \(A\) and \(\kappa_i\)**. For a conditional P9.70 IR family, two otherwise identical reference/control models with \(\kappa_1=1\) and \(\kappa_1=2\) can have exactly the same first local control-response jet and distinct IR sound speeds \(2A\kappa_1 r^2\).

**Scope:** This is not a universal no-go for the full finite-time, spatially distributed P6 response fingerprint \(\Sigma\), spectroscopy, multi-time probes, or independently calibrated Hamiltonian estimates. Recovering stiffness requires specified additional time/space probes and their inverse-conditioning/stability estimates, and provenance linking these parameters to P3 hidden flow.

## 6. Three-gate verdict requested by P9

| P9 question | H62 exact/conditional verdict | Open physical gate |
|---|---|---|
| (1) Does **actual P6** \(\Sigma\) produce positive coherent metric? | Declared readout \(R_{\rm obs}\) produces positive G; \(\Sigma^{(1)}_{XY}\) is phase-silent | Explicit \(D\Sigma\) / readout identification, positivity, instrument/noise/phase calibration, physical P6 controls |
| (2) Does G + hidden flow uniquely select polarization? | \(p\)-foliation intrinsically selects a **1D** Lagrangian leaf on U2; conditional isotropic G fixes transverse shear up to constant; gauge phase origin absent | CR-sourced positive metric/frame, actual hidden-flow horizontal connection and symmetry-breaking reference |
| (3) Does selected polarization fix stiffness/gradient? | NO for the specified zero-time first-control jet | Longer time/spatial response, \(A,K^{ij}\) identifiability, P7/P8 tensor matching, lattice→IR control and P9.72 error bounds |

**P9.72 handoff:** An approximate many-body→mean-field KKS reduction must identify the **physical observable/control algebra**, the coherent-sector preparation, common phase reference, the time/space response range, and provide errors sufficient to keep relevant Jacobian singular values bounded away from zero as the system size and continuum limit vary. Mere convergence of trajectories is not by itself a selector-provenance theorem. The bridge's rank/No-Go checks can then be transported conditionally; without those data the true microscopic P3/P6 selector remains OPEN.

## Exact audit

\`python3 P3/P9H62ResponsePolarizationIdentifiabilityExactCheck.py\` independently checks the P9 four-level control response, two coherent U2 phase choices with identical X/Y instant response and distinct Z response, isotropic metric/shear identity, anisotropic readout and rotated-frame dependence, K4 gauge-cycle rank and first-control-jet stiffness non-identification. Universal statements are justified by the displayed commutator, moment-map, incidence and tensor calculations, not by finitely sampled points alone. Keep Draft/unmerged, no frozen-paper edits or GR success claim.
