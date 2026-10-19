# SPS-H122 — Native Control-Jet Certification and the AX-ORIGIN Boundary

**2026-10-19; P3–P11 Mathematical Bridge, Static Primitive Selection track.** Stacks on SPS-H121 Draft PR #136, not the separate H75/P11 H113 of PR #132. Scope: exact conditional theorems, 65 finite SymPy assertions. **No physical native-control, P6 hardware gate, P9 gravity, or P11 Generative Completeness is claimed.**

## 1. The control-jet interface and a positive conditional reconstruction theorem

Work on M_d(C). Let **B** be a known baseline CPTP channel, followed by an **independently marked** Hamiltonian pulse:
\[
\Phi_u=\operatorname{Ad}_{e^{-iuH}}\circ B,\qquad H=H^\dagger,\qquad
T=\partial_u\Phi_u|_{u=0}.
\]
If B is **invertible as a linear superoperator**, and T is exactly characterized by complete process tomography, then
\[
\boxed{T B^{-1}=-i[H,\cdot].}
\]
Thus H is recoverable uniquely modulo a **real scalar multiple of I**. Proof: differentiate the post-baseline unitary conjugation. If [H-H',A]=0 for all A in M_d, then H-H' belongs to the center CI; Hermiticity forces a real scalar.

The linear inverse B^{-1} is generally **not CPTP**, and may be poorly conditioned. Finite-time semigroups B=e^{tL} are invertible linearly for every finite t (with inverse e^{-tL}), but that analytic fact does not certify stable laboratory inversion, pulse ordering, or an independently native pulse. If the pulse comes **before** B, the data jet is B∘(-i ad_H) and cannot in general be deconvolved by this same formula.

This assumes an **inner Hermitian derivation model**. For arbitrary CPTP control jets, T B^{-1} need not be a commutator map. A proposed coherent control is justified mathematically only if the measured deconvolved jet lies in the real space of inner *-derivations.

## 2. Observation-rank theorem (exact finite-dimensional real linear algebra)

With calibrated input preparations rho_b, measured Hermitian observables M_a and baseline B, define for a Hermitian Hamiltonian H
\[
\mathcal O_B(H)_{ab}
=\operatorname{Tr}\bigl[M_a(-i[H,B(\rho_b)])\bigr].
\]
Given an a priori target real subspace V⊆Herm_d/R I, **H is identifiable on V iff O_B restricted to V is injective**. In a real coordinate basis this is the criterion rank(O_B|_V)=dim_R(V). When V=Herm_d/R I, the required rank is d²−1.

This criterion can be achieved without an entire process-matrix tomography when carefully prepared probes and readouts already separate the candidate H directions. Exact qubit witness: with V=span_R{X,Y,Z}, diagonal-state preparations and diagonal-population readouts produce rank **0** for the first-order Hamiltonian signal; two noncommuting states |0><0| and |+><+| with calibrated X,Y,Z observables produce rank **3**. This is a local, exact Jacobian test; it does not guarantee robust practical inversion.

## 3. Explicit unobservability and source-inventory counterexamples

**Noninvertible baseline.** If Δ is full diagonal dephasing and Z is the diagonal Pauli operator, Ad_{e^{-iuZ}}∘Δ=Δ for all u, despite nontrivial Z. The post-pulse is invisible at every order. If R(ρ)=Tr(ρ)|0><0| is a reset, then R∘Ad_{e^{-iuH}}=R for all H,u: even all pre-reset unitaries are erased. These are noninjective interface examples; some singular baselines may still identify some controls, so no blanket failure theorem is claimed for all singular B.

**Exhaustiveness failure.** Two formal device completions have identical baseline B and all response words/derivatives over the **marked** X control, while one has an additional unmarked, independent Z control. All exact marked data agree; the true native actuator catalogues differ. Therefore identifying each *presented* knob never certifies that there are no **unpresented** native knobs. This is the H113/H117 fibre-descent obstruction, not experimental evidence for two real devices.

## 4. Fixed H37 finite mathematical check and its boundary

On the original H37 five-site path, let K_e=E_{e,e+1}−E_{e+1,e}, e=0..3, and the **declared** Hermitian control Hamiltonians H_e=iK_e. Their four formal commutator jets -i[H_e,.]=[K_e,.] are linearly independent as 25×25 superoperators (rank **4** in 625-dimensional matrix coefficient space). For the known H37 generator
\[
L(\rho)=-i[H_0,\rho]+\tfrac23(\Delta_D(\rho)-\rho),\quad
H_0=\tfrac12\sum_{e=0}^3(E_{e,e+1}+E_{e+1,e})
+\operatorname{diag}(0,1/7,-1/9,2/11,-3/13),
\]
B_t=e^{tL} has a linear inverse for any finite t by matrix-exponential algebra. **If** these controls are independently certified as post-baseline actuators and B_t plus their complete process derivatives are known, deconvolution recovers the four declared jets.

This is not certification that hardware has four independently actuated exchange controls, that four exhausts native control options, that the P6 static J5 is selected, or that hidden P3/P4 sectors equal native controls. H121's canonical dephasing noise space D_5^0 has complex dimension four but is diagonal, unlike the real four-dimensional offdiagonal marked K_e space. Dimension matching is not provenance.

## 5. AX-JET-SCOPE review certificate (proposed evidence interface, NOT an accomplished test)

- Native actuation: independent primitive origin, physical control port and pulse timing **before** target j01 data, distinct from Lie synthesis and terminal analyzer.
- Baseline: complete or sufficiently ranked channel/preparation/readout data; state when B is invertible and quantify conditioning/systematic error.
- Gauge/reference: marked site basis, relative X/Y phase reference and state-preparation/measurement frames, with gauge equivalence declared.
- Exhaustiveness: evidence **separate from marked-jet reconstruction** establishing which physical control knobs are included and excluded in the advertised native catalogue.
- Two-stage CPTP and comparator: independently calibrated P6 chain, matched standard GKSL predictions, a prospective distinguishing witness and locked criteria.
- Audit scope: raw dataset hash, device version, controls/observer/protocol list and independent physical reviewer; preserve blinded target readout where required.

## 6. Result table and stop condition

| Statement | Status |
|---|---|
| Complete post-baseline jet plus known invertible baseline determines marked H modulo R I | **EXACT, conditional** |
| Selected preparations/measurements identify H iff Jacobian has full rank | **EXACT, conditional** |
| Qubit diagonal-population-only first-order response identifies all X,Y,Z | **NO: rank 0 witness** |
| Completely dephased post-Z and pre-reset controls always visible | **NO: exact all-u witnesses** |
| Marked-control process jets imply an exhaustive physical native inventory | **NO-GO in weak source-expanded class** |
| H37 four declared marked control jets linearly independent | **EXACT finite algebra; physical premise OPEN** |
| Noncircular F-derived native source, P6 experiment, P9 GR and P11 completeness | **OPEN** |

**Decision:** SPS-H122 provides the bounded *mathematical* native-control-jet interface. On the presently supplied H37/P3/P4 data, **further automatic physical source certification is blocked**. Do not produce more arbitrary J5 candidates or mark any physics gate PASS until independent AX-JET-SCOPE evidence or a genuinely restrictive F-derived origin axiom is supplied. A future ledger/integration audit can classify proof obligations but cannot bypass the epistemic boundary.

## Reproduction and priority boundary

Run the companion SymPy 1.14 audit. Expected **65/65 exact finite assertions** and output JSON recording observation ranks 0/3, H37 marked jet rank4, and OPEN physics gates. The analytic rank and inner-derivation proofs above are not Lean mechanized, and CI does not provide independent human peer review.

Relevant established literature (not priority claims):
- Burgarth & Yuasa, *Quantum System Identification*, PRL 108, 080502 (2012), DOI 10.1103/PhysRevLett.108.080502.
- Burgarth & Yuasa, *Identifiability of Open Quantum Systems*, PRA 89, 030302(R) (2014), DOI 10.1103/PhysRevA.89.030302.
- Leghtas et al., *Hamiltonian identification through enhanced observability utilizing quantum control*, IEEE TAC 57, 2679–2683 (2012), DOI 10.1109/TAC.2012.2190209.
