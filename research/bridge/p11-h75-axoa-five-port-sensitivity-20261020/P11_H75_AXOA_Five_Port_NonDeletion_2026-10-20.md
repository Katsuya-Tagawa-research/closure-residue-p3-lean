# P11 G2/G3 — H75 AX-OA Five-Port Componentwise Non-Deletion Certificate

**2026-10-20 | P3–P11 Mathematical Bridge | Draft stacked on PR #176**

## Status, objective and stringent interpretation

**EXACT finite H75 result:** With the original **unchanged** four-Kraus six-level CPTP source \(\Phi_\mu\) inserted **exactly once** in each protocol, each of the five typed AX-OA coordinates — Preparation, Control, Instrument, Scheduling, Readout — admits an explicit pair of *physical* quantum protocols with **all other four typed coordinates held fixed** but **distinct exactly rational Born probabilities**.

This proves *componentwise operational sensitivity* and a **non-deletion theorem for this explicitly typed one-source evaluator**: a predictor receiving only four coordinates while the fifth is forgotten cannot correctly predict all five witness pairs. This **does not** prove the logical independence of five proposed axioms in a different representation, their unique irreducible minimality, the impossibility of encoding one coordinate into another, or physical generation of the five ports from F. The original-source 3-world hardware nonselection and P11 G2-intrinsic remain OPEN.

## 1. True H75 four-Kraus source and typed program evaluator

Let \(\mathcal H=\mathbb C^2_E\otimes\mathbb C^3_S\), with original fixed
\[
K_{ab}=|a\rangle\langle b|\otimes UM_a,\quad
U=\operatorname{diag}(i,1,i)
\begin{pmatrix}2/3&2/3&-1/3\\-2/3&1/3&-2/3\\-1/3&2/3&2/3\end{pmatrix},
\quad M_0=\operatorname{diag}(1,3/5,3/5),\quad
M_1=\operatorname{diag}(0,4/5,4/5).
\]
The original CPTP map \(\Phi_\mu(X)=\sum_{ab}K_{ab}XK_{ab}^\dagger\) is kept identical in all experiments.

Define a *typed single-trial certificate*
\[
c=(\rho,C,\mathcal I,\sigma,Q),
\]
where:

- \(\rho\) is a normalized PSD 6×6 **Preparation** density matrix;
- \(C\) is an independently authorized 6×6 unitary **Control port**;
- \(\mathcal I\) is an independently authorized one-outcome CPTP **Instrument** (one-outcome instruments are valid quantum instruments; both choices used below are trace preserving);
- \(\sigma\in\{\mathrm{pre},\mathrm{post}\}\) is **Scheduling**, specifying whether this control executes before or after the single fixed H75 source;
- \((Q,I_6-Q)\) is an independently authorized positive complete binary POVM **Readout**.

The typed Born evaluator is
\[
p(\rho,C,\mathcal I,\mathrm{pre},Q)
=\operatorname{Tr}\big[Q\,\mathcal I\big(\Phi_\mu(C\rho C^\dagger)\big)\big],
\]
\[
p(\rho,C,\mathcal I,\mathrm{post},Q)
=\operatorname{Tr}\big[Q\,\mathcal I\big(C\Phi_\mu(\rho)C^\dagger\big)\big].
\]
Every legal program applies the **same source** once and the same **one-outcome instrument** once. The control and instrument operations, time placement and final readout are **input resources** rather than proven outputs of F. This is a deliberately restricted, explicitly specified operational grammar, not the entire operational algebra of P6 or all possible measurement histories.

