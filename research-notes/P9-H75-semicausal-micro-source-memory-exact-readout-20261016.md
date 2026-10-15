# H75 — A Single Six-Dimensional CPTP Microscopic Source with Nonzero Original P3 Return, Full Two-Knob Real Control, and an Autonomous Exact-Readout Quantum Observer

**2026-10-16 | P3–P11 Mathematical Bridge / Route A.** Stacked on H74 Draft PR #93 (**parent 87/87 GitHub Actions PASS**). This result resolves a restricted **existence** question: one explicit *common microscopic quantum model* simultaneously has a true nonzero original P3 signed quadratic residue, all separately declared real A/B path exchange controls and independently calibrated site dephasing, a nontrivial information-bearing environment flag, an exact autonomous **3-dimensional quantum observer**, and matched **single-copy, physically positive** visible measurement instruments. It does **not** prove that these independently specified physical operations arise from P3 alone, or that CR provides new operational predictions beyond quantum theory.

## 1. Construct a genuine microscopic source, not an after-the-fact abstract observer

Let the microscopic Hilbert space be \(\mathcal H_{\mu}=\mathbb C^2_E\otimes\mathbb C^3_S\) (environment-first ordered basis, dimension six), with an unrestricted correlated input \(X\in M_6(\mathbb C)\). The observer is the standard, physically CPTP environment partial trace

\[
\boxed{C(X)=\operatorname{Tr}_E X\in M_3(\mathbb C).}
\]

It retains the **entire qutrit quantum state** but loses information about the actual two-state environment. It has a CPTP right inverse \(J(\rho)=|0\rangle\langle0|_E\otimes\rho\), but is **not** left-invertible as a channel on all 6D states. This obeys H74's general no-loss theorem: exact all-state single-copy visible population readout requires preserving the visible qutrit; H75 only discards the *additional hidden environment*, not those three physical quantum levels.

Fix the unchanged H42 original nonreal 3-site unitary

\[
U=\operatorname{diag}(i,1,i)\,
\begin{pmatrix}2/3&2/3&-1/3\\-2/3&1/3&-2/3\\-1/3&2/3&2/3\end{pmatrix}.
\]

Independently specify a genuine two-outcome *unsharp* site measurement on S with exact rational diagonal Kraus operators

\[
M_0=\operatorname{diag}(1,3/5,3/5),\qquad
M_1=\operatorname{diag}(0,4/5,4/5).
\]

The effects obey \(M_0^\dagger M_0+M_1^\dagger M_1=I\), but measurement outcomes contain genuine information about S: for \(|0\rangle_S\), outcome 1 probability is zero; for \(|1\rangle_S\), it is \(16/25\). The state-changing instrument partially dephases coherence involving site zero; it is not merely an ancilla spectator or state-independent hidden random flag.

The **fully microscopic four-Kraus quantum channel** on \(M_6\) is

\[
\boxed{
\Phi_\mu(X)=\sum_{a,b=0}^1L_{ab}XL_{ab}^\dagger,\qquad
L_{ab}=|a\rangle\langle b|_E\otimes UM_a.
}
\]

Interpretation: erase/reset the old two-state flag, perform the physical unsharp measurement of S, *record* the outcome as flag \(|a\rangle\), and apply the SAME fixed H42 nonreal quantum unitary U to S. The coherent two-outcome measurement and flag reset are physical **architectural assumptions**, not deduced from the original P3 filtration. The exact checker constructs all four 6×6 Kraus matrices, verifies \(\sum L_{ab}^\dagger L_{ab}=I_6\), and checks TP and Hermiticity preservation on all 36 matrix-unit inputs.

**Autonomous CPTP quotient on arbitrary correlated microscopic inputs.** Partial trace after the full microscopic CPTP step satisfies the exact all-operator identity

\[
\boxed{
C\Phi_\mu=\Phi_S C,\quad
\Phi_S(\rho)=U\left(M_0\rho M_0^\dagger
+M_1\rho M_1^\dagger\right)U^\dagger.}
\]

This identity works even if the initial microstate contains arbitrary system–environment entanglement/correlations or an arbitrary distribution of the old environment flag, because the reset/output Kraus pairs sum over the prior flag. There is *no hidden-to-visible feedback* in this architecture; this strong semicausal premise, not mere rank, makes the CP quotient possible.

## 2. H75.1 — original-P3 \(R_2=0\), \(R_3\ne0\) holds IN THE FULL SIX-DIMENSIONAL MICRO SOURCE

For any diagonal six-dimensional seed \(D\in D_6\), define the **original P3** microscopic hidden iterates

