# H48 — Instrument-compatible provenance: kernel criterion, information tiers, and the missing physical control selection law

**2026-10-15 | P3–P11 Mathematical Bridge.** Stacked on H47 Draft PR #66. This is a finite exact **linear descent / CP-instrument / physical control provenance audit** for the **same** original H42 rational 3-site unitary CPTP \(\Phi=\mathrm{Ad}_U\), H43/H44 observer extraction, H46 exact twelve-outcome instrument, and H47 preregistered one-knob exchange comparison. All physical claims are **ordinary quantum CPTP**. No frozen P3/P6 manuscript/main edits, new Lean kernel proof, human peer review, hardware demonstration, GR curvature or Einstein equation.

## 1. A necessary and sufficient condition for an observer record to carry its own dynamics

Let \(V\) be a finite-dimensional complex vector space of microscopic operators, \(\Phi:V\to V\) a known linear quantum update, and \(C:V\to W\) any *linear* measurement-record map. Its range is the putative effective output space.

**Theorem H48.1 (exact linear quotient criterion).** There exists a well-defined linear effective map
\[
\Phi_{\rm eff}:\operatorname{im}C\longrightarrow\operatorname{im}C,\qquad
\boxed{C\Phi=\Phi_{\rm eff}C}
\]
if and only if
\[
\boxed{\Phi(\ker C)\subseteq\ker C.}
\]
The proof is elementary: define \(\Phi_{\rm eff}(C(X)):=C(\Phi(X))\), which is independent of the representative \(X\) iff the kernel is invariant. On a family of controlled microscopic updates \(\{\Psi_x\}\) the condition must hold for **each** \(x\). For a continuously differentiable controlled family, it also yields a necessary tangent-level condition \(L_X(\ker C)\subseteq\ker C\) when the identity-time baseline preserves the kernel.

