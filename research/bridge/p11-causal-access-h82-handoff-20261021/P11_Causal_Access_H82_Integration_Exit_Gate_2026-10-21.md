# H82-compatible P11 Finite Causal-Prediction Certificate — Integration and Exit Gate

**2026-10-21 | P3–P11 Mathematical Bridge / P11 handoff**
**Status:** Stacked Draft on PR #183; CONDITIONAL FINITE-MATHEMATICAL HANDOFF CANDIDATE, **not** H82 amendment, not F Generative Completeness, not a physical P6 certificate.
**Reference:** H82 — Integration Audit and P9/P11 Handoff, Notion https://app.notion.com/p/3fd736b71e2d8198a5d0f4a3260064c8?pvs=204 . H82's Draft PR #101 stays independent. OA-G39–G42 *Uniform History-Tail Certificate* audit branch remains **UNNUMBERED** and UNMERGED; no H number is assigned in this package.

## 1. Precisely stated finite causal-prediction theorem

Let the **externally declared** finite operational grammar have (a) a finite real state carrier V (for ordinary quantum inputs, Herm(H)), (b) a finite classical-controller state set C, (c) a **finite set of CP trace-nonincreasing branch superoperators**, chosen via a specified legal scheduling/feedback automaton, and (d) a finite set of terminal effects. The controller must be included in the carrier or fixed as an explicit known input. Illegal operation words are excluded, either by defining admissibility in the program grammar, or by adjoining the finite controller to the linear carrier.

Form the combined finite real carrier
\[
\widehat V=\bigoplus_{c\in C}\mathrm{Herm}(\mathcal H)
\]
for a classical controller. Each legal branch transition is a linear CP TNI map on this carrier, with terminal positive linear readout functionals R. Define the ascending Heisenberg span
\[
\mathcal R_0=\mathrm{span}_{\mathbb R}(\text{legal terminal effects}),\qquad
\mathcal R_{n+1}=\mathcal R_n+\sum_{g\in \mathcal G}g^*(\mathcal R_n).
\]
Here \(\mathcal G\) is a **finite transition alphabet respecting legality** (it may contain controller-state-conditioned branch maps). For a fixed restricted classical-controller initial value, one may equivalently work on the corresponding reached sector, but must not silently identify its rank with the full-controller rank.

**Finite causal-predictive quotient theorem (EXACT finite linear algebra):**
1. The ascending chain stabilizes after finitely many strict rank jumps, no more than \(\dim_{\mathbb R}\widehat V-\dim\mathcal R_0\). If \(\mathcal R_{n+1}=\mathcal R_n\), it is invariant under every permitted adjoint generator, so \(\mathcal R_\infty=\mathcal R_n\).
2. Every finite legal experiment-word probability (including the complete **classically labelled branch history** when the labels are read and conditions obey the grammar) is a linear functional from \(\mathcal R_\infty\). Indeed the effect of a word w followed by terminal effect E is \(g_w^*(E)\in\mathcal R_\infty\). The probability of a specified branch-record prefix terminating without an explicit readout is \(g_w^*(I)\); I belongs to \(\mathcal R_0\) when the legal terminal POVM is complete. Summation over branch labels preserves membership.
3. Define \(\mathcal K_\infty=\mathcal R_\infty^\perp\) for the trace pairing. The linear quotient \(\widehat V/\mathcal K_\infty\) is the **canonical minimal sufficient linear carrier** for **exact finite-word probability prediction under this fixed grammar**. A surjective *linear* encoding q into Z predicts every word iff \(\ker q\subseteq\mathcal K_\infty\); hence \(\dim Z\ge\dim\mathcal R_\infty\). Equality identifies the quotient up to a compatible linear isomorphism.
4. This is **NOT** a claim that q is completely positive, that a quotient algebra/Hilbert-space realization exists, that the quotient inherits a legitimate CP action under arbitrary future context, or that an online apparatus with dimension rank R exists. The CP realization in the hypotheses is on the **original physical state + controller carrier**. A separately supplied CPTP encoding/recovery problem has independent constraints.

## 2. A uniform-tail theorem for legal, possibly adaptive no-event policies

