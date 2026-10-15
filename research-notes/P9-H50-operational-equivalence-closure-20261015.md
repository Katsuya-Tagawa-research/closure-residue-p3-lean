# H50 — Operational Equivalence and the Exact No-CR-Only-Discriminator Boundary in the Standard Finite CPTP Sector

**2026-10-15 | P3–P11 Mathematical Bridge | stacked on H49 Draft PR #68.**

## Verdict in one sentence

In the exact H35–H49 **standard finite CPTP/GKSL comparator sector**, an original-P3 quadratic residue, a static source label or a conditionally selected collective tangent does **not by itself** generate a novel quantum-outcome law if the **complete accessible controlled process and CP instruments** are unchanged. This is a precise **conditional sector no-discriminator theorem**, NOT an impossibility theorem for every conceivable closure–residue model. Physical microscopic P3/P4→P6 provenance and P9 GR/Einstein dynamics remain unproved. All claimed numerical identities are rational finite-dimensional calculations; no human review, new Lean kernel theorem, hardware data or rewritten frozen papers.

## 1. Formal theorem: operational equivalence under matched full Markovian instruments

Let \(\mathcal H\) be a finite-dimensional system Hilbert space, \(X\) its density operators, and \(\mathsf A\) an allowed set of control choices. Let \(\rho_0\) be a fixed initial density, \(\Psi_a:\mathcal B(\mathcal H)\to\mathcal B(\mathcal H)\) CPTP controlled updates for each \(a\in\mathsf A\), and \(\{\mathcal I_{\omega}^{(a)}\}_\omega\) a chosen outcome-resolved CP trace-nonincreasing instrument, with \(\sum_\omega\mathcal I_\omega^{(a)}\) CPTP. A finite adaptive experiment chooses its next \(a_k\) as an arbitrary predetermined function of the **previous classical observed outcomes** \(\omega_1,\dots,\omega_{k-1}\), and may perform legitimate (specified) classical postprocessing of the resulting records.

**Theorem H50.1 — finite adaptive operational-equivalence lemma.** If two theoretical descriptions have **the same initial density \(\rho_0\)**, **the same full controlled CPTP updates \(\Psi_a\)** for every permitted \(a\), and **the same CP instrument branches \(\mathcal I_\omega^{(a)}\)** for every permitted measurement (including any permitted state preparations, interventions, ancillary systems and feedback protocols), then for **every** finite adaptive protocol they predict identical joint distributions of classical outcomes and identical unnormalized conditional quantum output matrices for every labelled branch.

**Proof (finite induction).** For an outcome word \(\boldsymbol\omega=(\omega_1,\ldots,\omega_n)\), its unnormalized conditional state is the composition
\[
\widetilde\rho_{\boldsymbol\omega}
=\mathcal I_{\omega_n}^{(a_n)}\Psi_{a_n}
\cdots\mathcal I_{\omega_1}^{(a_1)}\Psi_{a_1}(\rho_0).
\]
Each \(a_j\) is the same deterministic function of the preceding identical labels, and every composed linear CP map is identical by premise. Therefore the two unnormalized matrices, their traces (joint probabilities), their conditional normalized states whenever probability is positive, and all postprocessed outcome laws coincide at arbitrary finite depth. No CR- or conventional-QM-specific assumption enters this elementary composition argument.

**Scope guard — critically important:** Matching only the *uncontrolled* CPTP map \(\Phi\), aggregate norm, center-population calibration, or even each *fresh one-step reduced channel* is **NOT** enough when a hidden environment retains inter-time correlations. Equality must be at the level of the **entire relevant controlled, instrument-conditioned multi-time process** (or an actually established common Markov CPTP composition). This theorem does not assume arbitrary non-Markovian processes factor into their reduced single-time maps.

Thus if a proposed CR description simply computes the **same** \((\rho_0,\{\Psi_a\},\{\mathcal I_\omega\})\) as the best same-calibration standard quantum model, it cannot predict an additional operationally observable event in that scope, no matter how different its interpretation of P3 hidden dynamics, microscopic static-sector names or generating ontology.

## 2. Exactly checked 144-branch two-step adaptive process with genuine CP instruments

