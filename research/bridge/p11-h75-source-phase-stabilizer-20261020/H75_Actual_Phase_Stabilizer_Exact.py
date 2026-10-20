#!/usr/bin/env python3
"""Exact H75 flag-phase stabilizer and oriented-port selection obstruction.

Directly rebuilds the unchanged H75 4-Kraus 6D channel. No imported checker.
Proves D_pi input+output symmetry on all 36 complex matrix units; original
18D block input equality for opposite W orientations; exact Born numbers.
A continuous U(1) statement is proved algebraically in the companion note.
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
Phi=lambda X:sum((k*X*k.H for k in K),sp.zeros(6))

# True source involutive stabilizer, a subgroup of its continuous U(1).
D=sp.kronecker_product(sp.diag(1,-1),I3)
assert D.H*D==I6 and D*D==I6
for i in range(6):
    for j in range(6):
        X=I6[:,i]*I6[j,:]
        a=Phi(X)
        assert Phi(D*X*D)==a
        assert D*a*D==a
# Offdiagonal input flag coherences are fully erased;
# output is flag diagonal: the two claims hold on ALL M_6.

W=sp.kronecker_product(
    sp.Matrix([[R(3,5),-R(4,5)],[R(4,5),R(3,5)]]),I3)
Wminus=W.T
assert W.H*W==I6 and Wminus.H*Wminus==I6
assert W != Wminus
assert D*W*D==Wminus and D*Wminus*D==W
# Anti-Hermitian infinitesimal orientation also changes sign.
JW=sp.kronecker_product(sp.Matrix([[0,-1],[1,0]]),I3)
assert D*JW*D==-JW

# Original conditional site SWAP and original Cayley-B coherent port.
S=E(0,1)+E(1,0)+E(2,2)
F=(sp.kronecker_product(sp.diag(1,0),I3)
   +sp.kronecker_product(sp.diag(0,1),S))
B=E(2,1)-E(1,2)
VB=sp.kronecker_product(I2,(I3+R(1,2)*B)*(I3-R(1,2)*B).inv())
for g in [F,VB]:
    assert g.H*g==I6 and D*g*D==g

P=F*W*VB*F*W
Pminus=F*Wminus*VB*F*Wminus
assert Pminus==D*P*D
for flag in range(2):
    for i in range(3):
        for j in range(3):
            X=sp.zeros(6)
            X[3*flag+i,3*flag+j]=1
            assert Phi(P*X*P.H)==Phi(Pminus*X*Pminus.H)

# Strictly positive physical pair and real (original) site population.
Xflag=sp.diag(-1,-1,-1,1,1,1)
rp,rm=I6/6+Xflag/12,I6/6-Xflag/12
assert rp.trace()==rm.trace()==1
assert all(v>0 for v in list(rp.diagonal())+list(rm.diagonal()))
Q1=sp.kronecker_product(I2,E(1,1))
assert Q1.H==Q1 and Q1*Q1==Q1
def prob(g,rho):
    return sp.expand(sp.trace(Q1*Phi(g*rho*g.H)))
for word in [P,Pminus]:
    assert prob(word,rp)==R(32271,78125)
    assert prob(word,rm)==R(59437,234375)
    assert prob(word,rp)-prob(word,rm)==R(37376,234375)

# A source fixed by the involution cannot have a natural selector of one
# oriented W representative: both are exchanged, no fixed candidate.
candidates=[W,Wminus]
assert all(D*C*D != C for C in candidates)
# With a separately furnished orientation BIT flipped by D, a
# two-valued equivariant selector DOES exist on that explicitly enriched set.
selector={1:W,-1:Wminus}
assert all(D*selector[s]*D == selector[-s] for s in (-1,1))

print("PASS: original H75 four-Kraus channel is CPTP")
print("PASS: same Dπ stabilizes H75 at input+output on ALL 36 matrix units")
print("PASS: oriented flag W and W^-1 exchanged by actual source stabilizer")
print("PASS: no fixed individual oriented W candidate; 1 imported bit suffices")
print("PASS: opposite W orientations give identical full source outputs on all 18 native block inputs")
print("PASS: same positive Born probabilities for both words: 32271/78125, 59437/234375")
print("OPEN: port hardware, F-derived orientation bit, original P6 provenance, P9 geometry")
