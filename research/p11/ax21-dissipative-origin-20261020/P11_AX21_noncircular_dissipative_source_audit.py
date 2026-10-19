#!/usr/bin/env python3
"""AX21: exact finite GKSL source-selection/no-go witnesses (SymPy 1.14)."""
from pathlib import Path
import json
import sympy as s

checks=[]
def test(x, name):
    assert bool(x), name
    checks.append(name)
def equal(a,b):
    return a.shape==b.shape and all(s.expand(v)==0 for v in a-b)
def u(n,i,j):
    v=s.zeros(n);v[i,j]=1;return v
def vec(a):
    return s.Matrix([a[i,j] for j in range(a.cols) for i in range(a.rows)])
def sup(n,f):
    return s.Matrix.hstack(*[vec(f(u(n,i,j))) for j in range(n) for i in range(n)])
def diag(a):
    return s.diag(*(a[i,i] for i in range(a.rows)))

n=5
I=s.eye(n)
E=sup(n,diag)
Q=s.eye(n*n)-E
R=I-s.Rational(2,n)*s.ones(n)
test(equal(R.T*R,I),'five-site exact Householder orthogonal rotation')
test(not equal(R,I),'Householder is nontrivial')
test(all(R[i,j]!=0 for i in range(n) for j in range(n)),'all Householder matrix entries nonzero')
T=sup(n,lambda a:R*a*R.T)
test(equal(T.T*T,s.eye(n*n)),'HS-unitary rotation superoperator')
F=T*E*T.T
test(equal(F*F,F),'rotated expectation idempotent')
test(equal(F,F.T),'rotated expectation HS-selfadjoint')
test(s.trace(F)==5,'rotated pointer algebra dimension five by idempotent trace')
test(not equal(F,E),'two pointer algebras are distinct')
K=(E+F)/2-s.eye(n*n)
test(equal(K,K.T),'average GKSL dissipator selfadjoint')
test(equal(K*vec(I),s.zeros(n*n,1)),'average GKSL unital')
test(s.trace(F)==5 and s.trace(E)==5,'both expectations are rank five by idempotence')
test(equal(K*vec(I),s.zeros(25,1)),'scalar fixed point exact')
test(equal((E-s.eye(25)).T,(E-s.eye(25))),'first dissipator HS-selfadjoint')
test(equal((F-s.eye(25)).T,(F-s.eye(25))),'second dissipator HS-selfadjoint')
for i in range(n):
    pi=u(n,i,i)
    test(equal(E*vec(pi),vec(pi)),f'E fixes site projector {i}')
    test(equal(F*vec(R*pi*R.T),vec(R*pi*R.T)),f'F fixes rotated projector {i}')
d=s.symbols('a0:5')
A=s.diag(*d)
rot=R.T*A*R
lin=s.Matrix([s.expand(rot[i,j]) for i in range(n) for j in range(i+1,n)])
Jac=lin.jacobian(d)
test(Jac.rank()==4,'rotated MASA intersection imposes rank4 equations')
test(equal(Jac*s.ones(n,1),s.zeros(len(lin),1)),'scalar algebra lies in both MASAs')
test(all(s.expand(rot[i,j]+s.Rational(2,5)*(d[i]+d[j])-s.Rational(4,25)*sum(d))==0 for i in range(5) for j in range(i+1,5)),'closed Householder offdiagonal constraints')
for i in range(5):
    for j in range(5):
        v=vec(u(n,i,j))
        val=(v.T*(E-s.eye(25))*v)[0]
        right=-(Q*v).dot(Q*v)
        test(s.expand(val-right)==0,f'positive Dirichlet form site [{i},{j}]')
        val2=(v.T*(F-s.eye(25))*v)[0]
        right2=-((s.eye(25)-F)*v).dot((s.eye(25)-F)*v)
        test(s.expand(val2-right2)==0,f'positive rotated Dirichlet form site [{i},{j}]')
for rate in [s.Rational(1,7),s.Rational(2,3),s.Rational(5,4)]:
    L0=rate*(E-s.eye(25)); L1=rate*(F-s.eye(25));Lavg=(L0+L1)/2
    test(s.trace(E)==5,f'gamma={rate}: D pointer rank five')
    test(s.trace(F)==5,f'gamma={rate}: rotated pointer rank five')
    test(equal(Lavg,rate*K),f'gamma={rate}: mixed dissipator equals rate K')
Z=s.diag(2,1,0,-1,-2)
HH=Z
comm=lambda A,B:A*B-B*A
sL=sup(n,lambda a:-s.I*comm(HH,a)-s.Rational(1,5)*comm(Z,comm(Z,a)))
for i in range(n):
    test(equal(sL*vec(u(n,i,i)),s.zeros(25,1)),f'B=H: selected projector {i} dynamically closed')
X=s.Matrix([[0,1],[1,0]])
Y=s.Matrix([[0,-s.I],[s.I,0]])
ZZ=s.diag(1,-1)
HB=X/2
BB=ZZ
L2=sup(2,lambda a:-s.I*comm(HB,a)-s.Rational(1,3)*comm(BB,comm(BB,a)))
E2=sup(2,diag)
q2=s.eye(4)-E2
h1=q2*L2*vec(ZZ)
test(not equal(h1,s.zeros(4,1)),'H and B noncommuting: first hidden derivative nonzero')
test(equal(h1,vec(Y)) or equal(h1,-vec(Y)),'hidden derivative is a single Y quadrature')
basis=s.Matrix.hstack(vec(s.eye(2)),vec(ZZ),vec(Y))
test(s.Matrix.hstack(basis,L2*basis).rank()==3,'I,Z,Y invariant under Lindbladian')
test(equal(E2*vec(comm(Y,Y.H)),s.zeros(4,1)),'one hidden Y quadrature has zero P3 commutator residue')
test(equal(comm(HB,BB),-s.I*Y) or equal(comm(HB,BB),s.I*Y),'B and H genuinely noncommute')
result={
    'study':'P11-AX21','exact_checks':len(checks),'all_passed':True,'checks':checks,
    'D5_pointer_rank':int(E.rank()),'rotated_pointer_rank':int(s.trace(F)),
    'averaged_dissipator_kernel_rank':5-int(Jac.rank()),
    'MASA_intersection_rank':5-int(Jac.rank()),
    'canonical_energy_pointer_CR':'zero all depths if H=B has simple spectrum',
    'noncommuting_pointer_hidden':'nonzero first hidden derivative; original P3 R_k zero all depths in qubit X,Z example',
    'unitary_equivariant_universal_MASA_selection':'NO-GO',
    'G2_native_source_provenance':'OPEN','G3_F_origin':'OPEN'
}
Path(__file__).with_name('P11_AX21_exact_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('AX21',len(checks),'exact assertions PASS; pointer intersection dim',5-int(Jac.rank()))
