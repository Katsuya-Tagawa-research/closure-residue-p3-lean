# H60 — Diagonal-Observer Rank Bottleneck and Quadratic K₄ Cycle Ambiguity at a Generic U(4) KKS Basepoint

**2026-10-15 | P3–P11 Mathematical Bridge → P9.64 GR-I.** Stacked on H59 Draft PR #78. H59 established local rank compatibility (a generic U(4) orbit has real tangent dimension 12) but a compact-orbit/global-exact-target symplectic No-Go; it also found the repaired odd S₄ unitary fails to preserve the fixed four-site diagonal population observer MASA. H60 investigates a separate, **single-time measurement information bottleneck**. No microscopic P3 residue provenance or Einstein dynamics is claimed.

## 1. Precise domain and observer

Take the **H59 independently selected comparator**, not the physically certified microscopic source,

\[
\rho_*=\operatorname{diag}(1,2,3,4)/10,\quad
\mathcal O=\{U\rho_*U^\dagger:U\in U(4)\},
\quad\dim_{\mathbb R}\mathcal O=12.
\]

Let \(D_4\) be the diagonal MASA, and define its ordinary quantum population observer

\[
\mu_D:\mathcal O\to\mathbb R^4,\qquad
\mu_D(\rho)=(\rho_{00},\rho_{11},\rho_{22},\rho_{33}),\quad
\sum_a\mu_D(\rho)_a=1.
\]

**Theorem H60.1 (single-snapshot population rank obstruction).** For every \(\rho\), \(\operatorname{rank}D\mu_D\leq 3\). Hence if the six K₄ spatial metric coordinates \(q^I\), \(I=1,\dots,6\), are stipulated to depend smoothly *only on* \(\mu_D(\rho)\) at a single instant, the map \(\rho\mapsto(q^1,\dots,q^6)\) cannot be a local submersion onto an open six-metric region. This is an observer-factorization No-Go, **not** a No-Go for general mappings that use coherences, interventions, multiple times or hidden response data.

Proof: trace preservation places all populations in an affine three-plane, giving differential rank at most three. The chain rule preserves this bound. H52's positive K₄ six-weight-to-symmetric-metric map has rank six, so the necessary surjectivity fails.

**Theorem H60.2 (first-order silence at the diagonal comparator basepoint).** At \(\rho_*\), every orbit tangent vector has the form \([K,\rho_*]\), with \(K^\dagger=-K\). Since \(\rho_*\) is diagonal,

\[
\boxed{\operatorname{diag}[K,\rho_*]=0,\qquad
D\mu_D\vert_{\rho_*}=0.}
\]

The full 12-dimensional KKS tangent is invisible to this *instantaneous, first-order diagonal* observer at this particular basepoint, notwithstanding nondegeneracy of the KKS 2-form. Do not extrapolate this basepoint statement to all orbit points or multi-time response.

## 2. Exact second-order signal and incidence-factorization theorem

For \(\rho(t)=e^{tK}\rho_*e^{-tK}\) and \(r_{ab}=|K_{ab}|^2\geq0\) (\(a<b\)), the diagonal evolution is

\[
\rho_{aa}(t)=\lambda_a+t^2 c_a(K)+O(t^3),\quad
\boxed{c_a(K)=\sum_{b\neq a}(\lambda_b-\lambda_a)|K_{ab}|^2}.
\]

Equivalently, \(\ddot\rho_{aa}(0)=2c_a(K)\). Orient all six edges of \(K_4\) from lower to higher site labels. Let \(B\in\mathbb R^{4\times6}\) be the oriented incidence matrix, with +1 at the lower endpoint, -1 at the higher endpoint. Define \(\delta_e=\lambda_b-\lambda_a>0\), \(D_\delta=\operatorname{diag}(\delta_e)\), and \(r=(r_e)\). Then

\[
\boxed{c=B D_\delta r,\quad
\operatorname{rank}(B D_\delta)=3,\quad
\dim\ker(B D_\delta)=3.}
\]

**Theorem H60.3 (quadratic population-cycle ambiguity).** Three independent triangles through vertex 0, namely \((0,1,2),(0,1,3),(0,2,3)\), generate the rank-three cycle space of \(K_4\). For any \(v\in\ker B\) and any sufficiently small \(\epsilon\),

\[
r'=r+\epsilon D_\delta^{-1}v>0
\quad\Longrightarrow\quad
BD_\delta r'=BD_\delta r.
\]

Thus there are **continuously many strictly positive edge-amplitude-square patterns** indistinguishable by the leading quadratic diagonal-population coefficients at the diagonal basepoint.

An explicit all-rational witness: choose \(r=(1,1,1,1,1,1)\) in edge order
\((01,02,03,12,13,23)\), and the triangle cycle \(v=(+1,-1,0,+1,0,0)\), \(\epsilon=1/100\). Then

