# H47 — Preregistered Dataset A/B calibration gate and finite-time odd-instrument strict comparator

**2026-10-15 | P3–P11 Mathematical Bridge.** Stacked on H46 Draft PR #65. H47 is an independently recomputed finite-time/finite-shot **conditional** realization of the *existing frozen P6 v9.1 collective-mode strict comparator hypothesis*, now with H46's explicitly constructed **CPTP instrument**. It is **not** a new framework-exclusive non-GKSL law or completed physical experimental test. The independently postulated microscopic static collective sector and oriented First-Residue Accessibility are **NOT derived** from original P3 full-diagonal CPTP filtration (H42 No-Go). Frozen P3/P6 manuscripts/main unchanged; no new Lean kernel proof, human expert review or empirical measurements.

## 1. Dataset A: explicitly freeze what IS and IS NOT calibrated

**Preregister before observing the target signal**: the three-site connected path 0–1–2; diagonal center preparation \(d=E_{11}\); an externally given one-real-parameter physical coherent control \(K=aA+bB\), \(A=E_{01}-E_{10}\), \(B=E_{21}-E_{12}\); independently calibrated overall strength
\[
\boxed{r^2=a^2+b^2=18/25};
\]
exact prescribed pulse duration \(x=1/2\) within independently bounded timing drift; shared **post-pulse** site dephasing \(\mathcal D_{\lambda}(\rho)=\lambda\rho+(1-\lambda)\Delta_D\rho\) with \(\lambda=3/4\); fixed diagonal Stark setting \(\alpha=0\) (or independently calibrated common Stark compensation); and an independently effect-calibrated, unmodified H46 **12-outcome CP instrument** whose signed flag \(Z\in\{-1,0,1\}\) has
\[
\boxed{\mathbb E_\rho Z=\frac{\rho_{00}-\rho_{22}}{2}}
\]
for every input state. The quantum marginal of the instrument is exactly H43's collective \(\mathcal E\), and the sample's quantum state is subsequently disturbed; use the flag **at the endpoint**, not as an inserted invasive step before the coherent preparation update.

**Dataset-A allowed training signals**: calibration/reference states for the detector and independent population center-survival traces \(p_1(x)\), pulse timing, dephasing/phase nuisance. **Dataset-A forbidden target leakage**: using the post-control signed odd flag \(Z\), separate left/right response populations, calibrated individual amplitudes \(a,b\), or target even-coherence response tomograms to choose the static \(J_{\rm col}\), orient the physical control tangent, or learn its split. When independently obtained calibration actually fixes the ratio \(a:b\), it MUST be supplied to the best standard comparator as well.

**Additional CR-specific CONDITIONAL structural premises** are preregistered independently of Dataset-B readout:
\[
\mathcal J_{\rm col}
=\operatorname{span}_{\mathbb C}\{T,T^\dagger\},\quad
T=E_{01}+E_{21};
\]
star-compatible microscopic-to-physical orientation/provenance and frozen P6's declared-control First-Residue Accessibility; hence \(a=b\) for the physical one-real-control tangent. These assumptions have not been established by original P3/P4 or by the H46 instrument: simply choosing them is not an independent experimental discovery.

## 2. Best same-Dataset-A standard quantum comparator, precisely matched

The honest comparator is the family of **standard unitary/CPTP** positive-time channels
\[
\Psi_x^{(a,b)}(\rho)
=\mathcal D_{3/4}\!\left(e^{xK(a,b)}\rho e^{-xK(a,b)}\right),
\qquad K(a,b)=aA+bB,
\]
with **identical graph, input, timing, dephasing, detector, overall norm \(r^2\)** and phase setting, but without a hypothetical micro-CR-sector-to-physical-tangent selection law. The exact finite-time center-state evolution is
\[
e^{xK(a,b)}|1\rangle
=\cos(rx)|1\rangle+
\frac{\sin(rx)}r(a|0\rangle+b|2\rangle).
\]
Consequently
\[
p_0(x)=\frac{a^2}{r^2}\sin^2(rx),\quad
p_2(x)=\frac{b^2}{r^2}\sin^2(rx),\quad
\boxed{p_1(x)=\cos^2(rx),}
\]
and the post-pulse dephasing preserves all populations. Thus **the complete center-survival calibration trace for all x is identical** for all same-\(r^2\) standard comparator tangents, and cannot determine their left/right split.

