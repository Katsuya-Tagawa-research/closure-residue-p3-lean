# H86 — Physical Exchange Ports Produce a Second-Jet Graph Laplacian: Local-Control No-Go, Coherent Sign Gap, and Conditional K4 Metric

**2026-10-18 | P3–P11 Mathematical Bridge / P9 GR-I / Route A (Constructive).**
**Base:** H85 Draft PR #104, **98/98 GitHub Actions PASS**. This paper-stage note initiates a *physical interaction-port / spatial response* gate, not a claim to have sourced intercell exchange from P3 or the generative map F. H75's genuine original microscopic \(\Phi_\mu\) and \(R_2=0,R_3=i\operatorname{diag}(-32,16,16,0,0,0)/135\neq0\) remain unchanged, with no main or frozen P1–P8 edits. The **four distinct physical cells** here are separately posited; they are not automatically identified with the four internal vertices of P7/P8's K4 carrier.

## 1. H86.1 — Strictly on-site coherent control cannot synthesize a genuine two-cell interaction (EXACT, scoped No-Go)

Take four separately identified physical Hilbert spaces \(\mathcal H_i\), with a catalog of **on-site Hamiltonians only**:
\[
H_{\rm loc}(t)=\sum_{i=0}^{3} I_0\otimes\cdots\otimes h_i(t)\otimes\cdots\otimes I_3.
\]
Here there is **no** shared environment, intercell Hamiltonian, entangling measurement, global postselection or feedback-mediated nonlocal gate. Hamiltonians on disjoint tensor factors commute and their Lie brackets remain sums of on-site operators; thus their dynamical Lie algebra is contained in
\[
\bigoplus_{i=0}^{3}\mathfrak u(\mathcal H_i).
\]
The propagator factors as \(U_{\rm loc}(t)=\bigotimes_iU_i(t)\) (even for independently time-dependent local drives), and maps product preparations to product states. In particular, a coherent exchange
\[
X_{ij}=|1_i0_j\rangle\langle0_i1_j|+
       |0_i1_j\rangle\langle1_i0_j|
\]
cannot be synthesized as a genuine interaction by such purely local unitary switches. It produces entanglement from localized one-excitation product inputs when pulsed nontrivially. The obstruction does **not** apply once a shared bath, global instrument, pre-entangled resource, nonlocal feedback or physical cross-cell port is independently introduced. This is standard quantum-control locality, not a CR-only No-Go.

Hence H75 single-cell CPTP data, P3 signed residues, H84 marginal channels, or H85 A4 affine weight assignments **do not automatically provide** this nonlocal Hamiltonian. A physical microscopic **edge-port certificate** is a necessary extra premise for this construction.

## 2. H86.2 — Conditional exchange Hamiltonian and the EXACT positive Laplacian in population second jets

Independently suppose there are four calibrated physical qubits (or two-level sectors of four *separately encoded* qutrit cells), with controllable, time-independent **real, symmetric**, excitation-preserving two-cell exchange Hamiltonian
\[
H_{\rm ex}(J)=\sum_{0\le i<j\le3}J_{ij}
(\sigma_i^+\sigma_j^-+\sigma_i^-\sigma_j^+),\qquad J_{ij}\in\mathbb R.
\]
It acts on the one-excitation sector \(V_1=\operatorname{span}\{|i\rangle:i=0,\dots,3\}\) exactly as
\[
H_J=\sum_{i<j}J_{ij}(E_{ij}+E_{ji}),\qquad(H_J)_{ii}=0.
\]
The actual **microscopic four-cell coupling ports, two-level embeddings, their accessibility before/after H75 resets, and all localized preparations** are independently supplied physical premises. This is a legitimate ordinary-QM cross-cell Hamiltonian, but it is *not* obtained by taking tensor powers of the uncontrolled H75 source.

For any genuinely prepared positive **diagonal** one-excitation state \(\rho_p=\sum_i p_iE_{ii}\) (where \(p_i\ge0\), \(\sum_i p_i=1\)), let \(p_i(t)=\operatorname{Tr}(E_{ii}e^{-itH_J}\rho_p e^{itH_J})\). Direct double-commutator calculation gives
\[
\dot p_i(0)=0,\qquad
\boxed{\ddot p_i(0)=2\sum_{j\ne i}J_{ij}^2(p_j-p_i).}
\tag{H86-JET}
\]
Writing \(w_{ij}=J_{ij}^2\ge0\) and the weighted Laplacian \(L_w=\sum_{i<j}w_{ij}(e_i-e_j)(e_i-e_j)^\top\), this is
\[
\boxed{\ddot{\boldsymbol p}(0)=-2L_w\boldsymbol p.}
\tag{H86-L}
\]

