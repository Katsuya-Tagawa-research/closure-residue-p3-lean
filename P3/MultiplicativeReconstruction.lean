import P3.ObservableThreePlusOne

/-!
# Phase 6.B: extension non-uniqueness versus multiplicative reconstruction

The physical unitary reflection channel has a 3-dimensional diagonal-seed
observable Krylov space, the transpose-symmetric plane. A second
complex-linear map obtained by precomposing the channel with matrix
transpose agrees on this entire plane but differs on the skew line.

For *multiplicative* complex-linear extensions, however, X and Z
are enough: their product is the skew direction J, so agreement on
the original P3 reachable plane forces equality on all M_2(C).

This module formalizes the algebraic uniqueness under the stated
multiplicativity assumption. It does not formalize complete positivity
or the multiplicative-domain theorem. A CP reconstruction corollary
requires these additional ingredients or an external mathematical
argument, and must not be labeled Lean-proven from this file.
-/

noncomputable section

namespace P3

/-- The diagonal Pauli Z observable. -/
def p3ReflectionPauliZ : A (Fin 2) :=
  !![(1 : ℂ), 0;
     0, -1]

/-- Pauli Z is in the original diagonal-seed Krylov space. -/
theorem p3ReflectionPauliZ_observable :
    p3ReflectionPauliZ ∈
      p3ObservableKrylovSpace p3RationalReflectionChannel := by
  rw [p3Reflection_observable_eq_symmetric]
  change p3ReflectionPauliZ 0 1 = p3ReflectionPauliZ 1 0
  norm_num [p3ReflectionPauliZ]

/-- The skew generator is the ordered product ZX. -/
theorem p3ReflectionSkewJ_eq_pauli_product :
    p3ReflectionSkewJ =
      p3ReflectionPauliZ * p3ReflectionSymmetricK := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [p3ReflectionSkewJ, p3ReflectionPauliZ,
      p3ReflectionSymmetricK, Matrix.mul_apply,
      Matrix.vecMul, dotProduct, Fin.sum_univ_two]

/-- The physical unitary conjugation channel is multiplicative. -/
theorem p3ReflectionChannel_mul (M N : A (Fin 2)) :
    p3RationalReflectionChannel (M * N) =
      p3RationalReflectionChannel M *
        p3RationalReflectionChannel N := by
  simp only [p3RationalReflectionChannel_apply]
  calc
    p3RationalReflectionU * (M * N) * p3RationalReflectionU =
        p3RationalReflectionU * M *
          (p3RationalReflectionU * p3RationalReflectionU) *
          N * p3RationalReflectionU := by
            rw [p3RationalReflectionU_sq]
            simp only [mul_one, mul_assoc]
    _ = (p3RationalReflectionU * M * p3RationalReflectionU) *
          (p3RationalReflectionU * N * p3RationalReflectionU) := by
            simp only [mul_assoc]

/-- A complex-linear map matching the observed plane and J is uniquely
the original physical channel, thanks to the exact 3+1 decomposition. -/
theorem p3Reflection_linear_reconstruction
    (Ψ : Dynamics (Fin 2))
    (hobs : ∀ M ∈
      p3ObservableKrylovSpace p3RationalReflectionChannel,
        Ψ M = p3RationalReflectionChannel M)
    (hJ : Ψ p3ReflectionSkewJ =
      p3RationalReflectionChannel p3ReflectionSkewJ) :
    Ψ = p3RationalReflectionChannel := by
  apply LinearMap.ext
  intro M
  obtain ⟨S, hS, c, hdec⟩ := p3Reflection_observed_plus_skew M
  calc
    Ψ M = Ψ (S + c • p3ReflectionSkewJ) := by rw [hdec]
    _ = Ψ S + c • Ψ p3ReflectionSkewJ := by
        simp only [map_add, map_smul]
    _ = p3RationalReflectionChannel S +
          c • p3RationalReflectionChannel p3ReflectionSkewJ := by
        rw [hobs S hS, hJ]
    _ = p3RationalReflectionChannel M := by
        rw [hdec]
        simp only [map_add, map_smul]

