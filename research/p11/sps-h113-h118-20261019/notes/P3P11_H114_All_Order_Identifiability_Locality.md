# H114 — All-Order Identifiability and Static Locality Obstruction

**P3–P11 Mathematical Bridge / 2026-10-19**  
**Status:** proved conditional finite-matrix statements; 47 exact SymPy assertions on a 3-level witness. **Not** a reconstruction or verification of H37, the full original P3/P4 hidden filtration, P6 physical source, or F-generative completeness.

## 0. Objects that must not be conflated

* `C_marked^infty`: **all** accessible baseline dynamics, compositions, derivatives, and response words formed from a given **marked** set of operations. “All-order” always means all orders **in those marked operations**, not previously unknown interventions.
* `H_k(Phi,D)`: P3's channel/observable-based dynamical hidden filtration. Its exact program-specific formula is not redefined in this note.
* `S_static`: independently supplied native physical primitive generators (a set of actuated first-order Hamiltonians or more general operators).
* `J_N^D(S_static)`: *-closed diagonal bimodule closure of those primitive operators, as in H113.
* `T_0 M_N^phys`: real physical tangent at an indicated physical control space; this depends on whether `M` means one-pulse control chart or the full switch-generated reachable subgroup.
* `Lie(S_static)`: brackets and commutators allowed by sequential control. In general not the space of first-order native actuation directions.

No equality between any two of the above follows from matching dimensions, matching residues, or a shared finite-horizon support.

## 1. H114.1 — All-marked-orders no-go (finite nonidentity CPTP countermodel)

Let `N=3`, `D_3=span_C{E_11,E_22,E_33}`, `X_12=E_12+E_21`, `X_23=E_23+E_32`, and

\[
U_\theta=e^{-i\theta X_{12}},\quad \theta=\pi/4,\quad \Phi_0=\operatorname{Ad}_{U_\theta}.
\]

Here `Phi_0` is a nonidentity unitary CPTP channel and sends `E_11` to an operator with a nonzero 1–2 coherence. Let two distinct admissible hardware completions have:

\[
\Phi_A(u)=\operatorname{Ad}_{e^{-iuX_{12}}U_\theta},\qquad
\Phi_B(u,v)=\operatorname{Ad}_{e^{-i(uX_{12}+vX_{23})}U_\theta}.
\]

Only `u` is in the marked, independently supplied control alphabet; `v` is an independently accessible physical control in B but not in A. Identically for **every** real `u`,

\[
\Phi_A(u)=\Phi_B(u,0).
\]

Thus every finite word, composition, input-output response, derivative of arbitrary order, and dynamical construction that is solely a function of `Phi_0`, `D_3`, and the marked `u` operations is identical in A and B. In particular, **if** `H_k` is determined by this shared channel and observation algebra, all its levels coincide.

Nevertheless native Hamiltonian primitives and diagonal-bimodule closures are

\[
S_A=\{X_{12}\},\quad J_A^D=\operatorname{span}_\mathbb C\{E_{12},E_{21}\}
\quad(\dim_\mathbb C=2),
\]
\[
S_B=\{X_{12},X_{23}\},\quad J_B^D=\operatorname{span}_\mathbb C\{E_{12},E_{21},E_{23},E_{32}\}
\quad(\dim_\mathbb C=4).
\]

The **one-pulse, first-order actuated** real tangent dimensions are 1 versus 2. The **switch-generated Lie algebra** dimensions are 1 versus 3 (see H114.3). Both are well-defined, but represent different physical control spaces.

**Conclusion (precise No-Go).** No selector depending only on `C_marked^infty` can return the correct native sector for both A and B. This is a fibre-constancy failure in the H113 descent theorem, and survives all response orders on the **marked** alphabet. It does **not** exclude selection from a complete experimentally certified catalogue of all controls, or from stronger independent microscopic information that includes `v`.

## 2. H114.2 — Strict diagonal-gauge obstruction to selecting a phase-fixed primitive

Let `G=T^3` act as `A -> U A U†`, with `U` diagonal unitary. Suppose the input `c` to a putative equivariant selector is **fixed** under all of `G` (e.g., a gauge-invariant structural summary). If a selector outputs a **single Hermitian matrix** `H(c)` and is equivariant, then

\[
H(c)=H(U\cdot c)=U H(c) U^\dagger
\]

for every diagonal `U`. Such matrices are exactly diagonal ones. Therefore an invariant input by itself **cannot equivariantly select a nonzero off-diagonal phase-fixed `X_ij` direction**. E.g., `U=diag(i,1,1)` rotates `X_12` to `-Y_12`, with `Y_12=-i(E_12-E_21)`.

