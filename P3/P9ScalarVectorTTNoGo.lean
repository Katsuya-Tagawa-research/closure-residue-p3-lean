import P3.P9TTFiniteSymbol

/-!
# Finite 1+3 -> TT no-go from quarter-turn covariance

At a nonzero spatial covector xi=e3, the stabilizer SO(2)_xi
contains the quarter-turn. On a real scalar-plus-vector input
(s,v1,v2,v3), this quarter-turn acts as diag(1,R90,1).
On TT plus/cross polarizations, a quarter-turn acts as -I2.

A linear TT map B that intertwines these actions obeys B H = -B.
Over Q, H+I4 is explicitly invertible, so B must vanish.

This is a *finite rational representation obstruction*, independent
of the physical P6/P7 response quotient. It says nothing about
whether the actual response quotient contains a spin-2 summand.
There is no new gravitational-wave prediction or general Lorentzian
continuum accessibility theorem in this module.
-/

namespace P3

/-- Quarter-turn about xi=e3 on (scalar,v1,v2,v3) coordinates. -/
def p9ScalarVectorQuarterTurnQ : Matrix (Fin 4) (Fin 4) ℚ :=
  !![(1 : ℚ), 0, 0, 0;
     0, 0, -1, 0;
     0, 1, 0, 0;
     0, 0, 0, 1]

/-- Explicit inverse of H+I. -/
def p9ScalarVectorQuarterTurnPlusOneInvQ : Matrix (Fin 4) (Fin 4) ℚ :=
  !![(1/2 : ℚ), 0, 0, 0;
     0, 1/2, 1/2, 0;
     0, -1/2, 1/2, 0;
     0, 0, 0, 1/2]

/-- The quarter-turn has no -1 eigenvector in the scalar+vector representation. -/
theorem p9ScalarVectorQuarterTurn_plus_one_right_inverse :
    (p9ScalarVectorQuarterTurnQ + 1) *
      p9ScalarVectorQuarterTurnPlusOneInvQ = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [p9ScalarVectorQuarterTurnQ,
      p9ScalarVectorQuarterTurnPlusOneInvQ,
      Matrix.mul_apply, Matrix.add_apply, Matrix.one_apply,
      Fin.sum_univ_succ] <;> decide

/-- A spin-two TT output intertwining the quarter-turn with
the scalar+vector input must vanish exactly. In particular
the linear TT response rank cannot be two. -/
theorem p9ScalarVector_tt_no_go
    (B : Matrix (Fin 2) (Fin 4) ℚ)
    (hCov : B * p9ScalarVectorQuarterTurnQ = -B) :
    B = 0 := by
  have hzero : B * (p9ScalarVectorQuarterTurnQ +
      (1 : Matrix (Fin 4) (Fin 4) ℚ)) = 0 := by
    calc
      B * (p9ScalarVectorQuarterTurnQ + 1) =
          B * p9ScalarVectorQuarterTurnQ +
            B * (1 : Matrix (Fin 4) (Fin 4) ℚ) :=
        Matrix.mul_add _ _ _
      _ = -B + B := by rw [hCov, Matrix.mul_one]
      _ = 0 := neg_add_cancel B
  calc
    B = B * (1 : Matrix (Fin 4) (Fin 4) ℚ) :=
      (Matrix.mul_one B).symm
    _ = B * ((p9ScalarVectorQuarterTurnQ +
          (1 : Matrix (Fin 4) (Fin 4) ℚ)) *
        p9ScalarVectorQuarterTurnPlusOneInvQ) := by
          rw [p9ScalarVectorQuarterTurn_plus_one_right_inverse]
    _ = (B * (p9ScalarVectorQuarterTurnQ + 1)) *
        p9ScalarVectorQuarterTurnPlusOneInvQ :=
      (Matrix.mul_assoc _ _ _).symm
    _ = 0 := by rw [hzero, Matrix.zero_mul]

end P3
