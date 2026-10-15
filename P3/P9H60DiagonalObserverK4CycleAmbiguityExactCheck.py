"""H60 exact rational audit: four-site diagonal-observer rank bottleneck,
quadratic population cycle ambiguity, and conditional X/Y tangent recovery.

Comparator: H59 generic U(4) density orbit, NOT proven to be the
microscopic original-P3/P6/P9.64 KKS source. Standard-library only.
"""
from fractions import Fraction as F
from itertools import combinations

def rank(A):
    M=[[F(x) for x in row] for row in A]
    if not M: return 0
    nr,nc,p=len(M),len(M[0]),0
    for j in range(nc):
        k=next((i for i in range(p,nr) if M[i][j]),None)
        if k is None: continue
        M[p],M[k]=M[k],M[p]
        v=M[p][j]
        M[p]=[x/v for x in M[p]]
        for i in range(nr):
            if i!=p and M[i][j]:
                v=M[i][j]
                M[i]=[x-v*y for x,y in zip(M[i],M[p])]
        p+=1
        if p==nr: break
    return p

def det(A):
    M=[[F(x) for x in row] for row in A]
    n=len(M);d=F(1)
    assert all(len(row)==n for row in M)
    for j in range(n):
        k=next((i for i in range(j,n) if M[i][j]),None)
        if k is None:return F(0)
        if j!=k:M[j],M[k]=M[k],M[j];d=-d
        v=M[j][j];d*=v
        for i in range(j+1,n):
            q=M[i][j]/v
            M[i]=[a-q*b for a,b in zip(M[i],M[j])]
    return d

def matvec(A,x):
    return [sum((a*b for a,b in zip(row,x)),F(0)) for row in A]

def matmul(A,B):
    return [[sum((a*b for a,b in zip(row,col)),F(0))
             for col in zip(*B)] for row in A]

def comm(A,B):
    AB,BA=matmul(A,B),matmul(B,A)
    return [[a-b for a,b in zip(x,y)] for x,y in zip(AB,BA)]

def diag(x):
    n=len(x)
    return [[x[i] if i==j else F(0) for j in range(n)] for i in range(n)]

lam=[F(1,10),F(2,10),F(3,10),F(4,10)]
edges=list(combinations(range(4),2))
assert edges==[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
gaps=[lam[b]-lam[a] for a,b in edges]
assert all(g>0 for g in gaps)

# For any offdiagonal anti-Hermitian K, diag[K,rho*]=0.
# This exact rational skew-Hermitian witness also checks the
# coefficient of t^2 in p_a(t)=diag(exp(tK)rho*exp(-tK)).
rho=diag(lam)
K=[[F(0)]*4 for _ in range(4)]
for e,(a,b) in enumerate(edges):
    K[a][b]=F(e+1,7)
    K[b][a]=-K[a][b]
first=comm(K,rho)
assert all(first[i][i]==0 for i in range(4))
assert all(first[a][b]==gaps[e]*K[a][b] for e,(a,b) in enumerate(edges))
second=comm(K,first)

# mu_D has trace-one codomain of dimension 3.
# Quadratic coefficient c_a=sum_b (lam_b-lam_a)*|K_ab|^2
# equals incidence(K4) diag(spectral gap) r.
inc=[[F(0)]*6 for _ in range(4)]
for e,(a,b) in enumerate(edges):
    inc[a][e]=F(1)
    inc[b][e]=F(-1)
D=[[inc[a][e]*gaps[e] for e in range(6)] for a in range(4)]
assert rank(inc)==rank(D)==3
assert all(sum(inc[a][e] for a in range(4))==0 for e in range(6))
r=[K[a][b]**2 for a,b in edges]
assert [second[a][a]/2 for a in range(4)]==matvec(D,r)

# Three independent K4 triangular cycles in ker(inc).
cycles=[]
for a,b in [(1,2),(1,3),(2,3)]:
    cyc=[F(0)]*6
    cyc[edges.index((0,a))]+=1
    cyc[edges.index((a,b))]+=1
    cyc[edges.index((0,b))]-=1
    assert matvec(inc,cyc)==[F(0)]*4
    cycles.append(cyc)
assert rank(cycles)==3 and len(edges)-rank(D)==3

# Positive pair r0,r1: equal quadratic population coefficients
# but DIFFERENT K4 edge weights. Every positive r admits a genuine
# K_ab=sqrt(r_ab) real anti-symmetric generator.
r0=[F(1)]*6
eps=F(1,100)
r1=[r0[e]+eps*cycles[0][e]/gaps[e] for e in range(6)]
assert r1==[F(11,10),F(19,20),F(1),F(11,10),F(1),F(1)]
assert all(x>0 for x in r0+r1) and r0!=r1
assert matvec(D,r0)==matvec(D,r1)
assert sum(matvec(D,r0))==0

# Exact independent re-derivation of H52 six-edge -> Sym^2(S):
# basis f_i=e_i-e_3, v_ab=f_a-f_b; B(w)=sum w v v^T.
f=[[F(1),F(0),F(0)],[F(0),F(1),F(0)],
   [F(0),F(0),F(1)],[F(-1),F(-1),F(-1)]]
v=[[f[a][j]-f[b][j] for j in range(3)] for a,b in edges]
V=[[[vi[i]*vi[j] for j in range(3)] for i in range(3)] for vi in v]
flat=lambda M:[M[0][0],M[1][1],M[2][2],M[0][1],M[0][2],M[1][2]]
B6=[[flat(V[e])[j] for e in range(6)] for j in range(6)]
assert rank(B6)==6 and det(B6)==-256
assert matvec(B6,r0)!=matvec(B6,r1)
# Both weights >0 give positive definite B(w). Since g(w)=
# 16 G B(w)^-1 G is injective, their spatial metrics differ.

# In contrast, ideal all-six-pair X/Y coherence readout would
# recover the six complex offdiagonal K_ab from delta rho_ab
# = (lam_b-lam_a)*K_ab, with tangent real rank 12.
coherence_rank=2*sum(g!=0 for g in gaps)
coherence_jac_det=F(1)
for g in gaps: coherence_jac_det*=g*g
assert coherence_rank==12 and coherence_jac_det>0
assert coherence_rank>rank(D)

print("PASS H60: diagonal observer rank <=3, and all 12 KKS tangent directions are first-order population silent at diagonal rho*")
print("PASS H60: population quadratic Jacobian incidence(K4) diag(gap) has rank 3 and 3 independent cycle blind directions")
print("PASS H60: two positive edge patterns have identical second-order populations but distinct H52 spatial metrics")
print("PASS H60: hypothetical all-pair X/Y readout has full real tangent rank 12, without establishing physical access")
print("BOUNDARY: no original P3 signed residue, physical P6 controls, KKS-ADM symplectomorphism, HDA or Einstein derivation")
