# H55 — Conditional ADM Canonical Chart in K₄ Edge-Weight Variables

**2026-10-15 | P3–P11 Mathematical Bridge / P9 GR-I.** Draft stacked on H54 [PR #73](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/73). All H55 results are **ordinary ADM canonical GR written in the exact H52–H54 local six-edge K₄ metric chart**. They require an **externally supplied** smooth spatial 3-manifold, physical K₄-to-\(TM\) solder with coordinate-compatible gluing, a 3+1 foliation, lapse/shift, standard ADM action, canonical brackets and boundary conditions. None of these physical premises are derived from original P3/P4 or frozen P6/P7/P8. The source is not a CR-exclusive observable and not a proof of spacetime/Einstein emergence. No main/frozen manuscripts changed; no Lean kernel, human journal referee or real experiment.

## 1. Exact local cotangent lift of the six K₄ weight coordinates

Write \(e\in E(K_4)\) for the six edges, and retain the **nonorthonormal** spatially soldered basis \(f_i=e_i-e_3\) of \(S=\mathbf1^\perp\subset\mathbb R^4\):
\[
G=f^\top f=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix},\qquad
B(w)=\sum_e w_e v_ev_e^\top,\qquad
\boxed{g_{ij}(w)=16[GB(w)^{-1}G]_{ij}.}
\]
For \(w_e>0\), H52 gives a local diffeomorphism from the six edge weights to an open cone of 3×3 SPD metrics:
\[
\boxed{
J_{ij,e}(w):=\partial_{w_e}g_{ij}
=-16[GB^{-1}v_ev_e^\top B^{-1}G]_{ij}.
}
\]
The 6×6 symmetric-metric coordinate Jacobian is invertible. **Do not count each symmetric off-diagonal coordinate twice as an independent metric coordinate**: with
\(q^A=(g_{00},g_{11},g_{22},g_{01},g_{02},g_{12})\), the canonical ADM dual coordinates are \(P_A=(\pi^{00},\pi^{11},\pi^{22},2\pi^{01},2\pi^{02},2\pi^{12})\), so
\[
\boxed{p_e=\sum_{ij}\pi^{ij}\partial_{w_e}g_{ij}
=\sum_A P_A\frac{\partial q^A}{\partial w_e}.}
\]
Then for every independent six-weight perturbation \(\delta w_e\),
\[
\boxed{\sum_e p_e\,\delta w_e=\pi^{ij}\delta g_{ij}.}
\]
Because the Jacobian is invertible, \(\pi^{ij}\) can be reconstructed uniquely from \((w_e,p_e)\), and the canonical 1-form \(\int \pi^{ij}\delta g_{ij}\,d^3x=\int p_e\delta w_e\,d^3x\) is preserved **pointwise** wherever the physical solder and field chart are consistently fixed. Hence the local cotangent lift is **a canonical/symplectic coordinate transformation** on the externally given continuum metric phase space; it is not a new microscopic derivation of the symplectic structure. The checker verifies exact metric and dual momentum inverses, the off-diagonal factors, and independent anisotropic momentum/velocity contractions across several rational strictly positive six-weight configurations.

**Diffeomorphism caveat:** under a spatial vector field \(\xi\), a metric transforms as
\[
(\mathcal L_\xi g)_{ij}=\xi^k\partial_kg_{ij}
+g_{kj}\partial_i\xi^k+g_{ik}\partial_j\xi^k.
\]
In this local K₄ chart the induced variation of weights is
\[
\boxed{\delta_\xi w=J(w)^{-1}\operatorname{symvec}(\mathcal L_\xi g).}
\]
Thus the **six weights are NOT simply six spatial scalar fields** \(w_e\mapsto\xi^k\partial_k w_e\) in a fixed coordinate solder: derivative-of-\(\xi\) terms arise from the metric's two covariant coordinate indices. The checker exhibits this even for uniform constant weights (all gradients zero) and a vector field with nonzero \(\partial\xi\): \(\delta_\xi w\ne0\). Compatibility under general chart changes/finite diffeos further requires the externally imposed solder and local positive-edge cone to transform consistently; an arbitrary finite diffeo may leave the given positive chart.

