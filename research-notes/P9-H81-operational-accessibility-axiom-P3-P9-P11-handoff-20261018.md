# H81 — Operational Accessibility as the Missing Source Datum: Exact Control-Order Witness and P9/P11 Handoff

**2026-10-18 | P3–P11 Mathematical Bridge / Route A.** This is an **integration and logical-boundary stage**, not a claim to have derived physical interventions from the original uncontrolled P3 filtration. H80's sharp five-Hilbert-level, thirteen-operator-rank CPTP recovery theorem has reached **93/93 CI PASS** (Draft PR #99). H81 preserves **unchanged** H75's six-dimensional microscopic CPTP channel \(\Phi_\mu\), the genuine original P3 diagonal \(R_2=0,R_3\neq0\), H76's physical flag observer, and H77/H78's catalog-dependent control-observability results. We establish a new **positive-density/positive-POVM, exact-rational causal-order witness** proving that even the same physical control gates and the same source require extra *temporal accessibility* information to select an observer. We then state one explicit, independently certifiable additional-data axiom **AX-OA**, with exact limits on which parts can be passed to P9 and P11.

## 1. H81.1 — the missing datum is not just an operator but a physically executable intervention schedule

Fix the H75 original quantum source

\[
\Phi_\mu(X)=\sum_{a,b=0}^{1}
\bigl(|a\rangle\langle b|_E\otimes UM_a\bigr)
X
\bigl(|a\rangle\langle b|_E\otimes UM_a\bigr)^\dagger,\qquad
\begin{cases}
M_0=\operatorname{diag}(1,3/5,3/5),\\
M_1=\operatorname{diag}(0,4/5,4/5),
\end{cases}
\]

on \(M_6(\mathbb C)\), with precisely the original H42 nonreal \(U\). The actual unperturbed P3 microscopic quadratic signed witness is unchanged:

\[
\boxed{R_3(D,D)=\frac{i}{135}
\operatorname{diag}(-32,16,16,0,0,0)\neq0.}
\]

Retain the rank-18 CPTP flag observer

\[
C_{\rm flag}(X)=P_0XP_0+P_1XP_1,\quad
\operatorname{im}C_{\rm flag}\cong M_3\oplus M_3.
\]

The H76 microscopic flag-rotation pulse and flag-conditioned physical feedback are, respectively,

\[
W=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}_E\otimes I_3,\qquad
F=|0\rangle\langle0|_E\otimes I_3+
  |1\rangle\langle1|_E\otimes S_{01}.
\]

Both are exact calibrated finite unitaries and generate authentic CPTP conjugation maps. The *same* gates and *same* \(\Phi_\mu\) admit physically distinct experimental schedules:

- **Schedule S0 (mandatory reset first):** \(\Phi_\mu\) acts before any \(W,F\) intervention. All flag-offdiagonal input coherence is erased by \(\Phi_\mu\) before the controls become accessible.
- **Schedule S1 (ports accessible before reset):** first \(W\), then \(F\), then the *same* compulsory \(\Phi_\mu\), and finally an ordinary quantum site-population measurement.

These two programs **do not differ in the original uncontrolled P3 source or signed residue**; they differ in the independently certifiable hardware clock/order specification. The distinction cannot be inferred from the unperturbed \(\Phi_\mu\) data alone.

## 2. H81.2 — genuine positive-state and *single-copy positive-POVM* witness

Define the Hermitian six-level *hidden flag-coherence* operator
\[
X=|0,0\rangle\langle1,0|+
  |1,0\rangle\langle0,0|,
\quad C_{\rm flag}(X)=0.
\]
Take the two fully positive normalized states
\[
\boxed{\rho_\pm=I_6/6\pm X/12>0.}
\]
Their eigenvalues are \(1/6\pm1/12\) on the nontrivial two-dimensional sector and \(1/6\) on the other four dimensions; no unphysical signed state probes are needed to witness the difference.

The initial flag observer cannot distinguish them:
\[
C_{\rm flag}(\rho_+)=C_{\rm flag}(\rho_-).
\]
The unchanged uncontrolled source also erases their distinction:
\[
\Phi_\mu(\rho_+)=\Phi_\mu(\rho_-),\qquad\Phi_\mu(X)=0.
\]
Hence for Schedule S0, **no sequence of later physical CPTP operations whatsoever can recover their earlier difference**.

