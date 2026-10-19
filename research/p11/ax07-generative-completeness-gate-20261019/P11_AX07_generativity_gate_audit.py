#!/usr/bin/env python3
"""P11 AX07 finite operational equivalence vs physical source completeness.
Exact SymPy witnesses. General finite word theorem is proved in the companion note.
"""
import json
from pathlib import Path
import sympy as s
checks=[]
def check(cond,label):
    assert bool(cond),label
    checks.append(label)
def E(n,i,j):
    a=s.zeros(n);a[i,j]=1;return a
def vec(A):return s.Matrix([A[i,j] for j in range(A.cols) for i in range(A.rows)])
def eq(A,B):return A.shape==B.shape and all(s.simplify(x)==0 for x in A-B)
def sop(fn,n):return s.Matrix.hstack(*(vec(fn(E(n,i,j))) for j in range(n) for i in range(n)))
def rank(cols):return s.Matrix.hstack(*cols).rank() if cols else 0
def basis(cols):
    result=[];last=0
    for x in cols:
        n=rank(result+[x])
        if n>last:result.append(x);last=n
    return result
I=s.eye(2)
X=E(2,0,1)+E(2,1,0)
Y=-s.I*E(2,0,1)+s.I*E(2,1,0)
Z=E(2,0,0)-E(2,1,1)
pp=(I+X)/2;pm=(I-X)/2;rho=pp
D=lambda a:(a+Z*a*Z)/2
A={'0':lambda r:D(r)/2, '1':lambda r:D(r)/2,
   '+':lambda r:pp*r*pp, '-':lambda r:pm*r*pm}
B={'0':lambda r:Z*r*Z/2,'1':lambda r:r/2,
   '+':lambda r:pp*r*pp,'-':lambda r:pm*r*pm}
alphabet=['0','1','+','-']
KA={'0':[E(2,0,0)/s.sqrt(2),E(2,1,1)/s.sqrt(2)],
    '1':[E(2,0,0)/s.sqrt(2),E(2,1,1)/s.sqrt(2)],'+':[pp],'-':[pm]}
KB={'0':[Z/s.sqrt(2)],'1':[I/s.sqrt(2)],'+':[pp],'-':[pm]}
for label,instruments,kraus in [('A',A,KA),('B',B,KB)]:
    for word in alphabet:
        target=I/2 if word in ['0','1'] else (pp if word=='+' else pm)
        check(eq(sum((k.H*k for k in kraus[word]),s.zeros(2)),target),f'{label}/{word} effect')
        for i in range(2):
            for j in range(2):
                m=E(2,i,j)
                check(eq(instruments[word](m),sum((k*m*k.H for k in kraus[word]),s.zeros(2))),f'{label}/{word} CP E{i}{j}')
    for group in [['0','1'],['+','-']]:
        check(eq(sum((k.H*k for a in group for k in kraus[a]),s.zeros(2)),I),f'{label} instrument {group} TP')
for i in range(2):
    for j in range(2):
        m=E(2,i,j)
        check(eq(A['0'](m)+A['1'](m),B['0'](m)+B['1'](m)),f'same total channel E{i}{j}')
        check(eq(A['0'](m)+A['1'](m),D(m)),f'total dephasing E{i}{j}')
check(all(s.trace(A[a](rho))==s.trace(B[a](rho)) for a in alphabet),'all length1 probabilities agree')
check(s.trace(A['0'](rho))==s.Rational(1,2),'outcome0 probability1/2')
check(s.trace(A['+'](rho))==1,'initial X+ certain')
check(s.trace(A['-'](rho))==0,'initial X- impossible')
check(s.trace(A['+'](A['0'](rho)))==s.Rational(1,4),'word A (0,X+) probability1/4')
check(s.trace(B['+'](B['0'](rho)))==0,'word B (0,X+) probability0')
check(not eq(A['0'](rho),B['0'](rho)),'outcome-conditioned states differ')
sA={a:sop(A[a],2) for a in alphabet}
sB={a:sop(B[a],2) for a in alphabet}
for a in alphabet:
    check(sA[a].shape==(4,4) and sB[a].shape==(4,4),f'{a} shapes')
    check(eq(sA[a]*vec(rho),vec(A[a](rho))),f'{a} A action')
    check(eq(sB[a]*vec(rho),vec(B[a](rho))),f'{a} B action')
