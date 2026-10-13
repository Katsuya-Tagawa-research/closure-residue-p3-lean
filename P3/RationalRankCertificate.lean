import P3.CanonicalSeeds

/-!
# Executable rational rank certificate checker for finite matrices

This first algorithmic bridge supplies a decidable, exact certificate
checker for the rank of an arbitrary rectangular matrix over ℚ.

A proposed rank r is certified by:
* a nonzero determinant of an r × r minor (lower rank bound);
* an exact factorization A = B * C through Fin r (upper rank bound).

Both predicates are decidable using rational arithmetic. The checker
is executable; its mathematical soundness is proven in Lean.
This module does NOT claim that certificates are automatically
produced for arbitrary inputs, nor that the full Krylov stopping
algorithm is already executable.
-/

namespace P3

section RationalRankCertificate

variable {m n : Type*} [Fintype m] [Fintype n]
  [DecidableEq m] [DecidableEq n]

/-- A finite, exactly checkable rank certificate for a rational
rectangular matrix. The row and column maps identify an invertible
square minor, while B*C factors through dimension r. -/
def p3RatRankCertificateAccepted
    (A : Matrix m n ℚ) (r : ℕ)
    (rows : Fin r → m) (cols : Fin r → n)
    (B : Matrix m (Fin r) ℚ) (C : Matrix (Fin r) n ℚ) : Bool :=
  decide ((A.submatrix rows cols).det ≠ 0 ∧ A = B * C)

/-- If the executable checker accepts, then the mathematical
matrix rank really is r. There are no approximate comparisons. -/
theorem p3RatRankCertificate_sound
    (A : Matrix m n ℚ) (r : ℕ)
    (rows : Fin r → m) (cols : Fin r → n)
    (B : Matrix m (Fin r) ℚ) (C : Matrix (Fin r) n ℚ)
    (h : p3RatRankCertificateAccepted A r rows cols B C = true) :
    A.rank = r := by
  have hcert : (A.submatrix rows cols).det ≠ 0 ∧ A = B * C := by
    exact of_decide_eq_true h
  obtain ⟨hdet, hfactor⟩ := hcert
  have hminor : (A.submatrix rows cols).rank = r := by
    simpa using Matrix.rank_of_det_ne_zero hdet
  have hlow : r ≤ A.rank := by
    calc
      r = (A.submatrix rows cols).rank := hminor.symm
      _ ≤ A.rank := Matrix.rank_submatrix_le A rows cols
  have hupp : A.rank ≤ r := by
    calc
      A.rank = (B * C).rank := congrArg Matrix.rank hfactor
      _ ≤ B.rank := Matrix.rank_mul_le_left B C
      _ ≤ Fintype.card (Fin r) := Matrix.rank_le_card_width B
      _ = r := Fintype.card_fin r
  exact Nat.le_antisymm hupp hlow

/-- The checker can compute its answer exactly on a concrete
two-by-two identity matrix. -/
example : p3RatRankCertificateAccepted
    (1 : Matrix (Fin 2) (Fin 2) ℚ) 2
    (fun i => i) (fun i => i)
    (1 : Matrix (Fin 2) (Fin 2) ℚ)
    (1 : Matrix (Fin 2) (Fin 2) ℚ) = true := by
  change decide
    (((1 : Matrix (Fin 2) (Fin 2) ℚ).det ≠ 0) ∧
      (1 : Matrix (Fin 2) (Fin 2) ℚ) = 1 * 1) = true
  simp

/-- Proof of the rank attached to the concrete computed certificate. -/
example : (1 : Matrix (Fin 2) (Fin 2) ℚ).rank = 2 := by
  exact p3RatRankCertificate_sound
    (1 : Matrix (Fin 2) (Fin 2) ℚ) 2
    (fun i => i) (fun i => i)
    (1 : Matrix (Fin 2) (Fin 2) ℚ)
    (1 : Matrix (Fin 2) (Fin 2) ℚ) (by
      change decide
        (((1 : Matrix (Fin 2) (Fin 2) ℚ).det ≠ 0) ∧
          (1 : Matrix (Fin 2) (Fin 2) ℚ) = 1 * 1) = true
      simp)

end RationalRankCertificate

end P3

/- Runtime smoke-test of the rational certificate checker. -/
#eval P3.p3RatRankCertificateAccepted
  (1 : Matrix (Fin 2) (Fin 2) ℚ) 2
  (fun i => i) (fun i => i)
  (1 : Matrix (Fin 2) (Fin 2) ℚ)
  (1 : Matrix (Fin 2) (Fin 2) ℚ)
