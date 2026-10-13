import P3.RationalKrylovBridge

/-!
# Bounded executable search for the first P3 observable plateau

An exact rational Krylov presentation at each queried depth supplies
executable ranks. A structurally recursive bounded search returns
the first adjacent equality. It is proved sound and complete within
the bound, and conditionally identified with the original P3 depth.

This is finite and conditional on exact rational presentations.
It does not rationalize arbitrary complex-linear dynamics.
-/

namespace P3

/-- Search at most `fuel` consecutive comparisons, beginning at `start`.
The Boolean comparison is exact, and the recursion is structural on fuel. -/
def p3FirstEqualRankAux (r : ℕ → ℕ) : ℕ → ℕ → Option ℕ
  | _, 0 => none
  | start, fuel + 1 =>
      if r (start + 1) = r start then some start
      else p3FirstEqualRankAux r (start + 1) fuel

/-- An accepted candidate is the first equality in the searched window. -/
theorem p3FirstEqualRankAux_sound (r : ℕ → ℕ) :
    ∀ fuel start s, p3FirstEqualRankAux r start fuel = some s →
      start ≤ s ∧ s < start + fuel ∧
      r (s + 1) = r s ∧
      (∀ k, start ≤ k → k < s → r (k + 1) ≠ r k) := by
  intro fuel
  induction fuel with
  | zero =>
      intro start s h
      simp [p3FirstEqualRankAux] at h
  | succ fuel ih =>
      intro start s h
      by_cases hnow : r (start + 1) = r start
      · have hs : s = start := by
          simpa [p3FirstEqualRankAux, hnow] using h.symm
        subst s
        refine ⟨by omega, by omega, hnow, ?_⟩
        intro k hk hlt
        omega
      · have hrec : p3FirstEqualRankAux r (start + 1) fuel = some s := by
          simpa [p3FirstEqualRankAux, hnow] using h
        obtain ⟨hlo, hhi, heq, hminimal⟩ :=
          ih (start + 1) s hrec
        refine ⟨by omega, by omega, heq, ?_⟩
        intro k hk hks
        by_cases hfirst : k = start
        · simpa [hfirst] using hnow
        · exact hminimal k (by omega) hks

/-- If there is an equality inside the fuel window, the finite
search returns some candidate. -/
theorem p3FirstEqualRankAux_complete (r : ℕ → ℕ) :
    ∀ fuel start witness, start ≤ witness →
      witness < start + fuel →
      r (witness + 1) = r witness →
      ∃ s, p3FirstEqualRankAux r start fuel = some s := by
  intro fuel
  induction fuel with
  | zero =>
      intro start witness hlo hhi _
      omega
  | succ fuel ih =>
      intro start witness hlo hhi hw
      by_cases hnow : r (start + 1) = r start
      · exact ⟨start, by simp [p3FirstEqualRankAux, hnow]⟩
      · have hnext : start + 1 ≤ witness := by
          by_contra hnot
          have heq : witness = start := by omega
          exact hnow (by simpa [heq] using hw)
        obtain ⟨s, hs⟩ := ih (start + 1) witness hnext (by omega) hw
        exact ⟨s, by simp [p3FirstEqualRankAux, hnow, hs]⟩

/-- A computational spelling of the rational rank reporter.
The earlier report lives in a noncomputable theorem section; this
definition is independent of that declaration's compilation status. -/
def p3RatComputableRank {m n : ℕ}
    (Q : Matrix (Fin m) (Fin n) ℚ) : ℕ :=
  (p3RatAutoRank Q).getD 0

/-- The computational spelling is definitionally equal to the audited
rational report used by the complex P3 bridge. -/
theorem p3RatComputableRank_eq_report {m n : ℕ}
    (Q : Matrix (Fin m) (Fin n) ℚ) :
    p3RatComputableRank Q = p3RatKrylovReport Q := rfl

/-- The executable stopping-depth search. It queries exact rational
matrices at depths 0 through `bound+1`. -/
def p3RatFirstStoppingDepth {V : Type*} [Fintype V] (bound : ℕ)
    (Q : (k : ℕ) → Matrix (Fin (Fintype.card (V × V)))
      (Fin (Fintype.card (Fin (k + 1) × V))) ℚ) :
    Option ℕ :=
  p3FirstEqualRankAux (fun k => p3RatComputableRank (Q k)) 0 (bound + 1)

noncomputable section

section FiniteStoppingDepth

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- At zero depth the observable Krylov rank is exactly the number
of diagonal seeds, including the empty vertex-set case. -/
theorem p3KrylovRank_zero_card (φ : Dynamics V) :
    p3KrylovRank φ 0 = Fintype.card V := by
  simp [p3KrylovRank, closure_zero, diagonalSubmodule_finrank]

