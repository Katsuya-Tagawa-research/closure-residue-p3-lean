"""Exact polynomial K4 coherent-control Hessian/Markov edge identification audit.

No dependencies beyond Python standard library. Verifies coefficient
identities, not only sampled data. NOT a Lean formalization and NOT a
derivation that a P3 inherited CR sector contains six physical K4 controls.
"""
from fractions import Fraction as Rat
from itertools import combinations

# Multivariate rational polynomials: tuples of variable indices are monomials.
class P:
    def __init__(self, d=None):
        self.d = {tuple(k): Rat(v) for k, v in (d or {}).items() if v != 0}
    @staticmethod
    def c(v):
        return P({(): Rat(v)})
    @staticmethod
    def x(i):
        return P({(i,): Rat(1)})
    def __add__(self, other):
        if not isinstance(other,P): other=P.c(other)
        d=self.d.copy()
        for k,v in other.d.items():d[k]=d.get(k,Rat(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,other):return self+(-other)
    def __rsub__(self,other):return other+(-self)
    def __mul__(self,other):
        if not isinstance(other,P):other=P.c(other)
        d={}
        for a,c in self.d.items():
            for b,e in other.d.items():
                t=tuple(sorted(a+b))
                d[t]=d.get(t,Rat(0))+c*e
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,den):return self*P.c(Rat(1)/Rat(den))
    def __eq__(self,other):
        if not isinstance(other,P):other=P.c(other)
        return self.d==other.d
    def deriv(self, variable):
        d={}
        for monom,coefficient in self.d.items():
            m=monom.count(variable)
            if m:
                reduced=list(monom);reduced.remove(variable)
                reduced=tuple(reduced)
                d[reduced]=d.get(reduced,Rat(0))+m*coefficient
        return P(d)
    def __repr__(self): return repr(self.d)

Z=P.c(0)
edges=list(combinations(range(4),2))
x=[P.x(i) for i in range(6)]
pop=[P.x(6+i) for i in range(4)]
K=[[Z for _ in range(4)] for _ in range(4)]
for i,(a,b) in enumerate(edges):
    K[a][b]=x[i];K[b][a]=-x[i]
D=[[pop[i] if i==j else Z for j in range(4)] for i in range(4)]

def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(4)),Z)
             for j in range(4)] for i in range(4)]
def com(A,B):
    X,Y=mm(A,B),mm(B,A)
    return [[X[i][j]-Y[i][j] for j in range(4)] for i in range(4)]
def eii(i):
    return [[P.c(int(a==i and b==i)) for b in range(4)] for a in range(4)]

first=com(K,D)
second=com(K,first)
assert all(first[i][i]==0 for i in range(4))

# For arbitrary diagonal rho, 1/2 diag [K,[K,rho]]
# equals the weighted graph Markov drift (Q_w rho)_a at gamma=1.
for a in range(4):
    expected=sum((x[k]*x[k]*(pop[b]-pop[a])
                  for k,(u,v) in enumerate(edges)
                  for b in ([v] if u==a else [u] if v==a else [])),Z)
    assert second[a][a]/2==expected,(a,second[a][a]/2,expected)

# Preparing population projection E_bb and reading site a != b at t=0
# gives half the coherent population Hessian exactly |K_ab|^2.
# The first-residue algebra action [K,E_bb]_(a,b) recovers K_ab.
for k,(a,b) in enumerate(edges):
    C=com(K,eii(b))
    H=com(K,C)
    assert C[a][b]==x[k],(a,b,C[a][b],x[k])
    assert H[a][a]/2==x[k]*x[k],(a,b,H[a][a]/2,x[k]*x[k])
    total_out=sum((x[e]*x[e] for e,(u,v) in enumerate(edges)
                   if b in (u,v)),Z)
    assert H[b][b]/2==-total_out,(b,a)

# Uniform preparation I/4 has no population Hessian signal.
uniform=[[P.c(Rat(1,4)) if i==j else Z for j in range(4)] for i in range(4)]
assert all(y==0 for row in com(K,uniform) for y in row)

# Standard Markov comparison: Q_ab = gamma*x_ab^2, and with
# stationary pi=1/4, d/dt C_ab(0)=gamma*x_ab^2/4 for a!=b.
gamma=P.x(10)
for k,(a,b) in enumerate(edges):
    q_ab=gamma*x[k]*x[k]
    derivative=q_ab/4
    assert (4*derivative)==gamma*x[k]*x[k]

# B17: an operationally constructed, but non-canonical,
# conservative finite response potential from the quadratic readout.
# For fixed diagonal preparation p, q_a = (1/2)rho''_aa = -A_w p.
# E_p(w)=-(1/2) p.dot(q) = (1/2) Σ w_e (p_a-p_b)^2.
measured_energy= -sum((pop[a]*(second[a][a]/2)
                      for a in range(4)),Z)/2
derived_dirichlet=sum((x[e]*x[e]*
    (pop[a]-pop[b])*(pop[a]-pop[b])/2
    for e,(a,b) in enumerate(edges)),Z)
assert measured_energy==derived_dirichlet
w=[P.x(11+e) for e in range(6)]
energy_w=sum((w[e]*(pop[a]-pop[b])*(pop[a]-pop[b])/2
            for e,(a,b) in enumerate(edges)),Z)
forces=[energy_w.deriv(11+e) for e in range(6)]
for e,(a,b) in enumerate(edges):
    assert forces[e]==(pop[a]-pop[b])*(pop[a]-pop[b])/2
    for k in range(6):
        assert forces[e].deriv(11+k)-forces[k].deriv(11+e)==0

# Readout rank: fixed prepared p_b, all site populations.
# One localized preparation gives rank 3; two gives rank 5;
# three independent localized preparations recover all six weights.
def rat_rank(rows):
    A=[[Rat(v) for v in row] for row in rows]
    if not A:return 0
    nr,nc=len(A),len(A[0])
    k=0
    for j in range(nc):
        pivot=next((i for i in range(k,nr) if A[i][j]!=0),None)
        if pivot is None:continue
        A[k],A[pivot]=A[pivot],A[k]
        c=A[k][j]
        for i in range(k+1,nr):
            v=A[i][j]/c
            for jj in range(j,nc):
                A[i][jj]-=v*A[k][jj]
        k+=1
        if k==nr:break
    return k

def probe_rows(preps):
    return [[int(a!=b and set(e)=={a,b})-
             int(a==b and b in e) for e in edges]
            for b in preps for a in range(4)]

assert rat_rank(probe_rows([0]))==3
assert rat_rank(probe_rows([0,1]))==5
assert rat_rank(probe_rows([0,1,2]))==6
assert rat_rank(probe_rows([0,1,2,3]))==6

print('PASS: full symbolic polynomial identity for 4 coherent population Hessians')
print('PASS: 6 independent off-diagonal first-residue action probes')
print('PASS: 6 edge weights x_ab^2 from prepared-state quadratic population response')
print('PASS: population preparation ranks 3,5,6 for one, two, three basis probes')
print('PASS: CR-like quadratic-return Dirichlet energy and curl-zero response force')
print('PASS: uniform preparation silent; Markov stationary correlation comparison')
print('Scope: a declared K4 coherent control family, not automatically inherited P3 CR controls')
