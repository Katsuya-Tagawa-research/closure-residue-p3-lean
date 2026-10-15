# H78 — Certified Microscopic Control Ports, Infinitesimal Observability, and the Reset-Preparation Scope Gate

**2026-10-16 | P3–P11 Mathematical Bridge / Route A.** Stacked on H77 Draft PR #96 (**90/90 GitHub Actions PASS**). The complete six-level H75 four-Kraus microscopic CPTP channel \(\Phi_\mu\), its independently verified **original P3** \(R_2=0\) and nonzero \(R_3\), and H76's flag-block CPTP observer \(\mathcal C_{\rm flag}\) remain **unchanged**. This stage supplies a **physical control-port certificate** for H77's catalog-dependent observability ranks, then tightens a potentially misleading conclusion: mandatory microscopic measurement/reset restricts the reachable source-output manifold to complex-linear **rank nine**, even though sufficiently rich **pre-reset** coherent controls render all 36 microscopic operator directions observable.

## 1. Exact microscopic port certificate, not a P3-derived device

Let \(\mathcal H_\mu=\mathbb C^2_E\otimes\mathbb C^3_S\) and \(\mathcal C_{\rm flag}(X)=\sum_{a=0}^1P_aXP_a\) with rank 18 and image \(M_3(\mathbb C)\oplus M_3(\mathbb C)\). The H75 four-Kraus microscopic source \(\Phi_\mu\) resets and writes an **informative physical environment flag**. The **additional hardware premise** of H78 is that particular calibrated controls can be independently switched **between** uses of this microscopic reset channel, including *before* the next compulsory reset:

- Flag port: the real anti-Hermitian generator
  \[
  J_E=(|1\rangle\langle0|-|0\rangle\langle1|)_E\otimes I_3,\quad
  J_E^\dagger=-J_E,\quad J_E^2=-I_6.
  \]
  Its continuous gate family may be implemented by the Hermitian Hamiltonian \(H_J=iJ_E\), so \(e^{-itH_J}=e^{tJ_E}\). The *exact* rational Cayley pulse
  \[
  V_J(t)=(I+tJ_E)(I-tJ_E)^{-1}
  =\frac{1-t^2}{1+t^2}I+\frac{2t}{1+t^2}J_E
  \]
  at \(t=1/2\) equals **the existing H76 actual flag-rotation gate** \(W\) with coefficients \(3/5,4/5\). There is no added complex phase calibration or invented imaginary hopping.
- Two independent site exchange ports: \(K_A=I_E\otimes(E_{01}-E_{10})\) and \(K_B=I_E\otimes(E_{21}-E_{12})\), both real anti-Hermitian with independently addressable real amplitudes. Their existing H75 rational Cayley pulses at \(t_A=1/2\), \(t_B=2/3\) are exactly H77's \(V_A,V_B\).
- Flag-conditioned feedback port: use the already physically declared H75/H76 controlled-SWAP unitary \(F\), and an *independently calibrated* Hermitian **projector** coupling
  \[
  H_F=\frac{I_6-F}{2}
      =|1\rangle\langle1|_E\otimes\frac{I_3-S_{01}}2.
  \]
  It obeys \(H_F^2=H_F\), and **one calibrated pulse area \(\pi\)** gives \(e^{-i\pi H_F}=I_6-2H_F=F\) by exact projector spectral calculus. This does not imply arbitrary Hamiltonian parameter estimation, a physically available port, or an experimental demonstration: those are independent microscopic **apparatus facts** that must be established.

Each listed device has an explicit finite six-dimensional unitary and, when switched, a genuine CPTP conjugation channel. The exact checker verifies the port generator and unitary matrices, the rational Cayley identities, \(H_F^2=H_F\), and the existing H77 gate identification on the **same original H75 source**. The original uncontrolled channel and its P3 signed residues are unchanged by whether these additional ports are installed. H78 is therefore a *constructive conditional source-to-port certificate*, not a claim of **P3-only generative accessibility**.

## 2. H78.1 — the *infinitesimal* calibrated-port Jacobian reproduces H77 rank 36

For a real anti-Hermitian generator \(K\), the infinitesimal action of its real one-parameter unitary group is
\[
\left.\frac d{dt}\operatorname{Ad}_{e^{tK}}(X)\right|_{t=0}=[K,X].
\]
For the rational Cayley path \(V_K(t)\), the derivative at zero is \(2[K,X]\); the factor of two does not alter the invariant kernel, observable span or rank. Its quantum Heisenberg transpose acts on the 36-dimensional dual operator coordinates with **exact rational coefficients**.

