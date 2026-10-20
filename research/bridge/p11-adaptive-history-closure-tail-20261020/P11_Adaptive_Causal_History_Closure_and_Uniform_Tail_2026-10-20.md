# P11/P6 Phase 3 — Adaptive Causal History Closure with Uniform History-Tail Gate

**2026-10-20 | P3–P11 Mathematical Bridge | Stacked Draft on PR #181.** The OA-G39–G42 Uniform History-Tail audit remains **unnumbered and unmerged on its independent audit branch**. This new document is a separate original-H75 adaptive-instrument connection and does not assign an H number, rename the earlier audit, or update the H82 Notion authority.

## Scope and assumptions

Use **the unchanged original four-Kraus H75 source** Phi on C^2 (flag) tensor C^3 (site); original site projections Q0,Q1,Q2; a separately granted nonselective site-dephasing CP map Delta; and two **selectively accessible** three-outcome instruments A/B with original H75 conditional-SWAP feedback on outcome 0 only, exactly as in PR #181.

The specified finite future **step alphabet** is:
- one source Phi as a deterministic CPTP step;
- one site-dephasing Delta as a deterministic CPTP step;
- each labelled CP trace-nonincreasing feedback branch G_A,j, G_B,j (j=0,1,2), with Kraus operators W_j L_j and W_j J_j, where W_0=F_fb, W_1=W_2=I; selectively observing a branch label, then conditionally continuing.

Any word in this grammar means an externally authorized sequence of these maps; the past branch outcomes are retained as classical conditioning information for the selected word. Unnormalized branch probabilities are evaluated by CP maps. This **does not** include arbitrary additional coherent ports, reset-external memory, an unrestricted process-tensor laboratory, or a source-selected hardware permit. All physical access and source reuse remain independent assumptions.

## Theorem A — finite adaptive Heisenberg closure (EXACT)

For this specific grammar, define
\[
R_0=\operatorname{span}_{\mathbb R}\{Q_0,Q_1,Q_2\},\qquad
R_{n+1}=R_n+\sum_{g\in\mathcal G} g^*(R_n).
\]
Original-H75 exact rational arithmetic gives the effect-space rank filtration
\[
\boxed{(\dim R_0,\dim R_1,\dim R_2,\dim R_3,\dim R_4)
=(3,7,10,12,12).}
\]
Once R4=R3, invariance under each generator proves R_n=R3 for every subsequent depth n, including arbitrary finite outcome-labelled adaptive paths.

All permitted adjoints preserve the **flag-block-diagonal** real Hermitian 18-dimensional effect algebra. Thus on the *full* Herm(6) state space (36 real), the legal future-observation quotient has rank exactly **12**, nullity **24**. The image of normalized density states has affine dimension **11**, since I6=sum Qj lies in R0 and I6/6 lies in the interior of physical state space.

