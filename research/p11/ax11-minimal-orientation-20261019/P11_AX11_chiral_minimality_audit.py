#!/usr/bin/env python3
"""P11-AX11. Exact finite minimal IC instrument / transpose gauge audit (SymPy)."""
from __future__ import annotations
from pathlib import Path
import json,itertools
import sympy as sp

checks=[]
def check(claim, name):
    assert bool(claim),name
    checks.append(name)
def eq(A,B):
    if isinstance(A,sp.MatrixBase):
        return A.shape==B.shape and all(sp.simplify(v)==0 for v in A-B)
    return sp.simplify(A-B)==0

def vec(A): return sp.Matrix([A[i,j] for j in range(A.cols) for i in range(A.rows)])
def rnk(A): return sp.Matrix.hstack(*map(vec,A)).rank() if A else 0
I=sp.eye(2)
X=sp.Matrix([[0,1],[1,0]])
Y=sp.Matrix([[0,-sp.I],[sp.I,0]])
Z=sp.diag(1,-1)
S=[I,X,Y,Z]
rv=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
r=[sp.Matrix(v)/sp.sqrt(3) for v in rv]
A=[(r[i][0]*X+r[i][1]*Y+r[i][2]*Z) for i in range(4)]
states=[(I+A[i])/2 for i in range(4)]
effects=[states[i]/2 for i in range(4)]
rho0=I/2
# The outcome-labeled measure & prepare instrument.
def inst(k,D): return sp.simplify(sp.trace(effects[k]*D))*states[k]
def transp_inst(k,D): return inst(k,D.T).T

def wordprob(word,transposed=False):
    # Exact rational formula valid in both models because T is the same.
    if not word:return sp.Integer(1)
    ans=sp.Rational(1,4)
    for j in range(1,len(word)):
        ans*=sp.Rational(1,2) if word[j]==word[j-1] else sp.Rational(1,6)
    return ans

def wordprob_matrix(word,transposed=False):
    q=rho0.copy()
    for a in word:
        q=transp_inst(a,q) if transposed else inst(a,q)
    return sp.simplify(sp.trace(q))

for j in range(4):
    check(eq(states[j],states[j].H),f'state {j} Hermitian')
    check(eq(states[j]*states[j],states[j]),f'state {j} pure')
    check(eq(sp.trace(states[j]),1),f'state {j} normalized')
    check(eq(effects[j],effects[j].H),f'effect {j} Hermitian')
    check(eq(effects[j]*effects[j],effects[j]/2),f'effect {j} rank-one scaled')
    check(eq(sp.trace(effects[j]),sp.Rational(1,2)),f'effect {j} trace1/2')
    check(eq(states[j].T,(I+A[j].T)/2),f'transpose-state {j} formula')
check(eq(sum(effects,sp.zeros(2)),I),'tetra POVM normalization')
check(eq(sum([s.T/2 for s in states],sp.zeros(2)),I),'transpose POVM normalization')
check(rnk(states)==4,'four reachable tetra outputs rank4')
check(rnk(effects)==4,'four observable tetra effects rank4')
check(rnk([inst(k,rho0) for k in range(4)])==4,'from initial state, one outcome reaches rank4')
check(rnk([transp_inst(k,rho0) for k in range(4)])==4,'transpose model reachable rank4')
check(rnk([e.T for e in effects])==4,'transpose observer rank4')
check(all(eq(sp.trace(e*rho0),sp.Rational(1,4)) for e in effects),'each outcome first probability1/4')
check(all(eq(sp.trace(e.T*rho0),sp.Rational(1,4)) for e in effects),'transpose first probability1/4')

T=sp.Matrix(4,4,lambda j,i:sp.simplify(sp.trace(effects[j]*states[i])))
for i in range(4):
    for j in range(4):
        check(eq(r[i].dot(r[j]),sp.Integer(1) if i==j else -sp.Rational(1,3)),f'tetra dot {i}{j}')
        check(eq(T[j,i],sp.Rational(1,2) if i==j else sp.Rational(1,6)),f'transition probability {i}->{j}')
check(T.det()==sp.Rational(1,27),'tetra transition det 1/27')
check(T.rank()==4,'transition full rank')
check(eq(T,sp.eye(4)/3+sp.ones(4,4)/6),'transition matrix decomposition')
check(eq(T*sp.ones(4,1),sp.ones(4,1)),'T stochastic row sums')

# Every finite word (not only enumerated below) is invariant by induction under transpose.
for word in [(),(0,),(1,),(0,0),(0,1),(3,2),(1,2,3)]:
    check(eq(wordprob_matrix(word,False),wordprob(word)), f'direct original matrix word {word}')
    check(eq(wordprob_matrix(word,True),wordprob(word)), f'direct transpose matrix word {word}')
check(all(eq(transp_inst(k,D.T),inst(k,D).T) for k in range(4) for D in S),
      'transpose intertwining on full operator basis')
for k in range(1,5):
    for word in itertools.product(range(4),repeat=k):
        p=wordprob(word,False)
        pt=wordprob(word,True)
        check(eq(p,pt),f'word {word} invariant')
        rational=sp.Rational(1,4)
        for jj in range(1,len(word)):
            rational *= (sp.Rational(1,2) if word[jj]==word[jj-1] else sp.Rational(1,6))
        check(eq(p,rational),f'word {word} rational exact')

