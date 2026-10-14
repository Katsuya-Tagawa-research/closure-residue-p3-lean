# H43 — Reflection-equivariant physical tangents, completely positive collective filtering, and the dynamical-intertwining obstruction

**2026-10-15 | P3–P11 Mathematical Bridge.** H43 is stacked on the **H42 Draft PR #61** using precisely the same genuine rational-Gaussian H42 CPTP microscopic channel \(\Phi=\operatorname{Ad}_U\) and its verified full original-P3 \(\mathcal R_3=D_3^0\). This audit clarifies exactly what *extra independent symmetry and observer data* can recover a collective candidate, and what remains *unproven* about frozen P6 \(\mathcal J_N\) and physical access. No frozen manuscript/main edits, Lean formalization or human review.

## 1. Two different meanings of symmetry, and a minimal conditional theorem

Let \(P=E_{02}+E_{11}+E_{20}\) implement the left/right reflection, and define real anti-Hermitian P6 exchange directions
\[
A=E_{01}-E_{10},\qquad B=E_{21}-E_{12},\qquad
\operatorname{Ad}_P(A)=B,\quad\operatorname{Ad}_P(B)=A.
\]
For \(K(a,b)=aA+bB\), the **pointwise** physical-tangent invariance assumption
\[
\operatorname{Ad}_P K(a,b)=K(a,b)
\]
holds **if and only if \(a=b\)**. Thus a 1-dimensional control parameter with **trivial** reflection action and a reflection-equivariant linear physical tangent map must have locked collective left/right exchange amplitudes. The conclusion is a *selection theorem under a new physical equivariance premise*, not a derivation of that premise from P3.

Crucially, this differs from **covariance of an entire 2-control family** with swapped control parameters. For \(\tau(x,y)=(y,x)\), the most general *real-linear* swap-equivariant map to the A/B two-edge exchange span is
\[
\boxed{\kappa_{c,d}(x,y)=(cx+dy)A+(dx+cy)B,}
\quad \operatorname{Ad}_P\kappa(x,y)=\kappa(\tau(x,y)).
\]
The domain splits into even/odd representations:
\[
\boxed{\kappa(x,x)=x(c+d)(A+B),\quad
\kappa(x,-x)=x(c-d)(A-B).}
\]
**Only an additional odd-mode exclusion \(c=d\)** makes every allowed tangent collective; reflection covariance of the full family does **not** require \(c=d\). In particular the 2-parameter standard CPTP family \(\Psi_{x,y}=\operatorname{Ad}_{e^{\kappa_{c,d}(x,y)}}\circ\Phi\) is fully covariant when \([U,P]=0\), even if it has distinct left/right controls. The source CPTP channel is not changed.

The frozen P6 center-site \(d_{\rm c}=E_{11}\) quadratic population Hessian obeys
\[
\ell_-\big(D^2\Sigma(0)[X,Y]\big)
=2(a_Xa_Y-b_Xb_Y),\quad
\ell_-(h)=h_{00}-h_{22}.
\]
For the explicit **swap-equivariant** map \(c=3/5,d=1/5\), take \(X=(1,1)\) (even) and \(Y=(1,-1)\) (odd). They yield
\[
\boxed{\ell_-\big(D^2\Sigma(0)[X,Y]\big)
=4(c+d)(c-d)=32/25\ne0,}
\]
even though the full physical control **family** transforms covariantly under reflection. The even-even and odd-odd quadratic readouts separately vanish by parity. This is a rigorous counterexample to falsely deducing P6's all-\(X,Y\) collective null from equivariance of a 2-control family alone.

## 2. Symmetry twirling is a genuine CPTP channel and DOES intertwine with the H42 microscopic update

The discrete reflection group averaging
\[
\boxed{\mathcal T(X)=\tfrac12(X+PXP)}
\]
is unital CPTP and idempotent: it is a random-unitary average of \(I\) and \(P\). The fixed H42 microscopic rational \(U\) commutes with \(P\), so
\[
\boxed{\mathcal T\Phi=\Phi\mathcal T.}
\]
Thus it is **incorrect** to say every symmetry projection is unphysical/non-CPTP: a genuine physical CP symmetry twirl exists and commutes with the given microscopic channel.

