# H84 — Spatial Coupling Provenance, Local-Source Nonidentifiability, and Calibrated Edge-Response Tomography

**2026-10-18 | P3–P11 Mathematical Bridge / P9 GR-I / Route A**

**Status:** H83's exact symbolic polynomial checker was repaired on PR #102 (commit \`cab3167\`); its dedicated CI succeeds. H84 is the next **spatial-coupling source/provenance** gate. This note gives (a) a *physical positive-state positive-POVM*, all-CPTP counterexample to a unique **multi-cell** process selected by a single-cell source, and (b) exact conditional edge identification by real two-site measurements for a separately supplied ZZ control Hamiltonian. Neither result derives coupling or gravity from P3/F.

## 1. Scope and the candidate generative problem

The original H75 single-cell four-Kraus source \(\Phi_\mu:M_6\to M_6\) remains exactly unchanged, including the original microscopic \(R_2=0,\ R_3=i\operatorname{diag}(-32,16,16,0,0,0)/135\ne0\) for its declared diagonal seed. H84 considers **two physically separate copies** and differently correlated, independently declared **post-source apparatus noise**. The resulting total effective single-cell map is \(D_p\circ\Phi_\mu\), which is common to both extensions but not asserted equal to \(\Phi_\mu\), nor asserted to have the same P3 residue. Thus no inadvertent alteration of H75's original source or frozen P3 definitions occurs.

A physically spatially extended P9 theory needs more than cellwise \(\Phi_\mu\): it must specify or derive adjacency, intercell interaction/noise, preparation scope, causal availability of edge ports, and multi-cell joint readout, with independently justified Lorentzian/ADM soldering and field dynamics. H84 tests two sharply limited parts of this requirement.

## 2. H84.1 — Two different CP multichannel extensions with IDENTICAL all-input one-cell marginals (EXACT NO-GO for uniqueness)

Let \(Z_S=\operatorname{diag}(1,-1,1)\) and \(Z_6=I_E\otimes Z_S\). Define the full six-level parity conjugation \(U_Z(X)=Z_6XZ_6\), and \(p_0=9/25,\ p_1=16/25\). The local CPTP phase noise is
\[
D_p(X)=p_0X+p_1U_Z(X).
\]
On **two independent physical H75 microscopic cells**, form two ordinary CPTP maps
\[
\boxed{\begin{split}
\mathcal E_{\rm ind}
 &= (D_p\circ\Phi_\mu)\otimes(D_p\circ\Phi_\mu),\\
\mathcal E_{\rm com}
 &= \bigl(p_0\,\mathrm{id}_{36}+p_1\,\mathrm{Ad}_{Z_6\otimes Z_6}\bigr)
   \circ(\Phi_\mu\otimes\Phi_\mu).
\end{split}}
\]
Here the common-noise map consists of *two genuine random-unitary CPTP branches* with Kraus weights \(3/5,4/5\); the independent-noise map has *four* branches with Kraus weights \(9/25,12/25,12/25,16/25\). All Kraus completeness statements follow from \((3/5)^2+(4/5)^2=1\). The coherent microscopic source is not inferred to cause the common noise: it is extra physical apparatus/environment coupling.

For **every** two-cell joint input \(X\in M_6\otimes M_6\), including correlated and entangled states,
\[
\boxed{
\operatorname{Tr}_{2}\mathcal E_{\rm ind}(X)=
\operatorname{Tr}_{2}\mathcal E_{\rm com}(X)=
(D_p\circ\Phi_\mu)(\operatorname{Tr}_{2}X),
}
\]
and symmetrically for \(\operatorname{Tr}_{1}\). Proof: partial tracing a local CPTP map on the traced-away factor returns the original other-factor marginal; and \(\operatorname{Tr}_2[(Z_6\otimes Z_6)Y(Z_6\otimes Z_6)]=Z_6(\operatorname{Tr}_2Y)Z_6\). Thus the **entire local input-output CPTP map** on each cell is identical for the two globally inequivalent apparatus specifications, not just a few scalar moments.

