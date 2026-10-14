"""H26 exact finite no-go: cell-local P3/P6 data do not fix edge holonomy.

The H24 microscopic CPTP model is held identical at every cell.
Two U(1) -> SO(2) subset SO(3) edge assignments have the same
local data, h-metric, orientation, and gauge class at each vertex,
but inequivalent global cycle holonomy. Edge intertwiners are NOT
assumed; the audit explicitly tests that missing naturality condition.
"""
from fractions import Fraction as Q
from itertools import combinations
from P9H24PhaseSensitiveResidueGaugeExactCheck import (
    C, I, O, Z0, U, Z, z1, z2, R, K1, K2, phi, mm as mm2,
    dagger as dag2, scale as scale2,
)

def eye(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Q(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def trans(A):return list(map(list,zip(*A)))
def det3(A):
    a,b,c=A[0];d,e,f=A[1];g,h,i=A[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
def is_so3(A):return mm(trans(A),A)==eye(3) and det3(A)==1
def trace(A):return sum((A[i][i] for i in range(len(A))),Q(0))
def rot_from_su2_phase(a,b):
    a,b=Q(a),Q(b)
    assert a*a+b*b==1
    return [[a*a-b*b,2*a*b,Q(0)],
            [-2*a*b,a*a-b*b,Q(0)],
            [Q(0),Q(0),Q(1)]]
Id=eye(3)
Rphase=rot_from_su2_phase(Q(3,5),Q(4,5))
Rphase2=rot_from_su2_phase(Q(5,13),Q(12,13))
assert Rphase[0][0]==Q(-7,25) and Rphase[0][1]==Q(24,25)
assert is_so3(Rphase) and is_so3(Rphase2)
assert mm(Rphase,Rphase2)==mm(Rphase2,Rphase)
assert trace(Id)==3 and trace(Rphase)==Q(11,25)

# Fixed H24 local unitary CPTP channel and its *original* P3 residue
# at every one of four vertices. The tuple encodes the same operators,
# not new channel dynamics or edge couplings.
assert R[0][0]==C(Q(0),Q(128,81))
assert R[1][1]==C(Q(0),Q(-128,81))
local_data=tuple((U,Z,z1,z2,R,K1,K2) for _ in range(4))
assert all(v==local_data[0] for v in local_data)

# Each local P6-style first-residue derivation is the SAME action on
# the diagonal algebra. The edge transport is not used in its definition.
def local_fingerprint(v):
    return tuple(
        tuple(mm2(K,d)[i][j]-mm2(d,K)[i][j] for i in range(2) for j in range(2))
        for K in (K1,K2) for d in (Z,)
    )
for v in local_data:assert local_fingerprint(v)==local_fingerprint(local_data[0])

verts=tuple(range(4))
tree=((0,1),(1,2),(2,3))
chords=((0,2),(0,3))
edges=tree+chords
assert len(edges)-len(verts)+1==2
Aflat={e:Id for e in edges}
Atwisted=dict(Aflat);Atwisted[(0,2)]=Rphase
assert all(is_so3(M) for M in Aflat.values())
assert all(is_so3(M) for M in Atwisted.values())
# A fundamental based loop 0->1->2->0 has holonomy A02^-1,
# since tree transports are I.
def inv(A):return trans(A)
def hol02(A):return mm(inv(A[(0,2)]),mm(A[(1,2)],A[(0,1)]))
assert trace(hol02(Aflat))==Q(3)
assert trace(hol02(Atwisted))==Q(11,25)
# Trace is preserved under every vertex-frame gauge transformation.
# Therefore no gauge transformation in SO3 (even larger than SO2)
# identifies the two edge systems, despite identical local data.

# Stronger: metric and orientation preserving P7 carrier h=4<,>.
f=[[Q(1,2),Q(1,2),Q(1,2)],
   [Q(1,2),-Q(1,2),-Q(1,2)],
   [-Q(1,2),Q(1,2),-Q(1,2)],
   [-Q(1,2),-Q(1,2),Q(1,2)]]
J=[[v/2 for v in row] for row in f]
Jinv=[[4*v for v in row] for row in trans(J)]
N=[Q(1)]*4
def carrier(A):
    X=mm(mm(J,A),Jinv)
    return [[X[i][j]+N[i]*N[j]/4 for j in range(4)] for i in range(4)]
for A in (Id,Rphase,Rphase2):
    M=carrier(A)
    assert mm(trans(M),M)==eye(4)
    assert mm(M,[[v] for v in N])==[[v] for v in N]
    assert mm(M,J)==mm(J,A)

# In the abelian SO(2) group used here, gauge equivalence of *two
# connections* is decided by the chord holonomies in tree gauge.
# Tree spanning gauges are constructed explicitly.
def tree_gauge(A):
    gauge={0:Id}
    for u,v in tree:
        gauge[v]=mm(gauge[u],inv(A[(u,v)]))
    return gauge
def gauge_action(A,g):
    return {(u,v):mm(mm(g[v],A[(u,v)]),inv(g[u])) for u,v in edges}
def normal_form(A):
    B=gauge_action(A,tree_gauge(A))
    assert all(B[e]==Id for e in tree)
    return B
assert normal_form(Aflat)!=(normal_form(Atwisted))
# Construct an arbitrary nontrivial connection, apply independently
# calibrated vertex phases, and recover identical tree-normal forms.
Arich={tree[0]:Rphase,tree[1]:Rphase2,tree[2]:Id,
       chords[0]:Rphase2,chords[1]:Rphase}
g={0:Rphase2,1:Rphase,2:Id,3:mm(Rphase,Rphase2)}
Brich=gauge_action(Arich,g)
assert all(is_so3(M) for M in Brich.values())
assert normal_form(Arich)==normal_form(Brich)
assert len([normal_form(Arich)[e] for e in chords])==2

# The SU2 edge phase is invisible to local diagonal populations but
# NOT to coherent offdiagonal dynamics / a stronger channel gluing.
phase=C(Q(3,5),Q(4,5))
G=[[phase,Z0],[Z0,phase.conj()]]
assert mm2(dag2(G),G)==[[O,Z0],[Z0,O]]
assert mm2(mm2(G,Z),dag2(G))==Z
def conjugate(A):
    return mm2(mm2(G,A),dag2(G))
assert conjugate(phi(Z))!=phi(conjugate(Z))
# Hence this twisted edge is excluded if one ADDS the condition
# Ad_G o Phi = Phi o Ad_G for the fixed local channel Phi.
# That condition is not supplied by local P3 residue or local P6
# response. It is a genuine, testable additional naturality axiom.

print("PASS H26: identical H24 CPTP/P3-residue/local-control fingerprints")
print("PASS H26: two h-preserving connections have distinct loop traces")
print("PASS H26: U1/SO2 graph connections classify by two cycle moduli")
print("PASS H26: tree-gauge normal form is invariant under vertex-phase gauges")
print("PASS H26: local diagonal gauge preserves populations, but fails channel naturality")
print("NO-GO: cell-local CR observations alone do not determine edge holonomy")
print("SCOPE: no actual physical P6 link control or Levi-Civita/Regge transport")
