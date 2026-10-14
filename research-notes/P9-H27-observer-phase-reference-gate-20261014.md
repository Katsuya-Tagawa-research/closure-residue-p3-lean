# P9 H27 — Physical-observer gate for reconstructing an internal phase connection

**2026-10-14.** Exact finite H27 audit, stacked on H26 Draft PR #44. Reuses H24's *actual* nonzero original P3 quadratic residue via its explicit rational-Gaussian two-level unitary CPTP channel; does not infer a physical P6 link apparatus, a unique physical connection, or any Levi-Civita/Regge curvature. Main and frozen P3 untouched. New result is checked using Python exact Gaussian rationals, not Lean formalization.

## 1. The observer-stabilizer ladder, at one cell

Let U and Phi(A)=UAU† be the H24 unitary. The first hidden Krylov direction of the original P3 filtration is
```math
z_1=Q\Phi(Z)=\begin{pmatrix}
0&a\\\bar a&0
\end{pmatrix},\quad a=(8+4i)/9\ne0.
```
Take a *diagonal* SU(2) population-gauge element `g(q)=diag(q,bar q)`, `|q|=1`, and its effective phase `tau=q²`. Its adjoint conjugation acts on the offdiagonal coefficient by `a→tau a`.

**Finite stabilizer criterion.** These three increasingly rich declarations give:
1. Preserve the diagonal algebra pointwise: **all** effective `tau∈U(1)` remain (populations are insensitive).
2. Preserve the first hidden *complex line as an unlabeled subspace*, `Ad_g(C z1)=C z1`: **only** `tau=±1` remain. Proof: on upper/lower entries the would-be common complex scalar must equal both `tau` and `bar tau`; hence `tau=bar tau=±1`.
3. Preserve the **labeled, phase-calibrated** `z1` (or preserve `Phi(Z)` itself): **only** effective `tau=1` remains, since `a≠0`.

The residual center `q=±1` of SU(2) always acts trivially under adjoint, so “identity” here always means the **effective PU(2)/SO(2) action**, not uniqueness of a literal SU(2) lift.

Moreover, if identical H24 local channels are connected by a diagonal phase g and one *adds* the strong naturality requirement `Ad_g◦Phi = Phi◦Ad_g` even just on the diagonal Z, then g must fix `Phi(Z)`, so `tau=1`. This demonstrates a **flatness trap**: demanding strict intertwining of identical, phase-calibrated microscopic dynamics via diagonal phases rules out a nontrivial effective SO(2) edge twist. This is conditional on identical channels and on the extra intertwining axiom; it is *not* a universal P6 theorem.

## 2. A nonzero parallel first-residue section forces flatness

On a connected graph with edge phases `t_uv∈U(1)`, let nonzero locally calibrated first-hidden offdiagonal amplitudes `a_v` all have the same norm. If one postulates **exact covariant constancy**
```math
t_{uv}a_u=a_v\quad\text{for every edge }u\to v,
```
then multiplying around any closed loop telescopes all nonzero `a_v` and forces `Hol(loop)=1`.

Thus **demanding transport preserve the *same labeled* nonzero first-residue amplitude on every edge is sufficient for flatness**, not an origin of nonzero curvature. H26's nontrivial loop transports necessarily break this stronger condition. A curvature-producing bridge must instead allow and model the edgewise covariant mismatch, or provide independent phase-sensitive cross-cell measurements.

## 3. Conditional two-quadrature intercell phase readout

Let `t_uv∈U(1)` be given by an *additional* intercell connection/coupling, not by cell-local P3 residue alone. Define the dimensionless complex link observable
```math
c_{uv}=\frac{\overline{a_v}\,t_{uv}\,a_u}{|a|^2}
\quad\in U(1),\qquad |a_u|=|a_v|=|a|>0.
```
Under independent local phase gauges `a_v→lambda_v a_v`, `t_uv→lambda_v t_uv bar(lambda_u)`, this c_uv is **gauge invariant**. For a closed oriented loop `ell` (reverse edges use complex conjugates),
```math
\prod_{e\in\ell} c_e=\prod_{e\in\ell} t_e,
```
because the local amplitudes telescope. Thus **if** the complex relative phase `c_uv` is independently measurable for each link, the loop holonomies are measurable and the **abelian** U(1) connection is reconstructed up to vertex gauge from a cycle basis, as in H26.

The difference between *one* and *two* quadratures matters operationally. A standard quantum mechanical **declared comparator** prepares `|+>=(|0>+|1>)/sqrt 2`, applies the calibrated unitary `V_c=diag(1,c)` and measures Pauli `X,Y`:
```math
\langle X\rangle=\Re c,\qquad \langle Y\rangle=\Im c.
```
Both measurements together identify the full complex `c`; `X` alone does not distinguish `c` and `bar c`. For rational SU(2) phase `q=(3+4i)/5`, `c=q²=(-7+24i)/25`, the two cases `c` and `bar c` have identical X expectation -7/25 but opposite Y values ±24/25. Populations remain one-half for every c. This is a **standard unitary CPTP interferometric protocol**, not a CR-specific prediction.

**Essential physical gap:** Implementing `V_c` with the actual intercell phase c, establishing a coherent intercell reference, calibrating the cross-cell observable, and proving it lies within the independently fixed *physical* P6 admissible control/measurement manifold are all extra tasks. Writing a possible Ramsey circuit alone does not derive an interface transport from P3/P6.

## 4. Exact graph tests

The checker repeats H26's four-cell graph with a three-edge spanning tree and two chords (b1=2). It assigns one rational phase to chord 02 and another to chord 03, verifies that complex gauge-invariant edge readouts are unchanged under arbitrary independently chosen local rational phases, and that their two oriented loop products equal the actual connection holonomies.

It also constructs a pure-gauge connection `t_uv=lambda_v bar(lambda_u)` with a nonzero covariantly constant section and proves both loop holonomies are identity; verifies phase-matched identical-channel naturality excludes a nontrivial diagonal twist; and checks the SU(2) population/hidden-line/labeled-generator stabilizers.

## 5. H27 gate and consequences for P9

H27 has a **conditional mathematical success**:
- the abstract distinction between local CR observables and a physical intercell connection is sharp;
- the extra *kind of* observational datum that would recover U(1) loop holonomy is explicitly identified;
- a testable CPTP two-quadrature comparator exists, with a one-quadrature ambiguity;
- naive *parallel labeled-residue matching* would force **zero** holonomy, so cannot be used as a general curvature-generation rule.

H27 **does not achieve the strong physical-bridge success** of deriving the cross-cell instrument or transport from inherited P6 accessibility. In the general nonabelian SO(3) case, all individual loop angles are insufficient; H25's simultaneous-conjugacy and group-holonomy data remain necessary. H24's residue is 2x2, not a spatial Regge/Levi-Civita tensor. B14 physical six-edge provenance, B15 GKSL comparator, B17 work-conjugate force, physical constraint propagation and Einstein dynamics remain open.

**Next gate H28:** build (or no-go) an explicit interface control/measurement transport and its gauge-natural phase reference from a physical P6 model, then test whether geometric soldering with an *independently specified* cell metric/Levi-Civita connection is possible. Do not infer soldering from dimension matching alone.

## Reproducibility

`P3/P9H27PhaseReferenceExactCheck.py` imports H24's rational-Gaussian first-hidden witness on the same research branch, then uses standard-library `fractions.Fraction` with exact complex rational arithmetic; all claims are checked without floating-point tolerances. GitHub Actions executes the checker independently. No Lean kernel proof or human peer-review claim.
