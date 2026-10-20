# P11/P6 — Exact Finite Future-Tester Closure of the Original H75 Source

**2026-10-20 | P3–P11 Mathematical Bridge | Stacked Draft on PR #179**

## Theorems and carefully delimited grammar

Keep the **unchanged original four-Kraus H75 six-level CPTP source** \(\Phi_\mu\), with three original native terminal site projectors \(Q_j=I_2\otimes|j\rangle\langle j|\). Permitted **future** operations after a causal cut consist only of: any finite number of independently scheduled copies of this **memoryless** source; any number of independently authorized, one-outcome site-dephasing CPTP interventions \(\Delta\), with their Kraus outcome labels discarded; a final original \(Q_j\) readout. There is **no** new coherent pre/post-control, conditioned intermediate measurement outcome, feed-forward, borrowed environment memory, or non-native readout in this grammar.

This is a finite **causal tester-completion theorem relative to an explicitly furnished future grammar**, not a theorem deriving scheduling, readout, or intervention apparatus from F. It strengthens #179's two-use counterexample and does not imply non-Markovianity.

### Exact results

1. **Finite stabilization:** the real Heisenberg-effect spans generated from the native three \(Q_j\) by up to \(n=0,1,2,3,4\) additional source uses have exact dimensions
   \[
   \boxed{3,\ 5,\ 7,\ 9,\ 9.}
   \]
   At **three** future source uses, the span is precisely \(I_2\otimes\operatorname{Herm}(3)\), dimension 9; no further permitted source use or unobserved site dephasing can enlarge it.
2. **Future-equivalence characterization:** for arbitrary six-level density states \(\sigma,\tau\) supplied **at the cut**, all allowed finite future test probabilities agree **iff**
   \[
   \boxed{\operatorname{Tr}_{E}(\sigma)=\operatorname{Tr}_{E}(\tau).}
   \]
   Thus the future-test quotient of the full real Hermitian 36D space is the 9D qutrit reduced-state space, with 27D linear kernel (affine normalized dimension 8). This does **not** say arbitrary full six-level density matrices are distinguishable.
3. **Completeness specifically on the H75 source-output image:** if \(\sigma,\tau\in\operatorname{im}\Phi_\mu\) are actual source output density matrices, then equality of the flag partial traces implies \(\sigma=\tau\). Hence **at most three** additional source uses and original site measurement discriminate **any two distinct original H75 output states**. This is an exact *relative finite observable completeness*, not access-generation completeness.
4. **Strictness in the reachable physical sector:** an explicit pair of **positive normalized source-output states** agrees on all original \(Q_j\) probabilities at depths \(0,1,2\) but differs at depth **3**. Consequently three future uses are necessary in general for the declared grammar; “three” is not merely a dimension-counting upper bound. For a state already produced by one initial H75 use, depth 3 means a total of up to four H75 uses including preparation of that cut state.

The original H75 source's discarded flag information is **never** recovered. These results concern observable content **within the source output image** and its reduced qutrit equivalence, not reversible dynamics on full six-level operators.

## I. Original H75 and exact adjoint reduction

Use the same authentic source as in #170–#179,
\[
K_{ab}=|a\rangle\langle b|\otimes UM_a,\quad
U=\operatorname{diag}(i,1,i)
\begin{pmatrix}2/3&2/3&-1/3\\-2/3&1/3&-2/3\\-1/3&2/3&2/3\end{pmatrix},
\]
\[
M_0=\operatorname{diag}(1,3/5,3/5),\quad
M_1=\operatorname{diag}(0,4/5,4/5).
\]
Writing \(Y=\operatorname{Tr}_E X=X_{00}+X_{11}\), the actual source is
\[
\Phi_\mu(X)=\operatorname{diag}\big(UM_0YM_0U^\dagger,\ UM_1YM_1U^\dagger\big).
\]
Every adjoint source image is therefore flag-identity:
\[
\Phi_\mu^*(Z)
=I_2\otimes\sum_{a=0,1}M_aU^\dagger Z_{aa}U M_a.
\]
In particular, define qutrit real-linear maps
\[
T(B)=\sum_{a=0,1}M_aU^\dagger BUM_a,\qquad
d(B)=\sum_{j=0}^2|j\rangle\langle j|B|j\rangle\langle j|.
\]
Then, for every Hermitian qutrit effect \(B\),
\[
\boxed{\Phi_\mu^*(I_2\otimes B)=I_2\otimes T(B),\qquad
\Delta^*(I_2\otimes B)=I_2\otimes d(B).}
\]
The Qj start with \(B=|j\rangle\langle j|\).

