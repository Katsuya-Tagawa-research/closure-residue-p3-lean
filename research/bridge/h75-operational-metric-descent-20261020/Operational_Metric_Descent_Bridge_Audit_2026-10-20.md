# P3–P11 Mathematical Bridge: Operational Metric Descent Audit

**2026-10-20**  
**Status:** integration research note, not an H-number or P9 stage assignment. No Notion/GitHub modifications.

## 1. Source boundary

The independent auxiliary H75 audit reports a native-observation equality on a fixed \(U(3)\times U(3)\) KKS orbit and a difference in the existing GT–K4 metric. This note **independently verifies** the two blocks' positivity, spectra, trace normalization, and same-orbit property. It **does not independently verify** \(R_{\rm obs}(\rho)=R_{\rm obs}(\sigma)\) or the GT–K4 metric difference because the full formulas for native \(R_{\rm obs}\), \(F\), and \(g_{\rm eng}\) were not included in the handoff. Those statements are accepted only as *reported results of the source audit* pending import of the full formulas.

Let
\[
B(a,b;p,q)=\begin{pmatrix}a&ip&0\\-ip&b&iq\\0&-iq&a\end{pmatrix}.
\]
The characteristic polynomial is
\[
\det(\lambda I-B)=(\lambda-a)\big((\lambda-a)(\lambda-b)-(p^2+q^2)\big).
\]
For the user's specified pair, both versions of block 0 satisfy \(p^2+q^2=57/2500\), eigenvalues \(1/2,3/25,3/50\); both versions of block 1 satisfy \(p^2+q^2=64/5625\), eigenvalues \(16/75,8/75,0\). Both 6×6 density matrices are positive semidefinite with trace one. They belong to the same fixed blockwise unitary orbit.

## 2. Exact factorization criteria

**Theorem A (set-theoretic descent).** For maps \(R:X\to Y\) and \(g:X\to Z\), there exists a unique \(\bar g:R(X)\to Z\) such that \(g=\bar g\circ R\) if and only if
\[
R(x)=R(y)\quad\Rightarrow\quad g(x)=g(y)\qquad(\forall x,y\in X).
\]
This is the fibre-constancy criterion. Its proof is that \(\bar g(R(x)):=g(x)\) is well-defined precisely under the displayed implication. Uniqueness is on \(R(X)\), not necessarily the whole ambient \(Y\).

**Theorem B (smooth descent).** If \(X,Y\) are smooth manifolds, \(R:X\to Y\) is a surjective submersion, and \(g:X\to \mathrm{SPD}(3)\) is smooth and constant on every fibre, then the unique \(\bar g:Y\to\mathrm{SPD}(3)\) is smooth. Proof: submersions possess smooth local sections; compose each local section with \(g\), and use fibre constancy to glue.

**Theorem C (infinitesimal criterion, and its limit).** At a point \(x\),
\[
\operatorname{rank}DR_x=\operatorname{rank}D(R,g)_x\ \Longleftrightarrow\ \ker DR_x\subseteq\ker Dg_x.
\]
This constrains derivatives only. Even equality at **every** point does not imply global descent without an appropriate condition on fibres and topology. On \(X=S^1\), define \(R(\theta)=(\cos 2\theta,\sin 2\theta)\) and \(g(\theta)=\mathrm{diag}(2+\cos\theta,2+\sin\theta,1)\). Then both differentials have rank 1 everywhere, but \(R(\theta)=R(\theta+\pi)\) while \(g(\theta)\ne g(\theta+\pi)\). Conversely, for a surjective submersion \(R\) with connected fibres, \(\ker DR\subseteq\ker Dg\) everywhere implies fibre constancy, hence smooth descent.