This does **not** prohibit a gauge-invariant complex support sector `span_C{E_12,E_21}`: it is preserved as a **subspace**. A phase-resolved native `X/Y` control requires a gauge-frame reference or equivalent physical calibration. This is a symmetry obstruction only for a **chosen representative**, not a universal no-go for an invariant sector.

## 3. H114.3 — Lie reachability can falsely enlarge static locality

The native B controls have generators `A=iX_12`, `B=iX_23`; their bracket is

\[
[A,B]=E_{31}-E_{13}=:C,
\quad [A,C]=-B,\quad [B,C]=A.
\]

Hence their real Lie algebra is 3-dimensional even though the independently actuated one-pulse control chart has only two directions. The commutator `C` carries the nonnative edge 1–3. Taking diagonal-bimodule closure after Lie completion produces

\[
J^D_{\rm native}=\operatorname{span}_\mathbb C
\{E_{12},E_{21},E_{23},E_{32}\}\quad(\dim=4),
\]
\[
J^D_{\rm Lie}=\operatorname{span}_\mathbb C
\{E_{12},E_{21},E_{23},E_{32},E_{13},E_{31}\}\quad(\dim=6).
\]

**Implication:** even full *reachable* coherent Lie algebra need not encode the **native** primitive graph. Additional labels specifying **first-order independently actuated** controls (versus synthesized higher-order directions) are required. This is an exact algebraic analogue of the conceptual caution against reading `H_k` as `J_N`; it is **not** an identity claiming P3's `H_k` equals a Lie closure.

## 4. H114.4 — Exact product-closure saturation theorem and finite-time support loss

For a finite undirected simple graph `G` on `{1,...,N}`, put

\[
J_E=\operatorname{span}_\mathbb C\{E_{ij}:\{i,j\}\in E(G)\},\qquad
V_k(G)=D_N+\sum_{\ell=1}^k J_E^\ell.
\]

Here `J_E^ell` denotes the **linear span of products of exactly ell elements**, and `V_0=D_N`.

**Theorem.**
\[
V_k(G)=\operatorname{span}_\mathbb C\{E_{ij}:d_G(i,j)\le k\}.
\]

**Proof.** Each nonzero product of `ell` edge matrix units is a matrix unit whose endpoints are joined by an edge walk of length `ell`; hence it has graph distance at most `ell`. Conversely, for a shortest path `i=v_0 -> v_1 -> ... -> v_ell=j`, the exact matrix unit product `E_{v_0v_1}...E_{v_{ell-1}v_ell}=E_{ij}` belongs to `J_E^ell`. Diagonal units are already in `D_N`. QED.

If `G` is connected then `V_k=M_N(C)` for all `k>=diam(G)` **irrespective of the graph's missing primitive edges**. Explicitly, for the path 1–2–3 and complete triangle K3, respectively:

```
               grade 0   grade 1   grade 2   saturated
path 1-2-3         3         7         9          9
triangle K3        3         9         9          9
```

So only the eventual algebra loses native locality. **The *full graded family* in this particular construction does distinguish the graphs at grade 1.** We do not infer that original P3 `H_k` has precisely this graded graph form.

**Classical semigroup analogue.** On a finite connected graph with strictly positive edge rates, let `Q` be its irreducible continuous-time Markov generator. For `nu>=max_i(-Q_ii)`, `P=I+Q/nu` is entrywise nonnegative and

\[
e^{tQ}=e^{-\nu t}\sum_{m\ge0}\frac{(\nu t)^m}{m!}P^m.
\]

For each `i,j`, graph connectedness supplies some `m` for which `(P^m)_ij>0`, so `(e^{tQ})_ij>0` for every `t>0`. Therefore **finite positive-time support alone** is complete for every connected graph and does not recover its native edges. In contrast, **full calibrated infinitesimal data** recover `Q=\lim_{t\downarrow0}(e^{tQ}-I)/t` and thereby its rate-supported edges under the CTMC assumptions. Distinguish support-only from full semigroup values.

## 5. H114.5 — Conditional positive theorem: what complete microscopic control tomography recovers

Assume a base unitary channel `Phi_0` is known and invertible as a superoperator, an exhaustive (independently validated) first-order *native* Hamiltonian control family `{H_alpha}` is available with a fixed control-coordinate chart, and the complete first derivatives of the channels

\[
\Phi_\alpha(u)=\operatorname{Ad}_{e^{-iuH_\alpha}}\circ\Phi_0
\]

are exactly tomographed at `u=0`. Then

\[
\bigl(\partial_u\Phi_\alpha|_0\bigr)\circ\Phi_0^{-1}
=-i[H_\alpha,\,\cdot\,].
\]

