#!/usr/bin/env python3
"""Exact finite H75 Causal Access Certificate: joint A/B no-event switch bound.

True H75 four-Kraus CPTP source. Two selective three-outcome instruments
with the same nonselective dephasing, original F_fb outcome-0 feedback,
arbitrary legal A/B selection and a finite parity controller.
No assumption that Generative Map F produces hardware or scheduling.
"""
from itertools import product
import sympy as s
r=s.Rational
I=s.I
I2,I3,I6=s.eye(2),s.eye(3),s.eye(6)
e=lambda j,k:I3[:,j]*I3[k,:]
O=s.Matrix([[r(2,3),r(2,3),-r(1,3)],
            [-r(2,3),r(1,3),-r(2,3)],
            [-r(1,3),r(2,3),r(2,3)]])
U=s.diag(I,1,I)*O
M=[s.diag(1,r(3,5),r(3,5)),s.diag(0,r(4,5),r(4,5))]
K=[s.kronecker_product(I2[:,a]*I2[b,:],U*M[a])
   for a,b in product(range(2),repeat=2)]
assert sum((x.H*x for x in K),s.zeros(6))==I6
Phi=lambda X:sum((k*X*k.H for k in K),s.zeros(6))
Phi_star=lambda X:sum((k.H*X*k for k in K),s.zeros(6))
L=[s.kronecker_product(I2,e(j,j)) for j in range(3)]
J=[(L[0]+L[1])/s.sqrt(2),(L[0]-L[1])/s.sqrt(2),L[2]]
for port in (L,J):
    assert sum((q.H*q for q in port),s.zeros(6))==I6
    assert sum((q*I6*q.H for q in port),s.zeros(6))==I6

# Distinct selective instruments, equal averaged dephasing on all 36 units.
for x,y in product(range(6),repeat=2):
    X=I6[:,x]*I6[y,:]
    A=sum((v*X*v.H for v in L),s.zeros(6))
    B=sum((v*X*v.H for v in J),s.zeros(6))
    assert A==B
SW=e(0,1)+e(1,0)+e(2,2)
F=s.kronecker_product(s.diag(1,0),I3)+s.kronecker_product(s.diag(0,1),SW)
assert F.H*F==I6
W=[F,I6,I6]
ports={'A':L,'B':J}
# One authorized cycle: original source -> chosen instrument -> outcome feedback.
# j=0 is no-event; j=1,2 are event outcomes.
cycle={name:[[W[j]*port[j]*k for k in K] for j in range(3)]
       for name,port in ports.items()}
for name,ks in cycle.items():
    assert sum((v.H*v for group in ks for v in group),s.zeros(6))==I6
    assert len(ks[0])==4 and len(ks[1])==4 and len(ks[2])==4

dualN=lambda name,X:sum((v.H*X*v for v in cycle[name][0]),s.zeros(6))
EA=dualN('A',I6);EB=dualN('B',I6)
AA=s.Matrix([[r(4,9),r(4,15),-r(2,15)],
             [r(4,15),r(4,9),-r(2,9)],
             [-r(2,15),-r(2,9),r(1,9)]])
assert EA==s.kronecker_product(I2,AA)
assert AA.eigenvals()=={0:1,r(1,2)-s.sqrt(745)/90:1,
                        r(1,2)+s.sqrt(745)/90:1}
b=r(5,6)
assert all((b*I3-AA)[:j,:j].det()>0 for j in (1,2,3))

# B0 effect = (site0 + site1)/2, giving the sharper <=I/2 bound.
assert J[0].H*J[0]==(L[0]+L[1])/2
assert EB==Phi_star((L[0]+L[1])/2)
assert EB==s.kronecker_product(I2,EB[:3,:3])
assert (I3/2-EB[:3,:3]).eigenvals()=={
    0:1,r(1,4)-s.sqrt(1513)/180:1,
    r(1,4)+s.sqrt(1513)/180:1}
assert all((b*I3-EB[:3,:3])[:j,:j].det()>0 for j in (1,2,3))
print("PASS: A/B instruments identical averaged CPTP on all 36 input units")
print("PASS: original H75 A0 source-cycle effect EA <= 5/6 I6")
print("PASS: original H75 B0 source-cycle effect EB <= 1/2 I6")

# A separate externally authorized one-bit classical parity controller
# alternates policies A and B. Explicit Kraus operators realize a CPTP
# source+instrument+feedback cycle on the 12D controller+source Hilbert space.
ctrl=s.eye(2)
controller=[]
controller_noevent=[]
for c,name in enumerate(('A','B')):
    flag=ctrl[:,1-c]*ctrl[c,:]
    for j in range(3):
        for v in cycle[name][j]:
            z=s.kronecker_product(flag,v)
            controller.append(z)
            if j==0:controller_noevent.append(z)
I12=s.eye(12)
assert len(controller)==24 and len(controller_noevent)==8
assert sum((v.H*v for v in controller),s.zeros(12))==I12
Econtroller=sum((v.H*v for v in controller_noevent),s.zeros(12))
assert Econtroller.H==Econtroller
assert Econtroller[:6,:6]==EA and Econtroller[6:,6:]==EB
assert Econtroller[:6,6:]==s.zeros(6)
assert Econtroller[6:,:6]==s.zeros(6)

# Analytic noncommutative switching proof:
# each N_t is CP, so N_t*(0<=X<=uI) <= u N_t*(I) <= ubI;
# induction over arbitrary legally chosen A/B words implies n-cycle
# survival <= b**n for every starting state. Finite exact matrix bounds
# EA and EB above are the machine-auditable inductive premises.
assert all((b*I3-AA)[:j,:j].det()>0 for j in (1,2,3))
assert all((b*I3-EB[:3,:3])[:j,:j].det()>0 for j in (1,2,3))
assert b**25>r(1,100)>=b**26
print("PASS: 2-state classical controller has exact Kraus CPTP completeness")
print("PASS: CP common one-step bound proves ANY permitted A/B switch tail (5/6)^n")
print("PASS: conservative 1% common survival-tail cutoff K=26")
print("BOUNDARY: controller and schedule separately assumed, not F-derived")
print("OPEN: exact infinite archive, P6 provenance, P9 gravity and P11 completeness")
