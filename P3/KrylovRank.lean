import P3.ObservableKrylov

/-!
# Finite Krylov column rank certificates for P3

For a finite vertex set V, choose a basis of the original diagonal
observables. At depth k, form finitely many Krylov columns
  φ^n(b_j),  0 ≤ n ≤ k.
Their linear-combination map has range exactly the *original* P3
closure M_k. Therefore its finite-dimensional column rank equals
finrank_C M_k. Equality of ranks at adjacent depths is an exact
certificate for stabilization, and strict rank growth before the
first plateau identifies the optimal observable depth.

Choosing a basis is noncomputable in Lean; the rank certificate is
a finite algebraic test, not yet a certified numerical matrix
row-reduction implementation.
-/

noncomputable section

namespace P3

section KrylovRank

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Rank of the original P3 observable finite-depth Krylov span. -/
def p3KrylovRank (φ : Dynamics V) (k : ℕ) : ℕ :=
  Module.finrank ℂ (closure φ k)

/-- Adjacent equal Krylov ranks are equivalent to actual stabilization
of the original P3 closure submodule. -/
theorem p3KrylovRank_eq_succ_iff_closure_plateau
    (φ : Dynamics V) (k : ℕ) :
    p3KrylovRank φ (k + 1) = p3KrylovRank φ k ↔
      closure φ (k + 1) = closure φ k := by
  constructor
  · intro h
    exact Submodule.eq_of_le_of_finrank_eq
      (closure_mono φ (Nat.le_succ k)) h.symm |>.symm
  · intro h
    change Module.finrank ℂ (closure φ (k + 1)) =
      Module.finrank ℂ (closure φ k)
    rw [h]

/-- Before the first P3 Krylov plateau, every new depth raises rank. -/
theorem p3KrylovRank_strict_before
    (φ : Dynamics V) (k : ℕ)
    (hk : k < p3ObservableKrylovDepth φ) :
    p3KrylovRank φ k < p3KrylovRank φ (k + 1) := by
  exact Submodule.finrank_lt_finrank_of_lt
    (lt_of_le_of_ne (closure_mono φ (Nat.le_succ k))
      (p3ObservableKrylovDepth_strict_before φ k hk).symm)

/-- Beyond the optimal observable depth, the Krylov rank stays fixed. -/
theorem p3KrylovRank_constant_after
    (φ : Dynamics V) (k : ℕ)
    (hk : p3ObservableKrylovDepth φ ≤ k) :
    p3KrylovRank φ k =
      p3KrylovRank φ (p3ObservableKrylovDepth φ) := by
  change Module.finrank ℂ (closure φ k) =
    Module.finrank ℂ (closure φ (p3ObservableKrylovDepth φ))
  rw [p3Closure_stabilizes_at_observableKrylovDepth φ k hk]

/-- A finite rank certificate pinpoints the *exact* first stationary
depth: no earlier adjacent ranks can be equal. -/
theorem p3ObservableKrylovDepth_eq_of_rank_certificate
    (φ : Dynamics V) (s : ℕ)
    (hstop : p3KrylovRank φ (s + 1) = p3KrylovRank φ s)
    (hearlier : ∀ k < s,
      p3KrylovRank φ k < p3KrylovRank φ (k + 1)) :
    p3ObservableKrylovDepth φ = s := by
  have hle : p3ObservableKrylovDepth φ ≤ s := by
    by_contra hnot
    have hlt : s < p3ObservableKrylovDepth φ := Nat.lt_of_not_ge hnot
    exact (ne_of_lt (p3KrylovRank_strict_before φ s hlt)) hstop
  have hnot : ¬ p3ObservableKrylovDepth φ < s := by
    intro hlt
    have hstrict := hearlier _ hlt
    have heq : p3KrylovRank φ
        (p3ObservableKrylovDepth φ + 1) =
          p3KrylovRank φ (p3ObservableKrylovDepth φ) :=
      (p3KrylovRank_eq_succ_iff_closure_plateau φ _).mpr
        (p3ObservableKrylovDepth_spec φ)
    exact (ne_of_lt hstrict) heq.symm
  exact Nat.le_antisymm hle (Nat.le_of_not_gt hnot)

