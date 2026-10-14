# H38 — Actual P6 real-exchange observer: one quadrature, a strict residue No-Go, and a conditional calibrated phase repair

**2026-10-14 | P3–P11 Mathematical Bridge**. Stacked on H37 Draft PR #56. Exact Gaussian-rational finite audits with a short analytic all-circuit invariant-subspace proof. No frozen P3/P6 source or main changes, no Lean kernel formalization, human peer review, claimed CR-exclusive experimental prediction, physical Lorentzian curvature or Einstein dynamics.

## 1. Source-grounded declared P6 benchmark: which controls are actually allowed?

The **concrete** 3-site physical exchange benchmark in the **frozen P6 final v9.1 manuscript** explicitly declares
\[
\mathcal M_B=\mathbb R^2,\qquad
z_x=g_Lx_LE_{12}+g_Rx_RE_{32},\qquad
K_x=z_x-z_x^\dagger,\quad U(x)=e^{K_x},
\]
with real control amplitudes and positive calibrated coupling scales \(g_L,g_R\). Up to relabeling to zero-based \(0,1,2\), these are
\[
A_{01}=E_{01}-E_{10},\quad B_{12}=E_{21}-E_{12},
\quad K=aA_{01}+bB_{12}\in\mathfrak{so}(3).
\]
The selected observer reads populations in the same site diagonal MASA \(D_3\). P6 also establishes a separate **conditionally calibrated** dissipative locality theorem for finite-range exchange plus independently calibrated site dephasing; this does not add coherent Stark/phase controls to the above *two-real-knob* target manifold.

**Scope:** the results below are rigorous for this **restricted real-exchange/pure site-dephasing benchmark**. They do **not** assert that arbitrary P6-compatible physical Hamiltonians, independently calibrated nuisance coherent controls, all laboratory instruments, or the abstract CR first-residue operator subtype are real matrices.

## 2. All-circuit imaginary-coherence No-Go (stronger than any finite pulse test)

A real-skew \(K\) exponentiates to a real orthogonal \(U\in SO(3)\), and \(U\rho U^T\) preserves the real vector-space splitting of Hermitian matrices into
\[
\rho=X+iY,\quad X=X^T\in M_3(\mathbb R),
\quad Y=-Y^T\in M_3(\mathbb R).
\]
Both subspaces remain invariant under arbitrary real orthogonal exchange conjugations. The independently calibrated site-dephasing CPTP map
\[
D_q(\rho)=q\rho+(1-q)\Delta_D\rho,\quad 0\le q\le1,
\]
also preserves each subspace; \(iY\) has identically zero diagonal. Consequently **every** finite concatenation of arbitrary real-exchange pulses and any site-dephasing channels, followed by any diagonal population measurement, depends only on \(X=\Re\rho\), and cannot detect \(Y=\Im\rho\).

Explicit physical density witness:
\[
\rho_\pm=\frac{I_3}{3}
\pm\frac{i}{6}(E_{01}-E_{10}).
\]
Both have eigenvalues \(1/6,1/3,1/2\), hence are valid positive trace-one states. Their imaginary-coherence signs differ, but all populations agree after **every** admissible real-exchange/dephasing circuit. The checker verifies a nontrivial five-pulse mixed circuit, and the preservation proof covers arbitrary pulse sequences and even time-dependent real exchange GKSL evolution. This is a **restricted physical-observer identifiability No-Go**, not a generic impossibility for coherent tomography in quantum mechanics.

## 3. Consequence for the *original* P3 quadratic residue of the restricted baseline

Take an originally diagonal seed \(d\in D_3\) and the real-exchange/pure-dephasing generator
\[
\mathcal L_K(\rho)=[K,\rho]+\gamma(\Delta_D\rho-\rho),
\quad K\in\mathfrak{so}(3),\ \gamma\ge0.
\]
It is a valid GKSL generator since \(K\) is anti-Hermitian and the jump operators may be \(\sqrt\gamma E_{jj}\). This dynamics preserves **real symmetric matrices** and is unital/CPTP. Thus for any \(t>0\), the original-P3 hidden filtration of the discrete CPTP update \(\Phi_t=e^{t\mathcal L_K}\), generated from the diagonal algebra, consists of **complex symmetric** offdiagonal matrices:
\[
\mathcal H_k(\Phi_t,D_3)
\subseteq\{Z\in M_3(\mathbb C): Z^T=Z,\ \Delta_D Z=0\}.
\]
For all such \(z,w\), the operator \(w^\dagger\) is again symmetric, so \([z,w^\dagger]\) is skew-symmetric, and its diagonal vanishes. Hence the **full original P3 quadratic residue filtration** of this restricted real-exchange model is
\[
\boxed{\mathcal R_k(\Phi_t,D_3)=\{0\}\quad
\text{for all }k\ge0.}
\]
This is stronger than saying one signed depth-three witness happens to vanish, and is consistent with H29's \(\mathfrak{so}(3)\) first-residue phase restriction. It is **not** a universal theorem that real Hamiltonian hopping gives zero residue: a conventional *real symmetric Hamiltonian* H generates a generally complex unitary \(e^{-itH}\). Here the physical coherent generator is **real skew** K and the unitary \(e^K\) is real orthogonal, precisely the frozen P6 toy exchange convention.

## 4. What the P6 exchange population response **does** read

Let \(A=E_{01}-E_{10}\), and let the exchange pulse start from an arbitrary Hermitian state \(\rho\). The generator is \([aA,\cdot]\). Then
\[
\boxed{
\left.\frac{d}{ds}\operatorname{Tr}[E_{00}
e^{s\operatorname{ad}_{aA}}(\rho)]\right|_{s=0}
=2a\,\operatorname{Re}\rho_{01}.
}
\]
The pure site-dephasing GKSL term has zero *instantaneous* population derivative and leaves this slope unchanged. This is genuine access to the **real** quadrature of a coherence when the corresponding edge pulse, input state and population slope are independently calibrated. It does not mean the frozen P6 preparation protocol supplies arbitrary non-diagonal input states, nor that the imaginary quadrature is accessible.

