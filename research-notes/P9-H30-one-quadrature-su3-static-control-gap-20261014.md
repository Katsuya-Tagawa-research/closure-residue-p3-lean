# P9 H30 — Minimal one-quadrature algebraic enlargement of the P6 real-exchange path

**2026-10-14.** Exact-rational finite audit candidate, stacked on H29 Draft PR #47. **Minimum** means the smallest number of *additional real linear control directions required to escape the original real Lie closure*, **not** a proven minimum number of experimentally implementable hardware knobs for H28's static flux scan. No claim of Lean proof, frozen P6/P3 microscopic inheritance, physical soldering or Einstein dynamics.

## 1. Exact P6 baseline

Use the exact concrete P6 v9.1 three-site path coherent control manifold, with positive edge scales absorbed into real pulse amplitudes, and zero-based sites:
```math
A=E_{01}-E_{10},\qquad
B=E_{21}-E_{12}.
```
The anti-Hermitian coherent Lie closure obeys
```math
C=[A,B]=-(E_{02}-E_{20}),\quad
[A,C]=-B,\quad[B,C]=A,
\qquad\operatorname{Lie}_\mathbb R\{A,B\}=\mathfrak{so}(3).
```
For every element \(K=aA+bB+cC\) with real \(a,b,c\), define \(H=iK\) and \(W=H_{01}H_{12}H_{20}\). Exact computation gives \(W=iabc\), hence \(\operatorname{Re} W=0\). No coherent Lie synthesis using only these two real-skew directions can produce the **instantaneous Lie generator** of H28's general four-phase flux family. The directly specified P6 controls contain only A,B and have \(W=0\).

## 2. A single extra REAL coherent quadrature suffices for full SU(3) Lie controllability

Add one anti-Hermitian quadrature on the **already present path edge**, without changing the support graph:
```math
Q_{01}=-i(E_{01}+E_{10})\notin\mathfrak{so}(3).
```
Exact repeated Lie brackets of A,B,Q01 yield **eight** real-linearly independent traceless anti-Hermitian \(3\times3\) matrices. Since \(\dim_\mathbb R\mathfrak{su}(3)=8\), it follows that
```math
\boxed{\operatorname{Lie}_{\mathbb R}\{A,B,Q_{01}\}=\mathfrak{su}(3).}
```
A rational Gaussian row-reduction checker computes real ranks of flattened real/imaginary matrix entries and closes under **all pairwise brackets** to stabilization, not just a guessed eight-element witness. Thus **one additional independent real coherent tangent direction** is sufficient to escape the real-skew obstruction; zero added directions cannot escape it. This *rank-count minimality* is relative to the original two-real-control P6 benchmark and real-linear tangent extensions.

The extra quadrature may or may not be in the inherited microscopic CR first-residue derivation space: that depends on the **independently specified actual** \(\Xi(\mathcal J_N)\). Even if it belongs to the static microscopic sector as a mathematical operator, the concrete P6 physical target-control manifold with two real amplitudes does not thereby acquire a separately addressable quadrature. The general P6 graph-internal selection theorem permits conditional complex amplitudes; it does not grant a hardware control knob.

## 3. Static-versus-Lie distinction: one extra direct quadrature is NOT itself an H28 flux knob

The direct **three-dimensional static linear** control set
```math
K_{\rm static}=aA+bB+dQ_{01}
```
is still supported only on edges 01 and 12. Hence \(H=iK_{\rm static}\) has no 02 hopping, and \(W=0\) exactly. This is a crucial boundary: Lie algebraic full controllability is **not** equivalent to free direct static Hamiltonian tuning in the H28 experiment, particularly with unavoidable site dephasing.

