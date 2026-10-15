"""H55 — Conditional ADM canonical variables in a local positive K4
metric chart. All-rational exact finite tensor audit.

EXTERNAL inputs: smooth physical 3-dimensional base, compatible
K4-to-TM solder, a 3+1 ADM foliation, lapse N>0, shift xi, action,
boundary conditions, canonical symplectic structure. Original P3/P4
does NOT derive these, and a single K4 cell has no spatial HDA.

The six K4 weights locally coordinate SPD(3). The COTANGENT lift
p_e = pi^{ij} (partial g_ij / partial w_e) preserves the canonical
one-form EXACTLY, including factors 2 for off-diagonal symmetric
components. The weight variables transform under spatial diffeos by
J(w)^-1 Lie_xi g, NOT as six ordinary scalars in a fixed solder.
The ADM Hamiltonian and momentum constraints can then be PULLED BACK
from EXTERNALLY assumed standard ADM, not derived from CR.
"""
from fractions import Fraction as F
from P9H52K4DeWittKinematicsCurvatureExactCheck import (
    I,zeros,add,scale,mm,trans,trace,inv,det,rank,B,G,cov_metric,
    dg,flatten_symmetric,positive_definite,dewitt
)
from P9H53K4SolderedSpatialCurvatureExactCheck import (
    conformal_jets,levi_civita_curvature
)
n=3
def subv(A,B):return add(A,scale(B,F(-1)))
def tensor_contract(A,B):
    return sum((A[i][j]*B[i][j]
                for i in range(n) for j in range(n)),F(0))
def matvec(A,v):
    return [sum((a*b for a,b in zip(row,v)),F(0)) for row in A]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def basis6(e):return [F(int(k==e)) for k in range(6)]
def Jmatrix(w):
    return [[flatten_symmetric(dg(w,basis6(e)))[i]
             for e in range(6)] for i in range(6)]
def weighted(dws,weighted_basis):
    out=zeros(n,n)
    for c,T in zip(dws,weighted_basis):
        out=add(out,scale(T,c))
    return out
def dual_pi(pi):
    return [pi[0][0],pi[1][1],pi[2][2],
            2*pi[0][1],2*pi[0][2],2*pi[1][2]]
def pi_from_dual(v):
    return [[v[0],v[3]/2,v[4]/2],
            [v[3]/2,v[1],v[5]/2],
            [v[4]/2,v[5]/2,v[2]]]
def p_of(pi,w):
    J=Jmatrix(w)
    return matvec(trans(J),dual_pi(pi))
def pi_of(p,w):
    return pi_from_dual(matvec(inv(trans(Jmatrix(w))),p))
def solve_weights(w,H):
    return matvec(inv(Jmatrix(w)),flatten_symmetric(H))
def lie_metric(g,gi,xi,dxi):
    # dxi[k][i] = partial_i xi^k, gi[k] = partial_k g
    return [[sum((xi[k]*gi[k][i][j]
                  +g[k][j]*dxi[k][i]+g[i][k]*dxi[k][j]
                  for k in range(n)),F(0))
             for j in range(n)] for i in range(n)]
def sqrt_g_uniform(w):
    # Nonorthonormal internal S frame f_i=e_i-e_3 is soldered
    # directly to spatial coordinate basis. det G=4, so
    # det(4G/w)=256/w^3 and sqrt(g)=16/w^(3/2).
    r={F(1):F(1),F(4):F(2),F(9):F(3)}[w]
    return F(16)/(r*r*r)
def canonical_pi(g,K,sqrtg):
    gi=inv(g)
    trK=trace(mm(gi,K))
    return scale(subv(mm(mm(gi,K),gi),scale(gi,trK)),sqrtg)
def adm_kinetic(g,v,N,sqrtg):
    assert N>0
    return sqrtg*dewitt(g,v,v)/(4*N)
def hamiltonian_kin(g,pi,N,sqrtg):
    p_lower=mm(mm(g,pi),g)
    contraction=tensor_contract(pi,p_lower)
    trpi=tensor_contract(pi,g)
    return N*(contraction-trpi*trpi/2)/sqrtg
def R_potential(g,sqrtg,R):
    return -sqrtg*R

