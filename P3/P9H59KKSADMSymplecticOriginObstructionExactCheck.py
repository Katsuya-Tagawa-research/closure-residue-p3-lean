"""H59 — exact conditional KKS→ADM interface: a finite U(4) orbit
has FULL 12-dimensional tangent rank but non-exact global KKS
symplectic class. A local Darboux chart exists; a GLOBAL
symplectic pullback into an exact cotangent ADM/K4 phase space
cannot exist. Site orientation repair requires extra microscopic
controls if the 4-site diagonal observer MASA and trivial mode
must both be preserved.

H58 supplies an external mathematical positive-edge cone normalizer;
H59 never claims P9.64 has a specific microscopic KKS orbit or that
any symplectic equivalence derives ADM gravity from P3.
Only rational exact algebra (and a standard explicitly stated
Stokes/topological KKS-sphere argument); no numeric estimates.
"""
from fractions import Fraction as F
from itertools import permutations
from math import prod
from P9H52K4DeWittKinematicsCurvatureExactCheck import (
    I,zeros,add,scale,mm,trans,trace,rank,det,T as f_basis,G
)
from P9H58K4PositiveConeSolderRigidityExactCheck import (
    site_perms,site_matrix,parity,Qsite,transition,
    edge_permutation,edge_perm_matrix
)

m=4
n=6
one=[F(1)]*4
def sub(A,B):return add(A,scale(B,F(-1)))
def comm(A,B):return sub(mm(A,B),mm(B,A))
def diagonal(d):return [[d[i] if i==j else F(0)
                         for j in range(len(d))] for i in range(len(d))]
def dot(u,v):return sum((a*b for a,b in zip(u,v)),F(0))
def matvec(A,v):return [dot(r,v) for r in A]
def inner(A,B):return sum((A[i][j]*B[i][j]
                           for i in range(len(A))
                           for j in range(len(A[0]))),F(0))
def ps(a,b):return [a[i]+b[i] for i in range(len(a))]
def skew_edge(i,j):
    A=zeros(m,m);A[i][j]=F(1);A[j][i]=F(-1)
    return A
def sym_edge(i,j):
    A=zeros(m,m);A[i][j]=A[j][i]=F(1)
    return A
def conjugate(W,X):return mm(mm(W,X),trans(W))
def perm_compose(p,q):return tuple(p[q[j]] for j in range(m))
def rho_from_eigenvalues(lams):return diagonal(lams)
def site_projector(E):return conjugate(E,diagonal([F(1),F(0),F(0),F(0)]))

# 1. A PHYSICAL four-level generic spectral KKS orbit:
# strictly positive TRACE-ONE, nondegenerate spectrum; not
# posited as the actual microscopic P9.64 orbit.
lam=[F(1,10),F(2,10),F(3,10),F(4,10)]
rho=rho_from_eigenvalues(lam)
assert trace(rho)==1 and all(x>0 for x in lam)
edges=[(i,j) for i in range(m) for j in range(i+1,m)]
assert len(edges)==6
X=[skew_edge(i,j) for i,j in edges]
S=[sym_edge(i,j) for i,j in edges] # i S is skew-Hermitian
# For U(4) coadjoint KKS:
# omega_rho(X#, (i S)#) = -i Tr(rho[X,i S])
#                            = Tr(rho[X,S])
#                            = 2*(lambda_i-lambda_j).
d=[F(2)*(lam[i]-lam[j]) for i,j in edges]
assert d==[F(-1,5),F(-2,5),F(-3,5),
           F(-1,5),F(-2,5),F(-1,5)]
for k,(a,b) in enumerate(edges):
    C=comm(X[k],S[k])
    assert C==scale(sub(diagonal([F(int(i==a)) for i in range(m)]),
                        diagonal([F(int(i==b)) for i in range(m)])),F(2))
    assert trace(mm(rho,C))==d[k]
    # Distinct root planes are symplectically orthogonal
    for j in range(n):
        if j!=k:
            assert trace(mm(rho,comm(X[k],S[j])))==F(0)
# Full 12x12 KKS tangent-form matrix in six X and six i S
# directions, absolutely NOT H52's symmetric DeWitt supermetric.
K=zeros(12,12)
for k,gap in enumerate(d):
    K[k][n+k]=gap
    K[n+k][k]=-gap
