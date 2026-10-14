"""H33: locality versus original P3 Krylov sector and actual P6 Xi provenance.

Exact rational-Gaussian audit. This imports H32's already audited single
connected unitary CPTP channel. All sectors below are explicitly *choices*
of static microscopic inputs, not automatically the frozen P6 J_N.

Nearest-neighbor edge truncation is a LINEAR SCHUR projection and is
NOT a completely positive quantum channel; we give an exact PSD witness.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    H,U3,Phi,rr,xi,scale,add,com,dagger,unit,z,diag,mm
)
N=3
def ploc(a):
    # Keep only length-one offdiagonal entries of the path 0--1--2.
    return [[a[i][j] if abs(i-j)==1 else Z0
             for j in range(N)] for i in range(N)]
def keepdiag_nearest(a):
    # The full Schur mask preserves diagonal and adjacent edges.
    return [[a[i][j] if abs(i-j)<=1 else Z0
             for j in range(N)] for i in range(N)]
def first_lie(a):
    return xi(scale(a,I/F(2)))
A01=add(unit(0,1),scale(unit(1,0),-1))
B12=add(unit(2,1),scale(unit(1,2),-1))
Q01=scale(add(unit(0,1),unit(1,0)),-I)
Q12=scale(add(unit(1,2),unit(2,1)),-I)
A02=add(unit(0,2),scale(unit(2,0),-1))
Q02=scale(add(unit(0,2),unit(2,0)),-I)

# Single Phi from H32 already passed genuine P3 residue and full Xi rank.
h10=H[1][0]
assert h10[0][2]==C(F(-4,27),F(8,27))!=Z0
assert rr([first_lie(h) for j in (1,2,3) for h in H[j]])==6
assert ploc(h10)[0][2]==Z0 and ploc(h10)[2][0]==Z0
# Along the path d(0,2)=2, so H_1 (hence H_3) violates any
# P6 inherited sector with hard local radius r0=1 on this graph.
# This is a genuine locality obstruction, not mere missing provenance.

# The linearly truncated candidate P_loc(H_k) has real Xi rank 2,4,4.
for depth,expect in ((1,2),(2,4),(3,4)):
    h=[ploc(t) for j in range(1,depth+1) for t in H[j]]
    image=[first_lie(t) for t in h]
    assert rr(image)==expect
    assert all(t[0][2]==Z0 and t[2][0]==Z0 for t in image)
    for target,is_in in zip((A01,B12,Q01,Q12,A02,Q02),
                            (True,depth>=2,depth>=2,depth>=2,False,False)):
        assert (rr(image+[target])==rr(image))==is_in, (depth,target)
# A concrete sufficient purely algebraic STATIC candidate at r0=1:
# J_loc = span_C{P_loc(H1), P_loc(H2)}; its Xi image is all four
# nearest-neighbor anti-Hermitian control quadratures.
local_h=[ploc(t) for j in (1,2) for t in H[j]]
local_xi=[first_lie(h) for h in local_h]
assert rr(local_xi)==4
assert rr(local_xi+[A01,B12,Q01,Q12])==4
assert rr(local_xi+[A02])==5

# The P6 MASA derivation action is injective on offdiagonal
# anti-Hermitian generators (diagonal phases are the only kernel).
D=[unit(j,j) for j in range(3)]
def action(x):return [com(x,d) for d in D]
def action_vector(x):
    result=[]
    for d in D:
        for i in range(N):
            for j in range(N):
                result.extend((com(x,d)[i][j].r,com(x,d)[i][j].i))
    return result
assert len(action_vector(A01))==2*N*N*N
assert action_vector(A01)!=action_vector(B12)
assert action_vector(Q01)!=action_vector(A01)
# For any x in this zero-diagonal generator basis, action(x)=0
# iff x=0, and rank of transformed spans equals rank of operators.
for seq in ([A01,B12,Q01,Q12],[A01,B12,Q01,Q12,A02,Q02]):
    # Use distinct diagonal entries to recover all offdiag components.
    d0=add(unit(1,1),scale(unit(2,2),2))
    commuted=[com(x,d0) for x in seq]
    assert rr(commuted)==rr(seq)

# Stronger support-graph insufficiency:
# A rank-one complex *linked* sector has both edges present in its
# support graph, but only TWO real Xi directions (a locked pair).
E01=unit(0,1);E12=unit(1,2)
Jlocked=add(E01,E12)
locked=[xi(Jlocked),xi(scale(Jlocked,I))]
assert rr(locked)==2
assert all(ploc(t)==t for t in locked)
assert rr(locked+[A01])==3 and rr(locked+[B12])==3
assert rr(locked+[Q01])==3
# Same locality and connected support, but independent edge controls
# are unavailable. By contrast the independent complex E01 and E12
# microscopic sector gives exactly all 4 local quadratures.
unlocked=[xi(E01),xi(scale(E01,I)),xi(E12),xi(scale(E12,I))]
assert rr(unlocked)==4
assert rr(unlocked+[A01,B12,Q01,Q12])==4
# Whether this J_unlocked is physically inherited cannot be inferred
# from the one-channel U3 alone.

# Local Schur truncation is not a physical CPTP channel.
# Its full diagonal-preserving mask is M=[[1,1,0],[1,1,1],[0,1,1]].
mask=keepdiag_nearest([[O for j in range(N)] for i in range(N)])
v=(O,-O,O)
quadratic=sum((v[i]*mask[i][j]*v[j] for i in range(N)
               for j in range(N)),Z0)
assert quadratic==-O
# From normalized positive rho=|+++><+++|=all-ones/3,
# the Schur-filtered output has strictly negative expectation -1/3.
rho=[[O/F(3) for _ in range(N)] for _ in range(N)]
bad=keepdiag_nearest(rho)
expectation=sum((v[i]*bad[i][j]*v[j] for i in range(N)
                 for j in range(N)),Z0)
assert expectation==C(F(-1,3))
assert sum((bad[i][i] for i in range(N)),Z0)==O

# A concise, precise conditional bridge statement:
# xi(J_loc) contains all 4 nearest-neighbor controls; if and only
# if P6 independently fixes J_N with corresponding Xi image
# containing these 4 generators, they meet FIRST-RESIDUE ACCESS
# at the coherent algebraic *derivation* level. It does not grant
# their actual physical controls or CPTP implementation.
print("PASS H33: H32 original P3 H1 has radius-two 02 coherence")
print("PASS H33: radius-one P6 locality excludes full H3 sector")
print("PASS H33: nearest-neighbor Krylov linear projections Xi ranks 2/4/4")
print("PASS H33: local rank-four candidate includes path and H30 quadrature")
print("PASS H33: same two-edge connected support can have locked Xi rank two")
print("PASS H33: local projection fails positivity on a pure state")
print("SCOPE: static Xi containment needs extra J_N identification, not P6 physical access")
