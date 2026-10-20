# P11 G2/G3 — Operational-Quotient Descent and the Surviving H75 Access-Selection No-Go

**2026-10-20 | P3–P11 Mathematical Bridge | Draft stacked on #174**

## Scope and status

This is a **finite, exact, source-specific theorem** that separates two logically different obstructions:

1. A **gauge-representative obstruction**: the genuine H75 source stabilizer \(D_\pi\) exchanges the oriented coherent flag ports \(W\) and \(W^{-1}\), so an equivariant source-only selector cannot choose one **oriented representative**. This is resolved mathematically by passing to the orbit \([W]\).
2. A **hardware-access-class obstruction**: three authorization catalogs \(\mathsf A_0,\mathsf A_4,\mathsf A_5\) based on the **same** original H75 source have distinct **native response row spaces** of dimensions \(6,17,18\). They therefore remain distinct even *after* identifying gauge-equivalent port orientations. No **hardware-faithful**, source-only deterministic selector of the actual operational class exists on this three-world family.

The second obstruction **survives** the quotient that removes the first. Neither result proves that a richer, as-yet-unaxiomatized Generative Map \(F\) cannot generate additional boundary data; it proves that the explicitly held-fixed H75 CPTP source data alone do not determine the external permissions.

These results use ordinary finite quantum mechanics, not a new CR-exclusive physical prediction. The original H75 four-Kraus source, P3 residues, frozen P1–P8, main branch and original P6 observer are unchanged.

## 1. Typed response-space quotient

Fix the native real input vector space
\[
V=\operatorname{Herm}(3)\oplus\operatorname{Herm}(3),\qquad \dim_{\mathbb R}V=18.
\]
For a **declared legal finite set** of control/readout programs \(\mathsf A\) for the original H75 source, let
\[
r_{P,T,j}(\rho)=\operatorname{Tr}\!\big[
Q_j\,T\,\Phi_\mu(P\rho P^\dagger)T^\dagger\big]
\in V^*,\qquad \rho\in V,
\]
where \(T\in\{I,V_A,V_{AB}\}\) and \(Q_j=I_2\otimes |j\rangle\langle j|\) are the same fixed post/source effects as in #170–#171.

