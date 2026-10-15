# H71 — Constructive Controlled-CPTP Reflection Observer: Symmetry-Locked Exchange, Dephasing and the P3 Provenance Boundary

**2026-10-16 | P3–P11 Mathematical Bridge / route A.** H71 inherits H42's **unchanged original P3 three-site rational unitary CPTP channel** \(\Phi=\operatorname{Ad}_U\), its true original signed quadratic residue, and H43/H44/H70's **reflection conditional expectation** \(\mathcal E=\frac12(\mathrm{id}+\operatorname{Ad}_P)\). It explicitly constructs a *conditional controlled-CPTP subfamily* preserving a nontrivial five-complex-dimensional observer and original signed P3 return for the reflection-even diagonal seed subdomain. It also proves that **two independent real-exchange controls or unequal endpoint dephasing generally violate the same observer closure**. These statements are finite ordinary quantum mechanics and **do not derive the hardware-control selection from P3 or frozen P6 v9.1**.

## 1. Fixed source, observer, and honest CP operations

Take the exact H42 reflection \(P=E_{02}+E_{11}+E_{20}\) and real anti-Hermitian physical-*type* exchange generators

\[
A=E_{01}-E_{10},\qquad B=E_{21}-E_{12},\qquad
K_+=A+B,\quad K_-=A-B.
\]

H42's **same** microscopic U obeys \([U,P]=0\). The H43 CP twirl is the explicitly physical **mixture** of identity and conjugation by P,

\[
\mathcal E(X)=\frac12(X+PXP)=P_+XP_++P_-XP_-,\quad P_\pm=(I\pm P)/2.
\]

It has a five-complex-dimensional unital C*-algebra range \(\operatorname{im}\mathcal E\simeq M_2(\mathbb C)\oplus\mathbb C\), and \(\ker\mathcal E\) is the four-complex-dimensional reflection-odd operator subspace. The physical availability of a controlled reflection/coin-twirl is an *extra implementation premise*, even though its mathematical CP realization is exact.

For the collective *one-knob* exchange \(K_+\) take a fully rational finite unitary control

\[
V_+(s)=(I+sK_+)(I-sK_+)^{-1},\quad s\in\mathbb Q,
\]

or its continuous exponential alternative. This is a genuine unitary for real s and \([V_+(s),P]=0\). No nonunitary truncation or false equation between Cayley and exponential is used.

For site-specific calibrated dephasing, use the independent CPTP site phase-flip mixtures

\[
\mathcal D_j^{(q)}(X)=qX+(1-q)Z_jXZ_j,\quad Z_j=I-2E_{jj},\quad 0\le q\le1.
\]

Each is a convex mixture of unitary channels. Fix an arbitrary center q1 but **match endpoint rates** \(q_0=q_2=q\), and set \(\mathcal D_{q,q_1}=\mathcal D_2^{(q)}\circ\mathcal D_1^{(q_1)}\circ\mathcal D_0^{(q)}\). Because the reflection interchanges the endpoint phase flips and all three site phase-flip maps commute,

\[
[\mathcal E,\mathcal D_{q,q_1}]=0,\quad [\mathcal E,\operatorname{Ad}_{V_+(s)}]=0,\quad [\mathcal E,\Phi]=0.
\]

**Theorem H71.1 — exact finite controlled CPTP constructive bridge (CONDITIONAL).** Every channel in the declared family

\[
\boxed{\Psi_{s,q,q_1}
=\mathcal D_{q,q_1}\circ \operatorname{Ad}_{V_+(s)}
 \circ\Phi}
\]

is CPTP and obeys

\[
\boxed{\mathcal E\Psi_{s,q,q_1}
 =\Psi_{s,q,q_1}\mathcal E}.
\]

Thus each such channel restricts to an **autonomous, honest CPTP map on the five-dimensional algebra** \(\operatorname{im}\mathcal E\). Every finite *adaptive predetermined sequence* of these controlled CPTP maps likewise intertwines \(\mathcal E\); the output observer tracks that sequence without restoring the four reflection-odd microscopic directions. The branch-independent algebraic sequence is proved by composition; this is not yet a full measured adaptive instrument with quantum outcome-conditioned channels. The exact checker demonstrates multiple noncommuting rational finite controls and dephasing settings on **all nine matrix units**, including a repeated sequence.