assert K==scale(trans(K),F(-1))
assert rank(K)==12
assert det(K)==prod(d)**2==F(144,244140625)
# Six independent (X,i S) root pairs span tangent rank12:
# generic U4 orbit dimension 4²-1²-1²-1²-1²=12.
degenerate_shapes={
    (4,):0,(3,1):6,(2,2):8,(2,1,1):10,
    (1,1,1,1):12
}
for shape,dim in degenerate_shapes.items():
    assert dim==16-sum(k*k for k in shape)
assert degenerate_shapes[(1,1,1,1)]==12
assert degenerate_shapes[(3,1)]<12
# Rank == 12 removes a DIMENSION-ONLY no-go, not existence,
# not physical independence, and not global topology.

# 2. S4 on FOUR-site Hilbert space lifts as exact unitary
# permutation conjugation of the entire orbit and preserves KKS
# because the trace commutator is invariant under conjugation.
J4=[[F(1,4)]*m for _ in range(m)]
Pi0=J4
PiS=sub(I(4),Pi0)
assert mm(Pi0,Pi0)==Pi0 and mm(PiS,PiS)==PiS
def Wplus(p):
    P=site_matrix(p)
    return add(Pi0,scale(mm(P,PiS),F(parity(p))))
assert len(site_perms)==24
Ws={}
for p in site_perms:
    P=site_matrix(p)
    W=Wplus(p)
    Ws[p]=W
    assert mm(W,trans(W))==I(4)
    assert matvec(W,one)==one
    assert mm(W,f_basis)==mm(f_basis,scale(Qsite(p),F(parity(p))))
    assert det(scale(Qsite(p),F(parity(p))))==1
    assert transition(scale(Qsite(p),F(parity(p))))==edge_perm_matrix(
        edge_permutation(p))
    # Both P and W are unitary SO/O matrices; each acts
    # symplectically by conjugation on this generic U4 orbit.
    for U in (P,W):
        rs=conjugate(U,rho)
        assert trace(rs)==F(1)
        for k in range(n):
            assert trace(mm(rs,comm(conjugate(U,X[k]),
                                    conjugate(U,S[k]))))==d[k]
    if parity(p)==1:
        assert W==P
    else:
        assert W!=P
        # W=(1/2)11^T-P has ALL entries ±1/2. Its rank-1
        # source-projector image is NOT in the original diagonal
        # observer MASA, although W fixes the trivial one-vector.
        assert all(abs(x)==F(1,2) for row in W for x in row)
        rotated_site=site_projector(W)
        assert rotated_site[0][1]!=0 and rotated_site[0][2]!=0
        assert rotated_site!=diagonal(
            [rotated_site[i][i] for i in range(m)])
for p in site_perms:
    for q in site_perms:
        assert mm(Ws[p],Ws[q])==Ws[perm_compose(p,q)]
# H58 orientation-repaired S4 has a mathematical faithful
# 4x4 REAL-ORTHOGONAL lift, but odd elements leave the fixed
# four-site observer MASA. Site permutations alone give only
# A4 if orientation+ on S AND one-vector fixed are both required.

# 3. The GLOBAL symplectic obstruction is TOPOLOGICAL, not rank.
# The (a,b) SU2 two-level subgroup orbit inside the generic
# compact U4 orbit is CP1=S². Under standard KKS normalization,
# integral over its oriented sphere is
#   ∫_S² omega_KKS = 2 pi (lambda_b-lambda_a) !=0.
# This follows from spin radius r=(lambda_b-lambda_a)/2:
#   omega = r sin(theta) dtheta∧dphi, area=4*pi*r.
# We check its exact nonzero rational COEFFICIENT of pi, and
# the two-patch potential/transition winding at the equator.
area_coeffs=[F(2)*abs(lam[i]-lam[j]) for i,j in edges]
assert area_coeffs==[F(1,5),F(2,5),F(3,5),
                     F(1,5),F(2,5),F(1,5)]
