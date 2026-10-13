import P3.ExecutableObservableDepth

/-!
# Small executable finite observable stopping-depth smoke test

A one-vertex rational matrix orbit for identity dynamics: the single
diagonal seed remains the identity under every iterate. Hence every
Krylov matrix is a 1 × (k+1) row of ones. The first plateau is at k=0.
This example exercises the exact rational-rank routine itself.

The separate abstract equality to the original one-vertex P3 depth is
verified below; general rationalization is not claimed.
-/

namespace P3

/-- The actual rational orbit-entry pattern for a single diagonal seed
under identity dynamics on the one-vertex matrix algebra. -/
def p3SingleVertexRationalOrbit (k : ℕ) :
    Matrix (Fin (Fintype.card (Fin 1 × Fin 1)))
      (Fin (Fintype.card (Fin (k + 1) × Fin 1))) ℚ :=
  fun _ _ => 1

/- Runtime regression: the certified rank-search procedure actually
computes the first plateau at zero. This guard is a compiler/evaluator
check, distinct from a kernel-checked theorem about this concrete value. -/
#eval p3RatFirstStoppingDepth 0 p3SingleVertexRationalOrbit
#guard p3RatFirstStoppingDepth 0 p3SingleVertexRationalOrbit == some 0

/-- In a one-vertex P3 model the original observable closure is already
the full matrix algebra at depth zero. -/
theorem p3SingleVertexObservableDepth_zero :
    p3ObservableKrylovDepth (LinearMap.id : Dynamics (Fin 1)) = 0 := by
  have h : p3ObservableKrylovDepth
      (LinearMap.id : Dynamics (Fin 1)) ≤ 0 := by
    simpa using p3ObservableKrylovDepth_le_quadratic_gap
      (LinearMap.id : Dynamics (Fin 1))
  exact Nat.eq_zero_of_le_zero h

/-- A mathematically checked comparison conditional on the
runtime-checked rational result. The guard above is executable evidence,
not silently imported as a theorem premise. -/
theorem p3SingleVertex_report_agrees_of_result
    (hresult :
      p3RatFirstStoppingDepth 0 p3SingleVertexRationalOrbit = some 0) :
    p3RatFirstStoppingDepth 0 p3SingleVertexRationalOrbit =
      some (p3ObservableKrylovDepth (LinearMap.id : Dynamics (Fin 1))) := by
  rw [p3SingleVertexObservableDepth_zero]
  exact hresult

end P3
