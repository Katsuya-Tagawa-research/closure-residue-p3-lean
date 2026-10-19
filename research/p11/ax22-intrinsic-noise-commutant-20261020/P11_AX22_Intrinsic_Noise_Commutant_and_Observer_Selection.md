# P11–AX22 — Intrinsic Noise Commutant and Conditional Observer Selection

**2026-10-20. Draft mathematical audit.** Human peer review, hardware source certification, and new general Lean formalization have NOT occurred. Stacked on AX21, with main and frozen papers unchanged.

## Exact algebraic theorem

Fix a known finite Heisenberg GKSL generator on M_d(C):

\[
\mathcal L(A)=i[H,A]+\sum_\alpha
(V_\alpha^\dagger A V_\alpha-\tfrac12\{V_\alpha^\dagger V_\alpha,A\}).
\]

Define intrinsic carré du champ without first choosing any observer algebra:

\[
\boxed{\Gamma_\mathcal L(A)=
\mathcal L(A^\dagger A)-\mathcal L(A^\dagger)A-A^\dagger\mathcal L(A)
=\sum_\alpha[V_\alpha,A]^\dagger[V_\alpha,A]\succeq0.}
\]

The Hamiltonian derivation cancels. The left-hand expression uses only the complete GKSL generator, so it is independent of Lindblad representation gauge and covariant under simultaneous unitary conjugation.

The instantaneous noise commutant is

\[
\boxed{\mathcal N_\mathcal L
=\{A:\Gamma_\mathcal L(A)=\Gamma_\mathcal L(A^\dagger)=0\}
=\{V_\alpha,V_\alpha^\dagger:\forall\alpha\}'.}
\]

A sum of positive matrices vanishes iff each summand vanishes, so these two vanishing conditions are precisely commutation with all noise operators and their adjoints. Thus this is an intrinsic unital star subalgebra.

IMPORTANT: This algebra is instantaneously noise silent, not necessarily invariant under the full GKSL evolution. Do not call it the full decoherence-free algebra without further Hamiltonian commutator conditions.

## Conditional P3 observer-selection gate

When and only when the computed algebra \(\mathcal N_\mathcal L\) is a MASA, the uniquely determined normalized-trace-preserving conditional expectation onto it gives a canonical candidate P3 observer E. The original P3 hidden filtration and commutator residue may then be computed from the actual finite map \(\Phi_t=e^{t\mathcal L}\), WITHOUT an additional manually chosen pointer basis.

The original P3 residue is a *space of diagonal commutators*, not identical to the linear operator \(E\mathcal L(I-E)\mathcal LE\) from AX14. AX15 proves the two need not be equivalent; AX16 proves a special H37 image coincidence.

## H37 exact result

For independently given H37 generator \(\mathcal L(A)=i[H,A]+\gamma(\Delta_D(A)-A)\) with \(\gamma=2/3\), noise operators \(V_j=\sqrt\gamma p_j\) give

\[
\boxed{\mathcal N_\mathcal L=\{p_j:j=0,\ldots,4\}'=D_5,}
\]
\[
\boxed{\operatorname{Tr}\Gamma_\mathcal L(A)=
2\gamma\|A-\Delta_D(A)\|_{\mathrm{HS}}^2.}
\]

Thus D5 is selected by the specified generator itself and is a MASA; the trace identity is an exact quantitative certificate. Changing the Hamiltonian leaves this instantaneous noise algebra unchanged, even though \(i[H,D_5]\) can be off-diagonal, generating genuine P3 hidden directions.

For nondegenerate selfadjoint \(B\) and generator \(\mathcal L=i[H,\cdot]-\kappa[B,[B,\cdot]]\), the noise algebra is the MASA \(C^*(B)\). With minimal eigenvalue gap \(\delta>0\),

\[
\operatorname{Tr}\Gamma_\mathcal L(A)
\ge2\kappa\delta^2\|A-E_{C^*(B)}A\|_{\mathrm{HS}}^2.
\]

## Counterexamples: no general MASA selection

1. Depolarizing generator \(\mathcal L(A)=\operatorname{Tr}(A)I_5/5-A\) has intrinsic noise algebra \(\mathbb CI_5\), dimension 1, not MASA.
2. Pure unitary \(\mathcal L(A)=i[H,A]\) has \(\Gamma_\mathcal L=0\), so noise algebra is full \(M_5\), dimension 25 and nonabelian.
3. Degenerate dephasing with \(B=\operatorname{diag}(0,0,1,1,2)\) gives \(M_2\oplus M_2\oplus\mathbb C\), dimension 9, nonabelian.
4. Nonnormal amplitude damping with jump \(V=E_{01}\) gives only scalar commutant; the adjoint vanishing condition matters.
5. A unitarily invariant depolarizing generator cannot select a unique MASA by a rule equivariant under all U(5), since no MASA is fixed by all inner automorphisms.

Therefore the candidate algebra is INTRINSIC, but not GENERALLY A POINTER MASA.

## Audit and scope

Run the included Python/SymPy audit with sympy==1.14.0. It checks exactly **171 symbolic assertions** covering H37, Hamiltonian changes, unitary covariance, Dirichlet trace identity, spectral gap, scalar/full/nonabelian countermodels, and nonnormal noise.

| Gate | Status |
|---|---|
| Generator intrinsic carré du champ, positivity and commutant | EXACT established mathematics |
| H37 intrinsic D5 and trace norm identity | EXACT conditional on supplied generator |
| All GKSL noise algebras maximal abelian | FALSE |
| Instantaneous noise algebra always fully invariant | FALSE |
| G2 physical generator and full native source provenance | OPEN |
| G3 F selects generator non-circularly | OPEN |
| P6 native hardware, P9 gravity, human peer review | OPEN |

Literature: Curvature-Dimension Conditions for Symmetric Quantum Markov Semigroups (2022), DOI 10.1007/s00023-022-01220-x; Agredo–Fagnola–Poletti, The Decoherence-Free Subalgebra of Gaussian Quantum Markov Semigroups (2022), DOI 10.1007/s00032-022-00355-0.

Next: demonstrate an *independent* physical/generative rule choosing L with falsifiable consequences. Computing its intrinsic noise algebra is not a proof that F generated L.
