# H45 — Exact parity-polynomial form of genuine P3 quadratic residue and minimal *seed-labelled* odd information

**2026-10-15 | P3–P11 Mathematical Bridge.** H45 is stacked on H44 Draft PR #63. Uses **the same fixed H42 reflection-equivariant 3-site rational-unitary CPTP update** \(\Phi(X)=UXU^\dagger\). All results in this note are about **actual original P3** hidden iterates and signed commutator residue, not generic population leakage. They are fully predicted by standard quantum mechanics and not claimed CR-exclusive, a new P6 microscopic provenance theorem, or Einstein/ADM/HDA dynamics. Frozen papers and main untouched. No Lean kernel formalization, human expert refereeing or laboratory result.

## 1. Exact full diagonal-seed decomposition: a two-coordinate quadratic return

For a **Hermitian diagonal seed** \(d=\operatorname{diag}(a,b,c)\) with arbitrary real entries (density preparations when all a,b,c≥0 and a+b+c=1), write
\[
u=\frac{a+c}{2},\qquad e=b-u,\qquad q=\frac{a-c}{2},\qquad
d=uI+eE_{11}+q(E_{00}-E_{22}).
\]
The parity-even seed is \(\mathcal T(d)=uI+eE_{11}\), which is exactly what the H44 augmented even quantum observer retains at preparation. The **one omitted real odd seed label** \(q\) is the signed left/right population imbalance. It is distinct from H44's dynamically missing even-chord memory \(m=\mathrm{Re}\rho_{02}\): q is an **initial preparation label**, not a memory coordinate that the even observer can infer from its future histories.

Define genuine original P3 hidden depths:
\[
h_j(d)=Q_D\Phi^j(d),\quad j=1,2.
\]
The signed legal depth-three witness is
\[
R_{1,2}(d,d')=\Delta_D([h_1(d),h_2(d')^\dagger]).
\]
With the two reference seeds \(d_e=E_{11}\) and \(d_o=E_{00}-E_{22}\), let \(h_j^e=h_j(d_e)\), \(h_j^o=h_j(d_o)\). Since \(Q_D\Phi^j(I)=0\), **for every real diagonal seed**
\[
h_j(d)=e\,h_j^e+q\,h_j^o.
\]
The following four original P3 commutator matrices are exact:
\[
\begin{aligned}
R_{ee}&=\Delta_D([h_1^e,h_2^e])
=\frac{i}{81}\operatorname{diag}(-8,16,-8),\\
R_{oo}&=\Delta_D([h_1^o,h_2^o])
=3R_{ee}=\frac{i}{81}\operatorname{diag}(-24,48,-24),\\
R_{oe}&=\Delta_D([h_1^o,h_2^e])
=\frac{i}{81}\operatorname{diag}(24,0,-24),\\
R_{eo}&=\Delta_D([h_1^e,h_2^o])
=3R_{oe}=\frac{i}{81}\operatorname{diag}(72,0,-72).
\end{aligned}
\]
These are all anti-Hermitian traceless diagonal, each with genuine P3 depth \(1+2=3\). The lower-depth \(1+1=2\) original P3 residues vanish in this fixed model (H42).

