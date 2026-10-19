#!/usr/bin/env python3
"""P11 AX02: exact finite CP-projection / observable algebra / quadratic residue audit."""
import sympy as sp
import json
from pathlib import Path
checks=[]
def ck(cond, desc):
    assert bool(cond),desc
    checks.append(desc)
def E(n,i,j):
    m=sp.zeros(n);m[i,j]=1;return m
def iszero(A): return all(sp.simplify(z)==0 for z in A)
def eq(A,B): return A.shape==B.shape and iszero(A-B)
def vec(A):return sp.Matrix([A[i,j] for j in range(A.cols) for i in range(A.rows)])
def linear_matrix(T,n):return sp.Matrix.hstack(*(vec(T(E(n,i,j))) for j in range(n) for i in range(n)))
def kraus_heis(X,K):return sum((a.H*X*a for a in K),sp.zeros(X.rows))
def choi_sch(K):return sum((vec(k)*vec(k).H for k in K),sp.zeros(K[0].rows**2))
p0,p1=E(2,0,0),E(2,1,1)
z,w=E(2,0,1),E(2,1,0)
def Delta(X):return p0*X*p0+p1*X*p1
for i in range(2):
    for j in range(2):
        x=E(2,i,j)
        ck(eq(Delta(Delta(x)),Delta(x)),f'Delta idempotent E{i}{j}')
ck(eq(Delta(sp.eye(2)),sp.eye(2)),'Delta unital')
ck(eq(Delta(z),sp.zeros(2)),'E01 hidden')
ck(eq(Delta(w),sp.zeros(2)),'E10 hidden')
ck(eq(Delta(z*w),p0),'hidden product visible p0')
ck(eq(Delta(w*z),p1),'reverse hidden product visible p1')
ck(eq(Delta(z*w-w*z),p0-p1),'diagonal commutator return')
ck(not eq(Delta(z*w),Delta(z)*Delta(w)),'projection not multiplicative')
ck(eq(Delta(z.H*z),p1),'faithful diagonal covariance on E01')
ck(eq(Delta(w.H*w),p0),'faithful diagonal covariance on E10')
ck(eq(Delta(z.H*z)-Delta(z.H)*Delta(z),p1),'Kadison-Schwarz gap on E01')
ck(eq(Delta(w.H*w)-Delta(w.H)*Delta(w),p0),'Kadison-Schwarz gap on E10')
ck(not eq(Delta(z*w),sp.zeros(2)),'hidden cannot form two-sided ideal')
q0,q1,q2=(E(3,i,i) for i in range(3))
K0=q0+q1;K1=E(3,0,2)/sp.sqrt(2);K2=E(3,1,2)/sp.sqrt(2);K=[K0,K1,K2]
def P(X):return kraus_heis(X,K)
def embed(A):
    B=sp.zeros(3)
    for i in range(2):
        for j in range(2):B[i,j]=A[i,j]
    B[2,2]=sp.trace(A)/2
    return B
def compress(X):return X[:2,:2]
for k,X in enumerate(K):ck(X.shape==(3,3),f'Kraus shape{k}')
ck(eq(sum((a.H*a for a in K),sp.zeros(3)),sp.eye(3)),'P UCP explicit Kraus unital')
ck(choi_sch(K).rank()==3,'P Kraus Gram rank3')
for i in range(3):
    for j in range(3):
        m=E(3,i,j)
        ck(eq(P(m),embed(compress(m))),f'P matches embed∘compress E{i}{j}')
        ck(eq(P(P(m)),P(m)),f'P idempotent E{i}{j}')
ck(eq(P(sp.eye(3)),sp.eye(3)),'P unital')
U=[E(2,i,j) for i in range(2) for j in range(2)]
R=[embed(A) for A in U]
ck(sp.Matrix.hstack(*(vec(v) for v in R)).rank()==4,'P range dimension4')
ck(all(eq(P(r),r) for r in R),'all range generators fixed')
ck(eq(R[0]+R[3],sp.eye(3)),'range contains identity')
ck(all(eq(embed(A).H,embed(A.H)) for A in U),'range star closed')
ck(not eq(R[0]*R[0],R[0]),'range not ambient algebra')
ck(eq(P(R[0]*R[0]),R[0]),'CE e00 idempotence')
ck(eq(P((R[0]-R[3])**2),sp.eye(3)),'CE Z square unit')
ck(not eq((R[0]-R[3])**2,sp.eye(3)),'ambient Z square not unit')
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                a,b=embed(E(2,i,j)),embed(E(2,k,l))
                target=embed(E(2,i,l) if j==k else sp.zeros(2))
                ck(eq(P(a*b),target),f'CE matrix unit {i}{j}·{k}{l}')
for i in range(4):
    for j in range(4):
        for k in range(4):
            a,b,c=R[i],R[j],R[k]
            ck(eq(P(P(a*b)*c),P(a*P(b*c))),f'CE associativity {i}{j}{k}')