## II. Finite closure and an exact rank certificate

Let
\[
\mathcal R_n=\operatorname{span}_{\mathbb R}
\{T^k(|j\rangle\langle j|):0\le k\le n,\ j=0,1,2\}
\subseteq\operatorname{Herm}(3).
\]
Choose the standard real Hermitian basis (three diagonal \(E_{jj}\), three \(E_{ab}+E_{ba}\), three \(i(E_{ab}-E_{ba})\)). Each \(\mathcal R_n\) is represented by a matrix over the rationals; \(U\)'s fixed \(i\) phases do not introduce floating-point entries. Independent exact rational row-reduction yields
\[
(\dim\mathcal R_0,\ldots,\dim\mathcal R_4)=(3,5,7,9,9).
\]
Since \(\dim_{\mathbb R}\operatorname{Herm}(3)=9\), \(\mathcal R_3=\operatorname{Herm}(3)\). This gives a rigorous stopping certificate for the entire finite grammar: \(T(\mathcal R_3)\subseteq\mathcal R_3\) and \(d(\mathcal R_3)\subseteq\mathcal R_3\); in fact \(d\) sends every Hermitian qutrit operator to the *initial* diagonal \(\mathcal R_0\). Inserting any number of intermediate unobserved dephasings cannot enlarge the full closed span. Moreover, for a future word with at most \(n\) source uses, its effect belongs to \(\mathcal R_n\), since \(d\) cannot add source-use depth.

For states at the cut, the accessible joint statistics are precisely the pairings with \(I_2\otimes B\), \(B\in\operatorname{Herm}(3)\). Consequently two cut-state operators have identical future outcomes exactly when their reduced qutrit matrices coincide. Only a **finite subset** of the \(3\times4=12\) native site readout/depth combinations is required to separate nonzero differences in the quotient. This is *relative complete tomography of the reduced qutrit*, not tomography of a six-level state.

## III. The source-output image is fully separated at depth 3

For any original input \(X\) write \(Y=\operatorname{Tr}_E X\). The reduced qutrit of the full source output is
\[
\operatorname{Tr}_E\Phi_\mu(X)=\Lambda(Y)
=U\left(\sum_aM_aYM_a\right)U^\dagger.
\]
The middle map is a Schur product \(\sum_aM_aYM_a=G\odot Y\) with the **entrywise-nonzero** rational matrix
\[
\boxed{
G=
\begin{pmatrix}
1&3/5&3/5\\
3/5&1&1\\
3/5&1&1
\end{pmatrix}.
}
\]
Although \(G\) is singular as a 3×3 matrix, **its Schur-multiplication superoperator is invertible**, because *all nine entries are nonzero*. Conjugation by unitary \(U\) is invertible, so \(\Lambda\) is injective (indeed bijective as a real 9D linear map). Moreover, \(\Phi_\mu(X)\) is already completely determined by \(Y\) via its two flag blocks. Thus, on the **actual source image**,
\[
\operatorname{Tr}_E\sigma=\operatorname{Tr}_E\tau
\iff \sigma=\tau,
\qquad \sigma,\tau\in\operatorname{im}\Phi_\mu.
\]
Combined with \(\mathcal R_3=\operatorname{Herm}(3)\), this proves that three future uses followed by native readout are sufficient to distinguish all distinct H75 source-output states. No independent complex-phase POVM is assumed.

## IV. Strict-depth-three physical positive-state witness

Let \(H\in\operatorname{Herm}(3)\) be the explicit traceless matrix
\[
H=
\begin{pmatrix}
-296/15 & -32/9+16i & -98/9+i\\
-32/9-16i & 16/15 & -176/15\\
-98/9-i & -176/15 & 56/3
\end{pmatrix}.
\]
Define physical qutrit preparations
\[
Y_\pm=I_3/3\pm H/300
\]
and **native flag-prepared input states** \(\rho_\pm=|0\rangle\langle0|\otimes Y_\pm\). These are both legitimate *strictly positive on their qutrit flag-support block*: \(H\) is Hermitian and traceless, and every absolute row sum obeys
\[
\sum_j|H_{ij}|
\le\sum_j(|\operatorname{Re}H_{ij}|+|\operatorname{Im}H_{ij}|)
<52.
\]
Hence all eigenvalues of \(I_3/3\pm H/300\) are bounded below by \(1/3-52/300>0\). Both preparations have unit trace, and their **actual source outputs** \(\sigma_\pm=\Phi_\mu(\rho_\pm)\) are distinct.

