# H113 — The H112 Causal-Break Memory Witness Has an Exact Classical Flag-Feedback Implementation; Energy Conservation and Autonomous Control Are Independent Gates

**2026-10-19 | P3–P11 Mathematical Bridge / P5 history / P6 observer & causal response / P9 GR-I / P11 AX-SRC/OA/CAN**

**Inherited H112 Draft PR #131, 125/125 ALL GitHub CI PASS verified with both pages.** Preserve all genuine H75 four-Kraus six-level CPTP source, true original signed P3 \(R_3\), site A/B control permissions and source flag/site observables, and published/frozen P1–P8 and main. Do not add another arbitrary link or identify the unrelated P9.126–128 Cartan 16/48D unitary sources with H75. All results below are exact finite rational-algebra claims about the given microscopic instruments, with physical execution still subject to explicit control permission.

## H113.1 — The a-output flag is ALREADY a directly readable H75 classical record (EXACT)

Original H75 has genuine Kraus blocks
\[
L_{ab}=|a\rangle\langle b|_{\rm flag}\otimes UM_a,\quad
M_0=\operatorname{diag}(1,3/5,3/5),\
M_1=\operatorname{diag}(0,4/5,4/5).
\]
Denote output-flag projectors \(P_a=|a\rangle\langle a|\otimes I_3\). For EVERY input \(X\in M_6\) (not just a positive selected state),
\[
\boxed{
P_a\Phi(X)P_a=\sum_{b=0}^1 L_{ab}XL_{ab}^\dagger,\qquad
\operatorname{Tr}[P_a\Phi(X)]=p_a(X)=\sum_b\operatorname{Tr}(L_{ab}XL_{ab}^\dagger).
}
\tag{H113-FLAG}
\]
The output is exactly BLOCK DIAGONAL in a; the existing P_a measurement causes **no additional quantum backaction on the already-produced H75 output density**. This is a particularly important fact missed by treating the older 4D Stinespring environment as the only possible carrier of a.

If a physical controller saves this measurable output a-bit before the H112 full-system causal break, its later use DOES NOT REQUIRE accessing the Stinespring environment itself. The flag measurement is already a positive observer of the original H75 mathematical device; **the delayed storage, triggering/feedback controller and its clock are nevertheless additional operational assumptions**, unless independently evidenced by the source apparatus. A separate 4D minimal pure environment is still required for the H110 one-step Stinespring realization; it does NOT mean four classical bits or a 4D quantum memory is necessary for THIS response.

## H113.2 — Classical delayed feedback produces EXACTLY the H112 fixed-history system response (EXACT CONDITIONAL, every input)

Use the SAME H112 complete causal break \(\mathcal B(Z)=\operatorname{Tr}(Z)\tau\), \(\tau=|0_{\rm flag},1_{\rm site}\rangle\langle0,1|\), and unchanged existing H75 site-B Cayley pulse \(R_B\) (unitary \(R_6=I_{\rm flag}\otimes R_B\)). Define only a **conditional delayed controller**:
\[
a=0\Longrightarrow I_6,\qquad
a=1\Longrightarrow R_6.
\]
One first applies the TRUE original H75 \(\Phi\), reads P_a and records the a-bit classically, fully discards/reprepares the system into \(\tau\), drives \(I\) or the original B pulse according to the stored a-bit, and finally applies the **unchanged** second \(\Phi\). Summing unobserved a outcomes gives
\[
\boxed{
\mathcal T_{\rm classical}[\mathcal B](X)
=\sum_a \operatorname{Tr}(P_a\Phi(X))\Phi(R_a\tau R_a^\dagger)
=p_0(X)\Phi(\tau)+p_1(X)\Phi(R_6\tau R_6^\dagger)
=\mathcal T_{\rm H112\ coherent}[\mathcal B](X).
}
\tag{H113-CLASSICAL}
\]
The exact checker audits equality for **ALL 36 true original M6 operator basis units**, by three independent routes (native P_a instrument, four genuine Kraus probabilities, and full 24D older-environment controlled unitary from H112). Thus H112's operational \(256/625\) causal-break witness can be instantiated with a **single retained classical a-bit** and the existing B pulse, if the classical delayed feedback controller is independently granted.

