# P11/P6 — Actual H75 Selective-Instrument and Adaptive Feedback Separation

**Date:** 2026-10-20. **Status:** finite exact mathematics; Draft stacked on #180. The original H75 four-Kraus source, P3 residue and frozen P1–P8 are unchanged.

## Exact result and its correct scope

A CPTP map obtained by **forgetting the results** of an instrument does *not* specify the instrument's individual completely positive branches, nor the joint classical–quantum outcome state. On the original H75 six-level source we exhibit two **genuine three-outcome quantum instruments** with exactly the same nonselective CPTP map on *all 36 complex matrix units*, whose outcome records differ on an **actual H75 output state**, and whose **outcome-dependent original H75 conditional-SWAP feedback** produces different *unlabelled* final native site probabilities after a second copy of the same source.

This makes a precise distinction between a single-time prediction of a coarse-grained CPTP channel and a fully typed causal program carrying a classical outcome register. It is ordinary finite Markovian quantum instrument mathematics, not quantum non-Markovian memory, an F-derived physical apparatus or a P3-exclusive prediction.

## 1. Original H75 plus two selective decompositions of the SAME CPTP channel

Keep the authentic original 4-Kraus map
\[
\Phi_\mu(X)=\sum_{a,b\in\{0,1\}}
K_{ab} X K_{ab}^{\dagger},\quad
K_{ab}=|a\rangle\langle b|\otimes U M_a,
\]
where \(U=\operatorname{diag}(i,1,i)\,O\),
\[
O=\begin{pmatrix}
2/3&2/3&-1/3\\-2/3&1/3&-2/3\\-1/3&2/3&2/3
\end{pmatrix},\
M_0=\operatorname{diag}(1,3/5,3/5),\
M_1=\operatorname{diag}(0,4/5,4/5).
\]
Define the original site effects \(L_j=I_2\otimes|j\rangle\langle j|\) for \(j=0,1,2\) and the following **independently imported**, selectively read out quantum instruments:
\[
\mathcal A_j(X)=L_j X L_j,\quad j=0,1,2,
\]
\[
J_0=(L_0+L_1)/\sqrt2,\quad
J_1=(L_0-L_1)/\sqrt2,\quad J_2=L_2,\qquad
\mathcal B_j(X)=J_j X J_j^\dagger.
\]
Each branch is a completely positive trace-nonincreasing map. Each three-outcome instrument is trace preserving after summing branches, because \(\sum_jL_j^\dagger L_j=\sum_jJ_j^\dagger J_j=I_6\).

**Identity on every operator:**
\[
\boxed{\sum_j\mathcal A_j(X)=\sum_j\mathcal B_j(X)
=\Delta(X)=\sum_jL_j X L_j.}\tag{1}
\]
Indeed the cross terms \(L_0XL_1+L_1XL_0\) cancel between \(J_0\) and \(J_1\). The exact checker independently verifies (1) on *all 36 complex 6×6 matrix units*, not merely on selected positive preparations.

The instruments are **not** the same result-resolved object. Their classically labelled quantum channels are
\[
\widehat{\mathcal A}(X)=\sum_{j=0}^2|j\rangle\langle j|_C\otimes\mathcal A_j(X),\quad
\widehat{\mathcal B}(X)=\sum_{j=0}^2|j\rangle\langle j|_C\otimes\mathcal B_j(X).
\]
They differ even though tracing out classical C yields precisely the same nonselective \(\Delta\).

## 2. An actual H75 source output already separates the outcome records (EXACT)

Let \(\rho_{01}=|0,1\rangle\langle0,1|\), a valid native flag-block-diagonal input, and \(\omega=\Phi_\mu(\rho_{01})\). The actual qutrit site populations are \((4/9,1/9,4/9)\). The probabilities for the three recorded outcomes are
\[
\boxed{
p_\mathcal A(j|\omega)=\left(\frac49,\frac19,\frac49\right),\quad
p_\mathcal B(j|\omega)=\left(\frac5{18},\frac5{18},\frac49\right).}\tag{2}
\]
Both distributions are normalized, while the nonselective outputs \(\Delta(\omega)\) are identical.

General exact **labelled-instrument identification lemma:** for a fixed admitted input subspace \(V\), two finite instruments are indistinguishable by *every* complete labelled classical-register outcome plus informationally complete conditional quantum readout precisely when their branch maps agree as linear maps on \(V\). Necessity follows from separating each \(\mathcal I_j(X)\) with effects; sufficiency is substitution. Equality of their summed CPTP maps is much weaker. This is a finite linear statement conditional on **access to the classical record and sufficiently rich conditional readout**, not a claim of actual P6 hardware.

## 3. Original registered H75 conditional-SWAP feedback reveals a difference without displaying the record

Use the **already registered original H75 real conditional site SWAP**
\[
S=|0\rangle\langle1|+|1\rangle\langle0|+|2\rangle\langle2|,\quad
F_{\rm fb}=|0\rangle\langle0|_E\otimes I_3+
|1\rangle\langle1|_E\otimes S.
\]
Let the **additional authorized classical feedback policy** apply \(F_{\rm fb}\) when instrument outcome \(j=0\) and the identity unitary for \(j=1,2\). Let \(\mathcal G_\mathcal A(X)=F_{\rm fb}\mathcal A_0(X)F_{\rm fb}^\dagger+\mathcal A_1(X)+\mathcal A_2(X)\), and similarly \(\mathcal G_\mathcal B\). Both are CPTP because the branch maps are CP and each conditional feedback unitary preserves trace.

