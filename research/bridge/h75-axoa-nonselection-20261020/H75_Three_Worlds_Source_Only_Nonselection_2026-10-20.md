# H75–P11 AX-OA: Three-World Source-Only Access Nonselection Theorem

**2026-10-20 | P3–P11 Mathematical Bridge | Draft stacked on PR #169**

## Scope and central decision

This is an exact, finite *source-only nonselection theorem*: a specified channel \(\Phi_\mu\), including all mathematical invariants computable solely from that channel (in particular any unchanged original P3 closure–residue data), cannot determine which of several physically allowed **external access catalogs** is actually furnished by a device. It is NOT a theorem that the full Generative Map \(F\), a richer theory with newly defined physical selection laws, or every conceivable source-plus-boundary datum cannot choose access. A mathematical preferred selector is not automatically a **hardware-faithful** selector.

**Lineage:** H82 integration baseline (Notion, 2026-10-19); original H75 four-Kraus six-level CPTP source (#94), H81 AX-OA scheduling (#100), global augmented operator-response rank-18 (#164), ranked fixed-catalog AX-OA resources (#166), 24-record stability (#167), sharp macro-depth-5 (#168), and conditional hardware compilation/error certificate (#169). None of main/frozen/published P1–P8 or these predecessors is revised by this Draft.

## 1. Exactly the same microscopic source, three nested externally authorized access catalogs

Let \(\mathcal V=\operatorname{Herm}(3)\oplus\operatorname{Herm}(3)\) be a real 18D space of input flag-block-diagonal six-level Hermitian matrices, including an open relative neighborhood of positive trace-one inputs around \(I_6/6\). Let the **same** original H75 source be
\[
\Phi_\mu(X)=\sum_{a,b=0}^{1}K_{ab}XK_{ab}^\dagger,\qquad
K_{ab}=|a\rangle\langle b|\otimes U M_a,
\]
with the original fixed qutrit \(U=\mathrm{diag}(i,1,i)O\), \(M_0=\mathrm{diag}(1,3/5,3/5)\), \(M_1=\mathrm{diag}(0,4/5,4/5)\). The source \(\Phi_\mu\), its Kraus realization, and all original P3 signed \(R_3\) data **do not change** across the three hypothetical device specifications.

The post-reset programs are always exactly \(T\in\{I_6,V_A,V_{AB}\}\); the positive readouts are always the three site projectors \(Q_j=I_2\otimes|j\rangle\langle j|\), \(j=0,1,2\). For an authorized pre-reset unitary \(P\) define its nine scalar linear response functionals
\[
R_{P,T,j}(X)=\mathrm{Tr}\bigl[Q_j T\Phi_\mu(PXP^\dagger)T^\dagger\bigr].
\]
The three **nested** AX-OA choices differ only in the independently authorized pre-reset schedule (mathematical permissions, NOT experimentally certified ports):

- \(\mathsf A_0\): only \(P=I_6\) (9 registered effect rows);
- \(\mathsf A_4\): \(P\in\{I_6,F_{\rm fb},F_{\rm fb}V_A,F_{\rm fb}V_B\}\) (36 rows; each pre-reset program uses at most **two** macros);
- \(\mathsf A_5\): *all* the \(\mathsf A_4\) programs plus \(P_5=F_{\rm fb}W V_B F_{\rm fb}W\), chronological \(W\to F_{\rm fb}\to V_B\to W\to F_{\rm fb}\) (45 rows).

All positive POVMs and post-reset settings are retained unchanged. The \(V_{AB}\) bundle is a registered macro-gate where used. No alternate source or observer is substituted.

## 2. EXACT three-rank theorem: 6 < 17 < 18

Construct the rational response matrices over the unchanged 18-dimensional real Hermitian basis:
\[
C_0\in\mathbb Q^{9\times18},\quad C_4\in\mathbb Q^{36\times18},\quad
C_5=\begin{pmatrix}C_4\\ C_{P_5}\end{pmatrix}\in\mathbb Q^{45\times18}.
\]
Exact-rational source calculations yield:
\[
\boxed{\mathrm{rank}_{\mathbb Q}(C_0)=6,\qquad
\mathrm{rank}_{\mathbb Q}(C_4)=17,\qquad
\mathrm{rank}_{\mathbb Q}(C_5)=18.}
\]
Consequently their observational kernels form a strict descending chain
\[
K_5=\{0\}\subsetneq K_4=\mathbb R\,X_{\rm flag}
\subsetneq K_0,\qquad
(\dim K_0,\dim K_4,\dim K_5)=(12,1,0),
\]
where \(X_{\rm flag}=\mathrm{diag}(-I_3,I_3)\). These **are input-linear observational dimensions**, not physical spatial dimensions, CP quantum-memory Hilbert dimensions or ADM degrees of freedom.

Proof/certificate: the companion script imports the previously source-verified exact H75 checker from #168, independently constructs \(C_0\), \(C_4\), \(C_5\), checks nested row identities, exact rational ranks, nullity and \(K_4\)'s unique \(X_{\rm flag}\) direction. \(\mathsf A_0\) rank 6 also matches the fixed catalog enumeration in #166. \(\mathsf A_4\)'s rank 17 and \(P_5\)'s rank-restoration were verified in #168. The source matrix and its original \(R_3\) data remain the same for all rows.

**Positive-state witness for \(\mathsf A_4\not\sim\mathsf A_5\):** \(\rho_\pm=I_6/6\pm X_{\rm flag}/12\) are distinct strictly positive trace-one density matrices, operationally identical for every \(\mathsf A_4\) effect (indeed every pre-reset word of length <=4); adding \(P_5\), one H75 reset and positive \(Q_1\) yields
\[
\Pr(Q_1|\rho_+)=32271/78125,\quad
\Pr(Q_1|\rho_-)=59437/234375,\quad
\boxed{\Delta=37376/234375}.
\]
The strict inclusion \(K_4\subsetneq K_0\) also implies a (possibly different) strictly positive pair distinguishable by \(\mathsf A_4\), but not by \(\mathsf A_0\): choose nonzero Hermitian \(Y\in K_0\setminus K_4\) of zero trace and sufficiently small \(t>0\), then \(I_6/6\pm tY\) are valid density matrices. Since every catalog contains the identity effect, any direction in the response kernel automatically has zero trace. Thus the rank differences are genuinely operational, not mere formal coordinate artifacts.

## 3. General source-only factorization theorem and exact nonselection corollary

Let \(\mathfrak D\) be any family of mathematical devices (carrier, physical source, permissible preparation/operation/schedule/readout data), \(s:\mathfrak D\to\mathfrak S\) the **forgetful map retaining only source-defined data** (including all invariant quantities determined by the retained source), and \(a:\mathfrak D\to\mathfrak O\) the **operational class** of the permitted response behavior (for this benchmark, use equality of the kernels on the common fixed input domain; this weak operational invariant already suffices).

**Source-only selection criterion.** A single-valued source-only, hardware-faithful choice \(g:\mathfrak S\to\mathfrak O\) with \(a=g\circ s\) exists **if and only if** \(a\) is constant on every fibre \(s^{-1}(\sigma)\). Proof: necessity by applying the factorization to two devices with the same source; sufficiency by defining \(g(\sigma)\) as their common operational class on the image \(s(\mathfrak D)\) (any extension beyond the image is separate).

**Exact H75 nonselection corollary.** The three finite devices above share \(s(\mathsf A_0)=s(\mathsf A_4)=s(\mathsf A_5)\), but their kernels have different dimensions \(12,1,0\), hence \(a(\mathsf A_0),a(\mathsf A_4),a(\mathsf A_5)\) are distinct. No single-valued function of the uncontrolled H75 channel and of **solely channel-derived P3 invariants** can reproduce which external AX-OA permission class is furnished in *all three* devices. This is a formal no-go for **universal source-only hardware-faithful selection on a family containing these three access variants**, not a no-go against any new axiom or richer generated data in P11.

On this **finite three-class benchmark only**, a noiseless external classifier must distinguish at least three values (e.g. at least two binary symbols in a fixed-length binary encoding). This is a bookkeeping lower bound on external *selection information*, NOT a physical Landauer cost, a universal minimum count of AX-OA axioms, or an origin claim about F.

## 4. Implications for P11's G2/G3 and P9

**G2/type-realization obligation:** specify a map from previously axiomatized \(F\)-side data to *complete* typed certificates:
\[
\operatorname{GenAcc}_F:\mathfrak F_{\rm pre}\to
(\mathrm{Prep},\mathrm{Ports},\mathrm{Instruments},
\mathrm{Schedule},\mathrm{Readout};\mathrm{Calibrations}),
\]
with a defined physical carrier, causal realizability, and independently checkable intervention meaning. H75 source data alone cannot provide a hardware-faithful selection for every permitted world.

**G3/noncircular uniqueness obligation:** to claim intrinsic access selection, state an explicit new physical restriction or principle that excludes unwanted source-identical devices or selects a definite class; prove it from independently prior \(F\) axioms without secretly inserting the desired observation metric, distinguished P6 \(J_N\), phased controls, or an externally chosen hardware list. The new principle, not the mere finite H75 rank proof, is what would distinguish the intended world.

**P9:** This nonselection theorem neither repairs original native-15 GT–K4 metric descent nor identifies H75 macros with physically sourced P9 Cartan/ADM canonical controls. Use the three-rank contrast only to record the operational-access provenance debt.

**OPEN:** independent actual hardware permission and laboratory preparation; frozen P6 \(\mathcal J_N\) provenance; G2/G3 generation from F; unique metric selection; large-system locality and continuum; Einstein/DeWitt/HDA dynamics; P12 universal gravity; human peer review and experiment. H82's five AX-OA components have NOT been proven uniquely minimal or mutually independent.

## Reproducibility and status

Companion test \`H75_AXOA_Three_Worlds_Exact.py\` checks true original source-catalog response ranks and exact positive-state witness using the predecessor's unchanged full-rational matrix implementation. Dedicated GitHub Actions runs the test on the stacked PR; until it completes successfully, do not claim GitHub CI PASS for this new theorem.

**Draft, unmerged.** The paper manuscripts, main and preceding Draft proofs stay unchanged.
