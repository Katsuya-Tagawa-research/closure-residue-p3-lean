"""H98: DeWitt lambda is NOT sourced by positive K4 spatial response.

(EXACT conditional) actual H75 positive flag data + INDEPENDENT H85
K4 edge selector admits exact nonlinear positive-metric chart and
canonical COTANGENT LIFT, but six p_w are EXTRA physical assumptions.

(EXACT ADM COMPARATOR) lambda-family kinetic signature switches at 1/3.
Under separately imported 3D canonical field Poisson brackets and
-R scalar curvature, the flat-but-nonuniform off-shell H-H anomaly is
2(1-2lambda) int (N dM-M dN) d(trace pi), hence zero for arbitrary
test data only lambda=1/2. A rational compact-interval witness shows
this WITHOUT a homogeneous minisuperspace shortcut.
No micro-derived ADM kinetic, actual sourced HDA or Einstein dynamics.
"""
from fractions import Fraction as F

import P9H85A4EdgeSourceSelectionExactCheck as H85
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P9H96FiniteGKSLDeWittProvenanceExactCheck as H96
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,gc
from P9H75SemicausalMicroMemorySourceExactCheck import R60

assert R60[0][0]==I*gc(F(-32,135))
assert H85.r==(F(0),F(16,25),F(16,25),F(4,25))
assert H85.wa==(4,4,1,8,5,5)
assert sum(H85.wa)==27 and all(v>0 for v in H85.wa)
assert len(H85.edges)==6
print("PASS H98.1: same genuine H75 positive flag outputs and original signed P3 residue, with declared A4/K4 additive spatial selector")

mm=H85.matmul
tr=H85.transpose
inv=H85.inv
B=H85.B
G0=mm(tr(B),B)

def sub(A,B):
    return [[u-v for u,v in zip(ra,rb)] for ra,rb in zip(A,B)]

def mat_scale(A,s):
    return [[s*v for v in row] for row in A]

def metric_chart(w):
    C=mm(mm(tr(B),H85.Lmatrix(w)),B)
    Ci=inv(C)
    return mat_scale(mm(mm(G0,Ci),G0),F(16))

def symvec(A):
    return [A[0][0],A[1][1],A[2][2],A[0][1],A[0][2],A[1][2]]

def jacobian(w):
    C=mm(mm(tr(B),H85.Lmatrix(w)),B)
    Ci=inv(C)
    columns=[]
    for k in range(6):
        dw=tuple(F(int(i==k)) for i in range(6))
        dC=mm(mm(tr(B),H85.Lmatrix(dw)),B)
        derivative=mat_scale(mm(mm(mm(mm(G0,Ci),dC),Ci),G0),F(-16))
        columns.append(symvec(derivative))
    return [list(row) for row in zip(*columns)]

def determinant(A):
    X=[[F(z) for z in row] for row in A]
    size=len(X);res=F(1)
    for j in range(size):
        k=next((k for k in range(j,size) if X[k][j]),None)
        if k is None:return F(0)
        if k!=j:X[j],X[k]=X[k],X[j];res=-res
        d=X[j][j]
        res*=d
        for k in range(j+1,size):
            z=X[k][j]/d
            if z:
                for s in range(j,size):X[k][s]-=z*X[j][s]
    return res

w=H85.wa
g=metric_chart(w)
assert mm(mm(tr(B),H85.ga),B)==g
assert g==[
    [F(144,49),F(64,49),F(64,49)],
    [F(64,49),F(2192,1225),F(1408,1225)],
    [F(64,49),F(1408,1225),F(2192,1225)]
]
assert all(v>0 for v in (g[0][0],determinant([row[:2] for row in g[:2]]),determinant(g)))
A=jacobian(w)
assert H91.rank(A)==6
assert determinant(A)==F(-16777216,2251875390625)
# The w -> C(w) map is linear, six-dimensional and invertible
# on Sym3; matrix inversion/congruence preserves nondegenerate
# differential on the open strictly-positive weight region.
Cmatrix=[
  symvec(mm(mm(tr(B),H85.Lmatrix(tuple(F(int(i==k)) for i in range(6)))),B))
  for k in range(6)
]
assert H91.rank(Cmatrix)==6
print("PASS H98.1: exact source-selected K4 positive metric g(w)=16 G0 (B^T L B)^-1 G0, det(dg/dw)=-16777216/2251875390625")

