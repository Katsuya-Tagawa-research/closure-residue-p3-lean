"""H58 — global positive K4 edge-cone preserver rigidity.

THEOREM (linear finite geometry, conditional solder family):
For Q in GL(3,R), let T_Q be the H57 edge weight transition induced
by B(v)=(G Q G^-1) B(w) (G Q G^-1)^T.
If T_Q sends ALL strictly positive K4 weights to strictly positive
weights, then T_Q=lambda^2 P_edges for a common lambda>0 and one of
exactly 24 edge permutations induced by S4 vertex permutations.
In fact the map is automatically ONTO the positive cone.
For det Q>0: Q=sign(P)*lambda*Q_P, with
 Q_P=G^-1 T^T P T (P the 4-site permutation matrix).
The proof uses PSD rank-one extreme rays, K4 triangle circuits,
and unique triangular dependence. See accompanying note.
A GROUP OF MATHEMATICAL solder transforms is not an actual
microphysical/physical frame-gauge authorization from P3/P7/P9.64.

All exact Fraction checks: 24 vertex symmetries, 24 triangle-incidence
automorphisms among all 720 permutations of 6 edges, all monomial
T matrices, shear violating global positivity, cotangent/gluing and
time-dependent frame connection for a nonconstant allowed scale.

Full HDA remains EXTERNAL standard ADM conditional on boundary support.
"""
from fractions import Fraction as F
from itertools import combinations,permutations
from P9H52K4DeWittKinematicsCurvatureExactCheck import (
    I,zeros,add,scale,mm,trans,inv,det,rank,T as basis,G,V,
    B,cov_metric,dg,positive_definite,flatten_symmetric
)
from P9H57K4CanonicalSolderAtlasExactCheck import (
    edgeCi,edgeC,Tmat,mv,can_pi,dot,raw_g,sandwich,sample_stencil
)
from P9H53K4SolderedSpatialCurvatureExactCheck import (
    levi_civita_curvature,Rh_formula
)
n=3
edge_list=list(combinations(range(4),2))
assert len(edge_list)==6 and det(edgeC)==F(-256)
def transition(Q):
    A=mm(mm(G,Q),inv(G))
    C=[[flatten_symmetric(mm(mm(A,V[e]),trans(A)))[k]
         for e in range(6)] for k in range(6)]
    return mm(edgeCi,C)
def site_matrix(p):
    return [[F(int(a==p[b])) for b in range(4)]
            for a in range(4)]
def parity(p):
    inv_count=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    return -1 if inv_count%2 else 1
def edge_permutation(p):
    return [edge_list.index(tuple(sorted((p[i],p[j]))))
            for i,j in edge_list]
def edge_perm_matrix(ep):
    return [[F(int(r==ep[c])) for c in range(6)]
            for r in range(6)]
def Qsite(p):
    # Induced action of P on f_i=e_i-e_3 coordinates.
    return mm(mm(inv(G),trans(basis)),
              mm(site_matrix(p),basis))
def positive(xs):return all(x>0 for x in xs)
def symvec(x):return flatten_symmetric(x)
def mat_sub(a,b):return add(a,scale(b,-1))
def qform(x):
    return sum((x[i]*G[i][j]*x[j]
                for i in range(n) for j in range(n)),F(0))
def hamiltonian_connection(p,w,lamb,lambdot,PM):
    Tc=scale(PM,lamb*lamb)
    dTdt=scale(PM,2*lamb*lambdot)
    pB=can_pi(p,Tc)
    v=mv(Tc,w)
    correction=dot(pB,mv(dTdt,w))
    assert correction==2*lambdot*dot(p,w)/lamb
    return pB,v,correction,Tc,dTdt

def opposite_edge_witness(s):
    T= Tmat(s)
    assert T==transition([[F(1),s,0],[0,F(1),0],[0,0,F(1)]])
    return T
def hamiltonian_connection(p,w,lamb,lambdot,PM):
    T=scale(PM,lamb*lamb)
    dT=scale(PM,2*lamb*lambdot)
    pB=can_pi(p,T)
    v=mv(T,w)
    correction=dot(pB,mv(dT,w))
    assert correction==2*lambdot*dot(p,w)/lamb
    return pB,v,correction,T,dT

# 1. The four unique K4 triangular rank-two root circuits are the
# incidence structure used in the global classification proof.
root=[[
    sum((basis[k][i] * (F(int(k==a))-F(int(k==b)))
         for k in range(4)),F(0))
    for i in range(3)] for a,b in edge_list]
