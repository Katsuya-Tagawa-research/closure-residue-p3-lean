# P9 H34 — Dynamic-invariance versus bounded-locality obstruction

**2026-10-14.** Exact finite-dimensional H34 audit stacked on Draft H33 PR #51. No claim that the frozen P6 microscopic sector is `Phi`-invariant. This **optional strengthening** is audited explicitly, not silently attributed to P6. The original P3 quadratic-residue and H32/H33 results remain unchanged. No physical pulse-access theorem, Levi-Civita/Regge soldering, Einstein equation, Lean kernel proof or human expert peer review.

## 1. Inputs from the already certified connected CPTP channel

The fixed discrete channel is the actual H32 rational 3-site unitary CPTP map
```math
\Phi(A)=U_3 A U_3^\dagger,\quad
U_3=
\begin{pmatrix}
(1-2i)/3&-2i/3&0\\
(-4-2i)/9&5/9&-2i/3\\
-4/9&(4-2i)/9&(1+2i)/3
\end{pmatrix}.
```
The site geometry is the **path** 0—1—2 with distances d(0,1)=d(1,2)=1 and d(0,2)=2. The complex vector space of all matrices with support distance at most one is
```math
\mathcal O_{\le1}
=\operatorname{span}_{\mathbb C}
\{E_{00},E_{11},E_{22},
E_{01},E_{10},E_{12},E_{21}\},
\qquad\dim_{\mathbb C}\mathcal O_{\le1}=7.
```
This is a **unital, *-closed operator system**, but *not* an associative/C*-subalgebra: E01 E12=E02 is outside O≤1. In general, an operator-system subspace need not be the range of a physically realizable conditional expectation or CPTP projection (H33 proved that the simple Schur mask is not even positive).

## 2. An exact radius-one dynamic closure No-Go

The first Krylov image of the diagonal projection E00 already leaves the nearest-neighbor operator system:
```math
\Phi(E_{00})_{02}=\frac{-4+8i}{27}\ne0.
```
Its second iterate contributes a linearly independent missing chord component:
```math
\Phi^2(E_{00})_{02}=\frac{572+176i}{2187},
\qquad
\Delta_{\rm chord}
=
\Phi(E_{00})_{02}\Phi^2(E_{00})_{20}
-\Phi(E_{00})_{20}\Phi^2(E_{00})_{02}
=\frac{3520i}{19683}\ne0.
```
Modulo \(\mathcal O_{\le1}\), the forbidden coordinates are exactly (A02,A20)∈C², and the two image vectors have nonzero determinant. Hence
```math
\boxed{
\operatorname{span}_{\mathbb C}\{
\mathcal O_{\le1},\Phi(E_{00}),\Phi^2(E_{00})\}
=M_3(\mathbb C).
}
```
Consequently the **smallest complex-linear, *-closed unital, \(\Phi\)-invariant operator system** containing every radius-one operator is **all M3(C)**. Relative to the given path, it has locality radius **two**. This uses only one fixed unitary CPTP channel and exact rational Gaussian arithmetic; no global or continuum claim.

The proof is finite and constructive: O≤1 supplies the diagonal and the four directed nearest-neighbor entries (dimension seven); two iterates give independent coordinates in its two-dimensional chord quotient; full M3 is manifestly \(\Phi\)-invariant.

## 3. Stronger test on only the P6-compatible nearest-neighbor coherent sector

Take the four-dimensional complex offdiagonal path space
```math
\mathcal V_{\rm path}
=\operatorname{span}_{\mathbb C}\{E_{01},E_{10},E_{12},E_{21}\}.
```
This is not an operator system (no identity); it is a complex vector space of traceless matrices. Exact iterative Krylov-style \(\Phi\)-closure has complex ranks
```math
\dim\mathcal V_{\rm path}=4,
\quad\dim\operatorname{span}\{\mathcal V_{\rm path},
\Phi(\mathcal V_{\rm path})\}=7,
\quad
\dim\operatorname{span}_{n\ge0}\Phi^n(\mathcal V_{\rm path})=8.
```
Trace is preserved by \(\Phi\); thus the final invariant space is precisely
```math
\boxed{\operatorname{span}_{n\ge0}\Phi^n(\mathcal V_{\rm path})
=\mathfrak{sl}_3(\mathbb C)}
```
(the eight-complex-dimensional traceless vector space, **not** the anti-Hermitian real Lie algebra su3, though a relation exists under an additional real-structure restriction).

