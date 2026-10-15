# H54 — Exact Spatial-Curvature Variation, Palatini Boundary Current, and K₄ Edge-Weight Chain Rule

**2026-10-15 | P3–P11 Mathematical Bridge / P9 — GR-I.** Stacked on H53 Draft [PR #72](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/72). The precise scope is an **intrinsic three-dimensional spatial-curvature action** built from a pre-existing smooth K₄ spatial metric, conditional on H53's **externally supplied** 3D spatial base, smooth positive six-weight fields, and internally/physically consistent soldering. No 4D Lorentzian Einstein–Hilbert action is derived, no dynamical lapse/shift or ADM/HDA algebra arises, and no P3→P6 physical provenance or CR-exclusive observation is shown. This is exact standard Riemannian/variational mathematics in K₄ weight coordinates. Draft/unmerged, no frozen paper/main edits, no new Lean kernel/human expert referee or laboratory result.

## 1. The object to vary: a 3D curvature functional, NOT 3+1 general relativity

Fix a smooth oriented 3-manifold or local spatial coordinate region \(M^3\), a fixed compatible solder between the internal \(S=\mathbf1^\perp\subset\mathbb R^4\) basis and the physical spatial tangent bundle, and smoothly gluable positive K₄ edge-weight fields \(w_e(x)>0\). At each spatial point in the fixed H52/H53 **nonorthonormal** \(S\)-frame:
\[
G=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix},\quad
B(w)=\sum_{e\in E(K_4)}w_e v_ev_e^\top,\quad
\boxed{g(w)=16GB(w)^{-1}G.}
\]
H52 established the weight-to-symmetric-metric chart Jacobian has full rank six on the positive edge cone. H53 added spatial 2-jets, Levi-Civita connection, Ricci and scalar curvature, **conditional on spatial gluing/soldering**. Define the standard 3-dimensional functional
\[
\boxed{S_3[w]=\int_{M^3} \sqrt{\det g(w)}\,R^{(3)}[g(w)]\,d^3x.}
\]
The volume factor is with respect to the **same external spatial coordinates** used for \(g_{ij}(x)\). On a manifold with nontrivial overlaps the stated solder/transition compatibility is assumed. \(S_3\) is **NOT** the Lorentzian 4D Einstein–Hilbert action \(\int\sqrt{-g_4}R_4\), **NOT** the ADM action with kinetic term \(K_{ij}K^{ij}-K^2\), and **NOT** a claim that P3 generates a gravitational variational law.

## 2. Exact H54.1: first variation of the spatial curvature density

Let \(H_{ij}=\delta g_{ij}\) be any smooth symmetric spatial metric variation induced by varying the K₄ weight field. Define \(G^{(3)}_{ij}=\mathrm{Ric}^{(3)}_{ij}-\frac12g_{ij}R^{(3)}\) and the exact connection variation
\[
\delta\Gamma^k{}_{ij}
=\frac12g^{k\ell}\bigl(\nabla_i H_{j\ell}
+\nabla_j H_{i\ell}-\nabla_\ell H_{ij}\bigr).
\]
The *Palatini boundary current* is
\[
\boxed{
V^k=g^{ij}\delta\Gamma^k{}_{ij}
-g^{ki}\delta\Gamma^j{}_{ij}.
}
\]
Then the **pointwise** scalar curvature variation is
\[
\boxed{
\delta R^{(3)}
=-\mathrm{Ric}^{(3)\,ij}H_{ij}
+\nabla_k V^k,
}
\]
and the volume variation \(\delta\sqrt{g}=\frac12\sqrt{g}\,g^{ij}H_{ij}\) gives
\[
\boxed{
\delta(\sqrt g\,R^{(3)})
=\sqrt g\left(-G^{(3)\,ij}H_{ij}
+\nabla_k V^k\right).
}
\]
This is **standard** spatial Palatini calculus, here checked in a nontrivial K₄-generated geometry. Boundary flux \(\sqrt g\nabla_kV^k=\partial_k(\sqrt gV^k)\) must be retained in an action variation; for a compactly supported variation inside the coordinate region its integral vanishes. For general boundary conditions, merely fixing \(H\) itself on \(\partial M\) does NOT force \(V\) to vanish because \(V\) depends on derivatives of \(H\); a suitable spatial boundary prescription/compensating extrinsic-curvature term is needed. This is separate from the 4D Gibbons–Hawking–York construction, which is not established here.

