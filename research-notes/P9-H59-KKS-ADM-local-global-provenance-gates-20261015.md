# H59 — KKS→ADM: Local Symplectic Possibility, Global Cohomological No-Go, and K₄ Observer-Provenance Gate

**2026-10-15 | P3–P11 Mathematical Bridge → P9 GR-I, in parallel with P9.64.** Stacked on H58 Draft [PR #77](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/77); H58 GitHub Actions **71/71 PASS** before H59 started. H59 does **not** presume the precise microscopic orbit or outcome of P9.64. It audits possible/excluded logical structures using an explicit **independently selected 4-site U(4) quantum density orbit** and a **different auxiliary six-spin local example**. Both are ordinary mathematical comparator models; neither is claimed as the actual original-P3 residue-generated physical source or a derivation of EH/ADM dynamics. Frozen manuscripts/main unchanged; no Lean kernel theorem, human expert referee, or experiment.

## 1. Candidate source: a genuine four-component compact KKS orbit, and exact dimension test

Independently choose a four-level quantum density with strictly positive **nondegenerate** spectral values
\[
\rho_\star=\operatorname{diag}\left(\frac1{10},\frac2{10},\frac3{10},\frac4{10}\right),\qquad
\mathcal O_\rho=\{U\rho_\star U^\dagger:U\in U(4)\}.
\]
This is the full flag coadjoint orbit \(U(4)/U(1)^4\) of real dimension
\[
\boxed{\dim_{\mathbb R}\mathcal O_\rho=4^2-4=12.}
\]
This does **not** say the actual microscopic P9.64 physical orbit is this particular \(\mathcal O_\rho\). It shows **dimension 12 can occur in an entirely standard four-component density model**, so blanket claims that a four-component KKS orbit cannot have six ADM coordinate-momentum pairs are false.

For each \(a<b\), define skew-Hermitian generators \(X_{ab}=E_{ab}-E_{ba}\) and \(iS_{ab}=i(E_{ab}+E_{ba})\). Use the explicit KKS convention
\[
\omega_{\rho_\star}([X,\rho_\star],[Y,\rho_\star])
=-i\,\operatorname{Tr}(\rho_\star[X,Y]).
\]
Then \([X_{ab},iS_{ab}]=2i(E_{aa}-E_{bb})\), and the six root-plane symplectic blocks obey
\[
\boxed{
\omega_{\rho_\star}(X_{ab}^{\#},(iS_{cd})^{\#})
=2(\lambda_a-\lambda_b)\,\delta_{(ab),(cd)}.
}
\]
In the ordered six-X/six-iS tangent basis, \(\omega_{\rho_\star}\) is a 12×12 anti-symmetric matrix \(\begin{pmatrix}0&D\\-D&0\end{pmatrix}\) with
\[
D=\operatorname{diag}(-\tfrac15,-\tfrac25,-\tfrac35,-\tfrac15,-\tfrac25,-\tfrac15).
\]
The all-rational checker verifies its rank 12 and
\[
\boxed{\det\omega_{\rho_\star}
=\left(\frac{12}{5^6}\right)^2=\frac{144}{244140625}>0.}
\]
By contrast, a 4-site orbit with spectral multiplicity partition \(3+1\), \(2+2\), \(2+1+1\) has respectively dimensions \(6,8,10\), and cannot locally parameterize an **open full 12-dimensional ADM canonical fiber** by a rank-preserving symplectomorphism. It may still embed as a smaller constrained symplectic sector. A full-rank source is necessary for an *onto full fiber* local isomorphism, not sufficient for physical provenance or dynamical intertwining.

## 2. Strong global obstruction: compact KKS forms cannot pull back from an exact canonical ADM cotangent phase space

**Theorem H59.1 — exact-target/global-orbit No-Go.** Let \((\mathcal O,\omega_{\rm KKS})\) be a compact nonzero-dimensional coadjoint orbit with nontrivial symplectic form, and let the target be any globally exact symplectic phase space \((T^*\mathcal Q,\Omega_{\rm can}=d\Theta)\), such as the cotangent space of an ADM metric configuration chart **before gauge/symplectic reduction**. There is **no globally defined smooth map**
\[
F:\mathcal O\longrightarrow T^*\mathcal Q
\]
satisfying \(F^*\Omega_{\rm can}=\omega_{\rm KKS}\) on the whole orbit.

**Proof:** The pullback of an exact 2-form is exact: \(F^*d\Theta=d(F^*\Theta)\). But a positive-dimensional compact symplectic manifold has \([\omega]\ne0\): if \(\omega=d\alpha\), then its positive symplectic volume
\(\int_{\mathcal O}\omega^{n}/n!\)
would vanish by Stokes since it is exact, contradiction. The compact unitary orbit \(\mathcal O_\rho\) above has no boundary and is symplectic of dimension 12. Hence no such global F exists regardless of **the matching local dimension**.

**Concrete H59 U(4) obstruction certificate:** for the SU(2) subgroup mixing any two distinct eigenlevels \(a,b\), the orbit contains an embedded 2-sphere/CP¹ of spin radius \(r=\frac12|\lambda_b-\lambda_a|\). With standard KKS orientation,
\[
\boxed{\int_{S^2_{ab}}\omega_{\rm KKS}
=4\pi r=2\pi|\lambda_b-\lambda_a|\ne0.}
\]
For levels (0,1) the flux is \(\pi/5\). One may use north/south local potentials \(A_N=r(1-\cos\theta)d\phi\), \(A_S=-r(1+\cos\theta)d\phi\). Their transition differs by \(2r\,d\phi\), whose winding is nonzero; there is **no globally defined single primitive**. The Fraction verifier checks the exact rational coefficient of \(\pi\) and all six nondegenerate level gaps; the nonexactness conclusion uses the explicitly stated standard Stokes/KKS theorem, not finite numerical quadrature.

**Scope guards:** This No-Go applies to a map **defined on the entire compact source orbit** into a **globally exact** target with equality of the full forms. It does not prohibit local Darboux charts, patches with omitted cycles, a *noncompact* source reduction, a presymplectic quotient, a nonexact target after GR gauge reduction, or a map that preserves only a weaker constrained Poisson relation. All such modifications must be stated and justified independently; they cannot be silently confused with a global symplectomorphism to the standard unreduced ADM cotangent phase space.

## 3. Positive local example: a six-spin KKS product has an exact 12D Darboux-to-positive-K₄ cotangent chart

To show that a KKS source is **not automatically excluded locally**, choose **six independent** SU(2) spin coadjoint orbits \(S^2_{r,e}\) of positive radius \(r_e\). This is *a different mathematical candidate from the single U(4) four-site orbit*, and is **not** asserted to be original-P3 physical data.

On a local cylinder chart away from poles and a longitude branch cut, take Darboux coordinates \((\phi_e,z_e)\), \(|z_e|<r_e\), so that
\[
\omega_{\rm KKS}=\sum_{e=1}^6 d\phi_e\wedge dz_e.
\]
Set
\[
\boxed{w_e=e^{\phi_e}>0,\qquad p_e=z_e e^{-\phi_e}.}
\]
Then \(dw_e=w_ed\phi_e\) and \(\sum p_e\,dw_e=\sum z_e\,d\phi_e\). Therefore
\[
\boxed{\sum_e dw_e\wedge dp_e
=\sum_e d\phi_e\wedge dz_e.}
\]
This is a genuine local symplectomorphism of real dimension 12 onto an open subset of the **positive-edge K₄ cotangent chart**, as a statement about **abstract symplectic manifolds**. At an exactly specified rational evaluation point \(w=(2,3,5,7,11,13)\), \(z=(1/10,-1/8,1/7,-1/6,1/9,-1/5)\), its 12×12 Jacobian satisfies
\[
J^\top \Omega_{\rm can}J=\Omega_{\rm KKS},\qquad \det J=1
\]
exactly using Gaussian rationals (here all coefficients are actually real Fractions). The checker also tests 24 edge permutations and common positive scaling as local cotangent maps.

**What this does NOT supply:** any independently derived physical map from the microscopic \(U(4)\) orbit \(\mathcal O_\rho\); the correct site-observer/causal-control algebra; physically sourced choice of six spins; any local Lorentzian solder; the full spacetime canonical functional Dirac delta brackets; a KKS Hamiltonian whose flows intertwine with ADM; the EH action, constraints, HDA or Einstein equations. The Darboux theorem by itself guarantees local symplectic coordinates, **not** emergence of ADM physics.

## 4. H58's repaired orientation-positive S₄ lift meets a sharp P3 observer-algebra gate

H58 gave an orientation-preserving 3D representation of all 24 projective K₄ root-line symmetries:
\[
Q_\sigma^+=\operatorname{sgn}(\sigma)\,Q_\sigma
\in SO(G),\qquad \sigma\in S_4.
\]
At the level of the **four site Hilbert states**, let \(P_\sigma\) be the real permutation matrix, \(\Pi_0=\mathbf1\mathbf1^\top/4\), \(\Pi_S=I-\Pi_0\). There is an exact 4×4 real-orthogonal (hence unitary) lift that fixes the trivial 1-mode and acts as \(Q_\sigma^+\) on S:
\[
\boxed{
W_\sigma=\Pi_0+\operatorname{sgn}(\sigma)P_\sigma\Pi_S.
}
\]
The checker verifies for all 24 permutations:
\[
W_\sigma^\top W_\sigma=I,\quad W_\sigma\mathbf1=\mathbf1,\quad
W_\sigma W_\tau=W_{\sigma\tau},
\]
and the action on KKS tangent generators by \(\operatorname{Ad}_{W_\sigma}\) is a true KKS symplectomorphism, since unitary conjugation preserves \(-i\operatorname{Tr}(\rho[X,Y])\).

**But there is a physically important distinction.** For **even** site permutations, \(W_\sigma=P_\sigma\), so the original site-population diagonal MASA \(D_4\) is preserved. For **odd** permutations,
\[
\boxed{W_\sigma=\tfrac12\mathbf1\mathbf1^\top-P_\sigma,}
\]
and every matrix entry has absolute value \(1/2\), so \(W_\sigma E_{00}W_\sigma^\top\) is NOT diagonal: the original four-site population observer algebra is **not preserved**. Thus:

- The mathematical H58 full S₄ **orientation-repaired** symmetry does have an honest unitary KKS-orbit lift if non-permutation coherent four-site controls are permitted.
- If physical controls are restricted to **literal site-permutation matrices**, while the trivial time sector is fixed with sign + and the 3D S spatial orientation is fixed, the **odd** repaired transformations are NOT among those permitted controls. Only the even/A₄ restriction is automatically compatible with that specified hardware.
- If one permits odd coherent gates \(W_\sigma\), then their action leaves the original site diagonal observer algebra \(D_4\), so the purportedly preserved P3 observer closure must be **enlarged or appropriately transformed**. A change in observer algebra/protocol is not free or automatically inherited from frozen P6.

This is a **conditional physical-accessibility no-go**, not a claim that no standard U(4) unitary exists: the explicit \(W_\sigma\) is such a unitary. If an alternative microscopic construction uses a different time sector, different source algebra, phase conventions, or allowed controls, those premises require fresh testing and can evade this specific constraint.

## 5. Precise handoff to P9.64

Use H59 as a screening ledger, not as a claim to have completed P9.64:

1. **Declare the actual source KKS orbit, stabilizer and dimension/rank**. Four-site **generic mixed** density U(4) orbits do have local rank 12; degenerate multiplicity types do not fill the entire 12D ADM fiber. A 12D tangent rank alone does not establish an ADM phase-space map.
2. **State local vs global domain.** If asserting a *global* symplectic map from an entire nontrivial compact U(4) orbit into an unreduced exact ADM cotangent space, H59.1 prohibits it, irrespective of equal dimension. A local chart or source/target reduction is viable only with an explicit topology and overlap prescription.
3. **Prove actual 2-form equality**, not merely pointwise tensor rank, a symmetric DeWitt quadratic form, 24-cell symmetry or a finite KKS normalization. Prove \(\mathcal F^*\Omega_{\rm ADM}=\omega_{\rm KKS}\) on its stated domain.
4. **Derive/declare the microphysical action of root-line symmetries on the observer and controls**, especially the odd repaired \(W_\sigma\) requiring non-permutation coherent action and changing the site MASA.
5. **Separately generate or intertwine Hamiltonian/constraint dynamics, spatial gluing, physical 1+3 solder, boundary conditions and full HDA**; local Darboux existence and symplectic topology are **not** Einstein dynamical provenance.

**H60 candidate:** if P9.64 supplies a real candidate map with explicit microscopic KKS orbit, controls and observer, evaluate its exact pullback 2-form (including degeneracies/reductions), root-cone/solder group action and dynamical Hamiltonian intertwiner. In the absence of that independently specified candidate, the next rigorous step is to classify *local* symplectic patch gluing and topological flux/transition obstructions under admissible constrained reductions, rather than falsely identifying the six-spin Darboux example with physical gravity.

## Reproducibility

`P3/P9H59KKSADMSymplecticOriginObstructionExactCheck.py` uses Python standard-library `fractions.Fraction`, plus previously independently checked H52/H58 finite K₄ functions. It verifies the U(4) KKS 12×12 skew matrix, spectral orbit dimensions, all 24 mathematically lifted S₄ actions on the orbit and the original diagonal MASA obstruction, nonzero KKS two-sphere flux coefficient, and the exact 12×12 symplectic Jacobian of the abstract six-spin local positive-edge chart. The global nonexactness theorem uses the stated compact-orbit Stokes argument; it is not a claim that numerical enumeration proves cohomology. Dedicated CI is part of a stacked Draft PR; main/frozen manuscripts untouched.
