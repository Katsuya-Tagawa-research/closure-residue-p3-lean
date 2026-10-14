import P3.P9TTFiniteSymbol

/-!
# P9 quadratic spin-two: a finite bilinear rank-two witness

This independent rational model defines the SO(3)-natural symmetric
trace-free quadratic tensor Q(u,v) = u⊗v + v⊗u - (2/3)(u·v)I.
Two specified transverse bilinear inputs are sent to independent
plus/cross coordinates by the verified finite TT symbol.

Crucial scope: this is an abstract algebraic construction from a
three-dimensional vector representation. It is NOT derived from the
actual P6 CR graph-divergence Hessian, physical controls, P7 structural
symmetry completion, or a continuum response symbol.
-/

namespace P3

/-- Standard basis vectors in the Euclidean three-space. -/
def p9SpinTwoE1 : Fin 3 → ℚ := fun i => if i = 0 then 1 else 0
def p9SpinTwoE2 : Fin 3 → ℚ := fun i => if i = 1 then 1 else 0

/-- A symmetric trace-free bilinear tensor-valued candidate. -/
def p9SpinTwoQuadratic (u v : Fin 3 → ℚ) :
    Matrix (Fin 3) (Fin 3) ℚ :=
  fun i j =>
    u i * v j + v i * u j -
      (2 / 3 : ℚ) *
        (u 0 * v 0 + u 1 * v 1 + u 2 * v 2) *
        (if i = j then 1 else 0)

/-- The tensor is symmetric in the spatial matrix coordinates. -/
theorem p9SpinTwoQuadratic_symmetric
    (u v : Fin 3 → ℚ) (i j : Fin 3) :
    p9SpinTwoQuadratic u v i j =
      p9SpinTwoQuadratic u v j i := by
  by_cases h : i = j
  · subst j
    rfl
  · have hj : j ≠ i := Ne.symm h
    simp [p9SpinTwoQuadratic, h, hj]
    ring

/-- The three diagonal coordinates sum to zero. -/
theorem p9SpinTwoQuadratic_trace_zero
    (u v : Fin 3 → ℚ) :
    p9SpinTwoQuadratic u v 0 0 +
      p9SpinTwoQuadratic u v 1 1 +
      p9SpinTwoQuadratic u v 2 2 = 0 := by
  simp [p9SpinTwoQuadratic]
  ring

/-- Tensor coordinate order: q11,q22,q33,q12,q13,q23. -/
def p9SpinTwoCoordinates (q : Matrix (Fin 3) (Fin 3) ℚ) :
    Fin 6 → ℚ :=
  ![q 0 0, q 1 1, q 2 2, q 0 1, q 0 2, q 1 2]

/-- The two columns use Q(e1,e1) and Q(e1,e2). -/
def p9SpinTwoQuadraticWitness : Matrix (Fin 6) (Fin 2) ℚ :=
  fun i j =>
    if j = 0 then
      p9SpinTwoCoordinates
        (p9SpinTwoQuadratic p9SpinTwoE1 p9SpinTwoE1) i
    else
      p9SpinTwoCoordinates
        (p9SpinTwoQuadratic p9SpinTwoE1 p9SpinTwoE2) i

/-- Explicit plus/cross output under the previously verified TT symbol. -/
theorem p9SpinTwoTTWitness_eq :
    p9TTFiniteSymbol * p9SpinTwoQuadraticWitness =
      !![(2 : ℚ), 0; 0, 1] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [p9TTFiniteSymbol, p9SpinTwoQuadraticWitness,
      p9SpinTwoCoordinates, p9SpinTwoQuadratic,
      p9SpinTwoE1, p9SpinTwoE2,
      Matrix.mul_apply, Fin.sum_univ_succ] <;> simp_all <;> norm_num

/-- Abstract quadratic response achieves two independent TT directions. -/
theorem p9SpinTwoTTWitness_rank_two :
    (p9TTFiniteSymbol * p9SpinTwoQuadraticWitness).rank = 2 := by
  have hdet :
      (p9TTFiniteSymbol * p9SpinTwoQuadraticWitness).det ≠ 0 := by
    rw [p9SpinTwoTTWitness_eq]
    norm_num [Matrix.det_fin_two]
  simpa using Matrix.rank_of_det_ne_zero hdet

end P3
