# P11 AX25 — Independent source provenance, permutation covariance and the F-origin gate

**October 20, 2026 | Stacked Draft on P11 AX24 PR #162.**

## Theorem 1 (conditional symmetric dephasing classification)
Fix a previously chosen pointer MASA D_d in M_d. Assume a norm-continuous unital CPTP semigroup acts as a Schur multiplier in that basis, fixes all diagonal matrix units, and is covariant under all permutations of the pointer labels. Then all offdiagonal matrix units are multiplied by the same real q(t) and the channel reads Phi_t=q(t)id+(1-q(t))Delta_D. Its Choi/Gram matrix is G_q=(1-q)I_d+q 11^T, so for an individual channel CP holds exactly if -1/(d-1)<=q<=1. Semigroup composition and continuity force q(t)=exp(-gamma*t) with gamma>=0. This fixes the functional form but not gamma, and the basis D_d remains an **assumption**.

## Theorem 2 (minimal channel environment is not complete interaction provenance)
For 0<q<1, G_q has eigenvalues 1-q (multiplicity d-1), 1+(d-1)q (multiplicity 1). Therefore Choi rank and minimum pure-state Stinespring environment dimension are d. Taking output bath vectors as columns of sqrt(G_q) yields a minimal dilation isometry. Minimal Stinespring isometries are unique only up to environment unitary, which does not select one native microscopic source.

For any full joint unitary U extending the isometry on system inputs with prepared bath |0>, let W be any bath unitary with W|0>=|0>. Then U'=U(I_S tensor W) generates exactly the same reduced channel for **all system inputs** when the bath is |0>, yet can differ on alternative bath input states. This persists even for minimal environment size (when d>=2), since a prepared input subspace of dimension d does not specify a unitary on all d^2 joint dimensions. Exact d=2,3,5 rotation-environment witnesses and a changed-bath-input distinguisher are included.

## Theorem 3 (rate requires independent time/physical input)
Each gamma>=0 meets the semigroup and covariance conditions. An uncalibrated clock rescaling t'=a*t transforms gamma'=gamma/a with invariant gamma*t. Even when clock units are calibrated, gamma remains an independent physical parameter requiring a native origin law or measurement. H37's gamma=2/3 does not follow from the channel class.

## Boundaries
* AX24 exhibited a d+1 collision environment. AX25 identifies minimum d for 0<q<1; this is not the actual bath dimension.
* The rational audit q=1/4 is a finite-time witness (for H37 gamma=2/3, Delta=(3/2)log 4), not an infinitesimal limit proof.
* The Schur property, chosen pointer basis, Markovian bath reset assumption, rate, Hamiltonian and all sources are independent inputs.
* This does not identify the original P3 residue with projected dynamical ELQLE.
* G1 predictions are conditional; G2 native apparatus/controls/environment completeness OPEN; G3 independent F-origin OPEN; no human expert review or experimental proof.

## Reproduce
Install SymPy 1.14.0 and run P11_AX25_source_provenance_audit.py. It runs **674 finite exact algebraic assertions**. It does not establish the global analytic theorem by enumeration; that theorem follows from continuity and the multiplicative Cauchy functional equation.

### Established background
Stinespring (1955), Choi (1975), Attal–Pautrat (2006), Pellonpää–Tukiainen (2017). These are standard quantum-information constructions rather than new foundational physics claims.

**Next AX26:** Define independent physical native-source input (bath preparation, coupling, calibrated clock, and observer basis) with falsifiable controls; check if any non-circular F axiom predicts them. Freeze G2/G3 as OPEN until that happens.
