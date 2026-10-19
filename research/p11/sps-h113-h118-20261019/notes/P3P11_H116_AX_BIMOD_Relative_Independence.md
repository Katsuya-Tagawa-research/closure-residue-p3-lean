# H116 — Independence of AX-BIMOD: Fixed Diagonal-Torus Invariance versus Gauge Covariance

**2026-10-19 (Asia/Tokyo)**  
**Workstream:** P3–P11 Mathematical Bridge / P11 foundational axiomatization  
**Status:** finite matrix exact audit (54/54 assertions PASS), analytic equivalence theorem and a *relative* expansion/countermodel argument. No general proof of the logical independence of AX-BIMOD from a completed first-order presentation of all P3/P4 axioms. No physical source identification, experiment, human peer review, external AI audit, GitHub CI, or P11 Generative Completeness.

## A. Mathematical objects and strict inference boundary

The fixed **H37 five-site** model uses the basis `0,...,4`, diagonal maximal abelian subalgebra `D_5=span_C{p_i}` where `p_i=E_ii`, and

\[
X_e=E_{e,e+1}+E_{e+1,e},\quad
K_e=E_{e,e+1}-E_{e+1,e},\quad
H_{\mathrm{hop}}=\tfrac12\sum_{e=0}^3X_e,
\]
\[
H=\operatorname{diag}(0,1/7,-1/9,2/11,-3/13)+H_{\mathrm{hop}},\qquad
\mathcal L(A)=-i[H,A]+\tfrac23(\Delta_D(A)-A).
\]

The **declared**, not physically certified, native coherent space is `K_nat=span_R{K_0,K_1,K_2,K_3}`. The extra static P6-sector label `J` is *not determined by the definition of* `(L,D_5,K_nat)` or the H37 response protocols.

The **weak bridge interface** `T_weak` permits any `J` satisfying: (a) off-diagonal, radius-one relative to `D_5`; (b) complex-linear and *-stable; (c) `H_hop∈J` and all native `K_e∈Xi(J)`; (d) internal quadratic diagonal residue span of rank four. We use `Xi(J)={z-z* : z∈J}` as a real vector space because `J` is entirely off diagonal. This interpretation agrees with Step 1D's `(1-Delta_D)(J-J*)` convention.

Distinguish three notions of gauge:

* **AX-GAUGE-COV:** A selector `sigma` on *marked-input data* is equivariant: `sigma(U.c)=U sigma(c) U*`. Here the native controls, Hamiltonian and reference frames in `c` all transform.
* **AX-GAUGE-FIX:** An individual output `J` is invariant under all diagonal `U`: `UJU*=J`, even without treating `U` as a symmetry of the marked input `c`.
* **AX-BIMOD:** An individual `J` obeys `D_5 J D_5⊆J`, i.e. is stable under independent diagonal left/right multiplications.

**AX-GAUGE-FIX is stronger than AX-GAUGE-COV.** Neither should be silently substituted for the other.

## B. Theorem H116.1 — relative independence on the fixed H37 base

Define

\[
J_{\rm mix}=\operatorname{span}_\mathbb C\{H_{\rm hop},K_0,K_1,K_2,K_3\},\qquad
J_{\rm full}=\operatorname{span}_\mathbb C\{E_{e,e+1},E_{e+1,e}:0\le e\le3\}.
\]

Both satisfy `T_weak` for the **same** fixed data `(D_5,L,H_hop,K_nat)`:

| Exact property | Mixed | Full |
|---|---:|---:|
| `dim_C J` | 5 | 8 |
| `dim_R Xi(J)` | 5 | 8 |
| Internal quadratic diagonal residue rank | 4 | 4 |
| Radius-one, off-diagonal, star-stable | yes | yes |
| `D_5 J D_5 ⊆ J` | **no** | **yes** |

Proof: `p_0 H_hop p_1=E_01/2`, but `E_01` is outside `J_mix`. Conversely `p_i E_ab p_j=delta_ia delta_bj E_ab`, so `J_full` is a `D_5`-bimodule. Inclusion of `K_e`, star-stability, support and ranks are exact rational matrix checks. The quadratic rank follows from the four independent incidence vectors `Delta_D([H_hop,K_e])`, or equivalently the adjacent `E` commutators.

