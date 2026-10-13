import P3.TwoVertexFirstResidue

/-!
# Exact rational Krylov orbit for a nontrivial two-vertex P3 dynamics

This file strengthens the two-vertex first-residue model from
"P3.TwoVertexFirstResidue" with a rational coordinate formula for its
entire diagonal-seed orbit. It proves exact equality, after a finite
reindexing and coefficient inclusion ℚ → ℂ, with the original P3
canonical observable Krylov matrix.

A separate explicit lexicographically indexed rational matrix provides
fast, executable, independently sound pivot-certificate checks of its
rank sequence, without the overhead of exhaustive automatic pivot search. The finite index
reindexing in the main algebraic theorem uses Fintype.equivFin, so that
general representation is noncomputable. The raw smoke-test matrix is
fully computable, and its coordinate convention is stated separately.

No completely positive or trace-preserving property is claimed for
the underlying nilpotent algebraic dynamics.
-/

noncomputable section

namespace P3

/-- Every iterate of the two-vertex nilpotent model beyond first order
vanishes on the full matrix algebra. -/
theorem p3TwoVertexFirstResidue_pow_ge_two
    (M : A (Fin 2)) (n : ℕ) (hn : 2 ≤ n) :
    (p3TwoVertexFirstResidue ^ n) M = 0 := by
  have hsq : p3TwoVertexFirstResidue ^ 2 = 0 := by
    apply LinearMap.ext
    intro X
    exact p3TwoVertexFirstResidue_square_zero X
  obtain ⟨t, rfl⟩ : ∃ t : ℕ, n = 2 + t :=
    ⟨n - 2, by omega⟩
  simp [pow_add, hsq]

/-- The rational coefficient of the j-th diagonal-seed orbit:
at j=0, E_aa; at j=1, E_01 only for a=0; and zero for j≥2. -/
def p3TwoVertexRationalOrbitEntry
    (j : ℕ) (a x y : Fin 2) : ℚ :=
  if j = 0 then
    if x = a ∧ y = a then 1 else 0
  else if j = 1 then
    if a = 0 ∧ x = 0 ∧ y = 1 then 1 else 0
  else 0

/-- At every power, each entry of the complex P3 orbit equals the
coefficient inclusion of the explicit rational orbit formula. -/
theorem p3TwoVertexRationalOrbitEntry_exact
    (j : ℕ) (a x y : Fin 2) :
    ((p3TwoVertexFirstResidue ^ j)
      (Matrix.single a a (1 : ℂ))) x y =
      (p3TwoVertexRationalOrbitEntry j a x y : ℂ) := by
  by_cases hzero : j = 0
  · subst j
    simp [p3TwoVertexRationalOrbitEntry, Matrix.single_apply]
  by_cases hone : j = 1
  · subst j
    simp only [pow_one]
    change
      (if x = (0 : Fin 2) ∧ y = (1 : Fin 2)
        then (Matrix.single a a (1 : ℂ)) 0 0 else 0) =
        (p3TwoVertexRationalOrbitEntry 1 a x y : ℂ)
    fin_cases a <;>
      simp [p3TwoVertexRationalOrbitEntry, Matrix.single_apply]
  · have hge : 2 ≤ j := by omega
    rw [p3TwoVertexFirstResidue_pow_ge_two
      (Matrix.single a a (1 : ℂ)) j hge]
    simp [p3TwoVertexRationalOrbitEntry, hzero, hone]

/-- The original physical axis labels are replaced with numbered
indices exactly as in P3.RationalKrylovBridge. -/
noncomputable def p3TwoVertexRationalKrylov (k : ℕ) :
    Matrix (Fin (Fintype.card (Fin 2 × Fin 2)))
      (Fin (Fintype.card (Fin (k + 1) × Fin 2))) ℚ :=
  fun row col =>
    let xy := (Fintype.equivFin (Fin 2 × Fin 2)).symm row
    let ja := (Fintype.equivFin (Fin (k + 1) × Fin 2)).symm col
    p3TwoVertexRationalOrbitEntry ja.1.val ja.2 xy.1 xy.2

