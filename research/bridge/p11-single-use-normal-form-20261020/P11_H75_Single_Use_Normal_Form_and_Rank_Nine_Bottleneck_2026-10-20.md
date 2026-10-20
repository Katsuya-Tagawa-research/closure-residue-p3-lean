# P11 G2/G3 — Exact Single-Use Operational Normal Form and Native H75 Nine-Dimensional Bottleneck

**Date: 2026-10-20 | P3–P11 Mathematical Bridge | Stacked Draft on PR #177**

## Status and claim boundaries

PR #177 proved **componentwise non-deletion** in a *fixed typed interface* (Preparation, Control, Instrument, Scheduling, Readout), by five exact original-H75 pairs differing in only one coordinate and yielding unequal rational Born probabilities.

The present result is logically complementary and sharper for P11's uniqueness question:

**EXACT general one-source normal form:** For the declared *single-use* quantum protocols, **all** five typed coordinates reduce at the level of input-output probabilities to a pair comprising (i) an effective preparation \(\rho_{\rm eff}\) and (ii) an effective positive readout effect \(E_{\rm eff}\). Such behavioral reduction does **not** permit physical implementation of the effective pair with the *originally authorized resource catalog*. It is a mathematical representation of the Born functional, not an F-generation theorem.

**EXACT H75 source bottleneck:** the unchanged original H75 four-Kraus channel has real rank 9 on **both** the whole 36-real-dimensional Hermitian 6×6 operator space and the 18-real-dimensional native flag-block-diagonal subspace, with respective kernel dimensions 27 and 9. Consequently normalized source-output state families have affine dimension 8; without extra pre-source controls, no number of post-source instruments/readouts can recover the discarded 27 (respectively 9 native) real linear directions.

**EXACT non-uniqueness:** physically different preparations, instruments and effects can become operationally indistinguishable after the original source. The single-use five-tuple is therefore **not uniquely reconstructible** from its complete Born behavior, even though each coordinate can individually affect that behavior when the other four are frozen.

These do **not** refute the previous finite H75 rank-18 reconstruction from **multiple different pre-source coherent port programs**. All source and control definitions are inherited, not modified. Original P3 residue, P6/P7/P8, P9 Einstein dynamics and intrinsic F-generated access remain separate OPEN gates.

## I. Single-use normal form: exact theorem for all finite CPTP sources

Let \(\Phi:B(\mathcal H)\to B(\mathcal H)\) be any CPTP channel and consider the explicitly typed five-tuple \(c=(\rho,C,\mathcal I,\sigma,Q)\), where:
- \(\rho\) is a positive normalized preparation on \(\mathcal H\);
- \(C\) is a unitary control **whose timing is specified by \(\sigma\)**;
- \(\mathcal I\) is a one-outcome CPTP instrument applied after the source and the (pre/post) control;
- \(\sigma\in\{\mathrm{pre},\mathrm{post}\}\) specifies the placement of \(C\) relative to the **one** source use;
- \((Q,I-Q)\) is a complete positive binary terminal POVM, \(0\le Q\le I\).

Set \(E=\mathcal I^*(Q)\), where \(\mathcal I^*\) is the Heisenberg adjoint determined by \(\operatorname{Tr}[A\mathcal I(B)]=\operatorname{Tr}[\mathcal I^*(A) B]\). Since \(\mathcal I\) is CPTP, its adjoint is positive and unital; thus \(0\le E\le I\). Define:

\[
(\rho_{\rm eff},E_{\rm eff})=
\begin{cases}
(C\rho C^\dagger,\ E),&\sigma=\mathrm{pre},\\
(\rho,\ C^\dagger E C),&\sigma=\mathrm{post}.
\end{cases}
\]

**Theorem (exact finite CPTP single-source operational normal form):**
\[
\boxed{\Pr(Q\mid c)=\operatorname{Tr}\!\left[E_{\rm eff}\Phi(\rho_{\rm eff})\right].}
\tag{NF}
\]
*Proof:* if pre, use \(\operatorname{Tr}[Q\mathcal I(\Phi(C\rho C^\dagger))]=\operatorname{Tr}[\mathcal I^*(Q)\Phi(C\rho C^\dagger)]\). If post, use \(\operatorname{Tr}[Q\mathcal I(C\Phi(\rho)C^\dagger)]=\operatorname{Tr}[C^\dagger\mathcal I^*(Q)C\,\Phi(\rho)]\). Both cases preserve positivity, trace of the effective input, and \(0\le E_{\rm eff}\le I\). The complementary effect \(I-E_{\rm eff}\) remains positive and forms a complete binary POVM.

