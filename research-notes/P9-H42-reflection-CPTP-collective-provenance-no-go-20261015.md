# H42 — A reflection-covariant CPTP channel with saturated genuine P3 residue does NOT force P6 collective provenance

**2026-10-15 | P3–P11 Mathematical Bridge.** Stacked on H41 Draft PR #60. This is an independently reproducible exact finite **No-Go for automatic derivation** of frozen P6 v9.1's collective-mode static sector and physical left/right tangent locking from original P3 diagonal closure–residue data, even adding left/right reflection covariance and maximum diagonal residue rank. Frozen papers/main unchanged; no human peer review, Lean kernel formalization or Einstein dynamics.

## 1. Exact single three-site microscopic CPTP update, chosen before target response

Take sites 0–1–2 and the actual P6 real exchange generator
\[
K=(E_{01}-E_{10})+(E_{21}-E_{12})\in\mathfrak{so}(3),
\]
with the left/right reflection \(P=E_{02}+E_{11}+E_{20}\), so \(PK=KP\). Its **rational Cayley step** (not an exact exponential at a claimed pulse time) is
\[
O=(I+\tfrac12K)(I-\tfrac12K)^{-1}
=\frac13\begin{pmatrix}2&2&-1\\-2&1&-2\\-1&2&2\end{pmatrix}.
\]
It is real orthogonal and reflection-covariant. Add the **reflection-symmetric, externally specified** diagonal phase \(V=\operatorname{diag}(i,1,i)\), and define a *single* rational-Gaussian unitary
\[
U=VO=
\begin{pmatrix}
2i/3&2i/3&-i/3\\
-2/3&1/3&-2/3\\
-i/3&2i/3&2i/3
\end{pmatrix},\qquad
\Phi(X)=UXU^\dagger.
\]
Then \(U^\dagger U=I\), \([U,P]=0\). Therefore the channel is **genuine single-Kraus unital CPTP**, connected and left/right symmetric. Its underlying real Cayley generator K has the nearest-neighbor *path* edge support, but U has a **nonzero finite-step 02 chord**; do **not** infer hard path locality from Cayley generator locality. Likewise the diagonal V is an independently added coherent phase resource, not the frozen P6 two-real-exchange benchmark.

## 2. Actual original-P3 filtration of the FULL diagonal MASA

Use the original P3 observable algebra \(D_3=\operatorname{span}_{\mathbb C}\{E_{00},E_{11},E_{22}\}\), not just the symmetric center seed. Write \(Q=I-\Delta_D\) and
\[
h_j^{(v)}=Q\Phi^j(E_{vv}),\quad
\mathcal H_k=Q\,\operatorname{span}_{\mathbb C}
\{D_3,\Phi(D_3),\ldots,\Phi^k(D_3)\}.
\]
Because \(\Phi\) is unital, \(\sum_vh_j^{(v)}=0\) at each depth. For j=1, exact hidden matrices include
\[
h_1^{(0)}=
\begin{pmatrix}
0&-4i/9&-2/9\\
4i/9&0&-2i/9\\
-2/9&2i/9&0
\end{pmatrix},\quad
h_1^{(1)}=
\begin{pmatrix}
0&2i/9&4/9\\
-2i/9&0&-2i/9\\
4/9&2i/9&0
\end{pmatrix}.
\]
The central hidden operator \(h_1^{(1)}\) is reflection-even and its **nearest-neighbor edge coefficients are locked**. Nevertheless it has a distance-two nonzero 02 entry \(4/9\). Meanwhile the full P3 D3 input also includes a reflection-odd hidden direction
\[
h_1^{(0)}-h_1^{(2)}
=\frac{-2i}{3}(A-B),
\quad
A=E_{01}-E_{10},\ B=E_{21}-E_{12}.
\]
Here the right-hand side is a Hermitian matrix because \((-2i/3)(A-B)\) is Hermitian. The full P3 observer algebra therefore **does not collapse to the reflection-even/collective sector** simply because the microscopic update commutes with reflection.

## 3. Strong test: a SATURATED P3 quadratic residue is still insufficient

