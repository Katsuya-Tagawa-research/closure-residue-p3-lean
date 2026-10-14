# B14: A finite K4 coherent-CR candidate and observable Hessian chart

**Date:** 2026-10-14.
**Status:** exact finite matrix identity, polynomially audited by
`P3/K4CoherentHessianExactCheck.py`; not a Lean proof or a proof
that P3's microscopic inherited sector supplies the required six
physically admissible control directions.

## Setup

Take `D_4`, the diagonal subalgebra in `M_4(C)`.
For the six undirected K4 edges `e=(a,b)`, a<b, set

```math
K_{ab}=E_{ab}-E_{ba}\in\mathfrak{u}(4),\quad
K(x)=\sum_{a<b}x_{ab}K_{ab},\quad
U_t(x)=e^{tK(x)},\quad
\Phi_{t,x}(\rho)=U_t(x)\rho U_t(x)^\dagger.
```

For every x,t, `Phi_{t,x}` is a unitary CPTP
channel; for fixed x it obeys the near-identity expansion
`Phi_{t,x}=id+t\,ad_{K(x)}+O(t²)`.
This is a **finite coherent physical model**. It has not been
identified as the specific inherited P3–P6 CR sector: that would
require establishing microscopic provenance and physical
controllability of all six generators from the CR filtration.

## First-residue observation tangent

With diagonal matrix unit `p_b=E_{bb}`,
for each edge a<b,

```math
[K(x),p_b]_{ab}=x_{ab}.
```

Thus the linear map
`x\mapsto (\mathrm{ad}_{K(x)}|_{D_4})` is injective
and admits an explicit six-coordinate left inverse.
This is exactly the **full matrix-algebra-action level** of
the P6 first-residue derivation `R^{(1)}` if the microscopic
CR sector is *assumed* to contain the six `K_{ab}`.

In contrast, diagonal observation kills every such first variation:

```math
\operatorname{diag}[K(x),\rho]=0
\quad (\rho\in D_4).
```

Therefore the **first-order population fingerprint is completely
silent** for these six controls. The full algebra action and the
actual population readout are different observer specifications;
the first cannot be claimed operationally measured by the
second without extra coherent measurement resources.

## Quadratic return and conductance readout

For diagonal `\rho=\operatorname{diag}(p_0,p_1,p_2,p_3)`,

```math
\frac12\left.\frac{d^2}{dt^2}
\operatorname{diag}(\Phi_{t,x}(\rho))_a\right|_{t=0}
=\frac12[K(x),[K(x),\rho]]_{aa}
=\sum_{b\ne a}x_{ab}^2(p_b-p_a).
```

This is the graph divergence/Markov Laplacian form with
**concrete** rates `w_{ab}=x_{ab}²`:

```math
\frac12\frac{d^2}{dt^2}
\operatorname{diag}(\Phi_{t,x}(\rho))|_0
=-A_w p.
```

This **derives** rather than merely postulates the squared-edge
coefficient *inside the specified K4 coherent control model*.

For each a<b, choose the prepared diagonal basis state
`\rho=p_b=E_{bb}`; then read out the population at the
different vertex a:

```math
w_{ab}=\frac12\left.\frac{d^2}{dt^2}
(\Phi_{t,x}(p_b))_{aa}\right|_{t=0}.
```

Thus six independent preparations/readouts determine all six rates
even though *every first-order population response vanishes*.
A **single prepared population** has at most three independent
zero-sum Hessian outputs, so it cannot generally determine
all six rates. The uniform maximally mixed state has an identically
zero coherent response under all unitary controls, so a single
uniform preparation provides no edge information.

On the positive amplitude patch x>0 the derived rate chart has
`Dw=\operatorname{diag}(2x_e)`, with rank six.
At x=(1,...,1), `\det Dw=64`.
For the P9.10 K4 tensor chart, `\det D(G\circ w)=-16384`.

## Minimal prepared-state observability: a finite No-Go and sharp threshold

A single fixed diagonal preparation `p` supplies a zero-sum
population Hessian `q=-A_w p` with at most three independent outputs,
so a full-rank reconstruction of six weights is impossible.

More strongly, **any two fixed diagonal preparations are insufficient**
for local identification of all six independent conductances from
these second-order population Hessians alone. To see this, project the
two preparation vectors onto `S=1^perp`, and choose
`0 != z in S` orthogonal to both projections.
Then the symmetric nonzero perturbation `δA=z z^T` on S
annihilates both prepared vectors. The K4 edge-to-tensor isomorphism
makes `δA` equivalent to a nonzero perturbation `δw`;
for small ε and all-positive base weights, `w+εδw` is still positive
but produces the same two Hessian outputs.
This is a rigorous **two-probe non-identifiability** statement within
the unrestricted six-weight K4 sector.

For **three independent projections** spanning S, the action of
`A_w|_S` on a basis determines the entire operator and hence all
six edge weights. Three localized preparations `E_00,E_11,E_22`
suffice. Exact rational response-matrix ranks are

```math
\operatorname{rank} R_{E_{00}}=3,\quad
\operatorname{rank} R_{E_{00},E_{11}}=5,\quad
\operatorname{rank} R_{E_{00},E_{11},E_{22}}=6.
```

These exact ranks are checked by the standalone polynomial audit.
This lower bound applies to **fixed short-time second-order population
readouts**. It does not prohibit reconstruction from fewer
preparations using additional observables, higher derivatives,
multiple times, or calibrated structure restricting the possible w.

## Relation and non-equivalence to the P9.11 Markov model

The P9.11 **continuous-time Markov** generator
`Q_w=-\gamma A_w` has stationary two-time offdiagonal
correlation derivative
`\dot C_{ab}(0)=\gamma w_{ab}/4`
for uniform stationary \pi.
Therefore, for the matched numeric w,
the coherent quadratic readout and Markov linear-in-time
correlation obey

```math
\dot C_{ab}(0)
=\frac\gamma8\frac{d^2}{dt^2}
(\Phi_{t,x}(p_b))_{aa}\big|_{t=0}.
```

This is a **cross-model coefficient identity**, not equality of
the unitary population dynamics and a Markov semigroup.
The coherent population response begins at `t²` while
the Markov population drift starts at `t`.
Standard GKSL paired jumps also realize `Q_w` for any such w,
without the coherent control mechanism.

## B14/B15/B17 decision

- **Constructive B14 conditional success:** A declared six-edge coherent
  unitary control manifold admits the exact CR-like
  `D→[K,D]→diag[K,[K,D]]` cycle and six-weight population
  Hessian reconstruction with independently prepared basis states.
- **Provenance limitation:** Neither this example nor P9.11 proves
  that the K4 `K_{ab}` lie in the inherited microscopic CR sector
  and physically controllable P6 submanifold.
- **B15 nonuniqueness:** The same edge weights and P9.11
  conductance-based metric are obtained from ordinary Markov/GKSL
  dynamics, so the observed rates alone cannot witness CR necessity.
- **B17 unresolved:** The Hessian determines w but does not choose
  an independent conjugate force `F_e(w)` or a variational action.
  A physical work protocol/readout and mixed-derivative calibration
  remain necessary.

No Einstein equations, continuous spacetime action, or
unconditional spin-2 physical accessibility follow.
