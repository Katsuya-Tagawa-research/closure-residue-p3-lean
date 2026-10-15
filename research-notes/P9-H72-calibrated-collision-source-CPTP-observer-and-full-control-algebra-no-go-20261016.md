# H72 — Calibrated Microscopic Collision Source and Constructive CPTP Observer; No Proper Algebraic Observer for the Full Two-Knob P6 Control Group

**2026-10-16 | P3–P11 Mathematical Bridge / Route A.** This manuscript-quality research note advances H71 by obtaining the collective control generator from **H42's independently specified microscopic collision factorization** rather than attaching an arbitrary after-channel knob. It also closes a key alternative with a representation-theoretic No-Go: no proper nontrivial **unital C*-subalgebra** of \(M_3(\mathbb C)\) is invariant under all independent real 01/12 exchange rotations. All results are standard finite quantum mechanics with exact Gaussian-rational checks, NOT a P3-only physical-origin theorem, a CR-exclusive discriminator or the whole frozen P6 hardware.

## H72.1 — source-derived collective control from a calibrated actual microscopic factor

The **original H42 channel** was built with one explicit rational three-level unitary

\[
U=P_{\rm ph}\,V,\qquad
P_{\rm ph}=\operatorname{diag}(i,1,i),\qquad
V=(I+\tfrac12 K)(I-\tfrac12 K)^{-1},\quad
K=A+B,
\]

\[
A=E_{01}-E_{10},\qquad B=E_{21}-E_{12},\qquad K^3=-2K.
\]

Its exact real Cayley factor and full physical one-step unitary matrix are **unchanged** from H42. Both \(P_{\rm ph}\) and \(K\) commute with the original site reflection \(P=E_{02}+E_{11}+E_{20}\).

**Additional independent microscopic calibration assumptions:**

- The architecture provides the factor \(P_{\rm ph}\) as a **known physical unitary operation with a fixed phase reference**, not just an unknown phase convention, and the full unitary representative \(U\) is calibrated relative to it.
- The real factor is known to arise from the *single collision architecture* \(V_s=(I+sK)(I-sK)^{-1}\), with the same microscopic \(K\) and a physically adjustable real collision-duration/coupling parameter \(s\). The existence of this control dial **does not follow from knowing a single uncontrolled CPTP map \(\Phi=\mathrm{Ad}_U\)**.
- The following site-dephasing controls are physically available with a **common matched endpoint setting**: \(\mathcal D_0^{(q)}\), \(\mathcal D_2^{(q)}\), and an independent calibrated center \(\mathcal D_1^{(q_1)}\). This symmetry-locking is a genuine hardware assumption, **not a frozen-P6 v9.1 theorem**.

Under the first assumption, one reconstructs the real collision unitary uniquely as \(V=P_{\rm ph}^\dagger U\). Since \(V+I\) is invertible, the **inverse Cayley formula** is exact:

\[
\boxed{K=2(V-I)(V+I)^{-1}=A+B.}
\]

The 3×3 matrix inverse and equality are verified over exact Gaussian rationals on the **same H42 U**. The construction is not a post-hoc definition of an arbitrary physical control generator: the specified microscopic collision architecture already uses K as its interaction. Nor is it legitimate to claim original P3 hidden Krylov candidates supplied the generator. Indeed H42's exact \(\Xi(H_{\le\infty})\) has rank 5 and does **not** contain \(A+B\). The new independent hardware fact is the calibrated factorization and the adjustable collision parameter; the unchanged P3 data alone remain insufficient (H42/H66).

**Unique-control extraction has a precise scope:** a CPTP conjugation channel determines its unitary only up to a global phase, and without an independently calibrated \(P_{\rm ph}\) the decomposition is not unique. The inverse Cayley map supplies a unique K **conditional on a fixed unitary representative, a fixed calibrated factor and the selected Cayley architecture**. It does not prove the architecture is the unique physical explanation of \(\Phi\).

## H72.2 — a *microscopically parameterized*, rather than appended, controlled-CPTP family

With the preceding collision architecture, the genuinely source-parameterized microscopic unitary is

