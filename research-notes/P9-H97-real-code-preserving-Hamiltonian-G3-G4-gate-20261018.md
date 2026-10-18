# H97 — Physical Real Hamiltonian Stabilizer of the Genuine H75/H92 Source: an Isotropic Three-Dimensional Control Orbit, Not ADM's Six-Pair Canonical Dynamics

**2026-10-18 | P9 GR-I, G3 physical symplectic/Hamiltonian map & G4 DeWitt provenance; P3–P11 Mathematical Bridge; Route A.**

**Base:** H96 Draft PR #115, latest SHA \`49d1015\`, whose original H96 finite-GKSL/DeWitt checker passed its earlier commit while latest GitHub global CI was pending at H97 start. This is a **DIRECT analysis of the already available H75/H76 real continuous coherent Hamiltonians**, not a new finite reset tomography model, new independent site phase knob, or physical gravity model. Original H75 six-level CPTP/P3 signed residue, main, and frozen published P1–P8 remain untouched.

## 1. Typed input: exactly what is physical and what is conditional

The original genuine six-level flag/site carrier is \(\mathcal H=\mathbb C^2_E\otimes\mathbb C^3_S\). The actual H75 coherent Hamiltonian controls arise from two REAL qutrit skew generators \(A=E_{01}-E_{10}\) and \(B=E_{21}-E_{12}\), lifted to \(K_A=I_2\otimes A,K_B=I_2\otimes B\) on six levels; with H75/H76 finite real gates W and F their **mathematical reversible conjugation/Lie closure** is \(\mathfrak{so}(6)\) (H93 exact). Taking all \(K\in\mathfrak{so}(6)\) as available infinitesimal Hamiltonians is a **generous algebraic upper bound** on actual timed apparatus, not an assertion that finite products realize arbitrary smooth gate pulses exactly.

The fixed complex qutrit unitary U in H75 is part of a **discrete noninvertible CPTP reset**; H94/H95/H96 prove it is not independently certified as an isolated pre-reset physical unitary control. It may be used to **identify source-derived physical support**, but not silently promoted to a new physical Hamiltonian knob.

H92 constructed a true source CPTP checkpoint output on the *same* six-level Hilbert system, supported on a physical five-dimensional subspace \(\mathcal K=\operatorname{Im}V\):
\[
\rho_6=V\sigma_0V^\dagger,\quad
\sigma_0=\frac9{59}I_3\oplus\frac{16}{59}I_2,\qquad
V:\mathbb C^5\hookrightarrow\mathbb C^6.
\]
If **independently supplied** full U(5) coherent flag controls were accessible, its Grassmann KKS orbit would be \(\mathrm{Gr}_2(\mathbb C^5)\) of dimension and symplectic rank 12. H93: the actual real control closure does NOT sweep that U5 orbit. H95/H96: the original discrete reset cannot act as coherent reversible transport on its twelve-dimensional KKS tangent.

**H97 question:** even giving the inherited REAL Hamiltonian Lie algebra the maximal \(\mathfrak{so}(6)\) closure, what is its largest code-preserving subalgebra, and what genuine KKS Hamiltonian orbit does it generate *at the original source state*?

## 2. H97.1 — The code-preserving real skew Hamiltonian Lie algebra is exactly so(4) (EXACT)

Let \(u=U|0\rangle\in\mathbb C^3\) be the true original H42/H75 complex first column and \(\zeta=|1_E\rangle\otimes u\in\mathbb C^6\) the one-dimensional mode excluded from the five-level H92 code. Explicitly,
\[
u=(2i/3,-2/3,-i/3)^\top,\qquad
\zeta=(0,0,0,2i/3,-2/3,-i/3)^\top,
\quad \mathcal K=\zeta^\perp,
\quad P_{\mathcal K}=I_6-|\zeta\rangle\langle\zeta|.
\]
Write \(\zeta=a+ib\) with REAL \(a,b\in\mathbb R^6\). The exact data are
\[
\langle a,b\rangle=0,\quad\|a\|^2=4/9,\quad
\|b\|^2=5/9,\quad \|\zeta\|^2=1.
\]
A real skew-Hermitian matrix \(K\in\mathfrak{so}(6)\) preserves the complex five-plane \(\mathcal K\) iff it also preserves the orthogonal one-complex-dimensional line \(\mathbb C\zeta\). Hence \(K\zeta=i\lambda\zeta\) for some real \(\lambda\), which means \(Ka=-\lambda b,Kb=\lambda a\). The skew condition \(\langle Ka,b\rangle=-\langle a,Kb\rangle\), combined with the unequal norms of \(a\) and \(b\), forces \(\lambda=0\). Therefore
\[
\boxed{
K\mathcal K\subset\mathcal K
\quad\Longleftrightarrow\quad
Ka=Kb=0,\qquad K\in\mathfrak{so}(6).
}
\tag{H97-STAB}
\]
Since \(a,b\) are independent, their common real orthogonal complement has dimension 4 and
\[
\boxed{
\mathfrak g_{\mathrm{code}}
=\{K\in\mathfrak{so}(6):K\zeta=0\}
\cong\mathfrak{so}(4),\qquad
\dim_\mathbb R\mathfrak g_{\mathrm{code}}=6.
}
\tag{H97-SO4}
\]
This is a mathematically *maximal favorable* code-preserving subgroup of the H93 fully generated real \(\mathfrak{so}(6)\) algebra. Direct exact Fraction/Gaussian-rational RREF on all 15 independent skew generators gives a **12×15 constraint matrix of rank 9, kernel dimension 6**, six code-preserving skew basis elements and exact Lie closure. The excluded \(\zeta\) is derived directly from the original H75 source U, **not** an arbitrary designed stabilizer.

