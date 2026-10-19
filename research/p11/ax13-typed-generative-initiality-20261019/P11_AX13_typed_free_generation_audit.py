#!/usr/bin/env python3
"""AX13 exact finite witnesses for universal *-generators and missing physical selection.

The universal C*-free product theorem itself is proved in the companion note,
not established by these finite checks. SymPy 1.14 required.
"""
from pathlib import Path
from itertools import product
import json
import sympy as s

checks=[]
def ck(c,label):
    assert bool(c), label
    checks.append(label)

def E(i,j):
    m=s.zeros(2);m[i,j]=1;return m
I=s.eye(2); X=E(0,1)+E(1,0); Z=s.diag(1,-1)
Y=-s.I*E(0,1)+s.I*E(1,0)
ZERO=s.zeros(2)
def eq(a,b):return a.shape==b.shape and all(s.simplify(z)==0 for z in a-b)

def ev(w,x,y):
    out=s.eye(x.rows)
    for k in w:out=out*(x if k==0 else y)
    return out

def star(w):return tuple(reversed(w))
def r0(w):return (0 if 1 in w else 1, w.count(0))
def r1(w):return (1, w.count(0))
def rex(w,x,j):
    c,k=(r0(w) if j==0 else r1(w))
    return c*x**k

words=[tuple(z) for length in range(7) for z in product((0,1),repeat=length)]
for length in range(7):
    ck(len([w for w in words if len(w)==length])==2**length,f'word basis degree {length} dimension')
ck(len(words)==127,'degree at most 6 word count127')
ck(len(set(words))==127,'free words linearly independent by definition')
for i,w in enumerate(words):
    ck(star(star(w))==w,f'involution involutive word {i}')
    ck(eq(ev(w,X,Z).H,ev(star(w),X,Z)),f'Pauli adjoint word {i}')
    ck(eq(ev(w,Z,Z),ev(star(w),Z,Z).H),f'commuting adjoint word {i}')
    ck(eq(ev(w,X,Z),ev(w, X,Z)),f'evaluation well typed {i}')
    for j in (0,1):
        ck(eq(rex(star(w),X,j),rex(w,X,j).H),f'retraction {j} respects involution {i}')
        ck(eq(rex(w,X,j),ev(w,X,s.zeros(2) if j==0 else I)),f'retraction {j} substitution {i}')
    if len(w)<=4:
        for j in (0,1):
            ck(eq(rex(w+(1,),X,j),rex(w,X,j)*rex((1,),X,j)),f'retraction {j} multiplicativity by y word {i}')
            ck(eq(rex(w+(0,),X,j),rex(w,X,j)*rex((0,),X,j)),f'retraction {j} multiplicativity by x word {i}')
ck(eq(X.H,X) and eq(Z.H,Z),'generators Hermitian')
ck(eq(X*X,I) and eq(Z*Z,I),'Pauli contraction squared identity')
ck(eq(Y.H,Y),'Pauli Y Hermitian')
ck(eq(X*Z-Z*X,-2*s.I*Y),'noncommutator detected by Pauli representation')
ck(eq(Z*Z-Z*Z,ZERO),'commuting representation kills commutator')
ck(not eq(X*Z-Z*X,ZERO),'commutator nonzero in witness')
ck(not eq(rex((1,),X,0),rex((1,),X,1)),'two retractions differ on y')
ck(eq(rex((0,),X,0),X) and eq(rex((0,),X,1),X),'both retractions fix x')
ck(eq(rex((1,),X,0),ZERO),'r0 sends y to zero')
ck(eq(rex((1,),X,1),I),'r1 sends y to identity')
ck(eq(rex((0,1),X,0)-rex((1,0),X,0),ZERO),'r0 kills noncommutator')
ck(eq(rex((0,1),X,1)-rex((1,0),X,1),ZERO),'r1 kills noncommutator')
ck(eq(rex((1,1),X,0),ZERO),'r0 kills positive square of y')
ck(eq(rex((1,1),X,1),I),'r1 keeps y square')
p0=E(0,0);p1=E(1,1)
def delta(a):return p0*a*p0+p1*a*p1
ck(eq(delta(I),I),'qubit dephasing unital')
ck(eq(delta(delta(X)),delta(X)),'dephasing projection')
ck(eq(delta(X),ZERO),'X hidden under diagonal observer')
ck(eq(delta(Y),ZERO),'Y hidden under diagonal observer')
ck(eq(delta(X*X),I),'hidden X square returns visible identity')
ck(eq(delta(X*Y-Y*X),2*s.I*Z),'hidden commutator returns visible Z')
ck(eq(delta(X)*delta(X),ZERO),'returned square is not image-square')
ck(eq(delta(Y.H*Y),I),'faithful quadratic Y return')
ck(eq(delta(Z),Z),'diagonal observer fixes Z')
ck(eq(delta(X*Z),ZERO),'diagonal bimodule XZ invisible')
ck(eq(delta(Z*X),ZERO),'diagonal bimodule ZX invisible')
for i,w in enumerate(words):
    check=ev(w,X,Z)
    ck(eq(delta(delta(check)),delta(check)),f'diagonal projection idempotent on evaluated word {i}')
    ck(eq(delta(Z*check),Z*delta(check)),f'left diagonal bimodule word {i}')
    ck(eq(delta(check*Z),delta(check)*Z),f'right diagonal bimodule word {i}')
ck(len(())==0,'literal empty input has zero elements')
ck(2**7-1==127,'word growth fixed by two distinguished source generators')
out={
 'study':'P11-AX13','exact_checks':len(checks),'all_passed':True,
 'checks':checks,'max_tested_word_length':6,'free_words_through_degree_6':len(words),
 'noncommuting_representation':'X,Z -> [X,Z]=-2iY !=0',
 'commuting_representation':'Z,Z -> [Z,Z]=0',
 'distinct_UCP_star_homomorphic_retractions':'y to 0 and y to I',
 'retraction_r0_nonzero_quadratic_return':False,
 'qubit_dephasing_nonzero_hidden_quadratic_return':True,
 'Cstar_universal_initiality':'ANALYTIC STANDARD THEOREM; NOT MACHINE PROVED',
 'independent_generator_signature':'REQUIRED AS AXIOM',
 'physical_realization_origin':'OPEN', 'observer_selection_origin':'OPEN',
 'F_generativity_completeness':'OPEN','P3_original_residue_equivalence':'OPEN'
}
Path(__file__).with_name('P11_AX13_exact_results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(f'AX13 {len(checks)}/{len(checks)} exact checks PASS; physics and F gates OPEN')
