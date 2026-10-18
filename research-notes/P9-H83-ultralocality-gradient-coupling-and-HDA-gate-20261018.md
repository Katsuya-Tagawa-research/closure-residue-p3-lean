# H83 — Ultralocality Obstruction and Conditional Nearest-Neighbor Spatial-Coupling Gate

**2026-10-18 | P9 GR-I, P3–P11 Mathematical Bridge / Route A.**

**Purpose:** Immediately after the H82 integration handoff (**95/95 Actions PASS on H82 head**, Draft #101), return to a *gravitational* rather than memory-rank question: can independent finite microscopic closure cells ever supply the spatial-gradient structure required by a nontrivial hypersurface-deformation algebra (HDA)? This note proves a limited **ultralocal No-Go**, gives a **conditional constructive** edge-coupling bracket on a periodic spatial lattice, and independently witnesses why its H–H success is **not** a full off-shell ADM constraint algebra. It does **not** claim micro-CR provenance of the required coupling.

## H83.1 — Ultralocal no-go (EXACT under canonical field assumptions)

Suppose a spatial manifold carries separately declared canonical fields \(q^A(x),p_A(x)\) with \(\{q^A(x),p_B(y)\}=\delta^A_B\delta(x-y)\), and let
\[
H[N]=\int_\Sigma N(x)\,h(q(x),p(x))\,d^dx,
\]
where the Hamiltonian density \(h\) has **no spatial derivatives of fields, no nonlocal kernels and no derivative dependence on \(N\)**. For compactly supported lapses (or boundary conditions without extra terms),
\[
\frac{\delta H[N]}{\delta q^A(x)}=N(x)\frac{\partial h}{\partial q^A}(x),\quad
\frac{\delta H[N]}{\delta p_A(x)}=N(x)\frac{\partial h}{\partial p_A}(x),
\]
and hence
\[
\boxed{\{H[N],H[M]\}=\int NM\,\sum_A
(\partial_{q^A}h\,\partial_{p_A}h-\partial_{p_A}h\,\partial_{q^A}h)=0.}
\]
The same result holds for independent canonical lattice cells and for separately selected ultralocal Hamiltonian densities \(h_i\). A *pointwise canonical reparametrization* cannot change this zero bracket. Thus, for generic configurations with a nonzero spatial momentum constraint \(D[\beta]\), independent ultralocal cells **cannot realize the nontrivial ADM relation**
\[
\{H[N],H[M]\}=D[g^{ij}(N\partial_jM-M\partial_jN)]
\]
off shell. It is the **combination** of canonical locality, identical lapse-smeared ultralocal density and a demanded **nontrivial faithful HDA** that causes the obstruction. A degenerate/trivial \(D=0\) representation is not ruled out. Neither the finite P3 residual filtration nor the K4 weight chart alone has been shown to supply the required spatial derivative interactions.

This is a standard canonical locality argument specialized to the present P9 generation boundary, **not a novel quantum-gravity no-go theorem**.

## H83.2 — Minimal edge-gradient benchmark (CONDITIONAL EXACT)

Choose **four spatial lattice cells on a periodic ring**, independent of the **four internal sites of any K4 chart**. Give each cell an independently postulated real canonical scalar pair \((q_i,p_i)\), \(\{q_i,p_j\}=\delta_{ij}\), and positive constants \(A,\kappa\). Define
\[
H_{\mathrm{edge}}[N]=
\sum_{i\in\mathbb Z/4\mathbb Z}\left[
\frac A2 N_i p_i^2+
\frac\kappa4(N_i+N_{i+1})(q_{i+1}-q_i)^2\right].
\]
Then **as a polynomial identity for all \(q,p,N,M\)**,
\[
\boxed{
\{H_{\mathrm{edge}}[N],H_{\mathrm{edge}}[M]\}
=\frac{A\kappa}{2}\sum_i
(N_iM_{i+1}-M_iN_{i+1})
(p_i+p_{i+1})(q_{i+1}-q_i).
}
\tag{H83-E}
\]
**Proof:** Write the potential part as a sum of edge differences. Its derivative at vertex \(i\) is
\[
\partial_{q_i}H[N]=\frac{\kappa}{2}
[(N_{i-1}+N_i)(q_i-q_{i-1})
 -(N_i+N_{i+1})(q_{i+1}-q_i)],
\]
while \(\partial_{p_i}H[N]=A N_i p_i\).
Kinetic–kinetic and potential–potential brackets vanish. The remaining cross terms regroup by edge into (H83-E). \(\square\)

The edge **lapse wedge** \(N_iM_{i+1}-M_iN_{i+1}\) is the discrete precursor of the continuum antisymmetrized lapse derivative. With lattice spacing \(a\), the appropriately normalized benchmark
\[
H_a[N]=\sum_i\left[
a\frac A2 N_i p_i^2+\frac{\kappa}{4a}
(N_i+N_{i+1})(q_{i+1}-q_i)^2\right],
\quad\{q_i,p_j\}=\frac{\delta_{ij}}a,
\]
has bracket \(A\kappa/(2a)\) times the edge sum in (H83-E) without its coefficient; for smooth continuum test profiles sampled on a refining periodic grid, this tends formally (under the usual smoothness and quadrature hypotheses) to
\[
\boxed{
\{H[N],H[M]\}_{\rm matter}
=\int dx\,A\kappa\,p\,\partial_xq
\,(N\partial_xM-M\partial_xN).
}
\]
The formal continuum identity is the **scalar-field H–H symbol**, NOT a derivation of the continuum, scalar constraint density, physical metric, or Einstein gravity from finite CR. For an arbitrary nonconstant dynamical background, cross brackets with gravitational degrees of freedom need additional analysis.

An independent exact sparse-rational-polynomial checker proves (H83-E) for all 16 formal variables in the 4-cell ring, not merely selected floating-point samples. For the explicit off-shell profile \(A=3/2,\kappa=5/3\), \(q=(0,1/2,1/3,-1/4)\), \(p=(1,2,-1,3)\), \(N=(1,0,2,-1)\), \(M=(0,1,-1,2)\),
\[
\boxed{\{H[N],H[M]\}=-55/12\ne0.}
\]
The nonzero value only certifies the specific **assumed edge coupling**.

## H83.3 — Finite-lattice H–H factorization does not yield full HDA (EXACT countercheck)

Define the natural, but **separately assumed**, symmetric edge shift candidate
\[
D_{\rm edge}[b]=\frac12\sum_i b_i(p_i+p_{i+1})(q_{i+1}-q_i).
\]
The H–H bracket (H83-E) is exactly \(A\kappa\,D_{\rm edge}[b(N,M)]\), where \(b_i=N_iM_{i+1}-M_iN_{i+1}\). This does **not** ensure H–D and D–D off-shell closure with continuum diffeomorphism composition on a fixed discrete grid. In particular, with the naive central differences
\[
b_i^{\rm site}=\frac12(b_{i-1}+b_i),\quad
\nabla_cN_i=\frac12(N_{i+1}-N_{i-1}),\quad
L_i=b_i^{\rm site}\nabla_cN_i,
\]
the canonical bracket generally does **not** satisfy \(\{D_{\rm edge}[b],H_{\rm edge}[N]\}=H_{\rm edge}[L]\).

A fully rational counterexample has the above \(q,p,N\) and \(b=(2,0,1,-1)\), with \(A=3/2,\kappa=5/3\):
\[
\{D_{\rm edge}[b],H_{\rm edge}[N]\}=-31679/1728,\qquad
H_{\rm edge}[L]=149/96,
\]
hence exact discrepancy
\[
\boxed{\{D_{\rm edge}[b],H_{\rm edge}[N]\}-H_{\rm edge}[L]=-34361/1728\ne0.}
\]
This is **a counterexample to the explicitly defined naive lattice shift/Lie-derivative comparison**, *not* a proof that every discretization or refinement can never reproduce continuum HDA. Avoid claiming Einstein dynamics from a single correct H–H sub-bracket.

## H83.4 — Conditional metric-symbol interface to the existing P9 K4 chart

The previously established positive \(K_4\) chart on \(S=\mathbf1^\perp\subset\mathbb R^4\) is
\[
A_w=\sum_{a<b}w_{ab}(e_a-e_b)(e_a-e_b)^\top,\quad
g_w=16(A_w|_S)^{-1},\quad
g_w^{-1}=\frac1{16}A_w|_S.
\]
For **an independently soldered spatial covector** \(v\in S\), a scalar gradient coupling in this spatial direction could be calibrated to
\[
\boxed{A\kappa(w)=\langle v,g_w^{-1}v\rangle=
\frac1{16}\sum_{a<b}w_{ab}(v_a-v_b)^2.}
\]
This is precisely the *conditional matter H–H inverse-metric symbol matching* of H61 in one direction; it does **not** force the coefficient from P3 or establish full ADM. For \(v=(1,1,-1,-1)/2\), \(\|v\|=1\), uniform \(w_{ab}=1\) gives \(A\kappa=1/4\). In edge order \((01,02,03,12,13,23)\), \(w=(1,2,1,3,2,1)\) gives \(A\kappa=1/2\). This positive-definite *matter acoustic contraction* does **not** fix H61's separate \((5+,1-)\) gravitational **DeWitt kinetic signature** obstruction.

The finite polynomial example above chose \(A\kappa=5/2\) only for its rational witness, and is **not** claimed to be simultaneously metric-matched to either specified \(K_4\) weight point. Such metric matching is an **additional condition**, not an identity satisfied by arbitrary numbers.

## H83.5 — P9/P11 consequences and next real proof gates

**EXACT:** A nontrivial HDA cannot arise from a purely independent ultralocal canonical Hamiltonian density; an explicitly assumed nearest-neighbor gradient interaction generates a nontrivial H–H edge-flux symbol and its anticipated smooth scalar limit.

**CONDITIONAL:** Interpreting the coefficient as physical \(g^{ij}\) needs a certified spatial solder and metric; propagating this to gravitational phase space needs independently generated canonical variables and a correct local DeWitt sector; obtaining full nonuniform off-shell HDA needs **H–H, H–D, D–D** closure with field-dependent structure functions, continuum/refinement/regularization and boundary consistency.

**NO-GO:** One naive finite grid \(D_{\rm edge}\) fails the continuum-type H–D comparison exactly. No general lattice gravity impossibility is claimed.

**OPEN (generative physics):** Original P3 residual data and H75–H82 operational-accessibility results do not generate the edge strength, spatial topology/adjacency, preferred lapse field, spatial solder, canonical symplectic map, DeWitt signature, full HDA or Einstein action. P11 AX-OA may certify a *physical spatial interaction port and schedule*, but such a certificate is still an independent assumption unless \(\mathcal G_{\rm access}(F,\dots)\) is proved.

**Recommended next P9 step:** Seek a real *micro-source-to-spatial coupling* selection principle with independently testable hardware/interaction provenance and a construction preserving spatial covariance/constraint closure; then tackle the Lorentzian DeWitt kinetic sector. Stop before falsely calling an imposed scalar gradient term a CR-generated Einstein theory.

**CI:** Exact Fraction sparse polynomial checker for ultralocal zero, full symbolic edge identity, nonzero off-shell witness, definite naive H–D mismatch, K4 metric contraction; retain H82/H80/H81 validation on stacked branch. This is an original scoped integration/benchmark note, not human expert peer review, experimental test, Lean formalization, or derivation of Einstein equations.
