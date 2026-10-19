# H107 — Typed Generative Completion and an Actual Positive Phase-Correlation Readout: P9/P11 Handoff After H106

**2026-10-19 | Twelve-Paper Generative Program — P3–P11 Mathematical Bridge; P9 GR-I, P11 F Axiomatization**

**Source:** H106 Draft PR #125 (100/100 CI PASS), H105 linked H75×H75 source, original H75 four-Kraus finite CPTP source and original P3 signed \(R_3\). No changes to main, the published/frozen P1–P8 or original source. **No new Hamiltonian is postulated at H107.** This phase closes the fictional interaction-example loop in favor of a typed, genuinely operational detection witness and rigorously source-scoped P9/P11 proof obligations.

## 1. H107.1 — One explicit positive, locally measurable two-cell phase-correlation effect separates H106's flag-indistinguishable states (EXACT CONDITIONAL)

H106 exhibited two true positive source inputs to the **same** original H75×H75 sixteen-Kraus two-cell CPTP device:

- Native \(\rho_{\rm prod}=P_1\otimes|+\rangle\langle+|\), a separable prepared state;
- Conditional \(\rho_{\rm link}=R\rho_{\rm prod}R^\dagger\), with precisely the **EXTERNAL** H105 coherent controlled-X interaction, not available from original local A/B Hamiltonians.

The entire joint two-flag distribution \(p_{ab}\) is identical in both cases; the actual source output flag00 probability is \(\boxed{153/625}\) and the conditional link branch is NPT, as witnessed by a negative partial-transpose principal minor \(-2916/390625\). Under original fixed \(U\otimes U\) output calibration, let
\[
\begin{aligned}
Y_{12}&=-i|1\rangle\langle2|+i|2\rangle\langle1|,\\
X_{01}&=|0\rangle\langle1|+|1\rangle\langle0|,\\
C&=Y_{12}\otimes X_{01},\qquad Q_C=\frac{I_9+C}{2},\\
E_C&=|00\rangle\langle00|_{\rm out\ flags}
\otimes(U\otimes U)Q_C(U\otimes U)^\dagger.
\end{aligned}
\tag{H107-POVM}
\]
Both \(X_{01},Y_{12}\) are Hermitian with eigenvalues \(-1,0,1\), so \(C\) has spectrum in \(\{-1,0,1\}\) and \(Q_C\) is a **legitimate positive effect** \(0\le Q_C\le I_9\). Thus \(E_C\) is a genuine \(0\le E_C\le I_{36}\) original-H75×H75 output positive effect. One can implement its statistics via **local Hermitian-site measurements** \(Y_{12}\) and \(X_{01}\), coarse flag00 postselection, and classical processing of their outcomes, PROVIDED these additional local detector settings are independently calibrated; no new coherent *intercell control* is required for detection.

The uncalibrated true flag00 site block from H106 is
\[
\sigma_{00}^{\rm link}
=\tfrac12|v\rangle\langle v|,\quad
v=\tfrac35|1,0\rangle+\tfrac{27}{125}|1,1\rangle-\tfrac{36i}{125}|2,1\rangle.
\]
The native state yields \(\sigma_{00}^{\rm prod}\) with site1 strictly supported on \(|1\rangle\). Direct, exact rational Born computations give
\[
\boxed{
\operatorname{Tr}(C\,\sigma_{00}^{\rm prod})=0,\qquad
\operatorname{Tr}(C\,\sigma_{00}^{\rm link})=-\frac{108}{625}.
}
\tag{H107-CORR}
\]
Consequently the **positive effect probabilities** differ by
\[
\boxed{
\operatorname{Tr}\big(E_C\,\Phi_\mu^{\otimes2}(\rho_{\rm prod})\big)
=\frac{153}{1250},\qquad
\operatorname{Tr}\big(E_C\,\Phi_\mu^{\otimes2}(\rho_{\rm link})\big)
=\frac9{250}.
}
\tag{H107-POSITIVE}
\]
Here \(\Phi_\mu^{\otimes2}(\rho)\) abbreviates the actual two-flag, two-site H75 input convention, not a made-up 9→9 trace-preserving channel.

Conditioned on the **same true original flag00 probability \(153/625\)**, the positive-effect probabilities are
\[
\boxed{
p(Q_C\mid00,{\rm prod})=\frac12,\qquad
p(Q_C\mid00,{\rm link})=\frac5{34}.
}
\tag{H107-CONDITIONAL}
\]
The checker computes these by the true H106 source matrices AND an independent explicit three-amplitude formula. Its exact Hermitian \(C^3=C\) polynomial certificate establishes effect positivity (no numerical diagonalization).

