# P9.38 → P3–P11 Mathematical Bridge: Independent Audit A (2026-10-14)

**Numbering:** this is an **independent P9.38 cross-audit**, not new H24–H27 entries. The bridge already uses H24–H34 for different validated tasks. Existing H21–H34 and all frozen manuscripts remain untouched. Audit labels: **PASS** proven finite mathematics; **CONDITIONAL PASS** algebra requires specified matching/measurement/locality assumptions; **FAIL** stronger implication has an explicit counterexample; **OPEN** physical/provenance construction absent.

**Summary verdict:**
- **PASS**: diagonal-Hamiltonian Laplacian identity including +2i coefficient; exact K4 six weights/rank-3 kernel/minor; witness-variation surjectivity; weighted connected-component gauge stabilizer; calibration residual sign.
- **CONDITIONAL PASS**: identification with *leading* depth-three original P3 witness under a small-time CPTP map; divergence/current matching on an already identified oriented edge basis.
- **PASS** (negative result): KKS pullback on the **independent product** \(\mathcal O_p\times\mathcal W_+\) has kernel dimension 6.
- **FAIL** as a proposed automatic implication: first population-step equivalence ⇒ two-step map intertwining; explicit **two CPTP unitary** counterexample.
- **OPEN**: independent frozen P6 \(\mathcal J_N\) provenance, calibrated control-phase readings, mixed symplectic polarisation selected by CR, ADM/HDA and Einstein dynamics.
- **No CR-exclusive discriminator** emerges from any of these ordinary CPTP/GKSL calculations.

## A1. General diagonal-gauge Laplacian identity — PASS

Let \(\Delta_D\) be the diagonal conditional expectation in the **same chosen orthonormal basis**, \(Q_D=I-\Delta_D\). Let d and \(\alpha=\operatorname{diag}(\alpha_a)\) be Hermitian and diagonal. Let \(\mathcal L_0\) be a complex-linear **Hermiticity-preserving** linear superoperator. (Its GKSL nature is needed to assert a physical forward CPTP semigroup, not for the algebra.) Put
```math
\mathcal L_\alpha=\mathcal L_0-i\operatorname{ad}_{\alpha},\quad
A=Q_D\mathcal L_0(d),\quad
B_\alpha=Q_D\mathcal L_\alpha^2(d).
```
Because \([\alpha,d]=0\), the first hidden jet is independent of alpha. Applying \(\mathcal L_\alpha\) again and using the fact that \(\alpha\) commutes with every diagonal matrix gives
```math
Q_D\mathcal L_\alpha(d)=A,\qquad
B_\alpha=B_0-i[\alpha,A].
```
Hermiticity preservation ensures \(A_{ba}=\bar A_{ab}\). Write \(w_{ab}=|A_{ab}|^2=w_{ba}\ge0\), \(L_w=\sum_{a<b}w_{ab}(e_a-e_b)(e_a-e_b)^T\). For each diagonal coordinate a,
```math
\begin{aligned}
(\Delta_D[A,B_\alpha-B_0])_{aa}
&=-i\sum_b\{A_{ab}(\alpha_b-\alpha_a)A_{ba}
-(\alpha_a-\alpha_b)A_{ab}A_{ba}\}\\
&=+2i\sum_b|A_{ab}|^2(\alpha_a-\alpha_b).
\end{aligned}
```
Therefore the exact identity is
```math
\boxed{\Delta_D([A,B_\alpha])-\Delta_D([A,B_0])
=+2i\operatorname{diag}(L_w\boldsymbol\alpha).}
```
A general *-preserving superoperator may have no CPTP interpretation unless it is a valid GKSL generator; positivity is not used in the algebra. We assume the **same** \(\mathcal L_0\) for all phase settings; control-dependent dissipators or detunings included inside \(\mathcal L_0\) invalidate this simple difference formula unless recalibrated.

The exact stabilizer of this **signed leading witness** is \(L_w\alpha=0\). Since
```math
\alpha^T L_w\alpha=\sum_{a<b}w_{ab}(\alpha_a-\alpha_b)^2,
```
it consists of vectors constant on each connected component of the positive-weight support graph. In particular for connected support it is \(\mathbb R\mathbf1\). This **does not** classify every population gauge under all observables, nor the entire P3 filtration \(\mathcal R_k\). A diagonal \(\alpha\) that is invisible to a first population derivative is a **physical coherent Hamiltonian difference**, not automatically a gauge symmetry of all higher responses.

