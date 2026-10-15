# H70 — Restricted-Code Quantum Recovery, Reflection-Twirl CPTP Closure and the Original P3 Residue Gap

**2026-10-16 | P3–P11 Mathematical Bridge → P9 GR-I.** H70 is stacked on H69 Draft PR #88 (**82/82 GitHub CI PASS**). It reuses precisely H42's original connected three-site rational unitary CPTP \(\Phi\), H46's 12-outcome CP quantum instrument \(C\), H68's 24-branch informationally complete randomized CP instrument \(\mathfrak I\), and H43's reflection parity twirl \(\mathcal E\). The objective is to find an honest restricted quantum memory, not to equate access to a full quantum-state estimator with a physical autonomous single-system observer.

## 1. The crucial distinction among three questions

1. **Quantum information recovery:** Given a state supported on a code \(P\mathbb C^3\), can a CPTP recovery \(\mathcal R\) invert the specified physical instrument \(\mathfrak I\) on *all* code states, including code coherences?
2. **Autonomous CPTP prediction:** Does a CPTP observer \(\mathcal E\) have a physical CPTP output channel \(\mathcal T\) satisfying \(\mathcal T\mathcal E=\mathcal E\Phi\), potentially even when \(\mathcal E\) cannot be inverted on all microscopic input states?
3. **Original P3 quadratic-residue sufficiency:** Does the observer's accessible current/future information determine the original signed nonlinear return \(\Delta_D([h_1(d),h_2(d')^\dagger])\) for the declared microscopic diagonal seeds?

These are distinct properties. H69 gave an informationally complete instrument failing CPTP autonomous closure. H70 shows **both a strong restricted-code No-Go for that instrument and a different positive lower-dimensional CPTP closure**, with a further failure to retain P3's signed quadratic residue.

## 2. H70.1 — NO exactly correctable qubit code for the fixed 24-branch H68 instrument

The original H46 12-branch instrument has CP outcome operators

\[
I_{k,t}(\rho)=\tfrac12D_k P^t\rho P^tD_k^\dagger,\qquad k=0,\ldots,5,\quad t=0,1,
\]

where \(P\) is the left-right reflection and the diagonal rational Kraus operators \(D_k\) are those of H46. H68's full 24-branch quantum-classical channel is

\[
\mathfrak I=\tfrac12 C\ \oplus\ \tfrac12 C\operatorname{Ad}_{U_A}.
\]

Its **arm-0** branch Kraus operators are \(K_{0kt}=\tfrac12D_kP^t\) (with orthogonal classical branch labels). Their effects

\[
F_{0kt}=K_{0kt}^\dagger K_{0kt}
=\tfrac14P^tD_k^\dagger D_kP^t
\]

are diagonal in the site basis. The **complex linear span of these twelve effects is ALL of the site diagonal algebra** \(D_3=\operatorname{span}\{E_{00},E_{11},E_{22}\}\). This is the independently audited H48 rank-three classical-probability fact; the H70 rational checker explicitly recomputes rank 3 of their output-probability vectors on the three site states, while proving the effects have no offdiagonal components.

Suppose any two-dimensional code projector \(P_C\) on \(\mathbb C^3\) admitted an exact CPTP left recovery \(\mathcal R\mathfrak I(\rho)=\rho\) for every density state supported in \(P_C\). The standard **whole-code Knill–Laflamme necessary condition** then requires

\[
P_C F_{0kt}P_C=c_{kt}P_C
\]

for each branch, including the arm-0 branches. Since their effect span is \(D_3\), we would have

\[
P_C E_{ii}P_C=\lambda_iP_C,\qquad i=0,1,2.
\]

But \(\operatorname{rank}(P_CE_{ii}P_C)\le1\), whereas \(\operatorname{rank}P_C=2\). Hence each \(\lambda_i=0\), and summing the identities implies

\[
P_C=\sum_iP_CE_{ii}P_C=0,
\]

a contradiction.

**Theorem H70.1 (instrument-specific exact qubit recovery NO-GO):**

\[
\boxed{\text{No two-dimensional quantum code in }\mathbb C^3
\text{ is exactly CPTP-recoverable from }\mathfrak I.}
\]

A one-dimensional known pure-state code is of course trivially recoverable by fixed state preparation. The no-go does **not** prevent ensemble tomography, classical inference, unmonitored extra quantum memory, an entirely different observation instrument, approximate code correction, or corrections on a suitably changed microscopic/source model. It also does **not** say that classical branch outcome probabilities are informationally complete on arbitrary qubit coherences; the point is that the classical effects disclose site populations and thus violate error-correction conditions for every candidate two-dimensional *quantum* code.

