# P11–AX07 — Axiomatic Integration and Generative Completeness Gate

**2026-10-19 | P11 axiomatization track | Draft.** This is independent of SPS-H113–H123 physical primitive-source studies. Finite mathematics is not a physical P6 test, a P9 gravity derivation, or a proof of the Generative Map F's universal completeness.

## Typed integration of AX01–AX06

| Type | What is established, given input | What is NOT obtained |
|---|---|---|
| AX01 linear observer | finite quotient V/N∞, induced observer dynamics, nonsplit extension witness | a new operator product or physical source |
| AX02 UCP projection | Choi–Effros product on range, compatible UCP witness | noncircular selection of that projection |
| AX03 specified observer subalgebra | unique trace-preserving conditional expectation | independent choice of subalgebra from F |
| AX04 specified measurement effects | minimum invariant *-algebra, H37 effect-generation closure | physical implementation of every formal algebra element |
| AX05 specified allowed channels/readouts | finite operational observability and H37 conditional rank25 | native device verification/exhaustive operations |
| AX06 specified instruments | selective CP maps, sequential words, tomography when frames full rank | actual hardware provenance and complete inventory |
| SPS-H113…H123 | finite static source-nonselection bounds and conditional marked-control identification | intrinsic physical AX-ORIGIN |

**Do not equate** a linear hidden kernel, a Choi–Effros quadratic return, P3's original dynamically generated hidden filtration/quadratic R_k, a Kraus/noise direction, a coherent native control, or an instrument outcome. They are distinct input/output types.

## AX07.1 Finite-word operational equivalence (EXACT, established method)

Given two independently specified finite-dimensional quantum machines with dimensions d_A,d_B and **a common finite labelled alphabet** Sigma of quantum operations I_a^A,I_a^B (CP trace-nonincreasing), and fixed initial density matrices rho_A,rho_B, the probability of a word w=a_1…a_k is

p_M(w)=Tr[I_{a_k}^M … I_{a_1}^M(rho_M)].

**Theorem:**

p_A(w)=p_B(w) for ALL words w
iff equality holds for every word of length at most
**L=d_A²+d_B²−1** (including empty word).

*Proof.* Define V=M_{d_A} ⊕ M_{d_B}, D=dim_C V=d_A²+d_B², v=(rho_A,rho_B), T_a=I_a^A ⊕ I_a^B and ell(X,Y)=Tr(X)−Tr(Y). Let R_k=span{T_w v:|w|<=k}. If R_{k+1}=R_k, it is invariant under every T_a and contains all longer T_w v. As dim R_0=1, strict growth can occur at most D−1 times; therefore R_{D−1} is stable. Equality of all probabilities for words <=D−1 says ell annihilates R_{D−1}, hence all words. Reverse implication trivial. **This is standard linear weighted automata/finite quantum machine equivalence theory, not new proof priority.** For multiple initial states/readouts treat each separately or enlarge the finite model; fixed protocol alphabet and finite dimension are essential.

Literature: Li–Feng, *Quantum Markov chains: Description of hybrid systems, decidability of equivalence, and model checking linear-time properties*, Information and Computation 244 (2015) 229–244, DOI 10.1016/j.ic.2015.07.001. Wang–Liu–Ying, *Equivalence checking of quantum finite-state machines*, JCSS 116 (2021) 1–21, DOI 10.1016/j.jcss.2020.08.004.

### Reused AX06 witness, exactly audited

Use outcomes 0,1 of the two candidate instruments:
A: I_0^A=I_1^A=Delta_Z/2;
B: I_0^B=Ad_Z/2, I_1^B=id/2.
Both have effects I/2 and the same nonselective channel Delta_Z. Add a common *separately selectable* X± projective instrument to both alphabets. From rho+=(I+X)/2, ALL one-step word probabilities agree, but

  p_A(0,X+)=1/4,   p_B(0,X+)=0.

