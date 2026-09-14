# Closure–Residue P3 Lean Formalization

Lean formalization of the finite closure–residue core developed in the third paper of the Generative Map research program.

**Author:** Katsuya Tagawa
**Affiliation:** Independent Researcher, Japan

## Overview

This repository contains the Lean formalization associated with:

**Closure–Residue Filtration and Non-Markovian Shadows**

The development formalizes the finite-dimensional matrix-algebraic core of observational closure, hidden sectors, quadratic return, residue formation, and the graph-incidence structure of QDMR.

## Main Formalized Structures

- finite matrix algebra \(A_N = M_N(\mathbb{C})\)
- diagonal observational subspace
- traceless diagonal sector \(D_N^0\)
- diagonal projection \(\Delta_D\)
- off-diagonal sector
- closure and hidden-sector filtrations
- hidden-flow and residue spaces
- support graphs and graph saturation
- quadratic return and divergence
- QDMR

## Main Formalized Results

The development includes the quadratic return / divergence identity

\[
\Delta_D([z,w^*])
=
\operatorname{div}(z\odot\overline{w}),
\]

together with the associated hidden-flow to diagonal-residue relation.

Under the saturation hypothesis, it formalizes the Incidence Rank Theorem

\[
\mathrm{QDMR}
=
\dim R_k
=
N-c(G_k),
\]

and the increment formula

\[
q_k
=
c(G_{k-1})-c(G_k).
\]

Finite delayed-return examples are also included.

## Verification

Run:

`lake build`

Reference environment:

- Lean 4.33.1
- mathlib v4.33.1

The reference build completes successfully with no `sorry` or `admit`.

## Scope

This repository formalizes the finite-dimensional closure–residue core.

The implication

\[
\text{generic dynamics}
\Longrightarrow
\text{saturation}
\]

is not proved here. Saturation is used as an explicit hypothesis where required.

Infinite-dimensional operator algebras, Type III structures, modular theory, and continuum extensions are outside the scope of this formalization.

## Repository Structure

- `P3/` — main Lean source files
- `P3.lean` — top-level P3 import
- `AxiomAudit_v0.1.lean` — axiom audit
- `ExpProbe_v0.1.lean` — finite-dimensional exponential probe
- `P3_Formalization_Completion_Note_v1.0.md` — completion and verification notes

## Status

**Finite closure–residue core: formally verified baseline.**