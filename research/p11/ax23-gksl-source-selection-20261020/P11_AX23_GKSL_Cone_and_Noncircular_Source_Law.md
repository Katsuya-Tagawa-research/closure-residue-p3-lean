# P11–AX23: GKSL source cone, symmetry and non-circular generator selection

**2026-10-20 | Draft on AX22 PR #160, main unchanged.** These are finite algebraic results/known covariance theory, not experimental facts or new quantum-gravity theorems.

## A. From GKSL admissibility to noise covariance
For Pauli operators \(\sigma_j\) and independently specified real symmetric PSD \(C\),
\[
\mathcal D_C(A)=-\frac12\sum_{jk}C_{jk}[\sigma_j,[\sigma_k,A]]
\]
is a legitimate unital GKSL generator, since \(C=\sum_r\lambda_r v_rv_r^T\) yields Hermitian Lindblad operators \(B_r=v_r\cdot\sigma\). The instantaneous noise algebra is the commutant of the \(B_r\) with \(\lambda_r>0\); \(C\) is **not generated from F** by CP positivity.

On Bloch vectors:
\[
\mathcal D_C(a\cdot\sigma)=[-2(\operatorname{tr} C\,I-C)a]\cdot\sigma.
\]
For any \(C=bb^T\ne0\), the kernel is the line \(\mathbb R b\) and the noise algebra is the MASA span\(\{I,b\cdot\sigma\}\). All \(b\) on the unit sphere yield permissible trace-one extreme rank-one covariance rays. Therefore **minimal noise rank + CP + entropy/purity contraction does not choose a canonical pointer axis** (axes related by unitary conjugation are gauge-equivalent without an external reference).

Mixing the \(X\)- and \(Z\)-noise rays gives \(C=(e_Xe_X^T+e_Ze_Z^T)/2\); its Bloch matrix has eigenvalues \(-1,-2,-1\). The resulting noise algebra is just \(\mathbb CI\), despite both components having MASA noise algebras.

## B. Symmetry non-selection
Standard finite covariance classification: a norm-continuous trace-preserving quantum Markov generator covariant under conjugation by every \(U\in U(d)\) is
\[
\mathcal L_\kappa(A)=\kappa(\operatorname{tr}A\, I/d-A),\qquad \kappa\ge0.
\]
The traceless adjoint representation is irreducible and Schur's lemma forces a scalar action there. For \(\kappa>0\), the instantaneous noise algebra is \(\mathbb CI\); for \(\kappa=0\), it is all \(M_d\), so full symmetry does not select a MASA. Nor does it fix the rate \(\kappa\). This is **known representation theory**, cf. Holevo 1993 and the covariant quantum-Markov literature, and is not claimed as a newly discovered theorem.

## C. Same observer does not fix the H37 generator
For the externally specified H37 5-site pointer projectors \(p_j\) and \(\gamma=2/3\),
\[
\mathcal D_{37}(A)=\gamma(\Delta_D(A)-A)
=-\frac\gamma2\sum_{j=0}^4[p_j,[p_j,A]].
\]
It damps *every* \(E_{ij},i\ne j\), by the same \(-\gamma\) rate, while its noise algebra is \(D_5\).

A **single** nondegenerate Hermitian \(B=\sum_i b_i p_i\) has the same noise algebra but instead damps \(E_{ij}\) at rate \(-(b_i-b_j)^2/2\). Three distinct points of a real line cannot have equal positive pairwise distances, so for \(d\ge3\) this cannot equal H37's uniform rate. Recovering the correct MASA does **not** reconstruct the GKSL generator. Similarly rotated noise bases are admissible unless independently fixed.

## D. Evidence and limits
The scope-limited SymPy 1.14 reproducibility program makes **283 exact finite assertions** on qubit covariance matrices, their Bloch actions, extreme rays, mixed noise, 5-site H37 projector structure, single-\(B\) inequivalence, and rotated pointer MASAs. It does not prove a new GKSL classification theorem, physically certify the controls, or prove G2/G3. AX23 does not replace the original P3 \(\mathcal R_k\) by \(E\mathcal LQ\mathcal LE\). P1–P8 frozen papers and main stay untouched.

| Gate | Status |
|---|---|
| Conditional \(C\mapsto\mathcal D_C\), noise algebra and H37 projector construction | EXACT |
| CP and full unitary symmetry canonically select nontrivial pointer source | NO |
| H37 generated from one nondegenerate \(B\) by uniform double-commutator dephasing | NO |
| Independent physical \(C,H\), native inventories (G2) | OPEN |
| Typed non-circular F-origin for \(C,H\) (G3) | OPEN |

**Next AX24:** independently specified source/environment interaction and covariance with traceable approximation hypotheses, then exact same-source P3 filtration and experimental readout gates, or a proof of their impossibility in a stated class.
