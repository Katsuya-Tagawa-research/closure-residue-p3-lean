# H49 — Controlled-process provenance certificate and the exact operational-equivalence boundary

**2026-10-15 | P3–P11 Mathematical Bridge.** Stacked on H48 Draft PR #67. The aim is to audit the **actual controlled microscopic CPTP process**, rather than asserting an inherited physical P6 control from an uncontrolled P3 update or from static closure data. The same H42 genuine rational 3-site unitary CPTP baseline \(\Phi=\mathrm{Ad}_U\), the same H46 twelve-outcome calibrated CP instrument \(\{\mathcal I_{k,t}\}\), and the H41 independently postulated static collective sector \(J_{\rm col}\) are reused unchanged. No frozen papers/main edits, new Lean formalization, human review, real hardware experiment, Lorentzian/Einstein dynamics or CR-only effect.

## 1. Declare the source/physical objects *before* looking at responses

Label sites 0 (left), 1 (center), 2 (right), and take the real-skew coherent physical tangent carrier
\[
W=\operatorname{span}_{\mathbb R}\{A,B\},\quad
A=E_{01}-E_{10},\quad B=E_{21}-E_{12}.
\]
The independently **hypothesized** static collective source is
\[
J_{\rm col}=\operatorname{span}_{\mathbb C}\{T,T^\dagger\},
\quad T=E_{01}+E_{21},\quad \Xi(J)=Q_D(J-J^\dagger).
\]
Then \(\Xi(T)=A+B\) and \(\Xi(J_{\rm col})\cap W=\mathbb R(A+B)\). **Do not call \(J_{\rm col}\) derived from P3**: H42's same genuine P3 filtration provides a counterexample to such an automatic implication.

