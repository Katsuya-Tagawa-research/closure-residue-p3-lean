# H100 — Conditional Einstein Constraint Closure Selects Structure but Does Not Generate Couplings: Source-to-Gravity P9/P11 Proof Gate

**2026-10-19 | P9 GR-I / P3–P11 Mathematical Bridge | G3–G6 and P11 axioms.**
**Base:** H99 Draft PR #118, original H99 source-rank/curvature checker and H98 regression **PASS**, 100/100 GitHub Actions on audited H99 head. Original H75 four-Kraus CPTP source, original signed P3 R3, main and frozen P1–P8 unchanged. No sourced Einstein field equations are claimed.

## 1. Question: How much is selected by the H–H bracket, versus borrowed from ADM?

H98 established, *conditional on independently imported canonical continuum ADM fields and scalar-curvature potential*, that flat nonuniform off-shell Hamiltonian-constraint closure selects the DeWitt trace coefficient \(\lambda=1/2\) within a kinetic one-parameter family with normalization already fixed. H99 showed two more **source-side** obstacles: the four actual H75 readouts via H85's *specific* normalized additive K4 selector have spatial metric rank 3, not 6; and even positive H75 outputs agree at a point through the first spatial jet while independent externally chosen spatial continuation laws produce distinct scalar curvatures and local standard ADM constraint values.

H100 allows the **two independent dynamical normalization parameters** and a cosmological density on the ADM comparison side. We ask whether even requiring a correctly normalized, *nonuniform, off-shell* H–H bracket determines a unique physical Hamiltonian and selects it from microscopic H75/P3/F data.

**Important provenance:** All continuum fields, \(\{g_{ij}(x),\pi^{kl}(y)\}\), a true 3D spatial atlas, curvature \(R[g]\), spatial derivative operators, ADM momentum constraint and the Hamiltonian family below are independently supplied **standard-GR comparator** ingredients. Inserting them is **not** deriving their existence from the original finite Closure–Residue source.

## 2. H100.1 — The two-normalization flat H–H constraint gate (EXACT conditional field calculation)

On a three-dimensional smooth spatial field with fixed standard ADM canonical Poisson convention and compactly supported/suitable zero-boundary lapse tests, introduce
\[
\boxed{
\mathcal H_{\alpha,\beta,\lambda,\Lambda}
=\frac{\alpha}{\sqrt g}\bigl(\pi^{ij}\pi_{ij}-\lambda\pi^2\bigr)
-\beta\sqrt g R[g]+2\Lambda\sqrt g,
\quad
H[N]=\int N\mathcal H,\quad
D[V]=\int V^i(-2g_{ij}\nabla_k\pi^{jk}).
}
\tag{H100-H}
\]
The kinetic/curvature normalizations \(\alpha,\beta\), conformal trace coefficient \(\lambda\), and cosmological density \(\Lambda\) are **free input parameters** on the comparator side.

At the **flat spatial metric** \(g_{ij}=\delta_{ij}\), with arbitrary *off-shell*, nonuniform symmetric momentum \(\pi^{ij}(x)\) and lapse N,M, antisymmetrized kinetic–kinetic brackets cancel because no spatial derivatives occur in K; potential–potential brackets vanish since both are functions of g; kinetic–cosmological cross brackets cancel because the \(\Lambda\)-term has no lapse derivatives. Only kinetic–curvature cross terms survive, proportional to \(\alpha\beta\). The resulting exact **flat-background, nonuniform** bracket is
\[
\boxed{
\{H[N],H[M]\}\big|_{g=I}
=\alpha\beta\left[
D[v]\big|_{g=I}
+2(1-2\lambda)\int v_i\,\partial^i\pi\,d^3x
\right],\qquad
v^i=N\partial^iM-M\partial^iN,\quad\pi=\pi^j{}_j.
}
\tag{H100-FLAT}
\]
No dependence on \(\Lambda\) remains. This is a **necessary flat-background off-shell comparator**, *not a proof of full arbitrary-metric HDA from P3*. The standard unscaled ADM right side is \(D[v]\), with coefficient exactly one in the independently chosen spatial momentum/lapse normalization.

