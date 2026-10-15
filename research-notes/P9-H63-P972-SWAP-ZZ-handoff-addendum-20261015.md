# H63 addendum — P9.72 compatibility gate

P9.72 reports an enlarged SWAP+ZZ many-body control and X/Y coherence-readout model. These are not automatically authorized by the frozen P6 v9.1 real-exchange/dephasing/population benchmark. A calibrated complex phase or coherent X/Y measurement is additional physical instrumentation. A partial trace is CPTP but is not automatically the original P6 closure map.

H63's anti-symplectic transpose no-go remains valid for the restricted real-instrument category, not for the enlarged model. Recovering an angle modulo pi with calibrated axes is not a gauge-invariant intrinsic phase selector. Even perfect identification of a ZZ parameter does not prove a CR dynamical law selecting its value.

The P9.72 original Jacobian and finite-time error formula have not been supplied to this branch, so P9.72-specific independent numerical reproduction is OPEN. The standard perturbation inequality sigma_r(J+E)>=sigma_r(J)-||E|| only preserves the first r singular directions; equality of the exact rank also requires a rank cap or full-column-rank premise.

A separately computed two-qubit product-state SWAP+ZZ comparator, with Bloch vectors a=(1/2,1/3,1/4), b=(1/5,1/7,1/6), gives the first-control Jacobian for local X,Y,Z readouts:

J0 = [ [-5/252, -1/9], [1/30, 1/6], [-1/210, 0] ].

The top minor equals 1/2520, and the squared Frobenius norm is 2645/63504 (less than 1), giving the conservative lower bound sigma_min(J0)>1/2520. For couplings J=kappa=1/10, a general bounded-commutator argument yields ||J_t-J0||<12t/5 for the finite-difference temporal response Jacobian. Thus t=1/10000 satisfies a sufficient rank-retention condition in this TWO-qubit comparator. This is not a P9.72 large-M uniform estimate.

At time zero, a single-replica control applied to a mean local observable scales the first-control response as 1/M; identical collective controls on M replicas retain order-one initial response. Finite-time propagation and large-M uniformity require extra estimates.

**Status:** independent finite conditional comparator; no physical P6 permission, CR provenance, many-body mean-field theorem, spatial tensor/HDA or Einstein derivation.