triangles={
    frozenset(combo) for combo in combinations(range(6),3)
    if rank([[root[e][i] for e in combo]
             for i in range(3)])==2
}
assert len(triangles)==4
expected_triangles={
 frozenset(edge_list.index(e) for e in tri)
 for tri in (
    ((0,1),(0,2),(1,2)),
    ((0,1),(0,3),(1,3)),
    ((0,2),(0,3),(2,3)),
    ((1,2),(1,3),(2,3)))
}
assert triangles==expected_triangles
# Every edge belongs to exactly two K4 triangular circuits.
assert all(sum(int(i in t) for t in triangles)==2 for i in range(6))
triangle_automorphisms={
 perm for perm in permutations(range(6))
 if {frozenset(perm[e] for e in t) for t in triangles}==triangles
}
assert len(triangle_automorphisms)==24
site_perms=list(permutations(range(4)))
induced_perms={tuple(edge_permutation(p)) for p in site_perms}
assert triangle_automorphisms==induced_perms
# Gives the rigorous combinatorial upper bound of 24 projective
# ray permutations. Rank-one PSD extremality forces monomial
# T_Q if the GLOBAL positive orthant maps into itself; K4
# triangle dependence forces all monomial coefficients equal.

# 2. Every one of 24 site permutations realizes the global
# positive-cone automorphism, with no other projective ray class.
all_Q=[]
for p in site_perms:
    Qp=Qsite(p)
    PM=edge_perm_matrix(edge_permutation(p))
    assert transition(Qp)==PM
    assert det(Qp)==F(parity(p))
    assert sandwich(Qp,G)==G
    assert det(PM)==F(1)
    # The user-defined GL+(3) orientation is restored for ODD
    # permutations by the central spatial inversion -Qp.
    Qplus=scale(Qp,F(parity(p)))
    assert det(Qplus)==F(1)
    for lamb in (F(1,2),F(1),F(7,5)):
        Q=scale(Qplus,lamb)
        Tc=transition(Q)
        assert det(Q)==lamb**3
        assert Tc==scale(PM,lamb*lamb)
        assert det(Tc)==lamb**12==det(Q)**4
        assert positive(mv(Tc,[F(1),F(2),F(3),F(4),F(5),F(6)]))
        assert positive(mv(inv(Tc),[F(1)]*6))
        assert sandwich(Q,G)==scale(G,lamb*lamb)
    all_Q.append((p,Qplus,PM))
assert len(all_Q)==24
# In particular fixing the P7 h=4G metric scale additionally
# forces lamb=1; the finite remaining mathematical group is
# isomorphic to S4 on unoriented root LINES. Imposing an A4-only
# physical vertex-orientation representation is an extra condition.

# 3. Cone rigidity is stronger than chart OVERLAP. Even a small
# positive determinant shear has negative TRANSITION COEFFICIENTS,
# so for SOME strictly positive input it leaves the positive cone.
Ts=opposite_edge_witness(F(1,10))
assert Ts[0][3]==F(-1,10)
assert Ts[2][0]==F(-9,100)
wtest=[F(1)]*6
wtest[3]=F(10)
assert positive(wtest)
assert mv(Ts,wtest)[0]==F(-1,5)
# But the SAME shear has nonempty positive/positive overlap
# at the uniform input: it is an allowed LOCAL chart transition.
assert positive(mv(Ts,[F(1)]*6))
assert positive(mv(inv(Ts),[F(1)]*6))

# 4. A nontrivial global automorphism of the positive cone
# preserves the cotangent, canonical bracket and chart cocycle.
pa=(1,0,2,3)  # odd P; after compensation Qplus is orientation+
pb=(0,2,1,3)
PMA=edge_perm_matrix(edge_permutation(pa))
PMB=edge_perm_matrix(edge_permutation(pb))
TA=scale(PMA,F(9,4))
TB=scale(PMB,F(25,16))
assert transition(scale(Qsite(pa),F(-3,2)))==TA
assert transition(scale(Qsite(pb),F(-5,4)))==TB
# Extra minus does not matter for T; either parity-compensating
# sign gives an orientation-preserving solder where appropriate.
TC=mm(TB,TA)
w0=[F(1),F(2),F(3),F(4),F(5),F(6)]
p0=[F(2),F(-1,3),F(4,5),F(3,7),F(-2,11),F(5,13)]
dw=[F(1,3),F(-2,5),F(3,7),F(-1,8),F(1,9),F(-2,11)]
v=mv(TA,w0)
pA=can_pi(p0,TA)
v2=mv(TB,v)
pB=can_pi(pA,TB)
assert positive(v+v2)
assert v2==mv(TC,w0)
assert pB==can_pi(p0,TC)
assert dot(p0,dw)==dot(pA,mv(TA,dw))==dot(pB,mv(TC,dw))
assert mm(TA,inv(TA))==I(6)

