# P11–AX18 — Physical Observer Selection and the G2/G3 Proof Gate

**2026-10-19 | P11 axiomatization | mathematical gate, NOT a physical certificate.** Follows AX17 Draft PR #155. Exact companion SymPy **336 assertions**. General statements are proved analytically here, not Lean-formalized.

## AX18-A (dimension-bounded exact pointer-selection theorem)

Let dim H = d exactly. Let ρ_0,…,ρ_{d-1} be density matrices and {M_0,…,M_{d-1}} a POVM on H such that Tr(M_i ρ_j)=δ_ij.

Then **there exists an orthonormal basis |j> with ρ_j=M_j=|j><j|**. Consequently, D_obs=C*(M_j) is an MASA and the unique trace-preserving conditional expectation onto it is Δ_D(X)=Σ_j M_j X M_j.

**Proof.** For a positive effect M_i≤I and density ρ_j, Tr(M_iρ_j)=0 forces supp(ρ_j)⊆ker M_i; Tr(M_jρ_j)=1 forces supp(ρ_j) into the eigenvalue-1 subspace of M_j. Distinct nonzero support spaces are mutually orthogonal. Exactly d supports in a dimension-d space must all be one-dimensional, and their sum is H. Thus ρ_j=p_j and M_i acts as δ_ij on every p_j, so M_i=p_i. QED.

**Scope:** The verified input is the **independently supplied dimension assumption** and the perfect prepare-and-measure outcome table, **not** a value chosen to maximize P3 residue. This is an elementary case of known dimension-bounded prepare-and-measure certification, not a novel quantum-information theorem. The selected pointer MASA is unique only up to common unitary frame and output labels; no coherent X/Y phase frame follows.

## AX18-B (robust effect error, calibrated-frame version)

Fix separately calibrated orthonormal rank-one inputs p_j. For a POVM with diagonal confusion bounds Tr(M_i p_i)≥1−ε and Tr(M_i p_j)≤ε for j≠i, 0≤ε≤1,

  ||M_i−p_i||_HS² ≤ 2(d−1)ε + (d²−2d+2)ε².

**Proof.** The diagonal squared error is at most d ε². The positivity matrix inequality |(M_i)_jk|²≤(M_i)_jj(M_i)_kk bounds the 2(d−1) offdiagonal entries with one index i by ε, and the remaining (d−1)(d−2) entries by ε². Sum. QED.

For d=5, bound 8ε+17ε². In the exact witness, rotate the first two measurement projections by rational cos=99/101, sin=20/101 relative to independently fixed p_i. ε=400/10201; actual squared HS error for each rotated effect is 2ε. Do **not** extend this fixed-frame robust theorem to an unknown preparation frame without further assumptions.

## AX18-C (sharp limits of the observer-selection input)

**Uncertified dimension:** On H=C^6, prepare only ρ_j=p_j for j=0,…,4. The two normalized 5-outcome POVMs with M_0=p_0+p_5 (other M_i=p_i) versus M_1=p_1+p_5 (other M_i=p_i) give identical perfect 5×5 tables on all supplied inputs. Preparing p_5 distinguishes them. Thus dimension/exhaustiveness are independent source conditions.

**Instrument nonidentification:** On C^5 the Lüders instrument I_i^L(ρ)=p_iρp_i and reset instrument I_i^R(ρ)=|0><i|ρ|i><0| have the **same exact effects** p_i and identical one-shot statistics. From p_4, the probability of two consecutive outcome-4 records is 1 for Lüders and 0 for reset. AX06 two-time/process tomography remains required.

**Residual phase gauge:** Every diagonal unitary V fixes the pointer PVM while rotating offdiagonal signed X/Y references. For V=diag(1,i,1,1,1), V X_01 V†=Y_01. Pointer selection does not provide a P6 physical phase reference, a complete native-control inventory or a canonical F observer.

## H37 and original P3 filtration

Under independently declared H37 H and γ=2/3, the chosen Δ_D yields projected K=E L(I−E)L E of rank 4 (exact check). AX16–AX17 separately established genuine P3 depth-2 R_2 saturation for their specified CPTP channels, but **AX18 does not identify these two differently typed objects** or claim experimentally certified R_2: its positive pointer theorem is conditional on a physically unverified perfect device table/dimension bound.

## Gate table / STOP

| Proof obligation | Status |
|---|---|
| d-dimensional perfect pointer correlation ⇒ pointer MASA and TP expectation | **EXACT, conditional** |
| Independent fixed-frame small ε ⇒ quantitative HS effect closeness | **EXACT, conditional** |
| Perfect 5×5 table implies Hilbert dimension exactly five | **NO** |
| Perfect pointer table determines instrument updates / all native ports / signed phase | **NO** |
| H37 finite K rank 4, relative to declared D_5 | **EXACT mathematics; physical source OPEN** |
| Independent A-DIM, A-PREP, A-POVM, A-PHASE, A-INSTRUMENT, A-INVENTORY | **OPEN physically** |
| P6 experiment and G2 source/observer completeness | **OPEN** |
| F's independent G3 generative completeness | **OPEN** |

The positive operational implication is **conditional observer selection**, not an unconditional F→D derivation. Accept no “device self-test” claim without physically sourced data and a justified dimension bound. Further arbitrary static J5 sectors cannot solve the missing source axiom.

### Reproduction
Python 3.11, SymPy 1.14:

  python research/p11/ax18-physical-observer-selection-20261019/P11_AX18_pointer_source_audit.py

Expected **336/336 finite exact assertions**, JSON with all physical/F gates OPEN. No external human review or complete Lean proof.

### Prior research / priority
- N. Miklin & M. Oszmaniec, *A universal scheme for robust self-testing in the prepare-and-measure scenario*, Quantum 5, 424 (2021), DOI: 10.22331/q-2021-04-06-424.
- A. Tavakoli et al., *Self-testing non-projective quantum measurements in prepare-and-measure experiments*, Science Advances 6, eaaw6664 (2020), DOI: 10.1126/sciadv.aaw6664.
