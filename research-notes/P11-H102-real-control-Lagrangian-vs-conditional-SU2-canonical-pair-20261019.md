# H102 — P11 AX-CAN: Source-Accessible Real Hamiltonian Orbits Are Lagrangian; a Nondegenerate Phase Canonical Pair Requires an Independently Sourced Quadrature

**2026-10-19 | P11 The Generative Map (F), P9 G3 physical canonical provenance | Constructive Route A**

**Base:** H101 Draft PR #120 (100/100 GitHub CI PASS). Original H75 four-Kraus 6-level CPTP source and nonzero original signed P3 \(R_3\), H85 K4 readout selection, and main/frozen P1–P8 are unmodified. **Independent Hamiltonian and detector permissions are typed; no ADM momentum, source gravity, or independent H42 complex gate is presumed.**

## 1. Why H101's \(\rho_t\) is NOT an actual Hamiltonian trajectory (EXACT corrective audit)

H101 used the physically positive one-parameter qutrit input family
\[
\rho_t=\begin{pmatrix}3/4&it/4&0\\-it/4&1/4&0\\0&0&0\end{pmatrix},
\qquad |t|\le1,
\]
to show four coarse H75 flag measurements and H85 K4 metric are insensitive to a phase readout. Its **purity**, however, is
\[
\boxed{\operatorname{Tr}\rho_t^2=\frac58+\frac{t^2}{8}.}
\tag{H102-PURITY}
\]
Consequently the entire parameterized family is **not one fixed-spectrum coadjoint orbit** and cannot be produced from \(\rho_0\) by a single closed Hamiltonian unitary flow. In particular, H101 operational distinguishability is *not* evidence of a realizable Hamiltonian phase-space direction. Its tangent at \(t=0\) does point along an abstract SU(3) KKS direction, but nonlinear completion of the LINEAR \(\rho_t\) path would require changing its diagonal populations to preserve the spectrum.

## 2. H102.1 — EXACT native three-level full SU(3) KKS orbit vs genuine H75 real controls

At the actual positive H101 source input
\[
\rho_0=\operatorname{diag}(3/4,1/4,0),
\]
the three eigenvalues are distinct; its abstract full \(U(3)\) coadjoint orbit has
\[
\boxed{\dim_{\mathbb R}\mathcal O_{U(3)}=3^2-3=6,\quad
\operatorname{rank}\omega_{\rm KKS}=6.}
\tag{H102-U3}
\]
The exact checker computes six independent Hermitian tangent matrices \(-i[H,\rho_0]\), \(H=X_{01},Y_{01},X_{02},Y_{02},X_{12},Y_{12}\), and the full six-by-six KKS Poisson matrix, both of rank 6.

The H75 **genuinely independently specified continuously tunable REAL site skew Hamiltonians** \(A=E_{01}-E_{10}\), \(B=E_{21}-E_{12}\) have Lie closure \(\mathfrak{so}(3)=\operatorname{span}\{A,B,[A,B]\}\). This is a generous mathematical Lie closure, not certification of arbitrary exact pulse engineering. Starting from real diagonal \(\rho_0\), every reachable density \(O\rho_0O^\top\), \(O\in SO(3)\), remains REAL symmetric. Since \(\rho_0\) has distinct eigenvalues, the stabilizer in \(SO(3)\) is discrete and its real-control orbit has exact dimension 3.

