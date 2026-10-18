"""H102 P11 AX-CAN: inherited H75 real site controls give Lagrangian SO3
orbit; a NON-SOURCED complex X Hamiltonian grants one conditional SU2
symplectic pair. Real positive H75 output effects audit the difference.
NO source-derived Einstein/ADM momentum or independent U pre-gate.
"""
from fractions import Fraction as F
from itertools import combinations
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    micro,embed,mattrace,matmul,matadj,eye_n,zero_n,R60,U,A,B
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P9H85A4EdgeSourceSelectionExactCheck as H85
import P11H101PhaseBlindFlagCanonicalProvenanceExactCheck as H101

assert R60[0][0]==I*gc(F(-32,135))
rho=H101.rho(F(0))
assert rho==H85.rho3
def hermvec(T):
    assert H91.dag(T)==T
    pairs=list(combinations(range(len(T)),2))
    return ([T[i][i].r for i in range(len(T))]+
            [T[i][j].r for i,j in pairs]+
            [T[i][j].i for i,j in pairs])
for t in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
    st=H101.rho(t)
    pure=H91.tr(H91.mm(st,st))
    assert pure.i==0 and pure.r==F(5,8)+t*t/F(8)
assert H91.tr(H91.mm(H101.rho(0),H101.rho(0)))!=H91.tr(H91.mm(H101.rho(1),H101.rho(1)))
print("PASS H102.1: H101 phase-parametrized positive rho_t is NOT a single isospectral Hamiltonian orbit (purity 5/8+t²/8)")

C=H91.comm(A,B)
real_controls=(A,B,C)
for K in real_controls:
    assert H91.dag(K)==H91.scale(K,-1)
    assert all(z.i==0 for row in K for z in row)
assert H91.rank([hermvec(H91.scale(K,I)) for K in real_controls])==3
for K,L in combinations(real_controls,2):
    bracket=H91.comm(K,L)
    assert H91.rank([hermvec(H91.scale(H,I)) for H in real_controls]+[
        hermvec(H91.scale(bracket,I))])==3

real_tangents=[H91.comm(K,rho) for K in real_controls]
for T in real_tangents:
    assert H91.dag(T)==T and H91.tr(T)==Z0
    assert all(z.i==0 for row in T for z in row)
assert H91.rank([hermvec(T) for T in real_tangents])==3
def tangent(H):return H91.scale(H91.comm(H,rho),-I)
def poisson(H,J):
    x=-I*H91.tr(H91.mm(rho,H91.comm(H,J)))
    assert x.i==0
    return x.r
real_h=[H91.scale(K,I) for K in real_controls]
assert all(poisson(H,J)==0 for H in real_h for J in real_h)

# The full U3 orbit of diag(3/4,1/4,0) has 6 nonzero gaps and
# nondegenerate 6-real-dimensional KKS structure.
basis=[]
for a,b in combinations(range(3),2):
    basis.extend((H91.hermX(3,a,b),H91.hermY(3,a,b)))
assert len(basis)==6
assert H91.rank([hermvec(tangent(H)) for H in basis])==6
P=[[poisson(H,J) for J in basis] for H in basis]
assert H91.rank(P)==6
assert all(P[i][j]==-P[j][i] for i in range(6) for j in range(6))
assert H91.rank([hermvec(t) for t in real_tangents]+[
    hermvec(tangent(H)) for H in basis])==6
print("PASS H102.2: inherited original H75 A/B controls have Lie closure so3; 3D REAL source orbit KKS zero and is LAGRANGIAN in nondegenerate rank6 full U3 qutrit orbit")

# Original physical A gives Y Hamiltonian up to sign. New X
# would be an INDEPENDENT COMPLEX coherent gate NOT inherited from
# the declared H75 real-generator Lie algebra.
X=H91.hermX(3,0,1)
Y=H91.hermY(3,0,1)
Z=H91.minus(H91.e(3,0,0),H91.e(3,1,1))
assert Y==H91.scale(A,-I)
assert H91.comm(X,Y)==H91.scale(Z,2*I)
assert H91.comm(Y,Z)==H91.scale(X,2*I)
assert H91.comm(Z,X)==H91.scale(Y,2*I)
assert H91.rank([hermvec(H) for H in real_h]+[hermvec(X)])==4
TX,TY=tangent(X),tangent(Y)
assert H91.rank([hermvec(TX),hermvec(TY)])==2
assert poisson(X,Y)==F(1) and poisson(Y,X)==F(-1)
assert H91.rank([[poisson(X,X),poisson(X,Y)],
                 [poisson(Y,X),poisson(Y,Y)]])==2
