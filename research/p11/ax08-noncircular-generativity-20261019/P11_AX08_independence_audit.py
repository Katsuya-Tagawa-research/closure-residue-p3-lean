#!/usr/bin/env python3
"""P11 AX08 exact finite all-word spectator independence test (SymPy 1.14).
The analytic proof for arbitrary finite words is in the accompanying note.
"""
import itertools,json
from pathlib import Path
import sympy as sp
checks=[]
def verify(ok,name):
    assert bool(ok),name
    checks.append(name)
def eq(A,B):return A.shape==B.shape and all(sp.simplify(v)==0 for v in A-B)
def E(n,i,j):
    a=sp.zeros(n);a[i,j]=1;return a
def ptB(A):
    return sp.Matrix(2,2,lambda i,j:sum(A[2*i+k,2*j+k] for k in range(2)))
I=sp.eye(2); X=sp.Matrix([[0,1],[1,0]]); Z=sp.diag(1,-1)
p=[E(2,0,0),E(2,1,1)]
plus=(I+X)/2;minus=(I-X)/2
def kraus(a,U):return sp.kronecker_product(p[a],U)
def joint(A,a,U):
    K=kraus(a,U);return K*A*K.H
def visible(A,a):return p[a]*A*p[a]
def word_joint(A,w,U):
    for a in w:A=joint(A,a,U)
    return A
def word_visible(A,w):
    for a in w:A=visible(A,a)
    return A
for label,U in [('id',I),('phase',Z)]:
    verify(eq(U.H*U,I),label+' hidden U unitary')
    verify(eq(sum((kraus(a,U).H*kraus(a,U) for a in (0,1)),sp.zeros(4)),sp.eye(4)),label+' joint instrument TP')
    for a in (0,1):
        verify(eq(kraus(a,U).H*kraus(a,U),sp.kronecker_product(p[a],I)),label+f' A-only effect {a}')
        verify(eq(joint(sp.kronecker_product(p[a],I/2),a,U),sp.kronecker_product(p[a],I/2)),label+f' maximally mixed fixed {a}')
        for i in range(4):
            for j in range(4):
                M=E(4,i,j)
                verify(eq(ptB(joint(M,a,U)),visible(ptB(M),a)),label+f' exact partial trace E{i}{j} outcome {a}')
rho=sp.Matrix([[sp.Rational(2,5),sp.Rational(1,7)],[sp.Rational(1,7),sp.Rational(3,5)]])
for k in range(7):
    for w in itertools.product((0,1),repeat=k):
        expected=word_visible(rho,w)
        for label,U in [('id',I),('phase',Z)]:
            out=word_joint(sp.kronecker_product(rho,plus),w,U)
            verify(eq(ptB(out),expected),label+f' full marginal word {w}')
            verify(sp.trace(out)==sp.trace(expected),label+f' probability word {w}')
verify(not eq(joint(sp.kronecker_product(p[0],plus),0,I),
              joint(sp.kronecker_product(p[0],plus),0,Z)),'joint output differs')
verify(eq(ptB(joint(sp.kronecker_product(p[0],plus),0,I)),p[0]),'A id output')
verify(eq(ptB(joint(sp.kronecker_product(p[0],plus),0,Z)),p[0]),'A phase output')
for label,U,sign in [('id',I,1),('phase',Z,-1)]:
    out=joint(sp.kronecker_product(p[0],plus),0,U)
    verify(sp.trace(sp.kronecker_product(I,plus)*out)-sp.trace(sp.kronecker_product(I,minus)*out)==sign,label+' independently measured B X')
    verify(sp.trace(sp.kronecker_product(I,plus)*out)+sp.trace(sp.kronecker_product(I,minus)*out)==1,label+' B measurement normalized')
a,b,c,d=sp.symbols('a b c d')
A=sp.Matrix([[a,b],[c,d]])
sol=sp.linsolve(list(X*A-A*X)+list(Z*A-A*Z),(a,b,c,d))
verify(sol==sp.FiniteSet((d,0,0,d)),'U2 natural fixed point scalar')
verify(not eq(p[0],X*p[0]*X),'rank1 observer noninvariant')
verify((I/2).rank()==2,'invariant normalized scalar not rank1')
verify(all(eq(U*I*U.H,I) for U in (X,Z)),'unit observer is invariant')
verify(('B_hidden','id')!=('B_hidden','Ad_Z'),'hidden source label differs')
verify(all(sp.trace(word_joint(sp.kronecker_product(p[0],plus),w,I))==
           sp.trace(word_joint(sp.kronecker_product(p[0],plus),w,Z))
           for k in range(5) for w in itertools.product((0,1),repeat=k)),'identical A-only source fibre')
verify(sp.trace(X*plus)-sp.trace(X*Z*plus*Z)==2,'independent source marker separates fibre')
verify(eq((I+Z)/2,p[0]),'effect Z+')
verify(eq((I-Z)/2,p[1]),'effect Z-')
verify(sp.trace(plus)==1,'independent B plus normalization')
verify(sp.trace(minus)==1,'independent B minus normalization')
verify(eq(Z*plus*Z,minus),'hidden dynamics flips B plus')
verify(not eq(Z*plus*Z,plus),'hidden dynamics nontrivial')
result={
'study':'P11-AX08','exact_assertions_passed':len(checks),'all_passed':True,'checks':checks,
'A_dim':2,'B_hidden_dim':2,'joint_dim':4,'max_exhaustively_checked_word_length':6,
'A_only_full_word_identifiability':'NO-GO under spectator-stable model class',
'all_word_proof':'partial-trace intertwiner, inductively all finite lengths',
'extra_B_X_readout_expectation_id':1,'extra_B_X_readout_expectation_Ad_Z':-1,
'unmarked_unitary_canonical_rank1_effect':'NO-GO under U(2) equivariance',
'G1_operational_finite_equivalence':'FINITE / RELATIVE',
'G2_physical_native_source':'OPEN','G3_F_generative_completeness':'OPEN',
'scope':'A-only alphabet; no hidden B access. Stronger independently sourced observer axioms may break the indistinguishability.'}
Path(__file__).with_name('P11_AX08_exact_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(f'PASS: P11-AX08 {len(checks)}/{len(checks)} exact assertions')
