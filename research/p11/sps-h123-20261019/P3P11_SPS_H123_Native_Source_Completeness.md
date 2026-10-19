# SPS-H123 — Native-Source Completeness and a Finite Certification Gate

**2026-10-19 — P3–P11 Mathematical Bridge / P11 AX-ORIGIN**  
**Scope:** exact finite-dimensional identifiability theorem and conservative quantitative time-bound for *declared* H37 coherent control directions. Not a claim of actual hardware calibration, exhaustive primitive provenance, AX-ORIGIN from F, or P11 Generative Completeness. Independent SPS naming (distinct from the unrelated H75/P11 H113 of GitHub PR #132). Stacks on SPS-H122 Draft PR #137.

## 1. Four-scalar native-jet response witness (EXACT conditional)

In the original H37 five-site basis indexed 0,…,4, let

\[
K_f=E_{f,f+1}-E_{f+1,f},\quad H_f=iK_f,\quad
p_e=E_{ee},\quad X_e=E_{e,e+1}+E_{e+1,e},\qquad e,f=0,\dots,3.
\]

Each \(H_f\) is Hermitian and each \(p_e\) a normalized physical pure-state matrix. Each \(X_e\) is a Hermitian off-diagonal *proposed* measurement observable, not independently certified hardware readout.

For an ideal identity baseline, define the response matrix

\[
A_{ef}(0)=\operatorname{Tr}[X_e(-i[H_f,p_e])]
=\operatorname{Tr}[X_e[K_f,p_e]]= -2\delta_{ef}.
\]

The equality follows because \([K_f,p_f]=-X_f\), and all distinct undirected edge matrix-unit supports are orthogonal under the trace pairing. Thus

\[
\boxed{A(0)=-2I_4,\ \operatorname{rank}A=4,\ \det A=16,\ \sigma_{\min}(A)=2.}
\]

This is *minimal in scalar count* for identifying an arbitrary four-parameter coefficient vector in the declared linear tangent space: fewer than four real scalar data cannot define an injective linear map from \(\mathbb R^4\). It does not prove that these four readouts are actually available, nor certify their phase reference independently of the target experiment.

If the controls act with small coefficients \(u_f\), the four observed first derivatives obey \(y=A(t)u+o(\|u\|)\) for a common post-baseline pulse; the linearized identification at \(t=0\) is \(u=-y/2\) without measurement error. The apparatus calibration and the word “native” remain separately postulated.

## 2. Positive finite-time continuity theorem, with a conservative explicit bound

Use the fixed H37 generator

\[
\mathcal L(\rho)=-i[H_0,\rho]+\tfrac23(\Delta_D(\rho)-\rho),\quad
H_0=\tfrac12\sum_{e=0}^3X_e+\operatorname{diag}(0,1/7,-1/9,2/11,-3/13).
\]

Let \(B_t=e^{t\mathcal L}\) and measure the same post-baseline control jets from prepared \(p_e\):

\[
A_{ef}(t)=\operatorname{Tr}\left[X_e(-i[H_f,B_t(p_e)])\right].
\]

The row-sum bound for the Hermitian \(H_0\) gives \(\|H_0\|_{\mathrm{op}}\le 5/4\); the Hilbert–Schmidt induced norm of \(\Delta_D-I\) is 1. Consequently,

\[
\|\mathcal L\|_{2\to2}\le2\|H_0\|_{\mathrm{op}}+\tfrac23\le\tfrac{19}{6}.
\]

Each matrix element satisfies

\[
|A_{ef}(t)-A_{ef}(0)|\le 2\sqrt2\left(e^{19t/6}-1\right)
\]

and the 4-by-4 spectral norm obeys

\[
\|A(t)+2I_4\|_2\le8\sqrt2(e^{19t/6}-1).
\]

By the singular-value perturbation bound,

\[
\sigma_{\min}(A(t))\ge2-8\sqrt2\left(e^{19t/6}-1\right)>0
\]

when \(0\le t<\frac6{19}\log(1+\frac1{4\sqrt2})\approx0.05140\), in the fixed mathematical time units. This bound is deliberately loose and is **not** a hardware scheduling recommendation. In particular, at \(t=1/100\), the elementary inequality \(e^x-1\le x/(1-x)\) yields an exactly certified perturbation bound

\[
\|A(1/100)+2I_4\|_2 \le \frac{152\sqrt2}{581}<2.
\]

Thus even with a finite baseline H37 evolution, the proposed readout matrix remains mathematically invertible for at least a specified short-time window.

If exact \(A(t)\) is calibrated and additive measurement noise is \(\eta\), the recovered four-vector \(\widehat u=A(t)^{-1}(A(t)u+\eta)\) satisfies \(\|\widehat u-u\|_2\le\|\eta\|_2/\sigma_{\min}(A(t))\). The result says nothing about uncalibrated systematic error or failed state-preparation and measurement assumptions.

## 3. Finite native catalogue completeness is an independent gate (restricted No-Go)

Define formal completion A with the four marked Hermitian control Hamiltonians \(\{H_0,H_1,H_2,H_3\}\) and formal completion B with these four **and** an independently actuated but *unmarked* diagonal detuning Hamiltonian

\[
H_{\rm extra}=p_0-p_1.
\]

Fix the same H37 baseline channel and the same exact native pulses/protocols involving **only the four marked knobs**. Then every experiment using that alphabet returns identical data for the two formal completions, including all orders in those marked controls. Nevertheless their actual first-order native control spaces have real dimensions four versus five. The extra direction is linearly independent of the marked off-diagonal directions. It is also invisible to the chosen diagonal-input/off-diagonal-readout protocol exactly at the identity-baseline point, since \([H_{\rm extra},p_e]=0\). This particular latter invisibility need not persist for finite \(t\) if the extra actuator is activated after coherent baseline evolution; it is not used in the all-marked-orders no-go.

**Theorem (relative exhaustive-inventory obstruction).** No selector from the complete collection of data over a *fixed restricted marked alphabet* can correctly return both formal native catalogues when unmarked actuator existence may differ. Proof is by data-fibre nonconstancy. This is not an observation of two actual H37 hardware devices and does not rule out independent engineering certification of the full hardware port set.

**Conditional positive source certificate.** If an independent physical specification establishes that the complete native coherent first-order tangent space is **exactly** the span of the four named ports, if their real control-to-Hamiltonian coordinate chart is calibrated, and if the requested preparations, readouts, and pulse placement are valid, then the full-rank response above identifies coefficients throughout that stipulated space. The completeness assumption is logically independent of the response-rank theorem; it is the **missing physical assertion**, not an output of the computation.

## 4. H123 stop rule and P11 / P6 handoff

The current mathematically exact result is a bounded, four-readout *identification protocol* for the four declared H37 control directions. It does **not** derive AX-ORIGIN from bare P3/P4 Closure–Residue dynamics and does **not** prove unique hardware-native primitives or a CR-exclusive signature. **Do not add another arbitrary J5 sector.** With no independently sourced hardware inventory, do not promote any exact finite rank result to P6 physical PASS or to P11 Generative Completeness. The next productive step is a finite, falsifiable evidence ledger for apparatus provenance, or a different intrinsically motivated P11 origin axiom that really restricts the model class.

**Status:** Exact finite algebra and analytic perturbation proof; reproducible SymPy audit. **OPEN:** independent source provenance, physical phase-resolved X-readout implementation, matched two-stage CPTP, comparison against best standard GKSL, P9 GR / ADM / HDA, and P11 Generative Completeness. No Lean mechanization or specialist human peer review of this note.