This is a **surjective mathematical re-description** of each typed certificate, not an injective resource decomposition. It is *not* valid as stated for unrestricted multi-time process tensors, instruments with conditioned intermediate outcomes, feedback policies, multiple interleaved source uses, or extra restrictions that force effective preparations/effects to remain inside a smaller authorized physical catalog. Those require their own theory.

## II. The precise H75 rank-nine bottleneck

Use the **unchanged original H75** model, not a surrogate:
\[
K_{ab}=|a\rangle\langle b|\otimes U M_a,\qquad
U=\mathrm{diag}(i,1,i)O,\quad
M_0=\mathrm{diag}(1,3/5,3/5),\quad
M_1=\mathrm{diag}(0,4/5,4/5),
\]
with the original orthogonal
\[
O=\begin{pmatrix}
2/3&2/3&-1/3\\
-2/3&1/3&-2/3\\
-1/3&2/3&2/3
\end{pmatrix}.
\]
Writing any 6×6 operator in 2×2 flag blocks \(X_{ab}\) and \(Y=X_{00}+X_{11}=\operatorname{Tr}_{E}X\), a direct Kraus sum gives
\[
\Phi_\mu(X)=
\begin{pmatrix}
UM_0YM_0U^\dagger&0\\
0&UM_1YM_1U^\dagger
\end{pmatrix}.
\tag{H75}
\]
The partial trace \(\operatorname{Tr}_E:\operatorname{Herm}(6)\to\operatorname{Herm}(3)\) is onto. The subsequent map \(Y\mapsto\operatorname{diag}(UM_0YM_0U^\dagger,UM_1YM_1U^\dagger)\) is injective since **\(M_0\) is invertible**. Hence
\[
\boxed{
\operatorname{rank}_{\mathbb R}\Phi_\mu|_{\operatorname{Herm}(6)}=9,\quad
\dim\ker=36-9=27.}
\]
The original native input \(V=\operatorname{Herm}(3)\oplus\operatorname{Herm}(3)\) is 18-real-dimensional, and partial trace remains onto there, so
\[
\boxed{
\operatorname{rank}_{\mathbb R}\Phi_\mu|_V=9,\quad
\ker(\Phi_\mu|_V)=\{(H,-H):H\in\operatorname{Herm}(3)\},\
\dim\ker=9.}
\]
On normalized density states, the positive identity state lies in the relative interior of the trace-one input affine slice. Since trace is preserved, the affine dimension of the source output is exactly **8** (a source with only eight normalized real state parameters after one use). The companion checker evaluates the genuine original four Kraus operators on **all 36 full 6×6 complex matrix units**, verifies (H75), checks exact superoperator rank 9, and checks the same rank on all **18 native block matrix units**.

**Scope:** rank 9 describes a *single source application without independent earlier intervention*. Multi-experiment response datasets using distinct pre-source controls depend on \(C\) and may jointly reconstruct more original input directions, as in PRs #168/#171/#176. It is not a contradiction.

## III. Exact H75 inequivalent resource implementations with identical behavior

### A. Hidden native preparation states, identical full source outputs

Let \(X_{\rm flag}=\operatorname{diag}(-I_3,I_3)\) and
\(\rho_\pm=I_6/6\pm X_{\rm flag}/12\). Both are full rank, normalized positive density matrices, \(\rho_+\ne\rho_-\) but
\[
\Phi_\mu(\rho_+)=\Phi_\mu(\rho_-).
\]
They therefore cannot be distinguished by **any** post-source CPTP instrument or POVM with no new pre-source intervention. A previously authorized pre-source five-macro coherent word *can* separate them; this demonstrates why the operation time/type matters, not a failure of H75 mathematics.

### B. Distinct valid POVM readouts, identical responses for all inputs

