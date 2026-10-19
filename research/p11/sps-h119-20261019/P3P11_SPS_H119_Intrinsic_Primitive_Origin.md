# SPS-H119 — Intrinsic Primitive Origin and Non-Circular Axiom Test

**2026-10-19; P3–P11 Mathematical Bridge / P11.** This **SPS** sequence is different from the H75-memory P11 H113 of GitHub PR #132. H113–H118 are in stacked Draft PR #133. **H119 status: exact conditional finite theorem and one-time observer counterexample; source origin, physical P6 experiment, and generative completeness are OPEN.**

## 1. Input and targets (do not conflate)

P3 dynamical \(\mathcal H_k(\Phi,D)\), static source \(S_{\rm static}\), static operator sector \(J_N\), physical tangent \(T_0M_N^{\rm phys}\), and Lie-reachable algebra are different data types. A mathematically named control is not an independently certified hardware-native control. No target \(j_{01}\) response may be used to retrofit an origin rule.

## 2. Restricted naturality cannot force a primitive source (THEOREM)

For a finite graph \(G=(V,E)\), choose diagonal vertex projectors \(p_i\) and for each oriented edge \(e=(i,j)\) a nonzero anti-Hermitian matrix \(K_e\) supported precisely on \(ij,ji\). Let the permitted arrows comprise simultaneous diagonal-gauge conjugations of inputs and outputs, edge/vertex relabellings transporting marked data, corner restrictions, and disjoint graph sums. **Not** arbitrary physical CPTP observer reductions or tensor interactions.

Define the anti-Hermitian quadrature
\[
Q_e(K_e)=i(p_iK_ep_j-p_jK_ep_i).
\]
Two rules on precisely the same marked input are
\[
T_{\min}(G,K)=\operatorname{span}_{\mathbb R}\{K_e\},\qquad
T_{\rm quad}(G,K)=\operatorname{span}_{\mathbb R}\{K_e,Q_e(K_e)\}.
\]
They both: contain the marked controls; preserve graph support/locality; commute with simultaneous diagonal gauge and relabellings; respect corner restrictions (edges leaving the subset vanish); and preserve disjoint direct sums. But
\[
\dim_{\mathbb R}T_{\min}=|E|,\qquad \dim_{\mathbb R}T_{\rm quad}=2|E|.
\]

**Proof.** Diagonal unitaries commute with every \(p_i\), whence \(Q_e(UK_eU^\dagger)=UQ_e(K_e)U^\dagger\). Relabelled projectors obey the same formula. A corner restriction either retains both endpoints and both edge operators, or removes their support. Disjoint sums are block sums of the marked operators. For each nonzero skew-Hermitian edge \(K_e=aE_{ij}-\bar aE_{ji}\), \(Q_e=i(aE_{ij}+\bar aE_{ji})\) is an independent real anti-Hermitian quadrature, and distinct edges have disjoint matrix-unit support. QED.

**Actual H37 matrices.** \(E=\{01,12,23,34\}\), \(K_e=E_{e,e+1}-E_{e+1,e}\): ranks are 4 and 8. Previously declared *complex static candidate sectors* are \(J_{\rm mix}\) of rank 5 and \(J_{\rm full}\) of rank 8; these **are not** the same objects as the two real source selections just constructed. \(H_{\rm hop}\) is a baseline drift; it is not silently counted as a native actuator by \(T_{\min}\).

**Meaning.** Even naturality plus these locality/composition constraints does not identify a **physically correct** source selector. Choosing the minimal completion is a convention; postulating native phase quadratures supplies an additional independent physical or axiomatic input. The theorem does not rule out stronger justified P11 source laws.

## 3. Tensor interaction and observer reduction can erase source identity (THEOREM)

Take a fixed factorization of two qubits \(A\otimes B\), with pointer algebra diagonal in the fixed computational product basis, and
\[
H_Z=X_A\otimes Z_B,\qquad H_X=X_A\otimes X_B.
\]
Both are self-adjoint involutions. Their source-operator partial traces over either factor vanish. However their diagonal-bimodule support sectors have complex rank four each and disjoint supports: \(H_Z\) flips \(A\) at fixed \(B\), whereas \(H_X\) flips both factors. They are inequivalent under **diagonal phase gauge and factor-preserving pointer relabellings**.