**Theorem H45.1 — complete ordered-pair Hermitian-diagonal depth-three return formula.** For **independently** chosen diagonal seeds \(d,d'\) with parity coordinates \(e,q\) and \(e',q'\):
\[
\boxed{
R_{1,2}(d,d')
=(ee'+3qq')R_{ee}+(3eq'+qe')R_{oe}.
}
\]
This follows from exact real bilinearity and the four reference commutators. In particular,
\[
\boxed{R(d)=R_{1,2}(d,d)
=(e^2+3q^2)R_{ee}+4eqR_{oe}.}
\]
**Scope:** d,d' are Hermitian diagonal, so e',q' are real. For arbitrary complex diagonal inputs, second-slot anti-linearity requires \(\overline{e'},\overline{q'}\) in the formula; the complex-linear span of all witnesses remains the same. This note does **not** identify this **particular** signed \(R(d)\) with the whole linear residue space \(\mathcal R_3\).

## 2. Exact bilinear minimal features and original P3 filtration rank

The full two-input bilinear return takes values in two independent **diagonal parity directions**:
\[
R_{ee}\;\text{(reflection-even)},\qquad R_{oe}\;\text{(reflection-odd)}.
\]
Consequently its image has **complex rank two**; the exact original P3 residue space is
\[
\boxed{\mathcal R_2=\{0\},\quad
\mathcal R_3=D_3^{0},\quad\dim_{\mathbb C}\mathcal R_3=2.}
\]
Every Hermitian-diagonal ordered witness is determined by exactly the **two real bilinear coordinates**
\[
\boxed{s_+=ee'+3qq',\qquad s_-=3eq'+qe'.}
\]
As an **output-linear representation in fixed parity basis vectors**, two independent scalar coordinates are necessary and sufficient since the image rank is two. This is **not** a claim that the underlying unknown seed q has two degrees of freedom.

For **reflection-even-only diagonal seeds** q=q'=0, only \(R_{ee}\) survives; the residue rank is one. Thus restricting the initial observer to a collective even seed changes the actual *set of original P3 witnesses*, and cannot be silently equated to the full-D3 filtration.

For a **single seed**, the odd×odd return is the explicitly one-dimensional invariant
\[
\boxed{
R_{oo}(d)=q^2R_{oo}=3q^2R_{ee}
}
\]
and therefore **does not itself add a new residue-space direction**: it alters the coefficient of the existing even diagonal return. The **mixed even×odd** term \(4eqR_{oe}\), in contrast, supplies the independent reflection-odd diagonal P3 direction required for \(\dim\mathcal R_3=2\).

## 3. Minimal extra *preparation information* relative to H44's even observer

**Theorem H45.2 — one signed real odd seed label is necessary and sufficient, within the fixed Hermitian-diagonal preparation class.** Assume the exact microscopic U is known and the even observer retains \(\mathcal T(d)\), hence u,e, but not signed q.

**Sufficiency:** retain **one signed real value \(q\) per independently prepared diagonal seed**. Then \(d=\mathcal T(d)+q(E_{00}-E_{22})\), so the original \(h_1(d),h_2(d)\) and all later hidden iterates can be computed, and the formula above reconstructs all signed depth-three ordered mixed P3 witnesses. No reconstruction of a generic 4-complex-dimensional parity-odd operator sector is required **for these labelled diagonal preparations**.

**Necessity for the full signed witness:** H44's entire even observer history (including the extra even chord memory) is insensitive to q. Even knowing **q²**, or the reflection-even part of the signed P3 residue, generally does not suffice to recover the parity-odd signed output. Explicitly choose two *physical, normalized* diagonal states
\[
d_\pm=\operatorname{diag}(3/8,1/2,1/8),\
\operatorname{diag}(1/8,1/2,3/8).
\]
Both have the same even preparation \(u=1/4\), \(e=1/4\), identical all-time even observer outputs, and \(|q|=1/8\), but their signed original depth-three witnesses differ:
\[
\boxed{
R(d_+)-R(d_-)=\frac{2i}{27}
\operatorname{diag}(1,0,-1)\ne0.
}
\]
Therefore no deterministic procedure based only on even observables and q² can return the full signed \(R\) for all allowed diagonal physical preparations. One additional **signed real odd preparation coordinate** is both enough and cannot be completely omitted. The wording "minimal" is relative to ordinary linear/signed seed coordinates, not a claim about all abstract encodings of a real number or information-theoretic bit complexity.

At exceptional symmetric preparations e=0 the mixed odd contribution vanishes, and **for that one special input family** q² alone suffices to calculate \(R(d)\). This does not remove the requirement for arbitrary e.

For example with \(d_0=E_{00}\), \(d_{\rm av}=(E_{00}+E_{22})/2\), the same even linear history still has
\[
\mathcal T R(d_0)-R(d_{\rm av})
=\frac{i}{81}\operatorname{diag}(-6,12,-6)
=\frac14R_{oo},
\]
the exact **odd×odd quadratic return** of H44.

## 4. Distinct tasks: selected signed witness, all depth-three bilinears and full dynamic provenance

The conclusion has three nested scopes that must not be conflated.

- **Selected same-seed signed \(R(d)\):** parity-even preparation data plus one real signed q suffices, and generically q's sign is necessary.
- **All ordered depth-1×depth-2 original P3 Hermitian-diagonal bilinears:** retain one q **for each independently chosen input seed** and use \((s_+,s_-)\) above. This covers the real Hermitian-diagonal generators of the full depth-three space. The complex extension requires correct conjugation in the adjoint slot.
- **Arbitrary physical quantum initial states/unknown time-dependent odd microscopic dynamics:** not addressed by this one-scalar theorem. The reflection-odd operator sector is complex 4-dimensional and a generic unknown odd state is *not* determined by the single initial diagonal q. The theorem crucially knows the exact U and restricts seeds to the original diagonal MASA.

Moreover, this q is an independently retained **preparation label**; the H44 legitimate CP even-only observer does **not dynamically infer q** and no CPTP instrument that physically reads q without disturbing hidden coherences or implements P6's frozen microscopic control sector is provided. A preparation's original left/right population imbalance can be independently measured or logged when preparing it, but that is additional observer access relative to the intentionally symmetry-erased H43/H44 extraction, not a novel CR selection principle.

In particular **none** of this proves \(\mathcal J_{\rm col}\) from P3, star-compatible P6 physical tangent provenance, a framework-only signal against standard GKSL, or P9 gravity dynamics.

## 5. Next gate

**H46 proposed:** ask whether a **single physically admissible CPTP instrument** can simultaneously preserve enough labelled original P3 quadratic return information and the required H44 CPTP even-sector Markovian quotient, without secretly reintroducing full-D3 observation or using known U/preparation labels as external storage. Test a concrete instrument versus an information–disturbance/no-broadcasting bound. If only a classical preparation label is retained, distinguish that operational extension from autonomous hidden-state recovery. A second option is an exact minimal sufficient *physical operator-system* for the full original \(\mathcal R_3\) under multiplication/adjoints, which may require enlarging the even algebra.

## 6. Exact reproducibility

`P3/P9H45QuadraticResidueSufficientOddSeedExactCheck.py` imports the unchanged H42/H44 exact rational microscopic model. It independently evaluates the four parity-reference original P3 commutators and **121 ordered pairs of exact rational Hermitian diagonal inputs**, compares to the closed polynomial, checks parity decomposition and rank of the two output directions, recovers all hidden iterates from even data plus q, and exhibits two positive density seeds with same even data/q² but different signed R. CI dedicated; no numerical tolerances. Frozen files/main untouched; no Lean kernel or human review claim.