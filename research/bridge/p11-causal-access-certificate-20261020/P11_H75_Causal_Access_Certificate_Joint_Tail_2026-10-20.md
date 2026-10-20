# P11 Phase 4 — Typed Causal Access Certificate: H75 Adaptive Prediction and Joint Uniform History Tail

**2026-10-20 | P3–P11 Mathematical Bridge | Stacked Draft on PR #182**
**Governance:** exact finite conditional mathematics only; no main/frozen manuscript changes. The OA-G39–G42 Uniform History-Tail audit remains UNNUMBERED and UNMERGED on its independent audit branch; this new bridge package does not replace or silently merge that independent audit.

## 1. Certificate schema and logical gates

A **relative, typed causal access certificate** is a tuple
\[
\mathsf{CAC}=(\mathcal H,\mathcal C,\mathcal P,\mathcal G,
\{\mathcal I^{(c)}_j\}_{c,j},\mathsf{policy},\mathsf{readout},
R_\infty,\mathsf N,b,\ell,\varepsilon,K,\mathsf{provenance}).
\]
Here \(\mathcal H\) is physical quantum source space; \(\mathcal C\) an externally authorized classical controller; \(\mathcal P\) legal preparations; \(\mathcal G\) declared *future* CPTP/branch alphabet; each \(\mathcal I^{(c)}_j\) is a selective CP trace-nonincreasing branch with sum CPTP; policy maps obtained outcome labels/controller states to next admissible operations; readout contains legal terminal effects; \(R_\infty\) is the invariant future Heisenberg span **relative to that grammar**. \(\mathsf N\) is the set of *no-event cycle maps*, and \(b,\ell,\varepsilon,K\) specify a *joint*, schedule-aware tail bound. Provenance names which permissions, source reuse, scheduling and error semantics were imported versus actually F-derived.

The certificate's verifier MUST keep separate:
1. **Finite predictive closure:** exact rank/stabilization of the Heisenberg effect span for the declared alphabet, including labelled CP branches.
2. **CP realization:** Kraus/Choi positivity and trace normalization for each instrument/controller state; legal preparation and readout cones.
3. **Joint uniform history-tail:** an explicit bound valid for **all legally admitted adaptive no-event switching schedules**, not merely for each fixed instrument separately.
4. **Archive semantics:** a tail cutoff is not a claim that all event times can be exactly retained by a bounded archive, and a 2-state policy controller is not an event-time archive.
5. **Physical access provenance:** existence of the mathematical circuit never implies the necessary apparatus is generated from the Generative Map F.

This is a **candidate certificate interface**, not a unique minimal axiomatization or theorem that F produces it.

## 2. Original H75 finite data — no surrogate source

