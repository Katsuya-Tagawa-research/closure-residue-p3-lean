# H36 — Soft locality of the original P3 quadratic residue

**2026-10-14 | P3–P11 Mathematical Bridge.** This is a new H36 continuation after H35 Draft PR #54 and distinct from the P9.38 cross-audit. It builds a mathematically valid **original P3 depth-three commutator witness** in an independently declared standard local GKSL model. **Not a CR-exclusive experimental discriminator**, not frozen P6 microscopic-sector identification, and not GR/Einstein dynamics. No frozen manuscripts/main changes, new Lean formal proof, or human peer review.

## 1. Actual P3 residue rather than population propagation

Fix a finite N-site one-ended nearest-neighbor chain, one-excitation algebra M_N(C), and uniformly bounded hopping J>0, real onsite energies v_j, and uniform local site dephasing gamma≥0:
\[
H=J\sum_{r=0}^{N-2}(E_{r,r+1}+E_{r+1,r})+\sum_rv_rE_{rr},\quad
\mathcal L_\gamma(\rho)=-i[H,\rho]+\gamma(\Delta_D\rho-\rho).
\]
The continuous-time CPTP/unital map is \(\Phi_t=e^{t\mathcal L_\gamma}\). **For any fixed t>0**, it can also be treated as a single *discrete* CPTP map for P3. Fix the diagonal seed d=E00; with Q=I-Delta_D define
\[
z(t)=Q\Phi_t(d)\in\mathcal H_1(\Phi_t,D_N),\qquad
w(t)=Q\Phi_t^2(d)=Q\Phi_{2t}(d)\in\mathcal H_2(\Phi_t,D_N).
\]
Both are Hermitian and offdiagonal. Consequently
\[
\boxed{R(t)=\Delta_D([z(t),w(t)^\dagger])\in\mathcal R_3(\Phi_t,D_N).}
\]
This is a **single signed depth-three witness**, not a claim that it spans or determines the complete residue *subspace* R3 for one map. As in the original P3 manuscript, if oriented edge currents are
\[
j_{uv}(t)=2\operatorname{Im}\bigl(z_{uv}(t)\overline{w_{uv}(t)}\bigr)
\quad(u<v),
\]
then
\[
\boxed{R(t)=i\operatorname{diag}(\partial_1j(t))}
\]
with incidence convention \(\partial_1(e_{uv})=e_u-e_v\). Hence the residue is the divergence of a quadratic *hidden coherence* current, not the population itself.

## 2. Certified residue-site Dyson soft-tail bound (all times)

For the above physical GKSL dynamics, H35 proves that for each matrix element, seed E00 and each s≥0,
\[
|\langle j|\Phi_s(E_{00})|k\rangle|
\le F_{j+k}(s)
:=\sum_{m\ge j+k}\frac{(4Js)^m}{m!}
\le e^{4Js}\frac{(4Js)^{j+k}}{(j+k)!}.
\]
Because the hidden projection only drops the diagonal, the same bound applies to z_{vu}(t) and w_{vu}(t) for v≠u. The exact divergence formula and triangle inequality yield
\[
|R(t)_{vv}|
\le2\sum_{u\ne v}|z_{vu}(t)|\,|w_{vu}(t)|.
\]
Using the H35 tails at t and 2t then gives the **new quadratic-residue soft locality estimate**:
\[
\boxed{
|R(t)_{vv}|
\le2e^{12Jt}\sum_{u\ne v}
\frac{(32J^2t^2)^{v+u}}{[(v+u)!]^2}
\qquad(t\ge0).
}
\]
The bound holds uniformly in chain size N, gamma≥0, and arbitrary real onsite energies. It controls the signed genuine P3 residue component, not an *arbitrary basis-dependent* element of R3 scaled without a norm constraint. Coefficients can be changed arbitrarily by linear combinations inside the filtration, so an unqualified norm bound on the full linear space R3 would be meaningless.

## 3. Spatial cutoff error is also factorially controlled

