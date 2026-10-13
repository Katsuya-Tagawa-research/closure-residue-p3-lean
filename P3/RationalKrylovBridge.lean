import P3.RationalMaximalPivot

/-!
# Exact rational rank reports for the original P3 observable closure

The canonical complex Krylov matrix has physical entries
    K_k[(x,y),(j,a)] = (φ^j (E_aa))[x,y].
A finite reindexing identifies its row/column axes with Fin-types.

If this reindexed complex matrix is *exactly* the coefficient extension
of an explicitly supplied rational matrix Q, the fully verified
exhaustive rational rank algorithm returns its exact complex rank,
which equals the original finite P3 closure rank.

No arbitrary complex dynamics is assumed to have rational entries.
This is a conditional computational bridge with precise hypotheses,
not yet an algorithm constructing rational Q from a given φ.
-/

noncomputable section

namespace P3

section RationalKrylovBridge

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- A numerically indexed copy of the exact canonical P3 Krylov
matrix; finite reindexing preserves its rank. -/
def p3FinIndexedKrylovMatrix (φ : Dynamics V) (k : ℕ) :
    Matrix (Fin (Fintype.card (V × V)))
      (Fin (Fintype.card (Fin (k + 1) × V))) ℂ :=
  (p3CanonicalKrylovMatrix φ k).reindex
    (Fintype.equivFin (V × V))
    (Fintype.equivFin (Fin (k + 1) × V))

/-- Changing the coordinate labels does not change the P3 closure rank. -/
theorem p3FinIndexedKrylovMatrix_rank_eq
    (φ : Dynamics V) (k : ℕ) :
    (p3FinIndexedKrylovMatrix φ k).rank = p3KrylovRank φ k := by
  calc
    (p3FinIndexedKrylovMatrix φ k).rank =
        (p3CanonicalKrylovMatrix φ k).rank := by
          exact Matrix.rank_reindex
            (Fintype.equivFin (V × V))
            (Fintype.equivFin (Fin (k + 1) × V))
            (p3CanonicalKrylovMatrix φ k)
    _ = p3KrylovRank φ k := p3CanonicalKrylovMatrix_rank_eq φ k

/-- Extract a numeric report from the exact rational automatic search.
The default is mathematically harmless because the search is proved
total for every finite rational matrix in P3.RationalMaximalPivot. -/
def p3RatKrylovReport {m n : ℕ}
    (Q : Matrix (Fin m) (Fin n) ℚ) : ℕ :=
  (p3RatAutoRank Q).getD 0

/-- For every finite rational rectangular matrix, the executable
numeric report equals its exact rational rank. -/
theorem p3RatKrylovReport_eq_rank {m n : ℕ}
    (Q : Matrix (Fin m) (Fin n) ℚ) :
    p3RatKrylovReport Q = Q.rank := by
  simp [p3RatKrylovReport, p3RatAutoRank_complete]

/-- Main conditional computational bridge: if the complex finite P3
Krylov matrix is entrywise the rational-to-complex cast of Q,
the *executable* rational report equals the original P3 closure rank. -/
theorem p3RatKrylovReport_eq_closure_rank
    (φ : Dynamics V) (k : ℕ)
    (Q : Matrix (Fin (Fintype.card (V × V)))
      (Fin (Fintype.card (Fin (k + 1) × V))) ℚ)
    (hQ : p3FinIndexedKrylovMatrix φ k = Q.map (Rat.castHom ℂ)) :
    p3RatKrylovReport Q = p3KrylovRank φ k := by
  calc
    p3RatKrylovReport Q = Q.rank := p3RatKrylovReport_eq_rank Q
    _ = (Q.map (Rat.castHom ℂ)).rank :=
      (p3RatAutoRank_complete_complex Q).symm
    _ = (p3FinIndexedKrylovMatrix φ k).rank :=
      congrArg Matrix.rank hQ.symm
    _ = p3KrylovRank φ k := p3FinIndexedKrylovMatrix_rank_eq φ k

/-- Two automatically computed rational reports detect precisely
the stabilization of the original P3 closure, given exact rational
presentations of the two complex orbit matrices. -/
theorem p3RatKrylovReport_stop_iff
    (φ : Dynamics V) (k : ℕ)
    (Qk : Matrix (Fin (Fintype.card (V × V)))
      (Fin (Fintype.card (Fin (k + 1) × V))) ℚ)
    (Qnext : Matrix (Fin (Fintype.card (V × V)))
      (Fin (Fintype.card (Fin (k + 2) × V))) ℚ)
    (hk : p3FinIndexedKrylovMatrix φ k = Qk.map (Rat.castHom ℂ))
    (hn : p3FinIndexedKrylovMatrix φ (k + 1) =
      Qnext.map (Rat.castHom ℂ)) :
    p3RatKrylovReport Qnext = p3RatKrylovReport Qk ↔
      closure φ (k + 1) = closure φ k := by
  rw [p3RatKrylovReport_eq_closure_rank φ (k + 1) Qnext hn,
    p3RatKrylovReport_eq_closure_rank φ k Qk hk]
  exact p3KrylovRank_eq_succ_iff_closure_plateau φ k

/-- Certified determination of the *first* P3 observable plateau
from a family of finite rational Krylov presentations through s+1,
using only exact automatic integer rank comparisons. -/
theorem p3ObservableKrylovDepth_eq_of_rational_reports
    (φ : Dynamics V) (s : ℕ)
    (Q : (k : ℕ) →
      Matrix (Fin (Fintype.card (V × V)))
        (Fin (Fintype.card (Fin (k + 1) × V))) ℚ)
    (hQ : ∀ k ≤ s + 1,
      p3FinIndexedKrylovMatrix φ k = (Q k).map (Rat.castHom ℂ))
    (hstop : p3RatKrylovReport (Q (s + 1)) =
      p3RatKrylovReport (Q s))
    (hearlier : ∀ k < s,
      p3RatKrylovReport (Q k) <
        p3RatKrylovReport (Q (k + 1))) :
    p3ObservableKrylovDepth φ = s := by
  apply p3ObservableKrylovDepth_eq_of_rank_certificate φ s
  · have hnext :=
      p3RatKrylovReport_eq_closure_rank φ (s + 1) (Q (s + 1))
        (hQ (s + 1) (Nat.le_refl _))
    have hthis :=
      p3RatKrylovReport_eq_closure_rank φ s (Q s)
        (hQ s (by omega))
    exact hnext.symm.trans (hstop.trans hthis)
  · intro k hk
    have hthis :=
      p3RatKrylovReport_eq_closure_rank φ k (Q k)
        (hQ k (by omega))
    have hnext :=
      p3RatKrylovReport_eq_closure_rank φ (k + 1) (Q (k + 1))
        (hQ (k + 1) (by omega))
    exact hthis ▸ hnext ▸ hearlier k hk

end RationalKrylovBridge

end P3
