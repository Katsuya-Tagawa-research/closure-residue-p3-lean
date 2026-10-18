"""H86 exact Fraction/Gaussian-rational audit of a conditional 4-cell exchange gate.

The 4-cell microscopic exchange Hamiltonian, physical qubit embeddings,
all accessible preparations and quantum readouts are INDEPENDENT ports;
not inferred from H75's six-level local CPTP source or original P3 R3.
"""
from fractions import Fraction as F
from itertools import combinations
from P9H24PhaseSensitiveResidueGaugeExactCheck import C, I, O, Z0, gc
from P9H75SemicausalMicroMemorySourceExactCheck import R60

assert R60[0][0] == I*gc(F(-32,135))

n=4
edges=list(combinations(range(n),2))
assert edges==[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def zeros():
    return [[Z0 for j in range(n)] for i in range(n)]
def eye():
    return [[O if i==j else Z0 for j in range(n)] for i in range(n)]
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(n)),Z0)
             for j in range(n)] for i in range(n)]
def dagger(A):
    return [[A[j][i].conj() for j in range(n)] for i in range(n)]
def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]
def scale(A,x):
    return [[x*A[i][j] for j in range(n)] for i in range(n)]
def com(A,B):
    return add(mm(A,B),scale(mm(B,A),-1))
def diagonal(p):
    return [[gc(p[i]) if i==j else Z0 for j in range(n)] for i in range(n)]
def hamiltonian(J):
    assert len(J)==6
    H=zeros()
    for (i,j),x in zip(edges,J):
        H[i][j]=gc(x)
        H[j][i]=gc(x)
    assert dagger(H)==H
    return H
def laplacian(J):
    L=[[F(0) for j in range(n)] for i in range(n)]
    for (i,j),x in zip(edges,J):
        w=F(x)**2
        L[i][i]+=w;L[j][j]+=w
        L[i][j]-=w;L[j][i]-=w
    return L
def second_jet(H,p):
    # rho''(0)=-[H,[H,rho]]; population readouts are positive E_ii.
    R=diagonal(p)
    C2=com(H,com(H,R))
    return [(-C2[i][i]).r for i in range(n)]
def jet_from_graph(L,p):
    return [-2*sum((L[i][j]*p[j] for j in range(n)),F(0))
            for i in range(n)]
def rank(A):
    X=[[F(v) for v in row] for row in A]
    m=len(X);ncol=len(X[0]);i=0
    for j in range(ncol):
        k=next((k for k in range(i,m) if X[k][j]),None)
        if k is None:continue
        X[i],X[k]=X[k],X[i]
        d=X[i][j]
        X[i]=[v/d for v in X[i]]
        for k in range(m):
            if k!=i and X[k][j]:
                c=X[k][j]
                X[k]=[a-c*b for a,b in zip(X[k],X[i])]
        i+=1
        if i==m:break
    return i

J=tuple(F(i) for i in range(1,7))
H=hamiltonian(J)
L=laplacian(J)
assert L==[
 [14,-1,-4,-9],
 [-1,42,-16,-25],
 [-4,-16,56,-36],
 [-9,-25,-36,70],
]
assert all(sum(row)==0 for row in L)
p=[F(1,2),F(1,4),F(1,8),F(1,8)]
assert sum(p)==1 and all(v>=0 for v in p)
assert second_jet(H,p)==jet_from_graph(L,p)
for j in range(n):
    ej=[F(int(i==j)) for i in range(n)]
    derivative=second_jet(H,ej)
    assert derivative==jet_from_graph(L,ej)
    for i in range(n):
        if i!=j:
            assert derivative[i]==2*H[i][j].r**2
    assert sum(derivative)==0
print("PASS H86.2: all localized positive-preparation second jets equal -2 weighted graph Laplacian, w_ij=J_ij^2")
print("PASS H86.2: exact nonuniform J=1,2,3,4,5,6 weighted Laplacian and physical positive site-effect inversion")

Jfull=(F(1),)*6
Jpath=(F(1),F(0),F(0),F(1),F(0),F(1))
Jdisconnected=(F(1),F(0),F(0),F(0),F(0),F(1))
Lfull=laplacian(Jfull)
assert Lfull==[[F(4*int(i==j)-1) for j in range(n)] for i in range(n)]
assert rank(Lfull)==3
assert rank(laplacian(Jpath))==3
assert rank(laplacian(Jdisconnected))==2
assert all(sum(row)==0 for row in Lfull)
# L|S=4I, g=16 (L|S)^-1 = 4 I.
for v in ((F(1),F(-1),F(0),F(0)),
          (F(0),F(1),F(-1),F(0)),
          (F(0),F(0),F(1),F(-1))):
    assert [sum(Lfull[i][j]*v[j] for j in range(n))
            for i in range(n)]==[4*x for x in v]
