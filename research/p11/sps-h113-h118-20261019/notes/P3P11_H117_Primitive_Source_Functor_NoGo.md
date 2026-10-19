# H117 — Primitive Source Functor and Generative Selection No-Go

**Date:** 2026-10-19 (Asia/Tokyo)  
**Workstream:** P3–P11 Mathematical Bridge / P11 Axiomatization  
**Outcome:** exact relative descent no-go, equivariant orbit-map classification, and source-versus-sector nonfaithfulness on the fixed H37 five-site finite model. An exact SymPy audit passed **50/50** assertions. **No** physical P6 source, universal source functor from F, complete P3/P4 logical independence, Einstein dynamics, or P11 Generative Completeness is established.

## A. Input data: strict separation

Let `C_CR` denote the *bare* dynamical and observational CR input: `(Phi,D)` or a specified generator `(L,D)` and every P3/P4 construction depending only on it. Let `C_marked` additionally include **externally marked** controls or a separately supplied Hamiltonian representative. The map `forget: C_marked -> C_CR` is not presumed invertible. Neither input is secretly allowed to contain a separately certified P6 `J`, an unknown physical control, or the target readout `j01` used as a source-selection datum.

The five-site fixed H37 model has `D_5 = span_C{p_0,...,p_4}`, with `E_ij` denoting matrix units, and

\[
X_e=E_{e,e+1}+E_{e+1,e},\quad K_e=E_{e,e+1}-E_{e+1,e},\quad H_{\rm hop}=\tfrac12\sum_{e=0}^3X_e.
\]
\[
H=\operatorname{diag}(0,1/7,-1/9,2/11,-3/13)+H_{\rm hop},\quad
\mathcal L(A)=-i[H,A]+\tfrac23(\Delta_D(A)-A).
\]

The four **declared**, not hardware-certified, native directions are `K_nat = span_R{K_0,...,K_3}`. The *extra* P6 static-sector label `J` is not part of the H37 channel definition. We will not infer that all Hamiltonian terms are separately actuated controls.

Distinct objects:

* `H_k(Phi,D)` is a dynamical hidden filtration determined by the stated channel and observer algebra.
* `S_static` is an *independently sourced* primitive collection; here this can be a hypothetical label in an enlarged model category, not necessarily certified hardware.
* `J_N` is the (conditional) static sector, perhaps reconstructed as a chosen closure of `S_static`.
* `T_0 M_N^{phys}` is a separately justified physical-control tangent; it does not follow from dimension matching.
* `K_nat` is the named one-pulse control space; `Lie(K_nat)` and its diagonal-bimodule closure need not equal `K_nat` or `T_0 M_N^{phys}`.

## B. Theorem H117.1 — equivariant descent necessary and sufficient condition

Let `P,C,S` be `G`-sets, and let `pi:P -> C` and `s:P -> S` be `G`-equivariant maps. Interpret `pi` as forgetting microscopic source data and `s` as selecting the actual source or actual sector (up to a declared physical equivalence relation). On the image of `pi`, a `G`-equivariant `f: im(pi) -> S` obeying `s=f∘pi` **exists if and only if**

\[
\pi(p)=\pi(q)\implies s(p)=s(q)\qquad (p,q\in P).
\]

**Proof.** If `s=f∘pi`, equality of the arguments forces equality of the values. Conversely define `f(c)=s(p)` for any preimage `p` with `pi(p)=c`; the condition makes this independent of the choice. For `g∈G`, `f(gc)=s(gp)=g s(p)=g f(c)`; hence `f` is equivariant. QED.

The result also works with `S` replaced by a set of gauge-equivalence classes, but equality then means exactly the equivalence relation declared in advance. It does **not** say that a selector can recover more microscopic distinctions than encoded in that quotient. A rule defined only on `im(pi)` need not automatically extend to all hypothetical `C` without extra choices.

In the action groupoid of the gauge action, this equivariant `f` induces a functor preserving gauge arrows. This is *not* automatically a functor for every conceivable CR morphism (such as embeddings or coarse-graining); those require separately defined compatibility axioms.

## C. Theorem H117.2 — restricted H37 no-go for universally correct static-sector reconstruction

The previously established weak bridge class admits two candidate expansions over **the same marked** H37 base `c=(D_5,L,Hhop,K_0,...,K_3)`:

\[
J_{\rm mix}=\operatorname{span}_\mathbb C\{H_{\rm hop},K_0,K_1,K_2,K_3\},\quad
J_{\rm full}=\operatorname{span}_\mathbb C\{E_{e,e+1},E_{e+1,e}:0\le e\le3\}.
\]

