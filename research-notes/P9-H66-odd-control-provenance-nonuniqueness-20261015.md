# H66 — Physical Odd-Control Provenance: Lie Closure, a Fixed-P3-Source Nonuniqueness Theorem and a Conditional Finite Pulse Certificate

**2026-10-15 | P3–P11 Mathematical Bridge → P9 GR-I.** Stacks on audited H65 Draft PR #84. It uses the **same exact connected rational three-site CPTP comparator \(\Phi\)** from H32 throughout the microscopic-source comparison. It never asserts H32's computed hidden-Krylov \(\Xi(H_{\le3})\) is the **independently inherited physical P6 v9.1 microscopic \(\mathcal J_N\)**, or that the newly added knob is part of frozen P6 hardware. A separate conditional physical control catalog is needed even when \(\Xi\) has full rank. The results are ordinary finite QM, not a CR-exclusive discriminator.

## 1. H66.1 — Lie-algebra control threshold: two real exchanges versus one odd extension

On \(\mathbb C^3\), take frozen-P6-like declared real anti-Hermitian exchange directions

\[
A=E_{01}-E_{10},\qquad B=E_{21}-E_{12}.
\]

Their bracket produces a third real skew direction on 02. The space of real skew \(3\times3\) matrices has dimension 3 and is closed under commutators. Thus, because \(A,B,[A,B]\) are independent,

\[
\boxed{\operatorname{Lie}_{\mathbb R}(A,B)=\mathfrak{so}(3)\,,\quad\dim=3.}
\]

No concatenation/commutator of **these real physical exchange controls** produces an imaginary-symmetric odd tangent. This is a control **Lie algebra** result; it should not be confused with the uncontrolled P3 hidden-Krylov candidate or P9.72's richer \(X/Y\) controls.

Now **independently declare one additional** phase-odd anti-Hermitian direction

\[
Q=i(E_{01}+E_{10}),\qquad Q^\dagger=-Q,\quad Q^T=Q.
\]

The adjoint action of \(\mathfrak{so}(3)\) on imaginary symmetric traceless matrices generates the five-dimensional complement of \(\mathfrak{so}(3)\) inside \(\mathfrak{su}(3)\). In particular, \([A,Q]\) gives a nonzero imaginary traceless diagonal generator, and commutation with the other real skew directions generates imaginary-symmetric 02/12 edges and the second diagonal generator. Explicit exact closure reaches 8 independent traceless anti-Hermitian directions:

\[
\boxed{\operatorname{Lie}_{\mathbb R}(A,B,Q)=\mathfrak{su}(3)\,,\quad\dim=8.}
\]

This is a **conditional mathematical possibility**: one declared extra odd control suffices for \(\mathfrak{su}(3)\) Lie-algebra generation, but no P3/P6 physical origin, calibration, controllable timing or independently inherited phase reference is inferred. There is also no implication that a global KKS Lagrangian polarization or Einstein dynamics has been generated.

## 2. H66.2 — same original P3 uncontrolled data, distinct physical control catalogs

Fix H32's one connected CPTP unitary channel \(\Phi=\mathrm{Ad}_{U_3}\) on \(M_3(\mathbb C)\), **with no modifications to \(\Phi\)**. Its genuine original P3 quadratic residue has rank two in the diagonal traceless subspace at depth three; its canonically **computed** candidate \(\Xi(H_{\le3})\) has real rank six. These are uncontested ordinary finite algebraic outcomes within that comparator.

Consider two alternative, separately **declared** control catalogs for this same source:

- **Catalog R:** the two **real physical** anti-Hermitian knobs \(A,B\), with controlled CPTP channels \(\Psi^R_{x,y}=\mathrm{Ad}_{e^{xA+yB}}\circ\Phi\).
- **Catalog C:** the same \(A,B\) plus the **extra odd** knob \(Q\), with \(\Psi^C_{x,y,z}=\mathrm{Ad}_{e^{xA+yB+zQ}}\circ\Phi\).

Both families reduce to **precisely the same** uncontrolled \(\Phi\) at zero controls, so **all original P3 hidden iterates and quadratic residues of that uncontrolled \(\Phi\) are identical**. Furthermore \(A,B,Q\in\Xi(H_{\le3})\) as **candidate tangent members**, yet the **declared physically enabled knobs differ**. Hence:

**Theorem H66.2 (P3-only physical control-selection nonuniqueness).** The exact original P3 uncontrolled filtration and even complete membership of a proposed odd direction in the finite candidate \(\Xi(H_{\le3})\) do **not** determine whether the odd direction belongs to the **physical allowed control manifold**. Both physically stipulated control catalogs are compatible with the *same* uncontrolled finite P3 data. The conclusion is a source-to-control **underdetermination** statement: a real control-manifold/source/intertwiner postulate or independently measured hardware fact is additionally necessary. It is not an assertion that arbitrary controlled CPTP families have the same full process; H50 implies identical *full* controlled process plus instruments is operationally indistinguishable.