Prepare the unobserved \(B\) in \(\tau_B=I_B/2\). For every \(t\in\mathbb R\) and every \(\rho_A\),
\[
\begin{aligned}
\Psi_t^{(Z)}(\rho_A)
&=\operatorname{Tr}_B[e^{-itH_Z}(\rho_A\otimes\tau_B)e^{itH_Z}]\\
&=\cos^2(t)\rho_A+\sin^2(t)X_A\rho_AX_A\\
&=\operatorname{Tr}_B[e^{-itH_X}(\rho_A\otimes\tau_B)e^{itH_X}]
=\Psi_t^{(X)}(\rho_A).
\end{aligned}
\]
**Proof.** For either \(P\in\{Z,X\}\), \(H=X\otimes P\) obeys \(H^2=I\), so \(e^{-itH}=\cos t\,I-i\sin t\,H\). Cross terms vanish after tracing \(B\) because \(\operatorname{Tr}(P\tau_B)=0\); the quadratic term reduces to \(X\rho_AX\), since \(P\tau_BP=\tau_B\). QED.

This is **exact equality of all one-time reduced CPTP maps on A for all \(t\)**, not just equality of finitely many population readouts. It does **not** assert equality of complete multi-time process tensors, full joint channels, or experiments that resolve B or intervene on the environment. The joint source matrices and static support sectors remain distinct.

## 4. Bounded source-selection stop (relative mathematical No-Go)

For a weak class of source-expanded models \(\mathfrak P\), let \(\pi:\mathfrak P\to\mathfrak C\) forget unmarked source data, and let \(s:\mathfrak P\to\mathfrak S\) be the *correct* source label modulo an equivalence relation specified before the test. If a fibre contains \(p,q\) with
\[
\pi(p)=\pi(q),\qquad s(p)\ne s(q),
\]
then no exact selector \(f:\mathfrak C\to\mathfrak S\) can satisfy \(s=f\circ\pi\) for the entire weak class. This follows immediately from applying \(f\) to equal inputs (the H117/H118 descent theorem).

In the H37 weak expansion class, different accepted static completions are compatible with the same H37 generator and marked control alphabet. The two-qubit construction gives a separate noninjective *observer-reduced* input fibre even if all **one-interval** times are known. Neither argument proves that *all physical sources* or *full joint microscopic experiments* are indistinguishable.

### Non-circular AX-ORIGIN review gates
1. Specify inputs before collecting target \(j_{01}\) response; do not inject the unknown source into the axiom.
2. Add genuinely independent microphysics or prove a motivated constraint that removes weak same-data completions; a statistic \(a=h\circ\pi\) cannot refine \(\pi\)-fibres.
3. Declare the allowed morphisms: gauge, corners, disjoint sums, tensor composition with or without interactions, and observer reduction are not interchangeable.
4. State whether the output is a phase-fixed matrix, real native tangent space, complex \(J\) sector, or gauge orbit.
5. Obtain independent hardware/source provenance and distinguish actual native actuation from smooth composites and terminal analyzers.
6. Re-test H37 alternative completions and the above observer witness rather than manufacturing more \(J_5\) candidates.

**Decision:** The present bare/marked H37 CR interface does not yet establish a unique physically correct \(S_{\rm static}\). Stop this *abstract selection-without-independent-input loop* until a new independent source axiom or physical evidence exists. P6's physical gate, P9 Einstein/ADM/HDA, and P11 Generative Completeness remain OPEN. Frozen P1–P8 are unchanged.

## 5. Reproduction and provenance

Run \`python -m pip install sympy==1.14.0\` then \`python research/p11/sps-h119-20261019/P3P11_SPS_H119_intrinsic_source_audit.py\`. The audit performs **31 exact finite SymPy assertions** on H37 graph source-rank, gauge/relabel/corner/disjoint-union compatibility and the two-qubit symbolic all-input, all-\(t\) identity. Analytic category/descent statements are proved in this note, not in Lean. Finite CI pass is not physical validation or human expert review.
