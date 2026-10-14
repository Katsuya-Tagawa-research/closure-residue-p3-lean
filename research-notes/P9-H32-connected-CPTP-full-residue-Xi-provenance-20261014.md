# P9 H32 — Connected single-channel CPTP witness: original P3 residue saturation and six first-residue directions

**2026-10-14.** Exact-rational finite construction, stacked on H31 Draft PR #49. **Finite constructive success under an explicit microscopic-sector assignment; not yet an independently inherited frozen P6 sector, calibrated physical control manifold, or metric/GR theorem.** The independent calculation was performed with SymPy and is implemented separately in the exact Fraction/Gaussian-rational audit. Main and frozen P3 remain unchanged.

## 1. A genuinely connected three-site microscopic CPTP channel

Use the rational complex H24 two-by-two unitary
```math
u=\frac13
\begin{pmatrix}1-2i&-2i\\-2i&1+2i\end{pmatrix}
\quad\text{with }u^\dagger u=I_2.
```
Embed it on 01 and 12 to form two 3x3 unitaries `U01=u\oplus1` and `U12=1\oplus u`. Now define **one fixed discrete microscopic time step**
```math
U_3=U_{12}U_{01}
=\begin{pmatrix}
(1-2i)/3&-2i/3&0\\
(-4-2i)/9&5/9&-2i/3\\
-4/9&(4-2i)/9&(1+2i)/3
\end{pmatrix},\quad
\Phi(A)=U_3AU_3^\dagger.
```
This is exactly unitary, hence a single-Kraus CPTP channel. Its one-step matrix entries have nonzero 01 and 12 couplings, with no decoupled site in the **specified site basis**. The construction uses **the composition of two edge unitaries to define one channel**. It does **not** claim that those two edge gates are independently available as controls within the frozen P6 hardware.

Let D3⊂M3(C) be the diagonal algebra, Δ_D the diagonal projection, Q=1−Δ_D, and E_jj the rank-one diagonal projections. Define
```math
h_j^{(m)}=Q\Phi^j(E_{mm}),\qquad
j=1,2,3,\quad m=0,1.
```
The omitted m=2 generator equals −h_j^(0)−h_j^(1) since Phi preserves I. Let
```math
\mathcal H_k=\operatorname{span}_\mathbb C
\{h_j^{(m)}:1\le j\le k,\ m=0,1\}.
```
These are **original P3 hidden Krylov projections**, not hand-selected phase-control vectors.

## 2. Exact real rank of the P6-type extraction from the P3 Krylov sector

Every h_j^(m) is Hermitian and offdiagonal. On the **declared canonical candidate microscopic sector** \(J_k:=\mathcal H_k\), the P6 real-linear map
```math
\Xi(J)=(1-\Delta_D)(J-J^\dagger)
```
has the exact real image
```math
\Xi(\mathcal H_k)
=\operatorname{span}_{\mathbb R}
\{i h_j^{(m)}:1\le j\le k,m=0,1\}.
```
A real/imaginary-coefficient rank calculation gives
```math
\boxed{
\dim_\mathbb R \Xi(\mathcal H_1)=2,\quad
\dim_\mathbb R \Xi(\mathcal H_2)=4,\quad
\dim_\mathbb R \Xi(\mathcal H_3)=6.}
```
The six-dimensional final image is exactly **all offdiagonal anti-Hermitian 3x3 generators**. It therefore contains both real exchange controls of the original P6 path benchmark
```math
A=E_{01}-E_{10},\qquad B=E_{21}-E_{12},
```
and the *new quadrature* needed for H30
```math
Q_{01}=-i(E_{01}+E_{10}).
```
Interestingly, none of those three *individual* basis directions lies in the k≤2 span, while **all** lie in k=3, because the early subspaces occupy generic linear combinations of the edge directions. With J=H3 declared, the real Lie closure of the six extracted directions is su(3), rank 8. **No extra ad hoc microscopic edge operator** is appended to the chosen J_k here: all six emerge from a single connected Phi.

This is a finite constructive microscopic compatibility example. It **does not** prove that P6's independent, frozen static microscopic \(J_N\) has been identified with H3, or that H3 is a physically addressable control sector rather than a Krylov observer sector.