# Explicit canonical cotangent lift: if z=z(w) and J=dz/dw,
# p_z=(J^T)^-1 p_w, so p_w dw = p_z dz. (The independent p_w
# variables are NOT actual physical H75 momentum observables.)
Ai=inv(A)
ATinv=tr(Ai)
for k in range(6):
    p_w=[F(int(i==k)) for i in range(6)]
    p_z=[sum((ATinv[i][j]*p_w[j] for j in range(6)),F(0))
         for i in range(6)]
    recovered=[sum((A[i][j]*p_z[i] for i in range(6)),F(0))
               for j in range(6)]
    assert recovered==p_w
    # {z_a,p_z_b}_{w,pw} = sum_i J_ai (J^-T)_bi
    for a in range(6):
        for b in range(6):
            lhs=sum((A[a][i]*ATinv[b][i] for i in range(6)),F(0))
            assert lhs==F(int(a==b))
print("PASS H98.1: exact K4 nonlinear positive-metric 6+6 cotangent lift preserves canonical one-form / Poisson brackets CONDITIONAL on independently supplied momenta")

def Dl(lam):
    lam=F(lam)
    D=[[F(0) for j in range(6)] for i in range(6)]
    for i in range(3):
        for j in range(3):
            D[i][j]=F(int(i==j))-lam
    for i in range(3,6):D[i][i]=F(2)
    return D

for lam in (F(0),F(1,3),F(1,2),F(2,3)):
    D=Dl(lam)
    vals=(F(1),F(1),1-3*lam,F(2),F(2),F(2))
    assert determinant(D)==F(8)*(1-3*lam)
    for v,eigen in H96.basis:
        # Same DeWitt eigenvectors hold for every lambda; trace
        # vector has eigenvalue 1-3lambda.
        target=(1-3*lam if eigen==F(-1,2) else eigen)
        out=[sum((D[i][j]*v[j] for j in range(6)),F(0)) for i in range(6)]
        assert out==[target*z for z in v]
    assert vals[2]>0 if lam<F(1,3) else (vals[2]==0 if lam==F(1,3) else vals[2]<0)
assert Dl(F(1,2))==H96.D
assert determinant(Dl(F(1,2)))==F(-4)
print("PASS H98.2: lambda-Hessian eigenvalues {1,1,1-3lambda,2,2,2}; same positive K4 source chart can accompany positive lambda=0 or indefinite ADM lambda=1/2 kinetic")

# Positive metric & legitimate symmetric momentum covariance:
# at actual source-derived conditional positive K4 metric g(w),
# pi^ij=a*g^{-1,ij} is conformal. Its kinetic NUMERATOR is
# (3-9lambda)a² regardless of the source-provided positive metric.
ginv=inv(g)
assert mm(g,ginv)==[[F(int(i==j)) for j in range(3)] for i in range(3)]
def kinetic_num(lam,pi):
    term=sum((pi[i][j]*pi[k][l]*g[i][k]*g[j][l]
              for i in range(3) for j in range(3)
              for k in range(3) for l in range(3)),F(0))
    gp=sum((g[i][j]*pi[i][j] for i in range(3) for j in range(3)),F(0))
    return term-F(lam)*gp*gp
assert kinetic_num(F(0),ginv)==3
assert kinetic_num(F(1,2),ginv)==F(-3,2)
# Positive example: genuine traceless nonzero pi created by removing
# its g-trace from a real diagonal tensor.
P=[[F(int(i==j and i==0)) for j in range(3)] for i in range(3)]
trace_gp=sum((g[i][j]*P[i][j] for i in range(3) for j in range(3)),F(0))
Ptr=[[P[i][j]-trace_gp/F(3)*ginv[i][j]
      for j in range(3)] for i in range(3)]
