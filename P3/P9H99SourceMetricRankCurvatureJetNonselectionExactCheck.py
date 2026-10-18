"""H99: original-source H75 -> normalized H85 K4 config rank3 and exact
two-source-positive-field scalar-curvature 2-jet nonselection at one point.

EXACT Gaussian-rational source probabilities and matrix calculation;
K4 spatial solder, source profile x, and ADM 3D field interpretation
are extra declared physical/geometric premises, NOT P3/F-generated
spatial interactions, canonical momenta, curvature dynamics or Einstein.
"""
from fractions import Fraction as F
from itertools import combinations

import P9H85A4EdgeSourceSelectionExactCheck as H85
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P9H98DeWittLambdaFlatHDASourceSelectorExactCheck as H98
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,gc
from P9H75SemicausalMicroMemorySourceExactCheck import R60

assert R60[0][0]==I*gc(F(-32,135))
assert H85.r==(F(0),F(16,25),F(16,25),F(4,25))
assert H85.wa==(4,4,1,8,5,5)
assert len(H85.edges)==6
assert H85.W==27
r0=tuple(H85.r)
S=sum(r0)
w0=H85.wa
assert S==F(36,25)

# H98 studied the FULL abstract six-variable metric map w -> g.
# But H85 actually SELECTS its weights via 4 sourced probabilities
# r, a scale-invariant positive-total normalized endpoint rule.
def selector(rr):
    return H85.additive(rr)

def jac_r(rr):
    total=sum(rr)
    assert total>0
    return [
        [H85.W/(3*total)*
         (F(int(k==i)+int(k==j))-F(rr[i]+rr[j])/total)
         for k in range(4)]
        for i,j in H85.edges
    ]
J=jac_r(r0)
assert len(J)==6 and all(len(row)==4 for row in J)
assert H91.rank(J)==3
assert [sum((J[e][k]*r0[k] for k in range(4)),F(0))
        for e in range(6)]==[F(0)]*6
end_inc=[[F(int(k==i)+int(k==j)) for k in range(4)]
         for i,j in H85.edges]
assert H91.rank(end_inc)==4
assert selector(r0)==w0
# Mathematically strongest way to state the 3 affine constraints:
# all three disjoint edge-pairs add to the same W/3, an exact constant.
for rr in (r0,(F(1,10),F(1,2),F(3,5),F(1,4))):
    ww=selector(rr)
    assert sum(ww)==H85.W
    assert ww[0]+ww[5]==ww[1]+ww[4]==ww[2]+ww[3]==H85.W/3
print("PASS H99.1: original H75 four flag probabilities -> H85 normalized K4 selector has exact 6x4 Jacobian rank3, sole scale kernel, THREE complementary edge-pair affine invariants")

# The 6x6 derivative of the FULL mathematical metric map is
# invertible, while the composite measured-source selection only
# spans three independent SPD3 configuration directions.
Ag=H98.jacobian(w0)
assert H91.rank(Ag)==6
composite=H85.matmul(Ag,J)
assert H91.rank(composite)==3
assert H98.determinant(Ag)==F(-16777216,2251875390625)
print("PASS H99.1: even though abstract w->SPD3 has rank6, the actually declared positive-source r->w->g tangent map has rank3, NOT ADM's six independent metric components")

mm=H85.matmul
tr=H85.transpose
inv=H85.inv
B=H85.B
G=H98.G0
g0=H98.metric_chart(w0)
assert g0==H98.g
assert H98.determinant(g0)==F(4096,1225)
assert H98.determinant(g0)>0
ginv=inv(g0)
assert mm(g0,ginv)==[[F(int(i==j)) for j in range(3)] for i in range(3)]

# Spatial profiles are externally labeled, but EVERY point's readout
# is implemented by a true positive original H75 qutrit preparation.
# For s(x)=x^T g0 x within [0,1], alpha = 0 or 1/5.
v=(F(0),F(-1),F(0),F(1))
alpha=F(1,5)
def profile(a,s):
    return tuple(r0[k]+a*s*v[k] for k in range(4))
def physical_r_preps(rr):
    preps=[]
    for i,val in enumerate(rr):
        assert 0<=val<=F(16,25)
        if i==0:rho=H85.d0
        elif i==2:rho=H85.d2
        else:
            q=F(25,16)*val
            assert 0<=q<=1
            rho=H85.matadd(H85.matscale(H85.d0,1-q),
                           H85.matscale(H85.d1,q))
        preps.append(rho)
    return preps

for a in (F(0),alpha):
    for s in (F(0),F(1,3),F(1,2),F(1)):
        rr=profile(a,s)
        assert rr[0]==0 and rr[2]==F(16,25)
        assert F(11,25)<=rr[1]<=F(16,25)
        assert F(4,25)<=rr[3]<=F(9,25)
        preps=physical_r_preps(rr)
        assert tuple(H85.flag1(rho) for rho in preps)==rr
        ww=selector(rr)
        assert sum(ww)==27 and all(we>0 for we in ww)
        assert ww[0]+ww[5]==ww[1]+ww[4]==ww[2]+ww[3]==9
        gm=H98.metric_chart(ww)
        assert H98.determinant(gm)>0
        assert gm[0][0]>0
        assert H98.determinant([row[:2] for row in gm[:2]])>0
    assert profile(a,0)==r0

