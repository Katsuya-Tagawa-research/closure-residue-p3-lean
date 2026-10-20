# H75 — Restricted AX-OA Minimum and Positive Phase Calibration

**2026-10-20 | P3–P11 Mathematical Bridge | Draft, stacked on PR #165.**

**Scope**: Keep unchanged H75 microscopic source \(\Phi_\mu\), qutrit unitary \(U=\mathrm{diag}(i,1,i)O\), unsharp two-outcome measurement/reset, and H75/H81 gates W, flag-conditional \(F_{\mathrm{fb}}\), real Cayley \(V_A,V_B,V_{AB}\). Restrict input to \(\operatorname{Herm}(3)\oplus\operatorname{Herm}(3)\), dimension 18. No full \(M_6\) tomography is claimed.

The four **pre-reset** programs are P0=identity, P1=\(F_{\mathrm{fb}}\), P2=\(V_A\) then \(F_{\mathrm{fb}}\), P3=\(W\) then \(F_{\mathrm{fb}}\) then \(V_B\) then \(W\) then \(F_{\mathrm{fb}}\). Three **post-reset** programs are T0=identity, T1=\(V_A\), T2=\(V_{AB}\). End by a positive site readout \(Q_j\) for j=0,1,2. PR #164 constructs the exact rational \(36\times18\) record \(C\), rank 18, and a certified 18×18 rational minor. PR #165 verifies source phase and reality.

## Exact resource-subset result

The exact ranks for the **specified catalog only** are:

| Subcatalog | Exact ranks |
|---|---|
| Any one pre-reset program (all post/site) | 6 |
| Any two pre-reset programs | 10 or 11 |
| Any three pre-reset programs | 15 or 16 |
| All four pre-reset programs | **18** |
| Any single post-reset setting (all pre/site) | 9 |
| Any two post-reset settings | **13,17,17** |
| All three post-reset settings | **18** |
| Any one site projector (all pre/post) | <18 |
| **Any two** site projectors (all pre/post) | **18** |

Thus **all four registered pre-reset programs and all three registered post-reset programs** are necessary for linear informational completeness among subsets of these fixed seven settings. **Any pair of the three final site effects** remains sufficient; a concrete 24-effect catalog replaces the original 36-effect catalog. No global minimum over different gate inventories is claimed.

H75 reset factors as \(\Phi_\mu=L\circ\operatorname{Tr}_E\). If compulsory reset is always performed before any flag-sensitive operation, all subsequent record functionals factor through \(\operatorname{Herm}(3)\), giving rank at most 9. Local \(I_E\otimes V\) pre-reset pulses alone do not evade this; an explicit local Cayley subcatalog has exact rank 9. The larger rank requires an independently authorized flag-sensitive pre-reset schedule. The mathematical existence of \(W,F_{\mathrm{fb}}\) is not proof of hardware permission.

## A positive phase-orientation calibration test

Take the externally **signed-phase-prepared** initial state
\[
\rho_\phi=I_6/6+\frac{i}{12}(|0,0\rangle\langle0,1|-|0,1\rangle\langle0,0|).
\]
It is positive and trace-one, with eigenvalues \(1/12,1/4,1/6,1/6,1/6,1/6\).
Use P0 (no pre-reset pulse), the same H75 reset, then \(V_A=V(1/4,0)\) and positive site-0 readout. Exact probabilities:
\[
p_U=265/867,\qquad p_{\overline U}=313/867,\qquad p_O=1/3,
\quad p_U-p_{\overline U}=-16/289.
\]
It discriminates the *two specified* models provided \(\rho_\phi\)'s **signed imaginary coherence** is independently calibrated. Conjugating the source and initial phase together leaves all probabilities invariant. Therefore the assay is **conditional**, not a generation of an absolute phase reference from real operations or \(F\).

## Status and boundaries

- **EXACT (finite, conditional)**: complete linear identification in the fixed 18D model with 24 effects; strict subset-resource ranks; conditional positive phase-readout contrast.
- **OPEN**: certified preparation/phase standard, permission for P3's long pre-reset causal order, independent Kraus/port/readout calibration, numerical conditioning of the reduced 24-effect scheme, physical accessible states.
- **OPEN**: P6 frozen \(\mathcal J_N\) provenance, G2 physical origin, G3 noncircular generation by the generative map \(F\); KKS→ADM and Einstein gravity.
- The previously established native-15 GT–K4 metric descent NO-GO remains intact: this theorem changes the *registered operational access*, not the old native record.
- CI checks the fixed-catalog exact rank subsets using the actual previously certified PR #165 source/record matrix, strict positivity and rational phase-readout predictions. The separate complete local audit verifies **164 exact assertions** and regenerates all source response matrices. These are not equivalent CI scopes. No human-review, laboratory measurement, new general Lean theorem, CR-exclusive signature or full-P9 GR success is claimed.
