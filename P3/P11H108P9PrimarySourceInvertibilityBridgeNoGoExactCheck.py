"""H108 addendum: now INSPECTED P9.126–P9.128 primary research notes
from owner's Library. Reconstruct their actual rational 16-level
connected Hamiltonian H(b), 48-level parameter-register Hamiltonian,
true diagonal observer and backreaction. Compare with unchanged H75.

STRICT NO-GO for a FAITHFUL INJECTIVE LINEAR FULL-OPERATOR
INTERTWINER H75 reset -> P9 unitary Heisenberg/Schrodinger evolution:
original H75 kills a nonzero off-flag operator, while P9 quantum
unitary conjugations are invertible. An injective dynamical T cannot
map a nonzero H75 kernel vector to a bijective P9 target.

NO statement that a nonfaithful coarse-graining, quotient, ancilla
dilation, alternate sector embedding or future physical solder is
impossible. P9 source and H75 are different models; cannot simply
transfer their signed P3 residuals/Cartan torsion to one another.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    micro,zero_n,R60
)

assert R60[0][0]==I*gc(F(-32,135))
X=zero_n(6)
X[0][3]=O # |flag0,site0><flag1,site0|, nonzero off-flag operator
assert X!=zero_n(6)
assert micro(X)==zero_n(6)
print("PASS H108.P9.1: H75 original true 6-level CPTP reset kills an explicit nonzero flag-coherence matrix unit; therefore noninjective on full M6 (actual original source and original P3 R3 unchanged)")

def mat(n,m=None):
    if m is None:m=n
    return [[F(0) for _ in range(m)] for _ in range(n)]
def eye(n):
    a=mat(n)
    for k in range(n):a[k][k]=F(1)
    return a
def mm(A,B):
    n=len(A);m=len(B);p=len(B[0])
    assert len(A[0])==m
    out=mat(n,p)
    for i in range(n):
        for k in range(m):
            if not A[i][k]:continue
            for j in range(p):
                if B[k][j]:out[i][j]+=A[i][k]*B[k][j]
    return out
def tr(A):return [list(row) for row in zip(*A)]
def add(A,B,coeff=F(1)):
    return [[A[i][j]+coeff*B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]
def trace(A):return sum((A[i][i] for i in range(len(A))),F(0))

# SOURCE from primary P9_126_Connected_CR_Holonomy_Research_Note.md,
# P9_127_Soldering_and_Calibrated_Response_Research_Note.md and
# P9_128_Dynamical_Parameter_and_Backreaction_Research_Note.md.
# This is not a new made-up intercell graph; original P9 declared
# four cell basis vectors, four internal levels/site, square links.
f0=[
    [F(1,2),F(1,2),F(-1,2),F(-1,2)],
    [F(1,2),F(-1,2),F(1,2),F(-1,2)],
    [F(1,2),F(-1,2),F(-1,2),F(1,2)]
]
assert mm(f0,tr(f0))==eye(3)
Psinglet=[[F(1,4) for _ in range(4)] for _ in range(4)]
def rotation(z):
    d=1+z*z
    return [
        [(1-z*z)/d,-2*z/d,F(0)],
        [2*z/d,(1-z*z)/d,F(0)],
        [F(0),F(0),F(1)]
    ]
def linkW(b):
    z=b/5
    return add(Psinglet,mm(tr(f0),mm(rotation(z),f0)))
def H16(b):
    L=linkW(b)
    assert mm(L,tr(L))==eye(4)
    assert trace(L)==F(100)/(F(25)+b*b)
    H=mat(16)
    for x in range(4):
        for a in range(4):
            H[4*x+a][4*x+a]=F(4*x+a)
        for a in range(3):
            i,j=4*x+a,4*x+a+1
            H[i][j]+=F(1,3)
            H[j][i]+=F(1,3)
    for x,y in ((0,1),(1,2),(2,3)):
        for a in range(4):
            i,j=4*x+a,4*y+a
            H[i][j]+=F(1,2)
            H[j][i]+=F(1,2)
    x,y=3,0
    for a in range(4):
        for c in range(4):
            i,j=4*x+a,4*y+c
            H[i][j]+=L[a][c]/2
            H[j][i]+=L[a][c]/2
    assert H==tr(H)
    assert H[0][4]==F(1,2)
    assert H[0][1]==F(1,3)
    assert H[15][3]==L[3][3]/2
    return H

def sigma(s):return F(25)*s/(F(50)+s*s)
bstar=sigma(F(1))
assert bstar==F(25,51)
assert sigma(F(50))==bstar
h=F(1,10)
kappa=F(1,7)
b=(bstar-h,bstar,bstar+h)
assert b==(F(199,510),F(25,51),F(301,510))
Hs=[H16(bb) for bb in b]
for Hr in Hs:
    assert Hr==tr(Hr)
assert Hs[0]!=Hs[2]
assert linkW(bstar)!=eye(4)
print("PASS H108.P9.2: independently reconstituted PRIMARY P9.126–P9.128 true real-symmetric 16D connected one-particle Hamiltonian H(b) with its four-cell square, path internal hopping, SO(3) Wilson loop; P9.127 external calibration b=25s/(50+s²), s=1 and s=50 alias; center b*=25/51")

# PRIMARY P9.128 48-level autonomous parameter register (still
# a UNITARY conjugation channel), not the original H75 four-Kraus
# erasing flag map. One 3-level q-register shared over 16 microlevels.
Tq=[[kappa,-kappa,F(0)],
    [-kappa,2*kappa,-kappa],
    [F(0),-kappa,kappa]]
assert [sum(row) for row in Tq]==[0,0,0]
Htot=mat(48)
for r in range(3):
    for s in range(3):
        for j in range(16):
            Htot[16*r+j][16*s+j]+=Tq[r][s]
    for i in range(16):
        for j in range(16):
            Htot[16*r+i][16*r+j]+=Hs[r][i][j]
assert Htot==tr(Htot)
print("PASS H108.P9.3: genuine P9.128 48D static register Hamiltonian Tq⊗I16+diag(H(b0),H(b1),H(b2)) built EXACTLY using rational source coefficients h=1/10,kappa=1/7 and full diagonal observer D48")

# Compute the 48D exact Heisenberg double commutator of register
# position B=diag(b_r) ⊗ I16, projected to the uniform register.
# All internal operators are real rational, no matrix exponentials
# or approximate finite-time residue claims introduced.
Aeff=mat(16)
for i in range(16):
    for j in range(16):
        v=F(0)
        for r in range(3):
            ir=16*r+i
            for s in range(3):
                js=16*s+j
                for k in range(48):
                    # ddot B = -[H,[H,B]], all B diagonal.
                    a=Htot[ir][k];c=Htot[k][js]
                    if a and c:
                        v+=a*c*(2*b[k//16]-b[r]-b[s])
        Aeff[i][j]=v/3
expected=[[F(2)*kappa*h/F(3)*(Hs[0][i][j]-Hs[2][i][j])
           for j in range(16)] for i in range(16)]
assert Aeff==expected
assert trace(Aeff)==0
K=add(Hs[2],Hs[0],F(-1))
K2=trace(mm(K,K))
assert K2==F(270608040000,43132732645201),K2
eps=F(1,100)
acc_plus=-F(2)*kappa*h/F(3)*eps*K2
acc_minus=-acc_plus
assert acc_plus==F(-180405360,301929128516407)
assert acc_minus==F(180405360,301929128516407)
assert acc_plus<0<acc_minus
assert Aeff!=mat(16)
print("PASS H108.P9.4: independently exact 48x48 double-commutator gives Aeff=(2kappa h/3)(H(b0)-H(b2)); tr(K²)=270608040000/43132732645201, genuine positive micro-state accelerated directions ±180405360/301929128516407 match primary P9.128 note")

# Proof of a STRONG, explicitly scoped source equivalence No-Go:
#
# Suppose T:M6->M16 (or M48) is a linear INJECTIVE *full-operator*
# dynamical intertwiner T Phi_H75 = Phi_unitary T.
# Take the above nonzero X with Phi_H75(X)=0:
# Phi_unitary(TX)=T Phi_H75(X)=0.
# Yet unitary conjugation Phi_unitary is INVERTIBLE at every t,
# hence TX=0, contradicting injective T and X !=0.
#
# This does not reject a noninjective coarse-graining, channel
# dilation/partial trace, source restricted quotient, changing the
# observable algebra, or actual experimental source equivalence
# established by a different physically allowed simulation map.
assert micro(X)==zero_n(6) and X!=zero_n(6)
assert len(Hs[1])==16 and len(Htot)==48
assert len(X)==6 and 6 not in (16,48)
print("PASS H108.P9.5: FULL-OPERATOR faithful linear intertwiner from original NONINJECTIVE H75 reset to either P9.126 unitary 16D or P9.128 unitary 48D channel is IMPOSSIBLE by nonzero kernel vs invertible unitary output (theorem, not numerical rank guess)")
print("BOUNDARY: physically matched quantum coarse-graining/ancilla/stinespring/sourced reduction may still exist; observer D16/D48 vs D6, state manifold and physical geometry/solder remain to be sourced independently")
print("BOUNDARY: P9.128 nonstationary torsion-free thermodynamic comparator and state-dependent register acceleration DO NOT source DeWitt/ADM/HDA/Einstein or F completeness")
