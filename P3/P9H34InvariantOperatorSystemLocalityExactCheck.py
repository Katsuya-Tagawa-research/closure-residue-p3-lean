"""H34: exact minimal Phi-invariant closure versus radius-one locality.

A SINGLE connected 3-site CPTP unitary Phi from H32 is fixed.
On the 0--1--2 path, the radius-one operator system O1 has
complex dimension seven. Its minimal Phi-invariant extension is M3(C).
The 4-dimensional traceless path offdiagonal sector instead closes to
sl3(C) (dimension eight), not to another radius-one sector.

Original P3 residue, microscopic static P6 Xi selection, dynamical
invariance, and experimental controls are distinct logical layers.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C, I, O, Z0
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    Phi,H,U3,rr,unit,z,eye,scale,add,sub,dagger,diag,mm,xi
)
N=3
def iszero(a):return a==z()
def P1(a):
    return [[a[i][j] if abs(i-j)<=1 else Z0 for j in range(N)]
            for i in range(N)]
def P1off(a):
    return [[a[i][j] if abs(i-j)==1 else Z0 for j in range(N)]
            for i in range(N)]
def cr(mats):
    if not mats:return 0
    # Complex dimension = half the underlying real dimension of span
    # over R of {v_j, i v_j}; rr is exact Gaussian-Fraction real rank.
    d=rr(mats+[scale(a,I) for a in mats])
    assert d%2==0
    return d//2
def saturate(seed):
    S=[]
    for a in seed:
        if cr(S+[a])>len(S):S.append(a)
    ranks=[len(S)]
    for _ in range(12):
        snap=S[:]
        for a in snap:
            b=Phi(a)
            if cr(S+[b])>len(S):S.append(b)
        ranks.append(len(S))
        if len(S)==len(snap):return S,ranks
    raise AssertionError("Phi-invariant closure did not stabilize")
D=[unit(i,i) for i in range(N)]
path=[unit(0,1),unit(1,0),unit(1,2),unit(2,1)]
chord=[unit(0,2),unit(2,0)]
O1=D+path
assert cr(O1)==7
assert all(P1(a)==a for a in O1)
assert cr(O1+chord)==9
assert mm(dagger(U3),U3)==eye()

# Original H32 Phi is NOT exact radius-one support preserving.
h=Phi(D[0])
assert h[0][2]==C(F(-4,27),F(8,27))
assert P1(h)!=h
v=Phi(h)
det=h[0][2]*v[2][0]-h[2][0]*v[0][2]
assert det==C(F(0),F(3520,19683))
# A first-time image provides one complex chord direction; second-time
# image an independent one. Their classes modulo O1 fill C^2.
assert cr(O1+[h])==8
assert cr(O1+[h,v])==9
S,ranks=saturate(O1)
assert len(S)==9 and cr(S)==9
assert all(cr(S+[Phi(a)])==9 for a in S)
assert cr(S+[a for a in chord])==9
assert all(cr(S+[a])==9 for a in D)
# Minimal *unital self-adjoint complex linear* Phi-invariant operator
# system containing O1 is therefore full M3(C), radius two on path.
# The support graph is a PATH, not the triangle declared as radius one.

# Even WITHOUT D, the P6-compatible nearest-neighbor *complex*
# path-offdiagonal sector has Phi-closure sl3(C) (dim 8).
assert cr(path)==4
traceless,r2=saturate(path)
assert len(traceless)==8 and cr(traceless)==8
assert all(a[0][0]+a[1][1]+a[2][2]==Z0 for a in traceless)
assert all(cr(traceless+[Phi(a)])==8 for a in traceless)
assert cr(traceless+chord)==8
assert cr(traceless+[sub(D[0],D[1]),sub(D[1],D[2])])==8
assert cr(traceless+[eye()])==9
assert r2[0]==4 and r2[-1]==8

# H33's local projection of ORIGINAL P3 hidden Krylov at depths 1,2
# spans the same 4D *complex* path-offdiagonal sector.  It is a
# microscopic candidate, not an operator system and not CPTP itself.
Jloc=[P1off(h) for j in (1,2) for h in H[j]]
assert cr(Jloc)==4
assert cr(Jloc+path)==4
assert rr([xi(scale(h,I/F(2))) for h in Jloc])==4
K,r3=saturate(Jloc)
assert cr(K)==8 and cr(K+[a for a in path])==8
assert cr(K+[eye()])==9
assert cr(K+chord)==8
# In particular, Phi(E01) generates forbidden distance-two support.
assert Phi(path[0])[0][2]==C(F(8,27),F(-2,9))
assert P1(Phi(path[0]))!=Phi(path[0])

# Explicit candidate conditional repair: taking r0=2 on this
# specific 3-vertex path permits the entire M3(C) operator system.
# This does not claim a uniform r0=2 for general growing systems.
assert all(abs(i-j)<=2 for i in range(N) for j in range(N))
assert cr([unit(i,j) for i in range(N) for j in range(N)])==9

# Distinct algebraic issue: local O1 is NOT multiplicatively closed:
# E01 E12 = E02, so its generated C* algebra is already M3(C).
assert mm(path[0],path[2])==chord[0]
assert P1(mm(path[0],path[2]))!=mm(path[0],path[2])

# P6 freezes a STATIC microscopic sector J_N with bounded locality.
# Its own selection theorem does NOT demand Phi(J_N) subset J_N.
# H34 is a conditional No-Go if invariance is ADDED to those axioms.
print("PASS H34: first hidden Phi(E00) has nonzero forbidden 02 matrix element")
print("PASS H34: two exact-time images have independent chord residues")
print("PASS H34: minimal Phi-invariant operator-system closure of O1 is M3(C)")
print("PASS H34: minimal Phi-invariant closure of path coherence = sl3(C)")
print("PASS H34: H33 local Krylov candidate also has invariant closure sl3(C)")
print("PASS H34: radius-two full system is an exact finite conditional repair")
print("PASS H34: local path operator system is not multiplicatively closed")
print("SCOPE: Phi-invariance is an ADDITIONAL hypothesis, not the frozen P6 axiom")
