# H111 — Infinite Fresh-Ancilla Collision Chain, Correlated Kraus Histories and a Markovian Reduced Process: A Source-Exact H75 / P5 / P9 / P11 Handoff

**2026-10-19 | P3–P11 Mathematical Bridge / P5 History–Ω / P9 GR-I / P11 AX-SRC, AX-OA, AX-CAN, AX-SP, AX-GEN**

**Inherit H110 Draft PR #129: ALL 123/123 GitHub Actions PASS**, original unchanged H75 six-level four-Kraus CPTP source with signed nonzero P3 R3, existing native real coherent A/B controls, positive flag/site observers. Main and frozen published P1–P8 remain unchanged, as do the independently specified P9.126–127 sixteen-level and P9.128 forty-eight-level unitary sources. No new physical Hamiltonian or fictitious Cartan soldering is postulated at H111.

## 1. Exactly what can a fresh-collision realization accomplish?

The TRUE unchanged H75 reset map on \(\mathcal H_S=\mathbb C_E^2\otimes\mathbb C_{\rm site}^3\) is
\[
\Phi(X)=\sum_{a,b=0}^1L_{ab}XL_{ab}^\dagger,\qquad
L_{ab}=|a\rangle\langle b|_{\rm flag}\otimes U M_a,\quad
M_0=\operatorname{diag}(1,3/5,3/5),\ M_1=\operatorname{diag}(0,4/5,4/5).
\]
The two indices \((a,b)\) explicitly record **output and incoming flag**, respectively; the existing original H75 flags and signed P3 residual are not rewritten by this environment notation. H110 proved exactly \(\sum L_{ab}^\dagger L_{ab}=I_6\), Choi/Kraus rank FOUR and the minimal pure single-step environmental dimension FOUR. For \(\mathcal H_e=\mathbb C^4\), the isometry
\[
\mathcal V|\psi\rangle=\sum_{a,b}L_{ab}|\psi\rangle\otimes|ab\rangle
\]
extends to a 24×24 unitary \(W\) on system×one collision ancilla by orthonormal column completion. The unitary extension is **not physically selected or accessible by the source** simply because a mathematical extension exists.

## 2. H111.1 — One autonomous UNITARY on a COUNTABLY INFINITE fresh environment realizes ALL H75 iterates (EXACT conditional existence)

Let \(\mathfrak E=\bigotimes_{j\in\mathbb Z}^{|0\rangle}\mathbb C^4_j\) denote the **incomplete infinite tensor product with reference vector \(|0\rangle_j\)**. It has a well-defined separable finite-excitation completion, and the bilateral shift \(\mathcal S\), moving each environment tensor factor at site \(j+1\) into site \(j\), is a unitary because it preserves the reference product vector.

Fix the ONE-STEP 24D extension \(W_{S,0}\) above (identity on every other ancilla), and define **one fixed unitary** on the *fixed but infinite* system+environment Hilbert space
\[
\boxed{\mathscr U=(I_S\otimes\mathcal S)\,W_{S,0}.}
\tag{H111-SHIFT}
\]
Initially all ancillas are in the reference state \(|0\rangle\). After each collision and shift, site \(0\) contains a **fresh uncorrelated ancilla** from the formerly positive-index part of the chain, while used quantum records move to negative sites and never interact with the system again. Thus **for every integer \(n\ge0\)** and all six-level operators \(X\),
\[
\boxed{
\operatorname{Tr}_{\mathfrak E}\left[
\mathscr U^n\left(X\otimes|\mathrm{vac}\rangle\langle\mathrm{vac}|\right)(\mathscr U^\dagger)^n
\right]=\Phi^n(X).}
\tag{H111-ALL-TIME}
\]
For any finite n this is the EXACT Kraus-word formula H110 verified, with the same \(4^n\) **SUFFICIENT** finite-history label Hilbert space. General n follows by induction: the next collision touches only a fresh reference ancilla and previously used ancillas are spectators.

**Important H110 comparison:** H110 forbids a fixed finite-dimensional *closed* bath and a single fixed unitary to realize **all** H75 resets because of finite-dimensional recurrence versus primitive mixing. H111 shows this obstruction is **sharp in environmental finiteness**: replacing the closed bath by a fixed, infinite, freshly supplied chain removes that finite-dimensional recurrence obstruction. H111 does **NOT** demonstrate a physical Hamiltonian logarithm with the correct locality/energy-boundedness or an experimentally sourced infinite reservoir. The discrete shift/collision clock is an **independent external temporal scaffold**, not a P1/P5/F derivation of time.

## 3. H111.2 — Genuine consecutive quantum environment RECORDS are correlated despite exactly Markovian system dynamics (EXACT source-positive finite witness)

Use a real, source-positive physical six-level preparation
\[
\rho_{\rm in}=|{\rm flag}=0,\,{\rm site}=1\rangle
\langle{\rm flag}=0,\,{\rm site}=1|.
\]
The first collision's genuine original four Kraus **environment label** \((a_1,b_1)\) has
\[
\boxed{\Pr(a_1=0,b_1=0)=9/25,\qquad
\Pr(a_1=1,b_1=0)=16/25}
\tag{H111-FIRST}
\]
and the other two first-label outcomes vanish exactly. At the next collision, the operator \(L_{a_2b_2}\) contains the input-flag projector \(\langle b_2|\), while the first collision has put the flag at \(|a_1\rangle\). Therefore for **every nonzero original Kraus trajectory**
\[
\boxed{b_2=a_1.}
\tag{H111-RECORD}
\]
In particular for classical projective measurements of these two orthogonal outgoing environmental label registers,
\[
\begin{aligned}
\Pr(a_1=0)&=\Pr(b_2=0)=9/25,\\
\Pr(a_1=0,b_2=0)&=9/25,\\
\boxed{\operatorname{Cov}(\mathbf1_{\{a_1=0\}},\mathbf1_{\{b_2=0\}})
=144/625>0.}
\end{aligned}
\tag{H111-CORR}
\]
Their classical mutual information is exactly \(h_2(9/25)>0\) bits, where \(h_2(p)=-p\log_2p-(1-p)\log_2(1-p)\). The exact Gaussian-rational checker verifies the full **16-entry two-record joint probability table** (not just the above marginals), its positivity/normalization and the hard support rule \(b_2=a_1\).

