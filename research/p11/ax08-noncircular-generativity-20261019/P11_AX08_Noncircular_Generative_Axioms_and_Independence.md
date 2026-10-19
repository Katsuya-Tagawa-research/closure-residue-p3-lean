# P11–AX08 — Non-Circular Generative Axioms and Independence Audit

**2026-10-19 • P11 axiomatization.** Follows AX07 Draft PR #145; independent of SPS-H113–H123 source-selection Drafts. **Conditional mathematical result, NOT a physical G2 or F-generative G3 PASS.**

## G1, G2 and G3 are distinct predicates

- **G1 Operational completeness:** predictions for all finite histories in a **declared** instrument/control/readout alphabet are fixed; AX07 gave a finite-dimensional finite-word equality test.
- **G2 Source/observer completeness:** the independently existing native physical ports, effects, instruments, phase references, microscopic source and catalogue exhaustiveness are established.
- **G3 Generative completeness:** a mathematically typed, noncircular F determines the required source/observer objects and morphisms (modulo *previously declared* gauge), with observer and composition consistency.

G1 implies neither G2 nor G3. The descent tautology s=f∘π iff s is constant on every π-fibre is a test of a proposed physical category, not a substantive F-origin axiom. No deterministic extra statistic a=h∘π refines its fibres.

## AX08.1 — All-word CPTP spectator nonidentifiability (exact conditional theorem)

Let finite A be observable, B an unobserved spectator. The observer is allowed only an alphabet of CP instrument maps {I_a} on A; sum_a I_a is CPTP. Pick *any* CPTP T_B on B, and define the joint instrument

  **Ĩ_a^T = I_a ⊗ T_B**.

For every joint R (including entangled R),

  Tr_B[(I_a ⊗ T_B)(R)] = I_a(Tr_B R).        (8.1)

Because T_B is trace preserving, the partial trace eliminates it; factor-A maps commute with partial trace. Induction shows (8.1) for *all finite outcome words* and all interleaved allowed A-only instruments. All observed word probabilities and reduced A output states agree, although the hidden T_B may differ. The result is relative to a class allowing physically unobserved spectator factors and a **fixed A-only operation alphabet**. It does not claim equality if the observer may act on B or couple A to B.

### Exact 2×2 joint qubit witness

Take I_0(rho)=p0 rho p0, I_1(rho)=p1 rho p1, B hidden id versus Ad_Z. The two joint Kraus sets {p_a⊗I} and {p_a⊗Z} are legitimate two-outcome instruments, with identical A-only effect family p_a⊗I. Full A-only probabilities for **every finite word** agree; the analytic reason is (8.1), and the exact SymPy audit checks matrix-unit intertwining and every binary word through length **6** (604 assertions total).

Relative to a fixed joint A⊗B factorization and fixed B input/output frame, id and Ad_Z are genuinely different hidden dynamics (the identity channel stays the identity under simultaneous unitary gauge, while Ad_Z does not). An *independently supplied* B preparation |+><+| and B-X readout after A outcome 0 gives B-X expectations **+1** versus **−1**. This distinguishes the two **only after broadening the permitted operations**; it has not been implemented or calibrated in the physical H37 apparatus. The example is a mathematical hidden-sector witness, not the original P3 generated commutator residue.

## AX08.2 — Unmarked U(d) symmetry obstructs a distinguished pointer

An observer selector from an *unmarked* Hilbert H=C^d, d>1, which is natural under every U in U(d) and returns a distinguished rank-one effect P, must satisfy U P U†=P for all U. The commutant of U(d) is the scalars, so P=λI. No nonzero rank-one projection has this form for d>1. For d=2 already commuting with Pauli X and Z forces scalar; this is exactly verified.

The statement is about a **single canonical nontrivial pointer**; it does not forbid selecting the identity, scalar algebra, entire M_d, *all* rank-one projectors as an equivariant family, or selecting one with independent physical symmetry-breaking data. It is not a universal no-go against a stronger properly typed F.