\[
U_s=P_{\rm ph}(I+sK)(I-sK)^{-1}
\]

and its CPTP channel is \(\Phi_s=\mathrm{Ad}_{U_s}\). At \(s=1/2\), \(\Phi_s=\Phi\) is **exactly the original H42 source**, with its genuine nonzero depth-three P3 signed quadratic return. This is a **different operational family** from the H71 after-channel composition \(\mathrm{Ad}_{V_+(s)}\circ\Phi\); both are finite CPTP and parity covariant, but only here is the control dial located inside the specified microscopic collision factor.

The control tangent is also derived, not guessed. Because \(K^3=-2K\), differentiation gives

\[
\frac{dV_s}{ds}V_s^\dagger
=\frac{2}{1+2s^2}\,K,\qquad
\boxed{
\frac{dU_s}{ds}U_s^\dagger
=\frac{2}{1+2s^2}\,P_{\rm ph}KP_{\rm ph}^\dagger.
}
\]

The right-logarithmic tangent is anti-Hermitian, nonzero, and commutes with reflection. H72 exact code checks the derivative identity by multiplying explicit rational matrix inverses, not by approximating a transcendental logarithm.

Let \(\mathcal D_j^{(q)}(X)=qX+(1-q)Z_jXZ_j\), \(Z_j=I-2E_{jj}\), be independently specified CPTP phase-flip channels. With **symmetric endpoint settings** \(q_0=q_2=q\), define

\[
\Psi_{s,q,q_1}
=\mathcal D_2^{(q)}\circ\mathcal D_1^{(q_1)}
 \circ\mathcal D_0^{(q)}\circ\Phi_s.
\]

Every factor has a genuine finite Kraus/unitary CPTP realization. Because the symmetric endpoint noise commutes with reflection conjugation, and \(P_{\rm ph}\) and \(V_s\) commute with reflection, the H43 physical reflection twirl

\[
\mathcal E(X)=\tfrac12(X+PXP)
\]

intertwines the **full** microscopic controlled channel for **all** specified settings:

\[
\boxed{\mathcal E\Psi_{s,q,q_1}=\Psi_{s,q,q_1}\mathcal E.}
\]

Every finite prescribed concatenation also closes on the nontrivial unital C*-algebra

\[
\operatorname{im}\mathcal E\cong M_2(\mathbb C)\oplus\mathbb C,\qquad
\dim_{\mathbb C}=5.
\]

The verification checks all nine \(M_3\) basis units, a range of rational s and noise settings, and an explicit finite sequence. The analytic proof works for arbitrary real s and q in [0,1], not only the exact tested grid, since covariance is an operator identity. Adaptive feedback conditioned on genuinely inserted instruments is not yet established.

**Limited original-P3 residue fidelity:** At the actual original \(s=1/2\) noiseless channel, true H42 signed P3 quadratic returns are computable from \(\mathcal E(d)\) on reflection-even diagonal seeds \(d=\operatorname{diag}(a,b,a)\), with nonzero rank-one return image (H71). Arbitrary diagonal seeds and genuinely noise-dependent new P3 residue filtrations are NOT covered; H70 supplies a reflection-pair counterexample to the unrestricted claim.

This is a meaningful finite Route-A **constructive benchmark under an explicit architecture**. It is not yet a **derivation of independently frozen P6 v9.1's two physical exchange knobs** and does not make the generator \(K\) a product of the original P3 hidden \(\Xi\) construction.

## H72.3 — the full two-real-knob P6 group has no proper invariant unital observer algebra

The frozen P6 benchmark admits separate real coherent edge controls \(A\) and \(B\). Their real Lie closure is \(\mathfrak{so}(3)\) (H66), whose connected compact group of unitaries is the standard irreducible real-rotation representation \(SO(3)\subset U(3)\).

The new exact checker computes the simultaneous complex centralizer of \(A,B\) on the nine matrix-unit basis. Its commutator constraint matrix has complex rank eight, so

\[
\boxed{\{X\in M_3(\mathbb C):[X,A]=[X,B]=0\}=\mathbb C I.}
\]

