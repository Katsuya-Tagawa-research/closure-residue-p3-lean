"""H54: exact conditional K4 spatial curvature-density first variation,
Palatini boundary-current identity and weight-to-metric Jacobian.

Assumes the EXTERNALLY PROVIDED H53 smooth 3D spatial chart and
physical solder. S3[w]=∫sqrt(g(w)) R3[g(w)] d^3x is the INTRINSIC
3D EH-like spatial-curvature functional, NOT the full 3+1 EH/ADM
gravitational action. The boundary divergence MUST be retained
except for compact-support variations or independently justified
boundary terms/conditions.

Proves by rational dual-number matrix jets:
 (δ(sqrt g R))/sqrt g = -G3^ij δg_ij + ∇_k V^k
 V^k=g^ij δGamma^k_ij-g^ki δGamma^j_ij .
K4 metric inverse derivative is exact in all 6 edge directions.
No sqrt computed: divide both sides by sqrt g and use
δ log sqrt g = (1/2)tr(g^-1δg).
"""
from fractions import Fraction as F
from P9H52K4DeWittKinematicsCurvatureExactCheck import (
    I,zeros,add,scale,mm,trans,trace,inv,det,rank,B,G,V,dg,
    flatten_symmetric,cov_metric
)
from P9H53K4SolderedSpatialCurvatureExactCheck import (
    metric_jets,levi_civita_curvature,w0,wi,wij,conformal_jets
)
n=3
f0=F(0)
def mat_minus(a,b):return add(a,scale(b,-1))
def mat_equal(a,b):return a==b
def inner(A,B):return sum((A[i][j]*B[i][j]
                           for i in range(3) for j in range(3)),F(0))
# Matrix dual numbers: (X, dX). All are EXACT Fraction arrays.
def Dadd(X,Y):return (add(X[0],Y[0]),add(X[1],Y[1]))
def Dneg(X):return (scale(X[0],-1),scale(X[1],-1))
def Dscale(X,c):return (scale(X[0],c),scale(X[1],c))
def Dmul(X,Y):
    return (mm(X[0],Y[0]),
            add(mm(X[1],Y[0]),mm(X[0],Y[1])))
def Dinv(X):
    i=inv(X[0])
    return (i,scale(mm(mm(i,X[1]),i),-1))
def Dprod(*parts):
    res=parts[0]
    for x in parts[1:]:res=Dmul(res,x)
    return res
def Dmat_const(X):return (X,zeros(len(X),len(X[0])))
def metric_weight_tangent(w0,wi,wij,u0,ui,uij):
    """Construct values AND exact epsilon derivs of (g,g_i,g_ij).

    Spatial and variation derivatives COMMUTE. All arrays are in the
    same physical spatial solder/frame (extra H53 hypothesis).
    """
    R=Dinv((B(w0),B(u0)))
    H=Dmat_const(G)
    fun=lambda W: (B(W[0]),B(W[1]))
    Bi=[fun((wi[i],ui[i])) for i in range(3)]
    Bij=[[fun((wij[i][j],uij[i][j])) for j in range(3)]
          for i in range(3)]
    def sandwich(X):return Dscale(Dprod(H,X,H),F(16))
    gd=sandwich(R)
    gid=[Dneg(sandwich(Dprod(R,X,R))) for X in Bi]
    gijd=[]
    for i in range(3):
        row=[]
        for j in range(3):
            Z=Dadd(Dprod(R,Bi[i],R,Bi[j],R),
                   Dprod(R,Bi[j],R,Bi[i],R))
            Z=Dadd(Z,Dneg(Dprod(R,Bij[i][j],R)))
            row.append(sandwich(Z))
        gijd.append(row)
    actual=metric_jets(w0,wi,wij)
    assert (gd[0],[x[0] for x in gid],
            [[x[0] for x in row] for row in gijd])==actual
    return (gd[0],[x[0] for x in gid],
            [[x[0] for x in row] for row in gijd],
            gd[1],[x[1] for x in gid],
            [[x[1] for x in row] for row in gijd])

# Scalar dual numbers (value, variation); exact rational Leibniz.
zero=(F(0),F(0))
def s(v):return (v,F(0))
def da(x,y):return (x[0]+y[0],x[1]+y[1])
def dn(x):return (-x[0],-x[1])
def ds(x,y):return da(x,dn(y))
def dm(x,y):return (x[0]*y[0],x[1]*y[0]+x[0]*y[1])
def dscale(x,c):return (x[0]*c,x[1]*c)
def dsum(xs):
    o=zero
    for x in xs:o=da(o,x)
    return o
def dmat(X,dX):
    return [[(X[i][j],dX[i][j])
             for j in range(len(X[0]))] for i in range(len(X))]
def dmm(X,Y):
    return [[dsum(dm(X[i][k],Y[k][j]) for k in range(len(Y)))
             for j in range(len(Y[0]))] for i in range(len(X))]
