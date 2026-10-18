# H99 — Physical-Source K4 Metric Rank-3 Deficit and Curvature Two-Jet Nonselection

**2026-10-18 | P9 GR-I G3/G4/G5; P3–P11 Mathematical Bridge, Route A.**
Base H98 Draft PR #117, **100/100 CI PASS**. Original genuine H75 four-Kraus six-level CPTP source, signed P3 R3, frozen P1–P8 and main unchanged. No new free physical Hamiltonian, ADM momenta or field equation is introduced. The spatial coordinates, K4 solder, positive graph selector and later ADM gravitational comparison remain **independent conditional premises**.

## 1. Exact source-selected configuration rank is three, not six

H85's actual H75 positive flag outcomes for four **separately prepared** qutrit states are
\[
r_\star=(0,16/25,16/25,4/25),\quad S_\star=36/25.
\]
Only after independently specifying four spatial-cell labels, a K4 topology, fixed edge budget W=27 and endpoint-local additivity does H85 choose
\[
w_{ij}(r)=\frac{W(r_i+r_j)}{3\sum_a r_a},
\quad w_\star=(4,4,1,8,5,5)
\]
in edge order 01,02,03,12,13,23. Exactly, for any positive-total r:
\[
\boxed{
w_{01}+w_{23}=w_{02}+w_{13}=w_{03}+w_{12}=W/3=9.
}
\tag{H99-COMP}
\]
These are three independent affine constraints on six edge weights. Moreover the selector is scale-invariant: w(cr)=w(r). Its 6-by-4 Jacobian obeys
\[
\frac{\partial w_{ij}}{\partial r_a}
=\frac W{3S}
\left(\delta_{ai}+\delta_{aj}-\frac{r_i+r_j}{S}\right),
\quad \boxed{\operatorname{rank}D_rw(r_\star)=3,\quad D_rw(r_\star)r_\star=0.}
\tag{H99-R3}
\]
The unsigned edge/endpoint incidence has full column rank four. The projective scale direction is the sole smooth ambient null direction, leaving exact rank three. The true physical readout profile touches probability-box boundaries, so physically admissible small changes may be one-sided, but their accessible local rank cannot **exceed** this exact algebraic rank.

H98 established an invertible abstract six-dimensional weight-to-positive-metric chart
\[
g(w)=16G_0[B^\top L_wB]^{-1}G_0,\quad
B=(e_0-e_3,e_1-e_3,e_2-e_3),\quad G_0=B^\top B.
\]
Although \(\det D_wg(w_\star)\neq0\), its **actual selected composite from only the four H75 readouts** has
\[
\boxed{\operatorname{rank}D_r[g(w(r))]_{r_\star}=3<6.}
\tag{H99-METRIC}
\]
Therefore H98's six freely independently adjustable edge positions and six canonical edge momenta constitute an **external T*R6 completion** rather than physical source-generated ADM 6+6 canonical data. The projective source-image submanifold is three-dimensional; even declaring its cotangent bundle externally supplies only three canonical pairs. This restriction concerns the **specific normalized H85 additive selector**, not all possible additional P3/CR measurements or physics.

## 2. Exact positive CPTP extension with identical local 1-jets and different 3D scalar curvature

The H85 positive metric at the true selected source value is
\[
g_\star=
\begin{pmatrix}
144/49&64/49&64/49\\
64/49&2192/1225&1408/1225\\
64/49&1408/1225&2192/1225
\end{pmatrix},
\quad\det g_\star=4096/1225,\quad\sqrt{\det g_\star}=64/35.
\]
Give an **external** 3D spatial chart x and define \(s(x)=x^\top g_\star x\). On the ellipsoidal neighborhood 0≤s≤1 construct two smooth source-outcome profiles:
\[
\boxed{
r^{(a)}(x)=r_\star+a s(x)(0,-1,0,+1),
\qquad a=0,\quad a=1/5.
}
\tag{H99-PROFILES}
\]
These are not abstract signed probabilities: every value is physically realizable from the **unchanged original H75 CPTP** source. The only changing outcomes satisfy
\[
r_1\in[11/25,16/25],\qquad r_3\in[4/25,9/25]\subset[0,16/25].
\]
For sites 1 and 3 prepare the genuine positive normalized qutrit density operator
\[
\rho_i(x)=\left(1-\frac{25r_i(x)}{16}\right)d_0
+\frac{25r_i(x)}{16}d_1;
\]
use d0 at site 0 and d2 at site 2. The actual four-Kraus H75 source produces the specified true positive flag outcome at **every** x in the stated region. The external x-labelled preparation schedule, K4 solder and any physical intercell influence are **not** derived from H75, P3 or F.

Use the **same positive normalized endpoint selector** \(w^{(a)}(x)=w(r^{(a)}(x))\) with \(\sum_e w_e=27\) for every x. Since \(\sum r^{(a)}(x)=36/25\) is constant,
\[
w^{(a)}(x)=w_\star+a s(x)d,\quad
d=(25/4)(-1,0,+1,-1,0,+1),
\]
and every weight remains strictly positive for 0≤s≤1. Both fields share identical zero- and first-order local observations and spatial geometry at x=0:
\[
\boxed{
r^{(0)}(0)=r^{(1/5)}(0)=r_\star,\quad
w^{(0)}(0)=w^{(1/5)}(0)=w_\star,\quad
g^{(0)}(0)=g^{(1/5)}(0)=g_\star,
\quad \partial_i r=\partial_i w=\partial_i g=0.
}
\tag{H99-ONEJET}
\]

