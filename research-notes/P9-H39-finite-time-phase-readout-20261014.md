# H39 — Finite-positive-time P6 exchange readout with an independently calibrated diagonal phase gate

**2026-10-14 | P3–P11 Mathematical Bridge.** H39 is stacked on Draft H38 PR #57. Mathematical result is a standard positive-time GKSL control and tomography theorem. It is **not** a claim that frozen P6 has an independently addressable diagonal Stark gate, source-derived static microscopic \(J_N\), or a CR-exclusive discriminator. Main and frozen manuscripts unchanged; no new Lean kernel formalization or human expert review.

## 1. Exactly the P6-compatible physical baseline

Frozen P6 v9.1 concretely declares two **real** exchange amplitudes \(x_L,x_R\) on the three-site path. For this H39 protocol, switch the right exchange off and interrogate the 01 edge only, with a real anti-Hermitian exchange generator
\[
A_{01}=E_{01}-E_{10},\qquad
\mathcal L_{\pm a}(\rho)=[\pm a A_{01},\rho]+\gamma(\Delta_D\rho-\rho).
\]
The two signs are two separately applied **positive-duration CPTP GKSL semigroups**, not a dissipative inverse. Assume that the signed exchange can be selected, that its magnitude is independently calibrated, and that during the two sign settings the same background dephasing \(\gamma\ge0\) and preparation are used.

