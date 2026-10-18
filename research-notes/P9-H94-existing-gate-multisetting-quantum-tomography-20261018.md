# H94 — Multi-Setting Coherence Recovery Using Existing H75/H76 Gates: Rank-12 *Classical Tomography* Despite the Destructive CPTP Reset

**2026-10-18 | P9 GR-I / P3–P11 Mathematical Bridge / Route A.**
**Base:** H93 Draft PR #112 at \`62f1ac2\`, **H93 100/100 GitHub Actions PASS**. Original H75 four-Kraus CPTP micro source, H92 genuine five-level output seed, P3 original signed residue, main, and frozen P1–P8 unchanged. This result separates **what can be inferred from multiple state preparations and readouts** from **what can be generated as a single coherent Hamiltonian/canonical phase space**.

## H94.1 — The complex U is a post-erasure unitary, not an available pre-reset U(5) control

The unchanged H75 Kraus operators on \(\mathbb C_E^2\otimes\mathbb C_S^3\) are
\[
L_{ab}=|a\rangle\langle b|_E\otimes U M_a,\quad a,b\in\{0,1\},
\quad M_0=\operatorname{diag}(1,3/5,3/5),\quad
M_1=\operatorname{diag}(0,4/5,4/5).
\]
For **every** six-level input \(X\),
\[
\boxed{
\Phi_\mu(X)
= \sum_{a=0,1}|a\rangle\langle a|
\otimes UM_a\bigl(\operatorname{Tr}_E X\bigr)M_aU^\dagger
= \mathcal J_{\!U}\bigl(\operatorname{Tr}_E X\bigr).
}
\tag{H94-F}
\]
The fixed H42 \(U\) can be complex; nevertheless, this exact factorization makes it a **downstream** site rotation in the reset map. The register lost by the partial trace is not re-created by a subsequent fixed \(U\), or by any deterministic postprocessing of the same reset output (linear data processing).

For the genuine source H92 seed
\(\sigma_0=\frac9{59}I_3\oplus\frac{16}{59}I_2\) and physical six-level isometry \(V:\mathbb C^5\hookrightarrow\mathbb C^6\), all twelve genuine source-seeded Grassmann KKS cross-flag tangents
\[
T_\alpha=V\bigl(-i[O_\alpha,\sigma_0]\bigr)V^\dagger,
\quad O_\alpha\in\{X_{ab},Y_{ab}:\ a<3,\ b\in\{3,4\}\},
\]
have \(\operatorname{Tr}_E(T_\alpha)=0\), hence \(\Phi_\mu(T_\alpha)=0\). **Without a pre-reset intervention**, neither a quantum channel acting after \(\Phi_\mu\) nor an arbitrary post-reset positive POVM can distinguish infinitesimal variations in these 12 directions.

The source's reduced qutrit map \(\mathcal V(Z)=U\bigl(\sum_aM_aZM_a\bigr)U^\dagger\) is nevertheless *linear injective* on \(M_3\): the measurement part is a Schur multiplier with strictly positive coefficients \(c_{00}=1\), \(c_{0j}=3/5\), \(c_{jk}=1\) for \(j,k\in\{1,2\}\). Consequently, for every pre-gate \(G\), the rank of \(\Phi_\mu\circ\operatorname{Ad}_G\) restricted to the twelve source tangents equals the rank of \(\operatorname{Tr}_E\circ\operatorname{Ad}_G\) there. A **single setting** has qutrit traceless Hermitian output of real dimension at most 8; it can never reconstruct all twelve infinitesimal Grassmann parameters by itself.

This is a *source-correct exact erasure/rank statement*, not a universal no-go against multiple preparations, time-ordered controls, or enlarged quantum memories.

## H94.2 — Four settings from the EXISTING gate catalog yield exact 12-response informational completeness (CONDITIONAL EXACT)

Use **no new gate**: retain exactly H75's physically declared \(U_A(1/2)\), H75/H76's \(F\) flag-conditioned SWAP and \(W\) real coherent flag rotation, using the original H75 four-Kraus reset. Assume the experiment **independently certifies** (AX-OA) that these already specified unitary operations can be applied in the shown order **BEFORE the reset** on reproducibly prepared copies of the same pre-reset coherent H92-orbit state. H76 used W as a coherent flag-rotation counterexample **outside** its restricted classical-feedback observer catalog; its physical availability and timing as part of this four-setting protocol are additional operational conditions, not consequences of P3 or H76's narrower closure theorem.

Define four **physical six-level** pre-reset words \(G_j\) by the application order
\[
\begin{array}{c|l|c|c}
j& \text{application order (earliest to latest)}&
\operatorname{rank}D_j&
\operatorname{rank}(D_1\oplus\dots\oplus D_j)\\\hline
1&W\ \to F\ \to U_A(1/2)\ \to F&6&6\\
2&F\ \to W\ \to F&4&10\\
3&W\ \to F&4&11\\
4&U_A(1/2)\ \to F\ \to W\ \to F&4&12
\end{array}
\tag{H94-WORDS}
\]
where the real output differential is
\[
\boxed{
D_j(T_\alpha)=
\operatorname{Tr}_E\left[
\Phi_\mu(G_jT_\alpha G_j^\dagger)\right]
\in\operatorname{Herm}_0(\mathbb C^3).
}
\tag{H94-D}
\]
The all-rational 36-output-by-12-input calculation (or a more economical set of 9 qutrit Hermitian coordinate readouts in each setting) gives
\[
\boxed{
\operatorname{rank}
\begin{pmatrix}D_1\\D_2\\D_3\\D_4\end{pmatrix}=12.
}
\tag{H94-IC}
\]
The rank-12 reconstruction uses only **independently prepared state copies** and separate measurement circuits; it is not a single 12D output, a CPTP decoder for an unknown pre-reset quantum state, a code-preserving five-level unitary, an observable canonical momentum map, or a way to transmit 12D coherent phase-space data through an individual destructive reset.

