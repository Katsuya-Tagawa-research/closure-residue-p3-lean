# H91 — Source-Specific KKS Rank Obstruction at a Genuine CPTP Reset Checkpoint

**2026-10-18 | P9 GR-I / P3–P11 Mathematical Bridge / Route A (Constructive)**

**Base:** H90 Draft PR #109, CI **100/100 PASS**. This note makes the first *source-specific* checkpoint algebra/Poisson-rank comparison with the full six-pair ADM fiber, rather than replacing the H75 six-level microphysics by the independent four-level U(4) comparator used in H59/H87–H89. All branches remain Draft/unmerged. Main and frozen P1–P8 remain unchanged.

## 1. Actual microscopic checkpoint state family, not a fictitious U(4) orbit

Retain the exact H75 four-Kraus microscopic CPTP source on \(\mathbb C_E^2\otimes\mathbb C_S^3\), with original signed P3 diagonal witness
\[
R_2=0,\qquad
R_3=\frac{i}{135}\operatorname{diag}(-32,16,16,0,0,0)\neq0.
\]
For the specified physical **reset protocol** with an initially fixed flag, let
\[
\mathcal J(\rho)
=\Phi_\mu(|0\rangle\langle0|_E\otimes\rho),
\qquad \rho\in\mathcal D(\mathbb C^3).
\]
H79/H80 proved that all \(\mathcal J(\rho)\) have five-level support and the *CP sufficient* output algebra is
\[
\boxed{\mathcal A=M_3(\mathbb C)\oplus M_2(\mathbb C)}
\tag{H91-A}
\]
of **complex linear dimension 13**, and that its faithful complete checkpoint quantum-state recovery requires Hilbert dimension \(\ge5\) and complex-linear encoder rank \(\ge13\). These are statements about physical CP sufficient memory at mandatory reset checkpoints, not general off-checkpoint observers.

After a **fixed blockwise unitary basis rotation** by the original H42 qutrit \(U^\dagger\), the five-dimensional output is exactly
\[
\boxed{
\widetilde{\mathcal J}(\rho)
=M_0\rho M_0\ \oplus\ 
\frac{16}{25}\bigl(P_{12}\rho P_{12}\bigr)\big|_{\operatorname{span}\{|1\rangle,|2\rangle\}},
\quad M_0=\operatorname{diag}(1,3/5,3/5).
}
\tag{H91-J}
\]
The original flag-1 qutrit output has a *third* zero direction in the rotated basis, which is precisely the omitted sixth Hilbert dimension. The exact checker verifies (H91-J) against **all nine** input qutrit matrix units of the unchanged H75 micro Kraus channel, not just diagonal probabilities.

### H91.1 — The genuine single-checkpoint output family has only eight real parameters (EXACT)

Because \(M_0\) is **invertible**, the first summand \(M_0\rho M_0\) uniquely identifies \(\rho\). Thus \(\widetilde{\mathcal J}\) is a real-linear injection of the 9-real-dimensional Hermitian qutrit space into the 13-real-dimensional Hermitian part of \(\mathcal A\). When restricted to physical trace-one qutrit states it is an injective affine immersion of an **8-real-dimensional** full-rank state manifold:
\[
\boxed{\dim_\mathbb R \widetilde{\mathcal J}
\bigl(\mathcal D_+(\mathbb C^3)\bigr)=8.}
\tag{H91-DIM}
\]
The full *ambient* trace-one Hermitian state space of the **sufficient algebra** \(M_3\oplus M_2\) has dimension \(9+4-1=12\). **These are not the same state family.** H80's rank-13 sufficient *algebra* means 13 independent operators are necessary to recover all possible source states under complete CPTP decoding; it does **not** imply that a single H75 reset output scans all twelve affine degrees of freedom.

**Scoped dimension obstruction:** Any differentiable map from **this one-state checkpoint image alone** to an open twelve-dimensional ADM 6+6 canonical chart has rank at most 8; it cannot be a local symplectomorphism / open phase-space chart. Other physical *histories*, multiple cells, additional quantum registers, or independent off-reset controls lie outside this restricted statement.

## 2. H91.2 — Natural KKS Lie–Poisson leaves of the 13-operator CP sufficient algebra have rank \(\le8\) (EXACT)

