# H68 — Minimal Predictive Completion, Quantum-Instrument Accessibility, and the CPTP Recovery Obstruction

**2026-10-16 | P3–P11 Mathematical Bridge → P9 GR-I.** Stacked on H67 Draft #86, whose head reached 80/80 GitHub CI PASS. The finite comparator is **exactly the prior H42 original-P3 CPTP unitary channel**, coupled to **exactly the H46 twelve-outcome CP quantum instrument** used in H48 and H67. This research Draft does not enlarge frozen-P6 physical permissions without labeling additional hardware. No CR-specific quantum prediction or gravity equation is asserted.

## 1. The linear observer dimension lower bound is sharp

Let \(M_3\) be the nine-dimensional COMPLEX operator space, \(\Phi=\mathrm{Ad}_U\) the fixed microscopic channel, and \(C:M_3\to \bigoplus_{12}M_3\) the H46 full **labelled conditional quantum-output** CP instrument. Important: \(C\) is **not** the frozen P6 population-only readout or merely the classical 12-outcome probability vector.

Existing exact H48 identities:

\[
\operatorname{rank}_{\mathbb C}C=7,\qquad
\ker C=\operatorname{span}_{\mathbb C}\{E_{02},E_{20}\},
\qquad
\operatorname{rank}_{\mathbb C}\binom{C}{C\Phi}=9.
\]

**Theorem H68.1 — exact necessary predictive information.** Suppose a linear record \(R:M_3\to W\) predicts both *present* and *one future* passive ensemble snapshot, i.e. there are linear \(L_0,L_1\) with \(C=L_0R\) and \(C\Phi=L_1R\). Then

\[
\ker R\subseteq\ker C\cap\ker(C\Phi)=\{0\},
\quad \boxed{\operatorname{rank}_{\mathbb C}R=9}.
\]

(The upper bound is 9 since the input space has complex dimension 9.) In particular the 7D original record requires at least two supplementary complex-linear directions. On the real affine space of Hermitian trace-one densities these are precisely two missing real coherence quadratures \(E_{02}+E_{20}\) and \(i(E_{02}-E_{20})\), independent of the trace. This is a **dimension result**, not a physical number-of-qubits-memory lower bound. For restricted initial conditions or limited future controls, smaller predictive subspaces can be possible; H68's quantifiers are arbitrary microscopic inputs and both prescribed full quantum records.

The equality \(\operatorname{rank}(C,C\Phi)=9\) was already in H48. H68's new contribution is a **minimal conditional CP measurement completion with two certified probes and a rigorous no-recovery boundary**, not a false claim to rediscover the H48 rank.

## 2. Exact minimal two-probe coherent tomography

Let \(A=E_{01}-E_{10}\), one existing **real-exchange control TYPE** in frozen P6, and choose the exact rational Cayley unitary

\[
U_A(h)=(I+hA)(I-hA)^{-1},\qquad h=1/4.
\]

Define the *extra*, independently specified controlled observation \(C_A=C\circ\operatorname{Ad}_{U_A}\), performed on a separately prepared copy before the H46 instrument. H67 established and H68 independently rechecks

\[
\operatorname{rank}_{\mathbb C}\binom{C}{C_A}=9.
\]

This is informational completeness of a pair of quantum-output measurement settings; it does NOT make the current 7D record autonomously predictive without the two extra observed components.

**Sharp two-function extension.** Since the kernel of C is exactly two complex dimensions and the restriction of \(C_A\) to that kernel is injective, an invertible \(2\times2\) minor exists among the coordinate components of \((C_A(E_{02}),C_A(E_{20}))\). Choose two such complex-valued conditional quantum-block matrix-entry functionals \(f_1,f_2\). Then

\[
R_{\rm min}(X)=\big(C(X),f_1(X),f_2(X)\big)
\]

is injective, of complex rank nine, with **exactly two additional complex scalar** linear readouts. The exact verifier *finds* an explicit nonzero minor and checks rank 9 over rational Gaussian numbers (not floating rank inference). For physical Hermitian densities two appropriately chosen **real** components of those same conditional outputs separate the two missing real coherence quadratures.

**Physical scope:** Access to **full labelled quantum-block tomography, coherent preparations and instrument calibration** is far beyond the frozen P6 v9.1 population-only instrument. The rational real-exchange \(A\) itself is of a declared P6 control type; combining it with the H46 quantum instrument and preparing separate copies remains a CONDITIONAL expanded measurement protocol. The selected two complex quantum-block matrix entries are linear reconstruction functionals; their values require statistical quantum-state tomography and are not single-shot scalar outcome probabilities.

## 3. H68.2 — a bona fide randomized 24-branch CPTP informationally complete instrument

There is a mathematically physical **single-use CP instrument** exhibiting the same information-access result, not just a formal concatenation of maps. Randomize the interrogation setting with a classical coin. With probability 1/2, apply H46's existing instrument C. With probability 1/2, first apply the unitary \(\mathrm{Ad}_{U_A}\) and then apply C. Retain the public setting label and all 12 existing CP outcome labels, giving 24 mutually labelled conditional quantum-output branches:

\[
\boxed{
\mathfrak I(X)
=\frac12 C(X)\oplus\frac12 C(U_AXU_A^\dagger).
}
\]