In contrast, the **actual pre-reset** \(W\) converts the hidden flag offdiagonal coherence into opposite *flag population* terms:
\[
C_{\rm flag}\operatorname{Ad}_W(X)=
-\frac{24}{25}|0,0\rangle\langle0,0|
+\frac{24}{25}|1,0\rangle\langle1,0|.
\]
The subsequent genuine flag-conditioned SWAP \(F\) changes the latter from site 0 to site 1 **before the mandatory source reset**. As H75's reset depends on the visible marginal, the final physical state difference after the full Schedule S1 is exactly

\[
\boxed{
\Phi_\mu\operatorname{Ad}_F\operatorname{Ad}_W(\rho_+)
-\Phi_\mu\operatorname{Ad}_F\operatorname{Ad}_W(\rho_-)
=\frac4{25}\bigl[\Phi_\mu(|0\rangle\langle0|_E\otimes E_{11})
-\Phi_\mu(|0\rangle\langle0|_E\otimes E_{00})\bigr].}
\]

This difference survives the reset and is visible in the **ordinary physical positive site-2 POVM effect**
\[
Q_2=I_E\otimes E_{22}.
\]
Using the unchanged H42 unitary U, the measured population contrast is

\[
\boxed{
p_2(\rho_+;\mathrm{S1})-p_2(\rho_-;\mathrm{S1})
=\operatorname{Tr}\!\left[
Q_2\bigl(\Phi_\mu FW(\rho_+)-\Phi_\mu FW(\rho_-)\bigr)
\right]
=\frac4{75}>0.}
\]

Here \(FW(\rho)\) abbreviates the CPTP compositions of conjugations, not a new non-CP operator. Both probabilities lie strictly between zero and one. In Schedule S0, by contrast,

\[
\boxed{p_2(\rho_+;\mathrm{S0})-p_2(\rho_-;\mathrm{S0})=0}
\]

after **any** subsequent CPTP control/readout, since the same reset has already made the two full states identical.

Neither \(W\) alone nor \(F\) alone **before reset** makes this particular hidden-X distinction survive the source reset: exact code verifies
\(\Phi_\mu\operatorname{Ad}_W(X)=0=
\Phi_\mu\operatorname{Ad}_F(X)\).
The effect requires both resources **in the stated order**. This is a sharp physical **joint causal accessibility** example rather than mere algebraic speculation.

The controlled site-2 probability is a standard quantum-mechanical operational effect; it is NOT an experimental detection of P3's signed residue and NOT a CR-specific difference against matched standard QM. The two initial states and the devices have not been built or tested in a laboratory.

## 3. H81.3 — an additional genuine physical readout increases predictive rank

The fixed rank-18 flag observer provides 18 complex-linear microscopic output functionals. Add the single ordinary site-2 population functional at the end of the S1 sequence:

\[
\ell(X)=\operatorname{Tr}\!\left[
Q_2\,\Phi_\mu\operatorname{Ad}_F\operatorname{Ad}_W(X)\right].
\]

The positive state-pair witness above proves \(\ell\) is **not in the span of the 18 flag-block output coordinate functionals**, because its restriction to the hidden flag-offdiagonal kernel of \(C_{\rm flag}\) is nonzero. Hence

\[
\boxed{
\operatorname{rank}_{\mathbb C}(C_{\rm flag},\ell)=19
}
\]

on the full \(M_6\) microscopic input. The checker recomputes **all 36 microscopic matrix units** and obtains rank18 without \(\ell\), rank19 with \(\ell\), by exact Gaussian-rational elimination. This is a **physically certified single extra output probability** that makes one previously hidden direction observable, conditional on the actual pre-reset controls and state preparation being available.

The contrast does **not** contradict H79/H80: their exact rank-13, five-level quantum memory is **optimal on the restricted, already source-reset output family and with full post-reset quantum readout only at subsequent reset checkpoints**. The pair \(\rho_\pm\) and the distinguishing operation \(FW\) are **pre-reset controls on unrestricted six-level input states**, outside that narrower information/recovery task. H77/H78's larger memory ranks are equally schedule-dependent.

