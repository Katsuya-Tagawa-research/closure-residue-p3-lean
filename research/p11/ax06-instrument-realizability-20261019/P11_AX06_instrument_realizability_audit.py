#!/usr/bin/env python3
"""AX06: exact instrument/POVM/source distinction, symbolic finite witnesses."""
from pathlib import Path
import json
import sympy as s
checks=[]
def ck(cond,name):
    assert bool(cond),name
    checks.append(name)
def E(n,i,j):
    a=s.zeros(n);a[i,j]=1;return a
def eq(a,b):return a.shape==b.shape and all(s.simplify(v)==0 for v in a-b)
def vec(a):return s.Matrix([a[i,j] for j in range(a.cols) for i in range(a.rows)])
def rank(mats):return s.Matrix.hstack(*(vec(m) for m in mats)).rank() if mats else 0
def inst(K,rho):return sum((k*rho*k.H for k in K),s.zeros(rho.rows))
def eff(K):return sum((k.H*k for k in K),s.zeros(K[0].cols))
def dual(K,a):return sum((k.H*a*k for k in K),s.zeros(a.rows))
def matmap(K,n):return s.Matrix.hstack(*(vec(inst(K,E(n,i,j))) for j in range(n) for i in range(n)))
i2=s.eye(2);p0,p1=E(2,0,0),E(2,1,1)
X=E(2,0,1)+E(2,1,0);Y=-s.I*E(2,0,1)+s.I*E(2,1,0);Z=p0-p1
paulis={'x':X,'y':Y,'z':Z}
eigenkets={'x':[s.Matrix([1,1])/s.sqrt(2),s.Matrix([1,-1])/s.sqrt(2)],
           'y':[s.Matrix([1,s.I])/s.sqrt(2),s.Matrix([1,-s.I])/s.sqrt(2)],
           'z':[s.Matrix([1,0]),s.Matrix([0,1])]}
Es=[];Ls=[];Rs=[]
for a,sig in paulis.items():
    for k,sign in enumerate([1,-1]):
        v=eigenkets[a][k];P=(i2+sign*sig)/2
        ck(eq(v*v.H,P),f'{a}{sign} Pauli eigenprojector')
        ck(eq(P*P,P),f'{a}{sign} spectral projector idempotent')
        Es.append(P/3)
        Ls.append([P/s.sqrt(3)])
        Rs.append([s.Matrix([1,0])*v.H/s.sqrt(3)])
ck(eq(sum(Es,s.zeros(2)),i2),'six-outcome Pauli POVM sum to identity')
ck(rank(Es)==4,'six-outcome POVM informationally complete')
ck(rank([i2,X,Y,Z])==4,'Pauli Hermitian operator basis')
for i,(e,l,r) in enumerate(zip(Es,Ls,Rs)):
    ck(eq(eff(l),e),f'Luders effect {i}')
    ck(eq(eff(r),e),f'reset effect {i}')
    ck(eq(dual(l,i2),dual(r,i2)),f'matched one-shot effects {i}')
    ck(eq(e,e.H),f'POVM effect Hermitian {i}')
    ck(e.trace()==s.Rational(1,3),f'POVM effect trace {i}')
for rho in [p0,p1,(i2+X)/2,(i2+Y)/2]:
    for j in range(6):
        ck(s.simplify(s.trace(inst(Ls[j],rho))-s.trace(inst(Rs[j],rho)))==0,
           f'one-shot probabilities match on sample {j}')
last=5
rho=p1
ck(s.simplify(s.trace(inst(Ls[last],rho))-s.Rational(1,3))==0,'Luders first Z- event probability')
ck(s.simplify(s.trace(inst(Rs[last],rho))-s.Rational(1,3))==0,'reset first Z- event probability')
pLL=s.trace(inst(Ls[last],inst(Ls[last],rho)))
pRL=s.trace(inst(Ls[last],inst(Rs[last],rho)))
ck(pLL==s.Rational(1,9),'two-shot Z- Z- Luders 1/9')
ck(pRL==0,'two-shot Z- Z- reset 0')
ck(not eq(inst(Ls[last],rho),inst(Rs[last],rho)),'same POVM different selective operations')
ck(not eq(sum((inst(k,rho) for k in Ls),s.zeros(2)),
          sum((inst(k,rho) for k in Rs),s.zeros(2))),
   'same POVM different nonselective channel')