/-- Multiplicativity removes the missing skew ambiguity: knowing
the original P3 observation space uniquely determines the map. -/
theorem p3Reflection_multiplicative_reconstruction
    (Ψ : Dynamics (Fin 2))
    (hmul : ∀ M N : A (Fin 2), Ψ (M * N) = Ψ M * Ψ N)
    (hobs : ∀ M ∈
      p3ObservableKrylovSpace p3RationalReflectionChannel,
        Ψ M = p3RationalReflectionChannel M) :
    Ψ = p3RationalReflectionChannel := by
  have hZ := hobs p3ReflectionPauliZ p3ReflectionPauliZ_observable
  have hX := hobs p3ReflectionSymmetricK p3ReflectionSymmetricK_observable
  have hJ : Ψ p3ReflectionSkewJ =
      p3RationalReflectionChannel p3ReflectionSkewJ := by
    calc
      Ψ p3ReflectionSkewJ =
          Ψ (p3ReflectionPauliZ * p3ReflectionSymmetricK) := by
            rw [p3ReflectionSkewJ_eq_pauli_product]
      _ = Ψ p3ReflectionPauliZ * Ψ p3ReflectionSymmetricK :=
        hmul _ _
      _ = p3RationalReflectionChannel p3ReflectionPauliZ *
          p3RationalReflectionChannel p3ReflectionSymmetricK := by
            rw [hZ, hX]
      _ = p3RationalReflectionChannel
          (p3ReflectionPauliZ * p3ReflectionSymmetricK) :=
        (p3ReflectionChannel_mul _ _).symm
      _ = p3RationalReflectionChannel p3ReflectionSkewJ := by
        rw [p3ReflectionSkewJ_eq_pauli_product]
  exact p3Reflection_linear_reconstruction Ψ hobs hJ

/-- Ordinary matrix transpose is complex linear, but not
asserted completely positive. -/
def p3ReflectionTranspose : Dynamics (Fin 2) where
  toFun M := M.transpose
  map_add' M N := by
    ext i j
    rfl
  map_smul' c M := by
    ext i j
    rfl

/-- Every P3-observable reachable symmetric matrix is fixed by transpose. -/
theorem p3ReflectionTranspose_fixes_observed
    (M : A (Fin 2))
    (hM : M ∈ p3ObservableKrylovSpace p3RationalReflectionChannel) :
    p3ReflectionTranspose M = M := by
  have hs := p3Reflection_observable_le_symmetric hM
  change M 0 1 = M 1 0 at hs
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [p3ReflectionTranspose, Matrix.transpose_apply, hs]

/-- A distinct complex-linear extension of the observed restriction. -/
def p3ReflectionTransposedExtension : Dynamics (Fin 2) :=
  p3RationalReflectionChannel.comp p3ReflectionTranspose

/-- Two linear maps can agree on every reachable observation. -/
theorem p3ReflectionTransposedExtension_agrees
    (M : A (Fin 2))
    (hM : M ∈ p3ObservableKrylovSpace p3RationalReflectionChannel) :
    p3ReflectionTransposedExtension M =
      p3RationalReflectionChannel M := by
  change p3RationalReflectionChannel (p3ReflectionTranspose M) =
    p3RationalReflectionChannel M
  rw [p3ReflectionTranspose_fixes_observed M hM]

/-- Transpose changes the sign of the unobserved skew direction. -/
theorem p3ReflectionTranspose_skew :
    p3ReflectionTranspose p3ReflectionSkewJ =
      -p3ReflectionSkewJ := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [p3ReflectionTranspose, p3ReflectionSkewJ,
      Matrix.transpose_apply]

/-- The two extensions differ on the unobserved direction J. -/
theorem p3ReflectionTransposedExtension_ne :
    p3ReflectionTransposedExtension ≠
      p3RationalReflectionChannel := by
  intro h
  have hJ := congrArg (fun f : Dynamics (Fin 2) =>
    f p3ReflectionSkewJ) h
  have ht : p3ReflectionTransposedExtension p3ReflectionSkewJ =
      p3ReflectionSkewJ := by
    change p3RationalReflectionChannel
      (p3ReflectionTranspose p3ReflectionSkewJ) =
        p3ReflectionSkewJ
    rw [p3ReflectionTranspose_skew]
    simp [p3ReflectionSkewJ_eigen_neg]
  have heq := congrArg
    (fun M : A (Fin 2) => M (0 : Fin 2) (1 : Fin 2)) hJ
  rw [ht, p3ReflectionSkewJ_eigen_neg] at heq
  norm_num [p3ReflectionSkewJ] at heq

end P3