However, the even-sector twirl alone does not impose strict radius-one locality. The center seed \(E_{11}\) is fixed by \(\mathcal T\), and its first genuine P3 hidden iterate \(h_1^{(1)}=Q\Phi(E_{11})\) is reflection-even **with a nonzero 02 chord coherence \(4/9\)**. In addition, twirling the *final physical state* erases the antisymmetric population signal being tested:
\[
\ell_-(\mathcal T(\rho))=0\quad\text{for every }\rho.
\]
The CP symmetry twirl may therefore serve as an *additional, separately justified MICROSCOPIC static-sector extraction*, but it is not a free replacement for the original P6 full-site population observer or an automatic way to deduce its physically permitted control tangents.

## 3. A rigorous CP support-filter tradeoff, rather than H33's nonpositive hard mask

For a 3-site path, take the site-basis Schur multiplier
\[
\mathcal S_s(X)=M_s\odot X,\qquad
M_s=\begin{pmatrix}1&s&0\\s&1&s\\0&s&1\end{pmatrix},\qquad s\in\mathbb R.
\]
It fixes **all populations**, multiplies BOTH nearest-neighbor coherences by \(s\), and kills the distance-two chord exactly. Since a Schur multiplier is completely positive if and only if \(M_s\succeq0\), and the eigenvalues are \(1,1\pm\sqrt2\,s\), the exact condition is
\[
\boxed{\mathcal S_s\text{ is CPTP}\iff |s|\le 1/\sqrt2.}
\]
At \(s=1\) the mask is *not CP*, reproducing H33's radius-one hard projection obstruction. But **attenuated** CP localization **is** possible, e.g. \(s=3/5\), for which the leading minors are \(1,16/25,7/25>0\). An attempted \(s=4/5\) has determinant \(-7/25<0\).

Indeed, if a unital CP map fixes every minimal diagonal projector \(E_{jj}\) and fixes BOTH offdiagonal matrix units on the two path edges exactly while erasing 02, no such map can exist. Each fixed rank-one projection belongs to its multiplicative domain, forcing the channel to act as a Schur multiplier in that basis, and its would-be correlation mask \(M_1\) is not positive. The exact coherence-preserving *projection* is forbidden; a CP channel must allow sufficient attenuation or modify other premises. Note that \(s<1\) is NOT an idempotent strict nearest-neighbor projection: \(\mathcal S_s^2\ne\mathcal S_s\).

## 4. A conditional CPTP extraction of a locked **microscopic candidate** tangent

Compose the two physical maps:
\[
\mathcal E_s=\mathcal S_s\circ\mathcal T
\quad\text{with }s=3/5.
\]
It is unital CPTP, reflection-equivariant, and its action on every **hidden offdiagonal** P3 operator lies within the *path-local parity-even complex-linear operator space*
\[
\boxed{\mathcal E_s(\mathcal H_k)\subseteq
\mathcal J_{\rm col}=
\operatorname{span}_{\mathbb C}
\{T,T^\dagger\},\quad T=E_{01}+E_{21}.}
\]
For the center-seed hidden iterate \(h=h_1^{(1)}\) in H42,
\[
(\mathcal E_s h)_{01}=(\mathcal E_s h)_{21}=\frac{2is}{9},\qquad
(\mathcal E_s h)_{02}=0.
\]
Therefore its **separately phase-polarized** first-residue image yields a locked P6-style tangent:
\[
\boxed{\Xi(i\mathcal E_s h)
=-\frac{4s}{9}(A+B)
=-\frac4{15}(A+B)\ne0.}
\]
This is a **positive conditional construction** rather than the nonpositive unattenuated mask of H42. Yet it requires three explicitly new decisions: (i) a physically/microscopically specified parity-twirl observer selection, (ii) an attenuation parameter and CP Schur filter that discards chord coherence, (iii) a coherent \(i\)-polarization in Xi. NONE of these follows solely from original P3 full-diagonal closure–residue filtration or the given H42 update, and none proves the actual frozen P6 microscopic \(\mathcal J_N\) is this extracted candidate. Mapping static data to **independently available physical tangent controls** remains a further premise.

