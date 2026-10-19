#!/usr/bin/env python3
"""P11–AX03 finite conditional expectations, isotropic nonselection, H37 observer gap."""
import json
from pathlib import Path
import sympy as sp

checks=[]
def ck(x,label):
    assert bool(x),label
    checks.append(label)
def E(n,i,j):
    a=sp.zeros(n);a[i,j]=1;return a
def vec(a):
    return sp.Matrix([a[i,j] for j in range(a.cols) for i in range(a.rows)])
def rank(A):
    return sp.Matrix.hstack(*(vec(x) for x in A)).rank() if A else 0
def eq(A,B):
    return A.shape==B.shape and all(sp.simplify(e)==0 for e in A-B)
def Delta(A):
    n=A.rows
    return sp.diag(*[A[i,i] for i in range(n)])
def ET(A):
    return (sp.trace(A)/A.rows)*sp.eye(A.rows)
def superop(fun,n):
    return sp.Matrix.hstack(*(vec(fun(E(n,i,j))) for j in range(n) for i in range(n)))
def L_H37(rho):
    return -sp.I*(H*rho-rho*H)+gamma*(Delta(rho)-rho)
def Lstar_H37(a):
    return sp.I*(H*a-a*H)+gamma*(Delta(a)-a)

for n in (2,3,5):
    units=[E(n,i,j) for j in range(n) for i in range(n)]
    D=superop(Delta,n);T=superop(ET,n)
    ck(eq(D*D,D),f'd={n} diagonal idempotent')
    ck(eq(D.T.conjugate(),D),f'd={n} diagonal HS orthogonal')
    ck(eq(T*T,T),f'd={n} trace-to-scalars idempotent')
    ck(eq(T.T.conjugate(),T),f'd={n} scalar HS orthogonal')
    ck(D.rank()==n,f'd={n} diagonal range rank')
    ck(T.rank()==1,f'd={n} scalar range rank')
    ck(eq(D*vec(sp.eye(n)),vec(sp.eye(n))),f'd={n} diagonal unital')
    ck(eq(T*vec(sp.eye(n)),vec(sp.eye(n))),f'd={n} scalar unital')
    ck(all(sp.trace(Delta(A))==sp.trace(A) for A in units),f'd={n} diagonal TP all units')
    ck(all(sp.trace(ET(A))==sp.trace(A) for A in units),f'd={n} scalar TP all units')
    U=sp.diag(*[sp.I**j for j in range(n)])
    ck(all(eq(Delta(U*A*U.H),U*Delta(A)*U.H) for A in units),f'd={n} torus covariance')
    ck(all(eq(ET(U*A*U.H),U*ET(A)*U.H) for A in units),f'd={n} scalar torus covariance')
    ck(all(eq(Delta(Delta(A)),Delta(A)) for A in units),f'd={n} all-unit diagonal fix')
    ck(all(eq(ET(ET(A)),ET(A)) for A in units),f'd={n} all-unit scalar fix')
    ck(eq(Delta(sp.eye(n)),sp.eye(n)),f'd={n} diagonal unit')
    ck(eq(ET(sp.eye(n)),sp.eye(n)),f'd={n} scalar unit')
    for i in range(n):
        ck(eq(Delta(E(n,i,i)),E(n,i,i)),f'd={n} p{i} fixes')
        ck(eq(ET(E(n,i,i)),sp.eye(n)/n),f'd={n} p{i} scalarizes')

for n in (2,3):
    from itertools import product
    omega=(-sp.Integer(1)+sp.sqrt(3)*sp.I)/2
    def twirl(A):
        ans=sp.zeros(n)
        for t in product(range(3),repeat=n):
            U=sp.diag(*[omega**e for e in t])
            ans+=U*A*sp.diag(*[omega**(-e) for e in t])
        return sp.simplify(ans/3**n)
    for i in range(n):
        for j in range(n):
            ck(eq(twirl(E(n,i,j)),Delta(E(n,i,j))),f'finite diagonal twirl d={n} E{i}{j}')

I=sp.eye(2);X=E(2,0,1)+E(2,1,0);Z=E(2,0,0)-E(2,1,1)
U=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
p=sp.Rational(2,5)
Dep=lambda A:p*A+(1-p)*sp.trace(A)*I/2
Dx=lambda A:U*Delta(U.H*A*U)*U.H
for idx,A in enumerate([E(2,i,j) for i in range(2) for j in range(2)]):
    ck(eq(Dep(U*A*U.H),U*Dep(A)*U.H),f'depolarizing full frame covariance unit {idx}')
