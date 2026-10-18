# H79 — Physical CPTP Predictive Memory at Mandatory Reset Checkpoints: A Five-Level, Rank-13 Recovery Construction

**2026-10-18 | P3–P11 Mathematical Bridge / Route A.** Stacked on H78 Draft PR #97 (**91/91 GitHub CI PASS**). This is an exact, reproducible finite quantum-information result for the **unchanged H75** four-Kraus microscopic \(6\)-level source with genuine original P3 \(R_2=0,R_3\neq0\), and with independently declared controls. It addresses the gap in H78 between the **complex-linear nine-dimensional post-reset source image** and an **actual completely positive predictive memory**.

The new result is a **strictly operational and causal-schedule-specific** physical quantum memory of five Hilbert levels, whose nontrivial block algebra has **complex linear rank 13**, admits explicit CPTP encoding and decoding and is exact at **mandatory reset checkpoints**, even when coherent environment rotations, flag-conditioned feedback and independent real 01/12 exchanges are used **between** those checkpoints. The result is NOT a proof of a rank-nine CPTP memory or a P3-derived physical control law.

## 1. Fixed source and an exact five-level reachable support

The microscopic Hilbert space and channel are **identical to H75**:

\[
\mathcal H_\mu=\mathbb C^2_E\otimes\mathbb C^3_S,\quad
\Phi_\mu(X)=\sum_{a,b=0}^1L_{ab}XL_{ab}^\dagger,\quad
L_{ab}=|a\rangle\langle b|_E\otimes UM_a,
\]

where \(U\) is the fixed nonreal original H42 three-site unitary and

\[
M_0=\operatorname{diag}(1,3/5,3/5),\qquad
M_1=\operatorname{diag}(0,4/5,4/5).
\]

The micro source resets the old flag at each application; \(\Phi_\mu\) has rank **nine as a complex-linear superoperator** and the original P3 six-level diagonal residue remains \(R_3(E_{00}^{(6)},E_{00}^{(6)})=i\,\operatorname{diag}(-32,16,16,0,0,0)/135\neq0\).

The output has a specific **physical support** that is stronger than the nine-dimensional source-image claim. Every \(\sigma=\Phi_\mu(X)\) is flag-block-diagonal and supported on the five-dimensional Hilbert subspace

\[
\boxed{
\mathcal K=
(|0\rangle_E\otimes\mathbb C^3_S)\ \oplus\
(|1\rangle_E\otimes U\,\operatorname{span}\{|1\rangle,|2\rangle\}_S).
}
\]

Reason: the flag-zero branch has full site support (\(M_0\) invertible); the flag-one branch \(UM_1\rho M_1U^\dagger\) is supported on the **two-dimensional** image of \(UM_1\), since \(M_1|0\rangle=0\). These ranges are orthogonal because their **environment flags** differ. Thus \(\dim\mathcal K=3+2=5\). The corresponding flag-block quantum algebra of output data is

\[
\boxed{\mathcal A_{3\oplus2}=M_3(\mathbb C)\oplus M_2(\mathbb C),\quad
\dim_{\mathbb C}\mathcal A_{3\oplus2}=9+4=13.}
\]

The exact checker constructs a six-by-five isometry \(V:\mathbb C^5\to\mathbb C^6\) whose first three columns are \(|0,j\rangle\), and last two are \(|1\rangle\otimes U|1\rangle\), \(|1\rangle\otimes U|2\rangle\). It verifies \(V^\dagger V=I_5\), \(P_{\mathcal K}=VV^\dagger\) is an orthogonal rank-five projection, and

\[
P_{\mathcal K}\Phi_\mu(X)=\Phi_\mu(X)=\Phi_\mu(X)P_{\mathcal K}
\]

on **all 36 six-level matrix units**.

## 2. H79.1 — a genuine rank-13 CPTP encoder with a physical recovery

Let \(P_0,P_1\) be the original mutually orthogonal rank-three environment flag projectors. Let \(|r\rangle=|1\rangle_E\otimes U|0\rangle_S\), the **one lost support mode**, so \(I_6-P_{\mathcal K}=|r\rangle\langle r|\). Choose a logical pure state \(|e_0\rangle\in\mathbb C^5\) supported on logical flag zero.

Define **three explicit Kraus operators** \(K_\ell:\mathbb C^6\to\mathbb C^5\):

\[
K_0=V^\dagger P_0,\qquad
K_1=V^\dagger P_1,\qquad
K_{\rm miss}=|e_0\rangle\langle r|.
\]

