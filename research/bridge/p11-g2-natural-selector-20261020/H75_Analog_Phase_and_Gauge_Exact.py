#!/usr/bin/env python3
"""Exact H75 six-level fractional-phase witness + finite equivariant-selector NO-GO.

Uses true original H75 source, original real registered coherent endpoints,
and a separately imported imaginary-phase-sensitive positive POVM.
The phase POVM is not a native H75 post-reset readout; it is a conditional
mathematical tester preceding the source reset.
"""
import sympy as sp

R, I=sp.Rational, sp.I
I2,I3,I6=sp.eye(2),sp.eye(3),sp.eye(6)
E=lambda i,j:I3[:,i]*I3[j,:]
O=sp.Matrix([[R(2,3),R(2,3),-R(1,3)],
             [-R(2,3),R(1,3),-R(2,3)],
             [-R(1,3),R(2,3),R(2,3)]])
U=sp.diag(I,1,I)*O
M=[sp.diag(1,R(3,5),R(3,5)),sp.diag(0,R(4,5),R(4,5))]
K=[sp.kronecker_product(I2[:,a]*I2[b,:],U*M[a])
   for a in range(2) for b in range(2)]
assert sum((k.H*k for k in K),sp.zeros(6))==I6

S=E(0,1)+E(1,0)+E(2,2)
Pm=(I3-S)/2
flag1=sp.diag(0,1)
P=sp.kronecker_product(flag1,Pm)
assert P==P.H and P*P==P and sp.trace(P)==1
F=I6-2*P
half=I6+(I-1)*P
assert sp.simplify(half*half-F)==sp.zeros(6)
assert sp.simplify(half.H*half-I6)==sp.zeros(6)

W=sp.kronecker_product(sp.Matrix([[R(3,5),-R(4,5)],[R(4,5),R(3,5)]]),I3)
A=E(0,1)-E(1,0)
B=E(2,1)-E(1,2)
def V(x,y):
    v=(I3+x*A)*(I3-x*A).inv()*(I3+y*B)*(I3-y*B).inv()
    return sp.kronecker_product(I2,v)
for fixed in (W,F,V(R(1,4),0),V(0,R(1,2)),V(R(1,4),R(1,3))):
    assert fixed.T*fixed == I6
    assert all(v.is_Rational for v in fixed)
assert half!=half.conjugate()
# The first three canonical basis vectors are +1 eigenvectors of half,
# so it cannot be real even after multiplying by a common overall phase
# while its flag-1 antisymmetric sector has relative +i phase.
assert half[0,0]==1
assert half[3,3]==(1+I)/2

plus=I3[:,2]
minus=(I3[:,0]-I3[:,1])/sp.sqrt(2)
assert (plus.T*plus)[0]==(minus.T*minus)[0]==1
assert (plus.T*minus)[0]==0
assert S*plus==plus and S*minus==-minus
chi=(plus+minus)/sp.sqrt(2)
chi_i=(plus+I*minus)/sp.sqrt(2)
psi=sp.kronecker_product(I2[:,1],chi)
phi=sp.kronecker_product(I2[:,1],chi_i)
rho=psi*psi.H
Q=sp.kronecker_product(I2,chi_i*chi_i.H)
assert rho.H==rho and sp.trace(rho)==1 and rho*rho==rho
assert sp.simplify(Q.H-Q)==sp.zeros(6)
assert sp.simplify(Q*Q-Q)==sp.zeros(6)
assert sp.trace(Q)==2
assert sp.simplify(half*psi-phi)==sp.zeros(6)
def p(U):
    return sp.simplify(sp.trace(Q*U*rho*U.H))
assert p(half)==1
assert p(I6)==sp.Rational(1,2)

# Exact algebra for arbitrary REAL output vector r:
# <r|Q|r> = 1/2 <r|Rproj|r>,
# Rproj an orthogonal projector, hence <= (r.T*r)/2.
projreal=sp.kronecker_product(I2,plus*plus.T+minus*minus.T)
assert sp.simplify(projreal*projreal-projreal)==sp.zeros(6)
assert sp.simplify(Q+Q.conjugate()-projreal)==sp.zeros(6)
x=sp.Matrix(sp.symbols("x0:6",real=True))
assert sp.simplify((x.T*Q*x)[0]-(x.T*projreal*x)[0]/2)==0
# Rproj's orthogonal complement is positive semidefinite:
compl=I6-projreal
assert sp.simplify(compl*compl-compl)==sp.zeros(6)
assert sp.simplify(compl.T-compl)==sp.zeros(6)
assert sp.trace(compl)==2

# Finite G=Z2 abstract gauge selector obstruction: one fixed source
# and two distinct candidate accesses swapped by the only nonidentity symmetry.
sources=("s",)
accesses=("plus","minus")
action={"+":{a:a for a in accesses},
        "-":{"plus":"minus","minus":"plus"}}
for choice in accesses:
    # Equivariant selection would require action_g(choice)=choice because g*s=s.
    assert action["-"][choice]!=choice
# A fixed object added to candidate space *would* permit a trivial selection,
# but it is not in the declared pair of admissible implemented access worlds.

print("PASS: authentic original four-Kraus H75 source is CPTP")
print("PASS: all fixed endpoint controls are real orthogonal")
print("PASS: half F pulse has complex relative i phase and squares to F")
print("PASS: rho is flagged block-diagonal; Q is positive complete POVM branch")
print("PASS: exact phase POVM p(analog)=1, sup_O(6) p(real endpoint)=1/2")
print("PASS: simple Z2 two-access candidate system has no natural deterministic selector")
print("BOUNDARY: independent phase-sensitive POVM and analog pulse authorization")
print("BOUNDARY: this Z2 example is not identified as an actual H75 source symmetry")
