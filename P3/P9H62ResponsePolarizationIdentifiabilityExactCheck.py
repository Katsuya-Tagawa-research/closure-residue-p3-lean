"""H62 — exact first-control-jet phase-silence / metric-selector scope audit.

P9.70/71 reported inputs: four-site rho0=diag(.4,.3,.2,.1),
control u X_ab+v Y_ab, calibrated X/Y/Z readouts.
Finite rational tests only: no CR/P6 provenance or field limit.
"""
from fractions import Fraction as F

def rank(A):
    A=[[F(x) for x in row] for row in A]
    n,m=len(A),len(A[0]); pivot=0
    for j in range(m):
        k=next((i for i in range(pivot,n) if A[i][j]),None)
        if k is None:continue
        A[pivot],A[k]=A[k],A[pivot]
        z=A[pivot][j];A[pivot]=[v/z for v in A[pivot]]
        for i in range(n):
            if i!=pivot and A[i][j]:
                z=A[i][j]
                A[i]=[x-z*y for x,y in zip(A[i],A[pivot])]
        pivot+=1
        if pivot==n:break
    return pivot

lam=[F(4,10),F(3,10),F(2,10),F(1,10)]
edges=[(a,b) for a in range(4) for b in range(a+1,4)]
gaps=[lam[a]-lam[b] for a,b in edges]
assert len(edges)==6 and all(d>0 for d in gaps)
J= [[F(0)]*12 for _ in range(12)]
for e,delta in enumerate(gaps):
    # outputs ordered X_0..X_5,Y_0..Y_5; controls u_0..u_5,v_0..v_5
    J[e][6+e]=2*delta
    J[6+e][e]=-2*delta
assert rank(J)==12
print("PASS H62: P9 calibrated full K4 diagonal-basepoint control Jacobian rank 12")

# Restrict to levels 1,2: eigenvalues .3,.2, c=.25,r=.05.
c,r,p,R=F(1,4),F(1,20),F(3,100),F(1,25)
assert r*r==p*p+R*R
assert c+r==lam[1] and c-r==lam[2]
# coherence = R exp(-i q), q=0 or q=pi/2,
# <X>=2R cos q, <Y>=2R sin q, <Z>=p.
# instantaneous control-response sensitivity at time zero:
# J_XYZ = d/d(u,v) (d/dt <X,Y,Z>)
# = [[0,4p],[-4p,0],[2R sin q,-2R cos q]].
def response(cosq,sinq):
    return [[F(0),4*p],[-4*p,F(0)],
            [2*R*sinq,-2*R*cosq]]
J0=response(F(1),F(0))
J90=response(F(0),F(1))
assert J0[:2]==J90[:2]  # phase-blind despite distinct coherent states
assert J0[2]!=J90[2]    # Z control response resolves relative phase
assert rank(J0[:2])==rank(J90[:2])==2
assert rank(J0)==rank(J90)==2
# An invariant response signature depending only on p cannot induce a
# positive rank-2 metric on (p,q) by ANY positive observer weighting.
# Flatten Sigma_XY=[0,4p,-4p,0], differential columns (dp,dq).
Dsig=[[F(0),F(0)],[F(4),F(0)],[F(-4),F(0)],[F(0),F(0)]]
Gram=[[sum(Dsig[k][i]*Dsig[k][j] for k in range(4))
       for j in range(2)] for i in range(2)]
assert Gram==[[F(32),F(0)],[F(0),F(0)]]
assert rank(Gram)==1 and Gram[1][1]==0
print("PASS H62: any U(1)-invariant Sigma(p) has phase-null pullback metric; no positive 2D G without q-sensitive channels")
print("PASS H62: calibrated X/Y immediate CONTROL slopes have no q information on a coherent U2 sector")
print("PASS H62: adding calibrated Z control-response supplies q-sensitive data, but uses fixed XY reference axes")

