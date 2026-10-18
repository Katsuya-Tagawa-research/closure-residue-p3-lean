# H85 — A4-Covariant Source-to-Edge Selection: Exact Affine Classification, Sharp Conditional Additive Selector, and Residual Provenance Gap

**2026-10-18 | P3–P11 Mathematical Bridge / P9 GR-I / Route A (Constructive).**

**Base:** H84 Draft PR #103 at \`25e2ca5\`, **97/97 CI PASS**. H85 is a finite edge-selection and provenance boundary, not a claimed derivation of spatial gravity. All prior H75–H84 genuine microscopic CPTP and P3 residual data remain **unchanged**; no frozen manuscripts or main edits.

## 1. The precise physical/mathematical distinction

Let **four separate physical copies** of the unchanged H75 six-dimensional microscopic source be assigned a set of four candidate spatial *cell labels* \(V=\{0,1,2,3\}\). These labels are **not** the four internal vertices in P7/P8 or automatically soldered physical positions. For independently chosen physical preparations and flag readout define a local calibrated scalar source signature \(r=(r_0,\dots,r_3)\in\mathbb R_{\ge0}^4\). A *candidate spatial interaction* is a positive unordered-edge weight vector \(w\in\mathbb R_{>0}^{E(K_4)}\) with six entries \(w_{ij}\). An actual **Hamiltonian** edge, correlated CP bath or physical metric coupling is *additional data*: a scalar weight assignment by itself is not a controlled interaction.

We ask whether (i) A4 symmetry, (ii) source readouts, (iii) edge locality, and (iv) a calibrated total coupling budget can select a unique edge-weight **mathematical assignment**. A4 acts by relabeling the four **declared** cells and their six unordered pairs. This may be used as an orientation-preserving comparator to the internal A4 representation of P7, but **physical action on these four cells and the solder identifying them with P7's internal carrier are NOT derived from P3/P7**. We do not assume S4 odd-permutation physical control ports.

## 2. H85.1 — Complete A4-equivariant affine edge-map classification (EXACT)

**Theorem.** Every affine map \(T:\mathbb R^4\to\mathbb R^{E(K_4)}\) satisfying \(T(P_\pi r)=P^{(E)}_\pi T(r)\) for **every** even permutation \(\pi\in A_4\) is uniquely of the form
\[
\boxed{T(r)_{ij}=c+\alpha(r_i+r_j)+\beta(r_k+r_l),\qquad\{i,j,k,l\}=\{0,1,2,3\},}
\tag{H85-A}
\]
for constants \(c,\alpha,\beta\in\mathbb R\). Thus the real vector space of A4-equivariant affine maps has **dimension 3**, not 1. The unperturbed local source \(\Phi_\mu\) does not select these three coefficients.

**Proof:** \(A_4\) acts transitively on the six unoriented edges. The stabilizer of \(\{0,1\}\) includes the double transposition \((01)(23)\), so the coefficient of \(r_0\) equals that of \(r_1\), and the coefficient of \(r_2\) equals that of \(r_3\). The constant term is fixed across every edge by transitivity. This gives the displayed three free coefficients at edge 01, propagated uniquely to all edges by A4. Conversely the displayed expression is manifestly A4-equivariant. \(\square\)

Exact Fraction rational elimination of all coefficient constraints (30 unknown coefficients including affine offsets, 324 nontrivial linear equations, rank **27**) independently certifies the three-dimensional solution space.

**Consequences / scoped No-Go:** positive weights, A4-equivariance and an externally prescribed total \(\sum_{i<j}w_{ij}=W\) at one nonzero source profile do **not** uniquely select an edge network. Even adding a zero-origin requirement on an affine map does not suffice: \(\alpha,\beta\) remain independent until further structure is imposed. A4 covariance is **not** a proven physical micro-interaction-selection mechanism.

## 3. H85.2 — A conditional unique additive edge assignment (EXACT, with all added assumptions explicit)

