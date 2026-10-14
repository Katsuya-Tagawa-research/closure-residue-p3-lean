# H46 — CPTP odd-seed information readout, instrument disturbance, and signed P3 residue error bounds

**2026-10-15 | P3–P11 Mathematical Bridge.** H46 is stacked on H45 Draft PR #64. All results use the EXACT fixed H42 reflection-equivariant 3-site unitary CPTP model \(\Phi=\operatorname{Ad}_U\), H43's verified unital CPTP collective extractor \(\mathcal E=\mathcal S_{3/5}\circ\mathcal T\), and H45's true original P3 depth-1×depth-2 signed quadratic-residue formula. This is ordinary standard quantum instrument theory, not a framework-exclusive CR signal, a frozen P6 physically sourced instrument, or gravitational dynamics. No frozen manuscripts/main changed, no Lean kernel or human referee proof.

## 1. Measurement is not the same as possessing an exact scalar in one shot

H45 showed for a **known Hermitian diagonal seed** \(d=\operatorname{diag}(a,b,c)\)
\[
u=(a+c)/2,\qquad e=b-u,\qquad q=(a-c)/2
\]
that the actual original P3 signed depth-3 witness is
\[
\boxed{R(d)=(e^2+3q^2)R_{ee}+4eqR_{oe},}
\]
with \(R_{ee}=\frac{i}{81}\operatorname{diag}(-8,16,-8)\) and \(R_{oe}=\frac{i}{81}\operatorname{diag}(24,0,-24)\). H44's CPTP parity-even carrier determines u,e, but deliberately erases q. The question here is whether a genuine **CPTP quantum instrument** can report q without falsely claiming that measurement outcomes on one copy equal exact ensemble expectation values or that inserted observations leave the microscopic trajectory intact.

**Answer H46:** There is (a) a CPTP instrument with **exactly the same nonselective H43 collective quantum output** \(\mathcal E\), while its labelled outcomes statistically determine q; and (b) a different two-outcome projective instrument whose **nonselective action leaves every original diagonal seed unchanged**, permitting later evolution by the original \(\Phi\). These are *different physical protocols*; neither establishes generic non-disturbing measurement on unknown coherent states or that frozen P6 authorizes the added instrument.

## 2. Fully explicit 12-outcome instrument whose quantum marginal is EXACTLY \(\mathcal E\)

Recall \(\mathcal T(\rho)=(\rho+P\rho P)/2\), where P swaps sites 0 and 2, and the H43 CP Schur channel \(\mathcal S_{s}\) has correlation matrix
\[
M_s=\begin{pmatrix}1&s&0\\s&1&s\\0&s&1\end{pmatrix},\qquad s=3/5.
\]
Give an **all-rational** Gram factorization \(M_s=(\langle v_i,v_j\rangle)_{i,j=0,1,2}\):
\[
\begin{aligned}
v_0&=(1,0,0,0,0,0),\\
v_1&=(3/5,4/5,0,0,0,0),\\
v_2&=(0,3/4,1/4,1/4,1/4,1/2).
\end{aligned}
\]
Each \(v_i\) is a unit vector, and \(\langle v_0,v_1\rangle=\langle v_1,v_2\rangle=3/5\), \(\langle v_0,v_2\rangle=0\). For k=0,...,5, set \(D_k=\operatorname{diag}(v_{0k},v_{1k},v_{2k})\). Define outcome-labelled **completely positive, trace-nonincreasing** maps
\[
\boxed{
\mathcal I_{k,t}(\rho)
=\frac12D_k P^t\rho P^tD_k^\dagger,\qquad
k=0,\ldots,5,\;t\in\{0,1\}.
}
\]
Their twelve-Kraus nonselective sum is **exactly**, as a map on all nine matrix units and therefore on all of \(M_3(\mathbb C)\),
\[
\boxed{\sum_{k,t}\mathcal I_{k,t}(\rho)
=\mathcal S_{3/5}(\mathcal T(\rho))=\mathcal E(\rho).}
\]
The classical instrument flag Z takes values +1 on outcome (k=0,t=0), -1 on (k=0,t=1), and zero otherwise. The effect difference for these two outcomes is
\[
\mathcal I_{0,0}^*(I)-\mathcal I_{0,1}^*(I)
=\frac12(E_{00}-E_{22}).
\]
Thus, for **every Hermitian physical state** \(\rho\) (not just diagonal),
\[
\boxed{
\mathbb E_\rho Z=\tfrac12(\rho_{00}-\rho_{22})=q(\rho).
}
\]
This is a concrete example where the **quantum marginal** \(\mathcal E(\rho)\) loses the signed odd information, but an explicitly retained **classical environment/outcome flag** reports it statistically. There is no violation of no-broadcasting: the quantum output is compressed/disturbed and a single flag does not reveal an unknown expectation value exactly.

