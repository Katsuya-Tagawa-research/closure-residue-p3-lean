#!/usr/bin/env python3
"""H75 fixed AX-OA: exact conjugation/phase blindness and rank check."""
from pathlib import Path
import csv
import sympy as s
I=s.I;R=s.Rational
def E(i,j,n=3):
 a=s.zeros(n);a[i,j]=1;return a
O=s.Matrix([[R(2,3),R(2,3),-R(1,3)],[-R(2,3),R(1,3),-R(2,3)],[-R(1,3),R(2,3),R(2,3)]])
U=s.diag(I,1,I)*O
M=[s.diag(1,R(3,5),R(3,5)),s.diag(0,R(4,5),R(4,5))]
W=s.kronecker_product(s.Matrix([[R(3,5),-R(4,5)],[R(4,5),R(3,5)]]),s.eye(3))
F=s.diag(s.eye(3),E(0,1)+E(1,0)+E(2,2))
A=E(0,1)-E(1,0);B=E(2,1)-E(1,2)
def V(x,y):return s.kronecker_product(s.eye(2),(s.eye(3)+x*A)*(s.eye(3)-x*A).inv()*(s.eye(3)+y*B)*(s.eye(3)-y*B).inv())
va=V(R(1,4),0); vb=V(0,R(1,2))
pre=[s.eye(6),F,F*va,F*W*vb*F*W]
post=[s.eye(6),va,V(R(1,4),R(1,3))]
q=[s.kronecker_product(s.eye(2),E(i,i)) for i in range(3)]
h=[E(i,i) for i in range(3)]
for i,j in ((0,1),(0,2),(1,2)):h += [E(i,j)+E(j,i),I*(E(i,j)-E(j,i))]
h18=[s.diag(t,s.zeros(3)) for t in h]+[s.diag(s.zeros(3),t) for t in h]
def C(u):
 ks=[s.kronecker_product(E(a,b,2),u*M[a]) for a in range(2) for b in range(2)]
 rows=[]
 for p in pre:
  for t in post:
   for qq in q:
    f=p.T*sum((k.H*t.T*qq*t*k for k in ks),s.zeros(6))*p
    rows.append([s.expand(s.trace(f*v)) for v in h18])
 return s.Matrix(rows)
c=C(U);real=C(O);conj=C(s.conjugate(U))
imag=(4,6,8,13,15,17)
assert (c.rank(),real.rank(),conj.rank())==(18,12,18)
assert all(real[:,j]==s.zeros(36,1) for j in imag)
assert all(conj[:,j]==(-c[:,j] if j in imag else c[:,j]) for j in range(18))
idx=[0,1,2,3,6,7,9,10,12,15,18,19,21,24,25,27,28,33]
cert=Path(__file__).resolve().parents[1]/'h75-operational-metric-descent-20261020'/'H75_Global_Access_18x18_Certificate.csv'
assert cert.exists(),f'parent AX-OA certificate absent: {cert}'
saved=s.Matrix([[R(x) for x in row] for row in csv.reader(cert.open())])
assert saved==c[idx,:]
assert saved.det()!=0
print('H75 PHASE EXACT PASS: rank 18 vs 12, conjugation parity and original 18x18 certificate; G2/G3 OPEN')