# 1. Exact six-dimensional SPD metric chart and its COTANGENT LIFT.
weights=[
    (F(1),)*6,
    (F(4),)*6,
    (F(2),F(3),F(1),F(4),F(5),F(2)),
    (F(3,5),F(4,5),F(6,5),F(1),F(9,10),F(11,10))
]
PI=[[F(2),F(1,3),F(-1,5)],
    [F(1,3),F(-3,2),F(2,7)],
    [F(-1,5),F(2,7),F(4,3)]]
assert PI==trans(PI)
dw=[F(1,3),F(-2,5),F(3,7),F(5,8),F(-1,9),F(2,11)]
for w in weights:
    g=cov_metric(w)
    assert positive_definite(g)
    J=Jmatrix(w)
    assert det(J)!=0 and rank(J)==6
    assert pi_of(p_of(PI,w),w)==PI
    assert solve_weights(w,weighted(dw,[dg(w,basis6(e))
                                        for e in range(6)]))==dw
    # Exact canonical one-form equality pi^ij δg_ij = p_e δw_e
    assert tensor_contract(PI,weighted(dw,
           [dg(w,basis6(e)) for e in range(6)]))==dot(p_of(PI,w),dw)
    # The cotangent lift is a local symplectomorphism by exact
    # equality of the canonical ONE-FORMS, not by a claimed
    # finite-cell proof of the full spatial HDA.
    assert Jmatrix(w)==trans(trans(J))
# Symmetric off-diagonal density components require factor 2.
assert pi_from_dual(dual_pi(PI))==PI

# 2. Standard ADM kinematic Legendre identity in nonorthonormal
# spatial solder frame: all 6 independent velocities and finite lapse.
w=weights[0]
g=cov_metric(w)
assert g==scale(G,F(4)) and det(g)==F(256)
sqrtg=sqrt_g_uniform(F(1))
assert sqrtg==F(16) and sqrtg*sqrtg==det(g)
N=F(3,2)
wdot=[F(1,3),F(-2,5),F(3,7),F(-1,8),F(1,9),F(-2,11)]
Jbasis=[dg(w,basis6(e)) for e in range(6)]
gdot=weighted(wdot,Jbasis)
K=scale(gdot,F(1)/(2*N))
pi=canonical_pi(g,K,sqrtg)
p=p_of(pi,w)
Lkin=adm_kinetic(g,gdot,N,sqrtg)
Hkin=hamiltonian_kin(g,pi,N,sqrtg)
assert Lkin==Hkin
assert dot(p,wdot)-Lkin==Hkin
assert Hkin!=0
assert pi_of(p,w)==pi

# 3. A genuinely spatially inhomogeneous SHIFT vector field
# changes physical metric components, even at uniform constant
# edge-weight background. The induced WEIGHT action is J^-1 £xi g.
xi=[F(1,3),F(0),F(-2,5)]
dxi=[
 [F(1),F(0),F(0)],
 [F(0),F(0),F(0)],
 [F(0),F(0),F(0)]
]
zero_gradient=[zeros(n,n) for _ in range(n)]
Lieg=lie_metric(g,zero_gradient,xi,dxi)
assert Lieg!=zeros(n,n)
dwx=solve_weights(w,Lieg)
assert any(dwx) and weighted(dwx,Jbasis)==Lieg
# A WRONG six-scalar-field transformation would have δxi w_e =
# xi^i∂_i w_e=0 for uniform w; it misses the inhomogeneous
# Lie derivative due to spatial vector-field gradients.
assert [F(0)]*6!=dwx
vshift=subv(gdot,Lieg)
Kwshift=scale(vshift,F(1)/(2*N))
pishift=canonical_pi(g,Kwshift,sqrtg)
pshift=p_of(pishift,w)
Lshift=adm_kinetic(g,vshift,N,sqrtg)
Hshift=hamiltonian_kin(g,pishift,N,sqrtg)
assert dot(pshift,wdot)-Lshift==Hshift+dot(pshift,dwx)
assert dot(pshift,dwx)==tensor_contract(pishift,Lieg)
assert Hshift!=0

# 4. Momentum constraint is the integrated by-parts form of the
# shift term, NOT a constraint derived from one isolated cell.
# On flat constant metric at a point, the local identity:
# pi^ij (£xi g)_ij = xi^k H_k + ∂j(2 pi^{ji} g_ik xi^k),
# H_k=-2g_ik ∂j pi^{ji}, holds with density-one pi.
dpi=[[
 [F((m+1)*(i+j+2),37) for j in range(n)]
 for i in range(n)]
 for m in range(n)]