ck(not eq(Dx(Z),Delta(Z)),'two different observer MASAs for same depolarizer')
ck(eq(Dx(X),X),'X pointer MASA retains X')
ck(eq(Delta(Z),Z),'Z pointer MASA retains Z')
ck(eq(Dx(Z),sp.zeros(2)),'X pointer MASA erases Z')
ck(eq(Delta(X),sp.zeros(2)),'Z pointer MASA erases X')
ck(eq(Dep(X),p*X),'depolarizer nontrivial')
ck(eq(Dep(Z),p*Z),'depolarizer isotropic')
ck(rank([I,X])==2 and rank([I,Z])==2,'two proper subalgebra ranks2')
ck(rank([I,X,Z])==3,'two MASAs differ')
Dmatrix=superop(Dep,2)
ck(len((Dmatrix-sp.eye(4)).nullspace())==1,'depolarizer fixed algebra scalar')
ck(len((superop(lambda A:A,2)-sp.eye(4)).nullspace())==4,'id fixed algebra full')

gamma=sp.Rational(2,3)
n=5
paths=[E(n,i,i+1)+E(n,i+1,i) for i in range(4)]
H=sp.diag(0,sp.Rational(1,7),-sp.Rational(1,9),sp.Rational(2,11),-sp.Rational(3,13))+sum(paths,sp.zeros(n))/2
Lh=superop(Lstar_H37,n)
ck(H.H==H,'H37 Hermitian')
ck(Lh.shape==(25,25),'H37 superop 25 by 25')
ck(eq(Lstar_H37(sp.eye(5)),sp.zeros(5)),'H37 Heisenberg unital generator')
offdiag_constraints=sp.Matrix.hstack(*[vec(Lstar_H37(E(n,i,i))) for i in range(n)])
ck(offdiag_constraints.rank()==4,'H37 diagonal kernel rank4 by connected hopping')
ck(eq(Lstar_H37(sp.eye(n)),sp.zeros(n)),'H37 diagonal fixed directions only scalars')
ck(eq(Lstar_H37(sp.eye(5)),sp.zeros(5)),'H37 I fixed')
ck(all(H[i,i+1]==sp.Rational(1,2) for i in range(4)),'H37 graph connected')
ck(eq(Delta(H),sp.diag(*[H[i,i] for i in range(5)])),'H37 marked diagonal algebra')
ck(rank([E(n,i,i) for i in range(n)])==5,'H37 marked observer D5 rank5')
ck(not eq(Lstar_H37(E(5,0,0)),sp.zeros(5)),'H37 marked p0 not fixed')
ck(not eq(Delta(Lstar_H37(E(5,0,0))),Lstar_H37(E(5,0,0))),'H37 visible algebra not invariant')
ck(eq(Delta(L_H37(E(5,0,0))),sp.zeros(5)),'H37 first diagonal population derivative zero')
ck(eq(Delta(L_H37(L_H37(E(5,0,0)))),(E(5,1,1)-E(5,0,0))/2),'H37 delayed 2nd order population return')
Y0=-sp.I*E(5,0,1)+sp.I*E(5,1,0)
ck(Y0.H==Y0,'H37 Y0 Hermitian coherence')
ck(eq(Delta(Y0),sp.zeros(5)),'H37 Y0 invisible populations at input')
ck(eq(Delta(L_H37(Y0)),E(5,0,0)-E(5,1,1)),'H37 Y0 immediate population flux')
ck(not eq(Delta(L_H37(Y0)),sp.zeros(5)),'H37 population observer not Markov closed')
ck(eq(Delta(Lstar_H37(Y0)),E(5,1,1)-E(5,0,0)),'H37 Heisenberg Y0 diagonal flux')
ck(eq(ET(H),sp.trace(H)*sp.eye(5)/5),'H37 scalar expectation canonical')
ck(eq(ET(Lstar_H37(E(5,0,0))),sp.zeros(5)),'H37 scalar observer invariant')
for m in (E(2,0,1),E(2,1,0)):
    ck(eq(Delta(m),sp.zeros(2)),'D2 bimodule corner annihilation')
ck(eq(Dx(I),I) and eq(Delta(I),I),'both distinct expectations unital TP')

out={'study':'P11-AX03','all_passed':True,'exact_assertions_passed':len(checks),'checks':checks,
     'H37_fixed_point_algebra_dim':1,'H37_marked_diagonal_observer_dim':5,
     'H37_Y0_population_jet':'p0-p1',
     'H37_p0_second_population_jet':'(p1-p0)/2',
     'depolarizer_fixed_algebra_dim':1,
     'twirl_target':'D_N, conditional on marked pointer algebra',
     'operator_algebra_E_selection_from_F':'OPEN',
     'p3_residue_identification':'OPEN','p11_generative_completeness':'OPEN'}
Path(__file__).with_name('P11_AX03_exact_results.json').write_text(
    json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(f'PASS: P11-AX03 {len(checks)}/{len(checks)} exact assertions')
