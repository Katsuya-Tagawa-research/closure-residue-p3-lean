import P3.RationalAutoPivots

/-!
# P9 finite spatial TT symbol: independent exact-rank certificate

This finite-dimensional calculation fixes a nonzero spatial covector
to xi = (0, 0, 1), using rotational covariance and rescaling.

Symmetric 2-tensor coordinates are ordered as
(q11,q22,q33,q12,q13,q23), and the TT quotient coordinates are
(q11-q22, q12). The 2x6 TT representative has exact rational rank 2.

The conformal/diffeomorphism gauge symbol on parameters
(v1,v2,v3,f) is q_ij = xi_i v_j + xi_j v_i + 2 f delta_ij.
Its image is annihilated by the TT representative.

Crucial scope: rank two of the ambient tensor TT projection is not
rank two of a CR response-to-tensor symbol. The latter requires a
separately constructed equivariant bridge and an accessibility test.
-/

namespace P3

/-- Coordinates (q11,q22,q33,q12,q13,q23) to
    (q11-q22,q12). Rank 2 means the tensor TT fiber has two
    independent polarizations in the xi=e3 frame. -/
def p9TTFiniteSymbol : Matrix (Fin 2) (Fin 6) ℚ :=
  !![(1 : ℚ), -1, 0, 0, 0, 0;
     0, 0, 0, 1, 0, 0]

/-- The exact rational TT representative has rank two.
The certificate uses a 2x2 invertible pivot at columns 0 and 3,
and checks the complete matrix reconstruction, not a floating-point
approximation or a Boolean-only runtime assertion. -/
theorem p9TTFiniteSymbol_rank_two :
    p9TTFiniteSymbol.rank = 2 := by
  exact p3RatPivotAccepted_sound
    p9TTFiniteSymbol 2
    (fun i : Fin 2 => i)
    (fun i : Fin 2 => if i = 0 then 0 else 3)
    (by decide)

/-- In the xi=e3 frame, the gauge/conformal map is
    (v1,v2,v3,f) -> (2f,2f,2v3+2f,0,v1,v2). -/
def p9ConformalGaugeSymbol : Matrix (Fin 6) (Fin 4) ℚ :=
  !![0, 0, 0, (2 : ℚ);
     0, 0, 0, 2;
     0, 0, 2, 2;
     0, 0, 0, 0;
     1, 0, 0, 0;
     0, 1, 0, 0]

/-- TT annihilates all gauge and conformal perturbations. -/
theorem p9TTFiniteSymbol_mul_gauge_zero :
    p9TTFiniteSymbol * p9ConformalGaugeSymbol = 0 := by
  decide

end P3
