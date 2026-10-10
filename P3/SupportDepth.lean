import P3.Support

/-!
# P3 support-depth bridge (Lean 4 / Mathlib)

This module is additive: it leaves the frozen P3 definitions unchanged.
It uses bounded walks in the *symmetric support* of the matrix H, avoiding
unnecessary connectivity/finite-distance assumptions.

This module has passed a GitHub Actions Lean typecheck. The final section
includes the universal support-halving identity. Axiom audit is separate.
-/

noncomputable section

open scoped BigOperators
open Matrix

namespace P3

section SupportDepth

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Undirected support relation of a matrix. It does not require Hermiticity. -/
def coupled (H : A V) (x y : V) : Prop :=
  H x y ≠ 0 ∨ H y x ≠ 0

/-- A walk of at most `n` support-edges, with both prepend/append forms. -/
inductive WalkWithin (H : A V) : ℕ → V → V → Prop where
  | zero (x : V) : WalkWithin H 0 x x
  | carry {n : ℕ} {x y : V} :
      WalkWithin H n x y → WalkWithin H (n + 1) x y
  | prepend {n : ℕ} {x y z : V} :
      coupled H x z → WalkWithin H n z y → WalkWithin H (n + 1) x y
  | append {n : ℕ} {x y z : V} :
      WalkWithin H n x z → coupled H z y → WalkWithin H (n + 1) x y

/-- A bounded walk remains bounded by every larger number of steps. -/
omit [Fintype V] [DecidableEq V] in
theorem walkWithin_mono (H : A V) {n m : ℕ} {x y : V}
    (hnm : n ≤ m) (h : WalkWithin H n x y) :
    WalkWithin H m x y := by
  induction m, hnm using Nat.le_induction with
  | base => exact h
  | succ m _ ih => exact WalkWithin.carry ih

/-- Matrices whose possible nonzero coordinates are within n support steps. -/
def localMatrix (H : A V) (n : ℕ) : Submodule ℂ (A V) where
  carrier := {X | ∀ x y, ¬ WalkWithin H n x y → X x y = 0}
  zero_mem' := by
    intro x y hfar
    rfl
  add_mem' := by
    intro X Y hX hY x y hfar
    simp [hX x y hfar, hY x y hfar]
  smul_mem' := by
    intro c X hX x y hfar
    simp [hX x y hfar]

theorem localMatrix_mono (H : A V) {n m : ℕ} (hnm : n ≤ m) :
    localMatrix H n ≤ localMatrix H m := by
  intro X hX x y hfar
  exact hX x y (fun hx => hfar (walkWithin_mono H hnm hx))

/-- Every diagonal observable has local depth zero. -/
theorem diagonal_local (H : A V)
    (d : diagonalSubmodule (V := V)) :
    d.1 ∈ localMatrix H 0 := by
  rcases d with ⟨_, ⟨p, rfl⟩⟩
  intro x y hfar
  have hxy : x ≠ y := by
    intro heq
    subst y
    exact hfar (WalkWithin.zero x)
  simp [diagonalEmbedding_apply, hxy]

/-- Infinitesimal commutator, without the harmless scalar `-i`. -/
def commutatorDynamics (H : A V) : Dynamics V where
  toFun X := H * X - X * H
  map_add' X Y := by
    ext x y
    simp [Matrix.mul_apply, mul_add, add_mul]
    ring
  map_smul' c X := by
    ext x y
    simp [Matrix.mul_apply, Finset.mul_sum, mul_sub, mul_comm]

/-- One commutator increases the maximum support distance by at most one. -/
theorem commutator_step_local (H : A V) (n : ℕ)
    {X : A V} (hX : X ∈ localMatrix H n) :
    commutatorDynamics H X ∈ localMatrix H (n + 1) := by
  intro x y hfar
  have hleft : (H * X) x y = 0 := by
    rw [Matrix.mul_apply]
    apply Finset.sum_eq_zero
    intro z _
    by_cases hh : H x z = 0
    · simp [hh]
    · have hnot : ¬ WalkWithin H n z y := by
        intro hz
        exact hfar (WalkWithin.prepend (Or.inl hh) hz)
      simp [hX z y hnot]
  have hright : (X * H) x y = 0 := by
    rw [Matrix.mul_apply]
    apply Finset.sum_eq_zero
    intro z _
    by_cases hh : H z y = 0
    · simp [hh]
    · have hnot : ¬ WalkWithin H n x z := by
        intro hz
        exact hfar (WalkWithin.append hz (Or.inl hh))
      simp [hX x z hnot]
  simp [commutatorDynamics, hleft, hright]

