import P3.RationalUnitaryKrylov

/-!
# Phase 6.A: an invariant observation-invisible direction

For the physical rational reflection channel, define the complex-linear
subspace of transpose-symmetric 2-by-2 matrices. The diagonal P3 seeds
lie in this subspace and the physical channel preserves it. Therefore
the *actual* P3 observable Krylov closure is contained in it.

The independent skew direction J=E01-E10 is not in that reachable
closure, yet the channel sends J to -J.

"Unreachable from the selected diagonal seeds" is a precise linear
statement. This does not assert that J is a P3 hidden-residue vector,
a universally inaccessible physical observable, or a full P11
generative-completeness theorem.
-/

noncomputable section

namespace P3

/-- The three-coordinate transpose-symmetric linear subspace. -/
def p3ReflectionSymmetric : Submodule ℂ (A (Fin 2)) where
  carrier := {M | M 0 1 = M 1 0}
  zero_mem' := by simp
  add_mem' := by
    intro M N hM hN
    simp only [Set.mem_setOf_eq, Matrix.add_apply]
    rw [hM, hN]
  smul_mem' := by
    intro c M hM
    simp only [Set.mem_setOf_eq, Matrix.smul_apply]
    rw [hM]

/-- The observed diagonal seeds are symmetric. -/
theorem p3Reflection_diagonal_le_symmetric :
    diagonalSubmodule (V := Fin 2) ≤ p3ReflectionSymmetric := by
  intro M hM
  change M 0 1 = M 1 0
  have h := delta_eq_self_of_mem_diagonalSubmodule (V := Fin 2) hM
  have h01 := congrArg (fun X : A (Fin 2) => X 0 1) h
  have h10 := congrArg (fun X : A (Fin 2) => X 1 0) h
  simp [delta_apply] at h01 h10
  exact h01.symm.trans h10

/-- Transpose-symmetry is preserved by the physical reflection channel. -/
theorem p3Reflection_symmetric_invariant
    (M : A (Fin 2)) (hM : M ∈ p3ReflectionSymmetric) :
    p3RationalReflectionChannel M ∈ p3ReflectionSymmetric := by
  change M 0 1 = M 1 0 at hM
  change (p3RationalReflectionChannel M) 0 1 =
    (p3RationalReflectionChannel M) 1 0
  rw [p3RationalReflectionChannel_apply]
  simp [Matrix.mul_apply, Fin.sum_univ_two, p3RationalReflectionU, hM]
  <;> ring

/-- Every diagonal-seed orbit lies in the symmetric subspace. -/
theorem p3Reflection_observable_le_symmetric :
    p3ObservableKrylovSpace p3RationalReflectionChannel ≤
      p3ReflectionSymmetric := by
  apply p3ObservableKrylovSpace_le_of_invariant
  · exact p3Reflection_diagonal_le_symmetric
  · intro M hM
    exact p3Reflection_symmetric_invariant M hM

/-- The fixed skew matrix J=E01-E10. -/
def p3ReflectionSkewJ : A (Fin 2) :=
  !![(0 : ℂ), 1;
     -1, 0]

/-- J cannot be produced from the chosen diagonal observation seeds. -/
theorem p3ReflectionSkewJ_not_symmetric :
    p3ReflectionSkewJ ∉ p3ReflectionSymmetric := by
  intro hJ
  change p3ReflectionSkewJ 0 1 = p3ReflectionSkewJ 1 0 at hJ
  norm_num [p3ReflectionSkewJ] at hJ

/-- In particular J lies outside the true P3 observable Krylov space. -/
theorem p3ReflectionSkewJ_not_observable :
    p3ReflectionSkewJ ∉
      p3ObservableKrylovSpace p3RationalReflectionChannel := by
  intro hJ
  exact p3ReflectionSkewJ_not_symmetric
    (p3Reflection_observable_le_symmetric hJ)

/-- The unreachable direction is dynamically persistent, with eigenvalue -1. -/
theorem p3ReflectionSkewJ_eigen_neg :
    p3RationalReflectionChannel p3ReflectionSkewJ =
      -p3ReflectionSkewJ := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [p3RationalReflectionChannel_apply,
      p3RationalReflectionU, p3ReflectionSkewJ,
      Matrix.mul_apply, Fin.sum_univ_two]

end P3
