import P3.P9TTFiniteSymbol

/-!
# P9 finite second-jet descent obstruction

The first response derivative A:T -> O_1 defines first-order silent
tangent directions ker A. A bilinear second response H:T×T->O_2
can factor bilinearly through the first response A only if it vanishes
when either argument is first-order silent.

We prove this necessary condition abstractly over rational vector
spaces and give an explicit finite polynomial second-jet example:
Sigma(x,y)=(x,y²), at the origin. Its first derivative kills e_y,
while the second derivative on (e_y,e_y) is nonzero.

This is a precise counterexample to automatic descent onto the
first response quotient. It does not construct the physical P6 CR
second response jet or a spatial spin-two tensor.
-/

namespace P3

section AbstractKernelObstruction

variable {T O₁ O₂ : Type*}
  [AddCommGroup T] [Module ℚ T]
  [AddCommGroup O₁] [Module ℚ O₁]
  [AddCommGroup O₂] [Module ℚ O₂]

/-- Factorization of a bilinear Hessian through the first derivative
forces every first-order silent direction to be second-order silent
in both slots. Only necessity is stated. -/
theorem p9SecondJet_factor_requires_kernel_silence
    (A : T →ₗ[ℚ] O₁)
    (H : T →ₗ[ℚ] T →ₗ[ℚ] O₂)
    (B : O₁ →ₗ[ℚ] O₁ →ₗ[ℚ] O₂)
    (hFactor : ∀ u v, H u v = B (A u) (A v))
    (k : T) (hk : A k = 0) (v : T) :
    H k v = 0 := by
  rw [hFactor k v, hk]
  simp

end AbstractKernelObstruction

/-- Finite control coordinates (x,y). -/
def p9ToySilentY : Fin 2 → ℚ := ![(0 : ℚ), 1]

/-- First derivative of Sigma(x,y)=(x,y²) at zero, viewed in
the first observable coordinate. -/
def p9ToyFirstDerivative (u : Fin 2 → ℚ) : ℚ := u 0

/-- The nontrivial second response component of the same map. -/
def p9ToySecondDerivative (u v : Fin 2 → ℚ) : ℚ :=
  2 * u 1 * v 1

/-- The y-direction is silent to first order. -/
theorem p9ToySilentY_first_zero :
    p9ToyFirstDerivative p9ToySilentY = 0 := by
  norm_num [p9ToyFirstDerivative, p9ToySilentY]

/-- Exactly the same direction has a nonzero second response. -/
theorem p9ToySilentY_second_nonzero :
    p9ToySecondDerivative p9ToySilentY p9ToySilentY = 2 := by
  norm_num [p9ToySecondDerivative, p9ToySilentY]

/-- No bilinear factorization through the first response can reproduce
this nonzero second variation: any bilinear B satisfies B(0,0)=0. -/
theorem p9ToySecondJet_no_factor_through_first :
    ¬ ∃ B : ℚ → ℚ → ℚ,
      (∀ z, B 0 z = 0) ∧
      (∀ u v : Fin 2 → ℚ,
        p9ToySecondDerivative u v =
          B (p9ToyFirstDerivative u) (p9ToyFirstDerivative v)) := by
  rintro ⟨B, hzero, hfactor⟩
  have h := hfactor p9ToySilentY p9ToySilentY
  rw [p9ToySilentY_first_zero, hzero] at h
  norm_num [p9ToySilentY_second_nonzero] at h

end P3
