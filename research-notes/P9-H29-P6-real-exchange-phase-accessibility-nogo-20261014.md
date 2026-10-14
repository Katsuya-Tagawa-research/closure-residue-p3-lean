# P9 H29 — Original P6 real-exchange controls do not supply H28's four-phase Wilson knob

**Date:** 2026-10-14. **Status:** exact-rational finite audit, stacked on H28 Draft PR #46; not Lean kernel proof, not real-hardware certification, and not Einstein dynamics. Do not merge or modify main/frozen P3. The full H28 Wilson readout remains a valid **conditional** standard GKSL computation.

## 1. Audit against the actual frozen P6 control definition, not a generic triangle

P6 v9.1, three-site path benchmark (Section 4, *Exchange-type edge control*), uses \(\mathcal M_B=\mathbb R^2\), positive fixed coupling scales, the oriented edge lift \(z_x=g_Lx_LE_{12}+g_Rx_RE_{32}\) (one-based labels), and the **real anti-Hermitian** generator \(K_x=z_x-z_x^*\). In zero-based labels and after absorbing positive g scales into amplitudes:
```math
A=E_{01}-E_{10},\qquad B=E_{21}-E_{12},\qquad
K_{\rm declared}(x)=x_L A+x_R B.
```
P6's *general* graph-internal theorem permits complex edge coefficients **if and only if the independently fixed microscopic CR sector and physical tangent support them**. The concrete two-real-control three-site benchmark does not, merely by being a graph-internal example, supply H28's independently tunable complex triangular hopping phases.

For the static benchmark the chord (0,2) does not exist, so the triangle Wilson invariant is **zero**. The coherent Lie closure has
```math
C=[A,B]=-(E_{02}-E_{20}),\quad
[A,C]=-B,\quad[B,C]=A,\qquad
\operatorname{Lie}_{\mathbb R}\{A,B\}=\mathfrak{so}(3).
```
The bracket is a **dynamical reachable direction under appropriate coherent-pulse assumptions**, not automatically a new **directly tunable independent static Hamiltonian tangent** in P6's declared manifold. This physical/operational distinction is preserved throughout.

## 2. Exact phase-orbit No-Go

Every element of the real Lie closure has \(K=aA+bB+cC\) with \(a,b,c\in\mathbb R\). Express it as a Hermitian Hamiltonian \(H=iK\), so \(K=-iH\). Its three hopping amplitudes are imaginary, with gauge-invariant oriented Wilson product
```math
W(H)=H_{01}H_{12}H_{20}=iab c.
```
Thus
```math
\boxed{\operatorname{Re}W=0}
```
for every instantaneous Hamiltonian in this **generously allowed entire** real \(\mathfrak{so}(3)\) Lie closure, not merely the original 2D tangent. If \(c=0\), then \(W=0\); otherwise its phase is ±π/2 modulo 2π. This statement is invariant under arbitrary diagonal on-site U(1) gauge changes.

H28's four-setting protocol requires multiplying a *nonzero* triangular Wilson product by \(\lambda\in\{1,-1,i,-i\}\), holding its edge magnitudes and common dephasing fixed. If \(W\in i\mathbb R\setminus\{0\}\), the \(iW\) and \(-iW\) settings have **nonzero real part**, hence are **outside this real-skew Lie algebra even after taking coherent commutators**. In H28's gauge with \(H_{01}=a>0,H_{12}=b>0\), this means a genuine complex direct chord with its full phase circle is an extra physical control capability, not derived from the P6 path.

An opposite-chirality **π flip** \(c\mapsto-c\) stays within \(\mathfrak{so}(3)\) algebraically, but producing it as a static, independently calibrated control at fixed \(a,b,\gamma\) still needs an actual supported pulse synthesis/drive calibration; algebraic Lie reachability alone is not sufficient to certify such a Hamiltonian.

The No-Go is explicitly **relative to the P6 real-exchange benchmark and its real Lie closure**. It does not exclude adding diagonal detunings, complex/Peierls hopping controls, synthetic gauge drives, Floquet Hamiltonians with their own dissipative calibration, or changing the microscopic sector; those modify the declared/physical control assumptions.

## 3. What positive-time CPTP pulse order comparison can still see

