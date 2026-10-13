import P3.ExecutableObservableDepthExamples

/-!
# Exact rational input bridge: identity dynamics on finite matrix algebras

Unlike a bare runtime rank check, the rational Krylov presentation below
is constructed from a specified complex-linear P3 dynamics and proved
entrywise equal to its canonical finite observable Krylov matrix.

The physical model here is the identity map, so it is intentionally
simple and not evidence for a general rationalization theorem. The
generic conditional computational theorem from Phase 5 is now usable
without an externally supplied rational-presentation hypothesis in
this model.
-/

namespace P3

section RationalIdentityModel

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Fully rational, finite diagonal-seed orbit matrix of the identity
channel on a finite matrix algebra. The generic Fin-indexing uses a
noncomputable choice of enumeration; for fully executable inputs one
must additionally supply a concrete finite enumeration.
Each column corresponding to (j,a) is the rational matrix unit E_aa,
regardless of j. -/
noncomputable def p3IdentityRationalKrylov (k : ℕ) :
    Matrix (Fin (Fintype.card (V × V)))
      (Fin (Fintype.card (Fin (k + 1) × V))) ℚ :=
  fun row col =>
    let xy := (Fintype.equivFin (V × V)).symm row
    let ja := (Fintype.equivFin (Fin (k + 1) × V)).symm col
    Matrix.single ja.2 ja.2 (1 : ℚ) xy.1 xy.2

/-- The explicit rational identity-model matrix is exactly the
coefficient presentation of the original P3 complex Krylov matrix,
at every finite depth. No rational-representability assumption remains. -/
theorem p3IdentityRationalKrylov_exact (k : ℕ) :
    p3FinIndexedKrylovMatrix (LinearMap.id : Dynamics V) k =
      (p3IdentityRationalKrylov (V := V) k).map (Rat.castHom ℂ) := by
  classical
  ext row col
  change
    p3CanonicalKrylovMatrix (LinearMap.id : Dynamics V) k
      ((Fintype.equivFin (V × V)).symm row)
      ((Fintype.equivFin (Fin (k + 1) × V)).symm col) =
    (Rat.castHom ℂ) (p3IdentityRationalKrylov (V := V) k row col)
  rw [p3CanonicalKrylovMatrix_entry]
  dsimp [p3IdentityRationalKrylov]
  split_ifs <;> simp_all [Matrix.single_apply]

/-- Fully verified executable stopping depth for the finite
identity-dynamics P3 model, with no externally supplied hQ. -/
theorem p3IdentityRationalKrylov_stopping_depth :
    p3RatFirstStoppingDepth
      (p3AlgebraDimension (V := V) - Fintype.card V)
      (p3IdentityRationalKrylov (V := V)) =
      some (p3ObservableKrylovDepth (LinearMap.id : Dynamics V)) := by
  apply p3RatFirstStoppingDepth_complete
    (LinearMap.id : Dynamics V)
    (p3IdentityRationalKrylov (V := V))
  intro k hk
  exact p3IdentityRationalKrylov_exact (V := V) k

/-- Identity dynamics preserves the P3 diagonal seed space, so the
original observable closure plateaus already at depth zero for ANY
finite vertex set, not only the one-vertex example. -/
theorem p3IdentityObservableDepth_zero :
    p3ObservableKrylovDepth (LinearMap.id : Dynamics V) = 0 := by
  have hpres : PreservesDiagonal (V := V)
      (LinearMap.id : Dynamics V) := by
    intro d
    simpa only [LinearMap.id_apply] using d.property
  have hplateau :
      closure (LinearMap.id : Dynamics V) 1 =
        closure (LinearMap.id : Dynamics V) 0 := by
    calc
      closure (LinearMap.id : Dynamics V) 1 =
          diagonalSubmodule (V := V) :=
        closure_one_eq_diagonal_of_preservesDiagonal _ hpres
      _ = closure (LinearMap.id : Dynamics V) 0 :=
        (closure_zero _).symm
  apply p3ObservableKrylovDepth_eq_of_rank_certificate
    (LinearMap.id : Dynamics V) 0
  · exact (p3KrylovRank_eq_succ_iff_closure_plateau _ 0).mpr hplateau
  · intro k hk
    omega

/-- The exact-rank algorithm returns the FIRST plateau, depth zero,
for every finite identity-dynamics input with its rational presentation. -/
theorem p3IdentityRationalKrylov_stopping_depth_zero :
    p3RatFirstStoppingDepth
      (p3AlgebraDimension (V := V) - Fintype.card V)
      (p3IdentityRationalKrylov (V := V)) = some 0 := by
  rw [p3IdentityRationalKrylov_stopping_depth,
    p3IdentityObservableDepth_zero]

/-- A concrete one-vertex physical dynamical input is completely
certified by the rational matrix calculation and the exact Lean bridge.
This equality is kernel-checked, unlike a standalone #guard. -/
theorem p3IdentitySingleVertex_stopping_depth :
    p3RatFirstStoppingDepth
      (p3AlgebraDimension (V := Fin 1) - Fintype.card (Fin 1))
      (p3IdentityRationalKrylov (V := Fin 1)) = some 0 := by
  rw [p3IdentityRationalKrylov_stopping_depth]
  exact congrArg some p3SingleVertexObservableDepth_zero

end RationalIdentityModel
end P3
