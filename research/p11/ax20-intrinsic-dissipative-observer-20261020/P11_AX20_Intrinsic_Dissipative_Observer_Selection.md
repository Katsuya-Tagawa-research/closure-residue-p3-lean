# P11-AX20 — Intrinsic Dissipative Observer Selection and Symmetry Obstruction

**Draft finite mathematical audit. The original P3, P6 and frozen P1-P8 are not edited.** Human peer review and physical provenance absent.

## Conditional theorem

Let A=M_d(C) carry the Hilbert-Schmidt inner product. Assume the **complete independently calibrated** GKSL generator belongs to the restricted class

L(X) = -i[H,X] + gamma(E(X)-X),

where H is Hermitian, gamma>0, and E is a trace-preserving Hilbert-Schmidt orthogonal conditional expectation onto a unital abelian C*-subalgebra D (in H37, the diagonal MASA). The HS-selfadjoint part

S_L = (L + L^{dagger_HS})/2 = gamma(E-I).

Since E is an orthogonal idempotent, **ker S_L = im E = D**. Therefore, in this restricted class a fully marked generator L mathematically selects its pointer algebra without an additional pointer label. The result is covariant under simultaneous unitary conjugation of L and D; no preferred Hilbert-space coordinate basis is claimed.

For H37, the exact 5-site H has diagonal energies (0,1/7,-1/9,2/11,-3/13), nearest-neighbor hopping 1/2, gamma=2/3. The HS symmetric 25x25 superoperator has eigenvalues **0 (5-fold) and -2/3 (20-fold)**, extracting exactly D5. This can be combined with prior AX16's **genuine** P3 R2 saturation only after preserving the identical marked generator and extracting this same D5. It does NOT establish P6 hardware realization or generative F-origin.

## Perturbation caution

In the exact restricted class with gamma>0, the algebra is recovered exactly. Under arbitrary small selfadjoint superoperator perturbations of norm delta<gamma/2, Weyl's inequality preserves an isolated five-dimensional **near-zero spectral cluster**, but the cluster need not form an algebra or lie in the exact kernel.

For example, adding depolarization eta(Tr(X)I/5-X), eta=1/17, leaves a GKSL generator but gives eigenvalues 0 (1), -eta (4), -(gamma+eta) (20). **The exact kernel then shrinks from 5D to the scalars**, although an approximate five-dimensional slow sector remains.

## Universal observer-selection no-go

There cannot be an assignment of a **MASA** to **every** finite GKSL generator (d>=2) that is equivariant under all unitary conjugations: the depolarizing generator L_dep(X)=kappa(Tr(X)I/d-X) is invariant under the whole U(d). An assigned MASA would have to be invariant under the whole U(d), thus contain the unitary orbit of each rank-one projector; such projectors need not commute. Contradiction. The no-go does not forbid observer selection for restricted classes with additional intrinsic structure, or selection of more general non-MASA observational objects.

## Physical and foundational gates

- **G1 / mathematical observer reconstruction:** PASS conditional on having the complete marked H37-like GKSL generator and pure dephasing class.
- **G2 physical native provenance and complete calibration of L:** OPEN. Full process tomography or calibrated trace/spectral data may themselves presume observer controls and should not be used circularly.
- **G3 generative selection of L and E from F:** OPEN. No independent F selection axiom was derived.
- General symmetry theorem is mathematical; new Lean proof of it and human peer review remain OPEN.

## Reproducibility

The repository compact standalone SymPy exact CI checks **81 equations/ranks**, with code in P11_AX20_ci_compact.py. The separately shared research ZIP contains a broader 81-check audit and expanded note. Neither CI nor SymPy certifies the physical G2/G3 gates.

Next proof obligation: propose a non-circular native-generator / source-selection principle with its own empirical tests; exclude isotropic symmetry by an independently grounded mechanism rather than naming the intended observer in the premise.
