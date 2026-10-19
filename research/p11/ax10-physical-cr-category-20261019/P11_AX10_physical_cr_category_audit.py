#!/usr/bin/env python3
"""P11 AX10 finite category obstruction and minimal Hankel realization audit."""
import json
from itertools import product
from pathlib import Path
import sympy as s

checks=[]
def ck(p,label):
    assert bool(p),label
    checks.append(label)
def E(n,i,j):
    a=s.zeros(n); a[i,j]=1; return a
def eq(a,b):
    return a.shape==b.shape and all(s.simplify(x)==0 for x in a-b)
def vec(a):
    return s.Matrix([a[i,j] for j in range(a.cols) for i in range(a.rows)])
def sop(f,n):
    return s.Matrix.hstack(*(vec(f(E(n,i,j))) for j in range(n) for i in range(n)))
def trB(a):
    return s.Matrix(2,2,lambda i,j:sum(a[2*i+b,2*j+b] for b in range(2)))
def inst(K,a,rho):
    return K[a]*rho*K[a].H
def wordmap(K,rho,w):
    for a in w:rho=inst(K,a,rho)
    return rho
def prob(K,rho,w):
    return s.simplify(s.trace(wordmap(K,rho,w)))
def words(n):
    return [w for k in range(n+1) for w in product([0,1],repeat=k)]

I=s.eye(2);P=[E(2,0,0),E(2,1,1)]
X=E(2,0,1)+E(2,1,0); Z=P[0]-P[1]
rho=(I+X)/2;tau=I/2;joint=s.kronecker_product(rho,tau)
KA=P
KY0=[s.kronecker_product(p,I) for p in P]
KY1=[s.kronecker_product(p,Z) for p in P]
ck(eq(rho,rho.H),'A Hermitian')
ck(s.trace(rho)==1,'A trace one')
ck(eq(rho*rho,rho),'A initial state pure')
ck(eq(tau,tau.H),'B Hermitian')
ck(s.trace(tau)==1,'B trace one')
ck(eq(joint,s.kronecker_product(rho,tau)),'AB product')
ck(s.trace(joint)==1,'AB trace one')
ck(eq(Z*Z,I),'Z involution')
ck(eq(Z,Z.H),'Z Hermitian')
for label,K in [('A',KA),('Y0',KY0),('Y1',KY1)]:
    d=K[0].rows
    ck(eq(sum((k.H*k for k in K),s.zeros(d)),s.eye(d)),f'{label} CPTP normalization')
    for a,k in enumerate(K):
        ck(k.shape==(d,d),f'{label} Kraus square {a}')
        ck(eq(k.H*k,P[a] if d==2 else s.kronecker_product(P[a],I)),f'{label} same POVM {a}')

for w in words(7):
    pa=prob(KA,rho,w);p0=prob(KY0,joint,w);p1=prob(KY1,joint,w)
    ck(pa==p0,f'A equals Y0 word {w}')
    ck(pa==p1,f'A equals Y1 word {w}')
    if len(w)>1 and len(set(w))>1:
        ck(pa==0,f'mixed word probability zero {w}')
    elif len(w)==0:
        ck(pa==1,'empty word probability one')
    else:
        ck(pa==s.Rational(1,2),f'constant word probability half {w}')

for a in range(2):
    for i in range(4):
        for j in range(4):
            x=E(4,i,j);y=trB(x)
            ck(eq(trB(inst(KY0,a,x)),inst(KA,a,y)),f'Y0 intertwine E{i}{j} label {a}')
            ck(eq(trB(inst(KY1,a,x)),inst(KA,a,y)),f'Y1 intertwine E{i}{j} label {a}')

for i in range(2):
    for j in range(2):
        x=E(2,i,j);lift=s.kronecker_product(x,tau)
        ck(eq(trB(lift),x),f'partial trace section retract {i}{j}')
        for a in range(2):
            ck(eq(inst(KY0,a,lift),s.kronecker_product(inst(KA,a,x),tau)),f'Y0 section intertwining {a} E{i}{j}')
            ck(eq(inst(KY1,a,lift),s.kronecker_product(inst(KA,a,x),tau)),f'Y1 section intertwining {a} E{i}{j}')