The construction is **not** a proof that frozen P6 admits only the collective \(sK_+\) knob, that its independent dephasing parameters satisfy \(q_0=q_2\), that physical site reflection and twirling are available, or that H42's original-P3 hidden sector causes these restrictions.

## 2. H71.2 — independent real-exchange controls violate this particular 5D closure

For the fixed P, \(PK_+P=K_+\) but \(PK_-P=-K_-\). An operator \(X\in\ker\mathcal E\) is parity-odd. Thus \([K_+,X]\) is odd and its twirl vanishes, while \([K_-,X]\) is even and may leak into the five-dimensional visible algebra. Take the explicit odd population witness

\[
W=E_{00}-E_{22}\in\ker\mathcal E,\qquad
\boxed{\mathcal E[K_-,W]\neq0}.
\]

For a two-knob real-exchange tangent \(K(x,y)=xA+yB\), one has

\[
K(x,y)=\tfrac{x+y}{2}K_+ + \tfrac{x-y}{2}K_-,
\]

hence on this exact W,

\[
\boxed{\mathcal E[K(x,y),W]=
\tfrac{x-y}{2}\mathcal E[K_-,W].}
\]

Therefore, requiring *every* infinitesimal allowed independent-control channel around zero to induce an autonomous **linear** observer map through this fixed \(\mathcal E\) forces **\(x=y\)**. In particular P6-like independent A/B knobs fail the fixed-five-dimensional observer criterion. A finite nonzero Cayley pulse built from \(K_-\) also leaks the hidden W into the visible twirled output, verified exactly. This is a **No-Go for THIS reflection observer and THIS independent exchange manifold**, not a claim that all other CPTP observers or enlarged physical memory must fail.

The family being *swap-covariant* under \((x,y)\mapsto(y,x)\) only relates two different controls; it does **not** make each channel commute with \(\mathcal E\). H43 made this distinction previously, and H71 applies it to predictive CPTP closure.

## 3. H71.3 — independently calibrated site dephasing also needs physical symmetry

Take the parity-odd offdiagonal witness \(Y=E_{01}-E_{21}\in\ker\mathcal E\). Under the three site phase-flip CPTP mixtures, \(E_{01}\) is multiplied by \((2q_0-1)(2q_1-1)\), and \(E_{21}\) by \((2q_2-1)(2q_1-1)\). Hence

\[
\mathcal E\mathcal D_{\mathbf q}(Y)
=\frac{(2q_1-1)((2q_0-1)-(2q_2-1))}{2}
(E_{01}+E_{21}).
\]

If \(q_1=1,\ q_0=4/5,\ q_2=3/5\), the right-hand side is exactly

\[
\boxed{\frac15(E_{01}+E_{21})\neq0}.
\]

Thus a fully legitimate CPTP, independently calibrated but **endpoint-asymmetric** dephasing channel can violate autonomous closure on this 5D observer. The matching condition \(q_0=q_2\) is sufficient for parity covariance; it is not claimed universally necessary at special complete-dephasing parameters that suppress all sensitivity.

A common global dephasing \(qX+(1-q)\Delta_DX\) *does* commute with the reflection, but frozen P6's broader independent site-dephasing declaration does not automatically enforce endpoint equality. This exact distinction must be retained.

## 4. H71.4 — a nontrivial RESTRICTED simultaneous signed-residue guarantee

The fixed original P3 signed return is

