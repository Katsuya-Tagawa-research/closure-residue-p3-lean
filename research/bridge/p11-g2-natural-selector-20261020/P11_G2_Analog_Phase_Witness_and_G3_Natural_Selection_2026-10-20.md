# P11 G2/G3: Analog Phase Witness and Gauge-Natural Access Selection

**2026-10-20 | P3–P11 Mathematical Bridge | Draft stacked on #172**

## The physical-origin problem remains OPEN

The original H75 6D CPTP source, its P3 closure–residue tensors and the endpoint gate definitions do **not** contain a physical grant of continuously tunable Hamiltonian control. #172 showed a strict separation:
- finite endpoint coherent unitary words \(\langle W,F_{\mathrm{fb}},V_A,V_B,V_{AB}\rangle\subset O(6)\);
- **conditionally imported** analog ports with generators \(J_W,J_F,J_B\) have dynamical Lie algebra \(\mathfrak u(6)\), provided independently controlled pulse time and drift/reset suppression.

This note (i) gives a *strictly positive-POVM* operational tester separating fixed real endpoints from a single fractional control pulse, and (ii) proves the general equivariant/gauge-natural selection criterion applicable to a future intrinsic \(\mathrm{GenAcc}_F\). It does **not** show that the original H75 hardware contains the tester, that F generates analog control, or that the formal gauge example is an actual symmetry of the H75 dynamics.

## I. EXACT positive phase tester on the same six-level carrier

Let \(S=E_{01}+E_{10}+E_{22}\) on the qutrit, \(P_-=(I_3-S)/2\), \(P_{1,E}=|1\rangle\langle1|\) on the flag, and \(P=P_{1,E}\otimes P_-\), a real rank-one orthogonal projector on \(\mathbb C^6\). The original conditional SWAP endpoint and its **additional fractional-pulse** analog are
\[
F_{\mathrm{fb}}=I_6-2P,\qquad
U_{1/2}=e^{(\pi/4)J_F}=I_6+(i-1)P,\quad
J_F=i\,P_{1,E}\otimes(I_3-S)=2iP.
\]
Hence \(U_{1/2}^2=F_{\mathrm{fb}}\) and \(U_{1/2}\) is unitary but not real up to any global phase: it acts as \(1\) on the five-dimensional \(P^\perp\) and \(i\) on the one-dimensional \(P\) sector.

Define mutually orthogonal **real** site unit vectors
\[
u=|2\rangle,\qquad v=(|0\rangle-|1\rangle)/\sqrt 2,
\quad Su=u,\ Sv=-v,
\]
and the real source-prepared state and externally phase-sensitive positive effect
\[
|\psi\rangle=|1\rangle_E\otimes(u+v)/\sqrt2,\quad
|\chi_i\rangle=(u+iv)/\sqrt2,\quad
Q_i=I_2\otimes|\chi_i\rangle\langle\chi_i|.
\]
\(\rho=|\psi\rangle\langle\psi|\) belongs to the **flag-block-diagonal 18-real-dimensional H75 input domain**, though it is pure rather than full-rank; \(Q_i\) is a genuine positive rank-two projection on six levels and \(\{Q_i,I-Q_i\}\) is a complete binary POVM.

The analog half pulse gives \(U_{1/2}|\psi\rangle=|1\rangle\otimes|\chi_i\rangle\), so
\[
\boxed{\operatorname{Tr}(Q_i U_{1/2}\rho U_{1/2}^\dagger)=1.}
\]
In contrast, for **every real orthogonal coherent unitary** \(O\in O(6)\), the output vector \(r=O|\psi\rangle\) is real. Writing \(r=|0\rangle\otimes r_0+|1\rangle\otimes r_1\), where \(r_0,r_1\in\mathbb R^3\) and \(\|r_0\|^2+\|r_1\|^2=1\), one has
\[
\begin{aligned}
\langle r|Q_i|r\rangle
&=\frac12\sum_{a=0,1}
\big[(u^T r_a)^2+(v^T r_a)^2\big]\\
&\le\frac12\sum_a\|r_a\|^2
=\frac12.
\end{aligned}
\]
Therefore
\[
\boxed{
p_{\mathrm{analog}}(Q_i|\rho)=1
\quad>\quad
\sup_{O\in O(6)} p_{\mathrm{real\ endpoint}}(Q_i|O\rho O^\dagger)
=\frac12.
}
\]
The supremum is attained by the identity endpoint (giving exactly \(1/2\)). Hence **no possible finite endpoint word, regardless of length, matches this analog phase output in the same state-and-effect tester**. The gap \(1/2\) is exact and does not rely on floating point, an informationally complete measurement, or a spectral estimate.

**Critical scope:** this tester measures **directly after the coherent pulse and before any H75 reset**, because the reset destroys specified flag information. The imaginary-phase-sensitive \(Q_i\) is **NOT** among the previously authorized real-site \(Q_j\) POVMs of #164–#172. A new independently calibrated phase readout is required for a physical discrimination experiment; the source cannot be credited with supplying it. The mathematical rank-18 reconstructions of #164–#171 did not certify such a measurement. This is a conditional ordinary-QM tester, **not a CR-exclusive observable**. The "same source" statement means the unchanged original H75 four Kraus operators can be retained *for other legal interventions*, while this tester omits that reset from its own program.

