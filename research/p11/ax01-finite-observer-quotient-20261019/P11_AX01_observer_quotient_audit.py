#!/usr/bin/env python3
"""P11 AX01: exact finite observer quotient / CPTP hidden extension audit."""
import json
from pathlib import Path
import sympy as s
checks=[]
def verify(cond,name):
    assert bool(cond),name
    checks.append(name)
def E(n,i,j):
    a=s.zeros(n);a[i,j]=1;return a
def vec(m):return s.Matrix([m[i,j] for j in range(m.cols) for i in range(m.rows)])
def stackobs(C,F,depth):
    m=C
    for k in range(1,depth):m=m.col_join(C*(F**k))
    return m

P=s.Matrix([[1,s.Rational(1,2),s.Rational(1,4)],
            [0,s.Rational(1,2),s.Rational(1,4)],
            [0,0,s.Rational(1,2)]])
C=s.Matrix([[1,1,0],[0,0,1]])
B=s.Matrix([[1,s.Rational(1,2)],[0,s.Rational(1,2)]])
n=s.Matrix([1,-1,0]);half=s.Rational(1,2)
verify(all(P[i,j]>=0 for i in range(3) for j in range(3)),'P entrywise nonnegative')
for j in range(3):verify(sum(P[:,j])==1,f'P column {j} sum=1')
verify(C*P==B*C,'exact lumped dynamics')
verify(C.rank()==2,'coarse observer rank2')
verify(C*n==s.zeros(2,1),'invisible fibre vector')
verify(P*n==half*n,'invisible fibre invariant')
verify(P.det()==s.Rational(1,4),'classical det1/4')
verify(P.eigenvals()=={s.Integer(1):1,half:2},'repeated nonunit eigenvalue')
verify((P-half*s.eye(3)).rank()==2 and (P-half*s.eye(3))*n==s.zeros(3,1),
       'repeated eigenvalue only hidden eigenvector')

O=stackobs(C,P,3)
verify(O.rank()==2,'finite three-step observation rank2')
verify(O.rank()==2 and O*n==s.zeros(6,1),'invisible states from full future are n')
for k in range(1,7):
    verify(C*P**k==B**k*C,f'future factorization k={k}')
    verify(stackobs(C,P,k).rank()==2,f'finite horizon rank stable {k}')

sec=s.Matrix([[1,0],[0,0],[0,1]])
R=P*sec-sec*B
verify(C*sec==s.eye(2),'section right inverse')
verify(R==n*s.Matrix([[0,-s.Rational(1,4)]]),'hidden extension residue exact')
verify(C*R==s.zeros(2),'residue is invisible')
u,v=s.symbols('u v')
t=n*s.Matrix([[u,v]])
Rnew=s.simplify(P*(sec+t)-(sec+t)*B)
verify(Rnew==n*s.Matrix([[-u/2,-s.Rational(1,4)-u/2]]),'splitting gauge transform')
verify(s.simplify((Rnew[0,1]-Rnew[0,0])+s.Rational(1,4))==0,
       'nonzero extension obstruction independent of section')
verify(s.linsolve((s.Matrix([[s.Rational(-1,2),0],[s.Rational(-1,2),0]]),
                   s.Matrix([0,s.Rational(1,4)])))==s.EmptySet,
       'no invariant section exact linear system')
verify((P-half*s.eye(3)).rank()==2,'Jordan eigenspace dimension1')

Ks=[s.sqrt(P[i,j])*E(3,i,j) for i in range(3) for j in range(3) if P[i,j]]
verify(len(Ks)==6,'number of positive classical Kraus operators')
verify(sum((k.H*k for k in Ks),s.zeros(3))==s.eye(3),'Kraus TP exactly')
def Phi(A):return sum((K*A*K.H for K in Ks),s.zeros(3))
def out(A):return s.Matrix([A[0,0]+A[1,1],A[2,2]])
units=[E(3,i,j) for j in range(3) for i in range(3)]
for k,unit in enumerate(units):
    verify(out(Phi(unit))==B*out(unit),f'CPTP coarse intertwining on E{k}')
