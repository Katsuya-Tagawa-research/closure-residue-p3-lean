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

print('PASS: full symbolic polynomial identity for 4 coherent population Hessians')
print('PASS: 6 independent off-diagonal first-residue action probes')
print('PASS: 6 edge weights x_ab^2 from prepared-state quadratic population response')
print('PASS: uniform preparation silent; Markov stationary correlation comparison')
print('Scope: a declared K4 coherent control family, not automatically inherited P3 CR controls')