Likewise the H33 candidate nearest-neighbor projection of the original H32 hidden Krylov images at depths ≤2 spans exactly V_path as a **complex** vector space; its \(\Phi\)-invariant closure is also sl3(C). A simple explicit witness is
```math
\Phi(E_{01})_{02}=\frac8{27}-\frac{2i}{9}\ne0.
```
Therefore, an **invariant complex-linear microscopic sector** containing all of these nearest-neighbor microscopic coherent directions cannot retain strict radius-one locality for this H32 channel.

## 4. Conditional radius-two repair and what it does *not* establish

On this particular three-vertex path the graph diameter is two. Choosing \(r_0=2\) and the full operator system \(M_3(\mathbb C)\) certainly gives a unital *-closed \(\Phi\)-invariant microscopic carrier and allows all six offdiagonal anti-Hermitian Xi directions algebraically. For the traceless part, the natural invariant vector space is sl3(C). This repair says **nothing** about a system-size-independent uniform radius \(r_0=2\) on a growing chain, a well-defined continuum causal cone, experimental control accessibility, or a CR-exclusive prediction.

There is a parallel, purely multiplicative obstruction even without dynamics: an associative operator algebra that contains the individual directed 01 and 12 matrix units must contain E02=E01 E12; hence it cannot remain the strict 7-dimensional radius-one vector space. This must **not** be conflated with the weaker operator-system or P6 static-microscopic-sector notion.

## 5. Exactly what P6 does and does not assume

P6 v9.1 specifies the inherited static sector \(\mathcal J_N\subseteq\mathcal A_N^{[\le r_0]}\), defines first-residue \(\Xi(J)=(1-\Delta_D)(J-J^\dagger)\), and imposes a separate **First-Residue Accessibility hypothesis** on a declared physical coherent control tangent. **It does not assume \(\Phi(\mathcal J_N)\subseteq\mathcal J_N\) for this arbitrary H32 microscopic channel.**

Thus H34 is **not** a contradiction of, a flaw in, or a refutation of P6. It answers an extra bridging question:
> If one tries to identify the static microscopic CR sector with a *dynamically inherited, \(\Phi\)-invariant* space containing all nearest-neighbor control quadratures, can it also stay at radius one?

For H32's connected channel, the exact answer is **no**. A bridge must either avoid imposing strong invariance of the same finite local operator sector, allow larger/soft locality, choose a different microscopic dynamics with a compatible sector, or clearly distinguish the static P6 input from the dynamically generated infinite/history shadow of P3/P5.

## 6. Consequences for the next gate

The rigorous finite dichotomy is:
- **Static, radius-one P6 candidate:** can contain four independent path coherent quadratures (H33) but is not \(\Phi\)-invariant for the specified H32 evolution.
- **Dynamically invariant space for H32:** must include the chord, and the minimal unital operator-system closure equals M3(C) (radius two).
- **Physical quantum operation:** the naive local Schur mask is not CPTP; a linear subspace projection is not an admissible instrument.
- **Micro-to-physical link:** neither choice is automatically the independently frozen \(\mathcal J_N\), a physically calibrated P6 control manifold, or physical Lorentzian curvature.

A precise next objective (H35) is a **finite-time soft-locality/graded-sector bridge**: use an actual continuous-time nearest-neighbor GKSL model to distinguish strict \(\Phi_t\)-invariance from quantitative exponentially/superpolynomially small distance tails, without postulating a hard finite time support cone. Also connect only to P6's proved unitary versus dissipative locality-class comparison within its declared assumptions, not a new universal finite-speed theorem.

## Exact audit

`P3/P9H34InvariantOperatorSystemLocalityExactCheck.py` relies only on Fraction-based exact complex arithmetic; it imports H32's already-audited fixed CPTP map and independently checks chord determinants, complex ranks, invariant closures, path candidate projection ranks, and the nonalgebraic product witness. No floating-point tolerance, external specialized package or human peer review.