They satisfy

\[
\sum_{\ell=0,1,\mathrm{miss}}K_\ell^\dagger K_\ell
=P_{\mathcal K}+|r\rangle\langle r|=I_6.
\]

The encoder

\[
\boxed{\mathcal C_{13}(X)=\sum_\ell K_\ell X K_\ell^\dagger:
M_6\to M_5}
\]

is **CPTP on all six-level input states**, not merely on a special family. It discards flag coherences, compresses the two flag blocks to logical dimensions three and two, and sends any occupation of the unreachable mode \(|r\rangle\) to a fixed logical flag-zero state. Its output range is exactly the unital block algebra \(M_3\oplus M_2\) inside \(M_5\), of **complex-linear rank 13**, checked on all 36 matrix-unit inputs.

The physical decoder

\[
\boxed{\mathcal D_5(Y)=VYV^\dagger:M_5\to M_6}
\]

is an **isometric CPTP channel on all five-level inputs**. It follows that

\[
\boxed{
\mathcal D_5\mathcal C_{13}\Phi_\mu=\Phi_\mu
}
\]

on **all 36 microscopic matrix units**, hence on all physically prepared input states. This is a true quantum recovery on the **post-reset source-output family**, retaining conditional quantum coherences within both flag blocks. The environment flag is retained as a classical direct-sum label, without keeping the inaccessible flag-one mode.

H76's fully flagged physical observer had output operator-algebra rank **18** (\(M_3\oplus M_3\) in the original six-level carrier). H79 establishes a physically implemented **rank-13** alternative for the restricted reset checkpoint schedule; the logical **quantum Hilbert carrier has dimension five** rather than six. This is **not** a proof that rank13 is globally minimal or that the rank-nine source-output linear manifold itself has a CPTP encoding of operator rank nine.

## 3. H79.2 — genuine CPTP closed dynamics at each reset checkpoint

Take any physically allowed finite quantum unitary/control channel \(\mathcal G\) on the original six-level system, including H75/H76's independently specified real 01/12 exchange ports, coherent real flag rotation \(W\), their products, and flag-conditioned SWAP feedback \(F\). The mandatory *reset-scheduled* step is

\[
\mathcal S_{\mathcal G}=\Phi_\mu\circ\mathcal G.
\]

The controls may transiently take a state outside \(\mathcal K\) before the reset. **Measurements/observer checkpoints occur only after the next application of \(\Phi_\mu\)**. On the physical logical carrier define

\[
\boxed{
\widetilde{\mathcal S}_{\mathcal G}
=\mathcal C_{13}\circ\Phi_\mu\circ\mathcal G\circ\mathcal D_5
:M_5\to M_5.
}
\]

Every factor is physically CPTP; therefore this is a **genuine CPTP output dynamics**, not a nonpositive algebraic inverse. For any source-prepared post-reset state \(\sigma=\Phi_\mu(X)\), \(\mathcal D_5\mathcal C_{13}(\sigma)=\sigma\), so

\[
\boxed{
\mathcal C_{13}\mathcal S_{\mathcal G}(\sigma)
=\widetilde{\mathcal S}_{\mathcal G}\mathcal C_{13}(\sigma).
}
\]

The checker verifies this on the true physical reset outputs of all 36 microscopic basis operators and for a catalog of explicit rational \(6\)-level finite unitaries, including separate site exchange and coherent flag controls. It verifies multiple successive reset-checkpoint steps by induction and exact physical source decoding. Since \(\Phi_\mu\) once again prepares an output supported on \(\mathcal K\), the same identity holds after each cycle, **however many steps are composed**.

**What this does not say:** If the experimental observer needs predictions **at times between control and reset**, then the microstate can leave \(\mathcal K\) and \(\mathcal C_{13}\) need not be sufficient. H77's full rank36 observability bound for arbitrary six-level preparations and observation at arbitrary pre-reset control words remains valid. Likewise an experimenter using intermediate flag-coherent or hidden measurements must include that intermediate instrument in the observed process; it is not automatically covered by the reset-checkpoint theorem. This is precisely why **causal ordering and measurement times** are part of the correct microscopic memory definition.

## 4. H79.3 — physically positive quantum readout and a strict failure of the bare qutrit marginal

Because the decoder reconstructs **the exact physical post-reset six-level density operator**, any flag-resolved/site POVM (or complete labelled quantum-output block tomography) can be applied after decoding, and will produce its **exact original quantum probabilities and conditioned states on a single copy**. There is no negative-coefficient statistical inversion like H73. The checker verifies the equality of all six flag-site matrix-diagonal probabilities for all actual source-prepared output basis operators.

