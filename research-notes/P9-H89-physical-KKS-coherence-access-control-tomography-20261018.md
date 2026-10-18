# H89 — Physical Access to the Coherence-Completed KKS Observer: Exchange/Phase-Port Tomography, Real-Control Blindness, and the ADM Provenance Gate

**2026-10-18 | P3–P11 Mathematical Bridge / P9 GR-I / Route A (Constructive).**

**Base:** H88 Draft PR #107 with **H88 new mathematical CI PASS** (full workflow rollup to be checked independently). H87 was **100/100 CI PASS**. H75's genuine six-dimensional microscopic CPTP source and original P3 residue remain **untouched**. H89's four-level U(4) coadjoint model and four separately posited physical single-excitation cells are **independently declared**. No mathematical or physical identification of this KKS orbit with the original H75 source, frozen P6 control sector or ADM phase space is claimed.

## H89.1 — A fully positive finite measurement certificate for all 15 su(4) coordinates (CONDITIONAL EXACT)

Consider the nondegenerate four-level quantum density register of H87/H88 with \(\rho_\star=\mathrm{diag}(2/5,3/10,1/5,1/10)\) and the six unordered cell pairs \(a<b\). Let
\[
d_a=\mathrm{Tr}(\rho E_{aa}),\quad
x_{ab}=\mathrm{Tr}(\rho X_{ab}),\quad
y_{ab}=\mathrm{Tr}(\rho Y_{ab}),\qquad
X_{ab}=E_{ab}+E_{ba},\quad Y_{ab}=-i(E_{ab}-E_{ba}).
\]
Assume the **separately calibrated, individually selectable** physical two-site gates, extended by identity on other sites, with \(c=3/5,\ s=4/5\):
\[
U^{(Y)}_{ab}|_{\{a,b\}}=
\begin{pmatrix}c&-is\\-is&c\end{pmatrix},\qquad
D_b=\operatorname{diag}(1,-i)_{\{a,b\}},\qquad
U^{(X)}_{ab}=D_bU^{(Y)}_{ab}D_b^\dagger
=\begin{pmatrix}c&s\\-s&c\end{pmatrix}.
\]
Each gate is unitary and each corresponding channel \(\rho\mapsto U\rho U^\dagger\) is CPTP; every final \(P_a=E_{aa}\) is a genuine positive projector readout. The gate \(U^{(Y)}\) is the same rational Cayley-type exchange-port pulse as H86 (when such a **physical nonlocal port** is independently available), whereas \(D_b\) additionally requires a calibrated **on-site phase** resource. Thus no nonlocal interaction is being silently derived from local controls.

Define the legitimate one-bit positive outcome probabilities
\[
p^{X}_{ab}(\rho)=\mathrm{Tr}(P_aU^{(X)}_{ab}\rho U^{(X)\dagger}_{ab}),\quad
p^{Y}_{ab}(\rho)=\mathrm{Tr}(P_aU^{(Y)}_{ab}\rho U^{(Y)\dagger}_{ab}).
\]
Direct matrix multiplication yields exact **all-state** identities:
\[
\boxed{p^{X}_{ab}=\frac9{25}d_a+\frac{16}{25}d_b+\frac{12}{25}x_{ab},\qquad
p^{Y}_{ab}=\frac9{25}d_a+\frac{16}{25}d_b+\frac{12}{25}y_{ab}.}
\tag{H89-Q}
\]
By measuring \(d_0,d_1,d_2\) directly, using \(d_3=1-d_0-d_1-d_2\), and applying one **separately selected** gate/readout setting for each \(p^X_{ab}\) and \(p^Y_{ab}\), all fifteen affine trace-one quantum-state coordinates are reconstructed:
\[
\boxed{x_{ab}=\frac{25p^X_{ab}-9d_a-16d_b}{12},\qquad
y_{ab}=\frac{25p^Y_{ab}-9d_a-16d_b}{12}.}
\tag{H89-INV}
\]
The **15-by-15** readout Jacobian, ordered by three independent diagonals, six x's and six y's, has determinant
\[
\boxed{\det D\mathsf M=(12/25)^{12}\ne0.}
\]
Exact Gaussian-rational and Fraction tests check the 15-outcome physical instrument construction on genuinely positive unitary-orbit states, every 6-pair identity, all-state linear operator identities (via the basis of \(M_4\)), and complete affine tomography. The user of the formula still needs **physical availability** of individually selectable edge exchange gates, calibrated phase knobs, independently prepared copies of the *same* state and projective population measurement. Those requirements were already the substantive AX-OA gap in H81/H84/H86 and are **not** consequences of H88 mathematical Lie–Poisson closure.

