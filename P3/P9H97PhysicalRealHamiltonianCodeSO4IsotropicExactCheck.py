"""H97: EXACT true H75-source code-preserving REAL Hamiltonian group is SO4,
its orbit at genuine H92 seed is 3D and KKS-isotropic, not ADM 6+6.

The entire full SO6 control Lie closure is a GENEROUS source-declared
reversible group completion, not a certification of exact arbitrary
finite-time coherent physical control. The original H75 A/B continuous
site generators leak out of the genuine five-level source support.
No new complex phase knob, Hamiltonian, ADM field or gravity action.
"""
from fractions import Fraction as F
from itertools import combinations

from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import R60,ONE6
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P9H92FiveLevelGrassmannKKSResetSilenceExactCheck as H92
import P9H93ExistingRealControlGrassmannAccessExactCheck as H93

assert R60[0][0]==I*gc(F(-32,135))
assert H91.rank(H92.P)==12
assert H93.real_orbit_rank==12 and H93.cross_response_rank==9
assert H92.physical_seed==H92.decode5(H92.sigma)

n=6
# The original H42/H75 complex unitary column0 in the SECOND flag:
# its complex line is the single exact sixth Hilbert mode excluded
# by the full original H79/H92 five-level CP checkpoint support.
zeta=[Z0,Z0,Z0]+[H92.U[i][0] for i in range(3)]
assert zeta==[
    Z0,Z0,Z0,I*gc(F(2,3)),gc(F(-2,3)),-I*gc(F(1,3))]
a=[z.r for z in zeta]
b=[z.i for z in zeta]
def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))
assert dot(a,b)==0
assert dot(a,a)==F(4,9)
assert dot(b,b)==F(5,9)
assert dot(a,a)!=dot(b,b)
assert dot(a,a)+dot(b,b)==1
orth=[[zeta[i]*zeta[j].conj() for j in range(6)]
      for i in range(6)]
assert orth==H93.lost
assert H91.mm(orth,orth)==orth
assert H91.mm(orth,H92.physical_seed)==H91.zero(6)
print("PASS H97.1: original H75 complex U first column produces genuine excluded unit vector zeta; Re and Im orthogonal unequal squares 4/9 and 5/9")

skews=[]
pairs=list(combinations(range(6),2))
for p,q in pairs:
    K=[[F(0) for _ in range(6)] for __ in range(6)]
    K[p][q]=F(1);K[q][p]=F(-1)
    skews.append(K)
assert len(skews)==15
def mv(K,v):
    return [sum((K[i][j]*v[j] for j in range(6)),F(0))
            for i in range(6)]
def mulz(K):
    return [
        sum((gc(K[i][j])*zeta[j] for j in range(6)),Z0)
        for i in range(6)
    ]
# Necessary AND sufficient because K is real skew and a,b have
# unequal norms: line-preserving Kzeta=i*lambda*zeta requires
# lambda*(||a||²-||b||²)=0, hence lambda=0, Ka=Kb=0.
constraints=[]
for v in (a,b):
    for i in range(6):
        constraints.append([mv(K,v)[i] for K in skews])
assert len(constraints)==12 and len(constraints[0])==15

