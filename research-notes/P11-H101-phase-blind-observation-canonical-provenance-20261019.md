# H101 — P11 AX-OA / AX-CAN: Phase-Blind Positive Source Data Do Not Determine a Physical Canonical Momentum

**2026-10-19 | P11 The Generative Map (F) / P9 GR-I G3–G4, Route A.**
**Base:** H100 Draft PR #119, dedicated H100 and global CI **100/100 PASS**. Original H75 true four-Kraus CPTP quantum source, original P3 signed residual \(R_3\neq0\), H85 normalized K4 selector, main, and frozen P1–P8 are UNCHANGED. No proposed mathematical "phase current" is identified with ADM momentum absent an independent source theorem.

## Question

H99 established that the **four H75 flag probabilities** used by the specifically normalized H85 endpoint-additive K4 selector determine at most a three-real-dimensional projective metric family, rather than six independent ADM configuration directions. H100 showed that even importing continuum ADM constraint algebra does not select gravitational coupling normalization or cosmological density.

H101 asks a stronger *physical observational sufficiency* question at the **already constructed** H75 source:

> Is the observed H85 four-probability K4 data complete for the microscopic phase information that a prospective physical canonical transport law would need? Could an ADM-like canonical momentum be recovered as a function of the same normalized observations without declaring additional readouts, preparation controls, or independent physical momentum laws?

## H101.1 — A continuous family of TRUE positive qutrit states with identical H75/K4 geometry (EXACT)

Use the original H75 qutrit site computational basis \(d_0=|0\rangle\langle0|\), \(d_1=|1\rangle\langle1|\). Replace **only the fourth** original H85 preparation \(\rho_3=(3/4)d_0+(1/4)d_1\) by
\[
\boxed{
\rho_t=
\begin{pmatrix}
3/4 & it/4&0\\
-it/4&1/4&0\\
0&0&0
\end{pmatrix},\quad -1\le t\le1.
}
\tag{H101-STATE}
\]
Every \(\rho_t\) is a valid positive trace-one input, not a signed tangent masquerading as a quantum state: its only nonzero 2-by-2 principal block has diagonal \(3/4,1/4\) and determinant \((3-t^2)/16\ge1/8>0\).

The unchanged H75 four-Kraus source uses
\[
M_0=\operatorname{diag}(1,3/5,3/5),\quad
M_1=\operatorname{diag}(0,4/5,4/5),\quad
L_{ab}=|a\rangle\langle b|\otimes U M_a.
\]
The true positive physical flag-1 effect is
\[
r_3(t)=\operatorname{Tr}\bigl[M_1\rho_tM_1\bigr]
=(16/25)\rho_{t,11}=\boxed{4/25}
\quad\text{for all }t.
\]
The **other three** original H85 preparations remain \(d_0,d_1,d_2\), with their unaltered positive outcomes. Hence the full observation tuple stays
\[
\boxed{r(t)=(0,16/25,16/25,4/25)}
\quad\Longrightarrow\quad
\boxed{w_{ij}(r(t))=(4,4,1,8,5,5)}
\tag{H101-FLAG}
\]
under H85's *independently postulated* fixed-budget normalized endpoint selection, and the selected positive K4 spatial response metric \(g[w(r(t))]\) is exactly constant.

This is a whole continuous interval of **honest positive original-source inputs**, not just a perturbative rank defect. The H75 channel's original signed P3 residue is unchanged because the source channel itself has not been modified; it would be incorrect to claim the P3 residual evaluated on every varying input is numerically identical without a separate definition.

## H101.2 — The phase is PHYSICALLY available by another positive measurement of the SAME channel (EXACT)

Let \(Y_{01}=-i|0\rangle\langle1|+i|1\rangle\langle0|\), and \(Q=(I_3+Y_{01})/2\). This is a genuine positive POVM effect: the spectrum of \(Y_{01}\) is \(\{-1,0,+1\}\), so \(0\le Q\le I_3\).

On the six-level H75 reset output, use the explicit positive effect
\[
\boxed{
E=|0\rangle\langle0|_E\otimes U Q U^\dagger,\qquad0\le E\le I_6.
}
\tag{H101-EFFECT}
\]
Here \(U\) is the same **fixed complex source unitary** inside the original reset. Its appearance in a detector calibration for the explicit output POVM is an **additional operational readout assumption**; it is NOT an independently available coherent Hamiltonian pulse.

Exact original-CPTP output gives
\[
\begin{aligned}
p_E(t)
&=\operatorname{Tr}\!\left[E\Phi_\mu(|0_E\rangle\langle0_E|\otimes\rho_t)\right]\\
&=\operatorname{Tr}\bigl[Q M_0\rho_tM_0\bigr]
=\boxed{\frac{21}{50}-\frac{3t}{20}}.
\end{aligned}
\tag{H101-PHASE}
\]
In particular
\[
\boxed{p_E(+1)=27/100,\quad p_E(-1)=57/100,\quad
p_E(+1)-p_E(-1)=-3/10.}
\tag{H101-GAP}
\]
Thus two genuine source-positive states with **identical all-four H85 flag probabilities and selected K4 metric** are distinguishable by a genuine positive effect on the **same unchanged microscopic CPTP output**. The full source output was never claimed to be phase-blind; only the *coarsened four flag probabilities* are.

The initial site-phase observable \(Y_{01}\) has \(\operatorname{Tr}(Y_{01}\rho_t)=-t/2\); it changes sign under the computational basis complex conjugation \(\rho_t\leftrightarrow\rho_{-t}\) (a simple time-reversal-like phase reflection). This is an **operational coherent-current candidate**, NOT a derived ADM canonical momentum, whose construction would require an independent Poisson/symplectic and Hamiltonian intertwiner.

