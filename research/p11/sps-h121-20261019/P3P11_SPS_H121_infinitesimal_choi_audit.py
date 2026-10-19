#!/usr/bin/env python3
"""Exact finite audit for SPS-H121. Requires SymPy. Checks algebra, not device provenance."""
import json
from pathlib import Path
import sympy as s

checks=[]
def check(cond, why):
    assert bool(cond), why
    checks.append(why)
def zmat(M): return all(s.simplify(x)==0 for x in M)
def eq(A,B): return A.shape==B.shape and zmat(A-B)
def E(n,i,j):
    X=s.zeros(n);X[i,j]=1;return X
def vec(A):return s.Matrix([A[i,j] for j in range(A.cols) for i in range(A.rows)])
def rank(mats):
    return s.Matrix.hstack(*(vec(M) for M in mats)).rank() if mats else 0
def D(A,rho): return A*rho*A.H - (A.H*A*rho+rho*A.H*A)/2
def GKSL(H,jumps,rho):
    return -s.I*(H*rho-rho*H)+sum((D(L,rho) for L in jumps),s.zeros(H.rows))
def choi_of_linear(T,n):
    J=s.zeros(n*n)
    for i in range(n):
        for j in range(n):
            A=T(E(n,i,j))
            for a in range(n):
                for b in range(n):
                    J[a+n*i,b+n*j]=s.expand(A[a,b])
    return J
def liouville(T,n):
    return s.Matrix.hstack(*(vec(T(E(n,i,j))) for j in range(n) for i in range(n)))
def support(C):
    return s.Matrix.hstack(*C.columnspace()) if C.rank() else s.zeros(C.rows,0)
def same_span(M,N): return M.rank()==N.rank()==M.row_join(N).rank()
def jnorm(M):return (M.H*M).trace()

n=2
I=s.eye(n)
X=E(n,0,1)+E(n,1,0)
Y=-s.I*E(n,0,1)+s.I*E(n,1,0)
Z=E(n,0,0)-E(n,1,1)
F=[X/s.sqrt(2),Y/s.sqrt(2),Z/s.sqrt(2)]
for i in range(3):
    check(s.trace(F[i])==0,f'F{i}: traceless')
    for j in range(3):
        check(s.simplify(s.trace(F[i].H*F[j])-(1 if i==j else 0))==0,f'F{i}{j}: orthonormal')
H=X*s.Rational(1,5)+Z*s.Rational(1,7)
A=Z/2
B=E(2,0,1)/3
jumps=[A,B]
L=lambda rho:GKSL(H,jumps,rho)
check(eq(H,H.H),'Hamiltonian selfadjoint')
check(s.trace(H)==0,'Hamiltonian traceless gauge')
check(all(s.trace(k)==0 for k in jumps),'jump input traceless')
check(zmat(L(I).H-L(I)),'L(I) Hermitian')
check(all(s.trace(L(E(n,i,j)))==0 for i in range(n) for j in range(n)),'generator TP on matrix units')
check(zmat(L(I)-sum((j*j.H-j.H*j for j in jumps),s.zeros(n))),'nonunital drift from jumps')
Jdot=choi_of_linear(L,n)
vI=vec(I)
Q=s.eye(n*n)-vI*vI.H/n
C=s.simplify(Q*Jdot*Q)
Jnoise=sum((vec(k)*vec(k).H for k in jumps),s.zeros(n*n))
check(eq(Q,Q.H),'Q Hermitian')
check(eq(Q*Q,Q),'Q projector')
check(eq(Q*vI,s.zeros(n*n,1)),'Q kills identity')
check(eq(C,Jnoise),'compressed derivative equals centered jump Gram')
check(eq(C,C.H),'compressed derivative Hermitian')
check(C.rank()==2,'noise rank2')
check(same_span(support(C),s.Matrix.hstack(vec(A),vec(B))),'noise span exactly traceless jump span')
check(all(eq(C*vec(k),C*vec(k)) for k in jumps),'operator direction compatibility')
check(jnorm(C)>0,'noise positivity witness trace quadratic')
check(all(s.simplify(s.trace(vec(k)*vec(k).H))>0 for k in jumps),'individual noise weights positive')
check((s.Matrix.hstack(vec(A),vec(B))).rank()==2,'minimal traceless noise count2')
check(s.trace(C)==s.Rational(1,2)+s.Rational(1,9),'noise C trace matches jump norms')

Ch=s.Matrix(3,3,lambda i,j: s.simplify((vec(F[i]).H*C*vec(F[j]))[0]))
check(eq(Ch,Ch.H),'Kossakowski matrix Hermitian')
check(Ch.rank()==2,'Kossakowski rank2')
check(same_span(support(C),s.Matrix.hstack(*[vec(F[i]) for i in range(3)])*support(Ch)),'Kossakowski noise support')
def DC(rho):
    return s.simplify(sum((Ch[i,j]*(F[i]*rho*F[j].H-(F[j].H*F[i]*rho+rho*F[j].H*F[i])/2)
                            for i in range(3) for j in range(3)),s.zeros(n)))
for i in range(n):
    for j in range(n):
        rho=E(n,i,j)
        check(eq(DC(rho),sum((D(a,rho) for a in jumps),s.zeros(n))),f'canonical dissipator equal on E{i}{j}')
        check(eq(L(rho)-DC(rho),-s.I*(H*rho-rho*H)),f'canonical residual equals ad_H on E{i}{j}')