**Example within the candidate reflection-even code:** H68's arm-0 branch \(k=t=0\) effect \(\operatorname{diag}(1/4,9/100,0)\) compresses to **different** logical diagonal values \(1/8\) on \((|0\rangle+|2\rangle)/\sqrt2\) and \(9/100\) on \(|1\rangle\). This single branch already fails qubit KL for that code. The global theorem follows from the whole diagonal POVM span and excludes *every* rank-two projector, not just the parity code.

## 3. H70.2 — the same H42 microscopic channel HAS a genuine 5D CPTP observer closure

Let \(P\) be the actual H42 site reflection, \(P^2=I\), and write \(P_\pm=(I\pm P)/2\). They have ranks \(2\) and \(1\), respectively. Define the CP conditional expectation

\[
\mathcal E(X)=\tfrac12(X+PXP)
=P_+XP_++P_-XP_-.
\]

This is physically a coin-controlled mixture of two unitary operations (identity and reflection) and hence CPTP, trace preserving, unital and idempotent. Its range is a *-closed C*-subalgebra

\[
\operatorname{im}\mathcal E\cong M_2(\mathbb C)\oplus\mathbb C,\qquad
\boxed{\operatorname{rank}_{\mathbb C}\mathcal E=5}.
\]

The **same fixed H42 microscopic unitary** obeys \([U,P]=0\). Consequently,

\[
\boxed{\mathcal E\Phi=\Phi\mathcal E.}
\]

Set \(\mathcal T=\Phi\) as an honest CPTP quantum channel on the output 3×3 quantum system. Then

\[
\mathcal T\mathcal E=\mathcal E\Phi,
\]

so the **five-dimensional image algebra is an autonomous CPTP predictive state space** for the full unmeasured fixed \(\Phi\) dynamics. No globally invertible state-recovery map is required for this autonomous coarse dynamics: \(\ker\mathcal E\) has dimension 4, yet is invariant under \(\Phi\).

This symmetry-twirl fact was already in H43 and its five-dimensional predictive closure was in H44; H70 does **not** advertise it as a novel discovery. The novel H70 synthesis is the sharp comparison with H68's **complete** 24-arm instrument: having *more* informational rank (9 rather than 5) does NOT guarantee CP dynamics, whereas the less informative CPTP twirl does possess it. The correct compatibility condition depends on **how the observer records and disturbs the quantum information**, not on rank alone.

### A genuine nontrivial correctable parity-even qubit code, but for \(\mathcal E\), not \(\mathfrak I\)

On the rank-two subspace \(P_+\mathbb C^3\), \(\mathcal E\) acts identically. The same microscopic unitary preserves this code by \([U,P_+]=0\), with nontrivial coherent action (the center seed \(E_{11}\) evolves to a different coherent state).

Define an explicit quantum recovery on all input 3×3 operators,

\[
\mathcal R_+(Y)
=P_+YP_++\operatorname{Tr}(P_-Y)\,\frac{P_+}{2}.
\]

The first summand is a CP compression, and the second is CP measurement-and-preparation of the normalized parity-even maximally mixed state. Their combined trace is \(\operatorname{Tr}Y\), so \(\mathcal R_+\) is CPTP and

\[
\boxed{\mathcal R_+\mathcal E(\rho)=\rho}
\]

for **all** states \(\rho\) supported on the even 2D code. The checker verifies every code-projected matrix unit, its CPTP trace identity and code invariance under \(\Phi\) in exact Gaussian rationals.

This is a **nontrivial conditional standard-QM success** for *restricted-state quantum recovery*, while full-state recovery from \(\mathcal E\) remains impossible by its rank-five noninjectivity. Its physical reflection symmetry is **independently specified**, not inferred to be an accessible frozen-P6 hardware operation from original P3 hidden-flow.

## 4. H70.3 — an autonomous CP observer can STILL lose original P3 signed quadratic return

Take two distinct valid original **diagonal** P3 seeds \(d_0=E_{00}\), \(d_2=E_{22}\). Reflection twirling erases their odd distinction:

\[
\mathcal E(d_0)=\mathcal E(d_2).
\]

Because \(\mathcal E\Phi=\Phi\mathcal E\), it follows **for every nonnegative integer n** that

\[
\boxed{\mathcal E\Phi^n(d_0)=\mathcal E\Phi^n(d_2)}.
\]