If two Hermitian matrices yield the same commutator superoperator on all `M_N`, their difference commutes with all matrix units and is therefore a real scalar multiple of `I`. Thus each `H_alpha` is uniquely reconstructed **modulo scalar identity**. The audit checks rank `N^2-1=8` for N=3.

Consequently the **off-diagonal** native support is determined, and so is the *diagonal-adjoined* support bimodule

\[
\widetilde J_{\rm native}
:=D_N+J_N^D(\{H_\alpha\})
=D_N+\operatorname{span}_\mathbb C\{E_{ij}:i\ne j,\ (H_\alpha)_{ij}\ne 0\ \text{for some }\alpha\}.
\]

The definition is invariant under additive scalar Hamiltonian gauge `H_alpha -> H_alpha+c_alpha I`, and basis-independent when the full native real control subspace has been calibrated. It is diagonal-gauge covariant as a **subspace**; choosing individual real `X/Y` phases still needs a reference.

**Caveats that cannot be omitted:**

1. The exhaustive native first-order control **catalogue is supplied externally**; tomography does not certify that an unknown extra control does not exist.
2. Full process tomography is stronger than population-only or H37's reported reduced residue data.
3. Recovery of the augmented bimodule is not recovery of fundamental interaction terms, control costs, decomposition into elementary hardware pulses, or diagonal primitive provenance.
4. If instead the **Lie-reachable** tangent is supplied, bracket-generated nonnative edges are included, so the reconstruction no longer targets native locality.
5. For dissipative general GKSL tangents the unitary commutator reconstruction formula is not by itself sufficient.

This theorem is deliberately **conditional**, not a derivation from P3, P4, F, or a closed observer response.

## 6. H37 / P6 / P9 / P11 interpretation

The user-supplied Step 1D premises state `dim_R Xi(J5_mix)=5` and `dim_R Xi(J5_full)=8` for candidates consistent with the same native exchange controls and up-to-four-dimensional second-order diagonal residue. H113 already yields a reduced-fingerprint non-identifiability result. H114 adds **a distinct exact mechanism**: all orders of the *specified marked-control alphabet* can fail to recover an unmarked physical primitive, and even the **Lie-generated reachable set** need not coincide with native first-order locality. **No H37 matrices have been evaluated in this audit; the H37 figures remain premises.**

* **P3**: Keep `H_k(Phi,D)` channel-dependent; do not identify it with static `J_N` or physical control tangent.
* **P4**: Higher-order visibility, product closure, and saturated algebra are three distinct mathematical constructs. Saturation loses graph origin in the proxy example, not necessarily in P4's exact filtration.
* **P6**: Physical provenance, independently certified native-controls catalogue, `X/Y` phase frame, and hardware validation stay OPEN.
* **P9**: An algebraically generated coupling or Cartan object requires a separate *native-origin certificate*. Nothing here supplies Einstein dynamics, ADM/HDA or true GR sourcing.
* **P11**: `AX-SRC`, `AX-ACCESS`, `AX-GAUGE`, and `AX-LOC` remain distinct proof obligations. Theorems provide constraints on any proposed axiomatization, not generative completeness.

## 7. Next gate H115: native accessibility filtration, not more arbitrary candidate J5 sectors

The next test should use the **actual frozen H37/P6 control definitions** and form an independently justified native first-order real subspace `K_nat`, then separate `K_nat`, `Lie(K_nat)`, `J_N^D(K_nat)`, and `H_k(Phi,D)`. Establish what is supplied versus generated. Compute the corresponding observation data map and test whether its fibre contains both H37 candidates. If the independent native-control data are unavailable, report a provenance **OPEN** rather than constructing additional sectors or declaring a full-information No-Go.

## 8. Reproducibility, limitations, and relevant background

Run `python P3P11_H114_all_order_locality_audit.py`. Requires SymPy. At creation the script passed **47/47 exact symbolic assertions** on the specified 3-level witnesses. It also uses an algebraic uniformization positivity argument for all `t>0`; finite checks themselves are not claimed as an exhaustive proof of the all-time result.

These are tailored mathematical observations, **not** claims of literature priority or of independent specialist peer review. Related quantum system-identification literature analyzes exactly the roles of inputs, observability, gauge, and identifiability:

- Burgarth and Yuasa, *Quantum System Identification*, Physical Review Letters **108**, 080502 (2012). DOI 10.1103/PhysRevLett.108.080502.
- Burgarth and Yuasa, *Identifiability of Open Quantum Systems*, Physical Review A **89**, 030302(R) (2014). DOI 10.1103/PhysRevA.89.030302.
- *Uniformization: Basics, extensions and applications*, 2017, https://www.sciencedirect.com/science/article/pii/S0166531617301451 (standard CTMC uniformization identity).

No GitHub PR, CI check, experiment, human peer review, or H37 reproduction has been performed by this H114 artifact.