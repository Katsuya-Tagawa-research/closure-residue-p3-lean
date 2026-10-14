# P9 H33 — Locality obstruction and the missing P3-Krylov-to-P6-microscopic-sector axiom

**Date:** 2026-10-14. Independent exact-rational finite audit candidate, stacked on H32 Draft PR #50. Original P3 and frozen P6 manuscripts unchanged; main untouched. **No Lean kernel proof, no human peer review, no verified P6 hardware access, no P7/P8 metric soldering, and no Einstein dynamics.**

## 1. What the actual frozen P6 v9.1 text assumes

In P6, the microscopic input \(\mathcal J_N\) inherited from the preceding static CR theory is an **independently fixed** uniformly local operator sector satisfying \(\mathcal J_N\subseteq\mathcal A_N^{[\le r_0]}\), for a declared finite locality radius \(r_0\). P6 defines
```math
\Xi_N(J)=(1-\Delta_D)(J-J^\dagger),
\qquad
\mathfrak R_N^{(1)}
=\{\operatorname{ad}_{\Xi_N(J)}|_{D_N}:J\in\mathcal J_N\}.
```
Its First-Residue Accessibility is explicitly a **hypothesis** about each tangent of the independently declared physical/target coherent-control manifold. It is *not* a theorem identifying \(\mathcal J_N\) with an arbitrary observable Krylov sector \(\mathcal H_k\) of a CPTP channel. Also \(\Xi(\mathcal J_N)\subseteq\mathsf{CRControl}(G^{\rm CR})\) is an inclusion, not surjectivity onto all graph-supported directions.

H32 made the transparent, *conditional* choice \(J_{\rm candidate}=\mathcal H_3\) for its connected three-site CPTP channel, verifying \(\operatorname{rank}_{\mathbb R}\Xi(\mathcal H_3)=6\) and original P3 quadratic residue \(\mathcal R_3=D_3^0\). H33 audits whether that choice is compatible with P6's own independent *locality* requirement, for the **nearest-neighbor path 0–1–2** with \(r_0=1\).

## 2. A sharp locality No-Go within the already audited H32 witness

Use H32's exact rational connected single-Kraus CPTP channel \(\Phi(A)=U_3AU_3^\dagger\) and the genuine P3 first Krylov-hidden operator
```math
h=Q\Phi(E_{00}),\quad Q=1-\Delta_D.
```
Its \(0,2\) entry is precisely
```math
h_{02}=\frac{-4+8i}{27}\ne0.
```
On the path 0–1–2, the graph distance is \(d(0,2)=2\). Consequently \(h\notin\mathcal A_3^{[\le1]}\), so \(\mathcal H_1\) and every \(\mathcal H_k\) containing it fail the **radius-one** P6 microscopic locality condition. In particular,
```math
\boxed{r_0=1\ \Longrightarrow\
\mathcal H_3^{\rm P3}\not\subseteq\mathcal J_3^{\rm P6}
\subseteq\mathcal A_3^{[\le1]}.}
```
This is a *specific* no-go: if P6's spatial metric/support is taken to be the path graph with radius one, full direct inheritance of H32 \(\mathcal H_3\) into its fixed sector is impossible, regardless of \(\mathcal J_3\)'s finer definition. This does **not** exclude \(r_0\ge2\), choosing another physical graph (e.g. complete triangle), or a different microscopic \(\Phi\). Those require independently justified model choices.

## 3. A more economical, but conditional, local-algebra bridge

Define a purely **linear** nearest-neighbor support projection \(P_{\le1}\) on offdiagonal operators by dropping the \(02\) and \(20\) entries, while retaining the \(01,10,12,21\) entries. Let
```math
J_k^{\rm loc}:=\operatorname{span}_{\mathbb C}
\{P_{\le1}h_j^{(m)}:1\le j\le k,\ m=0,1\}.
```
Exact computations of the P6-type real-linear images give
```math
\boxed{
\dim_{\mathbb R}\Xi(J_1^{\rm loc})=2,\qquad
\dim_{\mathbb R}\Xi(J_2^{\rm loc})=4,\qquad
\dim_{\mathbb R}\Xi(J_3^{\rm loc})=4.}
```
At depth two, this equals the entire **four-real-dimensional nearest-neighbor** graph-internal space. It therefore includes P6's original \(A_{01}, B_{12}\) and H30's added \(Q_{01}\) (and \(Q_{12}\)) as algebraic operator directions, but **not** an independent instantaneous \(02\) chord. This is an explicit sufficient **candidate**:
```math
\Xi(J_2^{\rm loc})
=\mathsf{CRControl}(0-1-2)
\quad\text{(for zero-diagonal anti-Hermitian operators).}
```
It is not derived that P6's frozen \(\mathcal J_N\) contains \(J_2^{\rm loc}\). If one independently assumes \(J_2^{\rm loc}\subseteq\mathcal J_3^{\rm P6}\) (or only the weaker image inclusion \(\Xi(J_2^{\rm loc})\subseteq\Xi(\mathcal J_3^{\rm P6})\)), then the **algebraic derivation** accessibility of the corresponding declared controls follows from P6's definitions and MASA rigidity. It does **not** make these controls hardware-accessible; the physical control tangent remains an additional calibrated input.