Choose a precommitted source map \(S_\lambda(x)=x\lambda T\), with \(\lambda=3/5\), so its predicted physical tangent is
\[
K_{\rm source}=\Xi(S_\lambda'(0))=\tfrac35(A+B).
\]
A declared actual **controlled microscopic** channel can instead be any
\[
\boxed{\Psi_x^K=\operatorname{Ad}_{e^{xK}}\circ\Phi,\qquad K=aA+bB,}
\]
with positive-time unitary control and the **identical** uncontrolled \(\Psi_0=\Phi\). This is conventional CPTP for all real x. The independent source hypothesis \(K=\Xi(S'(0))\) can be tested by comparing K recovered from the controlled process with the previously frozen source map. **Specifying S beforehand is a premise**, not a derivation or hidden inference from the target response. In this finite W:
\[
\boxed{\exists S:\mathbb R\to J_{\rm col}\text{ real linear, }\Xi S'(0)=K
\ \Longleftrightarrow\ a=b.}
\]
This is necessary/sufficient for algebraic source **factorization**, NOT the full physical micro-to-instrument causality provenance or CP quotient.

## 2. Exact conditional quantum instrument first-order certificate on an ORIGINAL diagonal seed

Use the allowed diagonal center seed \(d=E_{11}\). The baseline microscopic state \(\Phi(d)\) is precisely the H42 rational physical density matrix. Apply the predeclared H46 instrument **only after** the controlled update. Define its two *conditional output coherence slopes*
\[
u_K=\left.\frac d{dx}
\bigl(\mathcal I_{0,0}(\Psi_x^K(d))\bigr)_{01}\right|_{x=0},
\quad
v_K=\left.\frac d{dx}
\bigl(\mathcal I_{0,1}(\Psi_x^K(d))\bigr)_{01}\right|_{x=0}.
\]
From the genuine exact baseline \(U\), H46 rational diagonal Kraus \(D_0=\operatorname{diag}(1,3/5,0)\), and \(\frac d{dx}\Psi_x^K(d)|_0=[K,\Phi(d)]\), the **exact all-rational transfer** is
\[
\boxed{
\begin{pmatrix}u_K\\v_K\end{pmatrix}
=-\frac1{30}
\begin{pmatrix}3&4\\4&3\end{pmatrix}
\begin{pmatrix}a\\b\end{pmatrix}.
}
\]
This two-by-two matrix has determinant \(-7/900\ne0\), so the signed microscopic **real** tangent is identifiable from these two coherences:
\[
\boxed{
a=\frac{30}{7}(3u_K-4v_K),\quad
b=\frac{30}{7}(-4u_K+3v_K).
}
\]
In particular,
\[
\boxed{K\in\Xi(J_{\rm col})\cap W
\ \Longleftrightarrow\ a=b
\ \Longleftrightarrow\ u_K=v_K.}
\]
This is a **necessary and sufficient, directly refutable INSTRUMENT-TANGENT MEMBERSHIP certificate** for the specified two-real-control finite microscopic model and the existing full conditional quantum-output readout. It does **not** prove Jcol was physically sourced from P3, nor that the actual frozen P6 hardware can measure these coherences. Such measurement requires *post-selection-aware quantum-state tomography* / independently calibrated phase reference and control, beyond H46's original **classical flag-only** protocol.

The same 12 **classical outcome probabilities** have **zero** first derivative at this seed. Over the full W, their tangent response map has rank zero; the two conditional quantum-coherence slopes have rank two. The checker also computes full instrument-tangent matrices for all nine input matrix units and certifies rank two on W. Thus an unbiased classical flag estimator at second order is **not** interchangeable with signed coherent tangent tomography at first order.

For the three preregistered same-exchange-norm controls
\[
(a,b)\in\{(3/5,3/5),(3/25,21/25),(3/5,-3/5)\},
\quad a^2+b^2=18/25,
\]
only the first satisfies the oriented \(J_{\rm col}\)-membership. Both \(a=b\) and \(a=-b\) have zero *direct-center* H47 classical left-minus-right flag at all x, yet this full instrument-coherence certificate distinguishes their signs. Even an observed signed-control certificate does not *explain its source*; it only tests consistency with the precommitted S.

## 3. Genuine two-step controlled CPTP process, rather than only a tangent from one snapshot

Use two independent real pulse parameters \(x,y\) with the **same fixed microscopic controlled family**:
\[
\Psi_y^K\Psi_x^K(d)=
\operatorname{Ad}_{e^{yK}}\Phi\bigl(
\operatorname{Ad}_{e^{xK}}\Phi(d)\bigr).
\]
For all nonnegative m,n its exact formal joint Taylor coefficient is
\[
\boxed{
[x^m y^n]\Psi_y^K\Psi_x^K(d)
=\frac{\operatorname{ad}_K^n\,\Phi\,
\operatorname{ad}_K^m\,\Phi(d)}{m!\,n!},
}
\]
where \(\operatorname{ad}_K(X)=[K,X]\). The source checker verifies through all \((m,n)\) with \(m+n\le2\), using the original H46 **full twelve quantum instrument outputs** and separately the **classical output frequencies**, for three actual diagonal seed inputs and the three physical control tangents. This calculation includes the mixed two-step coefficient \(xy\); it is not simply a population-only one-step test.

For the locked and unlocked same-norm controls and original center seed, the DIFFERENCE of the final signed H46 flag Taylor coefficients is
\[
\begin{array}{c|ccccc}
(m,n)&(1,0)&(0,1)&(1,1)&(2,0)&(0,2)\\
\hline
[\mu_{\rm lock}-\mu_{\rm unlock}]_{x^m y^n}
&4/75&-4/25&-64/625&-24/625&152/625.
\end{array}
\]
Every entry is exact Gaussian rational. Both sides are **ordinary standard CPTP dynamics**. These two controlled models differ because the independently specified *physical K differs*, not because CR changes the quantum evolution equation.

**Operational-equivalence no-discriminator lemma:** If a proposed CR physical model and a standard quantum model have *identical* initial density, every **controlled CPTP superoperator** \(\Psi_x\) available in the permitted experiment, every CP instrument branch, and the same classical postprocessing, then by repeated composition they give **identical probabilities and conditional quantum records at every finite depth**, for arbitrary allowed adaptive instrument protocols. Hence the finite model has **no operational CR-only deviation from that matched standard CPTP model**. A strict *prediction-set restriction* from a precommitted, physically sourced accessibility hypothesis can still be tested, but the restriction must be separately justified and cannot be represented as non-GKSL evolution.

## 4. Invasive instrument versus passive two-time samples

The legitimate microscope-only no-insertion observer at depth two is
\[
\mathcal E\Phi^2(d),\qquad \mathcal E=\sum_{k,t}\mathcal I_{k,t}.
\]
If the H46 instrument is physically *inserted after the first* microscopic step and its outcome forgotten, the actual process is instead
\[
\mathcal E\Phi\mathcal E\Phi(d).
\]
For the original center diagonal d and the same rational microscopic U, the exact **center-site difference** is
\[
\boxed{
\left[\mathcal E\Phi^2(d)-\mathcal E\Phi\mathcal E\Phi(d)\right]_{11}
=\frac{32}{81}\ne0.
}
\]
Thus an instrument *compatible with the initial diagonal preparation* need not be a non-disturbing repeatable probe of later generated coherences. Two-step process claims must specify whether the measurements are on **separately prepared copies with endpoint observation** or are **invasive sequential instrument outcomes on one evolving system**. Merely fitting their classical distributions does not establish an all-depth channel intertwining.

## 5. Exact finite-positive-control CPTP example without transcendental assumptions

The continuous coherent process \(\Psi_x^K\) above uses \(e^{xK}\). To test a completely **rational finite-strength** controlled process independently, choose the genuine orthogonal **Cayley gate**
\[
Q_h(K)=(I+hK)(I-hK)^{-1}
=I+\frac{2h}{1+h^2r^2}K+
\frac{2h^2}{1+h^2r^2}K^2,
\quad r^2=a^2+b^2,\quad h=1/4>0.
\]
For every chosen rational K, \(Q_h(K)^\dagger Q_h(K)=I\); hence
\[
\widetilde\Psi_h^K=\operatorname{Ad}_{Q_h(K)}\circ\Phi
\]
is a bona fide finite CPTP controlled update, and so are two successive updates. Both the locked and unlocked gates share the same uncontrolled \(\Phi\), graph, static-source metadata and aggregate norm, but differ in process outputs. **Critical timing caveat:** the Cayley gate is a *distinct finite-step implementation*, **NOT** equal to \(\exp(xK)\) for the same nominal x. H49 never substitutes this rational gate for the finite-time exponential in H47's sine bound.

## 6. Honest experimental provenance status and H50 gate

**PASS finite mathematics:** exact injective two-component conditional quantum-instrument first-order response with the 2×2 inverse; \(u=v\) iff K in the oriented source \(\Xi(J_{\rm col})\) for W; classical instrument first-order null; two-step controlled process full instrument jet coefficients; invasive intermediate instrument distinction; bona fide positive-strength rational-Cayley quantum channels; identical full controlled processes under identical standard CPTP instruments give identical all-depth observational laws.

**CONDITIONAL PASS:** a source-controlled provenance **consistency certificate** given ex-ante \(J_{\rm col}\), a proposed source map S, verified physical control process and independently permitted full quantum instrument tomography. The certificate can **falsify** declared tangent-source membership. It cannot by itself prove the microscopic **origin** of S or the physical *-orientation, nor that the same source is inaccessible within a standard quantum model.

**FAIL/OPEN:** deriving P6's actual \(\mathcal J_N\) or its physical S solely from original P3/P4 full-diagonal dynamics; realizing H46 conditional quantum-output coherence tomography with P6's frozen two-real-knob apparatus; CR-exclusive quantum prediction after full matched standard process calibration; Lorentzian curvature, ADM/HDA and Einstein field equations.

**H50 gate:** audit whether an independently generated original-P3/P4 source process **with independently provided controlled interventions** imposes any nontrivial additional identity on *all controlled quantum process tensors* beyond the standard quantum operational equivalence class. If none exists, freeze a precise no-framework-discriminator theorem for the H35–H49 standard-GKSL finite sector and separate it from P9's gravitational/EH assumptions; shift emphasis to genuinely derived *-compatible provenance or independent gravity-dynamics premises. Alternatively formalize H49's kernel and causal instrument criterion in Lean on the finite rational state sector, without misrepresenting finite code PASS as Lean kernel proof.

## Reproducibility

`P3/P9H49ControlledProcessProvenanceCertificateExactCheck.py` reuses the exact unchanged original H42 microscopic U and H46 instrument; checks all nine input matrix units and all twelve instrument branches, unique signed tangent recovery, full two-controlled-step Taylor coefficients and distinct classical cross-jet values, the original H43 invasive two-step population discrepancy, and independent finite positive Cayley-controlled CPTP gates with Gaussian-Fraction matrices. A dedicated GitHub Actions check is attached to the stacked Draft PR. Main and frozen papers unchanged; no numerical tolerance, new Lean proof, human peer review or real experimental validation.