Suppose the desired selector additionally obeys an **affine linear edge-locality assumption**: the value of \(w_{ij}\) depends only on the source readouts \(r_i,r_j\), with no spectator-site dependence; and obeys the **zero-source/zero-weight condition** \(T(0)=0\). Equation (H85-A) then forces \(\beta=c=0\):
\[
w_{ij}=\alpha(r_i+r_j).
\]
For a *fixed observed nonnegative source profile* \(r\) with \(\sum_a r_a>0\), and a **separately calibrated** prescribed budget \(W>0\), the equality \(\sum_{i<j}w_{ij}=W\) uniquely fixes
\[
\boxed{\alpha=\frac{W}{3\sum_a r_a},\qquad
w_{ij}=\frac{W(r_i+r_j)}{3\sum_a r_a}.}
\tag{H85-B}
\]
All weights are nonnegative. Every edge is strictly positive iff each pair has \(r_i+r_j>0\) (for instance at most one vertex has \(r_i=0\)). The selector (H85-B), regarded as a function of *variable* \(r\) with fixed \(W\), is **homogeneous and nonlinear in \(r\)** because \(\alpha\) must be recalibrated. Do not call (H85-B) a single global affine map with fixed \(W\) for all possible \(r\).

**What was independently assumed:** the four candidate cell labels, their all-pairs K4 potential edges, a physical A4 relabeling principle, *additive linear edge locality*, the absolute total scale \(W\), and use of the observed \(r_i\) as interaction weights. Only **within this precise ansatz** is \(w\) uniquely selected. No original P3 residue or F axiom implies the ansatz or the weight budget.

**Nonuniqueness even with edge-locality if additivity is dropped:** for the same nonzero \(r\), the positive equivariant **nonlinear** alternative
\[
w^{(2)}_{ij}=\frac{W(r_i+r_j)^2}{\sum_{a<b}(r_a+r_b)^2}
\]
is edge-local, zero at zero before normalization, and obeys the budget where defined. It generally differs from (H85-B). Hence linear additivity is a substantive physical/modeling assumption, not a consequence of locality and positivity.

## 4. H85.3 — Genuine H75 physical flag-source data admit multiple positive A4 models (EXACT conditional illustration)

Keep the original four-Kraus six-level H75 source
\[
\Phi_\mu(X)=\sum_{a,b=0}^1
(|a\rangle\langle b|_E\otimes U M_a)X
(|a\rangle\langle b|_E\otimes U M_a)^\dagger,
\quad M_1=\operatorname{diag}(0,4/5,4/5).
\]
For **four separate** source uses with independently prepared visible states
\[
\rho_0=|0\rangle\langle0|,\quad
\rho_1=|1\rangle\langle1|,\quad
\rho_2=|2\rangle\langle2|,\quad
\rho_3=\tfrac34|0\rangle\langle0|+\tfrac14|1\rangle\langle1|,
\]
and a genuine positive physical flag-1 effect \(P_1=|1\rangle\langle1|_E\otimes I_3\), the measured probabilities after each \(\Phi_\mu(|0\rangle\langle0|_E\otimes\rho_a)\) are exactly
\[
\boxed{r=(0,16/25,16/25,4/25),\qquad\sum_a r_a=36/25.}
\]
The **original microscopic P3 witness remains** \(R_2=0,\ R_3=i\,\mathrm{diag}(-32,16,16,0,0,0)/135\ne0\); the four readout probabilities are conventional finite-QM observations and not observations of the signed \(R_3\).

For independently calibrated \(W=27\), (H85-B) yields six strictly positive edge weights in order \((01,02,03,12,13,23)\):
\[
\boxed{w^{\mathrm{add}}=(4,4,1,8,5,5).}
\]
But an equally positive, A4-equivariant, normalized affine *different* assignment for **the same profile and same budget** is
\[
\boxed{w^{\mathrm{unif}}=(9/2,9/2,9/2,9/2,9/2,9/2).}
\]
Indeed \(w^{\mathrm{unif}}\) is the affine (constant) A4 map, whereas \(w^{\mathrm{add}}\) belongs to the additive choice. An alternate **zero-at-origin linear map** satisfying the identical budget at the specified profile uses complementary vertex readouts:
\[
w^{\mathrm{comp}}_{ij}=\frac{W(r_k+r_l)}{3\sum r}
\quad\Rightarrow\quad
w^{\mathrm{comp}}=(5,5,8,1,4,4).
\]
All three are mathematically legitimate *candidate assignments* under the weaker symmetry, positivity and fixed-profile normalization assumptions. They are **not** independently certified physical Hamiltonians or different solutions to Einstein equations.

The nonlinear normalized *edge-local* comparator \(w^{(2)}\) above gives
\[
w^{(2)}=(144,144,9,576,225,225)/49,
\]
also strictly positive with total 27; it differs from \(w^{\mathrm{add}}\) unless additional additivity is imposed. H85's Fraction verifier independently checks the true H75 prepared states, flag probabilities, A4 covariance, all budgets/positivity, and distinct assignments.

