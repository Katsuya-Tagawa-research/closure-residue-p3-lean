# P9 H26 — No-Go for reconstructing cell-edge holonomy from cell-local CR data alone

**2026-10-14.** Exact-rational finite mathematical audit, stacked on H25 Draft #43. The checker reuses H24's exact rational Gaussian CPTP/P3 witness, so it does **not** quietly replace P3's original quadratic residue with a Lie commutator. Frozen P3 and main remain unchanged. Not Lean kernel proof, not experimentally calibrated P6 access, not Levi-Civita/Regge/EH gravity.

## Research question and separation of data types

Does the *collection of local* P3 finite closure/residue profiles, the *local* P6 first-residue control tangent and observer fingerprint, and P7's **pointwise** positive spatial metric/orientation uniquely determine the parallel-transport matrices along interfaces of cells?

**Answer: No, without a cross-cell compatibility or measurement law.** This is a mathematical underdetermination theorem for precisely the listed cellwise information. It is **not** a no-go once the input contains cross-cell transport, calibrated intercell coherent measurements, or a specific naturality/intertwining condition.

The H24 local CPTP channel is the same at every vertex:
```math
U=\frac13\begin{pmatrix}1-2i&-2i\\-2i&1+2i\end{pmatrix},\qquad
\Phi_v(A)=UAU^\dagger .
```
Its *actual original P3 hidden Krylov* pair and genuine nonzero residue are reused with identical values at each cell:
```math
z_1=Q\Phi_v(Z),\quad z_2=Q\Phi_v^2(Z),\quad
\Delta_D([z_1,z_2^*])=\frac{128i}{81}Z.
```
The declared local P6-style action of K1=i z1 and K2=i z2 on D2 is likewise identical for each cell. All local preparation/readout mappings are held fixed. A choice of **extra** intercell connection matrices has no argument in these local objects.

## H26 finite reconstruction No-Go

Take a connected 4-cell graph V={0,1,2,3} with spanning tree {01,12,23}, plus chords {02,03}; its first Betti/cycle rank is b1=5-4+1=2.

The internal diagonal-phase subgroup of SU(2) has adjoint image SO(2)⊂SO(3) rotating the Bloch X/Y plane and fixing Z. An explicit exact element is
```math
g=\operatorname{diag}\big((3+4i)/5,(3-4i)/5\big)\in SU(2),\quad
R=\operatorname{Ad}_g=
\begin{pmatrix}
-7/25&24/25&0\\
-24/25&-7/25&0\\
0&0&1
\end{pmatrix}\in SO(3),\quad\mathrm{tr}(R)=11/25\ne3.
```
Compare two **otherwise identical** edge assignments: A_e=I on all five edges, and A'_e=I except A'_{02}=R. Every edge is internal SO(2), orientation-preserving and orthogonal. Using an explicitly chosen P7 Hadamard isometry J:R3→S=1^perp (h=4 dot), both assignments induce metric-preserving carrier transformations. All vertex-local P3/P6 data are *identical in the two networks*.

Under vertex-frame gauge transformations G_v∈SO(3), an edge transforms as
```math
A_{uv}\longmapsto G_vA_{uv}G_u^{-1}.
```
A based closed-loop holonomy changes only by conjugation. The fundamental 0120 loop has trace **3** for the flat assignment, but **11/25** for the twisted assignment. Consequently no vertex gauge, even allowing all SO(3), relates them.

**Theorem (scope-restricted):** cell-local P3 Krylov filtration, local residue, local P6-style observer/control map, and P7 pointwise metric/orientation, *without any cross-cell constraint*, do not uniquely determine the gauge-equivalence class of a cell-edge transport. The counterexample uses two unitary CPTP copies of an already nonzero-residue microscopic witness, and all edge matrices are internal SU(2) adjoint SO(2) rotations.

This underdetermination is not the claim that an actual physical connection satisfying yet-unwritten CR gluing must allow the twist. It specifies the exact missing interface information.

## Conditional reconstruction theorem for phase transports

For a connected graph with V vertices and E edges, fix H=SO(2)=U(1) as above. For each oriented edge e:u→v, let A_e∈H and write gauge action A'_e=G_v A_e G_u^{-1}. Because H is abelian, choosing a root and tree and setting tree transports to identity leaves **b1=E-V+1** independent chord/loop holonomies. Gauge-equivalence classes are
```math
H^1(G;U(1))\cong\operatorname{Hom}(H_1(G;\mathbb Z),U(1))
\cong U(1)^{b_1}.
```
Thus, **given** independently fixed gauge-invariant holonomy around one cycle basis, and the common graph topology, the U(1) connection is determined *up to vertex gauge*. A tree (b1=0) has only one gauge class; it does **not** possess a canonically fixed frame-level edge transport without calibration.

The checker constructs a nontrivial connection, changes vertex phases, verifies the identical chord-based tree normal form, and checks that changing one chord holonomy produces an inequivalent gauge class.

For genuinely nonabelian SO(3) transports, merely matching individual traces/cycle angles is insufficient: H25's simultaneous conjugacy criterion must be used. The U(1) classification here is not silently promoted to the whole nonabelian group.

## Crucial extra gluing condition: the nontrivial phase fails dynamical naturality

The diagonal SU(2) phase g preserves the diagonal observational algebra pointwise, so diagonal populations alone cannot distinguish the frame twist. **But the same phase does not intertwine H24's local CPTP channel with itself:**
```math
\operatorname{Ad}_g\circ\Phi(Z)\ne
\Phi\circ\operatorname{Ad}_g(Z)=\Phi(Z).
```
The exact checker verifies the inequality. Consequently the twisted edge **is not a counterexample in a stronger model which postulates** that all edge maps are actual dynamical intertwiners for this fixed local Phi (or imposes appropriately calibrated cross-cell coherent fingerprints). This is the sharp boundary of the result.

One possible H27 success route is to derive **rather than postulate** a physically warranted transport/intertwining rule from independently calibrated P6 coherent controls and observables, and then check whether it uniquely fixes edge phases/holonomies or rules out H26-type twists.

## Consequences for P9.24, P7/P8 and B14/B15/B17

1. Pointwise h=4 spatial metric and an internal SU(2)→SO(3) representation do not specify the Levi-Civita connection: the latter needs a geometric manifold/gluing, metric variation and torsion/connection assumptions. Arbitrary compatible SO(3) graph connections are **not** automatically Levi-Civita transports.
2. A local nonzero P3 quadratic residue is not enough to determine a global gauge-field loop holonomy. A cross-cell CR-compatible transport law or independently accessible cross-cell observables are extra information.
3. On an abelian internal-phase subbundle, b1 independent cycle phase data suffice for gauge-class reconstruction if measured/calibrated. On the full nonabelian SO3 bundle H25 simultaneous conjugacy is necessary.
4. The B14 six-edge physical CR-accessibility gap, B15 standard-GKSL non-discrimination, B17 work-conjugate force and physical gravitational constraint propagation remain unresolved.
5. P9 Minimum Success and Einstein dynamics are **not** obtained.

## Reproduction and audit separation

`P3/P9H26TransportReconstructionNoGoExactCheck.py` uses only `fractions.Fraction` and the exact H24 rational-Gaussian witness already checked in #42. It verifies: identical local H24 data and local tangent action at every cell; two inequivalent metric-preserving SO2 connections with distinct loop traces; constructive tree-gauge normalization and its invariance under independently chosen vertex phases; the beta1=2 cycle count; h-compatible R4 carrier extension; failure of the added dynamical intertwining condition for the nontrivial phase. CI checks this script, not physical experimental realization or an unconditional curvature theorem.
