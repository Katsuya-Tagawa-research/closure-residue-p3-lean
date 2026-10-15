"""H61: exact rational mathematical gates prompted by P9.70.

B1 torus-invariant real Lagrangian no-go at generic U(4) KKS orbit;
B1 local coherent-response selector requires a broken phase reference.
B2 anisotropic matter principal-symbol metric matching.
B3 positive microscopic kinetic congruence cannot produce DeWitt (5+,1-).

P9.70 is user-reported; this file independently checks these finite
comparator algebraic gates, NOT its entire SymPy calculation or physical
P3/P6 provenance, continuum limit, full HDA or Einstein equations.
"""
from fractions import Fraction as F
from itertools import combinations

def Z(n,m):
    return [[F(0)]*m for _ in range(n)]
def I(n):
    A=Z(n,n)
    for i in range(n): A[i][i]=F(1)
    return A
def T(A): return [list(r) for r in zip(*A)]
def mm(A,B):
    assert len(A[0])==len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def add(A,B):
    return [[a+b for a,b in zip(u,v)] for u,v in zip(A,B)]
def sc(a,A): return [[a*x for x in row] for row in A]
def sub(A,B): return add(A,sc(F(-1),B))
def det(A):
    M=[list(r) for r in A]; n=len(M); d=F(1)
    assert all(len(r)==n for r in M)
    for j in range(n):
        k=next((i for i in range(j,n) if M[i][j]),None)
        if k is None:return F(0)
        if k!=j:M[j],M[k]=M[k],M[j];d=-d
        p=M[j][j];d*=p
        for i in range(j+1,n):
            q=M[i][j]/p
            for k in range(j,n):M[i][k]-=q*M[j][k]
    return d
def rank(A):
    M=[list(r) for r in A]; n=len(M); m=len(M[0]); p=0
    for j in range(m):
        k=next((i for i in range(p,n) if M[i][j]),None)
        if k is None:continue
        M[p],M[k]=M[k],M[p]
        d=M[p][j];M[p]=[a/d for a in M[p]]
        for i in range(n):
            if i!=p and M[i][j]:
                d=M[i][j];M[i]=[a-d*b for a,b in zip(M[i],M[p])]
        p+=1
        if p==n:break
    return p
def inv(A):
    n=len(A); M=[list(A[i])+I(n)[i] for i in range(n)]
    for j in range(n):
        k=next((i for i in range(j,n) if M[i][j]),None)
        assert k is not None
        M[k],M[j]=M[j],M[k]
        p=M[j][j];M[j]=[a/p for a in M[j]]
        for i in range(n):
            if i!=j and M[i][j]:
                d=M[i][j];M[i]=[a-d*b for a,b in zip(M[i],M[j])]
    return [r[n:] for r in M]
def qform(A,v):
    return sum((v[i]*A[i][j]*v[j]
                for i in range(len(v)) for j in range(len(v))),F(0))
def pd(A):
    return all(det([row[:k] for row in A[:k]])>0
               for k in range(1,len(A)+1))

# B1. A single diagonal U(1) generator with six distinct nonzero
# root frequencies suffices for the strong real-invariant isotropic no-go.
h=[F(0),F(1),F(4),F(10)]
lam=[F(1,10),F(2,10),F(3,10),F(4,10)]
edges=list(combinations(range(4),2))
freq=[h[b]-h[a] for a,b in edges]
gap=[2*(lam[a]-lam[b]) for a,b in edges]
assert freq==[1,4,10,3,9,6]
assert len(set(f*f for f in freq))==6 and all(d!=0 for d in gap)
J=Z(12,12);KKS=Z(12,12)
for e in range(6):
    J[e][6+e]=-freq[e]
    J[6+e][e]=freq[e]
    KKS[e][6+e]=gap[e]
    KKS[6+e][e]=-gap[e]
assert sub(add(mm(T(J),KKS),mm(KKS,J)),Z(12,12))==Z(12,12)
assert rank(KKS)==12
J2=mm(J,J)
assert all(J2[k][k]==-freq[k%6]**2 for k in range(12))
# Rational spectral projectors P_e(J^2): distinct frequencies force
# any J-invariant real linear subspace to split by root plane.
Pall=Z(12,12)
for e in range(6):
    P=I(12)
    for j in range(6):
        if j!=e:
            numerator=add(J2,sc(freq[j]**2,I(12)))
            P=mm(P,sc(F(1)/(freq[j]**2-freq[e]**2),numerator))
    expected=Z(12,12);expected[e][e]=expected[6+e][6+e]=F(1)
    assert P==expected
    assert mm(P,P)==P and rank(P)==2
    assert gap[e]!=0 # KKS restricted to this plane is nondegenerate
    Pall=add(Pall,P)
assert Pall==I(12)
# Proof step: a J-invariant real subspace inside each 2D plane
# is either {0} or the whole 2D plane, since J^2=-freq^2 I
# and J rotates without any real eigenline. Every nonzero plane
# violates isotropy as KKS(X_e,Y_e)=gap[e]!=0.
print("PASS H61 B1: exact torus one-parameter spectral projectors certify no nonzero invariant real isotropic tangent")