## 5. H85.4 — Conditional K4 metric injectivity does not generate its weights (EXACT)

Given a **separately soldered** fixed Euclidean 3D carrier \(S=\mathbf1^\perp\subset\mathbb R^4\), define the P9 positive K4 chart
\[
L_w=\sum_{a<b}w_{ab}(e_a-e_b)(e_a-e_b)^\top,\qquad
g_w=16(L_w|_S)^{-1}.
\]
For all six positive weights the restriction is strictly positive and invertible. Under a **known fixed solder**, knowledge of \(g_w\) reconstructs weights uniquely:
\[
\boxed{w_{ij}=-16\langle P e_i,g_w^{-1}P e_j\rangle,\quad i\ne j,\qquad
P=I-\tfrac14\mathbf1\mathbf1^\top.}
\tag{H85-C}
\]
This is the previously derived **K4 linear isomorphism**, re-used with its exact domain. Its uniqueness is inverse **reconstruction from a specified metric**, not generation of the metric or physical solder.

For \(v=e_0-e_1\in S\), the inverse-metric contractions for the two positive candidates above are
\[
\boxed{\langle v,g_{\mathrm{add}}^{-1}v\rangle=17/8,\qquad
\langle v,g_{\mathrm{unif}}^{-1}v\rangle=9/4.}
\]
Thus identical microscopic local flag probabilities plus symmetric positive normalized candidate assignments can produce **different conditional spatial metrics**. The two graphs in this example both have the full K4 set of allowed edges: **adjacency topology itself was supplied**, not generated.

**No implication of a physical metric:** the algebraic \(g_w\) is positive definite; it does not produce a Lorentzian spacetime, canonical ADM gravitational momentum, the DeWitt \((5+,1-)\) kinetic signature, or off-shell HDA. A physical solder/cell adjacency and coupling law remain to be sourced.

## 6. P9/P11 handoff / verdict / next gate

| Statement | Verdict |
|---|---|
| A4 affine vertex-readout→K4-edge classifier has exactly 3 parameters | **EXACT**, analytical proof + Fraction rank audit |
| A4 covariance + positivity + fixed weight budget uniquely select a graph/weight function | **NO-GO** at the specified source profile, explicit positive alternatives |
| Edge-local **additive linear** ansatz + zero source + fixed calibrated budget yield unique weights | **EXACT CONDITIONAL**, requires all added assumptions |
| Four true H75 flag probabilities and the different candidate weighted K4 metrics | **EXACT** under independently chosen physical preparations and algebraic solder |
| Observed source readouts force actual intercell Hamiltonian strength or graph | **OPEN** |
| P3/P6/P7/P8 independently generate spatial A4 hardware symmetry, edge ansatz, budget or K4 solder | **OPEN** |
| Full P9 ADM/HDA, Einstein equations, P11 generative completeness | **OPEN** |

**To P9:** symmetry/source readouts alone do not generate unique spatial weights; H85 supplies a reproducible conditional positive K4 metric *construction* but not a dynamical physical sourcing law. Next seek microscopic two-cell interaction/correlation propagation plus an independently justified variational/representation criterion selecting an actual spatial adjacency and coupling. Preserve H59 global symplectic and H61 DeWitt/polarization obstructions.

**To P11:** refine the proposed AX-OA by specifying spatial source features, actual multi-cell ports and scheduling (H81/H84), a physically justified edge-selection law, and an independent criterion for equivalence of apparatus. A4 representation-theoretic constraints are **necessary comparator mathematics** under symmetry, not sufficient proof that \(F\) generated the observed graph.

**Reproducibility:** H85 dedicated exact rational checker tests the H75 original source flag statistics, the A4 rank-27 affine constraint matrix, conditional uniqueness within the additive class, alternative positive normalized weights, K4 Laplacian inversions, and continuity with H80–H84 gates. CI PASS is computational validation within written scopes; not a Lean theorem, human referee, or physical experiment.

**Exit decision:** Avoid unbounded accumulation of invented edge laws. Unless a source-derived physical interaction-selection law becomes available, classify failure of unique selection as a formal **generative provenance gate** and move P9 toward canonical/constraint dynamics and P11 toward stronger axioms, not declare Einstein dynamics.
