#!/usr/bin/env python3
"""Exact original H75 two-use causal activation vs irrecoverable kernel.

Rebuilds unchanged four-Kraus H75 on C^2 x C^3; no import of surrogate model.
Single-use native site effects cannot detect separately supplied dephasing,
but two-use native site effects distinguish dephasing at the causal cut.
The full state equality for a source-kernel preparation pair remains irreversible
under any downstream channel-only memoryless process.
"""
import sympy as sp

R,I=sp.Rational,sp.I
I2,I3,I6=sp.eye(2),sp.eye(3),sp.eye(6)
def E(a,b):
    return I3[:,a]*I3[b,:]
O=sp.Matrix([[R(2,3),R(2,3),-R(1,3)],
             [-R(2,3),R(1,3),-R(2,3)],
             [-R(1,3),R(2,3),R(2,3)]])
U=sp.diag(I,1,I)*O
M=[sp.diag(1,R(3,5),R(3,5)),sp.diag(0,R(4,5),R(4,5))]
K=[sp.kronecker_product(I2[:,a]*I2[b,:],U*M[a])
   for a in range(2) for b in range(2)]
assert sum((k.H*k for k in K),sp.zeros(6))==I6

def phi(X):
    return sum((k*X*k.H for k in K),sp.zeros(6))
def phi_star(X):
    return sum((k.H*X*k for k in K),sp.zeros(6))
L=[sp.kronecker_product(I2,E(j,j)) for j in range(3)]
assert sum((l.H*l for l in L),sp.zeros(6))==I6

def delta(X):
    return sum((l*X*l.H for l in L),sp.zeros(6))
def delta_star(X):
    return sum((l.H*X*l for l in L),sp.zeros(6))
Q=L[:]  # same original three site population projections
assert sum(Q,sp.zeros(6))==I6
assert all(q.H==q and q*q==q for q in Q)
assert all(delta_star(q)==q for q in Q)

full_units=[I6[:,i]*I6[j,:] for i in range(6) for j in range(6)]
assert len(full_units)==36

# Strong exact shallow indistinguishability, linear over ALL 36 complex units.
for X in full_units:
    for q in Q:
        assert sp.simplify(sp.trace(q*delta(phi(X)))
                           -sp.trace(q*phi(X)))==0

rho00=sp.kronecker_product(sp.diag(1,0),E(0,0))
assert rho00==rho00.H and rho00.trace()==1 and rho00*rho00==rho00
omega=phi(rho00)
assert sp.simplify(omega.trace())==1
assert omega != delta(omega) # full source state is not dephased

def born(q,state):
    return sp.simplify(sp.trace(q*state))
single_id=[born(q,omega) for q in Q]
single_dephased=[born(q,delta(omega)) for q in Q]
assert single_id==single_dephased==[R(4,9),R(4,9),R(1,9)]

two_id=phi(omega)
two_dephased=phi(delta(omega))
assert two_id != two_dephased
dist_id=[born(q,two_id) for q in Q]
dist_dephased=[born(q,two_dephased) for q in Q]
assert dist_id==[R(7,15),R(8,45),R(16,45)]
assert dist_dephased==[R(11,27),R(8,27),R(8,27)]
difference=[v-w for v,w in zip(dist_id,dist_dephased)]
assert difference==[R(8,135),-R(16,135),R(8,135)]
assert sum(dist_id)==sum(dist_dephased)==1
assert sum(difference)==0
assert all(0<=v<=1 for v in dist_id+dist_dephased)

# The general adjoint-source tester criterion:
# one source: Phi*((id-Delta*)(Q)) = 0;
# two source: Phi*((id-Delta*)(Phi*(Q))) != 0 for at least one Q.
for q in Q:
    assert phi_star(q-delta_star(q))==sp.zeros(6)
assert any(
    phi_star(phi_star(q)-delta_star(phi_star(q))) != sp.zeros(6)
    for q in Q
)
for q in Q:
    d_eff=phi_star(phi_star(q)-delta_star(phi_star(q)))
    assert sp.simplify(sp.trace(d_eff*rho00)
                       -(born(q,two_id)-born(q,two_dephased)))==0

# A real *source-kernel* direction is erased at the causal state cut.
Xflag=sp.diag(-1,-1,-1,1,1,1)
rho_p,rho_m=I6/6+Xflag/12,I6/6-Xflag/12
assert rho_p!=rho_m and rho_p.trace()==rho_m.trace()==1
assert all(x>0 for x in list(rho_p.diagonal())+list(rho_m.diagonal()))
assert phi(rho_p)==phi(rho_m)
for suffix in (
    lambda x:x,
    phi,
    delta,
    lambda x:phi(delta(x)),
    lambda x:phi(phi(x)),
    lambda x:delta(phi(delta(x)))
):
    a=suffix(phi(rho_p))
    b=suffix(phi(rho_m))
    assert a==b

print("PASS authentic H75 four-Kraus source and imported dephasing both CPTP")
print("PASS shallow site-readout identity for all 36 complex input matrix units")
print("PASS one-use site distribution (4/9,4/9,1/9) with/without dephasing")
print("PASS second source without dephasing: (7/15,8/45,16/45)")
print("PASS second source with dephasing: (11/27,8/27,8/27)")
print("PASS exact two-use causal difference (8/135,-16/135,8/135)")
print("PASS correct one-use vs two-use Heisenberg effect criterion")
print("PASS full source-kernel rho+/- equality survives downstream channel compositions")
print("BOUNDARY: memoryless source reuse, intervening dephasing and scheduling imported")
print("OPEN: F-derived AX-OA, P6 physical provenance and P9/P11 completeness")