Write \(\rho_{aj}=|a,j\rangle\langle a,j|\), \(Q_j=I_2\otimes|j\rangle\langle j|\), \(S=|0\rangle\langle1|+|1\rangle\langle0|+|2\rangle\langle2|\), and the **already registered original H75 conditional SWAP**
\[
F_{\mathrm{fb}}=|0\rangle\langle0|_E\otimes I_3+
|1\rangle\langle1|_E\otimes S.
\]
Use the one-outcome identity instrument \(\mathcal I_{\rm id}=\operatorname{id}\) or the **nonunitary site-dephasing instrument**
\[
\mathcal I_{\Delta}(X)=\sum_{j=0}^2 L_jXL_j^\dagger,\qquad
L_j=I_2\otimes |j\rangle\langle j|.
\]
It is CPTP since \(\sum_j L_j^\dagger L_j=I_6\), and it is genuinely nonunitary, e.g. it removes \(|0\rangle\langle2|\) coherence. Its three Kraus operators are an *internally unobserved* fine-graining of a one-outcome instrument, not three revealed measurement results.

Finally define the real rank-two phase-interference test effect
\[
|\xi\rangle=(|0\rangle+|2\rangle)/\sqrt2,\qquad
Q_{02}=I_2\otimes|\xi\rangle\langle\xi|.
\]
The binary pair \(\{Q_{02},I_6-Q_{02}\}\) is a complete positive POVM. **Q02 is an independently supplied test readout**, not claimed to be among H75's earlier three site-population effects; only the original Q_j effects are used in the other four pairs.

## 2. Five exact componentwise witnesses

The companion checker evaluates the same fixed source once for each of the following ten protocols. In each paired row **every other typed coordinate is identical**, including which POVM outcome is counted.

| Changed coordinate | Tuple c_left (only relevant changes emphasized) | Tuple c_right | p_left | p_right |
|---|---|---|---:|---:|
| Preparation | \(\rho_{00}, I,\mathcal I_{\rm id},\mathrm{pre},Q_1\) | \(\rho_{01}, I,\mathcal I_{\rm id},\mathrm{pre},Q_1\) | \(4/9\) | \(1/9\) |
| Control | \(\rho_{10}, I,\mathcal I_{\rm id},\mathrm{pre},Q_1\) | \(\rho_{10}, F_{\rm fb},\mathcal I_{\rm id},\mathrm{pre},Q_1\) | \(4/9\) | \(1/9\) |
| Instrument | \(\rho_{00},I,\mathcal I_{\rm id},\mathrm{pre},Q_{02}\) | \(\rho_{00},I,\mathcal I_{\Delta},\mathrm{pre},Q_{02}\) | \(1/18\) | \(5/18\) |
| Scheduling | \(\rho_{10},F_{\rm fb},\mathcal I_{\rm id},\mathrm{pre},Q_1\) | \(\rho_{10},F_{\rm fb},\mathcal I_{\rm id},\mathrm{post},Q_1\) | \(1/9\) | \(4/9\) |
| Readout | \(\rho_{01},I,\mathcal I_{\rm id},\mathrm{pre},Q_1\) | \(\rho_{01},I,\mathcal I_{\rm id},\mathrm{pre},Q_2\) | \(1/9\) | \(4/9\) |

Proof for population probabilities: for a state initially at site \(j=0\), \(M_0|0\rangle=|0\rangle\) and \(M_1|0\rangle=0\), so after source it has qutrit site vector \(U|0\rangle=(2i,-2,-i)^\top/3\), with site populations \((4,4,1)/9\). For \(j=1\), output sums flag 0 and 1 with total site density \(U|1\rangle\langle1|U^\dagger\), whose populations are \((4,1,4)/9\). This yields the Preparation, Control, Scheduling and Readout rows from straightforward reordering/swapping.

Proof of **instrument sensitivity:** for source output \(U|0\rangle=(2i,-2,-i)^\top/3\), the coherent \(Q_{02}\) result is
\[
|\langle\xi|U|0\rangle|^2
=\left|\frac{i}{3\sqrt2}\right|^2=\frac1{18}.
\]
After independent site dephasing \(\mathcal I_\Delta\), the same effect gives
\[
\tfrac12\Bigl(\frac49+\frac19\Bigr)=\frac5{18}.
\]
Thus the distinction is between an identity and a **nonunitary CPTP instrument**, not the renaming of a coherent unitary gate as an instrument.