def ddot_tensor(X,Y):
    return dsum(dm(X[i][j],Y[i][j])
                for i in range(n) for j in range(n))

def palatini_audit(g,gi,gij,H,Hi,Hij):
    """FULL exact independent parameter first variation of R3.

    Uses dual-number Christoffels and their spatial derivatives
    to obtain δRic and δR, then independently constructs
    divergence of the standard Palatini boundary vector.
    """
    ginv=inv(g)
    dginv=scale(mm(mm(ginv,H),ginv),-1)
    J=dmat(ginv,dginv)
    gr=dmat(g,H)
    g1=[dmat(gi[m],Hi[m]) for m in range(n)]
    g2=[[dmat(gij[m][l],Hij[m][l])
         for l in range(n)] for m in range(n)]
    def C(i,j,l):
        return ds(da(g1[i][j][l],g1[j][i][l]),g1[l][i][j])
    DJ1=[[[dn(x) for x in row]
           for row in dmm(dmm(J,g1[m]),J)]
         for m in range(n)]
    Gam=[[[dscale(dsum(dm(J[k][l],C(i,j,l))
                         for l in range(n)),F(1,2))
           for j in range(n)] for i in range(n)]
         for k in range(n)]
    # spatial differential ∂m Γ^k_ij, also parameter-differentiated
    partial=[[[[dscale(dsum(da(
           dm(DJ1[m][k][l],C(i,j,l)),
           dm(J[k][l],ds(da(g2[m][i][j][l],
                             g2[m][j][i][l]),g2[m][l][i][j])))
              for l in range(n)),F(1,2))
            for j in range(n)] for i in range(n)] for k in range(n)]
         for m in range(n)]
    Ric=[[dsum(
         [ds(partial[k][k][i][j],partial[j][k][i][k])
          for k in range(n)]
         +[ds(dm(Gam[k][i][j],Gam[l][k][l]),
              dm(Gam[l][i][k],Gam[k][j][l]))
            for k in range(n) for l in range(n)])
         for j in range(n)] for i in range(n)]
    scalar=dsum(dm(J[i][j],Ric[i][j])
                for i in range(n) for j in range(n))
    R,deltaR=scalar
    assert [[a[0] for a in row] for row in Ric]==trans(
        [[a[0] for a in row] for row in Ric])
    directR,directRic,Ein,_=levi_civita_curvature(g,gi,gij)
    assert R==directR
    assert [[a[0] for a in row] for row in Ric]==directRic
    for m in range(n):
        for i in range(n):
            for j in range(n):
                assert Gam[i][m][j][0]==Gam[i][j][m][0]
    V=[sum((ginv[i][j]*Gam[k][i][j][1]
           -ginv[k][i]*Gam[j][i][j][1]
            for i in range(n) for j in range(n)),F(0))
       for k in range(n)]
    dV=[[sum((DJ1[m][i][j][0]*Gam[k][i][j][1]
            +ginv[i][j]*partial[m][k][i][j][1]
            -DJ1[m][k][i][0]*Gam[j][i][j][1]
            -ginv[k][i]*partial[m][j][i][j][1]
            for i in range(n) for j in range(n)),F(0))
          for k in range(n)] for m in range(n)]
    divV=sum((dV[k][k] for k in range(n)),F(0))
    divV+=sum((Gam[k][k][l][0]*V[l]
               for k in range(n) for l in range(n)),F(0))
    RicUp=mm(mm(ginv,directRic),ginv)
    EinUp=mm(mm(ginv,Ein),ginv)
    tr_gH=trace(mm(ginv,H))
    bulk=-inner(EinUp,H)
    density_delta=deltaR+R*tr_gH/2
    assert deltaR==-inner(RicUp,H)+divV, (
        "Palatini δR identity",deltaR,-inner(RicUp,H),divV)
    assert density_delta==bulk+divV, (
        "spatial EH δ density identity",density_delta,bulk,divV)
    assert trace(mm(ginv,Ein))==-R/2
    return {"R":R,"deltaR":deltaR,"bulk":bulk,"boundary_div":divV,
            "density_delta_normalized":density_delta,
            "H":H,"V":V,"Ein":Ein,"g":g}

# Generic anisotropic nonflat metric with arbitrary independent
# rational variations of 0/1/2-jet weights. Not only conformal.
variation0=[F(x,11) for x in (1,-1,2,1,3,-2)]
variation1=[[F((i+2)*(k%4-2),31)
             for k in range(6)] for i in range(n)]
variation2=[[[F((i+j+2)*(k-2),83)
              for k in range(6)] for j in range(n)] for i in range(n)]
g,gi,gij,H,Hi,Hij=metric_weight_tangent(
    w0,wi,wij,variation0,variation1,variation2)