# All endpoint values valid => all profiles on 0<=s<=1 valid:
# r1(s)=16/25-alpha*s, r3(s)=4/25+alpha*s are affine
# in s and positive; other sites are constant positive preparations.
assert profile(alpha,1)==(F(0),F(11,25),F(16,25),F(9,25))
assert profile(F(0),1)==r0
assert physical_r_preps(r0)[3]==H85.rho3
print("PASS H99.2: two smooth pointwise original-H75 CPTP-POSITIVE qutrit preparation/readout fields on 0<=x^T g*x<=1 keep fixed K4 budget W=27 and ALL strictly positive weights")

# Because sum(r) remains constant for BOTH profiles, the source-
# selected weights are AFFINE in the externally specified scalar
# spatial profile t=a*s(x), with exact d=d w/dt.
dw=tuple(F(25,4)*(v[i]+v[j]) for i,j in H85.edges)
assert dw==(F(-25,4),F(0),F(25,4),F(-25,4),F(0),F(25,4))
assert sum(dw)==0
for a in (F(0),alpha):
    for s in (F(0),F(1,2),F(1)):
        ww=selector(profile(a,s))
        assert ww==tuple(w0[e]+a*s*dw[e] for e in range(6))
# The first spatial derivatives of s(x)=x^T g0 x vanish at
# x=0. Thus both fields have IDENTICAL 0-jets and 1-jets
# of actual H75 readouts, conditional K4 edges and spatial g.
print("PASS H99.2: both source-positive fields have identical central r, w, g and first spatial jets (all zero), with distinct second spatial jets")

# Exact curvature computed by TWO mathematically independent routes:
#  (1) determinant/log-variation trace of C=B^T L B
#  (2) direct full Levi-Civita scalar contraction of second
#      metric derivatives at a center where ∂g=0 (Γ=0).
C=mm(mm(tr(B),H85.Lmatrix(w0)),B)
dC=mm(mm(tr(B),H85.Lmatrix(dw)),B)
assert C==[[F(22),F(13),F(13)],
          [F(13),F(38),F(13)],
          [F(13),F(13),F(38)]]
assert dC==[[F(25),F(25),F(25)],
            [F(25),F(0),F(25)],
            [F(25),F(25),F(25)]]
Ci=inv(C)
T=mm(Ci,dC)
trT=sum(T[i][i] for i in range(3))
assert trT==F(51,98)
g1=H98.mat_scale(mm(mm(mm(mm(G,Ci),dC),Ci),G),F(-16))
# Independent derivative from H98's exact 6x6 Jacobian.
symvec_g1=[sum(Ag[z][k]*dw[k] for k in range(6))
           for z in range(6)]
assert H98.symvec(g1)==symvec_g1
trginvg1=sum((ginv[i][k]*g1[k][i] for i in range(3)
             for k in range(3)),F(0))
assert trginvg1==F(-51,98)
assert trginvg1==-trT

def ddg(i,j,k,l,a):
    # ∂i∂j g_kl(0)=2a*g0_ij*g1_kl
    return 2*a*g0[i][j]*g1[k][l]

def levi_civita_scalar(a):
    # Γ(0)=0 due to identical zero first jets;
    # R=g^{ij}g^{kl}(∂k∂j g_il - ∂k∂l g_ij).
    return sum((ginv[i][j]*ginv[k][l]*
                (ddg(k,j,i,l,a)-ddg(k,l,i,j,a))
                for i in range(3) for j in range(3)
                for k in range(3) for l in range(3)),F(0))
for a in (F(0),alpha):
    R2=levi_civita_scalar(a)
    Rtrace=4*a*trT
    assert R2==Rtrace
assert levi_civita_scalar(F(0))==0
assert levi_civita_scalar(alpha)==F(102,245)
print("PASS H99.3: exact independent curvature computations agree; flat source-positive field R(0)=0 vs spatially varied source-positive field R(0)=102/245 despite same local 1-jets")

# CONDITIONAL external ADM constraint comparison. At the same
# locally supplied canonical momentum pi=0 and no cosmological
# constant, H_ADM(0)=-sqrt(det g)*R. sqrt(det g0)=64/35 exactly.
assert F(64,35)**2==H98.determinant(g0)
flat_constraint=F(0)
curved_constraint=-F(64,35)*levi_civita_scalar(alpha)
assert curved_constraint==F(-6528,8575)
assert flat_constraint!=curved_constraint
print("PASS H99.4: same pointwise H75 data, K4 spatial metric, spatial first jet AND externally zero ADM momentum admit different ADM constraints: 0 vs -6528/8575")
print("BOUNDARY: spatial coordinate x, positive-state preparation PROFILE, K4 graph/additive selector/solder and Levi-Civita ADM reading are INDEPENDENT assumptions, not a source-generated physical spatial propagation law")
print("BOUNDARY: rank3 applies to the SPECIFIC normalized additive H85 four-readout source selector, not all imaginable CR controls; full ADM six metric DOFs and six conjugate momenta remain physically UNSOURCED")
print("BOUNDARY: physical curvature two-jet/interaction selection, Hamiltonian action, full nonuniform off-shell HDA, Einstein equations and P11 F generative completeness remain OPEN")