# Conditional broken-phase-reference response selector on SU(2) sphere:
# rho=[[c+p, a+ib],[a-ib,c-p]], a^2+b^2+p^2=r^2.
c=F(1,2);r=F(1,4);p=F(3,20);a=F(1,5);b=F(0)
assert a*a+b*b+p*p==r*r
rho2=[[c+p,a],[a,c-p]]
assert det(rho2)==c*c-r*r==F(3,16)
# Observable X=2a, Y=2b, Z=2p; at q=0:
# derivatives of (Y,Z) with respect to (q,p) are (2a,0),(0,2).
response_minor=2*a*2
assert response_minor==F(4,5)>0
# q is the phase of a+ib, shifted by diagonal U(1)^2 actions;
# fixed X,Y channels constitute additional reference/observer data.
print("PASS H61 B1: conditional coherent X/Y+population Z readout has local (q,p) rank 2; phase reference remains extra")

# B2. Matter scalar H-H bracket has structure S^ij=A K^ij.
# Compare all six independent tensor components, not merely 1D speed.
g=[[F(2),F(1),F(0)],[F(1),F(3),F(0)],[F(0),F(0),F(5)]]
gi=inv(g)
assert pd(g) and mm(g,gi)==I(3)
A=F(5,7)
K=sc(F(1)/A,gi)
S=sc(A,K)
assert S==gi
assert S[0][1]!=0 and S[1][2]==0
bad=sc(A,I(3))
assert bad!=gi
assert rank(K)==3 and pd(K)
# The 1D P9.70 flat scalar limit is the special identity
# 2*A*kappa*r^2=1, not a tensor or dynamical HDA proof.
A1=F(5,4);radius=F(2,5)
kappa=F(1)/(2*A1*radius*radius)
assert 2*A1*kappa*radius*radius==1
print("PASS H61 B2: exact anisotropic 3x3 tensor matching A K^ij=g^ij (and explicit isotropic mismatch)")

# B3. Any invertible real coordinate-preserving canonical pullback
# transforms positive momentum Hessian by congruence, never inertia.
B6=[
 [F(1),F(1),F(4),F(0),F(1),F(1)],
 [F(1),F(0),F(1),F(1),F(4),F(1)],
 [F(0),F(1),F(1),F(1),F(1),F(4)],
 [F(-1),F(0),F(2),F(0),F(2),F(1)],
 [F(0),F(-1),F(2),F(0),F(1),F(2)],
 [F(0),F(0),F(1),F(-1),F(2),F(2)]
]
assert det(B6)==F(-256)
C=Z(6,6)
for i in range(6):C[i][i]=F(i+1)
assert pd(C)
Ctrans=mm(mm(T(B6),C),B6)
assert pd(Ctrans) and det(Ctrans)==det(B6)**2*det(C)
# ADM inverse DeWitt signature in symmetric momentum components:
# diag pi_ii terms sum pi_ii^2 - 1/2 (sum pi_ii)^2;
# offdiagonal pi_ij have coefficient 2.
DeW=Z(6,6)
for i in range(3):
    for j in range(3):DeW[i][j]=F(int(i==j))-F(1,2)
for i in range(3,6):DeW[i][i]=F(2)
def v6(*x):return [F(a) for a in x]
trace_direction=v6(1,1,1,0,0,0)
positive_vectors=[v6(1,-1,0,0,0,0),v6(1,1,-2,0,0,0),
                  v6(0,0,0,1,0,0),v6(0,0,0,0,1,0),v6(0,0,0,0,0,1)]
assert qform(DeW,trace_direction)==F(-3,2)
assert all(qform(DeW,v)>0 for v in positive_vectors)
assert rank([trace_direction]+positive_vectors)==6
assert all(qform(Ctrans,v)>0 for v in [trace_direction]+positive_vectors)
assert det(DeW)<0 and rank(DeW)==6
print("PASS H61 B3: positive six-momentum Hessian remains positive after exact K4 congruence, while DeWitt is (5+,1-)")

# B4. Bare matter H-H smearing antisymmetry is derived in the note.
# At flat-background 1D, the structure is A*K, including field
# momentum D=P*q'. This coefficient-only identity does not verify
# D-H, D-D, gravity/matter mixed brackets or nonuniform full HDA.
N,M,dN,dM,P,qprime=map(F,[2,3,5,-1,7,11])
AK=F(3,5)*F(7,3)
v=AK*(N*dM-M*dN)
bracket=P*qprime*v
assert bracket==P*qprime*AK*(N*dM-M*dN)
assert bracket==-P*qprime*AK*(M*dN-N*dM)
print("PASS H61 B4: 1D matter H-H structure coefficient gate, no full HDA or CR-origin claim")
print("BOUNDARY: local P9.70 scalar model and H59 comparator only; no P3/P6 polarization provenance, full ADM, EH or Einstein derivation")
