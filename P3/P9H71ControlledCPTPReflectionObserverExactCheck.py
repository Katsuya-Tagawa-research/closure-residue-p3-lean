"""H71 — constructive controlled-CPTP reflection observer, exact scope.

Reuse fixed H42 ORIGINAL P3 microscopic Phi, H43/44 CPTP twirl,
H45 original signed quadratic R12. All arithmetic Gaussian rationals.

Positively construct a physically legal CONDITIONAL symmetry-locked
CPTP control+site-dephasing subfamily with exact 5D observer closure.
Prove obstruction to extending this to two independent P6-like
exchange knobs or arbitrary non-reflection-symmetric dephasing.
On even diagonal seeds, the original signed P3 R12 IS retained by
this observer; on all diagonal seeds it is not (H70).

This is a rigorous finite CONSTRUCTION under independently declared
collective control and symmetric dephasing, NOT a derivation of those
physical restrictions from frozen P6 or the ORIGINAL P3 Xi source.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    N,eye,unit,z,add,sub,scale,mm,dagger,com,trace,rr
)
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import (
    reflection, U, A, B, H, Xi, rank_complex
)
from P9H43EquivariantCPTPCollectiveExtractionExactCheck import twirl
from P9H44MinimalObserverMemoryQuadraticResidueExactCheck import Phi
from P9H45QuadraticResidueSufficientOddSeedExactCheck import R12

assert N==3
P=reflection
EV=add(A,B)
OD=sub(A,B)
assert mm(P,P)==eye()
def conj(W,X):
    return mm(mm(W,X),dagger(W))
def parity(X):
    return conj(P,X)
def real_rank_end(X):
    return X==twirl(X)
def zero(X):
    return X==z()
def pow2(K):
    return mm(K,K)
def cayley(K,t):
    # Exact rational inverse of (I-tK) for any 3x3 anti-Hermitian K,
    # from row-reduction in the exact Gaussian-rational scalar field.
    E=eye()
    M=sub(E,scale(K,t))
    rhs=add(E,scale(K,t))
    aug=[M[i][:]+rhs[i][:] for i in range(3)]
    for col in range(3):
        row=next(k for k in range(col,3) if aug[k][col]!=Z0)
        aug[row],aug[col]=aug[col],aug[row]
        pivot=aug[col][col]
        aug[col]=[v/pivot for v in aug[col]]
        for other in range(3):
            if other!=col:
                c=aug[other][col]
                aug[other]=[v-c*w for v,w in zip(aug[other],aug[col])]
    Q=[r[3:] for r in aug]
    # M Q = rhs, commute since Q is a rational function of K
    assert mm(M,Q)==rhs
    assert mm(dagger(Q),Q)==E
    return Q

assert dagger(EV)==scale(EV,-1)
assert dagger(OD)==scale(OD,-1)
assert parity(EV)==EV
assert parity(OD)==scale(OD,-1)
assert parity(A)==B and parity(B)==A
assert mm(P,U)==mm(U,P)
for t in (F(0),F(1,4),F(2,5)):
    V=cayley(EV,t)
    assert parity(V)==V
    assert mm(P,V)==mm(V,P)
print("PASS H71: rational collective real-control Cayley pulses commute with H42 reflection and are unitary")

def flip(j):
    # Hermitian phase flip I-2|j><j|.
    Z=sub(eye(),scale(unit(j,j),gc(2)))
    assert mm(Z,Z)==eye() and dagger(Z)==Z
    return Z
FL=[flip(j) for j in range(3)]
def site_dephase(j,q,X):
    assert F(0)<=q<=F(1)
    return add(scale(X,q),scale(conj(FL[j],X),1-q))
def noise(qs,X):
    for j,q in enumerate(qs):
        X=site_dephase(j,q,X)
    return X
def step(t,qs,X):
    # Each piece CPTP: fixed unitary H42 Phi, collective Cayley U,
    # and independently calibrated dephasing phase-flip mixtures.
    return noise(qs,conj(cayley(EV,t),Phi(X)))
BASIS=[unit(i,j) for i in range(3) for j in range(3)]
SETTINGS=[
    (F(0),(F(1),F(1),F(1))),
    (F(1,4),(F(4,5),F(2,3),F(4,5))),
    (F(2,5),(F(3,5),F(7,8),F(3,5))),
]
for t,qs in SETTINGS:
    for X in BASIS:
        assert twirl(step(t,qs,X))==step(t,qs,twirl(X))
        assert trace(step(t,qs,X))==trace(X)
        assert dagger(step(t,qs,dagger(X)))==step(t,qs,X)
print("PASS H71: true conditional CP collective-control / endpoint-symmetric-site-dephasing source intertwines 5D twirl on all M3")

def run(seq,X):
    for t,qs in seq:
        X=step(t,qs,X)
    return X
for X in BASIS:
    for seq in (
        SETTINGS,
        SETTINGS[1:],
        SETTINGS[::-1]+SETTINGS[1:],
    ):
        assert twirl(run(seq,X))==run(seq,twirl(X))
print("PASS H71: arbitrary finite concatenations of parity-compatible CPTP controls have autonomous 5D observer dynamics")

# First-order necessary kernel preservation fails with odd control.
# In contrast even K preserves both parity eigenspaces.
KOD=OD
w=sub(unit(0,0),unit(2,2))  # strict parity-odd microscopic witness
assert twirl(w)==z()
assert twirl(com(EV,w))==z()
leak=twirl(com(KOD,w))
assert leak!=z()
assert parity(leak)==leak
assert twirl(com(A,w))!=z() and twirl(com(B,w))!=z()
# Under K(x,y)=xA+yB, the parity-odd component is (x-y)/2*(A-B).
# Thus at generator level, for this witness, kernel invariance forces
# x=y, assuming that the control is independently available near zero.
for x,y in ((F(1),F(1)),(F(1),F(0)),(F(0),F(1)),
            (F(3,5),F(4,5)),(F(-1),F(1))):
    K=add(scale(A,x),scale(B,y))
    out=twirl(com(K,w))
    assert (out==z())==(x==y)
# Not only generator: explicit unitary Cayley witness of leakage.
for t in (F(1,4),F(2,5)):
    V=cayley(OD,t)
    assert twirl(conj(V,w))!=z()
print("PASS H71: independent A,B real knobs and reflection-odd A-B leak observer kernel; x=y is necessary for full infinitesimal control family")

# Site-selective dephasing: the two endpoint rates need matching.
# For phase-flip channel q_j, an offdiagonal ij acquires
# f_i f_j where f_j=2q_j-1. Odd E01-E21 leaks when q0!=q2,
# provided the center factor f1 != 0.
oddedge=sub(unit(0,1),unit(2,1))
evenedge=add(unit(0,1),unit(2,1))
assert twirl(oddedge)==z()
q_asym=(F(4,5),F(1),F(3,5))
out=twirl(noise(q_asym,oddedge))
assert out==scale(evenedge,F(1,5))
assert out!=z()
for X in BASIS:
    qs=(F(4,5),F(3,4),F(4,5))
    assert twirl(noise(qs,X))==noise(qs,twirl(X))
print("PASS H71: endpoint-asymmetric independently allowed CPTP site dephasing breaks 5D observer closure; symmetric calibrated noise preserves it")

# Restricted ORIGINAL signed P3 quadratic return: parity-even diagonal
# seeds d=a(E00+E22)+b E11 are fully known from current twirl E(d)=d.
# Their original R12(d,d') can thus be computed from observer record
# and the same fixed microscopic Phi, without loss of signed values.
d_mid=unit(1,1)
d_edge=scale(add(unit(0,0),unit(2,2)),F(1,2))
for d in (d_mid,d_edge,scale(eye(),F(1,3)),
          add(scale(d_mid,F(1,3)),scale(d_edge,F(2,3)))):
    assert twirl(d)==d
    for e in (d_mid,d_edge):
        assert R12(d,e)==R12(twirl(d),twirl(e))
assert rr([R12(d,e) for d in (d_mid,d_edge)
           for e in (d_mid,d_edge)])==1
d0=unit(0,0);d2=unit(2,2)
assert twirl(d0)==twirl(d2)
assert R12(d0,d0)!=R12(d2,d2)
print("PASS H71: original signed P3 quadratic return reconstructible on reflection-even diagonal preparations (rank1); not on full D3")

# Actual unchanged H42 source has full P3 Xi span rank5 but
# excludes the physical collective locked even direction EV.
assert rank_complex(H)==5
assert rr([Xi(scale(h,I)) for h in H]+[EV])==6
print("PASS H71: source provenance NOT proved — actual original H42 P3 Xi(H∞) EXCLUDES locked A+B control")
print("BOUNDARY: concrete route-A CONDITIONAL finite construction, NOT P3->frozen P6 independent control/observer source")
print("BOUNDARY: frozen P6 independent two-knob controls and potentially unequal site-dephasing do NOT automatically meet reflection-locked premises")
print("BOUNDARY: no general residue fidelity outside even diagonal seeds, no KKS-ADM/Einstein/P9 Minimum Success")