def nullspace(A):
    A=[[F(x) for x in row] for row in A]
    rows=len(A);cols=len(A[0]);r=0;pivot=[]
    for c in range(cols):
        k=next((k for k in range(r,rows) if A[k][c]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r]
        f=A[r][c]
        A[r]=[x/f for x in A[r]]
        for k in range(rows):
            if k!=r and A[k][c]:
                f=A[k][c]
                A[k]=[x-f*y for x,y in zip(A[k],A[r])]
        pivot.append(c);r+=1
        if r==rows:break
    free=[c for c in range(cols) if c not in pivot]
    vectors=[]
    for f in free:
        v=[F(0)]*cols
        v[f]=F(1)
        for row,p in enumerate(pivot):v[p]=-A[row][f]
        vectors.append(v)
    assert r==len(pivot) and len(vectors)==cols-r
    return vectors

coeff=nullspace(constraints)
assert H91.rank(constraints)==9
assert len(coeff)==6 and H91.rank(coeff)==6

def lincomb(v):
    return [[sum((v[k]*skews[k][i][j] for k in range(15)),F(0))
             for j in range(6)] for i in range(6)]
code_lie=[lincomb(v) for v in coeff]
assert all(mulz(K)==[Z0]*6 for K in code_lie)
assert all(mv(K,a)==[F(0)]*6 and mv(K,b)==[F(0)]*6
           for K in code_lie)
assert H91.rank([H93.skvec(K) for K in code_lie])==6
for K in code_lie:
    assert H93.rcomm(K,H93.rt(K))==H93.sub(
        H93.rmm(K,H93.rt(K)),H93.rmm(H93.rt(K),K))
for K in code_lie:
    for L in code_lie:
        C=H93.rcomm(K,L)
        assert mulz(C)==[Z0]*6
        assert H91.rank([H93.skvec(X) for X in code_lie]+[H93.skvec(C)])==6
print("PASS H97.1: exact rational rank9 12x15 annihilator and six-dimensional code-preserving so4 Lie algebra, closed under all 36 commutators")

# At the genuine H75 seed the entire SO4 coherent code-preserving
# moment-map action is restricted to a 3D orbit, NOT a 12D symplectic
# KKS orbit. Its pulled-back KKS form is exactly ZERO.
source=H92.physical_seed
tangents=[H93.six_tangent(K) for K in code_lie]
assert H91.rank([H93.v36(T) for T in tangents])==3
for T in tangents:
    assert H91.dag(T)==T
    assert H91.tr(T)==Z0
    assert H91.mm(orth,T)==H91.zero(6)
    assert H91.mm(T,orth)==H91.zero(6)
    assert H91.rank([H93.v36(X) for X in H93.grass_tangents]+
                    [H93.v36(T)])==12

brackets=[]
for K in code_lie:
    line=[]
    for L in code_lie:
        # H_K=iK, H_L=iL; this is -i*Tr[rho [H_K,H_L]]
        HK=H93.real_as_complex(K)
        HL=H93.real_as_complex(L)
        pb=I*H91.tr(H91.mm(source,H91.comm(HK,HL)))
        assert pb==Z0
        line.append(pb)
    brackets.append(line)
assert brackets==[[Z0]*6 for _ in range(6)]
print("PASS H97.2: true H75 source yields rank3 physical SO4 tangent orbit inside 12D H92 Grassmann, with IDENTICALLY ZERO 6x6 KKS Poisson matrix (isotropic)")

# Physical continuous original H75 real site Hamiltonians A/B
# *fail* to preserve the code. The second-derivative leakage
# coefficients for e^{tK} rho e^{-tK} are exact, positive and
# evaluated using real SOURCE-POSITIVE rho rather than a surrogate.
for name,K,norm_expected,c_expected in (
    ("A",H93.ar,F(8,9),F(128,4779)),
    ("B",H93.br,F(5,9),F(464,4779)),
):
    kz=mulz(K)
    assert kz!=[Z0]*6
    norm=sum((w.r*w.r+w.i*w.i for w in kz),F(0))
    assert norm==norm_expected
    rk=[
        sum((source[i][j]*kz[j] for j in range(6)),Z0)
        for i in range(6)
    ]
    leakage=sum((kz[i].conj()*rk[i] for i in range(6)),Z0)
    assert leakage.i==0 and leakage.r==c_expected
    T=H93.six_tangent(K)
    assert H91.mm(orth,T)!=H91.zero(6)
    print("PASS H97.3: genuine H75 "+name+
          " Hamiltonian violates invariant five-level code: ||Kzeta||²="+
          str(norm_expected)+", positive t² leakage coefficient="+str(c_expected))

# The target independent ADM six momentum translations have tangent
# rank6 at any local unreduced T*SPD(3) point. A local symplectic map
# J that intertwines each such X_(p_i) with a source-accessible h_K
# is therefore impossible AT THIS source seed, since all available
# code-preserving real-control Hamiltonian fields span only 3D.
rank_physical=H91.rank([H93.v36(T) for T in tangents])
assert rank_physical==3 and rank_physical<6
assert H91.rank(H92.P)==12
print("PASS H97.4: six independent ADM canonical momentum-translation Hamiltonian fields CANNOT be physically intertwined with rank3 code-preserving REAL source controls at genuine H75 seed")
print("BOUNDARY: this scoped control-intertwining No-Go does NOT exclude ABSTRACT local Darboux maps or sourced COMPLEX/ancillary/historical/field Hamiltonians")
print("BOUNDARY: no H75 source-derived physical DeWitt kinetic (5+,1-), nonuniform off-shell HDA, Einstein field equations or F generative completeness")
