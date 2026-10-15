# H63 — Physical P6 Real-Instrument Fingerprints and the Anti-Symplectic Conjugation Obstruction

**2026-10-15 | P3–P11 Mathematical Bridge / P9 GR-I.** H63 continues H62's phase-sensitivity test by using the **specific frozen P6 v9.1 three-site benchmark**, as independently recorded in H38 and H39: two **real exchange** knobs, independently calibrated site-dephasing, and diagonal population observations. The richer P9.70 four-level \(X/Y\) Hamiltonian and calibrated X/Y channels are **not automatically authorized by frozen P6**. H63 adds a proof at the level of **outcome-adaptive real instruments and KKS symplectic orientation**. It does not invent a new P6 physical control; H38 already proved the underlying imaginary-coherence blindness for real exchange/dephasing.

## 1. Hardware provenance boundary: real P6 versus enhanced P9.70

Frozen P6's benchmark coherent generator is real antisymmetric \(K=z-z^\dagger\) with **real edge amplitudes**, so \(U=\exp(tK)\) is real orthogonal. The original readout is \(\Delta_D\), a diagonal population observer; calibrated dephasing is real and transposition-covariant. H38 proved it cannot read imaginary offdiagonal coherence at any depth for real-control sequences.

P9.70 instead allows a Hermitian control \(H_c=\sum_e(u_e X_e+v_eY_e)\) with \(X_e=E_{ab}+E_{ba}\) (real symmetric) and \(Y_e=-i(E_{ab}-E_{ba})\) (imaginary antisymmetric), plus independently phase-calibrated X/Y readout. Under Schrödinger evolution, the \(Y\)-generated unitary corresponds to a **real rotation** (up to convention), while \(X\) generically drives a **complex** unitary. Therefore treating both \(u_e,v_e\) as inherited physical frozen-P6 controls would be an unjustified hardware enlargement. As H39 established, calibrated Stark/phase gates are a separately declared **extra** physical resource.

## 2. H63.1 — all-depth transpose-equivariant classical observer theorem

Let \(\tau(\rho)=\rho^T\) (equivalently \(\bar\rho\) for Hermitian \(\rho\)). Consider any adaptive finite experiment built from:

- unitary conjugations by **real** orthogonal \(U\);
- calibrated real diagonal dephasing \(D_q(\rho)=q\rho+(1-q)\Delta_D(\rho)\), \(0\le q\le1\);
- outcome-resolved CP operations \(\mathcal I_j(\rho)=\sum_\alpha R_{j\alpha}\rho R_{j\alpha}^T\) whose Kraus matrices \(R_{j\alpha}\) are **real**, and whose total instrument is trace preserving;
- outcome-dependent choices of subsequent controls/instruments based only on **classical outcome histories**, ending in population observations or other real-symmetric effects.

Then each elementary map satisfies \(\mathcal E(\rho^T)=\mathcal E(\rho)^T\). Composition, branching and normalized conditional evolution on positive-probability branches preserve this identity. Since trace and real-symmetric output effects are transpose-invariant, the entire finite **joint classical outcome law** satisfies

\[
\boxed{P_{\boldsymbol j}(\rho)=P_{\boldsymbol j}(\rho^T)}
\]

for **every finite adaptive depth**, all allowed real control values and every initial Hermitian density matrix. This is a finite operational observational-equivalence statement within the declared real instrument subcategory. It is **not** true after adding general complex Kraus operators, coherent Y-tomography, a calibrated complex phase resource, or coherent quantum-block outputs beyond the diagonal observer.

**Exact physical witness:** \(\rho_\pm=I_3/3\pm\frac{i}{6}(E_{01}-E_{10})\) have positive spectra \(\{1/6,1/3,1/2\}\), satisfy \(\rho_-=\rho_+^T\), and are distinct. A standalone rational checker verifies transposition covariance and equality of all branch probabilities for an **adaptive two-outcome diagonal weak instrument**, rational real rotations on edges 01/12/02 and rational dephasing, for every outcome string through depth four (16 strings at final depth); actual all-depth validity follows by induction, not finite enumeration.

The original P6 model has only a subset of these real instruments; adding more **real** instruments does not remove the transpose obstruction. This extends H38's operational viewpoint to adaptive classical instruments without claiming that those extra instruments are physically available in the frozen protocol.

## 3. H63.2 — anti-symplectic pullback obstruction

On a regular coherent \(U(2)/U(1)\) KKS patch with local canonical \((q,p)\), complex conjugation acts

\[
\tau(q,p)=(-q,p),\qquad
\tau^*(dq\wedge dp)=-dq\wedge dp.
\]

Thus \(\tau\) is **anti-symplectic**: it reverses the KKS oriented area element. Let \(\Sigma:\mathcal U\to\mathcal V\) be any **classical** fingerprint built from the real-instrument protocol above, on a \(\tau\)-stable coherent domain \(\mathcal U\). By H63.1, \(\Sigma\circ\tau=\Sigma\).

