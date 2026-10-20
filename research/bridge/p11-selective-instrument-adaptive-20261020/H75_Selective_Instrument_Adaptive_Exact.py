#!/usr/bin/env python3
"""Exact true-H75 instrument-record/feedback audit on six-level Hilbert space.

Identical coarse CPTP source instruments on ALL 36 complex matrix units;
different three-outcome classical records after actual H75 source output;
conditional registered F_fb and second H75 use reveal an unlabelled
site-measurement contrast. Enlarged adaptive future program also separates
arbitrary cut states with equal flag partial trace, without resurrecting
original source-kernel differences. No F-generated hardware is claimed.
"""
import sympy as sp

R,I=sp.Rational,sp.I
I2,I3,I6=sp.eye(2),sp.eye(3),sp.eye(6)
def E(a,b):return I3[:,a]*I3[b,:]
O=sp.Matrix([[R(2,3),R(2,3),-R(1,3)],
             [-R(2,3),R(1,3),-R(2,3)],
             [-R(1,3),R(2,3),R(2,3)]])
U=sp.diag(I,1,I)*O
M=[sp.diag(1,R(3,5),R(3,5)),sp.diag(0,R(4,5),R(4,5))]
K=[sp.kronecker_product(I2[:,a]*I2[b,:],U*M[a])
   for a in range(2) for b in range(2)]
assert sum((k.H*k for k in K),sp.zeros(6))==I6
def Phi(X):
    return sum((k*X*k.H for k in K),sp.zeros(6))

L=[sp.kronecker_product(I2,E(j,j)) for j in range(3)]
J=[(L[0]+L[1])/sp.sqrt(2),
   (L[0]-L[1])/sp.sqrt(2),
   L[2]]
assert sum((k.H*k for k in L),sp.zeros(6))==I6
assert sum((k.H*k for k in J),sp.zeros(6))==I6

def A(X):return [k*X*k.H for k in L]
def B(X):return [k*X*k.H for k in J]
def total(branches):return sum(branches,sp.zeros(6))
full_units=[I6[:,i]*I6[j,:] for i in range(6) for j in range(6)]
assert len(full_units)==36

# Strongest source-free averaged-channel equality on the entire 6x6 algebra.
for X in full_units:
    assert total(A(X))==total(B(X))
assert A(I6)!=B(I6)

S=E(0,1)+E(1,0)+E(2,2)
F=sp.kronecker_product(sp.diag(1,0),I3)+sp.kronecker_product(sp.diag(0,1),S)
assert F.H*F==I6 and F==F.H
Q=L
assert sum(Q,sp.zeros(6))==I6
def rho(flag,site):
    return sp.kronecker_product(
        I2[:,flag]*I2[flag,:],E(site,site))
def pop(X):
    return [sp.expand(sp.trace(q*X)) for q in Q]

# A genuine H75 output has distinct A vs B classical outcome records.
omega=Phi(rho(0,1))
assert sp.trace(omega)==1
a_prob=[sp.expand(sp.trace(x)) for x in A(omega)]
b_prob=[sp.expand(sp.trace(x)) for x in B(omega)]
assert a_prob==[R(4,9),R(1,9),R(4,9)]
assert b_prob==[R(5,18),R(5,18),R(4,9)]
assert sum(a_prob)==sum(b_prob)==1
assert total(A(omega))==total(B(omega))

# Classical feed-forward policy: F on outcome 0, identity on 1,2.
def feedback(branches):
    controls=[F,I6,I6]
    return total([v*x*v.H for v,x in zip(controls,branches)])

# Both instruments give same native probabilities after second H75 IF
# their selective outcomes are forgotten BEFORE any feedback occurs.
assert pop(Phi(total(A(omega))))==pop(Phi(total(B(omega))))

# Identical source and identical FEEDBACK POLICY, but distinct instruments
# give genuinely different unconditional final statistics.
pA=pop(Phi(feedback(A(omega))))
pB=pop(Phi(feedback(B(omega))))
assert pA==[R(8,27),R(211,675),R(88,225)],pA
assert pB==[R(8,27),R(251,675),R(224,675)],pB
assert [a-b for a,b in zip(pA,pB)]==[0,-R(8,135),R(8,135)]
assert sum(pA)==sum(pB)==1
assert all(0<=v<=1 for v in pA+pB)

# The enlarged ADAPTIVE grammar no longer identifies arbitrary cut
# states solely by flag partial trace, unlike #180's smaller grammar.
cut0=rho(0,0)
cut1=rho(1,0)
trflag=lambda X:X[:3,:3]+X[3:,3:]
assert trflag(cut0)==trflag(cut1)
assert pop(Phi(cut0))==pop(Phi(cut1))
cut0_feedback=pop(Phi(feedback(A(cut0))))
cut1_feedback=pop(Phi(feedback(A(cut1))))
assert cut0_feedback==[R(4,9),R(4,9),R(1,9)]
assert cut1_feedback==[R(4,9),R(1,9),R(4,9)]
assert cut0_feedback!=cut1_feedback
# cut0/cut1 are generic legal cut states, NOT asserted in im(Phi).

# A true initial source kernel is still erased for any COMMON suffix,
# including selective classical record plus conditional F feedback.
Xflag=sp.diag(-1,-1,-1,1,1,1)
rp,rm=I6/6+Xflag/12,I6/6-Xflag/12
assert rp!=rm and rp.trace()==rm.trace()==1
assert all(v>0 for v in list(rp.diagonal())+list(rm.diagonal()))
assert Phi(rp)==Phi(rm)
for inst in [A,B]:
    assert inst(Phi(rp))==inst(Phi(rm))
    assert Phi(feedback(inst(Phi(rp))))==Phi(feedback(inst(Phi(rm))))

print("PASS original H75 four-Kraus CPTP source and both 3-outcome instruments")
print("PASS identical nonselective dephasing channel on all 36 matrix units")
print("PASS actual source output branch records (4/9,1/9,4/9) vs (5/18,5/18,4/9)")
print("PASS identical two-use unlabelled outcomes when record is discarded")
print("PASS conditionally controlled original F feedback yields (0,-8/135,+8/135)")
print("PASS enlarged adaptive grammar separates equal-flag-partial-trace cut states")
print("PASS full H75 source-kernel differences remain erased under shared adaptive suffix")
print("BOUNDARY: selective readout, outcome register, feedback and timing imported")
print("OPEN: intrinsic F-generated access, actual P6 provenance and P11 completeness")