Let P_<R be the orthogonal projection onto sites 0,...,R−1, R≥1; define
\[
z^{<R}=P_{<R}zP_{<R},\quad w^{<R}=P_{<R}wP_{<R},\quad
R^{<R}=\Delta_D([z^{<R},(w^{<R})^\dagger]).
\]
This operation is an algebraic comparison of hidden operators; it does **not** assert the truncated matrices arise from a valid reduced P6 microscopic update or a physical trace-preserving observer measurement. For 0≤v<u<N, an edge current is removed iff u≥R. Its divergence contributes to at most two diagonal sites. Hence
\[
\|R-R^{<R}\|_1
\le4\sum_{0\le v<u<N,\,u\ge R}|z_{vu}|\,|w_{vu}|
\]
and therefore
\[
\boxed{
\|R(t)-R^{<R}(t)\|_1
\le4e^{12Jt}\sum_{\substack{0\le v<u<N\\u\ge R}}
\frac{(32J^2t^2)^{v+u}}{[(v+u)!]^2}.
}
\]
For fixed t, the right side tends to zero faster than an exponential as R increases, uniformly in N. Taking R≤N is understood for finite systems, while the infinite path sum gives a uniform dominating series. (Block compression X↦PXP is CP but generally trace-decreasing, unlike H33's nonpositive nearest-neighbor Schur mask.)

These bounds give an **explicit local approximation** to the signed residue witness. They do not control physical P6 measurement readout error automatically without a specified measurement map/trace inequality and independently calibrated sector.

## 4. Cancellation improves the first residue distance jet by one time power

H35 established for localized d=E00 that the first coefficient of each coherence is
\[
[t^{v+u}]\rho_{vu}(t)
=\frac{(-iJ)^v(iJ)^u}{v!\,u!}
\quad (v\ne u).
\]
The same complex coefficient appears at time 2t multiplied by \(2^{v+u}\). Therefore the leading product \(z_{vu}(t)\overline{w_{vu}(t)}\) is **real** at time degree \(2(v+u)\), so its imaginary edge current cancels at that degree. Every current contributing to site r≥1 has v+u≥r, hence
\[
\boxed{[t^m]R(t)_{rr}=0\quad(m<2r+1),\qquad r\ge1.}
\]
For root r=0, the first possible degree is three. Note this is a **lower bound on the first possible order**, not a claim that a nonzero coefficient necessarily occurs at every site in every model: all-zero diagonal energies can yield additional cancellations, and the signed witness can even vanish identically for symmetry reasons.

The depth-three time coefficient is completely explicit:
\[
z(t)=tA+\tfrac{t^2}{2}B+O(t^3),\quad
w(t)=2tA+2t^2B+O(t^3),
\]
with \(A=Q\mathcal L_\gamma(d)\), \(B=Q\mathcal L_\gamma^2(d)\), so
\[
\boxed{[t^3]R(t)=\Delta_D([A,B]).}
\]
For this nearest-neighbor chain, with real hopping J and \(d=E_{00}\),
\[
[t^3]R_{00}=2iJ^2(v_0-v_1),\quad
[t^3]R_{11}=-2iJ^2(v_0-v_1),
\]
with all other diagonal entries zero. This is **independent of the control-independent site-dephasing rate** gamma because its \(B\) contribution is a multiple of A, which commutes with A. If v0≠v1 this is a concrete nonzero **original P3 signed quadratic-residue witness** in a standard GKSL chain. It is **not** a CR-only signal, nor a claim R2=0 for the full filtration.

## 5. Exact finite audit and rational full-time certificate

P3/P9H36OriginalP3QuadraticResidueSoftLocalityExactCheck.py imports H35's previously CI-passed exact Gaussian-rational model and independently computes:
- 8 N=5 parameter sets (two rational J, two nonnegative gamma, two onsite-potential vectors) through 12 time orders;
- every signed matrix coefficient of R(t), including anti-Hermiticity, zero trace, first forbidden time powers below 2r+1, and exact cubic coefficient;
- exact equality between the edge-current divergence and the original P3 diagonal commutator;
- one *rigorous finite-time rational certificate* for J=1/2, gamma=2/3, t=1/64, potential v=(0,1/7,-1/9,2/11,-3/13).

At that time, \(12Jt<1\) so \(e^{12Jt}\le(1-12Jt)^{-1}\) is an exact rational majorant. The original semigroup matrices rho(t),rho(2t) are replaced temporarily by degree-16 rational Taylor polynomials, but an independent entrywise generator supnorm bound \(M_0\le4J+\gamma+\max v-\min v\) provides **rigorous rational errors**
\[
\varepsilon_s\le\frac{(M_0s)^{17}}{17!\,(1-M_0s)}
\quad(s=t,2t,\quad M_0s<1).
\]
Positivity/tracenormalization of the exact semigroup gives |rho_{vu}(s)|≤1. The induced error of each signed residue diagonal is bounded by
\[
2(N-1)\bigl[\varepsilon_t+(1+\varepsilon_t)\varepsilon_{2t}\bigr].
\]
The checker certifies the *full physical residue*, not just its polynomial approximation, lies below each site bound and that every radius-cutoff trace-norm error lies below its explicit Dyson majorant. The general all-time proof is analytic; the rational example is a reproducibility certificate, not a replacement for that proof.

## 6. Relationship to H34/H35 and remaining research gates

H34 showed why a **strongly invariant, strictly radius-one microscopic operator system** is incompatible with the particular connected H32 rational discrete channel. H35 replaced hard invariance with **soft, quantitative GKSL propagation** in a separate local continuous-time comparison model. H36 brings that back to the **correct P3 quadratic residue itself**, proving a signed witness-level factorially localized divergence current and certified block truncation error.

No identification is claimed between the H32 one-step channel and H35/H36's GKSL semigroup, between this selected \(\mathcal R_3\) witness and the **entire** residue space, between P3 dynamic \(\mathcal H_k\) and P6's independently inherited bounded-static \(\mathcal J_N\), or between a residue divergence and physical spacetime curvature. The dephasing independence of the **cubic leading coefficient** is not an unconditional CR-only discriminator; ordinary GKSL predicts the same.

Open: the microscopic sector provenance from P3/P4 to frozen P6 \(\mathcal J_N\), actual physical coherent readout/calibration, microscopic-to-operational two-step intertwining, B14/B15/B17 physical gates, metric soldering and Einstein/ADM/HDA.

**Candidate next H37:** propagate these quantitative signed-witness error bounds through a **specified physical P6 observer/map**; determine whether a localized physical readout and calibrated phase adjustment preserves the same residue agreement or whether additional nullspace/cycle-current ambiguities remain. Avoid claiming an experiment or new curvature merely because the bound is finite.

## References and reproducibility

Original P3 quadratic filtration and flow–residue factorization from the frozen P3 paper; H35 analytic Dyson locality from Draft PR #54. All code uses stdlib Fraction / H24 Gaussian rationals. No new literature precedence/novelty claim beyond these stated finite observations; no Lean kernel proof or human peer review.