\[
H_1(D)=(I-\Delta_{D_6})\Phi_\mu(D),\quad
H_2(D)=(I-\Delta_{D_6})\Phi_\mu^2(D)
\]

and original signed quadratic return

\[
R_3(D,D')=\Delta_{D_6}\big([H_1(D),H_2(D')^\dagger]\big).
\]

This is not a new parity-labeled proxy or a reduced-memory-only commutator. The same original \(\Phi_\mu\) supplies both hidden iterates. Exact rational evaluation shows the second-order diagonal commutators \(\Delta_{D_6}[H_1(D),H_1(D')^\dagger]\) vanish for every pair of diagonal basis seeds (thus by bilinearity for all diagonal seeds), while for the genuine positive microscopic diagonal seed \(D=|0\rangle_E\langle0|\otimes E_{00}\),

\[
\boxed{
R_3(D,D)=\frac{i}{135}\operatorname{diag}(-32,16,16,0,0,0)\ne0.
}
\]

This is a genuine all-six-dimensional original-P3 diagonal quadratic witness for a CPTP quantum channel with an **informative and nontrivial** environmental output flag. The checker re-evaluates all 36 matrix-unit operations using exact Gaussian rational arithmetic, including all 36 basis-pair \(R_2\) vanishings.

The reduced visible channel \(\Phi_S\) also has a nonzero original signed depth-three return on the three-site diagonal algebra, for example

\[
R_3^{S}(E_{00},E_{00})
=\frac{i}{135}\operatorname{diag}(-32,16,16)
\]

and

\[
R_3^{S}(E_{11},E_{11})
=\frac{i}{405}\operatorname{diag}(-8,64,-56).
\]

The full six-dimensional and reduced three-dimensional residues are computed **separately**; no false identity such as \(\operatorname{Tr}_E[H_1,H_2^\dagger]=[\operatorname{Tr}_EH_1,\operatorname{Tr}_EH_2^\dagger]\) is assumed.

These are standard finite open-quantum-system effects, not CR-exclusive signatures; H50's full controlled process equivalence remains relevant.

## 3. H75.2 — retain BOTH independent real P6-type exchange knobs and independent site dephasing

Define \(A=E_{01}-E_{10}\), \(B=E_{21}-E_{12}\), and exact, independently chosen rational Cayley pulses

\[
V(x,y)=
(I+xA)(I-xA)^{-1}
(I+yB)(I-yB)^{-1}.
\]

They are genuine real-orthogonal qutrit unitaries; x,y are **independent microscopic physical-control parameters**, not restricted to x=y. Define the calibrated CPTP site phase-flip maps \(\mathcal D_j^{(q_j)}\) on S with arbitrary independent q0,q1,q2 in [0,1]. The controlled visible channel is

\[
\Psi^S_{x,y,\mathbf q}
=\mathcal D_2^{(q_2)}\mathcal D_1^{(q_1)}
 \mathcal D_0^{(q_0)}
 \operatorname{Ad}_{V(x,y)}\circ\Phi_S.
\]

**Microscopically**, use exactly the same operators on \(\mathbb C^2_E\otimes\mathbb C^3_S\), acting trivially on the environment flag after \(\Phi_\mu\). Because these Kraus controls do not signal from E back into S, on all 36 microscopic basis units

\[
\boxed{
C\Psi^\mu_{x,y,\mathbf q}
=\Psi^S_{x,y,\mathbf q}C.
}
\]

All components are explicitly CPTP. The identity continues to hold for every finite switching sequence, every correlated microscopic input, and arbitrary settings drawn from this declared control/noise catalog; the checker tests several exact independent rational settings and finite sequences.

This is a **nontrivial coexistence** of true nonzero original P3 microscopic quadratic residue and the full independent real two-exchange *control family*, which H74 could not achieve within the restricted 2D reflection-even code. It evades H72's subalgebra No-Go because the observer is \(M_6\to M_3\) partial trace, **not** a proper unital-subalgebra conditional expectation inside the original \(M_3\), and it does not lose any of the *visible* qutrit quantum information.

**Source/provenance boundary:** The independent A/B knobs and the unsharp measurement/reset are declared and realized directly inside a 6D **common microscopic control-channel architecture**, but there is NO theorem that the uncontrolled original P3 hidden filtration *uniquely forces* these controls, the flag readout or frozen P6 v9.1's independently sourced \(\mathcal J_N\). Existence of one such microscopic architecture is a meaningful Route-A intermediate success, not generative necessity from \(F\) or original P3 data.

## 4. H75.3 — exact single-copy physical population and visible adaptive-instrument equivalence

For each visible site \(j\), let \(Q_j=|j\rangle\langle j|\). The actual measured microscopic quantum instrument branch is \(\mathcal I^\mu_j(X)=(I_E\otimes Q_j)X(I_E\otimes Q_j)\). The reduced branch is \(\mathcal I^S_j(\rho)=Q_j\rho Q_j\). Partial trace strictly commutes with these branches,

\[
C\mathcal I^\mu_j=\mathcal I^S_j C.
\]

Consequently the full quantum–classical process of **visible-only** quantum controls and CP measurement branches has the same single-copy outcome probabilities and the same conditional reduced output states as the autonomous 3D CPTP observer, by induction over any finite adaptive sequence of such operations. Unlike H73's negative-coefficient statistical inversion, here measurement probabilities agree by direct physical partial trace, **with no offline tomography or nonpositive recovery**. The checker proves this on all microscopic matrix units and tests multiple conditional outcome histories.

This strong operational claim is carefully limited to interventions on S which do not condition on the unobserved E flag. If an experimenter can observe and act upon the environment, the full 6D process contains additional distinguishable outcomes not reproducible by the reduced S observer.

## 5. H75.4 — a precise hidden-feedback obstruction

The success depends on *absence of environment-to-visible signalling*. With the same 6D Hilbert space, allow a genuine CPTP feedback unitary that acts on S as the 01-site SWAP **only if the flag is 1**, and acts as identity if the flag is 0.

Then the two microscopic states \(|0\rangle_E\langle0|\otimes E_{00}\) and \(|1\rangle_E\langle1|\otimes E_{00}\) have **identical visible partial trace** before feedback but visibly different reduced states \(E_{00}\) and \(E_{11}\) afterward. Thus **no** autonomous reduced linear or CPTP channel for that feedback operation exists. H75 verifies this by exact 6×6 matrix arithmetic. This counterexample shows precisely how a genuine feedback-bearing non-Markovian shadow would invalidate the simple CP marginal closure and require physical quantum memory.

The four-Kraus source has an **informative flag** but resets it each step. It is not a generic unitary closed-system non-Markovian memory model where old environmental history feeds back. The boundary prevents misinterpreting this semicausal existence construction as a universal solution to P5 non-Markovian dynamics or quantum gravity.

## 6. Status, assumptions and H76 target

| Gate | H75 status |
|---|---|
| One explicit nontrivial 6D microscopic CPTP source | **EXACT**, four Kraus, all-input CP semicausal identity |
| Genuine original P3 \(R_2=0,R_3\ne0\) on **full M6** microscopic diagonal algebra | **EXACT**, nonzero 6D signed-return witness |
| Reduced original visible P3 return nonzero, independently computed | **EXACT** |
| Both independent real 01/12 exchange controls + independently calibrated site noise | **EXACT conditional construction**, no reflection lock |
| Autonomous visible CPTP evolution on all correlated 6D inputs | **EXACT**, \(\operatorname{Tr}_E\) intertwiner |
| Exact visible single-copy measurement and finite adaptive visible-only instrument histories | **EXACT**, CP branch intertwining |
| Hidden flag actually records site information and is genuinely discarded by observer | **EXACT** |
| Observer closes under explicit E-to-S feedback gate | **NO**, two-state exact counterexample |
| P3-only provenance of controls, unsharp instrument and quantum flag; frozen P6 physical \(\mathcal J_N\) | **OPEN**, architectural assumptions not derived from residues |
| CR-only discriminator; P7/P8 soldering; full off-shell HDA, ADM/Einstein dynamics | **OPEN**, P9 Minimum Success not met |

**H76 recommended gate:** isolate which part of the H75 *semicausal instrument architecture* can be inferred from original P3 dynamical data, rather than postulated. Derive a structural characterization of all CPTP extensions that obey the exact partial-trace intertwining condition, and test how a nontrivial hidden→visible feedback term can be retained if one adds a **minimal explicitly physical predictive quantum memory** rather than resetting the flag. A genuinely non-Markovian extension will require more than the H75 3D CP marginal. In parallel, P9 may safely use H75 as a **finite existence comparator only**, not as a microphysical derivation of ADM/HDA or Einstein gravity.

**Reproduce:** \`python3 P3/P9H75SemicausalMicroMemorySourceExactCheck.py\`. Source is explicit, all rank/commutator/Kraus identities use exact Gaussian rationals with no tolerance. Draft/unmerged, no changes to main/frozen papers, no Lean kernel proof, human expert peer review, lab experiment, CR-exclusive signature or P9 GR Minimum Success.
