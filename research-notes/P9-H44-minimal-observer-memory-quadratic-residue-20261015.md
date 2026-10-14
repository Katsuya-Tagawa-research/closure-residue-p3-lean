# H44 — Minimal Markovian observer memory and nonlinear P3 residue obstruction

**2026-10-15 | P3–P11 Mathematical Bridge | exact finite audit candidate.** Stacked on H43 Draft PR #62. Uses *exactly the fixed H42 rational 3-site CPTP channel* \(\Phi=\mathrm{Ad}_U\), and H43's fixed completely positive collective extractor \(\mathcal E=\mathcal S_{3/5}\mathcal T\). The microscopic dynamics is standard quantum mechanics; no CR-only observable, genuine independently inherited P6 sector/provenance, gravitational connection/Einstein dynamics, new Lean formalization or human expert review is claimed.

## 1. Main result: a single real memory coordinate repairs the linear future observation problem

Let the left/right reflection \(P=E_{02}+E_{11}+E_{20}\), and define
\[
\mathcal T(X)=\frac12(X+PXP),\qquad
\mathcal E(X)=\mathcal S_{3/5}(\mathcal T(X)),
\]
where \(\mathcal S_s(X)=M_s\odot X\) with
\[
M_s=\begin{pmatrix}1&s&0\\s&1&s\\0&s&1\end{pmatrix},\qquad s=3/5.
\]
H43 proved both maps unital CPTP; \([\Phi,\mathcal T]=0\), but \(\mathcal E\Phi\ne\Phi\mathcal E\). The source Hilbert-space parity eigenspaces have dimensions two and one. The reflection-even fixed-point algebra is
\[
\boxed{\mathcal A_+=\{X:PXP=X\}\cong M_2(\mathbb C)\oplus\mathbb C,\quad
\dim_\mathbb C\mathcal A_+=5.}
\]
The reflection-odd operator sector \(\mathcal A_-=\{X:PXP=-X\}\) has complex dimension four, and is invariant under \(\Phi\). In particular \(\mathcal T\) is a **CPTP conditional expectation** onto an invariant \(C^*\)-subalgebra, and \(\Phi_+=\Phi|_{\mathcal A_+}\) is a genuine **CPTP *-automorphism of that algebra**. This supplies a perfectly legitimate *quantum* autonomous observer carrier once the missing chord is **retained**, not forcibly deleted.

By contrast H43's path-local collective channel \(\mathcal E\) has range
\[
\mathcal V_{\rm path,+}=
\mathrm{span}_{\mathbb C}\{D_e,E_{11},T,T^\dagger\},
\quad D_e=E_{00}+E_{22},\quad T=E_{01}+E_{21},
\]
of dimension four. One complex extra coordinate is needed for its full linear dynamical closure; the missing parity-even direction can be chosen as
\[
C=E_{02}+E_{20}.
\]
For Hermitian density states \(\rho\), the one missing **real** scalar is
\[
\boxed{m(\rho)=\tfrac12(\rho_{02}+\rho_{20})=\operatorname{Re}\rho_{02}.}
\]
Write \(y(\rho)=(\mathcal E\rho_{00},\mathcal E\rho_{11},
\mathcal E\rho_{01},\mathcal E\rho_{10})\) and \(Y(\rho)=(y(\rho),m(\rho))\). The complete twirled density is reconstructed by the **linear algebraic** lift
\[
\boxed{
L(p,q,c,d,m)=pD_e+qE_{11}+(c/s)T+(d/s)T^\dagger+mC.}
\]
It satisfies \(L(Y(\rho))=\mathcal T(\rho)\) for all operators. **Caution**: \(L\) is not asserted to be a CPTP assignment on arbitrary independent classical-memory and truncated-state inputs; the true physical domain is the image of valid density matrices under \(Y\). The legitimate CPTP representation is the corresponding twirled quantum state \(\mathcal T(\rho)\) inside \(\mathcal A_+\).

## 2. Exact five-component autonomous recurrence

As \(\mathcal T\Phi=\Phi\mathcal T\), the augmented coordinates obey
\[
Y(\Phi\rho)=F(Y(\rho)),\qquad
F=Y\circ\Phi\circ L,
\]
and this identity holds for **every** step, not only one and two. In the ordered basis \(Y=(p,q,c,d,m)\), the fixed H42 \(U\) and H43 \(s=3/5\) yield the exact Gaussian-rational 5×5 matrix
\[
\boxed{
M_F=
\begin{pmatrix}
5/9&4/9&10/27&10/27&-4/9\\
8/9&1/9&-20/27&-20/27&8/9\\
-2i/15&2i/15&i/9&-8i/9&-2i/15\\
2i/15&-2i/15&8i/9&-i/9&2i/15\\
-4/9&4/9&10/27&10/27&5/9
\end{pmatrix}.
}
\]
The formula is a complex-linear change of coordinates for \(\Phi_+\), not an assertion that an arbitrary five-component vector is a quantum density matrix. For physical Hermitian trace-one inputs \(q,p,m\) are real, \(d=\overline c\), \(2p+q=1\), and \(L(Y)\succeq0\). Thus the **affine physical observer-state dimension** rises from **three** real parameters in \(\mathcal E\rho\) to **four** in \(\mathcal T\rho\): exactly one extra real memory parameter.

