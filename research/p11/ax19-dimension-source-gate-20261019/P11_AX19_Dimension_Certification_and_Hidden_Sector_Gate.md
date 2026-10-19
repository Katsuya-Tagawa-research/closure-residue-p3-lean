# P11–AX19 — Dimension Certification and the Hidden-Sector Independence Gate

**2026-10-19 | P11 AX-series**. Extends AX18 Draft PR #156; first-principles source/origin still OPEN. This is a finite exact mathematical audit, not an apparatus claim. No changes to main or frozen P1–P8.

## 1. What an operational dimension witness can and cannot prove

Let H be a complex Hilbert space of dimension d. Suppose an operational experiment supplies *independently marked* input density operators rho_j and output linear functionals represented by Hermitian operators A_i, producing D_ij=Tr(A_i rho_j).

Then **rank D <= d²**, since D factors through the real vector space Herm(H) of dimension d². Thus a rank r witness implies d >= ceil(sqrt(r)). This is a **lower** bound, not an upper bound. It does not certify the absence of unused Hilbert-space sectors, native controls or unmarked operations.

For time-resolved experiments A_i may be *time derivatives* (L†)^k(M_a), which are Hermitian linear probes rather than individually positive effects. They represent derivatives of physical measurement probabilities when the measurement and its time controls are independently available. Symbolic linear independence does **not** certify that such time derivatives can be robustly estimated or that the apparatus exists.

## 2. Exact H37 saturated lower-bound witness

Use the **fixed** five-level H37 GKSL generator from AX05–AX18:

H = 1/2 sum_{i=0}^3(E_{i,i+1}+E_{i+1,i}) + diag(0,1/7,-1/9,2/11,-3/13),
L(rho) = -i[H,rho] + (2/3)(Delta_D(rho)-rho).

With independently declared population effects p_i=E_ii, the Heisenberg generator Krylov tower has exact complex dimensions

5, 9, 13, 17, 21, 23, 25, 25.

Take the 25 legitimate pure preparations consisting of: (i) the five p_i; (ii) (p_i+p_j+X_ij)/2 for ten pairs; and (iii) (p_i+p_j+Y_ij)/2 for ten pairs, with X_ij=E_ij+E_ji and Y_ij=-iE_ij+iE_ji. They span Herm_5 over the reals. Select 25 independent functionals from the population/derivative Krylov family through derivative grade six. The resulting 25x25 matrix of exact pairings has **rank 25**.

Therefore any finite quantum realization of these *calibrated* bilinear response data has d>=5. H37 supplies a 5D realization, hence the **minimum compatible model dimension is exactly five**. This is a precise operational-minimality result, *not* actual device upper-bound certification. All linear algebra is exact rational computation, including a 25x25 nonsingular response submatrix.

## 3. The universal spectator-extension independence theorem

For any finite instrument {I_a} on a system A and arbitrary auxiliary B, let T_B be **any** CPTP channel and declare

tilde(I)_a = I_a ⊗ T_B,  tilde(rho)=rho_A ⊗ tau_B.

All finite outcome-word probabilities agree with the original system, because the partial trace satisfies

Tr_B[(I_a ⊗ T_B)(R_AB)] = I_a(Tr_B R_AB)

for **every** joint input R_AB, even entangled inputs. Iteration proves every finite word. The result also holds for all A-only time-resolved observables from the given semigroup. Nevertheless the physical Hilbert dimension multiplies by dim B, invisible to the marked interface.

Concrete 5-to-10D example: p_i vs p_i⊗I_2. The five prepared states p_j⊗|+><+| yield the same perfect-identification table delta_ij as in 5D. In 10D, the pointer effects have **rank 2, not rank 1**; all 25x25 H37 A-response pairings remain identical. Spectator channels id and Ad_Z give different B-side X expectations +1 and -1, but no A-only response distinguishes them.

**Consequence:** even informationally complete data on the **declared** 5D factor, saturated rank25, and a perfect 5-outcome pointer table do **not** certify that the true Hilbert space has dimension at most five. Choosing the smallest realization is a valid *operational convention*, but it does not identify actual physical hidden source completeness.

## 4. Noncircular G2 / G3 decision

There is a **conditional** theorem: if independent, externally certified evidence gives d<=5, and the calibrated response has rank25, then d=5 and AX18's perfect pointer table selects its rank-one pointer algebra up to a global unitary. This does not derive d<=5 from the trace table, the P3 residue or F. Using “choose the minimum dimension compatible with the observations” as **the physical truth** simply builds G2 into the selection axiom; it is not independent derivation.

| Obligation | Status |
|---|---|
| H37 response rank25 and minimum compatible dimension five | EXACT, conditional marked experiment |
| Perfect five-output table forces physical d=5 | NO: 10D spectator witness |
| All A records rule out hidden spectator sectors | NO: exact all-word theorem |
| Independent physical upper dimension bound and exhaustive port list | OPEN |
| Original P3 residue preserved as a **full 10D MASA residue** | NOT CLAIMED |
| F intrinsically supplies a 5D bound and pointer source | OPEN |
| P6 hardware certification, P9 Einstein, P11 G3 completeness | OPEN |

**STOP:** Do not proliferate more indistinguishable spectator examples under the same protocol class; the all-ancilla CPTP theorem already covers them. Next progress requires genuinely independent dimension/source evidence or a separately derived **F-origin axiom with provenance**, not an inference from observational rank and not physical self-testing by assumption. CI checks finite algebra only, not hardware calibration, independent review or global F completeness.

## Reproduction

Python >=3.11, SymPy 1.14: run P11_AX19_dimension_independence_audit.py. Expected **1433/1433 exact assertions**; H37 tower, saturated 25-rank response, 5D/10D pointer tables, and 625 response entries for two spectator dynamics. The **all-length** theorem is analytical and does not follow from the finite number of assertions. No result concerning F's cosmological universe, GR dynamics or the P3 residue for a full ten-dimensional *maximal* diagonal algebra is asserted.