The Scheduling row is genuinely different even though all four other coordinates are fixed: for \(\rho_{10}\), pre-source \(F_{\rm fb}\) sends site 0 to site 1, giving \(Q_1=1/9\); if F acts after the source, the output flag is 0 because \(M_1|0\rangle=0\), hence the flag-1-conditional F acts trivially and \(Q_1=4/9\).

All density matrices, channels, effects, and normalized probabilities are finite exact ordinary-QM objects. Only the original \(\Phi_\mu\) and original \(F_{\rm fb}\) are inherited; the new site-dephasing channel and \(Q_{02}\) readout are **imported conditional experimental resources**, not hardware realizations inferred from the source.

## 3. Typed non-deletion theorem — exact, but intentionally narrow

Let \(\mathfrak C\) be the finite union of the ten explicitly listed certificates, \(p:\mathfrak C\to[0,1]\) be the Born evaluator, and for each named coordinate \(k\) let \(\pi_{\neg k}\) forget that coordinate while preserving the remaining four.

**Theorem (EXACT restricted operational non-deletion):**
\[
\boxed{
\forall k\in\{\mathrm P,\mathrm C,\mathrm I,\mathrm S,\mathrm R\},
\quad
p\ne f_k\circ\pi_{\neg k}
\ \text{for every deterministic }f_k
\text{ on }\operatorname{im}\pi_{\neg k}.
}
\]
Indeed, in each row there are two certificates with the same four retained coordinates, while the rational output probabilities are unequal. If \(p=f_k\pi_{\neg k}\), they would be equal, contradiction. Nothing about all other possible protocols is needed to establish this non-factorization.

This is a rigorous **relative, typed, experimentally operational sensitivity** result. It does **not** establish the independence of five *logical axioms*, minimality under arbitrary re-encoding (e.g. storing a readout as part of a composite instrument), universality for all CPTP sources, or a source-derived choice of resources. AX-OA is a sufficient typed interface for this grammar, not yet an F-generated or unique one.

## 4. Transfer to P11 and P9 without circularity

The already-audited source-fibre counterexample (#170–#175) says identical original H75 source can coexist with hardware setups granting different typed resources, even after relative flag-phase quotient. This new result shows within that **same source** that each of the five types can matter to a Born prediction if independently furnished. Hence an intrinsic P11 result must do more than construct the universal observer quotient (#176); it must justify the provenance of whichever typed port information it claims is generated.

An admissible theorem of the form \(F\longmapsto\mathrm{GenAcc}_F\) must specify:
- what is included among genuinely **prior** F data (if a physical preparation, clock or measurement system is inserted as an input, label it an axiom, not a consequence);
- whether it yields an oriented concrete implementation, a gauge-invariant operational quotient class, or merely a *set of possible certificates*;
- how the five-port data are chosen **hardware-faithfully** for each physical source fibre, and how the output transforms naturally under actual declared source symmetries;
- which P6 provenance/soldering/physical calibration gate, if any, supplies the missing operational permissions.

**OPEN:** F-origin of any AX-OA component; independence of P11 abstract axiom schemes; unique minimality; native physical P6 provenance; GT–K4 fixed-orbit native metric descent; KKS→ADM/DeWitt/HDA/Einstein; universal gravity and Generative Completeness. The original P3 residue has not been equated to an ordinary Born-response functional. Not a CR-exclusive prediction, physical experiment, human peer review, Lean formalization, or frozen-manuscript update.

**Audit:** companion exact SymPy test rebuilds original H75 Kraus matrices, tests CPTP/PSD/POVM/scheduling, explicitly verifies all five rational pairs, and proves no dropped coordinate can factor the specified outcome table. Dedicated GitHub Actions CI checks finite arithmetic. Draft/unmerged.