Use only the original P3 complex-bilinear projected commutator convention
\[
\mathcal R_k=\operatorname{span}_{\mathbb C}
\{\Delta_D([z,w^\dagger]):z\in\mathcal H_i,\ w\in\mathcal H_j,\ i+j\le k\}.
\]
Exact Gaussian-rational calculations yield \(\mathcal R_2=0\) and two independent legal depth-3 witnesses
\[
r_{00}=\Delta_D([h_1^{(0)},(h_2^{(0)})^\dagger])
=i\,\operatorname{diag}(-32/81,16/81,16/81),
\]
\[
r_{10}=\Delta_D([h_1^{(1)},(h_2^{(0)})^\dagger])
=i\,\operatorname{diag}(40/81,-8/81,-32/81).
\]
These are linearly independent and span the full traceless diagonal space \(D_3^0\), so
\[
\boxed{\mathcal R_2=0,\qquad \mathcal R_3=D_3^0.}
\]
The signed vectors are anti-Hermitian but P3 complex-linear R3 includes all traceless diagonals. Thus the counterexample works even with **genuine nonzero saturated P3 quadratic closure–residue**, not a trivial channel with zero residue.

## 4. Exact failure of original P3 hidden-Xi derivation of collective P6 sector

Frozen P6 first-residue extraction is real-linear
\[
\Xi(J)=Q(J-J^\dagger).
\]
The source P6 static collective sector is
\[
\mathcal J_{\rm col}
=\operatorname{span}_{\mathbb C}\{T,T^\dagger\},
\quad T=E_{01}+E_{21},
\quad
\Xi(\mathcal J_{\rm col})\cap\mathfrak{so}(3)
=\mathbb R(A+B).
\]
But the above *one* reflection-equivariant genuine P3 channel produces the following exact full-diagonal Krylov-Xi real ranks:
\[
\dim_{\mathbb R}\Xi(\mathcal H_1)=2,\quad
\dim_{\mathbb R}\Xi(\mathcal H_2)=4,\quad
\dim_{\mathbb R}\Xi(\mathcal H_3)=5,
\]
and **the rank stays five** for k=4,...,8. Because the full complex superoperator \(\Phi:M_3\to M_3\) acts on a 9-dimensional complex vector space, Cayley–Hamilton guarantees every iterate beyond \(\Phi^8(D_3)\) is a linear combination of earlier iterates. Therefore the stable infinite-depth hidden-Xi image is exactly rank five.

Most importantly, the exact membership checks yield
\[
\boxed{
A-B\in\Xi(\mathcal H_\infty),\qquad
A+B\notin\Xi(\mathcal H_\infty),\qquad
A,B\notin\Xi(\mathcal H_\infty).
}
\]
In particular
\[
\boxed{\mathcal J_{\rm col}\not\subseteq\mathcal H_\infty,\qquad
\Xi(\mathcal J_{\rm col})\not\subseteq\Xi(\mathcal H_\infty).}
\]
Thus direct microscopic-sector identification \(\mathcal J_N=\mathcal H_\infty\), or merely demanding that its Xi image contain the P6 locked tangent, fails even **after adding all three strong premises**: connected finite unitary CPTP dynamics, exact left/right reflection covariance, and saturated genuine P3 quadratic residue.

This is a **counterexample to unconditional logical implication**, not a universal no-go against choosing an additional, independently derived static operator sector or a different microscopic channel.

## 5. Conditional way to manufacture the locked direction, and why it is NOT automatic

From ONLY the central diagonal seed, take \(h=h_1^{(1)}\). Delete its distance-two 02 chord by **purely linear offdiagonal support projection** \(P_{\rm path}\). Then
\[
\boxed{\Xi(iP_{\rm path}h)=-(4/9)(A+B).}
\]
So if one adds an **independent observer selection** that retains only reflection-even center-seed information, plus a static path support extraction and a particular phase conversion before applying Xi, the collective real-skew direction can indeed be obtained.