## 3. H97.2 — The SO4-compatible SOURCE orbit is 3-dimensional and KKS-isotropic (EXACT)

Grant the corresponding connected code-preserving real group on the same original physical source state \(\rho_6=V\sigma_0V^\dagger\). For every code-preserving real \(K\), its legitimate physical tangent
\[
T_K=[K,\rho_6]
\]
is Hermitian, trace zero, **fully supported inside** \(\mathcal K\), and tangent to the full H92 complex twelve-dimensional Grassmann KKS orbit. However the map \(\mathfrak g_{\rm code}\to T_{\rho_6}\mathcal O\) has exact rank
\[
\boxed{
\dim_\mathbb R\operatorname{span}_{K\in\mathfrak g_{\rm code}}
[K,\rho_6]=3\ll12.
}
\tag{H97-ORBIT}
\]
The exact checker computes the full **6-generator orbit tangents** on original six-level Hermitian matrices and the **rank 3** in rational Gaussian coordinates. This independently strengthens H93's non-constructive orbit-intersection count by producing the actual source-correct stabilizer subalgebra.

More sharply, let \(H_K=iK\) (Hermitian, up to an inessential Hamiltonian sign) and its physical quantum moment-map observable \(h_K(\rho)=\operatorname{Tr}(\rho H_K)\). With H92's KKS sign convention, their Poisson bracket is
\[
\{h_K,h_L\}_{\rm KKS}(\rho_6)
=-i\,\operatorname{Tr}\left[\rho_6[H_K,H_L]\right].
\]
The 6×6 exact rational Gaussian Poisson pairing matrix **vanishes entrywise**:
\[
\boxed{
\omega_{\rm KKS}(T_K,T_L)=0
\qquad\forall K,L\in\mathfrak g_{\rm code}.
}
\tag{H97-ISO}
\]
This is not only a checked accident: since \(K,L\) are real skew and both annihilate \(\zeta\), \([K,L]\) is real skew and annihilates \(\zeta\). The true seed density is
\[
\rho_6=\frac9{59}P_{E=0}
+\frac{16}{59}\bigl(P_{E=1}-|\zeta\rangle\langle\zeta|\bigr).
\]
The trace of a REAL skew matrix against either REAL block projector vanishes, and the \(\zeta\)-expectation of \([K,L]\) vanishes. Thus \(\operatorname{Tr}\rho_6[K,L]=0\), establishing (H97-ISO) without an approximation. The connected \(\mathrm{SO}(4)\) orbit through this seed is consequently a **3-real-dimensional KKS-isotropic** orbit inside the 12-dimensional symplectic Grassmannian. It is **not** itself a symplectic six-pair phase space, and isotropy persists along the connected group orbit by equivariance.

**Avoid category error:** the ambient full \(\mathrm{Gr}_2(\mathbb C^5)\) has nondegenerate rank-12 KKS form; only this restricted *physically real, code-preserving control orbit* has a zero pulled-back KKS two-form. The full orbit is not proven to be physically reachable.

## 4. H97.3 — The actual H75 continuously tunable site Hamiltonians violate the code invariance test (EXACT)

For the original two infinitesimal physical site generators \(K_A=I_2\otimes A\), \(K_B=I_2\otimes B\), their excluded-vector squared norms are
\[
\boxed{
\|K_A\zeta\|^2=\frac89,\qquad
\|K_B\zeta\|^2=\frac59.
}
\tag{H97-KZ}
\]
Both are strictly nonzero, so **neither independently generates a code-preserving continuous Hamiltonian flow** on the physical five-level source support. This is an actual invariant-subspace failure, not a failure of quantum positivity or unitarity.

