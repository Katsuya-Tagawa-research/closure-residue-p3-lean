"""H42: genuine P3 reflection-covariant connected CPTP with R2=0,
R3=D3^0, but NO derivation of P6 collective static Jcol or locked
physical control tangent from its full original P3 diagonal filtration.

A *single* exact rational-CPTP unitary U=diag(i,1,i)*Cayley(K/2),
K=(E01-E10)+(E21-E12), commutes with the left-right swap.

Full D3 -> parity-ODD hidden mode despite central seed parity-EVEN.
The complete hidden Xi image (checked through degree 8 and CH) lacks
the desired P6 real collective A+B, though nonzero P3 R3 saturates.
Two independent CPTP control extensions share EXACT SAME U, R3,
support and calibrated total control norm, but have opposite null status.
This is a logical provenance No-Go, not a CR-exclusive quantum effect.

All arithmetic exact Gaussian rationals (H24) and exact real ranks (H32).
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    N,unit,z,eye,scale,add,sub,mm,dagger,com,diag,hidden,trace,rr
)
assert N==3
def mat(rows):return [[gc(t) for t in row] for row in rows]
def conj_transpose(x):return dagger(x)
def action(U,x):return mm(mm(U,x),dagger(U))
def Xi(j):return hidden(sub(j,dagger(j)))
def scalar_product(P,X):return trace(mm(P,X))
def pop_difference(X):return (X[0][0]-X[2][2]).r
def hessian(U0,K,seed):
    rho=action(U0,seed)
    return com(K,com(K,rho))
def rank_complex(H):
    # For Hermitian independent generators, rank_C H equals rank_R Xi(iH),
    # and is checked using the already-audited exact real rank rr.
    return rr([Xi(scale(h,I)) for h in H])
def residue(h,k):
    return diag(com(h,dagger(k)))
def witness_value(m):
    return [m[j][j] for j in range(N)]

K=add(sub(unit(0,1),unit(1,0)),
      sub(unit(2,1),unit(1,2)))
A=sub(unit(0,1),unit(1,0))
B=sub(unit(2,1),unit(1,2))
T=add(unit(0,1),unit(2,1))
Jcol=[T,dagger(T)]
reflection=add(unit(0,2),add(unit(1,1),unit(2,0)))
Cayley=mat([[F(2,3),F(2,3),F(-1,3)],
            [F(-2,3),F(1,3),F(-2,3)],
            [F(-1,3),F(2,3),F(2,3)]])
Pphase=mat([[I,0,0],[0,1,0],[0,0,I]])
U=mm(Pphase,Cayley)
assert mm(dagger(Cayley),Cayley)==eye()
assert mm(dagger(U),U)==eye()
assert mm(reflection,U)==mm(U,reflection)
assert mm(reflection,reflection)==eye()
assert mm(reflection,K)==mm(K,reflection)
assert U==mat([[C(0,F(2,3)),C(0,F(2,3)),C(0,F(-1,3))],
               [F(-2,3),F(1,3),F(-2,3)],
               [C(0,F(-1,3)),C(0,F(2,3)),C(0,F(2,3))]])
# The microscopic continuous underlying K only couples path edges,
# but its finite Cayley unitary U already has a 0--2 chord matrix
# element: one-step Kraus support and generator graph differ.
assert U[0][2]!=Z0
assert action(U,unit(1,1))[0][1]!=Z0
assert action(U,unit(1,1))[2][1]!=Z0

D=[unit(i,i) for i in range(N)]
def iterate_all(maxdepth):
    H_all=[]
    H_depth=[]
    evolved=D[:]
    for step in range(1,maxdepth+1):
        evolved=[action(U,x) for x in evolved]
        Hk=[hidden(x) for x in evolved]
        assert Hk[0]==hidden(evolved[0])
        assert sum((Hk[j][0][1] for j in range(N)),Z0)==Z0
        assert all(dagger(x)==x for x in Hk)
        assert all(trace(x)==Z0 for x in Hk)
        H_depth.append(Hk)
        # use two seeds, because unitality makes h^(2)=-h^(0)-h^(1)
        H_all.extend(Hk[:2])
    return H_depth,H_all
by_depth,H=iterate_all(8)
h01=by_depth[0][0]
h11=by_depth[0][1]
h21=by_depth[0][2]
assert h01==mat([[0,C(0,F(-4,9)),F(-2,9)],
                 [C(0,F(4,9)),0,C(0,F(-2,9))],
                 [F(-2,9),C(0,F(2,9)),0]])
assert h11==mat([[0,C(0,F(2,9)),F(4,9)],
                 [C(0,F(-2,9)),0,C(0,F(-2,9))],
                 [F(4,9),C(0,F(2,9)),0]])
assert h21==action(reflection,h01)
assert h01!=h21
assert h11==action(reflection,h11)
assert action(reflection,sub(h01,h21))==scale(sub(h01,h21),-1)
# Even CENTER seed has a distance-two chord 02. It is not a local
# static collective T or T† generator by itself.
assert h11[0][2]==gc(F(4,9))!=Z0
assert rr([Xi(scale(sub(h01,h21),I))])==1
assert rr([Xi(scale(sub(h01,h21),I)),sub(A,B)])==1
# The P3 full diagonal algebra generates both reflection even and odd
# hidden sectors; restricting to only d=E11 is EXTRA observer selection.

r2=[residue(x,y) for x in by_depth[0] for y in by_depth[0]]
assert all(R==z() for R in r2)
# Two explicitly independent depth 1+2 ORIGINAL P3 quadratic
# witnesses (including adjoint, not an artificial Lie operation):
r31=residue(by_depth[0][0],by_depth[1][0])
r32=residue(by_depth[0][1],by_depth[1][0])
assert witness_value(r31)==[C(0,F(-32,81)),
                           C(0,F(16,81)),C(0,F(16,81))]
assert witness_value(r32)==[C(0,F(40,81)),
                           C(0,F(-8,81)),C(0,F(-32,81))]
assert rr([r31,r32])==2
assert trace(r31)==trace(r32)==Z0
# Thus original P3 R2=0 and R3=D3^0 (traceless diagonal two
# complex dimensions), within this ONE reflection-equivariant CPTP.

# Exact hidden complex Krylov dimensions and P6 Xi access:
# 2,4,5,5,... ; at depth 8 Cayley-Hamilton for 9-dimensional
# superoperator ensures all subsequent iterates are in the span of
# the already inspected j<=8 diagonal inputs.
rank_expected=(2,4,5,5,5,5,5,5)
acc=[]
for j,Hstep in enumerate(by_depth,1):
    acc.extend(Hstep[:2])
    rank=rank_complex(acc)
    assert rank==rank_expected[j-1],(j,rank)
    image=[Xi(scale(h,I)) for h in acc]
    assert rr(image+[add(A,B)])==rank+1
    assert rr(image+[A])==rank+1
    assert rr(image+[B])==rank+1
# Note the ORIGINAL P3 Xi(H∞) contains anti-collective A-B
# but not locked A+B.
assert rr([Xi(scale(h,I)) for h in H[:2]]+[sub(A,B)])==2
assert rr([Xi(T),Xi(scale(T,I))])==2
assert rr([Xi(T),Xi(scale(T,I)),add(A,B)])==2
assert rr([Xi(T),Xi(scale(T,I)),sub(A,B)])==3
# Consequently Jcol cannot be a subset of the full P3 H∞
# and the two spaces are not equal; independently supplying
# Jcol / a provenance map is a logically new hypothesis.
assert rank_complex(H)==5

# A CONDITIONAL localized "repair" is possible if we additionally:
# (i) choose only the center seed, (ii) delete chord 02 by a purely
# LINEAR non-CPTP spatial projection, and (iii) select i*h as the
# first-residue microscopic input. This yields the locked direction,
# but is NOT an inheritance theorem or physical projection.
h_center_local=[[h11[i][j] if abs(i-j)==1 else Z0
                 for j in range(N)] for i in range(N)]
locked_from_local=Xi(scale(h_center_local,I))
assert locked_from_local==scale(add(A,B),F(-4,9))
assert rr([locked_from_local,add(A,B)])==1
assert rr([locked_from_local,sub(A,B)])==2

# Two legitimate independent CPTP physical control extensions
# share exactly the same *uncontrolled* U, original P3 R2/R3,
# connected path generator K and calibrated aggregate norm.
# Define Psi_x=Ad_exp(x Kctrl) o Ad_U (CPTP for every real x).
# Their Hessians at x=0 are computed without needing to
# evaluate a transcendental matrix exponential.
locked=(F(3,5),F(3,5))
unlocked=(F(3,25),F(21,25))
def K_of(amps):return add(scale(A,amps[0]),scale(B,amps[1]))
def total_sq(amps):return amps[0]*amps[0]+amps[1]*amps[1]
assert total_sq(locked)==total_sq(unlocked)==F(18,25)
assert all(x!=0 for x in locked+unlocked)
rho0=action(U,unit(1,1))
assert action(reflection,rho0)==rho0
def response(amps):
    return pop_difference(hessian(U,K_of(amps),unit(1,1)))
assert response(locked)==F(0)
assert response(unlocked)==F(288,625)
assert response(locked)!=response(unlocked)
# Frozen P6's direct intervention family starting from E11 itself
# gives 0 vs -864/625. Both variants are legitimate, have same
# micro U/P3 data and norm, and only their independent controls differ.
def direct_response(amps):
    k=K_of(amps)
    return pop_difference(com(k,com(k,unit(1,1))))
assert direct_response(locked)==F(0)
assert direct_response(unlocked)==F(-864,625)
# Strong logical conclusion: even full one-step P3 channel and
# saturated original P3 residue do not uniquely determine an
# independently specified physical intervention tangent.
# Additional covariant tangent-provenance/exclusion axiom needed.
print("PASS H42: exact rational connected reflection-equivariant three-site unitary CPTP")
print("PASS H42: original P3 R2=0 and R3 saturates traceless diagonal D3^0")
print("PASS H42: full original P3 diagonal seeds include reflection-odd hidden direction")
print("PASS H42: full Krylov Xi image ranks 2/4/5 and excludes P6 locked A+B even at infinite depth")
print("PASS H42: independent same-U CPTP control extensions have equal aggregate norm and unequal Hessians")
print("PASS H42: central-seed local support projection only conditionally recovers locked tangent")
print("SCOPE: nonzero P3 quadratic residue and reflection symmetry do NOT derive frozen P6 Jcol")
print("SCOPE: external observer selection, CP-realizable locality and physical tangent provenance remain open")
