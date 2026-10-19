# P11–AX01 — Finite Observable Quotients and Nonsplit Residue Extensions

**2026-10-19 | P11 axiomatization track, separate from SPS-H113–H123.**
Scope: established Kalman finite-observability theorem, linear extension/residue theorem, exact nonsplit CPTP witness and independent quadratic-return witness. Not an F-generative-completeness result or physical-source discovery.

## AX01.1 Canonical observable Body from finite data

Let V,W be finite-dimensional complex vector spaces, dim V=n, Phi:V→V linear dynamics, C:V→W linear observation. Define

  N_inf=intersection_{k>=0} ker(C Phi^k), and O_n=(C, C Phi, ..., C Phi^{n-1}) stacked.

**Theorem:** N_inf=ker O_n, Phi N_inf ⊆ N_inf. Thus B_obs=V/N_inf has *unique* induced linear maps barPhi and barC satisfying qPhi=barPhi q and C=barC q. Moreover C Phi^k=barC barPhi^k q for all k>=0. Proof: Cayley–Hamilton reduces all powers >=n to powers below n; invisibility is invariant under Phi.

**Minimality:** If another factor T:V→Y is surjective, T Phi=Psi T and C=D T, then ker T ⊆ N_inf, so dim Y >= dim B_obs=rank O_n. The quotient itself attains equality and is exactly observable. It is a minimum **linear output realization** for all initial states, not automatically a CPTP realization or a new finite-dimensional quantum *-algebra.

**Restricted functor:** If (T,S) intertwines (V,Phi,C) and (V',Phi',C') by T Phi=Phi' T and S C=C' T, then T(N_inf)⊆N'_inf, so it descends to observable quotients and respects identity/composition. No naturality under arbitrary physical partial trace is inferred.

The finite-horizon theorem is well known in Kalman observability theory. It gives a precise answer to a bounded form of “how can infinitely many output times close from finite data?” It does not derive the infinite-dimensional universe or F.

## AX01.2 Hidden linear extension and a splitting-independent residue

For a linear section s:B_obs→V of the quotient q, set R_s=Phi s-s barPhi; this maps B_obs into N_inf. If s'=s+t, t:B_obs→N_inf, then

  R_s' = R_s + Phi_N t - t barPhi.

Thus [R] in Hom(B_obs,N_inf)/im(delta), with delta(t)=Phi_N t-t barPhi, is independent of section. The class vanishes iff an invariant section/invariant complement exists. This is a finite module-extension obstruction, **not the original P3 quadratic commutator residue**.

## AX01.3 Nonsplit CPTP witness with a perfectly closed observable Markov chain

Use column-stochastic
P=[[1,1/2,1/4],[0,1/2,1/4],[0,0,1/2]],
C=[[1,1,0],[0,0,1]],
barP=[[1,1/2],[0,1/2]].

Then CP=barP C; N=ker C=C·n where n=(1,-1,0), Pn=(1/2)n. With s(y1,y2)=(y1,0,y2), R_s=n(0,-1/4). Every alternative section s+t with t=n(u,v) yields R_s'=n(-u/2,-1/4-u/2). The **difference of the two residue coefficients is always -1/4**, so no invariant splitting exists. Equivalently the eigenvalue 1/2 has algebraic multiplicity 2 in P but only one eigenvector, n; the visible quotient itself has eigenvalue 1/2.

Lift this to an actual CPTP measure-and-prepare channel on M3 with Kraus K_ij=sqrt(P_ij)E_ij for all positive P entries. Six such Kraus matrices satisfy sum K†K=I. Define observer C_q(rho)=(rho00+rho11,rho22). Then C_q Phi=barP C_q on all M3. The observable quotient has **complex dimension 2**, the hidden N has **complex dimension 7**, and the same nonsplit obstruction persists in the full superoperator (its only eigenvector for eigenvalue 1/2 is p0-p1).

**Precisely:** a Markov-closed observer Body may coexist with a nonsplit microscopic hidden extension. The existence of a hidden extension does not by itself demonstrate operational non-Markovianity of observed output, nor does observed output identify that hidden extension without microscopic input.

## AX01.4 Linear closure does not provide a noncommutative quotient algebra

For M2 with Phi=Delta_D and output C=Delta_D, the invisible subspace N=span_C(E01,E10) is not an operator ideal. Let z=E01. Then

  Delta_D(z z†)=p0 and Delta_D([z,z†])=p0-p1 !=0.

Hence the observable vector-space quotient does not inherit ordinary matrix multiplication. This gives a quadratic visible return of the same **algebraic form** as a P3 diagonal commutator residue, BUT original P3's generated hidden filtration from D can be trivial here, as Phi(D)=D. N_inf is not definitionally P3's H_k(Phi,D).

## AX01.5 Sampling limitation

With C_X(A)=Tr(XA)/2 and Phi=Ad_Z (half-turn samples), Y is invisible for all discrete samples and the observability rank is 1. Under quarter-turn Phi=Ad_diag(1,i), Y becomes visible and the rank is 2. Therefore finite closure for a fixed sampled Phi cannot be equated with continuous-time generator visibility without addressing aliasing.

## Honest status / AX02 gate

- Finite observable quotient, minimality, restricted functor: EXACT / established linear systems mathematics.
- Section-independent extension class and nonsplit Markov/CPTP witness: EXACT.
- Quadratic product/commutator return in a separate dephasing witness: EXACT; NOT the P3-generated hidden filtration.
- General induced *-algebra, positivity, quantum CPTP quotient under arbitrary reductions: **OPEN without added compatibility axioms**.
- Unique physical native primitive source, P6 experimental gate, P9 ADM/HDA/Einstein, P11 Generative Completeness: **OPEN**.
- Next possible AX02: characterize when observation quotient carries an algebraic product/CP-compatible structure, and how it interacts with P3 quadratic residues; do not restart arbitrary H37 J5 candidates.

## Reproduce and review

Run P11_AX01_observer_quotient_audit.py with SymPy 1.14. Expected **74 exact assertions**. Analytic universal statements are proved here, not Lean-formalized. A successful finite CI is neither independent human review nor physical validation. Background on Kalman unobservability: https://mohammadijoo.github.io/CaaT_Academy/Lectures/Modern_Control_Course/Chapter19/Lesson4.html .