IA=[[p0/s.sqrt(2),p1/s.sqrt(2)],[p0/s.sqrt(2),p1/s.sqrt(2)]]
IB=[[Z/s.sqrt(2)],[i2/s.sqrt(2)]]
for i in range(2):ck(eq(eff(IA[i]),eff(IB[i])),f'coarse POVM match {i}')
for i in range(2):ck(eq(eff(IA[i]),i2/2),f'coin POVM I/2 outcome {i}')
for i in range(2):
    for j in range(2):
        v=E(2,i,j)
        ck(eq(sum((inst(K,v) for K in IA),s.zeros(2)),
              sum((inst(K,v) for K in IB),s.zeros(2))),
           f'nonselective maps match E{i}{j}')
ck(eq(sum((eff(K) for K in IA),s.zeros(2)),i2),'IA instrument trace preserving')
ck(eq(sum((eff(K) for K in IB),s.zeros(2)),i2),'IB instrument trace preserving')
plus=(i2+X)/2
pA=s.trace(plus*inst(IA[0],plus))
pB=s.trace(plus*inst(IB[0],plus))
ck(pA==s.Rational(1,4),'coarse instrument A conditional X+ joint probability 1/4')
ck(pB==0,'coarse instrument B conditional X+ joint probability zero')
ck(not eq(matmap(IA[0],2),matmap(IB[0],2)),
   'matched POVM and nonselective map not enough for selective map')
Vl=s.kronecker_product(s.Matrix([1,0]),s.Matrix([1,0]))*s.Matrix([[1,0]])+s.kronecker_product(s.Matrix([0,1]),s.Matrix([0,1]))*s.Matrix([[0,1]])
Vr=s.kronecker_product(s.Matrix([1,0]),s.Matrix([1,0]))*s.Matrix([[1,0]])+s.kronecker_product(s.Matrix([1,0]),s.Matrix([0,1]))*s.Matrix([[0,1]])
ck(eq(Vl.H*Vl,i2),'Luders ancilla isometry')
ck(eq(Vr.H*Vr,i2),'reset ancilla isometry')
ck(not eq(Vl,Vr),'different isometric dilations')
for a,V,K in [('Luders',Vl,[[p0],[p1]]),('reset',Vr,[[p0],[E(2,0,1)]])]:
    for j in range(2):
        pointer=s.Matrix([[1,0]]) if j==0 else s.Matrix([[0,1]])
        extracted=s.kronecker_product(i2,pointer)*V
        ck(eq(extracted,K[j][0]),f'{a} ancilla outcome {j} Kraus')
        ck(eq(extracted.H*extracted,[p0,p1][j]),f'{a} ancilla outcome {j} effect')
n=5;Q=[E(n,i,i) for i in range(n)]
L5=[[q] for q in Q]
R5=[[E(n,0,i)] for i in range(n)]
ck(eq(sum((eff(k) for k in L5),s.zeros(n)),s.eye(n)),
   'H37 formal population Luders instrument normalized')
ck(eq(sum((eff(k) for k in R5),s.zeros(n)),s.eye(n)),
   'H37 formal population reset instrument normalized')
for i in range(n):ck(eq(eff(L5[i]),eff(R5[i])),f'H37 same primitive effects {i}')
ck(rank(Q)==5,'H37 initial population one-shot effect rank5')
ck(s.trace(inst(L5[4],Q[4]))==1,'H37 endpoint outcome probability 1')
ck(s.trace(inst(R5[4],Q[4]))==1,'H37 reset endpoint outcome probability 1')
ck(s.trace(inst(L5[4],inst(L5[4],Q[4])))==1,
   'H37 repeated endpoint outcome Luders 1')
