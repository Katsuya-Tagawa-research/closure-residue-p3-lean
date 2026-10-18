# H87 — KKS-to-ADM Response-Solder Obstruction: Nonprojectable Poisson Brackets and the Independent DeWitt Gate

**2026-10-18 | P9 GR-I / P3–P11 Mathematical Bridge / Route A.**
**Base:** H86 Draft PR #105, **99/99 CI PASS**. H87 resumes the true gravitational *canonical* obstruction rather than extending artificial edge-weight models. Frozen P1–P8, main, and the original H75 six-dimensional CPTP source are unchanged. This **four-level U(4) coadjoint orbit** is an independently chosen standard quantum comparator, **not yet a derived orbit of H75/P3 or the physical P7/P8 spatial solder**.

## 1. H87.1 — The genuine six-pair KKS candidate

Fix the nondegenerate four-level density matrix
\[
\rho_\star=\operatorname{diag}(2/5,3/10,1/5,1/10)
\]
and its compact coadjoint orbit \(\mathcal O=U(4)\cdot\rho_\star\cong U(4)/U(1)^4\), of real dimension \(12\). For each unordered edge \(a<b\), define Hermitian coherence quadratures
\[
X_{ab}=E_{ab}+E_{ba},\qquad Y_{ab}=-i(E_{ab}-E_{ba}),
\]
and six real response readouts \(x_{ab}(\rho)=\operatorname{Tr}(\rho X_{ab})\), \(y_{ab}(\rho)=\operatorname{Tr}(\rho Y_{ab})\). With the quantum KKS Lie–Poisson convention
\[
\boxed{\{f_A,f_B\}(\rho)=-i\operatorname{Tr}(\rho[A,B]),\quad
 f_A(\rho)=\operatorname{Tr}(\rho A),}
\tag{H87-P}
\]
the six real root planes are symplectically paired at the reference state:
\[
\{x_{ab},y_{cd}\}(\rho_\star)
=2(\lambda_a-\lambda_b)\delta_{(ab),(cd)},\qquad
\{x_{ab},x_{cd}\}(\rho_\star)=0.
\]
Every gap is nonzero. Therefore \(\operatorname{rank}(Dx)(\rho_\star)=6\), and the full 12-dimensional KKS tangent has six independent real symplectic planes: **local rank/dimension is not an obstruction** to some local canonical six-pair model. This reproduces, without expanding, H59's exact local-vs-global distinction.

## 2. H87.2 — Same six coherence readouts, different Poisson brackets (EXACT obstruction)

Two edge response functions fail to Poisson commute away from the special diagonal point:
\[
[X_{01},X_{12}]=E_{02}-E_{20},\qquad
\boxed{\{x_{01},x_{12}\}=y_{02}.}
\tag{H87-NC}
\]
Consider the *genuine unitary conjugate physical density matrix*
\[
\rho_t=U_t\rho_\star U_t^\dagger,\qquad
U_t|_{\{0,2\}}=
\begin{pmatrix}
a_t&-ib_t\\-ib_t&a_t
\end{pmatrix},\quad
a_t=\frac{1-t^2}{1+t^2},\quad b_t=\frac{2t}{1+t^2},
\]
and \(U_t|_{\{1,3\}}=I\), with \(t\in\mathbb R\) sufficiently small. Since \(a_t^2+b_t^2=1\), the pulse is exactly unitary. For **every** \(t\) in this family:
\[
\boxed{x_{ab}(\rho_t)=0\ \text{for all six edges}.}
\tag{H87-SAME}
\]
But the hidden quadrature and Poisson bracket are
\[
\boxed{\{x_{01},x_{12}\}(\rho_t)
=y_{02}(\rho_t)
=-\frac{4t(1-t^2)}{5(1+t^2)^2}.}
\tag{H87-SHADOW}
\]
This is zero at \(t=0\), but nonzero for all small nonzero \(t\). At the exact rational point \(t=1/2\) one has \(a=3/5,b=4/5\),
\[
\boxed{\rho_{1/2,02}=12i/125,\quad
x(\rho_{1/2})=x(\rho_\star)=0,\quad
\{x_{01},x_{12}\}(\rho_{1/2})=-24/125.}
\]
Both are positive trace-one density matrices in the **same** U(4) unitary orbit; no fabricated nonphysical state is involved. H87's exact Gaussian-rational checker reproduces every readout and bracket.