Their initial post-source reduced site states are \(\Lambda(Y_\pm)\). An independent exact rational check shows:
\[
\operatorname{Tr}\!\left[Q_j\Phi_\mu^n(\sigma_+-\sigma_-)\right]=0,
\quad\forall j\in\{0,1,2\},\quad n=0,1,2,
\]
but at \(n=3\) the three probability differences (plus minus minus) are
\[
\boxed{
\left(
\frac{11864}{281250},
\frac{3728}{281250},
-\frac{15592}{281250}
\right)\neq(0,0,0).
}
\]
They sum exactly to zero, as required. Inserting optional unobserved site dephasing between the first 0,1,2 future source uses cannot reveal the pair any sooner because all those lower-depth effective readouts remain in \(\mathcal R_2\). Thus **depth three is necessary and sufficient for the fixed declared future grammar**, even on the physically reachable H75 source-output manifold.

This witness does not require coherent controls or foreign terminal POVMs, but it requires preparing the two nontrivial positive qutrit states and authorizing up to four total source uses—resources not derived from F.

## V. General finite linear closure theorem (separate from physical availability)

For any finite-dimensional real vector space \(V_{\rm obs}\) of Hermitian effects, specified linear Heisenberg maps \(L_1^*,\dots,L_s^*\) of legal deterministic future channels and a finite initial effect set \(E_0\), define
\[
R_0=\operatorname{span}E_0,\qquad
R_{n+1}=R_n+\sum_{i=1}^s L_i^*(R_n).
\]
This ascending sequence stabilizes after at most \(\dim V_{\rm obs}-\dim R_0\) **strict** dimension jumps; if \(R_{n+1}=R_n\) at any stage, then \(R_n\) is stable under every generator, so all future stages are equal. The least stable \(R_\infty\) is the unique invariant linear subspace containing \(E_0\).

For two input states, equality of every final measurement for every legal future *word* is equivalent to the state difference annihilating \(R_\infty\). Thus \(V_{\rm state}/R_\infty^\perp\) is the canonical future-predictive quotient for the **declared program grammar**. Its existence and uniqueness are ordinary finite linear algebra; no physical source chooses or authorizes the grammar by this theorem.

H75 is unusually explicit: saturation by **three source uses** yields the full reduced qutrit effect space rather than the whole \(\operatorname{Herm}(6)\).

## VI. P6/P11 transfer — proved vs assumed vs still open

**EXACT finite proofs:** the true H75 source dual reduction, source-output injective reduction, exact rank series 3/5/7/9/9, future-tester equivalence iff equal flag partial traces, minimal strict depth-three physically positive witness, complete erasure of original full source-kernel differences, general finite Heisenberg closure and quotient theorem.

**Independent resources assumed:** repeated memoryless H75 source uses; site-preparation states \(Y_\pm\) and readout ports; source scheduling; any optional dephasing instrument; the fact that a future program can apply those ports to the *same output state* without uncontrolled environmental memory. No experimentally verified P6 \(\mathcal J_N\) provenance or timing calibration is inferred.

**OPEN:** constructing the physical future grammar from genuinely prior F axioms rather than postulating AX-OA; all independent AX-OA logical minimality; signed P3 hidden-current physical readout; full process-tensor environmental memory; native KKS GT–K4 metric descent; P7/P8 soldering and KKS→ADM/HDA/Einstein; P11 Generative Completeness and P12. Exact rational CI is regression evidence only, not a universal Lean proof, real experiment or human peer review. Draft/unmerged and no main/frozen paper changes.

**Reproducibility:** a standalone SymPy checker reconstitutes the actual H75 four Kraus operators and their Heisenberg qutrit map, exact ranks, invariant closure under both source and dephasing, full-rank positive qutrit witness, exact depth-three probability differences, and invariant source erasure; dedicated scoped CI.
