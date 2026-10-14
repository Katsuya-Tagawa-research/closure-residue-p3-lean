"""H31 exact P3-to-P6 microscopic sector provenance gate.

An actual 3-site unitary CPTP channel contains the H24 original-P3 nonzero
quadratic residue, but its independently EXTRACTED Krylov hidden space has
only one-edge support. Only an EXTRA predeclared microscopic 12-edge
operator enlarges the Xi image and Lie closure to su(3).

All calculations use exact Gaussian rationals. The illustrative choice
J_micro=H2 of P3 is a conditional microscopic-sector assignment, not a
claim that the independently frozen P6 J_N equals this Krylov space.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import (
    C, gc, I, O, Z0, U, z1, z2, R
)

N=3
def zeros():return [[Z0 for j in range(N)] for i in range(N)]
def matunit(a,b):
    a0=zeros();a0[a][b]=O;return a0
def diagvec(values):
    a=zeros()
    for i,v in enumerate(values):a[i][i]=gc(v)
    return a
def add(a,b):return [[a[i][j]+b[i][j] for j in range(N)] for i in range(N)]
def scale(a,c):return [[a[i][j]*c for j in range(N)] for i in range(N)]
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(N)),Z0)
              for j in range(N)] for i in range(N)]
def dagger(a):return [[a[j][i].conj() for j in range(N)] for i in range(N)]
def bracket(a,b):return sub(mul(a,b),mul(b,a))
def d(a):return [[a[i][j] if i==j else Z0 for j in range(N)] for i in range(N)]
def q(a):return sub(a,d(a))
def xi(a):return q(sub(a,dagger(a)))
def tr(a):return sum((a[i][i] for i in range(N)),Z0)
def embed2(a):
    b=zeros()
    for i in range(2):
        for j in range(2): b[i][j]=a[i][j]
    return b
def vec(a):
    return [a[i][j].r for i in range(N) for j in range(N)]+[
            a[i][j].i for i in range(N) for j in range(N)]
def rank(mats):
    if not mats:return 0
    m=[[v[k] for v in [vec(a) for a in mats]]
       for k in range(2*N*N)]
    p=0
    for col in range(len(mats)):
        idx=next((j for j in range(p,len(m)) if m[j][col]!=0),None)
        if idx is None:continue
        m[p],m[idx]=m[idx],m[p]
        val=m[p][col];m[p]=[u/val for u in m[p]]
        for j in range(len(m)):
            if j!=p and m[j][col]:
                f=m[j][col]
                m[j]=[u-f*v for u,v in zip(m[j],m[p])]
        p+=1
        if p==len(m):break
    return p
def lie_closure(primitives):
    basis=[]
    for a in primitives:
        if rank(basis+[a])>len(basis):basis.append(a)
    for depth in range(12):
        old=basis[:]
        for a in old:
            for b in old:
                c=bracket(a,b)
                if rank(basis+[c])>len(basis):basis.append(c)
        if len(basis)==len(old):return basis
    raise AssertionError("finite Lie closure did not stabilize")
def supported(a,allowed):
    return all(i==j or frozenset((i,j)) in allowed or a[i][j]==Z0
               for i in range(N) for j in range(N))
def hilbert_schmidt_anti(k):
    return dagger(k)==scale(k,-1) and tr(k)==Z0

# U3 is an actual unitary microscopic CPTP model, with spectator |2>.
U3=add(embed2(U),matunit(2,2))
I3=diagvec((1,1,1))
assert mul(dagger(U3),U3)==I3
def Phi(a):return mul(mul(U3,a),dagger(U3))
Z3=diagvec((1,-1,0))
h1=q(Phi(Z3))
h2=q(Phi(Phi(Z3)))
assert h1==embed2(z1) and h2==embed2(z2)
assert rank([h1,h2])==2
assert rank([h1,scale(h1,I),h2,scale(h2,I)])==4
P3_res=d(bracket(h1,dagger(h2)))
assert P3_res==embed2(R)
assert P3_res==diagvec((C(F(0),F(128,81)),
                         C(F(0),F(-128,81)),0))
assert d(bracket(h1,dagger(h1)))==zeros()
assert tr(P3_res)==Z0 and P3_res!=zeros()
assert supported(P3_res,{frozenset((0,1))})

# Fix a *specific* microscopic candidate J_base = span_C{h1,h2},
# exactly the complex P3 hidden Krylov sector at depth <=2.
# Xi image over R is span_R{i*h1,i*h2} (rank two).
K1=xi(scale(h1,I/F(2)))
K2=xi(scale(h2,I/F(2)))
assert K1==scale(h1,I) and K2==scale(h2,I)
assert rank([K1,K2])==2
A01=sub(matunit(0,1),matunit(1,0))
Q01=scale(add(matunit(0,1),matunit(1,0)),-I)
B12=sub(matunit(2,1),matunit(1,2))
for k in (A01,Q01,B12,K1,K2):
    assert hilbert_schmidt_anti(k)
assert rank([K1,K2,A01,Q01])==2
assert rank([K1,K2,B12])==3
allowed={frozenset((0,1))}
assert all(supported(k,allowed) for k in (K1,K2,A01,Q01))
assert not supported(B12,allowed)
assert xi(scale(B12,F(1,2)))==B12

Lbase=lie_closure([K1,K2])
assert len(Lbase)==3 and rank(Lbase)==3
assert all(supported(k,allowed) for k in Lbase)
assert all(hilbert_schmidt_anti(k) for k in Lbase)
assert P3_res==scale(bracket(K1,K2),-1)

# A genuine *independent* microscopic extension J_aug =
# J_base + span_C{B12/2} adds one real Xi edge direction.
# It is not supplied by this block-diagonal CPTP Krylov sector.
Laug=lie_closure([K1,K2,B12])
assert len(Laug)==8 and rank(Laug)==8
assert all(hilbert_schmidt_anti(k) for k in Laug)
# su(3) has real dimension 8; thus full su3 accessibility is
# algebraically possible only after independently adding B12.
assert rank(Laug+[A01,Q01,B12])==8
A02=sub(matunit(0,2),matunit(2,0))
Q02=scale(add(matunit(0,2),matunit(2,0)),-I)
assert rank(Laug+[A02,Q02])==8

# Distinguish the original P6 physical TWO REAL PATH directions:
# J_P6path supports both 01 and 12 real exchange but *not* Q01.
# J_base supplies the complex 01 edge but no 12 edge. Neither
# inclusion follows from the other without independent provenance.
assert rank([A01,B12])==2
assert rank([A01,B12,Q01])==3
assert rank([K1,K2,B12])==3
assert rank([K1,K2,A01,Q01])==2

print("PASS H31: embedded 3-site unitary CPTP retains original P3 depth-three residue")
print("PASS H31: its extracted P3 H2 has one-edge support and Xi image rank two")
print("PASS H31: nonzero P3 residue generates only local su2, not connected su3")
print("PASS H31: independent 12-edge microscopic lift extends Xi and Lie closure to su3")
print("PASS H31: P6 two-real-path sector and H24 complex-one-edge sector are distinct")
print("SCOPE: choice J_micro=H2 is a conditional candidate, not frozen P6 provenance")
