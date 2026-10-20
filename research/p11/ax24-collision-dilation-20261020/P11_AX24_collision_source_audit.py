#!/usr/bin/env python3
"""AX24: exact finite collision-to-dephasing and Strang/obstruction witnesses.
SymPy 1.14. Finite verification; conditional theorem arguments in accompanying note.
"""
import json
from pathlib import Path
import sympy as s

checks=0
def ck(p,label):
    global checks
    if p is False or p==s.false:
        raise AssertionError(label)
    if p is not True and p!=s.true:
        raise AssertionError(f'{label}: undetermined {p}')
    checks+=1

def e(n,i,j):
    a=s.zeros(n);a[i,j]=1;return a
def dE(a):return s.diag(*[a[j,j] for j in range(a.rows)])
def unitary_blocks(n,c):
    b=n+1;u=s.zeros(n*b);t=s.sqrt(1-c*c);E0=e(b,0,0)
    for j in range(n):
        k=j+1
        v=s.eye(b)+(c-1)*(E0+e(b,k,k))+t*(e(b,k,0)-e(b,0,k))
        ck(v.T*v==s.eye(b),f'V_j orthogonal n={n} j={j}')
        ck(v[:,0]==c*s.eye(b)[:,0]+t*s.eye(b)[:,k],f'V_j maps vacuum {n} {j}')
        u+=s.kronecker_product(e(n,j,j),v)
    ck(u.T*u==s.eye(n*b),f'controlled unitary {n}')
    return u,[u[j*b:(j+1)*b,j*b:(j+1)*b][:,0] for j in range(n)]

for n in (2,3,5):
    for c in (s.Rational(3,5),s.Rational(4,5)):
        q=c*c;u,states=unitary_blocks(n,c);b=n+1
        gram=s.Matrix([[s.simplify((states[j].T*states[k])[0]) for k in range(n)] for j in range(n)])
        G=(1-q)*s.eye(n)+q*s.ones(n)
        ck(gram==G,f'environment Gram {n} {q}')
        ck(gram.det()==(1-q)**(n-1)*(1+(n-1)*q),f'Choi determinant {n} {q}')
        ck(gram.rank()==n,f'Choi rank {n} {q}')
        for j in range(n):
            ck((states[j].T*states[j])[0]==1,f'env normalized {n} {j}')
        for j in range(n):
            for k in range(n):
                X=e(n,j,k)
                got=sum((states[k][r]*states[j][r] for r in range(b)),s.Integer(0))*X
                expected=q*X+(1-q)*dE(X)
                ck(got==expected,f'channel operator units n={n} {j},{k}')
        for m in (1,2,3,5,10):
            ck(q**m==s.exp(-m*s.log(1/q)),f'exact collision semigroup time {n} {m} {q}')
        for j in range(n):
            ck(q*e(n,j,j)+(1-q)*dE(e(n,j,j))==e(n,j,j),f'population fixed {n} {j}')
        ck((G-s.diag(*[G[k,k] for k in range(n)])).rank()>0,f'nonzero overlap {n}')
for n in (2,3,5):
    for q in (s.Rational(0),s.Rational(1,3),s.Rational(9,25),s.Integer(1)):
        G=(1-q)*s.eye(n)+q*s.ones(n)
        ck(G.rank()==(1 if q==1 else n),f'Choi rank boundary/interior {n},{q}')
        eigen={s.Integer(n):1,s.Integer(0):n-1} if q==1 else ({s.Integer(1):n} if q==0 else {1-q:n-1,1+(n-1)*q:1})
        ck(G.eigenvals()==eigen,f'Choi eigenvalues {n},{q}')

