# H96 — Finite-Time Lindblad Embedding Obstruction of the Actual H75 Reset, and the Independent DeWitt Kinetic-Signature Gate

**2026-10-18 | P9 GR-I / P3–P11 Mathematical Bridge | Route A (G3/G4).**

**Base:** H95 Draft PR #114, **100/100 GitHub Actions PASS**. This is the terminal source-specific single-reset transport audit—not a new free-standing invented coherent quantum-control model. The original genuine six-level four-Kraus H75 CPTP channel with its original P3 signed diagonal residue, the existing experimental gate catalog, main and frozen P1–P8 remain unchanged.

## 1. What is being asked

H95 proved that a single six-level physical process
\[
\mathcal S\circ\Phi_\mu\circ\mathcal T
\]
with arbitrary fixed deterministic CPTP pre/postprocessors but **no independent information bypass** cannot transmit the entire rank-12 source-seeded H92 Grassmann KKS orbit as a local symplectic immersion: the qutrit reset bottleneck has real differential rank at most 8. H94's multi-copy four-setting positive-POVM tomography is consistent because it is a distinctly labeled *collection of experiments*, not one coherent channel.

H96 asks a **different, stronger dynamical question:** can the **unchanged source reset itself** be the *finite-time* map of an everywhere-bounded, continuous-time GKSL flow on the same microscopic six-level matrix algebra? Does mere positivity of the available response geometry generate the **indefinite** ADM gravitational kinetic Hamiltonian?

The answer to the first is an exact NO-GO under precisely stated conditions. The second requires independently sourced dynamical data and is not derived by P3/F.

## 2. Exact source superoperator kernel and rank (EXACT)

H75's actual four Kraus matrices on \(\mathcal H=\mathbb C^2_E\otimes\mathbb C^3_S\) are
\[
L_{ab}=|a\rangle\langle b|_E\otimes UM_a,\qquad
M_0=\operatorname{diag}(1,3/5,3/5),\quad
M_1=\operatorname{diag}(0,4/5,4/5),
\]
with \(U\) the **unchanged actual H42 complex unitary**. Thus, on *every* \(X\in M_6\),
\[
\Phi_\mu(X)=
\underbrace{\sum_a |a\rangle\langle a|_E\otimes UM_a(\operatorname{Tr}_E X)M_aU^\dagger}_{\mathcal J_U(\operatorname{Tr}_E X)}.
\tag{H96-FACT}
\]
The partial trace \(\operatorname{Tr}_E:M_6\to M_3\) is surjective and has complex rank 9, kernel dimension 27. Conversely \(\mathcal J_U:M_3\to M_6\) is injective because its flag-0 output block \(UM_0ZM_0U^\dagger\) is injective: \(M_0\) is invertible. Therefore
\[
\boxed{\operatorname{rank}_{\mathbb C}\Phi_\mu=9,\quad
\dim_{\mathbb C}\ker\Phi_\mu=27,\quad
\ker\Phi_\mu=\ker\operatorname{Tr}_E.}
\tag{H96-RANK}
\]
A concrete normalized Hilbert–Schmidt-norm-one kernel operator is
\[
\boxed{X_0=|0_E,0_S\rangle\langle1_E,0_S|=E_{0,3},\
\|X_0\|_2=1,\quad \Phi_\mu(X_0)=0.}
\tag{H96-KERNEL}
\]
The checker uses **all 36 matrix units** of the actual original channel and independently Gaussian-eliminates the exact Gaussian-rational \(36\times36\) superoperator matrix to rank 9. It also verifies an explicit independent 27-element kernel basis (nine \(|0,i\rangle\langle1,j|\), nine reverse, and nine block-population differences \(|0,i\rangle\langle0,j|-|1,i\rangle\langle1,j|\)), as well as unchanged original H75 P3 \(R_3\neq0\). No approximations, surrogate signed residues or renamed source channel.

## 3. H96.1 — NO finite-time bounded GKSL generator equals this reset (EXACT scoped NO-GO)