**Interpretation:** H106 supplied an entanglement existence/NPT diagnostic. H107 adds an **explicit valid positive, local-product-measurement-based phase-correlation readout** that distinguishes those same two H75 output cases although every coarse flag statistic matches. This is an operational *sufficiency example* for added readout settings—not an entanglement witness by itself (the probability difference is not universal across separable states), not a CR-exclusive prediction, and not an actual experiment or source-derived physical link. The physical detector permission is additional to coarse original H75 flags.

## 2. H107.2 — Exact logical factorization obstruction for the existing real local-only source (NO-GO, unchanged physics)

The whole inherited H75 local Hamiltonian control algebra on two cells is \(\mathfrak{so}(3)\oplus\mathfrak{so}(3)\). All time-dependent coherent propagators factor, all local H75 resets and any LOCC-separable coarse control preserve separability. Therefore **the H105 conditional linked state with the above NPT output cannot be produced by native local H75 operation permissions from the stated separable input**.

The distinction among operations is:
\[
\begin{aligned}
\text{Kraus-compatible mathematical link }&\not\Rightarrow\text{ physically permitted link Hamiltonian},\\
\text{physical entangling operation }&\not\Rightarrow\text{ nondegenerate generated 6-pair ADM phase space},\\
\text{nondegenerate KKS pair }&\not\Rightarrow\text{ physical Cartan connection/solder/curvature},\\
\text{Cartan-compatible curvature }&\not\Rightarrow\text{ source-generated DeWitt/HDA/Einstein}.
\end{aligned}
\tag{H107-TYPES}
\]
H105's extra controlled-X link is a constructive **sufficient example** of a CPTP-compatible *conditional* one-pair KKS orbit; it is NOT logically necessary that future physics implement that exact matrix. H106's native-local separability obstruction only makes some **nonlocal quantum resource** necessary for *this specific entanglement target* under the local-only initial state and permissions. It does not globally prohibit arbitrary sourced entangled resources, shared quantum memory or other physical interactions.

## 3. H107.3 — Typed same-source micro→ADM/Cartan integration certificate

A future genuine bridge theorem must supply explicit functions and experimentally/reconstructibly grounded facts, not merely equal dimensions:

**AX-SRC**: SAME physical microscopic Hilbert carrier \(\mathcal H\), CPTP/instrument \(E\), original P3 signed-residue definition, initial accessible state sector \(\mathscr S\), a separately evidenced list of physical coherent controls \(\mathscr U\), actual nonlocal Hamiltonian \(H_{\rm int}\) or a sourced dynamical memory, and a fixed observable algebra \(\mathcal A\). H75 local source is actual **mathematical source data**; the P9.125–128 Cartan dynamic register/observer source is reported in another thread and was NOT source-matched/independently fetched. A claimed \(H_{\rm int}\) must have more than \([H,M_a\otimes M_b]=0\): it must have actual operational provenance (control Hamiltonian or derived generator).

**AX-OA**: an observer map respecting physical effect positivity and making the claimed orbit and transport identifiable. The H107 \(E_C\) supplies one conditional demonstration of distinguishability, but neither this scalar witness nor the four coarse flags is an informationally complete field-observer system. State whether observer algebras are **fixed** or **covariantly transported**; H104 shows exact fine-MASA preservation destroys the native connected B-sector.

**AX-CAN**: a **physically preparable** isospectral manifold \(\mathcal O\), a nondegenerate KKS/symplectic \(\omega\), real physical Hamiltonian vector fields \(X_h\) accessible in the source controls, and spatially transported canonical pairs \((q,p)\) satisfying \(\iota^*\Omega_{\rm target}=\omega\) (or a precisely typed, constraint-reduced/gauge-quotiented alternative). H105 one conditional pair ≠ full 6+6 ADM. H99's particular source-selected K4 metric family has rank3, and H95 single-reset KKS transmission has rank≤8 across a 12D pre-reset orbit.

**AX-SP**: SAME-source physical cells, actual *intercell* channels/parallel transports \(T_{xy}\) with stated source-state naturality and edge orientation, a physically defined 3D spatial carrier and solder \(e_x\), and comparison Cartan transport \(\mathcal P_{xy}^{\rm Car}\) with \(e_yT_{xy}=\mathcal P_{xy}^{\rm Car}e_x\). Derive metric preservation, torsion (or its independent selector), curvature two-jet and loop consistency. H104 constructed different mathematical K4 holonomies compatible with the **same** local CPTP data; edge assignments are not source-selected. The P9.125–128 Cartan model is **not assumed H75**, and report of nonstationary free energy at torsion-free does not supply a selector.

