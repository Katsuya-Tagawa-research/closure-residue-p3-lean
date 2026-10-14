# P9.11 → P3–P11: B14/B17 finite K4 bridge audit

Date: 2026-10-14. Independent exact rational finite computations; **not** a new Lean theorem, not an external expert review, not a derivation of Einstein dynamics.

## Conventions and reconciliation with P9.11

Let `S=1^perp⊂R^4`, edges ordered
`(01),(02),(03),(12),(13),(23)`, and `r_ab=e_a-e_b`.
Define

```math
A_w = Σ_{a<b} w_ab r_ab r_ab^T,\quad
Q_w=-γ A_w,\quad
g_w=16(A_w|_S)^{-1}.
```

When all conductances equal one, `A_w|_S=4 I_S`, so `g_w=4 I_S`.
With the nonorthonormal basis `b_i=e_i-e_3` for i=0,1,2, the
*quadratic-form coordinate matrix* of `A_w` at uniformity is
`B^T A_w B=[[8,4,4],[4,8,4],[4,4,8]]`, not `4 I_3`.
This is only a coordinate distinction; the operator on `S` is `4I_S`.

The P9.11 stationary Markov two-time correlation and Green–Kubo
formulas are accepted as communicated analytical input. They are not
claimed to have been re-proven in Lean here.

## B14. The finite conductance-to-symmetric-tensor isomorphism

Let `G_ij(w)=b_i^T A_w b_j`, and list symmetric components in order
`(G_00,G_11,G_22,G_01,G_02,G_12)`.
Then `G_flat=M w` with

```text
M = [[ 1, 1, 4, 0, 1, 1],
     [ 1, 0, 1, 1, 4, 1],
     [ 0, 1, 1, 1, 1, 4],
     [-1, 0, 2, 0, 2, 1],
     [ 0,-1, 2, 0, 1, 2],
     [ 0, 0, 1,-1, 2, 2]]
det(M) = -256.
```

This independently certifies rank six for the **edge-to-tensor**
linear map, not for any CR-to-edge map.

### A conditional CR-to-conductance candidate

Assume that a gauge-reduced K4 CR control sector `Z_CR` has six
independently accessible real edge-amplitude functionals

```math
ℓ=(ℓ_e) : Z_CR -> R^6,
```

such that the infinitesimal coherent controls
`K_e=E_ab-E_ba` are genuinely present in its first-residue
derivation image. Define on the positive-amplitude patch

```math
x_e=ℓ_e(z)>0, \quad w_e(z)=x_e^2.
```

Then

```math
Dw_z = diag(2x_e) Dℓ_z.
```

Thus if `Dℓ_z` has rank six, `Dw_z` has rank six. At `x=(1,...,1)`,
`det Dw=64` in edge coordinates, and
`det D(G_flat∘w)=(-256)(64)=-16384`.
Also `D g_w[δw]=-16 A_w^{-1}(D A_w[δw]) A_w^{-1}`
(on `S`); since inversion is a local diffeomorphism on positive
definite matrices, rank-six tensor access survives in `g_w`.

**Critical outstanding assumption:** Neither the P3 two-state
unitary Krylov witness, the P6 calibrated finite-range exchange
example, nor P7 structural symmetry completion has supplied such a
six-dimensional **physical K4** edge-amplitude chart. If the available
quotient tangent dimension is `m<6`, then necessarily
`rank Dw ≤ m<6`; this is a dimension/rank NO-GO for full six-weight
local controllability in that sector. Restricted P9 conditional
sectors need not have full six-weight access.

### Generic GKSL comparator: B15 caution

Without assuming CR provenance, independently choose Lindblad
jump operators `L_{a←b}=sqrt(γ) x_ab |a><b|` and
`L_{b←a}=sqrt(γ) x_ab |b><a|` for each undirected edge.
The induced population Markov generator is exactly
`Q=-γ A_{x²}`. For positive x the process is irreducible.
Consequently both P9.11 two-time short-time reconstruction and the
Green–Kubo metric candidate follow **within standard GKSL/Markov
dynamics**. Thus these observables and a full-rank chart by
themselves do not prove residue necessity or any new
CR-specific physical prediction. The chosen mapping from coherent
CR amplitudes to these jump rates is an **additional constitutive
assumption**, not implied by P6 first-residue accessibility.

## B17. Two incompatible constitutive force laws on the same finite sector