**Physical-source caution:** A faithful identification of a microscopic \(\mathcal J\) with frozen-P6 \(\mathcal J_N\), a star/real-control-compatible surjection or embedding, and time/observer intertwining are STILL OPEN. Calling \(Q\) “P3-generated physical” on the grounds that it belongs to computed \(\Xi\) would silently assume precisely the claim being tested.

## 3. H66.3 — exact positive-time conventional CPTP witness for the added physical resource

An explicitly finite, noninfinitesimal conditional experiment can be made with a **rational Cayley** unitary on the extra Q-knob, distinguished carefully from an exponential gate:

\[
U_Q(h)=(I+hQ)(I-hQ)^{-1}.
\]

On edge 01, \(Q^3=-Q\), so for \(h=1/4\),

\[
U_Q=
\begin{pmatrix}
15/17&8i/17&0\\
8i/17&15/17&0\\
0&0&1
\end{pmatrix}.
\]

This is a genuine unitary, so its conjugation is CPTP. On the **same** original diagonal microscopic seed \(d=E_{00}\), compute \(\rho=\Phi(d)\) using H32's unchanged \(\Phi\). Then

\[
\langle E_{00}\rangle_{\rho}=\frac59,\qquad
\langle E_{00}\rangle_{U_Q\rho U_Q^\dagger}=\frac{18605}{23409}
\]

and therefore

\[
\boxed{\Delta p_0=\frac{5600}{23409}\ne0.}
\]

This is a **real operational consequence of declaring an additional coherent control**, not a CR-specific measurement or evidence that frozen-P6 permits \(Q\). It uses the same specified initial state and the same underlying uncontrolled \(\Phi\), but Catalog R has no right to interpret the extra \(z\)-dial as an allowed physical intervention.

For a separate positive Hermitian **coherent preparation** pair \(\rho_\pm=I_3/3\pm i(E_{01}-E_{10})/6\), identical frozen-real population circuits cannot distinguish their transpose-related imaginary coherences (H38/H63). But the independently supplied unitary \(U_Q\) produces the exact population contrast

\[
p_0^+=\frac{409}{867},\quad p_0^-=\frac{169}{867},\quad
\boxed{p_0^+-p_0^-=\frac{80}{289}.}
\]

These fractions, genuine unitarity, source invariants and full 3-versus-8 Lie ranks are all checked using exact Gaussian-rational arithmetic. No pulse is mislabeled as a true exponential for the same Hamiltonian/time; the Cayley gate is one explicit realizable **mathematical** unitary for a declared extra control.

## 4. H66.4 — source-and-instrument-certification gate

For future claims “P3 physically generates an odd phase control” require simultaneously:

1. **Fixed actual source:** a declared physical microscopic \(\Phi,\mathcal J_N\) with a proved relation to original P3 hidden filtration, not just an H32-computed candidate or a change of gauge coordinates.
2. **Microscopic-to-physical tangent assignment:** an independently sourced real-linear, star/anti-Hermitian-compatible \(S\) whose image includes the proposed odd \(Q\), respecting the correct observer/control symmetry and actual P6 control-manifold definition. H64's transpose-equivariant No-Go still excludes any odd image into the original \(\mathcal T\)-even physical W.
3. **Controlled dynamics/intertwining:** actual CPTP microscopic controls \(\Psi_x\), physical controls \(\widetilde\Psi_x\), and a source-to-observer \(\iota\) such that \(\iota\Psi_x=\widetilde\Psi_x\iota\) on a declared relevant operator space for **all physically offered controls**, including switched/concatenated histories. Infinitesimal agreement or a coordinate definition of \(\widetilde\Psi\) by conjugation is not independent provenance. If a quotient observer map is used, H48 kernel preservation \(\Psi_x(\ker C)\subseteq\ker C\) is a necessary condition for autonomous downstream evolution.
4. **Operational phase resource:** explicit preparations, reference-frame conventions, positivity/CPTP instrument branches, and an honest population or coherence response with nonzero conditioned singular value; ensure the claimed signal cannot simply be reproduced by the matched standard QM controlled process (H50).
5. **Continuum/GR separately:** any proposed mean-field KKS dynamics, metric matching, DeWitt negative direction, off-shell HDA and Einstein dynamics demand further independent proofs.

The **H66 result is a narrowly scoped mathematical no-go for selection from the existing uncontrolled P3 data**, together with a conditional positive full \(\mathfrak{su}(3)\) access model. No independently sourced odd-control derivation has been obtained.

## Next stage — H67

Test a concrete source-to-physical controlled-CPTP *nontrivial* intertwiner candidate against H48's kernel-invariance criterion and H50's matched-full-process equivalence; retain real-control no-go if the candidate merely declares an odd source or rephases coordinates. Give P9 an update only if a genuinely new microscopic admissibility criterion or strong source no-go beyond H66's scope is established.

**Verification:** \`python3 P3/P9H66OddControlLieAndSourceNonuniquenessExactCheck.py\`. Staged Draft/unmerged; not a Lean theorem, human expert peer review, actual hardware experiment, P9 Minimum Success, KKS→ADM microphysics, HDA or GR.
