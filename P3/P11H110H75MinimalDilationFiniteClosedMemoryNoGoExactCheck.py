"""H110 — original H75 4-Kraus exact minimal pure-ancilla
Stinespring, n-step fresh-ancilla histories and fixed finite
closed-memory infinite-horizon NO-GO.

All source coefficients exact Gaussian rationals. NO new independent
physical P9 Hamiltonian or fictitious intercell source. A 4-level
fresh Stinespring ancilla is mathematically available each step,
not declared a source-derived physical bath.

Exact n=1 dilation checked on all 36 6D matrix units; n=1..3
history isometry and multi-step source checks; Choi rank=4.
The no-go is an ANALYTICAL theorem by finite-dimensional unitary
recurrence combined with original H109 primitive mixing,
not a claim of an exhaustive finite-time numerical search.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    micro,visible,embed,qtrace,M0,M1,U,LK,R60,MBASIS,
    eye_n,zero_n,matmul,matadj,matadd,mattrace,qconj
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P11H109H75PrimitiveMixingTraceOnlyUnitaryIntertwinerExactCheck as H109

assert R60[0][0]==I*gc(F(-32,135))
assert len(LK)==4 and len(MBASIS)==36
I6=eye_n(6)
Z6=zero_n(6)
assert H91.rank(H109.G3)==8
assert H109.sigma==micro(H109.sigma)
assert H109.sigma!=embed(H91.e(3,0,0))

# One-step four-Kraus dilation isometry V: C6 -> C4env⊗C6.
# Rows enumerated k in {00,01,10,11}, then six output sites.
V=[[LK[k][i][j] for j in range(6)]
   for k in range(4) for i in range(6)]
assert len(V)==24 and all(len(row)==6 for row in V)
isometry_gram=[
 [sum((V[r][i].conj()*V[r][j] for r in range(24)),Z0)
  for j in range(6)] for i in range(6)]
assert isometry_gram==I6
kraus_gram=[[mattrace(matmul(matadj(K),L)) for L in LK] for K in LK]
expected_gram=[
 [gc(F(43,25)) if i==j and i<2 else
  gc(F(32,25)) if i==j else Z0
  for j in range(4)] for i in range(4)
]
assert kraus_gram==expected_gram
assert all(kraus_gram[i][i].r>0 for i in range(4))
# Gram is strictly positive diagonal and all Kraus labels (a,b)
# occupy disjoint output/input flag blocks. Complex linear
# independence => exact Choi rank4, pure ancilla dimension >=4.
print("PASS H110.1: original H75 four distinct 6x6 Kraus matrices form exact 24x6 isometry V†V=I6; Kraus Gram diag(43/25,43/25,32/25,32/25) proves Choi rank4, minimal one-step pure ancilla 4")

def rectangular_mm(A,B):
    assert len(A)>0 and len(B)>0 and len(A[0])==len(B)
    n,k,m=len(A),len(B),len(B[0])
    return [[sum((A[i][z]*B[z][j] for z in range(k)),Z0)
             for j in range(m)] for i in range(n)]
def rectangular_dag(A):
    return [[A[j][i].conj() for j in range(len(A))]
            for i in range(len(A[0]))]
Vdag=rectangular_dag(V)
assert rectangular_mm(Vdag,V)==I6
def reduced_one_step(X):
    # Explicit 24D Stinespring output density V X V†, then
    # partial trace of 4D fresh ancilla (not an all-Kraus
    # shortcut pretending environmental access).
    joint=rectangular_mm(rectangular_mm(V,X),Vdag)
    return [[sum((joint[6*k+i][6*k+j] for k in range(4)),Z0)
             for j in range(6)] for i in range(6)]
for E in MBASIS:
    assert reduced_one_step(E)==micro(E)
print("PASS H110.1: partial trace of the explicit actual 24x6 Stinespring isometry EXACTLY reproduces original 6D H75 CPTP map on all 36 physical matrix units")

# Every finite horizon is exactly dilatable by FRESH 4D copies.
# Products enumerated with physical chronological right-to-left
# Kraus application L_kn ... L_k2 L_k1.
products=[I6]
selected=[MBASIS[k] for k in (0,1,4,7,14,22,35)]
for n in range(1,4):
    products=[matmul(L,p) for p in products for L in LK]
    assert len(products)==4**n
    check=Z6
    for p in products:
        check=matadd(check,matmul(matadj(p),p))
    assert check==I6
    tests=MBASIS if n<=2 else selected
    for E in tests:
        reduced=Z6
        for p in products:
            reduced=matadd(reduced,qconj(p,E))
        iterated=E
        for _ in range(n):
            iterated=micro(iterated)
        assert reduced==iterated
    print("PASS H110.2: %d-step fresh-ancilla history has exactly %d original Kraus words, isometry completeness, and actual H75^%d reduced evolution on %d six-level source matrix units"%(n,len(products),n,len(tests)))
print("THEOREM H110.2: for general n, inductively appending a fresh independently initialized 4D ancilla realizes exact H75^n with a sufficient 4^n history-label environment; dimension 4^n is NOT asserted minimal")

# The H109 source has a unique physical stationary state sigma*
# and primitive mixing. Explicit truly positive nonstationary
# original-H75 input rho0 and its first reset output demonstrate
# that the asymptotic limit is distinct even after n>=1.
rho0=embed(H91.e(3,0,0))
rho1=micro(rho0)
sigma=H109.sigma
assert H91.dag(rho0)==rho0 and H91.dag(rho1)==rho1
assert mattrace(rho0)==mattrace(rho1)==mattrace(sigma)==O
assert rho0!=sigma and rho1!=sigma
def flag_one_probability(S):
    return sum((S[i][i] for i in range(3,6)),Z0)
assert flag_one_probability(rho0)==Z0
assert flag_one_probability(rho1)==Z0
assert flag_one_probability(sigma)==gc(F(32,75))
assert H109.H91.rank(H109.G8)==8
print("PASS H110.3: two genuinely positive nonstationary original source inputs n=0,1 have flag1=0, whereas unique primitive H75 stationary sigma*=J(I3/3) has flag1=32/75")

# ANALYTIC FINITE CLOSED-MEMORY NO-GO:
# Any fixed finite-dimensional unitary W has eigenvalues exp(i
# theta_j). The vector of finitely many phases has arbitrarily
# large common return indices n_k with W^n_k -> I (compact
# torus recurrence). Thus for ANY initially prepared joint
# system+environment state xi with system marginal rho0,
# partial tracing W^n_k xi W^-n_k -> rho0.
# But H109 proves Phi_H75^n_k(rho0)->sigma* !=rho0.
# Contradiction. The conclusion is for all n, not a single n.
#
# Even for all n>=1 only, W^(n_k+1)->W and the putative
# channel's n_k+1 output -> its actual n=1 output rho1,
# while H109 mixing forces sigma* !=rho1. Contradiction.
#
# Fixed finite environment dimension d and a SINGLE TIME-
# INDEPENDENT W, WITHOUT resetting ancilla, are essential.
# Infinite reservoirs, refreshed collision chains, explicitly
# time-dependent open controls and finite horizon simulations
# are excluded. This argument is independent of H75's Choi
# rank and stronger/different from H109 trace-only linear
# source->unitary target intertwiner.
assert H109.G1 and H109.G2 and H109.G3
assert sigma==H109.J(H109.cs(eye_n(3),F(1,3)))
assert rho0!=sigma and rho1!=sigma
print("THEOREM H110.3: NO fixed finite-dimensional CLOSED memory, fixed initial bath state and one fixed unitary can reproduce ALL original H75 CPTP iterates n>=0; true H75 primitive limit sigma* conflicts with closed finite-unitary recurrence")
print("THEOREM H110.3 strengthened: impossible EVEN if comparison begins at n>=1, by recurrence to the first-step output rho1 != sigma*")
print("BOUNDARY: exact pure 4D ancilla Stinespring for ONE step succeeds; FRESH reset/retained-history environment 4^n supplies each FINITE n; repeated exact fixed finite closed memory fails across ALL n")
print("BOUNDARY: does not exclude physically sourced infinite bath, coherent infinite collision chain, time-dependent operations, selective measurement, approximate finite horizon, Stinespring reduction with active resetting or a different source sector")
print("BOUNDARY: no P9 Cartan solder/metric or sourced 6-pair ADM phase space, DeWitt/HDA/Einstein, generative P5 Omega-history theorem, non-Markovian process-tensor claim or P11 F completeness is derived")