# State expectation readout R=(2R cosq,2R sinq,p), which is not
# identified with the P6 response fingerprint Sigma without a proof.
# Isotropic pullback G= w(d<X>^2+d<Y>^2)+wZ d<Z>^2.
w,wZ=F(1),F(1)
Gqq=4*w*R*R
Gpp=4*w*p*p/(R*R)+wZ
Gpq=F(0)
assert Gqq==F(4,625) and Gpp==F(13,4)
assert Gpp*Gqq-Gpq*Gpq==F(13,625)>0
# Canonical shear q_tilde=q+f(p) preserves dq∧dp;
# its G_(p,q_tilde) = G_pq-G_qq*f'(p).
for slope in (F(-2),F(-1),F(0),F(1),F(3,2)):
    assert (Gpq-Gqq*slope==0)==(slope==0)
print("PASS H62: isotropic externally calibrated expectation metric fixes p-dependent canonical shear up to constant")

# Anisotropic readout weights cause q-dependent shear obstruction.
# At q=0, sinq*cosq=0; at q=pi/4, sinq*cosq=1/2.
wx,wy=F(1),F(2)
Gp0=F(0)
Gq0=4*R*R*wy
Gp45=4*p*(wx-wy)*F(1,2)
Gq45=4*R*R*(wx+wy)*F(1,2)
assert Gq0>0 and Gq45>0
assert Gp0/Gq0==0
assert Gp45/Gq45==F(-25,4)
# So no ONE f'(p) can make G_pq vanish at both q=0 and q=pi/4.
print("PASS H62: anisotropic XY calibration cannot be repaired by a single p-only shear on the entire angle chart")

# Distinct p-dependent readout frames chi(p)=alpha*p, with
# X'=2R cos(q-chi), Y'=2R sin(q-chi), Z=p:
# G'=Gpp(dp)^2+Gqq(dq-alpha dp)^2; q_tilde=q-alpha*p.
alpha=F(2)
Gpq_rot=-alpha*Gqq
Gpp_rot=Gpp+alpha*alpha*Gqq
assert Gpq_rot==F(-8,625)
assert Gpp_rot*Gqq-Gpq_rot*Gpq_rot==Gpp*Gqq
assert Gpq_rot-Gqq*(-alpha)==0
# Both isotropic *in their own calibrated frames*, but yield
# distinct G and distinct preferred p-dependent shears.
print("PASS H62: positive isotropic readout metric does not canonically select a shear without fixing the calibration frame")

# Four-site diagonal rephasing: K4 incidence has three independent
# relative phases and three independent gauge-invariant cycle phases.
B=[[F(0)]*6 for _ in range(4)]
for e,(a,b) in enumerate(edges):
    B[a][e]=1;B[b][e]=-1
assert rank(B)==3
cycles=[]
for a,b in [(1,2),(1,3),(2,3)]:
    z=[F(0)]*6
    z[edges.index((0,a))]=1
    z[edges.index((a,b))]=1
    z[edges.index((0,b))]=-1
    cycles.append(z)
assert rank(cycles)==3
assert all(all(sum(B[v][e]*cyc[e] for e in range(6))==0
               for v in range(4)) for cyc in cycles)
# A single coherent U2 edge has no closed loop and its relative
# phase changes under its U(1) rephasing. p-level circles are
# already invariant Lagrangian 1D leaves on the regular U2 orbit;
# this does NOT select an absolute angular origin.
print("PASS H62: K4 phases have three rephasing directions and three cycle invariants, but U2 single-edge q has no intrinsic zero")

# Instantaneous CONTROL derivative is independent of additive drift:
# d/du dot<O>|t=0 = i Tr(rho [X,O]), independently of H0.
# Thus changing independently chosen gradient κ or local stiffness A
# leaves this *first control jet* unchanged at fixed rho/controls.
A=F(1)
kappa1,kappa2=F(1),F(2)
sound1=2*A*kappa1*r*r
sound2=2*A*kappa2*r*r
assert sound1==F(1,200) and sound2==F(1,100) and sound1!=sound2
assert response(F(1),F(0))==J0  # same initial control jet
print("PASS H62: first local control-response jet alone cannot identify independently specified gradient stiffness")
print("BOUNDARY: P3/P6-origin selector, calibrated full-time Sigma, 3D tensor matching, P9.72 many-body limit and Einstein/HDA all OPEN")