### Formal typing warning concerning the notation F: ∅→(Λ,Ω)

If interpreted literally as a set-theoretic map with empty domain, the unique map ∅→Y has no arguments and cannot output a distinguished element of Y. A categorical initial-object arrow also does not automatically select a normalized state or measurement pointer. The generative notation F may be a *symbolic relation or axiom*, but P11 must explicitly type it in a category with objects, allowed symmetries, and an independently meaningful existence/uniqueness statement. This clarification does not disprove the proposed generative philosophy.

## AX08.3 — Noncircular proof-obligation interface

**AX-DOM:** Specify admitted objects, their CR operational-data map π, physical source labels s and permitted equivalence *before* target response. Identify whether spectator extensions are admitted.

**AX-OBS:** Provide an independently justified observer instrument/POVM, initial preparations, phase/frame and complete protocol alphabet, or prove a new F-derived restriction that selects these without feeding in a target j01 fingerprint.

**AX-PROV:** Source origin or independently certified native access and exhaustiveness, not merely a renamed AX-SOURCE-SEP condition.

**AX-NAT:** Define exact gauge, tensor, embedding, restriction, observer-reduction and reset morphisms for the candidate source functor. Equivariance on one diagonal-gauge orbit does not imply functoriality over arbitrary physical CPTP processes.

**AX-PRED:** State which operation words and state-output claims are identifiable and whether hidden-source equivalence is even among the intended predictions.

**AX-SELF:** Formal self-description consistency for *observers generated internally* must be proved, not inferred from a finite observable quotient.

**AX-PHYS:** P6 two-stage CPTP experiment, independently calibrated physical native controls/readout and comparison with a matched standard GKSL model remain separately OPEN. P9 ADM/HDA/Einstein dynamics likewise OPEN.

## Relative conditional result

If additional independently sourced data a split every fibre on which the physical source label s differs, then by AX07/SPS-H118 the desired factorization on im(π,a) exists uniquely. This is a **conditional existence theorem**, not a recipe extracting the physical a from operational π.

## Decision ledger

| Question | Status |
|---|---|
| A-only all-word histories characterize A-only operational semantics | **EXACT relative to fixed alphabet** |
| All A-only histories determine independent hidden spectator dynamics | **NO** in a spectator-stable model class |
| Independent B preparation and B-X readout distinguish example | **EXACT toy; physical implementation OPEN** |
| Unmarked U(d)-natural distinguished rank-one pointer | **NO-GO** |
| Choosing a minimum-dimensional operational realization recovers full physical microstructure | **NOT IMPLIED** |
| G1 finite predictive completeness | **CONDITIONAL / exact finite system** |
| G2 source and observer physical completeness | **OPEN** |
| G3 F-generative completeness | **OPEN** |

**STOP rule:** Do not add arbitrary H37 J5 source-sector candidates or claim source/observer completeness from finite-word prediction ranks. Advance toward G2/G3 only with an independently justified restriction on the model class or source/observer evidence. If neither exists, preserve OPEN; mathematical completeness of G1 alone does not solve G3.

### Prior theory and verification limits

Nonuniqueness of microscopic implementations is consistent with Stinespring theory: minimum channel dilations have uniqueness only up to environmental isometry/unitary; minimum **operational** presentations do not certify absence of unseen physical spectators. Compare A. Acevedo and A. Falcó, *Geometric Complexity of Quantum Channels via Unitary Dilations* (arXiv:2601.00735, 2026), on intrinsic versus implementation-dependent channel properties.

Reproduce: \`python research/p11/ax08-noncircular-generativity-20261019/P11_AX08_independence_audit.py\`, SymPy 1.14. **604/604 exact finite assertions** including all binary words through length 6; all-length results are proved algebraically, **not mechanized in Lean**. This is neither independent human peer review nor a physical experiment.
