import P3.MatrixUnits

/-!
# Canonical diagonal seeds in the finite P3 observable Krylov matrix

Both axes of the Krylov matrix now have physical vertex indices:
  row (x,y) : matrix unit E_xy
  column (j,a) : the j-th orbit iterate of diagonal seed E_aa.

The range of the resulting column map is exactly the original
P3 closure. Its rank, plateau, and minimal depth therefore agree
with the existing formalized P3 invariants.

The results are finite-dimensional and algebraic. A verified
executable exact-rank algorithm is a separate subsequent task.
-/

noncomputable section

namespace P3

section CanonicalDiagonalSeeds

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- The basis of diagonal P3 observables transported from the
canonical coordinate basis of functions V → ℂ. -/
def p3CanonicalDiagonalBasis :
    Module.Basis V ℂ (diagonalSubmodule (V := V)) :=
  (Pi.basisFun ℂ V).map
    ((vertexEquiv (V := V)).symm.trans
      (diagonalEmbeddingEquiv (V := V)))

/-- Canonical diagonal basis vector is the actual matrix unit E_aa. -/
theorem p3CanonicalDiagonalBasis_apply (a : V) :
    (p3CanonicalDiagonalBasis (V := V) a).1 =
      Matrix.single a a (1 : ℂ) := by
  change diagonalEmbedding (V := V)
    ((vertexEquiv (V := V)).symm ((Pi.basisFun ℂ V) a)) =
      Matrix.single a a (1 : ℂ)
  rw [diagonalEmbedding_apply]
  simp [vertexEquiv, Pi.basisFun_apply, Matrix.diagonal_single]

/-- The actual orbit vector at finite depth j from diagonal seed E_aa. -/
def p3CanonicalKrylovColumn (φ : Dynamics V) (k : ℕ)
    (ja : Fin (k + 1) × V) : A V :=
  (φ ^ ja.1.val) ((p3CanonicalDiagonalBasis (V := V) ja.2).1)

/-- The column vector is precisely φ^j(E_aa). -/
theorem p3CanonicalKrylovColumn_eq_iterate_matrix_unit
    (φ : Dynamics V) (k : ℕ) (ja : Fin (k + 1) × V) :
    p3CanonicalKrylovColumn φ k ja =
      (φ ^ ja.1.val) (Matrix.single ja.2 ja.2 (1 : ℂ)) := by
  simp [p3CanonicalKrylovColumn, p3CanonicalDiagonalBasis_apply]

/-- Free finite coefficient vectors generate the canonical orbit columns. -/
def p3CanonicalKrylovColumnMap (φ : Dynamics V) (k : ℕ) :
    ((Fin (k + 1) × V) →₀ ℂ) →ₗ[ℂ] A V :=
  Finsupp.linearCombination ℂ (p3CanonicalKrylovColumn φ k)

/-- The canonical columns span exactly the *original* P3 closure M_k. -/
theorem p3CanonicalKrylovColumnMap_range_eq_closure
    (φ : Dynamics V) (k : ℕ) :
    LinearMap.range (p3CanonicalKrylovColumnMap φ k) = closure φ k := by
  rw [p3CanonicalKrylovColumnMap, Finsupp.range_linearCombination]
  apply le_antisymm
  · apply Submodule.span_le.mpr
    rintro z ⟨⟨i, a⟩, rfl⟩
    apply Submodule.subset_span
    refine ⟨p3CanonicalDiagonalBasis (V := V) a, i.val, ?_, rfl⟩
    exact Nat.le_of_lt_succ i.isLt
  · apply Submodule.span_le.mpr
    rintro z ⟨d, n, hn, rfl⟩
    let T : diagonalSubmodule (V := V) →ₗ[ℂ] A V :=
      (φ ^ n).comp (diagonalSubmodule (V := V)).subtype
    have hmem : d ∈ Submodule.span ℂ
        (Set.range (p3CanonicalDiagonalBasis (V := V))) := by
      rw [(p3CanonicalDiagonalBasis (V := V)).span_eq]
      exact Submodule.mem_top
    have hlinear :
        Submodule.span ℂ (Set.range (p3CanonicalDiagonalBasis (V := V))) ≤
          (Submodule.span ℂ (Set.range (p3CanonicalKrylovColumn φ k))).comap T := by
      apply Submodule.span_le.mpr
      rintro d ⟨a, rfl⟩
      apply Submodule.subset_span
      refine ⟨(⟨n, Nat.lt_succ_of_le hn⟩, a), ?_⟩
      rfl
    exact hlinear hmem

