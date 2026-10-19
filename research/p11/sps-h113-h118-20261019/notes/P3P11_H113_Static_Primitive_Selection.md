# H113 — Static Primitive Selection: Descent Criterion, No-Go, and Gauge-Constrained Closure

**P3–P11 Mathematical Bridge / 2026-10-19**

Status: **Mathematical finite result (self-contained proofs; toy-witness symbolic checks), P11 physical provenance and generative completeness OPEN.** The H37 figures below are accepted as the supplied Step 1D premises, not independently reconstructed by the companion code.

## 1. Typed interfaces

Distinguish:

- `H_k(Phi,D)`: dynamically generated hidden sector/filtration associated with a particular channel and observational diagonal algebra;
- `J_N`: statically specified complex operator sector/primitive closure;
- `T_0 M_N^{phys}`: *real* tangent space/cone of physically available transformations at the indicated base point. The geometry of `M_N^{phys}` depends on what preparations, hardware controls, couplings, and interventions are actually available.

These are not interchangeable; no equality or inclusion is inferred solely from dimensions or from matching diagonal residues.

## 2. Theorem H113.1: necessary and sufficient descent condition

Let `P` denote a class of admissible microphysical completions, `C` the data accessible to an independent CR-based source-selection rule, `pi:P -> C` the forgetful data map, and `sigma:P -> S` the physically valid static-sector assignment (or its gauge-equivalence class). Then a deterministic `f:C -> S` with `sigma=f o pi` on `P` exists **if and only if**

> `pi(p)=pi(q)` implies `sigma(p)=sigma(q)` for all `p,q in P`.

**Proof.** Necessity follows by substituting equal inputs into `f`. For sufficiency define `f(c)=sigma(p)` for any `p` satisfying `pi(p)=c`; the fibre condition makes this well-defined on `im(pi)`. Outside the image, the choice is irrelevant to the data domain. QED.

**Symmetry refinement.** If `P,C,S` carry compatible actions of a gauge group `G` and both `pi` and `sigma` are equivariant, the descended `f` is equivariant automatically on `im(pi)`. Selecting a gauge-fixed representative instead of a gauge-equivalence class is an *additional* gauge-fixing commitment.

### H37 reduced-data implication

For the *restricted* fingerprint consisting of H37 native exchange controls and the reported maximal four-dimensional second-order diagonal residue, Step 1D supplies two compatible sectors with `dim_R Xi(J5_mix)=5` and `dim_R Xi(J5_full)=8`. If the required target is `Xi(J)`, the fibre condition fails. Therefore no faithful unique selection of `Xi` descends from **that restricted fingerprint** alone.

This does **not** establish non-identifiability from the complete microscopic channel, an unlimited family of interventions, or a stronger independently supplied selection axiom. Neither `Jmix` nor `Jfull` is claimed to be exchanged by an automorphism: their dimensions differ.

## 3. Theorem H113.2: exact diagonal-bimodule closure

Let `D_N=span_C{E_ii}` inside `M_N(C)` and let `S subset M_N(C)` be any static primitive set. Put

`J_N^D(S)=span_C{d1*s*d2, d1*s†*d2 : s in S, d1,d2 in D_N}`.

Then

`J_N^D(S) = span_C { E_ij : exists s in S with s_ij != 0 or conjugate(s_ji) != 0 }`.

Indeed, `E_ii s E_jj=s_ij E_ij` proves inclusion of every such matrix unit; multiplying diagonal operators never creates a new matrix coordinate, proving the reverse inclusion. Consequently this is the **unique smallest complex-linear, *-closed, D_N-bimodule** containing `S`.

Important: different primitive sets with identical support union and adjoints have identical diagonal-bimodule closures; this closure forgets finer primitive provenance, amplitudes, and relative phase calibration. The theorem is a closure operation conditional on `S`; it is not a physical origin theorem for `S`.

## 4. Theorem H113.3: diagonal gauge-invariant sector classification

Let `T^N` act by conjugation `A -> U_theta A U_theta†`, with `U_theta=diag(e^{i theta_1},...,e^{i theta_N})`. If a complex-linear `J subset M_N(C)` is invariant under this action, it decomposes as

`J = W ⊕ span_C {E_ij : (i,j) in E_J, i != j}`,

where `W=J intersect D_N` may be any complex subspace of `D_N`. If `J` is *-closed, the off-diagonal edge set `E_J` is symmetric under `(i,j) <-> (j,i)`, and `W` is *-closed.

**Proof.** The torus characters `e^{i(theta_i-theta_j)}` are distinct for distinct ordered off-diagonal pairs. Fourier averaging the conjugation orbit extracts `A_ij E_ij` from each `A in J`. Averaging with the trivial character extracts its diagonal part. Invariance and complex linearity establish the stated direct sum. QED.

