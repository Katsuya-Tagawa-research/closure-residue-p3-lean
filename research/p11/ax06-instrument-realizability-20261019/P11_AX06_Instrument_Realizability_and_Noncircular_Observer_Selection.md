# P11–AX06 — Instrument Realizability and Non-Circular Observer Selection

**2026-10-19 | P11 axiomatization**. Stacked on AX05 Draft PR #143, separate from SPS-H113–H123. **133/133 exact SymPy finite checks**. The underlying quantum-instrument, POVM and dilation principles are established quantum measurement theory. This is a typed proof-gate application, not a claim of new Naimark/Stinespring results.

## AX06.1 — Four input categories must be kept separate

- POVM effects E_a >=0, Σ E_a=I, which determine only p(a|ρ)=Tr(E_aρ);
- outcome-labelled CP, trace-nonincreasing instrument maps I_a with Σ_a I_a CPTP and I_a†(I)=E_a;
- mathematically existing dilation: an isometry V and ancilla pointer measurement realizing those maps;
- independently calibrated physical device: specific native operations, state preparation, outcome resolution, controls, timing, phase frames and exhaustive declared operational scope.

**Abstract realizability does not certify the last category.** If I_a(ρ)=Σ_μ K_aμ ρ K_aμ†, define V|ψ>=Σ_aμ (K_aμ|ψ>)⊗|aμ>. Since Σ_aμ K_aμ†K_aμ=I, V†V=I. Pointer projection onto the |aμ> labels implements the instrument. Every finite POVM has at least the Lüders instrument K_a=√E_a. These are standard finite-dimensional quantum-measurement constructions, not F-generated physical observer axioms.

## AX06.2 — IC POVM does not determine selective instrument (exact qubit witness)

Let a∈{X,Y,Z}, s∈{+1,-1}, and define Pauli spectral projectors P_(a,s)=(I+s σ_a)/2. Six effects E_(a,s)=P_(a,s)/3=(I+s σ_a)/6 sum to I and have complex operator-span rank 4, i.e. **informational completeness for unknown initial qubit states**.

For each outcome, choose either
  K^L_(a,s)=P_(a,s)/√3
or
  K^R_(a,s)=|0><a,s|/√3.
Their Kraus effects coincide: K†K=E_(a,s) for every a,s, so **all one-shot probabilities coincide for all inputs**. But for input |1><1| the repeated outcome word (Z−, Z−) has probability **1/9** (Lüders) versus **0** (reset-to-|0>). Complete *input-state* information is not instrument identification. Both are perfectly valid abstract CP instruments.

## AX06.3 — Stronger selector failure with matched POVM and matched nonselective CPTP channel

With p0=|0><0|, p1=|1><1|, Z=p0−p1 and Δ_Z(ρ)=p0ρp0+p1ρp1, construct outcome CP maps

  I^A_0(ρ)=I^A_1(ρ)= Δ_Z(ρ)/2;
  I^B_0(ρ)= ZρZ/2; I^B_1(ρ)=ρ/2.

Both instruments have effects E0=E1=I/2 and the SAME nonselective channel Σ I_a=Δ_Z. They nevertheless have different outcome-conditioned channels. For ρ_+=|+><+| and post-outcome X+ readout,

  Tr[p+ I^A_0(ρ+)]=1/4,
  Tr[p+ I^B_0(ρ+)]=0.

Thus **POVM effects plus nonselective channel do not determine the selective quantum instrument**, even with complete tomography of both. A selector on their shared fibre cannot be universally correct without more independent input (H117/AX03 pattern). This is a **standard conceptual measurement distinction** with an explicit exact witness.

## AX06.4 — Finite sequential-effect closure and process-tomography criterion

For an independently specified instrument {I_a}, define O_0=C I and
  O_(k+1) = O_k + Σ_a I_a†(O_k).
