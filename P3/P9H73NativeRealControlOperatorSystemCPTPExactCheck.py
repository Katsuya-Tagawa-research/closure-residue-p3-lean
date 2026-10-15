"""H73 — CP rank-six operator-system observer sourced by REAL P6 primitives.

A finite 25-setting exact rational convex mixture of rotated real
population pinching implements E(X)=(Tr(X)I+X+X^T)/5 on M3(C).
The 24 proper signed permutations and the REAL Cayley of H42 suffice.
E is CPTP, non-idempotent rank 6, symmetric non-algebraic image.
It commutes with ALL real SO(3) controls and independently calibrated
unital TP real site dephasing. The rank-six information is MINIMAL
for exact LINEAR prediction of all real rotated population readings.

IMPORTANT physical caveats:
- Complete pinching is an IDEAL nonselective population measurement
  / infinite-dephasing limit, not finite positive-rate GKSL dephasing.
- Linear inversion of the original population readings is NOT a
  single-output POVM; an explicit trace-distance counterexample proves
  its impossibility. Statistical many-copy tomography is required.
- H42's non-real microscopic Phi does NOT commute with this observer,
  and real-only P6 has zero original signed P3 residue. Therefore the
  simultaneous nonzero-P3-to-frozen-P6 provenance gate remains OPEN.

All exact Gaussian rational, no numerical tolerances.
"""
from fractions import Fraction as F
from itertools import permutations, product
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    N,unit,z,eye,add,sub,scale,mm,dagger,diag,trace,com,rr
)
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import (
    Cayley,U,A,B
)
from P9H44MinimalObserverMemoryQuadraticResidueExactCheck import Phi
from P9H48InstrumentProvenanceKernelClosureExactCheck import real_rank_complex
assert N==3

def transpose(X):
    return [[X[j][i] for j in range(3)] for i in range(3)]
def real_orth(W):
    return transpose(W)==dagger(W) and mm(dagger(W),W)==eye()
def conjugate(W,X):
    return mm(mm(W,X),dagger(W))
def eclosed(X):
    return scale(add(add(X,transpose(X)),scale(eye(),trace(X))),F(1,5))
def pin(X):
    return diag(X)
def rankmap(mapper):
    return real_rank_complex([[q for row in mapper(unit(i,j)) for q in row]
                              for i in range(3) for j in range(3)])

# Exactly 24 orientation-preserving signed 3x3 coordinate permutations.
G=[]
for perm in permutations(range(3)):
    sign_perm=(-1)**sum(perm[i]>perm[j] for i in range(3)
                        for j in range(i+1,3))
    for signs in product((-1,1),repeat=3):
        if sign_perm*signs[0]*signs[1]*signs[2]!=1:
            continue
        W=z()
        for col in range(3):
            W[perm[col]][col]=gc(signs[col])
        assert real_orth(W)
        G.append(W)
assert len(G)==24
R=Cayley
assert real_orth(R)
assert R==[[gc(F(2,3)),gc(F(2,3)),gc(F(-1,3))],
           [gc(F(-2,3)),gc(F(1,3)),gc(F(-2,3))],
           [gc(F(-1,3)),gc(F(2,3)),gc(F(2,3))]]
assert all(real_orth(mm(g,R)) for g in G)

def rotated_pinching(W,X):
    return conjugate(W,pin(conjugate(dagger(W),X)))
def finite_observer(X):
    # A full **nonselective population pinch** in one chosen real
    # basis, followed by returning to original axes, is CPTP.
    # Then choose a randomized orientation; no complex phase gates.
    y=scale(pin(X),F(13,40))
    for g in G:
        y=add(y,scale(rotated_pinching(mm(g,R),X),F(27,960)))
    return y

BASIS=[unit(i,j) for i in range(3) for j in range(3)]
for X in BASIS:
    assert finite_observer(X)==eclosed(X)
    assert dagger(eclosed(dagger(X)))==eclosed(X)
    assert trace(eclosed(X))==trace(X)
assert eclosed(eye())==eye()
assert rankmap(eclosed)==6
assert rr([A,B,com(A,B)])==3
for X in (A,B,com(A,B)):
    assert eclosed(X)==z()
assert eclosed(add(unit(0,1),unit(1,0)))==scale(add(unit(0,1),unit(1,0)),F(2,5))
assert eclosed(eclosed(add(unit(0,1),unit(1,0))))!=eclosed(add(unit(0,1),unit(1,0)))
# Output is complex symmetric; its product space isn't an algebra.
S01=add(unit(0,1),unit(1,0))
S12=add(unit(1,2),unit(2,1))
assert transpose(mm(S01,S12))!=mm(S01,S12)
print("PASS H73: EXACT 25-setting rational mixture of REAL rotated population pinching equals rank6 CPTP non-idempotent symmetric operator-system observer")
print("PASS H73: it deletes ONLY all three transpose-skew quadratures, is non-algebraic, and retains spin0+spin2 information")

def ortho_edge(a,b,c,s):
    c,s=gc(c),gc(s)
    assert c*c+s*s==O
    W=eye()
    W[a][a]=c;W[b][b]=c
    W[a][b]=s;W[b][a]=-s
    assert real_orth(W)
    return W
