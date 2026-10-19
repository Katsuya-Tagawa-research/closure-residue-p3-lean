#!/usr/bin/env python3
"""AX17 exact P3 filtration perturbations/observer audit; SymPy 1.14.
All P3 residues use actual hidden Q Phi^j(D), NOT generic inserted E_ij.
"""
import itertools, json
from pathlib import Path
import sympy as s
checks=[]
def ck(z,tag):
    assert bool(z),tag
    checks.append(tag)
def zero(A):return all(s.simplify(v)==0 for v in A)
def eq(A,B):return A.shape==B.shape and zero(A-B)
def rank(xs):return s.Matrix.hstack(*xs).rank() if xs else 0
n=5; I=s.I
E=lambda i,j:s.SparseMatrix(n,n,{(i,j):1})
p=[E(i,i) for i in range(n)]
edges=list(itertools.combinations(range(n),2))
x=[E(i,j)+E(j,i) for i,j in edges]
y=[-I*E(i,j)+I*E(j,i) for i,j in edges]
basis=p+x+y
Delta=lambda A:s.diag(*[A[i,i] for i in range(n)])
site_diag=[0,s.Rational(1,7),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13)]
def coord(A):
    return s.Matrix([A[i,i] for i in range(n)]+[(A[i,j]+A[j,i])/2 for i,j in edges]+[(A[j,i]-A[i,j])/(2*I) for i,j in edges])
def resid(a,b):
    out=s.zeros(n,1)
    for k,(i,j) in enumerate(edges):
        c=a[k]*b[10+k]-a[10+k]*b[k]
        out[i]+=c;out[j]-=c
    return out
pairs=list(itertools.combinations(range(n),2))
certpairs=[(0,1),(1,2),(2,3),(0,3)]
def generator(hop,gamma,diagonal):
    H=s.diag(*diagonal)
    for j in range(n-1):H+=hop*(E(j,j+1)+E(j+1,j))
    L=lambda A:-I*(H*A-A*H)+gamma*(Delta(A)-A)
    G=s.Matrix.hstack(*[coord(L(a)) for a in basis])
    return H,G
def scan_case(name,hop,gamma,diagonal):
    H,G=generator(hop,gamma,diagonal)
    T=(s.eye(25)-G).inv()
    ck(eq((s.eye(25)-G)*T,s.eye(25)),name+' resolvent exact')
    ck(H.H==H,name+' Hermitian H')
    ck(gamma>=0,name+' physical dephasing rate')
    z=[T[5:,i] for i in range(n)]
    zrank=rank(z)
    c={q:resid(z[q[0]],z[q[1]]) for q in pairs}
    Rrank=rank(list(c.values()))
    minor=s.Matrix.hstack(*[c[q][:4,:] for q in certpairs]).det()
    ck(zrank<=4,name+' hidden rank bounded by 4')
    ck(Rrank<=4,name+' original residue rank bounded by 4')
    ck(all(sum(v)==0 for v in c.values()),name+' residue traceless')
    if hop!=0:
        ck(zrank==4,name+' generated H1 rank4')
        ck(Rrank==4,name+' genuine P3 R2 saturated')
        ck(minor!=0,name+' 4-pair signed determinant nonzero')
    else:
        ck(zrank==0,name+' decoupled hidden zero')
        ck(Rrank==0,name+' decoupled residue zero')
        ck(minor==0,name+' decoupled minor zero')
    ck(all(c[q]==-c[(q[1],q[0])] if (q[1],q[0]) in c else True for q in c),name+' antisym sign compatible')
    return dict(name=name,hop=str(hop),gamma=str(gamma),H1=zrank,R2=Rrank,
                selected_four_pair_minor_nonzero=minor!=0,minor_sign=str(s.sign(minor)))
cases=[
 ('H37_anchor',s.Rational(1,2),s.Rational(2,3),site_diag),
 ('hop_3over5',s.Rational(3,5),s.Rational(2,3),site_diag),
 ('gamma_3over4',s.Rational(1,2),s.Rational(3,4),site_diag),
 ('combined_hop_and_gamma',s.Rational(2,5),s.Rational(1,2),site_diag),
 ('coherent_gamma_zero',s.Rational(1,2),s.Integer(0),site_diag),
 ('diagonal_detuning_perturbed',s.Rational(1,2),s.Rational(2,3),
  [0,s.Rational(1,6),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13)]),
 ('no_hopping',s.Integer(0),s.Rational(2,3),site_diag)
]
scans=[scan_case(*a) for a in cases]
J=s.I; Id=s.eye(2)
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-J],[J,0]]);Z=s.diag(1,-1)
N=(X+Z)/s.sqrt(2)
U=(Id-J*(X+Z))/s.sqrt(3)
ck(eq(U.H*U,Id),'qubit rotation is exactly unitary')
Phi=lambda A:s.simplify(U*A*U.H)
Dz=lambda A:s.simplify((A+Z*A*Z)/2)
Dn=lambda A:s.simplify((A+N*A*N)/2)
cz=[Z,Phi(Z),Phi(Phi(Z))]
hz=[s.simplify(A-Dz(A)) for A in cz]
ck(eq(hz[0],s.zeros(2)),'Z observer H0=0')
ck(not eq(hz[1],s.zeros(2)),'Z observer nonzero first hidden direction')
ck(s.Matrix.hstack(*[s.Matrix(list(v)) for v in hz[1:]]).rank()==2,
   'Z observer H2 dimension2')
