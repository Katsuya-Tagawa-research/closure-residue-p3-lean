# P3–P11 Bridge — H75 AX-OA Control-Compilation and Error Certificate

**2026-10-20 | Draft continuation stacked on #168 | Finite conditional theorem, NOT an independent physical derivation.**

## 1. Original source, admissible mathematical access, and proof scope

Keep the original H75 six-level four-Kraus reset channel on \(\mathcal H=\mathbb C^2_E\otimes\mathbb C^3_S\). From prior H75/H76/H81 audits, independently registered macro-gates are flag mixing \(W=R_{2\times2}(3/5,4/5)\otimes I_3\), flag-controlled site SWAP \(F_{\mathrm{fb}}=|0\rangle\langle0|\otimes I_3+|1\rangle\langle1|\otimes S\), and real site Cayley controls \(V_A,V_B,V_{AB}\), all acting unitarily before one specified H75 reset. Here \(S=S_{01}\) exchanges qutrit sites 0 and 1; \(V_B=(I+(1/2)B)(I-(1/2)B)^{-1}\) on site, \(B=E_{21}-E_{12}\). For the registered alphabet, each \(V_{AB}\) is counted as **one macro-gate**. No autonomous H75 Hamiltonian, continuous hardware drift, pulse amplitudes, or physical pre-reset timing permission is inferred from this algebraic inventory.

Let \(X=Z_E\otimes I_3\), \(Z_E=\operatorname{diag}(-1,1)\), and \(\rho_\pm=I_6/6\pm X/12\), both strictly positive trace-one states. The original reset factors as \(\Phi_\mu=L\circ\operatorname{Tr}_E\). The preceding Draft #168 established via a 781-word exact rational enumeration that depth \(\le4\) is blind to \(X\) and that the depth-5 word
\[
P_5=F_{\rm fb}W V_B F_{\rm fb}W
\]
is the first successful macro-length, chronological \(W\to F_{\rm fb}\to V_B\to W\to F_{\rm fb}\), with a post-reset positive \(Q_1=I_E\otimes |1\rangle\langle1|\) contrast \(\Delta_0=37376/234375>0\).

## 2. ANALYTIC structural necessity: 2 W + 2 F + 1 S-breaking site

**Lemma 1 (need >=2 conditional SWAPs).** With no \(F_{\rm fb}\), all allowed flag \(W\) and site \(V\) commute across subsystems, so every word is a tensor product \(P=U_E\otimes U_S\); \(\operatorname{Tr}_E(PXP^\dagger)=\operatorname{Tr}(U_E Z_E U_E^\dagger)I=0\). With exactly one \(F_{\rm fb}\), write \(P=L F_{\rm fb} R\), where \(L,R\) are products of local flag/site rotations and therefore tensor products. Conjugation by \(R\) gives \(Z'_E\otimes I_3\) with trace-zero \(Z'_E\). Acting with \(F_{\rm fb}\) preserves the *diagonal flag blocks* \(z'_{00} I_3,z'_{11} I_3\); its new off-diagonal blocks do not contribute to \(\operatorname{Tr}_E\). Therefore its partial trace remains zero. Subsequent local \(L\) cannot restore it. Thus any successful word requires **at least 2 F**.

**Lemma 2 (need >=2 flag rotations).** In the absence of \(W\), all gates \(F_{\rm fb},I_E\otimes V\) are flag-block-diagonal and commute with \(X=\operatorname{diag}(-I_3,I_3)\). With exactly one \(W\), write \(P=L W R\), where both \(L,R\) are flag-block-diagonal. Because \(R\) commutes with \(X\), after the unique \(W\) the two diagonal flag blocks are \(c_{00}I_3,c_{11}I_3\) with \(c_{00}+c_{11}=\operatorname{Tr}Z_E=0\). Conjugation by any later flag-block-diagonal \(L\) leaves these diagonal scalar blocks unchanged, so the partial trace stays zero. Thus at least **2 W** are necessary.