### Why this is MINIMAL, not merely sufficient

On the full nine-dimensional complex operator algebra, \(\mathcal E\) has rank four, while \(\mathcal A_-\) (dimension four) is annihilated by \(\mathcal E\Phi^n\) for **all n**, since \(\Phi\) commutes with reflection. The missing fifth parity-even basis direction \(C\) satisfies
\[
\mathcal E(C)=0,\qquad
(\mathcal E\Phi(C))_{11}=8/9\ne0.
\]
Consequently the stacked one-step observability map
\[
X\longmapsto \bigl(\mathcal E X,\mathcal E\Phi X\bigr)
\]
has exact **complex rank five**. Since every future observable depends only on \(\mathcal T X\in\mathcal A_+\), its rank can never exceed five. The **stable unobservable kernel**
\[
\boxed{\mathcal N_\infty=\bigcap_{n\ge0}\ker(\mathcal E\Phi^n)=\mathcal A_-}
\]
therefore has complex dimension four, and the minimal **linear prediction carrier** \(\mathcal A/\mathcal N_\infty\) has dimension five. Because rank(\(\mathcal E\))=4, exactly **one** additional complex-linear coordinate is both sufficient and necessary for all future \(\mathcal E\)-outputs. On valid Hermitian trace-one states the corresponding missing freedom is exactly the one **real** chord \(m\).

Explicit PSD/trace-one necessity witness:
\[
\rho_\pm=\frac{I_3}{3}\pm\frac16(E_{02}+E_{20}),\qquad
\operatorname{spec}(\rho_\pm)=\{1/6,1/3,1/2\}.
\]
Then \(\mathcal E(\rho_+)=\mathcal E(\rho_-)=I_3/3\), but
\[
\boxed{
[\mathcal E\Phi(\rho_+)]_{11}
-[\mathcal E\Phi(\rho_-)]_{11}=\frac8{27}\ne0.
}
\]
One cannot predict the next output from the current compressed output alone.

## 3. Exactly TWO consecutive compressed observations suffice to infer the missing memory

The second row of \(M_F\) is
\[
q_{n+1}=\frac89p_n+\frac19q_n-\frac4{9s}(c_n+d_n)+\frac89m_n.
\]
Therefore, for consecutive (non-invasive, separately prepared) output snapshots \(y_n,y_{n+1}\) from the same microscopic update,
\[
\boxed{
m_n=\frac98\left[q_{n+1}-\frac89p_n-\frac19q_n
+\frac4{9s}(c_n+d_n)\right].
}
\]
The checker confirms exact reconstruction for multiple density preparations across up to ten updates, as well as exact prediction of \(y_{n+2}\) from \(y_n,y_{n+1}\) via this recovered memory and \(M_F\). This is an exact *finite two-snapshot history closure* of the **linear** observer outputs.

**Physical protocol qualifier:** these are observations of \(\mathcal E\Phi^n(\rho)\) on separately prepared state copies, **not** a single trajectory on which the CPTP extraction \(\mathcal E\) is inserted between microscopic updates. Repeated invasive extraction produces \((\mathcal E\Phi)^n\), which is a different channel because \([\mathcal E,\Phi]\ne0\).

## 4. Nonlinear P3 quadratic residue is NOT determined by this minimal linear carrier

The original P3 residue uses *all* diagonal seeds and the noncommutative **quadratic** return
\[
R(d)=\Delta_D\bigl([Q\Phi(d),\bigl(Q\Phi^2(d)\bigr)^\dagger]\bigr).
\]
H42 proved \(\mathcal R_2=0\), \(\mathcal R_3=D_3^0\), using actual full-D3 inputs. The H44 linear carrier sees the reflection-even part of any density, but the P3 quadratic operation can multiply two reflection-odd hidden directions and return a reflection-even **diagonal residue**.

Indeed choose physical *diagonal* seeds
\[
d_0=E_{00},\qquad d_{\rm av}=(E_{00}+E_{22})/2.
\]
Their **entire** \(\mathcal E\)-observable histories agree:
\[
\boxed{
\mathcal E\Phi^n(d_0)=\mathcal E\Phi^n(d_{\rm av})\quad
\text{for every }n\ge0
}
\]
because \(\mathcal T(d_0)=d_{\rm av}\), \(\mathcal T\Phi=\Phi\mathcal T\), and \(\mathcal E=\mathcal S_s\mathcal T\). Even the augmented \(Y\) histories (which retain the even chord) agree.