The direct-sum dimension is 8, its reachable-space dimensions 1,3,4,4, stable by length2; the general equality decision cutoff is 7 for two qubits.

## AX07.2 Source fibre descent (EXACT logical test; physical premise OPEN)

Let M be an **explicitly delimited** class of independently sourced physical/microscopic models. Let pi:M→D describe the actually available data and s:M→S the claimed physically meaningful native source/effect/instrument label **modulo a declared equivalence**.

There exists a correct selector f:im(pi)→S with s=f∘pi **iff**

    pi(m)=pi(m') ⇒ s(m)=s(m') for all m,m' in M.

Necessity follows by applying f. Sufficiency defines f(pi(m))=s(m) independent of the representative. Equivariance under a fixed group follows if pi,s are equivariant; arbitrary functorial naturality under coarse-graining, tensor interactions, observer reduction etc. needs independent morphism axioms.

**NO circularity:** a new datum h∘pi does not refine pi-fibres. A source postulated as part of the data is not thereby generated from bare CR or F. Successful exhaustive behaviour checking over a *marked* alphabet does not prove an actual device has no extra unmarked native control. Two formal completions may have the same labelled instruments but distinct native control inventories (one X-only, the other X and an unmarked Z).

## AX07.3 Proof-gate taxonomy (definitions, not a completed generative theorem)

- **G0 / Finite descriptive closure:** Given a fixed finite model and declared observation inputs, appropriate AX01–AX06 mathematical constructions yield typed finite closures. CONDITIONALLY EXACT.
- **G1 / Marked operational completeness:** The prediction of all outcome-word probabilities for a fixed fully specified finite instrument class can be checked by the finite-word theorem. Mathematical certificates exist; independent physical apparatus calibration remains additional.
- **G2 / Physical source-and-observer completeness:** Prove that independently certified native effects/controls/instruments are *exhaustive* for an explicitly bounded physical model class, and that source labels are constant on the fibres of **independent** data. OPEN; limited interface counterexamples in SPS/AX06.
- **G3 / Generative Completeness of F:** Supply a typed definition of F's domain, codomain, admissible universes, morphisms, existence, uniqueness up to specified gauge, finite-to-infinite construction/limit, observer source selection, and physical predictions. Establish those axioms rather than smuggling required sources into inputs. OPEN.

**No implication G1⇒G2⇒G3 is established.** Exact finite CI, algebra rank25, an operationally complete marked instrument, or GKSL/Choi canonization must not be called a proof of F:empty→(Lambda,Omega), quantum gravity, or Einstein dynamics.

## Independent P3, P6, P9 handoffs

P3: AX01 hidden quotient/AX02 Gamma_E require a proven map to original P3 generated hidden filtration R_k. P6: native controls, phase reference, independently measured selective instrument CP maps and full two-stage CPTP provenance remain OPEN; differentiation from calibrated standard GKSL remains OPEN. P9: no ADM/HDA/Einstein derivation follows from finite observational equivalence. P11: AX01–AX07 supply a typed, conditional mathematical skeleton but not physical/axiomatic completeness.

## Exact symbolic reproduction and next responsible gate

Run Python 3.11 with SymPy 1.14:
  python research/p11/ax07-generative-completeness-gate-20261019/P11_AX07_generativity_gate_audit.py

Expected **99 exact checks**, including CP Kraus witnesses, same POVM and nonselective channel, length2 distinguishing probability, finite reachable-basis ranks 1,3,4,4, a 16×16 full tomography frame and a formal unmarked-source collision. The general finite-word theorem is analytically proved above but is **not Lean mechanized**. No physical experiment or independent human expert review.

**AX08 (if an independent input is found):** propose a genuinely noncircular F-derived source/effect axiom and subject it to independence, naturality and model-class tests. Otherwise record the AX-ORIGIN gate OPEN/STOP, rather than manufacturing more mathematically admissible static sectors.
