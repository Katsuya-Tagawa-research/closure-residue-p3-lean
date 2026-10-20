# P11–AX24 — Collision Dilation, GKSL Limit and Physical Source Provenance

**20 October 2026 | Stacked Draft on AX23 PR #161 | main unchanged.** This is a conditional construction using standard collision-model and product-formula theory, not a derivation of hardware or the Generative Map F.

## 1. Exact finite unitary collision
Fix a d-level pointer family p_j=|j><j|, rate gamma>0, interval h>0, and **fresh** ancillary systems of dimension d+1 in |0>. Define q=exp(-gamma h), c=sqrt(q), s=sqrt(1-q), and V_j by the real plane rotation

    V_j|0>=c|0>+s|j>, V_j|j>=-s|0>+c|j>, V_j|k>=|k> otherwise.

The controlled unitary U_h=sum_j p_j tensor V_j satisfies U_h* U_h=I. Its conditional bath vectors e_j=V_j|0> have inner products <e_k|e_j>=1 (j=k), q (j!=k), so

    T_h(rho)=Tr_E[U_h(rho tensor |0><0|)U_h*]
            = q rho + (1-q) Delta_D(rho).

Since Delta_D²=Delta_D, T_h^m=exp(mh gamma(Delta_D-id)) **exactly at the collision grid**, assuming each fresh bath has the same state and collisions are independent. It does not hold for an unrefreshed reused ancilla without further conditions.

The bath Gram/Choi matrix is G_q=(1-q)I_d+q J_d, eigenvalues 1-q (d-1 times) and 1+(d-1)q (once). For 0<q<1, the **minimal** pure-environment dilation dimension equals its Choi rank **d**. Our explicit controlled-rotation construction uses d+1 and is **not minimal**. Both facts follow standard Stinespring–Choi theory.

## 2. Full H37: Strang limit rather than exact finite collision
Specify d=5, gamma=2/3, and nearest-neighbor H_j,j+1=H_j+1,j=1/2 (other entries zero). Let A=-i[H,.] and B=gamma(Delta_D-id). The collision–Hamiltonian step
    S_h=exp(h A/2) T_h exp(h A/2)
is CPTP and converges as lim_(m->infty) S_(t/m)^m=exp(t(A+B)), with a local O(h³) and global O(h²) splitting error by the finite-dimensional Strang formula.

Let C=[A,B]. The precise cubic difference operator is
    D3=-(1/24)[A,[A,B]]-(1/12)[B,[A,B]].
Using the 25x25 superoperator on M5, rank D3=11, and
    D3(p0)=(1/36)p0-(1/36)p1 +(i/54)(E01-E10)+(1/144)(E02+E20).
Thus the **whole** H37 semigroup is a limit, not in general exactly equal to an individual finite-time collision step. The authentic original P3 R2 result of AX16 transfers **only to the limiting H37 semigroup at sufficiently small positive sampling time**; it is not re-proved here for every coarse collision.

## 3. Fixed bounded bath no-go for first-order dissipation
For fixed finite bath state tau and fixed bounded Hermitian K on system tensor bath, set U_h=exp(-i h K). Then
    T_h(rho)=rho-i h [H_eff,rho]+O(h²),
    H_eff=Tr_E(K(I tensor tau)).
So the first-order reduced generator is Hamiltonian, *not dissipative*. One needs singular coupling, independent renewal, reservoir limits or other input to obtain a nonzero first-order GKSL dissipator. As an explicit qubit witness, K=Z tensor X, tau=|0><0| gives coherence factor cos(2h)=1-2h²+O(h⁴).

For our U_h, ||U_h-I||=O(sqrt(h)), and a collision Hamiltonian satisfying U_h=exp(-i h K_h) has ||K_h||=O(h^(-1/2)). At fixed macroscopic t, the number of independent bath units grows without bound as h tends to zero. Calling this construction "finite" refers to **each** collision's dimensions, not a fixed-size bath for arbitrarily many time steps.

## 4. Source-provenance audit
|Claim|Verdict|
|---|---|
|Exact dephasing step from specified pointer, fresh bath, collision unitary|EXACT CONDITIONAL|
|H37 GKSL from symmetric collision/Hamiltonian limit|EXACT CONDITIONAL|
|Minimal Stinespring bath dimension for specified T_h|d, EXACT|
|Native control/observer source, actual environment, calibration, independent preparation and renewal|G2 OPEN|
|Noncircular F-selection of H, p_j, gamma, bath, scaling and renewal|G3 OPEN|
|P6 physical readout/provenance, GR, full F-generativity|OPEN|

AX24 is a *constructed* microscopic lift of a prescribed channel, **not** a unique physical explanation, proof of a source inventory, nor an origin ex nihilo. Fixed system-only outputs do not rule out unobserved extra bath dynamics. This respects AX08–AX23 source ambiguity and the distinction between P3's commutator filtration and EL(I-E)LE.

## 5. Reproduction and literature
SymPy 1.14: run python research/p11/ax24-collision-dilation-20261020/P11_AX24_collision_source_audit.py. **263 exact finite assertions** check the controlled bath unitaries, 2/3/5-level Gram and Choi ranks, exact collision effects, H37 Strang cubic matrix/rank, first-order population silence and the fixed-bath obstruction. Finite checks do not themselves prove a continuum limit.

Related existing studies: S. Attal and Y. Pautrat, *From repeated to continuous quantum interactions*, Ann. Henri Poincaré 7 (2006), arXiv:math-ph/0311002. S. Attal and A. Joye, *Weak coupling and continuous limits for repeated quantum interactions*, J. Stat. Phys. 126 (2007), arXiv:math-ph/0501012. Stinespring/Choi and Strang product formula are standard. No new Lean general theorem, experimental test, or human peer review.

**Next independent gate:** if physical environment provenance and genuine native controls cannot be independently established, G2 and G3 must remain OPEN; an engineered dilation is not an origin proof.
