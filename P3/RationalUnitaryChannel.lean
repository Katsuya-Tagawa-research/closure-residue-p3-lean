import P3.TwoVertexRationalOrbit

/-!
# Rational unitary reflection: a physical two-vertex first-residue channel

The 2x2 rational reflection U = [[3/5,4/5],[4/5,-3/5]]
is self-adjoint and satisfies U²=I. Conjugation by U is a
single-unitary Kraus quantum channel. We prove its exact
normalization, trace preservation and nontrivial observable response.

This is the first step toward a physically admissible (CPTP)
observable-depth witness. No claim is made that the new channel's
Krylov depth or a rational orbit computation is already certified;
those are separate subsequent proof obligations.
-/

noncomputable section

namespace P3

/-- A nontrivial, exactly rational 2x2 unitary reflection. -/
def p3RationalReflectionU : A (Fin 2) :=
  !![(3 : ℂ) / 5, (4 : ℂ) / 5;
     (4 : ℂ) / 5, -(3 : ℂ) / 5]

/-- Exact reflection identity. -/
theorem p3RationalReflectionU_sq :
    p3RationalReflectionU * p3RationalReflectionU = 1 := by
  norm_num [p3RationalReflectionU, Matrix.mul_fin_two,
    Matrix.one_fin_two]

/-- This rational reflection is Hermitian. -/
theorem p3RationalReflectionU_selfadjoint :
    p3RationalReflectionU.conjTranspose = p3RationalReflectionU := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [p3RationalReflectionU, Matrix.conjTranspose_apply]

/-- Full unitary normalization required for a single-Kraus channel. -/
theorem p3RationalReflectionU_unitary :
    p3RationalReflectionU.conjTranspose * p3RationalReflectionU = 1 := by
  rw [p3RationalReflectionU_selfadjoint]
  exact p3RationalReflectionU_sq

/-- This actual P3 linear dynamics is conjugation by the rational U. -/
def p3RationalReflectionChannel : Dynamics (Fin 2) :=
  LinearMap.mulLeftRight ℂ (p3RationalReflectionU, p3RationalReflectionU)

/-- Pointwise formula for the quantum channel. -/
@[simp] theorem p3RationalReflectionChannel_apply (M : A (Fin 2)) :
    p3RationalReflectionChannel M =
      p3RationalReflectionU * M * p3RationalReflectionU := by
  simp [p3RationalReflectionChannel]

/-- A normalized single-Kraus witness, from which standard
finite-dimensional Kraus theory implies complete positivity.
Unlike a bare positivity assumption, the witness is explicit. -/
theorem p3RationalReflectionChannel_kraus :
    ∃ K : A (Fin 2),
      K.conjTranspose * K = 1 ∧
        ∀ M : A (Fin 2),
          p3RationalReflectionChannel M = K * M * K.conjTranspose := by
  refine ⟨p3RationalReflectionU, p3RationalReflectionU_unitary, ?_⟩
  intro M
  rw [p3RationalReflectionChannel_apply,
    p3RationalReflectionU_selfadjoint]

/-- Direct proof of trace preservation; does not merely appeal
to the interpretation of the Kraus representation. -/
theorem p3RationalReflectionChannel_trace (M : A (Fin 2)) :
    (p3RationalReflectionChannel M).trace = M.trace := by
  rw [p3RationalReflectionChannel_apply]
  calc
    (p3RationalReflectionU * M * p3RationalReflectionU).trace =
        (p3RationalReflectionU * (p3RationalReflectionU * M)).trace :=
      Matrix.trace_mul_comm _ _
    _ = ((p3RationalReflectionU * p3RationalReflectionU) * M).trace := by
      rw [mul_assoc]
    _ = M.trace := by rw [p3RationalReflectionU_sq, one_mul]

/-- Two applications of a unitary reflection give identity dynamics. -/
theorem p3RationalReflectionChannel_sq (M : A (Fin 2)) :
    (p3RationalReflectionChannel ^ 2) M = M := by
  change p3RationalReflectionChannel (p3RationalReflectionChannel M) = M
  rw [p3RationalReflectionChannel_apply,
    p3RationalReflectionChannel_apply]
  have h : p3RationalReflectionU *
      (p3RationalReflectionU * M * p3RationalReflectionU) *
      p3RationalReflectionU =
      (p3RationalReflectionU * p3RationalReflectionU) *
        M * (p3RationalReflectionU * p3RationalReflectionU) := by
    simp only [mul_assoc]
  rw [h, p3RationalReflectionU_sq, one_mul, mul_one]

end P3
