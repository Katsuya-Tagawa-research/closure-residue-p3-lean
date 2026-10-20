# P3–P11 Mathematical Bridge — H75/AX-OA operational metric descent access enlargement

**Date:** 2026-10-20  
**Status:** Standalone mathematical auxiliary audit; not assigned an H or AX stage.  
**Inputs:** H75 PR #94 source, H81 PR #100 feedback and schedule, H82 PR #101 access-certificate boundary, and the independent fixed-KKS-orbit GT–K4 counterpair supplied 2026-10-20.  
**No modification:** Notion, GitHub, frozen P1–P8, P9, P11 G2/G3.

## 1. Exact source and orbit facts

Work in `H_micro=C^2_E ⊗ C^3_S` with ordered basis `(E0S0,E0S1,E0S2,E1S0,E1S1,E1S2)`. Let

\[
B(a,b;p,q)=\begin{pmatrix}a&ip&0\\-ip&b&iq\\0&-iq&a\end{pmatrix}.
\]

For the two states `rho` and `sigma`, block 0 has `(a,b)=(3/25,11/25)` with `(p,q)` equal respectively `(sqrt(57)/50,0)` and `(257 sqrt(57)/38450,2736/19225)`; block 1 has `(a,b)=(8/75,8/75)` with `(p,q)` respectively `(0,8/75)` and `(256 sqrt(57)/19225,-2056/57675)`.

Both are positive trace-one with corresponding U(3) block spectra `(1/2,3/25,3/50)` and `(16/75,8/75,0)`. Consequently they belong to the same fixed `U(3)×U(3)` KKS orbit. Their difference `delta=sigma-rho` is nonzero and is entirely imaginary off-diagonal in each block, with zero diagonal.

**Crucial input limit.** Equality of the original `R_obs∈R^15`, the six GT coordinates and the GT–K4 metric *is reported by the user's independent audit*; we did not independently recompute it because complete executable definitions of `R_obs`, GT edges and `g_eng` were not provided. We neither claim to have established nor invalidate the original fixed-orbit no-go from this partial audit.

## 2. H75/H81 operators, independently checked

H75 source has four Kraus matrices `K_ab=|a><b|_E ⊗ U M_a`, with

\[
U=\operatorname{diag}(i,1,i)\begin{pmatrix}2/3&2/3&-1/3\\-2/3&1/3&-2/3\\-1/3&2/3&2/3\end{pmatrix},\qquad
M_0=\operatorname{diag}(1,3/5,3/5),\;M_1=\operatorname{diag}(0,4/5,4/5).
\]

This is an exact CPTP map `Phi_mu` because `sum K_ab^†K_ab=I_6`. H81's flag-conditioned feedback is

\[
F_{\rm fb}=|0\rangle\langle0|_E\otimes I_3+|1\rangle\langle1|_E\otimes S_{01},
\]

where `S_01` swaps system sites 0 and 1. H75's real system Cayley control is `V(0,y)=(I+yB)(I-yB)^(-1)` for `B=E21-E12`, lifted by `I_E⊗V(0,y)`. The genuine positive, physical site-1 measurement effect is `Q_1=I_E⊗|1><1|`.

**If the original source reset is mandatory first,** the pair cannot be distinguished at any subsequent time:
\[
\Phi_\mu(\sigma-\rho)=0
\quad\Longrightarrow\quad
\mathcal I_w\Phi_\mu(\sigma)=\mathcal I_w\Phi_\mu(\rho)
\]
for all subsequent identical linear CPTP/channel-instrument words `w`. This is an *exact* source-specific obstruction.

## 3. Concrete extension of permitted AX-OA scheduling: finite state-pair separation

The following **new certified-access assumption** is required:

1. Both input states can be prepared in the declared 6D flag/system basis.
2. The flag-conditioned unitary `F_fb` can be executed **before** the mandatory source reset `Phi_mu`.
3. The existing H75 real Cayley port `I_E⊗V(0,y)` can be executed **after** that reset and before a site measurement.
4. The site-1 population readout `Q_1` is available as a positive single-copy POVM effect.
5. Such a process is allowed to leave the original fixed KKS orbit at intermediate times. The KKS orbit specifies **input states**; H75's CPTP reset does not, in general, preserve the orbit or its block spectra.

This is an **extended S1-plus schedule**, not automatically the original H81 S0/S1 inventory. Define

\[
C_y(\tau)=\operatorname{Tr}\left[ Q_1 \operatorname{Ad}_{I\otimes V(0,y)}
\Phi_\mu\operatorname{Ad}_{F_{\rm fb}}(\tau)\right].
\]

