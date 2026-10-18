"""H91 exact source-specific reset-checkpoint KKS rank vs ADM 12D.

Checks genuine unchanged H75 Kraus source and H79/H80 minimal checkpoint
M3 direct-sum M2 quantum memory.  The source-state image is rank-9
complex-linearly, real affine dimension 8, whereas intrinsic block
Lie-Poisson rank is <=8 (rank4 at faithful source rho=I3/3).  A full
ADM six-pair canonical *local Poisson diffeomorphism* is impossible if
the physical domain is restricted to this unextended single-checkpoint
state/algebra with its natural block KKS bracket. It says nothing
universal about multi-cell, historical or externally enriched domains.
"""
from fractions import Fraction as F
from itertools import combinations

from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H75SemicausalMicroMemorySourceExactCheck import (
    micro,embed,envblock,matmul,matadj,U,M0,M1,R60
)

assert R60[0][0]==I*gc(F(-32,135))
assert R60[1][1]==I*gc(F(16,135))
assert R60[2][2]==I*gc(F(16,135))

def zero(n):
    return [[Z0 for j in range(n)] for i in range(n)]

def e(n,i,j):
    M=zero(n);M[i][j]=O;return M

def plus(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A))]
            for i in range(len(A))]

def scale(A,s):
    return [[s*v for v in row] for row in A]

def minus(A,B):
    return plus(A,scale(B,-1))

def mm(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),Z0)
             for j in range(n)] for i in range(n)]

def dag(A):
    n=len(A)
    return [[A[j][i].conj() for j in range(n)] for i in range(n)]

def comm(A,B):
    return minus(mm(A,B),mm(B,A))

def tr(A):
    return sum((A[i][i] for i in range(len(A))),Z0)

def J5(X):
    """Block-normal-form source checkpoint, five physical output levels."""
    Y=zero(5)
    d=(F(1),F(3,5),F(3,5))
    for i in range(3):
        for j in range(3):
            Y[i][j]=gc(d[i]*d[j])*X[i][j]
    for i in range(2):
        for j in range(2):
            Y[3+i][3+j]=gc(F(16,25))*X[1+i][1+j]
    return Y

for a in range(3):
    for b in range(3):
        X=e(3,a,b)
        raw=micro(embed(X))
        first=matmul(matmul(matadj(U),envblock(raw,0,0)),U)
        second=matmul(matmul(matadj(U),envblock(raw,1,1)),U)
        expected=J5(X)
        assert first==[row[:3] for row in expected[:3]]
        assert second==[
            [expected[2+i][2+j] if i>=1 and j>=1 else Z0
             for j in range(3)] for i in range(3)
        ]
        assert envblock(raw,0,1)==zero(3) and envblock(raw,1,0)==zero(3)
        assert tr(expected)==tr(X)
print("PASS H91.1: true original H75 4-Kraus source agrees on ALL 9 qutrit matrix units with rotated M3+M2 five-dimensional checkpoint state")

def hermX(n,a,b):
    return plus(e(n,a,b),e(n,b,a))

def hermY(n,a,b):
    return scale(minus(e(n,a,b),e(n,b,a)),-I)

def block_coords(M):
    """Real coordinates of Hermitian block M3⊕M2 (dimension 5+4*2=13)."""
    assert dag(M)==M
    pairs=((0,1),(0,2),(1,2),(3,4))
    v=[M[i][i].r for i in range(5)]
    assert all(M[i][i].i==0 for i in range(5))
    for a,b in pairs:v.append(M[a][b].r)
    for a,b in pairs:v.append(-M[a][b].i)
    assert len(v)==13
    assert all(M[a][b]==Z0 for a in range(3) for b in range(3,5))
    return v

def rank(rows):
    if not rows:return 0
    M=[[F(x) for x in row] for row in rows]
    h=len(M); w=len(M[0]); i=0
    for j in range(w):
        k=next((k for k in range(i,h) if M[k][j]),None)
        if k is None:continue
        M[i],M[k]=M[k],M[i]
        pivot=M[i][j]
        M[i]=[v/pivot for v in M[i]]
        for k in range(i+1,h):
            if M[k][j]:
                factor=M[k][j]
                M[k]=[v-factor*u for v,u in zip(M[k],M[i])]
        i+=1
        if i==h:break
    return i

basis_q=[e(3,i,i) for i in range(3)]
for a,b in combinations(range(3),2):
    basis_q.extend((hermX(3,a,b),hermY(3,a,b)))
assert len(basis_q)==9
assert rank([block_coords(J5(B)) for B in basis_q])==9
traceless=[minus(e(3,0,0),e(3,2,2)),
           minus(e(3,1,1),e(3,2,2))] + basis_q[3:]
assert len(traceless)==8
assert all(tr(B)==Z0 for B in traceless)
assert rank([block_coords(J5(B)) for B in traceless])==8