\[
R_{12}(d,d')=
\Delta_D\left(
[(1-\Delta_D)\Phi(d),
 ((1-\Delta_D)\Phi^2(d'))^\dagger]
\right).
\]

On the **reflection-even diagonal seed family**

\[
D_{\rm even}=\{d=\operatorname{diag}(a,b,a)\},
\]

the CP twirl fixes every seed pointwise: \(\mathcal E(d)=d\). Thus, from the observer's **initial twirled quantum record** and the known fixed microscopic \(\Phi\), all bilinear signed P3 returns for pairs from \(D_{\rm even}\) are uniquely calculable: \(R_{12}(d,d')=R_{12}(\mathcal E d,\mathcal E d')\). The true original-P3 return is **nontrivial**, with one-dimensional signed-return image on this even diagonal domain as previously proved in H45. Exact H71 checks reproduce the rank-one image for the two even diagonal basis seeds.

The assertion is *not* that a noisy observed record without independent knowledge of \(\Phi\) measures a signed CR-only return, nor that the observer retains the original P3 return for arbitrary diagonal seeds. H70's valid positive pair \(d_0=E_{00}\), \(d_2=E_{22}\) have \(\mathcal E(d_0)=\mathcal E(d_2)\) but different original signed returns, so the full \(D_3\)-seed claim is false. The restriction to symmetric prepared seeds is **substantive**. Symmetry-preserving controlled maps carry parity-even states into the even algebra, but the original P3 diagonal-seed return is still defined for the declared original \(\Phi\), not automatically for a new arbitrary controlled channel's residue filtration.

## 5. The decisive route-A provenance boundary — still NOT solved

This constructive result shows that a physically *admissible class of finite CPTP operations* can preserve a nontrivial quantum observer algebra with restricted P3 signed-return sufficiency, **provided** reflection-locked collective exchange, endpoint-symmetric dephasing, and the reflection-twirl observer are independently supplied.

**It is NOT the final P3→frozen-P6 construction theorem.** In fact the unchanged H42 source has a sharp counter-gate: its **true original-P3 computed hidden Krylov candidate** \(\Xi(H_{\le\infty})\) has real rank 5 and **does not contain the very collective direction** \(K_+=A+B\). This was already exact in H42 and is reasserted using the original rank code in H71. Therefore the strongest unjustified step would be to assert

\[
K_+\in\Xi(H_{\le\infty})\quad\text{or}\quad
\text{P3 signed residue}\Longrightarrow
\text{physically allowed collective control}.
\]

Both are unsupported; the first is *false for H42's actual computed source*. H42 also exhibited distinct same-source CPTP control extensions, enforcing a real independent source/protocol-selection gate. Calling this model a physical realization of **all** frozen P6 two-knob controls would contradict H71.2.

**H71 route-A achievement:** a verified constructive **conditional benchmark with precise admissibility conditions**, not a microscopic provenance theorem. This is the correct input for the next source selection analysis rather than a reason to abandon route A.

## 6. H72 — demand an actual microgenerated control-and-observer provenance certificate

For route A, the next stage should seek a new, independently specified CPTP \(\Phi_{\rm phys}\), microscopic generation \(\mathcal J_{\rm phys}\), control tangent map \(S\), and physically implemented observer \(C_{\rm phys}\) satisfying simultaneously:

1. source \(\mathcal J_{\rm phys}\) and allowed real/complex control manifold are linked by an **independently established** generator/intervention relation, not post-hoc identification with a convenient hidden Krylov projection;
2. the admitted controls and dephasing preserve **the same** observer kernel, or furnish a physically present, explicitly CP predictive memory that does;
3. the physically prepared initial sector is closed under admissible controlled dynamics, and the true original signed P3 return is reconstructible in the precisely declared source sector;
4. all controls/observer branches are CPTP with explicit microscopic error/conditioning estimates where needed; avoid unphysical perfect instantaneous tomography;
5. the microscopic controlled process must not be silently equated to frozen P6 v9.1 or the independently defined P9.72 SWAP+ZZ hardware.

The original H42 channel with unconstrained frozen-P6-like independent A/B controls plus arbitrary asymmetric dephasing **cannot** meet the H71 five-dimensional twirl criterion, so either physical controls are more symmetric, a different observer is required, or additional quantum memory is necessary. A route-A success must explicitly handle this fork without importing desired controls by assumption.

**Boundary:** ordinary finite CP/quantum control results; no CR-only experimental discriminator, physically proven frozen-P6 \(\mathcal J_N\), full KKS/ADM soldering, DeWitt kinetic provenance, off-shell HDA, Einstein gravity, or P9 Minimum Success. Draft/unmerged; Lean/human peer review/experiment not performed.