The original coherent Stinespring environment density after the first channel is already **block diagonal in its outgoing a-sector**:
\[
\operatorname{Tr}_{S}[VXV^\dagger]_{(a,b),(a',b')}=0
\quad(a\ne a'),
\tag{H113-A-DECOHERENCE}
\]
because the \(L_{ab}\) output system flag sectors are orthogonal. Thus, after a complete system break, DEPHASING the environment in a has no further effect for any original H75 input. The H112 coherent controlled-\(B\) unitary and classical a-measurement/feedforward **are indistinguishable in their resulting full system process for this source preparation class**. This does NOT assert that general quantum environment memory and classical feedback are the same resource.

**Operational conclusion:** H112 demonstrates **past-to-future memory** across a system causal break for its augmented process, but does NOT establish an **irreducibly quantum** non-Markov mechanism. The temporal dependence can be carried by one bit of ordinary classical history. A classical Markovian embedding of the augmented process, retaining that bit as part of the enlarged current state, is straightforward; a memory-bearing process can be non-Markov on the reduced system while Markov on system+controller.

## H113.3 — Independent control Lie obstruction: native local controls never synthesize the H112 coherent conditional G (EXACT SCOPED NO-GO)

H75's inherited original local site Hamiltonians act on **system ONLY**: any control sequence has generator \(I_{4,\rm old}\otimes H_S(t)\) on old 4D ancilla + system 6D, and optional ancilla-only Hamiltonians contribute \(K_E(t)\otimes I_6\). All commute across the bipartition:
\[
[K_E\otimes I_6,I_4\otimes H_S]=0.
\]
Hence even arbitrary time-dependent sequences exponentiate to **product unitaries** \(W_E\otimes W_S\), never an old-a-controlled system gate.

For the SAME H112 target
\[
G=P^{\rm old}_0\otimes I_6+P^{\rm old}_1\otimes R_6,\quad R_6\ne e^{i\phi}I_6,
\]
\(G\) has operator Schmidt rank TWO and is NOT a product. A fully explicit source-labelled witness: for **an independently prepared coherent old-register superposition**
\[
|\chi\rangle=(|00\rangle+|10\rangle)/\sqrt2,\qquad
|\psi\rangle=|0_{\rm flag},1_{\rm site}\rangle,
\]
\(G|\chi,\psi\rangle\) has Schmidt rank two, because \(|\psi\rangle\) and \(R_6|\psi\rangle\) have overlap \(3/5\); the reduced state purity is exactly
\[
\boxed{\operatorname{Tr}\rho_{\rm old}^2=(1+(3/5)^2)/2=17/25<1.}
\tag{H113-ENT}
\]
Such an old a-coherent register state is NOT produced by the actual H75 environment AFTER tracing/discarding the original system (H113.2); this witness is an **operator-theoretic nonfactorization test**, not a claimed H75 positive accessible preparation.

A **classical** delayed controller evades this coherent local-unitary no-go because its category includes **measurement, record storage and classical communication to a later control**, not merely isolated unitary products. It reproduces the reduced H112 response without implementing the coherent G on arbitrary history/system superpositions. Therefore "**B is locally permitted**" does NOT alone imply "**coherently controlled G is source-generated**", while fixed classical feedback is a strictly weaker explicitly specified implementation adequate for this witness.

## H113.4 — Exact energy-selection boundary for the ACTUAL H112 returned B pulse (EXACT, scoped)

Assign a **DECLARED TEST** nondegenerate system site Hamiltonian
\[
H_S=I_{\rm flag}\otimes\operatorname{diag}(0,\epsilon_1,\epsilon_2),
\quad \delta=\epsilon_2-\epsilon_1,
\tag{H113-ENERGY}
\]
and let the preserved original 4D history record have any **diagonal a-controlled** energy \(H_E\) commuting with old \(P^{\rm old}_{0,1}\). No such Hamiltonian was selected by original H75/P3/F: this is a hypothesis specifying what "energy conservation" means on the inter-collision RETURN GATE.

For the H112 target \(G=P^{\rm old}_0\otimes I+P^{\rm old}_1\otimes R_6\),
\[
[G,H_E\otimes I_6+I_4\otimes H_S]
=P^{\rm old}_1\otimes[R_6,H_S].
\]
The actual rational SO(3) Cayley rotation satisfies \(|(R_B)_{21}|^2=16/25\). Thus
\[
\boxed{
[G,H_{\mathrm{total}}]=0\quad\Longleftrightarrow\quad
\epsilon_1=\epsilon_2\quad\text{(within this diagonal-energy class)}.
}
\tag{H113-ENERGY-NOGO}
\]
In particular with the **declared test** \((\epsilon_1,\epsilon_2)=(1,2)\), the controlled old-memory return violates strict autonomous total-energy preservation when the history bit is required to remain unchanged: it transfers energy into the system 1→2 component, and old history a-energy stays fixed. For the same H112 source-positive two histories,
\[
\boxed{
\langle\Delta H_S\rangle_{\rho^{(0)}}=0,\quad
\langle\Delta H_S\rangle_{\rho^{(1)}}=
p_1(\rho^{(1)})\frac{16}{25}(\epsilon_2-\epsilon_1)
=\frac{256}{625}\,\delta.
}
\tag{H113-WORK}
\]
This is work/energy exchange **during the RETURN GATE ONLY**, BEFORE the final H75 channel. H75's fixed complex U need not conserve this declared \(H_S\), and we do NOT claim the entire two-step open protocol conserves site energy.

**Positive boundary:** For an equally declared degenerate site1/2 Hamiltonian \(\epsilon_1=\epsilon_2\), the SAME \(G\) is exactly energy-conserving across the old-memory-return step. Thus energy conservation alone does NOT universally forbid memory return. It still does not synthesize G from system-only A/B pulses; an independently implementable controlled interaction (or classical measurement/feedforward with suitable work accounting) is needed.

**No-Go scope:** History a is held fixed by G, and \(H_E\) is block-diagonal in a. A different old quantum battery state, a register-changing exchange Hamiltonian, external power/control, or a different physically sourced system Hamiltonian may evade the energy obstruction. None of those resources is demonstrated by H75, so do not promote "need an energy battery" to a universal theorem.

## H113.5 — P5/P6/P9/P11 handoff and explicit stop rule

| Gate | Status |
|---|---|
| AX-SRC original H75 classical output a-bit and native B control | EXACT mathematical source operations |
| AX-OA H112 causal-break output reproduced with ONE classical retained bit | EXACT conditional feedforward, additional controller timing/permission |
| AX-CAN coherent old history→system G generated from isolated local controls | NO-GO (operator Schmidt and control algebra) |
| Energy conservation of coherent G for \(\epsilon_1\ne\epsilon_2\), unchanged history bit | NO-GO under declared Hamiltonians |
| Energy conservation of G with \(\epsilon_1=\epsilon_2\) | CONDITIONAL algebraic consistency, still not source-generated |
| An irreducibly **quantum** old environment memory experimentally detected in H112 | NOT ESTABLISHED; classical feedback simulates whole tested process |
| P5/Ω generated nonclosure-return from original P3 residue | OPEN |
| P9 16D/48D unitary Cartan physical source equivalence, spatial solder/torsion/ADM | OPEN |
| AX-DYN/NORM/GEN source-derived Einstein dynamics and F completeness | OPEN |

**Next genuine priority:** Require an explicitly physical old-history controller and **energy/control model**, or demonstrate a **quantum-specific multi-time intervention witness that no classical record/feedback process can simulate**. Do NOT add more arbitrary return gates or claim sourced Einstein GR. A classically executable conditional source protocol is a useful concrete P6 causal memory *operational example*, but not a theorem of P5 Ω or P11 F. The original source and all freeze status are preserved.

**Reproducibility:** exact Gaussian-rational 4 Kraus/36 M6 native flag measurements, exact old-environment off-a coherence null, old G vs measured classical feedback, all positive H112 causal-break probabilities, exact coherent G Schmidt-rank witness and degenerate/nondegenerate source energy commutators, dedicated regression GitHub CI; no human referee or laboratory data.
