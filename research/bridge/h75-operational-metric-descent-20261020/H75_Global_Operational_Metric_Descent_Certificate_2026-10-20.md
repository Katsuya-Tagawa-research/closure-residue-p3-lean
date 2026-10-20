# P3–P11 Mathematical Bridge — H75 Global Operational Metric Descent under Extended AX-OA Access

**2026-10-20 | conditional finite theorem and exact-rational certificate | no H/AX number assigned.**

## Executive conclusion

A finite, explicit, 36-probability AX-OA *extension* of the H75/H81 quantum instrument catalog is **informationally complete on the full real vector space** \(\operatorname{Herm}(3)\oplus\operatorname{Herm}(3)\) of six-level block-diagonal microscopic input operators. Thus its restriction to any fixed \(U(3)\times U(3)\) KKS orbit is injective. Any assigned GT–\(K_4\) metric map \(g\) on that orbit (or on its domain of definition) factors *uniquely* through the augmented operational record. This establishes **set-theoretic global metric descent conditional on the declared access catalog**; it does not establish hardware feasibility, F-generated provenance, intrinsic metric selection, or Einstein gravity.

**Crucial distinction:** the reported independent fixed-orbit NO-GO for the original native 15-vector remains EXACT as communicated by the independent auxiliary auditor. The new theorem uses a strictly *stronger* 36-outcome catalog, which independently requires pre-reset controlled pulses. The prior 15-vector and GT metric full formulas were not independently fetched/recomputed in this certificate; no metric values need be known to prove factorization through an injective observation map.

## Mathematical source and precise protocols

Work on \(\mathcal H_\mu=\mathbb C^2_E\otimes\mathbb C^3_S\), environment-flag-first basis. The H75 source \(\Phi_\mu\) is the four-Kraus CPTP instrument, with
\[
K_{ab}=|a\rangle\langle b|\otimes UM_a,\quad
U=\operatorname{diag}(i,1,i)
\begin{pmatrix}2/3&2/3&-1/3\\-2/3&1/3&-2/3\\-1/3&2/3&2/3\end{pmatrix},
\]
\[
M_0=\operatorname{diag}(1,3/5,3/5),\quad M_1=\operatorname{diag}(0,4/5,4/5).
\]
The H76/H81 flag rotation and flag-conditional system SWAP (called \(F_{\mathrm{fb}}\), **not** the generative map \(F\)) are
\[
W=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}\otimes I_3,
\qquad F_{\mathrm{fb}}=|0\rangle\langle0|\otimes I_3+|1\rangle\langle1|\otimes S_{01}.
\]
The H75 independent real Cayley exchange ports are
\[
V(x,y)=I_E\otimes \bigl[(I+xA)(I-xA)^{-1}(I+yB)(I-yB)^{-1}\bigr],
\]
where \(A=E_{01}-E_{10},\ B=E_{21}-E_{12}\) on the visible qutrit. Define \(V_A=V(1/4,0)\), \(V_B=V(0,1/2)\), and \(V_{AB}=V(1/4,1/3)\). All these are rational **unitaries**, and the three final readouts \(Q_j=I_E\otimes |j\rangle\langle j|\) are positive projectors.

Prepare an arbitrary *block-diagonal* Hermitian input \(X=\operatorname{diag}(B_0,B_1)\). Use one of four pre-reset protocols:

| Label | Chronological gate sequence before the mandatory source reset | Algebraic unitary |
|---|---|---|
| P0 | No pre-reset operation | \(I_6\) |
| P1 | \(F_{\rm fb}\) | \(F_{\rm fb}\) |
| P2 | \(V_A\to F_{\rm fb}\) | \(F_{\rm fb}V_A\) |
| P3 | \(W\to F_{\rm fb}\to V_B\to W\to F_{\rm fb}\) | \(F_{\rm fb}W V_B F_{\rm fb}W\) |

After a **single** application of \(\Phi_\mu\), apply one of \(T\in\{I_6,V_A,V_{AB}\}\), then measure one of \(Q_0,Q_1,Q_2\). This makes \(4\times3\times3=36\) scalar probabilities:
\[
R_{a,b,j}(X)=\operatorname{Tr}\!\left[Q_j T_b\,\Phi_\mu(P_a X P_a^\dagger)\,T_b^\dagger\right].
\]
**These settings have not been certified as a physically executable complete pre-reset hardware schedule.** In particular P3 extends H81's original S0/S1 schedule by interleaving a pre-reset real site pulse between flag gates. This is an independently specified AX-OA access assumption, not a theorem from H75's uncontrolled channel or P3's residue.

## Exact full-domain injectivity theorem and reproducible certificate

For \(\mathcal V=\operatorname{Herm}(3)\oplus\operatorname{Herm}(3)\cong\mathbb R^{18}\), choose basis \(E_{ii}\), \(E_{ij}+E_{ji}\), \(i(E_{ij}-E_{ji})\) in each flag block. The above 36 linear functionals define a matrix \(C\in\mathbb Q^{36\times18}\).