Grant *optimistically* the full block-preserving unitary Lie group \(U(3)\times U(2)\) acting on all states of (H91-A); this is a mathematical allowance, **not** an independently proved physical H75 hardware catalog. Its Lie–Poisson bracket on the real dual of Hermitian \(\mathcal A\) is
\[
\boxed{
\{f_A,f_B\}(\sigma)=-i\,\operatorname{Tr}_{5}
\bigl(\sigma[A,B]\bigr),\qquad
A,B\in\mathcal A_{\rm sa}.
}
\tag{H91-KKS}
\]
For a block-diagonal \(\sigma=\operatorname{diag}(\alpha_1,\alpha_2,\alpha_3)\oplus
\operatorname{diag}(\beta_1,\beta_2)\), the KKS root-plane pairings are
\[
\{x_{ab},y_{cd}\}=2(\alpha_a-\alpha_b)\delta_{(ab),(cd)}
\quad\text{for }a<b\le3,
\]
and analogously \(2(\beta_1-\beta_2)\) in the \(2\times2\) block. Between blocks all allowed observables commute exactly. Therefore
\[
\boxed{
\operatorname{rank}\Pi_{\mathcal A}(\sigma)
=
2\,\#\{a<b\le3:\alpha_a\neq\alpha_b\}
+2\,\mathbf1_{\beta_1\neq\beta_2}
\le 6+2=8.
}
\tag{H91-RANK}
\]
For non-diagonal states conjugate by block unitaries to this form; Poisson rank is unchanged. A generic full block-spectrum orbit has real dimension
\[
\dim\mathcal O_{\rm gen}
=(3^2-3)+(2^2-2)=\boxed8,
\]
not 12. The ambient twelve-real-dimensional trace-one block state space has **four independent local Casimir/spectral directions**, i.e. it is a **rank-8 Poisson manifold generically**, not a symplectic twelve-manifold. Example local Casimirs are the block traces (one independent after fixing total trace), and three further independent block power sums/eigenvalue invariants.

**Actual sourced reference state is even more degenerate:** for \(\rho_\star=I_3/3\),
\[
\widetilde{\mathcal J}(\rho_\star)
=\operatorname{diag}(1/3,3/25,3/25)
\oplus\operatorname{diag}(16/75,16/75),
\]
and there are only two unequal first-block pairs; second block is scalar. Therefore
\[
\boxed{\operatorname{rank}\Pi_{\mathcal A}(\widetilde{\mathcal J}(I_3/3))=4.}
\tag{H91-REF}
\]
For the equally positive physical qutrit input \(\rho_{\rm gen}=\operatorname{diag}(1/2,1/3,1/6)\),
\[
\widetilde{\mathcal J}(\rho_{\rm gen})
=\operatorname{diag}(1/2,3/25,3/50)
\oplus\operatorname{diag}(16/75,8/75),
\]
and every within-block eigenvalue pair is unequal, so rank \(=8\). The checker constructs the exact 13×13 Hermitian-observable Poisson matrices, calculates their **Fraction Gaussian ranks 4 and 8**, and verifies all block commutators and Casimir annihilation.

**Warning:** the eight-real-dimensional sourced image \(\widetilde{\mathcal J}(\mathcal D_3)\) is not itself claimed to be a full natural KKS orbit or Poisson submanifold. The rank-eight statement applies to the **ambient block algebra's intrinsic KKS coadjoint leaves**, and the rank-eight source-image statement is a **separate smooth dimension bound**. Conflating these two spaces would invalidate the conclusion.

## 3. H91.3 — A sharp source-specific NO-GO for an unextended checkpoint-only ADM canonical identification

Let \(T^*\mathrm{SPD}(3)\) denote a local unreduced ADM canonical **one-spatial-point fiber** with six independent metric coordinates and six conjugate momenta. Its symplectic two-form is nondegenerate (rank 12). Then:

**Theorem (two independent checkpoint-only obstructions).**

1. **Actual checkpoint family:** No map from the 8-dimensional genuine H75 single-reset family \(\widetilde{\mathcal J}(\mathcal D_+(\mathbb C^3))\) can be a local diffeomorphism onto an **open 12-dimensional ADM fiber** (rank obstruction).
2. **Full sufficient checkpoint algebra:** No **Poisson local diffeomorphism** between a neighborhood in the trace-one Hermitian space of \(\mathcal A=M_3\oplus M_2\), with its **natural intrinsic \(U(3)\times U(2)\) Lie–Poisson structure**, and a neighborhood in a rank-12 ADM canonical fiber can exist. A Poisson diffeomorphism preserves the pointwise Poisson rank, yet the former has rank at most 8.

The theorem is stronger physically than simply importing H87's independent **U(4) orbit** of dimension 12. It demonstrates that **the actually source-derived H79–H80 minimal checkpoint algebra does not itself supply the required 12D KKS symplectic leaf**. H59's compact-orbit/global exact cotangent flux restriction remains a further independent obstruction even if a local rank-12 source were later found.

