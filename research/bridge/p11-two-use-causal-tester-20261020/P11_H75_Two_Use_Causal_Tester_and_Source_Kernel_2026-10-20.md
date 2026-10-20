# P11 G2/P6 — Two-Use H75 Causal Tester Separates Shallow Equivalence from Irrecoverable Source Kernel

**2026-10-20 | P3–P11 Mathematical Bridge | Stacked Draft on #178**

## Status and exact theorem claims

This audit uses the **original, unchanged** H75 four-Kraus source \(\Phi_\mu\) on \(\mathcal H=\mathbb C^2_E\otimes\mathbb C^3_S\), its original three site readouts \(Q_j=I_2\otimes|j\rangle\langle j|\), and a **separately authorized** site dephasing intervention \(\Delta\). The original map is used once or **twice** according to the declared schedule. The two uses are copies of the same finite CPTP map, with no retained source environment or additional memory port.

We distinguish three logically different statements:

1. **Shallow observational equivalence (EXACT):** for **all** six-level input operators \(X\) and each native site \(Q_j\), a *single source use followed by dephasing* is indistinguishable from one without dephasing:
   \[
   \operatorname{Tr}[Q_j\Delta(\Phi_\mu(X))]
   =\operatorname{Tr}[Q_j\Phi_\mu(X)].
   \]
2. **Two-use activation (EXACT):** if the same H75 source is run **again after the optional dephasing** and the final site outcomes are measured, one explicit physical input gives unequal, exactly rational probabilities:
   \[
   \operatorname{Tr}[Q_j\Phi_\mu^2(\rho_{00})]
   \ne
   \operatorname{Tr}[Q_j\Phi_\mu\Delta\Phi_\mu(\rho_{00})].
   \]