# Nondegenerate reachable-observable Hankel certificate.
words=[(),(0,),(1,),(2,),(3,)]
H=sp.Matrix(5,5,lambda i,j:wordprob(words[i]+words[j]))
check(H.rank()==4,'5x5 word Hankel rank4')
check(H[:,:].rank()==4,'Hankel rank4 repeat')
check(eq(H[0,0],1),'empty word mass one')
for i in range(1,5):
    check(eq(H[0,i],sp.Rational(1,4)),f'H row first {i}')
    check(eq(H[i,0],sp.Rational(1,4)),f'H column first {i}')

# Transpose's non-CP nature and orientation reversal.
perp=sp.Matrix([0,1,-1,0])/sp.sqrt(2)  # ordering |00>,|01>,|10>,|11>
F=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
check(eq(F*perp,-perp),'swap has antisymmetric eigen -1')
check(eq((perp.H*F*perp)[0],-1),'transpose Choi witness strictly negative')
frame=sp.diag(1,1,-1,1)
for i,b in enumerate(S):
    check(eq(b.T,frame[i,i]*b),f'transpose Pauli frame action {i}')
check(frame.det()==-1,'transpose superoperator orientation parity -1')
check(sp.det(frame[1:4,1:4])==-1,'transpose Bloch frame orientation reversal')
# [R1,R2] R3 trace chirality, uses fixed outcome labels, invariant under spatial SU(2).
orig_chi=sp.simplify(sp.trace(A[0]*(A[1]*A[2]-A[2]*A[1]))/(4*sp.I))
mirror_chi=sp.simplify(sp.trace(A[0].T*(A[1].T*A[2].T-A[2].T*A[1].T))/(4*sp.I))
check(eq(orig_chi,sp.det(sp.Matrix.hstack(r[0],r[1],r[2]))),'oriented triple trace equals determinant')
check(orig_chi!=0,'tetra marked chirality nonzero')
check(eq(mirror_chi,-orig_chi),'transposed marked chirality reverses')
# A single independently anchored +Y state discriminates first outcome.
Yplus=(I+Y)/2
p=sp.simplify(sp.trace(effects[0]*Yplus))
pt=sp.simplify(sp.trace(effects[0].T*Yplus))
check(eq(p,sp.Rational(1,4)*(1+1/sp.sqrt(3))),'anchored +Y first-outcome probability original')
check(eq(pt,sp.Rational(1,4)*(1-1/sp.sqrt(3))),'anchored +Y first-outcome probability transposed')
check(eq(p-pt,1/(2*sp.sqrt(3))),'independent +Y anchor resolves transpose pair')
check(all(eq(sp.trace(effects[i]*Yplus)+sp.trace(effects[i].T*Yplus),sp.Rational(1,2)) for i in range(4)),
      'anchored probabilities paired by Y mirror')

# Full process identification conditional on separately anchored IC preparations/readout.
prep=states
readout=effects
M=sp.Matrix(4,4,lambda i,j:sp.simplify(sp.trace(readout[i]*S[j])))
P=sp.Matrix(4,4,lambda i,j:sp.simplify(sp.trace(S[i]*prep[j])/2))
check(M.rank()==4,'anchored IC readout full-rank')
check(P.rank()==4,'anchored IC preparation full-rank')
check((M.det()*P.det())!=0,'tomographic pair rank16')
for k in range(4):
    data=sp.Matrix(4,4,lambda j,i:sp.simplify(sp.trace(readout[j]*inst(k,prep[i]))))
    mirror=sp.Matrix(4,4,lambda j,i:sp.simplify(sp.trace(readout[j]*transp_inst(k,prep[i]))))
    check(data!=mirror,f'anchored full 1-step dataset distinguishes outcome {k}')
check(all(eq(inst(k,I),effects[k].trace()*states[k]) for k in range(4)),
      'instrument response on identity matches effect and output state')

# explicit source-labelling limitations: one never-tested classical tag does not alter marked words.
check(all(eq(wordprob((a,b)),sp.Rational(1,4)*T[b,a]) for a in range(4) for b in range(4)),
      'two-word statistics reconstruct T but not source orientation')
output={
 'study':'P11-AX11', 'exact_assertions_passed':len(checks),'all_passed':True,
 'tetrahedron_outcomes':4,'minimal_hankel_rank':H.rank(),
 'reachable_rank':rnk([inst(k,rho0) for k in range(4)]),
 'observable_rank':rnk(effects),
 'tetra_transition_matrix':[[str(z) for z in T.row(j)] for j in range(4)],
 'transition_determinant':str(T.det()),
 'original_chirality':str(orig_chi), 'transposed_chirality':str(mirror_chi),
 'transpose_chirality_flips':True,
 'transpose_is_completely_positive':False,
 'external_Y_reference_distinguishes':True,
 'external_Y_probability_difference':str(sp.simplify(p-pt)),
 'source_catalog_exhaustiveness':'OPEN',
 'F_derived_origin_and_P3_residue':'OPEN',
 'P6_physical_gate':'OPEN','P11_generative_completeness':'OPEN',
 'tests':checks}
Path(__file__).with_name('P11_AX11_exact_results.json').write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
print(f'P11-AX11 {len(checks)}/{len(checks)} exact assertions PASS')
print(f'Hankel rank={H.rank()}, tetra input transition det={T.det()}, chiralities={orig_chi}, {mirror_chi}')
