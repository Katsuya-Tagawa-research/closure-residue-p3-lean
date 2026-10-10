import P3.JetSupport
import Mathlib.RingTheory.PowerSeries.Order
import Mathlib.RingTheory.Ideal.Span

/-!
# Jet support: formal power series and exact order doubling

The formal parameter T is real (formal), so coefficient conjugation
is applied to coefficients only, not to the parameter.

The order theorem is meaningful for any nonzero formal series:
the first nonzero coefficient at depth r produces a self-Hadamard
series whose exact order is 2r. The proof is a general formal-series
statement and does not claim a nonzero microscopic CR residue.
-/

noncomputable section

namespace P3

section JetPowerSeries

/-- Conjugate every complex coefficient, leaving the formal parameter fixed. -/
def jetConjugate (f : PowerSeries ℂ) : PowerSeries ℂ :=
  PowerSeries.mk (fun n => star ((PowerSeries.coeff n) f))

@[simp]
theorem jetConjugate_coeff (f : PowerSeries ℂ) (n : ℕ) :
    (PowerSeries.coeff n) (jetConjugate f) =
      star ((PowerSeries.coeff n) f) := by
  simp [jetConjugate]

/-- Order of a conjugated formal series at any finite order. -/
theorem jetConjugate_order_eq_nat
    (f : PowerSeries ℂ) (r : ℕ)
    (hf : f.order = (r : ℕ∞)) :
    (jetConjugate f).order = (r : ℕ∞) := by
  obtain ⟨hfirst, hbefore⟩ := (PowerSeries.order_eq_nat).mp hf
  apply (PowerSeries.order_eq_nat).mpr
  constructor
  · intro hzero
    apply hfirst
    have hs := congrArg star hzero
    simpa using hs
  · intro i hi
    simp [hbefore i hi]

/-- Exact twice-order law for the formal hidden self-flow. -/
theorem jetSelfFlow_order_double
    (f : PowerSeries ℂ) (r : ℕ)
    (hf : f.order = (r : ℕ∞)) :
    (f * jetConjugate f).order = ((2 * r : ℕ) : ℕ∞) := by
  calc
    (f * jetConjugate f).order =
        f.order + (jetConjugate f).order := PowerSeries.order_mul f (jetConjugate f)
    _ = (r : ℕ∞) + (r : ℕ∞) := by
      rw [hf, jetConjugate_order_eq_nat f r hf]
    _ = ((2 * r : ℕ) : ℕ∞) := by
      simp [two_mul, Nat.cast_add]

/-- The order-doubled hidden flow has a nonzero leading coefficient. -/
theorem jetSelfFlow_leading_ne_zero
    (f : PowerSeries ℂ) (r : ℕ)
    (hf : f.order = (r : ℕ∞)) :
    (PowerSeries.coeff (2 * r)) (f * jetConjugate f) ≠ 0 := by
  exact (PowerSeries.order_eq_nat).mp
    (jetSelfFlow_order_double f r hf) |>.1

/-- Powers of the formal parameter define the standard jet ideals. -/
def jetIdeal (r : ℕ) : Ideal (PowerSeries ℂ) :=
  Ideal.span {((PowerSeries.X : PowerSeries ℂ) ^ r)}

/-- Jet ideal membership exactly means vanishing of all earlier coefficients. -/
theorem mem_jetIdeal_iff
    (f : PowerSeries ℂ) (r : ℕ) :
    f ∈ jetIdeal r ↔
      ∀ n : ℕ, n < r → (PowerSeries.coeff n) f = 0 := by
  rw [jetIdeal, Ideal.mem_span_singleton, PowerSeries.X_pow_dvd_iff]

/-- Jet ideal membership is equivalent to a lower bound on series order. -/
theorem mem_jetIdeal_iff_order
    (f : PowerSeries ℂ) (r : ℕ) :
    f ∈ jetIdeal r ↔ (r : ℕ∞) ≤ f.order := by
  rw [mem_jetIdeal_iff]
  constructor
  · intro h
    exact PowerSeries.nat_le_order f r h
  · intro h n hn
    have hnr : (n : ℕ∞) < (r : ℕ∞) := by exact_mod_cast hn
    exact PowerSeries.coeff_of_lt_order n (lt_of_lt_of_le hnr h)

/-- Exact doubling gives a sharp order bound, hence membership in I_(2r). -/
theorem jetSelfFlow_mem_doubled_ideal
    (f : PowerSeries ℂ) (r : ℕ)
    (hf : f.order = (r : ℕ∞)) :
    f * jetConjugate f ∈ jetIdeal (2 * r) := by
  rw [mem_jetIdeal_iff_order, jetSelfFlow_order_double f r hf]

/-- The self-flow does not lie in the next jet ideal (sharpness). -/
theorem jetSelfFlow_not_mem_next_ideal
    (f : PowerSeries ℂ) (r : ℕ)
    (hf : f.order = (r : ℕ∞)) :
    f * jetConjugate f ∉ jetIdeal (2 * r + 1) := by
  intro hm
  have hzero := (mem_jetIdeal_iff _ _).mp hm
    (2 * r) (Nat.lt_succ_self _)
  exact (jetSelfFlow_leading_ne_zero f r hf) hzero

end JetPowerSeries

end P3