These record labels belong to *fresh ancillary Hilbert spaces* in the mathematical dilation. Measuring them would be an additional laboratory permission; mere existence of their record-space basis in Stinespring theory does not certify experimental accessibility. Stronger entanglement between quantum environment registers is NOT implied merely by this positive **classical joint outcome covariance**.

## 4. H111.3 — In spite of this correlated history, the system's controlled process has NO past-to-future memory across a fresh collision (EXACT source category)

For every quantum operation \(\mathcal A\) inserted **on the system** between the first and second collisions, linearity and independence of the next input ancilla give
\[
\boxed{
\mathcal T_{2:0}[\mathcal A](X)
=\sum_{k_1,k_2}L_{k_2}\,\mathcal A(L_{k_1}XL_{k_1}^\dagger)\,L_{k_2}^\dagger
=\Phi\circ\mathcal A\circ\Phi(X).}
\tag{H111-COMPOSITION}
\]
Likewise arbitrary intervention sequences yield
\[
\Phi\circ\mathcal A_{n-1}\circ\Phi\circ\cdots\circ\mathcal A_1\circ\Phi.
\]
Even in the presence of classical correlations between successive **past environmental records**, the next collision channel is precisely the SAME \(\Phi\) for every physically accessible current state and *does not query previous outgoing ancillas*. This is a **quantum-Markov fresh-collision process in the system-level operational process-tensor sense**. It is *not* a demonstration of an observable non-Markovian P5/Ω effect; indeed it is a counterexample to equating *history-storage/correlation* with *memory feedback*.

The exact checker verifies (H111-COMPOSITION) on all **36 original six-level matrix units** for a chosen genuine original-H75 local real-B coherent Cayley operation and a genuine positive flag measurement instrument (trace-nonincreasing CP), as well as the unconditional identity for all source inputs. This computational audit of two representative interventions is supplemented by the algebraic proof for **arbitrary** linear system operations \(\mathcal A\), which uses only the true Kraus sums and the tensor-product fresh ancilla input.

**Context caveat:** An experimenter who **conditions on past environment measurement outcomes** can of course have a history-dependent *state of knowledge* or may implement feedback based on records. This is not intrinsic environment-to-system memory, and any feedback gate or reusing a spent ancilla changes the model category. Similarly, observing only a restricted subsystem of the six-level source can require a separate operational Markov check; the stated property is for **the full six-level H75 system** with unrestricted system-side interventions and fresh independent ancillas.

## 5. H111.4 — AX-SRC / P5 Ω / P9 Cartan and P11 generative gates

| Claim | Scope and verdict |
|---|---|
| H75 one-step pure ancilla dimension four, Choi rank four | **EXACT** from H110 |
| For every finite n, fresh independent ancillas reproduce H75^n | **EXACT conditional** supply, H110 |
| ONE fixed infinite-chain bilateral-shift collision unitary reproduces ALL n | **EXACT mathematical existence** under countably infinite prepared chain |
| ONE fixed finite closed memory reproduces ALL n with no reset | **NO-GO**, H110 finite recurrence |
| Outgoing consecutive true H75 environment record registers are classically independent | **FALSE**, explicit covariance \(144/625\) |
| Full H75 fresh-collision controlled process is non-Markovian | **FALSE**, exact intervention factorization |
| Source-generated infinity, time, bath preparation and persistent non-Markov P5 Ω | **OPEN** |
| Actual P9.126–128 Cartan Hamiltonian = generated infinite-chain H75 unitary | **NOT SHOWN**: P9 finite 16D/48D source and distinct observer |
| Generated symplectic ADM six pairs, physical solder/curvature, Einstein action and F completeness | **OPEN** |

**Minimal noncircular requirements**: (AX-SRC) physical reservoir **and its repeated preparation/shift/collision law** derived or separately calibrated; (AX-OA) a stated observer-and-intervention category distinguishing recorded past from operational conditional future, including what is actually measurable; (AX-CAN) coherent physically accessible Hamiltonians preserving a nondegenerate KKS sector rather than an arbitrary Stinespring workspace; (AX-SP) common-source physical intercell adjacency, transport, sourced solder and Cartan torsion/curvature law; (AX-DYN/NORM) DeWitt+R curvature action, full offshell HDA and physical scale; (AX-GEN) a genuine axiom-of-F theorem creating the required reservoir/field structures, rather than an imported countably infinite tensor product.

**Stop decision:** H111 is an **exact positive construction AND a sharp counterexample to a tempting conceptual conflation**: an unbounded environment history can coexist with a fully Markovian reduced quantum process. The next claim of P5/Ω must introduce a separately source-specified *re-interaction, non-Markov process-tensor witness or a derived nonclosure mechanism*, while P9 still needs actual common Cartan/ADM solder and source-generated canonical dynamics. Do not infer gravity, physical infinite generation or subjective memory from Kraus records alone.

**Reproducibility:** exact source H75 Kraus matrices and positive seed, all 16 rational two-record probabilities, covariance, explicit two-step interventions on full 36 matrix units, H110/H109 exact regression and analytic bilateral-shift proof. Draft/unmerged; no human peer review, experiment or independent Lean Einstein theorem claimed.
