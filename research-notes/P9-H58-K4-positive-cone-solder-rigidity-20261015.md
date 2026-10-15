# H58 — Rigidity of the Globally Positive K₄ Solder Cone and the P9.64 Symplectic Origin Gate

**2026-10-15 | P3–P11 Mathematical Bridge / P9 GR-I**. Stacked Draft on H57 [PR #76](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/76); H57 parent verified **70/70 CI PASS** before H58. The result is a **finite real-linear automorphism classification** of K₄ edge geometry, conditional on the H52–H57 metric and *externally allowed* solder transformations. It is NOT an independent derivation of physical soldering, a KKS→ADM symplectic map or Einstein dynamics from original P3/P4/P7/P8; P9.64 retains that separate objective. No main/frozen manuscript changes, new Lean kernel proof, expert human referee or experiment.

## 1. Specify the group/action being classified

Let \(S=\mathbf 1^\perp\subset\mathbb R^4\), with H52's nonorthonormal basis \(f_i=e_i-e_3\), Gram matrix \(G=f^\top f\), six K₄ root covectors \(v_{ab}=f^\top(e_a-e_b)\) and rank-one PSD rays \(V_{ab}=v_{ab}v_{ab}^\top\). The invertible six-edge map
\[
L:\mathbb R^6\to\operatorname{Sym}_3,\qquad
L(w)=B(w)=\sum_{a<b}w_{ab}V_{ab}
\]
has determinant \(-256\) in the declared ordered coordinates. The **strict positive K₄ edge cone** is
\[
C_+^\circ=L(\mathbb R^6_{>0}),\qquad
C_+=L(\mathbb R^6_{\ge0}).
\]
For an *externally granted* invertible real \(3\times3\) physical solder transform \(Q\), H57's transition of weights is
\[
B(T_Qw)=A_QB(w)A_Q^\top,\qquad
A_Q=GQG^{-1}.
\]
Equivalently \(T_Q=L^{-1}\circ(B\mapsto A_Q B A_Q^\top)\circ L\). Always invertible as a **linear map on all six signed weights**; not always preserving the strict positive cone. H56/H57 already gave genuine counterexamples for unrestricted shears.

Define the **global positive-preserver condition** as
\[
\boxed{\ T_Q(\mathbb R^6_{>0})\subseteq\mathbb R^6_{>0}\ }.
\]
H58 classifies **all** Q satisfying this condition; **not** merely those mapping one chosen positive w, a small neighborhood, or two overlapping charts into positive weights.

## 2. The H58 rigidity theorem and proof

**Theorem H58.1 (K₄ global positive-cone solder rigidity).** Let \(Q\in GL(3,\mathbb R)\) and \(T_Q\) be as above. The following are equivalent:

1. \(T_Q\) maps the entire strict positive K₄ edge cone **into** itself.
2. \(T_Q\) is a positive scalar times a six-edge permutation induced by one of the **24** K₄ vertex permutations:
   \[
   \boxed{T_Q=\lambda^2P_{\rm edge}(\sigma),\qquad
     \lambda>0,\quad \sigma\in S_4.}
   \]
3. \(Q=cQ_\sigma\) for a nonzero real c and the natural representation
   \[
   \boxed{Q_\sigma=G^{-1}f^\top P_\sigma f}
   \]
   of a vertex permutation \(P_\sigma\) on \(S\), with \(\lambda=|c|\).

Thus a global **into** map is automatically **onto** the strict positive cone. If the solder is restricted to \(GL^+(3,\mathbb R)\), \(c\) must have the same sign as \(\sigma\), because \(\det Q_\sigma=\operatorname{sgn}(\sigma)\) and the S dimension is odd. Equivalently
\[
Q=\lambda\,\operatorname{sgn}(\sigma)Q_\sigma,
\qquad \lambda>0,\quad \sigma\in S_4,
\]
with \(\det Q=\lambda^3>0\). These 24 rays are distinct; the induced group is \(\mathbb R_{>0}\times S_4\) as an abstract mathematical group. Its identity-connected component is only positive common scaling. If the P7 normalization \(h=4G\) must be fixed **exactly**, scaling is additionally restricted to \(\lambda=1\), leaving a finite 24-element group. If physical transformations are limited to **actual orientation-preserving four-site permutations** without the extra internal inversion \(-I_S\), only the even subgroup \(A_4\) is available; neither enlarged physical permission is asserted here.

**Proof:**

(a) From \(T_Qw>0\) for every strictly positive w, take \(w=e_j+\varepsilon\mathbf 1\) and let \(\varepsilon\downarrow0\). Each column of \(T_Q\) is componentwise nonnegative. In matrix language, each rank-one PSD ray \(A_QV_jA_Q^\top\) has a **nonnegative** expansion in the K₄ PSD rays \(V_i\).

(b) A nonnegative sum \(\sum a_iV_i\) with two nonparallel \(v_i\) has rank at least two; since \(A_QV_jA_Q^\top\) is nonzero rank-one, precisely **one** coefficient \(a_i>0\) occurs in each column. Invertibility of \(T_Q\) then forces a **monomial** positive matrix (one nonzero in each column and row). In particular all six root *lines* are permuted.

(c) The six root lines exhibit exactly **four** distinct linearly dependent 3-subsets, corresponding to the four vertex triangles of K₄:
\[
\{01,02,12\},\quad
\{01,03,13\},\quad
\{02,03,23\},\quad
\{12,13,23\}.
\]
Each edge belongs to exactly **two** such triples, and is uniquely specified by the two triangles containing it. Any projective linear root-line symmetry permutes the four triangular circuits, thereby inducing one of at most \(4!=24\) edge permutations, precisely those from the K₄ vertex permutations. The exact checker independently enumerates all \(6!=720\) edge permutations and finds **exactly 24** that preserve the four circuits, all induced by S₄.

(d) Within a triangular circuit the three roots satisfy a relation with coefficients of absolute value one and unique up to overall scaling (e.g. \(v_{ab}-v_{ac}+v_{bc}=0\)). Mapping to another root triangle produces a unique dependence, so the three positive ray coefficients are **equal** after accounting for possible root signs. The K₄ triangle-circuit incidence graph connects all six edges, forcing a **single common** positive ray coefficient \(\lambda^2\). For each \(\sigma\in S_4\) its induced \(Q_\sigma\) realizes the same six projective root-line action with coefficient 1; consequently \(A_Q=\pm\lambda A_{Q_\sigma}\). A linear map fixing every one of the six root lines projectively must be scalar because the four tetrahedral root line circuits span this irreducible rank-three configuration. This proves \(Q=cQ_\sigma\). The converse is immediate and global positivity is automatic.

**Scope:** this theorem is a geometric normalizer classification in the fixed six-ray cone. It does **not** claim the entire continuous physical local-spatial diffeomorphism group arises as K₄ vertex automorphisms, or that such physical frame changes are available in the microscopic response hardware.

## 3. Why small shear overlap is not global preservation

The shear \(Q_s=\begin{pmatrix}1&s&0\\0&1&0\\0&0&1\end{pmatrix}\) at \(s=1/10\) has genuine positive-positive **chart overlap** (H57). But its induced \(T_Q\) has negative entries, e.g.
\[
(T_Q)_{0,3}=-1/10,\qquad
(T_Q)_{2,0}=-9/100.
\]
For a strictly positive input \(w=(1,1,1,10,1,1)\), the first output edge is
\[
\boxed{(T_Qw)_0=-1/5<0}.
\]
By contrast \(T_Q(1,1,1,1,1,1)\) and \(T_Q^{-1}(1,1,1,1,1,1)\) both remain strictly positive. Thus **local atlas transition** and **global cone automorphism** are categorically distinct. The H57 GL⁺ local atlas is still mathematically valid on **overlap domains**; H58 does not discard it, but shows it cannot be treated as a single global positive-cone gauge symmetry.

## 4. Exact canonical cocycle and spatial/time-dependent allowed scale

For a globally preserving \(Q=\lambda\operatorname{sgn}(\sigma)Q_\sigma\), the edge transition is \(v=\lambda^2 P_{\rm edge} w\). The cotangent lift is
\[
\boxed{p_v=\lambda^{-2}P_{\rm edge}p_w,\qquad
p_w^\top\delta w=p_v^\top\delta v.}
\]
This is a canonical/symplectic change of the **externally given ADM** local six-weight chart. The checker verifies nontrivial permutations, common scalings, cotangent three-chart cocycles and exact scalar symplectic pairings. Physical ADM tensor variables and constraint functions are unchanged **provided the solder co-transforms**, including spatial and time derivatives and legitimate boundary conditions.

For a nonconstant smooth positive \(\lambda(x)\) and locally constant vertex permutation \(\sigma\), the weight transition has extra derivatives:
\[
\boxed{\partial_i v=\lambda^2P_{\rm edge}\partial_i w
+2\lambda(\partial_i\lambda)P_{\rm edge}w.}
\]
The compensated physical solder \(Q(x)=\lambda(x)\operatorname{sgn}(\sigma)Q_\sigma\) restores the **same** physical coordinate metric. The checker produces a case with constant A-weights and nonzero B-weight gradient where the raw metric-gradient term **exactly cancels** the frame derivative. A nonflat conformal K₄ weight field has exactly identical metric/neighbor 2-jets, Ricci, Einstein tensor and curvature stencil across such nonconstant gauges (under separately stated smoothness and positivity), and hence identical standard-ADM \(g^{ij}\) structure function and physical momentum boundary current \(J^j=2\pi^{ji}g_{ik}\xi^k\) for the same physical \(g,\pi\).

If an *externally allowed* scale depends on time,
\[
T(t)=\lambda(t)^2P_{\rm edge},\qquad
p_v=T^{-\top}p_w,
\]
then the frame-connection contribution to the Hamiltonian density is
\[
\boxed{
\mathcal H_v=\mathcal H_w+
p_v^\top\dot T T^{-1}v,\quad
p_v^\top\dot T T^{-1}v
=2\frac{\dot\lambda}{\lambda}\,p_w^\top w.
}
\]
The checker gives a nonzero rational witness and verifies the canonical action one-form identity, avoiding an artificial apparent new Einstein evolution. The time-dependent correction is ordinary canonical mechanics, not microscopic CR physics.

## 5. Interface to P9.64 — KKS→ADM provenance remains OPEN

H58 contributes a **target-side rigidity gate**:

- If a P9.64 candidate claims its physical solder **preserves all positive-edge K₄ configurations in one fixed six-ray cone**, its induced frame transition is mathematically restricted to common positive scale times one of the 24 root-line permutations; fixing the P7 \(h\) norm gives only a finite subgroup. A generic continuous shear cannot be such a global symmetry.
- If a candidate instead uses the H57 open atlas of differently soldered local positive charts, the theorem does **not** prohibit the shear. It requires correct overlap/cocycle, derivative and time-frame connections and proper field/boundary gluing. P9.64 must derive or independently justify the physical permission to use those extra solder frames; H58 does not.
- None of these symmetric metric/cone identities supplies the fundamental **antisymmetric** equality \(F^*\Omega_{\rm ADM}=\omega_{\rm KKS}\), nor the proper rank, KKS reduction, physical causal-control interpretation, canonical dynamical intertwiner, full field/functional Poisson construction, or independently derived ADM/EH action. Do not identify the DeWitt supermetric with a symplectic form.
- The existence of the mathematical scalar frame mode \(\lambda(x)\) does **not** assert a dynamical dilaton, spacetime Weyl gauge symmetry, or an additional physical degree of freedom. Here it is simply a compensated solder/chart reparameterization of **the same** metric.

**H59 gate proposal:** use these explicit normalizer conditions as a physical provenance filter on **independently specified** P9.64 KKS/solder candidate generators; check whether accessible microscopic transformations can realize even the finite A₄ subgroup and whether the required symplectic curvature/connection/rank survive overlap. If they cannot, record a precise restricted-sector No-Go rather than postulate arbitrary GL⁺ as physical.

## 6. Exact reproducibility

`P3/P9H58K4PositiveConeSolderRigidityExactCheck.py` executes H52/H53/H57's exact rational geometry; independently enumerates 720 six-edge relabelings and 24 S₄ circuit symmetries, checks every induced 3×3 Q and monomial 6×6 T matrix, exact shear violation of cone positivity, global-cotangent canonical cocycles, nonconstant solder-gradient compensation, nonflat ADM geometric invariants and Hamiltonian frame connection. Dedicated GitHub Actions, stacked Draft/unmerged, no main/frozen edits or actual KKS/physical construction.
