# H109 — Exact Three-Step Mixing of the Original H75 CPTP Source and a Universal Trace-Only No-Go for Any Unitary-Target Linear Intertwiner

**2026-10-19 | P3–P11 Mathematical Bridge / P9.126–128 primary Cartan-source integration; AX-SRC/AX-OA/AX-CAN/AX-SP.**

**Parent:** H108 Draft PR #127, 100/100 GitHub CI PASS. All original P3/H75 finite microarchitecture, source-defined real A/B physical controls, original signed P3 \(R_3\), H75 positive POVMs and published/frozen P1–P8/main remain **unchanged**. P9.126/127 16D and P9.128 48D primary notes were directly located and audited at H108; both use reversible unitary Heisenberg evolution, whereas H75 uses genuine irreversible four-Kraus reset. H109 introduces **no new Hamiltonian, no additional Cartan interaction and no invented source identification**.

## 1. Problem: perhaps a NONfaithful intertwiner survives the H108 source-dynamics No-Go?

H108 ruled out an **injective** full-\(M_6\) linear dynamical intertwiner \(T\Phi_{\rm H75}=\Psi_{\rm P9}T\): H75 has a nonzero kernel, while \(\Psi_{\rm P9}\) is invertible unitary conjugation. It did NOT rule out nonfaithful \(T\), Stinespring dilation, time-dependent maps, one-way reductions, nonautonomous controlled processes, or a restricted physical phase-space construction.

H109 therefore **does not assume injectivity**. For the unchanged autonomous H75 CPTP map \(\Phi:M_6\to M_6\), determine every complex-linear \(T:M_6\to M_N\) satisfying
\[
\boxed{T\Phi=\operatorname{Ad}_{V}T}
\tag{H109-INT}
\]
for an arbitrary FIXED unitary \(V\in U(N)\). This includes the actual finite-time unitary-target maps of the P9.126/127 \(N=16\) and P9.128 \(N=48\) primary Hamiltonians. **This is a narrow direction and notion of intertwiner**: same-time, autonomous, linear on the entire source algebra, with unitary target and no control/memory dilation.

## 2. Original H75 exact reduction and visible quantum channel

The actual four-Kraus reset
\[
L_{ab}=|a\rangle\langle b|_E\otimes UM_a,\quad a,b\in\{0,1\},
\]
has
\[
M_0=\operatorname{diag}(1,3/5,3/5),\quad
M_1=\operatorname{diag}(0,4/5,4/5),\quad
U=\operatorname{diag}(i,1,i)
\begin{pmatrix}2/3&2/3&-1/3\\-2/3&1/3&-2/3\\-1/3&2/3&2/3\end{pmatrix}.
\]
Its true microscopic action is
\[
\Phi(X)=\mathcal J_U(\operatorname{Tr}_E X),\quad
\mathcal J_U(\rho)=\sum_{a=0,1}|a\rangle\langle a|_E\otimes UM_a\rho M_aU^\dagger.
\]
The **actual** qutrit marginal is the unital, trace-preserving and Hermiticity-preserving CP channel
\[
\mathcal V=\operatorname{Tr}_E\mathcal J_U
=\operatorname{Ad}_U\circ \mathcal D,\qquad
\mathcal D(X)_{jk}=c_{jk}X_{jk},
\quad c=\begin{pmatrix}
1&3/5&3/5\\
3/5&1&1\\3/5&1&1
\end{pmatrix}.
\tag{H109-Q}
\]
For every \(n\ge1\),
\[
\boxed{\Phi^n(X)=\mathcal J_U(\mathcal V^{n-1}(\operatorname{Tr}_E X)).}
\tag{H109-FACT}
\]
This is an EXACT identity on all 36 source matrix units; the checker audits the first three iterates of all 36 units and explicitly checks the qutrit marginal on all 9 qutrit units.

## 3. H109.1 — EXACT three-step strict Hilbert–Schmidt contraction on traceless \(M_3\)