## 3. H100.2 — Two independent rational nonuniform momentum probes force αβ=1 and λ=1/2 (EXACT conditional)

On \(x\in[0,1]\) times a unit transverse 2-torus, take the same rational nonhomogeneous lapses/profiles verified in H98:
\[
N=x(1-x),\quad M=x^2(1-x),\quad
f=x^2(1-x),\quad
v^x=NM'-MN'=x^2(1-x)^2,
\]
\[
\boxed{c=\int_0^1 f'(x)v^x(x)\,dx=\frac1{210}>0.}
\tag{H100-C}
\]
The two momentum profiles are independent **off-shell test configurations**, not fabricated sourced H75 momenta:

**Probe T — Traceless and divergent:** \(\pi^{ij}_T=f\,\mathrm{diag}(1,-1,0)\), with \(\mathrm{tr}\pi_T=0\), but \(D_T[v]=-2c=-1/105\ne0\). Thus
\[
\boxed{
\{H[N],H[M]\}_T=-\frac{\alpha\beta}{105},
\quad D_T[v]=-\frac1{105}.
}
\tag{H100-T}
\]
Requiring the **standard** H–H equality for this single nonuniform traceless probe forces
\[
\boxed{\alpha\beta=1.}
\tag{H100-PRODUCT}
\]
In other words, off-shell closure selects a **product** of kinetic and curvature normalizations, not either individually.

**Probe I — Pure isotropic:** \(\pi^{ij}_I=f\,\delta^{ij}\), with \(D_I[v]=-1/105\) but trace gradient \(\partial_x\pi_I=3f'\). The bracket is
\[
\boxed{
\{H[N],H[M]\}_I
=\frac{\alpha\beta(2-6\lambda)}{105},
\quad D_I[v]=-\frac1{105}.
}
\tag{H100-I}
\]
With \(\alpha\beta=1\), this second, independent off-shell probe requires
\[
\boxed{\lambda=\frac12.}
\tag{H100-LAMBDA}
\]
Conversely at the **flat** background these two conditions eliminate the displayed anomaly for *all* smooth momenta/lapses in the assumed comparator family.

This calculation is more informative than H98's **single isotropic** test: the traceless probe separates the otherwise confounded curvature normalization from the DeWitt trace coefficient. Both probes are integrated exactly by two independent Fraction-polynomial methods: direct lapse-second-derivative functional cross terms and their integration-by-parts momentum/trace-gradient decomposition. Neither is a minisuperspace or on-shell check.

## 4. H100.3 — Exact residual physical nonuniqueness after the H–H test (EXACT within imported comparator)

The standard normalized flat off-shell H–H test leaves the **two-parameter continuum**
\[
\boxed{
(\alpha,\beta,\lambda,\Lambda)
=\left(a,\frac1a,\frac12,\ell\right),
\quad a>0,\quad \ell\in\mathbb R.
}
\tag{H100-FAMILY}
\]
Here \(a\) is a kinetic-vs-curvature coupling scale analogous to choosing a gravitational coupling normalization; \(\ell\) is cosmological energy density. Standard HDA closure does not itself fix a Newton constant or a cosmological constant. Their values require additional physical normalization/boundary/measurement/axiomatic input. A common rescaling convention might set \(a=1\), but it **must be declared** rather than silently attributed to H75, P3 or F.

The *same* original H75 channel, same qutrit/flag observations and same conditional positive K4 response metric are compatible with all these externally supplied comparator choices. In particular the two examples
\[
(1,1,1/2,0),\qquad (2,1/2,1/2,0)
\]
give **identical** standard normalized flat H–H bracket with the same D, while their Hamiltonian densities are not equal for general physical canonical data.

Use H99's **genuinely H75-source-positive**, externally spatially labeled curvature witness at x=0: the two profiles have identical source-readout 1-jets but \(R^{(0)}=0\) and \(R^{(1/5)}=102/245\), with the same \(g_\star\) satisfying \(\sqrt{\det g_\star}=64/35\). At independently supplied \(\pi=0\) the comparison Hamiltonian density is
\[
\boxed{
\mathcal H_{\alpha,\beta,\lambda,\Lambda}(0)
=-\beta\frac{6528}{8575}
+\frac{128\Lambda}{35}
\quad\text{(curved profile),}
}
\tag{H100-CURVE}
\]
whereas on the flat profile it is \(128\Lambda/35\). For \(\Lambda=0\) and the two equally H–H-compatible coupling pairs above the curved constraint densities are \(-6528/8575\) and \(-3264/8575\), respectively; nothing in the original local microscopic source singles out one.

This remains **an underdetermination/provenance result**, not a theorem that no future physical axiom can select a or ℓ. Nor does a finite list of flat tests alone establish all standard ADM H–D/D–D brackets or the Einstein field equations.

## 5. H100.4 — Minimal typed P9/P11 generative completion gates

The first 100 bridge stages supply numerous **EXACT finite results and explicit conditional ADM comparisons**, but the following *physical arrows* are still OPEN:

1. **AX-SP / Spatial source and 2-jet:** A genuinely microscopic spatial localization, independent cell-to-cell transport/gluing, effective field regularity and **selected spatial connection/curvature second-jet** must arise from P3/F rather than an externally assigned coordinate mesh/profile. H99 proved the original four-readout selected K4 metric has rank3 and 1-jet alone does not select curvature.
2. **AX-CAN / Physical momenta and symplectic transport:** Actual source-realized **6+6** unreduced canonical variables or justified gauge-reduced equivalents, \(\omega\)- and Hamiltonian-preserving transport, and positive operational access. H95–H97 show the original one-reset real control route cannot provide these; H98's cotangent lift imports six canonical momenta.
3. **AX-DYN / Curvature and momentum constraint action:** The negative DeWitt conformal mode, a field \(R[g]\) potential, source-origin diffeomorphism momentum constraint and their nonuniform off-shell Poisson closure. H98/H100 merely show **what the standard ADM comparator selects after these are inserted**.
4. **AX-NORM / Couplings and scale:** Supply a source principle or explicit independent physical calibration that selects a gravitational coupling scale (the residual \(a\)), cosmological sector (\(\ell\)), lapse normalization, units/boundaries, and matter interactions. **H–H closure alone does not select them.**
5. **AX-GEN / Noncircular F-completeness:** Precisely typed map from closure/residue observations and independently declared physical controls to the above observable fields and action, with an external-vs-derived ledger and nontrivial, falsifiable physical consequences distinct from ordinary quantum measurement. At present this is a P11 proposal, not a completed axiom/theorem.

**Consequence for P9 GR-I:** It is legitimate to state a **conditional Einstein/ADM theorem**: *if* an independently identified CR sector carries a full continuum canonical ADM field representation, curvature/diffeomorphism constraints and their correct off-shell closure, then the flat nonuniform H–H test fixes λ=1/2 and αβ=1, with a, ℓ still free. It is not legitimate to assert that original finite H75/closure–residue data have **generated** these premisses. G3→G4→G5→G6 remain explicit proof obligations.

**Stopping rule and next step:** Do not create further arbitrary Hamiltonian-parameter families after H100. Either start a **specific physical source theorem** for canonical field/memory, or convert this typed gate ledger into **P11 F axiomatization** as explicit independent assumptions pending derivation and use it as the governing roadmap for P9/P12. The scope excludes a human-reviewed proof, Lean formalization of Einstein, actual sourced gravitational experiments or an unconditional quantum-gravity result.

**Verification:** exact all-Fraction two nonuniform momentum probes with independent integration routes, αβ normalization/rank checks, λ selection, Λ cancellation, residual family, and H99 original positive source-curvature witness. Dedicated regression CI for H83/H85/H90/H96–H99. No frozen-paper/main modifications.