Yet their genuine original P3 depth-three signed diagonal quadratic return differs. With \(h_1(d)=(1-\Delta_D)\Phi(d)\) and \(h_2(d)=(1-\Delta_D)\Phi^2(d)\), the **unchanged** original-P3 formula is

\[
R_{12}(d,d')=\Delta_D([h_1(d),h_2(d')^\dagger]).
\]

The fixed H42/H45 rational source yields

\[
\begin{aligned}
R_{12}(d_0,d_0)&=\frac{i}{81}\operatorname{diag}(-32,16,16),\\
R_{12}(d_2,d_2)&=\frac{i}{81}\operatorname{diag}(16,16,-32).
\end{aligned}
\]

These outputs are unequal even though **all** CP-twirl observable histories coincide. The checker reproduces both original signed residues exactly. The H45 bilinear formula attributes this to the missing parity-odd signed seed coordinate \(q=(d_{00}-d_{22})/2\), which the twirl discards.

**Theorem H70.3 (linear CPTP closure does not imply signed P3 residue sufficiency):**

\[
\boxed{\text{CPTP predictive Markovian closure of an observer}
\not\Rightarrow
\text{reconstruction of every original nonlinear P3 residue}.}
\]

This is a genuine boundary for P3→P6: closing observable linear dynamics is **not automatically enough** to reconstruct the generation's signed hidden-return filtration. It is not a CR-exclusive quantum anomaly, a new P6 physical observation, or a general minimum memory size theorem for arbitrary states. H44/H45 previously contained the relevant precursor; H70 combines it with the new qubit-recoverability restriction and clarifies the scope.

## 5. Full comparative verdict

| Fixed question | H68 24-branch \(\mathfrak I\) | H43 reflection twirl \(\mathcal E\) |
|---|---|---|
| Physical type | CPTP labelled quantum-outcome instrument (extra hardware) | CPTP symmetry conditional expectation (separately declared twirl) |
| Complex linear rank | 9 (informationally complete) | 5 (\(M_2\oplus\mathbb C\)) |
| Autonomous CPTP \(\mathcal T\) matching H42 \(\Phi\) | **NO** (H69 trace-distance witness) | **YES** (\(\mathcal T=\Phi\), covariance) |
| CPTP recovery on an arbitrary rank-two quantum code | **NO for every qubit code** (H70.1) | **YES for invariant even-parity qubit code**, not all codes |
| CPTP full-state recovery | NO (H68 KL) | NO (rank-five noninjective) |
| All-time observables determine original P3 \(R_3\) for all diagonal seeds? | No general sourcing theorem; informationally complete quantum-block stats can reconstruct density *offline* | **NO**: explicit \(d_0,d_2\) witness |
| Frozen P6 actual hardware and \(\mathcal J_N\) generated from P3? | OPEN | OPEN |

## 6. H71 research gate — operational source of CPTP symmetry memory

H70 establishes a **conditional existence** of nontrivial 5D CPTP predictive closure but reveals its strong dependency on physical reflection symmetry and on choosing a specific observer. H71 should seek (or rule out) a **microscopically sourced, actual P6-compatible CP conditional expectation** whose image remains invariant under *all physically allowed* coherent control and dephasing channels, not just the uncontrolled H42 unitary \(\Phi\). In particular H43 previously distinguished swap-covariant two-knob families from *pointwise invariant* controls; the former need not commute with the parity twirl. Test controls \(A,B\), their collective \(A+B\), and their antisymmetric \(A-B\) separately on the same nine matrix-unit basis. An odd controlled generator could break the equivariance of the apparently closed 5D observer, recovering H67's lesson that one control can reveal hidden memory. Keep physical control availability and source provenance separate.

For P9, a nontrivial CPTP observer closure does not derive a KKS→ADM symplectic map, 3D metric soldering, DeWitt negative kinetic, full off-shell HDA, or Einstein dynamics. P9 Minimum Success remains unmet.

**Verification:** \`python3 P3/P9H70RestrictedCodeCPTPTwirlResidueGapExactCheck.py\` recomputes the 3D diagonal POVM rank, reuses the unchanged H68 CP instrument, checks exact CP twirl/commutation and explicit rank-two code recovery on all nine input basis units, and independently evaluates two original signed P3 residue matrices. Exact analytic rank/KL/commutator proofs are given here. Draft/unmerged; frozen manuscripts/main untouched; no Lean formal proof, external human peer review or experiment.