Take two rational positive tangents,
\[
(a,b)_{\rm col}=(3/5,3/5),\quad
(a,b)_{\rm std}=(3/25,21/25),\quad
a^2+b^2=18/25.
\]
Both have nonzero control on BOTH physical path edges. Their held-out H46 odd flag means are
\[
\boxed{
\mu_{\rm col}(x)=0,\qquad
\mu_{\rm std}(x)
=-\frac{12}{25}\sin^2\!\left(\sqrt{18/25}\,x\right).
}
\]
All times share the same center survival and same post-dephasing. The ordinary standard model itself ALSO contains the collective \(a=b\) member giving zero; no claim that orthodox QM forbids this zero. The strict conditional prediction-set gap arises only because the additional precommitted CR **physical tangent selection** disallows unequal amplitudes while Dataset A has not independently determined their relative ratio.

For \(x=1/2\), \(r^2x^2=9/50<1\), use the elementary rigorous sine estimate \(\sin^2 y\ge y^2(1-y^2/3)\) for \(0\le y\le1\):
\[
\boxed{
|\mu_{\rm std}(1/2)|
\ge \frac{1269}{15625}>0,\qquad
\mu_{\rm col}(1/2)=0.
}
\]
These are **finite positive-duration** CPTP interventions, not infinitesimal Hessian limits. Independently computed degree-16 exact rational Taylor jets of the full three-site coherent state confirm the exact analytical all-time formula; no Taylor truncation is substituted for the physical sine evolution.

## 3. Finite-shot conditional test and explicit systematic calibration bound

The H46 flag variable always obeys \(|Z|\le1\), hence its variance is at most one. Assume \(n\) independent identically prepared experimental repetitions for the held-out target, and an **independently established absolute detector flag-mean systematic error bound**
\[
|\delta_{\rm det}|\le1/500.
\]
Also suppose the physical pulse time \(x\) differs from \(1/2\) by at most \(1/100\), with no unmodelled simultaneous coherent/dephasing crosstalk. For \(r^2=18/25\), a completely rational **uniform** gap certificate over this timing window is
\[
G_{\rm min}
=\frac{12}{25}\,
\left(\frac{18}{25}\left(\frac{49}{100}\right)^2\right)
\left(1-\frac13\frac{18}{25}\left(\frac{51}{100}\right)^2\right)
=\frac{7597529919}{97656250000}
\approx0.07780.
\]
The ex-ante sign-oriented test classifies the **specified** unlocked rational standard model when the sample flag mean is less than \(-G_{\rm min}/2\), and otherwise returns the collective-null classification. Both conditional hypotheses are separated by at least \(G_{\rm min}/2\) from that fixed threshold; after independent detector bias, the statistical safety margin is \(G_{\rm min}/2-1/500>0\).

Chebyshev's inequality gives a **per-hypothesis worst-case** error probability
\[
\boxed{
P_{\rm wrong}\le
\frac1{n(G_{\rm min}/2-1/500)^2}.
}
\]
For \(n=100000\), this exact rational bound is **strictly smaller than 1/100** (approximately 0.00735). This is a theoretical sampling bound **given all declared idealized preparation and calibration conditions**, not a statement that real hardware can implement 100000 such runs accurately or that it discriminates every standard model arbitrarily close to collective alignment with fixed n. Finite-shot errors from independently estimating aggregate norm, dephasing, timing and source state, plus uncertainty in a true physical Stavk/phase resource, must be included in any actual apparatus feasibility assessment; here only the indicated timing/detector nuisance is bounded explicitly.

**Important experimental-design separation:** the H46 instrument is **calibrated on independent reference inputs** in Dataset A. Its target-control outcome distribution on post-exchange states is evaluated **only on held-out Dataset B**. The presence of the instrument in the apparatus does not license fitting a:b from the same target flags before testing the P6 null.

