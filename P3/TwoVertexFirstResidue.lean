import P3.RationalIdentityModel

/-!
# Two-vertex algebraic first-residue witness

This finite complex-linear map sends the 00 matrix entry to the
off-diagonal 01 matrix unit and kills every other coordinate.
It is nilpotent of index two. Consequently the diagonal-seed
P3 observable closure grows strictly at depth one and stabilizes
at depth two: the first plateau is exactly s_obs = 1.

This is an algebraic P3 Dynamics witness. It is NOT claimed to
be a trace-preserving or completely positive physical channel.
A fully rational input presentation and computational connection
can be added in a subsequent layer without changing the P3 core.
-/

noncomputable section

namespace P3

/-- An explicit two-vertex nontrivial algebraic P3 dynamics.
The diagonal 00 seed moves into the previously invisible 01 coordinate. -/
def p3TwoVertexFirstResidue : Dynamics (Fin 2) where
  toFun M := fun x y =>
    if x = (0 : Fin 2) ∧ y = (1 : Fin 2) then M 0 0 else 0
  map_add' M N := by
    ext x y
    change (if x = (0 : Fin 2) ∧ y = (1 : Fin 2)
      then (M + N) 0 0 else 0) =
      (if x = 0 ∧ y = 1 then M 0 0 else 0) +
      (if x = 0 ∧ y = 1 then N 0 0 else 0)
    by_cases h : x = (0 : Fin 2) ∧ y = (1 : Fin 2)
    · simp [h, Matrix.add_apply]
    · simp [h]
  map_smul' c M := by
    ext x y
    change (if x = (0 : Fin 2) ∧ y = (1 : Fin 2)
      then (c • M) 0 0 else 0) =
      c • (if x = 0 ∧ y = 1 then M 0 0 else 0)
    by_cases h : x = (0 : Fin 2) ∧ y = (1 : Fin 2)
    · simp [h, Matrix.smul_apply]
    · simp [h]

/-- Applying the map twice annihilates every matrix. -/
theorem p3TwoVertexFirstResidue_square_zero (M : A (Fin 2)) :
    (p3TwoVertexFirstResidue ^ 2) M = 0 := by
  ext x y
  change p3TwoVertexFirstResidue (p3TwoVertexFirstResidue M) x y = 0
  change (if x = (0 : Fin 2) ∧ y = (1 : Fin 2)
    then (if (0 : Fin 2) = 0 ∧ (0 : Fin 2) = 1 then M 0 0 else 0)
    else 0) = 0
  simp

/-- The first hidden response is nonzero: E₀₀ goes to E₀₁. -/
theorem p3TwoVertexFirstResidue_noninvariant :
    ¬ PreservesDiagonal (V := Fin 2) p3TwoVertexFirstResidue := by
  intro hpres
  let d : diagonalSubmodule (V := Fin 2) :=
    p3CanonicalDiagonalBasis (V := Fin 2) (0 : Fin 2)
  have hd : d.1 = Matrix.single (0 : Fin 2) (0 : Fin 2) (1 : ℂ) :=
    p3CanonicalDiagonalBasis_apply (V := Fin 2) (0 : Fin 2)
  have hmem : p3TwoVertexFirstResidue d.1 ∈
      diagonalSubmodule (V := Fin 2) := hpres d
  have hfix := delta_eq_self_of_mem_diagonalSubmodule (V := Fin 2) hmem
  have hpoint := congrArg
    (fun M : A (Fin 2) => M (0 : Fin 2) (1 : Fin 2)) hfix
  have hleft :
      delta (V := Fin 2) (p3TwoVertexFirstResidue d.1) 0 1 = 0 := by
    simp [delta_apply]
  have hright : p3TwoVertexFirstResidue d.1 0 1 = (1 : ℂ) := by
    change d.1 0 0 = 1
    rw [hd]
    simp [Matrix.single_apply]
  have hcontr : (0 : ℂ) = 1 := calc
    0 = delta (V := Fin 2) (p3TwoVertexFirstResidue d.1) 0 1 :=
      hleft.symm
    _ = p3TwoVertexFirstResidue d.1 0 1 := hpoint
    _ = 1 := hright
  exact zero_ne_one hcontr

/-- An actual hidden (off-diagonal) P3 direction appears at depth one. -/
theorem p3TwoVertexFirstResidue_hidden_ne_bot :
    hidden p3TwoVertexFirstResidue 1 ≠ ⊥ :=
  (noninvariant_iff_hidden_one_ne_bot p3TwoVertexFirstResidue).mp
    p3TwoVertexFirstResidue_noninvariant

/-- The nilpotent map produces no new orbit directions after depth one. -/
theorem p3TwoVertexFirstResidue_closure_two_eq_one :
    closure p3TwoVertexFirstResidue 2 =
      closure p3TwoVertexFirstResidue 1 := by
  apply le_antisymm
  · apply Submodule.span_le.mpr
    rintro x ⟨d, n, hn, rfl⟩
    interval_cases n
    · simpa using
        (diagonalSubmodule_le_closure p3TwoVertexFirstResidue 1 d.property)
    · apply Submodule.subset_span
      exact ⟨d, 1, by omega, rfl⟩
    · rw [p3TwoVertexFirstResidue_square_zero]
      exact Submodule.zero_mem _
  · exact closure_mono p3TwoVertexFirstResidue (by omega)

/-- Exact first observable plateau: zero is too early, one is stationary. -/
theorem p3TwoVertexFirstResidue_depth_one :
    p3ObservableKrylovDepth p3TwoVertexFirstResidue = 1 := by
  apply p3ObservableKrylovDepth_eq_of_rank_certificate
    p3TwoVertexFirstResidue 1
  · exact (p3KrylovRank_eq_succ_iff_closure_plateau
      p3TwoVertexFirstResidue 1).mpr
        p3TwoVertexFirstResidue_closure_two_eq_one
  · intro k hk
    have hkzero : k = 0 := by omega
    subst k
    have hne : closure p3TwoVertexFirstResidue 1 ≠
        closure p3TwoVertexFirstResidue 0 := by
      intro heq
      apply p3TwoVertexFirstResidue_noninvariant
      intro d
      have hx : p3TwoVertexFirstResidue d.1 ∈
          closure p3TwoVertexFirstResidue 1 :=
        map_diagonal_mem_closure_one p3TwoVertexFirstResidue d
      rwa [heq, closure_zero] at hx
    exact Submodule.finrank_lt_finrank_of_lt
      (lt_of_le_of_ne
        (closure_mono p3TwoVertexFirstResidue (by omega))
        hne.symm)

end P3
