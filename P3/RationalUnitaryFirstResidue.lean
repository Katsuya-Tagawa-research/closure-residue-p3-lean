import P3.RationalUnitaryChannel

/-!
# First-residue and exact depth-one closure of a rational unitary channel

This file connects a normalized single-Kraus unitary quantum channel
to the ORIGINAL P3 diagonal-seed observable filtration. The rational
2×2 unitary sends E00 to an operator with a nonzero 01 coefficient.
The channel is involutive, so no further observable direction is
added after the first iterate. Accordingly, the first observable
plateau is exactly s_obs=1.

This is a statement about the standard complex-linear Heisenberg
and Schrödinger conjugation maps, which coincide for the involutive
self-adjoint U used here. The CPTP consequence of single-unitary
conjugation is standard mathematics; a separate explicit ancillary
complete-positivity theorem in Lean is not asserted in this module.
-/

noncomputable section

namespace P3

/-- The off-diagonal 01 response of the rational unitary channel
to the diagonal observable E00 is exactly 12/25. -/
theorem p3RationalReflectionChannel_E00_offdiag :
    (p3RationalReflectionChannel
      (Matrix.single (0 : Fin 2) (0 : Fin 2) (1 : ℂ))) 0 1 =
        (12 / 25 : ℂ) := by
  rw [p3RationalReflectionChannel_apply]
  norm_num [p3RationalReflectionU, Matrix.mul_apply,
    Matrix.vecMul, dotProduct, Fin.sum_univ_two, Matrix.single_apply]

/-- A physically valid unitary channel need not preserve the finite
diagonal observation subspace. -/
theorem p3RationalReflectionChannel_noninvariant :
    ¬ PreservesDiagonal (V := Fin 2) p3RationalReflectionChannel := by
  intro hpres
  let d : diagonalSubmodule (V := Fin 2) :=
    p3CanonicalDiagonalBasis (V := Fin 2) (0 : Fin 2)
  have hd : d.1 = Matrix.single (0 : Fin 2) (0 : Fin 2) (1 : ℂ) :=
    p3CanonicalDiagonalBasis_apply (V := Fin 2) (0 : Fin 2)
  have hmem : p3RationalReflectionChannel d.1 ∈
      diagonalSubmodule (V := Fin 2) := hpres d
  have hfix := delta_eq_self_of_mem_diagonalSubmodule (V := Fin 2) hmem
  have hpoint := congrArg
    (fun M : A (Fin 2) => M (0 : Fin 2) (1 : Fin 2)) hfix
  have hleft :
      delta (V := Fin 2) (p3RationalReflectionChannel d.1) 0 1 = 0 := by
    simp [delta_apply]
  have hright :
      p3RationalReflectionChannel d.1 0 1 = (12 / 25 : ℂ) := by
    rw [hd]
    exact p3RationalReflectionChannel_E00_offdiag
  have hz : (0 : ℂ) = (12 / 25 : ℂ) := calc
    0 = delta (V := Fin 2) (p3RationalReflectionChannel d.1) 0 1 :=
      hleft.symm
    _ = p3RationalReflectionChannel d.1 0 1 := hpoint
    _ = 12 / 25 := hright
  norm_num at hz

/-- First hidden-residue sector is genuinely nonzero. -/
theorem p3RationalReflectionChannel_hidden_one_ne_bot :
    hidden p3RationalReflectionChannel 1 ≠ ⊥ :=
  (noninvariant_iff_hidden_one_ne_bot p3RationalReflectionChannel).mp
    p3RationalReflectionChannel_noninvariant

/-- Involutivity ensures the diagonal-observable Krylov closure
is stationary at depth one. -/
theorem p3RationalReflectionChannel_closure_two_eq_one :
    closure p3RationalReflectionChannel 2 =
      closure p3RationalReflectionChannel 1 := by
  apply le_antisymm
  · apply Submodule.span_le.mpr
    rintro x ⟨d, n, hn, rfl⟩
    interval_cases n
    · simpa using
        (diagonalSubmodule_le_closure p3RationalReflectionChannel 1 d.property)
    · apply Submodule.subset_span
      exact ⟨d, 1, by omega, rfl⟩
    · rw [p3RationalReflectionChannel_sq]
      exact diagonalSubmodule_le_closure p3RationalReflectionChannel 1
        d.property
  · exact closure_mono p3RationalReflectionChannel (by omega)

/-- The first true observable Krylov plateau occurs precisely
at depth one, not at zero, for this unitary quantum channel. -/
theorem p3RationalReflectionChannel_depth_one :
    p3ObservableKrylovDepth p3RationalReflectionChannel = 1 := by
  apply p3ObservableKrylovDepth_eq_of_rank_certificate
    p3RationalReflectionChannel 1
  · exact (p3KrylovRank_eq_succ_iff_closure_plateau
      p3RationalReflectionChannel 1).mpr
        p3RationalReflectionChannel_closure_two_eq_one
  · intro k hk
    have hkzero : k = 0 := by omega
    subst k
    have hne : closure p3RationalReflectionChannel 1 ≠
        closure p3RationalReflectionChannel 0 := by
      intro heq
      apply p3RationalReflectionChannel_noninvariant
      intro d
      have hx : p3RationalReflectionChannel d.1 ∈
          closure p3RationalReflectionChannel 1 :=
        map_diagonal_mem_closure_one p3RationalReflectionChannel d
      rwa [heq, closure_zero] at hx
    exact Submodule.finrank_lt_finrank_of_lt
      (lt_of_le_of_ne
        (closure_mono p3RationalReflectionChannel (by omega))
        hne.symm)

end P3