This spans all effects of permitted finite outcome words I_a1†...I_ak†(I). Dimension increases at most d²−1 strict times. All arbitrary initial density matrices are distinguishable by complete allowed word statistics **iff** O_∞=M_d. If proper, the trace-orthogonal nonzero Hermitian traceless direction creates indistinguishable nearby density states.

**A different theorem** concerns identifying the maps I_a themselves: a fully specified set of preparations spanning M_d and a post-outcome measurement-effect set spanning M_d make the bilinear tomography values Tr[M_j I_a(ρ_i)] informationally complete **for each declared CP map**. On d=2, choosing four independent preparation states and four independent readouts gives linear response-frame rank d^4=16. The method **does not certify unmarked native ports**.

Exact finite examples: repeated Z-Lüders and Z-reset words both yield observable effect rank sequence (1,2,2,2,2); the six-outcome IC instruments give (1,4,4,4). **Even rank4 effect tomography of initial states does not determine the instrument**. In the explicit 4-by-4 process-tomography frame the two selective instruments are distinguishable.

## AX06.5 — H37 population instrument witness (formal, not physical provenance)

For H37 five sites, let p_i=E_ii and take the **same marked population POVM {p_i}** with two formal instruments:

  L_i(ρ)=p_iρp_i,
  R_i(ρ)=E_(0i)ρE_(i0)=Tr(p_iρ)p0.

Starting in p4, first outcome 4 occurs with probability 1 for both. The repeated outcome word (4,4) has probability **1** for Lüders and **0** for reset. Nonselective channels are Δ_D5 and full reset Tr(ρ)p0, respectively. This is a finite instrument-selection witness, **not** a new P6 static J5 candidate or a hardware claim.

AX05's H37 population-plus-time-evolution *ideal* observability rank25 is an input-state information theorem; it cannot certify which of these formal outcome updates is physically native, nor the full two-stage P6 CPTP implementation or a CR-exclusive prediction.

## AX-INSTR certification gate / final verdict

A noncircular claim of physical observer-source/instrument accessibility needs: (i) independently sourced POVM effects and outcome-resolved CP maps (or independent tomography thereof), (ii) known preparations, native controls, reset/feedback policy and two-time calibration, (iii) a valid finite ancilla/dilation **plus a separate hardware capability certificate**, (iv) scope/exhaustiveness of actual source ports, (v) blinded or prospective P6 readout and matched standard GKSL comparator, and (vi) versioned raw data and independent physical review. A mathematical isometry is insufficient.

| Result | Status |
|---|---|
| Finite instruments admit abstract ancilla dilation | EXACT, established |
| IC POVM determines selective instrument | NO-GO on stated data |
| Full POVM + nonselective channel determine selective maps | NO-GO on stated data |
| Sequential effect span stabilizes, distinguishes initial states iff rank=d² | EXACT, conditional |
| Complete pre-/post-frames identify marked outcome maps | EXACT, conditional |
| H37 formal repeated endpoint output depends on instrument | EXACT finite |
| Independently calibrated actual P6 instrument, F-derived source choice, P3 R_k bridge | OPEN |
| P9 Einstein / ADM / HDA, P11 Generative Completeness | OPEN |

**STOP:** Do not invent new J5 sectors or infer physical hardware from an abstract dilation. Continue to AX07 only to integrate the typed P11 axiom/No-Go ledger or on receipt of independently calibrated evidence.

**Reproduce:** run P11_AX06_instrument_realizability_audit.py with Python 3.11 / SymPy 1.14.0. Expect 133 exact finite assertions and JSON output. General principles are argued analytically, **not Lean mechanized** and **not human peer reviewed**.

**Background:** Davies–Lewis quantum instruments, Naimark and Stinespring dilation, and informationally complete measurements; L. E. Fischer et al., “Dual-frame optimization for informationally complete quantum measurements,” Phys. Rev. A 109, 062415 (2024), DOI 10.1103/PhysRevA.109.062415.
