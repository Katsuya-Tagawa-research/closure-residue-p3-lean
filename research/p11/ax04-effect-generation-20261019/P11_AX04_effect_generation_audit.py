#!/usr/bin/env python3
"""P11 AX04 — exact matrix/effect-observer closure tests (SymPy 1.14).
Finite algebra certificates only; no physical measurement source or F-completeness claim.
"""
import json
from pathlib import Path
import sympy as s
checks=[]
def ck(pred,name):
    assert bool(pred),name
    checks.append(name)
def E(n,i,j):
    r=s.zeros(n);r[i,j]=1;return r
def eq(a,b):return a.shape==b.shape and all(s.simplify(x)==0 for x in a-b)
def vec(a):return s.Matrix([a[i,j] for j in range(a.cols) for i in range(a.rows)])
def rank(mm):return s.Matrix.hstack(*[vec(a) for a in mm]).rank() if mm else 0
def in_span(a,mm):return rank(mm+[a])==rank(mm)
def span_same(a,b):return rank(a)==rank(b)==rank(a+b)
def superop(T,n):return s.Matrix.hstack(*[vec(T(E(n,i,j))) for j in range(n) for i in range(n)])
n=5
p=[E(n,i,i) for i in range(n)]
X=[E(n,i,i+1)+E(n,i+1,i) for i in range(n-1)]
Y=[-s.I*E(n,i,i+1)+s.I*E(n,i+1,i) for i in range(n-1)]
K=[E(n,i,i+1)-E(n,i+1,i) for i in range(n-1)]
H=s.diag(0,s.Rational(1,7),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13))+sum(X,s.zeros(n))/2
gamma=s.Rational(2,3)
def Delta(a):return s.diag(*[a[i,i] for i in range(n)])
def Ldag(a):return s.I*(H*a-a*H)+gamma*(Delta(a)-a)
def Lsch(a):return -s.I*(H*a-a*H)+gamma*(Delta(a)-a)
ck(eq(H,H.H),'H37 selfadjoint')
ck(eq(Ldag(s.eye(n)),s.zeros(n)),'Heisenberg generator unital derivative')
ck(rank(p)==5,'full diagonal effect algebra rank5')
for i in range(n-1):
    ck(eq(p[i]*Ldag(p[i])*p[i+1],-s.I*E(n,i,i+1)/2),f'isolated directed edge {i}->{i+1}')
    ck(eq(p[i+1]*Ldag(p[i])*p[i],s.I*E(n,i+1,i)/2),f'isolated reverse edge {i+1}->{i}')
    ck(eq(Delta(Ldag(p[i])),s.zeros(n)),f'no first-order population drift from diagonal p{i}')
    ck(eq(Ldag(p[i]),Ldag(p[i]).H),f'Heisenberg effect derivative Hermitian i={i}')
ck(eq(Delta(Ldag(p[-1])),s.zeros(n)),'terminal diagonal first-order zero')
ck(rank(p+[Ldag(a) for a in p])==9,'linear span effects plus first derivative rank9, not all algebra')
for i in range(n):
    for j in range(n):
        word=s.eye(n)
        if i==j:word=p[i]
        elif i<j:
            for k in range(i,j):word=word*E(n,k,k+1)
        else:
            for k in range(i,j,-1):word=word*E(n,k,k-1)
        ck(eq(word,E(n,i,j)),f'edge path product generates E{i}{j}')
ck(rank([E(n,i,j) for i in range(n) for j in range(n)])==25,'H37 invariant effect-algebra full M5')
def block_alg(m):
    basis=[E(n,i,j) for i in range(m) for j in range(m)]
    if m<n:basis.append(sum(p[m:],s.zeros(n)))
    return basis
expected=[2,5,10,17,25]
for m in range(1,n+1):
    A=block_alg(m)
    ck(rank(A)==expected[m-1],f'endpoint tower grade {m-1} dimension {expected[m-1]}')
    ck(all(in_span(a.H,A) for a in A),f'endpoint grade {m-1} star-closed')
    for a in A:
        ck(eq(a*sum(p[m:],s.zeros(n)),s.zeros(n)) if (m<n and a!=A[-1]) else True,
           f'endpoint prefix block orthogonal tail m{m} vector')
    if m<n:
        Ap=block_alg(m+1)
        for a in A:
            ck(in_span(Ldag(a),Ap),f'endpoint grade {m-1} image lies grade {m}')
        outgoing=p[m-1]*Ldag(p[m-1])*sum(p[m:],s.zeros(n))
        ck(eq(outgoing,-s.I*E(n,m-1,m)/2),f'endpoint boundary creates edge {m-1}->{m}')
        ck(in_span(outgoing,Ap),f'endpoint extracted edge in enlarged algebra m{m}')
    else:
        ck(all(in_span(Ldag(a),A) for a in A),'full tower Heisenberg invariant')
