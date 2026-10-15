# H53 — Conditional K₄ Cell Gluing, Soldered Spatial 2-Jets, Levi-Civita Curvature, and Exact Convergent Neighbor-Cell Stencils

**2026-10-15 | P3–P11 Mathematical Bridge / P9 — GR-I.** Stacked Draft on H52 [PR #71](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/71), with its exact cell metric convention and corrected 6×6 DeWitt regression fixture. The mathematics here consists of exact rational matrix differential geometry plus a finite-difference convergence theorem **conditional on an externally supplied smooth spatial manifold/coordinate chart and a consistent physical soldering**. This is not a derivation of physical spacetime, EH action, ADM/HDA, GR, or a CR-only prediction.

## 1. The previously missing assumption must be explicit

The original P9 K₄ cell has an **internal** oriented Euclidean real space \(S=\mathbf1^\perp\subset\mathbb R^4\), metric response \(g_w=16(A_w|_S)^{-1}\), and six edge weights. To speak of spatial derivatives \(\partial_i\), the Einstein spatial scalar curvature \(R^{(3)}\), or a field Lagrangian, a single finite cell is insufficient. H53 therefore **separately posits**:

- (S1) A **three-dimensional \(C^4\) spatial base** \(M\), a local chart \(x^1,x^2,x^3\), and a positive domain of smoothly varying **six** weights \(w_{ab}(x)>0\).
- (S2) A smooth, locally consistent **solder/frame identification** between the K₄ internal \(S\) and the actual physical tangent fibers \(T_xM\), with compatible overlap/chart transformations. In one chart fix a frame \(f_i=e_i-e_3\) for \(S\) and declare that its metric-component indices match the spatial coordinate basis \(\partial_i\). This is an **independent geometric premise**, not an automatic consequence of the P7/P8 response envelope.
- (S3) The spatial metric is **defined** from the cell response by \(g_{ij}(x)=16[G B(x)^{-1}G]_{ij}\), with \(G=f^\top f\) and \(B(x)=\sum_{a<b}w_{ab}(x)v_{ab}v_{ab}^{\mathsf T}\), \(v_{ab}=f^\top(e_a-e_b)\). Uniform positive weights guarantee \(B\succ0\) locally. On overlap, site relabeling/internal frame changes MUST be accompanied by solder-frame transformations; otherwise the number arrays need not define the same physical spatial tensor.

**Result:** under (S1)–(S3) the response assignment gives an honest smooth **Riemannian** 3-metric field on the chosen chart, so its unique metric-compatible torsion-free Levi-Civita connection and spatial curvature exist by standard geometry. Their *physical emergence* is NOT proved: the needed base, smoothness, compatibility and identification were independently chosen.

## 2. Exact inverse-metric spatial 2-jet theorem

Denote
\[
B_i=\partial_iB=\sum_{a<b}(\partial_iw_{ab})v_{ab}v_{ab}^{\mathsf T},
\quad
B_{ij}=\partial_i\partial_jB=
\sum_{a<b}(\partial_i\partial_jw_{ab})v_{ab}v_{ab}^{\mathsf T},\quad R=B^{-1}.
\]
With the same (nonorthonormal) internal frame normalization as H52:
\[
\boxed{g=16GRG,\qquad
g_i=-16GRB_iRG,}
\]
\[
\boxed{
g_{ij}=16G\left(
RB_iRB_jR+RB_jRB_iR-RB_{ij}R
\right)G.
}
\]
These hold for arbitrary \(C^2\) smooth positive weight fields, without approximations. The proof is twice differentiating \(BR=I\):
\[
R_i=-RB_iR,\qquad
R_{ij}=RB_iRB_jR+RB_jRB_iR-RB_{ij}R.
\]
H53's exact Fraction checker evaluates these with an **anisotropic rational jet** with nonzero first spatial gradients and nonzero mixed Hessians, producing a nonzero connection, Ricci tensor and scalar:
\[
\Gamma^0{}_{00}=-7/540,\quad
\operatorname{Ric}_{01}=3713/1215000,\quad
R^{(3)}=-120893/8640000
\]
for its explicitly fixed six weights and chosen first/second jets. These are model-specific witnesses of actual nontrivial geometry, not universal constants.

The standard Christoffel connection is explicitly
\[
\Gamma^k{}_{ij}
=\tfrac12g^{kl}(g_{jl,i}+g_{il,j}-g_{ij,l}),
\]
and its first derivatives use the exact second jets above with
\[
\partial_m g^{kl}=-g^{ka}g_{ab,m}g^{bl}.
\]
The spatial Ricci and scalar are then calculated by
\[
R_{ij}=\partial_k\Gamma^k{}_{ij}
-\partial_j\Gamma^k{}_{ik}
+\Gamma^k{}_{ij}\Gamma^\ell{}_{k\ell}
-\Gamma^\ell{}_{ik}\Gamma^k{}_{j\ell},
\qquad
R^{(3)}=g^{ij}R_{ij}.
\]
The checker asserts torsion-free symmetry, metric-compatibility \(\nabla g=0\), symmetric Ricci, and \(\mathrm{tr}_g(\mathrm{Ric}-\tfrac12gR)=-R/2\) in exactly 3 dimensions. **Do not equate this algebraic trace identity with the differential (contracted) Bianchi identity**, which requires a compatible **third spatial jet**, nor with ADM/HDA constraint closure.

### K₄ vertex labels are gauge, not physical coordinates

If the four site labels are permuted by \(P\), acting on internal \(S\), let \(L\) be its 3×3 change-of-basis matrix in \(f\): \(Pf=fL\). Permute all six weight values and their spatial jets accordingly. Their represented spatial tensor arrays obey
\[
\boxed{L^\top g_{P w}L=g_w,\qquad
L^\top (\partial_i g)_{Pw}L=\partial_i g_w,\quad
L^\top (\partial_{ij}g)_{Pw}L=\partial_{ij}g_w.}
\]
These three displayed identities compare **internal-basis metric arrays** after applying the compensating frame matrix (L). They do NOT authorize treating the unadjusted (g_{Pw}) arrays as physical coordinate-metric components in the original fixed chart. Indeed, the anisotropic exact witness gives the original physical scalar (R=-120893/8640000), but if one **incorrectly** feeds the raw site-relabelled internal (g_{Pw}) and its spatial jets to the coordinate Levi-Civita formula without transforming the physical solder, the scalar is (-114293/8640000), a different value. This is a constructive **unsoldered-label non-invariance counterexample**. Correctly map each of (g_{Pw},partial_i g_{Pw},partial_ipartial_j g_{Pw}) back to the fixed physical coordinate frame using (Mmapsto L^	op ML), then compute Levi-Civita, Ricci and scalar: all physical tensors and (R) agree EXACTLY. The spatial derivative **indices** remain in the same chart; we are compensating an internal basis change, NOT silently performing a coordinate transformation. This is conditional **internal frame gauge covariance with a matched physical solder**, not a derivation of full spacetime diffeomorphism invariance or smooth physical inter-cell transport without the gluing premise.

## 3. A truly finite neighboring-cell curvature reconstruction

A strong explicit test of the gluing assumption uses a smooth *positive-near-origin* K₄ weight field on the externally postulated spatial chart. In the nonorthonormal \(f\) frame use the FIXED spatial background quadratic form \(q(x)=x^\top Gx\) (using ordinary \(|x|^2\) in this nonorthonormal coordinate frame would change the curvature normalization). Let, for all six edges,
\[
\boxed{w_{ab}^{(c)}(x)=1-c\,q(x),\quad |x|\text{ small enough that }1-cq(x)>0.}
\]
The soldered metric is
\[
g_{ij}^{(c)}(x)=\frac4{1-cq(x)}\,G_{ij}.
\]
At the origin,
\[
w_{ab}(0)=1,\quad w_{ab,i}(0)=0,\quad
g(0)=4G,\quad g_i(0)=0,
\]
\[
w_{ab,ij}(0)=-2cG_{ij},\quad
\boxed{g_{ij,kl}(0)=8c\,G_{ij}G_{kl},\qquad R^{(3)}(0)=-3c.}
\]
This is a wholly algebraic rational local-jet calculation of a standard Riemannian scalar-curvature formula, not the microscopic origin of the derivative data. In particular changing \(c\) leaves the *same* center cell and its **first** spatial jet while changing intrinsic curvature: H52's no-go survives unchanged.

Now read neighboring K₄ cells at \(\pm h e_i\), and at \(\pm h e_i\pm h e_j\) (for \(i\ne j\)). Compute their six weights and **their solder-compatible metrics** \(g(x)\), then form standard central first and second finite differences:
\[
D_i^h g=\frac{g(he_i)-g(-he_i)}{2h},
\]
\[
D_{ii}^h g=\frac{g(he_i)-2g(0)+g(-he_i)}{h^2},
\]
\[
D_{ij}^h g=\frac{g(he_i+he_j)-g(he_i-he_j)-g(-he_i+he_j)+g(-he_i-he_j)}{4h^2}.
\]
Insert these stencils into the SAME rational Levi-Civita/Ricci construction as for exact jets to define \(R_h^{(3)}\). Under \(|c|\le3/2\), \(0<h\le1/4\), every stencil cell lies in the positive-weight domain. **Theorem H53.1 (exact neighbor-stencil identity)**:
\[
\boxed{
R_h^{(3)}(0)=
\frac{3c(-1+9ch^2)}
{(1-6ch^2)(1-2ch^2)}.
}
\]
Since the continuum value is \(-3c\),
\[
\boxed{
R_h^{(3)}(0)-R^{(3)}(0)=
\frac{3c^2h^2(1+12ch^2)}
{(1-6ch^2)(1-2ch^2)}.
}
\]
For the indicated parameter domain, the denominators are bounded below by
\((7/16)(13/16)=91/256\), and \(|1+12ch^2|\le17/8\). Therefore the **uniform exact error guarantee**
\[
\boxed{
|R_h^{(3)}(0)-R^{(3)}(0)|
\le \frac{1632}{91}c^2h^2.
}
\]
holds for every allowed \(c,h\), and is checked with exact rational samples for both positive and negative c and four lattice spacings. **This is a genuine finite-cell convergence statement**: with a *common external solder and compatible smooth weight field*, the lattice curvature reconstructs the intrinsic Riemannian curvature to second order in spacing for this nontrivial explicit family. It does not show that spacetime and its smooth weights physically arise from original P3/P4.

**General smoothness extension (standard numerical geometry):** for weights \(w_e\in C^4\) on a compact region where \(B(w)\succ0\) uniformly and a \(C^4\) solder/coordinate system is fixed, ordinary central differences approximate the first and second derivatives of g with \(O(h^2)\) error; curvature is a smooth rational expression in \((g,\partial g,\partial^2g)\) while g stays uniformly SPD, so \(R_h=R+O(h^2)\) locally. The explicit uniform rational constant \(1632/91\) above applies **only** to the specified conformal family and bounded parameters, not arbitrary C⁴ fields.

## 4. What changes and what remains OPEN for P9

| Target | H53 verdict | Assumptions and limits |
|---|---|---|
| Pointwise K₄ metric \(g_w\) | H52 exact | 6 positive edge weights and original normalized internal S |
| Spatial metric \(g_{ij}(x)\) | **CONDITIONAL** | independently given 3D base, smooth weight gluing and physical solder |
| Metric-compatible torsion-free connection \(\Gamma\) | **PROVEN CONDITIONAL GEOMETRY** | standard unique Levi-Civita connection from once derivatives exist |
| Spatial Ricci and \(R^{(3)}\) | **PROVEN CONDITIONAL GEOMETRY** | spatial 2-jets and compatible solder |
| K₄ relabel consistency | **PROVEN FINITE** | transform metric and solder *together*, not internal basis alone |
| Neighbor K₄ cell stencil curvature convergence | **PROVEN CONDITIONAL**, \(O(h^2)\) on declared family | second neighbors and compatible chart; explicit uniform bound |
| Physical source of smooth \(M\), edge gluing, solder, weight dynamics | **OPEN** | not obtained from H35–H52 |
| Spatial Bianchi differential identity | **not audited in this H53 finite jet checker** | standard theorem when metric sufficiently smooth; distinct from algebraic trace identity |
| Einstein–Hilbert/ADM potential, action variation and HDA closure | **OPEN** | independent spacetime/lapse/shift, curvature term, boundary and dynamics needed |
| Time-like Lorentz geometry / physical GR | **OPEN** | no conclusion from three-dimensional Riemannian curvature alone |

**H54 suggested gate:** conditionally add the **ADM lapse/shift** and a local spatial-curvature potential \(\sqrt g R^{(3)}\), then derive the metric/weight variational chain rule and boundary terms; explicitly test the HDA only if the canonical symplectic structure, lapse/shift smearings and integration domain have been independently justified. Alternatively seek an actual P7/P8 microphysical soldering rule before developing more conventional GR action algebra. This is not a request to relabel standard GR formulae as an emergence theorem.

## 5. Exact reproducibility

The new script \`P3/P9H53K4SolderedSpatialCurvatureExactCheck.py\` imports the corrected unchanged H52 core and uses `fractions.Fraction` for all weight jets, 3×3 Christoffels, Ricci, K₄ frame-transformation, exact central finite-difference reconstructions and rational convergence bounds; no floating tolerance. Dedicated CI checks H52's prerequisites as part of import. The result is **finite exact standard Riemannian geometry under explicit additional field/solder assumptions**, not a Lean kernel formalization, physical LQG/GR result or expert-reviewed proof. H52's earlier failed CI was traced to a mistaken expected final row in the 6×6 DeWitt regression fixture, which was corrected without changing the independently recalculated eigenvalues \(-1,1/8,1/8,1/4,1/4,1/4\) or (5+,1−) inertia.