# H64 — Source-versus-Access Theorem: P3 Hidden Odd Quadratures and Frozen P6 Real-Exchange Projection

**2026-10-15 | P3–P11 Mathematical Bridge → P9.** This stage follows audited H63 and distinguishes (a) algebraic candidates in an ORIGINAL P3 hidden Krylov construction from (b) the **physically admitted** frozen P6 v9.1 two-real-exchange controls and population observer. Its positive source example is the exact **H32** connected three-site rational unitary CPTP comparator; it is **not claimed to equal the independently inherited P6 microscopic \(\mathcal J_N\)**. Its negative comparator is the H38-type REAL channel. All results are standard finite quantum mechanics, with no CR-only anomaly or Einstein-generation claim.

## 1. Three layers of mathematical accessibility

Let \(S\) denote a microscopic hidden Krylov span computed from a specified channel and diagonal seed algebra \(D\). Define \(\Xi(J)=(1-\Delta_D)(J-J^\dagger)\); write the REAL candidate control space \(V_{\mathrm{micro}}=\Xi(S)\) and the frozen physical control space \(W_{\mathrm{P6}}=\operatorname{span}_{\mathbb R}\{A_{01},B_{12}\}\).

- An operator lying in \(\Xi(S)\) is a **candidate control tangent**, not proof that the frozen P6 physical manifold contains it. A source-to-control assignment needs independent physical \(\mathcal J_N\), a declared star-compatible map, controls and observer-closure intertwining.
- A large Lie closure of candidate generators is **not** a hardware accessibility theorem.
- Operationally distinguishing phase-sensitive states requires a protocol which breaks the relevant transpose identification; a formal antisymmetric KKS sector alone does not suffice.

## 2. H64.1 — six algebraic quadratures can coexist with a two-direction physical control space

H32's independently constructed single U(3) microscopic CPTP channel has exact computed

\[
\operatorname{rank}_{\mathbb R}\Xi(H_{\le 1})=2,\quad
\operatorname{rank}_{\mathbb R}\Xi(H_{\le 2})=4,\quad
\boxed{\operatorname{rank}_{\mathbb R}\Xi(H_{\le 3})=6}.
\]

It also has a **nonzero genuine original P3** depth-three signed residue. These are H32 comparator outcomes, **not a frozen-P6 physical control derivation**.

The full six-dimensional real space \(V\) of zero-diagonal anti-Hermitian three-site matrices splits as

\[
V=V^+\oplus V^-,\quad
V^+=\operatorname{span}_{\mathbb R}\{A_{01},A_{02},A_{12}\},\quad
V^-=\operatorname{span}_{\mathbb R}\{Q_{01},Q_{02},Q_{12}\},
\]

\[
A_{ab}=E_{ab}-E_{ba},\qquad
Q_{ab}=i(E_{ab}+E_{ba}),\qquad
\dim V^+=\dim V^-=3.
\]

The source involution on anti-Hermitian **control generators** compatible with state transposition \(\tau(\rho)=\rho^T\) is

\[
\mathcal T(K)=-K^T
\]

because \(\tau([K,\rho])=[-K^T,\tau(\rho)]\). Thus \(\mathcal T(A)=+A\) and \(\mathcal T(Q)=-Q\). This is distinct from simply transposing generators without the minus sign.

The physically admitted frozen-P6 exchange space \(W_{\mathrm{P6}}=\operatorname{span}_{\mathbb R}\{A_{01}, E_{21}-E_{12}\}\) is a two-dimensional **\(\mathcal T\)-even** subspace.

### H64.2 — universal equivariant linear-access NO-GO

Let \(L:V\to W_{\mathrm{P6}}\) be any **real-linear** source-to-physical-tangent assignment respecting state-transpose symmetry,

\[
L\circ\mathcal T_V=\mathcal T_W\circ L.
\]

Since \(\mathcal T_W=+I\), for every \(v\in V^-\) one gets

\[
L(-v)=L(v)\quad\Longrightarrow\quad\boxed{L(v)=0}.
\]

Thus all three imaginary-symmetric, phase-sensitive \(\mathcal T\)-odd quadratures necessarily lie in \(\ker L\). No **transpose-equivariant real-linear access map into frozen-P6 physical controls** can make them usable by the original two-real-exchange hardware. The proof is entirely representation-theoretic, not dependent on a particular arbitrary \(L\). It is not an impossibility statement for nonlinear, explicitly symmetry-breaking or expanded hardware with odd controls.

An exact concrete projection is

\[
L(K)=\operatorname{Re}K_{01}\,A_{01}
 +\operatorname{Re}K_{21}\,(E_{21}-E_{12}).
\]

It has real rank 2, kernel dimension 4 (the three odd quadratures plus one even 02 direction), is \(\mathcal T\)-equivariant and is **one declared mathematical assignment only**. It does not derive the actual frozen P6 microscopic source map, which remains OPEN.

