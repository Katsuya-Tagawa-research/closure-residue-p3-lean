#!/usr/bin/env python3
"""UNNUMBERED independent exact OA-G39..G42 Uniform History-Tail audit.

Finite SymPy regression only: no F-access-generation, H/PR assignment,
physical P6 experimental provenance, P3 residue equality or peer review.
"""
import sympy as sp
R=sp.Rational
I2=sp.eye(2)
E=lambda i,j:sp.eye(2)[:,i]*sp.eye(2)[j,:]

eta=R(1,4)
K0=sp.diag(1,sp.sqrt(eta))
K1=sp.sqrt(1-eta)*E(0,1)
assert K0.H*K0+K1.H*K1==I2
N=lambda X:K0*X*K0.H
Y=lambda X:K1*X*K1.H
x=E(1,1)
for k in range(1,9):
    assert sp.simplify(sp.trace(Y(x)))==(1-eta)*eta**(k-1)
    x=N(x)
assert sp.simplify(sp.trace(x))==eta**8

TN=sp.Matrix([[eta,0],[0,1]])
TE=sp.Matrix([[0,1-eta],[0,0]])
a=sp.Matrix([[1,0]])
ones=sp.ones(2,1)
assert TN+TE==sp.Matrix([[eta,1-eta],[0,1]])
def f(word):
    z=a
    for c in word:
        z=z*(TN if c=="N" else TE)
    return sp.expand((z*ones)[0])
H=sp.Matrix([[f(""),f("E")],[f("E"),f("EE")]])
assert H.det()==-(1-eta)**2 and H.rank()==2
for n in [1,2,5,10]:
    outcome=[(1-eta)*eta**(k-1) for k in range(1,n+1)]+[eta**n]
    assert len(outcome)==n+1 and sum(outcome)==1
print("PASS G39/G40: CPTP 2-state instrument, exact Hankel rank 2, n+1 archive outcomes")

for a,e,answer in [(R(1,2),R(1,8),3),(R(1,4),R(1,64),3),
                   (R(3,4),R(9,16),2),(R(1,3),R(1,81),4)]:
    d=1
    while a**d>e:d+=1
    assert d==answer and (d==1 or a**(d-1)>e)
    assert sum((1-a)*a**(k-1) for k in range(1,d+1))==1-a**d
print("PASS G41: conditional D_epsilon formula on exact geometric test cases")

# Fixed-dimensional gapless family with a decaying initial slow-mode weight.
for m in [2,3,7,19,101]:
    w=R(1,m)
    Q=sp.diag(0,1-w)
    alpha=sp.Matrix([[1-w,w]])
    for k in [1,2,4,10,50]:
        survival=(alpha*Q**k*sp.ones(2,1))[0]
        assert survival==w*(1-w)**k and survival<=R(1,k+1)

# Arbitrary nilpotent shifts have rho=0 but unbounded survival cutoffs.
for m in [2,3,5,9]:
    Q=sp.zeros(m)
    for j in range(m-1):Q[j,j+1]=1
    alpha=sp.Matrix([[1]+[0]*(m-1)])
    assert Q**m==sp.zeros(m)
    assert all((alpha*Q**k*sp.ones(m,1))[0]==1 for k in range(m))
    assert (alpha*Q**m*sp.ones(m,1))[0]==0
print("PASS G42: no uniform gap necessary; nilpotent unbounded-dim counterexample")

# True two-branch CP/TNI instrument with strict contraction only at ell=2.
K=sp.Matrix([[0,1],[R(1,2),0]])
L=sp.diag(sp.sqrt(R(3,4)),0)
assert K.H*K+L.H*L==I2
assert K.H*K==sp.diag(R(1,4),1)
assert (K**2).H*(K**2)==I2/4
ell,b=2,R(1,4)
for n in range(20):
    rem=b**(n//ell)*I2-(K**n).H*(K**n)
    assert all(v>=0 for v in rem.eigenvals())
print("PASS CP quantum block: N*2(I)=I/4, all-source tail <=4^-floor(n/2)")

# Conservative perturbation: N'=(1-xi)N, xi=1/8 in trace-induced norm.
xi=R(1,8)
Kp=sp.sqrt(1-xi)*K
assert Kp.H*Kp==(1-xi)*(K.H*K)
conservative=b+ell*xi
assert conservative==R(1,2)<1
assert all(v>=0 for v in
           (conservative*I2-(Kp**2).H*(Kp**2)).eigenvals())
print("PASS robustness: b+ell*xi=1/2 is a valid conservative bound")

# Rank-one replacement source is maximally mixing but instrument survival
# can approach 1 with N_p=(1-p)source while event branch E_p=p source.
ks=[E(0,0),E(0,1)]
assert sum((q.H*q for q in ks),sp.zeros(2))==I2
def S(X):return sum((q*X*q.H for q in ks),sp.zeros(2))
Sm=sp.Matrix.hstack(*(S(E(i,j)).reshape(4,1) for i in range(2)
                                            for j in range(2)))
assert Sm.rank()==1 and Sm.eigenvals()=={1:1,0:3}
for p in [R(1,2),R(1,10),R(1,100)]:
    def np(X):return (1-p)*S(X)
    for k in [1,2,8]:
        X=I2/2
        for _ in range(k):X=np(X)
        assert sp.expand(sp.trace(X))==(1-p)**k
print("PASS maximal source spectral gap but arbitrarily slow no-event tail")
print("ALL UNNUMBERED FINITE EXACT CERTIFICATE CHECKS PASS")