/-- Fully vertex-indexed rectangular Krylov matrix:
   rows (x,y) and columns (j,a). -/
def p3CanonicalKrylovMatrix (φ : Dynamics V) (k : ℕ) :
    Matrix (V × V) (Fin (k + 1) × V) ℂ :=
  (LinearMap.toMatrix Finsupp.basisSingleOne
    (p3MatrixUnitBasis (V := V))) (p3CanonicalKrylovColumnMap φ k)

/-- Entry formula with no abstract basis remaining:
     K_k[(x,y),(j,a)] = [φ^j(E_aa)]_(xy). -/
theorem p3CanonicalKrylovMatrix_entry
    (φ : Dynamics V) (k : ℕ) (x y : V)
    (ja : Fin (k + 1) × V) :
    p3CanonicalKrylovMatrix φ k (x,y) ja =
      ((φ ^ ja.1.val) (Matrix.single ja.2 ja.2 (1 : ℂ))) x y := by
  simp [p3CanonicalKrylovMatrix, LinearMap.toMatrix_apply,
    p3CanonicalKrylovColumnMap,
    Finsupp.coe_basisSingleOne, p3CanonicalKrylovColumn_eq_iterate_matrix_unit,
    p3MatrixUnitBasis_repr_entry]

/-- Rank of the canonical vertex-indexed matrix is the original
observable closure rank. -/
theorem p3CanonicalKrylovMatrix_rank_eq
    (φ : Dynamics V) (k : ℕ) :
    (p3CanonicalKrylovMatrix φ k).rank = p3KrylovRank φ k := by
  rw [Matrix.rank_eq_finrank_range_toLin
    (p3CanonicalKrylovMatrix φ k)
    (p3MatrixUnitBasis (V := V))
    (Finsupp.basisSingleOne)]
  rw [p3CanonicalKrylovMatrix, Matrix.toLin_toMatrix]
  change Module.finrank ℂ (LinearMap.range
    (p3CanonicalKrylovColumnMap φ k)) = p3KrylovRank φ k
  unfold p3KrylovRank
  rw [p3CanonicalKrylovColumnMap_range_eq_closure]

/-- Rank matches the abstract-basis finite-column certificate. -/
theorem p3CanonicalKrylovMatrix_rank_eq_previous
    (φ : Dynamics V) (k : ℕ) :
    (p3CanonicalKrylovMatrix φ k).rank =
      (p3MatrixUnitKrylovMatrix φ k).rank := by
  rw [p3CanonicalKrylovMatrix_rank_eq, p3MatrixUnitKrylovMatrix_rank_eq]

/-- Adjacent ranks of canonical orbit matrices stop iff M_k stabilizes. -/
theorem p3CanonicalKrylovMatrix_rank_stop_iff
    (φ : Dynamics V) (k : ℕ) :
    (p3CanonicalKrylovMatrix φ (k + 1)).rank =
        (p3CanonicalKrylovMatrix φ k).rank ↔
      closure φ (k + 1) = closure φ k := by
  rw [p3CanonicalKrylovMatrix_rank_eq, p3CanonicalKrylovMatrix_rank_eq]
  exact p3KrylovRank_eq_succ_iff_closure_plateau φ k

/-- A fully vertex-indexed, exact finite-rank certificate identifies
the first observable closure stopping depth. -/
theorem p3ObservableKrylovDepth_eq_of_canonical_matrix_certificate
    (φ : Dynamics V) (s : ℕ)
    (hstop : (p3CanonicalKrylovMatrix φ (s + 1)).rank =
      (p3CanonicalKrylovMatrix φ s).rank)
    (hearlier : ∀ k < s,
      (p3CanonicalKrylovMatrix φ k).rank <
        (p3CanonicalKrylovMatrix φ (k + 1)).rank) :
    p3ObservableKrylovDepth φ = s := by
  apply p3ObservableKrylovDepth_eq_of_rank_certificate φ s
  · simpa only [p3CanonicalKrylovMatrix_rank_eq] using hstop
  · intro k hk
    simpa only [p3CanonicalKrylovMatrix_rank_eq] using hearlier k hk

end CanonicalDiagonalSeeds
end P3
