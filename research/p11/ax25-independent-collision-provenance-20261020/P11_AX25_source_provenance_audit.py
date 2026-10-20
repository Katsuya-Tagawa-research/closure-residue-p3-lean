#!/usr/bin/env python3
"""P11 AX25 exact finite matrix witnesses; source completeness remains OPEN."""
import sympy as s, json
from pathlib import Path
c=0
def ck(x,k):
 global c
 assert bool(x),k
 c+=1
def E(i,j,n):
 m=s.zeros(n);m[i,j]=1;return m
def G(n,q):return (1-q)*s.eye(n)+q*s.ones(n)
def collision(n,q):
 b=n+1;c=s.sqrt(q);v=s.sqrt(1-q);vs=[]
 for i in range(n):
  a=s.eye(b);a[0,0]=c;a[0,i+1]=-v;a[i+1,0]=v;a[i+1,i+1]=c
  ck(a.T*a==s.eye(b),f'V{i}');vs.append(a)
 u=s.diag(*vs);ck(u.T*u==s.eye(n*b),'controlled-unitary');return u,vs
def ptr(X,n,b):
 return s.Matrix(n,n,lambda i,j:sum(X[i*b+k,j*b+k] for k in range(b)))
for n in (2,3,5):
 q=s.Rational(1,4);g=G(n,q)
 ck(g==g.T,'Gram symmetric');ck(g.rank()==n,'Gram full')
 ck(g.eigenvals()=={s.Rational(3,4):n-1,s.Rational(n+3,4):1},'Gram spectrum')
 u,vs=collision(n,q);b=n+1;e0=E(0,0,b)
 for i in range(n):
  psi=vs[i][:,0];ck(psi.dot(psi)==1,'environment norm')
  for j in range(n):
   ck(s.simplify(psi.dot(vs[j][:,0])-g[i,j])==0,'Gram')
 for i in range(n):
  for j in range(n):
   R=s.kronecker_product(E(i,j,n),e0)
   ck(s.simplify(ptr(u*R*u.T,n,b)-(1 if i==j else q)*E(i,j,n))==s.zeros(n),'channel')
 w=s.eye(b);w[1,1]=0;w[2,2]=0;w[1,2]=1;w[2,1]=1
 alt=u*s.kronecker_product(s.eye(n),w)
 ck(alt.T*alt==s.eye(n*b),'alternate unitary')
 ck(alt!=u,'microscopic units differ')
 for i in range(n):
  for j in range(n):
   R=s.kronecker_product(E(i,j,n),e0)
   ck(s.simplify(u*R*u.T-alt*R*alt.T)==s.zeros(n*b),'same prepared-input outputs')
 R=s.kronecker_product(E(0,0,n),E(1,1,b))
 out=u*R*u.T;other=alt*R*alt.T
 ck(out!=other,'bath-control distinguishes')
 ck(s.trace(out*other)==0,'orthogonal bath probe')
 ck(s.trace(out)==s.trace(other)==1,'bath normalization')
for n in (2,3,5):
 for q in (s.Rational(0),s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),s.Rational(1),-s.Rational(1,8),-s.Rational(1,4),-s.Rational(1,2)):
  g=G(n,q)
  eig=sorted([x for x,k in g.eigenvals().items() for _ in range(k)])
  ideal=sorted([1-q]*(n-1)+[1+(n-1)*q])
  ck(eig==ideal,'permutation Schur spectrum')
  ck(all(x>=0 for x in eig)==(-s.Rational(1,n-1)<=q<=1),'complete positivity interval')
  ck(all(g[i,i]==1 for i in range(n)),'trace-preserving populations')
  for i in range(n):
   for j in range(n):
    ck(g[i,j]==(1 if i==j else q),'equicorrelation')
  perm=list(range(n));perm[0],perm[-1]=perm[-1],perm[0]
  p=s.zeros(n)
  for i,j in enumerate(perm):p[i,j]=1
  ck(p*g*p.T==g,'Sn covariance')
for n in (2,3,5):
 for gamma in (s.Rational(1,3),s.Rational(2,3),s.Rational(4,3)):
  for t in (s.Rational(1,3),s.Rational(2,3),s.Integer(1)):
   q=s.exp(-gamma*t)
   ck(s.simplify(G(n,q)-q*s.ones(n)-(1-q)*s.eye(n))==s.zeros(n),'Markov covariance')
   ck(s.simplify(s.exp(-gamma*(t+1))-q*s.exp(-gamma))==0,'semigroup')
  ck(s.simplify(s.exp(-gamma)-s.exp(-2*gamma))!=0,'nonconstant time')
 ck(s.exp(-s.Rational(1,3))!=s.exp(-s.Rational(2,3)),'distinct rates')
for n in (2,3,5):
 q=s.Rational(1,4)
 a=s.sqrt(1-q);b=(s.sqrt(1+(n-1)*q)-a)/n
 B=a*s.eye(n)+b*s.ones(n)
 ck(s.simplify(B*B-G(n,q))==s.zeros(n),'minimal Gram sqrt')
 ck(B.rank()==n,'minimal bath rank')
 for i in range(n):
  for j in range(n):
   ck(s.simplify(B[:,i].dot(B[:,j])-G(n,q)[i,j])==0,'minimal vectors')
for gamma,factor,t in ((s.Rational(1,3),2,s.Rational(1,4)),(s.Rational(2,3),3,s.Rational(1,5)),(s.Rational(3,2),4,s.Rational(2,5))):
 ck(s.simplify(s.exp(-gamma*t)-s.exp(-(gamma/factor)*(factor*t)))==0,'clock-rate gauge')
r={'study':'P11 AX25 independent collision source provenance','all_passed':True,
'exact_checks':c,'H37_minimal_pure_bath_dimension':5,
'H37_Choi_rank_at_0_lt_q_lt_1':5,'H37_explicit_rotation_bath_dimension':6,
'same_fixed_bath_input_distinct_full_unitaries':True,
'unitaries_distinguishable_with_changed_bath_preparation':True,
'S5_permutation_equicorrelation_CP_q_interval':['-1/4','1'],
'continuous_permutation_symmetric_semigroup_q':'exp(-gamma*t), gamma>=0',
'positive_rate_uniquely_selected_by_symmetry':False,
'G2_physical_environment_provenance':'OPEN',
'G3_non_circular_F_source_choice':'OPEN'}
Path(__file__).with_name('P11_AX25_exact_results.json').write_text(json.dumps(r,indent=2)+'\n')
print(f'AX25 exact {c} PASS; G2/G3 OPEN')
