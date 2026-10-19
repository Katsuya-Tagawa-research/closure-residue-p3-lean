# H118 — Axiomatic Source Category and Locality-Preserving Descent

**Date:** 2026-10-19 (Asia/Tokyo)  
**Program:** P3–P11 Mathematical Bridge / P11 axiomatization  
**Status:** exact conditional set-theoretic and finite-matrix statements; **70/70 exact SymPy assertions** for the H37 fixed algebra. No physical P6 source certificate; no unconditional F-generative primitive law; no claim of P11 Generative Completeness.

## 0. Aim and preconditions

Use the original H37 five-site GKSL generator, diagonal observation algebra, hopping matrix, and four named skew-exchange native tangents. Do not conflate P3 dynamical hidden sectors, an independently supplied source family, a static bimodule, or physical independently actuated tangents. In particular a labelled mathematical native control is *not* evidence of a physically verified native actuator.

With site indices 0,...,4, let `E_ij` be matrix units and `p_i=E_ii`. Put

\[
D_5=\operatorname{span}_{\mathbb C}\{p_0,\ldots,p_4\},\quad X_e=E_{e,e+1}+E_{e+1,e},\quad K_e=E_{e,e+1}-E_{e+1,e},
\]
\[
H_{\rm hop}=\tfrac12\sum_{e=0}^3 X_e,\quad H=H_{\rm hop}+\operatorname{diag}(0,1/7,-1/9,2/11,-3/13),
\quad \mathcal L(A)=-i[H,A]+\frac23(\Delta_D A-A).
\]

Existing weak H37 expansions (Step 1D/H113–H117):

\[
J_{\rm mix}=\operatorname{span}_{\mathbb C}\{H_{\rm hop},K_0,K_1,K_2,K_3\},\quad
J_{\rm full}=\operatorname{span}_{\mathbb C}\{E_{e,e+1},E_{e+1,e}:0\le e\le3\}.
\]

These are *candidate static labels*, not measured physical source sectors. They share the same H37 channel and marked alphabet. Ranks: `dim_C Jmix = 5`, `dim_C Jfull = 8` and `dim_R Xi(Jmix) = 5`, `dim_R Xi(Jfull) = 8`.

## H118.1 — Necessary and sufficient information-refinement theorem (EXACT)

Let `P` be a set of microscopic models, `C` their available CR input data, `S` the desired source labels (or gauge-equivalence classes after declaring that equivalence), and `A` additional independently *proposed* data. Given maps

\[
\pi:P\to C,\quad s:P\to S,\quad a:P\to A,
\]

there is a unique map

\[
f:\operatorname{im}(\pi,a)\to S,\qquad s=f\circ(\pi,a)
\]

if and only if

\[
(\pi(p),a(p))=(\pi(q),a(q)) \Longrightarrow s(p)=s(q)
\quad \text{for every }p,q\in P. \tag{118.1}
\]

*Proof.* Necessity follows by applying `f` to equal input pairs. For sufficiency define `f(c,alpha)=s(p)` for any preimage `p` of `(c,alpha)`; (118.1) guarantees independence of the choice. Uniqueness holds on the image. **No extension of `f` to every unattained point of `C × A` is claimed.** If `G` acts on all four sets and the three original maps are `G`-equivariant, then `f` is also equivariant, by the same representative argument. QED.

### Universal coarsest *logical* completion (EXACT, not physical)

Define the source-labelled data image

\[
E_s:=\operatorname{im}(\pi,s)\subseteq C\times S,
\]

with `e_s:P->E_s`, `p->(pi(p),s(p))`. For *any* adequate auxiliary marker `a` satisfying (118.1), the image `E_a=im(pi,a)` has a unique **surjective** map

\[
q_a:E_a\to E_s,\qquad (\pi(p),a(p))\mapsto(\pi(p),s(p)), \tag{118.2}
\]

compatible with the projections to `C` and the original models. This defines a coarsest sufficient *abstract partition* of the model set (in the information-refinement order). **It is not a noncircular recipe for measuring `s`: `E_s` explicitly contains the unknown source label.** Any proposal calling this construction a physical solution would be circular.

### Information lower bound (EXACT)

For fixed `c ∈ C` define `P_c={p:pi(p)=c}` and the set `s(P_c)` of genuinely distinguishable source labels. Any adequate auxiliary marker must take at least `|s(P_c)|` distinct values on `P_c`; otherwise two distinct source labels share the same `(pi,a)` datum, contradicting (118.1). If these finite cardinalities equal `m`, a binary code requires at least `ceil(log2 m)` bits on that fibre. A two-candidate *restricted* H37 question needs at least one independent binary distinction. This does not say that the complete weak admissible sector space has only two candidates; nor does it identify a real physical measurement providing the bit.

## H118.2 — No source-selecting progress from a CR-derived extra marker (EXACT)

If `a=h∘pi` for any function `h:C->A`, then `ker(pi,a)=ker(pi)`. Consequently when `s` is not constant on a `pi`-fibre, adding `a` cannot produce an adequate selector. This applies to arbitrarily elaborate deterministic analyses of the **same** fixed `(Phi,D)` and the same marked operation alphabet, including every derived P3/P4 statistic, unless the analysis truly uses additional independent inputs or changes the admissible model class.