Keep the actual original four-Kraus source on \(\mathcal H=\mathbb C^2_E\otimes\mathbb C^3_S\):
\[
K_{ab}=|a\rangle\langle b|\otimes U M_a,\quad
U=\operatorname{diag}(i,1,i)
\begin{pmatrix}2/3&2/3&-1/3\\-2/3&1/3&-2/3\\-1/3&2/3&2/3\end{pmatrix},
\quad M_0=\operatorname{diag}(1,3/5,3/5),\
M_1=\operatorname{diag}(0,4/5,4/5).
\]
Let \(L_j=I_2\otimes|j\rangle\langle j|\). The previously constructed selectively labelled **two** three-outcome instruments are
\[
\mathcal I^A_j(X)=L_jXL_j,\quad
\mathcal I^B_j(X)=J_jXJ_j^\dagger,
\]
\[
J_0=(L_0+L_1)/\sqrt2,\quad
J_1=(L_0-L_1)/\sqrt2,\quad J_2=L_2.
\]
Each is a physical CP instrument, and their nonselective sums coincide with site dephasing \(\Delta\) on **all** 6x6 inputs. Their selective branches are **not** interchangeable when outcome-dependent feed-forward is available (PR #181).

Use original registered real flag-conditioned site SWAP
\[
F_{\rm fb}=|0\rangle\langle0|\otimes I_3+
|1\rangle\langle1|\otimes(|0\rangle\langle1|+|1\rangle\langle0|+|2\rangle\langle2|).
\]
The **externally authorized** cycle for policy \(c\in\{A,B\}\) is: one original source use \(\Phi_\mu\), then instrument c, and, if outcome j=0, original \(F_{\rm fb}\) feedback before continuing. Outcomes j=1,2 terminate the no-event run. For the CP branches of a cycle:
\[
V^c_{j,ab}=W_j M^c_j K_{ab},\quad W_0=F_{\rm fb},\quad W_1=W_2=I_6,
\quad M^A_j=L_j,\quad M^B_j=J_j.
\]
For each fixed c, \(\sum_{j,a,b}(V^c_{j,ab})^\dagger V^c_{j,ab}=I_6\), so this is a genuine CPTP quantum instrument with selected no-event CP branch
\[
\mathcal N_c(X)=\sum_{ab}V^c_{0,ab}X(V^c_{0,ab})^\dagger.
\]

## 3. New theorem: uniform tail under arbitrary A/B switching (EXACT)

The previous #182 audit obtained
\[
\mathcal N_A^*(I_6)=I_2\otimes
\begin{pmatrix}
4/9&4/15&-2/15\\
4/15&4/9&-2/9\\
-2/15&-2/9&1/9
\end{pmatrix}=I_2\otimes A.
\]
The eigenvalues of A are exactly \(0,\frac12-\frac{\sqrt{745}}{90},\frac12+\frac{\sqrt{745}}{90}\), so \(\mathcal N_A^*(I_6)\prec(5/6)I_6\). Its Sylvester principal minors for \((5/6)I_3-A\) are \(7/18,649/8100,31/1944\), all positive.

**New B certificate:** Since the B result-0 POVM effect is
\[
J_0^\dagger J_0=\tfrac12(L_0+L_1)=\tfrac12(I_6-L_2),
\]
the unital Heisenberg source map yields
\[
\mathcal N_B^*(I_6)
=\Phi_\mu^*(J_0^\dagger J_0)
=\tfrac12\big(I_6-\Phi_\mu^*(L_2)\big)
\preceq \tfrac12 I_6.
\]
(The conditional unitary feedback does not change trace and hence does not change this one-cycle no-event effect.) Thus both policy choices have the **common full-state one-cycle bound**
\[
\boxed{\mathcal N_c^*(I_6)\preceq bI_6,\quad
c\in\{A,B\},\quad b=5/6<1.}
\tag{CAC-Tail}
\]

**Switching theorem (EXACT):** Let \(c_1,\dots,c_n\) be **any legal predetermined or adaptively selected** A/B choices along a no-event history, possibly determined by a finite authorized classical controller and the earlier permitted outcome record. For every density input \(\rho\),
\[
\boxed{
\operatorname{Tr}\left[\mathcal N_{c_n}\circ\cdots\circ
\mathcal N_{c_1}(\rho)\right]
\le (5/6)^n.
}
\]
*Proof:* any CP trace-nonincreasing \(\mathcal N\) preserves the positive operator ordering of the adjoint: \(0\preceq X\preceq tI\Rightarrow0\preceq\mathcal N^*(X)\preceq t\mathcal N^*(I)\preceq tbI\). Apply this to the adjoints of the successive permitted cycles, inductively. This argument is **uniform in switch order** and hence applies also to an adaptively selected allowed policy. No commutativity between the two no-event CP branches is assumed.

For a fixed error tolerance \(\varepsilon=1/100\), the rational inequalities
\[
(5/6)^{25}>1/100\ge(5/6)^{26}
\]
give a conservative **common** tail cutoff \(K=26\), independent of total possible event history length and A/B switching pattern. This is a **tail/survival cutoff**, not the exact archive dimension or a proof of optimality.

The previous #182 2-state scheduling NO-GO remains valid: *separate fixed-policy multi-step extinction* can fail to give any switching bound. Here the stronger **common one-step** certificate does hold, so the NO-GO's premise differs.

## 4. A genuine two-state classical controller realization (EXACT)

A separate **assumed** classical policy bit \(c\in\{0,1\}\) alternates A/B each cycle and flips after each branch; it can be modelled as two block-diagonal copies of the original 6D quantum system, mathematically embedded in \(\mathbb C^2_C\otimes\mathbb C^6\). Its selective Kraus operators are
\[
\widehat V^{(c)}_{j,ab}
=|1-c\rangle\langle c|_C\otimes V^{(c)}_{j,ab},
\]
with \(c=0\) using A and \(c=1\) using B. Exact finite completeness is
\[
\sum_{c,j,a,b}(\widehat V^{(c)}_{j,ab})^\dagger
\widehat V^{(c)}_{j,ab}=I_{12}.
\]
The augmented no-event effect is the block diagonal operator
\[
\widehat{\mathcal N}^*(I_{12})
=\operatorname{diag}\!\left(\mathcal N_A^*(I_6),
\mathcal N_B^*(I_6)\right)\preceq(5/6)I_{12}.
\]
Thus a concrete finite-state *controller* realizes the common tail bound. This is **not** an exact archive of all past event times and does **not** show that the original H75 source generates a controller bit or clock.

## 5. Compatibility with finite adaptive predictive closure

In the already independently checked #182 future alphabet (source Phi, unobserved Delta, six A_j/B_j labelled feedback CP branches), the *un-normalized* Heisenberg effect spans have exact ranks
\[
\dim R_n=(3,7,10,12,12)\quad(n=0,1,2,3,4).
\]
Their exact 12D final quotient on all Herm(6) input operators is **relative to that alphabet**; the complement has 24 real linear directions. On the true original H75 source-output image the corresponding restricted response rank is 9, with no resurrection of a source-erased input direction. The companion CI **also reruns the existing #182 rank/checker** before checking the new A/B joint-tail certificate, so the two proven legs are version-locked at this stacked commit.

Hence the finite mathematics legitimately gives the **three-way conditional package**:
\[
\boxed{\text{finite adaptive predictor}
+\text{CP-selective realization}
+\text{joint, schedule-uniform tail bound}.}
\]
None of these asserts that a physically faithful AX-OA access schedule or the classical controller arises from F, that the whole infinite event-time archive is bounded, or that this is the original P3 quadratic Closure–Residue filtration.

## 6. Exact audit obligations and nonclaims

**Audit passes:** true original H75 Kraus, 36 complex matrix-unit equality of A/B nonselective CPTP, each selective instrument Kraus trace completeness, one-cycle A/B dual effects and strict common 5/6 bound, full 12D controller CP normalization, analytic induction for all switched no-event words, exact 1% cutoff, and #182 finite adaptive effect rank and source-output compatibility.

**Explicit independent assumptions:** source implementation/provenance; valid physical A and B instrument ports, their outcome labels and retention, clock and legal future re-use/schedule, branch-dependent real SWAP, classical controller/policy and event error interpretation. The bounded tail is true only for no-event sequences obeying these allowed source–instrument cycles. Adding arbitrary idling or uncontrolled waiting with no-event labels invalidates a naïve all-schedules conclusion.

**OPEN:** F→AX-OA physically faithful generation, unique axiom minimality, P6 observer and signed current provenance, original P3 residue / process tensor relation, infinite exact history archive, KKS→ADM/HDA/Einstein, P11 Generative Completeness and P12. Neither hardware feasibility nor human peer review, a new CR-specific physical prediction, or a universal Lean formalization is established. All PRs Draft/unmerged; no P1–P8 manuscript change.