Assume the legal no-event program consists of mandatory cycles; in each cycle, a policy (depending on the permitted classical record) selects one of a **finite specified family of CP TNI no-event maps** \(\mathcal N_c\), and events terminate the current event-time waiting run. Suppose
\[
\boxed{\forall c\text{ permitted},\quad \mathcal N_c^*(I)\preceq b I,\quad 0\le b<1.}
\tag{UT-1}
\]
If a classical controller is present and choices are sector-dependent, use its block identity and check the same condition on the augmented legal carrier. Then by CP order preservation and induction, for every initial density state and **every legal adaptive policy** selecting one of those maps at each surviving cycle:
\[
\boxed{s_\pi(K)=\Pr_\pi(\text{survive K no-event cycles})\le b^K.}
\tag{UT-2}
\]
This establishes the **common cutoff** condition from OA-G42 for this explicitly specified policy class. The bound is uniform over legal policies and initial states, but **NOT** over other sources/instruments that lack the same bound, nor over schedules allowed to idle without consuming a mandatory cycle. There is no claim of a source-only spectral gap implication.

For any loss \(f\) of complete event histories satisfying \(0\le f\le1\), define the truncated history estimate by retaining the exact contributions from terminal event times \(k\le K\) and dropping all event histories with survival beyond K. Its absolute expectation error is at most \(s_\pi(K)\le b^K\). Equivalently, one may store an **overflow marker** for event times beyond K, in which case all coarse-grained probabilities (k<=K plus overflow) can be represented **exactly**. The number of archive outcomes is then K+1 (times 1,...,K and overflow); storing k exactly without an overflow label uses a different coding objective, and a dimensional lower bound on exact/approximate quantum archive storage is a separate theorem (OA-G40/G41).

For b in (0,1), a sufficient worst-case truncation horizon is
\[
K=\left\lceil\frac{\log\varepsilon}{\log b}\right\rceil .
\]
For b=0, one consumed no-event cycle gives zero survival.

