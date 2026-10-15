# H67 — Controlled Instrument-Kernel Stabilizer and the Price of an Autonomous Physical Observer

**2026-10-15 | P3–P11 Mathematical Bridge; P9 GR-I.** Stacked on H66 Draft PR #85 (79/79 CI PASS). This stage deliberately returns to the **same H42/H46/H48 exact rational microscopic source** and the **same twelve-outcome CP quantum instrument** used in prior original-P3 research. It asks whether physically declared controls can preserve a current observer's kernel and permit an autonomous controlled observer quotient. It does not relabel this rich quantum-output instrument as the frozen P6's population-only apparatus. Its availability is an **independent conditional quantum-block-tomography assumption**.

## 1. Fixed microscopic/observer setup — no post-hoc changes

Let \(\Phi(X)=U XU^\dagger\) be the genuine fixed three-site H42 unitary channel with original P3 \(R_3=D_3^0\) and saturating signed residue, and let \(\mathcal C:M_3(\mathbb C)\to\bigoplus_{k=1}^{12}M_3(\mathbb C)\) denote H46's **full labelled quantum-output** CP instrument (not its classical outcome probabilities, and not its nonselective quantum marginal). The instrument's branch maps are individually CP, with total trace preserved.

H48 established by exact complex-linear rank audit,

\[
\operatorname{rank}\mathcal C=7,\quad
\ker\mathcal C=\operatorname{span}_{\mathbb C}\{E_{02},E_{20}\},
\quad
\operatorname{rank}(\mathcal C,\mathcal C\Phi)=9.
\]

In particular \(\Phi(\ker\mathcal C)\not\subseteq\ker\mathcal C\). Therefore even the **uncontrolled** observer cannot evolve autonomously on \(\operatorname{im}\mathcal C\) through a well-defined linear \(\Phi_{\rm eff}\) satisfying \(\mathcal C\Phi=\Phi_{\rm eff}\mathcal C\).

These are H48's prior exact results, reproduced in the new H67 checker to provide the common foundation for **new controlled-kernel classifications**. Measuring \(\mathcal C\) at an intermediate time *inserts an invasive instrument*. The stacked records \((\mathcal C,\mathcal C\Phi)\) describe **two non-interfering observations on separately prepared unmeasured copies**, not one physically nondisturbing two-step monitored process.

## 2. H67.1 — full anti-Hermitian stabilizer theorem of the H46 instrument kernel

For an anti-Hermitian control generator \(K^\dagger=-K\) the coherent tangent action on microscopic operators is \(\mathrm{ad}_K(X)=[K,X]\). A well-defined **instantaneous** induced linear control on the compressed instrument record requires

\[
\mathrm{ad}_K(\ker \mathcal C)\subseteq\ker\mathcal C.
\]

The kernel consists *precisely* of the endpoint chords \(E_{02},E_{20}\). For arbitrary complex \(3\times3\) K,

\[
\begin{aligned}
[K,E_{02}]&=(K_{00}-K_{22})E_{02}
   +K_{10}E_{12}-K_{21}E_{01}
   +K_{20}(E_{22}-E_{00}),\\
[K,E_{20}]&=(K_{22}-K_{00})E_{20}
   +K_{12}E_{10}-K_{01}E_{21}
   +K_{02}(E_{00}-E_{22}).
\end{aligned}
\]

Because only \(E_{02},E_{20}\) are in the kernel, the first commutator belongs to the kernel exactly when \(K_{10}=K_{21}=K_{20}=0\), and the second precisely when \(K_{12}=K_{01}=K_{02}=0\). Under anti-Hermiticity these are equivalent constraints; all offdiagonal entries vanish. Conversely diagonal anti-Hermitian K rotates the two chords within their span.

**Theorem H67.1 (exact 12-branch instrument-kernel stabilizer):**

\[
\boxed{\{K\in\mathfrak u(3):[K,\ker\mathcal C]\subseteq\ker\mathcal C\}
=\mathfrak u(1)^3}
\]

and in the traceless coherent subalgebra \(\mathfrak{su}(3)\) the stabilizer is the 2D diagonal Cartan algebra.

**Meaning:** neither the two real exchange controls actually declared for frozen P6 nor the added odd exchange Q from H66 induce an autonomous *instantaneous* coherent motion on this 7D **H46 full quantum-instrument quotient**; they mix omitted endpoint coherence back into the recorded sector. A mere diagonal Stark/phase gate *does* preserve this chosen kernel at control-only level, but H42's uncontrolled \(\Phi\) already violates its invariance; such a gate does not cure autonomous microscopic closed evolution.

Do not infer physical permission for \(\mathcal C\) or an actual P6 micro-to-observer intertwiner merely from this exact mathematical classification.

## 3. H67.2 — controlled leakage ranks distinguish side versus chord generators

Let \(\mathcal O_K=(\mathcal C,\mathcal C\mathrm{ad}_K)\) on the input operator space. The new exact checker verifies:

| Coherent control tangent | \(\mathrm{rank}(\mathcal C,\mathcal C\mathrm{ad}_K)\) | Interpretation |
|---|---:|---|
| Diagonal anti-Hermitian \(i(E_{00}-E_{11})\) or \(i(E_{11}-E_{22})\) | 7 | Chord remains hidden |
| Real 01/12 exchanges \(A,B\) | 9 | Both previously invisible chord directions appear |
| Imaginary symmetric 01/12 exchanges \(Q_{01},Q_{12}\) | 9 | Both chord directions appear, but knob is additional physical resource |
| Direct endpoint 02 exchange \(A_{02}\) or \(Q_{02}\) | 8 | One linear chord combination appears; one remains unseen |