\[
r'=(11/10,19/20,1,11/10,1,1)>0,
\qquad B D_\delta r'=B D_\delta r.
\]

Each positive \(r_e\) is physically realizable *mathematically* as the squared modulus of a skew-Hermitian infinitesimal Hamiltonian generator entry: \(K_{ab}=\sqrt{r_{ab}}\), \(K_{ba}=-\sqrt{r_{ab}}\). Thus the witness concerns honest U(4) infinitesimal controls in a comparator, not merely formal signed edge weights. It makes no assertion that the **entire** population trajectories are equal beyond the displayed order.

## 3. Why the ambiguity matters to the H52/H58 K₄ metric target

In the H52 basis \(f_i=e_i-e_3\subset\mathbf1^\perp\), let \(T=[f_1\ f_2\ f_3]\) be the 4×3 basis matrix and define \(v_{ab}=T^T(e_a-e_b)\), \(B_w=\sum_{a<b}w_{ab}v_{ab}v_{ab}^T\) and

\[
g_w=16G B_w^{-1}G,\qquad G=f^Tf.
\]

H52 proved, and the H60 standalone checker independently recomputes, the **linear isomorphism** from six edge coefficients to \(\operatorname{Sym}^2(S)\): its 6×6 flattening matrix has determinant \(-256\) and rank 6. If a *candidate* microscopic assignment sets \(w_e=r_e\), the distinct positive patterns \(r\) and \(r'\) yield distinct positive definite spatial metrics \(g_r\neq g_{r'}\) despite identical quadratic diagonal populations.

Therefore, **that candidate assignment cannot be reconstructed from the second-order population data alone**. This does **not** assert that \(w_e=|K_{ab}|^2\) is independently derived from P3/P6, nor that every possible KKS→ADM identification must fail. It is a controlled identifiability obstruction under an explicitly declared factorization.

## 4. Conditional recovery with non-diagonal X/Y channels

For \(a<b\),

\[
\delta\rho_{ab}=[K,\rho_*]_{ab}
=(\lambda_b-\lambda_a)K_{ab}.
\]

Since the six spectral gaps are nonzero, the six complex off-diagonal entries (both real and imaginary parts: all-pair \(X/Y\) coherence readouts) supply real tangent rank \(2\times6=12\). In this *ideal informationally complete tangent model*, each \(K_{ab}\) is recoverable from first-order off-diagonal data. This algebraic recovery does **not** establish that the P6 physical observer/control protocol actually permits all such channels, independently calibrates dephasing, or implements the KKS symplectic source and P9 solder.

H60 is compatible with earlier P9 finite comparator work: population-only reconstruction is blocked under its stated data restrictions; enhanced X/Y channels can remove that **specific** rank obstruction while leaving KKS topology, actual physical accessibility, symplectic pullback, Hamiltonian intertwining and HDA unresolved. H60's ordinary-U(4) quadratic response is **not** a CR-specific experimental discriminator or the original P3 signed residue.

## 5. Handoff to P9.64 / next gate

1. Declare the **actual** microscopic orbit/stabilizer, spectral degeneracy, observer MASA and permitted P6 controls. Do not silently equate the H59 comparator orbit with the genuine P3/P6 source.
2. Test whether the proposed gravitational edge weights or six configuration variables factor through a single-time population map; if so, H60.1 blocks local full-six-coordinate coverage. If they depend on second-order population coefficients alone at the diagonal basepoint, H60.3 supplies an exact three-dimensional cycle ambiguity.
3. If using coherences or multi-time readout, declare and verify these operational channels and their nuisance/calibration constraints, then test whether they resolve the cycle ambiguity with **independent accessible data**.
4. Only then test an explicit local pullback \(\mathcal F^*\Omega_{\mathrm{ADM}}=\omega_{\mathrm{KKS}}\), admissible S₄ solder/observer equivariance, patch gluing, and a dynamical Hamiltonian/constraint intertwiner. H59's **global exact-target obstruction still applies** if its premises hold.
5. Separate any conditional ADM kinematics from nonuniform-field off-shell HDA and independent CR-origin Einstein dynamics, which remain open.

**Verification:** `python3 P3/P9H60DiagonalObserverK4CycleAmbiguityExactCheck.py` uses only standard-library `fractions.Fraction`. It checks the exact commutator expansion for a rational skew generator, the rank-3 incidence factorization, three linearly independent cycles, two positive indistinguishable patterns, independent H52 six-to-six metric injectivity and the 12-real-rank X/Y tangent channel. The universally quantified mathematical claims additionally follow from the displayed trace/incidence/chain-rule proofs; enumerating examples alone is not the proof.

**Status boundary:** Standalone mathematical Draft, stacked on H59; not merged, not human peer reviewed or experimentally confirmed. No frozen P1–P8 papers or main modified. No P9.64 success assertion.
