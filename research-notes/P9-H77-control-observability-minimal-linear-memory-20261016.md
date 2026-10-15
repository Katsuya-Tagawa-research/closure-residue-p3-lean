# H77 — Exact Control-Observability Filtration and the Minimal Predictive Linear Memory: 18 → 27 → 31 → 35 → 36

**2026-10-16 | P3–P11 Mathematical Bridge / Route A.** Stacked on H76 Draft PR #95 (**parent 89/89 GitHub CI PASS**). This stage uses the **identical** H75 six-dimensional, four-Kraus microscopic CPTP source with actual original P3 signed \(R_2=0\), \(R_3\neq0\), and H76's physical two-block flag observer \(\mathcal C_{\rm flag}\). The new result is an **exact finite algebraic algorithm and rational certificate for the memory required by a declared control-and-readout catalog**, including a surprising full 36-complex-dimensional observability result from **only real coherent flag rotation, classical flag feedback, and the two independent real P6-type site exchanges**. No extra complex phase knob is needed for this finite linear-observability result.

## H77.1 — finite control-observability theorem, with correct linear/CPTP separation

Let \(V\) be a finite-dimensional complex operator vector space (here \(V=M_6(\mathbb C)\), complex dimension 36), \(C:V\to Y\) a **fixed output observation linear map**, and let \(\{\mathcal T_j\}\subset\operatorname{End}(V)\) be a **physically specified catalog** of state-changing linear channels or quantum instrument branches. The catalog's finite words \(\mathcal T_w=\mathcal T_{j_k}\cdots\mathcal T_{j_1}\), including the empty word, are the processes for which one seeks exact prediction of the complete outputs \(C\mathcal T_w(X)\) for **arbitrary** microscopic \(X\in V\).

Define the largest jointly invariant subspace concealed by the initial observation,

\[
\boxed{
K_*=\bigcap_{w\in\mathcal T^*}\ker(C\mathcal T_w)
\subseteq\ker C.
}
\]

Equivalently, the following finite descending subspace iteration stabilizes:

\[
K_0=\ker C,\qquad
K_{n+1}=K_n\cap\bigcap_j\mathcal T_j^{-1}(K_n).
\]

The limit \(K_*\) is the **maximal subspace** contained in \(\ker C\) invariant under every catalog operation. Stabilization takes at most \(\dim V\) strict dimension reductions, hence at most 36 strict drops in this example. Dually, the span of all **Heisenberg-pulled output coordinate rows** \(C\mathcal T_w\) has rank

\[
\boxed{r_*=\dim_{\mathbb C}V-\dim_{\mathbb C}K_*.}
\]

**Predictive linear lower bound:** If any linear recording map \(R:V\to Z\) admits linear decoders \(D_w:Z\to Y\) with \(C\mathcal T_w=D_wR\) for all finite words, then \(\ker R\subseteq K_*\), and so **\(\operatorname{rank}_{\mathbb C}R\ge r_*\)**. Conversely collecting a basis of the Heisenberg-pulled output rows as linear readouts attains rank \(r_*\) as an **abstract linear sufficient statistic**. On its linear image the action is closed because \(K_*\) is invariant.

**Crucial CP caveat:** The constructed abstract quotient is **not** automatically a CPTP channel or positive state space, nor does algebraic sufficiency guarantee a physical single-shot measurement. When \(r_*=36\), a strong positive realization is trivial: **the identity quantum memory** \(R(X)=X\) and the actual declared CPTP microscopic operations on all of \(M_6\), with the already physical flag measurement at the end. When \(r_*=18\) for the flag-classical catalog, H76 already physically constructed the rank-18 CPTP conditional expectation. No CPTP output memory is asserted here for the intermediate abstract ranks 27,31,35.

The claim is quantified over **arbitrary initial six-level quantum states**, complete (tomographically determined) **two labelled conditional qutrit quantum-output blocks**, and all finite catalog words. It does **not** claim rank minimality for initial-state restrictions, scalar-only flag/site probabilities, a single undisturbed trajectory, finite-shot estimation, or a recorder that only predicts at reset-cycle endpoints rather than after arbitrary control words.

## H77.2 — exact 6×6 physical control catalog

Retain H76's original, already physically realized (conditional device) two-block observation

\[
\mathcal C_{\rm flag}(X)=P_0XP_0+P_1XP_1,\quad
\operatorname{rank}_{\mathbb C}\mathcal C_{\rm flag}=18,\quad
\operatorname{im}\mathcal C_{\rm flag}\simeq M_3\oplus M_3.
\]