An exact calculation yields a real off-diagonal coherence on system 1↔2 after the pre-reset feedback and the source,

\[
\sum_{a=0}^1\operatorname{Re}[(\Phi_\mu\operatorname{Ad}_{F_{\rm fb}}(\sigma-\rho))_{(a,1),(a,2)}]
=\frac{14592+512\sqrt{57}}{96125}>0.
\]

The Cayley rotation converts it to an ordinary population difference:

\[
\boxed{
C_y(\sigma)-C_y(\rho)
=-\frac{4y(1-y^2)}{(1+y^2)^2}
\frac{14592+512\sqrt{57}}{96125}.}
\]

The difference is nonzero for **every real finite `y` except `0,±1`**, so the separation is open-dense in the one-dimensional calibrated control family (no claim of control/hardware availability). At `y=1/3`,

\[
C_{1/3}(\sigma)-C_{1/3}(\rho)
=-\frac{350208+12288\sqrt{57}}{2403125}\approx-0.184335132605.
\]

The genuine quantum probabilities are approximately `C_1/3(rho)=0.37057358645` and `C_1/3(sigma)=0.18623845385`, both between 0 and 1. Prior to the Cayley rotation, the **same site-1 population effect is still blind** even following F_fb→Phi_mu, so the final control contributes essential observable mixing in this specified test.

For comparison, W→F_fb→Phi_mu→V(0,1/3)→Q1 also separates the pair, but with smaller positive contrast

\[
C^{WF}_{1/3}(\sigma)-C^{WF}_{1/3}(\rho)=
\frac{2451456+86016\sqrt{57}}{60078125}\approx0.0516138371293.
\]

Unlike H81's special hidden *flag-coherence* pair, **this fixed-orbit pair does not require W**: F_fb alone before reset is enough when paired with the post-reset Cayley port. Do not universalize “W+F jointly necessary” across different inputs.

## 4. Precise logical status of operational metric descent

The *reported* native-observation equality and metric difference imply a **global no-go for the original GT–K4 metric under the original 15 native readouts**. Appending the controlled effect `C_1/3` removes **this particular collision**, assuming its production and observation are independently certified.

This does NOT prove the augmented map `(R_obs,C_1/3)` separates all fibres on the orbit; it does NOT prove a continuous, differentiable, or stable metric factorization. A repeated rank test at one checkpoint is not a substitute for global fibre-constancy. Nor does the existence of a mathematical CPTP instrument establish native implementation or F-origin. The new controlled effect can separate a disconnected pair even if differential rank at some point remains unchanged.

The AX-OA descriptor must independently name: `Preparation` of the orbit inputs; the **flag-conditioned** feedback port; the **real qutrit 12-Cayley** port and its calibration; the clock order F_fb before reset before V; the final positive site-1 readout. Controls must be physically certified independently of the GT metric being reconstructed.

If an AX-OA certificate only permits `Phi_mu` first, the pair is **provably indistinguishable thereafter under all downstream CPTP operations**. Thus the certificate's temporal accessibility changes the operational equivalence relation. This is exactly H81's scheduling lesson, applied to the new fixed-orbit pair.

## 5. Integration and future gates

- **P3 Bridge:** finite CPTP control/readout algebra. Do not misidentify probability contrasts with signed original P3 residue or an experimental CR-specific signature.
- **P9:** fixed-orbit native 15-vector descent no-go remains. This pair is removable by a *conditional enlarged access protocol*, but global native descent, KKS→ADM, DeWitt, HDA, Einstein remain OPEN.
- **P11:** add certificate-indexed descent and **source/port/scheduling proof**. Neither the existence of a controlled effect nor a minimal underlying quantum model proves generative completeness; G2/G3 remain OPEN.
- **P6, P7/P8:** all physical provenance, soldering and curvature transport gates remain OPEN.
- **H82:** do not restart rank optimization. No new H number or PR needed merely to recognize this pairwise test.

**Result classification:** EXACT finite algebraic discrimination for the specified matrices; CONDITIONAL operational status pending native physical access; GLOBAL DESCENT OPEN; G2/G3 OPEN. The original GT–K4 NO-GO for native 15 observables remains as reported, not independently re-certified here.

## Sources

- H75 code/notes, existing [Draft PR #94](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/94).
- H81 code/notes, existing [Draft PR #100](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/100).
- H82 integration / AX-OA boundary, [Notion H82](https://app.notion.com/p/3fd736b71e2d8198a5d0f4a3260064c8) and [Draft PR #101](https://github.com/Katsuya-Tagawa-research/closure-residue-p3-lean/pull/101).
- User-supplied fixed-orbit GT–K4 independent auxiliary audit, 2026-10-20.
