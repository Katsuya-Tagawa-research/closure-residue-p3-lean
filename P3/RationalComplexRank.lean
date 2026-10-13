import P3.RationalAutoPivots

/-!
# Exact rational certificates yield identical complex matrix ranks

A rational matrix may be embedded entrywise into the complex numbers.
The previously Lean-certified exact rational rank certificates give the
same *complex* rank: nonzero rational determinants remain nonzero and
rational matrix factorizations remain valid after coefficient casting.

This is a rigorous conditional link toward the P3 complex Krylov
matrices, not yet a proof that every P3 dynamics has rational entries.
-/

namespace P3

section RationalComplexRank

variable {m n : ℕ}

/-- Any exact rational rank certificate remains a rank certificate over ℂ. -/
theorem p3RatRankCertificate_complex_sound
    (A : Matrix (Fin m) (Fin n) ℚ) (r : ℕ)
    (rows : Fin r → Fin m) (cols : Fin r → Fin n)
    (B : Matrix (Fin m) (Fin r) ℚ)
    (C : Matrix (Fin r) (Fin n) ℚ)
    (h : p3RatRankCertificateAccepted A r rows cols B C = true) :
    (A.map (Rat.castHom ℂ)).rank = r := by
  have hcert : (A.submatrix rows cols).det ≠ 0 ∧ A = B * C :=
    of_decide_eq_true h
  obtain ⟨hdet, hfactor⟩ := hcert
  have hdetCast : (((A.submatrix rows cols).det : ℚ) : ℂ) ≠ 0 := by
    exact_mod_cast hdet
  have hdetEq :
      ((A.map (Rat.castHom ℂ)).submatrix rows cols).det =
        (((A.submatrix rows cols).det : ℚ) : ℂ) := by
    rw [Rat.cast_det]
    rfl
  have hminor : ((A.map (Rat.castHom ℂ)).submatrix rows cols).det ≠ 0 := by
    rw [hdetEq]
    exact hdetCast
  have hcomplexFactor :
      A.map (Rat.castHom ℂ) =
        B.map (Rat.castHom ℂ) * C.map (Rat.castHom ℂ) := by
    have hf := congrArg (fun X : Matrix (Fin m) (Fin n) ℚ =>
      X.map (Rat.castHom ℂ)) hfactor
    simpa only [Matrix.map_mul] using hf
  have hlow : r ≤ (A.map (Rat.castHom ℂ)).rank := by
    calc
      r = ((A.map (Rat.castHom ℂ)).submatrix rows cols).rank := by
        exact (by simpa using (Matrix.rank_of_det_ne_zero hminor)).symm
      _ ≤ (A.map (Rat.castHom ℂ)).rank :=
        Matrix.rank_submatrix_le _ rows cols
  have hupp : (A.map (Rat.castHom ℂ)).rank ≤ r := by
    calc
      (A.map (Rat.castHom ℂ)).rank =
          (B.map (Rat.castHom ℂ) * C.map (Rat.castHom ℂ)).rank :=
        congrArg Matrix.rank hcomplexFactor
      _ ≤ (B.map (Rat.castHom ℂ)).rank := Matrix.rank_mul_le_left _ _
      _ ≤ Fintype.card (Fin r) := Matrix.rank_le_card_width _
      _ = r := Fintype.card_fin r
  exact Nat.le_antisymm hupp hlow

/-- A returned result from the executable finite pivot search
certifies the rank even when the matrix is treated as complex. -/
theorem p3RatAutoRank_complex_sound
    (A : Matrix (Fin m) (Fin n) ℚ) (r : ℕ)
    (h : p3RatAutoRank A = some r) :
    (A.map (Rat.castHom ℂ)).rank = r := by
  unfold p3RatAutoRank at h
  generalize hf : min m n = fuel at h
  induction fuel with
  | zero =>
      unfold p3RatAutoRankFuel at h
      split_ifs at h with hc
      · cases h
        obtain ⟨rows, cols, hp⟩ :
            ∃ rows : Fin 0 → Fin m, ∃ cols : Fin 0 → Fin n,
              p3RatPivotAccepted A 0 rows cols = true :=
          of_decide_eq_true hc
        exact p3RatRankCertificate_complex_sound A 0 rows cols
          (p3RatPivotLeft A cols) (p3RatPivotRight A rows cols) hp
  | succ fuel ih =>
      unfold p3RatAutoRankFuel at h
      split_ifs at h with hc
      · cases h
        obtain ⟨rows, cols, hp⟩ :
            ∃ rows : Fin (fuel+1) → Fin m, ∃ cols : Fin (fuel+1) → Fin n,
              p3RatPivotAccepted A (fuel+1) rows cols = true :=
          of_decide_eq_true hc
        exact p3RatRankCertificate_complex_sound A (fuel+1) rows cols
          (p3RatPivotLeft A cols) (p3RatPivotRight A rows cols) hp
      · exact ih h

end RationalComplexRank
end P3