## 2. Conditional ADM action, momentum and Hamiltonian density in weight coordinates

**ADD the standard ADM physical action** (not derive it):
\[
\boxed{
S_{\rm ADM}=\int dt\,d^3x\;N\sqrt g\left(
K_{ij}K^{ij}-K^2+R^{(3)}
\right)
}
\]
with \(N>0\), shift \(N^i\), physical coordinate metric \(g(w)\), and
\[
K_{ij}=\frac1{2N}\left(\dot g_{ij}-(\mathcal L_{\vec N}g)_{ij}\right).
\]
Using conventional units \(16\pi G_N=1\), zero cosmological constant, no matter and appropriate ignored/compensated boundary terms, the ADM momentum density is
\[
\boxed{\pi^{ij}=\sqrt g(K^{ij}-g^{ij}K),\qquad
p_e=\pi^{ij}J_{ij,e}(w).}
\]
Its lapse Hamiltonian density is
\[
\boxed{
\mathcal H_\perp
=\frac1{\sqrt g}\left(
\pi^{ij}g_{ik}g_{j\ell}\pi^{k\ell}
-\frac12(\pi^{ij}g_{ij})^2\right)
-\sqrt g R^{(3)}.
}
\]
The shift density is
\[
\boxed{\mathcal H_i=-2g_{ik}\nabla_j\pi^{jk},}
\]
where \(\pi^{jk}\) is a weight-one tensor density. For smooth fields and suitable boundary conditions, the canonical Hamiltonian is
\[
H[N,N^i]=\int d^3x\left(N\mathcal H_\perp+N^i\mathcal H_i\right)
+\text{boundary terms},
\]
with \(\pi=\pi(w,p)\) the algebraic six-dimensional inverse cotangent map. The standard multiplier momenta \(p_N,p_{N^i}\) vanish as primary constraints, and lapse/shift variations impose \(\mathcal H_\perp=\mathcal H_i=0\) as secondary constraints **only because the ADM action was separately postulated**.

The exact verifier uses a nonzero six-component anisotropic velocity, nontrivial lapse, a nonconstant shift gradient and a full 3×3 rational spatial metric to check
\[
\boxed{
\sum_e p_e\dot w_e-\mathcal L_{\rm kin}
=\frac N{\sqrt g}\left(\pi^{ij}\pi_{ij}-\frac12\pi^2\right)
+\sum_e p_e(\delta_{\vec N}w)_e.
}
\]
Also \(\sum_e p_e(\delta_{\vec N}w)_e=\pi^{ij}(\mathcal L_{\vec N}g)_{ij}\). An exact flat-background identity with independently specified spatial \(\partial\pi\) and \(\partial N^i\) checks
\[
\pi^{ij}(\mathcal L_{\vec N}g)_{ij}
=N^i\mathcal H_i+\partial_j(2\pi^j{}_iN^i)
\]
at a point. The divergence is a **genuine boundary current**, not an identity that the boundary flux is always zero. Full general-space HDA Dirac Poisson brackets are **not proved** by a single-cell numerical/rational identity. When imported from established ADM for a compatible smooth spatial continuum, canonical pullback transports those brackets locally; their *physical origin* remains additional.

## 3. Exact homogeneous minisuperspace and the cell-volume normalization trap

For all six equal weights \(w_e=w(t)>0\), H52 gives \(g=4G/w\) in this **nonorthonormal coordinate solder**. Since \(\det G=4\),
\[
\boxed{\sqrt{\det g}=\frac{16}{w^{3/2}}.}
\]
By contrast, H52 computed the homogeneous ADM density in an **orthonormal spatial coordinate frame** with \(g_{\rm orth}=4I_3/w\), \(\sqrt{\det g_{\rm orth}}=8/w^{3/2}\). The factor of 2 is exactly the nonorthonormal fixed-coordinate volume Jacobian \(\sqrt{\det G}=2\); the properly transformed **integrated** action is the same. Mixing one frame's metric with the other frame's volume density would produce a spurious factor-of-two contradiction.