For genuine source-positive \(\rho_6\), the physically meaningful positive sixth-mode projector \(P_\perp=|\zeta\rangle\langle\zeta|\) has short-time leakage under the genuine continuous site controls \(e^{tK_A},e^{tK_B}\):
\[
\operatorname{Tr}\!\left[
P_\perp e^{tK}\rho_6 e^{-tK}
\right]
=t^2\,\langle K\zeta,\rho_6 K\zeta\rangle+O(t^3),
\]
with exact positive coefficients
\[
\boxed{
c_A=\frac{128}{4779},\qquad
c_B=\frac{464}{4779}.
}
\tag{H97-LEAK}
\]
The checker computes these coefficients directly in the original six-level physical basis using the **same** H75/H92 source state, all-rational complex matrices, and both original H75 continuous Hamiltonians. It also checks their infinitesimal tangents have nonzero coupling from \(\mathcal K\) to \(\zeta\), so this is not merely a finite-Cayley-gate artifact of H93.

## 5. H97.4 — Sharp CONDITIONAL G3/G4 Hamiltonian-intertwining gate, not another dimensional coincidence

Suppose a claimed physical local ADM canonical map \(J\) is required to identify *each* of the six ADM canonical **momentum-translation vector fields** \(X_{p_i}=\partial/\partial q_i\) with a Hamiltonian vector field induced by the **existing real code-preserving controls** \(K_i\in\mathfrak g_{\rm code}\) on the source orbit:
\[
dJ(X_{h_{K_i}})=X_{p_i}\circ J,\quad i=1,\ldots,6.
\]
The six ADM fields \(\partial/\partial q_i\) are independent at every ordinary 6+6 unreduced canonical chart point. But at the exact source state, the available code-preserving real physical Hamiltonian fields span **only three real dimensions**. Consequently
\[
\boxed{\text{No such six-momentum CONTROL-INTERTWINING map exists
at this H75 source point under the existing real code-preserving catalog.}}
\tag{H97-G3NO}
\]
This is a **scoped necessary operational correspondence condition**, NOT the claim that every abstract local Darboux symplectomorphism must preserve this particular real control catalog: a Darboux map exists on the entire H92 U5 Grassmann orbit if one grants the abstract orbit. Nor does canonical GR require experimental ability to independently switch every ADM momentum translation in every physical model; the obstruction concerns the stated **strong physical source-to-canonical-control identification**.

The additional H96 **G4** condition is *distinct*: the actual ADM gravitational kinetic momentum Hessian must have DeWitt inertia \((5+,1-)\) in a justified configuration polarization. The existing source's \(\mathfrak{so}(4)\) moment maps do not even furnish the six independent proposed ADM momentum translations at the seed, so one cannot promote Fisher-positive K4 geometry to a generated gravitational Hamiltonian by this route. H97 does NOT infer a universal Hessian-signature no-go for an unknown source-derived nonlinear gravitational Hamiltonian; local nonlinear canonical changes and added dynamical sectors must be analyzed separately.

## 6. Direct P9 / P11 exit

**P9 G3:** the H75/H76 *maximally favorable* inherited real continuous control closure inside the **true** five-level source support is SO4, generating an **isotropic rank-3 orbit**, not a nondegenerate rank-12 physical KKS Hamiltonian evolution. The original A/B generators leak out of the source support already at infinitesimal order. A genuine ADM canonical/physical dynamical intertwiner now needs a separately **source-justified coherent complex or historical carrier**, actual \(\omega\)-preserving accessible flows and six-pair ADM structure, not another mathematical 12D chart.

**P9 G4–G6:** physical kinetic DeWitt negative conformal direction, spatial gluing, independent full nonuniform off-shell constraint algebra and actual Einstein action/equations remain **OPEN**. The standard ADM target sign is independently verified (H96) but never sourced by H75/P3.

**P11:** \(\Omega\) cannot mean merely *discarded* microscopic phase data. If the program claims that an enlarged physically generative closure preserves and returns it, it must identify the **actual carrier and accessible Hamiltonians**. The exact isotropic real-control SO4 subgroup and H95/GKSL singular-reset bounds are necessary provenance tests for any such claim. F does not yet specify or select this missing physical transport.

**Stopping rule:** H97 is the final existing-H75-control **direct G3 Hamiltonian** audit. Do NOT continue lengthening the H75 finite toy-control sequence and silently relabel local Darboux coordinates as sourced gravity. Resume P9 GR-I at the **field-theoretic physical canonical map / DeWitt-signature action** proof obligations, or create and clearly classify genuinely new F axioms in P11. A NO-GO in the restricted real-control sector is a mathematical delimiter, not evidence against possible alternative sourced physics.

**Verification:** exact Fraction / Gaussian-rational 12×15 real skew constraint nullspace, six-dimensional \(\mathfrak{so}(4)\) commutator closure, six 6×6 Hermitian source orbit tangent matrices with rank3, full zero KKS pairing matrix, exact true H75 first-column values and original A/B positive short-time leakage coefficients, plus H96/H95/H92 regressions. No new Lean formalization, human expert referee, experiment, original-source Einstein equations or universal no-go.