## A2. Which original P3 depth? — CONDITIONAL PASS for its leading coefficient

Original P3 defines \(\mathcal H_k=Q_D\operatorname{span}\{D,\Phi(D),\ldots,\Phi^k(D)\}\) for a **discrete CPTP update** \(\Phi\) and
```math
\mathcal R_k=\operatorname{span}_\mathbb C
\{\Delta_D([z,w^\dagger]):z\in\mathcal H_i,
\;w\in\mathcal H_j,\;i+j\le k\}.
```
To connect a continuous GKSL generator to that definition, **choose** the same small-time discrete map \(\Phi_\tau=e^{\tau\mathcal L_\alpha}\), \(\tau>0\), and use
```math
z_1=Q_D\Phi_\tau(d)
=\tau A+\tfrac{\tau^2}{2}B_\alpha+O(\tau^3),\quad
z_2=Q_D\Phi_\tau^2(d)
=2\tau A+2\tau^2 B_\alpha+O(\tau^3).
```
Since \(z_1\in\mathcal H_1\), \(z_2\in\mathcal H_2\), both Hermitian, their P3-legal depth-(1+2)=3 witness obeys
```math
\boxed{\Delta_D([z_1,z_2^\dagger])
=\tau^3\Delta_D([A,B_\alpha])+O(\tau^4).}
```
So the **variation in its leading coefficient** is \(+2i\tau^3\operatorname{diag}(L_w\alpha)\). This does **not** prove \(\mathcal R_2=0\), \(\dim\mathcal R_3=N-1\), or stability/equality of \(\mathcal R_3(\Phi_\tau)\) under alpha. For finite \(\tau\), \(\mathcal R_2\) already includes commutators between possibly different first-hidden diagonal preparations and may contain nonzero higher-order terms. Scanning alpha **changes the discrete channel** and compares vectors from different spaces \(\mathcal R_3(\Phi_{\tau,\alpha})\); it is not a construction of N-1 independent witnesses *inside one fixed* residue subspace. Distinguish the **signed anti-Hermitian witness**, its line/span, the **full filtration subspace**, and physical observer outputs.

## A3. K4 exact arithmetic — PASS

With \(d=\operatorname{diag}(9,5,7,3)/24\), \(H=\sum_{a<b}(E_{ab}+E_{ba})\), and \(\mathcal L_0(\rho)=-i[H,\rho]+\gamma(\Delta_D\rho-\rho)\), \(\gamma\ge0\),
```math
A=\begin{pmatrix}
0&i/6&i/12&i/4\\
-i/6&0&-i/12&i/12\\
-i/12&i/12&0&i/6\\
-i/4&-i/12&-i/6&0
\end{pmatrix}.
```
Thus for ordered edges 01,02,03,12,13,23:
```math
w=(1/36,\;1/144,\;1/16,\;1/144,\;1/144,\;1/36).
```
The displayed P9.38 Laplacian matrix was independently reproduced **exactly**. It has rank 3, kernel \(\mathbb R(1,1,1,1)^T\), and leading principal 3×3 minor \(95/746496\). Therefore \(L_w\) is invertible on \(S=\mathbf1^\perp\), and the map \(\alpha\mapsto+2i\operatorname{diag}(L_w\alpha)\) is onto \(iD_4^{0,\rm sa}\). This is the **space of variations across alpha** of a selected leading witness, not automatically \(\dim\mathcal R_3=3\) for a fixed map.

In this **specific** uniform-site-dephasing model, \(B_0\) contains the term \(-\gamma A\), whose bracket with A vanishes, and
```math
\Delta_D([A,B_0])
=\frac{2i}{9}\operatorname{diag}(-1,1,1,-1)
```
is itself gamma-independent. The Laplacian variation identity is gamma-independent much more generally **when varying alpha leaves the rest of \(\mathcal L_0\) fixed**. This does NOT imply that all first-hidden data or device parameters are dephasing-independent for an arbitrary GKSL model.

## A4. Calibrated second-jet sign and error — PASS, conditional physical relevance

