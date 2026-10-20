#!/usr/bin/env python3
"""EXACT H75 adaptive future effects and CP uniform no-event tail certificate.

The finite operations and scheduling permissions are ASSUMED, not F-generated.
"""
import sympy as s
R,I=s.Rational,s.I
I2,I3,I6=s.eye(2),s.eye(3),s.eye(6)
E=lambda a,b:I3[:,a]*I3[b,:]
O=s.Matrix([[R(2,3),R(2,3),-R(1,3)],
            [-R(2,3),R(1,3),-R(2,3)],
            [-R(1,3),R(2,3),R(2,3)]])
U=s.diag(I,1,I)*O
M=[s.diag(1,R(3,5),R(3,5)),s.diag(0,R(4,5),R(4,5))]
K=[s.kronecker_product(I2[:,a]*I2[b,:],U*M[a])
   for a in range(2) for b in range(2)]
assert sum((k.H*k for k in K),s.zeros(6))==I6
Phi=lambda X:sum((k*X*k.H for k in K),s.zeros(6))
L=[s.kronecker_product(I2,E(j,j)) for j in range(3)]
J=[(L[0]+L[1])/s.sqrt(2),(L[0]-L[1])/s.sqrt(2),L[2]]
assert sum((v.H*v for v in L),s.zeros(6))==I6
assert sum((v.H*v for v in J),s.zeros(6))==I6
S=E(0,1)+E(1,0)+E(2,2)
F=s.kronecker_product(s.diag(1,0),I3)+s.kronecker_product(s.diag(0,1),S)
assert F.H*F==I6
W=[F,I6,I6]
ops={'Phi':K,'Delta':L}
for name,Jj in (('A',L),('B',J)):
    for j,C in enumerate(Jj):ops[f'{name}{j}']=[W[j]*C]
for name in ('A','B'):
    assert sum((v.H*v for j in range(3) for v in ops[f'{name}{j}']),s.zeros(6))==I6
adj=lambda name,X:sum((g.H*X*g for g in ops[name]),s.zeros(6)).applyfunc(s.expand)

pairs=((0,1),(0,2),(1,2))
basis=[]
for a in range(2):
    for j in range(3):
        X=s.zeros(6);X[3*a+j,3*a+j]=1;basis.append(X)
    for j,k in pairs:
        X=s.zeros(6);X[3*a+j,3*a+k]=X[3*a+k,3*a+j]=1;basis.append(X)
    for j,k in pairs:
        X=s.zeros(6);X[3*a+j,3*a+k]=I;X[3*a+k,3*a+j]=-I;basis.append(X)
assert len(basis)==18
def coord(X):
    assert X.H==X and X[:3,3:]==s.zeros(3) and X[3:,:3]==s.zeros(3)
    out=[]
    for a in range(2):
        Z=X[3*a:3*a+3,3*a:3*a+3]
        out+=list(Z.diagonal())
        out +=[s.expand(s.re(Z[j,k])) for j,k in pairs]
        out +=[s.expand(s.im(Z[j,k])) for j,k in pairs]
    assert len(out)==18 and all(x.is_Rational for x in out)
    return s.Matrix(out)
mat={name:s.Matrix.hstack(*[coord(adj(name,X)) for X in basis]) for name in ops}
assert all(B.shape==(18,18) for B in mat.values())
def add(rows,x):
    x=list(x)
    for p,r in sorted(rows.items()):
        if x[p]:
            c=x[p];x=[a-c*b for a,b in zip(x,r)]
    p=next((i for i,z in enumerate(x) if z),None)
    if p is None:return False
    c=x[p];rows[p]=[z/c for z in x]
    return True
def closure(names):
    pivots={};known=[];levels=[]
    for j in range(3):
        v=coord(L[j]);assert add(pivots,v)
        known.append((v,'Q'+str(j)))
    levels.append(known.copy())
    for depth in range(6):
        new=[]
        for v,word in known:
            for name in names:
                u=mat[name]*v
                if add(pivots,u):new.append((u,name+' '+word))
        known+=new;levels.append(known.copy())
        if not new:break
    return levels