ck(s.trace(inst(L5[4],inst(R5[4],Q[4])))==0,
   'H37 repeated endpoint outcome reset 0')
ck(eq(sum((inst(K,Q[4]) for K in L5),s.zeros(n)),Q[4]),
   'H37 Luders nonselective preserves endpoint')
ck(eq(sum((inst(K,Q[4]) for K in R5),s.zeros(n)),Q[0]),
   'H37 reset nonselective prepares origin')
def range_chain(kraus_by_outcome,d,depth):
    algebra=[s.eye(d)]
    dims=[rank(algebra)]
    for k in range(depth):
        additions=[dual(K,v) for v in algebra for K in kraus_by_outcome]
        combined=algebra+additions
        basis=[]
        for v in combined:
            if rank(basis+[v])>rank(basis):basis.append(v)
        algebra=basis
        dims.append(rank(algebra))
    return dims,algebra
for label,kas in [('Z Luders',[[p0],[p1]]),('Z reset',[[p0],[E(2,0,1)]])]:
    dims,obs=range_chain(kas,2,4)
    ck(dims==[1,2,2,2,2],f'{label} sequential-effect span D2 only')
    ck(rank(obs)==2,f'{label} sequential effects not IC')
    ck(rank(obs+[X])==3,f'{label} X inaccessible from any repeated Z-word')
for label,kas in [('IC Luders',Ls),('IC reset',Rs)]:
    dims,obs=range_chain(kas,2,3)
    ck(dims==[1,4,4,4],f'{label} IC effects full rank from length1')
    ck(rank(obs)==4,f'{label} all initial states operationally separated')
ck(not eq(matmap(Ls[5],2),matmap(Rs[5],2)),
   'IC same input-state access does not identify instrument')
states=[p0,p1,(i2+X)/2,(i2+Y)/2]
readouts=states
ck(rank(states)==4,'qubit input preparation space spans M2')
ck(rank(readouts)==4,'qubit readout effects span M2')
V=s.Matrix.hstack(*(vec(z) for z in states))
W=s.Matrix.vstack(*[vec(z.T).T for z in readouts])
ck(V.rank()==4,'preparation matrix invertible')
ck(W.rank()==4,'readout matrix invertible')
ck((s.kronecker_product(V.T,W)).rank()==16,
   'instrument response tomography linear rank16')
for lbl,K,J in [('IC Zminus',Ls[5],Rs[5]),('coarse coin0',IA[0],IB[0])]:
    D=matmap(K,2)-matmap(J,2)
    ck(not eq(D,s.zeros(4)),f'{lbl} selective map difference')
    ck(not eq(W*D*V,s.zeros(4)),f'{lbl} tomographically detectable')
out={'study':'P11-AX06','all_passed':True,'exact_assertions_passed':len(checks),'checks':checks,
     'six_outcome_IC_POVM_effect_rank':rank(Es),
     'same_POVM_different_Luders_reset_instruments':True,
     'same_POVM_and_same_nonselective_channel_different_instruments':True,
     'qubit_Z_sequential_effect_ranks':[1,2,2,2,2],
     'qubit_IC_sequential_effect_ranks':[1,4,4,4],
     'H37_population_effect_rank':5,
     'H37_two_step_repeated_endpoint_Luders_probability':'1',
     'H37_two_step_repeated_endpoint_reset_probability':'0',
     'full_qubit_instrument_tomography_linear_rank':16,
     'abstract_ancilla_dilation_exists':True,
     'independently_calibrated_device_instrument':'OPEN',
     'F_derived_physical_observer_source':'OPEN',
     'P6_physical_gate':'OPEN','P11_generative_completeness':'OPEN'}
Path(__file__).with_name('P11_AX06_exact_results.json').write_text(
    json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(f'PASS: P11–AX06 {len(checks)}/{len(checks)} exact assertions')
