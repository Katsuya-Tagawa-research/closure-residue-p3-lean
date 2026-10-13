import P3.RationalPivotFactorization

/-!
# Universal finite rational rank factorization

Every finite rational rectangular matrix A of matrix rank r admits a
factorization A = B*C through an intermediate space of dimension r.

Construction: factor the associated linear map through its image and
identify that image, of dimension r, with Fin r → ℚ. Map the two
linear factors back to matrices with LinearMap.toMatrix'.

This proves the *rank factorization existence* half of the maximal-
pivot certificate theorem. Existence of a nonzero r×r row/column
minor is a separate outstanding step.
-/

noncomputable section

namespace P3

section UniversalRationalRankFactorization

/-- An arbitrary rectangular rational matrix factors through
the dimension of its image, which is exactly its matrix rank. -/
theorem p3Rat_exists_rank_factorization {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) :
    ∃ (B : Matrix (Fin m) (Fin A.rank) ℚ)
      (C : Matrix (Fin A.rank) (Fin n) ℚ),
      A = B * C := by
  let f : (Fin n → ℚ) →ₗ[ℚ] (Fin m → ℚ) := A.mulVecLin
  let W : Submodule ℚ (Fin m → ℚ) := LinearMap.range f
  have hdim : Module.finrank ℚ (Fin A.rank → ℚ) = Module.finrank ℚ W := by
    simp only [Module.finrank_pi, Fintype.card_fin]
    rfl
  let e : (Fin A.rank → ℚ) ≃ₗ[ℚ] W :=
    LinearEquiv.ofFinrankEq _ _ hdim
  let g : (Fin A.rank → ℚ) →ₗ[ℚ] (Fin m → ℚ) :=
    W.subtype.comp e.toLinearMap
  let h : (Fin n → ℚ) →ₗ[ℚ] (Fin A.rank → ℚ) :=
    e.symm.toLinearMap.comp f.rangeRestrict
  have hcomp : g.comp h = f := by
    apply LinearMap.ext
    intro v
    simp [g, h, f, W, LinearMap.comp_apply]
  refine ⟨LinearMap.toMatrix' g, LinearMap.toMatrix' h, ?_⟩
  have hA : LinearMap.toMatrix' f = A := by
    change LinearMap.toMatrix' (Matrix.toLin' A) = A
    exact LinearMap.toMatrix'_toLin' A
  calc
    A = LinearMap.toMatrix' f := hA.symm
    _ = LinearMap.toMatrix' (g.comp h) := congrArg LinearMap.toMatrix' hcomp.symm
    _ = LinearMap.toMatrix' g * LinearMap.toMatrix' h := LinearMap.toMatrix'_comp g h

/-- The universal factorization also provides the exact value of
its intermediate dimension, without a basis-specific rank hypothesis. -/
theorem p3Rat_exists_factorization_with_rank {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) :
    ∃ (r : ℕ) (B : Matrix (Fin m) (Fin r) ℚ)
      (C : Matrix (Fin r) (Fin n) ℚ),
      A = B * C ∧ r = A.rank := by
  obtain ⟨B, C, h⟩ := p3Rat_exists_rank_factorization A
  exact ⟨A.rank, B, C, h, rfl⟩

end UniversalRationalRankFactorization
end P3