Use **unchanged** H42 rational microscopic \(U\in U(3)\), \(\Phi=\mathrm{Ad}_U\); **unchanged** H46 twelve-outcome instrument
\[
\mathcal I_{k,t}(\rho)=\frac12D_kP^t\rho P^tD_k^\dagger,
\quad k=0,\ldots,5,\quad t\in\{0,1\},
\]
and the P6 real exchange carrier \(K(a,b)=aA+bB\). To avoid pretending a rational polynomial equals an exact finite-time exponential, use the separately declared **bona fide finite orthogonal Cayley control gates**
\[
Q_h(K)=(I+hK)(I-hK)^{-1}
=I+\frac{2h}{1+h^2r^2}K
+\frac{2h^2}{1+h^2r^2}K^2,\quad r^2=a^2+b^2,
\]
for rational \(h>0\) and three predeclared real controls:
\[
(a,b)_{\rm locked}=(3/5,3/5),\quad
(a,b)_{\rm unlocked}=(3/25,21/25),\quad
(a,b)_{\rm opposite}=(3/5,-3/5).
\]
All have \(r^2=18/25\). A single microscopic controlled update is the CPTP map \(\widetilde\Psi_h^K=\mathrm{Ad}_{Q_h(K)}\circ\Phi\).

**Explicit adaptive protocol:** apply \(h_1=1/4\), locked K and the first 12-outcome H46 instrument; conditional on first outcome \((k,t)\), choose second control type \((k+2t)\bmod3\) and second rational gate duration \(h_2=1/4\) or \(1/5\) depending on \(t\); finally apply the second 12-outcome H46 instrument. There are **144 distinct second-stage labelled branches**.

The exact Gaussian-Fraction verifier computes every branch independently by (i) sequentially applying the two CP instrument maps and two controlled CPTP maps and (ii) building the **single composite Kraus operator** for the same branch:
\[
B_{\alpha\beta}
=D_\beta P^{t_\beta} Q_{h_2}(K_\alpha)\,U\,
D_\alpha P^{t_\alpha}Q_{h_1}(K_{\rm locked})\,U.
\]
The branch output is
\[
\boxed{\widetilde\rho_{\alpha\beta}
=\tfrac14 B_{\alpha\beta}\rho_0B_{\alpha\beta}^\dagger.}
\]
Every branch matches EXACTLY between these independently factored computations. All matrices are positive by Kraus form and sum to trace one over all 144 branches for each tested physical initial density. This is a concrete exact finite-depth verification of the universally proved induction lemma, not a proof by finite enumeration alone.

**Invasive warning:** the intermediate H46 instrument genuinely modifies the physical trajectory. These 144-branch processes are **not** silently equated with untouched \(\Phi^2(\rho_0)\). H49 showed an exact \(32/81\) difference in center population in its specific no-insertion versus insertion comparison.

## 3. Strict conditional P6 selection is a PROPER submodel of ordinary CPTP

The H41/H47 *conditional* collective-source hypothesis declares
\[
J_{\rm col}=\operatorname{span}_{\mathbb C}
\{T,T^\dagger\},\quad T=E_{01}+E_{21},
\quad \Xi(J_{\rm col})\cap W=\mathbb R(A+B),
\]
so an **independently justified physical source-to-control provenance axiom** forces \(a=b\) for the allowed one-real-knob exchange. The ordinary standard CPTP comparison set with the **same** calibrated graph and \(r^2=18/25\) admits **both** this locked control and unlocked controls. Hence
\[
\boxed{
\mathfrak M_{\mathrm{collective,\ conditional}}(A)
\subsetneq
\mathfrak M_{\mathrm{standard\ CPTP}}(A),
}
\]
when Dataset A includes the norm and graph but not the relative split. This proper **model-class restriction** can be falsified by held-out data, but is NOT a claim of observable probabilities outside the standard CPTP prediction set. Its microscopic P3/P4 derivation is still missing (H42 No-Go).

A new exact rational positive-Cayley witness for an endpoint H46 **classical signed flag** uses the *center seed directly*, where \(h=1/4\), \(r^2=18/25\). The Cayley gate acts on the centered vector with real amplitudes
\[
Q_h(K)|1\rangle=f a|0\rangle+c|1\rangle+f b|2\rangle,\qquad
f=\frac{100}{209},\quad c=\frac{191}{209}.
\]
Then center-site survival \(p_1=c^2\) is **exactly the same** across locked, unlocked and opposite-sign controls, but
\[
\boxed{
\mathbb E_{\rm locked}Z=0,\quad
\mathbb E_{\rm unlocked}Z=-\frac{3456}{43681}\ne0,\quad
\mathbb E_{\rm opposite}Z=0.
}
\]
This is ordinary finite quantum mechanics. The opposite-sign tangent \(a=-b\) is **outside** the oriented collective \(\Xi(J_{\rm col})\) but gives the **same entire H46 classical outcome-frequency vector** as the locked tangent for this direct center-seed Cayley experiment (since the probabilities depend on populations, which depend on \(a^2,b^2\)); the *conditional quantum output states* differ because their coherences carry opposite signs. Therefore a **classical null** does not establish oriented microscopic provenance.