/-- The chosen standard finite basis of the P3 diagonal seed space. -/
def p3FiniteDiagonalBasis :
    Module.Basis (Fin (Module.finrank ℂ (diagonalSubmodule (V := V))))
      ℂ (diagonalSubmodule (V := V)) :=
  Module.finBasis ℂ (diagonalSubmodule (V := V))

/-- Finite Krylov columns: iterates of the diagonal seed basis through k. -/
def p3FiniteKrylovColumn (φ : Dynamics V) (k : ℕ)
    (ij : Fin (k + 1) × Fin (Module.finrank ℂ
      (diagonalSubmodule (V := V)))) : A V :=
  (φ ^ ij.1.val) ((p3FiniteDiagonalBasis (V := V) ij.2).1)

/-- Explicit finite-column linear combination operator. Its domain is
a finite free ℂ-module of coefficient vectors. -/
def p3FiniteKrylovColumnMap (φ : Dynamics V) (k : ℕ) :
    ((Fin (k + 1) × Fin (Module.finrank ℂ
      (diagonalSubmodule (V := V)))) →₀ ℂ) →ₗ[ℂ] A V :=
  Finsupp.linearCombination ℂ (p3FiniteKrylovColumn φ k)

/-- The finite column map's image is exactly the existing P3 closure,
so its rank is the rank of the original diagonal-seed Krylov span. -/
theorem p3FiniteKrylovColumnMap_range_eq_closure
    (φ : Dynamics V) (k : ℕ) :
    LinearMap.range (p3FiniteKrylovColumnMap φ k) = closure φ k := by
  rw [p3FiniteKrylovColumnMap, Finsupp.range_linearCombination]
  apply le_antisymm
  · apply Submodule.span_le.mpr
    rintro z ⟨⟨i, j⟩, rfl⟩
    apply Submodule.subset_span
    refine ⟨p3FiniteDiagonalBasis (V := V) j, i.val, ?_, rfl⟩
    exact Nat.le_of_lt_succ i.isLt
  · apply Submodule.span_le.mpr
    rintro z ⟨d, n, hn, rfl⟩
    let T : diagonalSubmodule (V := V) →ₗ[ℂ] A V :=
      (φ ^ n).comp (diagonalSubmodule (V := V)).subtype
    have hmem : d ∈ Submodule.span ℂ
        (Set.range (p3FiniteDiagonalBasis (V := V))) := by
      rw [(p3FiniteDiagonalBasis (V := V)).span_eq]
      exact Submodule.mem_top
    have hlinear :
        Submodule.span ℂ (Set.range (p3FiniteDiagonalBasis (V := V))) ≤
        (Submodule.span ℂ (Set.range (p3FiniteKrylovColumn φ k))).comap T := by
      apply Submodule.span_le.mpr
      rintro d ⟨j, rfl⟩
      apply Submodule.subset_span
      refine ⟨(⟨n, Nat.lt_succ_of_le hn⟩, j), ?_⟩
      rfl
    exact hlinear hmem

/-- The rank of an explicitly finite-column operator exactly computes
the P3 Krylov rank. -/
theorem p3FiniteKrylovColumnMap_rank_eq
    (φ : Dynamics V) (k : ℕ) :
    Module.finrank ℂ (LinearMap.range
      (p3FiniteKrylovColumnMap φ k)) = p3KrylovRank φ k := by
  change Module.finrank ℂ (LinearMap.range
    (p3FiniteKrylovColumnMap φ k)) =
      Module.finrank ℂ (closure φ k)
  rw [p3FiniteKrylovColumnMap_range_eq_closure]

/-- An exact rank certificate using the explicitly finite-dimensional
column operators, not abstract equality of submodules. -/
theorem p3FiniteColumnRank_stop_iff
    (φ : Dynamics V) (k : ℕ) :
    Module.finrank ℂ (LinearMap.range
      (p3FiniteKrylovColumnMap φ (k + 1))) =
    Module.finrank ℂ (LinearMap.range
      (p3FiniteKrylovColumnMap φ k)) ↔
      closure φ (k + 1) = closure φ k := by
  rw [p3FiniteKrylovColumnMap_rank_eq,
      p3FiniteKrylovColumnMap_rank_eq]
  exact p3KrylovRank_eq_succ_iff_closure_plateau φ k

end KrylovRank
end P3
