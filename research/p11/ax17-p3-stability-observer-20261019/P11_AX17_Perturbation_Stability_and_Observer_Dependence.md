# P11–AX17 — Perturbation Stability and Observer Dependence of Genuine P3 Residues

**2026-10-19; Draft, stacked on AX16 #154.** Exact finite matrix mathematics; no human peer review, hardware P6 provenance, ADM/Einstein, or F Generative Completeness. Frozen papers remain unchanged. Full standalone proof note is in the AX17 companion ZIP distributed in the research chat.

## P3 original definitions

For a discrete CPTP channel Phi, diagonal MASA D_n with trace-preserving expectation E=Delta_D, Q=I-E:

M_k=span_C{D,Phi(D),...,Phi^k(D)}, H_k=Q M_k,
R_k=span_C{E([z,w†]):z∈H_i,w∈H_j,i+j≤k}.

The audit uses *actual* generated H_i; no independent offdiag E_ij are inserted. R_k is a vector subspace of traceless diagonal matrices, not AX14's different dynamical block E L Q L E.

## AX17-A: open perturbation stability of genuine H37 R2

Consider L_{H,gamma}(A)=-i[H,A]+gamma(E(A)-A) with H†=H and gamma>0 and its CPTP resolvent Phi_R=(I-L)^-1 = ∫₀∞ e^-s e^{sL} ds. This is a **genuine CPTP** map for each admissible parameter. Define h_a=Q Phi_R(p_a), and the four signed residue vectors v_ab=(2i)^-1 diag([h_a,h_b]) for pairs (0,1),(1,2),(2,3),(0,3). The determinant f(H,gamma) of their first four coordinates is real analytic on the entire connected H=H†,gamma>0 parameter domain. AX16 established f(H37,2/3)≠0; AX17 directly recomputes an exact nonzero rational determinant. Therefore a nonempty open neighborhood U of H37 has R2=D5^0, dim_C R2=4, and dim_C H1=4. Because f is a nonidentically-zero real-analytic function, the rank-4 set is **open dense and full-measure** within this **specified** H-plus-dephasing GKSL family (though rank4 need not hold for all parameters).

Independent rational exact witnesses change hopping (1/2→3/5), dephasing (2/3→3/4), both (2/5,1/2), the site detuning (1/7→1/6), and set dephasing=0 (all saturate). Removing all hopping with dephasing positive gives R2=0; local stability does not mean universal rigidity. An actual fixed H37 resolvent with independently rotated observer basis via a rational 3/5–4/5 orthogonal rotation also retains genuine rank4.

## AX17-B: correct deterministic semigroup quantifiers

For sampled Phi_t=e^{t L_{H,gamma}}, use the **same P3 generated** four-residue determinant F(t,H,gamma). AX16's fixed H37 certificate is

F(t,H37,2/3) = -[31890017/2655477015413839626240000] t^26 + O(t^27).

Hence F≠0 for all sufficiently small t>0 at the anchor. For **each fixed** anchor time t in that interval, parameter continuity gives an open perturbation neighborhood U_t with R2=D5^0. The neighborhood may depend on t. A compact window bounded away from t=0 admits a uniform parameter neighborhood. One cannot from these arguments claim **one** perturbation neighborhood works for every arbitrarily small t; no explicit laboratory interval is certified. For any particular parameter with one nonzero time witness, analyticity in t implies at most isolated exceptional times, including all sufficiently small t>0 for that fixed parameter.

## AX17-C: exact fixed-channel observer-switching counterexample

Take U=(I-i(X+Z))/sqrt(3) in M2, Phi=Ad_U; this is a fixed unitary CPTP channel.

* Z-observer D_Z=span{I,Z}: h1=Q_Z Phi(Z), h2=Q_Z Phi^2(Z), dim H1=1, dim H2=2, and E_Z([h1,h2])=(16i/9)Z≠0. Because H0=0 and R2=0, the **first nonzero original-P3 residue is R3**, dim_C=1.
* Rotation-axis observer D_N=span{I,N} with N=(X+Z)/sqrt2: Phi(N)=N, so **H_k=R_k=0 for all k**.

The CPTP channel is identical. Observer dependence is not a hidden change in the Hamiltonian. Independently, under a **simultaneous** unitary change Phi'=Ad_V Phi Ad_(V†), D'=V D V†, one has H'_k=V H_k V† and R'_k=V R_k V†. Hence ranks and first depths are gauge covariant. The audit checks explicit Hadamard covariance. Never equate simultaneous basis covariance with independent observer switching.

## Status / stop

| Claim | Status |
|---|---|
| H37 genuine resolvent R2 locally perturbation-stable | EXACT |
| Open dense rank4 in the specified 5-site H-plus-positive-dephasing family | EXACT conditional analytic genericity |
| Fixed-small-time semigroup local parameter stability (U_t) | EXACT |
| Single uniform U valid down to t=0 for all perturbations | NOT CLAIMED |
| Fixed channel qubit observer D_Z versus D_N changes genuine P3 CRP | EXACT |
| Simultaneous gauge covariance | EXACT |
| F selects physical observer or native P6 source / G2-G3 completeness | OPEN |
| Arbitrary P3 R_k equals AX14 projected dynamical return | FALSE in general (AX15) |

Audit: Python 3.11 + SymPy 1.14. Run the attached AX17 script. Expected **111 exact symbolic assertions**, including six saturated parameter witnesses and one decoupled no-return witness. No numerical rank tolerance is used. This is a model-family structural stability and observer-relativity result, not an experiment and not a new unconditional physical law.
