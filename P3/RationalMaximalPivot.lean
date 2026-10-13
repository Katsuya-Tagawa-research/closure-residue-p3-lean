import P3.RationalRankFactorization

/-!
# Maximal nonzero rational minors and totality of the exact rank search

Every finite rational matrix has a rank-sized nonzero determinant minor.
The proof selects independent coordinate rows from a full-column-rank
factor and independent coordinate columns from its full-row-rank
companion, and uses multiplicativity of determinants.

Combining that existence statement with P3.RationalPivotFactorization
and P3.RationalSearchAdequacy proves unconditional totality of the
exhaustive exact rational rank algorithm.

This remains a finite rational-algebra theorem. It does not assert
that arbitrary complex-valued quantum dynamics has rational entries.
-/

noncomputable section

namespace P3

section MaximalRationalPivot

/-- A finite matrix with full column rank has a square row minor
with nonzero determinant. -/
theorem p3Rat_exists_nonsingular_row_submatrix {m r : ℕ}
    (B : Matrix (Fin m) (Fin r) ℚ)
    (hB : B.rank = r) :
    ∃ rows : Fin r → Fin m, (B.submatrix rows id).det ≠ 0 := by
  classical
  obtain ⟨κ, a, ha, hspan, hli⟩ :=
    exists_linearIndependent' ℚ B.row
  letI : Finite κ := Finite.of_injective a ha
  letI : Fintype κ := Fintype.ofFinite κ
  have hcard : Fintype.card κ = r := by
    calc
      Fintype.card κ =
          Module.finrank ℚ (Submodule.span ℚ (Set.range (B.row ∘ a))) :=
        (finrank_span_eq_card hli).symm
      _ = B.rank := by rw [hspan]; exact (Matrix.rank_eq_finrank_span_row B).symm
      _ = r := hB
  let e : Fin r ≃ κ := (Fintype.equivFinOfCardEq hcard).symm
  let rows : Fin r → Fin m := a ∘ e
  have hliRows : LinearIndependent ℚ (B.submatrix rows id).row := by
    change LinearIndependent ℚ (B.row ∘ a ∘ e)
    exact hli.comp e e.injective
  have hunit : IsUnit (B.submatrix rows id) :=
    Matrix.linearIndependent_rows_iff_isUnit.mp hliRows
  exact ⟨rows, ((Matrix.isUnit_iff_isUnit_det _).mp hunit).ne_zero⟩

/-- Given a rank-r factorization, some r×r minor of A is invertible. -/
theorem p3Rat_exists_nonsingular_pivot_of_factorization
    {m n r : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ)
    (B : Matrix (Fin m) (Fin r) ℚ)
    (C : Matrix (Fin r) (Fin n) ℚ)
    (hfactor : A = B * C)
    (hr : A.rank = r) :
    ∃ (rows : Fin r → Fin m) (cols : Fin r → Fin n),
      (A.submatrix rows cols).det ≠ 0 := by
  have hB : B.rank = r := by
    apply Nat.le_antisymm
    · simpa using Matrix.rank_le_card_width B
    · calc
        r = A.rank := hr.symm
        _ = (B * C).rank := congrArg Matrix.rank hfactor
        _ ≤ B.rank := Matrix.rank_mul_le_left B C
  have hC : C.rank = r := by
    apply Nat.le_antisymm
    · simpa using Matrix.rank_le_card_height C
    · calc
        r = A.rank := hr.symm
        _ = (B * C).rank := congrArg Matrix.rank hfactor
        _ ≤ C.rank := Matrix.rank_mul_le_right B C
  obtain ⟨rows, hrows⟩ := p3Rat_exists_nonsingular_row_submatrix B hB
  have hCT : Cᵀ.rank = r := by simpa using hC
  obtain ⟨cols, hcolsT⟩ := p3Rat_exists_nonsingular_row_submatrix Cᵀ hCT
  have htranspose :
      (Cᵀ.submatrix cols id) = (C.submatrix id cols)ᵀ := by
    ext i j
    rfl
  have hcols : (C.submatrix id cols).det ≠ 0 := by
    rw [htranspose, Matrix.det_transpose] at hcolsT
    exact hcolsT
  have hminor :
      A.submatrix rows cols =
        (B.submatrix rows id) * (C.submatrix id cols) := by
    ext i j
    simp [hfactor, Matrix.mul_apply]
  refine ⟨rows, cols, ?_⟩
  rw [hminor, Matrix.det_mul]
  exact mul_ne_zero hrows hcols

/-- Every finite rational matrix has a nonzero square minor of size
equal to its exact matrix rank. -/
theorem p3Rat_exists_maximal_nonzero_minor {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) :
    ∃ (rows : Fin A.rank → Fin m) (cols : Fin A.rank → Fin n),
      (A.submatrix rows cols).det ≠ 0 := by
  obtain ⟨B, C, hfactor⟩ := p3Rat_exists_rank_factorization A
  exact p3Rat_exists_nonsingular_pivot_of_factorization A B C
    hfactor rfl

/-- Unconditional exact-rank computation by the finite rational pivot
search: it always returns the mathematical rank. -/
theorem p3RatAutoRank_complete {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) :
    p3RatAutoRank A = some A.rank := by
  obtain ⟨B, C, hfactor⟩ := p3Rat_exists_rank_factorization A
  obtain ⟨rows, cols, hdet⟩ :=
    p3Rat_exists_nonsingular_pivot_of_factorization A B C hfactor rfl
  have hbound : A.rank ≤ min m n := by
    apply Nat.le_min
    · simpa using Matrix.rank_le_card_height A
    · simpa using Matrix.rank_le_card_width A
  exact p3RatAutoRank_eq_some_of_factorization A B C rows cols
    hbound hfactor hdet

/-- The fully automatic rational algorithm never produces none. -/
theorem p3RatAutoRank_ne_none {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) :
    p3RatAutoRank A ≠ none := by
  rw [p3RatAutoRank_complete]
  decide

/-- Whenever the exact automatic result is interpreted in ℂ, its
rank is still the computed rational rank. -/
theorem p3RatAutoRank_complete_complex {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) :
    (A.map (Rat.castHom ℂ)).rank = A.rank := by
  apply p3RatAutoRank_complex_sound A A.rank
  exact p3RatAutoRank_complete A

end MaximalRationalPivot
end P3