## 5. The obstruction reappears at TWO-STEP DYNAMICAL INTERTWINING

This is where treating a CP map as a mere mathematical extraction would overclaim. Although \(\mathcal T\) intertwines with \(\Phi\), the **localized** composite \(\mathcal E_s=\mathcal S_s\mathcal T\) does **not**:
\[
\boxed{\mathcal E_s\Phi\ne\Phi\mathcal E_s.}
\]
An explicit witness is the central diagonal seed \(d=E_{11}\), fixed by \(\mathcal E_s\). In the H42 model,
\[
\bigl(\mathcal E_s\Phi(d)\bigr)_{02}=0,\qquad
\bigl(\Phi\mathcal E_s(d)\bigr)_{02}
=(\Phi(d))_{02}=4/9.
\]
Hence the CP conditional collective extractor is **not** the demanded microscopic-to-physical one/two-step update intertwiner. Calling it a valid CP map does not fix the provenance gap: additional dynamics on the extracted subsystem and a compatible operational control map must be independently constructed.

Separately, the full two-knob covariant control family allows odd tangible directions and a nonzero mixed parity population Hessian. One can obtain the P6 exact collective null only by restricting actual declared controls to the **pointwise-even/odd-excluded tangent subspace**, or by a separately proven equivalent image restriction, *and* by preserving appropriate readout/intertwining conditions. These are candidate axioms and can be individually falsified.

## 6. H43 interpretation, status and possible next gate

**PASS exact algebra:** symmetry covariance vs pointwise invariance equivalence; 2D representation decomposition and nonzero covariant mixed Hessian; CPTP twirl commuting with H42 Φ; exact Schur-filter CP threshold and no-go for an unattenuated population-preserving support cutoff; CPTP attenuated collective microscopic *candidate* with its explicit nonzero locked Xi; non-intertwining witness for the composite.

**CONDITIONAL PASS:** a collective real exchange tangent can be extracted by explicit CP observer selection/attenuation plus independently declared phase-polarization; the P6 all-control left/right null follows if actual physical tangent maps are pointwise P-even or all odd control modes are forbidden.

**FAIL automatic implications:** symmetry of uncontrolled P3 update ⇒ every physically permitted control tangent is even; full-family swap covariance ⇒ all tangents locked; path Schur projection with unchanged edge coherences is CPTP; CPTP collective extraction ⇒ two-step Φ-intertwining and frozen P6 provenance.

**OPEN:** a microphysically selected CP observer map that also has a genuinely compatible effective dynamics and physical control map; independent derivation of odd-mode exclusion and phase polarization from P3/P4 rather than physical control assumptions; a same-calibration framework-exclusive signal and full P9 gravitational bridges.

**Proposed H44:** attempt to construct an exact CP-compatible *effective* \(\Phi_{\rm eff}\) on the selected collective operator system satisfying \(\mathcal E_s\Phi=\Phi_{\rm eff}\mathcal E_s\), with actual invariant kernel; prove or refute existence (kernel-preservation test). Distinguish mere compression \(E\Phi E\) from a genuine quotient dynamical intertwiner. If an invariant quotient is impossible, identify the additional memory/state needed to close the effective observer dynamics, with H3/P3 closure–residue interpretation.

## Reproducibility

`P3/P9H43EquivariantCPTPCollectiveExtractionExactCheck.py` uses H42's exact original-P3 microscopic U and existing validated Gaussian-rational rank functions; all stated sample identities checked with exact Fraction, positive-semidefinite principal minor certificates and direct matrix products. Analytic proofs of general map properties rely on standard group twirl CP/Choi Schur multiplier criterion and multiplicative domain of unital CP maps; no floating tolerances. New dedicated Actions CI; no claim of new Lean kernel formalization or independent expert peer review.