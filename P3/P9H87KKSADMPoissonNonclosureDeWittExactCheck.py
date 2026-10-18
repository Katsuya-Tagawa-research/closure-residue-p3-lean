"""H87: exact four-level U4 KKS Poisson-readout nonclosure and DeWitt gate.

This four-level coadjoint orbit is an INDEPENDENT comparator, not the
proven H75 6D CPTP orbit or a source-derived ADM canonical realization.
All matrix algebra is exact Gaussian-rational and the metric/kinetic
quadratic-form certificates are Fraction-rational.
"""
from fractions import Fraction as F
from itertools import combinations

from P9H24PhaseSensitiveResidueGaugeExactCheck import C, gc, I, O, Z0
from P9H75SemicausalMicroMemorySourceExactCheck import R60

assert R60[0][0] == I*gc(F(-32,135))
n=4
edges=list(combinations(range(n),2))
assert len(edges)==6

def zz():
    return [[Z0 for j in range(n)] for i in range(n)]
def eye():
    return [[O if i==j else Z0 for j in range(n)] for i in range(n)]
def E(a,b):
    X=zz()
    X[a][b]=O
    return X
def plus(A,B):
    return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]
def scale(A,z):
    return [[z*A[i][j] for j in range(n)] for i in range(n)]
def minus(A,B):
    return plus(A,scale(B,-1))
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(n)),Z0)
             for j in range(n)] for i in range(n)]
def dag(A):
    return [[A[j][i].conj() for j in range(n)] for i in range(n)]
def com(A,B):
    return minus(mm(A,B),mm(B,A))
def tr(A):
    return sum((A[i][i] for i in range(n)),Z0)
def X(a,b):
    return plus(E(a,b),E(b,a))
def Y(a,b):
    return scale(minus(E(a,b),E(b,a)),-I)
def pb(r,A,B):
    return -I*tr(mm(r,com(A,B)))
def read(r,A):
    return tr(mm(r,A))
def diag(v):
    return [[gc(v[i]) if i==j else Z0 for j in range(n)]
            for i in range(n)]

lam=(F(2,5),F(3,10),F(1,5),F(1,10))
star=diag(lam)
xs=[X(*e) for e in edges]
ys=[Y(*e) for e in edges]

assert all(dag(A)==A for A in xs+ys)
assert tr(star)==O
for k,e in enumerate(edges):
    assert read(star,xs[k])==Z0 and read(star,ys[k])==Z0
    for l,f in enumerate(edges):
        expected=gc(2*(lam[e[0]]-lam[e[1]])*int(k==l))
        assert pb(star,xs[k],ys[l])==expected
        assert pb(star,xs[k],xs[l])==Z0
        # d/dt Tr(X_e e^{-itY_f} rho e^{itY_f}) at t=0
        tangent=scale(com(ys[l],star),-I)
        assert read(tangent,xs[k])==expected
assert all(lam[e[0]]!=lam[e[1]] for e in edges)
print("PASS H87.1: U4 KKS six exact nonzero root-plane pairings and rank-6 coherence response differential")

e01=xs[edges.index((0,1))]
e12=xs[edges.index((1,2))]
y02=ys[edges.index((0,2))]
assert com(e01,e12)==minus(E(0,2),E(2,0))
assert pb(star,e01,e12)==Z0

def unitary_t(t):
    t=F(t)
    a=(1-t*t)/(1+t*t)
    b=2*t/(1+t*t)
    U=eye()
    U[0][0]=gc(a)
    U[2][2]=gc(a)
    U[0][2]=-I*gc(b)
    U[2][0]=-I*gc(b)
    assert mm(U,dag(U))==eye()
    return U,a,b

for t in (F(0),F(1,100),F(1,10),F(1,2)):
    U,a,b=unitary_t(t)
    rho=mm(mm(U,star),dag(U))
    assert tr(rho)==O
    assert dag(rho)==rho
    assert all(read(rho,A)==Z0 for A in xs)
    assert rho[0][2]==I*gc(a*b*(lam[0]-lam[2]))
    bracket=pb(rho,e01,e12)
    assert bracket==read(rho,y02)
    expected=gc(-F(4)*t*(1-t*t)/(F(5)*(1+t*t)**2))
    assert bracket==expected,(t,bracket,expected)
    if t>0:
        assert bracket!=Z0
    if t==F(1,2):
        assert rho[0][2]==I*gc(F(12,125))
        assert bracket==gc(F(-24,125))
print("PASS H87.2: distinct positive unitary-orbit states in arbitrarily small rational family share all six x readouts but have unequal {x01,x12}=-24/125 at t=1/2")
print("PASS H87.2: no descended autonomous Poisson structure can preserve the chosen six coherence coordinates on ANY rho_star neighborhood")

# Conditional fixed-solder K4 chart w_e=1+Re x_e, all these
# different microscopic states have w=1 and L=4 P_S.
def laplacian(w):
    L=[[F(0) for j in range(n)] for i in range(n)]
    for v,(i,j) in zip(w,edges):
        L[i][i]+=v
        L[j][j]+=v
        L[i][j]-=v
        L[j][i]-=v
    return L

for t in (F(0),F(1,10),F(1,2)):
    U,_,_=unitary_t(t)
    rho=mm(mm(U,star),dag(U))
    w=tuple(F(1)+read(rho,A).r for A in xs)
    assert all(v>0 for v in w)
    L=laplacian(w)
    assert L==[[F(4*int(i==j)-1) for j in range(n)]
               for i in range(n)]
    assert pb(rho,e01,e12)==read(rho,y02)
print("PASS H87.3: same positive K4 metric response 4I_S does not restore six-readout Poisson projectability")

# Euclidean SPD3 momentum kinetic forms, exact rational inertia:
# D(P)=tr(P^2)-1/2(tr P)^2 versus E(P)=tr(P^2).
def sym3(vals):
    return [[F(vals[i][j]) for j in range(3)] for i in range(3)]
def basisdiag(a,b,c):
    return sym3(((a,0,0),(0,b,0),(0,0,c)))
def off(a,b):
    A=[[F(0) for j in range(3)] for i in range(3)]
    A[a][b]=F(1)
    A[b][a]=F(1)
    return A
def traceprod(A,B):
    return sum((A[i][j]*B[j][i] for i in range(3)
                for j in range(3)),F(0))
def trace3(A):
    return sum((A[i][i] for i in range(3)),F(0))
def DeWitt(A,B):
    return traceprod(A,B)-F(1,2)*trace3(A)*trace3(B)

traceless=[basisdiag(1,-1,0),basisdiag(1,1,-2),
           off(0,1),off(0,2),off(1,2)]
six=traceless+[basisdiag(1,1,1)]
expected=(F(2),F(6),F(2),F(2),F(2),F(-3,2))
for i,A in enumerate(six):
    for j,B in enumerate(six):
        assert DeWitt(A,B)==(expected[i] if i==j else F(0))
        if i<5:
            assert trace3(A)==0
assert traceprod(six[5],six[5])==3
assert DeWitt(six[5],six[5])==F(-3,2)
print("PASS H87.5: full exact six-direction DeWitt Gram has signature (5+,1-), while Euclidean momentum norm has (6+,0-)")
print("BOUNDARY: local Darboux charts exist but must replace noncommuting given physical readouts; compact KKS orbit not globally cotangent exact")
print("BOUNDARY: positive response metric is NOT ADM momentum kinetics; no sourced P3/P6/KKS-to-ADM, full HDA, EH/Einstein dynamics or F completeness")
