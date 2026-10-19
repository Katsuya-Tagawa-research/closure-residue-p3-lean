# H108 — An Exact Source-Output Positive Separability Witness: Robust Operational AX-OA/AX-CAN Handoff, without an Added Hamiltonian

**2026-10-19 | P3–P11 Mathematical Bridge / P9 Conditional Einstein Dynamics, AX-SRC / AX-OA / AX-CAN / AX-SP.**
**Base H107 Draft PR #126 — 100/100 GitHub CI PASS.** Genuine unchanged original H75 four-Kraus six-level CPTP source, genuine original P3 signed R3, original local A/B coherent control permissions and the H105 **independently posited** conditional coherent two-cell X link only as a comparison. Published/frozen P1–P8 and main untouched. No new interaction, gravitational action or P9 Cartan microscopic source assumed at H108.

## 1. Why H107's positive correlation effect was not yet an entanglement certificate

H106 showed the conditional H105 link and original-H75 local product branch have the same **entire joint four-flag distribution**, with genuine actual output flag00 probability \(p_{00}=153/625\), and H106's linked flag00 partial transpose contains a negative 2×2 principal minor \(-2916/390625\), with conditional pure-state entanglement negativity \(6/17\). H107 showed a valid positive site-correlation effect whose flag00 conditional probability differs \(1/2\) vs \(5/34\) for those two particular states. However *arbitrary other separable states* can have nonzero phase correlations too, so this particular comparison did **not** provide a state-independent separability inequality.

H108 asks whether a **genuine, positive, finite-H75-output POVM effect** can be found that exceeds a common upper bound for **ALL separable conditional two-cell site states** while the already-known hypothetical H105 linked output violates it. If yes, the AX-OA gate gains an operationally meaningful entanglement witness that does not assume an entangling Hamiltonian in the detector.

## 2. Exact decomposable entanglement witness and its physical positive effect

On the genuine \(\mathbb C^3_{S_1}\otimes\mathbb C^3_{S_2}\) site carrier use the same standard site basis as H105/H106 and set
\[
|\eta\rangle=\frac{|1,1\rangle+i|2,0\rangle}{\sqrt2},\qquad
\boxed{W=(|\eta\rangle\langle\eta|)^{T_{S_2}}.}
\tag{H108-W}
\]
Since \(|\eta\rangle\langle\eta|\ge0\), for EVERY separable positive two-qutrit state \(s=\sum_k p_k a_k\otimes b_k\), we have
\[
\boxed{\operatorname{Tr}(Ws)=\operatorname{Tr}(|\eta\rangle\langle\eta|\,s^{T_{S_2}})\ge0.}
\tag{H108-PPT-BOUND}
\]
The Hermitian witness has eigenvalues only \(+\tfrac12,-\tfrac12,0\) with \(\|W\|_\infty=1/2\), as can be checked by its nonzero 2×2 block and \(\boxed{W^3=W/4}\). Thus
\[
\boxed{Q=\frac{I_9}{2}-W,\quad 0\le Q\le I_9}
\tag{H108-POVM}
\]
is a genuine **positive effect**, giving a state-independent, normalized separability bound
\[
\boxed{p(Q\mid s)\le1/2\quad\text{for all separable normalized }s.}
\tag{H108-SEP}
\]
Under H75's fixed output \(U\), use the actual positive 36D physical effect
\[
\boxed{
E=|00\rangle\langle00|_{E_1E_2}\otimes
(U\otimes U)Q(U\otimes U)^\dagger.
}
\tag{H108-EFFECT}
\]
The independent ability to calibrate the output detector is explicitly assumed; \(U\otimes U\) is a fixed part of the *existing H75 output*, **not a freely usable pre-reset Hamiltonian gate**.

The effect is not based on a hypothetical joint two-cell entangling measurement: it is a known real linear combination of **local site population and local phase-correlation measurements**. With \(P_i=|i\rangle\langle i|\), \(Y_{12}=-i|1\rangle\langle2|+i|2\rangle\langle1|\), \(Y_{01}=-i|0\rangle\langle1|+i|1\rangle\langle0|\),
\[
\boxed{
W=\frac12(P_1\otimes P_1+P_2\otimes P_0)
+\frac14(Y_{12}\otimes X_{01}+X_{12}\otimes Y_{01}).
}
\tag{H108-LOCAL}
\]
The checker verifies this identity component by component over all 81 matrix entries. Reconstructing the expectation of Q uses only local site \(X/Y\), populations and classical correlations, once detectors are calibrated. The **effective yes/no positive POVM** Q is mathematically legitimate; directly implementing it as a single two-cell POVM device is not asserted.

## 3. Genuine source output with EXACT positive-probability violation (CONDITIONAL to H105's unsourced interaction)

