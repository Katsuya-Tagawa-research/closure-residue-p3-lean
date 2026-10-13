import P3.RationalRankCertificate

/-!
# Finite exhaustive pivot search for exact rational matrix rank

For any rectangular matrix over ℚ, enumerate all square pivot minors
of a proposed size r and synthesize an exact rational factorization
using the adjugate and determinant of each candidate pivot.

The search and all candidate evaluations are executable. Whenever it
returns a rank, the answer is mathematically sound via the previously
audited certificate validator.

Completeness of the automatic search for all rational matrices is NOT
claimed in this module; that is a separate algebraic theorem and audit.
Likewise this does not yet compute complex-valued P3 dynamics.
-/

namespace P3

section RationalAutomaticPivots

/-- A candidate left factor consists of the chosen pivot columns. -/
def p3RatPivotLeft {m n r : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ)
    (cols : Fin r → Fin n) : Matrix (Fin m) (Fin r) ℚ :=
  A.submatrix id cols

/-- Proposed right factor, formed by the adjugate formula for
the inverse of the pivot minor, followed by its selected rows.
The formula is evaluated exactly, even for a singular pivot;
the checker rejects singular pivots separately. -/
def p3RatPivotRight {m n r : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ)
    (rows : Fin r → Fin m) (cols : Fin r → Fin n) :
    Matrix (Fin r) (Fin n) ℚ :=
  (((A.submatrix rows cols).det)⁻¹ •
    (A.submatrix rows cols).adjugate) *
    (A.submatrix rows id)

/-- A candidate pivot minor passes if its determinant is nonzero
and its canonical rational factorization reconstructs A exactly. -/
def p3RatPivotAccepted {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) (r : ℕ)
    (rows : Fin r → Fin m) (cols : Fin r → Fin n) : Bool :=
  p3RatRankCertificateAccepted A r rows cols
    (p3RatPivotLeft A cols)
    (p3RatPivotRight A rows cols)

/-- If a generated pivot candidate is accepted, its rank is exact. -/
theorem p3RatPivotAccepted_sound {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) (r : ℕ)
    (rows : Fin r → Fin m) (cols : Fin r → Fin n)
    (h : p3RatPivotAccepted A r rows cols = true) :
    A.rank = r :=
  p3RatRankCertificate_sound A r rows cols
    (p3RatPivotLeft A cols)
    (p3RatPivotRight A rows cols) h

/-- Exhaustively check every finite pair of pivot-index maps.
This is a genuine finite computation: no arbitrary input witness
is needed to run the search. -/
def p3RatAutoRankAt {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) (r : ℕ) : Bool :=
  decide (∃ rows : Fin r → Fin m, ∃ cols : Fin r → Fin n,
    p3RatPivotAccepted A r rows cols = true)

/-- The automatic finite pivot search never reports a false rank. -/
theorem p3RatAutoRankAt_sound {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) (r : ℕ)
    (h : p3RatAutoRankAt A r = true) : A.rank = r := by
  obtain ⟨rows, cols, hc⟩ :
      ∃ rows : Fin r → Fin m, ∃ cols : Fin r → Fin n,
        p3RatPivotAccepted A r rows cols = true :=
    of_decide_eq_true h
  exact p3RatPivotAccepted_sound A r rows cols hc

/-- Search possible ranks in descending order up to a finite bound.
If no valid rational certificate is found, return none. -/
def p3RatAutoRankFuel {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) : (fuel : ℕ) → Option ℕ
  | 0 => if p3RatAutoRankAt A 0 then some 0 else none
  | fuel + 1 =>
      if p3RatAutoRankAt A (fuel + 1) then some (fuel + 1)
      else p3RatAutoRankFuel A fuel

/-- Any result returned by bounded automatic pivot search
equals the mathematical rank of A. -/
theorem p3RatAutoRankFuel_sound {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ)
    (fuel r : ℕ)
    (h : p3RatAutoRankFuel A fuel = some r) :
    A.rank = r := by
  induction fuel with
  | zero =>
      unfold p3RatAutoRankFuel at h
      split_ifs at h with hc
      · cases h
        exact p3RatAutoRankAt_sound A 0 (by simpa using hc)
      · cases h
  | succ fuel ih =>
      unfold p3RatAutoRankFuel at h
      split_ifs at h with hc
      · cases h
        exact p3RatAutoRankAt_sound A (fuel + 1) (by simpa using hc)
      · exact ih h

/-- A total executable search procedure returning an optional rank.
The bound is the minimum of the number of rows and columns. -/
def p3RatAutoRank {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) : Option ℕ :=
  p3RatAutoRankFuel A (min m n)

/-- Whenever the executable search yields a value, that value
is the correct rank (without any floating point thresholds). -/
theorem p3RatAutoRank_sound {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) (r : ℕ)
    (h : p3RatAutoRank A = some r) : A.rank = r :=
  p3RatAutoRankFuel_sound A (min m n) r h

end RationalAutomaticPivots
end P3

/-!
Executable examples to exercise automatically generated certificates.
The matrix with two identical nonzero columns has rank one.
-/

#eval P3.p3RatAutoRank (1 : Matrix (Fin 2) (Fin 2) ℚ)
#eval P3.p3RatAutoRank (0 : Matrix (Fin 2) (Fin 2) ℚ)
#eval P3.p3RatAutoRank (Matrix.of (fun i : Fin 2 => fun j : Fin 2 =>
  if i = 0 then (if j = 0 then (1 : ℚ) else 2)
  else (if j = 0 then (3 : ℚ) else 6)))