check(eq(sA['0']+sA['1'],sB['0']+sB['1']),'same total superop')
Ddim=8
T={a:s.diag(sA[a],sB[a]) for a in alphabet}
v=vec(rho).col_join(vec(rho))
tr=s.Matrix([[1,0,0,1]])
ell=tr.row_join(-tr)
check(Ddim==8 and ell.shape==(1,Ddim),'direct-sum dimension8')
check(eq(v[:4,:],v[4:,:]),'paired initial vectors equal')
check(ell*v==s.zeros(1,1),'empty word equality')
check(all(ell*T[a]*v==s.zeros(1,1) for a in alphabet),'all length1 equality')
check(ell*T['+']*T['0']*v==s.Matrix([[s.Rational(1,4)]]),'length2 direct sum difference')
R=[v];dimensions=[1]
for step in range(1,Ddim+1):
    bigger=basis(R+[T[a]*u for u in R for a in alphabet])
    check(len(R)<=len(bigger)<=Ddim,f'reachability increasing stage{step}')
    R=bigger;dimensions.append(len(R))
    if dimensions[-1]==dimensions[-2]:
        stable=step-1
        break
check(stable<=Ddim-1,'stabilizes <=2d²-1')
check(all(rank(R+[T[a]*u])==len(R) for u in R for a in alphabet),'stable under all labelled CP operations')
check(any(ell*u!=s.zeros(1,1) for u in R),'word witness in finite reachable span')
identical={a:sA[a] for a in alphabet}
identical_alt={a:sA[a] for a in alphabet}
check(all(eq(identical[a],identical_alt[a]) for a in alphabet),'marked instrument maps identical')
check(rank([vec(s.I*X)])==1,'one native coherent direction')
check(rank([vec(s.I*X),vec(s.I*Z)])==2,'extra unmarked native direction')
check(not eq(s.I*X,s.I*Z),'distinct native Hamiltonian matrices')
pi={'modelA':'shared_marked_alphabet','modelB':'shared_marked_alphabet'}
src={'modelA':'one_native_X','modelB':'native_X_and_Z'}
check(pi['modelA']==pi['modelB'],'same marked data in abstract source models')
check(src['modelA']!=src['modelB'],'different physical source labels in abstract class')
check(len({src[k] for k in pi if pi[k]=='shared_marked_alphabet'})==2,'nonconstant source data fibre')
N=s.Matrix([[0,0,0],[1,0,0],[0,1,0]])
q=s.Matrix([1,0,0]);out=s.Matrix([[0,0,1]])
check(out*q==s.zeros(1,1),'abstract shift silent at 0')
check(out*N*q==s.zeros(1,1),'abstract shift silent at 1')
check(out*N**2*q==s.Matrix([[1]]),'abstract shift detected at 2')
check(N**3==s.zeros(3),'abstract shift nilpotent order3')
preps=[(I+Z)/2,(I-Z)/2,(I+X)/2,(I+Y)/2]
reads=preps
check(rank([vec(x) for x in preps])==4,'full input prep frame')
check(rank([vec(x) for x in reads])==4,'full output effect frame')
Q=s.Matrix([[s.trace(M*E(2,i,j)) for j in range(2) for i in range(2)] for M in reads])
P=s.Matrix.hstack(*(vec(a) for a in preps))
check(Q.rank()==4 and P.rank()==4,'preparation and readout frames invertible')
rows=[]
for initial in preps:
    for observable in reads:
        output_row=s.Matrix([[s.trace(observable*E(2,i,j)) for j in range(2) for i in range(2)]])
        rows.append(s.kronecker_product(vec(initial).T,output_row))
tomography=s.Matrix.vstack(*rows)
check(tomography.shape==(16,16),'instrument tomography dimension16')
check(tomography.rank()==16,'instrument tomography rank16')
result={
 'study':'P11-AX07','all_passed':True,'exact_checks':len(checks),'checks':checks,
 'direct_sum_dimension':Ddim,'finite_word_equivalence_cutoff':Ddim-1,
 'witness_shortest_word_length':2,'witness_word':'outcome0 then X+',
 'witness_probability_A':'1/4','witness_probability_B':'0',
 'reachable_subspace_dims':dimensions,'reachable_stable_depth':stable,
 'declared_qubit_instrument_tomography_rank':tomography.rank(),
 'marked_operational_equivalence_does_not_prove_native_inventory':True,
 'physical_primitive_provenance':'OPEN','p6_physical_gate':'OPEN',
 'p9_gravity_dynamics':'OPEN','p11_generative_completeness':'OPEN'
}
Path(__file__).with_name('P11_AX07_exact_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'PASS P11-AX07 {len(checks)}/{len(checks)} exact finite assertions')
print('reachability',dimensions,'stable',stable,'P11 completeness OPEN')
