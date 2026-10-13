import P3.ExplicitStabilization
import Mathlib.FieldTheory.Minpoly.Field

/-!
# Minimal-polynomial bound for P3 finite closure and formal hidden jets

This module sharpens the characteristic-polynomial bound `D-1`
proved in P3.ExplicitStabilization to `r-1`, where
`r = natDegree (minpoly ℂ φ)`.

The bound is intrinsic to the fixed full linear map φ and may still be
nonoptimal for the diagonal-seed reachable subspace. Nothing here
establishes a uniform bound across increasing matrix dimensions.
-/

noncomputable section
open scoped BigOperators

namespace P3

section MinimalPolynomialStabilization

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Degree of the full dynamics' minimal polynomial. -/
def p3MinimalDegree (φ : Dynamics V) : ℕ :=
  (minpoly ℂ φ).natDegree

/-- The minimal polynomial is monic because every finite-dimensional
endomorphism is integral, by Cayley–Hamilton. -/
theorem p3Dynamics_minpoly_monic (φ : Dynamics V) :
    (minpoly ℂ φ).Monic := by
  exact minpoly.monic (LinearMap.isIntegral φ)

/-- The dynamics is annihilated by its minimal polynomial. -/
theorem p3Dynamics_minpoly_annihilates (φ : Dynamics V) :
    Polynomial.aeval φ (minpoly ℂ φ) = 0 := by
  exact minpoly.aeval ℂ φ

/-- All powers are determined by polynomial remainders modulo minpoly. -/
theorem p3Dynamics_pow_eq_aeval_minpoly_remainder
    (φ : Dynamics V) (n : ℕ) :
    φ ^ n =
      Polynomial.aeval φ ((Polynomial.X ^ n) %ₘ (minpoly ℂ φ)) := by
  calc
    φ ^ n = Polynomial.aeval φ (Polynomial.X ^ n) := by simp
    _ = Polynomial.aeval φ ((Polynomial.X ^ n) %ₘ (minpoly ℂ φ)) :=
      (Polynomial.aeval_modByMonic_eq_self_of_root
        (p3Dynamics_minpoly_annihilates φ)).symm

/-- The minimal-polynomial degree cannot exceed the matrix-algebra
dimension used in the earlier Cayley–Hamilton bound. -/
theorem p3MinimalDegree_le_dimension (φ : Dynamics V) :
    p3MinimalDegree φ ≤ p3AlgebraDimension (V := V) := by
  change (minpoly ℂ φ).natDegree ≤ p3AlgebraDimension (V := V)
  calc
    (minpoly ℂ φ).natDegree ≤ φ.charpoly.natDegree :=
      Polynomial.natDegree_le_of_dvd
        (LinearMap.minpoly_dvd_charpoly φ)
        (LinearMap.charpoly_monic φ).ne_zero
    _ = p3AlgebraDimension (V := V) :=
      p3Dynamics_charpoly_degree φ