The theorem does **not** assert that fifteen is an information-theoretic global minimum of all possible POVMs, that the H75 flag-qutrit source supplies a U4 register, or that six independent **literal physical edges** are mandatory if controls can synthesize remote two-level rotations by allowed sequences.

## H89.2 — The exact real-control observer blind spot (EXACT scoped operational No-Go)

Suppose instead the operational catalog allows **only real orthogonal gates** \(O\in O(4)\), real matrices for all Kraus operators/instruments, and real diagonal population or other real symmetric positive readouts. For *any finite adaptive sequence* of such real operations and readouts, its corresponding positive history effect is a real symmetric matrix (a sum of \(K^\top K\) over real history Kraus products \(K\)). Therefore the probability of every history is insensitive to the purely imaginary antisymmetric Hermitian part of the initial quantum state:
\[
\boxed{\mathrm{Tr}(E\rho)=\mathrm{Tr}(E\,\operatorname{Re}\rho),\qquad E=E^\top\in M_4(\mathbb R).}
\tag{H89-REAL}
\]
Choose the two physically genuine \(\rho_{\pm t}=U_{02}(\pm t)\rho_\star U_{02}(\pm t)^\dagger\) of H87 for any small \(t>0\). Their real matrix parts coincide, their imaginary 02 coherences have opposite signs, and their Poisson brackets satisfy
\[
\boxed{
\{x_{01},x_{12}\}(\rho_{+1/2})=-24/125,\quad
\{x_{01},x_{12}\}(\rho_{-1/2})=+24/125.
}
\]
All real-only experimental histories are **strictly indistinguishable** on these states. In particular every direct population and every \(p^X\) agrees. The catalog is not Poisson-projectable to all desired microscopic KKS response brackets. This statement excludes complex exchange pulses \(U^{(Y)}\), site phase gates or external complex coherence instruments; it does **not** apply to H89.1's complete catalog.

This is a conventional complex-phase observational symmetry, **not** a new CR-specific experimental prediction, nor proof that general full quantum tomography is impossible.

## H89.3 — The strict on-site/exchange/phase control hierarchy (EXACT ALGEBRA; conditional hardware)

- **Only on-site unitary ports acting on independent physical qubits** preserve product structure, so cannot generate an entangling two-cell exchange; H86's limited No-Go remains.
- **Independent coherent \(X_{ab}\) exchange ports** supply a genuinely nonlocal Hamiltonian \(H_{ab}\) acting in the declared one-excitation register, and the exact \(U^{(Y)}=\exp(-i\theta X_{ab})\) gate with \(\cos\theta=3/5,\sin\theta=4/5\), *if* that Hamiltonian can actually be switched/calibrated. An on-site phase \(D_b\) then conjugates it to \(U^{(X)}\); both quadratures become measurable via positive population POVMs.
- **Connected graph controllability theorem (conditional):** On a four-level one-excitation space, assume independently **selectable real exchange Hamiltonians** on the edges of a connected graph and independently selectable diagonal phase Hamiltonians \(Z_a\) (arbitrary controllable strengths and signs, not a single immutable pulse). The real Lie algebra generated by \(iX_{ab}\) on accessible edges and \(iZ_a\) equals \(\mathfrak u(4)\) (or \(\mathfrak{su}(4)\) if global phase is dropped). Indeed, diagonal commutators yield independent \(iY_{ab}\) on each physical edge; successive commutators along paths yield \(iX_{ac}\) and \(iY_{ac}\) on all vertex pairs, and \([X_{ab},Y_{ab}]\) spans traceless diagonals. Hence the full 15 real traceless Hermitian observables are Lie generated. A disconnected graph preserves a nontrivial block decomposition and cannot generate arbitrary pair mixing. Exact Fraction rank/commutator closure and disconnected control-rank witnesses are included.
- **Lie algebraic controllability ≠ physical apparatus provenance:** The controls must be actual independently certified Hamiltonian ports, timing/pulse calibration must be valid, the four-level sector must be invariant or leakage controlled, the H75 source reset must not invalidate a required gate sequence, and coherent phase references must survive. An abstract Lie closure also does **not** prove an efficient finite-length exact synthesis protocol for all requested pulses under arbitrary duration/bandwidth restrictions.