**Theorem (scoped Poisson nonprojectability).** There is **no autonomous Poisson bracket on the six-dimensional response image** \(x(\mathcal U)\subset\mathbb R^6\), for any neighborhood \(\mathcal U\) of \(\rho_\star\), such that \(x:\mathcal U\to x(\mathcal U)\) is a Poisson map for the KKS bracket and the six specified \(x_{ab}\) are its coordinate functions. **Proof:** if \(\{x_{01},x_{12}\}\) descended to a function of \(x\), it must have the same value at any \(\rho,\rho'\) with \(x(\rho)=x(\rho')\); (H87-SAME) and (H87-SHADOW) contradict this arbitrarily close to \(\rho_\star\). \(\square\)

This strengthens mere local noncommutation: **the candidate six-observable response quotient is not closed as a Poisson system**. It is a conventional KKS quantum-mechanical obstruction, **not automatically the original P3 diagonal quadratic residue, not a proof of impossibility of other observers/polarizations**, and not a novel universal quantum-gravity No-Go theorem.

## 3. H87.3 — A positive K4 metric cannot erase the missing symplectic information

As a deliberately **independent conditional algebraic solder**, assign six candidate edge weights
\[
w_{ab}(\rho)=1+\epsilon\,x_{ab}(\rho)\quad
(\epsilon>0,\ \text{on a sufficiently small neighborhood where }w>0),
\]
and define
\[
L_w=\sum_{a<b}w_{ab}(e_a-e_b)(e_a-e_b)^\top,\quad
S=\mathbf1^\perp,\quad g_w=16(L_w|_S)^{-1}.
\]
The six weights are locally invertible linear functions of the six response coordinates, and the **known** weighted K4 chart is a diffeomorphism from an open positive-edge cone into its SPD(3) metric image. Consequently any six local metric components that parametrize this image have the **same Poisson nonprojectability**, since an invertible change of observed coordinates cannot make a nonprojectable bracket projectable.

Indeed both \(\rho_\star\) and \(\rho_t\) have **identical**
\[
w_{ab}=1,\qquad L_w=4P_S,\qquad g_w=4I_S,
\]
yet the microscopic KKS bracket \(\{w_{01},w_{12}\}=\epsilon^2y_{02}\) differs. A metric response alone cannot be promoted to autonomous **canonical configuration** degrees of freedom while retaining exactly these six observed response functions. Taking \(\epsilon=1\) already works along the exhibited family, and positivity persists near \(\rho_\star\).

The A4/K4 dictionary here is a **candidate external mathematical construction**, not an identification of observed H86's positive second-jet \(J^2\), not a source-derived spatial graph, and not a genuine dynamic ADM solder.

## 4. H87.4 — What is still mathematically possible: local canonical completion after replacing the observables (EXACT CONDITIONAL)

Darboux's theorem applied to the nondegenerate KKS two-form guarantees *some* local canonical coordinates \((Q_1,\dots,Q_6,P_1,\dots,P_6)\) near \(\rho_\star\), with
\[
\omega_{\rm KKS}=\sum_{\alpha=1}^6dQ_\alpha\wedge dP_\alpha
\]
(up to one consistently chosen conventional sign). Choosing an arbitrary positive local six-weight chart \(w_e=1+Q_e\) **and independently supplying the K4 spatial solder**, the analytic bijection \(w\leftrightarrow g_w\) gives six local SPD(3) configuration coordinates \(g_{mn}(Q)\). Under its invertible Jacobian the usual cotangent-lift momentum assignment
\[
\boxed{\Pi = [D_Qg(Q)]^{-T}P}
\]
preserves the canonical one-form \(\sum_eP_e\,dQ_e=\sum_{\alpha}\Pi_\alpha\,dg_\alpha\). Hence a **local abstract symplectic identification** with an ADM-shaped \(T^*\mathrm{SPD}(3)\) chart exists.

This does **not** preserve \(Q=x\) from Section 2; indeed no canonical Darboux six-position chart can equal those six noncommuting response functions on an open region. It also does not prove that any quantum apparatus measures these new Q values, that the actual source selects their K4 weights/solder, that the physical H75 microscopic KKS sector has this orbit, or that the physical Hamiltonian/constraints intertwine. It leaves H59's **global** compact-orbit nonexactness obstruction in force: a local Darboux patch does **not** give a global symplectomorphism onto a globally exact cotangent phase space.

**Local feasibility vs sourced physics:**
\[
\text{12D KKS comparator}
\overset{\rm local\ Darboux}{\cong}
\text{12D canonical chart}
\overset{\rm chosen\ K4\ weight\ chart}{\cong}
\text{ADM-shaped local cotangent chart},
\]
where **both maps are conditional choices**, not derived by \(F\).

## 5. H87.5 — The gravitational DeWitt sign is additional DYNAMICAL data

