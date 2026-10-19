# H110 — Exact One-Step Stinespring Realization, Fresh-Ancilla Repetition, and a Finite Closed-Memory No-Go for the Original H75 CPTP Source

**2026-10-19 | P3–P11 Mathematical Bridge and P9 conditional GR, with P5 history relevance | Route A.**

**Inherited:** H109 Draft PR #128 (100/100 GitHub CI PASS). Original physical-mathematical H75 six-level CPTP source, actual four Kraus operators, real A/B controls, positive site/flag observers, original nonzero P3 quadratic signed \(R_3\), and published/frozen P1–P8/main are UNCHANGED. P9.126–127 physical-mathematical source is a separate specified 16-level unitary Hamiltonian, P9.128 a separate specified 48-level unitary register Hamiltonian. No identification of their operator algebras, observer, or Cartan solder is assumed.

## H110 question: does an exact finite unitary one-step dilation imply coherent P9 transport of arbitrary H75 measurement histories?

**No.** The answer separates two different source/memory permissions, each with an exact theorem.

### H110.1 — One-step minimal pure-environment Stinespring isometry (EXACT POSITIVE)

Use the *actual* H75 source \(\mathcal H_S=\mathbb C^6\) and its four unchanged Kraus matrices
\[
L_{ab}=|a\rangle\langle b|_{\mathrm{flag}}\otimes U M_a,\quad
a,b\in\{0,1\},\quad
M_0=\operatorname{diag}(1,3/5,3/5),\
M_1=\operatorname{diag}(0,4/5,4/5).
\]
Define a separate four-dimensional pure environment \(\mathcal H_E=\mathbb C^4\) with orthogonal labels \(|ab\rangle\), and the exact \(24\times6\) isometry
\[
\boxed{
\mathsf V|\psi\rangle=\sum_{a,b=0}^1 L_{ab}|\psi\rangle\otimes|ab\rangle_E.
}
\tag{H110-V}
\]
By \(\sum_{ab}L_{ab}^\dagger L_{ab}=I_6\),
\[
\boxed{\mathsf V^\dagger\mathsf V=I_6,\qquad
\operatorname{Tr}_E(\mathsf V X\mathsf V^\dagger)
=\Phi_{\rm H75}(X),\quad\forall X\in M_6.}
\tag{H110-STEP}
\]
The exact checker verifies both identities on **all 36** original six-level matrix units, using Gaussian-rational coefficients in the genuine H75 matrices. A \(24\times24\) unitary extension \(W\) exists by completing the six orthonormal columns of \(\mathsf V\) to an orthonormal basis; \(W(|\psi\rangle\otimes|0_E\rangle)=\mathsf V|\psi\rangle\) under the usual input-ancilla identification. This is a **mathematically constructive existence** proof, not an independently calibrated physical gate or an identification with the P9 Cartan Hamiltonian.

The four original Kraus operators are complex-linearly **independent**: they occupy disjoint flag output/input blocks \((a,b)\); all four are nonzero. Their exact Hilbert–Schmidt Gram matrix is diagonal
\[
\boxed{
\operatorname{Gram}(L_{00},L_{01},L_{10},L_{11})
=\operatorname{diag}(43/25,43/25,32/25,32/25).
}
\tag{H110-CHOI}
\]
Therefore the original six-level H75 channel has **Choi rank exactly four**, and the four-dimensional pure Stinespring ancilla is **minimal for ONE update** in the standard system⊗pure-environment tensor model. The resulting total Hilbert dimension \(6\times4=24\) is only a mathematical workspace bound. It is NOT the 16/48 P9 micro source, and a larger P9 Hilbert dimension by itself does not source the H75 Kraus dilation.

### H110.2 — Fresh environment copies simulate any FIXED finite horizon (EXACT POSITIVE with INDEPENDENT fresh-ancilla supply)

With a newly prepared and discarded four-level ancilla at each time step, define an \(n\)-step isometry
\[
\boxed{
\mathsf V_n|\psi\rangle
=\sum_{k_1,\ldots,k_n\in\{00,01,10,11\}}
\big(L_{k_n}\cdots L_{k_1}\big)|\psi\rangle
\otimes|k_1\rangle\otimes\cdots\otimes|k_n\rangle.
}
\tag{H110-HISTORY}
\]
It satisfies
\[
\boxed{
\mathsf V_n^\dagger\mathsf V_n=I_6,\qquad
\operatorname{Tr}_{E_1\cdots E_n}(\mathsf V_n X\mathsf V_n^\dagger)
=\Phi_{\rm H75}^n(X).
}
\tag{H110-ITER}
\]
The checker audits the operator-sum completeness of \(\mathsf V_n\) for \(n=1,2,3\), the all-36 matrix-unit equality for \(n=1,2\) and independent finite-horizon source state evolution at \(n=3\). General \(n\) is a simple exact induction using completeness of each original Kraus family. The allocated environment Hilbert dimension \(4^n\) is a **sufficient explicit history-register construction**, NOT a claimed minimum memory dimension for the reduced \(n\)-step channel (Kraus compositions can become linearly dependent).

This is an allowed **mathematical time-dependent ancilla supply/refresh process**, not a derivation of fresh environments, absolute time, irreversible resource replenishment, or P5 non-Markovian Ω from the original F map. A single physical source must additionally explain where the independent fresh ancillas come from and why their preparation is permitted.

### H110.3 — NO-GO: one fixed finite-dimensional CLOSED memory plus one fixed unitary cannot reproduce all H75 iterates (EXACT, scoped)