rho_ref=scale(plus(plus(e(3,0,0),e(3,1,1)),e(3,2,2)),F(1,3))
rho_gen=plus(plus(scale(e(3,0,0),F(1,2)),scale(e(3,1,1),F(1,3))),
             scale(e(3,2,2),F(1,6)))
sigma_ref=J5(rho_ref)
sigma_gen=J5(rho_gen)
assert [sigma_ref[i][i].r for i in range(5)]==[
    F(1,3),F(3,25),F(3,25),F(16,75),F(16,75)]
assert [sigma_gen[i][i].r for i in range(5)]==[
    F(1,2),F(3,25),F(3,50),F(16,75),F(8,75)]
assert tr(sigma_ref)==O and tr(sigma_gen)==O
assert all(sigma_ref[i][i].r>0 and sigma_gen[i][i].r>0
           for i in range(5))
print("PASS H91.1: actual reset-family Hermitian image rank9, trace-one physical tangent rank8; two faithful source states exact")

# All Hermitian generators of M3⊕M2, including the two central
# populations.  In particular NO coherent cross-block observables.
pairs=((0,1),(0,2),(1,2),(3,4))
basis=[e(5,i,i) for i in range(5)]
basis += [hermX(5,a,b) for a,b in pairs]
basis += [hermY(5,a,b) for a,b in pairs]
assert len(basis)==13
assert rank([block_coords(B) for B in basis])==13

def bracket(sig,A,B):
    z=-I*tr(mm(sig,comm(A,B)))
    assert z.i==0
    return z.r

def poisson(sig):
    return [[bracket(sig,A,B) for B in basis] for A in basis]

pref=poisson(sigma_ref)
pgen=poisson(sigma_gen)
assert rank(pref)==4
assert rank(pgen)==8
assert len(pref)==len(pgen)==13
assert all(pref[i][j]==-pref[j][i] and
           pgen[i][j]==-pgen[j][i] for i in range(13) for j in range(13))
assert all(pref[i][j]==0 and pgen[i][j]==0
           for i in range(5) for j in range(13))
# Four independent within-block root planes; two vanish at the
# symmetric reference and all four activate at the generic state.
for k,(a,b) in enumerate(pairs):
    vref=2*(sigma_ref[a][a].r-sigma_ref[b][b].r)
    vgen=2*(sigma_gen[a][a].r-sigma_gen[b][b].r)
    assert pref[5+k][9+k]==vref
    assert pgen[5+k][9+k]==vgen
    assert pgen[5+k][9+k]!=0
    for l in range(4):
        if l!=k:
            assert pref[5+k][9+l]==0
            assert pgen[5+k][9+l]==0
assert [pref[5+k][9+k] for k in range(4)]==[
    F(32,75),F(32,75),F(0),F(0)]
print("PASS H91.2: all thirteen physical checkpoint Hermitian generators have EXACT Lie-Poisson ranks 4 at J(I3/3), 8 at generic J(diag(1/2,1/3,1/6))")

# Independent local Casimir gradients: powers of each block state
# separately (k=0..2 on M3 and k=0..1 on M2).  Their spans have
# rank5 on 13D ambient real dual, rank4 mod the trace-one Casimir.
d=[sigma_gen[i][i].r for i in range(5)]
grad=[]
for block in ((0,1,2),(3,4)):
    for k in range(len(block)):
        G=zero(5)
        for i in block:G[i][i]=gc(d[i]**k)
        grad.append(G)
        assert all(bracket(sigma_gen,G,B)==0 for B in basis)
assert rank([block_coords(G) for G in grad])==5
print("PASS H91.2: five independent ambient spectral Casimir gradients (four after trace one), hence generic Poisson rank8 on 12-real-dimensional ambient checkpoint states")

# Target six unconstrained ADM canonical position/momentum pairs:
# natural Poisson bivector has rank 12; no rank-preserving local
# Poisson diffeomorphism to a rank<=8 intrinsic checkpoint KKS leaf.
adm=[[F(0) for j in range(12)] for i in range(12)]
for i in range(6):
    adm[i][6+i]=F(1)
    adm[6+i][i]=F(-1)
assert rank(adm)==12
assert max(rank(pref),rank(pgen))<rank(adm)
assert 12-rank(pgen)==4
assert 12-rank(pref)==8
print("PASS H91.3: ADM canonical Poisson rank12 exceeds native block KKS rank<=8; product-completion deficits >=4 generic / >=8 at reference")

print("BOUNDARY: 8D source output, 12D ambient block trace-one state space, 8D generic KKS leaf and 12D ADM are DISTINCT typed objects")
print("BOUNDARY: no non-product/time-history/multi-cell/extra-control universal no-go; true ADM solder, DeWitt kinetics, off-shell HDA, Einstein dynamics and F completeness OPEN")