S0=sop(lambda x:sum((inst(KY0,a,x) for a in range(2)),s.zeros(4)),4)
S1=sop(lambda x:sum((inst(KY1,a,x) for a in range(2)),s.zeros(4)),4)
ck(not eq(S0,S1),'source channels distinct')
ck(S0.rank()==8,'source channel Y0 rank8')
ck(S1.rank()==8,'source channel Y1 rank8')
ck(S0.trace()==8,'Y0 trace8')
ck(S1.trace()==0,'Y1 trace0')
ck(len((S0-s.eye(16)).nullspace())==8,'Y0 +1 multiplicity8')
ck(len((S1-s.eye(16)).nullspace())==4,'Y1 +1 multiplicity4')
ck(len((S1+s.eye(16)).nullspace())==4,'Y1 -1 multiplicity4')
ck(len(S1.nullspace())==8,'Y1 zero multiplicity8')

U=s.kronecker_product(I,Z)
def autob(x):return U*x*U.H
ck(eq(autob(joint),joint),'hidden source automorphism preserves reference state')
for a in range(2):
    for i in range(4):
        for j in range(4):
            x=E(4,i,j)
            ck(eq(autob(inst(KY0,a,x)),inst(KY0,a,autob(x))),f'hidden auto intertwines label {a} E{i}{j}')
x=s.kronecker_product(P[0],E(2,0,1))
ck(not eq(autob(x),x),'hidden automorphism nonidentity')
ck(eq(autob(autob(x)),x),'hidden automorphism inverse')

probe=s.kronecker_product(P[0],(I+X)/2)
o0=inst(KY0,0,probe);o1=inst(KY1,0,probe)
test=s.kronecker_product(I,X)
ck(s.trace(o0)==1,'B probe Y0 normalization')
ck(s.trace(o1)==1,'B probe Y1 normalization')
ck(s.trace(test*o0)==1,'external B-X Y0 expectation +1')
ck(s.trace(test*o1)==-1,'external B-X Y1 expectation -1')

W=[(),(0,),(1,),(0,0),(0,1),(1,0),(1,1)]
H=s.Matrix([[prob(KA,rho,u+v) for v in W] for u in W])
ck(H.rank()==2,'Hankel rank2')
ck(H[0,0]==1,'Hankel empty=1')
ck(H[0,1]==s.Rational(1,2),'Hankel 0=1/2')
ck(H[0,2]==s.Rational(1,2),'Hankel 1=1/2')
ck(H[1,2]==0,'Hankel 01=0')
ck(H[1,1]==s.Rational(1,2),'Hankel 00=1/2')
for w in words(5):
    prediction=1 if not w else (s.Rational(1,2) if len(set(w))==1 else 0)
    ck(prob(KA,rho,w)==prediction,f'all-word closed form witness {w}')

result={'study':'P11-AX10','all_passed':True,'exact_checks':len(checks),'checks':checks,
'observed_A_dimension':2,'joint_AB_dimension':4,
'observed_language_equal_for_all_words':'EXACT, proven via partial trace intertwining',
'nonisomorphic_source_witness':'different nonselective superoperator trace 8 vs 0',
'source_channel_superoperator_traces':[str(S0.trace()),str(S1.trace())],
'nonfaithful_observation_functor':True,'not_essentially_injective_on_source_objects':True,
'minimal_observation_hankel_rank':int(H.rank()),
'physical_source_reconstruction_from_language':'NO-GO in source-extension-closed category',
'gate_G1':'PASS conditional on finite fixed protocol','gate_G2':'OPEN',
'gate_G3_F_generativity':'OPEN','original_P3_residue_identification':'OPEN'}
Path(__file__).with_name('P11_AX10_exact_results.json').write_text(
    json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(f"P11–AX10 PASS {len(checks)}/{len(checks)} exact checks; Hankel rank {H.rank()}")