## 4. A precise minimal *type* of independent physical extra axiom: AX-OA (P11 candidate)

**AX-OA — Operational Accessibility Certificate.** A proposed microscopic quantum theory specifying an uncontrolled CPTP source \(\Phi\) must, before it can assert a unique physically realizable predictive observer, additionally provide an **independently physically justified** and finite-operationally meaningful tuple

\[
\boxed{
\mathfrak D_{\rm OA}=
\left(
\mathscr P,\ \mathscr U,\ \mathscr I,\ 
\mathscr S,\ \mathscr R
\right),
}
\]

with the following **typed contents**:

- \(\mathscr P\): certified input **preparation scope** (all quantum density operators, a quantum code, source-reset outputs, or another explicitly given physical set);
- \(\mathscr U\): actually switchable control **ports**, their finite microscopic Hamiltonian/Kraus realizations, calibrated parameter regions and physical uncertainties;
- \(\mathscr I\): allowed quantum **instruments** including state-change and conditionally accessible outcome branches, not just POVM probabilities;
- \(\mathscr S\): **causal and temporal scheduling** rules, including which operations may occur before/after an unavoidable source reset and which adaptive feedback accesses each outcome;
- \(\mathscr R\): physically accessible **readout data**, including the distinction between single-copy positive instruments, output quantum-block tomography on independent preparations, and post-hoc signed linear data reconstruction.

The precise mathematical output is the finite collection of **actual CPTP and CP trace-nonincreasing intervention maps** \(\mathscr T(\Phi,\mathfrak D_{\rm OA})\) on a **declared admissible preparation subspace** and its readout functionals. These maps must come from specified microscopic devices and are **not** assumed to be uniquely generated by \(\Phi\) or P3.

**Theorem (algebraic selection conditional on AX-OA).** For a specified *linear* output observer \(C\) and a specified finite-dimensional physically allowed intervention catalog \(\mathscr T=\{T_j\}\), a linear autonomous induced action on \(\operatorname{im} C\) for **every** allowed elementary map exists if and only if
\[
\boxed{
T_j(\ker C)\subseteq\ker C\quad\text{for all }j.
}
\]
When this holds, the unique induced linear map on the image is \(\widetilde T_j(CX)=C T_j X\). For exact prediction of all control histories but without a fixed C-kernel invariance, the **maximal future-indistinguishable hidden space** is
\[
K_*=\bigcap_{w\in\mathscr T^*}\ker(C T_w),
\]
and H77's finite descending kernel algorithm gives the optimal complex-linear predictive-record dimension \(\dim V-\dim K_*\).

**But:** neither the kernel criterion nor its minimal **linear** quotient **automatically produces a CPTP state encoding, CPTP extension of \(\widetilde T_j\), physically measurable recovery, or hardware implementation**. A physically realizable CP solution must supply an explicit CPTP recording channel \(\mathcal C\), actual CPTP output channels \(\widetilde T_j\), and positive instrument branches satisfying \(\mathcal C T_j=\widetilde T_j\mathcal C\) in the declared preparation/schedule scope. H75, H76, H79 and H80 gave distinct **conditional** examples; H81 does not convert the abstract AX-OA record into a guaranteed quantum memory.

**Incompleteness of uncontrolled source-only selection.** With exactly the **same** \(\Phi_\mu\) and every original-P3 residue datum, S0 and S1 differ only in \(\mathscr U,\mathscr S\) and lead to provably different readout probabilities for \(\rho_\pm\). Therefore there can be no **source-only algorithm** that universally selects the *actual* operational catalog or unique minimally sufficient observer for all experimentally distinct compatible devices without additional independent access data. Such a selector could exist **after** enriching the theory with independently established physical control-generation axioms, but that would not be a consequence of P3 data alone. This is a precise nonidentifiability theorem with an explicit physical counterexample, not a universal “no emergent controls” theorem.

**Foundational honesty:** AX-OA is the **minimal category of missing information**, not a proved uniquely minimal set of logically independent axioms. Specific stronger postulates may be reducible to each other in future P11 axiomatization. It is recommended as an **explicit assumption schema** for P11, not as an established consequence of \(F:\varnothing\to(\Lambda,\Omega)\).