## H101.3 — An exact observational sufficiency NO-GO (SCOPED)

Denote by \(\mathcal R\) the four H75 flag-readout map used in the H85 K4 selector, including the three unchanged separately prepared states and the fourth \(\rho_t\). Then
\[
\mathcal R(\rho_t)=r_\star
\quad\forall t,\qquad
\frac{d}{dt}\mathcal R(\rho_t)=0,
\]
but the physically accessible output probability obeys
\[
\boxed{\frac{d}{dt}p_E(t)=-3/20\ne0.}
\tag{H101-NECESSARY}
\]
Therefore **no single-valued function** \(f\) on the H85 flag-readout data can reproduce the physically meaningful phase-sensitive output observable on this family:
\[
\boxed{p_E\ne f\circ\mathcal R.}
\]
This is a direct counterexample to **observational completeness of this particular four-flag coarse-graining**, and to any proposed automatic reconstruction of the measured phase/current from \(r\) alone. It is **not** a universal no-go against adding site-sensitive readouts or sourced physical momentum fields.

The H99 normalized K4 edge image \(\mathcal R\to w(r)\to g(w)\) has smooth **rank3**. For any construction whose only physical input is \(r\), no differentiable map into any 12D canonical phase space can have derivative rank exceeding **3**. If one pulls a 2-form back to this **3D observable image**, its skew-symmetric rank is at most **2**, so a full nondegenerate 6-pair KKS/ADM symplectic form **cannot originate by a locally invertible transformation of this image**. This is a strict, typed chain-rule and skew-rank obstruction for this coarse-grained source, not a statement about the **entire** H75 quantum state space (which has phase-sensitive observables as explicitly shown).

Even supplying **every spatial jet** of the constant four-observation field does not repair this specific phase blindness: assign the independently prepared \(\rho_{t(x)}\) on an externally labelled spatial chart with arbitrary smooth \(t(x)\); all r(x), w(x), g(x) remain constant, while accessible phase POVM expectation varies as \(21/50-3t(x)/20\). This requires *external* independent preparations at each x, not sourced spatial dynamics, and proves only a necessary observational-completeness distinction.

## H101.4 — Proposed P11 typed AX-OA / AX-SP / AX-CAN conditions (OPEN, not established axioms)

A genuinely **noncircular** The Generative Map (F) program must separate six stages:

**AX-SRC (EXACT for the declared example, not universal):** Specify physical CPTP source, preparation, observable family and observable record. Here H75 is genuine and reproducibly measurable, but its physical hardware was independently posited, not derived by F or original P3 residues.

**AX-OA (OPEN generative selection, exact counterexample):** The measurement family intended to define physical fields must be declared **operationally complete for the target sector**. H101 shows the H85 four flag effects are not complete for a basic 1D source-coherent phase. A full site/phase POVM is mathematically possible but still is **observation, not sourced canonical dynamics**.

**AX-SP (OPEN):** An actual spatial localization/gluing/field-continuation law that selects six ADM configuration components (or an independently justified gauge reduction) and their **second spatial jets** from physical intercell couplings. H99 proves four-readout normalized additive metric rank3 and curvature 2-jet nonselection. An externally assigned x-index on separate preparations is not a sourced spatial field.

**AX-CAN (OPEN):** Construct from actual physical source dynamics a symplectic 2-form, conjugate momenta with a physically established Poisson algebra, and their Hamiltonian transport. An extra phase-sensitive measurable probability cannot simply be renamed \(\pi^{ij}\); one must prove the nondegeneracy, independence and transformation law of 6 canonical pairs, including relevant constraints.

**AX-DYN (OPEN):** Derive a source-compatible DeWitt-type kinetic Hessian, curvature action and spatial momentum constraint that close the nonuniform off-shell HDA, without circularly importing standard ADM as a source law. H98/H100 show what *externally supplied* standard ADM fields select, not how P3/F produces them.

**AX-NORM / AX-GEN (OPEN):** Specify noncircular physical selection of Newton/cosmological couplings, units and matter, and demonstrate F-generative completeness plus an empirically discriminating comparison against ordinary quantum mechanics. H100 showed that \(\alpha\beta=1,\lambda=1/2\) in an imported comparator leaves \((\alpha,\beta,\Lambda)=(a,a^{-1},\ell)\) free.

**Immediate P9 handoff:** Stop equating finite positive flag observations with six configuration + six momentum source dynamics. A future successful AX-CAN theorem must either (a) derive a physical momentum/phase readout family with an actual nondegenerate 2-form and controlled symplectic flow, or (b) reduce the target to a physically justified smaller gauge sector and *prove* its field/Hamiltonian covariance. A mathematical cotangent lift of freely postulated edge momenta is not sufficient.

**Verdict:** positive-state flag blindness and positive-POVM phase distinction **EXACT**; no \(f(r)\) determining this phase response and chain-rule source rank≤3 **EXACT scoped**; K4 physical spatial solder and readout detector calibration **CONDITIONAL**; generated gravitational momentum, 3D curvature field, full HDA, Einstein equations and F completeness **OPEN**.

**Reproducibility:** pure standard-library exact Fraction/Gaussian-rational original H75 CPTP source and positive 6D POVM computations, continuous positive 2×2 principal minor bound, source-preserved H85 four measurements/K4 geometry, sign-sensitive \(p_E(\pm1)\), H99 rank3 obstruction and inherited H98–H100 regression. Independent AI-generated arithmetic and GitHub CI do NOT constitute human specialist peer review, experiment or Lean formal proof.