The H75 original microscopic four-Kraus source \(\Phi_\mu\) has the genuinely nonzero unchanged P3 \(R_3\), and both \(\Phi_\mu\) and the physical H75/H76 visible control/noise branches preserve the flag-offdiagonal kernel **for the original restricted catalog**.

Define four specific **additional or existing** reversible physical 6×6 control operations:

1. \(F=|0\rangle\langle0|_E\otimes I_3+|1\rangle\langle1|_E\otimes S_{01}\). This is exactly H75/H76's **flag-conditioned site SWAP**, an independently specified physical *feedback* operation. It preserves the original flag-diagonal observer.
2. \(W=\begin{psmallmatrix}3/5&-4/5\\4/5&3/5\end{psmallmatrix}_E\otimes I_3\). This is exactly H76's **coherent real flag mixing unitary**. It is **not** a control derived from the original P3 residue, and expands H76's classically controlled device catalog.
3. \(V_A=I_E\otimes\operatorname{Cayley}(A,1/2)\), with \(A=E_{01}-E_{10}\). The exact site rotation matrix has cos \(3/5\), sin \(4/5\).
4. \(V_B=I_E\otimes\operatorname{Cayley}(B,2/3)\), with \(B=E_{21}-E_{12}\). It has cos \(5/13\), sin \(12/13\).

All four controls are **real orthogonal finite unitaries**, and the actual physical maps are \(\operatorname{Ad}_F,\operatorname{Ad}_W,\operatorname{Ad}_{V_A},\operatorname{Ad}_{V_B}\), hence genuine CPTP. The scalar orientation of A/B is exactly as in the preexisting H75 checker. The control-dependent statistics are computed **before** the flag-output observer, on separately prepared microscopic inputs. Applying Cflag at the end is a physical nonselective measurement with a quantum output block; its full matrix-element record requires experimental access to calibrated **quantum-block tomography**, not just the scalar joint flag/site population probability.

## H77.3 — exact finite observable-rank hierarchy

Let \(\mathscr O_{\mathcal S}\) be the complex span of all 18 coordinate rows of \(\mathcal C_{\rm flag}\) pulled back along finite words from the **listed reversible subcatalog \(\mathcal S\)**, including the empty word. All computations use rational coefficients and exact Gaussian-rational quantum-matrix definitions from H75/H76.

| Reversible subcatalog | Rank of all predicted quantum-block records | Rank by maximum word length (until stable) |
|---|---:|---|
| \(F\) only | **18** | 18 → 18 |
| \(W\) only | **27** | 18 → 27 → 27 |
| \(W,F\) | **31** | 18 → 27 → 31 → 31 |
| \(W,F,V_A\) | **35** | 18 → 27 → 31 → 34 → 35 → 35 |
| \(W,F,V_A,V_B\) | **36** | **18 → 27 → 31 → 35 → 36 → 36** |

The ranks **18,27,31,35,36 are exact complex-linear observability dimensions for the named reversible catalogs only**, not universal minima after adding arbitrary independently permitted nonunitary interventions. In particular \(\Phi_\mu\), arbitrary new flag instruments, postselection or all quantum effects are **not** silently inserted into the rank-31 or rank-35 catalog. Adding more actual physical operations can only increase observability rank, up to 36.

**Theorem H77.3 — full quantum operator memory is required for the expanded four-operation catalog.** The 36 ranks emerge already by control words of length **at most four**. Thus

\[
\boxed{
\bigcap_{|w|\le4,\; w\in\{W,F,V_A,V_B\}^*}
\ker\left(\mathcal C_{\rm flag}\circ\operatorname{Ad}_{U_w}\right)
=\{0\}.
}
\]

Consequently any exact **complex-linear** record that predicts all complete flag-resolved quantum-block outputs after every such finite control word must be **injective on \(M_6(\mathbb C)\)** and have rank 36. The full six-level identity CPTP quantum recorder is sufficient. For an output encoded exclusively as a \(d\)-dimensional quantum state, linear injectivity necessitates \(d^2\ge36\), hence \(d\ge6\); this is **not** a statement about minimal *physical* bits, qubits or arbitrary hybrid-algebra storage in less demanding protocols.

The exact checker implements **incremental Fraction Gaussian elimination** of Heisenberg-pulled **36-component** observable rows and produces every depth/rank in this table. No floating rank tolerances, inferred optimizer or approximate numerics are used. The table is *independently checked* against an exact symbolic rational prototype.

