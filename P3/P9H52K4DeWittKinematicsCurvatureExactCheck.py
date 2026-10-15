"""H52: P9 K4 finite response metric -> exact DeWitt (5+,1-)
ADM-KINEMATIC pullback; explicit local-to-curvature non-implication.

This is finite 3D spatial SPD geometry, NOT a 1+3 Lorentzian
spacetime/Einstein action. Needs external continuum base,
soldering, lapse/shift, spatial derivatives, dynamical variation,
ADM/HDA etc. No physical P3/P6 source provenance is inferred.

We use the NON-orthonormal basis f_i=e_i-e_3 of S=1^perp.
Its Gram G=T^T T != I. The correct COVARIANT metric matrix is
g_w = 16 G B_w^-1 G, B_w=sum w_ab v_ab v_ab^T,
v_ab=T^T(e_a-e_b). This convention gives g_star=4G.

Exact rational Fraction calculations only, standard Python.
"""
from fractions import Fraction as F
from itertools import combinations

n=3
I=lambda n:[[F(int(i==j)) for j in range(n)] for i in range(n)]
def zeros(r,c):return [[F(0) for _ in range(c)] for _ in range(r)]
def add(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(A,s):return [[s*v for v in row] for row in A]
def mm(A,B):
    assert len(A[0])==len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def trans(A):return [list(row) for row in zip(*A)]
def trace(A):return sum((A[i][i] for i in range(len(A))),F(0))
def det(A):
    m=[row[:] for row in A]
    n=len(m)
    assert all(len(row)==n for row in m)
    d=F(1)
    for j in range(n):
        k=next((k for k in range(j,n) if m[k][j]),None)
        if k is None:return F(0)
        if k!=j:
            m[j],m[k]=m[k],m[j];d=-d
        piv=m[j][j];d*=piv
        for i in range(j+1,n):
            fac=m[i][j]/piv
            for v in range(j,n):m[i][v]-=fac*m[j][v]
    return d
def inv(A):
    n=len(A)
    m=[list(A[i])+I(n)[i] for i in range(n)]
    for j in range(n):
        p=next((p for p in range(j,n) if m[p][j]),None)
        assert p is not None,"singular"
        m[j],m[p]=m[p],m[j]
        pivot=m[j][j]
        m[j]=[t/pivot for t in m[j]]
        for k in range(n):
            if k!=j and m[k][j]!=0:
                c=m[k][j]
                m[k]=[a-c*b for a,b in zip(m[k],m[j])]
    return [row[n:] for row in m]
def rank(A):
    M=[list(row) for row in A]
    if not M:return 0
    nr=len(M);nc=len(M[0]);r=0
    for j in range(nc):
        pivot=next((i for i in range(r,nr) if M[i][j]),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r]
        t=M[r][j]
        M[r]=[u/t for u in M[r]]
        for i in range(nr):
            if i!=r and M[i][j]:
                t=M[i][j]
                M[i]=[u-t*v for u,v in zip(M[i],M[r])]
        r+=1
        if r==nr:break
    return r
def same(A,B):return A==B
def ddot(v,w):return sum((a*b for a,b in zip(v,w)),F(0))
def outer(v,w):return [[a*b for b in w] for a in v]
T=[
 [F(1),F(0),F(0)],
 [F(0),F(1),F(0)],
 [F(0),F(0),F(1)],
 [F(-1),F(-1),F(-1)]
]
G=mm(trans(T),T)
assert G==[[F(2),F(1),F(1)],
           [F(1),F(2),F(1)],
           [F(1),F(1),F(2)]]
assert det(G)==4
edges=list(combinations(range(4),2))
assert edges==[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
e4=I(4)
v=[ [sum((T[a][i]*(e4[a][u]-e4[a][w])
                  for a in range(4)),F(0)) for i in range(3)]
     for u,w in edges]
V=[outer(vi,vi) for vi in v]
def flatten_symmetric(M):
    return [M[0][0],M[1][1],M[2][2],
            M[0][1],M[0][2],M[1][2]]
B6=[[flatten_symmetric(V[j])[i] for j in range(6)] for i in range(6)]
assert B6==[
 [1,1,4,0,1,1],
 [1,0,1,1,4,1],
 [0,1,1,1,1,4],
 [-1,0,2,0,2,1],
 [0,-1,2,0,1,2],
 [0,0,1,-1,2,2]
]
assert det(B6)==-256 and rank(B6)==6
def B(w):
    assert len(w)==6
    result=zeros(3,3)
    for a,R in zip(w,V):result=add(result,scale(R,a))
    return result
def cov_metric(w):
    Bw=B(w)
    return scale(mm(mm(G,inv(Bw)),G),F(16))
def positive_definite(M):
    return all(det([row[:k] for row in M[:k]])>0
               for k in (1,2,3))
w_star=(F(1),)*6
Bstar=B(w_star)
gstar=cov_metric(w_star)
assert Bstar==scale(G,F(4))
assert gstar==scale(G,F(4))
assert positive_definite(Bstar) and positive_definite(gstar)
# Change from non-orthonormal edge-coordinate columns f_i to
# Euclidean-orthonormal S frame leaves signature invariant.
# General metric derivative (fixed frame G):
# Dg[dw]=-16 G B^-1 (sum dw_e V_e) B^-1 G.
def dg(w,dw):
    Bi=inv(B(w))
    return scale(mm(mm(mm(mm(G,Bi),B(dw)),Bi),G),F(-16))
for j in range(6):
    dw=[F(0)]*6;dw[j]=F(1)
    assert dg(w_star,dw)==scale(V[j],F(-1))
assert rank([[flatten_symmetric(dg(w_star,[F(int(j==k))
           for k in range(6)]))[i] for j in range(6)]
           for i in range(6)])==6
# Exact differential inverse check B(w)=16 G g(w)^-1 G.
for w in ((F(1),)*6,
          (F(2),F(1),F(3),F(1),F(2),F(1)),
          (F(3,5),F(4,5),F(6,5),F(1),F(9,10),F(11,10))):
    gw=cov_metric(w)
    assert positive_definite(B(w)) and positive_definite(gw)
    assert scale(mm(mm(G,inv(gw)),G),F(16))==B(w)
    for k in range(6):
        dw=[F(int(i==k)) for i in range(6)]
        # finite-difference differential and exact identity
        eps=F(1,1000000)
        wp=tuple(w[i]+eps*dw[i] for i in range(6))
        delta=scale(add(cov_metric(wp),scale(gw,-1)),F(1)/eps)
        analytic=dg(w,dw)
        # Matrix inverse is differentiable: finite difference tends
        # to analytic, but DO NOT assert finite step equals derivative.
        assert max(abs(delta[i][j]-analytic[i][j])
                   for i in range(3) for j in range(3))<F(1,100)
# A strict proper cone: positive edge weights are sufficient to
# make SPD, but NOT every SPD inverse metric arises from all w>0.
wneg=(F(-1,10),F(1),F(1),F(1),F(1),F(1))
Bneg=B(wneg)
gneg=cov_metric(wneg)
assert positive_definite(Bneg) and positive_definite(gneg)
assert Bneg==[
 [F(69,10),F(51,10),F(4)],
 [F(51,10),F(69,10),F(4)],
 [F(4),F(4),F(8)]
]
assert gneg==[
 [F(94,9),F(14,9),F(4)],
 [F(14,9),F(94,9),F(4)],
 [F(4),F(4),F(8)]
]
assert det(Bneg)==F(576,5)
assert det(gneg)==F(5120,9)
# Unique inverse linear w(B) means wneg cannot be relabeled as
# another strictly positive edge assignment for same metric.

def dewitt(g,H,K):
    ginv=inv(g)
    return (trace(mm(mm(mm(ginv,H),ginv),K))
            -trace(mm(ginv,H))*trace(mm(ginv,K)))
# Pull back the n=3 DeWitt / ADM kinetic quadratic form:
# tr(g^-1 H g^-1 K)-tr(g^-1 H)tr(g^-1 K).
Dbasis=[]
for k in range(6):
    e=[F(int(i==k)) for i in range(6)]
    Dbasis.append(dg(w_star,e))
DW=[[dewitt(gstar,Dxx,Dyy) for Dyy in Dbasis]
    for Dxx in Dbasis]
assert DW==[
 [F(0),F(-3,16),F(-3,16),F(-3,16),F(-3,16),F(-1,4)],
 [F(-3,16),F(0),F(-3,16),F(-3,16),F(-1,4),F(-3,16)],
 [F(-3,16),F(-3,16),F(0),F(-1,4),F(-3,16),F(-3,16)],
 [F(-3,16),F(-3,16),F(-1,4),F(0),F(-3,16),F(-3,16)],
 [F(-3,16),F(-1,4),F(-3,16),F(-3,16),F(0),F(-3,16)],
 [F(-1,4),F(-3,16),F(-3,16),F(-3,16),F(0),F(-3,16)]
]
assert det(DW)==F(-1,4096)
# Exact eigenvalue multiplicities via the rational null-space ranks,
# after noting DW is REAL SYMMETRIC and hence diagonalizable:
# lambda -1 (mult1), 1/8 (mult2), 1/4 (mult3).
for eig,multiplicity in ((F(-1),1),(F(1,8),2),(F(1,4),3)):
    assert 6-rank(add(DW,scale(I(6),-eig)))==multiplicity
assert dewitt(gstar,scale(gstar,F(1)),scale(gstar,F(1)))==F(-6)
# A trace-free example: dw(01)=+1, dw(23)=-1.
dwtrace=[F(0)]*6
dwtrace[0]=F(1);dwtrace[5]=F(-1)
Haniso=dg(w_star,dwtrace)
assert trace(mm(inv(gstar),Haniso))==F(0)
assert dewitt(gstar,Haniso,Haniso)==F(1,2)
# ADM physical interpretation needs a separately CHOSEN lapse and
# shift, spacetime foliation and spatial derivative structure.
# For spatially UNIFORM positive weight w(t), the metric in an
# Euclidean-orthonormal S-frame is g_ij(t)=4/w(t)*delta_ij.
# With zero shift and prescribed lapse N(t)>0, K_ij=dot g_ij/(2N)
# and L_kin=N sqrt(det g)(K_ij K^ij-K^2)
#           = -12 * dot w²/(N*w^(7/2)).
# Only CHECK rational w where w^(1/2) is rational, e.g. w=1,4,9.
def iso_kin(w,wdot,N):
    scaleg=F(4)/w
    # volume = (2/sqrt(w))^3, rational on selected squares
    sqrts={F(1):F(1),F(4):F(2),F(9):F(3)}
    sw=sqrts[w]
    volume=F(8)/(sw**3)
    g=scale(I(3),scaleg)
    dotg=scale(I(3),-F(4)*wdot/w**2)
    direct=volume/(F(4)*N)*dewitt(g,dotg,dotg)
    analytic=-F(12)*wdot**2/(N*(sw**7))
    assert direct==analytic
    return direct
assert iso_kin(F(1),F(2),F(1))==F(-48)
assert iso_kin(F(4),F(1),F(2))==F(-3,64)
assert iso_kin(F(9),F(3),F(2))==F(-2,243)

# Local-to-curvature NO-GO: smooth K4 positive weight fields on
# 3D Euclidean base, w_ab(x)=exp(-c |x|²) for ALL six edges.
# In an orthonormal frame of S, g_ij(x)=4 exp(c|x|²)delta_ij.
# For all c, at x=0: w=1, g=4I, first spatial derivatives 0.
# The SECOND spatial derivatives vary as 8c delta_ij delta_kl.
# R(0) from metric jets at point (where dg=0):
# R= g^ik g^jl (partial_i partial_j g_kl
#                - partial_i partial_k g_jl).
# For conformal 3D metric directly R(0)=-3c.
def scalar_curvature_center(c):
    gij_inv=scale(I(3),F(1,4))
    def d2g(i,j,k,l):
        # second derivative in x_i,x_j of spatial g_kl
        return F(8)*c*F(int(i==j))*F(int(k==l))
    total=F(0)
    # R at zero for no first derivatives:
    # sum_{i,j}(partial_i partial_j g_ij
    #        - partial_i partial_i g_jj)/16.
    for i in range(3):
        for j in range(3):
            total+=F(1,16)*(d2g(i,j,i,j)-d2g(i,i,j,j))
    return total
for c in (F(-2),F(0),F(1),F(3,2)):
    assert scalar_curvature_center(c)==-3*c
assert scalar_curvature_center(F(0))==F(0)
assert scalar_curvature_center(F(1))==F(-3)
# Thus the very SAME finite K4 cell value, same first spatial jet
# and SAME DeWitt kinetic form can arise from smooth positive
# weight fields with different spatial scalar curvature. No R,
# EH action, HDA bracket or Einstein dynamics follows from the
# pointwise K4 metric/kinetic structure ALONE.

print("PASS H52: K4 six edge weights -> symmetric 3x3 inverse metric rank6 and det -256")
print("PASS H52: correct nonorthonormal S-frame g=16 G B^-1 G and uniform g*=4G=P7 h")
print("PASS H52: local diffeomorphism onto proper open subcone of SPD3, signed-edge SPD witness")
print("PASS H52: exact metric derivative and invertible tangent map")
print("PASS H52: pulled-back DeWitt metric eigenvalues -1, (1/8)x2, (1/4)x3: 5 positive, 1 negative")
print("PASS H52: exact prescribed-lapse homogeneous ADM kinetic minisuperspace identity")
print("PASS H52: smooth positive K4 weight fields equal at first jet but scalar R(0)=-3c differs")
print("SCOPE: ADM kinetic compatibility CONDITIONAL on external lapse/foliation; not Einstein dynamics")
print("SCOPE: 3D supermetric negative conformal mode is NOT spacetime Lorentz signature")
print("SCOPE: CR physical provenance, 4D soldering, EH potential and ADM/HDA remain OPEN")