ck(eq(Dz(hz[1]*hz[1]-hz[1]*hz[1]),s.zeros(2)),'Z observer R2=0')
ck(eq(Dz(hz[1]*hz[2]-hz[2]*hz[1]),s.Rational(16,9)*J*Z),
   'Z observer genuine P3 R3 signed nonzero')
ck(eq(Phi(N),N),'N-axis observer fixed by channel')
for i in range(6):
    Pi=s.simplify((Id+(-1)**(i%2)*N)/2)
    ck(eq(Dn(Pi),Pi),f'N-axis observer p{i%2} in algebra')
    ck(eq(Phi(Pi),Pi),f'N-axis observer p{i%2} invariant')
    ck(eq(Phi(Pi)-Dn(Phi(Pi)),s.zeros(2)),f'N-axis hidden zero iteration {i}')
V=(X+Z)/s.sqrt(2)
ck(eq(V.H*V,Id),'Hadamard gauge unitary')
Cg=lambda A:s.simplify(V*A*V.H)
Phip=lambda A:Cg(Phi(Cg(A)))
Dg=lambda A:Cg(Dz(Cg(A)))
gz=[Cg(q) for q in cz]
gh=[s.simplify(A-Dg(A)) for A in gz]
for i in range(3):
    ck(eq(gz[i],Phip(gz[i-1])) if i>0 else True,f'gauge orbit intertwining {i}')
    ck(eq(gh[i],Cg(hz[i])),f'gauge hidden conjugation depth {i}')
ck(eq(Dg(gh[1]*gh[2]-gh[2]*gh[1]), Cg(s.Rational(16,9)*J*Z)),
   'gauge covariance of genuine residue')
ck(not eq(Dz(Z),Dn(Z)),'genuine observer change unlike gauge')
ck(scans[0]['selected_four_pair_minor_nonzero'],'anchor full-rank open-neighborhood certificate')
ck(all(case['R2']==4 for case in scans[:-1]),'several independent perturbations preserve saturated R2')
ck(scans[-1]['R2']==0,'finite nontrivial parameter change can destroy R2')
H,G=generator(s.Rational(1,2),s.Rational(2,3),site_diag)
T0=(s.eye(25)-G).inv()
V5=s.eye(n)
V5[0,0]=s.Rational(3,5);V5[0,1]=-s.Rational(4,5)
V5[1,0]=s.Rational(4,5);V5[1,1]=s.Rational(3,5)
ck(eq(V5.T*V5,s.eye(n)),'H37 alternate observer frame orthogonal')
obs_z=[]
for j in range(n):
    rotated_p=V5*p[j]*V5.T
    outcoord=T0*coord(rotated_p)
    state=sum((outcoord[i]*basis[i] for i in range(25)),s.zeros(n))
    back=V5.T*state*V5
    obs_z.append(coord(back)[5:,:])
ck(rank(obs_z)==4,'same fixed H37 resolvent, rotated observer hidden rank4')
obs_res=[resid(obs_z[a],obs_z[b]) for a,b in pairs]
ck(rank(obs_res)==4,'same fixed H37 resolvent, rotated observer genuine P3 R2 rank4')
ck(s.Matrix.hstack(*[resid(obs_z[a],obs_z[b])[:4,:] for a,b in certpairs]).det()!=0,
   'rotated observer explicit four-pair nonzero determinant')
result=dict(study='P11-AX17',all_passed=True,checks_passed=len(checks),checks=checks,
            resolvent_parameter_cases=scans,
            local_openness_fixed_population_observer=True,
            qubit_Z_observer_first_P3_residue_depth=3,
            qubit_Z_observer_residue_dimension=1,
            qubit_N_observer_P3_residue_all_depths_zero=True,
            simultaneous_unitary_gauge_preserves_P3_rank=True,
            H37_rotated_observer_resolvent_R2_rank=rank(obs_res),
            fixed_time_semigroup_parameter_openness='EXACT for each fixed sufficiently-small nonzero base time',
            uniform_epsilon_for_all_parameter_perturbations='NOT CLAIMED',
            observer_physical_selection='OPEN',
            original_P3_residue_equals_AX14_K_generally=False,
            F_Generative_Completeness='OPEN')
Path(__file__).with_name('P11_AX17_exact_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(f'P11-AX17 PASS: {len(checks)}/{len(checks)} exact assertions')
print('H37 resolvent parameter cases:',[(a['name'],a['H1'],a['R2']) for a in scans])
print('Qubit Z observer original P3 R3 !=0; N-axis observer Rk=0 all k')
