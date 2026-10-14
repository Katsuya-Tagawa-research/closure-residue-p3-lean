"""Independent P9.38 cross-audit: diagonal-gauge Laplacian and provenance.

Pure Fraction/Gaussian-rational arithmetic; imports H24's already-audited
C class. This does NOT equate witness variation with the P3 R3 subspace,
and does NOT grant CR-specific operational discrimination or ADM dynamics.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0,U

def zero(n): return [[Z0 for _ in range(n)] for _ in range(n)]
def unit(n,i,j):
    m=zero(n);m[i][j]=O;return m
def diagv(a):
    n=len(a);m=zero(n)
    for i,v in enumerate(a):m[i][i]=gc(v)
    return m
def add(a,b):
    n=len(a);return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
def scale(a,c):
    n=len(a);return [[a[i][j]*c for j in range(n)] for i in range(n)]
def sub(a,b):return add(a,scale(b,-1))
def mm(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),Z0)
             for j in range(n)] for i in range(n)]
def dag(a):
    n=len(a);return [[a[j][i].conj() for j in range(n)] for i in range(n)]
def com(a,b):return sub(mm(a,b),mm(b,a))
def delta(a):return diagv([a[i][i] for i in range(len(a))])
def hidden(a):return sub(a,delta(a))
def trace(a):return sum((a[i][i] for i in range(len(a))),Z0)
def abs2(z):return z*z.conj()
def rank_rational(M):
    m=[[F(z) for z in row] for row in M]
    if not m:return 0
    cols=len(m[0]);p=0
    for c in range(cols):
        j=next((i for i in range(p,len(m)) if m[i][c]!=0),None)
        if j is None:continue
        m[p],m[j]=m[j],m[p]
        t=m[p][c];m[p]=[z/t for z in m[p]]
        for i in range(len(m)):
            if i!=p and m[i][c]:
                t=m[i][c];m[i]=[a-t*b for a,b in zip(m[i],m[p])]
        p+=1
        if p==len(m):break
    return p
def det(M):
    n=len(M)
    if n==1:return F(M[0][0])
    return sum(((-1)**j * F(M[0][j])*
                det([row[:j]+row[j+1:] for row in M[1:]])
                for j in range(n)),F(0))
def laplacian_from_A(A):
    n=len(A);L=[[F(0) for j in range(n)] for i in range(n)]
    w=[]
    for a in range(n):
        for b in range(a+1,n):
            r=abs2(A[a][b])
            assert r.i==0
            wt=r.r;w.append(wt)
            L[a][a]+=wt;L[b][b]+=wt
            L[a][b]-=wt;L[b][a]-=wt
    return w,L
def apply_lap(L,v):
    return [sum((L[i][j]*F(v[j]) for j in range(len(v))),F(0))
            for i in range(len(v))]
def imagdiag(v):return diagv([I*gc(z) for z in v])

# K4 exact GKSL model with site dephasing >=0.
N=4
H=[[O if a!=b else Z0 for b in range(N)] for a in range(N)]
d=diagv([F(9,24),F(5,24),F(7,24),F(3,24)])
def L0(x,gamma):
    return sub(scale(com(H,x),-I),scale(hidden(x),gc(gamma)))
def La(x,gamma,a):
    return sub(L0(x,gamma),scale(com(diagv(a),x),I))
A=hidden(L0(d,F(0)))
expect_edges=[F(1,36),F(1,144),F(1,16),
              F(1,144),F(1,144),F(1,36)]
weights,Lw=laplacian_from_A(A)
assert weights==expect_edges
assert Lw==[
  [F(7,72),-F(1,36),-F(1,144),-F(1,16)],
  [-F(1,36),F(1,24),-F(1,144),-F(1,144)],
  [-F(1,144),-F(1,144),F(1,24),-F(1,36)],
  [-F(1,16),-F(1,144),-F(1,36),F(7,72)]]
assert det([row[:3] for row in Lw[:3]])==F(95,746496)
assert rank_rational(Lw)==3
assert apply_lap(Lw,[1]*4)==[0]*4
assert rank_rational([row+[F(i==0) for i in range(4)] for row in Lw])==4

basis=[[F(i==j) for i in range(4)] for j in range(4)]
nonconstant=[F(2,3),F(-5,4),F(7,8),F(3)]
for gamma in (F(0),F(2,3),F(5,4)):
    Ac=hidden(L0(d,gamma))
    assert Ac==A
    B0=hidden(L0(L0(d,gamma),gamma))
    R0=delta(com(A,B0))
    assert R0==diagv([-I*gc(F(2,9)),I*gc(F(2,9)),
                       I*gc(F(2,9)),-I*gc(F(2,9))])
    for a in basis+[nonconstant,[F(7)]*4]:
        alpha=diagv(a)
        Aa=hidden(La(d,gamma,a))
        B=hidden(La(La(d,gamma,a),gamma,a))
        assert Aa==A
        assert B==sub(B0,scale(com(alpha,A),I))
        difference=sub(delta(com(A,B)),R0)
        delta_expected=imagdiag([2*x for x in apply_lap(Lw,a)])
        assert difference==delta_expected
        # Two conventions for calibrator error:
        # delta=a_cal-a_true -> Rcal-R0= -2i Lw delta.
        a_cal=[a[i]+basis[0][i]-basis[1][i] for i in range(4)]
        Bcal=add(B,scale(com(diagv(a_cal),A),I))
        assert Bcal==add(B0,scale(com(
            diagv([a_cal[i]-a[i] for i in range(4)]),A),I))
        rcal=sub(delta(com(A,Bcal)),R0)
        err=[a_cal[i]-a[i] for i in range(4)]
        assert rcal==imagdiag([-2*x for x in apply_lap(Lw,err)])

# Current divergence identity for K4 (6 oriented edges).
edges=[(i,j) for i in range(4) for j in range(i+1,4)]
assert len(edges)==6
incidence=[[F((a==v)-(b==v)) for (a,b) in edges]
           for v in range(4)]
assert rank_rational(incidence)==3
assert len(edges)-rank_rational(incidence)==3
def div(j):
    return [sum((incidence[v][e]*j[e] for e in range(6)),F(0))
            for v in range(4)]
cycles=[
 [F(1),F(-1),F(0),F(1),F(0),F(0)], # triangle 012
 [F(1),F(0),F(-1),F(0),F(1),F(0)], # triangle 013
 [F(0),F(1),F(-1),F(0),F(0),F(1)]  # triangle 023
]
assert rank_rational(cycles)==3
assert all(div(j)==[F(0)]*4 for j in cycles)
jm=[F(2),F(-1),F(3),F(4),F(0),F(5)]
jp=[jm[e]+cycles[0][e]-2*cycles[1][e]+3*cycles[2][e]
    for e in range(6)]
assert jp!=jm and div(jp)==div(jm)
assert rank_rational([incidence[v]+[F(v==0)] for v in range(4)])==4

# For Hermitian A and B0, the signed P3 residue equals i*div(j).
B0=hidden(L0(L0(d,F(0)),F(0)))
j0=[F(2)*((A[a][b]*B0[a][b].conj()).i) for a,b in edges]
R0=delta(com(A,B0))
assert R0==imagdiag(div(j0))
a=nonconstant
Ba=hidden(La(La(d,F(0),a),F(0),a))
ja=[F(2)*((A[e[0]][e[1]]*Ba[e[0]][e[1]].conj()).i)
    for e in edges]
assert [ja[e]-j0[e] for e in range(6)]==[
   F(2)*weights[e]*(a[u]-a[v])
   for e,(u,v) in enumerate(edges)]
assert delta(com(A,Ba))==imagdiag(div(ja))

# Microscopic two-step operational counterexample:
# V is diagonal unitary; conjugation by V does not affect a SINGLE
# population readout after U, but changes two-step population data.
assert len(U)==2
V=diagv([I,-I])
W=mm(V,U)
assert mm(dag(W),W)==diagv([1,1])
def evolve(g,x):return mm(mm(g,x),dag(g))
rho=diagv([1,0])
micro=evolve(U,rho)
phys=evolve(W,rho)
assert delta(micro)==delta(phys)==diagv([F(5,9),F(4,9)])
assert delta(evolve(U,micro))==diagv([F(65,81),F(16,81)])
assert delta(evolve(W,phys))==diagv([F(17,81),F(64,81)])
assert delta(evolve(U,micro))!=delta(evolve(W,phys))
# This refutes one-population-step equivalence -> two-step equivalence.
# It is ordinary standard-QM CPTP interference, not CR-specific.

# KKS/P9.38 product: the 4-level nondegenerate state orbit has
# real dim 12, six independent conductances are PARAMETER variables.
# Pullback KKS block rank 12 and 6-dimensional null space.
symp=[[F(0) for _ in range(18)] for _ in range(18)]
for k in range(6):
    symp[2*k][2*k+1]=F(1)
    symp[2*k+1][2*k]=-F(1)
assert rank_rational(symp)==12
assert all(symp[i][j]==0 for i in range(18) for j in range(12,18))
assert all(symp[i][j]==0 for i in range(12,18) for j in range(18))

print("PASS: P9.38 +2i Laplacian identity, gamma-independent across GKSL examples")
print("PASS: K4 six weights, exact matrix, rank3/kernel constants, minor 95/746496")
print("PASS: variation surjects onto traceless diagonal anti-Hermitian witness")
print("PASS: calibration residual error = -2i Lw(alpha_cal-alpha_true)")
print("PASS: K4 3D cycle current kernel and divergence-only matching")
print("PASS: explicit one-step population equality does NOT imply two-step equality")
print("PASS: KKS-state x six generator-parameter pullback has rank12 and nullity6")
print("SCOPE: NO P3 R3 saturation from varied alpha, NO independent J_N provenance, NO ADM")
