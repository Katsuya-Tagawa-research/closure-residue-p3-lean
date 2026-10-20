# H75 AX-OA — Exact pre-reset control-depth threshold

**2026-10-20 | P3–P11 Mathematical Bridge continuation | Draft, stacked on PR #167**

## Claim and strict domain

Retain the true original H75 6-level, four-Kraus CPTP reset \(\Phi\) from PR #94, its H76/H81 flag rotation \(W\), conditional flag/site SWAP \(F_{\rm fb}\), and site-real Cayley ports \(V_A,V_B,V_{AB}\). Fix the exact **five-element registered macro-gate alphabet** \(\mathcal G=\{W,F_{\rm fb},V_A,V_B,V_{AB}\}\). Each appearance of \(V_{AB}\) counts as **one registered macro**, even though its definition contains two Cayley factors. Allow ONE H75 reset **after** the pre-reset unitary word, followed by arbitrary post-reset processing. Prove an **observability depth** statement on the real 18D block-diagonal input algebra \({\rm Herm}(3)\oplus{\rm Herm}(3)\); no assertion concerning general off-block flag coherences.

Define the flag-bias Hermitian operator and strictly positive state pair
\[
X=(-|0\rangle\langle0|+|1\rangle\langle1|)_{\rm flag}\otimes I_3,\quad
\rho_\pm=I_6/6\pm X/12.
\]
Both states have eigenvalues \(1/12\) (multiplicity 3) and \(1/4\) (multiplicity 3), unit trace, and are distinct. Their flag-traced site states coincide.

## EXACT word-length <=4 source-blindness NO-GO

For **every** word \(P=g_\ell\cdots g_1\) with \(g_i\in\mathcal G\) and \(0\le\ell\le4\),
\[
{\rm Tr}_{\rm flag}(PXP^\dagger)=0.
\]
The independent SymPy exact-rational checker exhaustively enumerates all \(1+5+25+125+625=\mathbf{781}\) words **with repetitions**. This is a finite exact proof over the specified rational unitaries, not a numerical fit, nor a theorem for arbitrary possible controls.

For the original H75 instrument \(K_{ab}=|a\rangle\langle b|\otimes U M_a\), the source reset factors as \(\Phi=L\circ {\rm Tr}_{\rm flag}\). Therefore
\[
\Phi(P\rho_+P^\dagger)=\Phi(P\rho_-P^\dagger)
\quad (\ell\le4).
\]
The pair is indistinguishable even by **arbitrary** subsequent system quantum channels or positive POVMs, since the post-reset **entire output state** is identical. Measuring extra post-reset effects cannot recover the difference.

Since \(X\ne0\) is a common kernel vector, the stacked response matrix for **all** words of lengths 0–4 and any post-reset measurements has rank at most 17 on the fixed real 18D domain.

## EXACT sharp rank threshold: 17 at depth<=4, 18 at depth5

Keep precisely the post-reset catalog \(T\in\{I_6,V_A,V_{AB}\}\) with \(Q_j=I_2\otimes |j\rangle\langle j|\), \(j=0,1,2\), as in PRs #164–#167.

- The **short** four-pre-reset catalog \(\{I,F_{\rm fb},F_{\rm fb}V_A,F_{\rm fb}V_B\}\), with 36 original-source probability rows, has **exact rational rank 17**. Because of the universal \(X\) kernel, this supplies both a rank-17 lower witness and a rank-17 upper bound for arbitrary collections of pre-reset words of lengths <=4, with these or any further post-reset measurement processing.
- The existing long pre-reset word \(P_5=F_{\rm fb}W V_B F_{\rm fb}W\), chronological **\(W\to F_{\rm fb}\to V_B\to W\to F_{\rm fb}\)**, obeys the exact nonzero identity:
\[
{\rm Tr}_{\rm flag}(P_5 X P_5^\dagger)
=\frac1{15625}
\begin{pmatrix}
-9216&0&18432\\
0&9216&-18432\\
18432&-18432&0
\end{pmatrix}\ne0.
\]
- Replacing the short catalog's fourth setting \(F_{\rm fb}V_B\) by \(P_5\) (keeping the other three and the **same** post/readout catalog) gives an **exact rational rank-18** 36×18 record, as in PR #164.

Thus **depth 5 is the first length at which complete rank-18 reconstruction is possible in this fixed alphabet and registered post-set**, not a universal hardware-complexity or circuit-optimality theorem.

## Source-positive Born-probability witness with no post pulse

Apply \(P_5\), then the original H75 reset, then measure \(Q_1=I_2\otimes |1\rangle\langle1|\). On the two strictly positive inputs, the exact measured probabilities are:
\[
p_+=32271/78125,\qquad
p_-=59437/234375,\qquad
p_+-p_-=\boxed{37376/234375}>0.
\]
The measured effect is a genuine positive projector and both inputs are strictly positive. No hypothetical Hamiltonian or new gate was added. The nonzero outcome difference is an operational **finite-QM control witness**, not a direct measurement of P3 signed residue or a CR-specific empirical signature.

## Physical, geometric and foundational separation

- **Proved finite mathematics:** all 781 short words source-blind to \(X\); sharp rank-17/18 threshold for the registered catalog; exact positive-state Q1 contrast at length 5.
- **Independently assumed access:** feasibility, timing, ordering, coherent phase reference, and independent calibration of \(W,F_{\rm fb},V_A,V_B,V_{AB}\). Registering mathematically valid gates is not proof of physical control access.
- **Not proved:** universal optimal access, multi-reset/adaptive strategy lower bounds, experimental implementability, P6 frozen \(\mathcal J_N\) derivation, geometric soldering, sourced KKS→ADM/DeWitt/off-shell HDA/Einstein, or P11 F-generated AX-OA/G2/G3 and Generative Completeness.
- PR #164's original **native-15 GT–K4 metric-descent NO-GO** is unaffected. Here all rank claims explicitly use the independently enlarged source-plus-control access catalog.
- Main and published/frozen P1–P8 remain unchanged; Draft/unmerged, no human refereeing or experiment.

## Reproduction

Run \`python research/bridge/h75-access-depth-20261020/H75_AXOA_PreReset_Depth_Exact.py\` with SymPy. The checker computes all 781 exact rational word transports, source CPTP normalization, exact 36×18 ranks for short/long catalogs, and positive probabilities; the dedicated CI must pass before treating the deposited code as verified GitHub regression evidence. No claim of a general Lean-formalized theorem.