For n independent preparations and independent identically implemented instruments, the unbiased sample average \(\widehat q=n^{-1}\sum Z_i\) has \(\mathrm{Var}(\widehat q)=\mathrm{Var}(Z)/n\le1/n\), so **Chebyshev's inequality** gives
\[
\boxed{\Pr(|\widehat q-q|\ge\varepsilon)\le\frac1{n\varepsilon^2}.}
\]
This bound can be vacuous at small n/eps; it is an explicit, conservative probability guarantee, not hardware demonstration. The quantum emitter after this instrument has **nonselective state \(\mathcal E(\rho)\), not original \(\rho\)**. In particular for \(d=E_{00}\), \(\mathcal E(d)=\frac12(E_{00}+E_{22})\ne d\); continuing the original microscopic \(\Phi\) from the instrument output gives \(\Phi\mathcal E(d)\ne\Phi(d)\). The flag does not magically restore microphysical two-step evolution of the quantum output.

## 3. A physically simpler 2-outcome diagonal-input QND protocol

For the actual P3 initial class, the starting seed is **known to lie in the diagonal algebra**. Define
\[
P_0=E_{00},\quad Q_0=I-P_0,\qquad
\mathcal J_{\rm yes}(\rho)=P_0\rho P_0,\quad
\mathcal J_{\rm no}(\rho)=Q_0\rho Q_0.
\]
This is a valid two-outcome projective CPTP instrument. For **every Hermitian diagonal seed d**,
\[
\boxed{(\mathcal J_{\rm yes}+\mathcal J_{\rm no})(d)=d,}
\]
so after *discarding the outcome conditioning* and evolving for any number of steps, the original CPTP channel remains EXACT:
\[
\Phi^n((\mathcal J_{\rm yes}+\mathcal J_{\rm no})(d))
=\Phi^n(d)\quad(\text{all }n\ge0).
\]
The yes probability is \(a=d_{00}\). If the even preparation information \(u=(a+c)/2\) is independently determined from the H44/H43 even preparation, then
\[
\boxed{q=a-u=\Pr(\mathrm{yes})-u.}
\]
Only a **single binary population question** is added; one need not use full three-outcome site tomography. But for an unknown coherent input such as \(\frac12(|0\rangle+|1\rangle)(\langle0|+\langle1|)\), the nonselective instrument erases the 01 coherence, so it is **not generally nondisturbing**. Nor does conditioning on a particular yes/no outcome leave an unchanged state: its average does, **only on diagonal seeds**. The state after a later collective extractor still has to be interpreted as H43's quantum compressed observer output, not used to replace \(\Phi\) between original steps.

For n independent yes/no experiments and a separately known u, the Bernoulli estimate has variance at most \(1/(4n)\), hence
\[
\boxed{
\Pr(|\widehat q-q|\ge\varepsilon)\le\frac1{4n\varepsilon^2}.
}
\]
If u itself is estimated, its uncertainty must be added. The projective two-outcome operation is an **extra physically permitted detector**, not one known to be contained in frozen P6's declared two-real-exchange physical control family; actual bandwidth, state preparation and detector permissions remain OPEN.

**Generic information-disturbance boundary:** an instrument on the full noncommutative matrix algebra whose **nonselective channel is exactly identity on every input state** cannot have state-dependent outcome probabilities: the identity channel has Choi rank one, forcing all its Kraus operators to be scalar multiples of the identity, hence outcome effects are scalar. The restricted diagonal-seed Lüders protocol avoids this generic No-Go **because it is only nondisturbing on its commutative input sector**, not on arbitrary coherent states.

## 4. Why branch-wise quadratic residues cannot simply be averaged

