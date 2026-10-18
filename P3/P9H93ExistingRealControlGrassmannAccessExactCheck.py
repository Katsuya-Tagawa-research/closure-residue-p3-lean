"""H93: existing H75/H76 real controls vs source-seeded H92 KKS Grassmann orbit.

EXACT source-specific rational check.  No new physical control is added.
The independently specified real hardware gate catalog W,F,UA,UB is
mathematically closed under reversible products and infinitesimal
conjugation; only the original H75 A/B Cayley knobs are assumed continuously
tunable. A full SO6 control Lie closure DOES NOT mean full H92 Gr2(C5)
Poisson-orbit accessibility: the code is not invariant and the 12-coherence
tangent projection has rank9, while the exact preserved-Grassmann tangent
intersection with the entire O6 physical orbit is merely 3D.
"""
from fractions import Fraction as Fr

import P9H92FiveLevelGrassmannKKSResetSilenceExactCheck as H92
from P9H75SemicausalMicroMemorySourceExactCheck import (
    A,B,Fgate,lift,edge_cayley,ONE6,matmul,matadj,matscale,matadd,
    mattrace,qconj,micro,R60
)
from P9H76FeedbackFlagMemoryCPTPExactCheck import W
from P9H24PhaseSensitiveResidueGaugeExactCheck import O,Z0,I,gc

assert R60[0][0] == I*gc(Fr(-32,135))
assert len(H92.pairs)==6
assert H92.sigma==H92.expected
assert H92.physical_seed==H92.decode5(H92.sigma)

def realmat(M):
    for row in M:
        for z in row:assert z.i==0
    return [[z.r for z in row] for row in M]

def rt(M):
    return [list(r) for r in zip(*M)]

def rmm(A,B):
    assert len(A[0])==len(B)
    Bt=rt(B)
    return [[sum((a*b for a,b in zip(row,col)),Fr(0))
             for col in Bt] for row in A]

def sub(A,B):
    return [[x-y for x,y in zip(rowa,rowb)]
            for rowa,rowb in zip(A,B)]

def rcomm(A,B):
    return sub(rmm(A,B),rmm(B,A))

def skvec(K):
    n=len(K)
    assert n==6
    assert all(K[i][j]==-K[j][i] for i in range(n) for j in range(n))
    return [K[i][j] for i in range(n) for j in range(i+1,n)]

def rrank(vectors):
    return H92.rank(vectors) if vectors else 0

A6=lift(A)
B6=lift(B)
controls={
    "W":W,
    "F":Fgate,
    "UA":lift(edge_cayley(A,Fr(1,2))),
    "UB":lift(edge_cayley(B,Fr(2,3))),
}
for name,G in controls.items():
    assert matmul(matadj(G),G)==ONE6,(name,"not unitary")
    assert all(z.i==0 for row in G for z in row),(name,"not REAL")
assert realmat(A6)==sub([[Fr(0)]*6 for i in range(6)],rt(realmat(A6)))
assert realmat(B6)==sub([[Fr(0)]*6 for i in range(6)],rt(realmat(B6)))
print("PASS H93.1: actual W,F,UA,UB are REAL physical orthogonal 6D unitaries; A/B are continuously tunable real skew on-site generators")

# The full exact 5D code isometry of H92. Each listed inherited finite
# gate independently LEAKS some of the positive H92 genuine source seed
# outside this code. The five-level Grassmann orbit is therefore not
# invariant under these already certified 6D operations.
V=H92.V
P=H92.mulrect(V,H92.rectdag(V))
lost=matadd(ONE6,matscale(P,-1))
assert matmul(P,P)==P and matmul(lost,lost)==lost
leaks={}
for name,G in controls.items():
    prob=mattrace(matmul(lost,qconj(G,H92.physical_seed)))
    assert prob.i==0 and Fr(0)<prob.r<Fr(1),(name,prob)
    leaks[name]=prob.r
assert leaks=={
    "W":Fr(144,1475),
    "F":Fr(1280,4779),
    "UA":Fr(512,23895),
    "UB":Fr(87296,807651)
},leaks
print("PASS H93.2: source-seed positive leakage from the H92 U5 code is W=144/1475, F=1280/4779, UA=512/23895, UB=87296/807651")

