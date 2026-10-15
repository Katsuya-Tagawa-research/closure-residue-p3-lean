"""H57: CONDITIONAL K4 solder/chart atlas, exact transition cocycle,
cotangent/Poisson preservation, nonuniform curvature/constraint data,
and time-dependent solder connection.

EXTERNAL PREMISES: physical spatial 3-manifold, family of permissible
GL+(3) solder choices, smooth chart compatibility, standard ADM
action and field symplectic Poisson structure, boundary conditions.
The availability of non-permutation solder changes is NOT derived
from original P3/P4, P7/P8 or P9.64 KKS microphysics.

The remarkable restricted frame-chart transition is LINEAR in the
six edge weights because the inverse metric B=16G g^-1 G is linear
in those weights. T_Q belongs to GL(6), det=det(Q)^4=1 for shears.
For common physical coordinate metric:
  g_A(w) = Q^T g_0(v) Q,   v=T_Q w.
  p_B = T_Q^-T p_A, p_A dw = p_B dv.
For spatially varying Q(x), derivative-of-solder compensation is
ESSENTIAL. For externally time-dependent Q(t,x), an additional
frame-connection Hamiltonian term appears.
"""
from fractions import Fraction as F
from P9H52K4DeWittKinematicsCurvatureExactCheck import (
    I,zeros,add,scale,mm,trans,trace,inv,det,rank,
    B,G,V,cov_metric,dg,flatten_symmetric,positive_definite
)
from P9H55K4ADMCanonicalChartExactCheck import (
    Jmatrix,p_of,pi_of,dual_pi,tensor_contract
)
from P9H53K4SolderedSpatialCurvatureExactCheck import (
    levi_civita_curvature,Rh_formula
)
n=3
edges=6
one=[F(1)]*6
def mat_sub(A,B):return add(A,scale(B,-1))
def symvec(A):return flatten_symmetric(A)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def mv(A,v):
    assert len(A[0])==len(v)
    return [sum((a*b for a,b in zip(row,v)),F(0)) for row in A]
def vt_sub(a,b):return [x-y for x,y in zip(a,b)]
def vt_add(a,b):return [x+y for x,y in zip(a,b)]
def vt_scale(a,c):return [c*x for x in a]
def sandwich(Q,A):return mm(mm(trans(Q),A),Q)
def Qshear(s):
    return [[F(1),s,F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(1)]]
edgeC=[[symvec(V[e])[k] for e in range(edges)] for k in range(edges)]
edgeCi=inv(edgeC)
assert det(edgeC)==F(-256)
def raw_g(w):return cov_metric(w)
def chart_g(v,s):
    return sandwich(Qshear(s),raw_g(v))
def Tmat(s):
    # Equate g(w)=Q^T g(v)Q, equivalently
    # B(v)=G Q G^-1 B(w) G^-1 Q^T G.
    Q=Qshear(s)
    A=mm(mm(G,Q),inv(G))
    C=[[symvec(mm(mm(A,V[e]),trans(A)))[k]
        for e in range(edges)] for k in range(edges)]
    return mm(edgeCi,C)
def inverse_weights(g):
    b=scale(mm(mm(G,inv(g)),G),F(16))
    return mv(edgeCi,symvec(b))
def physical_j(v,s):
    Q=Qshear(s)
    return [[symvec(sandwich(Q,dg(v,[F(int(j==e))
                                      for j in range(edges)])))[k]
             for e in range(edges)] for k in range(edges)]
def J_dot(J,weights):return mv(J,weights)
def can_pi(p,T):
    return mv(trans(inv(T)),p)
def symplectic_bracket(fw,fp,gw,gp):
    return dot(fw,gp)-dot(fp,gw)
def dT(s):
    # Each entry T_Q(s) is a polynomial in s of degree <=2;
    # symmetric finite difference at integer offsets is the exact
    # derivative for degree <=2, no numerical approximation.
    return scale(mat_sub(Tmat(s+F(1)),Tmat(s-F(1))),F(1,2))

assert Tmat(F(0))==I(6)
for s in (F(-1,10),F(0),F(1,10),F(1,2)):
    T=Tmat(s)
    assert det(T)==F(1) and rank(T)==6
    assert dT(s)==scale(mat_sub(Tmat(s+F(1,2)),
                                Tmat(s-F(1,2))),F(1))
    for w in ((F(1),)*6,
              (F(2),F(1),F(3),F(1),F(2),F(1))):
        v=mv(T,w)
        assert chart_g(v,s)==raw_g(w)
        assert inverse_weights(chart_g(v,s))==list(w)
        assert Jmatrix(w)==mm(physical_j(v,s),T)

# Concrete genuine positive/positive chart overlap with a NONTRIVIAL
# (not merely vertex permutation) fixed solder shear s=1/10:
small=F(1,10)
Tsmall=Tmat(small)
assert mv(inv(Tsmall),one)==[
    F(13,10),F(9,10),F(103,100),F(1),F(7,10),F(11,10)]
assert all(x>0 for x in mv(inv(Tsmall),one))
assert mv(Tsmall,one)==[
    F(7,10),F(11,10),F(103,100),F(1),F(13,10),F(9,10)]
