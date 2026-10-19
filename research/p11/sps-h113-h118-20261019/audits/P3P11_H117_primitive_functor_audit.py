#!/usr/bin/env python3
"""H117 exact five-site source-functor / gauge stabilizer audit.
Model boundaries: fixed H37 marked data and optional static-source labels.
Mathematical theorems about descent, equivariant orbit maps and gauge stabilizers
are proved in accompanying Markdown, not formally verified by this code.
"""
from pathlib import Path
import json
import sympy as sp

N=5
I=sp.I
zero=sp.zeros(N)
E=lambda a,b: sp.eye(N)[:,a]*sp.eye(N)[b,:]
p=[E(i,i) for i in range(N)]
X=[E(i,i+1)+E(i+1,i) for i in range(N-1)]
K=[E(i,i+1)-E(i+1,i) for i in range(N-1)]
Hhop=sum(X,sp.zeros(N))/2
Hdiag=sp.diag(0,sp.Rational(1,7),-sp.Rational(1,9),sp.Rational(2,11),-sp.Rational(3,13))
H=Hhop+Hdiag
Jmix=[Hhop]+K
Jfull=[E(e,e+1) for e in range(4)]+[E(e+1,e) for e in range(4)]
S_hop=[Hhop]
S_edges=K
assertions=[]

def check(name,cond):
    assert bool(cond),name
    assertions.append(name)

def vector(A):return sp.Matrix(list(A))
def rank(mats):
    return sp.Matrix.hstack(*(vector(m) for m in mats)).rank() if mats else 0

def inc(A,mats):return rank(mats+[A])==rank(mats)
def same(A,B):return rank(A)==rank(B)==rank(A+B)
def dagger(A):return A.conjugate().T
def closure(S):
    T=[]
    for A in S:
        for B in [A,dagger(A)]:
            for i in range(N):
                for j in range(N):
                    C=p[i]*B*p[j]
                    if C !=zero: T.append(C)
    return T

def anti_to_real(A):
    return sp.Matrix([sp.re(z) for z in A]+[sp.im(z) for z in A])
def xi_basis(S):
    return [A-dagger(A) for A in S]+[I*(A+dagger(A)) for A in S]
def xi_rank(S):
    return sp.Matrix.hstack(*(anti_to_real(A) for A in xi_basis(S))).rank()
def xi_contains(A,S):
    V=[anti_to_real(m) for m in xi_basis(S)]
    return sp.Matrix.hstack(*V,anti_to_real(A)).rank()==sp.Matrix.hstack(*V).rank()
def act(U,A): return U*A*dagger(U)
def act_list(U,L):return [act(U,z) for z in L]

# Fixed microscopic/H37 algebra
check('H37 detunings exact',list(H.diagonal())==[0,sp.Rational(1,7),-sp.Rational(1,9),sp.Rational(2,11),-sp.Rational(3,13)])
check('H37 hop pattern exact',all(H[e,e+1]==sp.Rational(1,2) for e in range(4)))
check('H37 Hermiticity',dagger(H)==H)
check('four independent marked K',rank(K)==4)
check('rank Jmix = 5',rank(Jmix)==5)
check('rank Jfull = 8',rank(Jfull)==8)
check('mixed subspace in full',all(inc(s,Jfull) for s in Jmix))
check('star stable mixed',all(inc(dagger(s),Jmix) for s in Jmix))
check('star stable full',all(inc(dagger(s),Jfull) for s in Jfull))
check('all native Ks in both',all(inc(k,Jmix) and inc(k,Jfull) for k in K))
check('Hhop in both',inc(Hhop,Jmix) and inc(Hhop,Jfull))
check('native residue has rank four',rank([sp.diag(*[(Hhop*k-k*Hhop)[i,i] for i in range(N)]) for k in K])==4)

# CR-marked equal inputs with distinct static sectors
check('Xi of mix dimension 5',xi_rank(Jmix)==5)
check('Xi of full dimension 8',xi_rank(Jfull)==8)
contrast=I*(X[0]-X[1])
check('contrast anti-Hermitian',dagger(contrast)==-contrast)
check('contrast in full Xi',xi_contains(contrast,Jfull))
check('contrast not in mixed Xi',not xi_contains(contrast,Jmix))
check('mix closure equals full',same(closure(Jmix),Jfull))
check('full is bimodule',same(closure(Jfull),Jfull))
check('mix is not bimodule',not same(closure(Jmix),Jmix))

# Two different hypothetical primitive *sources* can generate same sector.
check('hop source rank 1',rank(S_hop)==1)
check('edge source rank 4',rank(S_edges)==4)
check('distinct generating linear spans',not same(S_hop,S_edges))
check('hop source closes to full',same(closure(S_hop),Jfull))
check('edge source closes to full',same(closure(S_edges),Jfull))
check('closure forgets source count',rank(S_hop)!=rank(S_edges) and same(closure(S_hop),closure(S_edges)))