The H37 weak two-label witness gives `pi(c,Jmix)=pi(c,Jfull)=c` but `s(c,Jmix) ≠ s(c,Jfull)` even modulo any dimension-preserving diagonal gauge. The theorem is an *information/descent obstacle*, not a proof that the real device is one of two experimentally observed hardware completions.

## H118.3 — Conditional selection by AX-BIMOD (EXACT; axiom not derived)

Define, for a family `S` of matrices,

\[
B_D(S)=\operatorname{span}_{\mathbb C}\{p_i A p_j,\ p_i A^\dagger p_j:
A\in S,\ 0\le i,j<N\}. \tag{118.3}
\]

This is the **smallest** complex-linear, `*`-stable, `D_N`-bimodule containing `S` (as a linear subspace). Minimality is by construction. In particular

\[
B_{D_5}(\{H_{\rm hop}\})
=B_{D_5}(\{K_0,K_1,K_2,K_3\})
=B_{D_5}(J_{\rm mix})=J_{\rm full}. \tag{118.4}
\]

For H37, assume a *separately imposed* static sector `J` is (i) entirely off-diagonal, (ii) radius-one on the five-site path, (iii) complex-linear and a `D_5`-bimodule, and (iv) contains `H_hop`. Then `p_e H_hop p_{e+1}=E_{e,e+1}/2` and its adjoint belong to `J`, so `Jfull ⊆ J`. Conditions (i) and (ii) give `J ⊆ Jfull`. Hence `J=Jfull`. There is a genuine conditional **sector** selection theorem.

**Axiom-origin boundary:** It is *not* established that F, original P3/P4 axioms, or the physical device necessitate the diagonal-bimodule rule. Under weaker H37 assumptions `Jmix` is a counterexample to derivability. Nor is the input source uniquely recovered: `span_C{Hhop}` has dimension one and `span_C{K0,...,K3}` dimension four, while their closures coincide. AX-BIMOD is a rule for constructing a sector from a source, not an independent source-origin law.

## H118.4 — Gauge, locality, restriction: sector functor theorem (EXACT)

Consider the category whose objects are `(V,G,D_V,S)` with finite labelled sites `V`, fixed support graph `G`, full diagonal algebra `D_V`, and a formal source family `S`. Restrict morphisms to (a) diagonal unitary conjugations, (b) site relabellings preserving the declared graph, and (c) coordinate restrictions to subsets `U⊆V` equipped with compressed `S|_U={P_U A P_U:A∈S}`. (For a strict ordinary category with all arrows composable one may take generated paths of these elementary operations modulo their evident relations; the identities below give coherence.) This is **not** a functor under arbitrary nonlinear physical coarse-graining or arbitrary CPTP channels.

(a) For diagonal unitary `U`, since `U p_i U†=p_i`, one has

\[
B_D(U S U^\dagger)=U B_D(S) U^\dagger. \tag{118.5}
\]

The analogous property holds for graph-preserving relabellings by permutation matrices (where diagonal projectors relabel). These maps respect composition and identity.

(b) Define locality relative to graph metric `d_G`: `S` is radius-`r` if every nonzero coefficient of its matrices joins vertices at graph distance at most `r`. Because `p_i A p_j=A_{ij}E_{ij}`, no new matrix-unit support is introduced by (118.3). Thus `B_D(S)` preserves the **entrywise** radius bound. It does *not* assert that a native source on an edge is a separately actuated hardware knob.

(c) For each site subset `U`, the coordinate-corner identity is

\[
P_U B_{D_V}(S)P_U
=B_{D_U}(\{P_U A P_U:A\in S\}).\tag{118.6}
\]

Here equality is understood after the natural zero-padding embedding of matrices on `U` into matrices on `V`. Proof: both sides are spanned by the same retained matrix units `A_ij E_ij` (and adjoints) for `i,j∈U`. These equalities commute with nested restrictions `W⊆U⊆V` and diagonal-gauge maps. This is a **locality-preserving sector functor conditional on supplied source data**.

This functor is nonfaithful as a source-recovery procedure: distinct labelled source families may produce identical global and local sectors. It is not a functor `bare CR -> physical primitive source`.

## H118.5 — Exact sector patch-gluing criterion (EXACT)

Let patches `U_alpha⊆V` cover every ordered off-diagonal pair `(i,j)` for which some matrix in `S` has nonzero `(i,j)` entry: at least one patch includes both endpoints. Then

\[
B_{D_V}(S)=\sum_\alpha \operatorname{ext}_{U_\alpha,V}\bigl(B_{D_{U_\alpha}}(S|_{U_\alpha})\bigr). \tag{118.7}
\]

Proof: every matrix unit appearing in `B_D(S)` appears in a compressed patch, while every patch corner lies in `B_D(S)`. The condition is essential: a vertex-only patch cover fails to capture offdiagonal edges.

