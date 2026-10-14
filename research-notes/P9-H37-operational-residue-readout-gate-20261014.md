# H37 — From signed P3 residue locality to a conditional coherent observer

**2026-10-14 | P3–P11 Mathematical Bridge.** A strict operational distinction, continuing H36 Draft PR #55. The model is a standard nearest-neighbor site-dephasing GKSL comparator; nothing is designated CR-exclusive. The coherent tomography observer is **added explicitly** rather than silently identified with P6's frozen population observer and independently fixed physical control manifold. Main and frozen P3/P6/P9 unchanged. No Lean proof or human peer review claim.

## 1. What exactly is observed?

Fix the H35/H36 one-ended 5-site chain, real-symmetric nearest-neighbor Hamiltonian with uniform hopping J>0, arbitrary real site potentials v, nonnegative uniformly calibrated site-dephasing gamma, and state preparation d=E00. For t>0 let Φ_t=exp(t L) be the CPTP discrete update. Its two P3 hidden iterates are
\[
z=Q_D\Phi_t(d)\in\mathcal H_1(\Phi_t,D),\qquad
w=Q_D\Phi_t^2(d)\in\mathcal H_2(\Phi_t,D).
\]
The **original** signed depth-three P3 residue is
\[
R=\Delta_D([z,w^\dagger])
=i\operatorname{diag}(\partial_1j),\qquad
j_{uv}=2\operatorname{Im}(z_{uv}\overline{w_{uv}}),\quad u<v.
\]
R itself is anti-Hermitian, not a density matrix or a directly recorded population difference. P6's chosen population readout cannot automatically return the coherences entering this quadratic bilinear.

## 2. Exact population-only No-Go, even with the entire time trace

For a real-symmetric H and real diagonal d, take the two genuine CPTP GKSL generators
\[
L_{+H}(\rho)=-i[H,\rho]+\gamma(\Delta_D\rho-\rho),\qquad
L_{-H}(\rho)=+i[H,\rho]+\gamma(\Delta_D\rho-\rho).
\]
Entrywise complex conjugation C commutes with diagonal pinching and dephasing, and satisfies
\[
C\circ L_{+H}=L_{-H}\circ C.
\]
Thus \(\rho_{-H}(s)=\overline{\rho_{+H}(s)}\) for **all s≥0**; in particular every population \(p_v(s)\) agrees at every time, not merely through finite perturbative order. However
\[
\boxed{R_{-H}(t)=\overline{R_{+H}(t)}=-R_{+H}(t).}
\]
For the specified rational example J=1/2, gamma=2/3, \(v=(0,1/7,-1/9,2/11,-3/13)\), the H36 depth-three root coefficient is
\[
[t^3]R_{+H,00}(t)=2iJ^2(v_0-v_1)=-i/14\neq0.
\]
At t=1/64 an exact rational degree-16 Taylor polynomial **together with rigorous semigroup remainder** proves the physical R00(t) remains nonzero. The negative-H model has opposite signed R and *identical full population time trace*. This is a genuine operational nonidentifiability result for **population-only observation**, not a claim that either positive/negative H is an already independently calibrated P6 hardware setting.

In particular neither the absolute sign of this selected signed R3 witness nor its microscopic current orientation is identifiable from populations alone. **Caution:** multiplying a nonzero witness by -1 does **not change the complex-linear span** of the P3 residue subspace. Thus this does not show the full R3 subspaces differ.

## 3. Positive conditional protocol: two phase-calibrated quadratures

Add a separate and independently calibrated measurement capability on a declared edge \((u,v)\): access to the Hermitian pair
\[
X_{uv}=E_{uv}+E_{vu},\qquad
Y_{uv}=-iE_{uv}+iE_{vu}.
\]
Perform separately prepared, phase-referenced state measurements at times t and 2t. Then
\[
z_{uv}=\frac{\langle X_{uv}\rangle_t-i\langle Y_{uv}\rangle_t}{2},
\qquad
w_{uv}=\frac{\langle X_{uv}\rangle_{2t}-i\langle Y_{uv}\rangle_{2t}}{2},
\]
because both hidden projections keep offdiagonal matrix entries unchanged. Hence these two quadratures at both times reconstruct j_uv, and measuring all declared coherence edges reconstructs the *signed* R. This is ordinary quantum coherence tomography, not a new noncommutative-only measurement or a CR-exclusive predictor.