If \(\alpha_{\rm true}\) is physical and \(\alpha_{\rm cal}\) is the independently measured calibration, define
```math
B^{\rm cal}=B_{\alpha_{\rm true}}
+i[\alpha_{\rm cal},A].
```
Then exact perfect calibration gives \(B^{\rm cal}=B_0\). For the unambiguous convention \(\delta\alpha=\alpha_{\rm cal}-\alpha_{\rm true}\),
```math
\boxed{R^{\rm cal}-R_0
=-2i\operatorname{diag}(L_w\,\delta\boldsymbol\alpha),}
```
where \(R^{\rm cal}=\Delta_D([A,B^{\rm cal}])\), \(R_0=\Delta_D([A,B_0])\). Reversing delta-alpha's convention reverses the sign. A robust norm bound is \(\|R^{\rm cal}-R_0\|_{2}=2\|L_w\delta\alpha\|_2\). P6's separately calibrated **site dephasing** is not an independent calibration of diagonal Stark energies, phase shifts, or control-dependent dissipative perturbations. Reconstructing B and A may itself require coherent state tomography beyond diagonal-only population readout.

## A5. Hidden current matching, K4 cycles and soldering — CONDITIONAL PASS

For Hermitian hidden A,B, put one real current on each oriented edge a<b:
```math
j_{ab}=2\operatorname{Im}(A_{ab}\bar B_{ab}).
```
With \(\partial_1(e_{ab})=e_a-e_b\), the original signed P3 residue witness is **exactly**
```math
\Delta_D([A,B])=i\operatorname{diag}(\partial_1j).
```
Thus **after an explicitly fixed common vertex/edge basis and orientation**
```math
R_{\rm phys}=R_{\rm mic}\iff
j_{\rm phys}-j_{\rm mic}\in\ker\partial_1.
```
On K4, \(\partial_1:\mathbb R^6\to\mathbb R^4\) has rank3, kernel dimension3. One cycle-current basis is
```text
edge order: (01,02,03,12,13,23)
(1,-1, 0,1,0,0), (1,0,-1,0,1,0), (0,1,-1,0,0,1).
```
Hence identical divergence **cannot** determine the three cycle-current components. Three distinct matches must not be conflated:
1. **Strong update intertwining:** a specified cross-model map intertwines the two CPTP dynamics through two actual steps, plus a diagonal/*-algebra-compatible embedding if residues are to match.
2. **Full hidden edge-current equality** \(j_{\rm phys}=j_{\rm mic}\), which implies equal divergence, but not equality of the underlying A,B pair or update map.
3. **Only signed residue/divergence matching**, allowing arbitrary cycle currents in \(\ker\partial_1\).

For a nonabelian SO(3) connection, even agreement of individual loop traces is insufficient for gauge soldering: H25 (existing PR #43) demands simultaneous based-loop conjugacy. Current divergence is an entirely different datum from a calibrated parallel-transport holonomy. Neither condition 2 nor 3 establishes geometric Levi-Civita/Regge transport.

## A6. KKS/ADM polarization — finite product No-Go PASS; physical choice OPEN

For nondegenerate four-level spectrum \(p\), \(\mathcal O_p\cong U(4)/U(1)^4\) has real dimension 12 and nondegenerate KKS 2-form \(\omega_{KKS}\). On the explicitly independent product \(\mathcal P=\mathcal O_p\times\mathcal W_+\), let \(\pi_1\) forget conductances w∈(0,∞)^6, and define \(\Omega=\pi_1^*\omega_{KKS}\). Then
```math
\operatorname{rank}\Omega=12,\qquad
\ker\Omega=\{0\}\times T\mathcal W_+,\qquad
\dim\ker\Omega=6.
```
This is an exact geometric fact; the checker independently verifies the rank in a local 12-dimensional Darboux chart augmented with six null coordinate directions. Existing P3 hidden flow and P6 First-Residue Accessibility, as stated, provide **no canonically chosen mixed state-conductance symplectic pairing**, no independent momenta conjugate to each w, and no ADM Hamiltonian constraint algebra.

Minimal new **type of data** for any upgrade: a physically/CR-justified map from six independent w directions to corresponding state-sector covectors or a canonical cotangent sector, including a **nondegenerate six-dimensional mixed pairing** and an integrable/closed 2-form respecting observer gauge and physical dynamics. The mere presence of 12 state coordinates or an **artificial** \(T^*\mathcal W_+\) does not select ADM gravity. Even a symplectic pairing would be far short of off-shell HDA and Einstein dynamics.

## A7. Actual P3/P6 provenance & two-step intertwining — FAIL for automatic implication; OPEN physically

Frozen P6 v9.1's microscopic sector \(\mathcal J_N\) is a *static* independently inherited uniformly local space \(\mathcal J_N\subseteq\mathcal A_N^{[\le r_0]}\) with \(\Xi_N(J)=Q_D(J-J^\dagger)\); First-Residue Accessibility restricts separately declared **physical coherent tangents modulo population gauge**. By contrast original P3 \(\mathcal H_k\) is defined **dynamically from one chosen CPTP update \(\Phi\)**. There is NO established identity \(\mathcal J_N\equiv\mathcal H_k(\Phi)\).

Earlier existing H31–H34 audits are relevant evidence rather than new P9.38 work: H32 generated a connected CPTP map with full original P3 residue and rank-six candidate Xi; H33 proved its exact P3 Krylov sector **violates radius-one P6 locality** on the path and that same microscopic support graph can have Xi ranks 2 or 4; H34 proved minimal invariant operator-system closure for that channel expands from radius one to M3. Therefore neither graph support nor full P3 saturation gives an inherited independent \(\mathcal J_N\).

**Fresh two-step operational counterexample:** let \(U\) be H24's exact rational 2x2 unitary, and let the second unitary be \(W=VU\) with \(V=\operatorname{diag}(i,-i)\). Both channels are single-Kraus **CPTP**. For \(\rho=E_{00}\), populations after one update are identical:
```math
\Delta_D(U\rho U^\dagger)
=\Delta_D(W\rho W^\dagger)
=\operatorname{diag}(5/9,4/9).
```
Yet after **two repeated updates of the respective channels**,
```math
\Delta_D(U^2\rho(U^\dagger)^2)
=\operatorname{diag}(65/81,16/81),\quad
\Delta_D(W^2\rho(W^\dagger)^2)
=\operatorname{diag}(17/81,64/81).
```
So **even exact first-step population matching does not imply two-step population matching**, much less a two-step microscopic-to-physical intertwiner or equal P3 quadratic residue. Here W=VU is a true physical diagonal phase difference, not an innocuous gauge of repeated dynamics.

A **sufficient conditional structural bridge** would be a fixed trace/*-compatible, injective algebra map \(\iota\) obeying \(\iota D_{\rm mic}\subseteq D_{\rm phys}\), \(\iota\Delta_{\rm mic}=\Delta_{\rm phys}\iota\) on all relevant generated operator sectors, and \(\iota\Phi_{\rm mic}^j=\Phi_{\rm phys}^j\iota\) on diagonal seeds for j=1,2. Then \(\iota\) maps the corresponding P3 hidden pairs and quadratic commutator witnesses to equal physical residues; matching of all witness spaces requires enough seeds/spanning to match both directions, not a one-sided inclusion. A map that only matches **populations** or only is linear (not product/* preserving) is insufficient.

**Still OPEN physically:** actual frozen P6 J_N identification/provenance; independently calibrated P6 hardware phases; physical two-step GKSL intertwiners satisfying the stated structure; a CR-only prediction not reproducible by a matched standard GKSL comparator.

## A8. Governance and next gates

1. Do **not** reuse P9's proposed H24–H27 audit names: existing bridge **H24–H34** are different documented tasks. Call this **P9.38 Cross-Audit A** and maintain trace links.
2. Preserve original P3 residue \(\Delta_D([z,w^\dagger])\) vs chosen Lie commutator, generator parameter variation vs actual observed measurement, and internal gauge/transport vs physical spacetime connection.
3. Report the **minimal physical experiment condition** separately: independent \(\alpha\)/Stark calibration in addition to dephasing; coherences A and B or an identifiable alternative; static \(\mathcal J_N\) obtained before the response data; explicit admissible control and two-step map, matched standard GKSL comparator.
4. P9.38's Laplacian identity is a valuable exact obstruction to treating the P6 diagonal population gauge as a universal higher-residue gauge. It does **not** obtain ADM/HDA, Einstein dynamics, or generative completeness.

### Reproduction

`P3/P938DiagonalGaugeProvenanceCrossAuditExactCheck.py` uses stdlib `fractions.Fraction` and H24's already-audited Gaussian rational class. It independently verifies K4 for three dephasing rates and multiple \(\alpha\) settings; all 6 weights, K4 Laplacian, rank3/nullity1 and \(95/746496\) principal minor; signed witness and calibration signs; 3-cycle divergence kernel; full current-to-residue identity; explicit exact 2-step population counterexample; and block presymplectic rank12/nullity6. Code audits finite algebra, not Lean kernel or experimental provenance.