**Subtlety:** gauge invariance alone does **not** imply a `D_N`-bimodule when `W` is an arbitrary diagonal subspace (e.g. `W=span{I}`). A gauge-invariant `J` is a diagonal bimodule exactly when `W` is spanned by a subset of coordinate projections `E_ii` (the off-diagonal part is automatically a bimodule).

Applied to physical selection, the classification is **conditional** on the input's full diagonal gauge symmetry. A phase-calibrated real `X` control can break that symmetry and must not be silently treated as gauge-invariant data.

## 5. H113.4: a canonical CP-map selector exists but does not recover physical primitives

For a CP map `Phi(A)=sum_a K_a A K_a†` use vectorization and Choi `C_Phi=sum_a |K_a>><<K_a|`. Thus

`K_can(Phi) := unvec(Ran C_Phi) = span_C{K_a}`.

The subspace is representation-independent, including under Kraus-unitary mixing, and the conditional construction `J_can(Phi)=J_N^D(K_can(Phi))` is therefore canonical from the channel.

However, this **is not** a selection of physical control primitives. Example: for the identity map `Phi=id`, `K_can=span{I}` and `J_can=D_N`. Hardware can independently make coherent `X_12` controls available at the same baseline. The channel alone cannot reconstruct that available physical tangent.

This disproves the implication 'canonical CP representation -> unique physical primitive' without an operational-completeness or microphysical-access assumption.

## 6. H113.5: exact three-level witness for physical tangent non-identifiability

Let `N=3`, `Phi=id`, `D_3=span{E11,E22,E33}`, and mark the native available control `X12=E12+E21`. Consider two distinct admissible physical implementations:

- `p_A` permits Hamiltonian generators `X12` only; `S_A={X12}`.
- `p_B` permits `X12` and independently `X23=E23+E32`; `S_B={X12,X23}`.

They share the exact same baseline channel, diagonal observation algebra, and marked known `X12` control, and hence the same CR filtration calculated **at the baseline only**.

Nevertheless, diagonal-bimodule closure gives `dim_C J_N^D(S_A)=2` and `dim_C J_N^D(S_B)=4`.

On the unitary-control side let `A=iX12`, `B=iX23`, `C=[A,B]=E31-E13`. Their Lie brackets satisfy

`[A,C]=-B`, `[B,C]=A`.

Thus the Lie algebra generated by `A` has real dimension 1, whereas that generated by `A,B` has dimension 3; corresponding local unitary-control adjoint tangent dimensions are 1 and 3. Both implementations use valid finite-dimensional unitary channels, but their accessible controls differ beyond the one **marked** native control. This is a self-contained **baseline-information** no-go, not an H37 hardware model.

## 7. P11 proof obligations

1. **AX-SRC (independent source):** specify `pi` and the admissible physical completions without consulting the target sector response to be predicted. State exactly which microscopic data are given.
2. **AX-DESC (fibre constancy):** prove the H113.1 fibre condition, ideally up to diagonal-gauge equivalence. Otherwise explicitly classify the indistinguishable fibres.
3. **AX-LOC:** show locality of the source rule and closure, with a specified radius and behaviour under composition and finite-time propagation.
4. **AX-GAUGE:** distinguish a gauge-covariant sector assignment, a gauge-invariant sector, and a physically phase-fixed control frame.
5. **AX-ACCESS:** prove which generated matrices correspond to real, physically admissible CPTP tangent directions, not just formal operator coordinates.
6. **AX-DISC:** produce an independently calibrated discriminant between H37 `J5_mix` and `J5_full`, or prove a full-data selection no-go. Merely selecting the smaller dimension is a convention, not an origin principle.
7. **AX-GEN:** only after the above prove any claimed dependence on generative map `F`; do not count a chosen primitive as an `F`-derived primitive.

## 8. Interfaces and status

- **P3/P4:** `H_k(Phi,D)` is dynamical; P4 higher-order visibility does not alone identify static primitives.
- **P6:** origin of the frozen `J_N`, available phase-sensitive X/Y readout, independent control calibration, and physical two-stage CPTP matching remain OPEN.
- **P9:** this work does not provide a Cartan soldering, KKS-ADM transfer, off-shell HDA, or Einstein equations. Any collision-model coupling operator requires an additional sector-descent certificate.
- **P11:** mathematical No-Go for insufficient fingerprints and precise necessary/sufficient descent criterion are established; *generative completeness* remains OPEN.

## 9. Reproducibility boundaries

`P3P11_H113_static_primitive_no_go_audit.py` checks the three-level matrix-unit and Lie-bracket witness, the identity-channel Choi support, and an elementary diagonal gauge character using exact SymPy arithmetic. It does **not** recompute H37 `Xi` dimensions or run any GitHub CI, experiment, or independent peer review.