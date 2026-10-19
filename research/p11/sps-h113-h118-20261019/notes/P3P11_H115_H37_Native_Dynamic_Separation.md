# H115 — H37 Native–Dynamic Separation and Primitive Selection Obstruction

**Date:** 2026-10-19 (Asia/Tokyo)  
**Program:** P3–P11 Mathematical Bridge / Twelve-Paper Generative Program  
**Status:** finite exact results from a fixed H37 GKSL matrix generator; selected conditional structural theorems. No physical provenance certificate, experiment, human peer review, CI, or proof of P11 generative completeness.

## Executive decision

H37/P6 Step 1D had two static *-closed off-diagonal radius-one candidates compatible with the same declared four native real exchange controls and the same four-dimensional diagonal quadratic-residue space. This H115 study uses the **actual fixed five-site H37 generator**, rather than another unrelated illustrative example, and explicitly separates (i) native first-order controls, (ii) their Lie brackets, (iii) their complex diagonal-bimodule closure, (iv) P6 static sector candidates and (v) P3 dynamical hidden filtration.

**Key results:**

1. An exact generator-Krylov calculation from the **full diagonal algebra** reaches all `M_5(C)` at order 6; the projected hidden space reaches complex dimension 20. This is dynamical generation, **not** 20 independently usable native controls.
2. The declared native real control space has dimension 4; the formal Lie closure of its anti-Hermitian generators has real dimension 10 (`so(5)`); the complex diagonal-bimodule closure of the **native generators alone** has dimension 8; that of their Lie closure has dimension 20.
3. The existing two P6 static candidate sectors are `J_mix` (complex dimension 5, real `Xi` dimension 5) and `J_full` (complex dimension 8, real `Xi` dimension 8). Both retain the four-dimensional diagonal quadratic-residue image.
4. Requiring the static sector to be a **diagonal bimodule** eliminates `J_mix` and forces `J_full`, conditional on radius-one/off-diagonal support. This requirement is an **independent category/selection axiom**, not something inferred from the H37 dynamics or P3/P4 alone.
5. Even when `J_full` is fixed by this axiom, the primitive source is not recovered: `{H_hop}` and `{K_0,K_1,K_2,K_3}` are distinct source collections but have the same diagonal-bimodule closure `J_full`.

## 1. Exact H37 data and definitions

Use sites `0,...,4`, `p_a=E_aa`, `D_5=span_C{p_a}`, `Delta_D(A)=sum_a p_a A p_a` and

\[
X_e=E_{e,e+1}+E_{e+1,e},\quad
K_e=E_{e,e+1}-E_{e+1,e},\quad e=0,1,2,3.
\]

Let

\[
H_{\rm hop}=\frac12\sum_{e=0}^3X_e,\qquad
H=\mathrm{diag}(0,1/7,-1/9,2/11,-3/13)+H_{\rm hop},
\]

\[
\mathcal L(A)=-i[H,A]+\frac23(\Delta_D(A)-A).
\]

This GKSL generator gives a legitimate CPTP semigroup `Phi_t=exp(t L)`. The declared native anti-Hermitian control space is `K_nat=span_R{K_e}`. It is a **declared mathematical control alphabet**; its independent realization by hardware has not been established.

## 2. Exact H37 generator-Krylov ranks (H115-A)

Set

\[
\mathcal M_k^{\mathcal L}=\sum_{j=0}^k\mathcal L^j(D_5),\qquad
\mathcal H_k^{\mathcal L}=(1-\Delta_D)\mathcal M_k^{\mathcal L}.
\]

These are complex linear spans. Each `L^j(p_a)` is Hermitian, so their complex rank equals the real rank of their Hermitian coefficient vectors (5 diagonal real entries plus 20 real coherence coordinates). SymPy computes exactly, over rationals (with real and imaginary components split):

| k | dim_C M_k^L | dim_C H_k^L |
|---:|---:|---:|
| 0 | 5 | 0 |
| 1 | 9 | 4 |
| 2 | 13 | 8 |
| 3 | 17 | 12 |
| 4 | 21 | 16 |
| 5 | 23 | 18 |
| 6 | **25** | **20** |

Consequently `M_6^L=M_5(C)` and `H_6^L=ker Delta_D`. A modular rank certificate on the `25 × 35` coordinate matrix gives rank 25 **modulo 101 and modulo 1009**; the denominator primes are invertible modulo both. Full rank modulo a prime implies rank 25 over the rationals, and the ambient dimension is 25. The script also checks exact rational ranks at all intermediate orders.

**Non-nearest-neighbor witness:**

\[
\bigl(\mathcal L(p_0)\bigr)_{01}=\frac i2,
\qquad
\bigl(\mathcal L^2(p_0)\bigr)_{02}=-\frac14.
\]