# Lie algebra of the CLOSED reversible real-control group, with
# continuous original A/B knobs and discrete W,F gates. The conjugate
# infinitesimal directions require reversible group access (or its
# compact closure): not a proof of arbitrary exact finite-time pulses.
wr=realmat(W)
fr=realmat(Fgate)
ar=realmat(A6)
br=realmat(B6)
FAr=rmm(rmm(fr,ar),rt(fr))
FBr=rmm(rmm(fr,br),rt(fr))
WFAr=rmm(rmm(wr,FAr),rt(wr))
WFBr=rmm(rmm(wr,FBr),rt(wr))
base=[ar,br,FAr,FBr,WFAr,WFBr]
assert rrank([skvec(K) for K in base])==6
lie=[]
rows=[]
def register(K):
    v=skvec(K)
    if rrank(rows+[v])>len(rows):
        rows.append(v)
        lie.append(K)
        return True
    return False
for K in base:register(K)
k=0
while k<len(lie):
    for j in range(k):
        register(rcomm(lie[k],lie[j]))
    k+=1
    assert len(lie)<=15
assert len(lie)==15 and rrank(rows)==15
print("PASS H93.3: exact 6-generator conjugation/Lie closure of existing real controls spans all 15 so(6) skew directions under reversible-control closure")

# Work with Galois-exact Gaussian rational *physical* 6D source seed:
# for each 6D real infinitesimal skew K, T=[K,rho_phys] is a genuine
# Hermitian trace-zero orbit tangent (no fictitious Grassmann
# preservation is inferred). The rank of the full physical SO6 orbit
# is 12, coincidentally the *dimension*, not the symplectic target.
def real_as_complex(K):
    return [[gc(v) for v in row] for row in K]

def six_tangent(K):
    kc=real_as_complex(K)
    return matadd(matmul(kc,H92.physical_seed),
                  matscale(matmul(H92.physical_seed,kc),-1))

def v36(T):
    assert len(T)==6
    assert matadj(T)==T
    assert mattrace(T)==Z0
    return (
        [T[i][i].r for i in range(6)]
        +[T[i][j].r for i in range(6) for j in range(i+1,6)]
        +[T[i][j].i for i in range(6) for j in range(i+1,6)]
    )

def five_project(T):
    return H92.mulrect(H92.mulrect(H92.rectdag(V),T),V)

def response12(T):
    b=five_project(T)
    vals=[H92.tr(H92.mm(b,Q)) for Q in H92.allobs]
    assert all(z.i==0 for z in vals)
    return [z.r for z in vals]

real_tangents=[six_tangent(K) for K in lie]
real_orbit_rank=rrank([v36(T) for T in real_tangents])
cross_response_rank=rrank([response12(T) for T in real_tangents])
assert real_orbit_rank==12,real_orbit_rank
assert cross_response_rank==9,cross_response_rank

# The FULL twelve-dimensional U5 code-preserving Grassmann tangent
# subspace is intrinsically different from the SO6-real physical orbit.
# Its embedded generator tangents are tested independently.
grass_tangents=[
    H92.decode5(H92.scale(H92.comm(Q,H92.sigma),-I))
    for Q in H92.allobs
]
assert rrank([v36(T) for T in grass_tangents])==12
combined=rrank([v36(T) for T in real_tangents+grass_tangents])
intersection=real_orbit_rank+12-combined
assert combined==21 and intersection==3,(combined,intersection)
print("PASS H93.4: although physical REAL SO6 unitary orbit is dimension12, H92 cross-flag 12-response differential rank is ONLY9")
print("PASS H93.4: exact intersection of real SO6 tangents with code-preserving full U5 Grassmann-12 tangents has dimension3 (combined 21D in physical 6D Hermitian space)")

# At the seed, W's real continuous flag generator produces off-flag
# coherences. The ACTUAL four-Kraus CPTP reset erases this first-order
# off-flag perturbation, even though finite W can alter populations.
Kflag=[[Fr(0) for j in range(6)] for i in range(6)]
for j in range(3):
    Kflag[j][j+3]=Fr(-1)
    Kflag[j+3][j]=Fr(1)
assert skvec(Kflag)
Tflag=six_tangent(Kflag)
assert Tflag!=[[Z0]*6 for _ in range(6)]
assert micro(Tflag)==[[Z0]*6 for _ in range(6)]
print("PASS H93.5: genuine continuous flag-rotation generator is first-order silent through the original H75 reset; finite W leaks and need not be fully silent")

print("BOUNDARY: lie algebra so6 uses REVERSIBLE closure and continuous existing H75 site Cayley controls; fixed W,F alone do not certify arbitrary timed pulses")
print("BOUNDARY: the real-control orbit is NOT the full 12D H92 compact complex Grassmann orbit; all four inherited gates fail invariant 5D code support")
print("BOUNDARY: no physical sourced ADM symplectic/Hamiltonian map, DeWitt kinetic, full off-shell HDA, Einstein dynamics or F axiomatization")