# Diagonal gauge orbit functoriality: two inequivalent equivariant assignments.
U=sp.diag(I,1,1,1,1)
V=sp.diag(1,-1,1,1,1)
UV=U*V
check('unitarity of U',U*dagger(U)==sp.eye(N))
check('unitarity of V',V*dagger(V)==sp.eye(N))
check('composition of marked gauge maps',act(UV,H)==act(U,act(V,H)))
check('composition of mixed functor',same(act_list(UV,Jmix),act_list(U,act_list(V,Jmix))))
check('composition of full functor',same(act_list(UV,Jfull),act_list(U,act_list(V,Jfull))))
check('mixed functor is equivariant at U',same(act_list(U,Jmix),[act(U,Hhop)]+act_list(U,K)))
check('full functor equivariant at U',same(closure(act_list(U,K)),act_list(U,Jfull)))
check('full functor equivariant at V',same(closure(act_list(V,K)),act_list(V,Jfull)))
check('two equivariant assignments remain distinct',rank(act_list(U,Jmix))!=rank(act_list(U,Jfull)))
check('U does not stabilize marked H',act(U,H)!=H)
check('global scalar stabilizes marked data',all(act(I*sp.eye(N),s)==s for s in [H]+K))
check('fixed full sector under U',same(act_list(U,Jfull),Jfull))
check('mixed sector not fixed under U',not same(act_list(U,Jmix),Jmix))

# Stabilizer of H: hopping incidence constraints have rank N-1, phases forced equal.
incidence=sp.zeros(4,N)
for e in range(4):incidence[e,e]=1;incidence[e,e+1]=-1
check('connected hopping graph incidence rank 4',incidence.rank()==4)
check('phase stabilizer kernel is scalar direction',incidence.nullspace()==[sp.ones(N,1)])

# Support-only input fixed by all diagonal gauges cannot select phase-fixed nonzero edge operator.
# Every E_ij, i != j, changes sign under some diagonal V_site.
for e in range(N):
    W=sp.diag(*[-1 if j==e else 1 for j in range(N)])
    check(f'site-{e} diagonal gauge preserves edge support',all((act(W,x))[a,b] == 0 for x in Jfull for a in range(N) for b in range(N) if abs(a-b)!=1))
check('no nonzero offdiag matrix fixed under all site sign gauges',all(any(act(sp.diag(*[-1 if t==i else 1 for t in range(N)]),E(i,j)) != E(i,j) for i in range(N)) for j in range(N) for i in range(N) if i!=j))
check('full support sector remains fixed under every site sign gauge',all(same(act_list(sp.diag(*[-1 if t==i else 1 for t in range(N)]),Jfull),Jfull) for i in range(N)))

# A witness already inside full Xi but outside mix Xi cannot by itself attest native accessibility.
check('contrast not a native tangent',not xi_contains(contrast,K))
check('contrast requires additional phase-sensitive declaration',xi_contains(contrast,Jfull) and not xi_contains(contrast,Jmix))

results={
    'study':'H117 — Primitive Source Functor and Generative Selection No-Go',
    'date':'2026-10-19',
    'system':'Fixed H37 5-site marked input (H, D5, K0..3), static sectors as independent labels',
    'exact_assertions_passed':len(assertions),
    'all_passed':True,
    'complex_sector_ranks':{'Jmix':rank(Jmix),'Jfull':rank(Jfull)},
    'real_Xi_ranks':{'Jmix':xi_rank(Jmix),'Jfull':xi_rank(Jfull)},
    'source_rank_contrast':{'Hhop_source_rank':rank(S_hop),'K_source_rank':rank(S_edges),'common_closure_rank':rank(closure(S_edges))},
    'gauge_H_stabilizer_dimension':len(incidence.nullspace()),
    'phase_contrast_in_Xi_mix':xi_contains(contrast,Jmix),
    'phase_contrast_in_Xi_full':xi_contains(contrast,Jfull),
    'boundaries':['Formal group-action and descent theorems are proved in Markdown, not in a proof assistant', 'No actual alternate hardware source has been independently realized', 'F has not been axiomatized as a source selecting functor', 'No physical P6 test, no GR dynamics or P11 generative completeness'],
    'assertions':assertions
}
pth=Path(__file__).with_name('P3P11_H117_primitive_functor_results.json')
pth.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(f'H117 PASS: {len(assertions)} exact symbolic assertions')
print(json.dumps({k:v for k,v in results.items() if k not in ['assertions','boundaries']},indent=2))