Take the genuine Hermitian Hilbert–Schmidt operator basis
\[
B=(E_{00},E_{11},E_{22},
 X_{01},Y_{01},X_{02},Y_{02},X_{12},Y_{12})
\]
over the REAL 9D Hermitian qutrit space. Define the (exact rational real) Gram matrix
\[
G_n^{ij}=\operatorname{Tr}(B_iB_j)-
\operatorname{Tr}(\mathcal V^n(B_i)\mathcal V^n(B_j)).
\tag{H109-GRAM}
\]
Because the visible channel is a unitary conjugation after Schur dephasing with each attenuating cross-\(\{0\}\)–\(\{1,2\}\) entry multiplied by \(3/5\), it is Hilbert–Schmidt contractive:
\[
\|X\|_2^2-\|\mathcal V(X)\|_2^2=
\frac{16}{25}\sum_{j\in\{1,2\}}\big(|X_{0j}|^2+|X_{j0}|^2\big)\ge0.
\]
The checker computes **ALL 81 exact entries** of \(G_1,G_2,G_3\) from the unchanged original H75 U and M_a and establishes
\[
\boxed{
\operatorname{rank}_{\mathbb R}G_1=4,\quad
\operatorname{rank}_{\mathbb R}G_2=7,\quad
\operatorname{rank}_{\mathbb R}G_3=8,\quad
\ker G_3=\operatorname{span}_{\mathbb R}(I_3).
}
\tag{H109-RANK}
\]
The rank-8 kernel statement is an exact Gaussian-rational certificate, not a floating-point spectral approximation. \(G_n\ge0\) follows from stepwise CP-Schur contraction; so \(G_3\) is strictly positive on the 8D traceless real Hermitian sector. Finite-dimensional norm equivalence gives **some** \(0\le q<1\), without needing to invent its value, such that for every complex traceless \(X\in M_3\),
\[
\boxed{\|\mathcal V^{3k}(X)\|_2\le q^k\|X\|_2,\qquad k\ge0.}
\tag{H109-MIX}
\]
Hermitian/anti-Hermitian decomposition carries the real Hermitian contraction into the full complex traceless algebra. In particular \(\mathcal V\) has no nontrivial peripheral eigenoperator, no noiseless noncommutative reversibly transported qutrit algebra, and the only fixed qutrit operator is \(I_3\):
\[
\boxed{
\mathcal V^n(X)\xrightarrow[n\to\infty]{}\frac{\operatorname{Tr}X}{3}I_3.
}
\tag{H109-PRIMITIVE}
\]
This is a **convergence theorem on the actual autonomous visible quantum source**, NOT a statement that the P3 signed residue vanishes at finite depth. The original genuine finite-depth P3 \(R_3\ne0\) remains intact. A one-time H75 output may still contain extensive positive site phase information; infinite-time preservation is a stronger requirement than finite-time tomography.

## 4. H109.2 — EXACT limiting channel of the full six-level irreversible physical source

With the same exact original \(\mathcal J_U\), define the unique stationary microscopic density
\[
\boxed{\sigma_*=\mathcal J_U(I_3/3),\qquad
\Phi(\sigma_*)=\sigma_*,\qquad \operatorname{Tr}\sigma_*=1.}
\tag{H109-FIXED}
\]
The source map \(\Phi^n\) converges as a finite-dimensional linear map to
\[
\boxed{\lim_{n\to\infty}\Phi^n(X)=\operatorname{Tr}(X)\sigma_*.}
\tag{H109-FULL}
\]
This uses the *actual* source reset, not an invented depolarizing channel. The checker confirms the rank-9 first-image, 27D kernel of the first reset, exact first three 36-basis iterates and the stationary state. The long-time limit is rank-one despite the nontrivial finite-time first-image rank9 and signed P3 residue.

## 5. H109.3 — Stronger than H108: any linear full-source intertwiner into reversible P9 unitary dynamics factors through TRACE (EXACT)