/-- The exact first plateau consumes at least one new rank per depth,
so it lies within the ambient-dimension minus seed-dimension budget. -/
theorem p3ObservableKrylovDepth_le_seed_gap (φ : Dynamics V) :
    p3ObservableKrylovDepth φ ≤
      p3AlgebraDimension (V := V) - Fintype.card V := by
  let s := p3ObservableKrylovDepth φ
  have hgrowth : ∀ k : ℕ, k ≤ s →
      Fintype.card V + k ≤ p3KrylovRank φ k := by
    intro k
    induction k with
    | zero =>
        intro _
        simpa [p3KrylovRank_zero_card φ]
    | succ k ih =>
        intro hk
        have hlt : k < s := by omega
        have hstep := p3KrylovRank_strict_before φ k hlt
        have hprev := ih (by omega)
        omega
  have hlarge := hgrowth s (le_refl s)
  have hupper : p3KrylovRank φ s ≤
      p3AlgebraDimension (V := V) := by
    exact Submodule.finrank_le (closure φ s)
  dsimp [s] at *
  omega

/-- For a finite vertex set the seed-gap bound is N²-N.
The bound is zero both for N=0 and N=1. -/
theorem p3ObservableKrylovDepth_le_quadratic_gap (φ : Dynamics V) :
    p3ObservableKrylovDepth φ ≤
      Fintype.card V * Fintype.card V - Fintype.card V := by
  have h := p3ObservableKrylovDepth_le_seed_gap φ
  have hdim : p3AlgebraDimension (V := V) =
      Fintype.card V * Fintype.card V := by
    simpa [p3AlgebraDimension, A] using (Module.finrank_matrix ℂ ℂ V V)
  simpa [hdim] using h

/-- Under exact rational presentation at all depths through bound+1,
a bounded search with bound at least the true plateau returns precisely
the original P3 first observable closure depth. -/
theorem p3RatFirstStoppingDepth_eq_observable
    (φ : Dynamics V) (bound : ℕ)
    (Q : (k : ℕ) →
      Matrix (Fin (Fintype.card (V × V)))
        (Fin (Fintype.card (Fin (k + 1) × V))) ℚ)
    (hQ : ∀ k ≤ bound + 1,
      p3FinIndexedKrylovMatrix φ k = (Q k).map (Rat.castHom ℂ))
    (hbound : p3ObservableKrylovDepth φ ≤ bound) :
    p3RatFirstStoppingDepth bound Q =
      some (p3ObservableKrylovDepth φ) := by
  let r : ℕ → ℕ := fun k => p3RatComputableRank (Q k)
  let depth := p3ObservableKrylovDepth φ
  have hplateau : r (depth + 1) = r depth := by
    change p3RatComputableRank (Q (depth + 1)) =
      p3RatComputableRank (Q depth)
    rw [p3RatComputableRank_eq_report, p3RatComputableRank_eq_report]
    apply (p3RatKrylovReport_stop_iff φ depth
      (Q depth) (Q (depth + 1))
      (hQ depth (by omega))
      (hQ (depth + 1) (by omega))).mpr
    exact p3ObservableKrylovDepth_spec φ
  obtain ⟨s, hs⟩ :=
    p3FirstEqualRankAux_complete r (bound + 1) 0 depth
      (Nat.zero_le _) (by omega) hplateau
  obtain ⟨_, hsBound, hsStop, hsMinimal⟩ :=
    p3FirstEqualRankAux_sound r (bound + 1) 0 s hs
  have hsP3 : closure φ (s + 1) = closure φ s := by
    have hsStop' : p3RatKrylovReport (Q (s + 1)) =
        p3RatKrylovReport (Q s) := by
      simpa only [r, p3RatComputableRank_eq_report] using hsStop
    exact (p3RatKrylovReport_stop_iff φ s
      (Q s) (Q (s + 1))
      (hQ s (by omega)) (hQ (s + 1) (by omega))).mp hsStop'
  have hsEq : s = depth := by
    apply Nat.le_antisymm
    · by_contra hnot
      have hdlt : depth < s := by omega
      exact hsMinimal depth (Nat.zero_le _) hdlt hplateau
    · by_contra hnot
      have hslt : s < depth := by omega
      exact (p3ObservableKrylovDepth_strict_before φ s hslt) hsP3
  change p3FirstEqualRankAux r 0 (bound + 1) = some depth
  simpa [hsEq] using hs

/-- Automatic first plateau determination using the intrinsic
finite seed-gap bound, without a minpoly nonconstancy hypothesis. -/
theorem p3RatFirstStoppingDepth_complete
    (φ : Dynamics V)
    (Q : (k : ℕ) →
      Matrix (Fin (Fintype.card (V × V)))
        (Fin (Fintype.card (Fin (k + 1) × V))) ℚ)
    (hQ : ∀ k ≤
      p3AlgebraDimension (V := V) - Fintype.card V + 1,
      p3FinIndexedKrylovMatrix φ k = (Q k).map (Rat.castHom ℂ)) :
    p3RatFirstStoppingDepth
      (p3AlgebraDimension (V := V) - Fintype.card V) Q =
        some (p3ObservableKrylovDepth φ) :=
  p3RatFirstStoppingDepth_eq_observable φ _ Q hQ
    (p3ObservableKrylovDepth_le_seed_gap φ)

end FiniteStoppingDepth
end

end P3