Let \(\mathscr O_0\) be the 18-dimensional linear span of the two flag-block output quantum-matrix coordinates. Define \(\mathscr O_{n+1}\) as the span of \(\mathscr O_n\) and all its Heisenberg pulls under the **infinitesimal** generators \(\mathrm{ad}_{J_E},\mathrm{ad}_{K_A},\mathrm{ad}_{K_B}\) and the exact discrete CPTP feedback conjugation \(\mathrm{Ad}_F\). This stabilizes in at most 36 strict rank increments.

The H78 **independently recomputed exact Fraction-rational rank table** is:

| Calibrated accessible port catalog | Heisenberg observable rank by iterative depth | Final complex rank |
|---|---|---:|
| \(F\) only | 18 → 18 | 18 |
| \(J_E\) only | 18 → 27 → 27 | 27 |
| \(J_E,F\) | 18 → 27 → 31 → 31 | 31 |
| \(J_E,F,K_A\) | 18 → 27 → 31 → 34 → 35 → 35 | 35 |
| \(J_E,F,K_A,K_B\) | **18 → 27 → 31 → 35 → 36 → 36** | **36** |
| \(F,K_A,K_B\) (no flag-coherent port) | 18 → 18 | 18 |
| \(J_E,K_A,K_B\) (no feedback coupling) | 18 → 27 → 27 | 27 |

These exact tangent-space ranks match H77's *discrete finite pulse* ranks **one for one** when the same physical ports are available. The verifier uses true **6×6** generators, explicitly constructs the 36×36 superoperator derivative matrices via \([K,X]\), applies the **independent** rational reduced-row-echelon algorithm from H77 and checks every row-rank and all stabilization depths. No floating-rank calculation and no fitted Lie reachability assumptions.

**Interpretation:** If experimental **control ports and temporal access** genuinely allow sequences of these Hamiltonian operations **before** the next compulsory microscopic reset, then all 36 microscopic operator directions are observable through complete flag-block quantum-output tomography after control words of length at most four. To see the equivalence between derivative and finite-control spans, note that in finite dimension any continuous one-parameter conjugation \(e^{t\,\mathrm{ad}_K}\) and its derivatives at zero generate the same finite-dimensional invariant span: forward inclusion follows from Taylor/polynomial functional calculus, and reverse inclusion from difference quotients plus finite-dimensional subspace closure. Exact finite pulses \(W,V_A,V_B\) furnish an independent check.

Thus any **complex-linear sufficient record** that predicts **every full flag-block output for every arbitrary six-level input state** and every allowed pre-reset pulse word must have rank **36**, with the physically CPTP identity quantum memory sufficient. This is NOT the minimum Hilbert dimension for a restricted input code, nor a lower bound for scalar-only flag/site outcome readout. The actual H76 rank-18 block memory remains CPTP sufficient if coherent flag mixing is *not* accessible.

## 3. H78.2 — mandatory reset restricts the source-output preparation manifold to rank NINE

The strongest new qualification concerns **which microscopic input states are physically preparable**. H75's four-Kraus source has Kraus matrices \(L_{ab}=|a\rangle\langle b|_E\otimes UM_a\) and acts by
\[
\Phi_\mu(X)
=\sum_a |a\rangle\langle a|_E\otimes
UM_a(\operatorname{Tr}_EX)M_a^\dagger U^\dagger.
\]
Therefore
\[
\Phi_\mu=\mathcal J_{\rm out}\circ \operatorname{Tr}_E
\]
for a completely positive trace-preserving **instrument-preparation** map \(\mathcal J_{\rm out}:M_3\to M_6\). The visible channel is invertible as a **linear** nine-complex-dimensional map in this rational H75 model (but its inverse is not claimed CPTP), so the full six-dimensional micro channel has
\[
\boxed{
\operatorname{rank}_{\mathbb C}\Phi_\mu=9.
}
\]
The exact H78 checker computes rank 9 from **all 36 true six-dimensional matrix-unit inputs**, not simply by dimensional intuition, and verifies that \(\mathcal C_{\rm flag}\) fixes its entire image:
\[
\mathcal C_{\rm flag}\Phi_\mu=\Phi_\mu,\qquad
\operatorname{rank}(\mathcal C_{\rm flag}\Phi_\mu)=9.
\]

If the actual hardware **forces a source measurement/reset first**, so admissible initial states are restricted to \(\mathrm{im}\Phi_\mu\), no subsequent word can require more than **nine complex-linear input degrees of freedom** to predict all outputs, because the initial preparation manifold itself is nine-dimensional. The empty-word flag-block record already has rank nine on that manifold, so nine is a **sharp linear-record dimension** under these *restricted initial preparation* quantifiers. For clarity, the set of normalized physical states in the source-output range is not itself a vector subspace, but its complex linear span is the indicated nine-dimensional subspace.

