import P3.MinpolyStabilization

/-!
# The exact observable Krylov closure depth of finite P3 dynamics

Unlike the degree of the minimal polynomial of φ on the full matrix
algebra, the first depth at which the P3 diagonal-seed closure ceases
to increase is specific to the observable reachable subspace.

We define the *least* plateau depth from the original P3 filtration,
prove that its closure is the minimal φ-invariant submodule containing
the diagonal seeds, and prove that both the closure and hidden
filtrations increase strictly before this depth and stabilize forever
after it. The degree r of the full minimal polynomial supplies only
an upper bound s ≤ r-1.

The exact plateau is existence-defined with Nat.find (noncomputable);
a constructive algorithm/certified rank computation is future work.
This is for finite matrix algebras only.
-/

noncomputable section

namespace P3

section ObservableKrylov

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Finite dimensionality ensures at least one stationary depth. -/
private theorem p3ExistsStationary (φ : Dynamics V) :
    ∃ s : ℕ, closure φ (s + 1) = closure φ s := by
  obtain ⟨s, hs⟩ := closure_eventually_constant φ
  exact ⟨s, hs (s + 1) (Nat.le_succ s)⟩

/-- The *first* depth at which the observable Krylov closure stabilizes.
It is a property of the original diagonal-seed orbit, not of the full
matrix algebra's minimal polynomial. -/
def p3ObservableKrylovDepth (φ : Dynamics V) : ℕ :=
  Nat.find (p3ExistsStationary φ)

/-- The first observable Krylov plateau genuinely is stationary. -/
theorem p3ObservableKrylovDepth_spec (φ : Dynamics V) :
    closure φ (p3ObservableKrylovDepth φ + 1) =
      closure φ (p3ObservableKrylovDepth φ) := by
  exact Nat.find_spec (p3ExistsStationary φ)

/-- Every earlier depth is strictly nonstationary. -/
theorem p3ObservableKrylovDepth_strict_before
    (φ : Dynamics V) (k : ℕ)
    (hk : k < p3ObservableKrylovDepth φ) :
    closure φ (k + 1) ≠ closure φ k := by
  exact Nat.find_min (p3ExistsStationary φ) hk

/-- The first stationary closure is an invariant subspace and hence
all later finite closures are identical to it. -/
theorem p3Closure_stabilizes_from_succ
    (φ : Dynamics V) (s k : ℕ)
    (hstable : closure φ (s + 1) = closure φ s)
    (hsk : s ≤ k) :
    closure φ k = closure φ s := by
  apply le_antisymm
  · exact closure_le_of_diagonal_le_of_invariant φ
      (closure φ s)
      (diagonalSubmodule_le_closure φ s)
      (closure_invariant_of_succ_eq φ hstable) k
  · exact closure_mono φ hsk

/-- The actual reachable observable Krylov space. -/
def p3ObservableKrylovSpace (φ : Dynamics V) :
    Submodule ℂ (A V) :=
  closure φ (p3ObservableKrylovDepth φ)

/-- This reachable space contains the diagonal seed subspace. -/
theorem p3ObservableKrylovSpace_contains_diagonal
    (φ : Dynamics V) :
    diagonalSubmodule (V := V) ≤ p3ObservableKrylovSpace φ :=
  diagonalSubmodule_le_closure φ _

/-- The reachable observable Krylov space is φ-invariant. -/
theorem p3ObservableKrylovSpace_invariant
    (φ : Dynamics V) :
    ∀ z ∈ p3ObservableKrylovSpace φ,
      φ z ∈ p3ObservableKrylovSpace φ :=
  closure_invariant_of_succ_eq φ
    (p3ObservableKrylovDepth_spec φ)

/-- Universal property: the reachable Krylov space is the smallest
φ-invariant complex submodule containing all diagonal seeds. -/
theorem p3ObservableKrylovSpace_le_of_invariant
    (φ : Dynamics V) (S : Submodule ℂ (A V))
    (hD : diagonalSubmodule (V := V) ≤ S)
    (hInv : ∀ z ∈ S, φ z ∈ S) :
    p3ObservableKrylovSpace φ ≤ S :=
  closure_le_of_diagonal_le_of_invariant φ S hD hInv _

/-- All finite-depth closures lie inside the reachable Krylov space. -/
theorem p3Closure_le_observableKrylovSpace
    (φ : Dynamics V) (k : ℕ) :
    closure φ k ≤ p3ObservableKrylovSpace φ := by
  exact closure_le_of_diagonal_le_of_invariant φ
    (p3ObservableKrylovSpace φ)
    (p3ObservableKrylovSpace_contains_diagonal φ)
    (p3ObservableKrylovSpace_invariant φ) k

/-- Every orbit of a diagonal seed is already contained in the
observable reachable subspace. -/
theorem p3ObservableKrylovSpace_mem_iterate
    (φ : Dynamics V) (d : diagonalSubmodule (V := V))
    (n : ℕ) :
    (φ ^ n) d.1 ∈ p3ObservableKrylovSpace φ := by
  apply p3Closure_le_observableKrylovSpace φ n
  apply Submodule.subset_span
  exact ⟨d, n, le_rfl, rfl⟩

/-- Exact infinite-orbit spanning characterization of the Krylov space. -/
theorem p3ObservableKrylovSpace_eq_span_orbits
    (φ : Dynamics V) :
    p3ObservableKrylovSpace φ =
      Submodule.span ℂ
        {z | ∃ d : diagonalSubmodule (V := V),
          ∃ n : ℕ, (φ ^ n) d.1 = z} := by
  apply le_antisymm
  · apply Submodule.span_le.mpr
    rintro z ⟨d, n, _hn, rfl⟩
    apply Submodule.subset_span
    exact ⟨d, n, rfl⟩
  · apply Submodule.span_le.mpr
    rintro z ⟨d, n, rfl⟩
    exact p3ObservableKrylovSpace_mem_iterate φ d n

