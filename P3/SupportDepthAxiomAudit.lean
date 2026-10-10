import P3.SupportDepth

/-!
# SupportDepth axiom audit

Review each `#print axioms` line. Accept only the standard foundational
axioms `propext`, `Classical.choice`, and `Quot.sound`.
No `sorryAx` or project-specific axiom may be present.
-/

#print axioms P3.walkWithin_mono
#print axioms P3.commutatorDynamics
#print axioms P3.commutator_step_local
#print axioms P3.commutator_iterate_local
#print axioms P3.commutator_closure_local
#print axioms P3.commutator_hidden_local
#print axioms P3.commutator_flow_local
#print axioms P3.commutator_support_depth
#print axioms P3.flowActive_iff_defectActive
#print axioms P3.supportGraph_eq_defectSupportGraph
