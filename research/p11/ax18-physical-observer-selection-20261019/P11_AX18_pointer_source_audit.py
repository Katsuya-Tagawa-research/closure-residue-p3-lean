#!/usr/bin/env python3
"""P11 AX18: exact symbolic dimension-bounded pointer-source evidence gate."""
import json
from pathlib import Path
import sympy as s
checks=[]
def ck(test,label):
    assert bool(test),label
    checks.append(label)
def Z(A):return all(s.simplify(a)==0 for a in A)
def eq(A,B):return A.shape==B.shape and Z(A-B)
def E(n,i,j):
    out=s.zeros(n);out[i,j]=1;return out
def Tr(A):return s.trace(A)
def hs2(A):return s.expand(Tr(A.H*A))
def span_rank(mats):return s.Matrix.hstack(*[s.Matrix(list(M)) for M in mats]).rank()
n=5
p=[E(n,i,i) for i in range(n)];I=s.eye(n)
for i in range(n):
    ck(eq(p[i].H,p[i]),f'pointer selfadjoint {i}')
    ck(eq(p[i]*p[i],p[i]),f'pointer projection {i}')
    ck(Tr(p[i])==1,f'pointer rankone {i}')
    for j in range(n):
        ck(Tr(p[i]*p[j])==(1 if i==j else 0),f'ideal correlation {i},{j}')
        ck(eq(p[i]*p[j],p[i] if i==j else s.zeros(n)),f'pointer orthogonality {i},{j}')
ck(eq(sum(p,s.zeros(n)),I),'five pointer effects normalize to identity')
ck(span_rank(p)==5,'five pointer effects are linearly independent')
def Delta(A):return sum((u*A*u for u in p),s.zeros(n))
for i in range(n):
    for j in range(n):
        A=E(n,i,j)
        ck(eq(Delta(A),A if i==j else s.zeros(n)),f'Delta matrix unit {i}{j}')
        ck(eq(Delta(Delta(A)),Delta(A)),f'Delta idempotence matrix unit {i}{j}')
ck(eq(Delta(I),I),'Delta unital')
ck(eq(sum((u.H*u for u in p),s.zeros(n)),I),'Delta has Kraus TP')
V=s.eye(n)
V[0,0]=s.Rational(3,5);V[0,1]=-s.Rational(4,5)
V[1,0]=s.Rational(4,5);V[1,1]=s.Rational(3,5)
q=[V*a*V.H for a in p]
ck(eq(V.H*V,I),'rotated Hilbert frame unitary')
for i in range(n):
    ck(eq(q[i]*q[i],q[i]),f'rotated rank-one PVM {i}')
    ck(Tr(q[i])==1,f'rotated state normalized {i}')
    for j in range(n):
        ck(Tr(q[i]*q[j])==(1 if i==j else 0),f'rotated operational table {i},{j}')
ck(not eq(q[0],p[0]),'global unitary gauge leaves table but changes absolute basis')
d6=6
states=[E(d6,i,i) for i in range(5)]
a=[E(d6,i,i) for i in range(5)]
b=[E(d6,i,i) for i in range(5)]
a[0]+=E(d6,5,5);b[1]+=E(d6,5,5)
ck(eq(sum(a,s.zeros(d6)),s.eye(d6)),'first 6D POVM normalized')
ck(eq(sum(b,s.zeros(d6)),s.eye(d6)),'second 6D POVM normalized')
ck(not eq(a[0],b[0]),'different hidden POVM completions')
for i in range(5):
    for j in range(5):
        ck(Tr(states[j]*a[i])==(1 if i==j else 0),f'6D completion A perfect table {i}{j}')
        ck(Tr(states[j]*b[i])==(1 if i==j else 0),f'6D completion B perfect table {i}{j}')
ck(Tr(E(d6,5,5)*a[0])==1 and Tr(E(d6,5,5)*b[0])==0,
   'independent hidden sixth input distinguishes completions')
W=s.eye(n)
W[0,0]=s.Rational(99,101);W[0,1]=-s.Rational(20,101)
W[1,0]=s.Rational(20,101);W[1,1]=s.Rational(99,101)
M=[W*x*W.H for x in p]
err=s.Rational(400,10201)
ck(eq(W.H*W,I),'near-pointer rotation is unitary')
ck(eq(sum(M,s.zeros(n)),I),'rotated noisy pointer POVM normalized')
for i in range(n):
    ck(eq(M[i]*M[i],M[i]),f'noisy rotated effect PVM {i}')
    ck(eq(M[i].H,M[i]),f'noisy rotated effect Hermitian {i}')
    diag=[Tr(M[i]*p[j]) for j in range(n)]
    ck(diag[i]>=1-err,f'calibration correct probability >=1-eps {i}')
    for j in range(n):
        ck(diag[j]<=err if j!=i else diag[j]>=1-err,
           f'calibration confusion entry bound {i}{j}')
    bound=2*(n-1)*err+(n*n-2*n+2)*err**2
    ck(hs2(M[i]-p[i])<=bound,f'HS operator error theorem epsilon {i}')