Both are complex linear, star-stable, off-diagonal, radius-one, contain the named controls and hopping Hamiltonian, and have four-dimensional internal quadratic diagonal residue. Nonetheless

\[
\dim_\mathbb C J_{\rm mix}=5,\quad\dim_\mathbb C J_{\rm full}=8,\quad
\dim_\mathbb R\Xi(J_{\rm mix})=5,\quad\dim_\mathbb R\Xi(J_{\rm full})=8.
\]

Construct the **mathematical expansion class** `P_weak` containing `(c,J_mix)` and `(c,J_full)`, with `pi(c,J)=c` and `s(c,J)=J`. Then `pi` is equal on these two elements but `s` differs, even after any dimension-preserving gauge quotient. H117.1 rules out any selector that is correct for *every expansion* in this class.

All P3/P4 features computed solely from `(L,D_5)` remain equal for the two expansions, as do all response words in the same marked-control alphabet. This is because the underlying generator, algebra, and marked protocols are identical by construction; it is **not** an independent calculation of the entire original P3/P4 filtration. If future P11 axioms add microscopic source information, this counterclass may be excluded, and this conditional no-go may cease to apply.

**Important quantifier:** this theorem does **not** assert that two certified physical H37 devices have been found. It is a relative mathematical non-identifiability theorem over the weak bridge interface, not a hardware impossibility theorem.

## D. Theorem H117.3 — equivariant maps on a gauge orbit exist in profusion

Let `G` act on inputs `C` and candidate outputs `S`. For a chosen input `c`, write `G_c={g:gc=c}` for its stabilizer. There is a bijection

\[
\left\{G\text{-equivariant }f:G\cdot c\to S\right\}
\cong S^{G_c},\qquad f\mapsto f(c),
\]

where `S^{G_c}` is the subset of outputs fixed by every element of `G_c`.

**Proof.** Equivariance implies `f(c)` is fixed by `G_c`. Conversely if `y` is fixed by `G_c`, set `f(gc)=gy`. If `g c=h c` then `h^{-1}g∈G_c`, so `gy=hy`; thus the definition is well-defined and equivariant. QED.

For H37 the diagonal gauge group is `G=T^5`. The nonzero edges `H_{e,e+1}=1/2` of the **fixed, phase-marked** Hamiltonian force `z_e \bar z_{e+1}=1` along all four path edges, so any stabilizer element is `z I_5`. Global scalar conjugation fixes **every** matrix subspace. Thus for *this gauge orbit*, **every** candidate subspace at the basepoint gives rise to a gauge-equivariant orbit selector.

In particular, the two **mathematically definable marked-data assignments**

\[
F_{\rm mix}(c)=\operatorname{span}_\mathbb C\{H_{\rm hop},K_0,K_1,K_2,K_3\},\qquad
F_{\rm full}(c)=J_5^D(\{K_e\})
\]

extend gauge-equivariantly by `F(Uc)=U F(c) U*`. They differ (rank 5 versus rank 8). The first is **not** a diagonal bimodule; the second is. Therefore **existence, equivariance, and actual-H37 stabilizer compatibility do not determine a physically correct selector**. These are assignments from **marked** H37 data, *not* constructions of `F_prim` from bare CR data or from the generative map `F`.

Do not overinterpret: covariance on the diagonal-gauge groupoid alone is weaker than being natural with respect to all potential physical and CR morphisms. No universal categorical uniqueness is proved here.

## E. Theorem H117.4 — support-only data cannot select a phase-fixed off-diagonal source

Let the input consist only of `(D_5, path support)` with **no marked hopping amplitudes, X/Y phase frame, or native control list**. Every diagonal torus element fixes this support-only input. If an equivariant selector were to output one nonzero phase-fixed off-diagonal matrix `A`, then for every diagonal unitary `U` it would obey `UAU*=A`. Entrywise `U E_ij U*=z_i\bar z_j E_ij`; varying `z_i` forces every `A_ij=0` for `i≠j`, contradiction.

Thus a **nonzero off-diagonal phase-fixed representative** cannot be naturally selected from this input alone.

This says *nothing* against selecting **edge lines**, support sets, or their span: for instance each ray `C E_ij` is fixed as a subspace by diagonal phase changes, and `J_full` is fixed. In fact for complex off-diagonal `J`, fixed-torus invariance is equivalent to the diagonal-bimodule property (H116). A unique **sector** can therefore be obtained by imposing such a categorical axiom, even while a physically calibrated source operator cannot.

## F. Theorem H117.5 — closure irreversibly forgets source provenance

Define `cl_D(S)` to be the complex, star-stable diagonal-bimodule closure of `S`. Then in H37

