# SPS-H120 — Canonical Choi Source and the Physical Primitive Gap

**2026-10-19 • P3–P11 Mathematical Bridge • Independent SPS sequence.** Stacked on SPS-H119 Draft PR #134. This track does not share numbering with H75/P11 H113 (#132).

## H120-A: canonical positive construction (standard Choi–Kraus mathematics)

For finite-dimensional CPTP maps \(\Phi:\mathcal B(H_A)\to\mathcal B(H_B)\), let \(J_\Phi\) denote the Choi operator, with consistent input/output vectorization. Define
\[
\boxed{\mathfrak K(\Phi)=\operatorname{unvec}(\operatorname{Ran}J_\Phi)
 =\operatorname{span}_{\mathbb C}\{K_\alpha:\Phi(\rho)=\sum_\alpha K_\alpha\rho K_\alpha^\dagger\}.}
\]

**Proof:** Writing \(B=[\operatorname{vec}K_1\ \cdots\ \operatorname{vec}K_r]\), \(J_\Phi=BB^\dagger\). Over \(\mathbb C\), \(\operatorname{Ran}BB^\dagger=\operatorname{Ran}B\). Thus this operator subspace is independent of Kraus-list choice, and its dimension is the Choi rank.

**Composition and tensor product:** If \(\Phi,\Psi\) are composable, the product Kraus family \(\{B_\beta A_\alpha\}\) represents \(\Psi\circ\Phi\), and the tensor family \(\{A_\alpha\otimes B_\beta\}\) represents \(\Phi\otimes\Psi\). Hence
\[
\mathfrak K(\Psi\circ\Phi)=\operatorname{span}\{BA:B\in\mathfrak K(\Psi),A\in\mathfrak K(\Phi)\},
\quad \mathfrak K(\Phi\otimes\Psi)=\mathfrak K(\Phi)\otimes\mathfrak K(\Psi),
\quad \mathfrak K(\mathrm{id})=\mathbb C I.
\]
Under input/output unitary change of frame, \(\mathfrak K(\operatorname{Ad}_U\circ\Phi\circ\operatorname{Ad}_{V^\dagger})=U\mathfrak K(\Phi)V^\dagger\). Thus \(\mathfrak K\) defines a composition/tensor-respecting functor to the category of complex operator subspaces, with composition given by span of operator products and canonical Hilbert tensor coherence. This is a **standard channel-level construction**; not an original physical source axiom.

## H120-B: information and provenance gaps

**Nonfaithfulness:** For \(0<q<1\), the dephasing channels
\[
\Phi_q(\rho)=q\rho+(1-q)\Delta_D(\rho)
\]
all have the same \(\mathfrak K(\Phi_q)=D_2\), even though their off-diagonal outputs differ. The canonical space alone does not reconstruct the map.

**H119 observer-fibre example:** The two distinct joint sources \(H_Z=X_A\otimes Z_B\) and \(H_X=X_A\otimes X_B\), when \(B\) initially has \(I/2\), produce the identical one-interval reduced channel on \(A\):
\[
\Psi_t(\rho)=\cos^2 t\,\rho+\sin^2 t\,X_A\rho X_A.
\]
For \(\sin t\cos t\neq0\), the Choi support is exactly \(\mathfrak K(\Psi_t)=\operatorname{span}_{\mathbb C}\{I_A,X_A\}\) (rank 2). The joint unitary channels and their pointer-supported joint sources remain different. This does **not** imply equality of full multi-time process tensors or access to environment-resolved controls.

**Failure to preserve static locality from a single finite-time channel:** On a three-site chain set \(H=X_{01}+X_{12}\), \(H^3=2H\). At \(t=\arccos(3/5)/\sqrt2\),
\[
U_t=e^{-itH}=I-\frac{2\sqrt2}{5}iH-\frac15H^2,\qquad (U_t)_{02}=-\frac15.
\]
All 9 entries of \(U_t\) are nonzero. Hence for diagonal-bimodule closure \(B_D\),
\[
\dim_{\mathbb C}B_D(\{H\})=4,\quad
\dim_{\mathbb C}B_D(\mathfrak K(\operatorname{Ad}_{U_t}))=9,
\]
although the unitary channel has Choi rank 1. The local *infinitesimal generator* cannot simply be replaced by the support of a finite-time channel. This does not forbid generator recovery with a known full time-labelled semigroup and appropriate assumptions.

## Verdict

- **EXACT / standard:** Kraus span is canonical and respects composition, tensor, and unitary-frame covariance.
- **EXACT limited No-Go:** This functor is nonfaithful, does not invert observer reduction, and does not automatically preserve the locality of a generator.
- **OPEN:** Relation of \(\mathfrak K(\Phi)\) to the *physical* native source \(S_{\rm static}\), H37's independently actuated controls, AX-ORIGIN from F, P6 physical gate, P9 Einstein/ADM/HDA and P11 Generative Completeness.
- **STOP:** Do not relabel the intrinsic Choi source as a physically certified \(J_N\) or primitive generator. Do not create more arbitrary H37 static sectors. Candidate SPS-H121 is an *infinitesimal* Choi/noise tangent with explicit native-control caveats.

## Reproduction and review

Full independent 51-check SymPy verification was executed in the current research environment. The repository includes its own reproducible finite audit and CI; all categorical/analytic proofs here are on paper, not Lean-verified. Human peer review and physical validation have not occurred.

Background (not priority claims): *Choi representation of completely positive maps in brief*, Z. Naturforsch. A (2024), DOI 10.1515/zna-2024-0144; QuTiP superoperator/vectorization documentation.
