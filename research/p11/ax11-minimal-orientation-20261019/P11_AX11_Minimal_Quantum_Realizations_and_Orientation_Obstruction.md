# P11–AX11 — Minimal Quantum Realizations and the Orientation Obstruction

**2026-10-19 | P11 axiomatization, stacked on AX10 Draft PR #148.** This is a rigorously bounded finite source-identification study. It does not prove any physical P6 provenance, H37 J5 native source, the original P3 generated residue, P9 gravity, or P11 Generative Completeness. Quantum gate-set tomography gauge and unitary/antiunitary symmetries are established prior literature.

## 1. All-word transpose companion theorem

For a finite labeled quantum instrument with initial density operator ρ and CP trace-nonincreasing branches I_a (sum TP), define the linear transpose operator T(X)=X^T and the companion source

  ρ'=T(ρ),   I'_a = T ∘ I_a ∘ T.

If I_a(X)=Σ_j K_aj X K_aj†, then I'_a(X)=Σ_j (K_aj)* X ((K_aj)*)†: every transformed branch is CP, and the sum is TP. (The standalone transpose map T is NOT CP for d≥2; the simultaneous conjugation of an entire instrument preserves CP.) By induction, for **every** outcome word a1…ak,

  I'_ak ... I'_a1(ρ') = [I_ak ... I_a1(ρ)]^T,

hence p'(w)=p(w) for all word lengths. The transpose is an invertible complex-linear superoperator and maps reachable/observable linear spaces bijectively; linear minimality and word Hankel rank are preserved.

This establishes **unanchored instrument gauge ambiguity**, NOT an empirical distinction between two laboratories when no physical complex-orientation reference exists.

## 2. Explicit tetrahedral 2-level instrument — minimal, no spectator

Let X,Y,Z be the Pauli operators and four Bloch vectors be

  r0=(1,1,1)/sqrt(3), r1=(1,-1,-1)/sqrt(3),
  r2=(-1,1,-1)/sqrt(3), r3=(-1,-1,1)/sqrt(3).

Set s_a=(I+r_a·σ)/2, E_a=s_a/2 and input ρ0=I/2. The four effects sum to I. The labeled measure-prepare CP instrument I_a(Q)=Tr(E_a Q) s_a is valid. All p(a)=1/4. Each s_a is a rank-one density operator.

The effects {E_a} span all M2(C), so the observer is fully informationally complete. From ρ0, the four one-word unnormalized posterior states s_a/4 also span all M2(C), so the reachable space is full. Consequently the word Hankel rank is **4**, exactly equal to d²: this is an **operationally minimal linear realization**, without a hidden spectator factor or an unreachable quantum-operator direction.

The exact conditional transition matrix is

  T_{b,a}=Tr(E_b s_a)=1/2 (a=b) or 1/6 (a≠b);
  T=(1/3)I4+(1/6)11ᵀ, det T=1/27.

A 5×5 word Hankel minor formed by empty word and the four single letters has rank4. The simultaneously transposed companion is another valid, fully reachable and observable minimal instrument, with **identical probabilities for every finite word**. The finite script checks all 340 labeled words of lengths1–4 in both models, and checks the analytic intertwiner on the full M2 basis; all-word equality follows from the theorem, not finite enumeration.

## 3. Oriented unitary subcategory: the obstruction survives minimality

On Bloch coefficients, transpose is (x,y,z)→(x,-y,z), an O(3) reflection with determinant −1. A spatially unitary qubit transformation induces a proper SO(3) rotation with determinant +1. Since three labeled tetra vectors are independent, the two **label-preserving, fixed-orientation models cannot be related by unitary conjugation**.

Define the signed triple of labeled Bloch operators A_a=r_a·σ:

  χ=Tr(A0 [A1,A2])/(4i)=det[r0,r1,r2]=4sqrt(3)/9.

Its transposed counterpart has χ'=-4sqrt(3)/9. The signed triple is invariant under common unitary conjugation and reverses under transpose. This is **not** a gauge-invariant experimental observable of the bare unanchored outcome language: the common antiunitary/transposed description may reasonably be treated as the same physics in that broader gauge category. The No-Go concerns reconstructing an **oriented spatial/unitary source class** from unanchored statistics.

Standalone transposition is not CP: its Choi matrix is the swap, with eigenvalue −1 on the antisymmetric two-qubit vector. This explains why the invertible linear Hankel gauge transformation does not automatically lie in the physically allowed spatial unitary gauge group, even though it transports a whole CP instrument family to another CP family.

## 4. Conditional positive gate — independent complex phase reference

If a **separately calibrated and held-fixed** external Y-positive state ρ_Y+=(I+Y)/2 is additionally preparable, the first tetra outcome distinguishes the two sources:

  Tr(E0 ρ_Y+)=(1+1/sqrt(3))/4,
  Tr(E0^T ρ_Y+)=(1−1/sqrt(3))/4,

with difference 1/(2sqrt(3)). The external reference **must not be co-transposed** along with the candidate instrument. This is a conditional mathematical orientation witness, **not** certification that the P6 hardware supplies an independent Y phase standard.

More generally, if independently calibrated preparations ρ_i and readout functionals F_j each span Herm_d over R, the numbers Tr(F_j I_a(ρ_i)) determine **each marked Hermiticity-preserving instrument branch** I_a in the known reference frame (ordinary process tomography). The tetrahedral inputs/readouts have ranks 4+4, giving a full rank 16 real coefficient map for each marked branch.

However, no amount of tomographic identification of the **declared** branches proves that additional unmarked native physical sources or controls are absent. Nor does linear minimality identify the selected effect list from F.

## 5. Independent-source proof-obligation ledger

- G1 operational minimal observer realization: **EXACT, conditional**. Hankel rank4 with reachable and observable rank4, old linear-realization theory.
- Same complete word language implies an identical **oriented** physical source up to unitary conjugation: **NO** in this model class.
- Standalone transpose CP: **NO** (Choi swap has a negative eigenvalue); instrument-wise simultaneous transpose remains CP.
- Independently anchored complex orientation can separate this specific transpose pair: **EXACT conditional**, assuming calibrated, externally sourced Y-reference.
- Marked instrument tomography plus independently fixed input/output frame: **EXACT conditional**.
- A complete catalogue of actual unmarked/native controls, original P3 signed-residue provenance, P6 differential prediction/hardware validation: **OPEN**.
- F-derived axioms selecting source catalogue and orientation, P11 Generative Completeness, P9 ADM/HDA/Einstein: **OPEN**.

Do not add arbitrary J5 controls or conflate gauge-nonuniqueness with a demonstrated physical multiplicity of laboratory devices.

## Evidence and literature

Run Python 3.11/SymPy 1.14 audit P11_AX11_chiral_minimality_audit.py, expected **803/803 exact assertions** and JSON preserving OPEN flags. Analytical proofs above are NOT Lean mechanized; finite CI does not establish independent human peer review.

- Blume-Kohout et al., “Demonstration of qubit operations below a rigorous fault tolerance threshold with gate set tomography,” Nature Communications 8, 14485 (2017), https://www.nature.com/articles/ncomms14485 — gauge non-uniqueness under frame transforms.
- Simon et al., “Two elementary proofs of the Wigner theorem on symmetry in quantum mechanics,” Physics Letters A 372 (2008), DOI 10.1016/j.physleta.2008.09.052 — unitary and antiunitary distinction.

**Next gate AX12:** no more claims of source uniqueness until a genuinely independent source/exhaustiveness axiom and complex orientation anchor are physically justified, or a non-circular F-derived restriction excludes both spectator and transpose ambiguities.