**Theorem H63.2 (orientation-from-real-observation NO-GO).** There exists **no** differential 2-form \(\beta\) on the fingerprint target \(\mathcal V\) for which

\[
\boxed{\Sigma^*\beta=\omega_{\mathrm{KKS}}}
\]

holds on the entire \(\tau\)-stable coherent domain. Proof: the left-hand side is \(\tau\)-invariant, while \(\tau^*\omega_{\rm KKS}=-\omega_{\rm KKS}\ne0\); pulling back the hypothetical equality gives a contradiction. In particular a unique oriented symplectic phase identification **cannot descend solely from the frozen-P6 real-classical fingerprint** under these premises. This is stronger than merely observing that a certain \(2\times2\) response Jacobian lacks one rank direction.

**Fixed-locus corollary:** At coherent real-state points \(q=0\) or \(q=\pi\), \(d\tau\) reverses the \(q\) tangent. Because \(D\Sigma\circ d\tau=D\Sigma\), one has \(D\Sigma(\partial_q)=0\). Any positive-semidefinite pullback response metric \(G_\Sigma=(D\Sigma)^TW D\Sigma\) is **phase-null at those fixed points** for every positive readout weighting \(W\). Away from the fixed locus, the classical fingerprint may have some phase sensitivity through \(\cos q\), but still identifies \(q\) and \(-q\): a universal local rank no-go at **every** phase is **not** claimed.

**Scope guard:** This orientation pullback no-go is about identifying the KKS form by a 2-form **derived entirely from an invariant fingerprint**. It does *not* forbid the original known KKS form on the microscopic orbit, an invariant 1D population foliation, a separately specified coherent reference, or a local chart confined to one branch that is not \(\tau\)-stable. More generally, a separately supplied *odd* symmetry-breaking object could restore an oriented selector, but proving its P3/P6 provenance is an extra task.

## 4. H63.3 — minimally sufficient EXTRA complex resource, without CR provenance

H38/H39 provided an independently calibrated diagonal Stark phase resource. For the exact witness above let

\[
V=\operatorname{diag}(-i,1,1).
\]

Its conjugation rotates the imaginary offdiagonal \(\rho_{01}=\pm i/6\) into real coherence \(\pm1/6\). Apply a real \((01)\)-rotation of coefficients \(c=3/5,s=4/5\). Then the final population contrast is **exactly**

\[
p_0^+=\frac{37}{75},\qquad
p_0^-=\frac{13}{75},\qquad
\boxed{p_0^+-p_0^-=\frac{8}{25}\ne0}.
\]

Without \(V\), the corresponding \(p_0\) values agree at \(1/3\). The finite rational checker verifies this numerical certificate. This is ordinary quantum control mathematics and does not show the Stark phase is supplied by P3 hidden flow or the original frozen P6 physical controls. The **minimum resource requirement** proven here is to **break the relevant transpose symmetry of the classical fingerprint**; the particular \(V\) is one sufficient way, not a universally minimal gate set.

## 5. Precise three-stage answer to P9 H62/H63

| P9 question | H63 verdict | Remaining provenance gate |
|---|---|---|
| (1) Does actual P6 fingerprint generate a coherence-sensitive positive metric? | Under **frozen real 3-site population benchmark**, transposition symmetry makes its classical fingerprint \(q\leftrightarrow-q\) indistinguishable; at real-coherence fixed points angular metric rank vanishes | Full original \(\Sigma\) could include other physical observables/protocols; specify actual \(C_A,T_B,E_t\) beyond baseline |
| (2) Does metric + P3 flow uniquely choose an oriented polarization? | No oriented KKS pullback from purely \(\tau\)-invariant classical fingerprint on a \(\tau\)-stable domain; extra odd reference required | Identify reference-generating CR operator, its transformation, actual physical control, and invariance group |
| (3) Does such choice determine \(A,\kappa_i\)? | No from baseline alone; H62 zero-time background-insensitivity persists | Finite-time spatially resolved physical \(\Sigma\), inverse conditioning, P9.72 large-system error budget |

**Next H64 gate:** Attempt a physically **honest microscopic control/source lift** for an anti-\(\tau\)-invariant phase-sensitive observable or operation, using the real P6 hardware and P3 signed hidden-flow as actually defined. Prove existence with explicit accessible controls and nonvanishing operational rank **or** establish a wider symmetry-preserving NO-GO. Independently transport through P9.72 only after its error estimates and common physical reference are supplied. Any enlargement of frozen-P6 hardware must remain an expressly conditional model change.

## Audit and paper boundaries

All algebra is ordinary finite quantum mechanics; these tests are not CR-exclusive experimental predictions. The checker uses standard-library \`fractions.Fraction\` only. H63 extends the previously proved H38 real-exchange blindness to adaptive **real CP instruments** and to the geometric **symplectic-orientation pullback obstruction**. It does not assume a new P3 signed-residue result, a U4 physical orbit identity, KKS→ADM global equivalence, DeWitt kinetic provenance, full HDA, or Einstein dynamics. Draft/unmerged; no frozen papers/main changes; no human peer review or experiment.