One must still **not** identify rank-nine complex source input information with an immediately reversible **3-level partial trace**. Consider the traceless Hermitian qutrit input difference

\[
\Delta=E_{00}-E_{11}+E_{01}+E_{10},
\qquad
\rho_\pm=I_3/3\pm \Delta/12.
\]

Both \(\rho_\pm\) are positive, normalized qutrit states: the nontrivial 2×2 eigenvalues are \(1/3\pm\sqrt2/12>0\). The actual joint flag-state difference after the micro preparation is \(\Phi_\mu(|0\rangle\langle0|_E\otimes\Delta)\). Its two orthogonal flag blocks have trace norms adding to

\[
\left\|\Phi_\mu(|0\rangle\langle0|_E\otimes\Delta)\right\|_1
=\frac{\sqrt{2056}+16}{25}.
\]

By contrast, the visible-qutrit-only partial trace has

\[
\left\|\operatorname{Tr}_E\Phi_\mu(|0\rangle\langle0|_E\otimes\Delta)\right\|_1
=\frac{2\sqrt{34}}{5}.
\]

The inequality is **strict**, for instance \(\sqrt{2056}>45\) and \(10\sqrt{34}<59\), hence \(\sqrt{2056}+16>61>59>10\sqrt{34}\). Since all quantities scale by the same positive factor for the bona fide density-state pair \(\rho_\pm\), the trace-distance contraction forbids the existence of any **CPTP recovery from the bare qutrit partial trace back to the entire physical post-reset joint flag quantum state on this full input family**. This pinpoints the limitation that H78's nine-dimensional linear statistic left unresolved.

This does **not** show that **every conceivable** 3-level physical CPTP encoding fails to be sufficient on the reset-image family. The negative theorem applies to the **specific natural qutrit marginal** \(\operatorname{Tr}_E\). Our rank13 positive construction is a sufficient example; global physical optimality remains open.

## 5. Precise status and H80 research gate

| Exact statement | Verdict |
|---|---|
| Unchanged H75 microscopic nonzero original signed P3 \(R_3\) | Inherited exact, source untouched |
| Mandatory reset outputs supported on a **5D physical Hilbert subspace** | **EXACT** |
| Physical 5-level, **rank13** CPTP block-memory encoder \(M_6\to M_5\) | **EXACT**, explicit 3 Kraus |
| Physical CPTP decoder reconstructs every post-reset microscopic state | **EXACT** |
| Closed CPTP dynamics through arbitrary declared inter-checkpoint controls **followed by mandatory reset** | **EXACT**, with causal schedule |
| Exact flag/site quantum readout at reset checkpoints | **EXACT** via isometric decoder |
| Bare visible qutrit marginal sufficient as a CPTP recovery of the full post-reset quantum flag state | **NO-GO**, positive density trace-distance witness |
| Minimal CPTP memory on post-reset family has *exact* rank 9 or 13 | **OPEN** |
| Intermediate pre-reset time output fully predicted by rank13 logical memory | **NOT CLAIMED** |
| P3-only generation of control port, device, causal reset schedule, frozen P6 \(\mathcal J_N\) | **OPEN** |
| CR-only signature; physical P7/P8 metric soldering; ADM/HDA/Einstein | **OPEN**; P9 Minimum Success remains unmet |

**H80 recommendation:** Attempt a rigorous **operational sufficiency/physical optimality classification** of the entire family \(\mathcal J_{\rm out}(\rho)\): can any smaller CPTP encoding than the explicit \(M_3\oplus M_2\) block memory recover all post-reset states, or do the complementary channel / Petz sufficient subalgebra obstruct compression to a 3- or 4-level quantum carrier? Separately check an explicit bounded-control dilation and intermediate observations; if physical operations allow pre-reset coherence probes, the small checkpoint memory alone is insufficient. Keep observer source provenance independent of P3 signed residue unless independently proved.

**Reproduce:** \`python3 P3/P9H79ResetCheckpointCPTPMemoryExactCheck.py\`. This uses the frozen H75 true six-level Kraus and original signed residue source without modification, builds all rectangular Kraus matrices and checks all 36 micro basis elements, exact CP recovery and multi-reset dynamics, exact operator ranks and positive-state no-go. Draft/unmerged; no human peer review, Lean formalization, experiment, frozen manuscript modification or claim of new quantum physics.