3. **True source-kernel erasure (EXACT for memoryless suffixes):** when two inputs already satisfy \(\Phi_\mu(\rho)=\Phi_\mu(\rho')\) as **complete density matrices**, no downstream fixed CPTP instrument, coherent control, reset repetition, adaptive classical protocol that accesses *only the same output system*, or POVM can distinguish them, provided no external retained system holds distinguishing correlations. This follows from linearity and composition; the 2-use activation in (2) does not contradict it.

Together these facts show: **equivalence relative to a restricted shallow readout is not a congruence under arbitrary authorized future interventions, whereas equality of the full state at a causal cut is.** This is ordinary Markovian quantum channel mathematics, **not** evidence of non-Markovian memory, a new P3 residue invariant, P6 physical implementation or a derived Einstein equation.

## 1. The exact original H75 source and the additional intervention

Reproduce without alteration
\[
K_{ab}=|a\rangle\langle b|\otimes U M_a,\quad
U=\operatorname{diag}(i,1,i)
\begin{pmatrix}
2/3&2/3&-1/3\\
-2/3&1/3&-2/3\\
-1/3&2/3&2/3
\end{pmatrix},
\quad
M_0=\operatorname{diag}(1,3/5,3/5),\quad
M_1=\operatorname{diag}(0,4/5,4/5).
\]
The CPTP condition \(\sum_{ab}K_{ab}^\dagger K_{ab}=I_6\) holds exactly. Denote the output quantum channel by \(\Phi_\mu(X)=\sum_{ab}K_{ab}XK_{ab}^\dagger\).

The optional **additional** intervention is dephasing in the original qutrit site basis,
\[
\Delta(Z)=\sum_{j=0}^2 L_j ZL_j^\dagger,\quad
L_j=I_2\otimes |j\rangle\langle j|.
\]
It is one-outcome CPTP with Kraus sum \(\sum_jL_j^\dagger L_j=I_6\). The three internal Kraus outcomes of the device are not separately read out. This is an independently supplied *Instrument port* in the AX-OA sense, not a port or timing permission derived from original H75, frozen P6 or F.

The three terminal effects are **original native** \(Q_j=L_j\), and form a complete POVM \(\sum_jQ_j=I_6\). All source runs and interventions are assumed **externally scheduled**, including the permission to insert \(\Delta\) between two source uses.

## 2. Theorem T1: one-use indistinguishability on all 36 input units

For every \(j\),
\[
\Delta^*(Q_j)=\sum_kL_k^\dagger Q_j L_k=Q_j.
\]
Therefore, for every \(6\times6\) input \(X\) (not only states in the 18D native domain),
\[
\boxed{\operatorname{Tr}[Q_j\Delta\Phi_\mu(X)]
=\operatorname{Tr}[Q_j\Phi_\mu(X)].}
\tag{T1}
\]
This equality is only of the three chosen terminal probabilities: \(\Delta\Phi_\mu(X)\) is **generally not** the same density matrix as \(\Phi_\mu(X)\), because the original H75 qutrit unitary \(U\) creates site coherences in the output.

T1 proves that \(\Delta\) is hidden by the *restricted one-use population tester*. It is not invisible to all possible complex phase-sensitive effects, or to every future causal program.

## 3. Theorem T2: exact two-use causal activation

Set \(\rho_{00}=|0,0\rangle\langle0,0|\), a valid native block-diagonal preparation. Compare two *fully specified* protocols with identical source and final readout:

\[
\mathsf P_{\mathrm{id}}:\quad
\rho_{00}\xrightarrow{\Phi_\mu}
\xrightarrow{\mathrm{id}}
\xrightarrow{\Phi_\mu}\xrightarrow{Q_j};
\qquad
\mathsf P_{\Delta}:\quad
\rho_{00}\xrightarrow{\Phi_\mu}
\xrightarrow{\Delta}
\xrightarrow{\Phi_\mu}\xrightarrow{Q_j}.
\]
All source uses are the same memoryless CPTP channel. The only difference is insertion of the genuinely nonunitary \(\Delta\) in the specified intermediate slot. Exact Born probabilities are
\[
\begin{array}{c|ccc}
 &Q_0&Q_1&Q_2\\\hline
\Phi_\mu^2&7/15&8/45&16/45\\
\Phi_\mu\Delta\Phi_\mu&11/27&8/27&8/27\\
\text{first minus second}&8/135&-16/135&8/135
\end{array}
\tag{T2}
\]
Every row sums to one; the difference row sums to zero. In particular:
\[
\boxed{\operatorname{Tr}[Q_1(\Phi_\mu^2-\Phi_\mu\Delta\Phi_\mu)(\rho_{00})]=-\frac{16}{135}\ne0.}
\]
Thus the intermediate dephasing is **not** equivalent to identity when tester programs permit a second source use before original native site readout. It is unnecessary to grant a new imaginary-phase-sensitive POVM for this witness: the original native \(Q_j\) suffice **when the new second source use and insertion schedule are granted**.

The exact checker verifies T1 on the 36 complex matrix units, computes both T2 distributions as simplified rationals from the true original Kraus matrices, and checks positivity/normalization, with no float rank or generic symbolic assumptions.

## 4. General exact Heisenberg tester closure criterion

For arbitrary CPTP \(\Phi\), CPTP intermediate \(\mathcal I\), and specified effect \(Q\), let \(\Phi^*\) and \(\mathcal I^*\) be the adjoint superoperators.

Single-use population equality for all input operators is equivalent to
\[
\Phi^*(\mathcal I^*(Q)-Q)=0.
\tag{S1}
\]
The stronger sufficient property \(\mathcal I^*(Q)=Q\) holds for the H75 site dephasing and original \(Q_j\). But with a second source, equality for all initial inputs becomes
\[
\boxed{\Phi^*((\mathcal I^*-\operatorname{id})\Phi^*(Q))=0.}
\tag{S2}
\]
The order of adjoints in S2 is essential: the new *future* source propagates terminal \(Q\) **backward** to the intermediate cut as \(\Phi^*(Q)\). The second use can make newly relevant effect directions that the shallow tester \(Q\) did not probe. Exact T2 implies S2 fails for at least one original \(Q_j\), even though S1 holds for all original \(Q_j\).

This suggests a relative **Heisenberg effect-space closure** test for any given, independently authorized future program family: choose an initial native effect span \(\mathcal R_0=\operatorname{span}\{Q_j\}\); repeatedly apply the adjoints of permitted future channels and controls, and ask whether the instrument acts identically on every effective effect **modulo the annihilator of the reachable source output space**. This is a proof obligation, not evidence of non-Markovian physical memory.

## 5. Theorem T3: irrevocable erasure at a true state cut

If \(\Phi_\mu(\rho)=\Phi_\mu(\rho')\) as **whole density matrices**, then for every fixed downstream CPTP channel \(\mathcal C\) (including any finite composition of source uses, controls and instruments) and terminal effect \(Q\):
\[
\boxed{\operatorname{Tr}[Q\mathcal C\Phi_\mu(\rho)]
=\operatorname{Tr}[Q\mathcal C\Phi_\mu(\rho')].}
\tag{T3}
\]
The same statement extends to ordinary adaptive *instruments* by linearity of every outcome branch, as long as the downstream protocol receives only that cut output and fixed program instructions; no input-dependent external memory or side-channel is allowed.

The original H75 has the exact pair
\[
X_{\mathrm{flag}}=\operatorname{diag}(-I_3,I_3),\qquad
\rho_{\pm}=I_6/6\pm X_{\mathrm{flag}}/12,
\]
with \(\rho_+\ne\rho_-\), both full-rank normalized positive and \(\Phi_\mu(\rho_+)=\Phi_\mu(\rho_-)\) because their flag partial traces are equal. The checker verifies the full output equality and at least the two repeated-source suffix distributions. **No "two-use resurrection" of a truly erased \(\Phi_\mu\)-kernel input direction is claimed or possible within this specified channel-only memoryless framework.**

The previously audited length-five **pre-source** coherent port word can distinguish \(\rho_\pm\); that intervention is applied **before** the first irrecoverable source cut, so T3 does not rule it out.

## 6. P6/P11 interpretation and strict transfer boundaries

**EXACT finite ordinary QM:** T1, T2, T3; original H75 full matrices and exact site probabilities; the general S1/S2 adjoint criterion; hidden intermediate dephasing can be revealed by a second authorized source use without exotic readout. These are mathematical *relative* operation-catalog results.

**Conditional assumptions:** actual permission to apply \(\Delta\), to insert it before a new source use, to restart/reuse the **same** ideal H75 CPTP source without uncontrolled environment memory, to prepare \(\rho_{00}\), and to perform original native site readouts. H75 as a mathematical map does not itself generate the 2-use scheduling controller. This is not a real hardware experiment.

**Still OPEN:** whether frozen P6's coherent observer/provenance permits those ports/schedules; a CR-specific signed hidden-current readout; \(\mathrm{GenAcc}_F\) intrinsic generation and physical access certificate selection; unique minimal AX-OA axioms; P3 process-tensor memory equivalence (explicitly **not** asserted); P7/P8 soldering, native GT–K4 descent, KKS→ADM/HDA/Einstein and P11 Generative Completeness. A standard Markovian CPTP channel already exhibits T2, so T2 alone is **not** a witness for non-Markovianity.

**Proof / status:** independent exact SymPy checker rebuilds original 4-Kraus H75, dephasing CPTP, all 36 one-use matrix-unit identities, exact two-use rational numbers and strict source-cut kernel erasure; dedicated CI. Draft/unmerged; no public/frozen manuscript changes, no human peer review or general Lean theorem.
