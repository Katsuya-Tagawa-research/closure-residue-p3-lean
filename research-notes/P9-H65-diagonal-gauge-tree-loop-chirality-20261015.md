# H65 — Diagonal-Gauge Intertwining, Tree-Phase No-Go and a Closed-Loop Chirality Witness

**2026-10-15 | P3–P11 Mathematical Bridge / H65.** Stacked on H64 Draft #83. This note separates three properties that need not coincide: algebraically nonzero imaginary/phase control direction, a nontrivial **gauge-invariant** microscopic loop flux, and a **physically inherited** P3→frozen P6 phase reference/observer map. H65 proves exact finite ordinary-quantum comparator statements; it does not prove P3 creates a new phase resource, that the H32 model is physically the frozen P6 source, or that P9 GR-I succeeds.

## 1. H65.1 — exact gauge-covariant P3 source/observer intertwiner, but coordinate-only

Recall the independent H32 connected three-site rational CPTP comparator \(\Phi=\operatorname{Ad}_U\), with diagonal conditional expectation \(\Delta_D\), hidden iterates \(h_k(d)=(1-\Delta_D)\Phi^k(d)\), exact rank-six candidate \(\Xi(H_{\le3})\), and a nonzero genuine original-P3 depth-three quadratic residue.

Choose \(G=\operatorname{diag}(1,i,1)\). Define \(\Gamma_G=\operatorname{Ad}_G\) and a **deliberately gauge-conjugated** channel

\[
\Phi_G=\Gamma_G\circ\Phi\circ\Gamma_G^{-1}.
\]

Because G is diagonal, its conjugation fixes the diagonal MASA pointwise and commutes with the diagonal expectation. On **all** matrix units (hence all \(M_3(\mathbb C)\)):

\[
\boxed{\Gamma_G\Phi=\Phi_G\Gamma_G},\quad
\Delta_D\Gamma_G=\Delta_D,\quad
(1-\Delta_D)\Gamma_G=\Gamma_G(1-\Delta_D).
\]

Therefore \(h^G_k(d)=\Gamma_G h_k(d)\) for diagonal d, and \(\Xi\Gamma_G=\Gamma_G\Xi\) on the complex hidden candidates. All diagonal original P3 quadratic residues are unchanged under this simultaneous gauge transform:

\[
\Delta_D([\Gamma_G z,\Gamma_G w^\dagger])
=\Delta_D([z,w^\dagger]).
\]

The matrix-unit intertwiner, hidden jets and candidate real rank are verified exactly. More generally every finite time and full synchronized controlled process has identical population histories **if** the states, operations and measurement instruments are all gauge-transformed consistently. Fixing an *independently calibrated external X/Y apparatus* instead of transforming it is a physically different comparison and can distinguish relative orientation.

**Crucial limit:** \(\Phi_G\) was defined by conjugation from the SAME microscopic source. This demonstrates coordinate covariance, **not** a nontrivial independent P3-to-frozen-P6 source derivation or a new physical control.

For the frozen-P6 path exchanges \(A_{01}=E_{01}-E_{10}\) and \(B_{12}=E_{21}-E_{12}\),

\[
\boxed{\Gamma_G A_{01}=-i(E_{01}+E_{10}),\quad
\Gamma_G B_{12}=-i(E_{12}+E_{21}).}
\]

Both real exchange generators become imaginary symmetric (T-odd relative to the **unchanged** bare transpose involution), but remain physically **the very same two knobs in a rotated coordinate frame** if source/target/observer are transformed together. The proper transformed transpose symmetry is \(\tau_G=\Gamma_G\circ\tau\circ\Gamma_G^{-1}\). H64's linear equivariant access obstruction remains valid **in the fixed original real-control frame**. Apparent imaginary control coefficients by themselves do not certify any microscopically generated transposition breaking.

## 2. H65.2 — gauge-trivial path phases: a rigorous tree theorem

Let \(H=H^\dagger\) have nonzero offdiagonal hopping entries only along an undirected finite tree T, with complex coefficients \(h_{ab}=|h_{ab}|e^{i\phi_{ab}}\), \(h_{ba}=\bar h_{ab}\). Choose one root and set its gauge phase \(g_r=1\). For each child b of an already assigned parent a, recursively choose

\[
g_b=g_a\,\frac{h_{ab}}{|h_{ab}|}.
\]