y=Y[0]
ck(eq(Delta(y),s.zeros(n)),'Y01 invisible to population observer')
ck(eq(Delta(Lsch(y)),p[0]-p[1]),'hidden phase first-order population return')
ck(eq(Delta(Lsch(p[0])),s.zeros(n)),'population p0 first derivative invisible')
ck(eq(Delta(Lsch(Lsch(p[0]))),(p[1]-p[0])/2),'p0 second derivative population transport')
ck(not eq(Delta(Lsch(y)),Delta(Lsch(Delta(y)))),'E L != E L E on Y01')
ck(eq(Delta(Lsch(p[0])),Delta(Lsch(Delta(p[0])))),'closure agreement on visible p0 alone')
Ld=superop(Ldag,n)
Dd=superop(Delta,n)
ck(not eq(Dd*Ld,Dd*Ld*Dd),'H37 Heisenberg observation is not autonomous')
Ls=superop(Lsch,n)
ck(not eq(Dd*Ls,Dd*Ls*Dd),'H37 Schr observation is not autonomous')
ck(eq((Ld.T*Dd).T,Dd*Ld),'superoperator orientation check')
I=s.eye(2);z=E(2,0,0)-E(2,1,1);x=E(2,0,1)+E(2,1,0)
y2=-s.I*E(2,0,1)+s.I*E(2,1,0)
MZ=[(I+z)/2,(I-z)/2];MX=[(I+x)/2,(I-x)/2]
ck(eq(sum(MZ,s.zeros(2)),I),'Z POVM normalized')
ck(eq(sum(MX,s.zeros(2)),I),'X POVM normalized')
ck(all(eq(mm,mm.H) for mm in MZ+MX),'all POVM effects Hermitian')
ck(all(mm*mm==mm for mm in MZ+MX),'two projective POVMs')
AZ=[I,z];AX=[I,x]
ck(rank(AZ)==2 and rank(AX)==2,'different POVMs each generate dimension2')
ck(not span_same(AZ,AX),'two declared observer algebras differ')
U=s.diag(1,s.I)
def Psi(a):return U.H*a*U
def EZ(a):return (a+z*a*z)/2
def EX(a):return (a+x*a*x)/2
ck(eq(Psi(z),z),'Z effects under phase evolution invariant')
ck(eq(Psi(x),-y2),'X effect rotates to -Y')
ck(not in_span(Psi(x),AX),'X POVM algebra not invariant')
ck(rank([I,x,Psi(x),x*Psi(x)])==4,'one-step enlarged X observable algebra M2')
ck(eq(EZ(Psi(x)),s.zeros(2)),'E_Z eliminates rotated X')
for aa in [E(2,i,j) for i in range(2) for j in range(2)]:
    ck(eq(EZ(Psi(aa)),EZ(Psi(EZ(aa)))),'Z POVM autonomous equality on matrix-unit basis')
ck(eq(EX(Psi(x)),EX(Psi(EX(x)))),'X pre-visible effect trivially agrees')
ck(not eq(EX(Psi(y2)),EX(Psi(EX(y2)))),'X observable closure fails hidden input Y')
def DeltaZ(a):return (a+z*a*z)/2
ck(eq(DeltaZ(x),s.zeros(2)),'dephasing crushes X but keeps I')
for aa in [E(2,i,j) for i in range(2) for j in range(2)]:
    ck(eq(EX(DeltaZ(aa)),EX(DeltaZ(EX(aa)))),'X effect dephasing E Phi = E Phi E')
    ck(eq(EZ(DeltaZ(aa)),EZ(DeltaZ(EZ(aa)))),'Z effect dephasing E Phi = E Phi E')
ck(all(in_span(DeltaZ(aa),AX) for aa in AX),'X observable algebra invariant under Delta')
out={
  'study':'P11-AX04','checks_passed':len(checks),'all_passed':True,
  'checks':checks,'H37_effect_algebra_dimension':5,
  'H37_minimal_invariant_algebra_dimension':25,
  'H37_full_effect_algebra_generation_grade':1,
  'H37_endpoint_effect_tower_dimensions':expected,
  'H37_population_autonomy':False,
  'two_qubit_POVM_algebras_distinct':True,
  'X_observer_under_phase_gate_closed':False,
  'Z_observer_under_phase_gate_closed':True,
  'abstract_algebraic_closure_not_equivalent_to_experimental_accessibility':True,
  'p11_generative_completeness':'OPEN',
  'observer_effect_origin':'EXTERNALLY MARKED / OPEN FROM F',
  'P3_original_quadratic_residue_identification':'OPEN'}
Path(__file__).with_name('P11_AX04_exact_results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(f'PASS: P11-AX04 {len(checks)}/{len(checks)} exact assertions')
print('H37: D5 -> M5 in one generated *-algebra step; endpoint tower',expected)