**Lemma 3 (need >=1 site operation breaking the SWAP eigenspaces).** Suppose **every** allowed site-local control \(V\) commutes with \(S\). Put \(P_\pm=(I_3\pm S)/2\). Each allowed elementary gate preserves \(\mathcal H_E\otimes P_\pm\mathcal H_S\); restricted to each \(S\)-eigenspace, \(F_{\rm fb}\) acts on the flag only (respectively \(I_E\) or \(\operatorname{diag}(1,-1)\)), \(W\) acts on the flag only, and \(V\) acts on the site only. Hence the entire unitary acts as a tensor product on each \(S\)-eigenspace. Since \(X=Z_E\otimes(I_{P_+}+I_{P_-})\), tracing over the flag gives zero in each sector and therefore globally. Thus an observable \(X\) requires at least **one** site operation \(V\) with \([V,S]\ne0\). The registered \(V_B\) meets this condition. A symmetry-breaking operation is necessary but not sufficient alone.

**Sharp theorem.** The three necessities concern disjoint categories of registered macros, giving \(N\ge2+2+1=5\). The already verified \(P_5\) saturates this bound. This supplies an *analytic explanation* of the exact 781-word result, without claiming optimality among arbitrary new hardware controls, adaptive/multi-reset strategies, or splitting the macro \(V_{AB}\) into other costing conventions.

## 3. Conditional exact Hamiltonian compilation: existence is not provenance

The three generators needed for the saturating word admit explicit finite-matrix Hamiltonians when they are **independently furnished as calibrated controllable ports**:

- Let \(\theta=\arctan(4/3)\), \(\sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}\). For a prescribed duration \(\tau_W>0\), the flag-only Hamiltonian \(H_W=(\theta/\tau_W)\,\sigma_y\otimes I_3\) satisfies \(e^{-iH_W\tau_W}=W\).
- Let \(P_{1,E}=|1\rangle\langle1|\), \(S=S_{01}\). For \(\tau_F>0\), \(H_F=(\pi/(2\tau_F))\,P_{1,E}\otimes(I_3-S)\) satisfies \(e^{-iH_F\tau_F}=F_{\rm fb}\).
- Let \(\varphi=2\arctan(1/2)\), \(B=E_{21}-E_{12}\) (real skew-adjoint). For \(\tau_B>0\), \(H_B=(\varphi/\tau_B)\,I_E\otimes iB\) is Hermitian and satisfies \(e^{-iH_B\tau_B}=V_B\). Its exact rational form is \(V_B=I_E\otimes(I_3+\frac45 B+\frac25 B^2)\).

A piecewise-constant **externally chosen** Hamiltonian schedule \(H_W,H_F,H_B,H_W,H_F\) then compiles the depth-5 channel. This is a finite **conditional construction**, not a proof that H75's autonomous CPTP reset, frozen P6 \(\mathcal J_N\), or \(F:\varnothing\mapsto(\Lambda,\Omega)\) *supplies* these three independent Hamiltonian ports, phase standards, clock/reset permission, or switching controls. An uncontrollably acting H75 reset during these pulses is outside the ideal schedule.

## 4. Robust positive-state signal under independently calibrated errors

Let the ideal five unitary channels be \(\mathcal U_j\) and the final reset be \(\Phi_\mu\), with **CPTP implementations** \(\widetilde{\mathcal U}_j,\widetilde\Phi_\mu\). Assume completely bounded trace/diamond norm deviations \(\|\widetilde{\mathcal U}_j-\mathcal U_j\|_\diamond\le\epsilon_j\), \(\|\widetilde\Phi_\mu-\Phi_\mu\|_\diamond\le\epsilon_R\). Assume independently calibrated strictly positive preparations \(\|\widetilde\rho_\pm-\rho_\pm\|_1\le\alpha_\pm\), and a genuine positive final effect \(0\le\widetilde Q_1\le I\) with \(\|\widetilde Q_1-Q_1\|_\infty\le\eta\). All inequalities concern the *same physical six-level carrier and laboratory frame*.