/-- The first plateau is an exact, non-asymptotic stabilization bound. -/
theorem p3Closure_stabilizes_at_observableKrylovDepth
    (φ : Dynamics V) (k : ℕ)
    (hk : p3ObservableKrylovDepth φ ≤ k) :
    closure φ k = p3ObservableKrylovSpace φ :=
  p3Closure_stabilizes_from_succ φ
    (p3ObservableKrylovDepth φ) k
    (p3ObservableKrylovDepth_spec φ) hk

/-- P3 hidden filtration stabilizes at the same observable depth. -/
theorem p3Hidden_stabilizes_at_observableKrylovDepth
    (φ : Dynamics V) (k : ℕ)
    (hk : p3ObservableKrylovDepth φ ≤ k) :
    hidden φ k = hidden φ (p3ObservableKrylovDepth φ) := by
  unfold hidden
  rw [p3Closure_stabilizes_at_observableKrylovDepth φ k hk]
  rfl

/-- The original hidden filtration strictly increases at every
earlier depth: no silent plateau can be followed by later growth. -/
theorem p3Hidden_strict_before_observableKrylovDepth
    (φ : Dynamics V) (k : ℕ)
    (hk : k < p3ObservableKrylovDepth φ) :
    hidden φ (k + 1) ≠ hidden φ k := by
  intro hEq
  apply p3ObservableKrylovDepth_strict_before φ k hk
  calc
    closure φ (k + 1) =
        diagonalSubmodule (V := V) ⊔ hidden φ (k + 1) :=
      closure_eq_sup_diagonal_hidden φ _
    _ = diagonalSubmodule (V := V) ⊔ hidden φ k := by rw [hEq]
    _ = closure φ k := (closure_eq_sup_diagonal_hidden φ _).symm

/-- The exact observable plateau never exceeds the full minimal
polynomial degree minus one. -/
theorem p3ObservableKrylovDepth_le_minpoly
    (φ : Dynamics V) (hpoly : minpoly ℂ φ ≠ 1) :
    p3ObservableKrylovDepth φ ≤ p3MinimalDegree φ - 1 := by
  unfold p3ObservableKrylovDepth
  apply Nat.find_min' (p3ExistsStationary φ)
  exact p3Closure_stabilizes_at_minpoly φ
    (p3MinimalDegree φ - 1 + 1) hpoly (Nat.le_succ _)

/-- The observable plateau is also bounded by the ambient matrix
algebra dimension, recovering the earlier coarse Cayley–Hamilton bound. -/
theorem p3ObservableKrylovDepth_le_dimension
    (φ : Dynamics V) (hpoly : minpoly ℂ φ ≠ 1) :
    p3ObservableKrylovDepth φ ≤ p3AlgebraDimension (V := V) - 1 := by
  exact (p3ObservableKrylovDepth_le_minpoly φ hpoly).trans
    (Nat.sub_le_sub_right (p3MinimalDegree_le_dimension φ) 1)

/-- The original finite-depth activity of a coordinate is unchanged
after the first observable Krylov plateau. -/
theorem p3DefectActive_stabilizes_at_observableKrylovDepth
    (φ : Dynamics V) (k : ℕ) (x y : V)
    (hk : p3ObservableKrylovDepth φ ≤ k) :
    defectActive φ k x y ↔
      defectActive φ (p3ObservableKrylovDepth φ) x y := by
  unfold defectActive
  rw [p3Hidden_stabilizes_at_observableKrylovDepth φ k hk]

/-- A finite depth test for whether *all* formal diagonal-seed
Taylor jets in an off-diagonal coordinate vanish identically.
No a priori degree upper bound is needed here: the exact observable
Krylov depth supplies the finite cutoff. -/
theorem p3AllHiddenJets_zero_iff_no_defect_at_observableKrylovDepth
    (φ : Dynamics V) (x y : V) (hxy : x ≠ y) :
    (∀ d : diagonalSubmodule (V := V),
      p3HiddenCoordinateJet φ d x y = 0) ↔
      ¬ defectActive φ (p3ObservableKrylovDepth φ) x y := by
  constructor
  · intro hzero hactive
    obtain ⟨_, d, n, _hn, hcoeff⟩ :=
      (defectActive_iff_exists_p3HiddenJet φ
        (p3ObservableKrylovDepth φ) x y).mp hactive
    have hz : (PowerSeries.coeff n)
        (p3HiddenCoordinateJet φ d x y) = 0 := by
      rw [hzero d]
      simp
    exact hcoeff hz
  · intro hsilent d
    apply PowerSeries.ext
    intro n
    have hzero : (PowerSeries.coeff n)
        (p3HiddenCoordinateJet φ d x y) = 0 := by
      by_contra hne
      have hactive : defectActive φ n x y :=
        (defectActive_iff_exists_p3HiddenJet φ n x y).mpr
          ⟨hxy, d, n, le_rfl, hne⟩
      obtain ⟨_, z, hz, hzne⟩ := hactive
      have hmap : hidden φ n ≤
          hidden φ (p3ObservableKrylovDepth φ) := by
        exact Submodule.map_mono
          (p3Closure_le_observableKrylovSpace φ n)
      exact hsilent ⟨hxy, z, hmap hz, hzne⟩
    simpa using hzero

end ObservableKrylov
end P3