**Physical positive-state/positive-POVM discriminator:** Prepare the genuine H75 post-source output \(\sigma=\Phi_\mu(|0,0\rangle\langle0,0|)\) independently on each cell. Take \(Y_{01}=i(|1\rangle\langle0|-|0\rangle\langle1|)\) on the visible qutrit (\(Y_{01}\) is Hermitian with eigenvalues \(+1,-1,0\)); lift \(O=I_E\otimes Y_{01}\). The actual H42 unitary gives
\[
\alpha=\operatorname{Tr}(O\sigma)=8/9,\qquad
\operatorname{Tr}(OZ_6\sigma Z_6)=-\alpha.
\]
(The sign convention fixes \(Y_{01}=[\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}]\) in the 0/1 block.) For the legitimate joint positive POVM effect \(Q_+=(I_{36}+O\otimes O)/2\), the exact output probabilities after the *source plus each declared noise architecture* are
\[
\boxed{p_+^{\rm ind}=\frac{53761}{101250},\qquad
p_+^{\rm com}=\frac{145}{162},\qquad
p_+^{\rm com}-p_+^{\rm ind}=\frac{2048}{5625}>0.}
\]
These are genuinely different two-cell operational predictions **despite equality of all one-cell marginals**. A simpler two-qubit exact rational verifier checks all 16 matrix units of common vs independent phase-noise channels and a joint \(XX\) parity-POVM probability contrast \(288/625\). The H75-specific positive witness uses the actual unchanged H75/H42 output, not a fabricated new source.

**NO-GO (precise):** \(\Phi_\mu\), even with complete single-cell data of \(D_p\circ\Phi_\mu\), and fixed local preparation/one-cell readout, cannot by themselves select a unique *actual* correlated multi-cell CPTP extension. Extra correlation/topology/noise provenance data are required, or a separately established source-derived uniqueness law. **This does NOT prove that a proposed F with new axioms can never generate coupling.** Shared environmental noise is not by itself a local Hamiltonian edge, nonzero curvature or a gravitational constraint.

## 3. H84.2 — An exact edge-coupling identification theorem (CONDITIONAL STANDARD QM)

To isolate what kind of operational data would *identify* a spatial interaction when a hardware Hamiltonian template **is independently supplied**, use four separately declared qubit cells with six possible unordered edges \(e=(i,j)\), distinct from P7/P8's four **internal K4 sites** or H83's spatial scalar quadrature grid. Define
\[
H(J)=\sum_{0\le i<j\le3}J_{ij} Z_iZ_j,\qquad
\rho_+=|+\rangle\langle+|^{\otimes4},\qquad
O_{ij}=Y_iZ_j.
\]
All \(J_{ij}\) are independently **specified hardware interaction coefficients**, not outputs of the original P3 channel. A pairwise Pauli measurement of \(Y_i\) and \(Z_j\) produces a legitimate two-outcome positive effect \(Q_{ij,+}=(I+Y_iZ_j)/2\), since \(Y_iZ_j\) is a Hermitian involution. Its small-time probability derivative at zero is
\[
\boxed{
\left.\frac{d}{dt}\operatorname{Tr}
   \bigl(Q_{ij,+}\,e^{-itH(J)}\rho_+e^{itH(J)}\bigr)\right|_{t=0}
=J_{ij}.
}
\tag{H84-R}
\]
**Proof:** The Heisenberg derivative is \(i[H(J),Q_{ij,+}]\). The only term with a nonzero \(|+\rangle^{\otimes4}\) expectation is the \(Z_iZ_j\) edge; it yields \(i[Z_iZ_j,Y_iZ_j]=2X_i\) and half this value for the POVM effect. Every other edge attached to i retains a \(Z_kZ_j\) factor with zero \(|+\rangle\) mean, and edges not touching i commute with the effect. Thus the full six-by-six Jacobian is the **identity**, \(\partial \dot p_{ij}/\partial J_{ab}=\delta_{(ij),(ab)}\), so every edge coefficient (including its sign) is identifiable under the declared preparation and readout.