## 5. P9 and P11 integration boundary

**Safe conditional input to P9 — GR-I.** H75–H80 give rigorous finite CPTP information/provenance *comparators*: a genuinely nonzero original-P3 residue on one conventional six-level open quantum source; autonomous quantum readout under a specified intervention catalog; a physically CPTP flag memory; and a sharp five-level/13-operator-dimension post-reset recovery theorem. H81 adds a single-copy device scheduling/provenance counterexample. These can support a precise **finite observer/control precondition** to any separately postulated geometric/soldering dynamics, and supply testable **ordinary QM** calibration experiments.

**Not safe as P9 Einstein evidence.** None of H75–H81 constructs a canonical microscopic KKS→ADM symplectic map on a nonuniform spatial field, the DeWitt indefinite kinetic pairing as a forced micro-invariant, an off-shell hypersurface deformation algebra on local densities, an induced Einstein–Hilbert variational principle, or Einstein equations from independently generated CR physical law. In particular finite memory-rank 5/13 and full control-observability rank36 **are not spacetime dimensions or gravity dynamics**. No physical CR-only discriminator has been derived.

**Safe conditional input to P11 — The Generative Map.** AX-OA provides a clean axiomatic *obligation*: a purported generator of observer/measurement/causality must specify or derive the physical intervention-accessibility data, including preparation, hardware ports, instruments, schedules and measurable readout, rather than inferring it from uncontrolled P3 quadratic residues. P11 may adopt AX-OA as an **independent declared axiom** or attempt a new explicit generating map \(\mathcal G_{\rm access}(F,\Phi,\cdots)\to\mathfrak D_{\rm OA}\) and prove its sufficiency/independent physical content. It may **not** claim either has already been derived. This is also consistent with the founder's question “why can the infinite close from the finite?”: the finite closure theorem is now exact **conditional on observable and accessible data**, but uniqueness or generative completeness from \(F\) remains an open foundational problem.

## 6. Research verdict and next program move (H82 or integration stop)

| Statement | Verdict |
|---|---|
| H80 sharp rank-13/5-level CPTP checkpoint memory | **92+1 = 93/93 CI PASS; retained** |
| Same P3 source with strictly different accessible controlled histories | **EXACT constructive positive-state / positive-POVM counterexample** |
| Pre-reset W→F→micro physically measured site2 population contrast | **EXACT \(4/75\)** |
| Reset before controls eliminates same state-pair contrast | **EXACT zero**, channel information loss |
| An additional controlled single-site readout raises fixed-observer linear rank | **EXACT 18→19** |
| Declared-catalog kernel criterion and maximal invariant hidden kernel | **Exact finite algebraic theorem**, H77 plus H81 |
| Unique control/observer catalog derived solely from unperturbed P3 | **NO**, underdetermination |
| AX-OA operational-accessibility assumption schema | **PROPOSED P11 AXIOM**, not proved generated |
| Full P3→frozen P6 actual \(\mathcal J_N\) physical provenance | **OPEN** |
| CR-exclusive operational observable / GR ADM-HDA / Einstein dynamics | **OPEN** |

**Recommendation:** **Do not** continue accumulating finite H-stages indefinitely after H81. One integration gate (H82 if required) should transmit the established finite CP/observer statements with exact assumptions to the running P9 GR-I / P11 F-axiomatization programs, classify every “port externally given” hypothesis, and then shift substantive proof effort to **independent physical generative provenance and geometric KKS–ADM/HDA constraints**, not more variations of the same quantum-memory rank. If new evidence of real P6 experimental control provenance appears, test the actual source-derived channel rather than append a convenient independent port.

**Reproducibility and integrity:** \`python3 P3/P9H81OperationalAccessibilityAxiomExactCheck.py\` uses exact Gaussian rationals and the **unchanged H75 original source**; checks full positive-state contrast under two causal schedules, all-operator kernel closure for a restricted physical CP observer, rank18→19, source and original nonzero P3 R3 identical. Stacked Draft/unmerged, frozen P1–P8/main untouched, no human referee/Lean kernel verification/lab experiment. The universal AX-OA impossibility statement is a logically scoped counterexample, not a claim of testing every physical quantum model.