**Theorem D (stable reconstruction).** Let \(R:X\to\mathbb R^m\) and \(g:X\to V\) where \(V\) is normed. There is an \(L\)-Lipschitz factorization \(\bar g:R(X)\to V\) if and only if
\[
\|g(x)-g(y)\|\le L\|R(x)-R(y)\|\qquad(\forall x,y\in X).
\]
This simultaneously implies fibre constancy and controls condition numbers. To reconstruct an SPD-valued metric robustly, a locally or globally adequate regularity assumption must also be checked, not inferred from rank.

**Theorem E (unavoidable reconstruction error).** Suppose \(R(x)=R(y)\) but \(g(x)\ne g(y)\). For every deterministic estimator \(\hat g:R(X)\to V\),
\[
\max\big(\|\hat g(R(x))-g(x)\|,\|\hat g(R(y))-g(y)\|\big)\ge\tfrac12\|g(x)-g(y)\|.
\]
Proof: triangle inequality. The source audit reports the signed GT-edge vector difference
\[
\Delta F=\frac{(0,0,7485696,0,0,-3735552)^\top}{369600625}.
\]
If the reported \(R_{\rm obs}\) equality and \(F\) difference are correct, any deterministic reconstruction of **that six-component F vector** from native observations has maximum componentwise absolute error at least \(3742848/369600625\approx 0.0101267361\) on this pair. This numeric bound concerns the **F vector**, not the SPD matrix; the metric matrix discrepancy requires the exact frame/edge conversion.

## 3. Operational enlargement and reachable sectors

Let \(\mathsf{Acc}=(\mathrm{Prep},\mathrm{Controls},\mathrm{Instruments},\mathrm{Scheduling},\mathrm{Readout})\) be a declared AX-OA certificate, and define \(R_{\mathsf{Acc}}\) from its permitted complete measurement records. The descent gate is conditional on \(\mathsf{Acc}\):
\[
\exists\bar g_{\mathsf{Acc}}:\ R_{\mathsf{Acc}}(X_{\mathsf{Acc}})\to\mathrm{SPD}(3),\quad g|_{X_{\mathsf{Acc}}}=\bar g_{\mathsf{Acc}}\circ R_{\mathsf{Acc}}|_{X_{\mathsf{Acc}}}.
\]
Additional readouts \(C\) could remove the reported collision only if \(C(\rho)\ne C(\sigma)\), or the pair is removed by a justified accessible-sector restriction. This **pairwise condition is necessary, not sufficient**, for a global descent theorem. Neither the new readout's hardware implementation nor the restriction's source may be assumed from the sought metric, to avoid circularity.

The user-supplied rank checkpoint \(\mathrm{rank}\,DR_{\rm obs}=\mathrm{rank}\,D(R_{\rm obs},F)=11\) is only infinitesimal information. The reported global collision does not itself identify whether disconnected regular fibres, singular loci, or failures elsewhere of the rank property account for the obstruction.

## 4. Research routing / gates

- **P3 Bridge:** keep source P3 residual filtration separate from KKS/GT metric or operational detection; no inference from same ranks to metric descent.
- **P9:** mark existing **fixed-orbit/global native GT–K4 descent** as **reported EXACT NO-GO** pending independent check of R_obs, F and g. Conditional or altered-access constructions remain OPEN.
- **P11:** define certificate-indexed observational equivalence; prove exact descent, smoothness, stability and access realizability separately; forbid reconstruction/selection circularity; G2 and G3 remain OPEN.
- **P6 / P7–P8 / GR:** the negative metric-descent result does not clear P6 provenance, soldering, KKS-to-ADM, DeWitt, off-shell HDA, Einstein equations or generative completeness.
- **H82:** do not restart finite-memory-rank optimizations as a consequence of this handoff.

## 5. Next independent evidence needed

To promote the source's GT–K4 statement from *reported result* to independently reverified statement: (i) executable \(R_{\rm obs}\) on the fixed H75 block orbit, (ii) the exact six GT-edge formulas \(F\), (iii) edge assignment/frame and \(g_{\rm eng}\) formula, and (iv) source audit or machine-checkable certificate for all equalities.