Now suppose \(\mathcal A\subset M_3(\mathbb C)\) is a **unital C*-subalgebra** invariant under **all** independent real coherent rotations \(e^{tA}\), \(e^{tB}\) and their inverses. The induced action of the connected \(SO(3)\) group continuously permutes the finitely many minimal central projections of \(\mathcal A\), so each is fixed. Each thus commutes with A and B and, by the scalar centralizer above, equals 0 or I. Hence \(\mathcal A\) has trivial center and is a finite-dimensional C*-factor. Such an algebra acts unitally on \(\mathbb C^3\) as \(M_k(\mathbb C)\otimes I_m\) with \(km=3\). Since 3 is prime,

\[
\boxed{\mathcal A=\mathbb C I\quad\text{or}\quad
       \mathcal A=M_3(\mathbb C).}
\]

**Theorem H72.3 (restricted but decisive control-algebra NO-GO):** no proper nontrivial unital C*-algebra can be invariant under the *full* two-independent-real-exchange control group. Therefore a **trace-preserving CP conditional expectation** onto a proper unital subalgebra cannot yield autonomous linear/CPTP evolution for the *entire reversible control group* and its inverse family. To see why control-induced quotient closure implies invariance in this case, recall that a trace-preserving conditional expectation onto a unital C*-subalgebra is the Hilbert–Schmidt orthogonal projection. If its kernel is preserved by a unitary superoperator and its inverse, the orthogonal range is invariant as well. The reduced CPTP dynamics are then restrictions of the microscopic conjugations, which requires that the image algebra be group-invariant.

This theorem excludes **neither** a proper non-idempotent CP observer representation with a nonalgebra image (e.g. possibly a covariance-based operator system), **nor** a quantum-classical memory carrier, state-dependent restricted sector, a purely scalar/trivial observer, or restricted physical controls. It does not prove the full P6 system has no physically useful quantum observer; it proves one **specific, natural algebraic architecture** cannot be simultaneously nontrivial, proper, and invariant under all the independent coherent P6 controls.

The original five-dimensional H43 observer is such a unital subalgebra; H71 already exhibited explicit failure of invariance under A and B. This theorem shows the obstruction is not peculiar to reflection parity among proper **subalgebra-valued** conditional-expectation observers.

## 4. Route A provenance boundary and H73

| Claim | Verdict |
|---|---|
| Reconstruct collision generator K from calibrated original H42 microscopic unitary factorization | **EXACT / conditional on known phase and architecture** |
| Tunable *microscopic* U_s family + symmetric site dephasing has true CPTP 5D observer closure | **EXACT / conditional physical family** |
| Original fixed-H42 nonzero signed P3 residue reconstructed on reflection-even diagonal seeds | **EXACT / restricted original channel** |
| Frozen P6 two independent real knobs admit a proper invariant unital-C*-algebra expectation observer under all rotations | **NO-GO** |
| Physical architecture, tunable collision dial and locked noise are generated by **P3-only** hidden algebra | **NOT PROVED** |
| This independently reproduces actual frozen P6 hardware \(\mathcal J_N\), X/Y readout or P9.72 SWAP+ZZ control | **NO** |
| CR-specific experimental discriminator, P9 Einstein minimum success, KKS/ADM/HDA | **NOT PROVED** |

**H73 target:** investigate a non-idempotent **CP operator-system observer** covariant under the full real-exchange plus dephasing P6 two-knob family. In a real-transpose-covariant sector an observer retaining the symmetric operator harmonics may be proper and quantum-CPTP despite no proper invariant *subalgebra* (do not preclude this by H72's factor theorem). If a physically specified map exists, check its positivity/CP/trace preservation, exact intertwining for *all* two-knob controls/dephasing, information loss and original-P3 signed residue access. Critically, source the observer physically (e.g. an actual independently calibrated CPTP noise/collision channel), not by constructing an arbitrary linear projection. Conversely show how added phase-generating detuning alters the invariant sectors. Alternatively, find a richer microscopic collision architecture that yields all physical control knobs without importing them.

**Scope:** Finite comparator, Gaussian-rational and analytic algebraic proofs, dedicated CI, Draft/unmerged; no frozen-main edits, Lean, human review or experiment.