The prior smaller grammar (#180) with only Phi and unobserved Delta had the exact filtration (3,5,7,9,9). Adding outcome-conditioned feedback therefore strictly refines operational equivalence on **arbitrary cut states**, but does not recover 24 hidden full-state linear directions. On the **actual nine-dimensional H75 source-output image**, the smaller grammar already distinguishes all different output states; the richer tester still has restriction rank 9 there. In particular, there is **no resurrection** of the original source kernel or creation of new P3 information.

### Physically positive strict depth-three example

Define the trace-zero Hermitian six-level H with upper-left qutrit block
\[
H_0=\begin{pmatrix}
0&5i/3&5i/6\\
-5i/3&0&i\\
-5i/6&-i&0
\end{pmatrix},
\quad H=\operatorname{diag}(H_0,0_3).
\]
Then
\[
\rho_\pm=I_6/6\pm(3/160)H
\]
are **strictly positive normalized** density matrices: every off-diagonal perturbation row absolute sum is at most 1/20, strictly below the positive diagonal 1/6. They agree on **all** length-at-most-two tester effects in the declared adaptive grammar (exact 10-dimensional rank), but after three H75 source uses and original Q0 site measurement,
\[
\boxed{
\operatorname{Tr}[Q_0\Phi^3(\rho_+)]-
\operatorname{Tr}[Q_0\Phi^3(\rho_-)]=11/500>0.
}
\]
So depth 3 is a *necessary and sufficient worst-case closure depth* for this explicit finite grammar. These full-rank cut states are not asserted to be prepared as outputs of a prior H75 reset.

## Theorem B — source-specific CP no-event history certificate (EXACT)

Build one legal but **externally authorized** adaptive cycle: apply the original Phi, perform Instrument A (L_j=I2 tensor |j><j|), record its outcome; if outcome 0, apply original F_fb, label the cycle **no-event** and continue; treat outcomes 1,2 as terminating event branches.

The no-event CP trace-nonincreasing map has Kraus operators V_ab=F_fb L_0 K_ab. The two event branches have Kraus operators L_1 K_ab and L_2 K_ab. Their aggregate is CPTP since
\[
\sum_{a,b,j}(W_jL_jK_{ab})^\dagger(W_jL_jK_{ab})=I_6.
\]
Thus the no-event Choi matrix is positive by its explicit finite Kraus Gram factorization. Moreover,
\[
\mathcal N^*(I_6)=I_2\otimes A,\qquad
A=\begin{pmatrix}
4/9&4/15&-2/15\\
4/15&4/9&-2/9\\
-2/15&-2/9&1/9
\end{pmatrix}
\]
has spectrum {0, 1/2-sqrt(745)/90, 1/2+sqrt(745)/90}, where sqrt(745)<30. Hence
\[
\boxed{\mathcal N^*(I_6)\prec(5/6)I_6.}
\]
For any initial density matrix rho and n repeated authorized no-event cycles,
\[
\boxed{\Pr(\text{n consecutive no-event outcomes}|\rho)
=\operatorname{Tr}\mathcal N^n(\rho)\le(5/6)^n.}
\]
The finite numerical cutoff K satisfying (5/6)^K<=epsilon gives an **all-state uniform tail bound for this fixed instrument/schedule**. This is a direct H75 realization of the OA-G42-style quantum CP block-tail certificate, **not** a derivation of that schedule from F. No particular online classical archive dimension follows.

## Theorem C — scheduling-switch NO-GO (EXACT)

Two ordinary 2-state CP trace-nonincreasing no-event branches with Kraus
\[
V_1=|0\rangle\langle1|,\qquad V_2=|1\rangle\langle0|
\]
have V1^2=V2^2=0. Each fixed repeated no-event map therefore obeys a perfect two-step tail certificate (ell=2,b=0); complement Kraus operators sqrt(I-Vj dagger Vj) complete each instrument into a genuine CPTP two-outcome instrument.

Nevertheless, starting from |1><1| and **alternating** V1 then V2, each two-step cycle returns exactly to |1><1| with unit probability. Thus
\[
\boxed{
\text{per-instrument block contraction}
\ \not\Rightarrow\
\text{uniform tail under arbitrary switching}.
}
\]
This 2-state scheduling example is a **separate ordinary-QM counterexample**, not asserted to be the original H75 apparatus.

**Sound joint sufficient condition:** for a fixed allowed adaptive schedule language, verify a common bound \(\mathcal N_w^*(I)\preceq b I\) for **each legally admissible no-event word w of block length ell**, with the same b<1, and ensure actual schedule concatenations are covered by these blocks. Then CP positivity yields the uniform tail \(b^{\lfloor n/\ell\rfloor}\). This is a sufficient condition, not claimed necessary for all models. OA-G42's worst-case tail criterion still provides the general common-cutoff iff at the distributional level.

## P11 handoff and explicit exclusions

**Finite EXACT:** relative adaptive future closure 12D/strict depth 3; true original-H75 CP and all-input contracted selected event tail b=5/6; the switched-schedule counterexample; joint-block sufficient condition. The associated test is standalone exact SymPy arithmetic and bounded finite regression, while the general CP induction and closure argument are mathematical proofs.

**Independent assumptions:** typed permission for the selective A/B instruments, classical record and adaptive policy, fixed Markovian repeated H75 source and site readouts, legal sequence timing/calibration, terminal error model and allowed initial-state family. These are not produced merely by computing an observable quotient.

**OPEN:** F intrinsic production of AX-OA; P6 physical observer and signed CR-current provenance; equivalence between standard Born/instrument memory and original P3 Closure–Residue filtration; unbounded classical-history archive; P7/P8 soldering; fixed-orbit GT–K4 metric descent and KKS→ADM/HDA/Einstein; P11 Generative Completeness. No CR-exclusive physical prediction, real experiment, human peer review, general Lean formalization or changes to published P1–P8.

**Governance:** new stacked Draft bridge PR; unnumbered original OA-G39–G42 audit remains on its separate branch and is not formally merged into H82 pending integrative approval.