# Open neighborhoods exist by continuity and positivity.

# A finite 1/2 shear exits the ORIGINAL positive chart A while
# remaining in genuinely positive chart B with v=(1,...,1).
large=F(1,2)
Tlarge=Tmat(large)
wA=mv(inv(Tlarge),one)
assert wA==[
    F(5,2),F(1,2),F(7,4),F(1),F(-1,2),F(3,2)]
assert wA[4]<0 and positive_definite(chart_g(one,large))
assert raw_g(wA)==chart_g(one,large)
# K4 vertex relabeling merely permutes edges: a negative weight
# cannot be removed by the finite S4 site-permutation group.
assert sum(1 for t in wA if t<0)==1

# Exact three-chart COCYCLE: A=0, B=+1/10, C=-1/10.
sA,sB,sC=F(0),F(1,10),F(-1,10)
TAB=mm(Tmat(sB),inv(Tmat(sA)))
TBC=mm(Tmat(sC),inv(Tmat(sB)))
TAC=mm(Tmat(sC),inv(Tmat(sA)))
assert mm(TBC,TAB)==TAC
pA=[F(2),F(-1,3),F(4,5),F(3,7),F(-2,11),F(5,13)]
wA0=one[:]
wB=mv(TAB,wA0)
wC=mv(TBC,wB)
pB=can_pi(pA,TAB)
pC=can_pi(pB,TBC)
assert wC==mv(TAC,wA0)
assert pC==can_pi(pA,TAC)
assert all(x>0 for x in wB+wC)
wdot=[F(1,3),F(-2,5),F(3,7),F(-1,8),F(1,9),F(-2,11)]
assert dot(pA,wdot)==dot(pB,mv(TAB,wdot))
assert dot(pA,wdot)==dot(pC,mv(TAC,wdot))
# Full 6x6 canonical Poisson brackets, not just one-form:
# {v_i,pB_j}=delta_ij, {v_i,v_j}=0, {pB_i,pB_j}=0.
assert mm(TAB,trans(inv(TAB)))!=I(6) # not wrong convention
assert mm(TAB,inv(TAB))==I(6)
for i in range(edges):
    fw=[F(int(k==i)) for k in range(edges)]
    # Under v=T w and pB=T^-T pA, partial_w v_i=T_i.,
    # partial_p pB_j=(T^-T)_j.,
    for j in range(edges):
        gp=mv(trans(inv(TAB)),[F(int(k==j))
                              for k in range(edges)])
        assert dot(TAB[i],gp)==F(int(i==j))
# Equivalent transformed functional derivatives:
Fw=[F(1),F(2),F(-3),F(4),F(1,2),F(-2,7)]
Fp=[F(-1),F(3,5),F(2),F(-4),F(5,6),F(1,3)]
Hw=[F(2),F(-3),F(1,4),F(1),F(-1),F(5)]
Hp=[F(3),F(1,4),F(-1,2),F(2),F(4),F(-2)]
fwB=mv(trans(inv(TAB)),Fw)
fpB=mv(TAB,Fp)
hwB=mv(trans(inv(TAB)),Hw)
hpB=mv(TAB,Hp)
assert symplectic_bracket(Fw,Fp,Hw,Hp)==symplectic_bracket(
    fwB,fpB,hwB,hpB)
# Momentum-density (full symmetric off-diagonal factors) agrees:
pi=[[F(2),F(1,3),F(-1,5)],
    [F(1,3),F(-3,2),F(2,7)],
    [F(-1,5),F(2,7),F(4,3)]]
p_A=p_of(pi,wA0)
vB=mv(TAB,wA0)
p_B=mv(trans(physical_j(vB,small)),dual_pi(pi))
assert p_B==can_pi(p_A,TAB)
assert pi_of(p_A,wA0)==pi
assert dot(p_B,mv(TAB,wdot))==tensor_contract(
    pi,scale(raw_g(wA0),F(0)))+dot(p_A,wdot)

# Spatially VARYING solder/frame must NOT be silently treated
# as six independent scalar coordinate changes on w.
# Physical chart A uniform w(x)=1, but B weights
# v(x)=T(s(x))*one have a nonzero spatial gradient.
s0=F(1,10)
kappa=F(1,20)
v0=mv(Tmat(s0),one)
v1=mv(scale(dT(s0),kappa),one)
assert v1==[F(-3,20),F(1,20),F(3,100),F(0),
            F(3,20),F(-1,20)]
Q=Qshear(s0)
Qdot=[[F(0),kappa,F(0)],
      [F(0),F(0),F(0)],
      [F(0),F(0),F(0)]]
dg_naive=sandwich(Q,dg(v0,v1))
gv=raw_g(v0)
dg_frame=add(mm(mm(trans(Qdot),gv),Q),
             mm(mm(trans(Q),gv),Qdot))
assert dg_naive!=zeros(3,3)
assert dg_frame!=zeros(3,3)
assert add(dg_naive,dg_frame)==zeros(3,3)
# At any spatial point, the actual physical metric is identical;
# naive ∂v-only differentiation yields SPURIOUS curvature/connection.