## 5. A mathematically sufficient but PHYSICALLY EXTRA phase-gate resource

Introduce a separately permitted, independently calibrated local coherent phase unitary
\[
V=\operatorname{diag}(-i,1,1),
\]
and independently calibrated site-dephasing attenuation q∈(0,1] before the exchange pulse. The resulting **CPTP** phase+dephasing channel is
\[
\mathcal E_{V,q}(\rho)=D_q(V\rho V^\dagger).
\]
It changes \(\rho_{01}\mapsto -iq\rho_{01}\). Therefore the same population slope under exchange aA gives
\[
\boxed{
s_X=2a\,\Re\rho_{01},\qquad
s_Y=2aq\,\Im\rho_{01}.
}
\]
For a≠0 and **calibrated q>0**,
\[
\boxed{
\Re\rho_{01}=s_X/(2a),\qquad
\Im\rho_{01}=s_Y/(2aq).
}
\]
The checker verifies this exactly on physical \(\rho_\pm\) and on a generic positive Hermitian state, with rational q=2/3 and rational coherent matrices. The generator-dephasing term contributes no instantaneous population derivative; the issue of implementing a **finite duration, calibrated phase gate** concurrently with other controls remains a separate physical pulse-synthesis question.

For absolute measured slope errors η_X and η_Y and exactly known nonzero a,q, worst-case coordinate errors are
\[
|\delta\Re\rho_{01}|\le\eta_X/(2|a|),\qquad
|\delta\Im\rho_{01}|\le\eta_Y/(2|a|q).
\]
If q, a or V's phase are themselves imperfectly calibrated, their systematic uncertainties must be propagated separately; site-dephasing calibration alone does **not** calibrate the Stark phase.

**Crucial provenance:** this phase gate is NOT in the frozen concrete P6 2-real-exchange target controls; it is a new external coherent resource, even though diagonal Hamiltonians have trivial *first* action on the population MASA. P9.38 independently showed that such diagonal Hamiltonian freedom is **not** a gauge symmetry of the original P3 higher-residue witness: the diagonal-gauge Laplacian variation is \(+2i\,\operatorname{diag}(L_w\alpha)\). Thus requiring a coherent phase reference is a physically significant new condition, not a harmless relabeling.

## 6. Release of a nonzero *leading* original P3 witness by the extra Stark detuning

Fix the same P6 real exchange K=aA+bB, real diagonal initial d=E00, γ≥0. Baseline α=0 gives zero residue at *every* P3 filtration depth by the theorem above. Add an **independently allowed** diagonal Hamiltonian \(\alpha=\mathrm{diag}(\alpha_j)\) so
\[
\mathcal L_{\alpha}(\rho)
=[K,\rho]-i[\alpha,\rho]+\gamma(\Delta_D\rho-\rho).
\]
Write \(A_h=Q_D\mathcal L_\alpha(d)\), \(B_h=Q_D\mathcal L_\alpha^2(d)\). The *leading coefficient* of the legal original-P3 depth-three witness is
\[
[t^3]\,\Delta_D([Q\Phi_t(d),Q\Phi_{2t}(d)])
=\Delta_D([A_h,B_h])
=2i\,a^2(\alpha_0-\alpha_1)(E_{00}-E_{11}).
\]
For a=2/3 and α=(1/7,0,0), the exact cubic coefficient is \(8i/63(E_{00}-E_{11})\), and it is independent of gamma in the declared dephasing model. This is an explicit intersection of P9.38's Laplacian identity and the P6 source-specific observer obstruction. It is **ordinary standard quantum GKSL**, not a new CR-exclusive witness. It also does not prove \(\mathcal R_3\)'s dimension/saturation at a fixed time.

## 7. Physical provenance and next proof gate

**PASS finite algebra:** all real-exchange/dephasing population circuits are blind to imaginary skew coherence; population slope reads one real coherence; the restricted model has \(\mathcal R_k=0\) for all depths; a separately calibrated diagonal phase gate unlocks the missing quadrature; detuning can produce nonzero depth-three leading signed P3 residue.

**OPEN physics:** a phase gate implementing V with calibrated control strength/duration and q, admissible within *independently fixed* P6 physical coherent control domain; two-time preparations with a phase-locked reference; actual frozen microscopic \(\mathcal J_N\) and target-control correspondence; P3/P6 *- and \(\Delta_D\)-compatible two-step map intertwining. Without these no claim of actual P6 device experimental accessibility, CR-only comparator or gravitational soldering.

**H39 suggestion:** attempt the smallest independently calibrated external diagonal phase/Stark resource and a concrete P6 physical control/readout to construct a **finite-time**, not only infinitesimal, two-quadrature scheme with uniform dephasing calibration. If the frozen declared control manifold must remain strictly two-real-exchange, freeze this no-go and do NOT claim an H37 coherent observer without explicitly adding physical inputs.

## Reproduction

P3/P9H38P6RealExchangeObserverGateExactCheck.py uses exact Fraction/Gaussian-rational data from CI-passed H32. It verifies physical density positivity, genuine orthogonal real pulses and CPTP dephasing, full initial-population invisibility in tested circuits, all P3 commutator diagonals for generated real-symmetric jets, X/Y exchange-slope readout after a calibrated phase channel, slope-conditioning bounds and P9.38-calibrated Stark leading-residue coefficient. Dedicated GitHub CI; no floating-point tolerances, formal Lean proof or hardware result.