The same diagonal local unitary change of basis \(g=\operatorname{diag}(\lambda_v)\) applied to **both** time measurements rotates \(z_{uv},w_{uv}\) by the common phase \(\lambda_u\bar\lambda_v\), so j_uv and R remain invariant. But if the measurement phase reference drifts **between** t and 2t, the inferred j generally changes while populations remain unchanged. Therefore a shared phase reference is a substantial **physical calibration requirement**, not dispensable notation.

A full readout does not require that offdiagonal matrix elements be *physical controllable tangent generators*. But experimentally accessing X/Y typically demands independent coherent basis rotations and readout calibration; P6's frozen First-Residue Accessibility constrains which coherent operations can be treated as internally permitted. The theorem does **not** demonstrate that those rotations, preparations or all-to-all coherence readouts belong to its original physical control family.

## 4. Combined quantitative reconstruction bound

Let \(P_{<R}\) project to the first R sites, and let \(\widehat z_{uv},\widehat w_{uv}\) be separately calibrated complex coherence estimates on the edges wholly inside this block. Suppose
\[
|\widehat z_{uv}-z_{uv}|\le\epsilon_z,\qquad
|\widehat w_{uv}-w_{uv}|\le\epsilon_w
\]
for every measured edge. Positivity and trace-one of both genuine physical density matrices imply the sharp bound \(|z_{uv}|,|w_{uv}|\le1/2\) for u≠v. Consequently, for the current \(j_{uv}=2\operatorname{Im}(z_{uv}\bar w_{uv})\),
\[
|\widehat j_{uv}-j_{uv}|
\le 2(|\delta z_{uv}|\,|w_{uv}|+|z_{uv}|\,|\delta w_{uv}|+|\delta z_{uv}|\,|\delta w_{uv}|)
\le \epsilon_z+\epsilon_w+2\epsilon_z\epsilon_w.
\]
Define \(\widehat R^{<R}\) as the divergence of these estimated measured-edge currents, including zeros outside the block. Each edge-current error contributes with opposite signs to two diagonal vertices. Therefore
\[
\boxed{
\|R-\widehat R^{<R}\|_1
\le B_{\rm H36}(R,t)
+2\,\#E_{<R}\,(\epsilon_z+\epsilon_w+2\epsilon_z\epsilon_w),
}
\]
where
\[
B_{\rm H36}(R,t)
=4e^{12Jt}\sum_{\substack{0\le u<v<N\\v\ge R}}
\frac{(32J^2t^2)^{u+v}}{[(u+v)!]^2}.
\]
The estimate is a **deterministic conditional** error bound, not a statistical confidence interval or a claim that finite shot counts achieve the errors. When the estimator derives from two quadrature readings each with individual absolute expectation error ≤η, the complex coherence error is ≤η/√2 and it is safe to use \(\epsilon_z,\epsilon_w\le\eta\) (plus separately certified numerical or calibration errors). The count \(\#E_{<R}\) means **actual measured coherence pairs** in the retained subspace, not necessarily nearest-neighbor hopping graph edges: time evolution can create distance-two and longer coherences, which also contribute to original P3 residue.

The checker constructs a pure rational experiment at t=1/64 with η=1/10000, using exact rational Taylor polynomials of degree16 and **rigorous rational Taylor remainders** \(\varepsilon_t,\varepsilon_{2t}\). For the physical truth, use \(\epsilon_z=\eta+\varepsilon_t\) and \(\epsilon_w=\eta+\varepsilon_{2t}\). It certifies the bound for all block radii R=1,...,5, including a full-matrix readout where no H36 cutoff error remains.

If all coherence pairs are needed, the number of edges grows quadratically with R and a uniform per-edge tomography error bound may not yield N-uniform total accuracy; an experimental resource/noise budget or local weighted measurement strategy is still necessary.

## 5. Divergence matching is weaker than hidden-current and connection matching

Even if a physical observer estimates the full signed diagonal residue R perfectly, it only determines \(\partial_1j\). On the **complete K5 coherence-edge graph**, there are ten oriented edges, incidence rank four and a six-dimensional cycle-current kernel. Adding the circulation \(j_{01}=+1,j_{12}=+1,j_{02}=-1\) changes j but leaves \(\partial_1j\) and R unchanged. In contrast a complete two-quadrature edge tomography of both z and w can reconstruct the actual edge currents in the chosen fixed phase basis.

This is an **algebraic ambiguity example**, not a demonstration that every added cycle-current vector is realizable as a pair of GKSL-generated hidden jets. Nor does equality of edge currents imply equality of the microscopic update map or of any spatial U(1)/SO(3)/Levi-Civita holonomies. The P9.38 cross-audit (#53) additionally proved that **diagonal-Hamiltonian gauge perturbations at fixed A** form a weighted-gradient subspace transverse to the cycle kernel. That does not remove cycle ambiguity for arbitrary independent hidden B modifications.

## 6. Calibration, real P6 provenance and the remaining gate

The original P6 v9.1 physical baseline uses population readout with separately calibrated site-dephasing and independently specified allowed coherent exchange controls. It does not automatically provide:
- a phase-stable coherent X/Y readout on arbitrary nonlocal coherence pairs;
- a coherent local basis-reference shared between t and 2t;
- calibration of diagonal Stark shifts \(\alpha\) distinct from dephasing \(\gamma\);
- a two-step *- and Δ-compatible microscopic-to-operational CPTP intertwiner;
- identity of the frozen P6 microscopic \(\mathcal J_N\) with P3 dynamically generated \(\mathcal H_k(\Phi)\).

The P9.38 Laplacian identity states for true/calibrated diagonal phases with \(\delta\alpha=\alpha_{\rm cal}-\alpha_{\rm true}\) that the **calibrated leading depth-three witness** has signed error \(-2i\operatorname{diag}(L_w\delta\alpha)\). H37's reconstructed *actual* signed R(t) is not automatically the **α-free reference witness**; removing physical diagonal detuning still requires that independent calibration. Exact two-time tomography and α compensation solve **different** tasks.

**H37 main verdict:** Population-only ⇒ signed original P3 R3 witness is **not identifiable** (an exact GKSL counterexample); independently calibrated coherent X/Y pairs at two timepoints ⇒ full hidden edge-current/residue readout is **mathematically sufficient**, with a rigorous combination of H36 factorial spatial truncation and deterministic measurement/numerical error. **Actual physically inherited P6 access remains OPEN**, and no CR-exclusive observation or geometric/Einstein conclusion follows.

### Suggested H38

A rigorous physical-control gate: choose a **specific independently calibrated P6 physical coherent tangent and observer** and test if it implements even one signed hidden edge-current quadrature. If only diagonal readout is admitted, freeze the observational nonidentifiability No-Go; if coherent readout is admitted, demonstrate source-grounded admissible control and two-step intertwining on the fixed microscopic sector before any CR-specific prediction or geometry.

## Reproducibility

P3/P9H37OperationalResidueReadoutExactCheck.py imports CI-passed H35/H36 Fraction-Gaussian computations; tests the all-time population equivalence by exact *real-H conjugation*, opposite nonzero signed residue with rational remainder, X/Y reconstruction, common-gauge invariance, drift ambiguity, current/divergence matching, complete-graph cycle null and measured-block norm-error bounds. Dedicated Actions CI. Original P3 and P6 manuscripts unchanged.