Assume zero shift and an independently prescribed lapse \(N(t)>0\). Then
\[
K^i{}_j=-\frac{\dot w}{2Nw}\delta^i{}_j,\qquad
\pi^{ij}=\frac{4\dot w}{Nw^{3/2}}(G^{-1})^{ij}.
\]
In the nonorthonormal coordinate density:
\[
\boxed{
\mathcal L_{\rm kin}=-\frac{24\dot w^2}{Nw^{7/2}},\quad
p_w=\sum_e p_e=-\frac{48\dot w}{Nw^{7/2}},\quad
\mathcal H_{\perp}^{\rm iso}=-\frac{w^{7/2}p_w^2}{96}.
}
\]
The full canonical Hamiltonian for this homogeneous flat potential-free sector is \(H=N\mathcal H_{\perp}^{\rm iso}\), and direct exact Legendre transformation gives \(p_w\dot w-\mathcal L_{\rm kin}=H\). The checker verifies \(w=1,4,9\) with nonzero positive/negative \(\dot w\) and multiple rational lapses. The **vacuum Hamiltonian constraint** \(\mathcal H_\perp=0\) in this completely homogeneous spatially flat/no-matter/no-cosmological-constant sector forces **\(p_w=0\)** and hence \(\dot w=0\) for finite lapse, so a nonzero-velocity kinematic trajectory is **not** a vacuum Einstein solution merely because the kinetic density can be written.

For H53's separately supplied smooth positive curved family \(w_e(x)=1-x^\top Gx\) at \(x=0\), \(R^{(3)}(0)=-3\) and \(\sqrt g=16\); at zero momentum the curvature potential is \(-\sqrt g R^{(3)}=+48\) locally, failing \(\mathcal H_\perp=0\) without an offsetting kinetic, matter or cosmological term. This is a straightforward constraint example, **not** evidence of CR-generated physical curvature dynamics.

## 4. Precise HDA and microscopic-generation boundary

- **Proved finite, under chart assumptions:** invertible 6-dimensional \(w\leftrightarrow g\), exact cotangent momentum chain, canonical one-form preservation, ADM kinetic Legendre identity, correct lapse/shift and shift-induced weight transformation, homogeneous Hamiltonian constraint and correct coordinate volume normalization.
- **Conditionally inherited from standard ADM, not derived here:** field-theory symplectic Poisson brackets, the full lapse/shift constraints on a physical 3-manifold, the Hamiltonian–diffeomorphism constraint algebra (HDA) on permitted boundary conditions, and the standard Einstein equations under the independent ADM action.
- **OPEN as *generative physics*:** derive the actual spatial base, solder, lapse/shift, choice of EH/ADM action, matter stress/energy and covariance, continuum domain, ADM first-class physical constraint representation and Einstein dynamics **from original P3/P4 finite CR and P7/P8 physically sourced ingredients**, as opposed to postulating them.

**H56 suggestion:** explicitly audit whether the **positive K₄ edge cone is invariant under all spatial diffeomorphisms**, or only a local coordinate patch requiring transitions; then prove conditional HDA equivalence via the ADM canonical cotangent lift with correct functional derivatives and boundary support if a physical continuum/solder is independently authorized. A proof that standard ADM brackets hold after an invertible canonical coordinate transformation would be useful but would remain a reformulation of standard GR. A genuinely new P9 step must derive or physically constrain the action/solder/control from CR rather than merely change ADM coordinates.

## 5. Exact reproducibility

`P3/P9H55K4ADMCanonicalChartExactCheck.py` uses standard-library exact Gaussian rational arithmetic, imports H52/H53's already checked K₄/SPD and spatial-curvature geometry, and checks canonical 1-form, full six-variable inverse momentum and ADM kinetic Legendre algebra, nontrivial coordinate Lie derivative, momentum boundary-current identity, two spatial volume normalizations, isotropic Hamiltonian constraint and nonzero curvature potential. Dedicated Actions audit is included. Frozen papers/main unchanged; no expert peer review, new Lean kernel or physical demonstration.