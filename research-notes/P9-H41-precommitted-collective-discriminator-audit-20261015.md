# H41 — Independent static-collective-sector selection versus the best same-calibration standard GKSL comparator

**2026-10-15 | P3–P11 Mathematical Bridge, stacked on H40 Draft PR #59.**

**Scope and novelty boundary:** This is an **independent exact finite audit and explicit same-norm comparator** of the *already published/frozen P6 v9.1 conditional collective-mode strict comparator candidate*, not a new unconditional CR-only experimental discovery. The P6 v9.1 manuscript explicitly distinguishes Dataset A vs Dataset B, the original two-real-control path benchmark, the abstract/physical First-Residue Accessibility hypotheses, and the requirement that a CR response constraint exclude an observable region the **best same-calibration standard microscopic quantum comparator** still allows. The conditional collective-mode theorem is therefore not newly claimed by H41. No Lean kernel proof/human external referee/actual hardware data or Einstein dynamics.

## 1. Separate independent sector assumptions and standard calibrated data

On the 3-vertex path 0–1–2 take static collective operator
\[
T=E_{01}+E_{21},\qquad
J_{\rm col}=\operatorname{span}_{\mathbb C}\{T,T^\dagger\}.
\]
Its supported edges are both 01 and 12; it is connected and radius-one local. The real-linear first-residue image
\[
\Xi(J)=Q_D(J-J^\dagger)
\]
obeys
\[
\dim_{\mathbb R}\Xi(J_{\rm col})=2,\quad
\Xi(J_{\rm col})\cap\mathfrak{so}(3)
=\mathbb R(A+B),
\]
where \(A=E_{01}-E_{10}\), \(B=E_{21}-E_{12}\). In comparison
\[
J_{\rm free}=\operatorname{span}_{\mathbb C}\{E_{01},E_{21}\},
\qquad
\dim_{\mathbb R}\Xi(J_{\rm free})=4.
\]
Importantly, **both static sectors have the same exact connected support graph**.

The proposed **conditional CR model** independently freezes \(J_{\rm col}\) in **Dataset A, before seeing the target Hessian**; its additional, unproved-in-P3 **star-compatible oriented provenance** and P6 declared-manifold First-Residue Accessibility require each physical real exchange tangent \(K_X=a_XA+b_XB\) to satisfy \(a_X=b_X\).

The **matched Dataset-A standard GKSL comparator** is not permitted to use the target Hessian, and knows the SAME support graph and calibrated **aggregate squared tangent norm** \(a_X^2+b_X^2\), but does not know the **relative physical amplitude ratio**. It also receives the independently fixed static \(J_{\rm col}\) as an input datum, but standard dynamics does not itself postulate that the *static* CR vector subspace equals the *physical* dynamical coherent tangent subspace. **If** further independent standard microscopic calibration does fix that relation, it must be included in the standard comparator, and the claimed set separation collapses.

This is a test of a *supplementary accessibility/provenance hypothesis*, not an incompatibility of the underlying differential equation with QM; both models evolve by ordinary GKSL.

## 2. Exact P6 population-Hessian identity for coherent exchange

For a diagonal population preparation \(d=E_{11}\) (middle site), a physical real exchange intervention
\[
K(x)=a(x)A+b(x)B,\qquad
U(x)=e^{K(x)},
\]
gives the mixed second population Hessian
\[
D^2\Sigma_d(0)[X,Y]
=2a_X a_Y(E_{00}-E_{11})
+2b_X b_Y(E_{22}-E_{11}).
\]
Let \(\ell_-(h)=\operatorname{Tr}[(E_{00}-E_{22})h]\). Then
\[
\boxed{
\ell_-\bigl(D^2\Sigma_d(0)[X,Y]\bigr)
=2(a_Xa_Y-b_Xb_Y).
}
\]
Under the **ex-ante CR collective/accessibility/provenance** assumption, \(a_X=b_X\) for every declared tangent and therefore
\[
\boxed{B_{\rm col;X,Y}^{CR}=0,\quad\ell_-D^2\Sigma_d(0)[X,Y]=0.}
\]
This is precisely the conditional collective-mode candidate theorem already present in frozen P6 v9.1, independently recomputed here. It is a population quadratic null, not a prediction that a new non-GKSL evolution law exists.