ans=palatini_audit(g,gi,gij,H,Hi,Hij)
assert ans["R"]!=0 and ans["bulk"]!=0
assert ans["boundary_div"]!=0
assert ans["density_delta_normalized"]==ans["bulk"]+ans["boundary_div"]
# Independent six-way chain rule at fixed spatial point, holding
# g, Ric and Einstein fixed in the BULK coefficient:
# -G3^ij H_ij= sum_e C_e η_e,
# C_e=-G3^ij D_{w_e}g_ij.
ginv=inv(g)
EinUp=mm(mm(ginv,ans["Ein"]),ginv)
coeff=[-inner(EinUp,dg(w0,[F(int(k==e)) for k in range(6)]))
       for e in range(6)]
assert sum((coeff[e]*variation0[e] for e in range(6)),F(0))==ans["bulk"]
assert rank([[flatten_symmetric(dg(w0,
    [F(int(j==e)) for j in range(6)]))[i]
    for e in range(6)] for i in range(6)])==6

# Pointwise BULK Euler-Lagrange vanishing for all six weights is
# equivalent to the three-dimensional vacuum Einstein tensor zero
# because the K4 chart has six independent metric variations.
# Algebraic 3D trace forces R=0, hence Ric=0.
# This says nothing about 3+1 dynamics without lapse, shift,
# kinetic gravitational action, constraints and boundary data.
assert trace(mm(ginv,ans["Ein"]))==-ans["R"]/2

# Explicit boundary-divergence obstruction on flat background:
# w_e(x)=1+ε q(x), q=x^T G x. At x=0 all perturbed weights
# and their first spatial gradients agree with unperturbed,
# so metric variation H=0, first gradients Hi=0, yet its second
# spatial jet is nonzero and δ(sqrt g R) is all divergence.
wflat=[F(1)]*6
z6=[F(0)]*6
zerograd=[z6[:] for _ in range(n)]
zerohess=[[z6[:] for _ in range(n)] for _ in range(n)]
perturb2=[[[2*G[i][j]]*6 for j in range(n)]
          for i in range(n)]
fg,fgi,fgij,FH,FHi,FHij=metric_weight_tangent(
    wflat,zerograd,zerohess,z6,zerograd,perturb2)
flat=palatini_audit(fg,fgi,fgij,FH,FHi,FHij)
assert flat["R"]==0
assert FH==zeros(3,3)
assert all(t==zeros(3,3) for t in FHi)
assert flat["bulk"]==0
assert flat["boundary_div"]==F(3)
assert flat["density_delta_normalized"]==F(3)
# The spatial divergence cannot be dropped POINTWISE merely
# because δg vanishes at the selected point.

# Also audit K4 curvature Einstein tensor for c=1 externally
# specified smooth positive weight field w=1-c x^T G x at origin.
c=F(1)
wg=[F(1)]*6
wgrad=[[F(0)]*6 for _ in range(n)]
whess=[[[-2*c*G[i][j]]*6 for j in range(n)]
       for i in range(n)]
gg,ggi,ggij,Hc,Hci,Hcij=metric_weight_tangent(
    wg,wgrad,whess,variation0,variation1,variation2)
curved=palatini_audit(gg,ggi,ggij,Hc,Hci,Hcij)
assert curved["R"]==-F(3)
assert curved["Ein"]==scale(G,F(2))
assert curved["bulk"]!=0
# Positive regularity of the open cell domain, not global
# surjectivity onto every SPD metric. The exact uniform chart
# yields first-variation coefficient sum 3c/2.
EcUp=mm(mm(inv(gg),curved["Ein"]),inv(gg))
Cs=[-inner(EcUp,dg(wg,[F(int(k==e)) for k in range(6)]))
    for e in range(6)]
assert sum(Cs,F(0))==F(3,2)

print("PASS H54: exact K4 weight-to-spatial-metric second-jet variations and six independent edge differentials")
print("PASS H54: full rational first variation of R3 equals -Ric^ij H_ij plus covariant Palatini divergence")
print("PASS H54: δ(sqrt g R3)/sqrt g = -G3^ij H_ij + ∇_k V^k, for nontrivial anisotropic jets")
print("PASS H54: signed K4 edge Euler bulk coefficient is six-component invertible DeWitt-admissible metric chain")
print("PASS H54: pure spatial S3 weight-vacuum stationarity implies Ric3=0 (NOT 3+1 Einstein)")
print("PASS H54: H=0 at a point while boundary-divergence δR3=3, forbidding a pointwise boundary deletion")
print("PASS H54: exact curved conformal origin R3=-3 and Einstein3=2G, weight-coefficient sum3/2")
print("SCOPE: 3D base/solder, smooth positive weight field, boundary/compact-support conditions independently added")
print("SCOPE: NO independent origin of EH/ADM 4D action, lapse-shift, matter, HDA, Einstein equations or CR-only signal")