By the hybrid/telescoping channel inequality, trace-norm contractivity, and \(|\operatorname{Tr}(E Y)|\le\|Y\|_1/2\) for \(0\le E\le I\) and Hermitian trace-zero \(Y\), the observed two-preparation difference obeys
\[
|\widetilde\Delta-\Delta_0|
\ \le\
\sum_{j=1}^5\epsilon_j+\epsilon_R
+\frac{\alpha_++\alpha_-}{2}+2\eta.
\]
Hence its **sign and nonzero distinction are guaranteed** if
\[
\boxed{\sum_j\epsilon_j+\epsilon_R
+\frac{\alpha_++\alpha_-}{2}+2\eta
<\frac{37376}{234375}.}
\]
For six channel maps each bounded by the same \(\epsilon\) and ideal prep/effect, the sufficient test is \(\epsilon<37376/1406250\). These are abstract diamond/trace/operator norm calibration tolerances, **not measured error rates or laboratory feasibility claims**.

## 5. Stronger 24-record informational-completeness calibration gate

The predecessor #167 proves exact rational \(\sigma_{\min}(C_{01})>3/50\) for the **24×18** matrix retaining \(Q_0,Q_1\), expressed in the specified non-Hilbert–Schmidt-orthonormal basis \(B_k\) of \(\operatorname{Herm}(3)\oplus\operatorname{Herm}(3)\). Exactly six \(B_k\) are diagonal projections with \(\|B_k\|_1=1\), and twelve are off-diagonal Hermitian real/imaginary generators with \(\|B_k\|_1=2\); hence \(\sum_{k=1}^{18}\|B_k\|_1^2=6+12\cdot4=54\).

Assume **each** of the 24 calibrated response programs is a physically CPTP product of its prescribed registered pre-reset gates, one H75 reset, and at most one post-reset gate, with *total programmed-channel* diamond discrepancy \(\le E_{\max}\). Each readout has effect-norm discrepancy \(\le\zeta\). For each of the 24×18 entries, the output difference of channels acting on Hermitian \(B_k\) is trace-zero and
\[
|\widetilde C_{rk}-C_{rk}|
\le\|B_k\|_1 (E_{\max}/2+\zeta).
\]
Therefore
\[
\|\widetilde C-C_{01}\|_2\le \|\widetilde C-C_{01}\|_F
\le \sqrt{24\cdot54}\,(E_{\max}/2+\zeta)
=36(E_{\max}/2+\zeta).
\]
By Weyl and #167, **full rank 18 survives** whenever
\[
\boxed{E_{\max}/2+\zeta<1/600.}
\]
If all up-to-five pre gates, the at-most-one post gate and reset are individually bounded in diamond norm by a uniform \(\delta\), then \(E_{\max}\le7\delta\). Under ideal readout calibration \(\zeta=0\), the simple **sufficient, conservative** threshold is \(\delta<1/2100\). Neither inequality is a necessary threshold, a sample-complexity guarantee, or an experimentally measured hardware specification. Separately certified independent prep, complete schedule, frame/phase standards, and gate equivalence are still required.

## 6. Research routing and nonclaims

- **H75/H81/P3–P11 Bridge:** Exact analytic structural necessity and explicit *conditional* five-pulse compilation, plus robust probability/rank sufficient error budgets. Source type and original P3 R3 remain untouched. Draft and unmerged.
- **P9:** The mathematical oscillator/Cartan candidate cannot be called the same physical H75 source merely because some finite unitary Hamiltonians can synthesize its assumed macros. No KKS→ADM, Einstein action, DeWitt negative direction, or off-shell HDA has been shown.
- **P11:** AX-OA Control ports + Scheduling now have testable, independently specifiable *provenance* and *norm* obligations. Producing suitable control matrices by logarithms of imported unitaries **does not prove their generation by F**.
- **Original native-15 GT–K4 metric-descent NO-GO** remains intact: only the augmented catalog admits the #164–#167 conditional 18D reconstruction; no intrinsic metric selection is derived.
- **OPEN:** actual apparatus preparation, clock/reset control, physical native P6 \(\mathcal J_N\), causal hardware sourcing, stable metric near positivity-boundary, source-derived soldering, universal sector, G2/G3 F-access-generation, Generative Completeness, experiment, and human peer review.

Companion checker independently audits the exact matrices, positive-state witness, lower-bound arithmetic and the source-gate distinctions. Algebraic lemmas are proved in this note; CI is a finite regression, not a general Lean theorem.
