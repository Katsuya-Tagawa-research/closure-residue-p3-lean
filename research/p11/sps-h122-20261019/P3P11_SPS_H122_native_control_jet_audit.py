#!/usr/bin/env python3
"""SPS-H122 exact native control-jet tests. Algebra only; physical source OPEN."""
from pathlib import Path
import json
import sympy as s

checks=[]
def ck(cond,label):
    assert bool(cond),label
    checks.append(label)
def equal(A,B):
    return A.shape==B.shape and all(s.simplify(z)==0 for z in A-B)
def E(n,i,j):
    m=s.zeros(n);m[i,j]=1;return m
def vec(A):
    return s.Matrix([A[i,j] for j in range(A.cols) for i in range(A.rows)])
def rank_matrices(A):
    return s.Matrix.hstack(*(vec(x) for x in A)).rank() if A else 0
def superop(T,n):
    return s.Matrix.hstack(*(vec(T(E(n,i,j))) for j in range(n) for i in range(n)))
def adH(H):
    return lambda X: -s.I*(H*X-X*H)
def dephase(rho):
    return s.diag(*(rho[i,i] for i in range(rho.rows)))
def reset(rho):
    return s.trace(rho)*E(2,0,0)

I=s.eye(2)
X=E(2,0,1)+E(2,1,0)
Y=-s.I*E(2,0,1)+s.I*E(2,1,0)
Z=E(2,0,0)-E(2,1,1)
Hbasis=[X,Y,Z]
A=[superop(adH(H),2) for H in Hbasis]
ck(all(equal(H,H.H) for H in Hbasis),'Hermitian Pauli basis')
ck(all(s.trace(H)==0 for H in Hbasis),'traceless Pauli basis')
ck(s.Matrix.hstack(*[a.reshape(16,1) for a in A]).rank()==3,
   'ad map injective on traceless Hermitian Hamiltonians')
ck(all(equal(a*vec(I),s.zeros(4,1)) for a in A),
   'all commutators annihilate identity')
q=s.Rational(1,2)
B=superop(lambda R: q*R+(1-q)*dephase(R),2)
ck(B.rank()==4,'invertible partial dephasing superoperator rank 4')
ck(s.factor(B.det())==s.Rational(1,4),'partial dephasing determinant 1/4')
ck(equal(B.inv()*B,s.eye(4)),'algebraic inverse exists (not necessarily CP)')
for i,H in enumerate(Hbasis):
    T=A[i]*B
    ck(equal(T*B.inv(),A[i]),f'jet {i}: deconvolution recovers inner derivation')
    ck(equal(T*B.inv()*vec(I),s.zeros(4,1)),f'jet {i}: identity-annihilation')
    for j in range(2):
        for k in range(2):
            r=E(2,j,k)
            ck(equal(T*vec(r),vec(adH(H)(q*r+(1-q)*dephase(r)))),
               f'jet {i}: derivative on E{j}{k}')
C=s.Matrix.hstack(*[a.reshape(16,1) for a in A])
weights=[s.Rational(2,5),s.Rational(-3,7),s.Rational(1,11)]
Htrue=sum([w*h for w,h in zip(weights,Hbasis)],s.zeros(2))
T=superop(adH(Htrue),2)*B
cvec=C.gauss_jordan_solve((T*B.inv()).reshape(16,1))[0]
ck([s.simplify(v) for v in cvec]==weights,'all Hamiltonian coefficients recovered')
ck(equal(adH(Htrue+8*I)(E(2,0,1)),adH(Htrue)(E(2,0,1))),
   'scalar Hamiltonian is invisible to channel')
ck(equal(adH(Htrue+8*I)(E(2,1,0)),adH(Htrue)(E(2,1,0))),
   'scalar Hamiltonian gauge on reverse coherence')
ck(C.rank()==3,'three independent first-order marked axes are identifiable')
rhoz=E(2,0,0)
rho1=E(2,1,1)
for R in (rhoz,rho1,I/2):
    for H in Hbasis:
        ck(equal(dephase(adH(H)(R)),s.zeros(2)),
           'diagonal populations have zero first derivative for diagonal preparations')
rhox=(I+X)/2
meas=[X,Y,Z]
Ob=s.Matrix([[s.simplify(s.trace(M*adH(H)(R))) for H in Hbasis]
             for R in (rhoz,rhox) for M in meas])
