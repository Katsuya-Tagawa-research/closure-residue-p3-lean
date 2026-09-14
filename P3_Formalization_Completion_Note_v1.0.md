# P3 Lean Formalization Completion Note v1.0

**Paper:** *Closure–Residue Filtration and Non-Markovian Shadows: A Finite Generative Principle for Non-Exhaustive Observational Closure*
**Author:** Katsuya Tagawa, Independent Researcher (Japan)
**Formalization status date:** 2026-09-10
**Lean:** 4.33.1
**mathlib:** v4.33.1
**Lean library target:** `P3`

---

## 1. Completion status

The finite-dimensional closure–residue core of P3 has been formalized in Lean and checked without `sorry` or `admit`.

The formalization covers:

- the diagonal observational algebra and traceless diagonal sector;
- diagonal/off-diagonal projections;
- finite closure and hidden-defect filtrations;
- quadratic return and the exact divergence identity;
- hidden-flow and residue filtrations;
- residue–stabilizer duality;
- graph incidence spaces and the incidence-rank theorem;
- support graphs and unconditional residue-to-incidence inclusion;
- explicit graph saturation as a hypothesis;
- graph-saturated residue and stabilizer dimension formulae;
- stable residue / QDMR;
- the two-dimensional linear–quadratic separation example;
- the delayed dynamic-depth example
  `H₁ ≠ 0`, `R₂ = 0`, `R₃ ≠ 0`;
- the exact unitary-conjugation realization of that example;
- the exact matrix-exponential realization
  `U = exp(- i π /(4√3) · (X + Y + h))`;
- the finite long-path example, including the `N - 1` incidence/residue dimension statement under graph saturation.

No infinite-dimensional, Type III, modular, continuum, or generic-dynamics-to-saturation theorem is asserted by this P3 formalization.

---

## 2. Module structure

The root module `P3.lean` imports:

```lean
import P3.Basic
import P3.Closure
import P3.QuadraticReturn
import P3.Filtration
import P3.Stabilizer
import P3.GraphIncidence
import P3.Support
import P3.Coupling
import P3.SaturatedStabilizer
import P3.QDMR
import P3.Examples
```

Main files:

- `P3/Basic.lean`
- `P3/Closure.lean`
- `P3/QuadraticReturn.lean`
- `P3/Filtration.lean`
- `P3/Stabilizer.lean`
- `P3/GraphIncidence.lean`
- `P3/Support.lean`
- `P3/Coupling.lean`
- `P3/SaturatedStabilizer.lean`
- `P3/QDMR.lean`
- `P3/Examples.lean`

---

## 3. Core finite structures fixed in Lean

### Algebra and observational sectors

- `A V := Matrix V V ℂ`
- `diagonalSubmodule`
- `DiagZero`
- `delta`
- `offProjection`
- `OffDiag`

### Dynamics and finite closure

- `Dynamics V := Module.End ℂ (A V)`
- `closure φ k`
- `hidden φ k`
- finite stabilization of the closure
- minimality / invariance properties

### Quadratic return

The exact finite identity

```lean
quadraticReturn_eq_divergence
```

formalizes the P3 mechanism

\[
\Delta_D([z,w^*])=\operatorname{div}(z\odot \overline w).
\]

### Filtrations

- `residue φ k`
- `hiddenFlow φ k`
- `primitiveDefect`
- `primitiveResidueSpan`
- `residue_eq_span_primitive`
- `residue_eq_map_divergence`

### Stabilizer duality

The formal theorem

```lean
residueOrthogonal_eq_stabilizer
```

implements the finite Residue–Stabilizer Duality.

### Graph coupling

- `incidenceSpace`
- `componentCount`
- `supportGraph`
- `residueCoordinateSpace_le_incidenceSpace`

Unconditionally:

\[
R_k \subseteq \mathcal B(G_k).
\]

Graph saturation is explicitly represented as

```lean
graphSaturated φ k
```

and is **not** derived automatically from generic dynamics.

Under graph saturation:

```lean
residue_finrank_of_graphSaturated
```

gives

\[
\dim R_k = N-c(G_k).
\]

The independent graph theorem is

```lean
incidence_rank
```

with

\[
\dim \mathcal B(G)=N-c(G).
\]

### Stable residue / QDMR

The stable quantity is formalized as

```lean
QDMR φ
```

and under graph saturation at infinity:

```lean
QDMR_eq_card_sub_components
```

gives

\[
\mathrm{QDMR}=N-c(G_\infty).
\]

---

## 4. Formalized paper examples

### Section 9 — Linear–Quadratic Separation

Formal theorem:

```lean
linearQuadraticSeparation_two
```

with