**Proof.** The quantum dynamics gives \(\ddot\rho(0)=-[H_J,[H_J,\rho_p]]\). Its diagonal entry is \(2\sum_j(H_J)_{ij}(H_J)_{ji}(p_j-p_i)\), yielding the identity. \(\square\)

This **second-order population response** is an exact physical certificate of a positive symmetric weighted graph form (conditional on calibrated real exchange). It is **NOT a Markov generator for the true populations**. Coherences intervene away from \(t=0\); e.g. a two-cell single-edge coherent pulse yields \(p_j(t)=\sin^2(J_{ij}t)\), whose first derivative at zero is zero, unlike a continuous-time Markov diffusion. Do **not** interpret H86-L as a derived GKSL semigroup, intrinsic spacetime propagation law or Einstein equation.

### Physical readout reconstruction (CONDITIONAL EXACT)

For independently available localized positive preparations \(\rho=E_{jj}\) and ordinary positive site-projector measurements \(E_{ii}\), \(i\ne j\),
\[
\boxed{w_{ij}=J_{ij}^2=
\tfrac12\,\left.\frac{d^2}{dt^2}\operatorname{Tr}
\bigl(E_{ii}e^{-itH_J}E_{jj}e^{itH_J}\bigr)\right|_{t=0}.}
\tag{H86-W}
\]
All **six nonnegative edge weights** (including absence of edges as \(w_{ij}=0\)) are therefore recoverable from the six calibrated independent short-time population measurements, **under the fixed exchange-only template and the required preparations/readouts**. For \(J=(1,2,3,4,5,6)\) in edges \((01,02,03,12,13,23)\), the resulting Laplacian is
\[
L=\begin{pmatrix}
14&-1&-4&-9\\
-1&42&-16&-25\\
-4&-16&56&-36\\
-9&-25&-36&70
\end{pmatrix}.
\]
The exact checker verifies the double-commutator identity for a rational nonuniform positive state and all four localized preparations.

This is a *physical source-to-response calculation* starting from a **declared interaction Hamiltonian**, not P3-only generation of an interaction.

## 3. H86.3 — Strict positivity, connectedness and the metric-generation boundary (EXACT graph theory; CONDITIONAL spatial interpretation)

For nonnegative \(w\), the real quadratic form satisfies
\[
x^\top L_wx=\sum_{i<j}w_{ij}(x_i-x_j)^2\ge0.
\]
The restriction \(L_w|_S\) to \(S=\mathbf1^\perp\subset\mathbb R^4\) is strictly positive definite **if and only if** the active edge graph \(\{ij:J_{ij}\ne0\}\) is connected. Equivalently \(\operatorname{rank}L_w=3\) on four vertices. A connected path with three nonzero edges suffices; full six-edge K4 connectivity is not needed.

Only after declaring a **physical solder** that identifies this response carrier \(S\) with spatial tangent directions may one define the conditional P9 K4 response metric
\[
\boxed{g_{J^2}=16\,(L_{J^2}|_S)^{-1}.}
\]
On uniform complete K4 with every \(J_{ij}^2=1\), \(L=4P_S\) and \(g=4I_S\), matching P7/P8's uniform metric normalization **algebraically**. For a disconnected graph, \(L|_S\) is singular, and this inverse metric construction fails. These are comparator statements, **not** an independent derivation of a 3D spatial manifold, Lorentzian response envelope, Einstein-Hilbert action or universal spacetime.

## 4. H86.4 — Population second jets lose coherent edge-sign / loop-phase information (EXACT limited No-Go)

The map \(J\mapsto L_{J^2}\) forgets every edge sign. This can lose **physically nontrivial** information, not just a basis sign convention. Consider the full K4 real symmetric \(H_+\) with **all six** offdiagonal couplings \(J_{ij}=+1\), and \(H_-\) with \(J_{01}=-1\) and the other five \(+1\). Both produce **exactly the same** \(L_{J^2}=4P_S\), all localized population second derivatives and conditional uniform metric \(g=4I_S\).

Nevertheless their gauge-invariant three-cycle products differ:
\[
\boxed{\operatorname{tr}(H_+^3)=24,\qquad
       \operatorname{tr}(H_-^3)=0.}
\]
Thus these are not even unitarily conjugate Hamiltonians on the one-excitation space (and not related by local site phase redefinitions). Their distinct coherent loop data cannot be recovered from the population **second jets** alone. This is *not* a universal impossibility for higher-time-order or coherent data.