Each branch is CP, and summing trace over both settings/12 outcomes gives \(\mathrm{Tr}X\). The original H46 branches have a Kraus representation, and the real-Cayley unitary is exact, so \(\mathfrak I\) is a genuine trace-preserving quantum-to-labelled-quantum CPTP channel. As a complex-linear map, \(\operatorname{rank}\mathfrak I=9\); thus it provides an **informationally complete** observer record for tomography across *many independently prepared copies*. Two positive Hermitian density pairs differing solely in the real or imaginary 02 chord have identical original C outputs and **different** \(\mathfrak I\) outputs, certified exactly in the checker.

This does **not** constitute a passive, nondisturbing, autonomous single-system quantum memory. The coin-controlled pulse and the quantum instrument intervene in the system; a measurement may destroy the coherence information required for later dynamics. It cannot be inserted into the middle of a microscopic \(\Phi\)-trajectory and silently equated to snapshots of the unmeasured system. Likewise, the H48 record pair \((C,C\Phi)\) is a passive **separate-preparation ensemble** construction, not one sequential noninvasive instrument.

## 4. H68.3 — informational completeness does NOT provide CPTP quantum recovery

Because \(\mathfrak I\) is injective as a LINEAR map on the nine-dimensional complex input operator space, there is an abstract linear inverse on \(\operatorname{im}\mathfrak I\). Thus, for any specified microscopic linear \(\Phi\), one may define a LINEAR predictive flow

\[
\widehat\Phi=\mathfrak I\circ\Phi\circ(\mathfrak I|_{M_3})^{-1}
\]

*only on the nine-dimensional range*. This is algebraically well defined; its extension to a CPTP channel on the full 24-block output algebra is **not proven** and does not follow from injectivity.

There is a sharper negative result for *recovery of the input quantum state*. For a quantum channel with CP-labelled orthogonal flag branches \(\{K_j\}\), perfect correction on the entire input Hilbert space requires the whole-space Knill–Laflamme condition \(K_i^\dagger K_j=c_{ij}I\). For \(\mathfrak I\)'s **unchanged H46 arm**, consider the outcome arm=0, k=0, t=0. The exact Kraus operator is \(\tfrac12 D_0\), where \(D_0=\mathrm{diag}(1,3/5,0)\). Consequently,

\[
\boxed{K_j^\dagger K_j
=\operatorname{diag}(1/4,\,9/100,\,0)
\not\propto I.}
\]

Therefore the channel \(\mathfrak I\) **cannot have a CPTP left inverse recovering every unknown quantum input state**. The checker verifies this effect matrix in exact rationals. This result uses a standard quantum error-correction necessity; it does not assert impossibility of ensemble state estimation, nor rule out a special-state or codespace recovery map.

This distinction blocks a tempting overclaim: an informationally complete quantum measurement is not automatically an emergent physically autonomous Markovian quantum observer. A full-state physical memory carrier would require independently engineered quantum storage/dynamics, not merely invertible quantum-block tomography outputs. The identity-channel “store the entire microscopic state” construction is formally sufficient and explains nothing about independent generative observer provenance.

## 5. Source/protocol/Einstein status and next H69

| Item | H68 mathematical conclusion | Physical status |
|---|---|---|
| Linear record to predict all C and C Phi for arbitrary microscopic input | Rank 9 NECESSARY, H48 already supplies lower bound; two extra complex readouts suffice | Requires independently realized full quantum-output instrument |
| Positive trace-preserving CP instrument with informationally complete output | YES as conditional arm-randomized C plus real-Cayley C | Invasive and ensemble-tomographic; not frozen P6 hardware |
| Full quantum-state CPTP recovery from that instrument | NO, exact nonscalar Kraus effect violates whole-space KL criterion | Restrict codespace/different quantum memory may evade |
| CPTP autonomous future evolution solely on 24-block record | NOT derived: linear range-conjugated map does not imply global CP extension | OPEN |
| P3-generated real/odd control and microscopic physical \(\mathcal J_N\) | Neither follows from original P3's uncontrolled filtration | OPEN |
| Independent KKS–ADM symplectic physical map, DeWitt, HDA/Einstein | None generated | P9 Minimum Success remains UNMET |

**H69 suggested next gate:** test whether the *range* of this specific informationally complete CPTP instrument is invariant under any explicitly specified **physical output CPTP channel** realizing a microscopic \(\Phi\), rather than assuming positivity extends from the range. Independently study restricted-code/subalgebra cases and controlled quantum memory with actual coupling/provenance, separating the formal nine-complex-dimensional full-state sufficient statistic from a genuine emergent lower-dimensional observer. H50 remains binding: matched standard QM full controlled processes/instruments reproduce all statistics; no CR-only prediction has appeared.

## Verification and review

Reproduce using \`python3 P3/P9H68MinimalPredictiveCPAugmentationExactCheck.py\`; it imports the exact H48 source + H46 instrument, performs all-rational rank checks, constructs concrete minimal complex and real chord-output pivot minors, verifies 24 CP-branch trace preservation and real-Cayley unitarity, tests positive pair discrimination, and shows a precise nonscalar effect obstructing full-state CPTP recovery.

All newly established conclusions are finite mathematical statements under declared sources, instruments and protocols. **Draft/unmerged; no frozen/manuscript/main modifications; no human expert peer review, Lean kernel proof, experiment, independently sourced frozen-P6 hardware, CR-exclusive dynamics, P9 GR-I success, HDA or Einstein result.**
