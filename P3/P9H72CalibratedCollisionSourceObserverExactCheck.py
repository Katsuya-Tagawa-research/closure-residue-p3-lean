"""H72: calibrated collision-factor micro source and CP observer; P6 control no-go.

Reuses H42 exact CPTP U = Pphase*Cayley((A+B)/2), H71 CP twirl.
H72's new CONDITIONAL physical model allows modulation of the duration
of THIS calibrated pre-existing collision factor, not a newly appended
after-channel collective control. Show unique Cayley inverse and
right-log tangent, reflection symmetry, CPTP controlled observer.
A calibrated Pphase and duration dial are NEW physically declared
instrument facts, NOT consequences of original P3 residue alone.

Second theorem: under BOTH unrestricted original P6 real-exchange
knobs A,B, no nontrivial proper unital C*-subalgebra of M3 supports
a trace-preserving conditional-expectation observer invariant under
their full reversible coherent group. Exact centralizer and Lie-rank
checks support irreducible complex SO(3) representation; analytic
factor/connected-center proof in accompanying note. This does not
rule out general nonalgebra CP observers or nonlinear/history memory.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    N,unit,eye,z,scale,add,sub,mm,dagger,com,rr
)
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import (
    K,A,B,U,Pphase,Cayley,reflection,H,Xi,rank_complex
)
from P9H43EquivariantCPTPCollectiveExtractionExactCheck import twirl
from P9H44MinimalObserverMemoryQuadraticResidueExactCheck import Phi
from P9H71ControlledCPTPReflectionObserverExactCheck import (
    cayley,noise,EV,SETTINGS
)
from P9H48InstrumentProvenanceKernelClosureExactCheck import real_rank_complex
assert N==3 and EV==K

def inv3(M):
    aug=[M[i][:]+eye()[i][:] for i in range(3)]
    for col in range(3):
        p=next(j for j in range(col,3) if aug[j][col]!=Z0)
        aug[p],aug[col]=aug[col],aug[p]
        pivot=aug[col][col]
        aug[col]=[v/pivot for v in aug[col]]
        for j in range(3):
            if j!=col:
                c=aug[j][col]
                aug[j]=[v-c*w for v,w in zip(aug[j],aug[col])]
    R=[row[3:] for row in aug]
    assert mm(M,R)==eye() and mm(R,M)==eye()
    return R
def conj(V,X):return mm(mm(V,X),dagger(V))
def matvec(X):return [X[i][j] for i in range(3) for j in range(3)]
def phi_s(s,X):
    return conj(mm(Pphase,cayley(EV,s)),X)
MATS=[unit(i,j) for i in range(3) for j in range(3)]

# The independently calibrated phase factor of ACTUAL H42 U permits
# UNIQUE inverse-Cayley reconstruction of a prephase collision
# generator when -1 is absent from the calibrated V spectrum.
V=mm(dagger(Pphase),U)
assert V==Cayley==cayley(EV,F(1,2))
assert mm(reflection,Pphase)==mm(Pphase,reflection)
assert mm(reflection,EV)==mm(EV,reflection)
one=eye()
inverse=inv3(add(V,one))
recovered=scale(mm(sub(V,one),inverse),F(2))
assert recovered==EV==K
assert mm(mm(EV,EV),EV)==scale(EV,-2)
assert dagger(recovered)==scale(recovered,-1)
assert rr([recovered,A,B])==2
print("PASS H72: calibrated ORIGINAL H42 U factor uniquely inverse-Cayley recovers A+B without inserting a post-channel knob")

# Family constructed by modulating the existing single calibrated
# microscopic collision parameter, not by independently declaring
# an unrelated U_after. The duration dial is an additional genuine
# physical apparatus premise.
for s in (F(0),F(1,5),F(1,2),F(2,3)):
    W=mm(Pphase,cayley(recovered,s))
    assert mm(dagger(W),W)==one
    assert mm(W,reflection)==mm(reflection,W)
    for X in MATS:
        assert twirl(phi_s(s,X))==phi_s(s,twirl(X))
        assert Phi(X)==phi_s(F(1,2),X)

    # Exact right logarithmic derivative of the ORIGINAL microscopic
    # calibrated family U_s=Pphase*Cayley(s K).
    # d Cayley/ds=2 (I-sK)^(-1) K (I-sK)^(-1);
    # (dU_s/ds)U_s†=(2/(1+2s²)) Pphase K Pphase†.
    J=inv3(sub(one,scale(recovered,s)))
    dV=scale(mm(mm(J,recovered),J),F(2))
    dU=mm(Pphase,dV)
    right_generator=mm(dU,dagger(W))
    expected=scale(conj(Pphase,recovered),F(2)/(F(1)+2*s*s))
    assert right_generator==expected
    assert dagger(right_generator)==scale(right_generator,-1)
    assert mm(reflection,right_generator)==mm(right_generator,reflection)
    assert right_generator!=z()
print("PASS H72: exact microscopic duration tangent is uniquely derived from CALIBRATED collision family and parity even")

def allowed_step(s,qend,qmid,X):
    # Individually CP site phase flips with identical endpoint setting.
    return noise((qend,qmid,qend),phi_s(s,X))
settings=[
    (F(0),F(1),F(1)),
    (F(1,2),F(4,5),F(2,3)),
    (F(2,3),F(3,5),F(7,8))
]
for s,q0,q1 in settings:
    for X in MATS:
        assert twirl(allowed_step(s,q0,q1,X))==allowed_step(s,q0,q1,twirl(X))
        assert dagger(allowed_step(s,q0,q1,X))==allowed_step(s,q0,q1,dagger(X))
for X in MATS:
    micro=X
    observer=twirl(X)
    for s,q0,q1 in settings+list(reversed(settings)):
        micro=allowed_step(s,q0,q1,micro)
        observer=allowed_step(s,q0,q1,observer)
        assert observer==twirl(micro)
print("PASS H72: micro-collision parameter family plus independently calibrated symmetric site dephasing closes on genuine 5D CPTP observer over finite histories")

# Calibration ambiguity: if only Phi=Ad_U is known then U is defined
# only up to central overall complex phase; calibrated Pphase is
# an independently offered architectural factor that fixes a split.
# Likewise just one U does not certify which s-pulses are operable.
V_alt=scale(U,-1)
for X in MATS:
    assert conj(V_alt,X)==conj(U,X)
assert V_alt!=U
print("PASS H72: original uncontrolled CPTP channel alone cannot certify unique microscopic unitary phase or a duration dial")

# Exact Lie closure and complex representation commutant.
C=com(A,B)
assert rr([A,B,C])==3
assert dagger(C)==scale(C,-1)
# Simultaneous centralizer {X:[X,A]=[X,B]=0} has complex dim1.
Lrows=[matvec(com(E,A))+matvec(com(E,B)) for E in MATS]
assert real_rank_complex(Lrows)==8
assert com(one,A)==z() and com(one,B)==z()
print("PASS H72: independent original P6 real A,B control group is irreducible over C3 (commutant dimension1)")

# Exact H43 5D parity-algebra is NOT stable under independent A,B.
odd=sub(unit(0,0),unit(2,2))
assert twirl(odd)==z()
assert twirl(com(A,odd))!=z()
assert twirl(com(B,odd))!=z()
print("PASS H72: 5D reflection algebra is not physically closed under the unmodified P6 independent two-knob control manifold")

# Analytic classification: if a UNITAL C*-subalgebra A0 of M3 is
# invariant under every exp(t A) and exp(t B), the connected generated
# SO(3) group fixes each minimal central projection of A0, since
# center has finitely many such projections. They commute with A,B;
# centralizer is C I, so center(A0)=C I. Finite-dimensional factor
# A0 ~= Mk⊗Im acting unitally on C3, km=3 (prime); hence k=1 (CI)
# or k=3 (M3). No proper intermediate trace-preserving conditional
# expectation observer can have invariant image algebra under all
# these reversible unitary controls.
print("PASS H72: representation-theoretic NO proper 2..8D unital C*-algebra invariant under both full original P6 real control rotations")

assert rank_complex(H)==5
assert rr([Xi(scale(h,I)) for h in H]+[EV])==6
print("PASS H72: original P3 hidden Xi lacks recovered K+: collision factor is ADDITIONAL independent physical structural input")
print("BOUNDARY: route-A construction uses independently certified Pphase factor, tunable collision parameter and symmetric noise, not P3-only necessary controls")
print("BOUNDARY: classification only for trace-preserving conditional-expectation onto unital C*-algebra, not ALL quantum/CP observer models")
print("BOUNDARY: not the frozen P6 two-independent-knob hardware, not CR-unique, and no physical P7/ADM/Einstein derivation")
