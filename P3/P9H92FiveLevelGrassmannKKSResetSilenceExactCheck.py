"""H92: source-realized 5D 3+2 KKS Grassmann orbit, coherent access and reset loss.

Unchanged original H75 four-Kraus CPTP reset. A coherent U5 flag-crossing
intervention is an INDEPENDENT physical control assumption, not P3-sourced
or physically demonstrated. Full U5 coadjoint orbit Gr_2(C5) is 12D but
the H79 post-reset intrinsic M3+M2 KKS algebra stays rank<=8.
"""
from fractions import Fraction as F
from itertools import product

from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    micro,embed,U,R60,qtrace,matmul,matadj,mattrace
)
from P9H91CheckpointKKSRankADMObstructionExactCheck import (
    J5,zero,e,plus,minus,scale,mm,dag,comm,tr,rank,bracket
)
assert R60[0][0]==I*gc(F(-32,135))

rho_input=plus(plus(scale(e(3,0,0),F(9,59)),
                    scale(e(3,1,1),F(25,59))),
               scale(e(3,2,2),F(25,59)))
assert tr(rho_input)==O
sigma=J5(rho_input)
la,lb=F(9,59),F(16,59)
expected=zero(5)
for a in range(3):expected[a][a]=gc(la)
for b in range(3,5):expected[b][b]=gc(lb)
assert sigma==expected and tr(sigma)==O
assert 3*la+2*lb==1 and la!=lb
print("PASS H92.1: true unchanged H75 positive qutrit input (9,25,25)/59 has exactly 3+2 source checkpoint eigenvalues 9/59 and 16/59")

def mulrect(A,B):
    assert len(A[0])==len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Z0)
             for j in range(len(B[0]))] for i in range(len(A))]
def rectdag(A):
    return [[A[j][i].conj() for j in range(len(A))]
            for i in range(len(A[0]))]
def decode5(X):
    return mulrect(mulrect(V,X),rectdag(V))

# Physical columns of the source rotated-normal-form five-level code:
# flag0 ⊗ U e0/e1/e2, flag1 ⊗ U e1/e2.
V=[[Z0 for j in range(5)] for i in range(6)]
for a in range(3):
    for j in range(3):
        V[a][j]=U[a][j]
for a in range(3):
    for j in range(2):
        V[a+3][j+3]=U[a][j+1]
assert mulrect(rectdag(V),V)==[
    [O if a==b else Z0 for b in range(5)] for a in range(5)]
physical_seed=micro(embed(rho_input))
assert decode5(sigma)==physical_seed
assert mattrace(physical_seed)==O
print("PASS H92.1: explicit 6x5 physical flag/site isometry decodes source Grassmann seed to EXACT original H75 CPTP reset output")

pairs=tuple((a,b) for a in range(3) for b in range(3,5))
assert len(pairs)==6

def X(a,b):
    return plus(e(5,a,b),e(5,b,a))
def Y(a,b):
    return scale(minus(e(5,a,b),e(5,b,a)),-I)

xs=[X(*p) for p in pairs]
ys=[Y(*p) for p in pairs]
allobs=xs+ys
assert all(dag(A)==A for A in allobs)

P=[[bracket(sigma,A,B) for B in allobs] for A in allobs]
assert len(P)==12 and rank(P)==12
for i in range(6):
    for j in range(6):
        assert P[i][j]==0 and P[i+6][j+6]==0
        assert P[i][j+6]==(2*(la-lb) if i==j else 0)
        assert P[i+6][j]==(-2*(la-lb) if i==j else 0)
assert 2*(la-lb)==F(-14,59)
assert 25-(3**2+2**2)==12
print("PASS H92.2: full U5 coadjoint orbit of actual-source 3+2 eigenstate is Gr2(C5), real dim12; exact 12x12 cross-flag KKS rank12 with six pairings -14/59")

# No mathematical cross-block X/Y observable is in the declared M3⊕M2
# CPTP checkpoint algebra, whose U3×U2 orbit fixes this seed point.
assert all(sigma[i][i]==gc(la) for i in range(3))
assert all(sigma[i][i]==gc(lb) for i in range(3,5))
assert all(bracket(sigma,A,B)==0
           for A in [e(5,i,i) for i in range(5)]
           for B in allobs)