\[
\operatorname{cl}_D(\{H_{\rm hop}\})
=\operatorname{cl}_D(\{K_0,K_1,K_2,K_3\})
=J_{\rm full}.
\]

Yet `span_C{Hhop}` has dimension 1, whereas `span_C{K_0,...,K_3}` has dimension 4. Both sets are already present as *formal matrices* in the fixed H37 description, but neither source list is hereby certified to be the physical list of independent native primitives.

Consequently `cl_D` is noninjective: choosing the closure does not reconstruct the primitive source, number of native control knobs, native/synthesized distinction, or microscopic provenance. In terms of mathematical information, `cl_D` identifies an equivalence class of generating lists; a unique representative requires a **new** selection criterion.

A specific phase-contrast direction

\[
W=i(X_0-X_1)
\]

lies in `Xi(J_full)` but not in `Xi(J_mix)`. Its presence in an **independently specified and calibrated native tangent catalogue**, together with the appropriate P6 Accessibility and source assumptions, could distinguish the two candidates. Merely exhibiting `W` algebraically or observing it through a synthesized sequence/terminal analyzer does **not** show that it is a native primitive. Nor may measurements of the target `j01` be used retroactively to manufacture source independence.

## G. What an honest P11 `F_prim` construction now needs

1. **Domain definition:** Specify whether `F_prim` takes *bare* P3/P4 `(Phi,D)` data, marked microscopic controls, or a stronger independently given generating object. State which are axioms and which are derived.
2. **Source equivalence:** Specify whether the output is a literal ordered primitive list, a real first-order tangent subspace, a complex operator subspace, a gauge orbit, or a diagonal-bimodule closure. These are not equivalent targets.
3. **Fibre constancy:** Prove H117.1 on the admitted physical model category, or exhibit an exact pair on the same input fibre with inequivalent sources; that is the decisive selection/no-go test.
4. **Naturality:** Specify morphisms of CR inputs beyond diagonal-gauge arrows if claiming a *universal functor*. Test equivariance, embeddings, locality maps, composition, and the appropriate observer reduction rather than assuming they coincide.
5. **Locality and timing:** Prove that the source is defined *before* Lie-reachable/dynamically propagated closure and that it has an independently justified locality radius.
6. **Non-circular physics:** Produce an independent primitive-origin certificate not inferred from `j01`, not extracted post hoc from a convenient closure, and not assuming the target P6 Accessibility result it is supposed to support.

The formal descent theorem already supplies a necessary-and-sufficient **logical test**, but it does not supply the physical category or guarantee fibre constancy.

### Explicit stop rule

No further arbitrary `J5` sector is introduced. If only current H37/P3/P4 input is available, the weak-interface `F_prim` physical selection task is **BLOCKED BY IDENTIFIABILITY**. Future productive work requires either (i) a genuinely new independently motivated P11 source axiom or (ii) independently calibrated physical native-source evidence. A proposed source law can be investigated as mathematics, but must not be presented as uniquely compelled by existing P3/P4 data.

## H. Result table and exact audit

| Claim | Status |
|---|---|
| `G`-equivariant factorization iff source labels are constant on data fibres | **THEOREM (all G-sets)** |
| H37 weak bridge inputs distinguish `J_mix` from `J_full` | **NO (relative NO-GO)** |
| Equivariant maps on a single orbit classified by stabilizer-fixed outputs | **THEOREM (all G-sets)** |
| Gauge covariance on marked H37 orbit uniquely selects `J` | **NO (two equivariant assignments)** |
| Support-only data select a nonzero phase-fixed off-diagonal matrix | **NO (torus stabilizer obstruction)** |
| `cl_D` determines physical primitive generator list | **NO (rank 1 vs rank 4 source witness)** |
| Bare finite CR determines the physically correct `F_prim` | **OPEN / unsupported by current interface** |
| P6 physical source and experimental gate; F Generative Completeness; GR / ADM / HDA | **OPEN** |

Reproduction: `python P3P11_H117_primitive_functor_audit.py`. It performs **50 exact SymPy assertions** on the fixed H37 matrices, source and sector ranks, a phase-contrast discriminator, gauge covariance checks, and the hopping-graph stabilizer. The general theorems in §§B, D, E are analytic proofs and are **not** mechanized in Lean. Checks on mathematical labels are **not** hardware evidence. No GitHub, Notion, Zenodo, human specialist review, or external AI audit was performed.

**Next gate H118:** Axiomatic source category and locality-preserving descent. Formulate the *smallest non-circular extra axiom* under which fibres become constant, and prove whether that axiom is independent of target response. Do not declare source success merely by setting `S_static=cl_D(K_nat)`; that is a sector closure, not physical provenance.