Thus a connected **certified interaction graph** plus independently accessible onsite phases is mathematically sufficient for full four-level quantum-state tomography, but neither connectedness nor controllable couplings is selected by P3/F. It is **not** necessary to assume all six literal intercell ports are independently hardware-wired if a sufficiently rich connected control network is truly available.

## H89.4 — From physically measured KKS coordinates to canonical ADM: still a generative gate

Given H89.1's independent hardware premises, the acquired 15 quantum expectation coordinates allow the **entire four-level density matrix** to be reconstructed; on the independent nondegenerate U4 orbit, the full KKS Poisson tensor can therefore be evaluated and H88's local twelve-response Poisson closure can be operationally probed within declared apparatus scope. A Darboux six-pair coordinate chart can be **chosen mathematically** and expressed as local nonlinear functions of the recovered state. This is an exact **conditional observer reconstruction**, not a physical ADM identification.

The following remain **OPEN**:
1. Actual microphysical source \(\Phi_\mu\) \(\to\) invariant four-level U4 KKS sector, independently calibrated spatial graph and all its coherent ports; specifically the H75 flag \(\mathbb C^2_E\otimes\mathbb C^3_S\) is **not** silently replaced by \(\mathbb C^4\).
2. Why one chosen **six-dimensional involutive** local Darboux configuration observable subalgebra rather than another is physically selected, and how it maps to *physical* spatial \(g_{ij}\) (P7/P8 solder).
3. Physically sourced conjugate ADM momenta, KKS–ADM symplectic intertwining on a noncompact patch or justified reduction, with H59 global KKS topological obstruction respected.
4. Correct DeWitt \((5+,1-)\) gravitational kinetic Hamiltonian selection, constraints/lapse/shift (H61), nonuniform field gluing and all three full off-shell ADM H–H/H–D/D–D relations (H56/H83).
5. Einstein–Hilbert/Einstein equations derived from \(F\) or original CR data and a CR-only physical experimental discriminator.

**P11 handoff:** H89 sharpens the independent AX-OA threshold: an observable mathematically present in \(\mathfrak{su}(4)\) becomes a **physically accessible** generator only with a concrete certified control/readout schedule (such as H89.1); real-only hardware can provably erase precisely the imaginary components that restore H88's Poisson closure. Generative completeness would require \(F\) to select or imply the *apparatus interaction/phase catalog*, not merely allow a formal su4 Lie–Poisson algebra on paper. Nothing in H89 shows that an abstract successful operational catalog uniquely originates from F.

## 5. Verdict and stopping rule

| Claim | Verdict |
|---|---|
| Six exchange-mixer settings, six phase-conjugated settings and three populations reconstruct any four-level density | **CONDITIONAL EXACT**, valid positive effects and invertible exact rational calibration |
| Real-gate/real-instrument observer can distinguish conjugate complex coherent KKS states | **NO-GO** within all finite real Kraus histories |
| Connected selectable exchange graph plus local phases generates all \(\mathfrak{su}(4)\) infinitesimal directions | **EXACT ALGEBRA**, conditional physical port assumptions |
| Physical four-level state/Poisson reconstruction solves canonical ADM or Einstein dynamics | **NO**; **OPEN** gravitational provenance |
| H75/P3/F derive hardware ports, phases, source sector, spatial solder, DeWitt, HDA, Einstein or F completeness | **OPEN** |

**Research exit recommendation:** Treat H89 as a finite operational KKS-closure **conditional success** and send exact missing-provenance requirements to the P9/P11 core programs. Avoid unbounded H90+ toy rank studies unless new source-dependent cross-cell controls and gravitational dynamics have actually been proved.

**Audit:** Exact positive-state/instrument Gaussian-rational tomography, globally valid all-matrix effects, real-only indistinguishability, connected graph Lie rank15 vs disconnected block-rank8 (including u1 centers appropriately), and inherited H80–H88 programs in CI. Independent AI/code audit is **not** human expert peer review, Lean formalization, physical experiment or P9 GR-I minimum success.
