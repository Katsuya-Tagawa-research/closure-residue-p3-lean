# P11–AX09 — Universal Observable Realization and the Boundary of the Generative Map F

**2026-10-19; P11 axiomatization.** Stacked on AX08 Draft PR #146, not on the separately maintained SPS static-primitive source track. We establish a **relative** observable minimum using *standard rational-series/Hankel theory*. Neither a universal physical model nor the claimed Generative Completeness of F has been derived.

## 1. Correctly type the model BEFORE asking for universal generation

Mark a finite outcome alphabet Σ, a d-level quantum instrument {I_a} of CP trace-nonincreasing maps whose sum is CPTP, an initial density state rho and allowed labelled word protocols. Let p(w)=Tr(I_{a_k}...I_{a_1}(rho)) for w=a_1...a_k and p(empty)=1. On V=M_d(C), dimension D=d², let T_a=I_a, r=rho, f=Tr. Here the instrument, controls, initial state and output alphabet are **independent physical/mathematical inputs**; none has been derived from F.

## 2. The exact relative universal property (previously known)

Put R=span_C{T_w r:w∈Σ*}, N={x∈R:f(T_v x)=0 for all future words v∈Σ*}, and M(p)=R/N. R and N are invariant under every T_a. The operations, distinguished initial state and f therefore descend to M(p). The induced model is reachable and observable and reproduces every word probability.

**Minimality and uniqueness:** any other reachable and observable *linear* representation (V',T'_a,r',f') realizing the identical word series p admits exactly one intertwining linear isomorphism from M(p), taking [T_w r] to T'_w r' for all words. To prove well-definedness, a relation sum_w c_w T_w r∈N implies sum_w c_w p(wv)=0 for every future word v. The target's observability forces sum_w c_w T'_w r'=0. A symmetric argument gives the inverse. Thus the minimum dimension is unique, but this only implies linear similarity, not complete positivity or unitary equivalence of devices.

For the Hankel matrix H_p=(p(uv))_{u,v∈Σ*}, reachable and observable factorization yields

    rank H_p = dim_C M(p) <= D.

All prefix-reachable and suffix-output spans stabilize once words up to length D−1 are included, by finite-dimensional rank monotonicity. Hence the finite Hankel block with prefix and suffix words of length <=D−1 has full rank. This is an exact **finite algorithm for a fixed marked linear representation**, not an origin axiom for an unknown physical instrument.

These are classical theorems in Schützenberger/Carlyle–Paz/Fliess weighted automata realization theory. In particular rank-Hankel=minimal-linear-dimension is described in *Spectral Learning of General Weighted Automata via Constrained Matrix Completion* (NeurIPS 2012), and S. Kiefer, *Notes on Equivalence and Minimization of Weighted Automata* (2020, arXiv:2009.01217).

## 3. Exact CP two-outcome model

Take column-stochastic P=[[3/4,1/3],[1/4,2/3]], emissions D0=diag(3/4,1/4), D1=diag(1/4,3/4), Ta=P Da, initial population r=(2/5,3/5) and f=(1,1). A genuine CP quantum instrument is specified by Kraus operators K_{a,j,i}=sqrt((Ta)_{ji}) E_{ji} on M2; sum_{a,j,i} K†K=I.

Here p(0)=9/20 and p(1)=11/20; joint probability p(00) differs from p(0)². The rank of prefix reachability starts at 1 and reaches 2 after length1, and suffix observability also reaches 2. The finite Hankel has **exact rank2** (verified again at prefix/suffix word lengths 2 and 4). This is an exact finite physical-CP witness of the abstract relative construction.

Similarity S=[[1,1],[0,1]] produces a different linear-coordinate realization of all the same word weights. S is not unitary; **linearly equivalent realizations are not automatically physically equivalent CPTP devices**. A 3-coordinate extension with one unreachable/invisible direction realizes the same p and has the same minimal quotient dimension.

## 4. A physical countermodel to microscopic reconstruction from M(p)

Introduce an independent unmeasured qubit B initially in |+><+|. Compare A-labelled instruments

    J_a^(0)=I_a^A tensor id_B,
    J_a^(1)=I_a^A tensor Ad_Z_B.

For any joint matrix R, any A outcome a and any TP map T_B,

    Tr_B[(I_a^A tensor T_B)(R)] = I_a^A(Tr_B R).

By induction, the **entire set of A-only finite-outcome probabilities and A post-record reduced states** is identical between the two models, although the joint channels are different. If B is independently prepared in |+> and observed in its X basis, id_B yields +1 and Ad_Z_B yields −1 in X expectation after a step. The two micro-sources are not the same, but the minimal A-only Hankel realization is.

This is a bounded non-identifiability witness relative to the declared A-only protocol alphabet, not a universal theorem that all physically realizable controls or interventions cannot distinguish the two objects.

## 5. Do not conflate universal linear realization with universal generative F

**G1:** The fixed instrument/observer protocol has a canonical reachable-observable **linear realization** up to similarity; PASS conditional, with standard prior art.

**G2:** Origin and exhaustive physical identity of the native source, observer effect, and instrument are not reconstructed by H_p; same-series microscopic counterexample; OPEN.

**G3:** A typed category of physical CR objects, independently justified generation and a genuinely source-selective universal characterization of F have not been supplied; OPEN.

If the data are invariant under all U(d) rotations with no symmetry-breaking mark, a rank-one pointer projection fixed by all U(d) cannot be chosen: such an operator must be scalar, hence has rank0 or d. This is a limited symmetry obstruction; an additional noncircular origin axiom could change it.

This result does not establish equality with the original P3 quadratic residue, the P6 experimental phase/native control gate, P9 ADM/HDA/Einstein equations, or F:empty→(Λ,Ω) as a literal set map. It is not a Lean proof of the general categorical statement and has no independent human peer-review.

## 6. AX10 design / STOP

For further universal-property research, specify a nontrivial category **C_CR^phys** of marked microscopic sources, observers and morphisms; define the forgetful functor to measured word-series; exhibit a candidate adjoint or reconstruction law that is independently motivated (not defined by the answer); verify existence, uniqueness and functoriality; and test this AX09 hidden-ancilla pair. If the proposed axioms still admit the pair as inequivalent models with identical observational input, **G2/G3 remain OPEN and no universal physical selection theorem may be claimed.**

Run Python 3.11+ / SymPy 1.14:
    python research/p11/ax09-universal-observable-realization-20261019/P11_AX09_hankel_universal_audit.py

Expected **203/203 exact finite assertions**. The all-words statement rests on the analytic trace identity and rational-series proof, not enumeration to length4. An exact finite CI PASS is not physical apparatus certification or peer review.