## 3. A strict same-graph, same-*exact*-aggregate-norm comparator (PASS under Dataset-A information condition)

Use rational tangent values
\[
(a,b)_{\rm locked}=(3/5,3/5),\qquad
(a,b)_{\rm standard}=(3/25,21/25).
\]
Both have **nonzero amplitudes on BOTH edges**, the same supported 3-site path, and exactly equal independently calibratable squared aggregate tangent norm:
\[
a^2+b^2=\frac{18}{25}.
\]
But the population curvature readout for a single tangent direction \(X\) differs:
\[
\boxed{
\ell_-D^2\Sigma_d(0)[X,X]
=
\begin{cases}
0 &\text{locked CR branch }a=b=3/5,\\
-864/625 &\text{unlocked ordinary GKSL comparator }(a,b)=(3/25,21/25).
\end{cases}
}
\]
The standard model is a genuine finite CPTP unitary control channel \(U(x)=\exp[x(aA+bB)]\), optionally followed by *the same calibrated* site-dephasing, which preserves final populations. The standard comparator differs **only** by an edge-amplitude split not resolved in Dataset A; it is not a different graph, added chord, altered total coupling or nonlinear/decohering channel trick.

**Logical verdict:** a **strict prediction-set separation** exists *under the stated condition that Dataset A independently fixes the collective static CR sector but does not already determine the physical left/right tangent ratio*. This reproduces and strengthens the frozen P6 conditional comparator with an explicit same-**equality**, not merely same upper-bound, aggregate norm witness. The result is not a new theory-versus-QM dynamical separation: conventional GKSL with an explicitly locked real exchange also predicts zero. It is the **hypothesis that the independently measured static Jcol selects the physical dynamical tangent**, not the quantum channel, which is under test.

If independent hardware calibration also fixes the locked ratio \(a=b\) for the standard comparator, then
\[
\boxed{B_{\rm col}^{std}=B_{\rm col}^{CR}=0;}
\]
the separation **disappears**. If the device actually has independently certified \(a\ne b\) while the fixed Jcol/CR provenance hypotheses remain asserted, that **falsifies the declared CR selection/accessibility premise** for that device, not standard QM. Fitting or reselecting Jcol after seeing such a result is prohibited.

## 4. No automatic CR-specific prediction from the H40 original P3 residue readout

Using the **same fixed real-exchange tangent** \(K=aA+bB\), uniform independently calibrated gamma site dephasing and a diagonal prepared state \(d=E_{11}\), the **actual original P3 depth-three leading signed witness** depends on a diagonal Stark energy alpha that is *not fixed by the static Xi(Jcol)* or first-order population tangent:
\[
A_h=Q_D L_\alpha(d),\quad
B_h=Q_D L_\alpha^2(d),
\]
\[
\boxed{
\Delta_D([A_h,B_h])
-\Delta_D([A_h,B_h])_{\alpha=0}
=2i\operatorname{diag}(L_w\alpha).
}
\]
For collective locked \(a=b=3/5\), gamma arbitrary ≥0 and the two external settings
\(\alpha=(0,0,0)\) and \(\alpha=(1/7,0,0)\),
\[
\boxed{
R_{3,\rm lead}(0)=0,\qquad
R_{3,\rm lead}(\alpha)=\frac{18i}{175}(E_{00}-E_{11}).
}
\]
Both have the same ex-ante \(J_{\rm col}\), same initial and dynamical real-exchange first hidden tangent, same dephasing, same **P6 exchange-intervention population Hessian null**, yet different P3 signed leading residue coefficients due to independently unspecified phase/Stark data. This is P9.38's independently audited diagonal-gauge Laplacian identity. It is **not** a No-Go against a model that includes independently calibrated Stark energies in its Dataset A; adding calibrated alpha resolves this ambiguity in BOTH CR and ordinary standard GKSL.

