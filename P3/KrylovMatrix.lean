import P3.KrylovRank

/-!
# Explicit rectangular matrix for the finite P3 observable Krylov rank

This module upgrades the abstract finite-column linear-combination
operator in `P3.KrylovRank` to an honest finite rectangular
`Matrix`, whose columns are the coordinates of the orbit vectors
`φ^j(d_a)` in a finite ambient basis of `A V`.

No Gaussian-elimination implementation or numerical tolerance is
claimed. The basis choice and matrix rank over ℂ are noncomputable.
The main point is that the *matrix* rank exactly recovers the
original P3 observable-closure dimension.
-/

noncomputable section

namespace P3

section KrylovMatrix

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- A finite coordinate basis for the full P3 matrix algebra. -/
def p3FiniteAmbientBasis :
    Module.Basis (Fin (Module.finrank ℂ (A V))) ℂ (A V) :=
  Module.finBasis ℂ (A V)

/-- A finite rectangular Krylov matrix. Rows are ambient coordinates,
and columns are indexed by the iteration depth and diagonal seed index.
Its size is dim(A) by (k+1)*dim(D₀). -/
def p3FiniteKrylovMatrix (φ : Dynamics V) (k : ℕ) :
    Matrix (Fin (Module.finrank ℂ (A V)))
      (Fin (k + 1) × Fin (Module.finrank ℂ
        (diagonalSubmodule (V := V)))) ℂ :=
  (LinearMap.toMatrix
    (Finsupp.basisSingleOne)
    (p3FiniteAmbientBasis (V := V)))
      (p3FiniteKrylovColumnMap φ k)

/-- Every matrix entry is the ambient coordinate of a concrete
finite Krylov orbit column, rather than an unrelated presentation. -/
theorem p3FiniteKrylovMatrix_entry
    (φ : Dynamics V) (k : ℕ)
    (i : Fin (Module.finrank ℂ (A V)))
    (j : Fin (k + 1) × Fin (Module.finrank ℂ
      (diagonalSubmodule (V := V)))) :
    p3FiniteKrylovMatrix φ k i j =
      ((p3FiniteAmbientBasis (V := V)).repr
        (p3FiniteKrylovColumn φ k j)) i := by
  simp [p3FiniteKrylovMatrix, LinearMap.toMatrix_apply,
    p3FiniteKrylovColumnMap, Finsupp.coe_basisSingleOne]

/-- The rank of the explicit finite rectangular matrix equals the
rank of the actual original P3 observable Krylov closure. -/
theorem p3FiniteKrylovMatrix_rank_eq
    (φ : Dynamics V) (k : ℕ) :
    (p3FiniteKrylovMatrix φ k).rank = p3KrylovRank φ k := by
  rw [Matrix.rank_eq_finrank_range_toLin
    (p3FiniteKrylovMatrix φ k)
    (p3FiniteAmbientBasis (V := V))
    (Finsupp.basisSingleOne)]
  rw [p3FiniteKrylovMatrix, Matrix.toLin_toMatrix]
  exact p3FiniteKrylovColumnMap_rank_eq φ k

/-- Equal adjacent *matrix* ranks certify and are certified by
stabilization of the original P3 observable closure. -/
theorem p3FiniteKrylovMatrix_rank_stop_iff
    (φ : Dynamics V) (k : ℕ) :
    (p3FiniteKrylovMatrix φ (k + 1)).rank =
        (p3FiniteKrylovMatrix φ k).rank ↔
      closure φ (k + 1) = closure φ k := by
  rw [p3FiniteKrylovMatrix_rank_eq,
    p3FiniteKrylovMatrix_rank_eq]
  exact p3KrylovRank_eq_succ_iff_closure_plateau φ k

/-- Exact first observable plateau certificate directly in terms
of finite rectangular matrices. -/
theorem p3ObservableKrylovDepth_eq_of_matrix_rank_certificate
    (φ : Dynamics V) (s : ℕ)
    (hstop : (p3FiniteKrylovMatrix φ (s + 1)).rank =
      (p3FiniteKrylovMatrix φ s).rank)
    (hearlier : ∀ k < s,
      (p3FiniteKrylovMatrix φ k).rank <
        (p3FiniteKrylovMatrix φ (k + 1)).rank) :
    p3ObservableKrylovDepth φ = s := by
  apply p3ObservableKrylovDepth_eq_of_rank_certificate φ s
  · simpa only [p3FiniteKrylovMatrix_rank_eq] using hstop
  · intro k hk
    simpa only [p3FiniteKrylovMatrix_rank_eq] using hearlier k hk

end KrylovMatrix

end P3