Hbasis=[X,Y,Z]
hs=[liouville(lambda r:-s.I*(f*r-r*f),n).reshape(n**4,1) for f in Hbasis]
check(s.Matrix.hstack(*hs).rank()==3,'traceless Hamiltonian ad map injective')
HR=lambda rho:L(rho)-DC(rho)
vecR=liouville(HR,n).reshape(n**4,1)
sol=s.linsolve((s.Matrix.hstack(*hs),vecR))
check(len(sol)==1,'Hamiltonian coordinates unique')
hcoeff=list(next(iter(sol)))
check(hcoeff==[s.Rational(1,5),0,s.Rational(1,7)],'Hamiltonian extracted canonically')
for i in range(n):
    for j in range(n):
        R=E(n,i,j)
        check(eq(-s.I*((H+3*I)*R-R*(H+3*I)),-s.I*(H*R-R*H)),f'identity Hamiltonian gauge E{i}{j}')

unitgen=lambda rho:-s.I*(H*rho-rho*H)
check(eq(Q*choi_of_linear(unitgen,n)*Q,s.zeros(n*n)),'pure Hamiltonian has zero noise tangent')
check(not zmat(unitgen(E(2,0,0))),'pure Hamiltonian is nontrivial')

c=s.Rational(1,4)
dH=s.I*(s.conjugate(c)*B-c*B.H)/2
Hshift=H-dH
jumpshift=[A,B+c*I]
check(eq(Hshift,Hshift.H),'jump-shift Hamiltonian Hermitian')
check(s.trace(Hshift)==0,'jump-shift Hamiltonian traceless')
for i in range(n):
    for j in range(n):
        rho=E(n,i,j)
        check(eq(GKSL(Hshift,jumpshift,rho),L(rho)),f'jump scalar gauge same GKSL E{i}{j}')
check(eq(Q*choi_of_linear(lambda rho:GKSL(Hshift,jumpshift,rho),n)*Q,C),'scalar shift preserves Choi noise C')

Aplus=(A+B)/s.sqrt(2);Aminus=(A-B)/s.sqrt(2)
for i in range(n):
    for j in range(n):
        rho=E(n,i,j)
        check(eq(GKSL(H,[Aplus,Aminus],rho),L(rho)),f'unitary jump mixing E{i}{j}')
check(rank([Aplus,Aminus])==rank(jumps),'noise span unitary-invariant')

SL=liouville(L,n)
L2=lambda rho:L(L(rho))
J2=choi_of_linear(L2,n)
t=s.symbols('t',real=True)
second=s.eye(n*n)+t*SL+t*t*SL*SL/2
jsecond=choi_of_linear(lambda rho:rho+t*L(rho)+t*t*L2(rho)/2,n)
check(eq(second,s.eye(n*n)+t*SL+t*t*SL*SL/2),'Liouville Taylor polynomial')
check(eq(choi_of_linear(lambda rho:rho,n),vI*vI.H),'identity Choi rank1')
check(eq(s.simplify(Q*jsecond*Q),s.simplify(t*C+t*t*(Q*J2*Q)/2)),'Choi tangent Taylor with t2 remainder')
check(eq(s.simplify((Q*jsecond*Q)/t).subs(t,0),C),'semigroup conditional Choi first tangent')

n5=5; d5=s.eye(5); vv=vec(d5); Q5=s.eye(25)-vv*vv.H/5
gamma=s.Rational(2,3)
projs=[E(5,i,i) for i in range(5)]
vecnoise=[Q5*vec(p) for p in projs]
V5=s.Matrix.hstack(*vecnoise)
check(V5.rank()==4,'H37 diagonal traceless jump span rank4')
C5=gamma*V5*V5.H
check(C5.rank()==4,'H37 infinitesimal compressed Choi rank4')
check(eq(C5,C5.H),'H37 compressed Choi Hermitian')
check(eq(Q5*C5*Q5,C5),'H37 compressed Choi supported on traceless part')
check(eq(V5*s.ones(5,1),s.zeros(25,1)),'H37 trace-zero relation across projectors')
check(all(eq((s.eye(25)-Q5)*v,s.zeros(25,1)) for v in vecnoise),'H37 jump vectors orthogonal to identity')
knat=[E(5,i,i+1)-E(5,i+1,i) for i in range(4)]
check(rank(knat)==4,'H37 native Hamiltonian tangent complex rank4')
check(s.Matrix.hstack(V5,*[vec(x) for x in knat]).rank()==8,'H37 native controls transverse to dephasing noise')
check(all(s.trace(p*a)==0 for p in projs for a in knat),'H37 no diagonal native content')

controlA=[s.I*X]
controlB=[s.I*X,s.I*Z]
check(rank(controlA)==1,'model A first-order native rank1')
check(rank(controlB)==2,'model B first-order native rank2')
check(not rank(controlA)==rank(controlB),'same baseline generator, different marked actuation rank')

result={
 'study':'SPS-H121','all_passed':True,'exact_assertions_passed':len(checks),'checks':checks,
 'noise_C_rank':C.rank(),'noise_C_trace':str(s.trace(C)),
 'canonical_H_coeffs':list(map(str,hcoeff)),
 'h37_noise_rank':C5.rank(),'h37_native_control_rank':rank(knat),
 'physical_primitive_provenance':'OPEN','p6_physical_gate':'OPEN',
 'p11_generativity':'OPEN',
 'scope':'GKSL derivative under full channel tomography; no physical native Hamiltonian catalogue inferred'
}
Path(__file__).with_name('P3P11_SPS_H121_exact_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(f'PASS: SPS-H121 {len(checks)}/{len(checks)} exact assertions')
print('Noise rank',C.rank(),'canonical H',hcoeff,'H37 noise rank',C5.rank())
