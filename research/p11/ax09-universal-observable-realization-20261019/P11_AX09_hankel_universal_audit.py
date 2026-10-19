#!/usr/bin/env python3
"""P11 AX09: exact Hankel minimality and inaccessible micro-source CP witness."""
import itertools,json
from pathlib import Path
import sympy as s
checks=[]
def ck(q,l): assert bool(q),l; checks.append(l)
def E(n,i,j):
    a=s.zeros(n);a[i,j]=1;return a
def words(n):return [w for k in range(n+1) for w in itertools.product((0,1),repeat=k)]
def act(T,w,r):
    for a in w:r=T[a]*r
    return r
def p(T,r,f,w):return (f*act(T,w,r))[0]
def hankel(T,r,f,L,R):return s.Matrix(len(L),len(R),lambda i,j:p(T,r,f,L[i]+R[j]))
def ptB(m):return s.Matrix(2,2,lambda i,j:sum(m[2*i+k,2*j+k] for k in range(2)))
P=s.Matrix([[s.Rational(3,4),s.Rational(1,3)],[s.Rational(1,4),s.Rational(2,3)]])
D0=s.diag(s.Rational(3,4),s.Rational(1,4));D1=s.eye(2)-D0
T={0:P*D0,1:P*D1};r=s.Matrix([s.Rational(2,5),s.Rational(3,5)]);f=s.Matrix([[1,1]])
for j in range(2):ck(sum(P[:,j])==1,f'P stochastic col{j}')
ck(T[0]+T[1]==P,'nonselective P')
ck(f*(T[0]+T[1])==f,'instrument total trace preserving')
for a in (0,1):ck(all(T[a][i,j]>=0 for i in range(2) for j in range(2)),f'positive subchannel{a}')
ck(f*r==s.Matrix([[1]]),'initial normalization')
K={a:[s.sqrt(T[a][j,i])*E(2,j,i) for i in range(2) for j in range(2)] for a in (0,1)}
ck(sum((k.H*k for aa in K.values() for k in aa),s.zeros(2))==s.eye(2),'Kraus sum TP')
def I(a,X):return sum((k*X*k.H for k in K[a]),s.zeros(2))
for a in (0,1):
 for i in range(2):
    ck(I(a,E(2,i,i))==s.diag(*T[a][:,i]),f'Kraus classical a{a} i{i}')
    for j in range(2):
        if i!=j:ck(I(a,E(2,i,j))==s.zeros(2),f'off-diagonal killed a{a} {i}{j}')
W0,W1,W2,W4=words(0),words(1),words(2),words(4)
R0=s.Matrix.hstack(*(act(T,w,r) for w in W0))
R1=s.Matrix.hstack(*(act(T,w,r) for w in W1))
O1=s.Matrix.vstack(*(f*act(T,w,s.eye(2)) for w in W1))
ck(R0.rank()==1,'reachability initial rank1')
ck(R1.rank()==2,'reachability rank2')
ck(O1.rank()==2,'output functional rank2')
H=hankel(T,r,f,W1,W1)
ck(H.rank()==2,'Hankel rank2')
ck(H==R1.T*O1.T,'Hankel row column factorization')
ck(hankel(T,r,f,W2,W2).rank()==2,'Hankel len2')
ck(hankel(T,r,f,W4,W4).rank()==2,'Hankel len4')
ck(p(T,r,f,())==1,'empty word')
ck(p(T,r,f,(0,))==s.Rational(9,20),'p0=9/20')
ck(p(T,r,f,(1,))==s.Rational(11,20),'p1=11/20')
ck(p(T,r,f,(0,0))!=p(T,r,f,(0,))**2,'non-IID')
for n in range(6):
    ck(sum(p(T,r,f,w) for w in itertools.product((0,1),repeat=n))==1,f'normalization n{n}')
S=s.Matrix([[1,1],[0,1]]);Si=S.inv()
Ts={a:S*T[a]*Si for a in (0,1)};rs=S*r;fs=f*Si
ck(S.det()==1,'S invertible')
ck(S.T*S!=s.eye(2),'S nonunitary')
for a in (0,1):ck(Ts[a]==S*T[a]*Si,f'similarity a{a}')
for w in W4:ck(p(Ts,rs,fs,w)==p(T,r,f,w),f'similar word{w}')
ck(hankel(Ts,rs,fs,W1,W1)==H,'Hankel similarity invariant')
T3={a:s.diag(T[a],s.Rational(1,2)) for a in (0,1)}
r3=s.Matrix([r[0],r[1],0]);f3=s.Matrix([[1,1,0]])
for w in W4:ck(p(T3,r3,f3,w)==p(T,r,f,w),f'hidden 3rd word{w}')
ck(s.Matrix.hstack(*(act(T3,w,r3) for w in W2)).rank()==2,'hidden 3rd unreachable')
ck(s.Matrix.vstack(*(f3*act(T3,w,s.eye(3)) for w in W2)).rank()==2,'hidden 3rd unobservable')
Z=s.diag(1,-1);X=s.Matrix([[0,1],[1,0]])
plus=(s.eye(2)+X)/2
initial=s.kronecker_product(s.diag(r[0],r[1]),plus)
ck(s.trace(plus)==1 and plus*plus==plus,'B plus state normalized')
ck(s.trace(Z*plus*Z*X)==-1,'hidden Z flips X')
ck(s.trace(plus*X)==1,'hidden identity keeps X')
ck(plus!=Z*plus*Z,'hidden microstate different')
def joint(a,R,U):
    return sum((s.kronecker_product(k,U)*R*s.kronecker_product(k,U).H for k in K[a]),s.zeros(4))
for w in W4:
    q0=q1=initial
    for a in w:q0=joint(a,q0,s.eye(2));q1=joint(a,q1,Z)
    pw=p(T,r,f,w)
    ck(s.trace(q0)==pw and s.trace(q1)==pw,f'joint word{w}')
    ck(ptB(q0)==ptB(q1),f'reduced joint state{w}')
for a in (0,1):
 for i in range(4):
    for j in range(4):
        m=E(4,i,j)
        ck(ptB(joint(a,m,s.eye(2)))==ptB(joint(a,m,Z)),f'partial trace a{a} E{i}{j}')
p0=E(2,0,0);Had=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
ck(Had*Had.H==s.eye(2),'Hadamard unitary')
ck(Had*p0*Had.H!=p0,'rank1 not invariant under all unitaries')
ck(Z*p0*Z==p0,'rank1 invariant under some unitaries')
result={'study':'P11-AX09','checks_passed':len(checks),'all_passed':True,'checks':checks,
 'hankel_rank':H.rank(),'reachable_dimension':R1.rank(),'observable_dimension':O1.rank(),
 'finite_prefix_suffix_bound':1,'all_finite_words_equivalence':'partial trace induction, finite len<=4 checks',
 'minimality':'unique reachable observable linear representation up to similarity',
 'physical_primitive_identity':'OPEN','observer_effect_origin':'OPEN',
 'F_generativity':'OPEN','P11_generative_completeness':'OPEN'}
Path(__file__).with_name('P11_AX09_exact_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(f'PASS: P11-AX09 {len(checks)}/{len(checks)} exact symbolic assertions')