## 3. Exact H54.2: K₄ edge-weight variation with independent spatial jets

Let \(\eta_e(x)=\delta w_e(x)\) be an allowed smooth variation and \(\delta B=\sum_e\eta_eV_e\), \(V_e=v_ev_e^\top\). From H52,
\[
\boxed{H=-16GB^{-1}(\delta B)B^{-1}G,\qquad
\frac{\partial g}{\partial w_e}=-16GB^{-1}V_eB^{-1}G.}
\]
H54 differentiates all THREE spatial jet levels \((g,\partial_i g,\partial_i\partial_jg)\) with respect to the perturbation parameter, keeping the solder/spatial chart fixed and correctly commuting variation with spatial derivatives. The **independent fractional-dual matrix calculation** implements both inverse differentiation \(\delta B^{-1}=-B^{-1}(\delta B)B^{-1}\) and the spatial inverse-derivative formulas of H53.

The bulk term for a given \(\eta_e\) is
\[
-\sqrt g\,G^{(3)\,ij}H_{ij}
=\sum_{e=1}^{6}\sqrt g\,C_e\,\eta_e,\qquad
\boxed{
C_e=-G^{(3)\,ij}\frac{\partial g_{ij}}{\partial w_e}
=16G^{(3)\,ij}[GB^{-1}V_eB^{-1}G]_{ij}.
}
\]
The **full** local density variation is
\[
\boxed{
\delta(\sqrt gR^{(3)})
=\sqrt g\sum_e C_e\eta_e
+\partial_k(\sqrt g\,V^k).
}
\]
No derivative terms in \(\eta\) may be dropped before integrating and deciding the legitimate boundary behavior. The six \(\partial g/\partial w_e\) matrices are linearly independent (H52 rank-six chart); therefore, **for arbitrary compactly supported variations in the positive-weight interior**, stationary \(S_3\) is equivalent to
\[
\boxed{G^{(3)}_{ij}=0.}
\]
But since this is a **three-dimensional** Einstein tensor, \(\operatorname{tr}_gG^{(3)}=-\frac12R^{(3)}\), it follows that \(R^{(3)}=0\), then \(\mathrm{Ric}^{(3)}=0\); in three dimensions the Riemann tensor is determined algebraically by Ricci, so the spatial metric is locally flat. This is a statement about **standalone pure 3D vacuum curvature functional**, NOT a derivation of 3+1 vacuum general relativity or of physical constraint dynamics. One cannot import this standalone 3D stationary equation as the ADM evolution equation.

## 4. Independently check the boundary-current contribution: no pointwise deletion

The exact checker uses a genuinely anisotropic rational jet \((w,\partial w,\partial^2 w)\) with nonzero \(\Gamma\), \(\mathrm{Ric}\), and \(R^{(3)}\), plus independently chosen six-component variation jets \((\eta,\partial\eta,\partial^2\eta)\). It computes \(\delta R\) two ways: by **dual-number differentiating the full Ricci/Christoffel algorithm** (so no finite-\(\varepsilon\) approximation), and by independently evaluating the covariant Palatini current and its divergence. The two match **exactly as rational numbers**, as do the six-component K₄ weight bulk chain coefficients.

A second useful witness begins with the **flat uniform cell field** \(w_e(x)=1\), then varies it as
\[
w_e^{(\varepsilon)}(x)=1+\varepsilon q(x),
\qquad q(x)=x^\top Gx.
\]
At \(x=0\), \(\delta w_e=0\), \(\partial_i\delta w_e=0\), and thus
\[
H(0)=0,\quad \partial_iH(0)=0,\quad
G^{(3)}(0)=0.
\]
Yet \(q\) has nonzero second derivatives. The metric generated from these varying weights obeys at the origin
\[
\boxed{
\delta R^{(3)}(0)
=\nabla_kV^k(0)=3,\qquad
-\bigl(G^{(3)\,ij}H_{ij}\bigr)(0)=0.
}
\]
Hence \(\delta(\sqrt g R)/\sqrt g=3\) at that point **entirely from a spatial divergence**, despite \(H(0)=0\). Discarding the boundary current as a *pointwise equality* is false. It can be removed from the *integrated* action only under proper compact-support/boundary assumptions.