After a second independently scheduled memoryless use of the *same* authentic \(\Phi_\mu\), with the **original native terminal site effects** \(Q_k=L_k\) and the same initial \(\rho_{01}\), exact probabilities are:
\[
\begin{array}{c|ccc}
 &Q_0&Q_1&Q_2\\\hline
\Phi_\mu\mathcal G_\mathcal A\Phi_\mu&8/27&211/675&88/225\\
\Phi_\mu\mathcal G_\mathcal B\Phi_\mu&8/27&251/675&224/675\\
\mathcal A\text{ minus }\mathcal B&0&-8/135&+8/135
\end{array}\tag{3}
\]
Every row is normalized and the difference row sums to zero. This is an **unlabelled terminal observation**: the classical record is used internally to control \(F_{\rm fb}\), but need not be exposed at the final readout. If that feedback is removed, the channels coincide by (1) even after the second source use; the exact checker verifies this.

**Core conclusion:**
\[
\boxed{
\operatorname{Tr}_C\widehat{\mathcal A}
=\operatorname{Tr}_C\widehat{\mathcal B}=\Delta
\quad\not\Rightarrow\quad
\Phi_\mu\mathcal G_\mathcal A\Phi_\mu
=\Phi_\mu\mathcal G_\mathcal B\Phi_\mu.}\tag{4}
\]
This implication fails only because an *outcome-conditioned future operation* was granted. This makes a precise point for AX-OA: a bare coarse-grained CPTP map is not a complete **adaptive instrument-and-schedule access certificate**.

## 4. The future effect quotient changes when adaptive flag control is authorized

#180 proved that with **only** repetitions of \(\Phi_\mu\), optional unobserved site dephasing and original \(Q_k\), all future effects from an *arbitrary cut state* are \(I_2\otimes B\), and two cut states are future-equivalent iff their flag partial traces agree.

Under the *enlarged* grammar that now also authorizes a **selective site instrument, a classical outcome wire, and the conditional \(F_{\rm fb}\) before the next source**, this flag-partial-trace equivalence is **no longer valid on arbitrary cut inputs**.

For example, \(\tau_0=|0,0\rangle\langle0,0|\) and \(\tau_1=|1,0\rangle\langle1,0|\) have identical flag partial trace \(|0\rangle\langle0|\) on the qutrit. Under one future original H75 source with no feedback their site probabilities agree, \((4/9,4/9,1/9)\). But under the same \(\mathcal A\) selective-site instrument and the above branch-0 conditional \(F_{\rm fb}\), followed by one original H75 source, they produce
\[
p(\tau_0)=\left(\frac49,\frac49,\frac19\right),\qquad
p(\tau_1)=\left(\frac49,\frac19,\frac49\right).\tag{5}
\]
Therefore the prior future quotient requires **recalculation for the enlarged authorized grammar**. In (5), \(\tau_0,\tau_1\) are ordinary **cut-input density states, not claimed to be elements of \(\operatorname{im}\Phi_\mu\)**; (5) does not contradict #180's stronger observability on that actual source-output subspace.

## 5. Irrecoverable cut erasure remains invariant (EXACT)

The original strictly positive native pair \(\rho_\pm=I_6/6\pm\operatorname{diag}(-I_3,I_3)/12\) satisfies \(\Phi_\mu(\rho_+)=\Phi_\mu(\rho_-)\) as full six-level density matrices. For either selective instrument, both records and all their branch states coincide when acting on these equal cut states; feed-forward, another source and site effects remain identical. This follows for any common downstream **memoryless** adaptive instrument policy by linearity, in the absence of a distinguishing environmental side channel.

Thus adaptive future control can refine *coarse observational equivalence*, but cannot resurrect a **true erased full quantum state difference at the causal cut**.

## 6. Generative program boundary

**EXACT finite:** (1) nonselective CPTP equality on all 36 basis matrices, (2) distinct 3-result outcome distributions for an actual source-output state, (3) adaptive unlabelled terminal contrast \((0,-8/135,8/135)\), (4) strict enlargement of future distinguishability on arbitrary cut states, (5) no resurrection of true source-kernel differences, and general finite labelled-instrument identification criterion.

**Independently ASSUMED:** physical access to both Kraus decompositions as different **selective implementations**, readable/classically storable outcome labels, branch-0 feed-forward control and its sign/timing calibration, ability to reuse the same memoryless original H75 source, final site measurement. These resources are *not* generated by F, by #180's closure calculation or by a frozen P6 observer hypothesis.

**OPEN:** F-intrinsic generation/uniqueness/minimality of AX-OA; actual P6 \(\mathcal J_N\) and signed hidden-current provenance; quantum process-tensor memory and intermediate correlations (none inferred here); original fixed-orbit GT–K4 metric descent and P7/P8 soldering; KKS→ADM/HDA/Einstein dynamics; P11 Generative Completeness and P12. Neither the observed standard CPTP effect nor the finite calculator tests a new CR-specific physical signature. Draft/unmerged; no main or published paper changes, no human peer review and no general Lean theorem.

**Reproducibility:** standalone exact SymPy script recreates the original H75 four Kraus operators, both quantum instruments and feedback, checks (1) on all 36 matrix units and the full rational distributions (2),(3),(5), and separately verifies true source-kernel erasure. Dedicated CI tests the finite arithmetic, not physical feasibility.