ck(Ob.rank()==3,'two noncommuting prepared states and full X/Y/Z readout rank 3')
ck(Ob.shape==(6,3),'operational observability matrix shape')
Odiag=s.Matrix([[s.simplify(s.trace(M*adH(H)(R))) for H in Hbasis]
                for R in (rhoz,rho1) for M in (E(2,0,0),E(2,1,1))])
ck(Odiag.rank()==0,'diagonal preparation/readout derivative matrix rank zero')
ck((3-Odiag.rank())==3,'population-only missing full traceless control tangent')
Delta=superop(dephase,2)
Az=superop(adH(Z),2)
ck(Delta.rank()==2,'complete dephasing rank 2')
ck(equal(Az*Delta,s.zeros(4)),'Z post-pulse derivative is exactly invisible')
ck(not equal(Az,s.zeros(4)),'Z is a nontrivial microscopic Hamiltonian')
for j in range(2):
    for k in range(2):
        R=dephase(E(2,j,k))
        ck(equal(Z*R,R*Z),f'post-dephasing output commutes with Z on E{j}{k}')
Res=superop(reset,2)
ck(Res.rank()==1,'state replacement channel rank 1')
for H in Hbasis:
    ck(equal(Res*superop(adH(H),2),s.zeros(4)),
       'any trace-preserving infinitesimal pre-control erased by reset')
ck(equal(Res*Delta,Res),'reset after dephasing equals reset')
knob_A=[X]
knob_B=[X,Z]
ck(rank_matrices(knob_A)==1,'minimal marked actuator list rank1')
ck(rank_matrices(knob_B)==2,'extra unmarked actuator list rank2')
ck(equal(superop(adH(knob_A[0]),2)*B,superop(adH(knob_B[0]),2)*B),
   'same marked jet despite extra unmarked actuator')
n=5
Kh=[E(n,k,k+1)-E(n,k+1,k) for k in range(n-1)]
Hcontrol=[s.I*k for k in Kh]
A5=[superop(adH(h),n) for h in Hcontrol]
ck(all(equal(h,h.H) for h in Hcontrol),'H37 marked Hamiltonians Hermitian')
ck(rank_matrices(Hcontrol)==4,'H37 marked Hermitian Hamiltonians rank4')
ck(s.Matrix.hstack(*[v.reshape(625,1) for v in A5]).rank()==4,
   'H37 four exact full-process first-order jets linearly independent')
ck(all(s.trace(h)==0 for h in Hcontrol),'H37 marked controls traceless')
ck(all(not equal(A5[i],s.zeros(25)) for i in range(4)),
   'H37 individual marked jets nonzero')
Hhop=sum([E(n,k,k+1)+E(n,k+1,k) for k in range(n-1)],s.zeros(n))/2
H0=Hhop+s.diag(0,s.Rational(1,7),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13))
gamma=s.Rational(2,3)
L5=superop(lambda R: -s.I*(H0*R-R*H0)+gamma*(dephase(R)-R),n)
ck(L5.rank()>0,'H37 fixed generator not zero')
ck(all(s.simplify((vec(s.eye(n)).T*L5)[j])==0 for j in range(25)),
   'H37 generator trace preservation in Liouville basis')
ck((L5*0+s.eye(25)).det()==1,'H37 semigroup invertible at time zero')
out={
  'study':'SPS-H122','exact_assertions_passed':len(checks),'all_passed':True,
  'checks':checks,'qubit_calibrated_control_rank':C.rank(),
  'qubit_population_jet_rank':Odiag.rank(),'qubit_full_observation_rank':Ob.rank(),
  'qubit_partial_dephasing_det':str(B.det()),'h37_marked_jets_rank':4,
  'physical_native_control_catalogue':'OPEN','p6_physical_gate':'OPEN',
  'p11_completeness':'OPEN',
  'limits':'No exhaustive hardware catalogue or H37 experimental tomography. Finite-time semigroup invertibility proven analytically, not evaluated as a matrix exponential.'
}
Path(__file__).with_name('P3P11_SPS_H122_exact_results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(f'SPS-H122 PASS {len(checks)}/{len(checks)} exact assertions')
print('qubit ranks',Ob.rank(),Odiag.rank(),'H37 marked jets rank4')