Let the native source input be H106's truly positive, unentangled
\(\rho_{\rm prod}=|1\rangle\langle1|\otimes |+\rangle\langle+|\), \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\). Compare the H105 **externally posited** conditional source-compatible unitary \(R\) state \(\rho_{\rm link}=R\rho_{\rm prod}R^\dagger\), with EXACTLY the same local original-H75 channels and true flag00 output blocks:
\[
\sigma_{00}^{\rm native}=\mathcal J_{00}(\rho_{\rm prod}),\qquad
\sigma_{00}^{\rm link}=\mathcal J_{00}(\rho_{\rm link}),
\quad\operatorname{Tr}\sigma_{00}=p=\frac{153}{625}.
\]
After the fixed local-U calibration, H106's unrotated linked site branch is
\[
\sigma_{00}^{\rm link}=\frac12|v\rangle\langle v|,\quad
v=\frac35|1,0\rangle+\frac{27}{125}|1,1\rangle-\frac{36i}{125}|2,1\rangle,
\]
whereas the native branch is explicitly separable. The witness evaluates to
\[
\boxed{
\operatorname{Tr}(W\sigma_{00}^{\rm native})=\frac{81}{2500}>0,\quad
\operatorname{Tr}(W\sigma_{00}^{\rm link})
=-\frac{4671}{62500}<0.
}
\tag{H108-NEGATIVE}
\]
This is obtained by both the exact original 9D matrix trace and the independent two-index partial-transpose principal-subblock contraction
\(\frac12[\sigma^{T_2}_{44}+\sigma^{T_2}_{66}+\cdots]
=\frac{729}{62500}-\frac{54}{625}
=-4671/62500\).
For the native product source, the nonzero original population of |1,1> gives the positive witness expectation 81/2500; it is not zero. This leads to the **actual positive original-source output probabilities**
\[
\boxed{
\Pr(E\mid{\rm native})=\frac9{100},\quad
\Pr(E\mid{\rm link})=\frac{12321}{62500}.
}
\tag{H108-PHYSICAL}
\]
For the same exact flag00 normalization \(p=153/625\),
\[
\boxed{
\Pr(Q\mid00,\mathrm{native})=\frac{25}{68},\qquad
\Pr(Q\mid00,\mathrm{link})=\frac{1369}{1700}>\frac12.
}
\tag{H108-VIOLATION}
\]
This exceeds the **universal separability bound** by
\[
\boxed{\frac{1369}{1700}-\frac12=\frac{519}{1700}>0.}
\tag{H108-GAP}
\]
The original joint **four coarse flag probabilities remain completely identical**, despite a positive calibrated effect violating the bound after conditioning. Source-local H75 channels and local Hamiltonian / LOCC control from a separable input **cannot generate this NPT-violating conditional state**, as H106 established.

A useful quantitative distinction holds for the normalized conditional linked state \(s_{\rm link}\) and **any separable normalized** \(s_{\rm sep}\):
\[
\boxed{
D_{\rm tr}(s_{\rm link},s_{\rm sep})
=\tfrac12\|s_{\rm link}-s_{\rm sep}\|_1
\ge\frac{519}{1700}.
}
\tag{H108-DIST}
\]
Indeed \(\operatorname{Tr}(W s_{\rm sep})\ge0\), \(\operatorname{Tr}(W s_{\rm link})=-519/1700\), and \(\|W\|_\infty=1/2\) imply \(\|s_{\rm link}-s_{\rm sep}\|_1\ge2(519/1700)\). This is an exact **lower bound**, not an optimized minimal distance proof.

**Scope:** The H108 instrument measures standard-QM entanglement conditional on an **EXTRA** H105 unitary and extra calibrated local detectors; it does not demonstrate this physical link exists, nor discriminate CR from ordinary QM. No new theoretical physical coupling or experiment is introduced.

## 4. What this DOES and DOES NOT transfer from H75 to P9.125–128 Cartan and P11 F

The H108 witness is a concrete new **AX-OA witness** addressing an insufficient readout part of the source-level access problem: coarse original flags cannot distinguish the two processes; valid, separately calibrated local X/Y/site-population detectors can witness actual conditional two-cell entanglement in the postulated link completion. It is NOT a demonstration that the original H75 control system generated the H105 interaction, nor an accessible six-pair ADM canonical field.

The original local-only no-go remains \(\mathfrak{so}(3)\oplus\mathfrak{so}(3)\), source-local operator/superoperator separability, and exact H106 NPT obstruction. **AX-CAN** still requires independent source-generated nonlocal Hamiltonian or actual quantum memory/coupling, physical nondegenerate orbit and real coherent transport, without filling gaps by choosing arbitrary compatible commutants. **AX-SP** requires physically given cell adjacency, actual intercell parallel transport, noncircular spatial solder/metric and torsion/curvature second jet. **AX-DYN** requires sourced DeWitt kinetic, curvature term, momentum constraints and full off-shell HDA rather than imported ADM identities; **AX-NORM** must select gravitational couplings; **AX-GEN** must produce all necessary physical structures from explicit F axioms.

The P9.125–128 connected Cartan source is **not** independently found in the authorized linked GitHub repository or targeted Notion research sources. Therefore the H75 phase witness cannot be declared a P9 Cartan/Einstein prediction by equating the two systems. Only a future **typed physical source-identity/simulation certificate** bearing physical controls, observer algebras, CPTP channel, parallel transport, solder, and primitive dynamics on a shared carrier permits direct integration.

## 5. H108 stop rule and handoff

1. Do not invent H109 as another arbitrary two-cell entangler or simply boost an observational rank.
2. Issue a concise sourced-vs-independent-vs-open P9 handoff referencing H103–H108, with the **specific local-positive measurement bound** \(p_{\rm sep}(Q|00)\le1/2\) and conditional violation \(1369/1700\).
3. The next theorem-worthy physical task is to obtain real P9 Cartan **primary micro Hamiltonian, observer, register dynamics and spatial solder** and see if it can actually instantiate/derive some nonlocal coherent transport rather than merely commute with H75 Kraus operators. Failing that, classify such an interaction as AX-SRC/AX-CAN independently posited, not a theorem of Generative Completeness.

**Verdict:** original 2-cell H75 mathematical source and local-only no-go **EXACT**; decomposable positive effect/separability bound **EXACT**; H105 link output violation **CONDITIONAL EXACT**; common physical Cartan source, sourced nonlocal Hamiltonian, ADM/Einstein/F completeness **OPEN**. No human specialist peer review, physical experiment, or Lean gravitational theorem is asserted.
