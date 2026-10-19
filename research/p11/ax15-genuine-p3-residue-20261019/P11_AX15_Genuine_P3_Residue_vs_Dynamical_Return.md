# P11–AX15 — Exact Compatibility Audit: Original P3 Residue vs Dynamical Return

**2026-10-19 • P11 axiomatization** — stacked on AX14 Draft PR #152. Source: Katsuya Tagawa, *Closure–Residue Filtration and Non-Markovian Shadows*, September 15, 2026 P3 v1 candidate. Frozen P3 definitions are imported, not rewritten.

## Definition and type barrier

For a genuine finite CPTP Phi on M_n(C), with diagonal D, E=Delta_D, Q=id-E, original P3 defines:

- M_k(D)=span_C{D,Phi(D),...,Phi^k(D)};
- H_k=Q M_k(D), with H_0=0;
- R_k=span_C{ E([z,w†]) : z in H_i, w in H_j, i+j <= k } subset D^0.

AX14 instead defines a **linear operator** K=E L Q L E : D -> D for a GKSL generator L. R_k is a **subspace**, so literal R_k=K is ill-typed; even R_k=im K is not generally true.

## Countermodel A — K nonzero, all-depth original P3 residue zero

Let H=X/2, L(A)=-i[H,A], U=e^{-i pi X/4}=(I-iX)/sqrt2 and Phi=Ad_U (genuine unitary CPTP).

K(p0)=(p1-p0)/2; K(p1)=(p0-p1)/2, so rank K=1. But U^4=-I, all Phi^j(D) are in span_C{I,Z,Y}, and H_k=span_C{Y} for every k>=1. Thus [z,w†]=0 for all z,w in any generated hidden space, and

**R_k(Phi,D)=0 for every k, although K != 0.**

The raw algebraic identity Delta([E01,E10])=p0-p1 cannot be substituted: those two edge units are **not separately present** in this H_k.

## Countermodel B — genuine P3 R2 nonzero, K zero

Define rho_x=(I+X)/2, rho_y=(I+Y)/2, the genuine measure-and-prepare CPTP channel
Psi(A)=Tr(p0 A)rho_x+Tr(p1 A)rho_y
with Kraus V0=|+><0|, V1=|+i><1|. Let L=Psi-id, a valid GKSL generator with Phi_t=e^{tL}. Since Psi annihilates all offdiagonal matrices, E L Q=0, hence K=0.

Psi^3=Psi^2, so at t=log2 the actual sampled CPTP map is Phi_t=(id+t Psi+(1-t)Psi^2)/2. Its genuine P3 depth-one hidden generators are

h0=Q Phi_t(p0)=[(X+Y)+t(X-Y)]/8,
h1=Q Phi_t(p1)=[(X+Y)-t(X-Y)]/8.

They span H1=span_C{X,Y}, with E([h0,h1†])=i log(2) Z/8 != 0. Therefore

**K=0 and R2(Phi_t,D)=span_C{Z} != 0.**

Together A and B disprove both unconditional nonzero-implications within CPTP/GKSL dynamics.

## Conditional positive image theorem

Restrict to L=-i[H,.]+gamma(E-id), H Hermitian, gamma>=0, and actual Phi_t=e^{tL} for fixed positive t. Let G be the graph of nonzero H_ij edges; W_G=span_C{p_i-p_j: {i,j} an edge}. Direct computation yields

K(p_i)=2 sum_{j!=i} |H_ji|^2 (p_j-p_i);
**im K=W_G**, rank(K)=n-c(G).

Add an **independent P3-hidden-edge resolution hypothesis**: for each graph edge {i,j}, matrix unit E_ij belongs to genuine H_m(Phi_t,D) for some common finite m (one orientation suffices by *-closure).

Then **R_{2m}(Phi_t,D)=W_G=im K**. Each edge E_ij produces E([E_ij,E_ij†])=p_i-p_j, so W_G is included in R. All Phi_t generated hidden matrices preserve connected blocks, so any residue commutator is traceless in each block, giving reverse inclusion.

The edge-resolution hypothesis is not implied merely by graph connectivity. Equality here is of **two subspaces**, not of maps or coefficients. In another positive two-level GKSL witness, L_mix=-i[X/2,.]+Psi-id has linearly independent hidden derivatives QL_mix(p0), QL_mix(p1), leading P3 commutator iZ, and rank K_mix=1. By analyticity of Phi_t at t=0, for all sufficiently small t>0 genuine H1=offdiag full space and R2=im K_mix=span Z. This mixed-dissipator witness is not presented as a special case of the pure-dephasing-only graph theorem.

## H37 boundary

For the original H37 five-site path, with four hopping amplitudes 1/2 and gamma=2/3, AX14's projected return satisfies K=-(1/2)L_path5, rank K=4 and im K=D5^0.

**OPEN:** the original P3 H_m and R_k for actual sampled Phi_t=e^{t L_H37}; this note does not verify the edge-resolution assumption in H37. Do not substitute the rank4 of K for a P3 residue rank, or claim original P3 residue matches AX14 at an unspecified depth.

## Audit and nonclaims

- Original P3 R_k type and depth rule — SOURCE VERIFIED.
- Both unconditional implications between genuine P3 R_k and dynamical K — FALSE, exact countermodels.
- Conditional equality of images when P3 hidden edge-matrix resolution holds — EXACT conditional.
- H37 projected K rank4 — EXACT; original H37 P3 filtration — OPEN.
- P3 Lean/paper changed — NO.
- Physical P6 apparatus, original P3 R_k identification for H37, P9 Einstein, P11 G2/G3 — OPEN.

Run Python3 + SymPy 1.14: python research/p11/ax15-genuine-p3-residue-20261019/P11_AX15_original_P3_residue_audit.py. Expected **94 exact symbolic assertions** and generated JSON flags. Analytical all-depth/conditional theorems are not formalized here in Lean. CI is not peer review or hardware evidence.

Next AX16, only if warranted: derive genuine H37 P3 hidden filtration and finite sampled residue depth, with exact evidence; not by relabeling K.