Suppose there exist ANY finite-dimensional environment \(\mathbb C^d_E\), ANY fixed initial density \(\eta_E\) (mixed allowed), and ANY one fixed unitary \(W\in U(6d)\), with no reset, no external intervention, no replacement ancilla and no measurement-conditioned classical feedback, such that
\[
\boxed{
\operatorname{Tr}_E\bigl[W^n(\rho\otimes\eta_E)(W^\dagger)^n\bigr]
=\Phi_{\rm H75}^n(\rho),\quad \forall \rho\in\mathcal S(\mathbb C^6),\ \forall n\ge0.
}
\tag{H110-CLOSED}
\]
H109 proved **primitive mixing**
\[
\Phi_{\rm H75}^n(\rho)\longrightarrow
\sigma_*=\mathcal J_U(I_3/3),\qquad n\to\infty
\]
for every original H75 positive density \(\rho\), with nontrivial positive inputs \(\rho\ne\sigma_*\).

But in a **fixed finite-dimensional closed** system, the adjoint dynamics of \(W\) is recurrent: since \(W\) has finitely many eigenphases, there exists a sequence of positive integers \(n_j\to\infty\) with \(W^{n_j}\to I\) in operator norm (simultaneous recurrence of a finite torus rotation). For every \(\rho,\eta_E\), continuity of conjugation and partial trace gives
\[
\operatorname{Tr}_E[W^{n_j}(\rho\otimes\eta_E)(W^\dagger)^{n_j}]
\longrightarrow\rho.
\]
If (H110-CLOSED) held, the same sequence would converge to \(\sigma_*\) by primitive mixing. Choosing \(\rho=|0_E,0_S\rangle\langle0_E,0_S|\) (positive true original 6D seed) gives \(\rho\ne\sigma_*\). **Contradiction.** Even restricting to \(n\ge1\) rather than \(n\ge0\), recurrence near the first iterate forces that iterate to equal the stationary limit, which it does not.

\[
\boxed{
\text{No finite }d,\ \text{fixed }\eta_E,\ \text{fixed closed }W
\text{ exactly realizes all original H75 iterates without refresh.}
}
\tag{H110-FINITE-NOGO}
\]
The result does not depend on the particular dimension \(16\) or \(48\). Thus P9's 16/48-dimensional *closed, fixed-Hamiltonian* microscopic unitary evolution cannot realize **the entire indefinitely iterated H75 reset process via a fixed factor-subsystem reduction with a one-time initial ancilla and no external refresh**. P9's actual physical Cartan model is different already at one step; this theorem does NOT discredit its independent Hamiltonian, register or finite holonomy calculations.

The proof also holds for a FIXED initial assignment \(\rho\mapsto\xi_\rho\) in the same finite closed carrier whenever the reduced initial state is \(\rho\) and the full evolution for that prepared joint state follows one time-independent unitary. It does NOT say that every open quantum process requires an infinite environment for ONE timestep: H110.1 explicitly proves the opposite.

**Scope exclusions:** a genuinely increasing fresh-ancilla chain, a continuum bath, externally refreshed finite ancillas (nonclosed dynamics), time-dependent controls, intermediate selective measurements, nonlinear/postselected state updates, approximate finite-horizon simulation, or a changed restricted/noiseless source sector. The theorem forbids **exact indefinite repetition of H75's mixing map by one initially finite closed quantum memory under one fixed unitary**, and nothing broader.

### H110.4 — A precise P5 Ω / P9 / P11 typed handoff

**P5-history/Ω:** Every finite horizon \(n\) has a finite Stinespring history register; unbounded horizons can be modeled with fresh ancillas or another explicitly sourced bath/measurement mechanism. This is a mathematically exact **history-resource distinction**, NOT a derivation of “the infinite” from finite F, the Born interpretation, or an actual non-Markovian backflow theorem. Repeated H75 CPTP is Markovian at the reduced source level by construction, even when a coherent dilation retains environment records; do not equate environment memory storage with a proven observable non-Markovian process.

**P9 AX-CAN / AX-SP:** A 24D one-step dilation does not generate a Hamiltonian KKS↔ADM canonical transport. The original H75 long-time channel destroys all traceless coherent source directions, and a bare fixed closed finite unitary model cannot reproduce its indefinitely refreshed measurements. Any physical common P9 Cartan/H75 model needs explicit **system/environment factorization, bath-state preparation, time-step collision law, observer transport, Hamiltonian/control source, and actual solder**. Merely embedding dimensions (e.g., 48≥24) or mentioning a formal Stinespring unitary cannot satisfy those conditions.

**P11 AX-SRC / AX-OA / AX-GEN:** Distinguish: (a) finite 4-dimensional pure ancilla is EXACT for ONE original H75 reset; (b) \(4^n\) fresh-history space is a SUFFICIENT conditional implementation for n resets; (c) fixed finite closed environment + identical unitary + no refresh is IMPOSSIBLE for all n; (d) independent physical justification of fresh ancilla supply, correlated histories, observer algebra and F generative completeness is OPEN. None of these establishes sourced Einstein action, off-shell HDA, physical Newton scale, torsion-free Cartan selection, or physical GR empirical equivalence.

**Stop rule:** H111 should examine ONLY a physically justified change of the model category (fresh-ancilla collision mechanism, observable-sector restriction, actual sourced P9 open reduction), with quantified environment preparation and source Hamiltonian. Do not infer universal gravity from a unitary dilation or invent another arbitrary entangling K4 edge. All PRs Draft/unmerged, no human referee or experimental claim, original frozen P1–P8 untouched.