These are statements about **linearized two-channel algebraic response on the current instrument observer**, not autonomous quotient existence. Full rank 9 means the stacked operator-space readout is informationally complete **if** full labelled quantum-block records and control derivatives can be independently accessed on physically prepared copies.

The rank profile follows from the exact commutators above and \(\ker\mathcal C=\mathrm{span}\{E_{02},E_{20}\}\). The missing two complex basis elements determine the rank increment. In particular an arbitrary 01/12 coherent tangent with nonzero nearest-neighbor components generically releases both missing complex directions, whereas an endpoint-only tangent releases only one. The exact checker verifies the canonical eight traceless anti-Hermitian basis cases using Gaussian fractions, without treating rank as an instrument's classical-probability sensitivity.

## 4. H67.3 — a physically legitimate finite CPTP pulse test

A rational **real** exchange Cayley control

\[
U_A(h)=(I+hA)(I-hA)^{-1},\quad h=1/4,
\]

is unitary and coherent CPTP, and it yields

\[
\operatorname{rank}\bigl(\mathcal C,\mathcal C\operatorname{Ad}_{U_A}\bigr)=9.
\]

This is an exact finite pulse counterpart to the infinitesimal rank leakage; the same *fixed* \(\mathcal C\) observes all outputs.

By contrast a separately supplied diagonal unitary \(G=\mathrm{diag}(-i,1,1)\), considered **only as a control** on an already supplied input, preserves \(\ker\mathcal C\) and yields

\[
\operatorname{rank}(\mathcal C,\mathcal C\operatorname{Ad}_G)=7.
\]

The latter comparison **does not** say a diagonal phase cannot help a *different protocol* recover imaginary coherence (H39), or that the full output of a 7D observer is population-only. Different observer protocols and their kernels must not be silently identified.

Finally, any hypothetical family \(\Psi_x=\operatorname{Ad}_{U_x}\circ\Phi\) that includes an identity control \(U_0=I\) cannot satisfy an autonomous controlled effective quotient \(\mathcal C\Psi_x=\widetilde\Psi_x\mathcal C\) for **all** \(x\) since at \(x=0\) it would require the already false \(\Phi(\ker\mathcal C)\subseteq\ker\mathcal C\). One special nonzero pulse may alter a kernel property, but cannot repair the *family* while its zero-control baseline is unchanged.

## 5. H67.4 — H50 operational-equivalence and physical-source boundary

An exact **controlled process** requires not just \(\mathcal C\mathrm{ad}_K\) but actual same-source microscopic CPTP operations and outcome-conditioned measurements at every relevant time. If the complete physical and standard-QM descriptions have identical initial states, **all** controlled CPTP maps, CP instrument branches and adaptive control choices, H50 already proves equality of all finite joint probabilities and conditional outputs by induction. Hence the rank changes here are conventional finite quantum mechanics, not evidence of a CR-only new quantum law.

A valid P3→P6 provenance claim would require:

1. an independently inherited physical microscopic sector \(\mathcal J_N\) and **actual** source-to-control tangent map, not simply the computed H32 Krylov \(\Xi(H_{\le3})\) or a declared supplementary Q;
2. matching physical observer algebra/instrument and a source-compatible *-map or an appropriately structured CP map;
3. either kernel preservation for a proposed **autonomous quotient** or explicit predictive memory augmentation; a rank-9 passive two-copy record is not a nondisturbing quantum instrument at two times;
4. explicit physically admissible coherent calibration, positive CP branches, conditioning/singular-value estimates and device timing if proposing operational phase access;
5. separate mathematical proofs for spatial K4 soldering, DeWitt signature provenance, full off-shell HDA/ADM/Einstein dynamics.

**H67 verdict:** An exact full instrument-kernel stabilizer and a rank-by-control classification are established **within the declared finite comparator**, and a new all-control autonomous quotient is ruled out for that fixed \((\Phi,\mathcal C)\). A nontrivial independently *physically sourced* P3→P6 controlled-CPTP intertwiner remains OPEN. The H48 kernel criterion's sufficiency concerns **linear** induced maps on \(\mathrm{im}\mathcal C\), not automatic completely positive extensions.

## 6. Next H68

Seek a minimal **honest predictive augmentation** for \(\mathcal C\) which carries its two missing chord quadratures without invasive measurement, then test which physical controls close it and whether they are actually sourced from P3/P6. An injected full 9D operator state is algebraically sufficient, but calling that an emergent observer theory would be vacuous unless a physically independent memory carrier and its admissible CP dynamics are specified. In parallel check whether a smaller partial domain (e.g., reflection-even diagonal seeds) allows a nontrivial, physically meaningful autonomous controlled quotient, always declaring that state/domain restriction.

**Reproduce:** \`python3 P3/P9H67ControlledObserverKernelStabilizerExactCheck.py\`. Draft/unmerged, no frozen/main edits, no Lean proof, human expert refereeing, real hardware measurement, CR-specific discriminator, or P9 Minimum Success/Einstein dynamics.