## 4. Why the strict comparator vanishes under stronger Dataset-A calibration

Independent measurement of the physical ratio a:b, or an equivalent coherent control response, can collapse the conditional CR-vs-standard prediction-set difference. Algebraically,
\[
\boxed{
2r^2-(a+b)^2=(a-b)^2.
}
\]
Knowing \(r^2\) **and** independently certifying \((a+b)^2=2r^2\) forces \(a=b\), so the **best calibrated standard quantum model** predicts \(\mu_{\rm std}=0\) as well. On the H47 two models,
\[
(a+b)_{\rm col}^2=2r^2,\quad
(a+b)_{\rm unlocked}^2<2r^2.
\]
For example, a phase-referenced even-coherence response from a center-launched exchange pulse is proportional to
\[
\frac{a+b}{r}\cos(rx)\sin(rx)
\]
and would resolve the relative split when the transfer factor is nonzero. If such data are independently part of Dataset A, excluding them from standard calibration is unfair. Similarly, calibrating left/right response populations in Dataset A fixes q and invalidates a claimed held-out response prediction. The source of the conditional gap is the **additional accessibility/provenance selection hypothesis under incomplete relative-split calibration**, not a departure from standard CPTP or GKSL evolution.

An independently measured **static \(J_{\rm col}\)** belongs in the standard comparator's facts as well. What is not standardly implied is an operational map forcing its image to equal the physical real control tangent unless that map is also physically/independently given. H42's same-uncontrolled-CPTP control extension counterexample rules out inferring the map from unconditional microscopic symmetry/P3 residue alone.

## 5. Review status and precise next proof gate

**PASS algebraic/pre-registered thought experiment:** exact same-control-norm and full-center-survival standard comparator; positive-time odd-flag response gap; exact rational degree-16 state-jet identity; post-pulse dephasing no-effect on population/flag mean; explicit timing-systematic and n-shot Chebyshev bound; collapse of gap under ratio/even-coherence calibration.

**CONDITIONAL PASS:** strict prediction-set separation under the **ex-ante** P6 v9.1 collective star-compatible accessibility hypothesis and the explicitly restricted Dataset-A information. It is a falsifiable *hypothesis about physical control selection*, not a CR-only modification of standard quantum mechanics. If an independent real-device dataset violating the locked null were obtained under proven assumptions, the *conditional model* would be falsified rather than standard QM.

**OPEN:** independently P3/P4-inherited actual microscopic \(J_N\), a physically sourced star-/instrument-compatible tangent map, experiment delivering the required B response and calibration/nuisance guarantees without dataset leakage, true full eligible P6 control manifold, any stronger framework discriminator, Lorentzian soldering and GR/Einstein equations.

**H48 suggestion:** make the precommitted H47 data partition and the independent P6 physical tangent-selection claims **operationally checkable** from an independently source-derived finite CPTP physical control model or actual calibrated device design. Test whether complete independent calibration of all physical control knobs extinguishes every remaining conditional prediction-set gap. If so, publish the sharp P6 *conditional control selection theorem* rather than a "CR versus quantum mechanics" violation claim. An alternative mathematical gate is to formulate a necessary/sufficient **instrumental provenance condition** under which the P3/P4 static sector controls exactly the admissible target tangent directions, and independently falsify or prove it.

## Reproduction

`P3/P9H47PreregisteredInstrumentComparatorExactCheck.py` checks full exact Gaussian-rational state/coherent Taylor jets through order16, explicit H46 per-Kraus flag mean, same Dataset-A calibration values and post-pulse dephasing, rigorous rational positive-time sine lower bounds, 1/100 timing drift, 1/500 instrument bias, 100000-copy worst-case Chebyshev probability bound, and the coherent sum-calibration collapse. Dedicated Actions CI in stacked Draft PR; H46's unrelated earlier Lean toolchain-download HTTP500 is an external CI setup failure, not an algebraic failure, and was explicitly retried without altering mathematical statements. No new Lean or external human reviewer validation is asserted.