**Logical interpretation.** In a language where the fixed P3/P4 channel/observational data do not refer to the newly introduced `J`, and where `T_weak` is exactly the bridge category, a single fixed underlying structure has two admissible expansions, one satisfying AX-BIMOD and one satisfying its negation. Therefore `T_weak` does **not entail** AX-BIMOD and does **not entail** its negation. This is a relative model-expansion independence result. To call it absolute model-theoretic independence of AX-BIMOD from *all* P3/P4 axioms requires their complete formal language/axioms plus a proof that they contain no further relevant static-sector constraints. That separate task is OPEN.

No inference of `J` from the H37 channel or all marked input-output words is possible in this category: the same marked channel-control data accompany both labels, so the projection from labeled models to marked data is noninjective. This is the H113 fibre obstruction applied at the H37 point. This **does not** rule out a new independent primitive source, a physically justified stronger category, or newly available interventions.

## C. Theorem H116.2 — equivalence of fixed torus invariance and diagonal bimodule (off-diagonal case)

For every `N>=2`, let `D_N` be the standard diagonal maximal abelian algebra, `O_N=ker Delta_D` the complex off-diagonal subspace, and `T^N` the group of diagonal unitaries. For **any complex linear `J⊆O_N`**,

\[
\boxed{ UJU^*=J\quad\forall U\in T^N
\iff D_NJD_N\subseteq J. }
\]

*Proof (⇒).* `E_ij` (`i≠j`) has torus character `chi_ij(z)=z_i \bar z_j`. These characters are pairwise distinct on `T^N`. For `a∈J`, Fourier averaging over the compact group yields

\[
\int_{T^N}\overline{\chi_{ij}(z)}\,U(z)aU(z)^*\,dz=a_{ij}E_{ij}\in J.
\]

Therefore every supported matrix unit belongs to `J`. Multiplication on both sides by any diagonal `d_1,d_2` preserves `J`. *Proof (⇐).* If `D_NJD_N⊆J`, taking `d_1=U`, `d_2=U*` gives `UJU*⊆J`; using the inverse `U*` gives equality. QED.

On the H37 **off-diagonal radius-one** class containing all native `K_e`, AX-GAUGE-FIX/AX-BIMOD force `J_full`: each `K_e` contains a nonzero coefficient on both ordered edge matrix units; Fourier extraction isolates them. Locality excludes further matrix units. This is a **conditional uniqueness** statement.

**Necessary scope caveat:** This equivalence is false without `J⊆O_N`: e.g. `J=C I_N` is fixed by the entire torus but is not a `D_N`-bimodule, because `p_0 I_N p_0=p_0` is not in `C I_N` for `N>1`. To allow diagonal primitives requires separate diagonal-module axioms.

## D. Theorem H116.3 — gauge covariance does not select AX-BIMOD

Take the full *marked input* `c=(D_5,H_hop,K_0,...,K_3)` and define two sector assignments on its diagonal-gauge orbit:

\[
\sigma_{\rm mix}(c)=\operatorname{span}_\mathbb C\{H_{\rm hop},K_0,...,K_3\},
\quad\sigma_{\rm full}(c)=J_5^{D}(\{K_e\}).
\]

For any diagonal `U`, define `U.c` by simultaneous conjugation of all marked matrix inputs. Then

\[
\sigma_{\rm mix}(U.c)=U\sigma_{\rm mix}(c)U^*,\quad
\sigma_{\rm full}(U.c)=U\sigma_{\rm full}(c)U^*.
\]

Thus **both selectors are covariant**. Yet the first is not a bimodule: this is an explicit counterexample to `AX-GAUGE-COV ⇒ AX-BIMOD`.

For the exact diagonal unitary `U=diag(i,1,1,1,1)`,

\[
UK_0U^*=iX_0\notin J_{\rm mix},
\]

so `J_mix` is **not fixed** under `U`, although its *covariant family* transforms correctly. `J_full` *is* fixed. SymPy checks both exact claims, along with `J^D(U.S)=U J^D(S)U*`.

## E. Theorem H116.4 — H37's actual fixed-input diagonal-gauge stabilizer is trivial on sectors

Consider diagonal `U=diag(z_0,...,z_4)` with `|z_i|=1` and **require the fixed H37 Hamiltonian matrix itself to be unchanged**: `UHU*=H`. The four nonzero nearest-neighbor matrix entries `H_{e,e+1}=1/2` imply

\[
z_e\bar z_{e+1}=1\ \text{for }e=0,1,2,3,
\quad\Longrightarrow\quad z_0=z_1=z_2=z_3=z_4.
\]