**Theorem:** \(\operatorname{rank}_\mathbb Q C=18\). In particular, for **every** pair \(X,Y\in\mathcal V\),
\[
R_{\rm aug}(X)=R_{\rm aug}(Y)\quad\Longrightarrow\quad X=Y.
\]

**Proof/certificate:** exact SymPy rational row reduction selects 18 independent physical effects, with zero-based indices
\[
(0,1,2,3,6,7,9,10,12,15,18,19,21,24,25,27,28,33).
\]
The rational \(18\times18\) submatrix is included as `H75_Global_Access_18x18_Certificate.csv`. Each denominator is invertible modulo prime \(p=1,000,000,007\). Dependency-free rational modular elimination returns
\[
\boxed{\det(C_{18})\bmod p=39,156,989\neq0.}
\]
If a rational matrix were singular over \(\mathbb Q\), its reduction modulo any prime not dividing denominators would be singular. This nonzero modular determinant therefore proves the rational matrix is nonsingular. Incremental ranks for P0, P0–P1, P0–P2, and P0–P3, each with the same 3 post controls and site POVMs, are exactly \(6,10,15,18\).

The checker also reconstructs the **user-supplied fixed-orbit pair** with identical block characteristic polynomials, verifies \(\Phi_\mu(\sigma-\rho)=0\), and exhibits nonzero contrast in the new 36-record vector, consistent with prior pairwise calculations.

## Global metric descent theorem, smoothness and stability

Let \(\mathcal O\subset\mathcal V\) be any fixed block-diagonal \(U(3)\times U(3)\) coadjoint orbit. Let \(X_g\subseteq\mathcal O\) be the subset where the chosen GT–\(K_4\) metric \(g:X_g\to\mathrm{SPD}(3)\) is actually defined (and positive). Since \(R_{\rm aug}|_{X_g}\) is injective, the **unique function on the measured image**
\[
\bar g:R_{\rm aug}(X_g)\to \mathrm{SPD}(3),\qquad
\bar g(R_{\rm aug}(x))=g(x)
\]
exists; no separate GT formula is needed for this factorization. It is not a canonical extension to all \(\mathbb R^{36}\), and does not select a unique physically preferred \(g\).

Since the observation map is the restriction of an injective linear map on \(\mathcal V\), it is a smooth embedding of the orbit into \(\mathbb R^{36}\) when the orbit is a smooth manifold. Any smooth \(g\) on its domain descends smoothly to the embedded image. The restricted linear left inverse \(L:C(\mathcal V)\to\mathcal V\) is bounded, and in an orthonormal Hermitian basis \(\|x-y\|\le\|L\|\|R_{\rm aug}(x)-R_{\rm aug}(y)\|\). If \(g\) is Lipschitz (e.g. smooth on a compact domain under suitable regularity), then \(\bar g\) is Lipschitz with constant at most \(\operatorname{Lip}(g)\,\|L\|\). This is **mathematical stability for perfectly calibrated records**; it is not a bound against experimental uncertainty in the apparatus or a source-origin certificate.

The original native 15-vector NO-GO is untouched: its fibers are coarser. Stronger, schedule-dependent access refines them to singleton fibers in the block-diagonal state space. This is a conditional sufficiency certificate, not minimality, not a necessity theorem for P11 AX-OA's five clauses, and not a CR-exclusive experimental prediction.

## Classification and export

| Claim | Status |
|---|---|
| Existing H75/H81 CPTP/Kraus and real unitary gates, positive readouts | EXACT finite model |
| 36-outcome augmented record full rank on Herm(3) ⊕ Herm(3) | **EXACT: rank 18**, rational modular certificate |
| Set-theoretic metric descent on fixed KKS orbit, metric defined there | **CONDITIONAL EXACT** on the new catalog |
| Smoothness / Lipschitz stability for metric | CONDITIONAL on regularity of metric / calibration |
| Hardware preparation and lengthy pre-reset schedule (AX-OA) | **OPEN** |
| Injectivity on arbitrary all-36-dimensional Hermitian \(M_6\), including flag coherences | **NOT CLAIMED** |
| Independent check of original native-15 vector, GT metrics, g positivity globally | **NOT PERFORMED** |
| Origin of the chosen metric, P6 source controls, F-generated access G2/G3 | **OPEN** |
| P7/P8 soldering, KKS→ADM, DeWitt, off-shell HDA, Einstein | **OPEN** |

**Suggested research handoff:** send this conditional global descent theorem to P9 and P11 with its complete exact certificate. P9's earlier native-readout NO-GO and observed rank information remain untouched. P11 should treat the long pre-reset hardware schedule as a hard provenance gate, not a derived fact. No H/AX number, Notion edit, GitHub PR, or frozen manuscript changes are made by this standalone auxiliary audit.

## Sources

- [H75 original microscopic source and controls (Draft PR #94)](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/94)
- [H81 access/scheduling (Draft PR #100)](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/100)
- [H82 integration baseline (Notion)](https://app.notion.com/p/3fd736b71e2d8198a5d0f4a3260064c8)
- User-supplied fixed-orbit GT–K4 native descent independent audit, 2026-10-20.