For any input mixture \(d=p d_1+(1-p)d_2\), the original P3 quadratic return has interference/cross terms:
\[
R(d)=p^2R(d_1)+(1-p)^2R(d_2)
+p(1-p)\bigl[R_{1,2}(d_1,d_2)+R_{1,2}(d_2,d_1)\bigr].
\]
Therefore **in general**
\[
\boxed{
R(d)\ne pR(d_1)+(1-p)R(d_2).
}
\]
The checker gives an exact physical 3-site diagonal mixture example and verifies this inequality. Consequently the correct operational target is the signed quadratic functional of the **unconditioned density preparation** inferred from repeated data, not the average of different branch-conditioned P3 residues. Failing to respect this point would incorrectly equate a classical postselected quadratic statistic with the original P3 algebraic \(\mathcal R_3\) witness.

## 5. Exact deterministic error propagation to signed original P3 R3

In the fixed H45 model, for known e and an estimate \(|\widehat q-q|\le\varepsilon\), the same-seed witness estimator
\[
\widehat R=(e^2+3\widehat q^2)R_{ee}
+4e\widehat q R_{oe}
\]
satisfies
\[
\boxed{
\|\widehat R-R(d)\|_1
\le3\|R_{ee}\|_1(2|q|\varepsilon+\varepsilon^2)
+4|e|\|R_{oe}\|_1\varepsilon,
}
\]
where \(\|R_{ee}\|_1=32/81\), \(\|R_{oe}\|_1=48/81\). These are trace norms of diagonal anti-Hermitian matrices (sum of diagonal absolute values), not trace norms of density states. Combining with Chebyshev provides a **conditional finite-sample probabilistic accuracy guarantee** for original P3 R(d), subject to known U,e and correct independent preparations. For the ordered pair \(R_{1,2}(d,d')\) with independently estimated q,q' at error eps,eps', the exact bilinear formula gives
\[
\boxed{
\|\widehat R_{1,2}-R_{1,2}\|_1\le
3\|R_{ee}\|_1(|q|\varepsilon'+|q'|\varepsilon+\varepsilon\varepsilon')
+\|R_{oe}\|_1(3|e|\varepsilon'+|e'|\varepsilon).
}
\]
The checker verifies both bounds in exact Gaussian rationals on several valid density preparations and perturbation directions. Calibration error in U, e and the real hardware readout channel is **not** included and must be added in any laboratory protocol.

## 6. Research status and H47 gate

**PASS mathematical physical instrument existence:** H43's collective CPTP quantum marginal with an odd classical flag; alternative two-outcome diagonal-input nonselectively nondisturbing instrument; exact restoration of source \(\Phi^n(d)\) **only for the original diagonal seed class**; exact trace-norm error propagation from finite-shot estimate to actual original P3 signed witness.

**FAIL strong unconditional claim:** one measurement of a generic unknown quantum state provides its exact q without disturbance or exact residual; a quantum marginal preserving E contains q; processing the extracted quantum state with original Phi reproduces original two-step trajectory; average postselected quadratic residues equals the original mixture residue.

**OPEN:** explicit **frozen P6 physical hardware** implementation of the extra detector/environment readout and independent microphysical source of its q information; calibration of U and preparation, chosen observer history, practical shot budget, full physical controls; a CR-exclusive discrepancy with matched standard quantum prediction. Both H46 protocols are standard CPTP quantum instruments, so none alone distinguishes CR from orthodox quantum physics. Nor do they imply Einstein/gravity dynamics.

**H47 proposed:** formulate an **independent apparatus-calibration/data-split audit** for the H46 odd-information instrument and H41 P6 collective strict null. Explicitly prevent using the same outcome record to retrospectively choose J_col, physical odd-mode exclusions, or the Stark phase. Test whether the matched standard quantum model with all independently calibrated effects leaves a strict observable prediction-set gap. Alternatively, derive a resource lower bound on finite-shot q readout for a specified admissible physical detector family, rather than inferring experimentally feasible distinguishability from a positive algebraic construction.

## Reproducibility

`P3/P9H46CPTPOddInstrumentReadoutDisturbanceExactCheck.py` uses all-rational Gram vectors / diagonal Kraus operators, full 9-matrix-unit quantum-channel equality verification, physical odd-flag expectation moments, exact conditional/unconditional projective Lüders state updates, a coherent-input information-disturbance witness, nonlinear branch-averaging counterexample, and trace-norm signed original-P3 residue error bounds. New dedicated Actions CI in stacked Draft PR. No finite-sample simulation is presented as exact experimental data; Chebyshev is an analytic inequality on repeated independent preparations.