print("PASS H102.3: conditional extra (not sourced) complex coherent X plus inherited Y yield one nondegenerate SU2 KKS symplectic pair, Poisson {hX,hY}=1")

def positive_effect(H):
    assert H91.dag(H)==H and H91.mm(H91.mm(H,H),H)==H
    Q=H91.scale(H91.plus(eye_n(3),H),F(1,2))
    E=zero_n(6)
    uq=matmul(matmul(U,Q),matadj(U))
    for i in range(3):
        for j in range(3):E[i][j]=uq[i][j]
    assert H91.dag(E)==E
    return E
EX,EY=positive_effect(X),positive_effect(Y)
def expect(E,st):
    z=mattrace(matmul(E,micro(embed(st))))
    assert z.i==0
    return z.r
j=[
  [H91.tr(H91.mm(EX,micro(embed(T)))).r for T in (TX,TY)],
  [H91.tr(H91.mm(EY,micro(embed(T)))).r for T in (TX,TY)]
]
assert j==[[F(0),F(3,10)],[F(-3,10),F(0)]],j
assert H91.rank(j)==2
assert j[0][0]*j[1][1]-j[0][1]*j[1][0]==F(9,100)
assert all(0<=expect(E,rho)<=1 for E in (EX,EY))
print("PASS H102.4: TWO positive calibrated original-H75 output POVMs locally read CONDITIONAL symplectic pair with Jacobian [[0,3/10],[-3/10,0]], det9/100")

# Exact ISOSPECTRAL positive phase states from rational SU2
# unitary V±=(15/17)I01 ∓ i(8/17)X, with spectator level2.
def pulse(sign):
    P01=H91.plus(H91.e(3,0,0),H91.e(3,1,1))
    return H91.plus(
      H91.plus(H91.scale(P01,F(15,17)),
               H91.scale(X,-I*gc(sign*F(8,17)))),
      H91.e(3,2,2))
vp,vm=pulse(1),pulse(-1)
for V in (vp,vm):
    assert H91.mm(H91.dag(V),V)==eye_n(3)
sp=H91.mm(H91.mm(vp,rho),H91.dag(vp))
sm=H91.mm(H91.mm(vm,rho),H91.dag(vm))
assert H91.dag(sp)==sp and H91.dag(sm)==sm
assert H91.tr(sp)==H91.tr(sm)==O
assert sp!=sm
assert sp[0][0]==sm[0][0]==gc(F(739,1156))
assert sp[1][1]==sm[1][1]==gc(F(417,1156))
assert sp[0][1]==I*gc(F(60,289))
assert sm[0][1]==-I*gc(F(60,289))
for st in (sp,sm):
    assert H91.tr(H91.mm(st,st))==gc(F(5,8))
    assert H91.tr(H91.mm(H91.mm(st,st),st))==H91.tr(
        H91.mm(H91.mm(rho,rho),rho))
    assert H85.flag1(st)==F(1668,7225)
rp=tuple(H85.flag1(st) for st in (H85.d0,H85.d1,H85.d2,sp))
rm=tuple(H85.flag1(st) for st in (H85.d0,H85.d1,H85.d2,sm))
assert rp==rm
assert H85.additive(rp)==H85.additive(rm)
assert H85.k4metric(H85.additive(rp))==H85.k4metric(H85.additive(rm))
pp,pm=expect(EY,sp),expect(EY,sm)
assert (pp,pm)==(F(13,50),F(7357,14450)),(pp,pm)
assert pp-pm==F(-72,289)
assert 0<=pp<=1 and 0<=pm<=1
assert all(t[i][j].i==0 for t in real_tangents for i in range(3) for j in range(3))
assert sp[0][1].i and sm[0][1].i
print("PASS H102.5: ISOSPECTRAL source-positive SU2 pair (requires extra X gate) has identical H75 four flags and K4 metric but valid positive Y-POVM gap -72/289")
print("BOUNDARY: source real controls cannot prepare these imaginary coherent states from rho0; the extra X Hamiltonian is NOT generated by original H75/P3/F")
print("BOUNDARY: phase observability != sourced canonical Hamiltonian transport; this one conditional SU2 pair is NOT ADM 6+6 nor Einstein/DeWitt/HDA dynamics")