Let \(\Psi=\operatorname{Ad}_V\) with any unitary \(V\in U(N)\) (including the actual finite-time unitary \(e^{itH_{P9}}\) for \(N=16,48\)). Suppose **arbitrary**, possibly NONinjective complex-linear \(T:M_6\to M_N\) obeys \(T\Phi=\Psi T\) on **all** \(M_6\) operators. For any traceless \(X\), source mixing gives \(\Phi^n(X)\to0\). But by the intertwiner and unitary Hilbert–Schmidt isometry,
\[
\|T(X)\|_2=\|\Psi^nT(X)\|_2=\|T\Phi^n(X)\|_2\longrightarrow0.
\]
Therefore \(T\) annihilates every traceless matrix, and
\[
\boxed{T(X)=\operatorname{Tr}(X)Y,\quad Y=T(\sigma_*),\quad VYV^\dagger=Y.}
\tag{H109-TRACE-ONLY}
\]
Conversely any target unitary-invariant \(Y\) produces such a (nonfaithful) linear intertwiner. This is an **if-and-only-if classification** of ALL full-source, linear, autonomous one-step H75→fixed-unitary-target intertwiners. Its image dimension is at most ONE complex scalar direction. Even allowing noninjective T does **not** transfer nontrivial H75 source coherences, signed residue or a nondegenerate KKS canonical pair as such an autonomous target dynamical operator.

**Do not overclaim:** A faithful Stinespring **dilation** of a one-step noisy channel necessarily introduces an ancilla and may store information in environment and correlations; it does NOT satisfy this full-M6 intertwiner into unitary P9 on the nose without additional state/trace operations. A time-dependent T, restricted invariant subalgebra, observer quotient or physical nonunitary target might escape the theorem's assumptions. A future physically generated open-system reduction of the 16D/48D P9 source could also exist; H109 has **not** constructed or ruled out all such reductions.

## 6. Typed consequences for P9 and P11 — close the H75→P9 bare-source equality fork

- **AX-SRC:** Two different directly source-verified actual mathematical micro models exist: H75 six-level flag-erasing CPTP and P9.126/127 16-level, P9.128 48-level unitary true CPTP. H108/H109 rule out any informationally nontrivial full-source linear time-homogeneous intertwiner FROM irreversible H75 TO those unitary target dynamics. Therefore the **naïve common-source identification must stop**. Actual physical commonality requires a **newly sourced system–environment dilation/reduction or restricted carrier** with quantified lost information, not simply unitary equality or operator counting.
- **AX-OA:** H107/H108 demonstrated positive phase/separability readouts for selected finite states **conditional on externally supplied detector settings and H105 physical link**. Such finite-time effects are consistent with long-time primitive mixing. The sole recurrent H75 observable transported into a P9 unitary target under H109's whole-operator intertwiner is trace.
- **AX-CAN:** Neither H75 finite local A/B controls, nor an autonomous H75→P9 unitary intertwiner, furnish sourced nondegenerate KKS six-pair physical ADM transport. H105's conditional one-pair link remains independently assumed.
- **AX-SP:** P9 internal SO(3) Wilson holonomy/calibrated rotation and separately imported coframe have a primary source, but physical spatial solder, translational Cartan sector and source-selected torsion-free connection remain OPEN; P9 fixed-diagonal observer-normalizing solder already meets a scoped No-Go.
- **AX-DYN/AX-NORM:** P9.128's autonomous 48D register backreaction is genuine for its declared Hamiltonian but its register/kinetic/Gibbs assumptions are external, its selected Gibbs functional not stationary at torsion-free comparison, and no source-derived DeWitt/Einstein action or continuum off-shell HDA / gravitational scales has been shown.
- **AX-GEN:** F completeness must either derive a new physical coupling/reduction framework that evades the clearly labeled H109 assumptions or accept such a link as an additional axiom. F has NOT proven such a principle yet.

**Status:** H109 three-step qutrit primitive mixing, full six-level rank-one asymptotic, and trace-only classification of ALL linear full-source → unitary-target intertwiners **EXACT, source-scoped**; P9/H75 physical common source, Cartan-to-KKS/ADM six-pair transport and Einstein/F completeness **OPEN**.

**Stopping decision:** Do NOT invent H110 as another arbitrary two-cell entangling gate or reuse exact source-compatibility as physical provenance. The next theorem-worthy positive work needs a **physical source-defined environment/reduction preserving the necessary symplectic and observer data**, or an explicitly justified change of the autonomous intertwiner category. No human specialist review, experiment or Lean Einstein gravity theorem is asserted.