For \(G=\mathrm{diag}(g_v)\), the transformed edge is \(h'_{ab}=g_a h_{ab}\bar g_b=|h_{ab}|>0\). Because T has no cycle, this recursion never gives conflicting assignments. Thus **every static complex edge-hopping phase on a tree can be made positive-real by diagonal unitary rephasing**, preserving the diagonal population observable algebra and the eigenvalues. Diagonal onsite energies are untouched.

**No-Go scope:** H65.2 rules out claiming a **gauge-invariant static loop chirality** purely from hopping phases on the original P6 three-site path \(0-1-2\). It does **not** rule out relative phases with an independently fixed external coherence axis, control timing or multiple controls on the same edge, temporal gauge/effective electric effects, nontrivial driven Floquet loops, dissipative phase-sensitive instruments, or larger graphs with cycles. A phase basis change alone does not create a physical operational resource.

**Important non-equivalence with the original P3 residue:** Tree-phase removability does **not** force the original P3 diagonal quadratic residue to vanish in general. H36/H40 already exhibited a real nearest-neighbor path hopping Hamiltonian with nonuniform diagonal onsite energies and a genuine nonzero original P3 signed depth-three residue, including leading coefficient proportional to \(2iJ^2(v_0-v_1)\), despite the absence of a static hopping loop. The P3 signed residue probes relative hidden-iterate phases and diagonal energy differences; it is **not identical to the hopping Wilson-loop flux**. H65's H32 example additionally confirms nonzero signed residue is unchanged by diagonal rephasing. Therefore neither "nonzero P3 residue implies triangular flux" nor "tree gauge triviality implies R3=0" is valid. H64's all-depth zero-residue result had the stronger premise that all hidden iterates stay real symmetric under real orthogonal dynamics; H36's onsite detuning violates that invariance condition.

## 3. H65.3 — cycle flux escapes the tree obstruction, explicitly and conditionally

Add a **physical** 02 chord, enlarging the path to a triangle. Consider the ordinary Hermitian three-level Hamiltonian

\[
H_\triangle=
\begin{pmatrix}
0&1&-i\\
1&0&1\\
i&1&0
\end{pmatrix}.
\]

Its oriented closed-loop product is

\[
\boxed{\mathcal W=H_{01}H_{12}H_{20}=i.}
\]

Under any diagonal gauge the three site phases telescope, so \(\mathcal W\) remains i. Consequently **no** diagonal unitary can make all three nonzero hopping entries real, because a product of three real numbers would be real. Unlike a single path edge phase, \(\arg\mathcal W=\pi/2\) is an intrinsically gauge-invariant *relative closed-loop* chirality of this declared microscopic Hamiltonian.

**Conventional quantum signal:** start in the diagonal pure seed \(\rho_0=E_{00}\); let \(p_j(t)=\operatorname{Tr}(E_{jj}e^{-itH_\triangle}\rho_0e^{itH_\triangle})\) at the same positive t. Using the exact first and second amplitude coefficients,

\[
\begin{aligned}
p_1(t)&=t^2+t^3+O(t^4),\\
p_2(t)&=t^2-t^3+O(t^4),\\
\boxed{p_1(t)-p_2(t)}&=\boxed{2t^3+O(t^4)}.
\end{aligned}
\]

This follows from \(a_{j0}(t)=-it H_{j0}-t^2(H^2)_{j0}/2+O(t^3)\). A finite positive-time statement is rigorously certified: \(\|H_\triangle\|_{\mathrm{op}}\le2\) (Hermitian max row absolute sum 2), so \(\|-i[H_\triangle,\cdot]\|_{1\to1}\le4\). Each population fourth-order-and-higher Taylor remainder at \(0<t<1/4\) is bounded by \((4t)^4/[24(1-4t)]\). Thus

\[
p_1(t)-p_2(t)\ge 2t^3-\frac{2(4t)^4}{24(1-4t)}
\]

and at **t=1/100**,

\[
2t^3=\frac1{500000}>\frac1{4500000}
\]

so the real-time signal is **strictly positive**, not just a formal series or Cayley surrogate. The comparator uses a genuinely Hermitian non-real H; its signal is standard quantum physics and cannot be called a CR-specific prediction.

**Physical source boundary:** the added 02 chord and loop phase are NOT the original two-edge frozen P6 real-control manifold. Their independent microscopic origin, control and readout permissions and compatibility with the actual P6 \(\mathcal J_N\) remain UNPROVEN. The cycle flux is not itself a unique 12D KKS Lagrangian polarization, an absolute U(1) phase reference, a CR hidden-flow theorem, an Einstein gravitational sector, or a 3D metric-matching result.

## 4. H65 provenance verdict / next H66 gate

| Question | Exact verdict | Remaining physical provenance |
|---|---|---|
| H64 odd-looking controls generated by diagonal rephasing? | **Gauge-coordinate equivalence:** does not create a new independent knob | Source-control-hardware fixed reference and full CP/process intertwiner |
| Can path-only complex hopping produce a nontrivial static Wilson/loop flux? | **NO-GO** on a finite tree with hopping phases | Alternative mechanism: reference apparatus, time-dependent operation, or real microscopic cycle |
| Can a real finite quantum model exhibit genuinely gauge-invariant chirality? | **YES conditionally** on independently specified triangle/chord and imaginary loop product | Whether P3/P6 physically generates that chord and phase, not just embeds it by fiat |
| Does observed flux or exact population asymmetry prove CR-only dynamics? | **NO**; ordinary Schrödinger evolution gives exactly the signal | Independently sourced CR restriction or falsifiable matched-standard comparator |
| Does H65 solve P9/P7 Einstein/ADM? | **NO** | KKS polarization origin, DeWitt kinetic, full HDA, independent gravity dynamics |

**H66 target:** establish a **source-and-instrument-certified odd-control provenance criterion**. For a proposed P3 hidden source sector \(\mathcal J\), demand (i) a physically fixed microscopic \(\Phi\) and \(\mathcal J\), (ii) a star-compatible source→hardware map on declared real control tangents, (iii) explicit full controlled-CPTP/observer intertwining or state-preparation-to-readout characterization, and (iv) a gauge-invariant or independently calibrated observable distinguishing the added odd resource. Run a concrete path-plus-chord source candidate and determine whether any of these conditions actually follows from the ORIGINAL P3 quadratic residue. If not, prove a restricted No-Go, rather than supplying a physically new chord by assumption. P9.72's SWAP+ZZ phase/calibration remains an independent conditional resource until its source and uniform limits are audited.

## Reproducibility

\`python3 P3/P9H65TreeGaugeCycleChiralityExactCheck.py\` checks the H32 matrix-unit/Krylov gauge intertwiner, physical-path-exchange→apparent odd-coordinate conversion, gauge-invariant loop flux, exact \(t^2,t^3\) population series and strict certified positive-time tail inequality using Gaussian rational arithmetic. Its exact finite statements and analytic tree recursion are distinct from physical-source claims.

**Status:** staged Draft/unmerged; no changes to frozen manuscripts/main; no independently verified P9.72 original Jacobian, human peer review, Lean formalization, CR-exclusive observable, full HDA/ADM or Einstein derivation.