Define the **accessible response subspace**
\[
\mathcal E(\mathsf A)=\operatorname{span}_{\mathbb R}\{
r_{P,T,j}: P\in\mathsf A,\ T,j\text{ as above}\}\subseteq V^*.
\]
A finite basis of \(V\) produces a matrix \(C_{\mathsf A}\) whose row space represents \(\mathcal E(\mathsf A)\), so
\[
\dim\mathcal E(\mathsf A)=\operatorname{rank}C_{\mathsf A}.
\]
Equality of the response spaces gives a mathematically precise **coarse operational equivalence** \(\mathsf A\simeq_{\rm lin}\mathsf A'\). It detects the span of distinguishable linear response functionals but is not a full equivalence of labelled experiments, hardware capabilities, signal-to-noise, or costs. In particular, **equal row space is a coarser relation** than equality of every labelled probability; when we show literal equality of response rows below, both conclusions hold.

A change of real input coordinates \(R\in GL(V)\) acts by invertible right multiplication on all response matrices, hence cannot change rank or the strictness of their nested subspace dimensions. This avoids interpreting a selected coordinate presentation as a physical metric.

## 2. Theorem Q1 (gauge-representative quotient is exact on the native H75 experiment)

For \(D=D_\pi=\operatorname{diag}(1,-1)\otimes I_3\), #174 proved on **all** \(M_6(\mathbb C)\)
\[
\Phi_\mu\circ\operatorname{Ad}_D=\Phi_\mu
=\operatorname{Ad}_D\circ\Phi_\mu.
\]
On the native \(V\), \(\operatorname{Ad}_D\) is the identity. Every fixed site control, flag-conditional \(F_{\mathrm{fb}}\), post-control \(T\), and site projection \(Q_j\) commutes with \(D\). Also \(DWD=W^{-1}\).

For any legal native pre-reset coherent word \(P\), replace each \(W\) by \(W^{-1}\) and leave the \(D\)-commuting controls unchanged, giving \(P^-=DPD\). Then for all \(\rho\in V\):
\[
\Phi_\mu(P^-\rho(P^-)^\dagger)
=\Phi_\mu(DP\rho P^\dagger D)
=\Phi_\mu(P\rho P^\dagger).
\]
Consequently **all** retained downstream labelled \(T,Q_j\) statistics are identical, so
\[
\boxed{\quad \mathcal E(\mathsf A)=\mathcal E(D\mathsf A D),\quad
C_{\mathsf A}=C_{D\mathsf A D}\ \text{for consistently ordered programs.}\quad}
\]
This is a strictly stronger statement than merely preserving rank. Choosing the gauge orbit \([W]\) rather than a specific oriented \(W\) removes the #174 representative-selection obstruction **for these native H75 interventions**. No claim is made about newly authorized off-diagonal flag preparations, a new phase reference, or coherent flag readouts outside this experiment class.

## 3. Theorem Q2 (three distinct H75 operational classes survive gauge quotient)

Use the **same original H75 four Kraus operators** and the previously exact-audited nested pre-reset catalogs
\[
\begin{aligned}
\mathsf A_0&=\{I\},\\
\mathsf A_4&=\{I,F_{\mathrm{fb}},F_{\mathrm{fb}}V_A,F_{\mathrm{fb}}V_B\},\\
\mathsf A_5&=\mathsf A_4\cup\{P_5\},\quad
P_5=F_{\mathrm{fb}}WV_BF_{\mathrm{fb}}W.
\end{aligned}
\]
Their actual 9×18, 36×18, 45×18 rational response matrices \(C_0,C_4,C_5\) have exact ranks
\[
\boxed{\operatorname{rank}(C_0,C_4,C_5)=(6,17,18)}
\]
and nullities \((12,1,0)\). In fact, the literal row inclusion \(C_0\subset C_4\subset C_5\) and these ranks yield the **strict** response-space filtration
\[
\boxed{
\mathcal E_0\subsetneq\mathcal E_4\subsetneq
\mathcal E_5=V^*.
}
\]
The exact checker reuses and reruns #171's original-source rational H75 response generator, checks \(D\Phi_\mu D=\Phi_\mu\) on all 36 complex matrix units, verifies \(P_5^-=DP_5D\), and **independently checks**
\[
\boxed{\operatorname{Rows}(P_5^-)=\operatorname{Rows}(P_5)}
\]
entry by entry for all nine original readout configurations. Therefore the catalog \(\mathsf A_5^-=\mathsf A_4\cup\{P_5^-\}\) has **exactly the same** 45×18 response matrix as \(\mathsf A_5\), while neither can be operationally identified with \(\mathsf A_0\) or \(\mathsf A_4\).

Thus the native phase quotient removes orientation duplicates but **does not collapse the three genuine response-space classes**:
\[
\{[\mathsf A_0],[\mathsf A_4],[\mathsf A_5]\}
\quad\text{contains three distinct operational classes, despite one fixed }\Phi_\mu.
\]
This statement concerns *the explicitly declared finite catalogs*, not unrestricted control words with additional undocumented schedules.

The positive state witness \(\rho_\pm=I_6/6\pm\operatorname{diag}(-I_3,I_3)/12\) remains:
\[
\Pr(Q_1|P_5,\rho_+)-\Pr(Q_1|P_5,\rho_-)
=\frac{37376}{234375}>0.
\]
The \(P_5^-\) orientation yields the same difference. The restricted \(\mathsf A_4\) remains blind to the witness direction (nullity one), and \(\mathsf A_0\) has 12 invisible real directions. Orientation symmetry has not erased the physically distinct **authorized information-access depth**.

## 4. Theorem Q3 (necessary and sufficient factorization after quotient)

Let \(\mathfrak D\) be a set of admissible *device worlds*, let \(s:\mathfrak D\to\mathfrak S\) be a map recording only independently specified prior source data, and let
\[
a_{\rm op}:\mathfrak D\to\mathfrak Q
\]
record the actual **gauge-quotiented operational response class**. Here \(\mathfrak Q\) may be the equivalence classes of typed access catalogs under \(\mathsf A\simeq_{\rm lin}\mathsf A'\), or a finer **fixed** operational equivalence if precisely defined.

Then a deterministic **hardware-faithful** source-only quotient selector \(f:\operatorname{im}s\to\mathfrak Q\) with
\[
a_{\rm op}=f\circ s
\]
exists **iff**
\[
\boxed{
s(d)=s(d')\Longrightarrow a_{\rm op}(d)=a_{\rm op}(d')
\quad\text{for all }d,d'\in\mathfrak D.
}
\]
**Proof:** necessity is substitution. Sufficiency defines \(f(s(d))=a_{\rm op}(d)\); fibre constancy makes it well defined; uniqueness holds only on \(\operatorname{im}s\). This is the source-fibre factorization theorem *after* gauge descent; it is distinct from #173's stabilizer-fixed-point theorem for an equivariant selection of an **oriented representative**.

**H75 corollary:** take three worlds with identical \(s(d)=\Phi_\mu\) but actual permissions \(\mathsf A_0,\mathsf A_4,\mathsf A_5\). Their \(a_{\rm op}\) classes are distinct because their response ranks are 6, 17, 18. The fibre condition fails. So **no universal hardware-faithful deterministic selector from that source-only datum exists, even after the oriented flag-phase quotient**.

**Conditional information bound (only this fixed three-world benchmark):** any additional independent boundary selector data \(b(d)\), combined with \(s(d)\), that restores factorization must distinguish three values; a fixed-width binary encoding needs at least \(\lceil\log_2 3\rceil=2\) bits. This does **not** imply that AX-OA itself has a universally minimal number of independent axioms, or that these bits are physical entropy costs.

## 5. EXACT mathematical relaxation vs OPEN generative completeness

A set-valued assignment \(\Phi_\mu\mapsto\{\mathcal E_0,\mathcal E_4,\mathcal E_5\}\) is consistent as a **catalog of possible access classes**. It **does not** select which physical world is realized and is not an intrinsic Generative Map law merely because one writes the set notation.

Likewise, conventionally declaring "choose the maximal catalog \(\mathsf A_5\)" gives a deterministic mathematical preference but fails to be hardware-faithful for devices realizing only \(\mathsf A_0\) or \(\mathsf A_4\). The actual physical authorization cannot be inferred from identical CPTP dynamics unless further prior data are physically justified.

**P11 now has three sharply separated output types**:
- **Representative:** oriented concrete ports and phase frames; H75 has a real source stabilizer obstruction to a natural choice.
- **Quotient class:** native operational signatures modulo phase-representative gauge; orientation obstacle is removed but the three-world source-fibre obstacle remains.
- **Realized certificate:** one physically authorized preparation/control/instrument/schedule/readout/calibration package; its reality and selection are neither proved by a quotient nor by ordinary rational matrices.

A noncircular \(F\mapsto\mathrm{GenAcc}_F\) must specify which output type it claims, and which independently prior F axioms supply extra access-class selector data. Merely repackaging \(\mathsf A_5\), assuming independent pulse calibration, or requiring the eventual P6/P9 geometry as an input would be circular.

**P9 boundary unchanged:** P6 physical provenance, native-15 GT–K4 metric descent no-go, P7/P8 soldering, KKS→ADM/DeWitt/HDA, nonuniform off-shell Einstein dynamics and universal gravity remain unresolved. The original P3 quadratic residue is not the same object as this response rank; no new CR-exclusive quantum prediction or experimental verification. CI checks finite arithmetic only; no general proof-assistant formalization or human peer review. PR is Draft/unmerged.
