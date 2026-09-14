import P3

/-!
Axiom audit for the P3 finite closure–residue formalization.

Expected acceptable foundational axioms from Lean/mathlib may include:
`Classical.choice`, `propext`, and `Quot.sound`.

There must be no `sorryAx` and no project-specific/custom axioms.
-/

#print axioms P3.flowResidueFactorization
#print axioms P3.residue_eq_map_divergence
#print axioms P3.residueOrthogonal_eq_stabilizer
#print axioms P3.incidence_rank
#print axioms P3.residue_finrank_of_graphSaturated
#print axioms P3.QDMR_eq_card_sub_components

#print axioms P3.linearQuadraticSeparation_two
#print axioms P3.dynamicDepthPhenomenon
#print axioms P3.dynamicDepthPhenomenon_unitaryFinite
#print axioms P3.normedExp_dynamicPaperExponent_eq_dynamicUFinite
#print axioms P3.finiteLongPathConclusion
#print axioms P3.longPath_QDMR_eq