/-- Iterated commutators of diagonal matrices have depth at most n. -/
theorem commutator_iterate_local (H : A V)
    (d : diagonalSubmodule (V := V)) (n : ℕ) :
    ((commutatorDynamics H) ^ n) d.1 ∈ localMatrix H n := by
  induction n with
  | zero => simpa using diagonal_local H d
  | succ n ih =>
      simpa [pow_succ'] using commutator_step_local H n ih

/-- Every element of the original P3 closure filtration obeys walk-locality. -/
theorem commutator_closure_local (H : A V) (n : ℕ) :
    closure (commutatorDynamics H) n ≤ localMatrix H n := by
  apply Submodule.span_le.mpr
  intro X hX
  rcases hX with ⟨d, m, hm, rfl⟩
  exact localMatrix_mono H hm (commutator_iterate_local H d m)

/-- Every element of the P3 hidden-defect filtration obeys walk-locality. -/
theorem commutator_hidden_local (H : A V) (n : ℕ) :
    hidden (commutatorDynamics H) n ≤ localMatrix H n := by
  intro X hX
  rcases hX with ⟨Y, hY, rfl⟩
  intro x y hfar
  have hxy : x ≠ y := by
    intro heq
    subst y
    exact hfar (walkWithin_mono H (Nat.zero_le n) (WalkWithin.zero x))
  have hy : Y x y = 0 :=
    (commutator_closure_local H n hY) x y hfar
  simp [offProjection_apply, delta_apply, hxy, hy]

/-- The directed-edge coordinate as a complex-linear functional. -/
def flowCoordinate (x y : V) (hxy : x ≠ y) :
    EdgeSpace V →ₗ[ℂ] ℂ where
  toFun f := f.ofLp ⟨(x, y), hxy⟩
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

@[simp]
theorem flowCoordinate_apply (x y : V) (hxy : x ≠ y)
    (f : EdgeSpace V) :
    flowCoordinate x y hxy f = f.ofLp ⟨(x, y), hxy⟩ := rfl

/-- A P3 hidden flow cannot be supported beyond half its total defect depth. -/
theorem commutator_flow_local (H : A V) (k : ℕ)
    {x y : V} (hxy : x ≠ y)
    (hfar : ¬ WalkWithin H (k / 2) x y)
    {f : EdgeSpace V}
    (hf : f ∈ hiddenFlow (commutatorDynamics H) k) :
    edgeMatrix (V := V) f x y = 0 := by
  have hker : hiddenFlow (commutatorDynamics H) k ≤
      LinearMap.ker (flowCoordinate x y hxy) := by
    apply Submodule.span_le.mpr
    intro g hg
    rcases hg with ⟨i, j, hij, z, w, hz, hw, rfl⟩
    change flowCoordinate x y hxy (hadamardFlow z w) = 0
    rw [flowCoordinate_apply, hadamardFlow_apply]
    by_cases hle : i ≤ j
    · have hik : i ≤ k / 2 := by omega
      have hiFar : ¬ WalkWithin H i x y := by
        intro hi
        exact hfar (walkWithin_mono H hik hi)
      have hzx : z.1 x y = 0 :=
        (commutator_hidden_local H i hz) x y hiFar
      simp [hzx]
    · have hjk : j ≤ k / 2 := by omega
      have hjFar : ¬ WalkWithin H j x y := by
        intro hj
        exact hfar (walkWithin_mono H hjk hj)
      have hwx : w.1 x y = 0 :=
        (commutator_hidden_local H j hw) x y hjFar
      simp [hwx]
  have hz : flowCoordinate x y hxy f = 0 := hker hf
  simpa only [flowCoordinate_apply, edgeMatrix_offdiag (V := V) f hxy] using hz

/-- Exact P3 support implies a bounded walk in at least one orientation. -/
theorem commutator_support_depth (H : A V) (k : ℕ) {x y : V}
    (h : (supportGraph (commutatorDynamics H) k).Adj x y) :
    WalkWithin H (k / 2) x y ∨ WalkWithin H (k / 2) y x := by
  rcases (supportGraph_adj (φ := commutatorDynamics H) (k := k) x y).mp h with
    ⟨hne, f, hf, hfne⟩ | ⟨hne, f, hf, hfne⟩
  · left
    by_contra hfar
    exact hfne (commutator_flow_local H k hne hfar hf)
  · right
    by_contra hfar
    exact hfne (commutator_flow_local H k hne hfar hf)

/-! ## Support-halving identity from the frozen P3 filtration

This theorem is algebraic. It requires neither a Hamiltonian nor graph saturation.
It is deliberately distinct from the `commutator_support_depth` theorem.
-/

/-- Off-diagonal coordinate-support relation for the hidden defect space. -/
def defectActive (φ : Dynamics V) (d : ℕ) (x y : V) : Prop :=
  x ≠ y ∧ ∃ z : A V, z ∈ hidden φ d ∧ z x y ≠ 0

/-- `defectActive` is exactly `flowActive` at twice the hidden depth,
with integer division accommodating odd total depths. -/
theorem flowActive_iff_defectActive (φ : Dynamics V) (k : ℕ)
    (x y : V) :
    flowActive φ k x y ↔ defectActive φ (k / 2) x y := by
  classical
  constructor
  · rintro ⟨hxy, f, hf, hfne⟩
    refine ⟨hxy, ?_⟩
    by_contra hn
    have hzero : ∀ z : A V, z ∈ hidden φ (k / 2) → z x y = 0 := by
      intro z hz
      by_contra hne
      exact hn ⟨z, hz, hne⟩
    have hker : hiddenFlow φ k ≤
        LinearMap.ker (flowCoordinate x y hxy) := by
      apply Submodule.span_le.mpr
      intro g hg
      rcases hg with ⟨i, j, hij, z, w, hz, hw, rfl⟩
      change flowCoordinate x y hxy (hadamardFlow z w) = 0
      rw [flowCoordinate_apply, hadamardFlow_apply]
      by_cases hij' : i ≤ j
      · have hik : i ≤ k / 2 := by omega
        have hz' : z.1 x y = 0 :=
          hzero z.1 ((hidden_mono φ hik) hz)
        simp [hz']
      · have hjk : j ≤ k / 2 := by omega
        have hw' : w.1 x y = 0 :=
          hzero w.1 ((hidden_mono φ hjk) hw)
        simp [hw']
    have hfzero : flowCoordinate x y hxy f = 0 := hker hf
    apply hfne
    simpa only [flowCoordinate_apply, edgeMatrix_offdiag (V := V) f hxy] using hfzero
  · rintro ⟨hxy, z, hz, hzxy⟩
    let zOff : OffDiag (V := V) :=
      ⟨z, (hidden_le_OffDiag φ (k / 2)) hz⟩
    have hzOff : zOff.1 ∈ hidden φ (k / 2) := hz
    have hdepth : k / 2 + k / 2 ≤ k := by omega
    have hflow : hadamardFlow zOff zOff ∈ hiddenFlow φ k :=
      hadamardFlow_mem_hiddenFlow φ hdepth zOff zOff hzOff hzOff
    have hstar : star (z x y) ≠ 0 := by
      intro hstar0
      apply hzxy
      have h := congrArg star hstar0
      simpa using h
    refine ⟨hxy, hadamardFlow zOff zOff, hflow, ?_⟩
    rw [edgeMatrix_hadamardFlow_apply]
    exact mul_ne_zero hzxy hstar

/-- Undirected support of the hidden defect subspace at a fixed depth. -/
def defectSupportGraph (φ : Dynamics V) (d : ℕ) : SimpleGraph V where
  Adj x y := defectActive φ d x y ∨ defectActive φ d y x
  symm := ⟨by
    intro x y h
    exact h.symm⟩
  loopless := ⟨by
    intro x h
    rcases h with h | h
    · exact h.1 rfl
    · exact h.1 rfl⟩

/-- Exact graph identity: P3's flow support at total depth k is precisely
 the defect-coordinate support at depth floor(k/2). No graph-saturation
 or dynamical hypotheses are used. -/
theorem supportGraph_eq_defectSupportGraph (φ : Dynamics V) (k : ℕ) :
    supportGraph φ k = defectSupportGraph φ (k / 2) := by
  apply SimpleGraph.ext
  funext x y
  apply propext
  change (flowActive φ k x y ∨ flowActive φ k y x) ↔
    (defectActive φ (k / 2) x y ∨ defectActive φ (k / 2) y x)
  constructor
  · rintro (h | h)
    · exact Or.inl ((flowActive_iff_defectActive φ k x y).mp h)
    · exact Or.inr ((flowActive_iff_defectActive φ k y x).mp h)
  · rintro (h | h)
    · exact Or.inl ((flowActive_iff_defectActive φ k x y).mpr h)
    · exact Or.inr ((flowActive_iff_defectActive φ k y x).mpr h)

end SupportDepth

end P3