This choice would preserve radius-one operator locality **at the static-sector level** but need not be invariant under the same microscopic \(\Phi\), and hence is not automatically a dynamically inherited CR sector.

## 4. Same connected CR support graph is insufficient even if locality holds

Let \(E_{jk}=|j\rangle\langle k|\). Consider two independent static candidate microscopic sectors supported on the *same* two-edge graph:

- **Locked sector:** \(J_{\rm lock}=\operatorname{span}_{\mathbb C}\{E_{01}+E_{12}\}\).
- **Unlocked sector:** \(J_{\rm free}=\operatorname{span}_{\mathbb C}\{E_{01},E_{12}\}\).

Both have radius-one support with both edges \(01\) and \(12\) present in the microscopic support graph. But
```math
\dim_{\mathbb R}\Xi(J_{\rm lock})=2,
\qquad
\dim_{\mathbb R}\Xi(J_{\rm free})=4.
```
In the locked sector, the two edges always occur in a coupled ratio; neither individual P6 path edge nor H30's quadrature is independently selectable from the two-dimensional image. In the free sector, all four nearest-neighbor coherent quadratures are available **as algebraic elements**.

**Conclusion:** matching the graph support, graph connectivity and finite radius **does not suffice** for first-residue control provenance. One needs image/rank information and a justified microscopic sector, not just a drawn CR edge graph.

## 5. A serious physical implementation warning: support truncation is not CP

The full diagonal-preserving nearest-neighbor Schur mask for the path is
```math
M=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}.
```
Applying it entrywise to the **positive** pure state \(\rho=\frac13\mathbf1\mathbf1^T\) produces \(M/3\). For \(v=(1,-1,1)^T\),
```math
v^T (M/3)v=-\frac13<0.
```
Thus this Schur projection is **not even a positive map**, and cannot be a CPTP quantum channel. Its restriction to an operator *vector space* is a legitimate algebraic support selection, but physically realizing a truncation requires a different, independently justified CP operation or microscopic restriction. **Do not silently interpret \(P_{\le1}\) as an observer measurement, admissible dissipator, or quantum preparation.**

## 6. Exact conditional First-Residue Accessibility criterion

For a MASA D_N, the restriction of \(\operatorname{ad}_K\) to D_N determines every **offdiagonal** matrix entry of K. Thus for anti-Hermitian traceless offdiagonal coherent generators \(K_X\) and \(\Xi(J)\):
```math
\operatorname{ad}_{K_X}|_{D_N}
=\operatorname{ad}_{\Xi(J)}|_{D_N}
\iff K_X=\Xi(J).
```
For arbitrary K with diagonal terms, equality holds iff \(K-\Xi(J)\in D_N\) (the population gauge). Therefore the **precise algebraic** condition for a proposed control-tangent space T is
```math
Q(T)\subseteq\Xi(\mathcal J_N)
\quad\text{(assuming T is a real-linear family of anti-Hermitian controls).}
```
This is a criterion on an *independently fixed* microscopic sector, not a consequence of \(\mathcal R_3=D_3^0\), full H32 Krylov rank, or a connected graph alone.

## 7. H33 status and downstream scope

The finite mathematical outcome is **No-Go + conditional repair**:
1. Full H32 Krylov sector violates nearest-neighbor r0=1 locality already at depth1; it cannot be directly identified with P6's r0=1 J_N.
2. The purely algebraic radius-one projected candidate has rank4 by depth2 and can supply every path-edge coherent quadrature **if declared as a legitimate microscopic input**.
3. Identical two-edge support graphs can give Xi ranks2 versus4.
4. The local Schur projection is not CP; no physical projection is constructed.
5. The missing assumption is an independently inherited \(\mathcal J_N\) with sufficient Xi image, followed by actual physical coherent-control calibration and dissipative compatibility.

No H33 result proves that the required microscopic sector is uniquely dictated by P3/P4, that a physical CPTP pulse implements the linear truncation, that H28 static four-phase scan is available, or that microscopic U(1)/SU(3) holonomy is Lorentzian/Levi-Civita/Regge curvature. B14/B15/B17 and Einstein dynamics remain open.

**Suggested next gate H34:** Determine whether \(\Phi\)-invariance and radius-one locality can coexist with the desired nontrivial Krylov-derived Xi image; if not, prove the minimal invariant operator-sector radius or a finite invariant-subspace obstruction. Also separate \(\Phi\)-invariant *operator systems* from arbitrary linear subspaces before any dynamical/physical interpretation.

## Reproduction

`P3/P9H33LocalityXiProvenanceExactCheck.py` imports the H32 connected unitary CPTP witness and implements exact rational-Gaussian ranks, target-matrix membership, locked/unlocked two-edge sectors, and an explicit negative-expectation witness for Schur-mask nonpositivity. CI audits these exact identities; no numeric tolerances, Lean or experimental realization is claimed.
