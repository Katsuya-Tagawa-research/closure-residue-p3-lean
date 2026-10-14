# P9.23 -> P3-P11: H21-H23 independent finite audit

**2026-10-14. Status:** exact-rational finite matrix audit submitted, not Lean formalization and not an inherited P6 physical-control theorem. Independent Draft stacked on B20 PR #40; main and frozen P3 unchanged. Use **H21/H22/H23** provisional labels to avoid collision with bridge B18/B19/B20 (PRs #38/#39/#40).

## H21. Silent ideals — what is proved and what is not

If `g_acc` is an actual Lie algebra and `N=ker DΣ` is a linear subspace of it, the Lie bracket descends to `g_acc/N` iff `N` is a Lie ideal. The quotient bracket is otherwise not well-defined. This says **only** that Lie brackets with silent directions stay silent when N is an ideal; it does not say that every possible higher-order physical observable is silent.

On `so(4)` with `K_ab=E_ab-E_ba`:

- The 3-dimensional anti-self-dual subspace `span(K01-K23, K02+K13, K03-K12)` is an ideal. The complementary self-dual ideal commutes with it. This is a purely algebraic comparison; orientation determines which ideal is called self-dual.
- Projecting to the 3x3 lower-right rotation block (indices 1,2,3) has kernel `span(K01,K02,K03)`. It is not an ideal: `[K01,K02]=-K12` has nonzero visible block.
- **Counterexample to a stronger inference:** For *first-time diagonal population* readout, `diag[K,D(p)]=0` for every real antisymmetric K and diagonal p. Its kernel is **all of so(4)**, hence an ideal; nevertheless `(1/2)diag[K02,[K02,E00]]=(-1,0,1,0)≠0`. Therefore *ideal silence of a first derivative does not force second population silence*. The ideal criterion is specifically about Lie-bracket descent, not arbitrary second derivatives.

**Actual P6 qualification:** P6 v9.1, §1.5, defines a declared coherent-control tangent `κ_N:T_0M_N -> u(A_N)` and First-Residue Accessibility `ad_{κ_N(X)}|_{D_N}∈ R_N^(1)` with `R_N^(1)` inherited from `Xi_N(J_N)`. It does not, from that assumption alone, establish that the physically accessible tangent image is a Lie subalgebra, that every inverse-pulse commutator is admissible, or that K4's six controls are all reachable. Hence one cannot honestly decide `ker DΣ` is an ideal *for the actual P6 system* without separately fixing: (i) primitive admissible generators and their Lie closure, (ii) physical inverse-pulse/composition permission, (iii) observer response map with its measurement/readout order and preparation set, (iv) gauge quotient and its bracket consistency.

For the same **declared** full K4 `so(4)` controls different observers give different kernels: population-first-time N=g (ideal); B20 full coherence first-time N=0 (ideal); spatial 3x3 block N=span(K0i) (nonideal). These are not interchangeable response fingerprints.

## H21-to-P3 strict residue mismatch: decisive counterexample

P3 defines the *original quadratic commutator residue* for an observational diagonal algebra `D` as
```math
\mathcal R_k=\operatorname{span}\{\Delta_D([z,w^*]):z\in\mathcal H_i,\ w\in\mathcal H_j,\ i+j\le k\},
\quad\mathcal H_j=(1-\Delta_D)\mathcal M_j(D).
```
This is **not** `diag[K,[K,D]]` and not a control Lie commutator.

If the channel is conjugation by a real orthogonal `U` (including the real K4 coherent pulse family and its commutator loops), each `U^j d (U^T)^j` is **complex symmetric** for all complex diagonal d. Hence the entire hidden Krylov space `H_j` consists of offdiagonal complex symmetric matrices. For any complex symmetric z,w, `w^*=overline w` is symmetric, and
```math
( [z,w^*] )_{aa}
=\sum_b(z_{ab}\overline{w_{ab}}-\overline{w_{ab}}z_{ab})=0.
```
Consequently `R_k={0}` at **every depth** for such an orthogonal-conjugation P3 model. This is consistent with nonzero first hidden response, nonzero P6 population quadratic return and nonzero Lie-control holonomy. The checker verifies all first-order diagonal-seed symmetric-hidden pairs; the argument above gives the general all-depth result.

**Critical conclusion:** Neither `[N,g] not subset N` nor `[K01,K12]≠0` certifies P3 `R_k≠0`. A genuine P3-to-P9 curvature bridge needs either a microscopic channel that generates *phase-sensitive, nonsymmetric hidden operators* and a specified nonzero P3 `R_k`, or an additional explicit morphism relating the P3 commutator residue to P6 nested-derivation return. One must not silently replace P3's definition.

## H22. CPTP group-commutator holonomy and readout order

Set `A=K01`, `B=K12` and
```math
U_square(eps)=e^{eps A}e^{eps B}e^{-eps A}e^{-eps B}
=I+eps^2 K02+O(eps^3).
```
All exact factors are real orthogonal/unitary, hence the conjugation channels are CPTP for every real eps. With diagonal `rho=E00`, the *coherence* output `rho'_{02}` has coefficient `-eps^2`, while the *diagonal population* difference has leading coefficients
```math
\Delta\operatorname{diag}\rho'
=eps^4(-1,0,1,0)+O(eps^5).
```
The checker obtains these from exact rational truncated series to degree 5. The general order claims require a preparation with nonzero contrast and an appropriate measured coherence; special states (e.g. uniform maximally mixed) have no signal.

This is fully consistent with orthodox unitary quantum mechanics: it is **not CR-specific**. Its order-eps^4 population return is also not P3's original quadratic commutator residue, which is zero for this real-orthogonal channel family.

## H23. CR-to-Regge soldering cannot be inferred from internal holonomy

A candidate intertwining on adjacent cells T,T' is
```math
U_{TT'}=e_{T'}^{-1}P^{LC}_{TT'}e_T.
```
This requires physical maps `e_T` (soldering) preserving the declared metric/orientation and an independently specified physical Levi-Civita or Regge parallel transport `P^{LC}`. Around a closed loop based at T it implies the **necessary** conjugacy condition
```math
U_{hol}=e_T^{-1}P^{LC}_{hol}e_T,
\qquad \operatorname{tr} U_{hol}=\operatorname{tr} P^{LC}_{hol}.
```
The checker records a simple obstruction: internal identity holonomy has trace 3, but a nontrivial 90-degree geometric rotation has trace 1. No invertible soldering map can reconcile them. This is a **data-compatibility no-go**, not an assertion that actual P9 cell data exhibit this mismatch. Further required gates: independent physical metric from CR, face/cell matching, metric compatibility, orientation, path composition, torsion/closure (as appropriate), and continuum control. Nonzero internal Lie holonomy is not a derivation of physical curvature.

## B14/B15/B17 and P9 minimum success unchanged

B14 six-edge *physical* CR accessibility is unproved; B15 standard GKSL/Markov comparator remains; B17 actual physical work-conjugate force remains unknown. Nothing in H21-H23 delivers physical soldering, propagating spin-two dynamics, canonical gravitational constraints, an Einstein-Hilbert action, or Einstein equations.

## Reproducibility

`P3/P9H21H23SilentHolonomyExactCheck.py` is an exact rational, pure Python-standard-library matrix and formal-epsilon-series checker. It checks both ideals via brackets, the nonideal block witness, the ideal-but-return example, first-hidden-pair P3 residue zero, group-loop leading terms, separate coherence/population orders, and closed-loop trace mismatch. The all-depth P3 vanishing result is a separate elementary symmetry argument above rather than a claim that the finite script enumerates all Krylov depths.