**Precisely what is NOT ruled out:** (a) more than one checkpoint state / a history-dependent enlarged state, (b) coherent flag-off-diagonal operations **before** the mandatory reset and an enlarged accessible algebra, (c) tensor-product multi-cell sectors, (d) symplectic reduction or different quotient targets with fewer physical canonical degrees of freedom, (e) independently sourced extra symplectic degrees or a wholly **different** Poisson structure on the ambient 12-dimensional state space, (f) restricted minisuperspace ADM sectors of dimension \(\le8\). The last case is not the full unreduced six-pair Einstein/gravitational field sector. No blanket claim about all possible KKS-ADM maps, unknown F axioms, or Einstein solutions is made.

## 4. H91.4 — Exactly how many new canonical directions would be necessary?

In a **direct product symplectic completion** that retains a generic intrinsic checkpoint KKS leaf of rank 8 as a factor, reaching a twelve-real-dimensional ADM canonical fiber requires at least
\[
\boxed{12-8=4\ \text{extra real symplectic directions}=2\ \text{extra canonical pairs}.}
\tag{H91-NEED}
\]
At the reference \(\widetilde{\mathcal J}(I_3/3)\) where the intrinsic Poisson rank is only 4, a product completion at that point needs at least **8 additional symplectic directions = 4 canonical pairs** to attain rank 12 there.

These numbers are **necessary only in the specifically declared product/completion setting**; they are neither a physically realized P3-generated oscillator/field sector nor a lower bound against any non-product reorganization, altered Poisson bracket, multi-cell entangled histories or constraints.

A valid repair candidate must therefore present a precise physical *domain*, its true symplectic structure and rank, **actual observed** canonical q/p coordinates, and a Hamiltonian/constraint generator whose pullback matches real ADM dynamics. Merely noting that the sufficient checkpoint state space has 12 real affine coordinates, or that H87's independent U4 orbit has 12 symplectic dimensions, does **not** meet this requirement.

## 5. P9 GR-I / P11 generative handoff and exit criterion

**P9 G3 canonical-bridge obstruction made more precise:**
\[
\begin{array}{ccccc}
\text{actual H75 reset family} &(8\ \text{real params})&
\not\cong&
\text{ADM open 12D canonical fiber},\\
\text{H79–80 checkpoint KKS leaf} &(\operatorname{rank}\le8)&
\not\cong_{\rm Poisson}&
\text{ADM rank-12 canonical fiber}.
\end{array}
\]
To move the physical P9.64/G3 research forward, one must establish a **new physical dynamical sector** beyond this one-checkpoint block algebra (e.g., source-derived coherent interblock coupling, sequential memory/history, or multi-cell field organization), prove rank-12 symplectic accessibility on the true physical states, and only then seek an ADM-covariant physical solder, \(\omega\)-preserving canonical map and Hamiltonian/constraint intertwining. DeWitt \((5+,1-)\), the nonuniform off-shell HDA, Einstein action/equations remain **separate OPEN gates** (H61/H90). The existence of real rank-12 **state-space coordinates** is not enough.

**P11:** write the generative rule that upgrades finite closure data from a single-reset sufficient CP operator algebra to additional *physical* symplectic directions. Such a rule must specify real controls/preparations/readouts and show why the operational state/constraint sector is the one selected by \(F\), rather than assuming an independent U4 comparator. Distinguish the source-image manifold, sufficient C*-algebra, KKS coadjoint orbit, and target ADM phase space as separate types. AX-OA, AX-SP, AX-CAN and AX-DYN remain independently required unless derivable.

**Result ledger:**
- **EXACT:** original H75 micro source and H79/H80 five-level M3⊕M2 CP memory premises, 8D actual reset-image, 13 complex-dimensional sufficient operator algebra, 12D ambient trace-one block states.
- **EXACT / scoped NO-GO:** intrinsic block KKS maximum rank 8; at actual reference rank 4; consequently no unextended checkpoint-only **Poisson local diffeomorphism** to unreduced ADM rank12.
- **CONDITIONAL necessary:** direct-product completion at generic rank8 needs at least two more symplectic canonical pairs.
- **OPEN:** source-derived coherent/infinite/historical symplectic enlargement, physical ADM mapping, DeWitt kinetic mechanism, all full ADM HDA, Einstein equations, P11/F generative completeness and CR-specific experimental signature.

**Audit:** standard-library exact Fraction/Gaussian rational verification of nine genuine source matrix-unit outputs, rank-nine image on full Hermitian qutrit input and rank-eight trace-one tangent, full 13-Hermitian observable intrinsic KKS Poisson ranks 4/8 and 4 Casimir nullities, and rank12 target canonical symplectic matrix. Run retained H79/H80 and H82/H90 regressions in GitHub Actions. This is an exact finite research/computer audit under written hypotheses, not Lean kernel proof, human expert peer review, or Einstein dynamics.
