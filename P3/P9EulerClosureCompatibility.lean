import P3.P9TTFiniteSymbol

/-!
# Finite first-order Euler shift: saturated observable closure compatibility

For any finite complex-linear P3 Dynamics L and nonzero complex Δ, let
Phi_Δ = id + Δ L. The original P3 diagonal-seed observable Krylov
submodule of Phi_Δ is exactly the Krylov submodule of L.

The proof uses the universal minimal invariant submodule property:
a submodule is L-invariant if and only if it is (id+ΔL)-invariant
when Δ!=0.

Caution: an arbitrary explicit Euler shift of a GKSL generator need
NOT be CPTP. This is an algebraic compatibility benchmark; it does
not assert that every physical P1 near-identity CPTP family has the
same observable Krylov space. The o(Δ) perturbation and exact
semigroup cases require their own hypotheses and proofs.
-/

noncomputable section

namespace P3

/-- Exact linear Euler shift of finite observable dynamics. -/
def p9EulerShift {V : Type*} [Fintype V] [DecidableEq V]
    (L : Dynamics V) (Δ : ℂ) : Dynamics V :=
  LinearMap.id + Δ • L

/-- The Euler-shifted map acts as z + Δ L(z). -/
theorem p9EulerShift_apply
    {V : Type*} [Fintype V] [DecidableEq V]
    (L : Dynamics V) (Δ : ℂ) (z : A V) :
    p9EulerShift L Δ z = z + Δ • L z := by
  simp [p9EulerShift]

/-- The saturated diagonal-seed observable closure of an exact
Euler shift is independent of nonzero step size. -/
theorem p9EulerShift_observableSpace_eq
    {V : Type*} [Fintype V] [DecidableEq V]
    (L : Dynamics V) (Δ : ℂ) (hΔ : Δ ≠ 0) :
    p3ObservableKrylovSpace (p9EulerShift L Δ) =
      p3ObservableKrylovSpace L := by
  apply le_antisymm
  · apply p3ObservableKrylovSpace_le_of_invariant
      (p9EulerShift L Δ) (p3ObservableKrylovSpace L)
      (p3ObservableKrylovSpace_contains_diagonal L)
    intro z hz
    rw [p9EulerShift_apply]
    exact (p3ObservableKrylovSpace L).add_mem hz
      ((p3ObservableKrylovSpace L).smul_mem Δ
        (p3ObservableKrylovSpace_invariant L z hz))
  · apply p3ObservableKrylovSpace_le_of_invariant
      L (p3ObservableKrylovSpace (p9EulerShift L Δ))
      (p3ObservableKrylovSpace_contains_diagonal (p9EulerShift L Δ))
    intro z hz
    have hshift :
        p9EulerShift L Δ z ∈
          p3ObservableKrylovSpace (p9EulerShift L Δ) :=
      p3ObservableKrylovSpace_invariant (p9EulerShift L Δ) z hz
    have hdiff :
        Δ • L z ∈ p3ObservableKrylovSpace (p9EulerShift L Δ) := by
      have hrewrite : Δ • L z = p9EulerShift L Δ z - z := by
        rw [p9EulerShift_apply]
        abel
      rw [hrewrite]
      exact (p3ObservableKrylovSpace (p9EulerShift L Δ)).sub_mem hshift hz
    have hdiv :
        Δ⁻¹ • (Δ • L z) ∈
          p3ObservableKrylovSpace (p9EulerShift L Δ) :=
      (p3ObservableKrylovSpace (p9EulerShift L Δ)).smul_mem Δ⁻¹ hdiff
    have hcancel : Δ⁻¹ • (Δ • L z) = L z := by
      simp [smul_smul, hΔ]
    rw [hcancel] at hdiv
    exact hdiv

end P3