**Block generalization:** a common all-legal-word ell-step dual bound \(\mathcal N_w^*(I)\preceq bI\) for each actual legal ell-step no-event word gives \(b^{\lfloor K/\ell\rfloor}\) if every legal long word decomposes into such admissible blocks. One-step individual bounds are stronger and sufficient under arbitrary switching. Per-instrument *own* ell-step bounds are NOT sufficient under arbitrary switching (#182 two-state alternating NO-GO).

## 3. Original-H75 concrete certificate — exactly what is proved

The H75 source \(\Phi_\mu\) is the **unchanged original four-Kraus six-level CPTP channel**. The proven finite **physical CP realization** uses separately *furnished* selective Instrument A/B (three outcomes each), the originally registered real conditional flag-site SWAP on result 0, an externally authorized classical A/B control bit, reuse of the same memoryless source and original site readout.

- The **actual six-level-source future Heisenberg grammar without an additional controller register** (source, site dephasing, and six selectively-labelled feedback CP branch maps A_j/B_j) has exact rank sequence \((3,7,10,12,12)\). Hence a **12-dimensional real predictive quotient on Herm(6)** and a 24D linear kernel. A fixed supplied controller state may select legal words from this alphabet; this rank12 is **not** silently the full controller-plus-system quotient rank.
- On the actual 9D source-output image, the response rank is 9; no erased full-state input information is resurrected.
- Full source+Instrument A and source+Instrument B no-event CP cycles each have genuine Kraus realizations and event complements. **Distinct, independently authorized** selective branch instruments share one nonselective CPTP dephasing map.
- In the original H75 model, the exact finite dual bounds are \(\mathcal N_A^*(I_6)\preceq(5/6)I_6\) and \(\mathcal N_B^*(I_6)\preceq(1/2)I_6\), so UT-1 holds with **common b=5/6 for every legally switched A/B cycle**.
- A separately imported 2-state classical parity controller has an explicit 12-level block-diagonal CP Kraus implementation, without claiming to store all past event times.
- For \(\varepsilon=1/100\), exact arithmetic confirms \((5/6)^{25}>1/100\ge (5/6)^{26}\). **K=26** is sufficient for the declared worst-case uniform event-history truncation (not the minimal archive Hilbert dimension, not a unique optimal cutoff under every initial state).

The exact regression in this stacked PR **reruns the two source-specific prior H75 checkers from #182 and #183**; a new independent checker audits finite causal-prefix effects, the 26-step rational bound, and the sufficiency of the declared cut-off across the two legal branch policies.

## 4. Classification required by H82 (claims / independent assumptions / F-origin obligations)

### A. What is established as FINITE CONDITIONAL MATHEMATICS
- Canonical **linear** future-observer quotient and finite stabilization for **fixed finite legal grammars**; H82 rank=dim(W/K) comparison and rank/scope caveats preserved.
- Original-H75 exact CP instrument and 2-branch adaptive event dynamics, including the 12D input-side future effect span on the 6-level cut and the 9D source-output-restricted observability.
- Exact joint, schedule-uniform no-event tail for the two designated A/B cycles, with a rigorous 1% cutoff and corresponding bounded-test expectation error.
- Exact NO-GOs: original source alone does not select hardware-faithful AX-OA catalogs; labels/instruments matter despite equal averaged CPTP; future shallow observational equivalence is not necessarily stable under future allowed interventions; arbitrary switching defeats unrelated per-instrument multistep extinction; full H75 erased source-kernel differences remain irrecoverable.

### B. Independent access / physical / structural assumptions REQUIRED
- H75 source chosen and physically implemented, with validated CPTP Kraus model and all relevant source and reset timings.
- *Physical authorization* of preparation states, flag and site coherent controls, selective A/B instruments, real branch-outcome classical record and feed-forward, terminal POVMs, and any calibrated clock/scheduling rule.
- Reusing exactly the **same ideal memoryless source**, with no inaccessible retained correlations or unauthorized side channels; limiting allowed policies to A/B cycles and stopping on events.
- The target notion of approximation: event-time probability tail/worst-case bounded loss, not exact full history archive or arbitrary online CP compression.
- Additional physical P6 provenance, native observer encoding, calibrated Xi/J_N sectors and relevant locality conditions, if any microscopic relation is claimed.
- Any desired CP encoding/recovery of the mathematically minimal linear quotient requires a new independently validated map (not supplied by the quotient).

### C. Open P11 F-GENERATION PROOF OBLIGATIONS (and P9 gates)
- Construct \(\operatorname{GenAcc}_F\) from **genuinely prior** F axioms, yielding a typed access certificate or a rigorously specified *set-valued family*; no use of desired source/device hardware as hidden premises.
- Check existence, type validity, CP realization, schedule legality, observer/source symmetry equivariance, operational equivalence/gauge invariance and actual hardware-faithful selection. Original-H75 source-fibre no-selection means source-only F cannot select differing actual operational classes **without additional distinguishing input or law**.
- Prove any claimed **uniform** bound over **F-generated families**, not merely the fixed H75 example; OA-G42's common-cutoff criterion is essential. No inference from source spectral gap alone.
- Either prove or explicitly retain AX-OA as independent axioms; five-port *componentwise* sensitivity (#177) does NOT prove their logical independence or unique minimality, and one-use behavioral normal forms (#178) do not identify their physical implementations.
- Establish any *separate* P6 physical signed hidden-current provenance/phase reference and CP intertwiner, P7/P8 geometric soldering, original KKS GT–K4 native metric descent gate, ADM/DeWitt/off-shell HDA/Einstein dynamics for P9; P11 Generative Completeness and P12 generality remain OPEN. No circular use of an anticipated P11 result to justify P9.

## 5. Bridge exit contract — NOT a declaration that P11 is finished

**Finite-mathematical exit candidate:** exact source-specific checkers plus stated finite general factorization/closure/CP-order proofs, reproducible CI and clearly bounded scope; a handoff that P11 can accept without interpreting the typed access ports as generated.

**Before declaring this bridge closed:** confirm stacked Draft CI all PASS (not just dedicated check), ensure independent unnumbered OA-G39–G42 audit remains separate until governed import, reconcile with H82 Notion ledger (no rewrite of H82 Draft #101 without its explicit review), and deliver the three-column classification to P11 and the limited P9 acceptance gate. No merging, H numbering or manuscript rewrites in this PR.

**P11 deliverable:** a typed relative finite causal-prediction certificate, counterexamples and the exact list of generative duties.
**P9 deliverable:** finite CP conditional mathematics and apparatus/provenance/geometry-dynamics exclusions. No CR-exclusive physical witness, spacetime geometry or Einstein action is inferred.

**CI and review boundaries:** exact SymPy computation is finite regression, not universal theorem formalization in Lean; all physical apparatus and all generative claims need independent proof or experiment; no human peer review is claimed. PRs remain Draft/unmerged.