Hence `U=z I_5`; conjugation by `U` is trivial on all subspaces `J`.

Consequently, requiring a candidate sector to be invariant **only under gauge transformations that leave this fixed marked H37 Hamiltonian unchanged** does **not distinguish** `J_mix` and `J_full`! To select `J_full` by gauge symmetry one must introduce the *stronger, gauge-frame-independent internal invariance* condition of Theorem H116.2 (or the equivalent AX-BIMOD), not just covariance or the stabilizer of the actual H37 input.

For the H37 Lindbladian the conclusion is also consistent with the nontrivial coherent hopping terms; this note proves the stated Hamiltonian stabilizer directly, not an exhaustive classification of every possible dynamical automorphism.

## F. Theorem H116.5 — even a uniquely selected bimodule does not identify primitive origins

Define `J^D(S)` as the star-stable diagonal-bimodule closure. Direct matrix-unit extraction gives

\[
\boxed{J^D(\{H_{\rm hop}\})=J^D(\{K_0,K_1,K_2,K_3\})=J_{\rm full}.}
\]

The sources are different even as linear generating collections (`dim_C span{H_hop}=1` versus `dim_C span{K_e}=4`), yet their bimodule closures are identical. Thus an axiom fixing a local **sector** cannot by itself certify which interactions were independently native, how many hardware knobs exist, whether phase contrasts are realizable, or how the source derives from `F`.

This is not a claim that these two source sets represent two experimentally verified H37 devices. It is the exact noninjectivity of the mathematical closure map.

## G. Result summary / P11 axiomatization gate

| Statement | Status |
|---|---|
| Relative independence of AX-BIMOD from explicitly stated weak H37 bridge interface | **EXACT (conditional scope)** |
| Fixed full diagonal-torus invariance ↔ bimodule for complex off-diagonal subspaces | **EXACT (all finite N)** |
| Gauge covariance alone ⇒ bimodule | **FALSE; exact counterexample** |
| Fixed-H37 Hamiltonian gauge stabilizer selects `J_full` | **FALSE; global scalar only** |
| AX-BIMOD plus off-diagonal radius-one support + `K_nat` chooses `J_full` | **EXACT, conditional** |
| Uniquely chosen sector ⇒ uniquely identified source | **FALSE; exact counterexample** |
| P3/P4 alone physically derive AX-BIMOD or P11's full source functor | **OPEN** |
| H37 physical phase-control/primitive provenance and P6 experiment | **OPEN** |
| ADM/HDA, Einstein dynamics, CR-exclusive experimental predictions, Generative Completeness | **NOT ESTABLISHED** |

### H117 recommended gate: independent **source-generating** rule

Rather than introducing a new artificial `J5`, demand a specific `S_static=F_prim(CR data)` and analyze:

1. **Independent input:** list the precise CR invariants provided to `F_prim` without target `j01`, terminal analyzer feedback, or unmarked physical-control labels.
2. **Naturality:** prove `F_prim(U.c)=U F_prim(c) U*` for a declared gauge action (do not substitute invariant output for equivariant output).
3. **Locality and derivation:** exhibit a rule for primitive graph *before* Lie/dynamic saturation, with a proof that it truly selects native sources.
4. **Fibre test:** exhibit whether inputs indistinguishable under the available CR information can have different sources; if yes, state an exact limited no-go or add an independently justified axiom.
5. **Physical boundary:** no promotion to a P6 physical PASS or P9/P11 completion absent new independent evidence.

## H. Reproducibility and relationship to prior work

Run:

```bash
python P3P11_H116_ax_bimod_independence_audit.py
```

The SymPy code checks **54/54** exact finite-matrix assertions, writes `P3P11_H116_ax_bimod_exact_results.json`, and uses no approximate numerical threshold. The finite checks are *not* a mechanized proof of the all-N torus averaging theorem or the general logical expansion argument; those proofs are in the text. No GitHub PR, CI, Zenodo update, or publication action was performed.

For background on the dependence of quantum system identification on input-output accessibility and assumptions, see Burgarth and Yuasa, *Identifiability of Open Quantum Systems*, Physical Review A **89**, 030302(R) (2014), DOI:10.1103/PhysRevA.89.030302. No claim of literature priority is made for these elementary finite matrix statements.

**Prior local record:** H115 fixed-H37 mathematical audit and P6 Step 1D static-provenance report, both dated 2026-10-19.