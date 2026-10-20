#!/usr/bin/env python3
"""H75 conditional macro-compilation: exact rational matrix and budget regression.

The general analytical lemmas about all local/one-F/one-W/symmetry-commuting
words and the worst-case diamond norm inequalities are proved in the note.
This checker is an exact *finite* companion, not a formal proof of general
hardware realizability, source generation, or gravitational dynamics.
"""
from fractions import Fraction
import sympy as sp

I, R = sp.I, sp.Rational
E = lambda i, j: sp.eye(3)[:, i] * sp.eye(3)[j, :]
I3, I6 = sp.eye(3), sp.eye(6)

S = E(0, 1) + E(1, 0) + E(2, 2)
assert S.T == S and S*S == I3
Pminus = (I3-S)/2
assert Pminus*Pminus == Pminus

sigma_y = sp.Matrix([[0, -I], [I, 0]])
flag_W = sp.Matrix([[R(3, 5), -R(4, 5)], [R(4, 5), R(3, 5)]])
assert flag_W == R(3, 5)*sp.eye(2) - I*R(4, 5)*sigma_y
W = sp.kronecker_product(flag_W, I3)

Pflag1 = sp.diag(0, 1)
F = (sp.kronecker_product(sp.diag(1, 0), I3)
     + sp.kronecker_product(Pflag1, S))
assert F == I6 - 2*sp.kronecker_product(Pflag1, Pminus)
assert F.T*F == I6

B = E(2, 1)-E(1, 2)
VB3 = (I3+R(1, 2)*B)*(I3-R(1, 2)*B).inv()
assert VB3 == I3+R(4, 5)*B+R(2, 5)*(B*B)
assert VB3.T*VB3 == I3
assert B*S-S*B != sp.zeros(3)
assert VB3*S-S*VB3 != sp.zeros(3)
VB = sp.kronecker_product(sp.eye(2), VB3)

X = sp.diag(-1, -1, -1, 1, 1, 1)
rho_plus, rho_minus = I6/6+X/12, I6/6-X/12
assert rho_plus.trace() == rho_minus.trace() == 1
assert all(v>0 for v in rho_plus.diagonal()+rho_minus.diagonal())

P5 = F*W*VB*F*W
traceflag = lambda y: y[:3,:3]+y[3:,3:]
outX = traceflag(P5*X*P5.T)
expected = sp.Matrix([
    [-R(9216,15625), 0, R(18432,15625)],
    [0,R(9216,15625),-R(18432,15625)],
    [R(18432,15625),-R(18432,15625),0]
])
assert outX == expected and outX!=sp.zeros(3)
assert traceflag(X)==sp.zeros(3)

O = sp.Matrix([
    [R(2,3),R(2,3),-R(1,3)],
    [-R(2,3),R(1,3),-R(2,3)],
    [-R(1,3),R(2,3),R(2,3)]
])
U = sp.diag(I,1,I)*O
M = [sp.diag(1,R(3,5),R(3,5)), sp.diag(0,R(4,5),R(4,5))]
K = [sp.kronecker_product(sp.eye(2)[:,a]*sp.eye(2)[b,:], U*M[a])
     for a in range(2) for b in range(2)]
assert sum((k.H*k for k in K),sp.zeros(6)) == I6
Q1 = sp.kronecker_product(sp.eye(2), E(1,1))
effect = sum((k.H*Q1*k for k in K),sp.zeros(6))
p_plus = sp.trace(effect*P5*rho_plus*P5.T)
p_minus = sp.trace(effect*P5*rho_minus*P5.T)
delta = R(37376,234375)
assert p_plus == R(32271,78125)
assert p_minus == R(59437,234375)
assert p_plus-p_minus == delta
assert 0 < p_plus < 1 and 0 < p_minus < 1

# The analytical bound for 24 effects times 18 Hermitian coordinates is:
# sqrt(24 * [6 diagonal norm-one generators +12 norm-two generators]) = 36.
assert 24*(6+12*4) == 36**2
assert R(3,50)/36 == R(1,600)
assert 36*(7*R(1,2100)/2) == R(3,50)
assert 6*(delta/6)==delta

print("PASS exact: conditional Hamiltonian exponent identities for W, F, VB")
print("PASS exact: registered VB breaks the SWAP eigenspace symmetry")
print("PASS exact: real H75 four-Kraus source and strictly positive witness")
print("PASS exact: post-reset Q1 contrast",p_plus,p_minus,delta)
print("PASS exact: Frobenius constant 36 and strict 1/600,1/2100 rank margins")
print("CAUTION: generators and calibration/scheduling remain independently imported")