Because \(\mathfrak{su}(3)\) is fully generated as a Lie algebra, it contains \(C\) (coherent effective chord) and the complementary imaginary-symmetric chord quadrature
```math
Q_{02}=-i(E_{02}+E_{20}).
```
If one **adds a separate coherent pulse-synthesis/control theorem** enabling the independently calibrated effective generator
```math
K(a,b,c,d)=aA+bB+cC+dQ_{02},
\qquad H=iK,
```
then \(W=ab(d+ic)\). For a nonzero complex q choose \(d=\operatorname{Re}q\) and \(c=\operatorname{Im}q\). The unitary on-site gauge \(G=\mathrm{diag}(1,i,1)\) converts the effective Hamiltonian **exactly** into H28's form
```math
GHG^\dagger=
\begin{pmatrix}0&a&\bar q\\a&0&b\\q&b&0\end{pmatrix}.
```
This holds for every \(q\in\mathbb C\), including the four equal-magnitude phase choices \(q, -q, iq, -iq\). The checker verifies rational q=(3+4i)/5 for two independent rational a,b pairs. This identifies the **full algebraic target**, not a pulse-level implementation.

In the narrower *linear static-control* architecture that keeps the two existing path edges fixed and independently adjusts the *entire chord complex amplitude* \(q\), two real chord quadratures (C and Q02) are necessary and sufficient as independent linear tangent directions. This is a distinct engineering requirement from the **one** added path-edge quadrature needed for full Lie closure. A nonlinear phase knob, synthetic driving, or pre-existing fixed chord could change a hardware knob count; none is ruled out by this linear-algebra statement.

## 4. Open-system and operational restrictions

One extra quadrature can make full SU3 coherent unitary controllability algebraically possible under signed coherent amplitude, switchability, adequate pulse times and model-validity assumptions. It does not automatically implement the **single-time-independent H28 family with the same calibrated site-dephasing background**. Positive-time GKSL pulse synthesis, control-dependent dephasing, detunings, crosstalk, leakage, pulse errors and whether the effective \(\mathcal L_H=-i[H,\cdot]+\gamma(\Delta_D-I)\) can be generated with *fixed* \(\gamma\) need separate analysis.

The H28 third-time-population-jet Wilson readout is standard QM/GKSL even when such controls are realized, **not CR-exclusive**. It is **not** P3's original quadratic residue. H24's genuinely nonzero P3 residue was obtained in a separate microscopic two-level channel; an explicit microscopic CR-to-three-site inclusion/provenance map remains missing. No H30 result identifies the internal flux with physical Levi-Civita or Regge holonomy.

## 5. H30 audit summary and the physical gate to integration

Proved in the declared finite coherent algebra and verified exactly:
- Original P6 real pair generates precisely so3, and enforces Re W=0.
- Add a single anti-Hermitian imaginary-symmetric quadrature on an existing edge; the Lie closure is exactly su3 (real rank eight).
- The 3D **static** primitive control span still has W=0.
- Effective, independently synthesized chord quadratures C,Q02 recover arbitrary q and H28's full four-phase family after a specified site gauge.
- Existence of a formal \(\Xi(J)\) preimage does not show that J lies in the independently inherited P3/P6 microscopic sector or that its corresponding control is physically available.

**Not proved:** physical P6 first-residue quadrature provenance, calibrated pulse synthesis preserving GKSL dissipator, identifiable GR curvature, CR-specific B15 discriminator, B14 six-edge reachability, B17 response-conjugate force, or Einstein dynamics.

Suggested next research gate: either demonstrate an explicit physically admissible coherent and dissipative pulse synthesis with an **independently measured** phase-control calibration and actual microscopic CR provenance, or freeze the finite bridge with this gap as an explicit conditional assumption/no-go. Do not promise universal gravitational dynamics from mere SU3 controllability.

## Reproduction

`P3/P9H30OneQuadratureSU3ExactCheck.py` reuses H24's pure-Python rational Gaussian arithmetic, implements independent Fraction rank reduction on flattened real and imaginary entries, and checks full iterative Lie-bracket closure, exact support/no-flux condition, phase/scanning target and site gauge. A dedicated GitHub workflow executes it. No floating-point tolerances, Lean formalization or human peer-review claim.