## 3. H64.3 — nonzero hidden flow need not have any signed P3 residue in the real comparator

For a second independently defined 3-site channel choose a product \(U_{\mathbb R}=R_{12}(5/13,12/13)R_{01}(3/5,4/5)\) of explicit **real orthogonal** site rotations, and \(\Phi=\operatorname{Ad}_{U_{\mathbb R}}\). For every real diagonal seed \(d\), all hidden iterates

\[
z_k=(1-\Delta_D)\Phi^k(d)
\]

are **real symmetric**: this is preserved by the real orthogonal channel and the diagonal projection (and also by independently calibrated real site-dephasing). Yet for the exhibited channel some \(z_k\ne0\): nontrivial hidden flow exists.

For any two real symmetric hidden operators \(z_i,z_j\),

\[
[z_i,z_j^\dagger]^T=-[z_i,z_j^\dagger]
\quad\Longrightarrow\quad
\boxed{\Delta_D([z_i,z_j^\dagger])=0}.
\]

Thus the **original P3 signed diagonal commutator-residue filtration is zero at all depths**, despite nonzero hidden iterates. This is an analytic all-depth theorem, with exact rational finite-depth witnesses, not a universal claim about all possible P3 channels. In particular: **nonzero P3 hidden flow alone does not select a phase-odd physical control or a nonzero signed quadratic return**.

Contrast the H32 non-real CPTP comparator: its 6D algebraic \(\Xi\) and nonzero original P3 signed residue show a blanket claim that **all P3 algebraic channels** have no odd direction or nonzero residue would be false. Distinct comparators are never silently identified with one physical frozen-P6 realization.

## 4. H64.4 — breaking transposition is necessary, not independently generated

As an **additional independently calibrated** conventional QM control, \(V_\phi=\operatorname{diag}(-i,1,1)\) converts a sign pair of imaginary coherences to real coherences before a real exchange/population readout. For \(\rho_\pm=I_3/3\pm i(E_{01}-E_{10})/6\), a real rational rotation \(R_{01}(3/5,4/5)\) produces an exact population **contrast magnitude** \(8/25\) after \(V_\phi\). Without that extra resource the contrast is identically zero. This matches H38/H39/H63 and shows physical feasibility **conditional on independently authorizing the phase gate**, not new CR dynamics.

This does not provide the source of the gate, an absolute phase standard, the original P6 \(\mathcal J_N\), a full microscopic-to-physical CPTP intertwiner or a CR-specific operational discriminator. Actual P3 signed residues are the same finite QM objects in both CR and standard CPTP comparator descriptions.

## 5. P9.72 / H64 handoff and next H65 gate

**H64 classification:**

1. **EXACT comparator existence:** an independently specified P3 source can have a six-real-dimensional odd/even candidate space and nonzero original quadratic signed return (H32).
2. **EXACT / CONDITIONAL NO-GO:** no real-linear **transpose-equivariant** source map to the frozen two-real-exchange P6 physical tangent space can retain an odd generator.
3. **EXACT restricted source NO-GO:** real orthogonal P6-compatible dynamics can have nontrivial hidden flow but zero original P3 signed return in the diagonal real-symmetric sector.
4. **CONDITIONAL escape:** coherent Stark phase/complex readout breaks the operational transpose obstruction, but requires **extra calibrated physical resources**, as does P9.72's enhanced SWAP+ZZ X/Y measurement/control sector.

**Next H65:** examine whether a *microscopically independently supplied* physical complex/odd control can be linked by an honest star/CPTP/source-compatible \(L\) or whether the frozen real-control source conditions force equivariance. Do not assume the H32 \(\Xi(H_3)\) is the frozen P6 inherited \(\mathcal J_N\); that unproven identification is the remaining provenance gate. For P9.72, await explicit original finite response Jacobian/time error and P9.72's many-body error bounds before claiming reproduction or \(M\)-uniformity. If full controlled processes and instruments coincide, H50 still forces exact operational equivalence with ordinary QM.

## Reproducibility and status

Run \`python3 P3/P9H64MicroscopicOddSourceEquivariantAccessExactCheck.py\`. The stdlib rational/Gaussian-rational checker imports and reuses previously verified H32 3-site source data, independently constructs the transpose-even/odd control basis and equivariant projection, and independently constructs a real orthogonal channel with hidden iterates and all signed residues zero. It also checks the extra calibrated Stark gate contrast. Universal claims follow from the two displayed involution identities; finite enumeration is evidence, not their logical proof.

This is a Draft/unmerged research bridge. No frozen P1–P8 paper/main changes, Lean kernel proof, independent human expert peer review, experimental signal, P9 Minimum Success, HDA or Einstein dynamics.