An independent **nonzero curvature witness** uses H53's \(\,w_e(x)=1-q(x)\) near the origin. Exactly there,
\[
R^{(3)}(0)=-3,\quad
\mathrm{Ric}^{(3)}(0)=-4G,\quad
\boxed{G^{(3)}(0)=2G.}
\]
At this uniform cell the **sum of the six unnormalized edge-weight bulk coefficients** is \(\sum_e C_e=3/2\). The checker asserts this and the full nontrivial Palatini identity, so it explicitly detects an unbalanced Einstein-tensor bulk term in a curved 3D weight field; it does **not** announce that this is a new physical field equation.

## 5. Boundary, canonical and HDA gates needed before any P9 GR-I success claim

An actual (conditional) ADM/EH theory needs **independently supplied and audited**: a 3+1 Lorentzian spacetime/slicing and relation to P7/P8, lapse \(N\), shift \(N^i\), time variation of the 3-metric, canonical momenta or equivalent Lagrangian variables, the *kinetic* \(K_{ij}K^{ij}-K^2\) term (H52 only computed a homogeneous kinematic expression given lapse), curvature *potential* \(R^{(3)}\), matter/stress conservation if present, sign conventions, physical boundary terms, and **first-class Hamiltonian/diffeomorphism constraints** with the full HDA/Dirac bracket. A 3D curvature-density calculus by itself establishes NONE of these physical dynamics or the microscopic origin of its assumptions.

H54 distinguishes three nested logical levels:

1. **PROVEN CONDITIONAL GEOMETRIC CALCULUS:** smooth soldered K₄ weight fields encode a Riemannian 3-metric and the spatial \(\sqrt gR^{(3)}\) functional obeys exact Palatini/weight-chain variation.
2. **PROVEN MATHEMATICAL IMPLICATION UNDER STANDALONE ACTION:** compact-support vacuum stationary variations of *this 3D functional alone* give \(G^{(3)}=0\) and local spatial flatness; not 3+1 field evolution.
3. **OPEN PHYSICAL GR-I:** independently derive or state a full Lorentzian/ADM action and genuinely demonstrate correct metric/matter constraints, Bianchi conservation, HDA and Einstein equations. Also OPEN: P3/P4→P6 physical provenance and P7/P8 solder origin.

**H55 proposed gate:** set up the **full ADM gravitational Lagrangian** \(\mathcal L=N\sqrt g(K_{ij}K^{ij}-K^2+R^{(3)})\) under explicitly declared lapse, shift, field/gluing and boundary assumptions, then derive/verify the K₄-pulled-back canonical momentum and primary/secondary constraints in exact finite (e.g. homogeneous minisuperspace) test cases; do not claim the HDA from a single finite cell. A separate full spatial-field Poisson-bracket proof and source-to-physical-soldering theorem remain necessary.

## 6. Reproducibility

`P3/P9H54K4SpatialCurvatureVariationExactCheck.py` imports the corrected H52/H53 rational matrix geometry; computes \(\delta g,\delta g_i,\delta g_{ij}\) via exact dual matrix inverse; computes \(\delta\Gamma,\partial_i\delta\Gamma,\delta\mathrm{Ric},\delta R\) by independent dual scalar matrix-tensor differentiation; derives the Palatini \(V,\nabla V\) and checks the bulk six-edge chain and nonzero pure-boundary witness. Only Python stdlib \`fractions.Fraction\` and previously audited model code; no numerical tolerances. A dedicated GitHub Actions workflow executes it on the stacked Draft branch, without touching frozen manuscripts/main.