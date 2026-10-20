#!/usr/bin/env python3
"""Exact original-H75 causal future-tester closure and strict positive depth-3 witness.

Checks the unchanged four-Kraus source. Exact 3,5,7,9,9 rank sequence;
invariance under allowed source/dephasing adjoints; reduced source-image
injectivity; two strictly positive qutrit-prepared outputs distinguishable
only with 3 future source uses and native site readout.
"""
import sympy as s

R,I=s.Rational,s.I
I2,I3,I6=s.eye(2),s.eye(3),s.eye(6)
E=lambda a,b:I3[:,a]*I3[b,:]
O=s.Matrix([[R(2,3),R(2,3),-R(1,3)],
            [-R(2,3),R(1,3),-R(2,3)],
            [-R(1,3),R(2,3),R(2,3)]])
U=s.diag(I,1,I)*O
M=[s.diag(1,R(3,5),R(3,5)),s.diag(0,R(4,5),R(4,5))]
K=[s.kronecker_product(I2[:,a]*I2[b,:],U*M[a])
   for a in range(2) for b in range(2)]
assert sum((k.H*k for k in K),s.zeros(6))==I6

phi=lambda X:sum((k*X*k.H for k in K),s.zeros(6))
phi_star=lambda B:sum((k.H*B*k for k in K),s.zeros(6))
L=[s.kronecker_product(I2,E(j,j)) for j in range(3)]
assert sum((l.H*l for l in L),s.zeros(6))==I6
delta_star=lambda X:sum((k.H*X*k for k in L),s.zeros(6))
T=lambda B:sum((m*U.H*B*U*m for m in M),s.zeros(3)).applyfunc(s.expand)
d=lambda B:s.diag(B[0,0],B[1,1],B[2,2])
lift=lambda B:s.kronecker_product(I2,B)
trflag=lambda X:X[:3,:3]+X[3:,3:]
Lambda=lambda Y:(U*sum((m*Y*m for m in M),s.zeros(3))*U.H).applyfunc(s.expand)

Hb=([E(j,j) for j in range(3)]
    +[E(a,b)+E(b,a) for a,b in ((0,1),(0,2),(1,2))]
    +[I*(E(a,b)-E(b,a)) for a,b in ((0,1),(0,2),(1,2))])
assert len(Hb)==9
for B in Hb:
    assert phi_star(lift(B))==lift(T(B))
    assert delta_star(lift(B))==lift(d(B))
    assert T(B).H==T(B) and d(B).H==d(B)

# Rational coordinates of a Hermitian qutrit effect; no floating-point SVD.
def coords(X):
    a=[s.expand(X[j,j]) for j in range(3)]
    for j,k in ((0,1),(0,2),(1,2)):
        a.extend([s.expand(s.re(X[j,k])),s.expand(s.im(X[j,k]))])
    assert all(x.is_Rational for x in a)
    return s.Matrix(a)
def rank(Eff):
    return s.Matrix.hstack(*(coords(X) for X in Eff)).rank()

seed=[E(j,j) for j in range(3)]
levels=[];effects=[]
for depth in range(5):
    effects+=seed
    levels.append(rank(effects))
    seed=[T(Q) for Q in seed]
assert levels==[3,5,7,9,9],levels
basis=[]
for a in effects[:12]:
    if rank(basis+[a])>len(basis):
        basis.append(a)
assert len(basis)==9
for a in basis:
    assert rank(basis+[T(a)])==9
    assert rank(basis+[d(a)])==9

# Original H75 source reduced channel is an invertible Schur multiplier
# followed by unitary conjugation: all coefficients of G are nonzero.
G=s.Matrix([[sum((m[j,j]*m[k,k] for m in M)) for k in range(3)]
            for j in range(3)])
assert G==s.Matrix([[1,R(3,5),R(3,5)],
                   [R(3,5),1,1],
                   [R(3,5),1,1]])
assert all(v!=0 for v in G)
for X in Hb:
    inp=s.kronecker_product(s.diag(1,0),X)
    assert trflag(phi(inp))==Lambda(X)

# A concrete traceless Hermitian difference, hidden at future depth <=2.
H=s.Matrix([[-R(296,15),-R(32,9)+16*I,-R(98,9)+I],
            [-R(32,9)-16*I,R(16,15),-R(176,15)],
            [-R(98,9)-I,-R(176,15),R(56,3)]])
assert H.H==H and s.trace(H)==0
# Exact rational Gershgorin bound: each row absolute sum <52,
# so I_3/3 +- H/300 are positive definite.
for i in range(3):
    upper=sum((abs(s.re(H[i,j]))+abs(s.im(H[i,j]))
               for j in range(3)))
    assert upper<52
assert R(1,3)-R(52,300)>0
Yp,Ym=I3/3+H/300,I3/3-H/300
assert Yp.H==Yp and Ym.H==Ym and s.trace(Yp)==s.trace(Ym)==1
assert Yp!=Ym

sigma_p=phi(s.kronecker_product(s.diag(1,0),Yp))
sigma_m=phi(s.kronecker_product(s.diag(1,0),Ym))
assert sigma_p!=sigma_m
Zp,Zm=trflag(sigma_p),trflag(sigma_m)
assert (Zp-Lambda(Yp)).applyfunc(s.expand)==s.zeros(3)
assert (Zm-Lambda(Ym)).applyfunc(s.expand)==s.zeros(3)
assert Zp!=Zm
for depth in range(4):
    diff=[s.expand((Zp-Zm)[j,j]) for j in range(3)]
    if depth<=2:
        assert diff==[0,0,0],(depth,diff)
    else:
        assert diff==[R(11864,281250),R(3728,281250),
                      -R(15592,281250)],diff
    Zp,Zm=Lambda(Zp),Lambda(Zm)

# Full six-level channel-kernel directions remain invisible after first source.
Xflag=s.diag(-1,-1,-1,1,1,1)
assert trflag(Xflag)==s.zeros(3)
rp,rm=I6/6+Xflag/12,I6/6-Xflag/12
assert phi(rp)==phi(rm)

print("PASS: authentic four-Kraus original H75 and qutrit dual reduction")
print("PASS: exact future tester rank filtration 3,5,7,9,9")
print("PASS: source/dephasing adjoint-invariant nine-dimensional closure")
print("PASS: all future effects factor through the flag partial trace")
print("PASS: original H75 source image injective under reduced flag trace")
print("PASS: positive reachable outputs equal for depths 0,1,2, distinct at 3")
print("PASS: nonzero exact depth-three native site probability differences")
print("PASS: original complete source-kernel erasure remains irreversible")
print("OPEN: hardware authorization, P6 provenance and intrinsic F completeness")