assert sum((g[i][j]*Ptr[i][j] for i in range(3) for j in range(3)),F(0))==0
assert Ptr!=[[F(0)]*3 for _ in range(3)]
assert kinetic_num(F(0),Ptr)==kinetic_num(F(1,2),Ptr)>0
print("PASS H98.2: at SAME H75-flag-derived positive K4 source metric, pure conformal momentum is positive for lambda0 but negative for ADM lambda1/2, traceless directions stay positive")

# All-Fraction polynomial algebra for nonuniform 1D section of a
# STANDARD EXTERNALLY ASSUMED 3D ADM field theory at g=I.
# Lapse N,M and trace momentum f both vanish at boundaries.
def trim(v):
    a=list(v)
    while a and a[-1]==0:a.pop()
    return tuple(a)

def padd(a,b):
    return trim([(a[k] if k<len(a) else F(0))+
                 (b[k] if k<len(b) else F(0))
                 for k in range(max(len(a),len(b)))])

def pscale(a,c):
    return trim([F(c)*v for v in a])

def psub(a,b):
    return padd(a,pscale(b,-1))

def pmul(a,b):
    x=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w0 in enumerate(b):x[i+j]+=v*w0
    return trim(x)

def derivative(a):
    return trim([F(k)*a[k] for k in range(1,len(a))])

def integrate01(a):
    return sum((v/F(k+1) for k,v in enumerate(a)),F(0))

N=(F(0),F(1),F(-1))       # x(1-x)
M=(F(0),F(0),F(1),F(-1)) # x²(1-x)
f=M                         # isotropic pi_ij=f delta_ij
wedge=psub(pmul(N,derivative(M)),pmul(M,derivative(N)))
assert wedge==(F(0),F(0),F(1),F(-2),F(1))  # x² (1-x)²
c=integrate01(pmul(derivative(f),wedge))
assert c==F(1,210)
# The momentum constraint at g=I is H_i=-2∂jπ^ij = -2f'δ_i^x
momentum=-2*c
assert momentum==F(-1,105)

def bracket_direct(lam):
    # At g_ij=delta_ij, the 3D cross functional derivative yields
    # 2 int f*(1+3(2lambda-1))*(N M'' - M N'').
    pref=F(2)*(F(1)+F(3)*(2*F(lam)-F(1)))
    cross=psub(pmul(N,derivative(derivative(M))),
               pmul(M,derivative(derivative(N))))
    return pref*integrate01(pmul(f,cross))

def bracket_constraint(lam):
    # Independently integrated by parts H-H = D + anomaly.
    return momentum+F(2)*(1-F(2)*F(lam))*F(3)*c

for lam in (F(0),F(1,3),F(1,2),F(2,3)):
    lhs=bracket_direct(lam)
    rhs=bracket_constraint(lam)
    assert lhs==rhs
    assert lhs==(F(2)-F(6)*lam)/F(105)
    assert lhs-momentum==(F(1)-F(2)*lam)/F(35)

assert bracket_direct(F(0))==F(2,105)
assert bracket_direct(F(1,2))==F(-1,105)
assert bracket_direct(F(1,2))==momentum
assert bracket_direct(F(0))!=momentum
print("PASS H98.3: EXACT nonuniform flat-off-shell 3D ADM H-H lambda anomaly from independent polynomial second-derivative and integration-by-parts routes, rational witness int f' wedge=1/210")
print("PASS H98.3: undeformed standard momentum constraint requires lambda=1/2 for arbitrary lapse/momentum; explicit lambda0 bracket 2/105 vs momentum -1/105")

print("BOUNDARY: ADM canonical field Poisson brackets, curvature -sqrt(g)R, momentum constraint and externally introduced edge momenta are ASSUMED comparison physics, NOT original H75/P3/F source consequences")
print("BOUNDARY: g=I off-shell H-H is a necessary nonuniform gate, NOT complete arbitrary-metric HDA or actual Einstein equations")
print("BOUNDARY: DeWitt lambda selection under standard ADM assumptions is NOT derivation of standard ADM/Einstein from CR; G3 physical cotangent source, G4 Hamiltonian provenance, G5/G6 full HDA/Einstein OPEN")