More strongly, the KKS two-form on this **actual real-control orbit** is **identically zero**:
\[
\boxed{\dim\mathcal O_{\rm real}=3,\qquad
\omega_{\rm KKS}|_{\mathcal O_{\rm real}}=0.}
\tag{H102-LAG}
\]
Indeed for real \(K,L\in\mathfrak{so}(3)\), the Hamiltonians \(H_K=iK\), \(H_L=iL\) are Hermitian, and
\(-i\operatorname{Tr}[\rho_{\rm real}[H_K,H_L]]=i\operatorname{Tr}[\rho_{\rm real}[K,L]]=0\)
because \(\rho_{\rm real}\) is real symmetric and \([K,L]\) real skew. The orbit is in fact **Lagrangian** in the abstract six-dimensional complex KKS coadjoint orbit: half dimension, zero restricted two-form. (This is a statement about the source-real controlled **site** orbit, independent from H97's distinct 5D source-output SO(4) orbit.)

In particular the original real A/B controls **cannot create nonzero computational-basis imaginary coherence** \(Y_{01}\) from this real diagonal seed, regardless of how they are concatenated in the real orthogonal group. The H75 fixed complex U appears *downstream inside an irreversible reset* and is **not** an independently sourced coherent pre-reset Hamiltonian; it cannot be counted to evade this real-control restriction.

## 3. H102.2 — An abstract and operational 2D KKS pair if an independently certified EXTRA X quadrature is available (CONDITIONAL EXACT)

Define the Pauli-type Hermitian source-site operators
\[
X=E_{01}+E_{10},\quad
Y=-iE_{01}+iE_{10}=-iA,\quad
Z=E_{00}-E_{11}.
\]
The existing real A continuous control provides the Hamiltonian \(H_Y=Y\) **up to sign**. The independent Hermitian \(H_X=X\) would require the imaginary skew generator \(-iX\), **not contained in the source-declared real \(\mathfrak{so}(3)\)**. H102 does **not** posit that F/P3/H75 generates \(H_X\); it is an explicit proposed **AX-CAN extra operational premise**.

With BOTH \(H_X,H_Y\) granted, their Lie closure on the 01 two-level sector is \(\mathfrak{su}(2)\), and the isospectral 2-dimensional coadjoint orbit through \(\rho_0\) is \(\mathrm{SU}(2)/\mathrm{U}(1)\cong S^2\), embedded as a spectator-zero qutrit state. The physical tangent directions
\[
T_X=-i[X,\rho_0],\qquad T_Y=-i[Y,\rho_0]
\]
are independent. Their KKS moment-map bracket is explicitly
\[
\boxed{
\{h_X,h_Y\}_{\rm KKS}(\rho_0)
=-i\operatorname{Tr}\bigl(\rho_0[X,Y]\bigr)
=2\operatorname{Tr}(\rho_0Z)
=1\ne0.
}
\tag{H102-POISSON}
\]
Thus this **conditional** 2D Hamiltonian orbit has a nondegenerate KKS two-form. It is **ONE canonical pair**, not ADM's physical six pairs, and the full H75 source does not justify adding the independent \(H_X\) knob.

The **original H75 four-Kraus output channel remains unchanged**. Independent detector calibration using the same fixed source U gives two positive effects
\(E_Q=|0_E\rangle\langle0_E|\otimes UQ U^\dagger\), for \(Q_X=(I_3+X)/2\) and \(Q_Y=(I_3+Y)/2\). Each Q has spectrum \(0,1/2,1\). On infinitesimal isospectral control directions \((T_X,T_Y)\), their two Born-probability response Jacobian is
\[
\boxed{
J_{\rm readout}=
\begin{pmatrix}
0&3/10\\ -3/10&0
\end{pmatrix},
\quad \det J_{\rm readout}=9/100\ne0.
}
\tag{H102-READOUT}
\]
Hence IF the missing X quadrature is genuinely supplied, its SU2 orbit has an operationally readable local symplectic pair using valid positive original-H75 output effects. The readout positivity does **not** imply that the X Hamiltonian can be implemented, and readout rank is not gravitational Hamiltonian provenance.

## 4. H102.3 — Isospectral positive phase witness removes H101's variable-purity loophole (CONDITIONAL EXACT)

The following **rational unitary** is an explicit mathematical gate built from the **EXTRA, presently unsourced** Hamiltonian X:
\[
V_\pm=
\begin{pmatrix}
15/17 & \mp 8i/17&0\\
\mp 8i/17&15/17&0\\0&0&1
\end{pmatrix},
\quad
\tilde\rho_\pm=V_\pm\rho_0V_\pm^\dagger.
\tag{H102-UNIT}
\]
They are genuine positive isospectral source-site qutrit states:
\[
\tilde\rho_\pm=
\begin{pmatrix}
739/1156 & \pm 60i/289 &0\\
\mp 60i/289&417/1156&0\\
0&0&0
\end{pmatrix},
\quad
\operatorname{spec}(\tilde\rho_\pm)=\{3/4,1/4,0\}.
\]
Both give the same true original H75 flag-1 outcome
\[
\boxed{r_{\rm flag1}(\tilde\rho_\pm)=1668/7225.}
\]
Thus holding the *other three* H85 preparations unchanged, both define the **same** four-source-flag profile and corresponding same normalized additive K4 metric (not necessarily the initial H85 \(w_\star\)), despite being distinct positions on **one fixed-spectrum SU2 KKS orbit**.

For the original source H75 reset followed by the independently calibrated **positive** \(Y\)-effect in the flag-0 output,
\[
\boxed{
p_{E_Y}(\tilde\rho_+)-p_{E_Y}(\tilde\rho_-)
=-72/289\ne0.
}
\tag{H102-POS}
\]
The checker uses the actual six-level H75 Kraus micro operator and the same U—not an invented unphysical measurement channel—and verifies both probabilities are in [0,1]. This strengthens H101's identification witness to a **pair of isospectral quantum states** but its PREPARATION still needs the independently postulated X control (or another independently demonstrated equivalent preparation). It is not an original-H75-source-generated nonreal orbit.

## 5. P11 / P9 handoff

**AX-OA:** Operational informational completeness for a proposed phase-space sector depends on explicitly certified detector settings. The four H85 flag statistics and K4 response cannot infer all accessible source phase information. The original H75 output admits positive phase-sensitive POVMs under independently calibrated readout; no special CR-exclusive measurement effect is thereby predicted.

**AX-CAN:** A genuine symplectic sector needs **(i)** a fixed-spectrum source-state manifold and phase-space identification, **(ii)** two independent accessible Hamiltonian vector fields that are not merely an abstract span, **(iii)** a nondegenerate KKS or physically derived two-form, **(iv)** an actual physical control/transport or Hamiltonian field, and **(v)** operationally calibrated positive readouts. H102 has a **conditional one-pair constructive success** if an added X control is permitted, and a **scoped NO-GO** using only inherited H75 real controls from real \(\rho_0\).

**AX-SP/AX-DYN/AX-NORM/AX-GEN:** Source-generated spatial localization/intercell curvature 2-jets (H99), six ADM canonical pairs (H95–H99), DeWitt indefinite kinetic/action and full nonuniform off-shell HDA (H98–H100), physical Newton/cosmological normalization and truly noncircular F completeness remain **OPEN**. A single conditional SU2 qutrit pair neither furnishes six physical ADM pairs nor proves any spatial coupling or Einstein equation.

**Verdict:** H101 family non-isospectral **EXACT**; 3D real-SO3 orbit embedded Lagrangian in full 6D qutrit KKS orbit **EXACT scoped**; conditional missing \(X\) control yields 2D nondegenerate symplectic orbit and calibrated two-positive-POVM local rank2 **CONDITIONAL EXACT**; positive isospectral two-state flag-blind but Y-sensitive original H75 output **CONDITIONAL EXACT**; any P3/F-derived physical complex control, KKS→ADM canonical transport or Einstein gravity **OPEN**.

**Stopping criterion:** H103 must NOT declare this abstract one-pair SU2 completion an Einstein dynamics source. It should audit whether original P3/H75 causal-control algebra *physically provides a coherent imaginary-phase quadrature* (without independently importing it), or explicitly close this qutrit one-pair branch and record AX-CAN as unsolved for P11. Draft/unmerged, no new Lean Einstein theorem, lab confirmation or human expert peer review.
