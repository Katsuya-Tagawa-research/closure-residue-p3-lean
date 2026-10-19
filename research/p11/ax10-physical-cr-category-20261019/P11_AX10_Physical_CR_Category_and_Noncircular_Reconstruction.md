# P11–AX10 — Physical CR Category and the Non-Circular Reconstruction Gate

**2026-10-19 • P11 axiomatization track, stacked on AX09 Draft PR #147.** This is a **finite instrument-realization interface**, not yet the F-derived physical CR category, not original P3-generated R_k, and not a proof of physical P6 provenance, P9 gravity, or P11 Generative Completeness. Local audit: 990 exact assertions. See the downloadable full research bundle for the expanded proof.

## 1. A finite category with observer series

Fix a finite outcome alphabet Σ. An object M in **FinInstr_Σ** consists of M_d(C), density matrix ρ, and CP trace-nonincreasing maps {I_a} whose sum is CPTP. A morphism T:M→M′ is a CPTP linear map preserving initial states (Tρ=ρ′) and intertwining all marked instruments T I_a=I′_a T. Identity/composition make a category.

The **word-observation series** is p_M(a_1...a_k)=Tr[I_{a_k}...I_{a_1}(ρ)], p_M(empty)=1. Let **Lang_Σ** be the thin category of such series (one arrow exactly when they coincide). Then U:FinInstr_Σ→Lang_Σ sends objects to their word series and every intertwiner to the unique corresponding identity. This is a functor because trace-preserving intertwiners preserve all finite-word probabilities by induction.

This is a declared **marked-protocol observer interface**; choosing which instruments/hardware/source signatures to mark is extra input, not derived from the Generative Map F.

## 2. Same all-word statistics, nonisomorphic physical dynamics

Take an observed qubit A and hidden qubit B. Set p_a=|a><a|, Z_B=p0-p1, rho_A=|+><+|, tau_B=I_B/2. Compare

  I_a^A(x)=p_a x p_a  (A only),
  J_a^(0)(x)=(p_a⊗I)x(p_a⊗I)  (Y0),
  J_a^(1)(x)=(p_a⊗Z)x(p_a⊗Z)  (Y1).

For **arbitrary joint input x**, Tr_B J_a^(j)(x) = I_a^A(Tr_B x) for j=0,1. Iteration proves p_A(w)=p_Y0(w)=p_Y1(w) for **every** finite word w. Exact series: p(empty)=1, p(0^k)=p(1^k)=1/2 for k≥1, p(mixed w)=0.

Despite equality of all marked observations, the total nonselective superoperators Σ_a J_a^(0) and Σ_a J_a^(1) on M4(C) have traces **8** and **0**, respectively. Similarity would preserve trace, so Y0/Y1 are not isomorphic even as finite labeled linear dynamics, much less as CPTP instrument objects. The extra B source can be distinguished only with **additional independently allowed B access**: for input p0⊗|+><+|, outcome0 followed by X_B yields expected values +1 (Y0) versus −1 (Y1).

**Failure of faithfulness on morphisms:** Y0 has distinct CPTP instrument-intertwining automorphisms id and Ad_(I⊗Z), both preserving rho_A⊗tau_B. Both are mapped by U to the single identity of the same operational language. Therefore U is not faithful and not injective on object isomorphism classes.

### Relative categorical No-Go (exact)

There is **no** reconstruction functor R:Lang_Σ→FinInstr_Σ with a natural isomorphism R U≅Id on this whole hidden-source-extension-closed category: it would force nonisomorphic Y0 and Y1 to be isomorphic to the same R(p). Likewise U cannot be an equivalence because it is not faithful. **Choosing one representative of each observed word language is possible, but is a choice/axiom, not evidence that it selects the unique actual physical source.** The result is conditional on the unrestricted category, and does not disprove stronger *independently physically justified* restrictions.

## 3. The positive universal property has a strictly smaller codomain

For any fixed finite-rank recognizable word series p, its Hankel matrix H_(u,v)=p(uv) has rank r; quotienting the reachable linear span by the future-unobservable subspace produces a **minimal reachable/observable linear realization of dimension r**, unique up to intertwining linear isomorphism. This is the classic Schützenberger/Hankel realization theorem. It does not reconstruct a native Hilbert-space source.

The concrete series above has **rank H=2**, with a classical 2D linear realization:
  initial β=(1/2,1/2)^T, output α=(1,1), T0=diag(1,0), T1=diag(0,1).
It reproduces all words. Any d-level quantum realization gives some linear representation of dimension ≤d², so r≤d² is necessary, not sufficient to infer the physical d.

## 4. Required G2/G3 proof gates and STOP

G1 (fixed-protocol observable description) is boundedly exact in finite dimension. G2 (physical source/observer reconstruction) cannot follow from observational equivalence alone in a category admitting hidden ancillas. G3 (full generative completeness of F) needs a **prior independently typed F axiom category**, its physically motivated objects and morphisms, proof of unique observer/source up to justified equivalence, and validated bridges to the original P3 residue / P6 physical controls / P9 geometry.

A proposed reconstruction theorem must specify which microscopic distinctions **count as physically equivalent**, which source/observer marks are independently given, and how any restricted category excludes Y0/Y1 without assuming the conclusion. Source object identifiability and functor faithfulness are necessary for recovering all objects/arrows, but by themselves not sufficient to establish a categorical equivalence. Any argument using future measured target response to define the allowed native source list is circular.

**Do not** invent more static J5 candidate sectors, promote mathematical instrument examples to physical P6 PASS, confuse Hankel-rank minimization with generative source selection, or infer Einstein equations from operational completeness.

## 5. Exact reproducibility and status

Run the companion script with Python 3.11 / SymPy 1.14. Expected 990 exact assertions, including words to length7, all 16 matrix-unit partial-trace intertwining identities for two outcomes and both hidden models, nonisomorphic channel superoperator trace and spectra, nonfaithful self-morphisms, external B witness and finite Hankel rank2.

All-word identity is proved by the arbitrary-input partial trace formula above, **not** extrapolated from length7 checks. Generic categorical statements are analytic and not Lean-formalized; no human expert peer review claimed.

Background: modern quantum instrument definition and channel/input equivalence: https://pmc.ncbi.nlm.nih.gov/articles/PMC7209144/ ; classical minimal linear realization/Hankel-rank context: https://link.springer.com/article/10.1007/s00029-021-00629-2 .

**Next proposed AX11:** Define an independently physically sourced *restricted* CR object category and attempt genuine source-identifiability, or document an explicit STOP with G2/G3 OPEN.