/-- The explicitly rational orbit is an EXACT presentation of the
original P3 Krylov matrix at every depth (not just a rank match).
The enumeration equivalence is fixed by the existing P3 convention. -/
theorem p3TwoVertexRationalKrylov_exact (k : ℕ) :
    p3FinIndexedKrylovMatrix p3TwoVertexFirstResidue k =
      (p3TwoVertexRationalKrylov k).map (Rat.castHom ℂ) := by
  classical
  ext row col
  change
    p3CanonicalKrylovMatrix p3TwoVertexFirstResidue k
      ((Fintype.equivFin (Fin 2 × Fin 2)).symm row)
      ((Fintype.equivFin (Fin (k + 1) × Fin 2)).symm col) =
    (Rat.castHom ℂ) (p3TwoVertexRationalKrylov k row col)
  rw [p3CanonicalKrylovMatrix_entry]
  exact p3TwoVertexRationalOrbitEntry_exact
    ((Fintype.equivFin (Fin (k + 1) × Fin 2)).symm col).1.val
    ((Fintype.equivFin (Fin (k + 1) × Fin 2)).symm col).2
    ((Fintype.equivFin (Fin 2 × Fin 2)).symm row).1
    ((Fintype.equivFin (Fin 2 × Fin 2)).symm row).2

/-- The rational first-equal-rank depth of the constructed, exact
P3 Krylov input is 1, eliminating the assumed rational presentation
from the Phase-5 conditional algorithm in this nontrivial model. -/
theorem p3TwoVertexRationalKrylov_stopping_depth :
    p3RatFirstStoppingDepth
      (p3AlgebraDimension (V := Fin 2) - Fintype.card (Fin 2))
      p3TwoVertexRationalKrylov = some 1 := by
  have h :=
    p3RatFirstStoppingDepth_complete
      p3TwoVertexFirstResidue
      p3TwoVertexRationalKrylov
      (by
        intro k hk
        exact p3TwoVertexRationalKrylov_exact k)
  rw [p3TwoVertexFirstResidue_depth_one] at h
  exact h

/-- A separate directly computable lexicographic rational representation.
Row index r=2*x+y, column index c=2*j+a. The first two columns
represent E00, E11; at the next iterate only E01 survives.
This avoids the noncomputable Fintype.equivFin enumeration. -/
def p3TwoVertexExecutableRationalKrylov (k : ℕ) :
    Matrix (Fin (Fintype.card (Fin 2 × Fin 2)))
      (Fin (Fintype.card (Fin (k + 1) × Fin 2))) ℚ :=
  fun row col =>
    if col.val = 0 ∧ row.val = 0 then 1
    else if col.val = 1 ∧ row.val = 3 then 1
    else if col.val = 2 ∧ row.val = 1 then 1
    else 0

/-!
For this small sparse matrix, the general automatic pivot enumerator
needlessly checks many singular 4×4 minors. The explicit pivot-certificate
checker is already verified sound and is substantially faster. Each guard
below checks an invertible minor AND an exact reconstruction factorization,
so it certifies the three rational matrix ranks 2,3,3. Together with the
kernel-checked stopping-depth theorem above, this tests the same first
plateau without exhaustively enumerating large numbers of bad pivot maps.
These runtime guards are not smuggled into a kernel theorem.
-/

#guard p3RatPivotAccepted
  (p3TwoVertexExecutableRationalKrylov 0) 2
  (fun i : Fin 2 => if i = 0 then 0 else 3)
  (fun i : Fin 2 => if i = 0 then 0 else 1) == true

#guard p3RatPivotAccepted
  (p3TwoVertexExecutableRationalKrylov 1) 3
  (fun i : Fin 3 => if i = 0 then 0 else if i = 1 then 1 else 3)
  (fun i : Fin 3 => if i = 0 then 0 else if i = 1 then 2 else 1) == true

#guard p3RatPivotAccepted
  (p3TwoVertexExecutableRationalKrylov 2) 3
  (fun i : Fin 3 => if i = 0 then 0 else if i = 1 then 1 else 3)
  (fun i : Fin 3 => if i = 0 then 0 else if i = 1 then 2 else 1) == true

end P3