for i in range(3):
    verify(Phi(E(3,i,i))==sum((P[j,i]*E(3,j,j) for j in range(3)),s.zeros(3)),
           f'CPTP classical action {i}')
for i in range(3):
    for j in range(3):
        if i!=j:verify(Phi(E(3,i,j))==s.zeros(3),f'CPTP kills offdiag ({i},{j})')
S=s.Matrix.hstack(*(vec(Phi(e)) for e in units))
Obs=s.Matrix.hstack(*(out(e) for e in units))
verify(S.shape==(9,9) and Obs.shape==(2,9),'CPTP Liouville and observer dimensions')
verify(Obs*S==B*Obs,'full complex-space CPTP quotient intertwining')
verify(stackobs(Obs,S,9).rank()==2,'full complex future observer quotient dim2')
verify(len(stackobs(Obs,S,9).nullspace())==7,'full complex hidden N dim7')
verify(S.rank()==3,'measure-prepare superoperator rank3')
verify((S-half*s.eye(9)).rank()==8 and
       (S-half*s.eye(9))*vec(E(3,0,0)-E(3,1,1))==s.zeros(9,1),
       'all full-system lambda=1/2 eigenvectors hidden')

P0=E(2,0,0);P1=E(2,1,1);e01=E(2,0,1);e10=E(2,1,0)
def Delta(A):return P0*A*P0+P1*A*P1
V2=[E(2,i,j) for j in range(2) for i in range(2)]
S2=s.Matrix.hstack(*(vec(Delta(e)) for e in V2))
O2=S2
verify(S2*S2==S2,'dephasing idempotent CPTP')
verify(S2.rank()==2,'dephasing rank2')
verify(stackobs(O2,S2,4).rank()==2,'dephasing observable quotient rank2')
verify(Delta(e01)==s.zeros(2) and Delta(e10)==s.zeros(2),'offdiagonal coherences hidden')
verify(Delta(e01*e10)==P0,'hidden multiplication returns visible diagonal')
verify(Delta(e10*e01)==P1,'opposite hidden multiplication returns visible diagonal')
verify(Delta(e01*e10-e10*e01)==P0-P1,'hidden commutator diagonal return')
verify(P0*e01==e01,'hidden subspace not two-sided ideal')
verify(e01*e10!=s.zeros(2),'multiplication cannot descend to quotient')

X=e01+e10;Y=-s.I*e01+s.I*e10;Z=P0-P1
C_X=s.Matrix([[s.trace(X*a)/2 for a in V2]])
def Adj(U):return s.Matrix.hstack(*(vec(U*a*U.H) for a in V2))
Ppi=Adj(Z)
Pquarter=Adj(s.diag(1,s.I))
verify(C_X.rank()==1,'single X readout rank1')
verify(stackobs(C_X,Ppi,4).rank()==1,'pi sampled process aliases Y')
verify(stackobs(C_X,Pquarter,4).rank()==2,'quarter turn reveals Y')
verify((C_X*vec(Y))[0]==0,'Y initially X-invisible')
verify((C_X*Pquarter*vec(Y))[0]!=0,'Y becomes visible after quarter-turn')
verify((C_X*Ppi*vec(Y))[0]==0,'Y remains pi-stroboscopic invisible')
verify(Pquarter**4==s.eye(4),'quarter turn fourth power identity')
result={'study':'P11-AX01','all_passed':True,'exact_assertions_passed':len(checks),
        'checks':checks,
        'classical_obs_quotient_dim':O.rank(),
        'quantum_obs_quotient_dim':stackobs(Obs,S,9).rank(),
        'quantum_hidden_dim':len(stackobs(Obs,S,9).nullspace()),
        'extension_obstruction':'-1/4',
        'sampling_observability_rank_pi':stackobs(C_X,Ppi,4).rank(),
        'sampling_observability_rank_quarter':stackobs(C_X,Pquarter,4).rank(),
        'p11_generative_completeness':'OPEN','physical_native_source':'OPEN'}
Path(__file__).with_name('P11_AX01_exact_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: P11-AX01 {len(checks)}/{len(checks)} exact assertions')