**Theorem.** On the fixed finite-dimensional Banach space \(M_6\), let \(\mathcal L_s:M_6\to M_6\) be a bounded piecewise-continuous real-time generator on \(0\le s\le t<\infty\), including every bounded finite-dimensional time-dependent GKSL generator. Its propagator \(\Psi_t\) solves
\[
\frac d{ds}\Psi_s=\mathcal L_s\Psi_s,\qquad
\Psi_0=\operatorname{id}_{M_6}.
\]
Then \(\Psi_t\) is an **invertible linear operator on \(M_6\)** at every finite \(t\). Its inverse need not be CPTP; linear invertibility alone is sufficient. Therefore
\[
\boxed{\Psi_t\neq \Phi_\mu,\qquad 0<t<\infty.}
\tag{H96-GKSL}
\]
The conclusion holds a fortiori for a fixed bounded Lindblad semigroup \(\Psi_t=e^{t\mathcal L}\) and a unitary Hamiltonian conjugation \(\Psi_t(X)=V_tXV_t^\dagger\). The original source reset's **rank-9** map has 27 kernel directions, while any finite-time fundamental solution on unchanged \(M_6\) has full complex rank **36**.

This does **not** contradict P1. P1 studies the local continuous-time limit of a **differentiable near-identity CPTP family**. H75's fixed reset is a legitimate finite discrete CPTP channel which is **not** the finite-time exponential of any bounded generator on the unchanged full microscopic algebra. Quantum instruments, partial-trace/reinitialization, singular endpoint rates, arbitrarily long relaxation and Hilbert-space enlargement with discard are outside the theorem's continuous-time fixed-\(M_6\) reversible-linear-propagator class. None of those alternative mechanisms is thereby proved to source ADM dynamics.

## 4. H96.2 — Quantitative cost of approaching the singular reset (EXACT)

Let \(\|\mathcal L_s\|_{2\to2}\le K(s)\) with finite \(A_t=\int_0^tK(s)\,ds\), using the **Hilbert–Schmidt induced norm** on linear maps \(M_6\to M_6\). Grönwall's inequality on the inverse fundamental solution gives
\[
\|\Psi_t^{-1}\|_{2\to2}\le e^{A_t}.
\]
For the exact Hilbert–Schmidt unit kernel vector \(X_0\),
\[
\begin{aligned}
\|\Psi_t-\Phi_\mu\|_{2\to2}
&\ge\|(\Psi_t-\Phi_\mu)(X_0)\|_2\\
&=\|\Psi_t(X_0)\|_2
\ge e^{-A_t}.
\end{aligned}
\]
Hence
\[
\boxed{\|\Psi_t-\Phi_\mu\|_{2\to2}\ge
\exp\!\left[-\int_0^t\|\mathcal L_s\|_{2\to2}\,ds\right].}
\tag{H96-LOWER}
\]
In the homogeneous case \(\|\mathcal L\|_{2\to2}\le K\), an error \(\varepsilon<1\) requires
\[
\boxed{Kt\ge\log(1/\varepsilon).}
\tag{H96-COST}
\]
So bounded integrated generator strength prohibits **arbitrarily precise** finite-time approximation to the exact reset. This bound is general for this singular source and uses **the actual nonzero original H75 kernel operator**, not a formal divergence metaphor. It does not assert a universal positive approximation gap if \(Kt\) is allowed to diverge.

For unitary Hamiltonian superoperator flow, \(\|\Psi_t(X_0)\|_2=1\) exactly, hence \(\|\Psi_t-\Phi_\mu\|_{2\to2}\ge1\).

A useful exact scalar comparison is \(\gamma(t)=e^{-kt}\) on a kernel direction: it is positive for all finite \(t\), can approach zero as \(kt\to\infty\), but it cannot **be** zero under bounded integrated flow. This comparison does not assert that such a damping semigroup reproduces all of H75 \(\Phi_\mu\).

## 5. H96.3 — ADM DeWitt kinetic form independently needs one negative mode (EXACT algebraic gate; OPEN provenance)

