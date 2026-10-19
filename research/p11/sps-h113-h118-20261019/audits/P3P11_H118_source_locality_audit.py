#!/usr/bin/env python3
"""H118 exact H37 sector closure/locality/independent certificate audit.

All checks concern rational five-site matrices or elementary finite fibre
partitions. General universal-property and naturality proofs live in the note.
No claims about certified physical sources or completeness of P11.
"""
import json
from pathlib import Path
import sympy as s
N=5
I=s.I
E=lambda a,b: s.eye(N)[:,a]*s.eye(N)[b,:]
p=[E(i,i) for i in range(N)]
X=[E(i,i+1)+E(i+1,i) for i in range(4)]
K=[E(i,i+1)-E(i+1,i) for i in range(4)]
Hhop=sum(X,s.zeros(N))/2
Hdiag=s.diag(0,s.Rational(1,7),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13))
H=Hhop+Hdiag
Jmix=[Hhop]+K
Jfull=[E(e,e+1) for e in range(4)]+[E(e+1,e) for e in range(4)]
checks=[]
def check(name,predicate):
    if not bool(predicate):raise AssertionError(name)
    checks.append(name)
def dag(A):return A.conjugate().T
def flat(A):return s.Matrix(list(A))
def rank(L): return s.Matrix.hstack(*[flat(a) for a in L]).rank() if L else 0
def same(L,M):return rank(L)==rank(M)==rank(L+M)
def in_span(A,L):return rank(L+[A])==rank(L)
def corner(U,A):
    Q=s.diag(*[int(i in U) for i in range(N)])
    return Q*A*Q
def closure(L):
    B=[]
    for A in L:
        for Z in [A,dag(A)]:
            for i in range(N):
                for j in range(N):
                    c=p[i]*Z*p[j]
                    if c !=s.zeros(N): B.append(c)
    return B
def xi(L):return [A-dag(A) for A in L]+[I*(A+dag(A)) for A in L]
def revec(A):return s.Matrix([s.re(x) for x in A]+[s.im(x) for x in A])
def rrank(L):return s.Matrix.hstack(*[revec(A) for A in L]).rank() if L else 0
def xi_rank(L):return rrank(xi(L))
def act(U,A):return U*A*dag(U)
def act_set(U,L):return [act(U,a) for a in L]

# H37 original dimensions; no new candidate microscopic J sectors
check('H37 hopping component has exact rational coefficient',all(Hhop[e,e+1]==s.Rational(1,2) for e in range(4)))
check('H37 detuning diagonal', list(Hdiag.diagonal())==[0,s.Rational(1,7),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13)])
check('native control rank four',rank(K)==4)
check('Jmix rank five',rank(Jmix)==5)
check('Jfull rank eight',rank(Jfull)==8)
check('Xi mix rank five',xi_rank(Jmix)==5)
check('Xi full rank eight',xi_rank(Jfull)==8)
check('mix is a strict subspace of full',all(in_span(z,Jfull) for z in Jmix) and not same(Jmix,Jfull))
check('closure of hop is full',same(closure([Hhop]),Jfull))
check('closure of four native K is full',same(closure(K),Jfull))
check('closure of mix is full',same(closure(Jmix),Jfull))
check('full closure is itself',same(closure(Jfull),Jfull))
check('mix is not bimodule',not same(closure(Jmix),Jmix))
check('p0 Hhop p1 outside mix',not in_span(p[0]*Hhop*p[1],Jmix))
check('source span dimensions differ',rank([Hhop])==1 and rank(K)==4)
check('two source spans inequivalent',not same([Hhop],K))

# Supports and structural sector locality; diagonal corners of closure
for e in range(4):
    U={e,e+1}
    A=corner(U,Hhop)
    check(f'edge patch {e} hop has only e,e+1 support',all(A[i,j]==0 for i in range(N) for j in range(N) if (i,j) not in [(e,e+1),(e+1,e)]))
    check(f'edge patch {e} closure rank two',rank(closure([A]))==2)
    check(f'edge patch {e} restriction-closure equality',same([corner(U,Z) for Z in closure(K)],closure([corner(U,Z) for Z in K])))
    check(f'edge patch {e} two sources have same sector',same(closure([corner(U,Hhop)]),closure([corner(U,z) for z in K])))