For any (not necessarily diagonal) independently prepared density matrix, define the initial diagonal population contrast \(z_0=\rho_{00}-\rho_{11}\) and one coherence quadrature \(x_0=\Re\rho_{01}\). These obey exactly the **closed real Bloch system**
\[
\dot z=4a x,\qquad \dot x=-a z-\gamma x,
\quad
\frac d{dt}\begin{pmatrix}z\\x\end{pmatrix}
=
\begin{pmatrix}0&4a\\-a&-\gamma\end{pmatrix}
\begin{pmatrix}z\\x\end{pmatrix}.
\]
The three-site spectator population never enters when the other edge is off. Solving
\(z''+\gamma z'+4a^2z=0\) yields
\[
z_{+a}(s)=f_{a,\gamma}(s)z_0+4a g_{a,\gamma}(s)x_0,\quad
z_{-a}(s)=f_{a,\gamma}(s)z_0-4a g_{a,\gamma}(s)x_0.
\]
The even part \(f\) cancels in the physical **positive-time comparison**:
\[
\boxed{
C_X(s):=z_{+a}(s)-z_{-a}(s)
=D_{a,\gamma}(s)\Re\rho_{01},\quad
D_{a,\gamma}(s)=8a\,g_{a,\gamma}(s).
}
\]
For \(\omega^2=4a^2-\gamma^2/4\),
\[
g_{a,\gamma}(s)=
\begin{cases}
e^{-\gamma s/2}\sin(\omega s)/\omega,&\omega^2>0,\\
s e^{-\gamma s/2},&\omega^2=0,\\
e^{-\gamma s/2}\sinh(\kappa s)/\kappa,&\omega^2=-\kappa^2<0.
\end{cases}
\]
Thus the contrast is nonzero for every s>0 in the critically/over-damped regimes, and for \(0<s<\pi/\omega\) in the underdamped regime. **Blind times** at \(s=n\pi/\omega\) must be avoided underdamping. This is a finite-time result, not a differential slope or an assumption of inverse Lindbladian evolution.

## 2. Additional, separately calibrated physical phase/Stark resource

Add an **external** diagonal phase gate \(V_\phi=\mathrm{diag}(e^{-i\phi},1,1)\), \(\phi\) separately calibrated, and a calibrated offdiagonal coherence attenuation factor \(q\in(0,1]\) during the phase application. The combined CPTP map acts on the edge coherence as
\[
(\mathcal P_{\phi,q}\rho)_{01}
=q e^{-i\phi}\rho_{01},
\quad\text{so}\quad
\Re(\mathcal P_{\phi,q}\rho)_{01}
=q(x_0\cos\phi+y_0\sin\phi),
\quad y_0=\Im\rho_{01}.
\]
Apply the *same* positive-duration \(\pm a\) interrogation after the gate. Then
\[
\boxed{
C_\phi(s)=D_{a,\gamma}(s)\,q
\bigl(x_0\cos\phi+y_0\sin\phi\bigr).
}
\]
For the nominal \(\phi=\pi/2\) and \(Dq\ne0\):
\[
\boxed{
x_0=\frac{C_X(s)}{D_{a,\gamma}(s)},
\qquad
y_0=\frac{C_{\pi/2}(s)}{D_{a,\gamma}(s)q}.
}
\]
More generally, for calibrated \(\sin\phi\ne0\),
\[
y_0=\frac{C_\phi/(Dq)-x_0\cos\phi}{\sin\phi}.
\]
Thus the missing quadrature is available **conditionally** in a real P6 exchange/population architecture augmented with the one specified physical phase capability. By H38's all-circuit symmetry No-Go, no combination of the original two real-exchange controls and pure site dephasing alone can supply that phase capability.

A physical positive-duration realization of this *extra* map can be described by \(H_{\rm Stark}=\alpha E_{00}\), gate duration \(\tau>0\), coherent \(\phi=\alpha\tau\), and simultaneously calibrated dephasing \(q=e^{-\gamma_\phi\tau}\) (when \(\gamma_\phi\ge0\)). Since the diagonal Hamiltonian and pinching generator commute, this phase+attenuation formula is **exactly** a CPTP semigroup, with no inverse-time step. Choosing arbitrary q and φ requires matching \(\alpha,\gamma_\phi,\tau\) or supplying an independently calibrated phase/dephasing module. In particular, if \(\gamma_\phi=0\) and no other attenuation, q=1.

**Critical physics caveat:** P6's originally declared real 2-control manifold includes **neither** Stark amplitude \(\alpha\) nor its physical calibration. The mathematical existence of a Hamiltonian \(H_{\rm Stark}\) does not mean the hardware or the inherited P6 \(J_N\) permits it. Coherent reference states and phase-locked repeated preparations also require independent access/verification.

## 3. Measurable calibration and conditioning

A physically independently certified real-edge reference preparation with \(\Re\rho_{01}=1/2\), for example \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\), has \(C_X=D/2\) at the same pulse length and dephasing. Hence one may **measure** \(D=2C_X^{\rm cal}\) in the finite-time protocol, rather than infer it solely from assumed ideal values of a, gamma and s. Such a certified reference preparation is a **required additional calibration resource**, not guaranteed from P6's population-only target experiment. Its feasibility with allowed signed exchange and finite preparation dephasing must be tested experimentally.

Let the independently calibrated transfer and attenuation be \(\widehat D,\widehat q>0\) with \(|D-\widehat D|\le\delta_D\), \(|q-\widehat q|\le\delta_q\). Let the two measured population-contrast errors be bounded by \(\eta_X,\eta_Y\); assume \(\widehat D>\delta_D\). For physical density matrices \(|\rho_{01}|\le1/2\), and a perfectly implemented \(\phi=\pi/2\):
\[
\boxed{
|\widehat x-x_0|
\le\frac{\eta_X+\delta_D/2}{|\widehat D|},
}
\]
\[
\boxed{
|\widehat y-y_0|
\le\frac{\eta_Y+\delta_D/2}{|\widehat D|\,\widehat q}
+\frac{\delta_q}{2\widehat q}
}
\]
(the second bound is conservative, taking physical q≤1).
If \(\phi=\pi/2+\delta\phi\), the additional, separately calibrated mixing error obeys
\[
\left|x_0\cos\phi+y_0\sin\phi-y_0\right|
\le\tfrac12|\delta\phi|+\tfrac14(\delta\phi)^2.
\]
This last bound should be **added** to the RHS for y, without dividing it by the transfer if it is a relative phase mixing bias. All calibrations must apply to the same coherent pulses/dephasing and timing as the actual readout. When control-dependent dissipators or crosstalk change between sign settings, the cancellation is no longer automatic.