Nevertheless **their scalar curvatures differ**. For \(C=B^\top L_wB\) and the d-direction,
\[
C_\star=\begin{pmatrix}22&13&13\\13&38&13\\13&13&38\end{pmatrix},\quad
C_1=\begin{pmatrix}25&25&25\\25&0&25\\25&25&25\end{pmatrix}.
\]
The genuine positive K4 metric differential is
\[
g_1=-16G_0C_\star^{-1}C_1C_\star^{-1}G_0,\qquad
\mathrm{tr}(g_\star^{-1}g_1)
=-\mathrm{tr}(C_\star^{-1}C_1)=-51/98.
\]
Since \(s\) is quadratic and the reference g is spatially constant,
\[
g^{(a)}(x)=g_\star+a s(x)g_1+O(s^2),
\quad
\partial_i\partial_jg^{(a)}_{kl}(0)=2a(g_\star)_{ij}(g_1)_{kl}.
\]
Using the exact standard Levi-Civita scalar curvature formula at vanishing Christoffel symbols at x=0,
\[
\begin{aligned}
R[g^{(a)}](0)
&=g_\star^{ij}g_\star^{kl}
(\partial_k\partial_jg^{(a)}_{il}
-\partial_k\partial_lg^{(a)}_{ij})\big|_0\\
&=-4a\,\mathrm{tr}(g_\star^{-1}g_1)
=\frac{102a}{49}.
\end{aligned}
\]
Thus
\[
\boxed{R[g^{(0)}](0)=0,\qquad R[g^{(1/5)}](0)=102/245\neq0.}
\tag{H99-CURVATURE}
\]
The exact Fraction checker evaluates BOTH the matrix-trace expression and the independent full four-index second-derivative curvature contraction.

As a **conditional standard ADM comparison only**, fix \(\pi^{ij}(0)=0\), cosmological constant zero and conventional \(\mathcal H= ( \pi^{ij}\pi_{ij}-\pi^2/2)/\sqrt g-\sqrt gR\). Then the two nominal Hamiltonian constraint densities at the same point, with identical local source outcomes and the same local momentum, are
\[
\boxed{
\mathcal H^{(0)}(0)=0,\qquad
\mathcal H^{(1/5)}(0)=-(64/35)(102/245)
=-6528/8575\neq0.
}
\tag{H99-ADM-WITNESS}
\]
The same pointwise source facts and **same spatial 1-jet** cannot select the physical curvature-potential value or determine whether this externally imported ADM constraint holds. An actual neighborhood metric **including its 2-jet** would, of course, determine the ordinary Levi-Civita curvature uniquely; no contradiction of differential geometry is claimed.

## 3. G3/G4/G5/P11 proof obligations

**G3:** The specific four-positive-readout normalized H85 selector only spans **three** independent metric configuration directions. H98's six independent positive K4 edge weights and six conjugate momenta are a formal **external completion**, not a source-produced physical 6+6 ADM phase space. Additional source-origin metric fields and physically controlled canonical momenta remain unsolved.

**G4:** Even all weight positivity, a fixed total budget, normalized A4 additive covariance, exact original source-positive preparation at every externally labelled x and identical local first jets **do not select** the 3D spatial scalar curvature. A genuine physical second-spatial-jet law, cell solder/interactions and curvature potential remain to be sourced.

**G5/G6:** Two source-consistent spatial continuations give **different** curvature and opposite outcomes for the *zero* vs *nonzero* standard ADM Hamiltonian constraint density at \(\pi=0\). H98 selected the DeWitt coefficient \(\lambda=1/2\) only after **independently importing** continuum curvature, brackets and the standard momentum generator. Complete nonuniform off-shell HDA and Einstein equations are still **OPEN**.

**P11:** An AX-SP/AX-CAN/AX-DYN completion must source (i) the remaining three independent spatial configuration directions or a physically justified reduction, (ii) physical canonical momenta, (iii) a spatial second-jet/intercell curvature law, and (iv) a physically selected action and constraint algebra. The H75 channel alone does not uniquely determine these additional objects.

**Scope:** The constructed \(r(x)\) are **external spatial profiles of separately prepared quantum experiments**, not a demonstrated propagating quantum field or sourced gravitational background. The K4 graph/topology/endpoint selector and Levi-Civita/ADM identification are conditional extra inputs. This is an exact mathematical/positive-CPTP witness **inside that specific conditional framework**, not a universal No-Go against future coherent/historical P3 physical generations.

**Exit:** H100 should not endlessly generate fresh spatial toy metrics. It must identify an **already physically justified intercell/spatial coupling generating the second jet and canonical momenta**, or hand off these exact rank-and-curvature blockers to P9/P11 as unproven axioms. No human peer review, laboratory demonstration, Lean kernel proof or generated Einstein equations.