print("PASS H86.3: uniform complete K4 metric 4I on S; connected path rank3; disconnected graph rank2")

Hplus=hamiltonian(Jfull)
Jminus=(-F(1),)+Jfull[1:]
Hminus=hamiltonian(Jminus)
assert laplacian(Jfull)==laplacian(Jminus)
for j in range(n):
    ej=[F(int(i==j)) for i in range(n)]
    assert second_jet(Hplus,ej)==second_jet(Hminus,ej)
def cube_trace(A):
    B=mm(mm(A,A),A)
    t=sum((B[i][i] for i in range(n)),Z0)
    assert t.i==0
    return t.r
assert cube_trace(Hplus)==24
assert cube_trace(Hminus)==0
assert (Jfull[0]*Jfull[1]*Jfull[3]) != (Jminus[0]*Jminus[1]*Jminus[3])
print("PASS H86.4: same entire positive population second-jet Laplacian, but distinct gauge-invariant triangle products and tr(H^3)=24 vs 0")

# Separate phase-referenced entangled one-excitation positive preparation
# |psi>= (|i> + i|j>)/sqrt(2); its density matrix is rational Gaussian.
# The signed first derivative of positive projector E_ii is + J_ij.
def phase_pair_density(i,j):
    rho=zeros()
    rho[i][i]=gc(F(1,2))
    rho[j][j]=gc(F(1,2))
    rho[i][j]=-I*gc(F(1,2))
    rho[j][i]=I*gc(F(1,2))
    assert dagger(rho)==rho
    assert mm(rho,rho)==rho and sum((rho[k][k] for k in range(n)),Z0)==O
    return rho
for (i,j),amp in zip(edges,J):
    rho=phase_pair_density(i,j)
    d=-I*com(H,rho)[i][i]
    assert d==gc(amp),(i,j,d,amp)
for (i,j),amp in zip(edges,Jminus):
    if (i,j)==(0,1):
        rho=phase_pair_density(i,j)
        assert -I*com(Hminus,rho)[i][i]==gc(amp)
print("PASS H86.4: phase-referenced entangled positive preparations recover signed real J_ij by one-site positive first derivative")

# Exact physical rational Cayley exchange pulse, acting on the one-
# excitation subspace as U=(I-i X/2)(I+i X/2)^-1.
X=zeros()
X[0][1]=O
X[1][0]=O
U=eye()
U[0][0]=gc(F(3,5)); U[1][1]=gc(F(3,5))
U[0][1]=-I*gc(F(4,5)); U[1][0]=-I*gc(F(4,5))
assert mm(dagger(U),U)==eye()
assert mm(U,dagger(U))==eye()
lhs=mm(U,add(eye(),scale(X,I*gc(F(1,2)))))
rhs=add(eye(),scale(X,-I*gc(F(1,2))))
assert lhs==rhs
prob=U[1][0]*U[1][0].conj()
assert prob==gc(F(16,25))
negativity=F(3,5)*F(4,5)
assert negativity==F(12,25)>0
print("PASS H86.5: exact Gaussian-rational unitary Cayley edge gate, positive site probability 16/25 and pure two-cell entanglement negativity 12/25")

# Example local control algebra: [X⊗I,I⊗Z]=0, not a crossed
# exchange generator; the full no-go is the analytic tensor Lie proof.
XI=[[F(0),F(0),F(1),F(0)],
    [F(0),F(0),F(0),F(1)],
    [F(1),F(0),F(0),F(0)],
    [F(0),F(1),F(0),F(0)]]
IZ=[[F(1),F(0),F(0),F(0)],
    [F(0),F(-1),F(0),F(0)],
    [F(0),F(0),F(1),F(0)],
    [F(0),F(0),F(0),F(-1)]]
def mm4(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(4)),F(0))
             for j in range(4)] for i in range(4)]
assert mm4(XI,IZ)==mm4(IZ,XI)
print("PASS H86.1: disjoint local operators commute; no cross-cell Lie generation without an extra resource")
print("BOUNDARY: derived L only from INDEPENDENTLY supplied coherent exchange ports; population second jet is NOT Markov semigroup evolution")
print("BOUNDARY: true CR-to-port/physical solder, KKS-ADM, DeWitt sector, off-shell HDA, Einstein dynamics and F-completeness remain OPEN")
