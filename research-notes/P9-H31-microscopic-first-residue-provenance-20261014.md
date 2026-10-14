# P9 H31 — Microscopic first-residue provenance: a nonzero P3 residue does not force a connected control graph

**2026-10-14.** Finite exact-rational audit candidate stacked on H30 Draft #48, before any merge/freeze. It treats the **original P3 quadratic residue** and P6's **microscopic first-residue extraction** as distinct constructions. Not a proof that the frozen P6 `J_N` equals a P3 Krylov hidden sector; the explicit J choice here is a *declared candidate* for a controlled comparison. Not actual physical control/measurement permission, Levi-Civita/Regge curvature, Einstein dynamics, or a CR-exclusive prediction.

## 1. Audit against the P6 v9.1 original mathematical gate

P6 defines a microscopic sector `J_N` inherited from prior static CR theory, together with
```math
\Xi_N(J)=(1-\Delta_D)(J-J^\dagger),\quad
\mathfrak R_N^{(1)}
=\{\operatorname{ad}_{\Xi_N(J)}|_{D_N}:J\in J_N\}.
```
The physical declared control tangent is required by **First-Residue Accessibility** to belong to these inherited derivation directions modulo diagonal gauge. P6 also proves `Xi_N(J_N)⊂CRControl(G_CR)`. **This is an inclusion**, not a proof that every graph-supported complex quadrature, every graph edge, or every Lie-synthesized bracket is physically addressable.

Its concrete three-site path benchmark independently declares only two *real* anti-Hermitian exchange controls: A=E01−E10 and B=E21−E12. H30 showed that adding a **third, new 01-edge quadrature** Q01=−i(E01+E10) gives su3 Lie closure *if all three are permitted*. H31 tests what an actual original-P3 microscopic witness does and does not supply.

## 2. Construct a three-site unitary CPTP witness with genuine nonzero P3 quadratic residue

Embed H24's rational-Gaussian two-site unitary with a spectator third site:
```math
U_3=\begin{pmatrix}
(1-2i)/3&-2i/3&0\\
-2i/3&(1+2i)/3&0\\
0&0&1
\end{pmatrix},\quad
\Phi_3(A)=U_3 A U_3^\dagger.
```
This is an exact three-site unitary single-Kraus CPTP channel. With D3 the diagonal algebra and Z=E00−E11, its first two original-P3 Krylov hidden operators are h1=Q Phi3(Z), h2=Q Phi3²(Z), precisely the 3x3 zero-padded H24 h1,h2. The original P3 quadratic residue is
```math
\Delta_D([h_1,h_2^\dagger])
=\tfrac{128i}{81}(E_{00}-E_{11})\ne0.
```
The original P3 depth indexing i+j gives the first nonzero return at k=3; its residue has **rank one inside the two-dimensional traceless diagonal D3^0**. Unlike the H24 two-dimensional D2^0, it does **not** saturate D3^0.

Crucially, all hidden Krylov operators, at every depth for this Phi3 and initial D3, have only 01 support. The spectator 2 remains dynamically decoupled; the P3 residue cannot produce a 12/02 microscopic edge by itself.

## 3. A concrete candidate microscopic J_base extracted from P3 has Xi rank two only

Declare, specifically **for this comparison**, `J_base:=span_C{h1,h2}`. Its offdiagonal operators have 01 support; h1 and h2 are complex-linearly independent. P6's real-linear Xi sends J_base into all anti-Hermitian offdiagonal generators on that edge:
```math
K_1=\Xi(ih_1/2)=ih_1,\quad K_2=\Xi(ih_2/2)=ih_2,
\quad\mathrm{rank}_{\mathbb R}\Xi(J_{\rm base})=2.
```
In particular, both A01=E01−E10 and Q01=−i(E01+E10) belong to the real Xi image, but the **12-edge** B12=E21−E12 does not. The generated Lie algebra is the embedded local su(2) on sites 0,1:
```math
\operatorname{Lie}_{\mathbb R}\{K_1,K_2\}
=\mathfrak{su}(2)_{01},\quad\dim_{\mathbb R}=3.
```
The exact diagonal bracket reproduces the **original** P3 quadratic residue up to sign, but it cannot couple the spectator third site.

Thus a nonzero genuine P3 residue, even together with a 2-real-dimensional Xi image including both 01 quadratures, **does not force** P6's desired connected two-edge path or a triangular H28 flux. This is a scope-restricted finite counterexample; it does not imply that all P3 systems have disconnected closure supports.

## 4. Conditional positive augmentation and missing physical provenance

If one independently adds **one extra microscopic 12-edge direction**, e.g.
```math
J_{\rm aug}
=J_{\rm base}+\operatorname{span}_{\mathbb C}\{B_{12}/2\},\quad
\Xi(B_{12}/2)=B_{12},
```
then `Lie_R{K1,K2,B12}=su(3)`: an exactly computed eight-dimensional real Lie closure. This recovers the *algebraic* H30 setting without changing the original spectator CPTP map used to calculate P3's residue.

This is explicitly a **new microscopic-sector assumption**, not a consequence of the block-diagonal original P3 dynamics. In particular, the original P6 physical two-real-edge control benchmark supplies B12 but not a calibrated complex 01 quadrature; the chosen H24 microscopic Krylov sector supplies complex 01 but not B12. Their combination must not be described as already inherited from either separately.

Moreover, su3 Lie generation is not H28's directly calibrated time-independent four-phase Hamiltonian scan under shared GKSL dephasing. The latter also requires validated pulse synthesis or additional independent static controls. No added microscopic edge is inferred to be hardware addressable solely from Xi inclusion.

## 5. Exact nontrivial theorem and next physical gate

**H31 finite No-Go (precise scope):** There exists a three-site unitary CPTP channel with nonzero *original* P3 depth-three quadratic residue and a concrete P3-hidden-derived candidate microscopic sector J_base such that Xi(J_base) has nonzero complex 01-edge control quadratures but its real Lie closure acts trivially on site 2. Consequently neither a connected P6 control graph nor an H28 triangular flux follows from (i) nonzero P3 residue, (ii) local Xi accessibility to J_base, and (iii) graph-internal Lie closure alone.

**H31 conditional construction:** independently appending a 12-edge microscopic lift is enough for su3 Lie closure algebraically. The missing derivation is to identify a *single independently fixed* static CR microscopic sector giving both directions, and to prove a physical control interface to the actual declared P6 coherent manifold. The construction here **does not** assert that J_base is the already frozen J_N in P6.

**Potential next H32:** Construct and audit a genuinely *connected* three-site microscopic CPTP channel (rather than a spectator embedding) whose **original P3** quadratic residue and fixed J_N support both necessary controls; verify whether First-Residue Accessibility follows, is conditional, or fails. Then perform forward-only open-system pulse synthesis tests. Alternatively, if no such microscopic inheritance can be proved, freeze the mathematical bridge with the control-provenance requirement explicitly open.

B14 six-edge physical CR provenance, B15 GKSL CR-specific comparator, B17 physical conjugate-force/variational law, P7/P8 physical soldering, and P9 Einstein dynamics remain open.

## Reproducibility

`P3/P9H31MicroscopicFirstResidueProvenanceExactCheck.py` imports H24 exact rational Gaussian data and checks unitarity of U3, original P3 residual coefficient, real rank of Xi on the chosen microscopic J_base, exact support, local su2 closure, independently augmented su3 closure and P6 baseline path mismatch. Dedicated GitHub Actions runs the script; no floating-point approximations or Lean kernel proof claims.
