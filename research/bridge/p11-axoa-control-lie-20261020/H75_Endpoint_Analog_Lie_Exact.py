#!/usr/bin/env python3
"""Exact H75 endpoint-vs-analog controllability certificate.

- Source/control endpoints: exact SymPy Gaussian rationals.
- Lie rank: 36 explicit integer-valued iterated brackets.
- Nonzero integer determinant: exact reduction mod prime 1000003.
No floating-point rank assertions, proof assistant, or hardware claims.
"""
import numpy as np
import sympy as sp

I, R = sp.I, sp.Rational
I2, I3, I6 = sp.eye(2), sp.eye(3), sp.eye(6)
def E(a,b):
    return I3[:,a]*I3[b,:]
S=E(0,1)+E(1,0)+E(2,2)
A=E(0,1)-E(1,0)
B=E(2,1)-E(1,2)
W=sp.kronecker_product(
    sp.Matrix([[R(3,5),-R(4,5)],[R(4,5),R(3,5)]]),I3)
F=(sp.kronecker_product(sp.diag(1,0),I3)
   +sp.kronecker_product(sp.diag(0,1),S))
def V(x,y):
    C=(I3+x*A)*(I3-x*A).inv()*(I3+y*B)*(I3-y*B).inv()
    return sp.kronecker_product(I2,C)
VA,VB,VAB=V(R(1,4),0),V(0,R(1,2)),V(R(1,4),R(1,3))
for G in (W,F,VA,VB,VAB):
    assert G.T*G==I6
    assert all(v.is_Rational for v in G)
assert F*F == I6
assert VB == sp.kronecker_product(I2,I3+R(4,5)*B+R(2,5)*B**2)

# Same original non-real H75 four-Kraus source, never a unitary port.
O=sp.Matrix([[R(2,3),R(2,3),-R(1,3)],
             [-R(2,3),R(1,3),-R(2,3)],
             [-R(1,3),R(2,3),R(2,3)]])
U=sp.diag(I,1,I)*O
M=[sp.diag(1,R(3,5),R(3,5)),sp.diag(0,R(4,5),R(4,5))]
K=[sp.kronecker_product(I2[:,a]*I2[b,:],U*M[a])
   for a in range(2) for b in range(2)]
assert sum((k.H*k for k in K),sp.zeros(6))==I6
assert U!=sp.conjugate(U)

# Real and imaginary parts of skew-Hermitian 6x6 Gaussian-integer matrices.
# Coordinates: 15 real upper offdiagonal +21 imaginary upper/diagonal.
zero=lambda: np.zeros((6,6),dtype=np.int64)
jw=zero()
jw[:3,3:]=-np.eye(3,dtype=np.int64)
jw[3:,:3]=np.eye(3,dtype=np.int64)
jf=zero()
jf[3:5,3:5]=np.array([[1,-1],[-1,1]],dtype=np.int64)
jb=zero()
jb[1,2]=-1
jb[2,1]=1
jb[4,5]=-1
jb[5,4]=1
generators=[(jw,zero()),(zero(),jf),(jb,zero())]

def coords(z):
    real,imag=z
    assert np.array_equal(real,-real.T)
    assert np.array_equal(imag,imag.T)
    return [int(real[i,j]) for i in range(6) for j in range(i+1,6)]+[
        int(imag[i,j]) for i in range(6) for j in range(i,6)]

def commutator(z,w):
    a,b=z
    c,d=w
    # All inputs encountered are tiny integer arrays; with bound below,
    # every six-entry matrix product and four-term sum is exactly int64.
    bound=max(int(np.abs(q).max()) for q in (a,b,c,d))
    assert bound < 1000000   # worst product sums < 4*6*(10**6)^2 < 2**63
    return (a@c-b@d-c@a+d@b,a@d+b@c-c@b-d@a)

prime=1000003
mod_echelon={}
def independent(v):
    w=[t%prime for t in v]
    for k in sorted(mod_echelon):
        coeff=w[k]
        if coeff:
            b=mod_echelon[k]
            w=[(x-coeff*y)%prime for x,y in zip(w,b)]
    piv=next((i for i,x in enumerate(w) if x),None)
    if piv is None:
        return False
    mul=pow(w[piv],-1,prime)
    mod_echelon[piv]=[(x*mul)%prime for x in w]
    return True

basis=[]
depth=[]
for x in generators:
    assert independent(coords(x))
    basis.append(x)
    depth.append(1)
i=0
while i<len(basis) and len(basis)<36:
    for g in generators:
        new=commutator(basis[i],g)
        if independent(coords(new)):
            basis.append(new)
            depth.append(depth[i]+1)
            if len(basis)==36:
                break
    i+=1
assert len(basis)==36
assert sorted(mod_echelon)==list(range(36))
assert max(depth)==7
counts=[depth.count(k) for k in range(1,8)]
assert counts==[3,2,5,6,10,7,3]
vectors=[coords(x) for x in basis]
assert max(abs(v) for vec in vectors for v in vec)==16

def det_mod(rows,p):
    a=[[x%p for x in row] for row in rows]
    n=len(a)
    assert n==36 and all(len(row)==36 for row in a)
    d=1
    for col in range(n):
        pivot=next((r for r in range(col,n) if a[r][col]),None)
        assert pivot is not None
        if pivot!=col:
            a[pivot],a[col]=a[col],a[pivot]
            d=(-d)%p
        coeff=a[col][col]
        d=(d*coeff)%p
        inverse=pow(coeff,-1,p)
        for r in range(col+1,n):
            ratio=a[r][col]*inverse%p
            if ratio:
                for c in range(col+1,n):
                    a[r][c]=(a[r][c]-ratio*a[col][c])%p
                a[r][col]=0
    return d

residue=det_mod(vectors,prime)
assert residue==754500
assert residue != 0

print("PASS exact: five original H75 registered endpoints belong to O(6)")
print("PASS exact: original non-real H75 four-Kraus source retained")
print("PASS exact: 36 independent Gaussian-integer brackets at lengths",counts)
print("PASS exact: det(36x36) mod 1000003 =",residue)
print("THEOREM: relative dynamical Lie algebra is full u(6), dimension 36")
print("BOUNDARY: requires independently authorized continuously tunable")
print("          Hamiltonian ports, phase/timing and reset-off scheduling")