**Interpretation:** H76's one-bit classical flag memory is an exact CPTP solution when environment operations remain **flag-classical**. Once the device admits real **coherent** flag mixing along with flag-conditioned site feedback and the two independent real site exchange controls, the formerly invisible flag coherences can be transferred into the observed flag-quantum-block outputs. Because the rotation sites and conditional feedback do not commute, repeated control probes span the *entire* 36D microscopic operator space, not merely the 27D flag-symmetric sector. Importantly this full recovery requires **no extra calibrated complex/imaginary phase knob**—the microscopic operator algebra is complex even when the physical controls are real. This observability is a conventional-quantum-control result, not a uniquely CR-generated effect.

## H77.4 — the original P3 data cannot select the physical catalog

The original uncontrolled source \(\Phi_\mu\) and **every original P3 datum derived solely from it** are unchanged when we merely alter which **physical controls** the laboratory declares accessible. In particular the genuine original H75/H76 witness

\[
R_3(D,D)=\frac{i}{135}
\operatorname{diag}(-32,16,16,0,0,0)\neq0
\]

remains unchanged. With the flag-classical H76 control catalog (including \(F\), visible A/B controls, site-dephasing and CP flag/site instruments), the **rank-18 physical CPTP flag observer** is closed. With the physically expanded catalog admitting the **extra coherent flag rotation \(W\)**, the exact reversible subcatalog \(\{W,F,V_A,V_B\}\) already requires **rank 36** for arbitrary full six-level input states and complete block-quantum outputs.

Hence the **same uncontrolled P3 source and residue filtration** are compatible with physically different control catalogs with *different* exact predictive memory requirements. There is no map depending on \(\Phi_\mu\) **alone** that can correctly select the unique minimum operational memory for all these experimental catalogs without being told which controls are actually permitted. This is a rigorous **source-selection underdetermination** statement, not a universal prohibition on extending P3 by an additional, independently derived **generative control-accessibility axiom**.

This is a central Route-A distinction: success cannot merely be *existence* of CP memory, as H75/H76 already gave that; it requires explaining **why a particular physical control catalog is generated/selected by the theory**, not by the researcher choosing a favorable apparatus.

## H77.5 — audit status and exact next gate H78

| Requirement | H77 status |
|---|---|
| H75 exact 6D original-P3 nonzero source unchanged | Inherited and checked |
| H76 physical rank-18 flag observer closes for declared classical-flag control catalog | Inherited H76 EXACT |
| Catalog-dependent **minimum linear predictive observability rank** | EXACT rank ladder 18/27/31/35/36 |
| Extended coherent-flag + feedback + full real two-site-control catalog | EXACT rank36, by words length ≤4 |
| Reduced flag-classical observer works for this enlarged catalog | NO; complete original quantum coherence becomes observable |
| CPTP record with sufficient rank36 | YES trivially: full M6 quantum identity memory |
| Physically realized CPTP records with ranks27,31,35 | **NOT ESTABLISHED**; linear ranks are not CP source claims |
| Source-selected device catalog and observer from original P3 alone | **NOT ESTABLISHED**; same source permits distinct catalogs |
| CR-only observable, independently inherited frozen-P6 \(\mathcal J_N\), metric/ADM/HDA/Einstein | **NOT ESTABLISHED**; P9 Minimum Success remains unmet |

**H78 (recommended route-A gate):** formulate and verify a **minimal independent microscopic control-accessibility premise**—specified, for example, by a *fixed laboratory interaction Hamiltonian/Kraus dilation and switchable control ports*—under which the actual catalog can be deduced from hardware and the associated finite \(K_*\) constructed **without arbitrary intervention selection**. Then test whether the actual P3 hidden-flow and quadratic signed residues supply *additional* operational selection information beyond that ordinary quantum-control data. A strong success would give a nontrivial **source-to-device** map, not merely a catalog-conditioned observability theorem. Avoid merging H77's finite predictive-memory theorem into P9 as ADM/HDA or Einstein provenance: it is not.

**Verification:** \`python3 P3/P9H77ControlObservabilityMemoryRankExactCheck.py\` performs exactly rational Gaussian elimination and reuses H75/H76's true six-dimensional Kraus and P3 witness. This is a stacked **Draft/unmerged** finite research PR, without human peer review, Lean formalization, experimental confirmation, changed frozen manuscripts or P9 Einstein Minimum Success.
