"""H24 exact finite bridge: nonzero original P3 residue -> diagonal gauge holonomy.

Pure Python fractions; rational Gaussian integers represented exactly.
The microscopic P6 sector/control permissions are not assumed inherited.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial

@dataclass(frozen=True)
class C:
    r: F = F(0)
    i: F = F(0)
    def __add__(self,y):
        y=gc(y); return C(self.r+y.r,self.i+y.i)
    __radd__=__add__
    def __neg__(self): return C(-self.r,-self.i)
    def __sub__(self,y): return self+-gc(y)
    def __rsub__(self,y): return gc(y)+-self
    def __mul__(self,y):
        y=gc(y)
        return C(self.r*y.r-self.i*y.i,self.r*y.i+self.i*y.r)
    __rmul__=__mul__
    def conj(self): return C(self.r,-self.i)
    def __truediv__(self,y):
        y=gc(y)
        d=y.r*y.r+y.i*y.i
        return C((self.r*y.r+self.i*y.i)/d,
                 (self.i*y.r-self.r*y.i)/d)
def gc(x):
    return x if isinstance(x,C) else C(F(x),F(0))
I=C(F(0),F(1))
O=gc(1); Z0=gc(0)
def mzero(): return [[Z0,Z0],[Z0,Z0]]
def eye(): return [[O,Z0],[Z0,O]]
def plus(a,b): return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
def scale(a,x): return [[x*a[i][j] for j in range(2)] for i in range(2)]
def minus(a,b): return plus(a,scale(b,-1))
def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(2)),Z0)
             for j in range(2)] for i in range(2)]
def dagger(a): return [[a[j][i].conj() for j in range(2)] for i in range(2)]
def com(a,b): return minus(mm(a,b),mm(b,a))
def diag(x,y): return [[gc(x),Z0],[Z0,gc(y)]]
def hidden(a): return [[Z0,a[0][1]],[a[1][0],Z0]]

U=[[C(F(1,3),F(-2,3)),C(F(0),F(-2,3))],
   [C(F(0),F(-2,3)),C(F(1,3),F(2,3))]]
assert mm(dagger(U),U)==eye()
def phi(a): return mm(mm(U,a),dagger(U))
Z=diag(1,-1)
z1=hidden(phi(Z))
z2=hidden(phi(phi(Z)))
assert z1==[[Z0,C(F(8,9),F(4,9))],
           [C(F(8,9),F(-4,9)),Z0]]
assert z2==[[Z0,C(F(32,81),F(-56,81))],
           [C(F(32,81),F(56,81)),Z0]]
assert dagger(z1)==z1 and dagger(z2)==z2
R=com(z1,dagger(z2))
assert R==diag(C(0,F(128,81)),C(0,F(-128,81)))
# A nonzero determinant proves z1,z2 span the entire 2D complex
# offdiagonal sector. H1 is C*z1; H2 is the full offdiagonal sector.
det=z1[0][1]*z2[1][0]-z2[0][1]*z1[1][0]
assert det==C(0,F(128,81))
assert com(z1,dagger(z1))==mzero()
# Original P3 R_2=0 and R_3=D_2^0, for depth i+j<=k.

K1=scale(z1,I); K2=scale(z2,I)
assert dagger(K1)==scale(K1,-1)
assert dagger(K2)==scale(K2,-1)
B=com(K1,K2)
assert B==scale(R,-1)
assert B[0][1]==Z0 and B[1][0]==Z0
assert com(B,diag(1,0))==mzero()
assert com(B,K1)!=mzero()
assert com(B,K1)[0][0]==Z0 and com(B,K1)[1][1]==Z0
# The diagonal gauge N=span_R(iZ) is not an ideal in the
# dynamically generated su(2) Lie algebra.

# P6 Xi(J)=(1-Delta)(J-J^*), with a separately DECLARED complex
# microscopic sector J containing i*z1/2, i*z2/2.
for z,k in ((z1,K1),(z2,K2)):
    j=scale(z,I/2)
    assert hidden(minus(j,dagger(j)))==k

# Exact polynomial commutator loop in pulse amplitude eps.
DEG=6
def pmul(a,b):
    out=[mzero() for _ in range(DEG+1)]
    for i in range(DEG+1):
        for j in range(DEG+1-i):
            out[i+j]=plus(out[i+j],mm(a[i],b[j]))
    return out
def pexp(a,sgn):
    out=[]
    power=eye()
    for k in range(DEG+1):
        out.append(scale(power,F(sgn**k,factorial(k))))
        power=mm(power,a)
    return out
def pdag(a): return [dagger(x) for x in a]
def emb(a): return [a]+[mzero() for _ in range(DEG)]
loop=pexp(K1,1)
for a,sgn in ((K2,1),(K1,-1),(K2,-1)):
    loop=pmul(loop,pexp(a,sgn))
assert loop[0]==eye() and loop[1]==mzero() and loop[2]==B
E00=diag(1,0)
Dout=pmul(pmul(loop,emb(E00)),pdag(loop))
assert all(Dout[k][i][i]==Z0 for k in range(1,6) for i in range(2))
c6=F(183762944,43046721)
assert Dout[6][0][0]==gc(-c6) and Dout[6][1][1]==gc(c6)
assert Dout[3][0][1]==C(F(13312,6561),F(-2560,6561))
# In contrast, a coherent prepared state sees diagonal-gauge
# commutator action already at order eps^2.
X=[[Z0,O],[O,Z0]]
rho_plus=scale(plus(eye(),X),F(1,2))
coh=pmul(pmul(loop,emb(rho_plus)),pdag(loop))
assert coh[2]==com(B,rho_plus)
assert coh[2][0][1]==C(0,F(-128,81))
assert coh[2][1][0]==C(0,F(128,81))
assert all(coh[2][i][i]==Z0 for i in range(2))
# Each exact exp(eps*K_j) is unitary: K_j^*=-K_j.
print("PASS H24: explicit rational Gaussian U is unitary/CPTP")
print("PASS H24: original P3 R2=0, R3=D_2^0, residue=128i Z/81")
print("PASS H24: [i*z1,i*z2]=-R lies in diagonal gauge")
print("PASS H24: gauge kernel in generated su2 is nonideal")
print("PASS H24: chosen Xi sector conditionally realizes both controls")
print("PASS H24: holonomy coherence starts eps2; diagonal population eps6")
print("Scope: internal U(2)/T2 gauge holonomy, no P6 physical provenance or LC curvature")
