"""H75 — genuine 6D CPTP micro source + quantum-classical memory, route A.

One fixed 3-level H42 original complex U and a TWO-flag microscopic
quantum register. A fully specified four-Kraus 6D CPTP channel
performs a NONTRIVIAL partial site-0 measurement (two rational Kraus
M0, M1), records the outcome in the flag and then applies H42 U.

Partial trace of flag is an EXACT autonomous CPTP 3-level observer
for ALL MICROSCOPIC INPUTS, even initially entangled/correlated ones.
Independently specified REAL 01/12 exchange controls and arbitrary
site-dephasing are available on the same 6D physical source, with exact
visible single-copy POVM readout and all finite adaptive visible-only
instrument histories. Original TRUE P3 (not arbitrary surrogate) has
R2=0, R3 != 0 on the FULL microscopic 6D diagonal algebra, plus on
the reduced 3D channel. The flag records nontrivial site information.

This is a CONDITIONAL constructive semicausal quantum microarchitecture.
The hardware Kraus measurement, reset, two control knobs, quantum
marginal access and noise are INDEPENDENT SOURCE DATA, not consequences
of P3-only hidden residues. The observer retains the full accessible
qutrit, so H74 whole-qutrit strong-readout rigidity is fully respected.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    N,unit,z,eye,add,sub,scale,mm,dagger,com,diag,hidden,trace,rr
)
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import U,A,B
from P9H45QuadraticResidueSufficientOddSeedExactCheck import R12
assert N==3

def eye_n(n):
    return [[O if i==j else Z0 for j in range(n)] for i in range(n)]
def zero_n(n):
    return [[Z0 for j in range(n)] for i in range(n)]
def matadd(X,Y):
    return [[X[i][j]+Y[i][j] for j in range(len(X))] for i in range(len(X))]
def matscale(X,c):
    return [[c*X[i][j] for j in range(len(X))] for i in range(len(X))]
def matadj(X):
    n=len(X)
    return [[X[j][i].conj() for j in range(n)] for i in range(n)]
def matmul(X,Y):
    n=len(X)
    return [[sum((X[i][k]*Y[k][j] for k in range(n)),Z0)
             for j in range(n)] for i in range(n)]
def matcomm(X,Y):
    P=matmul(X,Y);Q=matmul(Y,X)
    return [[P[i][j]-Q[i][j] for j in range(len(X))] for i in range(len(X))]
def mattrace(X):
    return sum((X[i][i] for i in range(len(X))),Z0)
def diag_n(X):
    Y=zero_n(len(X))
    for i in range(len(X)):Y[i][i]=X[i][i]
    return Y
def hidden_n(X):
    Y=zero_n(len(X))
    for i in range(len(X)):
        for j in range(len(X)):
            if i!=j:Y[i][j]=X[i][j]
    return Y
def envblock(X,a,b):
    return [[X[3*a+i][3*b+j] for j in range(3)]
            for i in range(3)]
def embed(X,env=0):
    Y=zero_n(6)
    for i in range(3):
        for j in range(3):Y[3*env+i][3*env+j]=X[i][j]
    return Y
def qtrace(X):
    return matadd(envblock(X,0,0),envblock(X,1,1))
def qconj(W,X):
    return matmul(matmul(W,X),matadj(W))
def lift(W):
    Y=zero_n(6)
    for env in (0,1):
        for i in range(3):
            for j in range(3):Y[3*env+i][3*env+j]=W[i][j]
    return Y

ONE=eye_n(3)
ONE6=eye_n(6)
M0=[[gc(a) if i==j else Z0 for j in range(3)]
    for i,a in enumerate((F(1),F(3,5),F(3,5)))]
M1=[[gc(a) if i==j else Z0 for j in range(3)]
    for i,a in enumerate((F(0),F(4,5),F(4,5)))]
assert matadd(matmul(matadj(M0),M0),
              matmul(matadj(M1),M1))==ONE
Ms=(M0,M1)
UM=[matmul(U,M) for M in Ms]

# Four explicitly specified quantum Kraus operators of micro channel:
# L_(a,b) = |a><b|_flag tensor (U M_a).
# This resets the old flag, records the unsharp measurement outcome
# a, and gives a genuine nontrivial instrument on the visible system.
LK=[]
for a in (0,1):
    for b in (0,1):
        W=zero_n(6)
        for i in range(3):
            for j in range(3):W[3*a+i][3*b+j]=UM[a][i][j]
        LK.append(W)
TOT=zero_n(6)
for W in LK:TOT=matadd(TOT,matmul(matadj(W),W))
assert TOT==ONE6
def micro(Y):
    T=zero_n(6)
    for W in LK:
        T=matadd(T,qconj(W,Y))
    return T
def visible(X):
    Y=zero_n(3)
    for m in Ms:
        Y=matadd(Y,matmul(matmul(m,X),matadj(m)))
    return qconj(U,Y)

SBASIS=[unit(i,j) for i in range(3) for j in range(3)]
MBASIS=[[[O if (i==j0 and j==k0) else Z0 for j in range(6)]
         for i in range(6)]
        for j0 in range(6) for k0 in range(6)]
assert len(MBASIS)==36
for Y in MBASIS:
    assert qtrace(micro(Y))==visible(qtrace(Y))
    assert mattrace(micro(Y))==mattrace(Y)
    assert matadj(micro(matadj(Y)))==micro(Y)
assert visible(unit(0,0))==qconj(U,unit(0,0))
assert visible(unit(1,1))==qconj(U,unit(1,1))
print("PASS H75: 4-Kraus MICRO 6D CPTP source with actual environment flag, exact all-input semicausal CPTP partial-trace intertwiner")

# The environment acquires actual state information (not a dummy tensor
# spectator), and the microscopic output flags are nonconstant.
d0=unit(0,0);d1=unit(1,1);d2=unit(2,2)
r0=micro(embed(d0));r1=micro(embed(d1))
assert mattrace(envblock(r0,0,0))==O
assert mattrace(envblock(r0,1,1))==Z0
assert mattrace(envblock(r1,0,0))==gc(F(9,25))
assert mattrace(envblock(r1,1,1))==gc(F(16,25))
assert r1!=embed(qtrace(r1))
print("PASS H75: nontrivial environment registers measured site information: flag1 probability 0 for E00 vs 16/25 for E11")

# EXACT original P3 diagonal quadratic residue:
# X is a true 6D DIAGONAL micro seed; h1=(I-Delta_6) micro(X),
# h2=(I-Delta_6) micro^2(X), R12=Delta_6([h1,h2†]).
def r6(a,b):
    h1=hidden_n(micro(a))
    h2=hidden_n(micro(micro(b)))
    return diag_n(matcomm(h1,matadj(h2)))
def r6same(X):
    return r6(X,X)
def r3(a,b):
    h1=hidden(visible(a))
    h2=hidden(visible(visible(b)))
    return diag(com(h1,dagger(h2)))
def r2micro(a,b):
    h1=hidden_n(micro(a))
    k1=hidden_n(micro(b))
    return diag_n(matcomm(h1,matadj(k1)))
D6=[MBASIS[6*i+i] for i in range(6)]
assert all(r2micro(x,y)==zero_n(6) for x in D6 for y in D6)
R60=r6same(D6[0])
assert [R60[i][i] for i in range(6)]==[
    I*gc(F(-32,135)),I*gc(F(16,135)),I*gc(F(16,135)),
    Z0,Z0,Z0]
assert R60!=zero_n(6)
R30=r3(d0,d0)
R31=r3(d1,d1)
assert [R30[i][i] for i in range(3)]==[
    I*gc(F(-32,135)),I*gc(F(16,135)),I*gc(F(16,135))]
assert [R31[i][i] for i in range(3)]==[
    I*gc(F(-8,405)),I*gc(F(64,405)),I*gc(F(-56,405))]
assert r6same(D6[1])!=zero_n(6)
print("PASS H75: full ORIGINAL P3 on 6D micro diagonal has all R2=0 but nonzero genuine R3 witness i diag(-32,16,16,0,0,0)/135")
print("PASS H75: reduced 3D original P3 also has nonzero signed quadratic R3, with exact independent diagonal seed witnesses")

# Two INDEPENDENT real 01 and 12 site knobs acting on the SAME 6D
# physical micro quantum channel. Site-dephasing q_j are also
# independent CPTP calibrated physical nuisance operations.
def edge_cayley(K,t):
    assert mm(mm(K,K),K)==scale(K,-1)
    assert dagger(K)==scale(K,-1)
    W=add(eye(),
          add(scale(K,F(2)*t/(1+t*t)),
              scale(mm(K,K),F(2)*t*t/(1+t*t))))
    assert mm(dagger(W),W)==eye()
    return W
def control(x,y):
    W=mm(edge_cayley(A,x),edge_cayley(B,y))
    assert mm(dagger(W),W)==eye()
    return W
def dephase_j(j,q,X):
    Z=eye()
    Z[j][j]=-O
    return add(scale(X,q),scale(qconj(Z,X),1-q))
def noise(qs,X):
    for j,q in enumerate(qs):
        X=dephase_j(j,q,X)
    return X
def physical_visible(x,y,qs,X):
    return noise(qs,qconj(control(x,y),visible(X)))
def physical_micro(x,y,qs,Y):
    Z=micro(Y)
    W6=lift(control(x,y))
    Z=qconj(W6,Z)
    for j,q in enumerate(qs):
        Z6=lift(eye())
        for env in (0,1):Z6[3*env+j][3*env+j]=-O
        Z=matadd(matscale(Z,q),matscale(qconj(Z6,Z),1-q))
    return Z
SETTINGS=[
    (F(0),F(0),(F(1),F(1),F(1))),
    (F(1,4),F(-2,5),(F(4,5),F(3,5),F(7,8))),
    (F(-3,7),F(1,3),(F(1,2),F(1),F(1,4))),
]
for x,y,qs in SETTINGS:
    for Y in MBASIS:
        assert qtrace(physical_micro(x,y,qs,Y))==physical_visible(x,y,qs,qtrace(Y))
print("PASS H75: TWO independently calibrated real controls, arbitrarily asymmetric real site dephasing and SAME micro P3 source intertwine CPTP visible dynamics on ALL 36 matrix units")

# Arbitrary prescribed sequences and arbitrary adaptive visible-only
# CP measurement branches commute with the partial trace. Their
# normalized probabilities therefore agree by induction for every
# visible measurement choice / history.
def visible_branch(j,X):
    pj=unit(j,j)
    return mm(mm(pj,X),pj)
def micro_branch(j,Y):
    P=lift(unit(j,j))
    return qconj(P,Y)
for j in range(3):
    for Y in MBASIS:
        assert qtrace(micro_branch(j,Y))==visible_branch(j,qtrace(Y))
for X in (embed(d0),embed(d1),embed(d2),embed(scale(eye(),F(1,3)))):
    full=X
    reduced=qtrace(X)
    for s,(x,y,qs) in enumerate(SETTINGS):
        full=physical_micro(x,y,qs,full)
        reduced=physical_visible(x,y,qs,reduced)
        j=(s+1)%3
        full=micro_branch(j,full)
        reduced=visible_branch(j,reduced)
        assert qtrace(full)==reduced
        assert mattrace(full)==trace(reduced)
print("PASS H75: exact physical single-copy site readout, CP outcome branches and finite adaptive visible-only process equality")

# A single environment-FEEDBACK gate destroys semicausality even
# though it is itself fully unitary CPTP. Same visible microscopic
# state with different initial hidden flags produces different outputs.
SWAP01=add(add(unit(0,1),unit(1,0)),unit(2,2))
assert mm(dagger(SWAP01),SWAP01)==eye()
Fgate=zero_n(6)
for i in range(3):Fgate[i][i]=O
for i in range(3):
    for j in range(3):Fgate[3+i][3+j]=SWAP01[i][j]
assert matmul(matadj(Fgate),Fgate)==ONE6
assert qtrace(embed(d0,0))==qtrace(embed(d0,1))
assert qtrace(qconj(Fgate,embed(d0,0)))==d0
assert qtrace(qconj(Fgate,embed(d0,1)))==d1
print("PASS H75: EXACT feedback unitary counterexample — hidden -> visible signalling forbids autonomous marginal CP closure without additional memory")

# Quantum-full-input recovery from partial trace is impossible, even
# though it perfectly reproduces ALL visible single-copy POVMs:
# two orthogonal environment flag input states have same output.
assert qtrace(embed(d0,0))==qtrace(embed(d0,1))
assert embed(d0,0)!=embed(d0,1)
print("PASS H75: no full 6D input quantum recovery; observer has retained the COMPLETE 3D visible system, so H74 readout rigidity is respected")
print("BOUNDARY: 6D source includes independent unsharp instrument, reset/flag register, visible A/B knobs and dephasing as declared PHYSICAL assumptions")
print("BOUNDARY: genuine original P3 R3 here is ordinary CP quantum mechanics, NOT CR-specific experimental novelty; no derivation of frozen P6 microscopic J_N")
print("BOUNDARY: autonomous semicausal closure requires NO hidden-to-visible feedback; it is not a generic non-Markovian shadow-return mechanism")
print("BOUNDARY: no physical P7/P8 soldering, KKS->ADM, off-shell HDA or Einstein/P9 Minimum Success")
