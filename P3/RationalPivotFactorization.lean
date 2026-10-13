import P3.RationalSearchAdequacy

/-!
# Pivot factorization identity for a rational low-rank matrix

Suppose A = B*C factors through a dimension-r intermediate space.
If an r×r selected pivot block of A has nonzero determinant, the
canonical pivot reconstruction constructed by P3.RationalAutoPivots
is exactly A. This bridges abstract rank factorization and the
executable rank certificate generator.

Unconditional existence of suitable B, C, rows, and cols for every
rational matrix is a separate outstanding theorem.
-/

namespace P3

section RationalPivotFactorization

variable {m n r : ℕ}

theorem p3RatPivot_reconstruct_of_factorization
    (A : Matrix (Fin m) (Fin n) ℚ)
    (B : Matrix (Fin m) (Fin r) ℚ)
    (C : Matrix (Fin r) (Fin n) ℚ)
    (rows : Fin r → Fin m) (cols : Fin r → Fin n)
    (hfactor : A = B * C)
    (hdet : (A.submatrix rows cols).det ≠ 0) :
    A = p3RatPivotLeft A cols * p3RatPivotRight A rows cols := by
  let X : Matrix (Fin r) (Fin r) ℚ := B.submatrix rows id
  let Y : Matrix (Fin r) (Fin r) ℚ := C.submatrix id cols
  let P : Matrix (Fin r) (Fin r) ℚ := A.submatrix rows cols
  have hP : P = X * Y := by
    ext i j
    simp [P, X, Y, hfactor, Matrix.mul_apply]
  have hL : p3RatPivotLeft A cols = B * Y := by
    ext i j
    simp [p3RatPivotLeft, Y, hfactor, Matrix.mul_apply]
  have hR : A.submatrix rows id = X * C := by
    ext i j
    simp [X, hfactor, Matrix.mul_apply]
  have hPdet : P.det ≠ 0 := hdet
  have hXdet : X.det ≠ 0 := by
    rw [hP, Matrix.det_mul] at hPdet
    exact (mul_ne_zero_iff.mp hPdet).1
  have hPX : IsUnit X.det := isUnit_iff_ne_zero.mpr hXdet
  have hPP : IsUnit P.det := isUnit_iff_ne_zero.mpr hdet
  have hmiddle : Y * P⁻¹ * X = 1 := by
    calc
      Y * P⁻¹ * X = (X⁻¹ * X) * (Y * P⁻¹ * X) := by
        rw [Matrix.nonsing_inv_mul X hPX, Matrix.one_mul]
      _ = X⁻¹ * (X * Y) * P⁻¹ * X := by
        simp only [Matrix.mul_assoc]
      _ = X⁻¹ * (P * P⁻¹) * X := by rw [← hP]; simp only [Matrix.mul_assoc]
      _ = 1 := by
        rw [Matrix.mul_nonsing_inv P hPP]
        simp [Matrix.nonsing_inv_mul X hPX]
  have hC : p3RatPivotRight A rows cols =
      P⁻¹ * (A.submatrix rows id) := by
    simp only [p3RatPivotRight, P]
    rw [Matrix.inv_def, Ring.inverse_eq_inv]
  calc
    A = B * C := hfactor
    _ = B * ((Y * P⁻¹ * X) * C) := by rw [hmiddle, Matrix.one_mul]
    _ = (B * Y) * (P⁻¹ * (X * C)) := by
      simp only [Matrix.mul_assoc]
    _ = p3RatPivotLeft A cols * p3RatPivotRight A rows cols := by
      rw [hL, hC, hR]

/-- The generated pivot certificate is automatically accepted
when an r-dimensional factorization and a nonzero pivot exist. -/
theorem p3RatPivotAccepted_of_factorization
    (A : Matrix (Fin m) (Fin n) ℚ)
    (B : Matrix (Fin m) (Fin r) ℚ)
    (C : Matrix (Fin r) (Fin n) ℚ)
    (rows : Fin r → Fin m) (cols : Fin r → Fin n)
    (hfactor : A = B * C)
    (hdet : (A.submatrix rows cols).det ≠ 0) :
    p3RatPivotAccepted A r rows cols = true := by
  unfold p3RatPivotAccepted p3RatRankCertificateAccepted
  exact decide_eq_true
    ⟨hdet, p3RatPivot_reconstruct_of_factorization A B C
      rows cols hfactor hdet⟩

/-- Under a rank factorization and invertible pivot block, the
fully automated exhaustive search returns the exact rank. -/
theorem p3RatAutoRank_eq_some_of_factorization
    (A : Matrix (Fin m) (Fin n) ℚ)
    (B : Matrix (Fin m) (Fin r) ℚ)
    (C : Matrix (Fin r) (Fin n) ℚ)
    (rows : Fin r → Fin m) (cols : Fin r → Fin n)
    (hbound : r ≤ min m n)
    (hfactor : A = B * C)
    (hdet : (A.submatrix rows cols).det ≠ 0) :
    p3RatAutoRank A = some r :=
  p3RatAutoRank_eq_some_of_pivot A r hbound rows cols
    (p3RatPivotAccepted_of_factorization A B C rows cols hfactor hdet)

end RationalPivotFactorization
end P3
