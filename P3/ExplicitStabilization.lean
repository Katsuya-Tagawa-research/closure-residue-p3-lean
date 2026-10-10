import P3.CayleyHamiltonJets

/-!
# Explicit stabilization of the finite P3 closure and hidden filtration

The Cayley–Hamilton finite reconstruction from P3.CayleyHamiltonJets gives
an effective uniform bound for *each fixed finite matrix algebra*:
if the characteristic polynomial of φ is nonconstant, then
  closure φ k = closure φ (D-1)
  hidden φ k = hidden φ (D-1)
for k ≥ D-1, where D = finrank ℂ (A V).

The edgewise formal Taylor jets are identically zero precisely when their
first D normalized coefficients vanish, equivalently to the absence of
a hidden coordinate at depth D-1.

This is not a dimension-uniform or infinite-volume closure theorem.
-/

noncomputable section

open scoped BigOperators

namespace P3

section ExplicitStabilization

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Every orbit vector belongs to the explicitly bounded P3 closure. -/
theorem p3Iterate_mem_closure_at_dimension
    (φ : Dynamics V) (d : diagonalSubmodule (V := V))
    (n : ℕ) (hpoly : φ.charpoly ≠ 1) :
    (φ ^ n) d.1 ∈ closure φ (p3AlgebraDimension (V := V) - 1) := by
  rw [p3Dynamics_iterate_finite_reconstruction φ d n hpoly]
  apply Submodule.sum_mem
  intro i hi
  apply Submodule.smul_mem
  apply Submodule.subset_span
  refine ⟨d, i, ?_, rfl⟩
  have hlt : i < p3AlgebraDimension (V := V) :=
    Finset.mem_range.mp hi
  omega

/-- Every finite closure M_k is contained in M_(D-1). -/
theorem p3Closure_le_dimension_bound
    (φ : Dynamics V) (k : ℕ) (hpoly : φ.charpoly ≠ 1) :
    closure φ k ≤ closure φ (p3AlgebraDimension (V := V) - 1) := by
  apply Submodule.span_le.mpr
  rintro z ⟨d, n, _hn, rfl⟩
  exact p3Iterate_mem_closure_at_dimension φ d n hpoly

/-- Explicit Cayley–Hamilton stabilization of P3's original M_k. -/
theorem p3Closure_stabilizes_at_dimension
    (φ : Dynamics V) (k : ℕ) (hpoly : φ.charpoly ≠ 1)
    (hbound : p3AlgebraDimension (V := V) - 1 ≤ k) :
    closure φ k = closure φ (p3AlgebraDimension (V := V) - 1) := by
  apply le_antisymm
  · exact p3Closure_le_dimension_bound φ k hpoly
  · exact closure_mono φ hbound

/-- Explicit stabilization of P3's original hidden filtration H_k. -/
theorem p3Hidden_stabilizes_at_dimension
    (φ : Dynamics V) (k : ℕ) (hpoly : φ.charpoly ≠ 1)
    (hbound : p3AlgebraDimension (V := V) - 1 ≤ k) :
    hidden φ k = hidden φ (p3AlgebraDimension (V := V) - 1) := by
  unfold hidden
  rw [p3Closure_stabilizes_at_dimension φ k hpoly hbound]

/-- The original primitive-generator presentation also stabilizes. -/
theorem p3PrimitiveHiddenSpan_stabilizes_at_dimension
    (φ : Dynamics V) (k : ℕ) (hpoly : φ.charpoly ≠ 1)
    (hbound : p3AlgebraDimension (V := V) - 1 ≤ k) :
    primitiveHiddenSpan φ k =
      primitiveHiddenSpan φ (p3AlgebraDimension (V := V) - 1) := by
  calc
    primitiveHiddenSpan φ k = hidden φ k :=
      (hidden_eq_span_primitive φ k).symm
    _ = hidden φ (p3AlgebraDimension (V := V) - 1) :=
      p3Hidden_stabilizes_at_dimension φ k hpoly hbound
    _ = primitiveHiddenSpan φ (p3AlgebraDimension (V := V) - 1) :=
      hidden_eq_span_primitive φ _

/-- If the coordinate is absent at the dimension-bound depth,
every seed's infinite formal Taylor jet vanishes identically there. -/
theorem p3AllHiddenJets_zero_of_no_defect_at_dimension
    (φ : Dynamics V) (x y : V) (hpoly : φ.charpoly ≠ 1)
    (hxy : x ≠ y)
    (hsilent : ¬ defectActive φ (p3AlgebraDimension (V := V) - 1) x y) :
    ∀ d : diagonalSubmodule (V := V),
      p3HiddenCoordinateJet φ d x y = 0 := by
  intro d
  apply p3HiddenJet_zero_first_implies_zero φ d x y hpoly
  intro i hi
  by_contra hnonzero
  apply hsilent
  apply (defectActive_iff_exists_p3HiddenJet φ
    (p3AlgebraDimension (V := V) - 1) x y).mpr
  refine ⟨hxy, d, i, ?_, hnonzero⟩
  omega

/-- An exact finite test for complete formal-jet silence in a fixed
off-diagonal coordinate. -/
theorem p3AllHiddenJets_zero_iff_no_defect_at_dimension
    (φ : Dynamics V) (x y : V) (hpoly : φ.charpoly ≠ 1)
    (hxy : x ≠ y) :
    (∀ d : diagonalSubmodule (V := V),
      p3HiddenCoordinateJet φ d x y = 0) ↔
    ¬ defectActive φ (p3AlgebraDimension (V := V) - 1) x y := by
  constructor
  · intro hzero hactive
    obtain ⟨_, d, i, _hi, hnonzero⟩ :=
      (defectActive_iff_exists_p3HiddenJet φ
        (p3AlgebraDimension (V := V) - 1) x y).mp hactive
    have hz : (PowerSeries.coeff i) (p3HiddenCoordinateJet φ d x y) = 0 := by
      rw [hzero d]
      simp
    exact hnonzero hz
  · exact p3AllHiddenJets_zero_of_no_defect_at_dimension φ x y hpoly hxy

end ExplicitStabilization

end P3
