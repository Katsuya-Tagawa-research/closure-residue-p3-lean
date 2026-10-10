import P3.HiddenJetBridge
import Mathlib.LinearAlgebra.Charpoly.Basic
import Mathlib.Algebra.Polynomial.Div

/-!
# P3 / P11 Cayley–Hamilton finite determination of all Taylor jets

The algebra of finite matrices is finite dimensional. For any complex-linear
dynamics φ on it, Cayley–Hamilton supplies a fixed characteristic polynomial.
Every iterate φ^n is represented by a polynomial of degree smaller than the
matrix-algebra dimension, namely the remainder of X^n mod charpoly φ.

These are exact algebraic identities, including for the primitive hidden
defects Q(φ^n d). No convergence, residue noncancellation, or universal
infinite-dimensional closure is asserted.
-/

noncomputable section

open scoped BigOperators

namespace P3

section CayleyHamiltonJets

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Matrix-algebra dimension: for finite V it equals (card V)^2. -/
def p3AlgebraDimension : ℕ := Module.finrank ℂ (A V)

/-- The characteristic polynomial annihilates the P3 dynamics. -/
theorem p3Dynamics_charpoly_annihilates
    (φ : Dynamics V) :
    Polynomial.aeval φ φ.charpoly = 0 := by
  exact LinearMap.aeval_self_charpoly φ

/-- Every iterate is determined by the remainder of X^n
modulo one finite characteristic polynomial. -/
theorem p3Dynamics_pow_eq_aeval_remainder
    (φ : Dynamics V) (n : ℕ) :
    φ ^ n = Polynomial.aeval φ ((Polynomial.X ^ n) %ₘ φ.charpoly) := by
  exact LinearMap.pow_eq_aeval_mod_charpoly φ n

/-- The characteristic polynomial has degree equal to the vector-space
dimension of the finite matrix algebra. -/
theorem p3Dynamics_charpoly_degree
    (φ : Dynamics V) :
    φ.charpoly.natDegree = p3AlgebraDimension (V := V) := by
  exact LinearMap.charpoly_natDegree φ

/-- Each orbit vector is a finite linear combination of the first D
orbit vectors, where D = dim_C A(V). Coefficients are explicit
polynomial-remainder coefficients and may depend on n. -/
theorem p3Dynamics_iterate_finite_reconstruction
    (φ : Dynamics V) (d : diagonalSubmodule (V := V))
    (n : ℕ) (hpoly : φ.charpoly ≠ 1) :
    (φ ^ n) d.1 =
      ∑ i ∈ Finset.range (p3AlgebraDimension (V := V)),
        (((Polynomial.X ^ n) %ₘ φ.charpoly).coeff i) • ((φ ^ i) d.1) := by
  have hlt : (((Polynomial.X ^ n) %ₘ φ.charpoly).natDegree) <
      p3AlgebraDimension (V := V) := by
    rw [← p3Dynamics_charpoly_degree (V := V) φ]
    exact Polynomial.natDegree_modByMonic_lt _
      (LinearMap.charpoly_monic φ) hpoly
  calc
    (φ ^ n) d.1 =
        (Polynomial.aeval φ ((Polynomial.X ^ n) %ₘ φ.charpoly)) d.1 := by
          rw [p3Dynamics_pow_eq_aeval_remainder]
    _ = (∑ i ∈ Finset.range (p3AlgebraDimension (V := V)),
          (((Polynomial.X ^ n) %ₘ φ.charpoly).coeff i) • (φ ^ i)) d.1 := by
          rw [Polynomial.aeval_eq_sum_range' hlt]
    _ = ∑ i ∈ Finset.range (p3AlgebraDimension (V := V)),
          (((Polynomial.X ^ n) %ₘ φ.charpoly).coeff i) • ((φ ^ i) d.1) := by
          simp only [Finset.sum_apply, LinearMap.smul_apply]

/-- The same finite reconstruction holds after P3's original hidden
off-diagonal projection Q. -/
theorem p3PrimitiveDefect_finite_reconstruction
    (φ : Dynamics V) (d : diagonalSubmodule (V := V))
    (n : ℕ) (hpoly : φ.charpoly ≠ 1) :
    (primitiveDefect (V := V) φ n d).1 =
      ∑ i ∈ Finset.range (p3AlgebraDimension (V := V)),
        (((Polynomial.X ^ n) %ₘ φ.charpoly).coeff i) •
          (primitiveDefect (V := V) φ i d).1 := by
  simp only [primitiveDefect_val]
  rw [p3Dynamics_iterate_finite_reconstruction φ d n hpoly]
  simp only [map_sum, map_smul]

/-- If one matrix coordinate is zero in the first D primitive defects
for a diagonal seed, it is zero at every higher iterate. -/
theorem p3PrimitiveDefect_zero_first_implies_all
    (φ : Dynamics V) (d : diagonalSubmodule (V := V))
    (x y : V) (hpoly : φ.charpoly ≠ 1)
    (hzero : ∀ i, i < p3AlgebraDimension (V := V) →
      (primitiveDefect (V := V) φ i d).1 x y = 0) :
    ∀ n : ℕ, (primitiveDefect (V := V) φ n d).1 x y = 0 := by
  intro n
  rw [p3PrimitiveDefect_finite_reconstruction φ d n hpoly]
  simp only [Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul]
  apply Finset.sum_eq_zero
  intro i hi
  simp [hzero i (Finset.mem_range.mp hi)]

/-- Consequently, the entire formal Taylor series in this coordinate
is zero when its first D normalized coefficients vanish. -/
theorem p3HiddenJet_zero_first_implies_zero
    (φ : Dynamics V) (d : diagonalSubmodule (V := V))
    (x y : V) (hpoly : φ.charpoly ≠ 1)
    (hzero : ∀ i, i < p3AlgebraDimension (V := V) →
      (PowerSeries.coeff i) (p3HiddenCoordinateJet φ d x y) = 0) :
    p3HiddenCoordinateJet φ d x y = 0 := by
  apply PowerSeries.ext
  intro n
  have hprim : ∀ i, i < p3AlgebraDimension (V := V) →
      (primitiveDefect (V := V) φ i d).1 x y = 0 := by
    intro i hi
    by_contra hn
    exact ((p3HiddenCoordinateJet_coeff_ne_zero_iff φ d x y i).mpr hn)
      (hzero i hi)
  have hn := p3PrimitiveDefect_zero_first_implies_all φ d x y hpoly hprim n
  simp [p3HiddenCoordinateJet_coeff, hn]

end CayleyHamiltonJets

end P3