/-- Exact reconstruction of all orbit vectors from the first r
iterates, with coefficients defined by polynomial division. -/
theorem p3Dynamics_iterate_minpoly_reconstruction
    (φ : Dynamics V) (d : diagonalSubmodule (V := V))
    (n : ℕ) (hpoly : minpoly ℂ φ ≠ 1) :
    (φ ^ n) d.1 =
      ∑ i ∈ Finset.range (p3MinimalDegree φ),
        (((Polynomial.X ^ n) %ₘ (minpoly ℂ φ)).coeff i) •
          ((φ ^ i) d.1) := by
  have hlt :
      ((Polynomial.X ^ n) %ₘ (minpoly ℂ φ)).natDegree <
        p3MinimalDegree φ := by
    exact Polynomial.natDegree_modByMonic_lt _
      (p3Dynamics_minpoly_monic φ) hpoly
  calc
    (φ ^ n) d.1 =
        (Polynomial.aeval φ ((Polynomial.X ^ n) %ₘ minpoly ℂ φ)) d.1 := by
          rw [p3Dynamics_pow_eq_aeval_minpoly_remainder]
    _ = (∑ i ∈ Finset.range (p3MinimalDegree φ),
          (((Polynomial.X ^ n) %ₘ minpoly ℂ φ).coeff i) •
            (φ ^ i)) d.1 := by
          rw [Polynomial.aeval_eq_sum_range' hlt]
    _ = ∑ i ∈ Finset.range (p3MinimalDegree φ),
          (((Polynomial.X ^ n) %ₘ minpoly ℂ φ).coeff i) •
            ((φ ^ i) d.1) := by
          simp only [LinearMap.sum_apply, LinearMap.smul_apply]

/-- The finite reconstruction descends to original P3 primitive defects. -/
theorem p3PrimitiveDefect_minpoly_reconstruction
    (φ : Dynamics V) (d : diagonalSubmodule (V := V))
    (n : ℕ) (hpoly : minpoly ℂ φ ≠ 1) :
    (primitiveDefect φ n d).1 =
      ∑ i ∈ Finset.range (p3MinimalDegree φ),
        (((Polynomial.X ^ n) %ₘ minpoly ℂ φ).coeff i) •
          (primitiveDefect φ i d).1 := by
  simp only [primitiveDefect_val]
  rw [p3Dynamics_iterate_minpoly_reconstruction φ d n hpoly]
  simp only [map_sum, map_smul]

/-- Every generated orbit already lies in the minpoly-depth closure. -/
theorem p3Iterate_mem_closure_at_minpoly
    (φ : Dynamics V) (d : diagonalSubmodule (V := V))
    (n : ℕ) (hpoly : minpoly ℂ φ ≠ 1) :
    (φ ^ n) d.1 ∈ closure φ (p3MinimalDegree φ - 1) := by
  rw [p3Dynamics_iterate_minpoly_reconstruction φ d n hpoly]
  apply Submodule.sum_mem
  intro i hi
  apply Submodule.smul_mem
  apply Submodule.subset_span
  refine ⟨d, i, ?_, rfl⟩
  have hlt : i < p3MinimalDegree φ := Finset.mem_range.mp hi
  omega

/-- The full finite-depth closure lies below the minpoly bound. -/
theorem p3Closure_le_minpoly_bound
    (φ : Dynamics V) (k : ℕ) (hpoly : minpoly ℂ φ ≠ 1) :
    closure φ k ≤ closure φ (p3MinimalDegree φ - 1) := by
  apply Submodule.span_le.mpr
  rintro z ⟨d, n, _hn, rfl⟩
  exact p3Iterate_mem_closure_at_minpoly φ d n hpoly

/-- P3 closure stabilizes no later than minimal-polynomial degree minus 1. -/
theorem p3Closure_stabilizes_at_minpoly
    (φ : Dynamics V) (k : ℕ) (hpoly : minpoly ℂ φ ≠ 1)
    (hbound : p3MinimalDegree φ - 1 ≤ k) :
    closure φ k = closure φ (p3MinimalDegree φ - 1) := by
  apply le_antisymm
  · exact p3Closure_le_minpoly_bound φ k hpoly
  · exact closure_mono φ hbound

/-- So does P3's original hidden defect filtration. -/
theorem p3Hidden_stabilizes_at_minpoly
    (φ : Dynamics V) (k : ℕ) (hpoly : minpoly ℂ φ ≠ 1)
    (hbound : p3MinimalDegree φ - 1 ≤ k) :
    hidden φ k = hidden φ (p3MinimalDegree φ - 1) := by
  unfold hidden
  rw [p3Closure_stabilizes_at_minpoly φ k hpoly hbound]

/-- And the original primitive hidden-generator span. -/
theorem p3PrimitiveHiddenSpan_stabilizes_at_minpoly
    (φ : Dynamics V) (k : ℕ) (hpoly : minpoly ℂ φ ≠ 1)
    (hbound : p3MinimalDegree φ - 1 ≤ k) :
    primitiveHiddenSpan φ k =
      primitiveHiddenSpan φ (p3MinimalDegree φ - 1) := by
  calc
    primitiveHiddenSpan φ k = hidden φ k :=
      (hidden_eq_span_primitive φ k).symm
    _ = hidden φ (p3MinimalDegree φ - 1) :=
      p3Hidden_stabilizes_at_minpoly φ k hpoly hbound
    _ = primitiveHiddenSpan φ (p3MinimalDegree φ - 1) :=
      hidden_eq_span_primitive φ _

/-- If all first r primitive defects vanish at a coordinate, every
higher-order formal Taylor coefficient vanishes too. -/
theorem p3HiddenJet_zero_first_minpoly_implies_zero
    (φ : Dynamics V) (d : diagonalSubmodule (V := V))
    (x y : V) (hpoly : minpoly ℂ φ ≠ 1)
    (hzero : ∀ i, i < p3MinimalDegree φ →
      (PowerSeries.coeff i) (p3HiddenCoordinateJet φ d x y) = 0) :
    p3HiddenCoordinateJet φ d x y = 0 := by
  have hprim : ∀ i, i < p3MinimalDegree φ →
      (primitiveDefect φ i d).1 x y = 0 := by
    intro i hi
    by_contra hn
    exact ((p3HiddenCoordinateJet_coeff_ne_zero_iff φ d x y i).mpr hn)
      (hzero i hi)
  have hall : ∀ n : ℕ, (primitiveDefect φ n d).1 x y = 0 := by
    intro n
    rw [p3PrimitiveDefect_minpoly_reconstruction φ d n hpoly]
    simp only [Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul]
    apply Finset.sum_eq_zero
    intro i hi
    simp [hprim i (Finset.mem_range.mp hi)]
  apply PowerSeries.ext
  intro n
  simp [p3HiddenCoordinateJet_coeff, hall n]

end MinimalPolynomialStabilization
end P3