ordinary=closure(['Phi','Delta'])
adaptive=closure(list(ops))
assert [len(a) for a in ordinary]==[3,5,7,9,9]
assert [len(a) for a in adaptive]==[3,7,10,12,12]
HS=s.diag(*([1]*3+[2]*6+[1]*3+[2]*6))
R2=s.Matrix.vstack(*[(v.T*HS) for v,_ in adaptive[2]])
R3=s.Matrix.vstack(*[(v.T*HS) for v,_ in adaptive[3]])
assert (R2.rank(),R3.rank())==(10,12)
H=s.zeros(6)
H[:3,:3]=s.Matrix([[0,5*I/3,5*I/6],
                    [-5*I/3,0,I],[-5*I/6,-I,0]])
v=coord(H)
assert H.H==H and s.trace(H)==0
assert R2*v==s.zeros(10,1) and R3*v!=s.zeros(12,1)
rp,rm=I6/6+R(3,160)*H,I6/6-R(3,160)*H
assert rp.trace()==rm.trace()==1
for j in range(6):
    row=sum((abs(s.re(H[j,k]))+abs(s.im(H[j,k])) for k in range(6)))
    assert R(3,160)*row<=R(1,20)<R(1,6)
for n in range(4):
    diff=s.expand(s.trace(L[0]*(rp-rm)))
    assert diff==[0,0,0,R(11,500)][n]
    rp,rm=Phi(rp),Phi(rm)
print("PASS: original future ranks 3,5,7,9,9; adaptive 3,7,10,12,12")
print("PASS: exact positive depth-three cut-state contrast 11/500")

# Original H75 output image remains a nine-dimensional observable subspace.
qbase=[]
for j in range(3):qbase.append(E(j,j))
for j,k in pairs:qbase.append(E(j,k)+E(k,j))
for j,k in pairs:qbase.append(I*(E(j,k)-E(k,j)))
out=[Phi(s.kronecker_product(s.diag(1,0),X)) for X in qbase]
resp=s.Matrix([[s.expand(s.trace(sum((v[j]*basis[j] for j in range(18)),s.zeros(6))*X))
                for X in out] for v,_ in adaptive[-1]])
assert resp.rank()==9
print("PASS: 12D full-cut quotient (24D kernel), 9D original source-output image")

# One designated adaptive outcome-0 NO-EVENT cycle: Phi -> A0 -> F.
noevent=[F*L[0]*k for k in K]
events=[L[j]*k for j in (1,2) for k in K]
assert sum((g.H*g for g in noevent+events),s.zeros(6))==I6
NstarI=sum((g.H*g for g in noevent),s.zeros(6))
A=s.Matrix([[R(4,9),R(4,15),-R(2,15)],
            [R(4,15),R(4,9),-R(2,9)],
            [-R(2,15),-R(2,9),R(1,9)]])
assert NstarI==s.kronecker_product(I2,A)
assert A.eigenvals()=={0:1,R(1,2)-s.sqrt(745)/90:1,
                       R(1,2)+s.sqrt(745)/90:1}
b=R(5,6)
assert 745<900
V=b*I3-A
assert all(V[:k,:k].det()>0 for k in (1,2,3))
# Choi positive semidefinite by the actual Kraus Gram decomposition.
columns=s.Matrix.hstack(*(g.reshape(36,1) for g in noevent))
choi=columns*columns.H
assert choi==choi.H and choi.shape==(36,36)
Nstar=lambda X:sum((g.H*X*g for g in noevent),s.zeros(6))
eff=I6
for n in range(1,8):
    eff=Nstar(eff)
    block=(b**n*I6-eff)[:3,:3]
    assert all(s.simplify(ev)>=0 for ev in block.eigenvals())
assert b**7<=R(1,3)
print("PASS: CP/Choi no-event H75 cycle and uniform b=5/6 all-state tail")

# Individually nilpotent no-event maps can lose ALL uniform contraction when
# the schedule switches between them; both have valid CP event complements.
V1=s.Matrix([[0,1],[0,0]])
V2=s.Matrix([[0,0],[1,0]])
assert V1**2==V2**2==s.zeros(2)
for G in (V1,V2):
    assert all(e>=0 for e in (I2-G.H*G).eigenvals())
rho=s.Matrix([[0,0],[0,1]])
for _ in range(8):
    rho=V1*rho*V1.H;assert s.trace(rho)==1
    rho=V2*rho*V2.H;assert rho==s.Matrix([[0,0],[0,1]])
print("PASS: individual 2-step extinction does not guarantee arbitrary switching")
print("OPEN: operational scheduling/access provenance and F generative completeness")