Let
\[
T=(|0\rangle\langle1|+|1\rangle\langle0|)_E\otimes I_3,\qquad
E_\pm=\tfrac12 I_6\pm\tfrac14 T.
\]
Both effects have eigenvalues \(1/4,3/4\), and \(\{E_\pm,I_6-E_\pm\}\) are complete positive binary POVMs. They are distinct operators, but the source output is strictly flag-block-diagonal; thus
\[
\boxed{\Phi_\mu^*(E_+)=\Phi_\mu^*(E_-)=I_6/2}
\]
and both yield Born probability \(1/2\) for every density input through the original H75 source. They may be separated by independently authorized **post-source coherent flag-mixing controls** or by other physical timing arrangements, so the equivalence is limited to the specified one-use/no-post-control experiment grammar.

### C. Nonunitary instrument vs changed effective readout

Let \(|\xi\rangle=(|0\rangle+|2\rangle)/\sqrt2\),
\(Q=I_2\otimes|\xi\rangle\langle\xi|\), and
\[
\Delta(Z)=\sum_{j=0}^2
(I_2\otimes|j\rangle\langle j|)\,Z\,
(I_2\otimes|j\rangle\langle j|).
\]
This is a genuine *nonunitary* dephasing CPTP one-outcome instrument. Its adjoint maps the positive binary effect to
\[
Q_{\rm eff}=\Delta^*(Q)
=\tfrac12\,I_2\otimes
(|0\rangle\langle0|+|2\rangle\langle2|).
\]
Then \(\Delta\) followed by \(Q\) is operationally identical to the identity one-outcome instrument followed by the distinct (nonprojective but positive) effect \(Q_{\rm eff}\):
\[
\boxed{\operatorname{Tr}[Q\,\Delta(Z)]
=\operatorname{Tr}[Q_{\rm eff}\, Z]\quad\text{for every }Z.}
\]
The checker verifies this identity for all 36 complex basis input operators \(X\) with \(Z=\Phi_\mu(X)\), and the earlier numeric contrast \(\operatorname{Tr}[Q\,\Delta(\Phi_\mu(\rho_{00}))]=5/18\). The effective effect need **not** be in the original H75 authorized site-projector readout catalog. Hence the identity proves behavioral non-uniqueness, not hardware equivalence.

### D. Preparation vs original pre-source coherent control

With the registered H75 conditional SWAP \(F_{\rm fb}\), the actual physical native preparations \(\rho_{10}=|1,0\rangle\langle1,0|\) and \(\rho_{11}=|1,1\rangle\langle1,1|\) satisfy
\[
F_{\rm fb}\rho_{10}F_{\rm fb}^\dagger=\rho_{11}.
\]
Consequently the two typed resource pairs \((\rho_{10},F_{\rm fb}\text{ pre-source})\) and \((\rho_{11},I\text{ pre-source})\) produce **identical full H75 source output**, and agree under every subsequent instrument and terminal POVM. Both are valid but differently typed implementations; no source-only probability identifies which one was used.

## IV. Implications for P11 and exact no-go scope

PR #177's **componentwise non-deletion** is true: holding the other four typed settings fixed, each fifth coordinate can change the prediction.

The new result shows an apparent "independence ⇒ uniqueness" inference is false: **when coordinated changes of multiple settings are allowed, the five-tuple has nontrivial observational fibres**. These fibres are a *separate* obstruction from the three-world source-fibre selection obstruction of PRs #170–#175, and not equivalent to the original P3 quadratic commutator residue.

P11 must distinguish:
1. **typed operational certificate** (concrete intended resources);
2. **behavioral equivalence class** for a **fully specified set of admissible experiments**;
3. **mathematical effective normal form** under an allowed one-source grammar;
4. **physically realized source-selected** preparation/control/instrument/schedule/readout hardware.

A **universal theorem** describing the behavioral normal form of a restricted grammar does not generate a source-selected physical instrument or imply one-to-one decomposition. An intrinsic \(F\to\mathrm{GenAcc}_F\) theorem must either physically derive ports/clock/calibration from prior F data, or explicitly mark them as independent assumptions and claim only relative mathematical prediction.

**Unproved gates remain:** actual F access generation; unique AX-OA axiom minimality; P6 provenance and CR-specific experimental witness; native GT–K4 metric descent; KKS→ADM/DeWitt/HDA/Einstein dynamics; P11 Generative Completeness; P12 universal gravity. This finite SymPy regression is not a Lean general theorem, a human peer review, or a physical experiment. This PR is Draft/unmerged and does not change frozen manuscripts.