This sharp distinction resolves an overly strong reading of H77:
\[
\boxed{
\begin{array}{l}
\text{arbitrary pre-reset 6D inputs + access to ports before reset}\\
\qquad\Rightarrow \text{exact predictive record rank }36,\\[2pt]
\text{post-reset source-prepared inputs only}\\
\qquad\Rightarrow \text{linear record rank }9\text{ suffices}.
\end{array}
}
\]
The second statement does **not** establish a nine-dimensional CPTP quantum memory after arbitrary future controls: an abstract linear nine-direction encoding may fail complete positivity or fail to support an autonomous output CPTP extension. The **physical** H76 flag record remains a legitimate rank-18 CPTP memory for its declared feedback catalog, and the full 6D micro carrier can implement any expanded actual CPTP control sequence. One must state whether the observer is interrogated **after each forced reset**, or whether a coherent control word can act **before the next reset**, and whether intermediate instrument outcomes are accessible.

This preparation/causal-order dependence is operationally as important as the abstract catalogue itself.

## 4. H78.3 — calibration can measure a port response, but P3 alone cannot determine port existence

Let
\[
X=|0,0\rangle\langle1,0|+|1,0\rangle\langle0,0|.
\]
It obeys \(\mathcal C_{\rm flag}(X)=0\). Nevertheless,
\[
\boxed{
\mathcal C_{\rm flag}[J_E,X]
=-2|0,0\rangle\langle0,0|
+2|1,0\rangle\langle1,0|\ne0.
}
\]

The two **positive** density operators \(\rho_\pm=I_6/6\pm X/12\) have the same initial \(\mathcal C_{\rm flag}\) output, but acquire distinct flag-block output records after the calibrated flag-port Cayley pulse \(W\). Both positivity and the exact first-order response are checked rationally. This is a concrete **device-calibration response** for a coherent flag port provided such pre-reset coherent preparations and flag population readout are independently possible. It is a standard quantum response, not a CR-exclusive signature. If the H75 reset always precedes any experimental access, this witness is erased and the claimed port calibration protocol is not physically available.

Most importantly: exactly the same uncontrolled \(\Phi_\mu\) and **all original P3 data derived solely from it**, including its genuinely nonzero signed \(R_3\), can coexist with (i) no coherent flag port, or (ii) the additional port \(J_E\), or (iii) all the independently switchable ports specified above. Device accessibility is **not a mathematical function of uncontrolled P3 input alone**. H78 supplies explicit certified **sufficient physical premises** that let the H77 operator-filtration compute predictive memory; it does not derive those premises from the P3 hidden Krylov space, the signed quadratic return, frozen P6 v9.1's actual hardware, or the Generative Map \(F\).

## 5. H78 formal verdict / next gate

| Criterion | H78 result |
|---|---|
| Fixed H75 original six-dimensional CPTP source with genuine nonzero original P3 \(R_3\) | SAME, exact |
| Independently specified finite microscopic Hamiltonian control ports and pulse-to-gate maps | EXACT **conditional** certificate |
| Exact infinitesimal control-observability Jacobian for named port catalog | EXACT ranks **18/27/31/35/36** |
| Finite-pulse H77 observability recovered from calibrated microscopic generators | EXACT |
| Full rank36 needed for arbitrary pre-reset correlated six-level states and all full quantum-block control readouts | EXACT **under declared quantifiers** |
| Full rank36 forced for preparations only after H75's mandatory micro reset | **NO** — exact source-output linear rank9 |
| Nine-direction abstract post-reset record always realizable as autonomous CPTP memory | **NOT PROVED** |
| Source-only original P3 can infer which physical ports exist or their switchability | **NO** (same \(\Phi_\mu\), different device catalogs) |
| Full frozen P6 provenance, CR-exclusive prediction, P9 ADM/HDA/Einstein success | **OPEN** |

**H79 recommended goal:** Find the physical/operational **causal scheduling conditions** that admit pre-reset port access and flag-quantum coherence preparation, then test a concrete microscopic Hamiltonian **dilation** with bounded-strength switchable ports instead of merely an abstract port catalog. If those conditions cannot be sourced independently of P3, state a minimal separate control-accessibility axiom for P11 and do not claim it has already been derived. In parallel test the genuine **quantum CP/trace-preserving sufficient-statistic construction** on the rank-nine post-reset source-output family under the restricted intervention catalog (not just linear rank), perhaps obtaining a sharper physical memory size than H76's rank18 for reset-scheduled protocols.

**Reproducibility:** \`python3 P3/P9H78MicroscopicHardwarePortsObservabilityExactCheck.py\`. Exact rational original-H75 Kraus sourcing, port matrices, projector pulse, infinitesimal 36×36 superoperators, full rank-depth audit, micro-channel rank9, P3 source invariant and positive density-pair port response. Stacked Draft/unmerged, frozen papers/main untouched, no Lean kernel proof, human referee, experiment, independent frozen P6 hardware mapping or P9 Einstein Minimum Success.
