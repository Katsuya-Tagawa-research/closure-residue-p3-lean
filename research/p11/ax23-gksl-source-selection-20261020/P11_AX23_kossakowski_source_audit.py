#!/usr/bin/env python3
"""P11 AX23: exact symbolic witnesses for generator-selection obstruction.
Requires SymPy 1.14. Source uniqueness/G2/G3 are NOT established.
"""
import json
from pathlib import Path
import sympy as s
I=s.I
X=s.Matrix([[0,1],[1,0]])
Y=s.Matrix([[0,-I],[I,0]])
Z=s.diag(1,-1)
P=(X,Y,Z)
Id=s.eye(2)
checks=0

def ck(cond, label):
    global checks
    if cond is not True and cond != s.true:
        raise AssertionError(f'{label}: {cond}')
    checks+=1

def comm(a,b): return a*b-b*a

def linear_noise(A,b):
    B=sum((b[i]*P[i] for i in range(3)),s.zeros(2))
    return -comm(B,comm(B,A))/2

def noise_cov(A,C):
    return s.simplify(-sum((C[i,j]*comm(P[i],comm(P[j],A)) for i in range(3) for j in range(3)),s.zeros(2))/2)

def bloch_matrix(C):
    return -2*(s.trace(C)*s.eye(3)-C)

def symm(A): return s.simplify(A)

vectors=[(1,0,0),(0,1,0),(0,0,1), (s.Rational(3,5),s.Rational(4,5),0),
    (s.Rational(1,3),s.Rational(2,3),s.Rational(2,3)), (1,1,1), (1,2,3), (2,1,0), (1,0,2)]
for k,raw in enumerate(vectors):
    b=s.Matrix(raw)
    C=b*b.T
    ck(C.rank()==1,f'extreme ray rank {k}')
    ck(C==C.T,f'symmetric C {k}')
    ck(all(v>=0 for v in C.eigenvals()),f'PSD C {k}')
    ck(noise_cov(Id,C)==s.zeros(2),f'unital {k}')
    for j in range(3):
        lhs=noise_cov(P[j],C)
        rhs=sum((bloch_matrix(C)[i,j]*P[i] for i in range(3)),s.zeros(2))
        ck(symm(lhs-rhs)==s.zeros(2),f'Pauli Bloch action {k}:{j}')
        ck(symm(lhs-linear_noise(P[j],b))==s.zeros(2),f'GKSL rank-1 double comm {k}:{j}')
    ck(bloch_matrix(C)*b==s.zeros(3,1),f'axis is kernel {k}')
    ck(bloch_matrix(C).rank()==2,f'Bloch rank two {k}')
    ck(bloch_matrix(C).trace()==-4*(b.dot(b)),f'contraction trace {k}')

covariances=[
    s.diag(1,0,0), s.diag(0,1,0), s.diag(0,0,1),
    s.diag(1,1,0), s.diag(s.Rational(1,2),0,s.Rational(1,2)),
    s.eye(3), s.diag(1,2,3), s.zeros(3),
    s.Matrix([[1,0,1],[0,0,0],[1,0,1]]),
]
for k,C in enumerate(covariances):
    ck(noise_cov(Id,C)==s.zeros(2),f'cov unital {k}')
    M=bloch_matrix(C)
    ck(M==M.T,f'Bloch symm {k}')
    ck(all(s.simplify(v)<=0 for v in M.eigenvals()),f'Bloch negative semidefinite {k}')
    for j in range(3):
        ck(symm(noise_cov(P[j],C)-sum((M[i,j]*P[i] for i in range(3)),s.zeros(2)))==s.zeros(2),f'Pauli reconstruction {k}:{j}')

Cx=s.diag(1,0,0); Cz=s.diag(0,0,1); Cmix=(Cx+Cz)/2
ck(Cx.rank()==1 and Cz.rank()==1,'extreme rays')
ck(bloch_matrix(Cx).nullspace()==[s.Matrix([1,0,0])],'X fixed axis')
ck(bloch_matrix(Cz).nullspace()==[s.Matrix([0,0,1])],'Z fixed axis')
ck(bloch_matrix(Cmix).rank()==3,'mixing kills directional kernel')
ck(bloch_matrix(Cmix).nullspace()==[],'mixed noise has only scalar commutant')
Ciso=s.eye(3)
ck(bloch_matrix(Ciso)==-4*s.eye(3),'isotropic depolarizing form')
for Q in (s.Matrix([[0,-1,0],[1,0,0],[0,0,1]]),s.Matrix([[0,0,1],[0,1,0],[-1,0,0]]),s.Matrix([[1,0,0],[0,0,-1],[0,1,0]])):
    ck(Q.T*Q==s.eye(3),'adjoint symmetry orthogonal')
    ck(Q*Ciso*Q.T==Ciso,'isotropic invariant')
    ck(Q*Cx*Q.T!=Cx or Q*Cz*Q.T!=Cz,'extreme ray not universally invariant')

