import P3.RationalComplexRank

/-!
# Witness-relative completeness of the exact rational rank search

The rational search in P3.RationalAutoPivots already has verified
soundness. This module formalizes the *finite-search completeness*
step: if one correct pivot certificate exists among the finitely
enumerated candidates at rank r, the automatic search cannot return
none. Moreover, the returned exact rank equals r.

This is a useful computational adequacy theorem, but it does NOT yet
prove that a maximal invertible minor and rank factorization exist
for every rational rectangular matrix. That separate linear-algebra
existence argument is required for unconditional totality.
-/

namespace P3

section AutoRankSearchAdequacy

/-- Every individually accepted pivot appears in the finite exhaustive
candidate predicate at the same proposed rank. -/
theorem p3RatAutoRankAt_of_accepted {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) (r : ℕ)
    (rows : Fin r → Fin m) (cols : Fin r → Fin n)
    (h : p3RatPivotAccepted A r rows cols = true) :
    p3RatAutoRankAt A r = true := by
  simp only [p3RatAutoRankAt, decide_eq_true_eq]
  exact ⟨rows, cols, h⟩

/-- A finite search of depth fuel cannot miss an already accepted
candidate at rank r ≤ fuel, even if it finds a higher rank first. -/
theorem p3RatAutoRankFuel_exists_of_accepted_rank {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) :
    ∀ (fuel r : ℕ), r ≤ fuel →
      p3RatAutoRankAt A r = true →
      ∃ s : ℕ, p3RatAutoRankFuel A fuel = some s := by
  intro fuel
  induction fuel with
  | zero =>
      intro r hr hacc
      have hr0 : r = 0 := by omega
      subst r
      exact ⟨0, by simp [p3RatAutoRankFuel, hacc]⟩
  | succ fuel ih =>
      intro r hr hacc
      by_cases htop : p3RatAutoRankAt A (fuel + 1) = true
      · exact ⟨fuel + 1, by simp [p3RatAutoRankFuel, htop]⟩
      · have hrlt : r ≤ fuel := by
          by_contra hle
          have heq : r = fuel + 1 := by omega
          exact htop (heq ▸ hacc)
        obtain ⟨s, hs⟩ := ih r hrlt hacc
        exact ⟨s, by simp [p3RatAutoRankFuel, htop, hs]⟩

/-- If a pivot certificate exists within the geometric rank bound,
the fully automatic rational search returns an actual value. -/
theorem p3RatAutoRank_exists_of_pivot {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) (r : ℕ)
    (hbound : r ≤ min m n)
    (rows : Fin r → Fin m) (cols : Fin r → Fin n)
    (h : p3RatPivotAccepted A r rows cols = true) :
    ∃ s : ℕ, p3RatAutoRank A = some s := by
  exact p3RatAutoRankFuel_exists_of_accepted_rank A (min m n) r
    hbound (p3RatAutoRankAt_of_accepted A r rows cols h)

/-- Under existence of one valid pivot certificate, the *automatic*
result is forced to equal that certificate's rank, over ℚ. -/
theorem p3RatAutoRank_eq_some_of_pivot {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) (r : ℕ)
    (hbound : r ≤ min m n)
    (rows : Fin r → Fin m) (cols : Fin r → Fin n)
    (h : p3RatPivotAccepted A r rows cols = true) :
    p3RatAutoRank A = some r := by
  obtain ⟨s, hs⟩ := p3RatAutoRank_exists_of_pivot A r hbound rows cols h
  have hsRank : A.rank = s := p3RatAutoRank_sound A s hs
  have hrRank : A.rank = r := p3RatPivotAccepted_sound A r rows cols h
  have hsr : s = r := hsRank.symm.trans hrRank
  simpa only [hsr] using hs

/-- The same rank returned by the automated rational certificate
has been proved correct after coefficient extension to ℂ. -/
theorem p3RatAutoRank_eq_some_complex_of_pivot {m n : ℕ}
    (A : Matrix (Fin m) (Fin n) ℚ) (r : ℕ)
    (hbound : r ≤ min m n)
    (rows : Fin r → Fin m) (cols : Fin r → Fin n)
    (h : p3RatPivotAccepted A r rows cols = true) :
    (A.map (Rat.castHom ℂ)).rank = r := by
  exact p3RatAutoRank_complex_sound A r
    (p3RatAutoRank_eq_some_of_pivot A r hbound rows cols h)

end AutoRankSearchAdequacy
end P3