The original qutrit partial trace is the *reduced output* of the genuine six-level H75 CP reset; every one of these four channel maps is a bona fide CPTP map. No isolated implementation of H42 complex \(U\) as a pre-reset gate is presumed; it occurs only inside its original four-Kraus source.

### Positive POVM realization (EXACT conditional on availability of the specified readout)

For the qutrit reduced output \(\rho_{S,j}=\operatorname{Tr}_E\Phi_\mu(G_j\rho G_j^\dagger)\), measure on independent copies the nine positive effects
\[
P_k=|k\rangle\langle k|\ (k=0,1,2),\qquad
Q^{X,+}_{kl}=\frac12(I_3+X_{kl}),\qquad
Q^{Y,+}_{kl}=\frac12(I_3+Y_{kl})
\quad(k<l).
\]
Each \(Q^+\) has spectrum \(\{0,\tfrac12,1\}\) (its negative complementary effect is \(I-Q^+\)); each population \(P_k\) is a projector. Their nine outcome probabilities determine every complex qutrit density matrix, and the four sets of probabilities have Jacobian **rank12** along the H92 Grassmann directions at the physical seed. The checker explicitly audits **genuine positive source-seeded post-gate states**, all probability bounds \([0,1]\), and the exact rank using the true H75 \(\Phi_\mu\).

**This is not a standard-QM-vs-CR discriminator:** it is an ordinary quantum-tomographic separation of distinct *possible* states with an independently permitted experimental schedule, using the fixed H75 conventional CP channel.

## H94.3 — Why the result does NOT overturn H93 (EXACT distinction of quantifiers and objects)

H93 computed the **reachable pure-unitary orbit** from the actual source state under the inherited real gate Lie group \(SO(6)\). Its H92 12-coherence instantaneous readout rank is only 9 and its physical state-tangent intersection with the code-preserving complex Grassmann 12-orbit is dimension 3. The inherited finite gates also leak the 5D source code, all as exact positive-state facts.

H94 asks a **different operational question**: *if* a physically valid but not necessarily otherwise preparable point of the 12D H92 Grassmann orbit is given as the repeated input, can **multiple distinct** existing pre-reset measurement circuits distinguish all its nearby coherent tangent parameters **classically**? The answer is **YES** for the declared 4-setting schedule.

This does **NOT** prove:
1. The actual inherited W/F/U_A/U_B control catalog can prepare an arbitrary H92 Grassmann orbit state from the original H75 source checkpoint seed. H93 proves it cannot span all of that orbit by one uninterrupted real unitary group action.
2. The 12D quantum state survives a single physical reset; it does not, since \(\Phi_\mu(T_\alpha)=0\) and \(\operatorname{rank}D_j\le8\) for every individual setting.
3. The four mutually exclusive readout settings coexist as a single quantum-preserving CPTP inverse. They are separate destructive experiments requiring repeated copies of the *same* initial state and independently certified causal pre-reset access.
4. A code-preserving complex U(5) unitary is generated by composing the H42 complex source \(U\) with the real gates; the source's complex U remains part of **irreversible** \(\Phi_\mu\) and is not an independently available pre-gate.
5. Real canonical 6+6 ADM variables, their symplectic transport, DeWitt negative conformal kinetic direction, off-shell full HDA, or Einstein field equations have been physically sourced.

Thus H94 is a **constructive informational restoration** on a finite observer family, while the stronger **coherent dynamical/canonical restoration remains OPEN**. Tomographic inversion of a multi-experiment classical record does not implement the KKS \(\omega\)-preserving Hamiltonian flow.

## H94.4 — P9/P11 exit decisions

**P9 G3:** Even having local operationally informationally complete H92 KKS readouts is inadequate to establish a **physical symplectic realization** for ADM gravity. The next theorem must exhibit a physically available **source-preserving unitary or channel-family dynamics** with nondegenerate KKS tangent action, a genuine 6+6 observable canonical mapping and a source-derived Hamiltonian/constraint **intertwiner**. H59 global compact-to-exact cotangent No-Go, H61 DeWitt inertia, H83 nonuniform HDA and H90 source-to-spatial-symbol ambiguity still apply. A four-protocol qutrit tomography experiment cannot by itself create ADM.

**P11 AX-OA:** Explicitly distinguish (A) state *preparability*, (B) multi-copy *identifiability*, (C) one-channel *reversible coherent transport*, (D) operational timing and readout causality, and (E) generative selection by F. H93's (A) failure in its restricted Lie group is perfectly consistent with H94's (B) conditional success, and H92's destructive reset excludes (C) for the unchanged unswitched source. The observable quantum memory is not the same object as the source's Hilbert-space capacity.

**Status:** H94.1 reset erasure and reduced-map injectivity **EXACT**; H94.2 four real-gate settings and positive POVM rank12 **CONDITIONAL EXACT**, dependent on independently permitted pre-reset schedule and ability to supply identical orbit-state copies; H93 reachable-KKS obstruction remains **EXACT scoped NO-GO**; truly coherent code-preserving source-generated access, actual KKS→ADM dynamics, DeWitt and Einstein **OPEN**.

**STOPPING RULE:** After audit, do not continue creating arbitrary tomography gate words and label them gravity. H95 should either (i) formulate and test a physical coherent **transport** or KKS–ADM Hamiltonian morphism from declared source data, or (ii) formally close the finite source-specific observation branch and transfer evidence to P9/P11. No human expert peer review, laboratory experiments, Lean theorem, generated Einstein equation, or CR-only physical signature is claimed.
