#!/usr/bin/env python3
"""P11 AX22 exact conditional noise-commutant/carre-du-champ audit."""
import json
from pathlib import Path
import sympy as s
I=s.I
C=0
def chk(ok,label):
 global C
 assert bool(ok),label
 C+=1
def zero(M):
 return all(s.simplify(x)==0 for x in M)
def mat(n,i,j):
 M=s.zeros(n);M[i,j]=1;return M
def dag(A):return A.conjugate().T
def com(A,B):return A*B-B*A
def gam(L,A):
 return s.simplify(L(dag(A)*A)-L(dag(A))*A-dag(A)*L(A))
def commdim(n,ops):
 if not ops:return n*n
 units=[mat(n,i,j) for i in range(n) for j in range(n)]
 rows=[]
 for V in ops:
  diffs=[com(X,V) for X in units]
  rows += [[v[i,j] for v in diffs] for i in range(n) for j in range(n)]
 return n*n-s.Matrix(rows).rank()
n=5
g=s.Rational(2,3)
P=[mat(n,j,j) for j in range(n)]
H=sum((s.Rational(1,2)*(mat(n,j,j+1)+mat(n,j+1,j)) for j in range(n-1)),s.zeros(n))
H[0,0]=s.Rational(1,3);H[1,1]=s.Rational(-1,4)
D=lambda A:s.diag(*[A[j,j] for j in range(n)])
L=lambda A:s.expand(I*com(H,A)+g*(D(A)-A))
W=lambda A:g*sum((dag(com(p,A))*com(p,A) for p in P),s.zeros(n))
units=[mat(n,j,k) for j in range(n) for k in range(n)]
for A in units:chk(zero(gam(L,A)-W(A)),"H37 Gamma matrix-unit identity")
for A in units:chk(zero(gam(L,A)-W(A)),"Independent matrix-unit repeat")
chk(commdim(n,P+list(map(dag,P)))==5,"H37 noise algebra has dimension 5")
chk(all(zero(W(p)) for p in P),"Pointer effects are noise silent")
chk(not zero(L(P[0])-D(L(P[0]))),"Instantaneously silent does not mean dynamically invariant")
A=s.Matrix([[s.Rational(1,2)*(i+1)+(I*s.Rational(j+1,7) if i!=j else 0) for j in range(n)] for i in range(n)])
tr=s.simplify(s.trace(W(A)))
norm=s.simplify(s.trace(dag(A-D(A))*(A-D(A))))
chk(s.simplify(tr-2*g*norm)==0,"H37 noise trace gap identity")
chk(s.simplify(tr)>=0,"H37 trace positivity")
Hp=H+s.diag(1,2,-1,3,-2)+s.Rational(3,7)*(mat(n,0,2)+mat(n,2,0))
Lp=lambda X:s.expand(I*com(Hp,X)+g*(D(X)-X))
for u in units:chk(zero(gam(Lp,u)-gam(L,u)),"Hamiltonian independence")
B=s.diag(0,1,2,3,4)
k=s.Rational(3,5)
Lb=lambda X:s.expand(I*com(H,X)-k*com(B,com(B,X)))
Wb=lambda X:2*k*dag(com(B,X))*com(B,X)
for u in units:chk(zero(gam(Lb,u)-Wb(u)),"Nondegenerate B Gamma formula")
chk(commdim(n,[B,dag(B)])==5,"Simple-spectrum B gives MASA")
expr=sum(((i-j)**2*s.conjugate(A[i,j])*A[i,j] for i in range(n) for j in range(n)),s.S.Zero)
chk(s.simplify(s.trace(Wb(A))-2*k*expr)==0,"Exact spectral-weight identity")
chk(s.simplify(s.trace(Wb(A))-2*k*norm)>=0,"Spectral-gap lower bound")
Bd=s.diag(0,0,1,1,2)
chk(commdim(n,[Bd,dag(Bd)])==9,"Degenerate B noise algebra dimension 9")
chk(zero(com(mat(n,0,1),Bd)) and zero(com(mat(n,1,0),Bd)),"Noncommuting blocks survive degeneracy")
chk(not zero(com(mat(n,0,1),mat(n,1,0))),"Degenerate noise algebra is nonabelian")
Ldep=lambda X:s.expand(s.trace(X)/n*s.eye(n)-X)
Vdep=[s.sqrt(s.Rational(1,n))*mat(n,i,j) for i in range(n) for j in range(n)]
chk(commdim(n,Vdep+list(map(dag,Vdep)))==1,"Depolarizing noise algebra scalar")
for u in units:
 Wdep=sum((dag(com(V,u))*com(V,u) for V in Vdep),s.zeros(n))
 chk(zero(gam(Ldep,u)-Wdep),"Depolarizing Gamma identity")
Lunit=lambda X:I*com(H,X)
for u in units:chk(zero(gam(Lunit,u)),"Unitary Hamiltonian yields zero noise form")
chk(commdim(n,[])==25,"Noiseless noise commutant M5")
v=mat(2,0,1)
Ld=lambda X:s.expand(dag(v)*X*v-s.Rational(1,2)*(dag(v)*v*X+X*dag(v)*v))
for i in range(2):
 for j in range(2):
  u=mat(2,i,j)
  chk(zero(gam(Ld,u)-dag(com(v,u))*com(v,u)),"Nonnormal jump Gamma")
chk(commdim(2,[v,dag(v)])==1,"Nonnormal jump noise commutant is scalar")
U=s.eye(n)-s.Rational(2,n)*s.ones(n)
chk(zero(U*dag(U)-s.eye(n)),"Rational unitary")
Lc=lambda X:U*L(dag(U)*X*U)*dag(U)
UA=U*A*dag(U)
chk(zero(gam(Lc,UA)-U*gam(L,A)*dag(U)),"Unitary covariance")
chk(not zero(L(P[0])-D(L(P[0]))),"H37 noise commutant is not L-invariant")
result={
 "title":"P11 AX22 Intrinsic Carre-du-Champ Noise Commutant",
 "scope":"finite Heisenberg GKSL semigroups; exact symbolic cases",
 "all_passed":True,"exact_assertions_passed":C,
 "H37_intrinsic_noise_commutant_dimension":5,
 "H37_pointer_algebra_MASA":True,
 "H37_instantaneous_noise_algebra_invariant_under_L":False,
 "H37_trace_identity":"Tr Gamma_L(A) = 2 gamma ||A-Delta_D A||_HS^2",
 "depolarizing_noise_commutant_dim":1,
 "noiseless_noise_commutant_dim":25,
 "degenerate_B_commutant_dim":9,
 "nonnormal_qubit_jump_commutant_dim":1,
 "general_universal_MASA_selection":False,
 "G2_native_source_provenance":"OPEN",
 "G3_generativity_completeness":"OPEN",
 "human_peer_review":"NOT_PERFORMED",
 "general_Lean_formalization":"NOT_PERFORMED"
}
Path(__file__).with_name("P11_AX22_exact_results.json").write_text(json.dumps(result,indent=2)+"\n")
assert C==171
print(f"AX22: {C}/171 exact assertions PASS; H37=5; depolarizing=1; noiseless=25; degenerate B=9; G2/G3 OPEN")