Hence H40's exact nonzero original P3 signed residue, two-step evolution and H39/H40 finite-time tomography **do not by themselves constitute a CR-specific observable**: they were *constructed within standard GKSL* with an explicit Stark phase. H41 refuses to retrofit a CR discrimination narrative to that success.

## 5. Distinguishing a falsifiable accessibility hypothesis from a framework-level signal

A correct experimental comparison must keep four stages separate:

**Dataset A / preregistration:** independently determine \(J_{\rm col}\) and star-compatible oriented provenance **without target Hessian data**; register actual declared and full physically available coherent tangent sets; independently calibrate known physical exchange amplitudes, dephasing gamma and Stark/phase shifts alpha. A standard comparator must receive **the same input information**, not fewer independently calibrated facts.

**Dataset B / held-out response:** estimate \(\ell_-D^2\Sigma[X,Y]\) on new data with finite-difference, systematic and statistical uncertainty; preserve sign conventions and populations.

**Selection test:** if the independently registered CR null is violated beyond the prespecified uncertainty, the **conditional P6 accessibility/provenance hypothesis** fails on that device. A positive result is consistency, not an experimental proof of the framework.

**Framework-discrimination test:** require a measurable region \(\mathcal O_{std}(\mathrm{Dataset\ A})\setminus\mathcal O_{CR}(\mathrm{Dataset\ A})\) remaining genuinely open after **all independently calibrated standard constraints** are imposed. The rational same-norm pair constructs such a region when relative tangent alignment is unknown to the standard comparator. If a calibrated standard microscopic model already entails alignment, there is no distinction.

The P6 manuscript's **conditional collective-mode theorem** is the correct strongest existing candidate under these requirements. The H40 operational residue readout does not strengthen this discriminating constraint without a separate, truly **independently-derived** phase-sensitive CR prediction (and provenance into physical controls).

## 6. Current boundary and next bridge objective

**PASS finite**: Xi sector ranks2/4 on identical path support; source P6 collective locked null; exact-norm-matched standard nonzero Hessian witness; collapse of gap when the same physical tangent alignment is calibrated for standard QM; P9.38 original P3 cubic residue dependence on Stark alpha outside static Xi/Jcol data.

**CONDITIONAL PASS**: strict CR-vs-standard Dataset-A prediction-set separation, conditional on independently fixed static collective sector, oriented provenance/Accessibility, and standard relative-angle calibration uncertainty. This is not established from original P3/P4 definitions and is **not** an unconditional new physical prediction.

**FAIL as claimed implication**: presence of a nonzero H40 original P3 signed residue ⇒ intrinsically CR-only operational observation; first-residue static sector plus two-real-control graph ⇒ unique signed cubic residue without independent Stark calibration.

**OPEN:** derivation/physical determination of locked static \(J_{\rm col}\) and oriented microphysical provenance directly from an independent original P3/P4 update, reproducible hardware realization, complete real physical-control manifold, actual cross-validated Dataset A/B protocol, and any novel gravitational ADM/HDA/Einstein constraints.

**H42 candidate:** the next honest research gate is to **derive or refute** the preregistered static collective sector from a specified original P3/P4 microscopic CPTP generator **without imposing the locked control vector by hand**, and show that the induced physical control restriction is independent of all standard calibration inputs. If that cannot be derived, retain P6's result explicitly as a conditional accessibility theorem, not as a completed CR-specific discriminator.

## Files, exact reproducibility and review

`P3/P9H41PrecommittedCollectiveComparatorExactCheck.py` uses H24's Fraction Gaussian rationals and H32's exact rank; checks Hessian tensor algebra for three rational tangent pairs, static Jcol/Xi image rank2 vs Jfree rank4, exact same graph/nonzero two-edge/same aggregate norm and distinct response; plus alpha-independent P6 Hessian versus exact gamma-independent original P3 cubic residue variation. Dedicated GitHub Actions CI. Main branch and frozen P3/P6/P9 files untouched; no Lean/new human peer review/experimental data asserted.