The conductance family `w`, and the metric `g_w`, **do not specify a
unique response-conjugate force 1-form**. Any force model must first
be independently defined and calibrated; integrability must then
be tested.

### (a) Integrable standard equilibrium benchmark

On the positive orthant let

```math
U_{eq}(w)=log det(A_w|_S),\quad
F_e^{eq}(w)=∂_e U_{eq}
=r_e^T (A_w|_S)^{-1} r_e
=\tfrac1{16} r_e^T g_w r_e.
```

For all edges e,f,

```math
∂_f F_e^{eq} =
-(r_e^T (A_w|_S)^{-1}r_f)^2
=∂_e F_f^{eq}.
```

Therefore `V_ef=∂_e F_f-∂_f F_e=0`. This
potential is standard finite Markov/spectral mathematics, not proof
of CR-specific variational forces, a local spacetime action, or
Einstein–Hilbert dynamics.

### (b) A nonintegrable commutator-defined coherent response force

Assume the six `K_e` lie in a physically permitted K4 first-residue
coherent-control sector. Fix `J=K_02` and the positive
inner product `<X,Y>=-(1/2)Tr(XY)` on real antisymmetric matrices.
For an independently specified affine control section
`κ(w)=Σ_e(w_e-1)K_e` define the response-force candidate

```math
F_e(w) = <J,[K_e,κ(w)]>
       = Σ_f c_ef(w_f-1),
c_ef = <J,[K_e,K_f]> = -c_fe.
```

A concrete noncommutativity witness is

```math
[K_01,K_12]=K_02=J,\quad
c_{01,12}=1,\quad c_{12,01}=-1,
F_{01}=w_{12}-1,\quad F_{12}=-(w_{01}-1),\quad
V_{01,12}=∂_{01}F_{12}-∂_{12}F_{01}=-2.
```

Therefore this **chosen** force 1-form has no local scalar
potential anywhere on the positive orthant. The nonzero curvature
is a mathematically explicit algebraic obstruction, not a
demonstration that the P6/P9 physical force must have this form.

The affine `κ(w)` section above is distinct from the B14
`w=x²` chart. One can match the charts consistently by setting
`κ(x)=Σ_e x_e K_e` and treating
`α_x=Σ_e <J,[K_e,κ(x)]> dx_e` as the physical covector.
On `x_e=sqrt(w_e)>0`, the correctly pulled-back 1-form is

```math
F^w_e(w)=\frac{1}{2\sqrt{w_e}}\sum_f c_{ef}\sqrt{w_f},
\quad
V^w_{01,12}(w)=-\frac{1}{2\sqrt{w_{01}w_{12}}}.
```

In particular the curl at the uniform point is `-1/2` rather
than `-2`; nonintegrability survives the coordinate change.
This last formula follows by the ordinary transformation law for
differential 1-forms; the rational checker independently tests the
uniform-point coefficient.

**Important:** `J=K_02`, the pairing, and the force law are
specific **modeling choices**. It remains open whether the actual
CR-generated K4 response fingerprint independently specifies these
choices, gauge covariance, readout meaning, and physical control
accessibility. The commutator alone is not a variational-force
uniqueness theorem.

## Required progress gates

**B14:** (i) Define an actual K4 CR `Z_CR` from P3/P6, including the
K4 residue/edge map, its gauge quotient and six genuine physical
directions; (ii) prove or refute rank six on a positive chart;
(iii) compute the observable map from calibrated short-time
correlations and check that it does not reuse the target Hessian.

**B15:** Compare P9.11 observables against the standard GKSL model
above. Unless additional independently calibrated CR constraints
distinguish prediction sets, residue necessity is unsupported.

**B17:** Derive a physically meaningful `F_e(w)` independently
from the CR dynamics; check its mixed derivatives. The two
counterposed choices above prove that the K4 conductance/metric
data alone neither imply integrability nor force
nonintegrability. For continuum local actions one must also
establish Helmholtz conditions, locality, covariance, and
appropriate gluing.

**B16:** Separately build a near-identity CPTP family and
control uniformity under growing cell size. No uniform gap,
continuum gluing or Einstein dynamics is asserted here.

## Verification

`P3/K4B14B17ExactCheck.py` uses only Python's `fractions.Fraction`
and checks the finite determinant, full-rank control chart,
noncommutative bracket, antisymmetry and both curl witnesses.
This constitutes an **independent executable rational audit**,
not a Lean kernel proof. All existing frozen P3 modules are
untouched. The pull request remains Draft pending review.
