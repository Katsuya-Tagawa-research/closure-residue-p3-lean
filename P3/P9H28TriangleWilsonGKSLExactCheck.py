"""H28: exact three-site gauge-flux population-jet readout with GKSL control.

All coefficients are exact rational-Gaussian arithmetic (no floats).
The independently phase-calibrated loop knob and CR graph provenance
are DECLARED conditions, not consequences of P3/P6 accessibility.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C, gc, I, O, Z0
from math import factorial

N=3
def mz():return [[Z0 for _ in range(N)] for _ in range(N)]
def eye():return [[O if i==j else Z0 for j in range(N)] for i in range(N)]
def adj(A):return [[A[j][i].conj() for j in range(N)] for i in range(N)]
def add(A,B):return [[A[i][j]+B[i][j] for j in range(N)] for i in range(N)]
def scale(A,s):return [[A[i][j]*s for j in range(N)] for i in range(N)]
def sub(A,B):return add(A,scale(B,-1))
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(N)),Z0)
             for j in range(N)] for i in range(N)]
def comm(A,B):return sub(mm(A,B),mm(B,A))
def Delta(A):return [[A[i][j] if i==j else Z0 for j in range(N)] for i in range(N)]
def off(A):return sub(A,Delta(A))
def tr(A):return sum((A[i][i] for i in range(N)),Z0)
def norm2(z):return z*z.conj()

def H_of(a,b,q):
    a=gc(a);b=gc(b);q=gc(q)
    return [[Z0,a,q.conj()],[a,Z0,b],[q,b,Z0]]

def L_of(H,rho,gamma):
    # Standard GKSL uniform site dephasing:
    # -i[H,rho] + gamma*(Delta(rho)-rho).
    return sub(scale(comm(H,rho),-I),scale(off(rho),gc(gamma)))

E0=mz();E0[0][0]=O
def population_jets(H,gamma,degree=5):
    R=E0
    out=[]
    for k in range(degree+1):
        out.append(tuple(R[i][i] for i in range(N)))
        if k<degree:R=scale(L_of(H,R,gamma),F(1,k+1))
    return out

a=F(1);b=F(1)
q=C(F(3,5),F(4,5))
lam=(O,I,-O,-I)
assert norm2(q)==O
def W(H):return H[0][1]*H[1][2]*H[2][0]
def test_formula(aa,bb,qq,gamma):
    H=H_of(aa,bb,qq)
    assert adj(H)==H and Delta(H)==mz()
    jets=population_jets(H,gamma,5)
    assert jets[0]==(O,Z0,Z0) and jets[1]==(Z0,Z0,Z0)
    qnorm=norm2(qq);imW=W(H).i
    assert W(H)==gc(aa)*gc(bb)*qq
    assert jets[2][0]==gc(-(aa*aa+qnorm.r))
    assert jets[2][1]==gc(aa*aa)
    assert jets[2][2]==qnorm
    assert jets[3][1]==gc(aa*bb*imW/(aa*bb)-gamma*aa*aa/3)
    assert jets[3][2]==gc(-aa*bb*imW/(aa*bb)-gamma*qnorm.r/3)
    assert jets[3][0]==gc(gamma*(aa*aa+qnorm.r)/3)
    assert all(sum(jet,Z0)==Z0 for jet in jets[1:])
    assert jets[3][1]-jets[3][2]==gc(2*imW-gamma*(aa*aa-qnorm.r)/3)
    return jets

for qq in (q,q.conj(),I*q,-I*q,-q):
    for gamma in (F(0),F(2,3)):
        test_formula(a,b,qq,gamma)
# For arbitrary positive real a,b: cubic chiral population = Im W,
# not merely Im(q).
for aa,bb in ((F(2,3),F(5,4)),(F(3,2),F(2))):
    for gamma in (F(0),F(2,3)):
        test_formula(aa,bb,q,gamma)

# Gauge invariance of the Wilson product under arbitrary independent
# rational unit phases on the three sites.
phases=(O,C(F(3,5),F(4,5)),C(F(5,13),F(12,13)))
assert all(norm2(z)==O for z in phases)
H=H_of(a,b,q)
Hg=[[phases[i]*H[i][j]*phases[j].conj() for j in range(N)] for i in range(N)]
assert W(Hg)==W(H)
assert population_jets(Hg,F(2,3),5)==population_jets(H,F(2,3),5)

# Two phase settings recover sine/cosine components of a Wilson loop
# from the cubic *time* population coefficient with calibrated amplitudes.
# Four +/- settings cancel any phase-independent dephasing background,
# without requiring a numerical gamma value.
gamma=F(2,3)
def cubic(l):return population_jets(H_of(a,b,l*q),gamma,3)[3][1]
im=(cubic(O)-cubic(-O))/gc(2*a*b)
re=(cubic(I)-cubic(-I))/gc(2*a*b)
assert im==gc(q.i) and re==gc(q.r)
assert im==gc(F(4,5)) and re==gc(F(3,5))
# p'''(0)=6*cubic: divide the paired p''' differences by 12ab.
assert 6*(cubic(O)-cubic(-O))/gc(12*a*b)==gc(q.i)
assert 6*(cubic(I)-cubic(-I))/gc(12*a*b)==gc(q.r)
assert all(population_jets(H_of(a,b,l*q),gamma,2)[2]
           ==population_jets(H,gamma,2)[2] for l in lam)
assert cubic(O)!=cubic(q.conj()/q)
# Opposite Wilson chirality has identical first two population jets.
assert population_jets(H_of(a,b,q),gamma,2)==population_jets(
    H_of(a,b,q.conj()),gamma,2)
assert population_jets(H_of(a,b,q),gamma,3)[3][1]!=population_jets(
    H_of(a,b,q.conj()),gamma,3)[3][1]

# No triangle: tree (edge 02 removed) has no Wilson loop and
# no flux-odd cubic response, even with site dephasing.
tree=H_of(a,b,Z0)
assert W(tree)==Z0
assert population_jets(tree,gamma,3)[3][1]==gc(-gamma*a*a/3)

# Local P6-style first-residue selection, with a PREDECLARED maximal
# complex edge-operator microscopic sector containing H for all phases:
# K=-iH is anti-Hermitian and zero diagonal; Xi(K/2)=K.
# This proves a scope-conditional algebraic compatibility only.
for l in lam:
    h=H_of(a,b,l*q)
    K=scale(h,-I)
    assert adj(K)==scale(K,-1)
    assert Delta(K)==mz()
    J=scale(K,F(1,2))
    assert off(sub(J,adj(J)))==K
    assert Delta(comm(K,E0))==mz()

# Explicit negative boundary: if physical hopping controls are real,
# the imaginary Wilson invariant always vanishes. Phase extension is
# a strictly extra control assumption.
real=H_of(a,b,gc(F(3,5)))
assert W(real).i==0
assert population_jets(real,F(0),3)[3][1]==Z0

print("PASS H28: rational three-site Hermitian exchange plus GKSL dephasing")
print("PASS H28: cubic population chirality = Im(H01 H12 H20)")
print("PASS H28: gauge-invariant Wilson loop and phase-conjugate second-jet ambiguity")
print("PASS H28: +/-0 and +/-pi/2 phase scans recover both Wilson quadratures")
print("PASS H28: four-setting antisymmetrization cancels shared dephasing")
print("PASS H28: declared full-edge Xi sector contains phase-modulated coherent controls")
print("SCOPE: intercell phase knob and P6 physical access are extra calibrated conditions")