But these are **new maps/axioms**, absent from the original P3 full-D3 filtration. The nearest-neighbor Schur support truncation is **not a CPTP map** in general (H33 exact nonpositivity witness), and even the one-dimensional projected candidate is **not automatically the full two-complex-dimensional P6 \(\mathcal J_{\rm col}\)**. It gives at most the locked real-skew Xi direction; the other quadrature and independent source-level provenance still require justification.

## 6. Independent physical control families with IDENTICAL microscopic P3 channel

Keep **exactly this fixed U and all its P3 Hk/Rk**. Define two independently admissible standard quantum physical control extensions
\[
\Psi_x^{(a,b)}=\operatorname{Ad}_{e^{x(aA+bB)}}\circ\Phi,\quad x\in\mathbb R.
\]
These are bona fide CPTP families with **identical uncontrolled channel** \(\Psi_0=\Phi\), identical reflection-covariant microscopic P3 data, and the same independently calibrated squared control norm
\[
a^2+b^2=18/25
\]
for the two different control tangents
\[
(a,b)_{\rm lock}=(3/5,3/5),\quad
(a,b)_{\rm unlock}=(3/25,21/25).
\]
Every edge has nonzero amplitude in both families. Their left-minus-right population Hessian from middle seed \(d=E_{11}\), **after the same fixed baseline update Φ**, obeys
\[
\ell_-\,\frac{d^2}{dx^2}\Delta_D\Psi_x(d)\big|_{x=0}
=
\begin{cases}
0,&(a,b)_{\rm lock},\\
288/625,&(a,b)_{\rm unlock}.
\end{cases}
\]
For reference, the P6 intervention Hessian acting directly on d (without the common Φ preparation) gives \(0\) and \(-864/625\), respectively (H41). Neither standard-model control family is selected by the predeclared microscopic Φ data **alone**.

This countermodel proves a **precise missing map premise**: a response-/instrument-compatible **physical tangent provenance map** from an independently justified static microscopic CR sector into the *full physically available coherent control tangent* is essential to derive left/right locking. Graph symmetry of the uncontrolled Φ or the saturation of its P3 residue does **not** supply that map. Even equality of aggregate norms plus a complete common *uncontrolled* channel is insufficient.

## 7. Status, H43 options and non-claims

**PASS exact finite:** connected reflection-covariant unitary CPTP example; original P3 \(\mathcal R_2=0,\mathcal R_3=D_3^0\); parity-even center vs parity-odd full-D3 Krylov; complete infinite-depth Xi rank five excluding P6 locked A+B; two standard CPTP physical control extensions identical in full uncontrolled Φ/P3 data and exact norm with distinct held-out Hessians.

**FAIL as an unconditional implication:** "P3 CPTP + full-diagonal finite CR saturation + reflection symmetry ⇒ frozen P6 \(J_{\rm col}\) or physical locked \(a_L=a_R\)." The displayed one-channel model refutes it.

**CONDITIONAL direction:** center-only observer selection + non-CP support restriction + separately justified Xi phase choice produces a *candidate* locked tangent, but no autonomous CR provenance or physical CPTP realization is proved.

**OPEN:** genuinely independent derivation of \(J_{\rm col}\) from the whole microscopic P3/P4 theory, a star-compatible physical tangent map, micro-to-operational intertwining that forces coherent controls rather than merely conjugating one quantum model, matched Dataset-A-to-B empirical separation, B14/B15/B17, GR/Einstein HDA/ADM.

**H43 prospective gate:** prove a **minimal conditional reflection-equivariant provenance theorem** making the new static selection/polarization and tangent map explicit; alternatively prove impossibility of a covariant, positivity-preserving radius-one truncation that recovers the locked direction *without adding new control data*. Avoid treating observed symmetric response as input to Jcol.

## Exact reproducibility

`P3/P9H42ReflectionCPTPCollectiveProvenanceExactCheck.py` is run by dedicated CI and uses only exact Fraction/Gaussian rationals + proven H32 rank helper. Checks all U/P matrices, full diagonal hidden sectors, P3 original commutator depth indices, Cayley–Hamilton finite-depth stabilization, Xi image membership, and both fully standard CPTP independent control-family Hessians. No floating numerical tolerance, new Lean proof, hardware result, CR-only signal, or physical gravitational curvature claimed.