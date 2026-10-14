# H40 — One fixed microscopic GKSL channel, P3 two-step residue, and finite-time operational matching

**2026-10-14 | P3–P11 Mathematical Bridge.** Follow-on to H39 Draft PR #58. This is a **conditional finite constructive alignment in an augmented standard-GKSL control architecture**, not a nontrivial proof that a P3/P4-generated static sector is the **independently frozen** P6 \(\mathcal J_N\). Does not assert a CR-exclusive signature, physical Levi-Civita soldering, ADM/HDA or Einstein dynamics. Main and frozen papers are untouched. Independent human peer review/Lean kernel proof not claimed.

## 1. Specify all microscopic inputs before any residue calculation

Work in \(M_3(\mathbb C)\), diagonal population MASA \(D_3\), sites on 0–1–2. **First independently declare** a radius-one static microscopic candidate sector
\[
\mathcal J_{\rm static}
=\mathrm{span}_{\mathbb C}\{E_{01},E_{21}\}
\subset\mathcal A_3^{[\le1]}.
\]
Its first-residue map \(\Xi(J)=Q_D(J-J^\dagger)\) contains the original concrete P6 anti-Hermitian real coherent controls
\[
A=E_{01}-E_{10},\quad B=E_{21}-E_{12},
\quad K=aA+bB
=\Xi(aE_{01}+bE_{21}).
\]
Set rational physical parameters **before computing the dynamic hidden sector**:
\[
a=2/3,\quad b=3/5,\quad
\gamma=1/2,\quad
\alpha=\operatorname{diag}(1/7,0,-1/11).
\]
Fix ONE preparation channel for every step and both clocks:
\[
\mathcal L(\rho)=[K,\rho]-i[\alpha,\rho]
+\gamma(\Delta_D\rho-\rho),\qquad
\Phi_t=e^{t\mathcal L}.
\]
The generator is legitimate GKSL for gamma≥0, with anti-Hermitian K and Hermitian alpha. The Stark term alpha and the phase-reference/readout modules are explicitly **additional independently calibrated coherent capabilities** beyond frozen P6's two-real-exchange target control manifold; do not relabel them as inherited CR operators. The microscopic J_static above is a **fixed compatible candidate**, NOT the proven frozen P6 \(\mathcal J_3\).

## 2. Original-P3 depth-three witness of the SAME two-step channel

Prepare \(d=E_{00}\). For one fixed positive t set
\[
\rho_1=\Phi_t(d),\quad
\rho_2=\Phi_t(\rho_1)=\Phi_{2t}(d),\quad
z=Q_D\rho_1\in\mathcal H_1(\Phi_t,D_3),\quad
w=Q_D\rho_2\in\mathcal H_2(\Phi_t,D_3).
\]
The **actual original P3 quadratic commutator witness** is
\[
R(t)=\Delta_D([z,w^\dagger])
=i\operatorname{diag}(\partial_1j),\quad
j_{uv}=2\operatorname{Im}(z_{uv}\bar w_{uv}).
\]
The exact leading time coefficient is
\[
\boxed{[t^3]R(t)
=2ia^2(\alpha_0-\alpha_1)(E_{00}-E_{11})
=\frac{8i}{63}(E_{00}-E_{11}).}
\]
It is independent of control-independent gamma for this specified generator, and agrees with the independently audited P9.38 \(+2i\) diagonal-gauge Laplacian theorem. For sufficiently small t the selected signed witness is nonzero. The checker uses **t=1/4096** and degree-16 exact rational Taylor expansions of \(\rho_1,\rho_2\), together with independently proved entrywise semigroup remainder estimates, to certify the actual R00(t) is nonzero rather than merely its polynomial approximation.

This does **not** prove \(\dim\mathcal R_3\) or the entire original P3 residue filtration is nonzero in a stronger way than the displayed nonzero witness; a single nonzero vector is all that is used.

## 3. The two-step quantum intertwiner succeeds only with full hidden data

A deliberately explicit nonidentity *coordinate* isomorphism tests the full bridge conditions, not a guessed population match. Choose
\[
G=\operatorname{diag}\bigl(1,(3+4i)/5,1\bigr),
\quad\iota(X)=GXG^\dagger.
\]
Define the physical **gauge-coordinate representation** of the same channel by
\[
K_{\rm phys}=GKG^\dagger,\quad
\mathcal L_{\rm phys}(\rho)
=[K_{\rm phys},\rho]-i[\alpha,\rho]
+\gamma(\Delta_D\rho-\rho).
\]
The **exact** identities (checked on all 9 matrix units) are
\[
\boxed{\iota\mathcal L=\mathcal L_{\rm phys}\iota},
\qquad
\iota\Delta_D=\Delta_D\iota,
\quad\iota(X^\dagger)=\iota(X)^\dagger,
\quad\iota(XY)=\iota(X)\iota(Y).
\]
Consequently \(\iota\Phi_t^j=\Phi_{t,\rm phys}^j\iota\) for **every** \(j\ge0\) (by analytic exponentiation) and in particular j=1,2; \(\iota\) maps the original P3 hidden pairs and their quadratic signed residue. Since R is diagonal, \(\iota(R)=R\). This also maps the **chosen** static sector \(\mathcal J_{\rm static}\) and its \(\Xi\) directions to its gauge-coordinate representation.

**Critical limitation:** the two channels were explicitly **constructed to be gauge-conjugate**, so this is an existence check of the exact matching conditions, not a discovery of a nontrivial microscopic-to-independent-hardware CR provenance map. Moreover \(K_{\rm phys}\) need not be real skew in the transformed coordinate basis; this is only a common site-phase representation of one quantum model, not a new P6 physical target manifold.

