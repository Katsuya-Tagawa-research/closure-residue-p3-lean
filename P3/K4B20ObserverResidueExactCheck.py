"""B20 exact finite K4 observer-granularity and residue-factorization audit.

Rational matrix identities, not Lean formalization. Controls are declared,
not derived from a specific inherited P3/P6 experimental control manifold.
"""
from fractions import Fraction as F
from itertools import combinations, permutations

N=4
EDGES=list(combinations(range(N),2))
Z=F(0)
O=F(1)

def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(N)),Z)
             for j in range(N)] for i in range(N)]
def comm(A,B):
    X,Y=mm(A,B),mm(B,A)
    return [[X[i][j]-Y[i][j] for j in range(N)] for i in range(N)]
def diag(p):
    return [[p[i] if i==j else Z for j in range(N)] for i in range(N)]
def diagonal(M):return tuple(M[i][i] for i in range(N))
def K(x):
    M=[[Z for j in range(N)] for i in range(N)]
    for e,(a,b) in enumerate(EDGES):
        M[a][b]=x[e];M[b][a]=-x[e]
    return M
def res(x,p):return comm(K(x),diag(p))
def half_time_hessian(x,p):
    D=comm(K(x),res(x,p))
    return tuple(D[i][i]/2 for i in range(N))
def control_hessian(u,v,p):
    A=comm(K(u),res(v,p));B=comm(K(v),res(u,p))
    return tuple((A[i][i]+B[i][i])/2 for i in range(N))
def dot(a,b):return sum((u*v for u,v in zip(a,b)),Z)
def rank(rows):
    A=[list(map(F,r)) for r in rows]
    if not A:return 0
    nr,nc=len(A),len(A[0]);k=0
    for col in range(nc):
        pivot=next((i for i in range(k,nr) if A[i][col]),None)
        if pivot is None:continue
        A[k],A[pivot]=A[pivot],A[k]
        a=A[k][col]
        for i in range(k+1,nr):
            t=A[i][col]/a
            for j in range(col,nc):A[i][j]-=t*A[k][j]
        k+=1
        if k==nr:break
    return k

f1=tuple(F(v,2) for v in (1,1,-1,-1))
f2=tuple(F(v,2) for v in (1,-1,1,-1))
u=(F(1,4),)*4
p1=tuple(a+b/4 for a,b in zip(u,f1))
p2=tuple(a+b/4 for a,b in zip(u,f2))
assert p1==(F(3,8),F(3,8),F(1,8),F(1,8))
assert p2==(F(3,8),F(1,8),F(3,8),F(1,8))
ps=(p1,p2)
basis=[tuple(F(i==j) for i in range(6)) for j in range(6)]
coefT=((-1,1,0,0,1,-1),(0,0,1,-1,0,0))
assert EDGES==[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def TT_from_time_H(x):
    q1=half_time_hessian(x,p1);q2=half_time_hessian(x,p2)
    return (-4*(dot(f1,q1)-dot(f2,q2)),-4*dot(f1,q2))
def TT_from_control_H(u,v):
    q1=control_hessian(u,v,p1);q2=control_hessian(u,v,p2)
    return (-4*(dot(f1,q1)-dot(f2,q2)),-4*dot(f1,q2))

for x in basis+[(F(1),)*6,(F(-2),F(1,3),F(3),F(0),F(5,2),F(-4))]:
    for p in ps:
        C=res(x,p)
        assert all(C[i][i]==0 for i in range(N))
        assert C==[list(row) for row in zip(*C)]
        for e,(a,b) in enumerate(EDGES):
            assert C[a][b]==x[e]*(p[b]-p[a])
        q=half_time_hessian(x,p)
        expected=[]
        for a in range(N):
            expected.append(sum((x[e]**2*(p[b]-p[a])
                  for e,(v,b) in enumerate(EDGES) if v==a),Z)
                +sum((x[e]**2*(p[v]-p[a])
                  for e,(v,b) in enumerate(EDGES) if b==a),Z))
        assert q==tuple(expected)
    target=tuple(sum((F(coefT[i][e])*x[e]**2 for e in range(6)),Z)
                 for i in range(2))
    assert TT_from_time_H(x)==target

coherent_rows=[]
for p in ps:
    for a,b in EDGES:
        coherent_rows.append([res(e,p)[a][b] for e in basis])
assert rank(coherent_rows)==6
for p in ps:
    assert rank([[res(e,p)[a][b] for e in basis] for a,b in EDGES])==4
assert all(any(p[b]!=p[a] for p in ps) for a,b in EDGES)

def decode(C1,C2):
    out=[]
    for a,b in EDGES:
        i=0 if p1[b]!=p1[a] else 1
        p=ps[i]
        out.append((C1 if i==0 else C2)[a][b]/(p[b]-p[a]))
    return tuple(out)
for x in basis+[(F(3),F(-2),F(1,2),F(0),F(7),F(-4))]:
    assert decode(res(x,p1),res(x,p2))==x

pop_first_rows=[[res(e,p)[i][i] for e in basis]
                for p in ps for i in range(N)]
assert rank(pop_first_rows)==0
weight_rows=[[half_time_hessian(e,p)[i] for e in basis]
             for p in ps for i in range(N)]
assert rank(weight_rows)==5

for i,e in enumerate(basis):
    for j,f in enumerate(basis):
        for p in ps:
            h=control_hessian(e,f,p)
            if i!=j:assert h==(Z,)*N
            else:assert h==tuple(2*t for t in half_time_hessian(e,p))
            TT=TT_from_control_H(e,f)
            expected=tuple(2*F(coefT[a][i]) if i==j else Z
                           for a in range(2))
            assert TT==expected

for x in basis+[(F(1),)*6]:
    for y in basis:
        uu=decode(res(x,p1),res(x,p2))
        vv=decode(res(y,p1),res(y,p2))
        assert TT_from_control_H(x,y)==tuple(
            2*sum((F(coefT[a][i])*uu[i]*vv[i] for i in range(6)),Z)
            for a in range(2))
assert TT_from_control_H(basis[0],basis[0])==(-2*O,Z)
assert half_time_hessian(basis[0],p1)==half_time_hessian(
    tuple(-z for z in basis[0]),p1)
assert res(basis[0],p2)!=res(tuple(-z for z in basis[0]),p2)

def pv(p,sigma):
    v=[Z]*4
    for a in range(N):v[sigma[a]]=p[a]
    return tuple(v)
def pm(M,sigma):
    m=[[Z]*N for _ in range(N)]
    for a in range(N):
        for b in range(N):m[sigma[a]][sigma[b]]=M[a][b]
    return m
for sigma in permutations(range(N)):
    for e in basis:
        A=pm(K(e),sigma)
        for p in ps:
            dp=pv(p,sigma)
            lhs=comm(A,diag(dp))
            assert lhs==pm(res(e,p),sigma)
            rhs=comm(A,lhs)
            assert diagonal(rhs)==pv(
                tuple(2*z for z in half_time_hessian(e,p)),sigma)

print('PASS B20: six-dimensional full first-residue recovery')
print('PASS B20: two positive preparations, coherent first-time rank six')
print('PASS B20: population first-time rank zero, second-time weight rank five')
print('PASS B20: cross-edge return cancellation, TT second-control factorization')
print('PASS B20: complete S4 permutation covariance of residue and return')
print('Scope: declared K4 unitary controls, no inherited physical P3/P6 access')