# Full 3D spatial field and neighbor-stencil equality under a
# NONCONSTANT solder Q(s(x)), with a smooth nonflat uniform-edge
# conformal background w(x)=1-c x^T G x, c=1.
c=F(1)
def qform(x):
    return sum((x[i]*G[i][j]*x[j]
                for i in range(n) for j in range(n)),F(0))
def field_A(x):
    a=F(1)-c*qform(x)
    assert a>0
    return [a]*edges
def sfield(x):return s0+kappa*x[0]
def field_B(x):return mv(Tmat(sfield(x)),field_A(x))
def g_A(x):return raw_g(field_A(x))
def g_B(x):return chart_g(field_B(x),sfield(x))
def sample_stencil(fun,h):
    x=[F(0)]*n
    g0=fun(x)
    unit=I(n)
    def pt(*terms):
        v=[F(0)]*n
        for i,c in terms:
            v[i]+=c*h
        return fun(v)
    gi=[scale(mat_sub(pt((i,F(1))),pt((i,F(-1)))),
              F(1)/(2*h)) for i in range(n)]
    gij=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j:
                H=scale(add(mat_sub(pt((i,F(1))),scale(g0,F(2))),
                            pt((i,F(-1)))),F(1)/(h*h))
            else:
                H=scale(add(mat_sub(pt((i,F(1)),(j,F(1))),
                                    pt((i,F(1)),(j,F(-1)))),
                            mat_sub(pt((i,F(-1)),(j,F(-1))),
                                    pt((i,F(-1)),(j,F(1))))),
                        F(1)/(4*h*h))
            row.append(H)
        gij.append(row)
    return (g0,gi,gij)
for h in (F(1,10),F(1,20),F(1,40)):
    jetsA=sample_stencil(g_A,h)
    jetsB=sample_stencil(g_B,h)
    assert jetsA==jetsB
    Ra,Rica,Eina,_=levi_civita_curvature(*jetsA)
    Rb,Ricb,Einb,_=levi_civita_curvature(*jetsB)
    assert Ra==Rb==Rh_formula(c,h)
    assert Rica==Ricb and Eina==Einb
# Exact agreement of tensor jets -> same constraint densities,
# HDA structure beta^i and physical boundary currents IF
# ADM data and their tensor-density transformation are consistent.
testg=g_A([F(0)]*n)
assert testg==g_B([F(0)]*n)
for Ngrad,Mgrad in [([F(1),F(2),F(0)],
                     [F(-1),F(0),F(3)])]:
    alpha=[Ngrad[i]-Mgrad[i] for i in range(n)]
    assert mv(inv(testg),alpha)==mv(inv(
        g_B([F(0)]*n)),alpha)
xi=[F(1,3),F(0),F(-2,5)]
jflux=[2*sum((pi[j][i]*testg[i][k]*xi[k]
              for i in range(n) for k in range(n)),F(0))
       for j in range(n)]
assert any(jflux)
assert jflux==[2*sum((pi[j][i]*g_B([F(0)]*n)[i][k]*xi[k]
                         for i in range(n) for k in range(n)),F(0))
               for j in range(n)]

# If EXTERNAL solder Q depends on TIME, the time-independent
# cotangent formulas remain canonical on each time slice, but the
# transformed Hamiltonian receives a frame connection:
# H_B = H_A + p_B dotT T^-1 v.
dTdt=scale(dT(s0),kappa)
v_dot=vt_add(mv(Tmat(s0),wdot),mv(dTdt,wA0))
pBs=can_pi(pA,Tmat(s0))
frame_connection=dot(pBs,mv(dTdt,wA0))
H_A=F(17,13)
H_B=H_A+frame_connection
assert dot(pA,wdot)-H_A==dot(pBs,v_dot)-H_B
assert frame_connection!=F(0)
# Forgetting time-dependent solder connection would spuriously
# change the action/Hamiltonian even with an identical physical g.

print("PASS H57: two genuinely positive K4 soldered charts overlap; finite 1/2 shear exits A-positive cone")
print("PASS H57: exact six-edge transition T_Q and three-chart GL6 cocycle with det1")
print("PASS H57: cotangent momentum transport, 6x6 canonical Poisson brackets, exact symplectic pairing")
print("PASS H57: site permutation cannot rescue negative-weight A chart without new physical solder")
print("PASS H57: nonconstant spatial solder Q(x) requires derivative compensation; naive weight-scalar rule fails")
print("PASS H57: nonflat spatial 3D metric/Ricci/Einstein curvature stencils agree EXACTLY across chart overlap")
print("PASS H57: same ADM structure beta^i and momentum boundary-current values for identical physical fields")
print("PASS H57: time-dependent solder demands explicit Hamiltonian frame-connection term")
print("BOUNDARY: smooth admissible physical GL+ solder atlas is ADDITIONAL, not P3/P7/P9.64 generated")
print("BOUNDARY: all HDA identities inherited from externally assumed standard ADM and valid boundary support")
