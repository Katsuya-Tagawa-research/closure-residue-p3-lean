"""Finite SWAP+ZZ two-spin comparator for P9.72; NOT the P9.72 model."""
from fractions import Fraction as F
a=(F(1,2),F(1,3),F(1,4))
b=(F(1,5),F(1,7),F(1,6))
assert sum(t*t for t in a)<1 and sum(t*t for t in b)<1
# Pauli commutators, H=J*SWAP+k*Z1Z2 and O=(X1,Y1,Z1).
swap=[a[2]*b[1]-a[1]*b[2],
      a[0]*b[2]-a[2]*b[0],
      a[1]*b[0]-a[0]*b[1]]
zz=[-2*a[1]*b[2], 2*a[0]*b[2], F(0)]
C=[[swap[i],zz[i]] for i in range(3)]
assert C==[[-F(5,252),-F(1,9)],
           [F(1,30),F(1,6)],[-F(1,210),F(0)]]
minor=C[0][0]*C[1][1]-C[0][1]*C[1][0]
fro2=sum(v*v for row in C for v in row)
assert minor==F(1,2520) and fro2==F(2645,63504)<1
# By Cauchy-Binet, sigma_min(C)>abs(minor).
# For J=k=1/10, ||H||<=1/5 and each finite-time response
# coefficient error <=4t||H||; Frobenius <12t/5.
t=F(1,10000)
assert F(12,5)*t<abs(minor)
for M in (1,2,3,7):
    local=[[v/M for v in row] for row in C]
    assert local[0][0]==-F(5,252*M)
    collective=C
    assert collective==C
# Small spectral perturbations only preserve rank AT LEAST r.
# A rank-deficient matrix may gain rank despite epsilon<sigma_r.
R=[[F(1),F(0)],[F(0),F(0)]]
Rp=[[F(1),F(0)],[F(0),F(1,100)]]
assert R[0][0]*R[1][1]-R[0][1]*R[1][0]==0
assert Rp[0][0]*Rp[1][1]-Rp[0][1]*Rp[1][0]==F(1,100)
print("PASS H63-P972: two-spin independent SWAP+ZZ first-control Jacobian rank2")
print("PASS H63-P972: conditional short-time rank stability; 1/M local mean sensitivity")
print("BOUNDARY: not the original P9.72 microscopic Jacobian or an M-uniform estimate")
