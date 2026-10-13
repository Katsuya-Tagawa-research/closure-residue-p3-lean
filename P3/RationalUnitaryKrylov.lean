import P3.RationalUnitaryFirstResidue

/-!
# Exact rational Krylov presentation of the two-vertex unitary channel

The rational reflection R = [[3/5,4/5],[4/5,-3/5]] has a
coefficientwise embedding into the previously verified complex unitary U.

Starting with the rational diagonal matrix units E_aa, recursively
conjugate by R. The resulting finite rational orbit is proved equal,
AFTER coefficient inclusion ℚ → ℂ, to every iterate of the actual
complex P3 quantum channel. Reindexing via the canonical P3
Fintype.equivFin gives an exact rational presentation of the original
observable Krylov matrices at all depths.

The generic index equivalences are noncomputable. Therefore this
module asserts exact rational *mathematical representability*, not a
fully executable arbitrary-enumeration implementation. An explicitly
indexed finite numerical reporter is an additional task.
-/

noncomputable section

namespace P3

/-- The physical two-vertex reflection written over the rational field. -/
def p3RationalReflectionMatrixQ : Matrix (Fin 2) (Fin 2) ℚ :=
  !![(3 : ℚ) / 5, (4 : ℚ) / 5;
     (4 : ℚ) / 5, -(3 : ℚ) / 5]

/-- Rational-to-complex coefficient extension is exactly the physical U. -/
theorem p3RationalReflectionMatrixQ_cast :
    p3RationalReflectionMatrixQ.map (Rat.castHom ℂ) =
      p3RationalReflectionU := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [p3RationalReflectionMatrixQ, p3RationalReflectionU]

/-- All rational diagonal-seed iterates, using only exact ℚ arithmetic. -/
def p3RationalReflectionOrbitQ (a : Fin 2) :
    ℕ → Matrix (Fin 2) (Fin 2) ℚ
  | 0 => Matrix.single a a 1
  | n + 1 =>
      p3RationalReflectionMatrixQ *
        p3RationalReflectionOrbitQ a n *
        p3RationalReflectionMatrixQ

/-- All rational orbit matrices are exactly the original complex
unitary quantum-channel orbit matrices after scalar extension. -/
theorem p3RationalReflectionOrbitQ_cast
    (j : ℕ) (a : Fin 2) :
    (p3RationalReflectionOrbitQ a j).map (Rat.castHom ℂ) =
      (p3RationalReflectionChannel ^ j)
        (Matrix.single a a (1 : ℂ)) := by
  induction j with
  | zero =>
      ext x y
      by_cases h : a = x ∧ a = y
      · simp [p3RationalReflectionOrbitQ, Matrix.single_apply, h]
      · simp [p3RationalReflectionOrbitQ, Matrix.single_apply, h]
  | succ n ih =>
      calc
        (p3RationalReflectionOrbitQ a (n + 1)).map (Rat.castHom ℂ) =
            p3RationalReflectionMatrixQ.map (Rat.castHom ℂ) *
              (p3RationalReflectionOrbitQ a n).map (Rat.castHom ℂ) *
              p3RationalReflectionMatrixQ.map (Rat.castHom ℂ) := by
                simp only [p3RationalReflectionOrbitQ, Matrix.map_mul]
        _ = p3RationalReflectionU *
              ((p3RationalReflectionChannel ^ n)
                (Matrix.single a a (1 : ℂ))) *
              p3RationalReflectionU := by
                rw [p3RationalReflectionMatrixQ_cast, ih]
        _ = (p3RationalReflectionChannel ^ (n + 1))
              (Matrix.single a a (1 : ℂ)) := by
                rw [pow_succ']
                change _ = p3RationalReflectionChannel
                  ((p3RationalReflectionChannel ^ n)
                    (Matrix.single a a (1 : ℂ)))
                exact (p3RationalReflectionChannel_apply _).symm

/-- Exact rational coefficient representation with precisely the same
finite row/column coordinate convention as the existing P3 bridge. -/
noncomputable def p3RationalReflectionKrylovQ (k : ℕ) :
    Matrix (Fin (Fintype.card (Fin 2 × Fin 2)))
      (Fin (Fintype.card (Fin (k + 1) × Fin 2))) ℚ :=
  fun row col =>
    let xy := (Fintype.equivFin (Fin 2 × Fin 2)).symm row
    let ja := (Fintype.equivFin (Fin (k + 1) × Fin 2)).symm col
    (p3RationalReflectionOrbitQ ja.2 ja.1.val) xy.1 xy.2

/-- Every canonical complex P3 Krylov entry of the physical unitary
channel has this exact rational representation at ALL finite depths. -/
theorem p3RationalReflectionKrylovQ_exact (k : ℕ) :
    p3FinIndexedKrylovMatrix p3RationalReflectionChannel k =
      (p3RationalReflectionKrylovQ k).map (Rat.castHom ℂ) := by
  classical
  ext row col
  change
    p3CanonicalKrylovMatrix p3RationalReflectionChannel k
      ((Fintype.equivFin (Fin 2 × Fin 2)).symm row)
      ((Fintype.equivFin (Fin (k + 1) × Fin 2)).symm col) =
    (Rat.castHom ℂ) (p3RationalReflectionKrylovQ k row col)
  rw [p3CanonicalKrylovMatrix_entry]
  let xy := (Fintype.equivFin (Fin 2 × Fin 2)).symm row
  let ja := (Fintype.equivFin (Fin (k + 1) × Fin 2)).symm col
  have h := congrArg
    (fun M : Matrix (Fin 2) (Fin 2) ℂ => M xy.1 xy.2)
    (p3RationalReflectionOrbitQ_cast ja.1.val ja.2)
  simpa [p3RationalReflectionKrylovQ, xy, ja] using h.symm

/-- The original first observable stopping depth in a genuine
single-Kraus quantum channel is recovered by the exact rational
rank-search bridge. This avoids any externally assumed rational Q. -/
theorem p3RationalReflectionKrylovQ_stopping_depth :
    p3RatFirstStoppingDepth
      (p3AlgebraDimension (V := Fin 2) - Fintype.card (Fin 2))
      p3RationalReflectionKrylovQ = some 1 := by
  have h := p3RatFirstStoppingDepth_complete
    p3RationalReflectionChannel p3RationalReflectionKrylovQ
    (by
      intro k hk
      exact p3RationalReflectionKrylovQ_exact k)
  rw [p3RationalReflectionChannel_depth_one] at h
  exact h

end P3
