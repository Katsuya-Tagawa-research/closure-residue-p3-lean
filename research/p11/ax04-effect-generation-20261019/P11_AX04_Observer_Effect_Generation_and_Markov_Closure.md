# P11–AX04 — Observer-Effect Generation and Markov Closure Compatibility

**2026-10-19 • P11 axiomatization track.** Stacks on AX03 Draft PR #141, distinct from SPS-H113–H123. Status: conditional exact finite matrix algebra theorems and **195/195 exact SymPy tests**. Independent physical POVM sourcing, P3-residue identification, P6 physical gate, P9 GR and P11 Generative Completeness remain **OPEN**. General matrix-algebra closure and invariant observable methods are not claimed as original inventions.

## AX04.1 — Finite minimal invariant effect-algebra theorem (EXACT, finite dimension)

Given independently specified POVM effects M_a on C^d, set A_0=C*(M_a) (unital *-subalgebra). For Schr CPTP Phi let Psi=Phi† be unital CP and define A_{k+1}=C*(A_k ∪ Psi(A_k)). For a continuous semigroup generator use A_{k+1}=C*(A_k ∪ L†(A_k)).

**Theorem:** the sequence stabilizes after at most d²−dim_C(A_0) strict inclusions; its terminal algebra is the unique smallest invariant unital *-subalgebra containing the measured effect algebra. Generator invariance is equivalent to invariance under e^{t L†} for all t≥0.

**Proof:** each strict *-algebra inclusion increases complex vector dimension by ≥1. Equality A_{k+1}=A_k is precisely invariance under the chosen linear map. Every invariant unital *-subalgebra containing A_0 contains each A_k by induction. A finite-dimensional invariant subspace is closed under matrix exponentials, and differentiation at zero gives the reverse. **This construction assumes the initial POVMs are specified; it does not derive the device's observable selection from F.**

## AX04.2 — Exact autonomous-observation condition

Let A⊂M_d be a **specified unital *-subalgebra** and E_A its trace-preserving, unital CP, Hilbert–Schmidt-selfadjoint conditional expectation (AX03). Then

    E_A Phi = E_A Phi E_A    iff    Phi†(A) ⊆ A.

The proof is to take HS adjoints: the left side becomes Psi E_A=E_A Psi E_A. This holds exactly when Psi of every element in Ran(E_A)=A is again in A. Under it Psi|A is a UCP map, hence yields autonomous Markovian dynamics on states of the abstract finite C*-algebra A. Likewise E_A L=E_A L E_A iff L†(A)⊆A, giving closure for all e^{t L} when valid.

**Not automatic:** a linear AX01 observable quotient is not necessarily an algebra; the CE product of AX02 requires an independent CP projection. A single discrete sampled Phi may close although continuous generator dynamics does not.

## AX04.3 — Connected coherent hopping makes full population-effect algebra generate M_N in one step (EXACT all-N)

Let p_i=E_ii, D_N=span_C{p_i}, H=H† and suppose its nonzero off-diagonal entries form a **connected** undirected graph. For L†(a)=i[H,a]+gamma(Delta_D(a)−a) with gamma≥0,

    p_i L†(p_i) p_j = −i H_ij E_ij   (i!=j).

Thus C*(D_N,L†(D_N)) contains every oriented nonzero graph edge E_ij and its adjoint. Products along paths give every E_ij, so it is **M_N(C)**. The statement depends on the **entire declared population effect list**, a connected hopping graph and dephasing dissipator, not on a generically sourced observer.

### Fixed H37 witness

H37: H=diag(0,1/7,−1/9,2/11,−3/13) +(1/2)sum_{e=0}^3(E_{e,e+1}+E_{e+1,e}), gamma=2/3. The effect algebra starts as D5, dim_C=5, but its one-step invariant *-algebra completion is M5, dim_C=25. Importantly, the *linear span* of {p_i,L†(p_i)} has only dimension 9; all 25 matrix-unit directions arise when **multiplication** is allowed. This distinguishes *-algebra completion from AX01's linear observability ranks.

### Single endpoint detector: a five-stage graded tower

Starting only with POVM {p0,I−p0}, the successive *-algebras under generator-adjoining are

    M1 ⊕ C I4 → M2 ⊕ C I3 → M3 ⊕ C I2 → M4 ⊕ C I1 → M5,

with exact complex dimensions **2,5,10,17,25**.