**AX-DYN**: a Hamiltonian/action derived from \(\mathcal H,E,H_{\rm int},\mathcal A\) with correct spatial derivative \(R[g]\) and indefinite DeWitt kinetic form, nonuniform off-shell constraint generators satisfying actual full HDA, lapse/shift interpretation and physical Einstein dynamics. H98/H100's \(\lambda=1/2,\alpha\beta=1\) are exact **conditional comparisons to imported ADM** after the curvature/canonical hypotheses are supplied—not a derived CR gravitational action.

**AX-NORM**: distinguish mathematical canonical rescalings from physically fixed Newton/cosmological coupling, material units/boundary/matter sector. H100 leaves \((\alpha,\beta,\lambda,\Lambda)=(a,a^{-1},1/2,\ell)\) within the imported ADM comparison; a or ℓ are NOT selected by original four H75 effects.

**AX-GEN**: formally axiomatize F and give **noncircular proofs** generating AX-SRC→AX-OA/AX-CAN/AX-SP→AX-DYN/AX-NORM on a stated sector; maintain formal countermodels where the antecedent holds but the next conclusion fails. Otherwise those are additional independent physical axioms, not a completed generative completeness theorem.

All seven AX headings are **research axiom candidates/proof obligations**, NOT adopted established axioms of the published F program or physical consequences of P3.

## 4. P9.125–128 reported findings and exact limits of compatibility

The P9 track reports (i) holonomy and signed P3 residue are mutually insufficient to select torsion; (ii) locally calibrated connected transport and witnesses can conflict with observer-algebra invariance; (iii) dynamic-register acceleration and the tested free-energy functional do not select torsion-free by stationarity.

No primary source-level P9 Cartan Hamiltonian/observer/solder was available through connected repo/targeted Notion during this audit. Thus no identification with H75's \(\Phi_\mu\), A/B, 16-Kraus product source, or H105 hypothetical link is asserted. A future P9 handoff must provide **source definitions and matching maps** before either model's theorem can be transferred. This is a **provenance gate**, not evidence P9 Cartan results are incorrect.

**Required P9 source-bundle fields (typed):**
\[
\boxed{
(\mathcal H_{\rm P9},\mathcal L_{\rm P9},\mathscr U_{\rm P9},
\mathscr S_{\rm P9},\mathcal A_{\rm P9},
\{T_{xy}^{\rm P9}\},\{e_x^{\rm P9}\},
\text{Cartan }\nabla,\text{proof artefacts}),
}
\]
plus a proposed physical embedding/simulation map into/from H75 carrying observables and Hamiltonian controls with preserved probabilities and channels; not merely \(3=3\) dimensional correspondence.

## 5. Decision and stop rule

**Current P9 verdict:** A source-compatible two-cell link and operational two-site phase readout are mathematically constructible; the original H75 physical control Lie algebra lacks the link, the formal compatible links do not select a Cartan connection, and no actual common P9.125–128 source nor ADM fields are independently established. Therefore **P9 GR-I remains conditional** and Einstein physics is not sourced by this finite branch.

**Current P11 verdict:** Precisely typed, independent **AX-INTERCELL/AX-CAN** physical interaction, **AX-SP** spatial gluing/solder and **AX-DYN** action/constraint generation are unavoidable additional obligations, but the concrete controlled-X matrix is **a sufficient illustrative candidate, not a uniquely necessary axiom**. H107's positive effect demonstrates what further operational measurements can resolve *given* the link, not why nature or F must supply it.

**Next substantive work:** Only (a) fetch and independently inspect a concrete physically authored P9 source Hamiltonian + observer + Cartan transport + solder bundle, or (b) formulate and independently audit a theorem deriving such a bundle from new *explicit* F axioms. Do **not** extend the H75 sequence with more hypothetical intercell links or arbitrary ADM potential choices as a substitute for physical provenance.

**Audit status:** explicit genuine original-H75 two-cell positive effect and phase separation **EXACT CONDITIONAL**; local-only nonlocal-link inaccessibility **EXACT scoped**; shared P9/H75 origin, Einstein dynamics and F completeness **OPEN**. This is an independently reproducible exact arithmetic / GitHub CI program, NOT human peer review, experiment or Lean Einstein formalization.
