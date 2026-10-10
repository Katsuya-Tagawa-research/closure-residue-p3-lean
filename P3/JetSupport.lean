import P3.SupportDepth

/-!
# P3 jet support: formal Taylor coefficient locality

This file is an additive extension to the audited P3.SupportDepth.
It proves locality and quadratic order bounds for the unnormalized
commutator jets. Multiplying degree-n jets by the physical nonzero factor
(-i)^n/n! does not affect the vanishing conclusions.

No generic noncancellation or graph saturation is assumed.
-/

noncomputable section

open scoped BigOperators

namespace P3

section JetSupport

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- The unnormalized nth Taylor jet for the commutator generator. -/
def commutatorJet (H : A V)
    (d : diagonalSubmodule (V := V)) (n : ℕ) : A V :=
  ((commutatorDynamics H) ^ n) d.1

/-- The nth jet is supported within n steps of the matrix-coupling graph. -/
theorem commutatorJet_mem_local (H : A V)
    (d : diagonalSubmodule (V := V)) (n : ℕ) :
    commutatorJet H d n ∈ localMatrix H n := by
  exact commutator_iterate_local H d n

/-- A jet coefficient vanishes outside its depth-n support region. -/
theorem commutatorJet_far_zero (H : A V)
    (d : diagonalSubmodule (V := V)) (n : ℕ)
    (x y : V) (hfar : ¬ WalkWithin H n x y) :
    (commutatorJet H d n) x y = 0 := by
  exact (commutatorJet_mem_local H d n) x y hfar

/-- Degree-n coefficient of the Hadamard product of two formal jet series.
No factorial normalization is needed for its support bounds. -/
def jetHadamardCoeff (H : A V)
    (d e : diagonalSubmodule (V := V))
    (x y : V) (n : ℕ) : ℂ :=
  ∑ j ∈ Finset.range (n + 1),
    (commutatorJet H d j) x y *
      star ((commutatorJet H e (n - j)) x y)

/-- If n is smaller than twice the shortest admissible excursion depth,
then the degree-n hidden Hadamard coefficient is identically zero.
The estimate is only a vanishing result; it does not assert that the
next coefficient is nonzero. -/
theorem jetHadamardCoeff_far_zero
    (H : A V) (d e : diagonalSubmodule (V := V))
    (x y : V) (r n : ℕ)
    (hfar : ¬ WalkWithin H r x y)
    (hn : n ≤ 2 * r + 1) :
    jetHadamardCoeff H d e x y n = 0 := by
  unfold jetHadamardCoeff
  apply Finset.sum_eq_zero
  intro j hj
  have hjle : j ≤ n := Nat.le_of_lt_succ (Finset.mem_range.mp hj)
  have hsplit : j ≤ r ∨ n - j ≤ r := by omega
  rcases hsplit with hjr | hnr
  · have hfarj : ¬ WalkWithin H j x y := by
      intro hwalk
      exact hfar (walkWithin_mono H hjr hwalk)
    have hz : (commutatorJet H d j) x y = 0 :=
      commutatorJet_far_zero H d j x y hfarj
    simp [hz]
  · have hfarnj : ¬ WalkWithin H (n - j) x y := by
      intro hwalk
      exact hfar (walkWithin_mono H hnr hwalk)
    have hz : (commutatorJet H e (n - j)) x y = 0 :=
      commutatorJet_far_zero H e (n - j) x y hfarnj
    simp [hz]

end JetSupport

end P3
