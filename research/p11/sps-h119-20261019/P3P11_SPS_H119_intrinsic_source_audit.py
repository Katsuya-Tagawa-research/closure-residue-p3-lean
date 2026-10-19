#!/usr/bin/env python3
"""SPS-H119 finite checks: restricted naturality and one-interval reduced-channel nonidentifiability."""
import json
from pathlib import Path
import sympy as s

checks=[]
def verify(cond,name):
    assert bool(cond),name
    checks.append(name)
def E(n,i,j):
    r=s.zeros(n);r[i,j]=1;return r
def rank_C(mats):
    if not mats:return 0
    n=mats[0].rows
    return s.Matrix.hstack(*[m.reshape(n*n,1) for m in mats]).rank()
def rank_R(mats):
    if not mats:return 0
    n=mats[0].rows
    cols=[]
    for M in mats:
        v=M.reshape(n*n,1)
        cols.extend([v.applyfunc(s.re),v.applyfunc(s.im)])
    return s.Matrix.hstack(*cols).rank()
def same_R(A,B):
    return rank_R(A)==rank_R(B)==rank_R(A+B)
def same_C(A,B):
    return rank_C(A)==rank_C(B)==rank_C(A+B)
def ptB(M,da=2,db=2):
    return s.Matrix(da,da,lambda i,j:sum(M[i*db+k,j*db+k] for k in range(db)))
def ptA(M,da=2,db=2):
    return s.Matrix(db,db,lambda i,j:sum(M[k*db+i,k*db+j] for k in range(da)))
def bimod(A):
    n=A.rows
    return [E(n,i,j) for i in range(n) for j in range(n)
            if A[i,j]!=0 or A[j,i]!=0]

n=5
edges=[(i,i+1) for i in range(4)]
K=[E(n,i,j)-E(n,j,i) for i,j in edges]
Q=[s.I*(E(n,i,j)+E(n,j,i)) for i,j in edges]
T0=K
T1=K+Q
verify(rank_R(T0)==4,"H37 native real rank4")
verify(rank_R(T1)==8,"H37 phase complete real rank8")
verify(all(z+z.H==s.zeros(n) for z in T1),"anti-Hermitian source vectors")
verify(not same_R(T0,T1),"two different source completions")
Hhop=sum([(E(n,i,j)+E(n,j,i))/2 for i,j in edges],s.zeros(n))
Jmix=[Hhop]+K
Jfull=[E(n,i,j) for i,j in edges]+[E(n,j,i) for i,j in edges]
verify(rank_C(Jmix)==5,"H37 mixed complex rank5")
verify(rank_C(Jfull)==8,"H37 full complex rank8")
verify(same_C(Jfull,K+Q),"completed complex edge sector")

U=s.diag(s.I,1,-1,s.I,1)
Kg=[U*k*U.H for k in K]
Qg=[]
for (i,j),g in zip(edges,Kg):
    pi,pj=E(n,i,i),E(n,j,j)
    Qg.append(s.I*(pi*g*pj-pj*g*pi))
verify(all(s.simplify(g-U*q*U.H)==s.zeros(n) for g,q in zip(Qg,Q)),
       "quadrature completion diagonal-gauge naturality")
verify(same_R(Kg,[U*z*U.H for z in T0]),"minimal gauge covariance")
verify(same_R(Kg+Qg,[U*z*U.H for z in T1]),"phase gauge covariance")

ind=[0,1,2]
K3=[E(3,i,i+1)-E(3,i+1,i) for i in range(2)]
Q3=[s.I*(E(3,i,i+1)+E(3,i+1,i)) for i in range(2)]
verify(same_R([z.extract(ind,ind) for z in T0],K3),"minimal corner naturality")
verify(same_R([z.extract(ind,ind) for z in T1],K3+Q3),"completed corner naturality")

