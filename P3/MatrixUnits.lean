import P3.KrylovMatrix

/-!
# Matrix-unit coordinates for finite observable Krylov closure

In P3.KrylovMatrix the ambient rows were indexed by an abstract Fin
basis. Here the rows are canonically indexed by ordered vertex pairs
(x,y), using the standard matrix units E_xy.

The diagonal-seed basis remains an abstract finite basis, and complex
matrix rank here is a theorem-level quantity, not executable certified
row reduction.
-/

noncomputable section

namespace P3

section MatrixUnits

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- The standard matrix-unit basis E_xy of A = Matrix V V ℂ. -/
def p3MatrixUnitBasis : Module.Basis (V × V) ℂ (A V) :=
  Matrix.stdBasis ℂ V V

/-- The standard basis vectors are literally matrix units E_xy. -/
theorem p3MatrixUnitBasis_apply (x y : V) :
    p3MatrixUnitBasis (V := V) (x, y) =
      Matrix.single x y (1 : ℂ) := by
  exact Matrix.stdBasis_eq_single (R := ℂ) x y

/-- Canonically row-indexed rectangular observable Krylov matrix.
The row (x,y) denotes the matrix-unit coordinate E_xy, while each
column denotes an iterate of one diagonal seed. -/
def p3MatrixUnitKrylovMatrix (φ : Dynamics V) (k : ℕ) :
    Matrix (V × V)
      (Fin (k + 1) × Fin (Module.finrank ℂ
        (diagonalSubmodule (V := V)))) ℂ :=
  (LinearMap.toMatrix
    (Finsupp.basisSingleOne)
    (p3MatrixUnitBasis (V := V)))
      (p3FiniteKrylovColumnMap φ k)

/-- The coordinate of each orbit column in the actual matrix-unit basis. -/
theorem p3MatrixUnitKrylovMatrix_entry
    (φ : Dynamics V) (k : ℕ)
    (x y : V)
    (j : Fin (k + 1) × Fin (Module.finrank ℂ
      (diagonalSubmodule (V := V)))) :
    p3MatrixUnitKrylovMatrix φ k (x, y) j =
      ((p3MatrixUnitBasis (V := V)).repr
        (p3FiniteKrylovColumn φ k j)) (x, y) := by
  simp [p3MatrixUnitKrylovMatrix, LinearMap.toMatrix_apply,
    p3FiniteKrylovColumnMap, Finsupp.coe_basisSingleOne]

/-- The standard matrix-unit coordinates are exactly the raw
matrix entries: the E_xy coefficient of M is M[x,y]. -/
theorem p3MatrixUnitBasis_repr_entry
    (M : A V) (x y : V) :
    ((p3MatrixUnitBasis (V := V)).repr M) (x, y) = M x y := by
  refine (p3MatrixUnitBasis (V := V)).repr_apply_eq
    (fun N ij => N ij.1 ij.2) ?_ ?_ ?_ M (x, y)
  · intro N N'
    funext ⟨a, b⟩
    simp
  · intro c N
    funext ⟨a, b⟩
    simp
  · intro ⟨i, j⟩
    funext ⟨a, b⟩
    simp [p3MatrixUnitBasis_apply, Matrix.single_apply,
      Finsupp.single_apply, Prod.mk.injEq]

/-- Every Krylov-matrix entry is the actual (x,y) matrix coefficient
of the corresponding P3 diagonal-seed orbit vector. -/
theorem p3MatrixUnitKrylovMatrix_entry_raw
    (φ : Dynamics V) (k : ℕ)
    (x y : V)
    (j : Fin (k + 1) × Fin (Module.finrank ℂ
      (diagonalSubmodule (V := V)))) :
    p3MatrixUnitKrylovMatrix φ k (x, y) j =
      (p3FiniteKrylovColumn φ k j) x y := by
  rw [p3MatrixUnitKrylovMatrix_entry,
    p3MatrixUnitBasis_repr_entry]

/-- Matrix-unit coordinate rank is the exact original P3 closure rank. -/
theorem p3MatrixUnitKrylovMatrix_rank_eq
    (φ : Dynamics V) (k : ℕ) :
    (p3MatrixUnitKrylovMatrix φ k).rank = p3KrylovRank φ k := by
  rw [Matrix.rank_eq_finrank_range_toLin
    (p3MatrixUnitKrylovMatrix φ k)
    (p3MatrixUnitBasis (V := V))
    (Finsupp.basisSingleOne)]
  rw [p3MatrixUnitKrylovMatrix, Matrix.toLin_toMatrix]
  exact p3FiniteKrylovColumnMap_rank_eq φ k

/-- Matrix-unit coordinates have the same rank as the earlier
abstract-Fin-coordinate rectangular matrix. -/
theorem p3MatrixUnitKrylovMatrix_rank_eq_finite
    (φ : Dynamics V) (k : ℕ) :
    (p3MatrixUnitKrylovMatrix φ k).rank =
      (p3FiniteKrylovMatrix φ k).rank := by
  rw [p3MatrixUnitKrylovMatrix_rank_eq, p3FiniteKrylovMatrix_rank_eq]

/-- Equal successive matrix-unit ranks are equivalent to observable
closure stabilization of the *original* P3 filtration. -/
theorem p3MatrixUnitKrylovMatrix_rank_stop_iff
    (φ : Dynamics V) (k : ℕ) :
    (p3MatrixUnitKrylovMatrix φ (k + 1)).rank =
        (p3MatrixUnitKrylovMatrix φ k).rank ↔
      closure φ (k + 1) = closure φ k := by
  rw [p3MatrixUnitKrylovMatrix_rank_eq, p3MatrixUnitKrylovMatrix_rank_eq]
  exact p3KrylovRank_eq_succ_iff_closure_plateau φ k

/-- A finite matrix-unit rank certificate determines the exact
first observable plateau, rather than an arbitrary upper bound. -/
theorem p3ObservableKrylovDepth_eq_of_matrix_unit_certificate
    (φ : Dynamics V) (s : ℕ)
    (hstop : (p3MatrixUnitKrylovMatrix φ (s + 1)).rank =
      (p3MatrixUnitKrylovMatrix φ s).rank)
    (hearlier : ∀ k < s,
      (p3MatrixUnitKrylovMatrix φ k).rank <
        (p3MatrixUnitKrylovMatrix φ (k + 1)).rank) :
    p3ObservableKrylovDepth φ = s := by
  apply p3ObservableKrylovDepth_eq_of_rank_certificate φ s
  · simpa only [p3MatrixUnitKrylovMatrix_rank_eq] using hstop
  · intro k hk
    simpa only [p3MatrixUnitKrylovMatrix_rank_eq] using hearlier k hk

end MatrixUnits

end P3