# Edge-cover gluing reproduces sector, though not source labels
patches=[{e,e+1} for e in range(4)]
glued=[z for U in patches for z in closure([corner(U,Hhop)])]
check('edge-cover gluing exactly Jfull',same(glued,Jfull))
check('patch cover recovers eight complex edge matrix units',rank(glued)==8)
# A vertex-only cover loses all offdiagonal edges
singletons=[{i} for i in range(5)]
check('vertex-only patch cover fails',rank([z for U in singletons for z in closure([corner(U,Hhop)])])==0)

# Diagonal gauge covariance for source-closure (and locality)
U=s.diag(I,-1,1,I,-1)
V=s.diag(1,I,-1,1,I)
for name,G in [('U',U),('V',V),('UV',U*V)]:
    check(f'{name} is diagonal unitary',dag(G)*G==s.eye(5))
    check(f'{name}: closure equivariance for hop',same(closure(act_set(G,[Hhop])),act_set(G,closure([Hhop]))))
    check(f'{name}: closure equivariance for native controls',same(closure(act_set(G,K)),act_set(G,closure(K))))
    check(f'{name}: mixed subspace transforms covariantly',rank(act_set(G,Jmix))==5)
check('gauge transformation can move Jmix',not same(act_set(U,Jmix),Jmix))
check('full sector invariant under diagonal gauge',same(act_set(U,Jfull),Jfull))
check('gauge composition on hopping source',act(U*V,Hhop)==act(U,act(V,Hhop)))

# Source vs sector: localized closure cannot identify native actuator count
check('local and global closures agree across differing source families',same(closure([Hhop]),closure(K)))
check('closure map not source injective',rank([Hhop])!=rank(K) and same(closure([Hhop]),closure(K)))

# Independent coherent contrast markers, *if* certified; mathematical only
contrasts=[I*(X[0]-X[1]),I*(X[1]-X[2]),I*(X[2]-X[3])]
for i,C in enumerate(contrasts):
    check(f'contrast {i} anti-Hermitian',dag(C)==-C)
    check(f'contrast {i} in full Xi',rrank(xi(Jfull)+[C])==xi_rank(Jfull))
    check(f'contrast {i} absent from mix Xi',rrank(xi(Jmix)+[C])>xi_rank(Jmix))
check('three contrasts span Xi full with Xi mix',rrank(xi(Jmix)+contrasts)==8)
check('one contrast is insufficient to span full Xi',rrank(xi(Jmix)+contrasts[:1])==6)
check('two contrasts are insufficient to span full Xi',rrank(xi(Jmix)+contrasts[:2])==7)
check('source native K does not span contrast',rrank(xi(K)+contrasts[:1])>xi_rank(K))

# Finite information refinement on the 2-element weak fibre: 
# a constant function of base C does not distinguish; one independent bit does.
models=['mixed','full']
pi=lambda p:'identical-H37-marked-input'
a_from_C=lambda p:'constant'
a_bit=lambda p:0 if p=='mixed' else 1
source=lambda p:p
check('base CR fibre coincides',pi(models[0])==pi(models[1]))
check('source values differ',source(models[0])!=source(models[1]))
check('any base-derived marker remains constant',a_from_C(models[0])==a_from_C(models[1]))
check('independent one-bit label separates binary classes',a_bit(models[0])!=a_bit(models[1]))
check('augmented fibres have constant source',all(source(p)==source(q) for p in models for q in models if (pi(p),a_bit(p))==(pi(q),a_bit(q))))

result={
    'study':'H118 — Axiomatic Source Category and Locality-Preserving Descent',
    'date':'2026-10-19',
    'passed':len(checks), 'all_passed':True,
    'sector_ranks':{'mixed':rank(Jmix),'full':rank(Jfull)},
    'source_ranks':{'hop':rank([Hhop]),'four_native_K':rank(K)},
    'native_Xi_mix_plus_contrasts_ranks':[rrank(xi(Jmix)+contrasts[:n]) for n in range(4)],
    'patch_count':len(patches),'edge_patch_glued_rank':rank(glued),
    'scope':'H37 exact finite matrices and abstract binary information fibre; no native physical evidence',
    'not_proved':['actual source completeness','primitive generation from F','P11 generative completeness','P6 hardware gate','P9 Einstein dynamics'],
    'checks':checks,
}
out=Path(__file__).with_name('P3P11_H118_source_locality_results.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('H118 PASS:',len(checks),'exact assertions')
print('Xi ranks after 0..3 contrast markers:', result['native_Xi_mix_plus_contrasts_ranks'])