## 4. A population-only two-step **No-Go in the same channel**

The diagonal observation \(C=\Delta_D\) does not close under this coherent update. Let the one-step classical population-only surrogate be \(T_t=\Delta_D\Phi_t|_{D_3}\). Then a direct Taylor calculation gives
\[
\boxed{
\Delta_D\Phi_t^2(d)-T_t^2(d)
=t^2\Delta_D\mathcal L^2(d)+O(t^3),
\quad
\Delta_D\mathcal L^2(d)=2a^2(E_{11}-E_{00})\ne0.}
\]
The exact checker verifies the coefficient in its same rational model. Thus even when the full quantum two-step intertwiner is exact, inserting a population projection *between* updates destroys the two-step matching. P9.38 independently exhibited a different pair of CPTP maps agreeing at one population step and differing at two steps; here the failure is within **one** fixed channel under an intermediary observer projection.

The failure is standard quantum coherent transport, not a CR-exclusive non-Markovian memory theorem.

## 5. Matched positive-time H39 operational reading of actual hidden jets

The preparation at t and 2t uses the **same** fixed \(\Phi_t\). The observer receives independently prepared copies of \(\rho_1,\rho_2\). At each readout it switches the right exchange b and the preparation Stark detuning off and uses the H39 **signed ±a positive-time GKSL** interrogation with the same calibrated gamma, then (in a separate setting) the **additional calibrated** phase gate \(V=\mathrm{diag}(-i,1,1)\) and independently calibrated attenuation \(q=3/4\).

With \(D_{a,\gamma}(s)=8a\,g_{a,\gamma}(s)\) at interrogation time s=1/4, H39 gives finite-time population contrasts:
\[
C_X=D_{a,\gamma}(s)\,\Re\rho_{01},\qquad
C_Y=D_{a,\gamma}(s)q\,\Im\rho_{01}.
\]
No dissipative inverse is applied. Exact 3-level GKSL Taylor jets verify **both** identities for each of the two actual time-prepared states, as well as a rational nonzero-transmission semigroup enclosure for D. From these physical contrasts and independently calibrated phase reference one can reconstruct \(z_{01}\), \(w_{01}\) and the **01 contribution** \(j_{01}\) to the original P3 residue.

**Do not overclaim**: a 01-only observer does not measure the 02 contribution to the root residue in a three-site dynamically spreading system. H36, however, bounds this omitted current:
\[
|R_{00}(t)-i j_{01}(t)|
=|j_{02}(t)|
\le \frac{2e^{12Jt}(32J^2t^2)^2}{(2!)^2},
\quad J=\max(a,b).
\]
For t=1/4096, use the independent rational majorant \(e^{12Jt}\le(1-12Jt)^{-1}\). Together with the actual preparation Taylor remainders and independently declared population-contrast/tomography errors, the checker certifies
\[
|\widehat j_{01}|>
B_{02}(t)+E_{\rm prep}(t)+E_{\rm readout}
\]
for the displayed *extremely high-precision conditional observation parameters*. Thus the measured 01 current **certifies a nonzero signed root P3 residue** in this explicitly fixed augmented mathematical model, while the **full residue vector** remains unread by this single-edge protocol. The measurement precision (e.g. 10^-16 contrast-error assumption), coherent preparation/phase stability, and actual hardware capability are **additional conditional inputs**, not experimentally demonstrated.

## 6. Physical status and standard-GKSL comparator

The microscopic P3 update, algebraic candidate J_static, quantum two-step intertwining, and conditional positive-time 01 measurement can all be written in a **single standard GKSL model**. This closes a finite **internal consistency/existence** problem, including a nonzero true P3 witness and a quantitative readout bound. It does **not** prove the independently frozen P6 \(\mathcal J_N\) is this sector, nor that its original declared real-exchange hardware can independently enable the Stark shift, coherent phase gate, coherent reference state, or signed pulse controls. The gauge-coordinate \(\iota\) is **chosen**, not microphysically derived. Because conventional GKSL with the same parameters predicts **the identical signed residue and readout**, no stronger CR-specific experimental discriminator is obtained.

**H40 conditional verdict:** PASS for one coherent explicitly fixed micro/operational comparator model, *- and Δ-compatible gauge-coordinate two-step map and mathematically certified 01-edge **partial** operational residue readout; FAIL for a population-only intermediate observer projection as an automatic two-step intertwiner; OPEN for genuine independent P3/P6 provenance, fully accessible physical tomography, CR-exclusive discrimination, soldered spacetime curvature, ADM/HDA and Einstein dynamics.

**H41 next gate:** ask whether a **genuinely independent** static P3/P4 inherited microscopic sector, fixed *without referencing the selected physical control/response outcome*, can impose a testable inequality stronger than standard GKSL given identical independently calibrated data. If not, freeze the bridge as a conditional controllability/tomography theorem with a no-discriminator statement instead of claiming an experimental CR origin.

## Reproducibility

P3/P9H40SingleChannelTwoStepOperationalExactCheck.py reuses CI-passed H38/H39 rational-Gaussian control modules. It independently computes the fixed 3-site GKSL preparation Taylor jets, original P3 depth3 coefficient, physical signed residue at a small certified finite time, exact 9-matrix-unit strong generator intertwining, gauge-invariance of the residue, the nonzero population-Markov two-step defect, the two actual prepared states' H39 interrogation-coefficient identities and a rigorous rational total readout+omitted-edge error budget. Dedicated Actions CI. No floating tolerance, new Lean kernel formalization, human expert review, or physical measurement claim.