n=5;gamma=s.Rational(2,3);H=s.zeros(n)
for j in range(n-1):H[j,j+1]=H[j+1,j]=s.Rational(1,2)
units=[e(n,i,j) for i in range(n) for j in range(n)]
def a_map(x):return -s.I*(H*x-x*H)
def b_map(x):return gamma*(dE(x)-x)
def vec(x):return s.Matrix([x[i,j] for i in range(n) for j in range(n)])
def represent(f):return s.Matrix.hstack(*[vec(f(m)) for m in units])
A=represent(a_map);B=represent(b_map);L=A+B
ck(A.H==-A,'H37 Hamiltonian anti-Hermitian superoperator')
ck(B.H==B,'H37 dephasing Hermitian superoperator')
ck(B==gamma*(represent(dE)-s.eye(n*n)),'H37 dephasing projection')
ck(B.rank()==n*n-n,'H37 dephasing rank 20')
ck(represent(dE).rank()==n,'H37 observed D5 dim')
C=A*B-B*A
D3=-s.Rational(1,24)*(A*C-C*A)-s.Rational(1,12)*(B*C-C*B)
S2=A*A/2+B*B/2+(A*B+B*A)/2
ck(S2==L*L/2,'Strang order two')
S3=A**3/6+B**3/6+(A*A*B+B*A*A)/8+A*B*A/4+(A*B*B+B*B*A)/4
ck(S3-L**3/6==D3,'Strang third-order Lie-bracket defect')
p0=vec(e(n,0,0))
expected=s.Matrix([s.Rational(1,36),s.I/s.Integer(54),s.Rational(1,144),0,0,
                   -s.I/s.Integer(54),-s.Rational(1,36),0,0,0,
                   s.Rational(1,144),0,0,0,0,
                   0,0,0,0,0,
                   0,0,0,0,0])
ck(D3*p0==expected,'explicit H37 Strang third-order p0 witness')
ck(D3.rank()==11,'nonzero H37 Strang defect rank 11')
for j in range(n):
    ck(dE(a_map(e(n,j,j)))==s.zeros(n),'Hamiltonian first-order population silence')
    ck(dE(b_map(e(n,j,j)))==s.zeros(n),'dephasing first-order population silence')
ck(dE(a_map(a_map(e(n,0,0))))==s.Rational(1,2)*(e(n,1,1)-e(n,0,0)),'H37 projected return')
T=s.symbols('t',real=True)
ck(s.series(s.cos(2*T),T,0,6).removeO()==1-2*T**2+s.Rational(2,3)*T**4,'bounded interaction offdiag cos2t')
ck(s.diff(s.cos(2*T),T).subs(T,0)==0,'bounded collision has zero 1st dissipative derivative')
ck(s.diff(s.cos(2*T),T,2).subs(T,0)==-4,'bounded collision has nonzero 2nd dissipative derivative')
result={
'module':'P11–AX24 Collision-Derived Pure Dephasing and Provenance Gate',
'all_passed':True,'exact_assertions_passed':checks,
'environment_system_dimensions':[2,3,5],
'explicit_controlled_unitary_env_dimension':6,
'minimum_pure_stinespring_environment_dimension_at_0_q_1':5,
'rational_q_values':['9/25','16/25'],
'H37_dephasing_gamma':'2/3','H37_H_nearest_neighbor_coupling':'1/2',
'H37_dephasing_superoperator_rank':B.rank(),
'H37_Strang_first_nonzero_error_degree':3,
'H37_Strang_cubic_defect_rank':D3.rank(),
'H37_Strang_cubic_defect_on_p0':[str(v) for v in expected],
'bounded_H_SE_dissipative_derivative_first_order':0,
'requires_fresh_ancillas':True,
'collision_unitary_identity_distance_scaling':'O(sqrt(Delta))',
'collision_Hamiltonian_norm_scaling':'O(Delta^(-1/2))',
'G1_fixed_protocol':'CONDITIONAL',
'G2_native_source_inventory':'OPEN',
'G3_F_origin_of_environment_and_scaling':'OPEN',
'H37_P3_R2_via_AX16':'CONDITIONAL_SMALL_POSITIVE_TIME',
'no_hardware_verification':True,'no_human_peer_review':True}
Path(__file__).with_name('P11_AX24_exact_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False,default=str)+'\n')
print('AX24',checks,'EXACT symbolic assertions PASS; G2/G3 OPEN')