ck(eq(P(R[1]*R[2]),R[0]),'CE E01 E10 returns matrix unit')
ck(eq(P(R[2]*R[1]),R[3]),'CE E10 E01 returns matrix unit')
ck(eq(P(R[1]*R[2]-R[2]*R[1]),R[0]-R[3]),'CE commutator preserves noncommutativity')
ck(eq(P(sp.eye(3)*R[1]),R[1]),'CE left unit')
ck(eq(P(R[1]*sp.eye(3)),R[1]),'CE right unit')
xa=E(3,0,2);xb=E(3,2,0);xc=q2
for m,lbl in [(xa,'02'),(xb,'20'),(xc,'22')]:
    ck(eq(P(m),sp.zeros(3)),f'P-hidden {lbl}')
ck(eq(P(xa.H*xa),sp.zeros(3)),'nonfaithful zero hidden ordered-square return')
ck(eq(P(xb.H*xb),R[0]),'another hidden ordered-square returns R00')
ck(eq(P(xa*xa.H),R[0]),'hidden reversed square returns R00')
ck(eq(P(xa*xb-xb*xa),R[0]),'hidden commutator returns R00')
ck(eq(P(xc.H*xc),sp.zeros(3)),'nonfaithful invisible bottom projection')
ck(eq(P(xa)*P(xb),sp.zeros(3)),'hidden images product zero')
ck(not eq(P(xa*xb),sp.zeros(3)),'ker P not two-sided ideal')
swap=E(2,0,1)+E(2,1,0)
K0swap=embed(swap);Kt=[K0swap,K1,K2]
def T(X):return kraus_heis(X,Kt)
ck(eq(sum((k.H*k for k in Kt),sp.zeros(3)),sp.eye(3)),'T unital CP Kraus witness')
for i in range(3):
    for j in range(3):
        m=E(3,i,j)
        ck(eq(T(m),embed(swap*compress(m)*swap)),f'T lifted CP dynamics E{i}{j}')
        ck(eq(P(T(m)),T(m)),f'P T = T E{i}{j}')
        ck(eq(T(P(m)),T(m)),f'T P = T E{i}{j}')
ck(eq(T(sp.eye(3)),sp.eye(3)),'T unital')
for i in range(4):
    for j in range(4):
        ck(eq(T(P(R[i]*R[j])),P(T(R[i])*T(R[j]))),f'T preserves CE product {i}{j}')
ck(eq(T(R[0]),R[3]),'visible CE dynamics swaps e00 e11')
ck(eq(T(R[1]),R[2]),'visible CE dynamics swaps e01 e10')
ck(linear_matrix(P,3).rank()==4,'CP idempotent superoperator rank4')
ck((sp.eye(9)-linear_matrix(P,3)).rank()==5,'CP hidden linear kernel dimension5')
Q=sp.Matrix([[1,sp.Rational(1,2),sp.Rational(1,4)],
             [0,sp.Rational(1,2),sp.Rational(1,4)],
             [0,0,sp.Rational(1,2)]])
C=sp.Matrix([[1,1,0],[0,0,1]])
B=sp.Matrix([[1,sp.Rational(1,2)],[0,sp.Rational(1,2)]])
Hobs=lambda a,b:sp.diag(a,a,b)
for i in range(2):
    for j in range(2):
        ck(eq(Hobs(i,j)*Hobs(j,i),Hobs(i*j,j*i)),f'classical visible algebra product {i}{j}')
ck(eq(C*Q,B*C),'AX01 classical Markov lumping')
ck(all(sum(Q[:,j])==1 for j in range(3)),'AX01 classical source stochastic TP')
visible_basis=[Hobs(1,0),Hobs(0,1)]
def dual_class(A):return sp.diag(*[sum(Q[i,j]*A[i,i] for i in range(3)) for j in range(3)])
for idx,a in enumerate(visible_basis):
    coef=sp.Matrix([a[0,0],a[2,2]])
    expected=Hobs(*(B.T*coef))
    ck(eq(dual_class(a),expected),f'AX01 invariant Heisenberg observable algebra {idx}')
    ck(eq(dual_class(a),Hobs(*(B.T*coef))),f'AX01 dual reduced CPTP {idx}')
N=sp.Matrix([1,-1,0]);section=sp.Matrix([[1,0],[0,0],[0,1]])
residue=Q*section-section*B
ck(eq(residue,N*sp.Matrix([[0,-sp.Rational(1,4)]])),'AX01 nonsplit hidden extension persists')
u,v=sp.symbols('u v')
res2=Q*(section+N*sp.Matrix([[u,v]]))-(section+N*sp.Matrix([[u,v]]))*B
ck(sp.simplify(res2[0,1]-res2[0,0])==-sp.Rational(1,4),'AX01 nonsplit obstruction independent of section')
out=dict(study='P11-AX02',all_passed=True,checks_passed=len(checks),checks=checks,
         dephasing_hidden_dim=2,ce_range_dimension=4,ce_kernel_dimension=5,
         ce_ambient_product_closed=False,ce_abstract_product='M2 (Choi-Effros)',
         ce_dynamics='UCP and CE star automorphism',ax01_extension_obstruction='-1/4',
         quadratic_return='nonzero in some hidden directions, zero in others',
         extra_cp_projection_independently_required=True,
         physical_primitive_provenance='OPEN',p11_generative_completeness='OPEN')
Path(__file__).with_name('P11_AX02_exact_results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(f'PASS: P11-AX02 {len(checks)}/{len(checks)} exact symbolic assertions')