**Crucial distinction:** this is a necessary and sufficient criterion for a **LINEAR** induced dynamics on a vector-space quotient. When it holds, it does **not** automatically prove the induced map is completely positive on an arbitrary chosen operator-algebra structure, nor that a CP state-assignment/lift or physical instrument exists. A fixed invariant \(C^*\)-subalgebra with a CP conditional expectation is a safer *additional* sufficient structure (as in H44's parity-even \(M_2\oplus\mathbb C\)). In the H48 case **even linear descent fails**, making a CP effective one-step channel impossible.

## 2. Three distinct information tiers of the very same H46 quantum instrument

The H46 instrument has twelve CP outcome maps
\[
\mathcal I_{k,t}(X)=\tfrac12D_k P^t X P^t D_k^\dagger,\qquad
k=0,\ldots,5,\ t\in\{0,1\},
\]
with independently fixed rational diagonal \(D_k\) and reflection \(P\). It is trace preserving upon outcome sum, and its nonselective quantum marginal is exactly the **H43** path-local CPTP \(\mathcal E=\mathcal S_{3/5}\mathcal T\). Define three DIFFERENT observation maps:

\[
C_{\rm cl}(X)=(\operatorname{Tr}\mathcal I_{k,t}(X))_{k,t},
\quad
C_{\rm ns}(X)=\sum_{k,t}\mathcal I_{k,t}(X)=\mathcal E(X),
\]
\[
\boxed{\mathcal C(X)=\bigoplus_{k,t}\mathcal I_{k,t}(X)}.
\]
The last map is a legitimate quantum-classical CPTP **instrument channel**, preserving **both outcome labels and conditional quantum output blocks**; merely recording the twelve classical outcome **probabilities** is NOT equivalent to coherently tomographing those blocks. All ranks below are over the complex operator vector space \(M_3(\mathbb C)\):

| Observation data actually retained | Rank |
|---|---:|
| Twelve classical probabilities \(C_{\rm cl}\) only | **3** |
| Nonselective collective quantum marginal \(C_{\rm ns}=\mathcal E\) only | **4** |
| Twelve labelled conditional quantum blocks \(\mathcal C\) | **7** |
| Current plus next labelled blocks \(X\mapsto(\mathcal C X,\mathcal C\Phi X)\) | **9** |

These are exact Gaussian-rational matrix ranks calculated on all nine matrix units. The general rank7 statement assumes the experiment has permitted separate **quantum tomography of the conditional post-instrument outputs**, in addition to recording their classical labels. Frozen P6 does not guarantee that measurement hardware.

## 3. Full instrument rank7 still does not yield autonomous time evolution

The precise full labelled instrument kernel is
\[
\boxed{\ker\mathcal C=\operatorname{span}_{\mathbb C}\{E_{02},E_{20}\}.}
\]
All twelve H46 branches annihilate both oriented 0–2 chord matrix units because no corresponding diagonal Kraus factor has support simultaneously at endpoints 0 and 2. However
\[
\boxed{\mathcal C\Phi(E_{02})\ne0,\qquad
\mathcal C\Phi(E_{20})\ne0,}
\]
and the two resulting record vectors are independent. Hence
\[
\boxed{\operatorname{rank}\begin{pmatrix}\mathcal C\\\mathcal C\Phi\end{pmatrix}=9,\qquad
\Phi(\ker\mathcal C)\not\subseteq\ker\mathcal C.}
\]
By Theorem H48.1 **no** autonomous effective linear update, a fortiori no CPTP one, can evolve the current twelve labelled quantum output blocks into the correct next twelve labelled blocks for **all** microscopic states.

**This failure holds on genuine physical density matrices.** Define two independent Hermitian chord directions
\[
X=E_{02}+E_{20},\qquad
Y=i(E_{02}-E_{20}),
\]
and for either one take \(\rho_\pm=I_3/3\pm X/6\) (respectively \(\pm Y/6\)). Each density is trace one and positive, with spectrum \(1/6,1/3,1/2\). For each pair
\[
\boxed{\mathcal C(\rho_+)=\mathcal C(\rho_-),\qquad
\mathcal C\Phi(\rho_+)\ne\mathcal C\Phi(\rho_-).}
\]
The real chord \(X\) returns to a *population* component
\[
(\Phi(X))_{11}=8/9,
\]
whereas the imaginary chord \(Y\) returns to a distinguishable *conditional coherence* in the quantum outcome \((k,t)=(0,0)\):
\[
\left(\mathcal I_{0,0}(\Phi(Y))\right)_{01}=1/5.
\]
Thus **both** missing chord quadratures matter for the **fully labelled** quantum-record prediction, not only the single real parity-even chord of H44. On generic trace-one Hermitian states, rank7 corresponds to six real observable parameters and the two missing chord quadratures bring the minimal complete linear predictive carrier to eight physical real affine parameters (full \(3\times3\) density). On the full complex operator space the minimal linear predictive dimension is nine. This dimension result is about **linear-output future prediction for all physical states**, not the minimum instrument or storage cost for a restricted diagonal preparation family.

**There is no contradiction with H44:** H44 retained only the *parity-even* operator algebra \(\mathcal A_+\cong M_2\oplus\mathbb C\); its admissible restricted state sector has a single real even chord. H48 allows **all** quantum states and tracks **conditional quantum outputs** from an apparatus whose nonselective quantum marginal is H43's collective channel.

## 4. Separate independent static-sector membership from PHYSICAL tangent provenance

Let \(W=\mathrm{span}_{\mathbb R}\{A,B\}\) with the frozen concrete P6 real exchange generators
\[
A=E_{01}-E_{10},\quad B=E_{21}-E_{12}.
\]
Predeclare H41's source candidate
\[
\mathcal J_{\rm col}
=\operatorname{span}_{\mathbb C}\{T,T^\dagger\},\quad
T=E_{01}+E_{21},\qquad
\Xi(J)=Q_D(J-J^\dagger).
\]
Its *real-skew* first-residue image intersects W in
\[
\boxed{\Xi(\mathcal J_{\rm col})\cap W
=\mathbb R(A+B).}
\]

**Theorem H48.2 (conditional source-to-control factorization test).** For a linear physical real-knob tangent map \(K:\mathcal U\to W\), a real-linear source preimage map \(S:\mathcal U\to\mathcal J_{\rm col}\) satisfying
\[
\boxed{K=\Xi\circ S}
\]
exists **if and only if** \(\operatorname{im}K\subseteq\Xi(\mathcal J_{\rm col})\cap W\). In this concrete real-exchange example that is exactly the condition \(a_X=b_X\) for each declared physical tangent. Since all spaces are finite dimensional, a linear right inverse on \(\operatorname{im}K\) proves sufficiency. This theorem is an **EXISTENCE/factorization equivalence**, not an independent derivation of S or its physical meaning. To assert real microscopic provenance, S must be fixed independently of target response, respect whichever time, *-orientation, instrument/observer, physical-control and two-step dynamics the experiment requires, and its actual image restriction must be physically validated.

**Counterexample under identical static and apparatus information.** H42/H47 already give two legitimate standard CPTP control extensions of the same uncontrolled microscopic \(\Phi\), same H46 instrument, same static \(\mathcal J_{\rm col}\) candidate (provided as an **independent datum**, not identified with the actual original P3 hidden sector), same nearest-neighbor graph, and exactly equal tangent norm:
\[
(a,b)_{\rm locked}=(3/5,3/5),\quad
(a,b)_{\rm unlocked}=(3/25,21/25),\quad
a^2+b^2=18/25.
\]
Only the first has physical tangent in \(\Xi(\mathcal J_{\rm col})\). The same uncontrolled channel, static metadata, CP detector and aggregate norm do **not** specify which physical control extension is actually present; they cannot themselves construct a source-to-physical tangent map. Ordinary quantum dynamics admits both.

## 5. The stronger quantum output can directly calibrate the tangent and eliminate the H47 separation

For a direct center-seed input \(d=E_{11}\) and a physical real exchange pulse \(U_x=e^{x(aA+bB)}\), the first derivative of the controlled density is
\[
\boxed{\dot\rho|_{x=0}=[aA+bB,E_{11}]
=a(E_{01}+E_{10})+b(E_{21}+E_{12}).}
\]
Apply the **same** H46 labelled CP maps to that tangent. Since \(D_0=\operatorname{diag}(1,3/5,0)\),
\[
\boxed{
\left(\mathcal I_{0,0}(\dot\rho)\right)_{01}=\frac{3a}{10},
\qquad
\left(\mathcal I_{0,1}(\dot\rho)\right)_{01}=\frac{3b}{10}.
}
\]
Thus if experimental **Dataset A** independently calibrates these *conditional quantum output coherences* and the coherent phase convention, then it determines BOTH signed a,b, and the best standard quantum comparator will impose the same collective alignment whenever a=b. **The strict conditional H47 prediction-set gap then collapses.** Merely calibrating classical instrument **outcome frequencies** does **not** do this: their first derivatives are zero from the diagonal center seed, and the signed H46 odd flag measures \(a^2-b^2\) at leading order.

Even if the held-out classical odd flag equals zero at every nonblind pulse time,
\[
a^2-b^2=0\quad\Longrightarrow\quad |a|=|b|,
\]
which still leaves the **opposite-sign** physical exchange
\[
(a,b)=(3/5,-3/5)
\]
allowed by standard CPTP and aggregate norm but *outside* the **oriented** collective tangent image \(\mathbb R(A+B)\). Its flag also vanishes. Therefore a null outcome is *consistency* with the collective hypothesis, **not proof** of its oriented microscopic provenance. A separately calibrated phase-sign/coherent readout is necessary to test that stronger orientation claim.

**Instrumentation caveat:** knowing the mathematical CP branch output \(\mathcal I_{0,t}(\rho)\) does not give an experimentalist direct access to its 01 matrix element without **additional coherent tomography operations** and independent apparatus permissions, and those operations are not established in frozen P6's two-real-exchange hardware. H47's actual classical flag-only protocol does not possess the rank7 information tier.

## 6. Status and the next honest mathematical gate

**PASS:** universal finite-dimensional linear kernel criterion; exact rank hierarchy classical3 / nonselective quantum4 / full labelled quantum7 / one-step history9 for original H46/H42; explicit full-instrument positive-state twin counterexamples; independence of source static Jcol and physical control selection in same full uncontrolled CPTP/instrument model; direct tangent identification from extra conditional-coherent readout and the opposite-sign null ambiguity.

**CONDITIONAL PASS:** \(K=\Xi S\) source-control factorization existence iff physical real tangents lie in the independently fixed static Xi image; proper *-orientation, control-provenance, instrument observability, actual device resources and multi-step compatibility require **extra hypotheses**. H47's collective strict null remains a falsifiable **conditional selection theorem** under a deliberately limited Dataset A; not an unconditional CR-only physical law.

**FAIL unconditional claims:** CPTP instrumental validity alone ⇒ observer future closure; H46 outcome probabilities alone ⇒ signed microscopic coherent tangent; shared uncontrolled \(\Phi,\mathcal J_{\rm col}\) and instrument ⇒ P6 locked physical controls; finite-time classical flag null ⇒ oriented \(a=b\); one extra real memory scalar sufficient for *arbitrary* quantum input and all labelled H46 outputs.

**OPEN:** independent original P3/P4 microphysical derivation of \(\mathcal J_N\), real physical S and its *-/control-time/intervention intertwining, experimental access to conditional-output coherence tomography, hardware calibration under full physical control manifold, a residual testable theory-vs-standard-QM gap after genuinely complete calibration, actual P9 EH/Einstein dynamics.

**H49 proposed:** formulate a **minimal, experimentally falsifiable microphysical provenance certificate** that is fixed before Dataset B and independently validates \(S\) (including a controlled \(\Phi_x\), not only an uncontrolled \(\Phi\)); compare the resulting full controlled process tensors and instrument response operators between CR and best standard QM. If they are operationally equivalent, explicitly freeze a no-discriminator theorem rather than infer a CR-only physical effect. Alternatively derive a *specific* non-GKSL constraint from P3 axioms before retesting physical predictions.

## Reproducibility

`P3/P9H48InstrumentProvenanceKernelClosureExactCheck.py` uses H42's exact rational \(U\), H46's unchanged twelve CP branch maps, Gaussian-Fraction exact 9×9 linear ranks (including stacked large output maps), valid positive mixed-state twins, and the H41/H47 static sector and real exchange data. No floating tolerances, no identity of distinct physical map notions, no independent expert/laboratory validation. Dedicated GitHub Actions CI; original frozen manuscripts unchanged.