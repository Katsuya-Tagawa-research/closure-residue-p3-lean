#!/usr/bin/env python3
"""Exact H75 source-only AX-OA three-world selection benchmark.

Rebuilds original four Kraus operators and each response from scratch.
Proves finite rational rank/nullity statements only. G2/G3 abstract
factorization and physical-provenance boundaries are established in the note.
"""
from itertools import combinations
import sympy as sp

R, I = sp.Rational, sp.I
I2, I3, I6 = sp.eye(2), sp.eye(3), sp.eye(6)
def E(a, b):
    return I3[:, a] * I3[b, :]
O = sp.Matrix([[R(2,3), R(2,3), -R(1,3)],
               [-R(2,3), R(1,3), -R(2,3)],
               [-R(1,3), R(2,3), R(2,3)]])
U = sp.diag(I, 1, I)*O
M = [sp.diag(1, R(3,5), R(3,5)),
     sp.diag(0, R(4,5), R(4,5))]
K = [sp.kronecker_product(I2[:,a]*I2[b,:], U*M[a])
     for a in range(2) for b in range(2)]
assert sum((k.H*k for k in K), sp.zeros(6)) == I6

A, B = E(0,1)-E(1,0), E(2,1)-E(1,2)
def V(x,y):
    C = ((I3+x*A)*(I3-x*A).inv()
         *(I3+y*B)*(I3-y*B).inv())
    return sp.kronecker_product(I2, C)
VA, VB, VAB = V(R(1,4), 0), V(0,R(1,2)), V(R(1,4),R(1,3))
W = sp.kronecker_product(sp.Matrix([[R(3,5),-R(4,5)],
                                    [R(4,5), R(3,5)]]), I3)
S = E(0,1)+E(1,0)+E(2,2)
F = (sp.kronecker_product(sp.diag(1,0),I3)
     + sp.kronecker_product(sp.diag(0,1),S))
P5 = F*W*VB*F*W
for g in [VA, VB, VAB, W, F, P5]:
    assert g.H*g == I6
post=[I6,VA,VAB]
effects=[sp.kronecker_product(I2,E(j,j)) for j in range(3)]
assert sum(effects,sp.zeros(6)) == I6

# 18-dimensional real Hermitian block-diagonal basis
basis=[]
for flag in range(2):
    for j in range(3):
        m=sp.zeros(6)
        m[3*flag:3*flag+3,3*flag:3*flag+3]=E(j,j)
        basis.append(m)
    for a,b in combinations(range(3),2):
        for t in [E(a,b)+E(b,a), I*(E(a,b)-E(b,a))]:
            m=sp.zeros(6)
            m[3*flag:3*flag+3,3*flag:3*flag+3]=t
            basis.append(m)
assert len(basis)==18

def rows(P):
    vals=[]
    for T in post:
        for Q in effects:
            Eout=T.H*Q*T
            Ein=P.H*sum((k.H*Eout*k for k in K),sp.zeros(6))*P
            vals.append([sp.expand(sp.trace(Ein*b)) for b in basis])
    assert len(vals)==9 and all(v.is_Rational for row in vals for v in row)
    return sp.Matrix(vals)

C0=rows(I6)
C4=sp.Matrix.vstack(C0,rows(F),rows(F*VA),rows(F*VB))
C5=sp.Matrix.vstack(C4,rows(P5))
assert [C0.shape,C4.shape,C5.shape]==[(9,18),(36,18),(45,18)]
assert [C0.rank(),C4.rank(),C5.rank()]==[6,17,18]
assert [len(C.nullspace()) for C in (C0,C4,C5)]==[12,1,0]
X=sp.diag(-1,-1,-1,1,1,1)
xc=sp.Matrix([-1,-1,-1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0])
assert sum((xc[j]*basis[j] for j in range(18)),sp.zeros(6))==X
assert C4*xc==sp.zeros(36,1) and C5*xc!=sp.zeros(45,1)
assert sp.Matrix.hstack(C4.nullspace()[0],xc).rank()==1

rp, rm=I6/6+X/12,I6/6-X/12
assert rp.trace()==rm.trace()==1
assert all(v>0 for v in list(rp.diagonal())+list(rm.diagonal()))
Q1=effects[1]
def prob(rho):
    return sp.trace(Q1*sum((k*P5*rho*P5.H*k.H for k in K),
                           sp.zeros(6)))
assert prob(rp)==R(32271,78125)
assert prob(rm)==R(59437,234375)
assert prob(rp)-prob(rm)==R(37376,234375)

# Independently authorized short and long schedule permissions.
# Only on this specified three-world benchmark, these two bits suffice
# to label exactly the three distinct observational equivalence classes.
worlds={(0,0):C0,(1,0):C4,(1,1):C5}
assert len(worlds)==3 and 2**1 < len(worlds) <= 2**2
assert [worlds[b].rank() for b in [(0,0),(1,0),(1,1)]]==[6,17,18]
print("PASS exact H75 source; 9/36/45 authentic original-channel effects")
print("PASS exact ranks 6,17,18 and kernel dimensions 12,1,0")
print("PASS strict-positive state witness delta=37376/234375")
print("PASS conditional two-bit labels for THREE declared source-identical worlds")
print("OPEN actual hardware/calibration and intrinsic F-generated G2/G3")
