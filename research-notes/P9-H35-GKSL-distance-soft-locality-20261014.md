# H35 — Exact GKSL distance jets and soft-locality tails
**2026-10-14 | P3–P11 Mathematical Bridge | mathematical audit candidate.**
Stacks on P9.38 Cross-Audit A (#53), following H34 (#52). This is **not** a claim that H32's discrete one-step channel equals the new continuous-time GKSL semigroup; the two are different comparison models. No frozen papers/main changes, no Lean proof or human peer review.

## 1. Model and exact leading-jet theorem

Fix the one-ended N-site path with sites 0,...,N-1. Choose a nearest-neighbor Hermitian hopping Hamiltonian and ordinary uniform site dephasing:

\[
H=J\sum_{r=0}^{N-2}(E_{r,r+1}+E_{r+1,r})+\sum_r v_rE_{rr},
\qquad J>0,\ v_r\in\mathbb R,
\]
\[
\mathcal L_\gamma(\rho)=-i[H,\rho]+\gamma(\Delta_D\rho-\rho),
\qquad\gamma\ge0,\qquad \rho(0)=E_{00}.
\]

This is standard CPTP GKSL dynamics: Lindblad operators are \(\sqrt\gamma E_{rr}\). In the doubled path basis E_jk, write L=D+B. D acts diagonally on each matrix unit, with coefficient \(-\gamma(1-\delta_{jk})-i(v_j-v_k)\), and B moves exactly one of j,k by one nearest-neighbor step. Thus at least j+k hopping events are needed to reach the (j,k) entry from (0,0).

**Theorem H35.1 (leading distance jet):** For all finite N, all positive J, arbitrary real diagonal energies v and all gamma≥0,

\[
[t^m]\rho_{jk}(t)=0\quad(m<j+k),
\qquad
\boxed{[t^{j+k}]\rho_{jk}(t)
=\frac{(-iJ)^j(iJ)^k}{j!\,k!}.}
\]

In particular for the site-r population,

\[
\boxed{p_r(t)=\frac{J^{2r}}{(r!)^2}t^{2r}+O(t^{2r+1}),\quad r\ge1.}
\]

The coefficient is positive and independent of diagonal energies/dephasing; higher coefficients need not be. The coefficient comes from the binomial number \(\binom{2r}{r}\) of shortest doubled-index trajectories, each of length 2r with r ket and r bra hops. Every dissipative or onsite insertion adds a factor of t and cannot modify this coefficient. Hence for every fixed finite r, p_r(t)>0 for **all sufficiently small** t>0: no exact instantaneous finite-range hard support cone. Do not assert positivity at every positive time, when coherent cancellations can occur.

## 2. All-time uniform Dyson tail theorem

The diagonal part D satisfies \(|e^{sD_{jk}}|=e^{-\gamma s(1-\delta_{jk})}\le1\) for s≥0, regardless of v. Each hopping insertion has modulus J, with at most four possible next doubled-index neighbors. The m-hop Dyson time simplex has volume \(t^m/m!\). The resulting **rigorous for all t≥0 and all gamma≥0** matrix-entry bound is

\[
\boxed{|\rho_{jk}(t)|
\le\sum_{m\ge j+k}\frac{(4Jt)^m}{m!}
\le e^{4Jt}\frac{(4Jt)^{j+k}}{(j+k)!}.}
\]

For total one-ended-chain population outside radius R,

\[
\boxed{\sum_{r=R}^{N-1}p_r(t)
\le e^{4Jt}\sum_{r=R}^{N-1}\frac{(4Jt)^{2r}}{(2r)!}.}
\]

The bound depends on hopping strength/time and distance, **not on gamma, v, or N** except for the summation range. More generally on a graph of max degree D and edge magnitudes ≤J, the same proof yields an entrywise bound with \(4J\) replaced by \(2DJ\) and j+k replaced by \(d_G(0,j)+d_G(0,k)\). The special exact leading coefficient formula with factorials requires the unique one-ended path and equal real hopping amplitudes.

This does **not** prove two-sided operator-norm/normalized-trace visible-leakage equivalence for dissipative GKSL dynamics. P6's previously proved comparison is an N-uniform exponential locality **class**; its stronger intrinsic equivalence is limited to the coherent subclass.

## 3. Fraction/Gaussian-rational finite checks and actual finite-time certificate

The exact Python checker (P3/P9H35GKSLLocalityTailExactCheck.py) audits the N=5 path for 12 rational model configurations (two J, three gamma≥0, two rational onsite potentials), every one of 25 matrix entries and degrees through ten. It checks trace, Hermiticity, vanishing low jets, complete leading coefficient formula and dephasing dependence of later jets.

To ensure finite Taylor tests are **not misrepresented as the full semigroup**, it separately establishes a certified rational remainder at one time. For t=1/16, J=1/2, gamma=2/3, v=(0,1/7,-1/9,2/11,-3/13), the entrywise generator bound is \(M_0\le4J+\gamma+(\max v-\min v)\). For M0*t<1, the error of the degree-n Taylor polynomial is bounded by

\[
\mathrm{Err}_n \le \frac{(M_0t)^{n+1}}{(n+1)!\,[1-M_0t]}.
\]

The checker verifies that the degree-16 exact Taylor partial sum **plus its rigorous error** lies below the rational Dyson upper bound \((4Jt)^{2r}/[(2r)!(1-4Jt)]\) for all r=1,...,4 and for aggregated beyond-radius leakage. General all-time theorem rests on the analytic Dyson proof above, not this single-time certificate.

## 4. Interpretation and strict boundaries

H33 showed that a radius-one static operator sector can have enough candidate Xi edge directions, but need not match P6's independently frozen physical microscopic J_N; its naive support Schur truncation is not a positive map. H34 showed that requiring strong invariance under H32's particular discrete rational CPTP channel forces an enlarged radius-two M3 operator system. **H35 gives a different, soft and quantitative description for a separately chosen local GKSL dynamics**: distance tails begin at definite time orders and obey uniform factorial bounds without an exact finite support cone.

No identification is made between this propagation tail, original P3 quadratic residue \(\Delta_D([z,w^\dagger])\), P6's physical control permission, or any spatial Levi-Civita/Regge curvature. These are all standard GKSL quantities. The new bounds therefore cannot constitute a CR-exclusive prediction or Einstein dynamics.

Remaining gates: an explicit *independently sourced* P3 microscopic to P6 physical-control provenance map and two-step intertwining; actual coherent/dissipative calibration; P9.38's diagonal-Hamiltonian gauge compensation where appropriate; physical S0(3) soldering; B14/B15/B17 constraints; off-shell HDA, conditional Einstein dynamics.

**Suggested H36:** formulate a graded/static-to-dynamic map on the inherited P6 operator sector and estimate quadratic P3-residue *tails* using this GKSL locality bound, without requiring hard invariance or equating a vector-space projection with CPTP.

## Reproducibility and review

Strict mathematical analytic proof + independent exact finite coefficient computations; dedicated Actions CI. No Lean kernel proof/human expert peer review claim. Keep PR draft and frozen originals unchanged.