\[
\Delta_D(E_{12})=\Delta_D(E_{21})=0,
\]

but

\[
\Delta_D([E_{12},E_{21}])=E_{11}-E_{22}\neq0.
\]

This fixes the exact finite linear/quadratic separation.

### Section 10 — Dynamic-depth phenomenon

Formal theorem:

```lean
dynamicDepthPhenomenon
```

proves

\[
H_1\neq0,\qquad R_2=0,\qquad R_3\neq0.
\]

The same phenomenon is connected to an actual unitary conjugation by

```lean
dynamicPhiFinite
```

with

```lean
dynamicPhiFinite_eq_core
```

and

```lean
dynamicDepthPhenomenon_unitaryFinite
```

so that

\[
\Phi(a)=U^\dagger aU.
\]

The algebraic generator

\[
K=X+Y+h
\]

satisfies

\[
K^2=3I.
\]

The exact exponential bridge is formalized by

```lean
normedExp_dynamicPaperExponent_eq_dynamicUFinite
```

with

\[
U=
\exp\!\left(
-\frac{i\pi}{4\sqrt3}(X+Y+h)
\right).
\]

Thus the paper's finite unitary and exponential presentation is connected directly to the delayed-residue theorem.

### Section 11 — Finite long-path example

The finite path graph is formalized as

```lean
longPathGraph n
```

on `Fin (n+1)`.

The path is connected, and

```lean
longPathGraph_incidence_finrank
```

gives

\[
\dim\mathcal B(P_{n+1})=n=N-1.
\]

Under graph saturation:

```lean
finiteLongPathConclusion
```

gives

\[
\mathfrak s=0,
\qquad
\dim R=N-1.
\]

The stabilized version

```lean
longPath_QDMR_eq
```

gives

\[
\mathrm{QDMR}=N-1.
\]

This remains a finite-dimensional statement for every fixed finite `N`.

---

## 5. Scope boundary deliberately preserved

The P3 formalization does **not** prove:

- generic dynamics imply graph saturation;
- flow saturation is universal;
- CPTP assumptions are necessary for the finite algebraic theorem;
- an infinite-dimensional / Type III / modular / continuum limit;
- a black-hole Page-time theorem;
- spacetime, gravity, or quantum-gravity emergence.

Those belong to later work, especially P4 and beyond.

This separation is intentional: the finite theorem is fixed first, and later extensions must import the finite kernel rather than silently strengthen it.

---

## 6. Reproducibility checks

From the project root:

```bash
grep -RInE '\bsorry\b|\badmit\b' P3 P3.lean
lake build
lake env lean AxiomAudit_v0.1.lean
```

Expected results:

1. `grep` produces no output.
2. `lake build` completes successfully.
3. `AxiomAudit_v0.1.lean` reports only standard Lean/mathlib foundational axioms such as:

```text
propext
Classical.choice
Quot.sound
```

There must be:

```text
no sorryAx
no project-specific/custom axiom
```

---

## 7. Axiom audit set

The audit includes at least:

```lean
P3.flowResidueFactorization
P3.residue_eq_map_divergence
P3.residueOrthogonal_eq_stabilizer
P3.incidence_rank
P3.residue_finrank_of_graphSaturated
P3.QDMR_eq_card_sub_components
P3.linearQuadraticSeparation_two
P3.dynamicDepthPhenomenon
P3.dynamicDepthPhenomenon_unitaryFinite
P3.normedExp_dynamicPaperExponent_eq_dynamicUFinite
P3.finiteLongPathConclusion
P3.longPath_QDMR_eq
```

At the completion audit these all depended only on:

```text
[propext, Classical.choice, Quot.sound]
```

---

## 8. Recommended freeze procedure

After one final clean run of the reproducibility checks:

```bash
git status
git add P3 P3.lean lakefile.toml lake-manifest.json lean-toolchain AxiomAudit_v0.1.lean
git commit -m "Complete P3 finite closure-residue formalization"
git tag -a p3-formalization-v1.0 -m "P3 finite closure-residue formalization v1.0"
```

Optional verification:

```bash
git show --stat p3-formalization-v1.0
```

At this point P3 should be treated as a fixed finite kernel. Future mathematical development should proceed in new modules / papers rather than silently modifying the established P3 theorem set.

---

## 9. Completion statement

**P3 finite closure–residue formalization is complete.**

The finite core has been:

- stated explicitly;
- proved in Lean;
- integrated across modules;
- checked without `sorry` / `admit`;
- checked by whole-project build;
- checked by axiom audit;
- connected to the explicit finite examples in Sections 9–11.

The next research stage is P4: lifting the fixed finite kernel into an effective envelope while preserving the distinction between proved finite structure and later infinite-dimensional or observational extensions.