## II. EXACT necessary-and-sufficient symmetry/equivariance selection criterion

Let \(G\) be a finite group representing accepted changes of presentation or a gauge/relabeling symmetry, acting on a finite set \(\mathsf S\) of prior source/F-data and on a finite set \(\mathsf O\) of typed operational-access candidate classes. Let \(\mathcal A_s\subseteq\mathsf O\) be the **nonempty set of permitted candidates** for each \(s\in\mathsf S\), with compatibility/naturality of the relation:
\[
\mathcal A_{g s}=g\,\mathcal A_s\quad
(\forall g\in G,s\in\mathsf S).
\]
Call a deterministic selected access **gauge-natural** if \(\sigma:\mathsf S\to\mathsf O\) satisfies
\[
\sigma(s)\in\mathcal A_s,\qquad
\sigma(g s)=g\sigma(s).
\]

**Theorem (equivariant selector iff stabilizer-fixed candidate):**
\[
\boxed{
\exists\,G\text{-equivariant }\sigma
\ \Longleftrightarrow\
\forall s \in \mathsf S/G\text{ orbit representatives},
\quad \mathcal A_s\cap\mathsf O^{G_s}\ne\varnothing,
}
\]
where \(G_s=\{g\in G:g s=s\}\), and \(\mathsf O^{G_s}=\{o\in\mathsf O:\forall h\in G_s,\ h o=o\}\).

*Proof (necessity):* if \(\sigma\) is equivariant and \(h s=s\), then \(h\sigma(s)=\sigma(h s)=\sigma(s)\). Thus the chosen candidate is fixed by the source stabilizer.

*Proof (sufficiency):* independently choose one \(o_s\in\mathcal A_s\cap\mathsf O^{G_s}\) for each source orbit representative and define \(\sigma(gs)=g o_s\). If \(g s=g' s\), then \(g'^{-1}g\in G_s\) fixes \(o_s\), so the value is independent of the chosen orbit representative word. Naturality of the candidate relation guarantees \(\sigma(gs)\in\mathcal A_{gs}\); equivariance follows by construction.

**EXACT two-point symmetry NO-GO benchmark.** Take \(G=\mathbb Z_2\), a single source \(s\) fixed by its entire group, and two candidate accesses \(\mathsf O=\{o_+,o_-\}\) interchanged by the nontrivial group element. Set \(\mathcal A_s=\{o_+,o_-\}\). Then \(\mathsf O^{G_s}=\varnothing\), so no deterministic equivariant selector exists even though each candidate is individually valid. Adding an *independently supplied* orientation/phase label to the prior data can break the source stabilizer and remove the obstruction; adding labels is not the same thing as proving they were generated by F. A randomized or set-valued symmetric output may be mathematically possible, but is not automatically a single physically realized preparation/control/schedule certificate.

**Do not overstate the benchmark:** it is an abstract G-set counterexample, *not* a demonstrated nontrivial stabilizer group of the original H75 source or of the actual Generative Map F. For a theorem about a specific P11 F candidate, the G-action, accessible candidate relation, and stabilizers must first be physically and mathematically identified.

## III. The combined G2/G3 proof obligation — mathematical checklist

Any candidate \(F\mapsto\mathrm{GenAcc}_F\) must at minimum:
1. **Type its resource outputs:** distinguish fixed endpoint executable words from analog Hamiltonian pulses with independently tunable duration/amplitude, reset scheduling and phase-oriented readout.
2. **Prove source-fibre faithfulness**, as in #170–#171, rather than demand the same F-data magically select source-identical apparatuses with distinct external authorization.
3. **Prove naturality under the declared representation/gauge changes:** the stabilizer criterion above is a necessary-and-sufficient finite selection test.
4. **Give prior-generation/provenance evidence** for any extra orientation/phase/time/interaction resource; merely choosing such a label to match a desired KKS/ADM metric or P6 observer is circular.
5. **Distinguish a conditional mathematical tester from hardware access:** the new \(Q_i\) POVM is an independent additional readout, not a native H75 positivity readout.

These statements do not establish the five-part AX-OA independence/unique minimality, any new human peer review, a physical P6 \(\mathcal J_N\), native-15 GT–K4 descent, P7/P8 soldering, ADM/HDA/Einstein, or P11 Generative Completeness. The original source H75/PR #94 and all main/frozen/published P1–P8 remain unchanged.

**Status:** exact finite tester and general elementary equivariant-selector theorem, plus *conditional* physical-phase access. Companion exact SymPy checker checks the explicit matrices, POVM projections, real-channel inequality algebra and finite \(\mathbb Z_2\) no-go. Dedicated CI is a regression check, not a general Lean formalization. Draft/unmerged.