Conversely, for only *single-site* readout \(X_i\) in the same initial preparation,
\[
\left.\frac{d}{dt}\langle X_i\rangle\right|_{0}=0,\qquad
\left.\frac{d^2}{dt^2}\langle X_i\rangle\right|_{0}
=-4\sum_{j\ne i}J_{ij}^2.
\]
At this differential order, sign information and adjacency distinctions can be lost. Hence a particular instrument/readout **catalog** matters, in the same sense as H81's control accessibility. The checker verifies the six exact Pauli-commutator slopes and local second derivatives for a nonuniform rational edge-weight witness.

**Important qualifier:** The edge-identification theorem is *operationally reconstructive*, not *generative*: measuring \(J_{ij}\) after assuming and calibrating a \(ZZ\) port does **not** show that P3, P6 or F compelled a specific \(J\), forced that graph, generated a continuum or yielded ADM gravity. The real-time pulse/readout must be physically available before relevant resets; it is precisely a new **spatial AX-OA** data field.

## 4. Separate the two kinds of missing spatial source data

- **Spatial correlation certificate** \(\mathscr E_{\rm corr}\): specifies joint intercell channels/common baths/noise couplings, their compatibility with all local marginals, allowed multi-cell preparations and joint positive readouts. H84.1 proves cellwise data do not select this field.
- **Spatial Hamiltonian edge certificate** \(\mathscr E_{\rm ham}\): specifies graph adjacency, strengths \(J_{ij}\), calibration, spatiotemporal port access and causal ordering. H84.2 proves coefficients are measurable in one finite comparator under strong independent assumptions. H84.1 common noise is **not equivalent** to this Hamiltonian interaction.

One may extend H82's AX-OA tuple by a separately typed multi-cell component \(\mathscr E=(\mathscr E_{\rm corr},\mathscr E_{\rm ham},\dots)\), or attempt a rigorous \(F\)-derived intercell source/solder selection theorem. **Neither is already a P1–P8 theorem.** Gauge/operational equivalence classes may be the mathematically natural target rather than unique literal hardware labels.

## 5. Hand-off to P9 / P11 and next gate

**To P9:** Spatially extended local CPTP data leave correlations and intercell Hamiltonian unspecified. H83's nontrivial H–H flux arises only with a declared gradient coupling; H84 supplies an independent *operational identification* protocol for a declared ZZ graph, **not** the metric-gradient coupling or physical K4/ADM solder. The next genuinely gravitational gate is a **source-to-edge/solder construction** that supplies \(g^{ij}\), a spatial derivative operator and a correct canonically normalized field Hamiltonian, simultaneously respecting the H59 symplectic/topology and H61 DeWitt/polarization obstacles, then **all** H–H/H–D/D–D nonuniform off-shell relations.

**To P11:** Treat selection of multi-cell process extensions and edge-port accessibility as explicit generative-completeness obligations. The H84 CP extension example supplies a scoped **relative nonidentifiability counterexample**; the positive POVM and identity edge-response Jacobian quantify what extra empirically certifiable data can resolve. They do not refute generation by a stronger future F axiom.

**Verdicts:** H84.1 same-local-marginal/different-joint-CPTP channel = **EXACT** with independently declared physical noise; H84.2 \(J\) reconstruction = **CONDITIONAL EXACT** standard QM; microscopic \(\Phi_\mu\to J_{ij}\), external \(\mathscr E\) from F, spacetime metric or EH/Einstein dynamics = **OPEN**. CI checks exact positive-state/probability certificates, all qubit basis-unit marginal equalities, source nonzero original P3 witness, Pauli response and inherited H80–H83 gates. Draft only; no frozen/main modifications or human peer review, Lean kernel proof, CR-only empirical discriminator or experiment.