assert area_coeffs[0]>0
r=(lam[1]-lam[0])/2
assert r==F(1,20)
assert F(4)*r==area_coeffs[0]
# Smooth northern/southern KKS potentials:
# A_N=r(1-cosθ)dφ, A_S=-r(1+cosθ)dφ.
# A_N-A_S=2r dφ with 2π winding, transition flux 4πr.
assert 2*r==lam[1]-lam[0]
# Any globally defined map F from this compact U4 orbit into
# EXACT ADM cotangent phase space with F*Omega_ADM=omega_KKS
# would make omega exact. Its integral on this S² would vanish
# by Stokes, contradiction with area_coeffs[0]*pi>0.
# This rules out a GLOBAL symplectic pullback to globally exact
# T*(positive K4 chart) — even though DIMENSION matches 12.
# Reductions/targets with non-exact forms can evade this premise.

# 4. Conversely LOCAL canonical matching is mathematically
# possible. Six independent SU2 spin spheres (dim 12) with
# Darboux cylinders (φ_e,z_e) (|z|<r, one φ-chart) have KKS
# omega=sum dφ_e∧dz_e, and the local change
#  w_e=exp(φ_e)>0, p_e=z_e/w_e
# is an exact symplectomorphism into the K4 six-weight cotangent
# chart. Prove using its rational pointwise JACOBIAN, without
# approximating exponentials or pretending to give a global φ.
w=[F(2),F(3),F(5),F(7),F(11),F(13)]
z=[F(1,10),F(-1,8),F(1,7),F(-1,6),F(1,9),F(-1,5)]
p=[z[i]/w[i] for i in range(n)]
J=zeros(12,12)
for i in range(n):
    J[i][i]=w[i]
    J[n+i][i]=-p[i]
    J[n+i][n+i]=F(1)/w[i]
Om=zeros(12,12)
for i in range(n):
    Om[i][n+i]=F(1)
    Om[n+i][i]=F(-1)
assert mm(mm(trans(J),Om),J)==Om
assert det(J)==F(1) and rank(J)==12
# Canonical one-form matching θ_KKS=Σ z dφ = θ_ADM=Σ p dw
dphi=[F(1,3),F(-1,5),F(2,7),F(1,9),F(-3,11),F(4,13)]
dw=[w[i]*dphi[i] for i in range(n)]
assert dot(z,dphi)==dot(p,dw)
# H58 S4 edge relabel acts by permuting the six independent
# spheres, and local positive-cone scale shifts longitudes.
for p4 in site_perms:
    ep=edge_permutation(p4)
    wp=[F(0)]*n
    zp=[F(0)]*n
    for i,j in enumerate(ep):
        wp[j]=w[i]
        zp[j]=z[i]
    pp=[zp[i]/wp[i] for i in range(n)]
    assert sum(zp)==sum(z)
    assert dot(zp,[dphi[ep.index(i)] for i in range(n)])==dot(z,dphi)
    assert all(wp[i]>0 for i in range(n))
    assert dot(pp,[dw[ep.index(i)] for i in range(n)])==dot(p,dw)
for lam_scaling in (F(1,2),F(2),F(3,2)):
    ww=[lam_scaling**2*x for x in w]
    pp=[x/(lam_scaling**2) for x in p]
    assert dot(pp,[lam_scaling**2*x for x in dw])==dot(p,dw)
    assert [ww[i]*pp[i] for i in range(n)]==z
# The local six-spin symplectomorphism is a mathematical
# counterexample to saying a KKS→ADM map is IMPOSSIBLE
# solely because KKS has spin degrees of freedom.
# It is NOT a physical four-site U4 orbit map, not global,
# not a dynamical intertwiner, not an observer/P6 causal map.

print("PASS H59: generic four-site U4 density orbit has EXACT nondegenerate 12D KKS matrix, unlike lower-degeneracy orbits")
print("PASS H59: all 24 S4 site permutations and orientation-repaired W lifts preserve U4-orbit KKS brackets")
print("PASS H59: odd orientation-repair W is NOT a site MASA-preserving permutation; 4-site control provenance gate")
print("PASS H59: compact U4 KKS has nonzero CP1 2-cycle flux 2pi|lambda_a-lambda_b|, forbidding global exact-ADM symplectic pullback")
print("PASS H59: explicit six-spin local Darboux->positive K4 cotangent Jacobian preserves exact 12D symplectic form")
print("PASS H59: mathematical S4 edge permutations/common positive scaling are locally symplectic but NOT physically certified")
print("BOUNDARY: H59 does not assume actual P9.64 KKS orbit, physical solder/control, field limit or KKS-to-Einstein dynamics")