order=[2,0,4,1,3]
P=s.zeros(n)
for old,new in enumerate(order):P[new,old]=1
verify(P*P.T==s.eye(n),"site permutation unitary")
Kp=[P*k*P.T for k in K]
Qp=[]
for (i,j),g in zip(edges,Kp):
    pi,pj=E(n,order[i],order[i]),E(n,order[j],order[j])
    Qp.append(s.I*(pi*g*pj-pj*g*pi))
verify(all(v==P*q*P.T for q,v in zip(Q,Qp)),"site relabelling naturality")

k2=E(2,0,1)-E(2,1,0)
q2=s.I*(E(2,0,1)+E(2,1,0))
embed=lambda x:s.diag(x,s.zeros(2))
embed2=lambda x:s.diag(s.zeros(5),x)
Ku=[embed(x) for x in K]+[embed2(k2)]
Qu=[embed(x) for x in Q]+[embed2(q2)]
verify(rank_R(Ku)==5,"disjoint sum native rank5")
verify(rank_R(Ku+Qu)==10,"disjoint sum quadrature rank10")
verify(same_R(Ku+Qu,[embed(x) for x in T1]+[embed2(k2),embed2(q2)]),
       "disjoint sum exact")

I=s.eye(2)
X=s.Matrix([[0,1],[1,0]])
Z=s.diag(1,-1)
HZ=s.kronecker_product(X,Z)
HX=s.kronecker_product(X,X)
verify(HZ.H==HZ and HX.H==HX,"Hermitian joint interactions")
verify(HZ*HZ==s.eye(4) and HX*HX==s.eye(4),"joint interactions involutions")
verify(s.trace(HZ)==s.trace(HX)==0,"joint traceless sources")
verify(ptA(HZ)==s.zeros(2) and ptA(HX)==s.zeros(2),
       "both A-operator marginals zero")
verify(ptB(HZ)==s.zeros(2) and ptB(HX)==s.zeros(2),
       "both B-operator marginals zero")
verify(rank_C(bimod(HZ))==4,"XZ bimodule rank4")
verify(rank_C(bimod(HX))==4,"XX bimodule rank4")
verify(rank_C(bimod(HZ)+bimod(HX))==8,"disjoint joint support")

c,h=s.symbols("c h",real=True)
a,b,d,e=s.symbols("a b d e")
rho=s.Matrix([[a,b],[d,e]])
joint=s.kronecker_product(rho,I/2)
target=c**2*rho+h**2*X*rho*X
for label,H in [("XZ",HZ),("XX",HX)]:
    Ut=c*s.eye(4)-s.I*h*H
    verify(s.simplify(ptB(Ut*joint*Ut.H)-target)==s.zeros(2),
           label+" equal one-interval A channel all t")
verify(HZ!=HX,"different joint Hamiltonians")
verify(all(HZ[i,j]*HX[i,j]==0 for i in range(4) for j in range(4)),
       "disjoint support pointwise")
verify(not same_C(bimod(HZ),bimod(HX)),
       "diagonal-gauge cannot identify sectors")
verify(same_C([ptB(HZ)],[ptB(HX)]),"joint source B marginals coincide")

out={
    "study":"SPS-H119",
    "checks_passed":len(checks),
    "all_passed":True,
    "checks":checks,
    "H37_native_real_dim":rank_R(T0),
    "H37_phase_real_dim":rank_R(T1),
    "Jmix_dim_C":rank_C(Jmix),
    "Jfull_dim_C":rank_C(Jfull),
    "joint_support_union_dim_C":rank_C(bimod(HZ)+bimod(HX)),
    "one_time_reduced_channel":"cos(t)^2*rho + sin(t)^2*X*rho*X for H=X⊗Z and H=X⊗X, initial B=I/2",
    "limits":"restricted source category; one-interval not arbitrary process tensor; no physical primitive provenance or P11 completeness"
}
Path(__file__).with_name("P3P11_SPS_H119_exact_results.json").write_text(
    json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"PASS: SPS-H119 {len(checks)}/{len(checks)} exact assertions")