assert all(v==trans(v) for v in dpi)
dpi_div=[sum((dpi[j][j][i] for j in range(n)),F(0))
         for i in range(n)]
Hvec=[-2*sum((g[i][k]*dpi_div[i] for i in range(n)),F(0))
      for k in range(n)]
bulk_constraint=dot(xi,Hvec)
div_current=F(0)
for j in range(n):
    for i in range(n):
        for k in range(n):
            div_current+=2*(dpi[j][j][i]*g[i][k]*xi[k]
                             +pishift[j][i]*g[i][k]*dxi[k][j])
assert tensor_contract(pishift,Lieg)==bulk_constraint+div_current
# Boundary current is not negligible without appropriate
# compact supports or boundary variation prescription.

# 5. Exact homogeneous K4 minisuperspace in SAME physical chart.
# sqrt g=16/w^(3/2) in nonorthonormal chart; this is TWICE
# H52's orthonormal-coordinate density, not a contradiction.
for wval,sw in ((F(1),F(1)),(F(4),F(2)),(F(9),F(3))):
    ww=(wval,)*6
    gg=cov_metric(ww)
    assert gg==scale(G,4/wval)
    vol=F(16)/sw**3
    assert vol*vol==det(gg)
    for wdot_scalar,Np in ((F(3),F(2)),(F(-2),F(3))):
        gdt=scale(G,-4*wdot_scalar/(wval*wval))
        Kiso=scale(gdt,F(1)/(2*Np))
        piiso=canonical_pi(gg,Kiso,vol)
        # All six physical edges share w(t): the REDUCED momentum
        # is sum of six individual edge momenta.
        pscalar=sum(p_of(piiso,ww),F(0))
        Liso=adm_kinetic(gg,gdt,Np,vol)
        hiso=hamiltonian_kin(gg,piiso,Np,vol)
        assert Liso==-24*wdot_scalar*wdot_scalar/(Np*sw**7)
        assert pscalar==-48*wdot_scalar/(Np*sw**7)
        assert hiso==-Np*sw**7*pscalar*pscalar/96
        assert pscalar*wdot_scalar-Liso==hiso
        # Local homogeneous, flat spatial scalar R=0 and
        # vacuum Hamiltonian constraint Hperp=0 force pscalar=0.
        assert (hiso==0)==(pscalar==0)
# For a NONZERO wdot an arbitrary lapse does not make a valid
# vacuum ADM solution; the Hamiltonian constraint excludes it.

# 6. Curvature potential check uses an INDEPENDENTLY GIVEN smooth
# spatial field with physical soldering, as H53/H54 required.
gcur, dgcur, ddgcur=conformal_jets(F(1))
Rcur, Riccur, Eincur, _=levi_civita_curvature(
    gcur,dgcur,ddgcur)
assert Rcur==F(-3)
assert gcur==g and R_potential(gcur,sqrtg,Rcur)==F(48)
# At zero canonical momentum this local Hperp density is +48,
# not a physical solution of Hperp=0 absent further kinetic,
# matter or cosmological terms.
assert R_potential(gcur,sqrtg,Rcur)!=0

print("PASS H55: exact local K4 positive six-weight chart / six ADM spatial metric DOF")
print("PASS H55: p_e=pi^ij dg_ij/dw_e invertible COTANGENT lift; canonical 1-form preserved")
print("PASS H55: six-variable anisotropic ADM Legendre identity including nonzero lapse and spatial shift")
print("PASS H55: Lie_xi induced weight action contains ∂xi; six w_e NOT spatial scalars in fixed solder")
print("PASS H55: pointwise momentum-constraint/boundary-current identity on flat coordinate metric")
print("PASS H55: nonorthonormal volume 16/w^(3/2) versus orthonormal 8/w^(3/2) reconciled")
print("PASS H55: reduced homogeneous p_w, Hperp, lapse constraint; nonzero vacuum flat wdot excluded")
print("PASS H55: independently soldered nonzero R3 gives finite local ADM curvature potential")
print("BOUNDARY: all ADM dynamics/foliation/canonical brackets are EXTERNALLY ASSUMED standard GR")
print("BOUNDARY: full spatial HDA not proved by finite-cell checks; microphysical K4-to-gravity emergence OPEN")