**Proof by induction:** if the algebra at grade m−1 is M_m on sites 0..m−1 plus a common scalar on the remaining tail, nearest-neighbor hopping ensures its L† images are contained in the algebra with an (m+1)-site prefix; no longer-range matrix entry is introduced. The boundary operator

    p_{m−1} L†(p_{m−1}) (sum_{j=m}^4 p_j) = −(i/2)E_{m−1,m}

isolates the next edge. Its adjoint and products isolate p_m and all (m+1)² matrix units on the prefix. Iteration yields the displayed tower; for m=5 the full algebra is invariant. The exact tests check algebra ranks, image containment and every boundary extraction.

**Crucial accessibility restriction:** algebraic products of formal effects and their Heisenberg images need not be implementable as independent apparatus readings or simultaneous measurements. Reaching M5 algebraically does **not** certify informationally complete physical tomography, a P6 independent calibrated X/Y analyzer, or P11's physically sourced observer.

## AX04.4 — Original H37 population observer is not autonomous

With Schr generator L=−i[H,.]+(2/3)(Delta_D−id) and hidden Y01=−i E01+i E10,

    Delta_D(Y01)=0,
    Delta_D L(Y01)=p0−p1 !=0.

Therefore **Delta_D L != Delta_D L Delta_D** and the diagonal-observer subalgebra is not generator-invariant. For diagonal initial p0,

    Delta_D L(p0)=0,
    Delta_D L²(p0)=(p1−p0)/2.

These are exact first and second-order **population visibility** calculations. Do not conflate them with original P3 dynamically generated hidden filtration, its signed quadratic commutator residue R_k, or reduced process-tensor non-Markovianity.

## AX04.5 — Independently supplied effect lists select different observers (relative No-Go)

Fix the *same* qubit phase channel Phi=Ad_U with U=diag(1,i). Declare Z-POVM effects (I±Z)/2 or X-POVM effects (I±X)/2. They generate different 2D algebras A_Z=span{I,Z} and A_X=span{I,X}. Psi(Z)=Z so A_Z is invariant; Psi(X)=−Y not in A_X, and C*(X,Psi(X))=M2 in one step. Consequently a given channel does not tell which physical detector was independently supplied. This does **not** prohibit choosing a mathematical invariant algebra by an additional convention or axiom.

A different baseline dephasing channel Delta_Z preserves both A_Z and A_X (X maps to 0). Thus a **proper** autonomous observed algebra is mathematically possible when the dynamics and effects satisfy the criterion.

## AX04 final ledger and next gate

| Claim | Status |
|---|---|
| Finite stabilized minimum effect-generated invariant algebra | EXACT, standard finite-dimensional algebra |
| Canonical TP expectation + Heis-invariance iff autonomous reduced Schr dynamics | EXACT, conditional |
| Connected H with full population effects → M_N in one *-algebra step | EXACT, conditional all-N theorem |
| H37 D5→M5 and endpoint effect tower 2,5,10,17,25 | EXACT finite witness |
| H37 D5 populations give autonomous Markov closure | **NO** |
| Same channel fixes unique physically present effect list | **NO** in weak marked-effect model class |
| Generated M5 equals experimentally accessible native POVM/control catalogue | **OPEN**, not implied |
| AX04 algebra chain equals original P3 R_k / F intrinsically selects effects | **OPEN** |
| P6 native hardware, P9 gravity/Einstein, P11 Generative Completeness | **OPEN** |

**Next AX05:** Explicitly separate algebraically generated effects from actually instrument-accessible measurement protocols; formulate a non-circular observer-accessibility gate. Repeating arbitrary static J5 choices or reporting physics PASS from symbolic ranks remains prohibited.

## Audit/prior-work boundary

Run with Python 3.11 and SymPy 1.14:

    python research/p11/ax04-effect-generation-20261019/P11_AX04_effect_generation_audit.py

Expected **195/195 exact assertions**; proofs here are analytical and not Lean-formalized; no independent human peer review. Literature context: H. Umegaki, “Conditional expectation in an operator algebra, III,” Kodai Math. Sem. Rep. 11 (1959), DOI 10.2996/kmj/1138844157; M.-H. Chang, *Quantum Stochastics*, CUP (2015), Chapters 5 and 7. The finite *-algebra stabilization mechanism is elementary and is **not a new operator-algebra theorem**.