ck(hs2(M[0]-p[0])==2*err,'actual rankone rotation squared HS distance')
ck(hs2(M[1]-p[1])==2*err,'rotated second effect HS distance')
ck(all(eq(M[i],p[i]) for i in range(2,n)),'unrotated pointer effects preserved')
K_L=p;K_R=[E(n,0,i) for i in range(n)]
ck(eq(sum((k.H*k for k in K_L),s.zeros(n)),I),'Luders instrument TP')
ck(eq(sum((k.H*k for k in K_R),s.zeros(n)),I),'reset instrument TP')
for i in range(n):
    ck(eq(K_L[i].H*K_L[i],p[i]),f'Luders effect {i}')
    ck(eq(K_R[i].H*K_R[i],p[i]),f'reset effect {i}')
    for j in range(n):
        ck(Tr(K_L[i]*p[j]*K_L[i].H)==(1 if i==j else 0),f'Luders first-shot probabilities {i},{j}')
        ck(Tr(K_R[i]*p[j]*K_R[i].H)==(1 if i==j else 0),f'reset first-shot probabilities {i},{j}')
def Iout(K,i,rho):return K[i]*rho*K[i].H
ck(Tr(Iout(K_L,4,Iout(K_L,4,p[4])))==1,'Luders two-step (4,4) probability 1')
ck(Tr(Iout(K_R,4,Iout(K_R,4,p[4])))==0,'reset two-step (4,4) probability 0')
ck(not eq(Iout(K_L,4,p[4]),Iout(K_R,4,p[4])),'same POVM different conditional poststates')
phase=s.diag(1,s.I,1,1,1)
X01=E(n,0,1)+E(n,1,0)
Y01=-s.I*E(n,0,1)+s.I*E(n,1,0)
ck(eq(phase.H*phase,I),'diagonal gauge unitary')
for i in range(n):ck(eq(phase*p[i]*phase.H,p[i]),f'pointer stabilizer gauge {i}')
ck(eq(phase*X01*phase.H,Y01),'phase rotates X01 to Y01')
ck(not eq(phase*X01*phase.H,X01),'coherent phase datum not fixed by pointer POVM')
H=sum((E(n,i,i+1)+E(n,i+1,i) for i in range(4)),s.zeros(n))/2+s.diag(0,s.Rational(1,7),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13))
L=lambda A:-s.I*(H*A-A*H)+s.Rational(2,3)*(Delta(A)-A)
Wret=[Delta(L(L(p[i]))) for i in range(n)]
Wexpected=s.zeros(n)
for i in range(n):
    for j in range(n):Wexpected[j,i]=Wret[i][j,j]
Wpath=s.zeros(n)
for i in range(4):
    Wpath[i,i]-=s.Rational(1,2);Wpath[i+1,i+1]-=s.Rational(1,2)
    Wpath[i,i+1]+=s.Rational(1,2);Wpath[i+1,i]+=s.Rational(1,2)
ck(eq(Wexpected,Wpath),'H37 projected second return weighted path Laplacian')
ck(Wexpected.rank()==4,'H37 projected K rank4 conditional on chosen pointer')
ck(eq(Delta(L(E(n,0,1))),Delta(L(Delta(E(n,0,1))))) is False,
   'chosen pointer algebra need not autonomously close H37 dynamics')
out=dict(study='P11-AX18',all_passed=True,exact_assertions_passed=len(checks),checks=checks,
    perfect_discrimination_dimension=5,perfect_table_rank=5,
    ideal_pointer_effect_algebra_dimension=span_rank(p),
    higher_dimension_ambiguous_completion=True,
    epsilon_exact=str(err),robust_HS_squared_bound='8 epsilon + 17 epsilon^2',
    instrument_same_effects_but_distinct=True,phase_orientation_uncertainty=True,
    H37_conditional_K_rank=Wexpected.rank(),physical_dimension_certification='OPEN',
    actual_device_pointer_source='OPEN',native_inventory_exhaustiveness='OPEN',
    G2_source_observer_completeness='OPEN',G3_F_generative_completeness='OPEN',
    P6_physical_gate='OPEN')
Path(__file__).with_name('P11_AX18_exact_results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(f'P11-AX18 exact checks PASS {len(checks)}/{len(checks)}')