But their original P3 quadratic signed witnesses do **not**:
\[
R(d_0)=\frac{i}{81}\operatorname{diag}(-32,16,16),\quad
R(d_{\rm av})=\frac{i}{81}\operatorname{diag}(-2,4,-2).
\]
More strongly, even the *reflection-even part* of the full signed residue differs:
\[
\boxed{
\mathcal T(R(d_0))=
\frac{i}{81}\operatorname{diag}(-8,16,-8)
\ne
R(d_{\rm av}).
}
\]
Write the two hidden pairs from \(d_0\) as \(z=z_++z_-\), \(w=w_++w_-\), where \(\operatorname{Ad}_P(z_\pm)=\pm z_\pm\). Cross-parity terms have odd parity, so after twirling the quadratic commutator,
\[
\boxed{
\mathcal T R(d_0)
=\Delta_D([z_+,w_+^\dagger])
+\Delta_D([z_-,w_-^\dagger]).
}
\]
The **odd–odd return** is explicitly
\[
\boxed{
\Delta_D([z_-,w_-^\dagger])
=\frac{i}{81}\operatorname{diag}(-6,12,-6)\ne0.
}
\]
The even–even term equals \(R(d_{\rm av})=\frac{i}{81}\operatorname{diag}(-2,4,-2)\). Thus the loss of reflection-odd hidden information is invisible to **all future linear collective measurements** but visible to a nonlinear functional of the **original microscopic hidden trajectory**: P3's quadratic return.

This is an important logical separation:
- **PASS:** exactly one real chord memory restores autonomous prediction of **all \(\mathcal E\)-linear outputs** on physical density matrices; the CPTP parity-twirled algebra \(\mathcal A_+\) gives its quantum realization.
- **FAIL:** that linear memory alone lets one reconstruct the **original full-D3 quadratic P3 residue**. The odd-hidden quadratic term is not a function of \(Y(\rho)\) or the entire even-output history. More data (parity-odd hidden amplitudes / labeled observer seed identity, or an explicit restriction to reflection-even preparation sectors) are required.
- **CONDITIONAL:** for strictly parity-even seeds such as \(E_{11}\), there is no odd–odd term and the genuine original P3 signed depth-three witness is reproducible from the retained \(\mathcal A_+\) trajectory; it still cannot be inferred by treating \(\mathcal S_s\) as multiplicative or forgetting its known attenuation.

The scalar \(m=\Re\rho_{02}\) is sufficient for **linear Markovian closure**, not generically a sufficient statistic for original P3 *quadratic* residue. Retaining parity-odd history may expand the sufficient carrier toward the full matrix algebra; a globally minimal nonlinear-residue carrier is **not** derived here.

## 5. Relation to the P3/P6/GR program

The H44 distinction realizes a precise mathematical version of the program's closure/residue tension: a CP reduced observer can be made Markovian by retaining a *single* omitted chord scalar, while a higher-order quadratic hidden return remains sensitive to degrees of freedom that are permanently invisible to the reduced **linear** observer. **Both effects are predicted within ordinary standard finite quantum mechanics** and do not constitute a framework-discriminating signal.

This does not establish that H44's \(\mathcal A_+\) is the independently frozen P6 microscopic \(\mathcal J_N\), nor a physically implementable extraction/readout instrument under the original two real P6 exchange knobs, nor a micro-to-physical two-step intertwiner on the path-only \(\mathcal E\) output. The **legitimate** CPTP restricted dynamics lives on the larger reflection-even algebra \(\mathcal A_+\); the path-only collective output still lacks an autonomous CPTP update without the extra chord. No physical Lorentzian soldering, ADM/HDA constraints or Einstein equations follow.

**H45 gate:** Determine the minimal **quadratic-residue-sufficient** observer memory for all original P3 diagonal seed trajectories: what parity-odd hidden data must be retained, and can it be reduced to a finite algebraic bilinear invariant rather than the entire odd 4-real-dimensional sector? The solver must preserve the distinction between (i) predicting future \(\mathcal E\)-linear outputs, (ii) reconstructing a selected signed P3 residue witness, and (iii) identifying the full P3 residue subspace \(\mathcal R_3\).

## Reproducibility

`P3/P9H44MinimalObserverMemoryQuadraticResidueExactCheck.py` uses the H43 exact standard CPTP maps and previous Gaussian-Fraction rational engine. It verifies all complex operator-space ranks by exact Gaussian elimination, explicit 5×5 recurrence and future histories, two-output memory recovery, physical density witness, the whole parity-odd stable kernel, original full-D3 P3 residue differences, and the exact odd–odd quadratic return. Dedicated CI on Draft PR, frozen files/main untouched. No numerical approximation, new Lean formalization, independent peer review, experimental validation or GR claim.