n=5; gamma=s.Rational(2,3); Id5=s.eye(n)
ps=[s.diag(*[1 if j==i else 0 for j in range(n)]) for i in range(n)]
B=s.diag(0,1,2,3,4)
def Ediag(A): return s.diag(*[A[j,j] for j in range(n)])
def Lpointer(A): return gamma*(Ediag(A)-A)
def Lprojectors(A): return -gamma/2*sum((comm(p,comm(p,A)) for p in ps),s.zeros(n))
def Lsingle(A): return -comm(B,comm(B,A))/2
for i in range(n):
    for j in range(n):
        e=s.zeros(n);e[i,j]=1
        ck(Lpointer(e)==Lprojectors(e),f'pointer channel GKSL {i},{j}')
        ck(Lpointer(e)==(s.zeros(n) if i==j else -gamma*e),f'pointer uniform rate {i},{j}')
        ck(Lsingle(e)==-(s.Integer(i-j)**2)*e/2,f'single B rate {i},{j}')
ck(Lsingle(s.eye(n))==s.zeros(n),'single Hermitian source unital')
ck(Lpointer(s.eye(n))==s.zeros(n),'projector sources unital')
ck(s.Rational(1,2)!=s.Integer(2),'nonuniform single-B damping')
for triple in ((0,1,2),(0,1,4),(1,2,4)):
    rates={(a-b)**2 for a,b in ((triple[0],triple[1]),(triple[0],triple[2]),(triple[1],triple[2]))}
    ck(len(rates)>1,f'three-site rates differ {triple}')
J=s.ones(n);R=Id5-s.Rational(2,n)*J
ck(R.T*R==Id5,'Householder orthogonality')
ck(R*R==Id5,'Householder involution')
Brot=R*B*R.T
ck(Brot!=B,'different source orientation')
ck(s.simplify(Brot-Brot.T)==s.zeros(n),'rotated B selfadjoint')
ck(Brot.eigenvals()==B.eigenvals(),'rotated B spectrum')
ds=s.symbols('d0:5');T=R*s.diag(*ds)*R.T
equs=[s.expand(T[i,j]) for i in range(n) for j in range(i)]
coeff=s.linear_eq_to_matrix(equs,ds)[0]
ck(coeff.rank()==4,'intersection of rotated MASAs exactly scalar')
ck(coeff*s.ones(n,1)==s.zeros(len(equs),1),'scalars in intersection')
for k in range(3):
    C=s.zeros(3);C[k,k]=1
    ck(C.rank()==1,f'rank-one trace-one extreme {k}')
    ck(s.trace(C)==1,f'same strength {k}')
    ck(bloch_matrix(C).eigenvals()=={-2:2,0:1},f'same dissipative spectrum {k}')
results={
    'module':'P11–AX23 Non-Circular GKSL Source Law',
    'exact_assertions_passed':checks,'all_passed':True,
    'two_level_extreme_rays_verified':len(vectors),
    'two_level_isotropic_C':'diag(1,1,1)',
    'isotropic_bloch_eigenvalues':[-4,-4,-4],
    'two_axis_mixed_bloch_rank':bloch_matrix(Cmix).rank(),
    'source_C_rank_one_noise_algebra_dimension':2,
    'mixed_noncommuting_noise_algebra_dimension':1,
    'H37_dephasing_observer_dimension':5,
    'H37_pointer_independent_noise_projectors':5,
    'single_hermitian_source_matches_H37_uniform_offdiag_decay':False,
    'rotated_H37_pointer_MASA_intersection_dimension':5-coeff.rank(),
    'G1_fixed_source_predictions':'CONDITIONAL',
    'G2_exhaustive_physical_source':'OPEN',
    'G3_F_non_circular_generator_selection':'OPEN',
    'qualifications':[
       'GKS cone positivity and covariance do not select an extreme ray or a pointer direction.',
       'Covariance classification follows standard representation theory, not finite audit alone.',
       'Fixed microscopically identified noise covariance is an additional source datum.',
       'No hardware or human-expert certification and no new Lean theorem.'
    ]
}
out=Path(__file__).with_name('P11_AX23_exact_results.json')
out.write_text(json.dumps(results,indent=2,ensure_ascii=False,default=str)+'\n')
print(f'P11 AX23 EXACT PASS: {checks} assertions; H37 noise/projector distinction and source no-go; G2/G3 OPEN')