**Coherent access repair, independently assumed:** If one can prepare the phase-referenced **entangled across-cell** one-excitation state
\[
|\psi_{ij}\rangle=(|i\rangle-i|j\rangle)/\sqrt2
\]
and measure the positive site-occupation projector \(E_{ii}\), then
\[
\boxed{
\left.\frac d{dt}\operatorname{Tr}
[E_{ii}e^{-itH_J}|\psi_{ij}\rangle\langle\psi_{ij}|e^{itH_J}]
\right|_{0}=J_{ij}.
}
\tag{H86-SIGN}
\]
This identifies even the signs under a common calibrated coherence-phase convention. Preparing this intercell superposition **is itself a strong additional quantum-accessibility resource**, generally not obtainable from only local unitary ports starting from product states. A phase-reference convention and actual positive quantum preparation/readout must be part of AX-OA. This is an exact conventional quantum-control fact, not a CR-exclusive signature.

## 5. H86.5 — Genuine finite rational coherent edge CPTP pulse (EXACT CONDITIONAL CONSTRUCTION)

For one independently certified edge port with \(J_{ij}=1\), define the exact rational Cayley pulse on \(\operatorname{span}\{|i\rangle,|j\rangle\}\)
\[
U_{ij}=(I-\tfrac i2 X_{ij})(I+\tfrac i2 X_{ij})^{-1}
=\frac35 I-\frac{4i}{5}X_{ij},
\]
extended by identity on the orthogonal complement. It is a genuine **unitary** gate, so \(X\mapsto U_{ij}XU_{ij}^\dagger\) is CPTP. On the genuine product one-excitation state \(|i\rangle\) in the physical four-cell qubit embedding,
\[
U_{ij}|i\rangle=\frac35|i\rangle-\frac{4i}{5}|j\rangle.
\]
The ordinary positive site-\(j\) projector gives exact probability \(16/25\). The two affected cells have a nonzero entangled Schmidt pair \((3/5,4/5)\), negativity \(12/25\), which no local-only product-unitary catalog can create from this input. The **finite Cayley pulse parameter** is an independently controlled laboratory assumption; there is still no source-only theorem supplying this port.

## 6. Integration ledger and P9/P11 exit conditions

| Claim | Verdict |
|---|---|
| Strictly independent on-site unitary controls generate a genuine intercell exchange gate | **NO-GO** under the stated restricted control Lie algebra |
| Declared real exchange Hamiltonian \(\to\) \(p''(0)=-2L_{J^2}p\) | **CONDITIONAL EXACT**, analytic identity and exact Fraction check |
| Localized positive populations recover every **nonnegative squared** exchange coefficient | **CONDITIONAL EXACT** with sufficient preparations, clock calibration and projector readouts |
| Laplacian invertible on \(S\) iff active spatial candidate graph connected | **EXACT**, standard weighted graph theorem |
| Laplacian alone determines signed physical exchange / loop phase | **NO-GO**, exact \(H_+\)/\(H_-\) spectral-moment counterexample |
| Coherent phase-referenced entangled preparations recover signs | **CONDITIONAL EXACT**, separate AX-OA requirement |
| Coherent finite rational physical entangling edge gate exists | **EXACT CONSTRUCTION**, only after postulating a nonlocal port |
| Exchange, cell adjacency, true physical solder, DeWitt sector, off-shell full HDA, Einstein dynamics derived from original P3/F | **OPEN** |

**P9 handoff:** H86 supplies a cleaner *conditional microscopic physical Hamiltonian \(\to\) graph response \(\to\) positive algebraic metric* bridge than simply choosing six weights. But squared exchange response is **not** the ADM canonical symplectic pairing, DeWitt \((5+,1-)\) gravitational kinetic form, nonuniform spatial field derivative operator or exact H–H/H–D/D–D off-shell constraint closure. Source the **cross-cell port and solder** before claiming any physical gravity. No conflict with H56/H59/H61's conditional/no-go gravity gates.

**P11 handoff:** H81 AX-OA must include genuine **intercell interaction ports**, their causal availability before source resets and entangling/coherent preparation resources where sign reconstruction is required. H84 and H85 showed local-process and symmetric-weight nonidentifiability. H86 sharpens the independent physical premise: P3-only on-site controlled source cannot synthesize a nonlocal exchange through local unitary Lie closure. A new *source-derived* coupling-selection axiom/theorem \(F\Rightarrow H_{\rm ex}(J)\) is the missing generative obligation.

**Reproducibility:** Standalone exact Fraction Gaussian elimination / matrix algebra checker verifies second jets, spectrum/loop obstruction, connectedness criterion examples, phase-sensitive sign response and rational Cayley amplitude; H85–H80 exact regressions run in CI. Draft and unmerged, no human expert referee/experimental confirmation or additional Lean formalization.

**Exit recommendation:** Unless a genuinely independently sourced intercell dynamics law becomes available, **do not** continue inventing physical couplings merely to enlarge H87+. Redirect major proof effort to P9's independently sourced KKS→ADM/DeWitt/HDA dynamics and P11's AX-OA/F-generative completeness axiomatization.