Thus order 2 already reaches the non-native 0–2 coherence. In fact `H_1^L=span_C{K_e}` (both have dimension 4), but `H_2^L` is **not** `J_full`, despite both having complex dimension 8: `H_2^L` includes a distance-two component absent from `J_full`.

**Fidelity to the original P3 definition.** The displayed `H_k^L` is generator-Krylov-based, and should not be silently identified grade by grade with `H_k(Phi_t,D)` using a discrete CPTP channel. There is, however, a direct **eventual saturation** theorem for the actual CPTP semigroup:

**Nonresonant sampling lemma.** Let `L` be a finite-dimensional linear map. If `exp(t lambda)` is distinct for every pair of distinct eigenvalues `lambda` of `L`, then `C[L]=C[exp(tL)]`. Proof: the exponential is locally invertible (derivative `t exp(t lambda) != 0`) near each spectral point; distinct images permit Hermite interpolation of a polynomial `q` satisfying `q(exp(t z))=z` to the required Jordan orders at each eigenvalue. Thus `L=q(exp(tL))`, while `exp(tL)` is already a polynomial in `L` by Cayley–Hamilton. In particular, for all sufficiently small real `t>0`, the required spectral nonresonance holds. For such `t`, cyclic subspaces generated by `D_5` under `L` and under `Phi_t` coincide.

Therefore for all sufficiently small `t>0`, the **actual discrete-channel** filtration `M_k(Phi_t,D_5)` also **eventually** fills `M_5(C)` and its projected hidden filtration eventually fills the full 20-dimensional off-diagonal space. This theorem **does not identify the discrete-channel grade-6 rank** nor claim the full P3 residue/QDMR hierarchy equals the generator-Krylov hierarchy grade by grade. If the P3 construction is read on the Heisenberg-adjoint channel, the same dimension conclusions follow for this real symmetric H37 Hamiltonian via entrywise complex conjugation, which intertwines `L` and `L^dagger` on the diagonal-seeded Hermitian space.

## 3. Four different closures (H115-B)

Let `J^D(S)=span_C{d_1 s d_2, d_1 s^dagger d_2: d_1,d_2 in D_5, s in S}` (excluding an automatic addition of `D_5`).

1. `K_nat=span_R{K_0,...,K_3}`: **real dimension 4** (declared independent native generators).
2. `Lie_R(K_nat)=so(5)` as represented by real antisymmetric matrices: **real dimension 10**. This follows from `[K_ab,K_bc]=K_ac` and the path 0–1–2–3–4. It is a formal Lie closure and not necessarily the one-pulse hardware tangent.
3. `J^D(K_nat)=J_full`: **complex dimension 8**, where `J_full=span_C{E_{e,e+1},E_{e+1,e}}`. The exact identity `p_e K_e p_{e+1}=E_{e,e+1}`, `p_{e+1}K_e p_e=-E_{e+1,e}` proves this directly.
4. `J^D(Lie_R(K_nat))=ker Delta_D`: **complex dimension 20**, because Lie brackets span all `K_ab`, and diagonal projections isolate all off-diagonal matrix units.

These 4, 10, 8 and 20 are **different spaces with different real/complex conventions**; comparing their numbers alone has no physical interpretation.

## 4. Why a closure axiom discriminates but does not explain provenance (H115-C)

The P6 Step 1D sector choices are

\[
J_{\rm mix}=\mathrm{span}_\mathbb C\{H_{\rm hop},K_0,K_1,K_2,K_3\},
\]

\[
J_{\rm full}=\mathrm{span}_\mathbb C\{E_{e,e+1},E_{e+1,e}:e=0,1,2,3\}.
\]

Both are radius-one, off-diagonal, complex linear and `*`-stable, with `dim_C J_mix=5`, `dim_C J_full=8`. Both include the native `K_e`. For the Step 1D `Xi(J)=(1-Delta_D)(J-J^dagger)` on real-linear underlying spaces, they give `dim_R Xi(J_mix)=5` and `dim_R Xi(J_full)=8`. Their internal diagonal quadratic residues both span the four-dimensional traceless diagonal algebra: `Delta_D([H_hop,K_e])` runs through four independent incidence directions, while `[E_{e,e+1},E_{e+1,e}]=p_e-p_{e+1}` in the full sector.

But `J_mix` is **not** stable under `D_5` left/right multiplication: `p_0 H_hop p_1=(1/2)E_01` does not lie in `J_mix`. Meanwhile

\[
J^D(K_{\rm nat})=J^D(J_{\rm mix})=J^D(\{H_{\rm hop}\})=J_{\rm full}.
\]