Let \(\mathcal L_A(\rho)=[A,\rho]+\gamma(\Delta_D\rho-\rho)\), similarly \(\mathcal L_B\). For \(\gamma\ge0\), both \(e^{t\mathcal L_A}\) and \(e^{t\mathcal L_B}\) are genuine CPTP semigroups for forward \(t\ge0\). Compare, for fixed \(\rho_0=E_{00}\),
```math
(e^{t\mathcal L_A}e^{t\mathcal L_B}
-e^{t\mathcal L_B}e^{t\mathcal L_A})(\rho_0)
=t^2[\mathcal L_A,\mathcal L_B](\rho_0)+O(t^3).
```
An exact computation gives
```math
[\mathcal L_A,\mathcal L_B](E_{00})
=[C,E_{00}]+\gamma[A,E_{00}],
\quad
\Delta_D[\mathcal L_A,\mathcal L_B](E_{00})=0.
```
The 02 *coherence* coefficient equals exactly **1** at order \(t^2\) and is independent of the common site-dephasing \(\gamma\). The 01 coherence coefficient is instead \(-\gamma\), a calibrated nuisance term. Thus comparing **two forward physical preparations** is a possible operational witness of the coherent Lie bracket under the stated identical dephasing, ability to swap pulse order, and ability to read out 02 coherence. It is a comparator in orthodox GKSL physics; it does not independently prove a nonzero P3 *original* quadratic residue or a CR-specific signal. Nor is this 2-pulse order-contrast the four-setting *static* Wilson-phase scan of H28.

### Why the four-factor inverse-Lindblad loop is invalid with dissipation

The ideal unitary group commutator \(e^{\epsilon A}e^{\epsilon B}e^{-\epsilon A}e^{-\epsilon B}\) is physically unitary when \(\gamma=0\) and signed controls are available. When \(\gamma>0\), replacing each factor by a Markov semigroup generator \(\mathcal L_A,\mathcal L_B\) and inserting \(e^{-\epsilon\mathcal L_A}\) requires reversing dephasing. Even pure dephasing \(\mathcal D_\gamma=\gamma(\Delta_D-I)\) sends coherence \(\rho_{01}\) to \(e^{-\gamma t}\rho_{01}\), so its inverse amplifies it by \(r=e^{\gamma t}>1\), turning the positive state \(|+\rangle\langle+|\) into a matrix with 2×2 principal determinant \((1-r^2)/4<0\). The inverse is **not positive, hence not CPTP**. A viable dissipative operational bracket test must compare forward sequences, as above, or specify an actually feasible echo whose dissipation is analyzed separately.

## 4. P9 bridge consequences

**What is finite-proved conditional math:** the P6 real two-edge tangent closure is \(\mathfrak{so}(3)\); every Lie-synthesized static Hamiltonian in that closure has \(\operatorname{Re}W=0\); a 90-degree flux knob as used in H28 is impossible **within that declared algebra**, even when coherent brackets are freely allowed; independently calibrated forward GKSL pulse order can witness the missing chord Lie bracket through a coherence readout.

**What is not supplied:** P6's actual inherited P3/P4 CR sector for the H24 phase-sensitive two-level witness, independent complex triangle phase controls, a CP-valid negative-dissipation commutator loop, calibration of the effective synthetic chord, a CR-specific comparator separation under B15, or physical soldering into P7/P8. Real Hamiltonian terms, control-dependent dissipators, and measurement imperfections require explicit independent calibration.

**Recommended next gate H30 (or the program's integration/freeze gate, naming pending):** test the *minimum enlarged* physical control algebra that supplies \(\operatorname{Re}W\ne0\) while retaining a separately fixed CR microscopic sector, then formulate independent, falsifiable nulls for that enlargement. If it cannot be derived from First-Residue Accessibility, record it explicitly as an added hardware postulate, not P3-generated spatial curvature.

## Exact verification

`P3/P9H29P6RealExchangePhaseAccessExactCheck.py` imports the already audited H24 exact rational-Gaussian arithmetic; uses only standard-library Fraction; verifies Lie brackets and Wilson gauge restriction, absence of static path chirality, four-phase accessibility obstruction, forward semigroup order contrast with common site dephasing, and failure of inverse dephasing positivity. Dedicated GitHub Actions executes the checker. There are no floating-point tolerances, Lean proof claims, or human-review claims.