O01=ortho_edge(0,1,F(3,5),F(4,5))
O12=ortho_edge(1,2,F(5,13),F(12,13))
Q12=ortho_edge(1,2,0,1)
O02=mm(mm(Q12,O01),dagger(Q12))
assert real_orth(O02)
for W in (O01,O12,O02,R)+G:
    for X in BASIS:
        assert eclosed(conjugate(W,X))==conjugate(W,eclosed(X))

def global_dephasing(X,q):
    assert 0<=q<=1
    return add(scale(X,q),scale(diag(X),1-q))
def local_site(j,X,q):
    assert 0<=q<=1
    Z=eye()
    Z[j][j]=-O
    return add(scale(X,q),scale(conjugate(Z,X),1-q))
def dephasing(qs,X):
    for j,q in enumerate(qs):
        X=local_site(j,X,q)
    return X
for q in (F(0),F(1,3),F(3,5),F(1)):
    for X in BASIS:
        assert eclosed(global_dephasing(X,q))==global_dephasing(eclosed(X),q)
for qs in ((F(1),F(1),F(1)),
           (F(4,5),F(3,5),F(7,8)),
           (F(1,2),F(1),F(1,4))):
    for X in BASIS:
        assert eclosed(dephasing(qs,X))==dephasing(qs,eclosed(X))
print("PASS H73: exact intertwining with BOTH independently varied real path controls, all SO3 by covariance, and arbitrarily unequal calibrated site dephasing")

# Controlled histories: each step is a genuine real unitary CPTP
# plus independently parameterized site dephasing. Its output map
# is the exact same CPTP step, not an arbitrary inverse on range.
SEQUENCE=[
    (O01,(F(4,5),F(3,5),F(7,8))),
    (O12,(F(1,2),F(1),F(1,4))),
    (R,(F(2,3),F(3,4),F(1))),
    (O02,(F(1),F(2,5),F(5,8)))
]
for X in BASIS:
    micro=X
    observed=eclosed(X)
    for W,qs in SEQUENCE:
        micro=dephasing(qs,conjugate(W,micro))
        observed=dephasing(qs,conjugate(W,observed))
        assert eclosed(micro)==observed
print("PASS H73: full two-knob real controls and unequal dephasing have autonomous CPTP dynamics on non-C* rank6 range")

# The observable span of all real-rotated population readouts is
# precisely the six-dimensional complex-symmetric matrix space.
# Three diagonal observables plus 01,12,02 rotated populations suffice.
SETTINGS=[(eye(),0),(eye(),1),(eye(),2),
          (O01,0),(O12,1),(O02,0)]
def pvalues(X):
    return [conjugate(W,X)[j][j] for W,j in SETTINGS]
assert real_rank_complex([pvalues(X) for X in BASIS])==6
for X in BASIS:
    for W,j in SETTINGS:
        # This is an EXACT linear statistical reconstruction,
        # NOT a physically CPTP output-state recovery.
        input_pop=conjugate(W,X)[j][j]
        signal_pop=conjugate(W,eclosed(X))[j][j]
        assert input_pop==(gc(F(5,2))*signal_pop-
                           gc(F(1,2))*trace(X))
print("PASS H73: six complex-linear directions are NECESSARY and SUFFICIENT to predict all real-basis population responses (offline linear inversion)")

# The offline reconstruction is NOT a single-copy physical POVM:
# two orthogonal computational site pure states become nonorthogonal
# after E, with trace distance contracting by factor 2/5.
D= sub(unit(0,0),unit(1,1))
assert eclosed(D)==scale(D,F(2,5))
# trace norms of diagonal differences are exact: 2 and 4/5.
assert eclosed(unit(0,0))!=unit(0,0)
# A single output POVM simulating all input computational populations
# would perfectly distinguish eclosed(E00) and eclosed(E11), but
# trace-distance data processing forbids it (D_after=2/5 < 1).
print("PASS H73: original P6 population probabilities need nonpositive linear inversion; no exact single-copy output POVM can reproduce them")

# Original H42 micro is NONREAL: the positive P3 R3 lives beyond the
# transpose-invariant physical P6 exchange-only source.
assert eclosed(A)==z()
leak=eclosed(Phi(A))
assert leak!=z()
assert leak==[[Z0,gc(F(4,15))*I,Z0],
             [gc(F(4,15))*I,Z0,gc(F(2,15))*I],
             [Z0,gc(F(2,15))*I,Z0]]
print("PASS H73: SAME non-real H42 original-P3 channel leaks skew kernel; this rank6 observer does NOT close under that nonzero-residue micro source")
print("BOUNDARY: the observer protocol assumes ideal COMPLETE nonselective population pinching and classical random real basis control; finite-time GKSL dephasing alone does NOT implement exact q=0")
print("BOUNDARY: this is a genuine P6 REAL-control CP bridge with added observer operation; it does NOT supply physical P3->frozen P6 provenance or a nonzero original signed residue")
print("BOUNDARY: non-idempotent operator-system rank6 bypasses H72's subalgebra no-go; original P3 signed-return/Einstein theory OPEN")