Thus **if one independently adopts** `AX-BIMOD: the correct static P6 sector is the smallest *-closed off-diagonal D_5-bimodule containing the declared microscopic source`, then one uniquely obtains `J_full`. Under Step 1D's weaker admissibility category (complex `*`-stable radius-one sectors), one does **not** uniquely obtain `J_full`.

However, `AX-BIMOD` is not demonstrated to follow from P3/P4 or the generating map `F`. Changing the category from star-span to diagonal-bimodule **changes the conclusion**. Moreover the assignment `S_static -> J^D(S_static)` is **non-injective**: for example the distinct source sets `{H_hop}` and `{K_0,K_1,K_2,K_3}` have the same eight-dimensional closure. Therefore an axiom fixing the *sector* does not prove the origin, individuality, independence or laboratory implementability of the *primitive source*.

### Gauge distinction

For entirely off-diagonal complex subspaces `J`, invariance as a **fixed subspace** under every diagonal phase conjugation `J -> UJU^dagger` is equivalent to diagonal-bimodule stability: distinct off-diagonal matrix units transform under distinct torus characters, whose Fourier averages isolate the individual `E_ij`. Therefore unrestricted fixed-subspace diagonal-torus invariance forces `J_full` in the radius-one category containing all `K_e`. `J_mix` is not invariant as a fixed subspace.

This does **not** imply that a physically **covariant family** `c -> J(c)` must be invariant at each fixed `c`: under a gauge change the Hamiltonian and control-frame inputs also transform, and `J(U.c)=U J(c) U^dagger` permits a transformed mixed subspace. Gauge covariance of the full inputs is weaker than invariance of an individual fixed output. Gauge arguments alone cannot silently install `AX-BIMOD` without stating which action/invariance requirement is physically justified.

## 5. Physical tangent and the five P11 proof obligations

The physical manifold tangent `T_0 M_5^phys` is **not** fixed by the algebraic computations. If the four declared `K_e` are confirmed as independently actuated native controls, they supply a real 4-dimensional subspace of that tangent. Their Lie-generated directions, drift Hamiltonian and terminal-analyzer operations must not automatically be counted as independent first-order native tangent coordinates.

The required P11 obligations are:

- **AX-SRC (source):** supply a measurement-independent origin rule `F -> S_static`, not merely reconstruction from the reported `j_01` or the native-control tomography.
- **AX-CAT (closure category):** derive or explicitly assume why `J` should be a star-span, diagonal bimodule, fixed-torus invariant subspace or another category; prove uniqueness **in that category**.
- **AX-LOC (locality):** preserve radius-one **native** locality rather than applying Lie/saturated dynamical closure as if it were native.
- **AX-GAUGE (covariance):** state how the input gauge frame changes and distinguish invariance of an individual sector from covariance of a sector-valued assignment.
- **AX-PHYS (operational correspondence):** independently tie primitive labels, native control chart and coherent tangents to one actual device, with phase calibration and matched two-stage CPTP experiments if making the full P6 physical claim.

Any P11 selector `sigma` based on information `pi(p)` must satisfy the H113 descent/fibre condition: `pi(p)=pi(q)` implies `sigma(p)=sigma(q)` (or gauge equivalence, if so specified). For Step 1D's admissible class with `J_mix` and `J_full` the condition fails if the sector label is truly independent of the fixed measured H37 data. Imposing AX-BIMOD shrinks the admissible class and restores sector uniqueness **conditionally**; it does not recover `S_static` uniquely.

## 6. Downstream handoff and explicit limits

**To P6:** The original frozen P6 preprint is unchanged. H37's standard GKSL channel and signed-current witness remain mathematical testbeds, not CR-exclusive experimental predictions. Physical static provenance and device verification remain OPEN.

**To P9:** A formally produced effective coupling, commutator, curvature source or collision operator cannot be called a *CR-derived native primitive* merely because its direction appears in a dynamical Krylov, Lie or diagonal-bimodule closure. Require an independent source certificate before making that stronger claim. No ADM, HDA or Einstein-dynamics result is supplied here.

**To P11:** The next gate should test the **existence and independence of AX-BIMOD or a competing physical closure principle**, not proliferate more ungrounded `J_5` sectors. Demand a source functor with a non-circular input, gauge/locality proof, and an explicit countermodel or universality criterion.

**Evidence status:** exact rational symbolic calculation plus two modular full-rank certificates; independent external AI audit, GitHub CI, physical hardware, human peer review and Lean proof **not performed**. This H115 audit establishes finite algebraic facts and conditional structural consequences, not Generative Completeness.

## 7. Reproduction

`python P3P11_H115_h37_exact_audit.py` writes `P3P11_H115_h37_exact_results.json`, verifies the 5-site generator, 4/5/8/10/20 dimensions, diagonal-residue rank, off-support witness, and all generator-Krylov ranks exactly. Run with SymPy installed. No random samples or floating point thresholds enter the calculations.