When Dataset A includes independent quantum-coherent controlled-process tomography of both physical signed amplitudes \(a,b\) (H48/H49), standard CPTP makes the same conditional prediction as the selected CR submodel. The putative “CR versus standard QM” statistical difference **collapses** under that complete relevant calibration. A null may be consistent with collective provenance; it cannot demonstrate why the control was selected.

## 4. Separate No-Go: equality of fresh one-step reduced CPTP maps does not imply multi-time equivalence

Use an ordinary **standard quantum + classical hidden environment** toy model on \(M_3\) with diagonal phase \(P_-= \operatorname{diag}(-1,1,1)\). Suppose the fresh single-step reduced channel is
\[
\mathcal D(\rho)=\tfrac12(\rho+P_-\rho P_-).
\]
Two physically legitimate stochastic implementations share exactly this fresh reduced map:

1. **Correlated hidden sign:** sample \(\sigma\in\{0,1\}\) once with equal probabilities, and apply the SAME \(P_-^\sigma\) at both steps. Since \(P_-^2=I\), the unconditioned two-step channel is **identity**.
2. **Independent hidden sign:** sample a new \(\sigma\) at each step, giving \(\mathcal D^2=\mathcal D\) at two steps.

For the positive coherent density
\[
\rho_+=\tfrac12(|0\rangle+|1\rangle)(\langle0|+\langle1|),
\]
the two-step 01 coherence is \(1/2\) in the correlated implementation and zero in the independent implementation. Thus
\[
\boxed{\mathcal D_{\mathrm{one\ step}}^{\mathrm{corr}}
=\mathcal D_{\mathrm{one\ step}}^{\mathrm{iid}},
\quad
\mathcal P^{(2)}_{\mathrm{corr}}\ne
\mathcal P^{(2)}_{\mathrm{iid}}.}
\]
This is **ordinary** quantum non-Markovian process-memory physics, conceptually related to P3 observation/closure but neither a novel CR signal nor identical with original P3 \(\mathcal R_k\). It prevents an overly broad "matching a one-step map implies no discriminator" claim.

## 5. Final H50 research boundary: what exactly has (and has not) been obtained

**PASS mathematical theorem:** complete-process/CP-instrument equality implies all finite adaptive operational equivalence; nontrivial 144-branch rational CPTP/Kraus verification; true proper conditional collective selection submodel; exact norm-matched Cayley zero-vs-nonzero odd-flag comparator and opposite-sign false-positive null; explicit standard non-Markovian counterexample when **only fresh one-step reduced CPTP** maps match.

**FAIL overclaim:** the mere existence of an original P3 quadratic residue or static collective metadata ⇒ a CR-only quantum signal different from matched standard QM in the H35–H49 finite standard-CPTP sector. A successful original P3 quadratic-residue or instrument readout is reproducible by standard quantum dynamics unless the **controlled process prediction itself** acquires an independently derived distinct constraint.

**OPEN:** microscopic derivation of frozen P6 \(\mathcal J_N\), star-compatible physical tangent provenance, hardware realization and independent calibration of extra coherent instruments, an actual experiment, universal original-P3 quadratic-residue sufficient sector for arbitrary states, P9 ADM/HDA/EH/Einstein dynamics and P11 generative completeness. H50 does not rule out additional genuinely independent future constraints; it marks exactly which ones cannot be claimed on present evidence.

**H51 proposed — handoff/freeze gate:** consolidate H35–H50 into an explicit **Proven / Conditional / Refuted / Open** research bridge dossier and formulate P9's next required *gravity-specific* assumption ledger (metric/hyperbolicity, field variation, Bianchi/covariant conservation, Einstein–Hilbert action or HDA), rather than continuing to call standard GKSL control tomography CR-only. Alternatively, formalize Theorem H50.1 at the abstract finite CPTP/instrument-composition level in Lean, keeping mathematical proof distinct from human journal referee approval.

## Exact reproducibility and GitHub boundaries

`P3/P9H50OperationalEquivalenceClosureExactCheck.py` uses exact Fraction/Gaussian rationals, unchanged H42 \(U\), H46 Kraus blocks, and H49 controlled Cayley gates. It checks all 144 joint outcomes for each of three genuine density preparations; the full source \(J_{\rm col}\) rank and H42 failure of its automatic original-P3 inheritance; the proper norm-matched conditional comparison; and the standard non-Markovian phase-sign counterexample. CI dedicated in stacked Draft PR; nothing was merged or used to alter frozen source papers.