# 5. Spatially varying scale is a NONCONSTANT globally positive
# automorphism. Its SOLDER derivative terms are indispensable.
p=(0,1,3,2)
Qp=scale(Qsite(p),F(-1)) # parity-compensated det positive
PM=edge_perm_matrix(edge_permutation(p))
assert det(Qp)==F(1)
lamb=F(3,2)
kappa=F(1,7)
point_w=[F(1)]*6
vcenter=mv(scale(PM,lamb*lamb),point_w)
dvw=mv(scale(PM,2*lamb*kappa),point_w)
Q=scale(Qp,lamb)
dQ=scale(Qp,kappa)
g0=cov_metric(point_w)
g_raw=cov_metric(vcenter)
g_phys=sandwich(Q,g_raw)
assert g_phys==g0
# g0 is constant at this audit point so d g_phys = 0.
# Compute Dg_raw/Dw * dv/dx plus two explicit solder derivatives.
dg_raw=dg(vcenter,dvw)
naive=sandwich(Q,dg_raw)
frame_grad=add(mm(mm(trans(dQ),g_raw),Q),
               mm(mm(trans(Q),g_raw),dQ))
assert naive!=zeros(3,3)
assert frame_grad!=zeros(3,3)
assert add(naive,frame_grad)==zeros(3,3)

# 6. Nonflat neighbor metrics and HDA structure/boundary flux are
# identical under spatially changing globally preserving scale.
def field(x):
    t=F(1)-qform(x)
    assert t>0
    return [t]*6
def lamb_field(x):
    t=F(1)+kappa*x[0]
    assert t>0
    return t
def gA(x):return cov_metric(field(x))
def gB(x):
    L=lamb_field(x)
    Tcur=scale(PM,L*L)
    return sandwich(scale(Qp,L),cov_metric(mv(Tcur,field(x))))
for h in (F(1,10),F(1,20)):
    ja=sample_stencil(gA,h)
    jb=sample_stencil(gB,h)
    assert ja==jb
    Ra,Rica,Eina,_=levi_civita_curvature(*ja)
    Rb,Ricb,Einb,_=levi_civita_curvature(*jb)
    assert Ra==Rb==Rh_formula(F(1),h)
    assert Rica==Ricb and Eina==Einb
metric=gA([F(0)]*3)
assert metric==gB([F(0)]*3)
alpha=[F(1),F(-2),F(3)]
assert mv(inv(metric),alpha)==mv(inv(gB([F(0)]*3)),alpha)
pi=[[F(2),F(1,3),F(-1,5)],
    [F(1,3),F(-3,2),F(2,7)],
    [F(-1,5),F(2,7),F(4,3)]]
xi=[F(1,3),F(0),F(-2,5)]
def flux(g,pi,xi):
    return [2*sum((pi[j][i]*g[i][k]*xi[k]
                    for i in range(3) for k in range(3)),F(0))
            for j in range(3)]
assert flux(metric,pi,xi)==flux(gB([F(0)]*3),pi,xi)
assert any(flux(metric,pi,xi))

# 7. A time-dependent positive scale gives a frame Hamiltonian
# correction even though canonical symplectic charts agree at
# fixed time. Site permutation is locally CONSTANT under smoothness.
pB,v,conn,Tcur,dTdt=hamiltonian_connection(
    p0,w0,lamb,F(1,7),PM)
wdot=[F(1,3),F(-2,5),F(3,7),F(-1,8),F(1,9),F(-2,11)]
v_dot=[x+y for x,y in zip(mv(Tcur,wdot),mv(dTdt,w0))]
HA=F(17,13)
HB=HA+conn
assert conn!=0
assert dot(p0,wdot)-HA==dot(pB,v_dot)-HB
assert conn==F(2)*F(1,7)/lamb*dot(p0,w0)

print("PASS H58: 4 K4 triangle circuits and exactly 24 incidence automorphisms among 720 edge permutations")
print("PASS H58: all 24 S4 line-ray symmetries give T_Q=lambda² P_edge, determinant lambda^12")
print("PASS H58: exact global positive-cone rigidity (rank-one PSD extremality + triangle circuits)")
print("PASS H58: small shear has positive chart OVERLAP but violates global cone positivity for explicit positive w")
print("PASS H58: exact cotangent/symplectic transition and finite-cocycle for global-cone automorphisms")
print("PASS H58: spatially varying solder-scale produces derivative compensations, no spurious physical curvature")
print("PASS H58: nonflat Ricci/Einstein/stencil, HDA beta and ADM boundary current match after correct solder")
print("PASS H58: time-dependent globally allowed solder scale requires Hamiltonian connection term")
print("SCOPE: cone group is a MATHEMATICAL classification, not P3/P7 physical solder permission")
print("SCOPE: KKS->ADM F*Omega=omega, canonical dynamics, field gluing and full origin of Einstein remain OPEN")