At a Euclidean three-metric \(g_{ij}=\delta_{ij}\), decompose symmetric momentum \(P\in\mathrm{Sym}^2(\mathbb R^3)\) into five traceless components and its trace. The normalized ADM kinetic quadratic form is
\[
\boxed{\mathscr D(P)=\operatorname{tr}(P^2)
-\tfrac12(\operatorname{tr}P)^2.}
\]
For traceless \(P_0\), \(\mathscr D(P_0)=\|P_0\|^2>0\); for the pure trace \(P=tI_3\), \(\mathscr D(tI_3)=-3t^2/2<0\). Thus its signature is **(5+,1−)**. A positive quadratic form \(\mathscr E(P)=\operatorname{tr}(P^2)\) has (6+,0−). Under a **configuration-preserving real invertible** momentum change \(P\mapsto CP\), the inertia of the momentum Hessian cannot change (Sylvester's law). Therefore the simple positive Fisher/Laplacian-induced finite comparator does **not** automatically give the ADM conformal kinetic negative direction; this reaffirms H61's limited signature gate.

**Do not overstate this:** an abstract 12D symplectic manifold admits *both* a positive local Hamiltonian \(H_+=\frac12\sum P_a^2+V(Q)\) and an indefinite model \(H_D=\frac12(P_1^2+\cdots+P_5^2-P_6^2)+V(Q)\). KKS symplectic geometry alone does not forbid an indefinite Hamiltonian, nor does it physically select one. Arbitrary canonical transformations that mix configuration/momenta are outside the above **configuration-preserving** inertia statement and must be assessed against the specific ADM configuration interpretation. A negative conformal kinetic direction is not, by itself, proof of a quantum ghost.

## 6. Provenance ledger / P9–P11 handoff

| Statement | Verdict |
|---|---|
| Generic U4 KKS orbit dimension 12, six nonzero root-plane pairings | **EXACT** for the specified independently chosen orbit |
| Six fixed physical-looking X-edge observables can themselves serve as a mutually commuting local ADM q-family | **NO-GO** on any neighborhood of the diagonal basepoint |
| Their six-response quotient admits an autonomous descended KKS Poisson bracket | **NO-GO**, two bona fide same-response positive states with different brackets |
| Conditional positive K4 metric can be assigned from those responses | **EXACT CONDITIONAL**; metric alone does not restore missing Poisson data |
| Some locally canonical 6+6 Darboux coordinates and cotangent-lift SPD metric chart exist | **EXACT LOCAL**, but not for the same six response observables |
| Positive finite momentum Hessian becomes ADM DeWitt (5+,1−) by a configuration-preserving invertible real change | **NO-GO**, inertia obstruction |
| DeWitt-indefinite Hamiltonians cannot exist on a KKS patch | **FALSE**; the symplectic form does not choose kinetic signature |
| Source-derived physical KKS orbit, canonical map, constraints, nonuniform off-shell HDA, EH/Einstein equations, generative completeness of F | **OPEN** |

**P9 requirement:** Supply independently justified **closed six-dimensional configuration observables** (in involution, not merely independent), six canonically conjugate momenta, actual physical KKS-to-ADM Hamiltonian/constraint intertwining, nonuniform field/boundary gluing, DeWitt kinetic selection, and fully correct H–H/H–D/D–D structure functions. A standard off-shell ADM comparator cannot be silently taken as generated.

**P11 requirement:** If F is proposed to generate the observer/configuration sector, its axiom must select a **Poisson-projectable** observer quotient or a valid retained-memory enlargement carrying missing coherence y. This is a precise finite KKS **closure failure witness**, but it is *not* the original P3 residue nor proof that a particular F axiomatization forces a unique repair.

**Reproducibility:** A dedicated exact Gaussian-rational checker constructs rho*, real six x/y observable matrices, the rational physical U02(t=1/2) conjugate, proves all six observed x vanish at both states, verifies differing Poisson bracket -24/125, six independent tangent response directions, positive metric basepoint, and DeWitt (5+,1−) rational signature witnesses. It retains H80–H86 exact checks. Draft/unmerged; no human expert peer review, new Lean kernel proof, laboratory measurement, physical Einstein dynamics or CR-specific prediction.

**Recommended next H88 gate:** Stop accumulating arbitrary finite static comparators. Either (A) find an explicitly physically accessible, Poisson-projectable six-observable sector in an actual micro-source *and* prove its gravitational Hamiltonian transport, or (B) formally record a P9/P11 generative obstruction with missing assumptions and hand off to the physical P9.64 canonical-map work. Do not claim all quantum-geometric observable quotients are impossible.