For H37, the four patches `{0,1}`, `{1,2}`, `{2,3}`, `{3,4}` reconstruct the eight-dimensional `Jfull` sector exactly. A cover by five individual vertices returns no hopping sector. Even the successful edge patch cover does **not** recover the global one-knob `Hhop` source versus four formally marked separate `K_e` sources; that distinction was erased by `B_D`.

## H118.6 — Phase-contrast information bound on a declared coherent manifold (EXACT linear algebra; physical status OPEN)

`Xi(Jmix)` is a five-dimensional real subspace of `Xi(Jfull)`, dimension eight. Set

\[
W_0=i(X_0-X_1),\quad W_1=i(X_1-X_2),\quad W_2=i(X_2-X_3).
\]

The three classes of `W_e` form a basis of `Xi(Jfull)/Xi(Jmix)`; the ranks after adjoining 0,1,2,3 are exactly `5,6,7,8`. Consequently **three independent phase-contrast classes** are necessary and sufficient to span the full eight-dimensional coherent tangent **starting from the declared five-dimensional mixed span**. One such contrast distinguishes *the two named* sectors (if independently certified as a native tangent), but one contrast is not enough to force the full coherent space among all admissible intermediate subspaces.

This is only a vector-space test. A synthesized Lie direction, terminal analyzer pulse, mathematically available Hamiltonian, or the target `j01` response must **not** be silently promoted to an independent native tangent. Accessibility assumptions also cannot be used in a circular fashion to prove source provenance.

## H118.7 — Noncircular axiom interface for P11 (proposal, not completed derivation)

The weakest *logical* requirement is fibre separation (118.1). Calling it AX-SOURCE-SEP is useful, but by itself it only renames the desired conclusion. A substantive physically meaningful proposal must additionally provide:

1. **AX-SRC / AX-NATIVE:** an independent way of declaring the source object and its native (one-pulse, first-order) operational status, with exhaustive-scope evidence, or an independently derived generative restriction on admissible models. Neither may be inferred from `j01`.
2. **AX-GAUGE:** a declared equivalence group and its action on sources, site basis and phase frame; distinguish gauge-fixed native matrices from invariant supports.
3. **AX-LOC:** an independently justified site graph, radius and restriction maps, before Lie or dynamical propagation.
4. **AX-BIMOD (optional):** an independently defended diagonal-bimodule closure rule if the selected output is a sector. It alone cannot certify an actual primitive origin.
5. **AX-MATCH:** an independently established map from the abstract source family to actual device preparations, controls and calibrated channels. This is a separate physical gate, not a consequence of these mathematical theorems.
6. **AX-NAT:** naturality under explicitly chosen morphisms beyond gauge/restriction if a universal functor is claimed; prove those morphisms preserve the source category.

A sufficient **conditional** mathematical construction takes an externally supplied, exhaustive native first-order operator list `S_nat` and sets `J=B_D(S_nat)`; on the restricted source category this is local, gauge-covariant, and restriction-compatible. This proves an existence statement for the **sector functor on source-labelled inputs**. It is not an F-derived universal source functor on bare CR objects.

## H118.8 — Final decision

| Claim | Status |
|---|---|
| Joint-data fibre constancy iff exact source reconstruction on attained inputs | EXACT, general theorem |
| Coarsest sufficient abstract completion `im(pi,s)` and its universal property | EXACT, but tautological as physical source prescription |
| Auxiliary marker derived solely from CR removes H37 weak-fibre ambiguity | NO-GO |
| AX-BIMOD + offdiag/radius-one/Hhop selects `Jfull` | EXACT conditional sector theorem |
| `B_D` preserves graph-radius, diagonal gauge covariance, and corner restriction | EXACT |
| Edge-patch cover reconstructs static support sector | EXACT with pair-cover hypothesis |
| Edge patch support or `Jfull` determines original primitive actuator list | NO-GO |
| Three independent relative-phase tangents fill the mixed/full gap | EXACT algebra; native certification OPEN |
| Independence and physical origin of the extra marker | OPEN |
| Derivation of AX-BIMOD, a source functor, or source separation directly from F | OPEN |
| P6 physical gate, P9 Einstein dynamics, P11 Generative Completeness | OPEN |

## Reproduction and limitations

Run `python P3P11_H118_source_locality_audit.py`; it uses exact SymPy rational/complex arithmetic and checks 70 finite statements including rank, offdiagonal support, four edge corners, gauge conjugation, mixed/full closure, three contrasts and a toy two-element information fibre. The **general abstract theorems** are proved in this note, not verified formally in Lean; the 70 finite checks are not a substitute for those proofs. No external experimental result, hardware validation, full original P3/P4 formal-axiom independence, scientific referee review, Github CI, Notion edit, Zenodo upload or independent AI audit has occurred.

**H119 decision gate:** Seek an intrinsically defined primitive-source *constraint* from the algebra of finite CR generation that removes weak expansions **without restating** source constancy, and test nontrivial tensor composition, observer reduction and locality. If no noncircular physical or mathematical input appears, record a structural source-selection STOP rather than manufacturing further admissible `J5` alternatives.