## 3. First nonzero *original P3* quadratic residue is at depth three and saturates D3^0

At P3 return-depth k=2 all projected quadratic commutators from the k=1 hidden sector vanish:
```math
\Delta_D([h_1^{(m)},(h_1^{(n)})^\dagger])=0
\quad(m,n\in\{0,1\}).
```
At k=3 (one factor from H1, one from H2), two exact witnesses are
```math
r_{00}=\Delta_D([h_1^{(0)},(h_2^{(0)})^\dagger])
=i\operatorname{diag}(80/243,-16/2187,-704/2187),
```
and
```math
r_{10}=\Delta_D([h_1^{(1)},(h_2^{(0)})^\dagger])
=\frac{80i}{243}\operatorname{diag}(-1,1,0).
```
Their two independent diagonal vectors span D3^0 (complex traceless diagonals), so
```math
\boxed{\mathcal R_2=\{0\},\qquad\mathcal R_3=D_3^0.}
```
Both the depth ordering and the original P3 \(\Delta_D([z,w^*])\) are respected. This is a stronger construction than H31's spectator case, where R3 had rank one inside D3^0.

**Do not conflate:** the P3 depth-three nonzero residue, the P6 first-residue Xi image at depth three, the su3 Lie commutator control closure and H28's gauge-invariant Wilson loop. They are different objects connected here by an **explicit candidate choice** of microscopic J.

## 4. New boundary: algebraically complete but still physically uncalibrated

The constructive chain is:
```text
ONE connected rational unitary CPTP channel Phi on M3
 -> original P3 H1,H2,H3 Krylov sector
 -> original P3 R2=0, R3=D3^0
 -> candidate sector J_micro:=H3 (DECLARED identification)
 -> Xi(J_micro)=all six anti-Hermitian offdiagonal 3-site controls
 -> Lie_R Xi(J_micro)=su3 (algebraic).
```
This closes **H31's finite spectator/provenance obstruction** in an explicit connected model. It does not resolve three distinct physical gates:

1. **Independent microscopic provenance:** justify from the *frozen static CR theory* that P6's actual inherited J3 includes (or equals) this H3 in a way respecting controls, rather than choosing a convenient J after knowing the desired conclusion.
2. **Physical control access and decoherence:** prove the target coherent tangent K_X is in the independently calibrated, physically permitted control manifold, not just in Xi(H3); synthesize static/near-static H28 phase settings with dissipation and timing constraints, not simply abstract su3 Lie generation.
3. **Geometric soldering:** construct independent metric-compatible cell transport and prove H25's simultaneous loop-intertwining condition (not a dimension-matching assignment). No physical Lorentzian/Levi-Civita/Regge curvature or Einstein–Hilbert dynamics follows from this three-level matrix exercise.

The H28 4-phase scan is still a **standard quantum GKSL effect**, not an unconditional CR-specific prediction. B14 six-edge K4 physical CR-control provenance, B15 standard GKSL comparator and B17 independent response-conjugate force remain unresolved.

## 5. Audit and next decision

**H32 minimum finite success:** one fully connected single unitary CPTP witness exhibits *both* saturation of the original P3 quadratic residue in D3^0 and complete rank-six P6-style first-residue extraction from **its own** Krylov sector by depth 3. This is new finite algebraic compatibility, not a general theorem.

A sensible next step is **H33: microscopic-to-physical provenance audit**, deciding whether J_k=H_k is a derivable statement about P6's independently frozen microscopic sector, and if not, producing a precise no-go/conditional axiom for that assignment. This should precede any claims of experimentally realized CR-to-curvature transport.

## Reproduction

`P3/P9H32ConnectedCPTPKrylovProvenanceExactCheck.py` uses pure `fractions.Fraction` with H24 exact Gaussian rationals. It verifies U3 unitary, full Hermitian hidden orbit and rank-2/4/6 Xi images, original P3 R2=0 and two independent exact R3 residue witnesses, membership of actual P6 controls and H30 quadrature first at k=3, and su3 Lie closure. The independent mathematical calculation was also reproduced with SymPy. Dedicated GitHub Actions executes the script; this is **not** Lean formalization or human peer review.