At a physical 3D spatial metric chart \(g=I_3\), the ADM gravitational momentum quadratic form (suppressing the conventional positive \(1/\sqrt g\) factor) is
\[
\boxed{\mathscr K_{\rm DW}(\pi)
=\pi_{ij}\pi_{ij}-\frac12(\operatorname{tr}\pi)^2,
\quad\pi=\pi^\top\in\operatorname{Sym}(3).}
\tag{H96-DW}
\]
In independent real tensor entries \(p=(\pi_{11},\pi_{22},\pi_{33},\pi_{12},\pi_{13},\pi_{23})\), its symmetric quadratic-form matrix (half the ordinary Hessian) is
\[
D=\begin{pmatrix}
1/2&-1/2&-1/2&0&0&0\\
-1/2&1/2&-1/2&0&0&0\\
-1/2&-1/2&1/2&0&0&0\\
0&0&0&2&0&0\\
0&0&0&0&2&0\\
0&0&0&0&0&2
\end{pmatrix}.
\]
The \(3\times3\) diagonal block is \(I_3-\frac12\mathbf1\mathbf1^\top\); its quadratic-form-matrix eigenvalues are \(1,1,-1/2\), and the three off-diagonal modes have eigenvalue 2 each. The actual coordinate Hessian is \(2D\), with eigenvalues \(2,2,-1,4,4,4\); both matrices have the same inertia. Thus
\[
\boxed{\operatorname{inertia}(D)=(5+,1-),\quad
\det D=-4.}
\tag{H96-SIGN}
\]
The **negative conformal trace mode** is \(\pi=aI_3\):
\(\mathscr K_{\rm DW}(aI_3)=-\frac32 a^2\).
The traceless modes are all positive. For any \(g>0\), the momentum tensor undergoes an invertible real congruence plus positive scalar prefactor, so the inertia stays \((5+,1-)\).

A positive Fisher/K4 response metric or any positive-definite quadratic \(F>0\) cannot be transformed into \(D\) by a **configuration-preserving invertible real momentum change** \(F\mapsto B^\top FB\) (Sylvester's inertia theorem). However, this does **NOT** prove that every possible microscopic Hamiltonian must have positive kinetic Hessian; a genuinely sourced Hamiltonian might independently have an indefinite kinetic term. H96 establishes a **necessary dynamical sign test**, not an impossibility theorem for all future F/P3 axioms.

The checker exactly computes all six quadratic-form eigen-directions, determinant \(-4\), positive traceless and negative trace witnesses, and a rational positive-congruence comparison. This is an independent finite audit, **not** a derivation of GR from the H75 source.

## 6. Direct P9/P11 proof handoff: stop replacing physics by observation rank

**P9 G3:** the fixed actual H75 reset cannot be a finite-time bounded GKSL/Hamiltonian automorphism on the unchanged six-level microscopic state algebra. Its loss of KKS rank cannot be healed by writing \(\Phi_\mu=e^{t\mathcal L}\) with a finite bounded \(\mathcal L\) or by longer unaugmented deterministic postprocessing. A genuine physical sourced **non-reset/historical carrier with an actual accessible symplectic tangent and Hamiltonian** is required for full rank-12 KKS→ADM transport. The *literal* ADM map must intertwine both symplectic structure and dynamics and be spatially/gauge covariant.

**P9 G4:** once a source Hamiltonian exists, test its **physical momentum Hessian** in the independently justified ADM configuration polarization. The target DeWitt Hessian must have one negative and five positive directions, **not** six positive Fisher directions. Proving only rank12 KKS, local Darboux existence, tomography or scalar acoustic-velocity matching does not pass this gate.

**P9 G5/G6:** derive full *nonuniform off-shell* H–H/H–D/D–D constraints, physical spatial gluing/boundaries and Einstein–Hilbert/field equations **without importing standard ADM as an axiom and calling it generation**. Existing H56/H83 conditional comparisons remain not full CR-origin Einstein dynamics.

**P11:** either formalize a physical \(\Omega\)/history memory that **survives the H75 partial-trace loss with an explicit sourced storage channel**, or state that the original H75 finite source cannot furnish the desired coherent whole. \(F:\varnothing\to(\Lambda,\Omega)\) needs actual typed selection rules for physical process, interaction, memory, polarization and action rather than merely the ability to fit finite rank signatures.

### Verdict / stopping rule

| Item | Verdict |
|---|---|
| Original H75 CPTP superoperator exact rank9 and kernel27 | **EXACT** |
| Finite-time bounded Markov/GKSL flow on unchanged \(M_6\) equals \(\Phi_\mu\) | **NO-GO** |
| Sharp general inverse-propagator norm lower bound \(e^{-A_t}\) on approximation error | **EXACT** |
| ADM 6-component DeWitt momentum kinetic form inertia \(5+,1-\) | **EXACT as standard ADM algebra**, independent gravitational premise |
| Source-derived 12D KKS-preserving Hamiltonian transport and DeWitt Hamiltonian | **OPEN** |
| Source-derived full nonuniform off-shell HDA / Einstein equations / F completion | **OPEN** |

**H96 closes the source-specific single-reset mathematical audit**. The next research task must concern actual physical coherent/field transport or a precise new F axiom—not an indefinitely enlarged series of reset tomography toy models. No new Lean kernel proof, experiment, human expert referee or Einstein equation is claimed.
