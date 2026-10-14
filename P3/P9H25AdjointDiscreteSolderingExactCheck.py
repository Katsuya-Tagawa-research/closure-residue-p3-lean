"""H25: rational SU2 adjoint/spatial carrier and discrete soldering obstructions.

Finite exact arithmetic only. This is not physical Levi-Civita transport:
physical edge transports, frames and metric matching are additional data.
"""
from fractions import Fraction as Q

def mat(A): return [[Q(x) for x in row] for row in A]
def eye(n): return [[Q(i == j) for j in range(n)] for i in range(n)]
def T(A): return list(map(list,zip(*A)))
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Q(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def madd(A,B):
    return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def neg(A): return [[-x for x in a] for a in A]
def tr(A): return sum((A[i][i] for i in range(len(A))),Q(0))
def det3(A):
    a,b,c=A[0];d,e,f=A[1];g,h,j=A[2]
    return a*(e*j-f*h)-b*(d*j-f*g)+c*(d*h-e*g)
def is_so3(R):return mm(T(R),R)==eye(3) and det3(R)==1

X=mat([[0,1,0],[0,0,0],[0,0,0]])  # inert placeholder; SU2 basis below
# Pauli B=-(128i/81)Z from the exact H24 original P3 residue.
# On (Pauli X, Pauli Y, Pauli Z), ad_B(X)=(256/81)Y,
# ad_B(Y)=-(256/81)X, ad_B(Z)=0.
c=Q(256,81)
L=mat([[0,-c,0],[c,0,0],[0,0,0]])
assert madd(T(L),L)==mat([[0]*3 for _ in range(3)])
assert L!=mat([[0]*3 for _ in range(3)])
assert mm(L,mat([[0],[0],[1]]))==mat([[0],[0],[0]])

# An exact SU(2) diagonal phase g=diag((3+4i)/5,(3-4i)/5)
# acts on the traceless Hermitian Pauli triple by Ad_g:
# X -> cos(2theta)X - sin(2theta)Y; Y -> sin(2theta)X+cos(2theta)Y.
cos2=Q(3,5)**2-Q(4,5)**2
sin2=2*Q(3,5)*Q(4,5)
assert (cos2,sin2)==(Q(-7,25),Q(24,25))
Rad=mat([[cos2,sin2,0],[-sin2,cos2,0],[0,0,1]])
assert is_so3(Rad)
assert mm(Rad,L)==mm(L,Rad) # same axial rotation generator
# This is an internal spin-one representation, not a soldering map.

# P7 carrier S=1-perp subset R^4 with h=4 dot, oriented frame optional.
# f_i are Euclidean orthonormal and e_i=f_i/2 are h-orthonormal.
f=mat([[Q(1,2), Q(1,2), Q(1,2)],
       [Q(1,2),-Q(1,2),-Q(1,2)],
       [-Q(1,2),Q(1,2),-Q(1,2)],
       [-Q(1,2),-Q(1,2),Q(1,2)]])
J=[[v/2 for v in row] for row in f]
assert mm(T(J),J)==[[Q(i==j,4) for j in range(3)] for i in range(3)]
Jinv=[[4*v for v in row] for row in T(J)]
assert mm(Jinv,J)==eye(3)
n=mat([[1],[1],[1],[1]])
assert mm(T(n),J)==mat([[0,0,0]])
Pi=mat([[Q(1,4)]*4 for _ in range(4)])
Ps=mm(J,Jinv)
assert madd(Ps,Pi)==eye(4)
Rcarrier=madd(mm(mm(J,Rad),Jinv),Pi)
assert mm(T(Rcarrier),Rcarrier)==eye(4)
assert mm(Rcarrier,n)==n
assert mm(Rcarrier,J)==mm(J,Rad)
# This carrier transport uses an explicitly CHOSEN h-isometry J.

Rz=mat([[0,-1,0],[1,0,0],[0,0,1]])
Rx=mat([[1,0,0],[0,0,-1],[0,1,0]])
I3=eye(3)
assert is_so3(Rz) and is_so3(Rx)
assert tr(Rz)==tr(Rx)==Q(1)
assert mm(Rz,Rx)!=mm(Rx,Rz)
assert tr(mm(Rz,Rx))==Q(0)
assert tr(mm(Rz,Rz))==Q(-1)

# Edge equation E_v A_uv = P_uv E_u for a chosen oriented graph.
# On a connected graph, a prescribed root frame E0 extends via a
# spanning tree, and extends to all edges iff every chord is compatible.
def recover_from_tree(vertices,tree,all_edges,A,P,E0):
    frames={0:E0}
    pending=list(tree)
    while pending:
        progressed=False
        for e in pending[:]:
            u,v=e
            if u in frames and v not in frames:
                frames[v]=mm(mm(P[e],frames[u]),T(A[e]))
                pending.remove(e);progressed=True
            elif v in frames and u not in frames:
                frames[u]=mm(mm(T(P[e]),frames[v]),A[e])
                pending.remove(e);progressed=True
            elif u in frames and v in frames:
                pending.remove(e);progressed=True
        if not progressed:raise AssertionError("disconnected spanning tree")
    assert set(frames)==set(vertices)
    for e in all_edges:
        u,v=e
        if mm(frames[v],A[e])!=mm(P[e],frames[u]):
            return False,frames,e
    return True,frames,None

verts=range(4)
tree=[(0,1),(1,2),(2,3)]
edges=tree+[(0,2),(0,3)]
A={tree[0]:Rz,tree[1]:Rx,tree[2]:T(Rz),
   (0,2):Rx,(0,3):Rz}
frames0={0:I3,1:Rz,2:Rx,3:mm(Rz,Rz)}
P={e:mm(mm(frames0[e[1]],A[e]),T(frames0[e[0]]))
   for e in edges}
assert all(is_so3(M) for M in A.values())
assert all(is_so3(M) for M in P.values())
ok,frames,problem=recover_from_tree(verts,tree,edges,A,P,I3)
assert ok and frames==frames0 and problem is None

# A single-loop trace mismatch obstructs soldering (necessary only).
Ac={e:I3 for e in edges};Pc={e:I3 for e in edges}
Pc[(0,2)]=Rz
assert tr(Ac[(0,2)])!=tr(Pc[(0,2)])
assert recover_from_tree(verts,tree,edges,Ac,Pc,I3)[0] is False

# Stronger: each corresponding fundamental-loop trace agrees, yet
# no COMMON root SO3 conjugacy exists.
An={e:I3 for e in edges};Pn={e:I3 for e in edges}
An[(0,2)]=Rz
An[(0,3)]=Rx
Pn[(0,2)]=Rz
Pn[(0,3)]=Rz
assert tr(An[(0,2)])==tr(Pn[(0,2)])==1
assert tr(An[(0,3)])==tr(Pn[(0,3)])==1
# Any common E must conjugate both internal loops into two commuting
# physical loops; contradiction, since the internal loops do not commute.
assert mm(An[(0,2)],An[(0,3)])!=mm(An[(0,3)],An[(0,2)])
assert mm(Pn[(0,2)],Pn[(0,3)])==mm(Pn[(0,3)],Pn[(0,2)])
# Even a mixed-loop conjugacy invariant separates them:
assert tr(mm(An[(0,2)],An[(0,3)]))!=tr(mm(Pn[(0,2)],Pn[(0,3)]))

print("PASS H25: H24 diagonal P3 residue induces nonzero internal so3 generator")
print("PASS H25: rational SU2 diagonal-phase Ad is exact SO3 rotation")
print("PASS H25: chosen P7 h=4 carrier frame produces an isometric S rotation")
print("PASS H25: compatible edge data recovered from spanning tree")
print("PASS H25: single-loop trace mismatch obstructs soldering")
print("PASS H25: per-loop traces match but simultaneous conjugacy fails")
print("Scope: conditional discrete soldering data, NO Levi-Civita derivation")
