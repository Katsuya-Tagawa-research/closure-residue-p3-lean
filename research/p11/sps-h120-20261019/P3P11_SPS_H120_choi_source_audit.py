#!/usr/bin/env python3
"""SPS-H120 exact Choi-space / physical-primitive gap audit; finite, not a device test."""
import sympy as s, json
from pathlib import Path
checks=[]
def check(x,description):
    assert bool(x),description
    checks.append(description)
def zero(M):return all(s.simplify(x)==0 for x in M)
def eq(A,B):return A.shape==B.shape and zero(A-B)
def E(n,i,j):
    a=s.zeros(n);a[i,j]=1;return a
def vec(A):return s.Matrix([A[i,j] for j in range(A.cols) for i in range(A.rows)])
def sr(K):return s.Matrix.hstack(*[vec(x) for x in K]).rank() if K else 0
def same(A,B):return sr(A)==sr(B)==sr(A+B)
def choi(K):
    return sum((vec(x)*vec(x).H for x in K),s.zeros(K[0].rows*K[0].cols))
def apply(K,X):
    return sum((a*X*a.H for a in K),s.zeros(K[0].rows))
def cl(K):
    n=K[0].rows
    return [E(n,i,j) for i in range(n) for j in range(n)
            if any(s.simplify(a[i,j])!=0 or s.simplify(a[j,i])!=0 for a in K)]
def ptB(A):
    return s.Matrix(2,2,lambda i,j:sum(A[2*i+k,2*j+k] for k in range(2)))
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1)
p0=E(2,0,0);p1=E(2,1,1);q=s.Rational(1,3)
D=[s.sqrt(q)*I,s.sqrt(1-q)*p0,s.sqrt(1-q)*p1]
check(eq(sum((k.H*k for k in D),s.zeros(2)),I),'dephasing TP')
check(sr(D)==2,'dephasing Kraus span')
check(choi(D).rank()==2,'dephasing Choi rank')
R=[(D[0]+D[1])/s.sqrt(2),(D[0]-D[1])/s.sqrt(2),D[2]]
check(same(R,D),'Kraus mixing span')
check(eq(choi(R),choi(D)),'Kraus mixing Choi')
check(all(eq(apply(D,E(2,i,j)),apply(R,E(2,i,j))) for i in range(2) for j in range(2)),'Kraus mixing channel')
Dq=[s.sqrt(s.Rational(1,2))*I,s.sqrt(s.Rational(1,2))*p0,s.sqrt(s.Rational(1,2))*p1]
check(same(D,Dq),'different strengths same Kraus span')
check(not eq(apply(D,E(2,0,1)),apply(Dq,E(2,0,1))),'channel weights not encoded')
check(eq(apply(D,E(2,0,1)),q*E(2,0,1)),'dephasing offdiag')
A=[s.diag(1,s.sqrt(3)/2),s.Matrix([[0,s.Rational(1,2)],[0,0]])]
check(eq(sum((k.H*k for k in A),s.zeros(2)),I),'amplitude damping TP')
C=[k*b for k in D for b in A]
check(eq(choi(C),choi([k*b for k in D for b in A])),'product Choi')
check(all(eq(apply(C,E(2,i,j)),apply(D,apply(A,E(2,i,j)))) for i in range(2) for j in range(2)),'composed channel')
check(same(C,[k*b for k in D for b in A]),'composed source span')
check(eq(sum((k.H*k for k in C),s.zeros(2)),I),'composed TP')
T=[s.kronecker_product(k,b) for k in D for b in A]
check(sr(T)==sr(D)*sr(A),'tensor source rank')
check(eq(sum((k.H*k for k in T),s.zeros(4)),s.eye(4)),'tensor TP')
check(choi(T).rank()==sr(T),'tensor Choi rank')
check(sr([I])==1,'identity Kraus rank')
check(eq(choi([I]),vec(I)*vec(I).H),'identity Choi')
for label,K in [('dephase',D),('amplitude',A),('composition',C),('tensor',T)]:
    B=s.Matrix.hstack(*[vec(k) for k in K]); J=choi(K)
    check(J.rank()==B.rank(),label+' rank equality')
    check(B.row_join(J).rank()==B.rank(),label+' Choi range equality')
Jdirect=s.Matrix(4,4,lambda a,b:apply(D,apply(A,E(2,a//2,b//2)))[a%2,b%2])
check(eq(Jdirect,choi(C)),'process-action Choi agreement')
U=s.diag(s.I,-1);Dt=[U*k*U.H for k in D]
check(same(Dt,[U*k*U.H for k in D]),'unitary Kraus-space covariance')
check(all(eq(apply(Dt,U*E(2,i,j)*U.H),U*apply(D,E(2,i,j))*U.H)
          for i in range(2) for j in range(2)),'unitary channel covariance')
HZ=s.kronecker_product(X,Z);HX=s.kronecker_product(X,X)
c=s.Rational(3,5);h=s.Rational(4,5);Kred=[c*I,h*X]
for label,H in [('XZ',HZ),('XX',HX)]:
    V=c*s.eye(4)-s.I*h*H
    check(eq(V.H*V,s.eye(4)),label+' joint U')
    check(all(eq(ptB(V*s.kronecker_product(E(2,i,j),I/2)*V.H),apply(Kred,E(2,i,j)))
              for i in range(2) for j in range(2)),label+' reduced channel on all units')
Br=s.Matrix.hstack(*[vec(k) for k in Kred])
check(Br.row_join(choi(Kred)).rank()==Br.rank(),'H119 reduced Choi range')
check(choi(Kred).rank()==2,'H119 reduced Choi rank')
check(sr(Kred)==2,'H119 reduced Kraus span rank')
check(not same([c*s.eye(4)-s.I*h*HZ],[c*s.eye(4)-s.I*h*HX]),'joint Kraus lines distinct')
check(not same(cl([HZ]),cl([HX])),'joint static support sectors distinct')
H=E(3,0,1)+E(3,1,0)+E(3,1,2)+E(3,2,1)
V=s.eye(3)-s.I*(2*s.sqrt(2)/5)*H-s.Rational(1,5)*H*H
check(eq(H**3,2*H),'path cubic relation')
check(eq(V.H*V,s.eye(3)),'path U unitary')
check(H[0,2]==0 and H[2,0]==0,'path generator local')
check(V[0,2]==-s.Rational(1,5),'nonlocal finite-time amplitude')
check(all(s.simplify(V[i,j])!=0 for i in range(3) for j in range(3)),'all 9 finite-time entries')
check(sr(cl([H]))==4,'generator bimodule 4')
check(sr(cl([V]))==9,'finite-time channel bimodule 9')
check(choi([V]).rank()==1,'finite-time channel Choi rank1')
check(sr([V])==1,'finite-time Kraus line')
check(not same([H],[V]),'generator vs time channel')
check(same([I],[3*I]),'identity Kraus line scalar invariant')
check(not same([I],[X]),'native control not present in identity')
result=dict(label='SPS-H120',exact_checks=len(checks),all_passed=True,checks=checks,
            dephase_intrinsic_dim=sr(D),reduced_H119_intrinsic_dim=sr(Kred),
            path_generator_bimodule_dim=sr(cl([H])),
            path_finite_time_channel_bimodule_dim=sr(cl([V])),
            path_finite_time_02_amplitude=str(V[0,2]),
            physical_primitive_provenance='OPEN')
Path(__file__).with_name('P3P11_SPS_H120_exact_results.json').write_text(
    json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(f'PASS: SPS-H120 {len(checks)}/{len(checks)} exact checks')