## 4. Exact rational-gate computation and positive-time certificate

The standalone H39 checker uses the H38 original real P6 exchange matrices and H24's rational-Gaussian arithmetic. At three decoherence regimes (γ=0,1/2,4), it independently computes through Taylor order 18:
- the full **three-level GKSL** positive-time semigroup population-contrast coefficients for states with purely real, purely imaginary and mixed coherence;
- the independent closed Bloch (z,x) model's transfer coefficients;
- exact equality of all coefficients \(C_X=D x_0\) and \(C_\phi=Dq(x_0\cos\phi+y_0\sin\phi)\) at every order, for **ideal** phase \(\phi=\pi/2\) and an additional rational unit phase \(\cos\phi=3/5,\sin\phi=4/5\);
- exact finite-time positive reference-coherence contrast certification for separately prepared \(|+\rangle\), \(|-\rangle\) states;
- deterministic transfer, attenuation, phase and population-contrast uncertainty bounds.

For the example a=2/3, γ=1/2, interrogation duration s=1/4, \(D=2[e^{sM}]_{01}\), M=[[0,4a],[-a,-γ]]. From the full rational degree-18 Taylor polynomial \(D_{18}\) and \(h=s\max(4|a|,|a|+\gamma)=2/3<1\), obtain a **certified rational interval**:
\[
|D-D_{18}|\le
\frac{2h^{19}}{19!(1-h)}.
\]
Independently, underdamped \(0<\omega s\le1\), elementary \(e^{-x}\ge1-x\) and \(\sin x/x\ge1-x^2/6\) imply the **strict positive rational lower bound**
\[
D\ge 8as(1-\gamma s/2)(1-\omega^2s^2/6)>0.
\]
This bounds a **nonzero actual finite-time CPTP population contrast**, not just a nonzero derivative or a truncated numerical Taylor polynomial. All evaluated matrix jets and certificate intervals are exact fractions without floating tolerance.

## 5. Relationship to the original P3 residue and next gate

Under only the original two-real P6 exchange controls with pure site dephasing, **the entire original P3 quadratic residue filtration is zero from diagonal seeds**, as H38 proved for that restricted benchmark. Hence H39's non-diagonal **tomography** of an arbitrary supplied state does **not** by itself generate a nonzero genuine P3 residue in the original restricted channel: it is a conditional **readout capability**, not provenance of a particular hidden jet.

Allowing a real physical diagonal Stark \(\alpha\) breaks the real-symmetric invariance and can produce a genuine depth-three signed P3 residue with coefficient \(+2i\,\mathrm{diag}(L_w\alpha)\) (P9.38 and H38), but then this is a **different, externally extended** physical control model. If this is adopted, one must ensure that the same actual micro-to-operational one/two-step CPTP map, independent phase calibration, and observer measurement permissions are explicitly declared before claiming P3/P6 provenance.

**H39 result:** CONDITIONAL PASS for implementability *within an explicitly augmented standard-GKSL control model*, with a mathematically complete finite-positive-time transfer and error estimate. **OPEN** for implementation inside P6's originally frozen physical exchange manifold and for any CR-exclusive residue comparator, physical Lorentzian/Levi-Civita curvature or Einstein/ADM/HDA.

**H40 proposed:** use a **single explicitly fixed augmented microscopic CPTP/GKSL model** with Stark phase and exchange, and independently freeze a local \(J_N\) and a physical readout. Check whether its original P3 hidden depth-three pair and operational two-time tomography actually intertwine under *the same* channel, and whether anything stronger than the matched standard GKSL signal remains. Do not infer inherited microscopic \(J_N\) from success of the readout.

## Reproducibility

`P3/P9H39FiniteTimePhaseReadoutExactCheck.py` is executed by a dedicated GitHub Actions workflow. Main and frozen manuscripts unchanged; no claim of Lean kernel proof, human review or hardware implementation.