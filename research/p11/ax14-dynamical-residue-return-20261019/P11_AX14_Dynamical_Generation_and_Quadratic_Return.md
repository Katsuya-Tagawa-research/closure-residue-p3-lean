# P11–AX14 — Dynamical Generation and the Necessity of Quadratic Population Return

**2026-10-19; P11 axiomatization, stacked on AX13 PR #151.** Scope: conditional exact GKSL theorem, fixed H37 and triangle finite witnesses, 114 exact SymPy checks. This is **not** the original P3 hidden-filtration quadratic commutator residue R_k or an F-derived source theorem. No P6 hardware certification, P9 gravity, G2/G3 completeness, general Lean proof, or human expert peer review.

## AX14.1 Typed CPTP / closure-return input

On M_n(C) let p_i=E_ii, E=Delta_D be the trace-preserving unital CP diagonal expectation, Q=id-E. **Supply independently** a Hermitian H and dephasing rate gamma>=0, and set

 L(rho)=-i[H,rho]+gamma(E(rho)-rho).

This is a bona fide GKSL generator (Lindblad operators sqrt(gamma) p_i); e^{tL} is CPTP. Define the *AX14 projected dynamical return block*, NOT P3 R_k, by

 K_{E,L}=E L Q L E.

Here E L E=0. Hence E L² E=E L Q L E. Furthermore, since L(E(X))=-i[H,E(X)] is purely off-diagonal and the gamma-dephasing term is killed by the final E,

 **K_{E,L}(X)=-E[H,[H,E(X)]].**

This exact identity is **specific** to the above pure-dephasing + Hamiltonian model. Arbitrary GKSL jumps can produce first-order population transitions and need not satisfy it.

## AX14.2 Conditional existence/iff theorem (quadratic population current)

For all i,

 E L(p_i)=0,
 E L²(p_i)=2 sum_{j != i}|H_ji|²(p_j-p_i).

The j!=i diagonal element of -[H,[H,p_i]] is 2|H_ji|²; the ii entry follows from trace conservation. Therefore **K_{E,L}|D_n != 0 iff H has a nonzero off-diagonal element**, equivalently [H,D_n]!=0. This is a theorem *from assumed off-diagonal H and diagonal observer E*, NOT a theorem deriving H, E, noncommutativity, physical observers, or the generated map F from empty premises.

Analyticity gives p(i→j;t)=Tr(p_j e^{tL}(p_i))=|H_ji|² t²+O(t³) for j!=i. Nonzero coefficient yields strictly positive transition probability for sufficiently small t>0. This is familiar short-time quantum transition/Zeno behavior, not a novelty claim. Context: K. Unnikrishnan, Phys. Rev. A 60, 41 (1999), DOI 10.1103/PhysRevA.60.41.

## AX14.3 Weighted graph Laplacian

For diagonal x=sum_i x_i p_i, K acts as the negative graph Laplacian with symmetric positive weights w_ij=2|H_ij|²:

 K_matrix=-sum_{i<j}w_ij(e_i-e_j)(e_i-e_j)^T.

Thus rank K=n-c(G) for the undirected positive-weight coupling graph. This is standard Laplacian algebra, analogous to P3/P4 motifs but **NOT PROOF** that their weighted Laplacian or P3's quadratic commutator residual are identical to this AX14 block.

### Fixed H37 witness

Use exactly H=diag(0,1/7,-1/9,2/11,-3/13)+(1/2)sum_{i=0}^3(E_{i,i+1}+E_{i+1,i}), gamma=2/3. Then

 K = (1/2) * [[-1,1,0,0,0],[1,-2,1,0,0],[0,1,-2,1,0],[0,0,1,-2,1],[0,0,0,1,-1]],

with rank4, E L²(p0)=(p1-p0)/2, and p(0→1;t)=t²/4+O(t³). The second population derivative is independent of pure-dephasing gamma and of diagonal energy shifts. No hardware-realisable readout/phase reference follows.

## AX14.4 Information-loss and higher-order discriminator

Different H diagonal potentials and different gamma produce identical second-order populations if the hopping magnitudes agree. Nonzero K does **not** identify a unique microscopic source.

Explicit 3-site triangle:

 H_real=[[0,1,1],[1,0,1],[1,1,0]];
 H_flux=[[0,1,i],[1,0,1],[-i,1,0]].

At gamma=1/3 they have identical first and second population derivatives at each p_i because all off-diagonal absolute values equal1, but at p0:

 E L_real³(p0)=diag(4/3,-2/3,-2/3),
 E L_flux³(p0)=diag(4/3,-20/3,16/3).

The oriented gauge-invariant loop quantity Im(H01 H12 H20) is 0 vs -1. Thus further higher-order responses can distinguish this **particular pair**. It does not imply universal higher-order source completeness or independently calibrated time readout.

## Proof ledger

| Claim | Status |
|---|---|
| E L Q L E=-E[H,[H,E(.)]] | EXACT under declared GKSL class |
| Nonzero return iff nonzero off-diagonal H | EXACT conditional |
| Weighted hopping Laplacian and rank formula | EXACT / known finite graph fact |
| H37 coefficient, gamma independence, triangle chiral counterexample | EXACT finite witnesses |
| Arbitrary GKSL produces only quadratic population transfer | NOT CLAIMED |
| K_{E,L} equals original P3 R_k built from generated hidden filtration | OPEN |
| H, E, physically accessible observables derived from F | OPEN |
| Native controls and P6 gate; P9 GR; G2 and G3 completeness | OPEN |

**Next AX15:** import the *exact* original frozen P3 hidden-filtration/commutator-residue definitions; attempt a type-correct map to AX14's projected semigroup block, or establish explicit conditions/obstructions. Do not equate the two quadratic objects based on notation or shared Laplacian shape.

## Reproduce

Run Python 3.11+, SymPy 1.14: python research/p11/ax14-dynamical-residue-return-20261019/P11_AX14_dynamical_return_audit.py. Expected **114/114 exact finite symbolic assertions**; CI also verifies OPEN flags. General analytic statements are not Lean formalized or human reviewed.