# At the reference basepoint, all full-U5 orbit tangents have cross
# flag blocks only. Original micro reset annihilates every one.
for G in allobs:
    tangent=scale(comm(G,sigma),-I)
    assert tangent!=zero(5)
    assert all(tangent[i][j]==Z0
               for i in range(5) for j in range(5)
               if (i<3)==(j<3))
    assert micro(decode5(tangent))==[
        [Z0 for _ in range(6)] for _ in range(6)]
print("PASS H92.3: all twelve nontrivial rank12 Grassmann tangent directions are killed at FIRST ORDER by the GENUINE original H75 CPTP reset")

# Rational entangling flag-coherence pulse and its opposite phase.
# Both are unitary on the SAME source Hilbert-five carrier and have
# identical blockwise populations but opposite imaginary coherence.
def pulse(sign):
    M=[[O if i==j else Z0 for j in range(5)] for i in range(5)]
    a,b=0,3
    M[a][a]=gc(F(3,5))
    M[b][b]=gc(F(3,5))
    M[a][b]=-I*gc(F(sign*4,5))
    M[b][a]=-I*gc(F(sign*4,5))
    assert mm(dag(M),M)==[
        [O if i==j else Z0 for j in range(5)] for i in range(5)]
    return M
def apply(G,X):
    return mm(mm(G,X),dag(G))
rp=apply(pulse(1),sigma)
rm=apply(pulse(-1),sigma)
assert dag(rp)==rp and dag(rm)==rm
assert tr(rp)==tr(rm)==O
assert rp!=rm
assert rp[0][3]==-I*gc(F(84,1475))
assert rm[0][3]==I*gc(F(84,1475))
assert rp[0][0]==rm[0][0]==gc(la+F(112,1475))
assert rp[3][3]==rm[3][3]==gc(lb-F(112,1475))
assert all(rp[i][j]==rm[i][j] if (i<3)==(j<3)
           else rp[i][j]==-rm[i][j]
           for i in range(5) for j in range(5))

# The actual H75 full-six-dimensional physical map ignores source input
# cross-flag coherences, not merely a modelled abstract block projection.
reset_p=micro(decode5(rp))
reset_m=micro(decode5(rm))
assert reset_p==reset_m
assert reset_p!=physical_seed
assert mattrace(reset_p)==mattrace(reset_m)==O

# A positive effect Q=(I+Y03)/2 on 5D; its 6D physical embedded
# effect VQV^† obeys 0<=Q<=I via Y^3=Y (eigenvalues -1,0,+1).
coherence=Y(0,3)
assert mm(mm(coherence,coherence),coherence)==coherence
eye5=[[O if i==j else Z0 for j in range(5)] for i in range(5)]
Q=scale(plus(eye5,coherence),F(1,2))
assert dag(Q)==Q and mm(Q,Q)!=Q # valid unsharp positive effect
prob_p=tr(mm(Q,rp))
prob_m=tr(mm(Q,rm))
assert prob_p.i==prob_m.i==0
assert F(0)<=prob_p.r<=F(1)
assert F(0)<=prob_m.r<=F(1)
assert prob_p.r-prob_m.r==F(168,1475)
assert decode5(Q)!=zero(6)
print("PASS H92.4: genuine physical positive pre-reset orbit states are distinguished by positive cross-flag POVM (difference 168/1475), yet have IDENTICAL post-reset 6D CPTP output")
print("BOUNDARY: U5 interblock coherent pulse and phase readout are INDEPENDENT physical AX-OA, not H75/P3/F sourced")
print("BOUNDARY: full rank12 pre-reset Grassmann KKS orbit is compact/global nonexact, its ordinary H75 reset loses first-order Grassmann tangent memory")
print("BOUNDARY: local ADM Darboux possibility is NOT physically sourced DeWitt kinetic/HDA/Einstein/F-completeness")
