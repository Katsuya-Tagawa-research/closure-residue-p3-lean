"""H65 exact phase-source gate: tree gauge vs cycle flux and signed chirality.

Original H32 finite P3 hidden operators transform covariantly under a
declared diagonal-unitary change of basis, while diagonal observations
are unchanged if states, controls, and instruments transform together.
A path's hopping phases are gauge-removable; an added complex triangle
chord carries gauge-invariant loop flux and a third-order population
chirality witness. This conventional QM witness is not a frozen-P6
physical control, an inherited P3 J_N, or a CR-exclusive phenomenon.

Pure Gaussian-Fraction computations with exact certified positive time.
"""
from fractions import Fraction as F
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    C,gc,I,O,Z0,N,z,eye,unit,add,sub,scale,mm,dagger,com,
    diag,hidden,trace,rr,Phi,H,image,xi
)
assert N==3
def adjG(M,U):return mm(mm(U,M),dagger(U))
def check_unit(U):return mm(dagger(U),U)==eye()
def transpose(M):
    return [[M[j][i] for j in range(N)] for i in range(N)]
def phase_loop(M):
    return M[0][1]*M[1][2]*M[2][0]

G=eye();G[1][1]=I
assert check_unit(G)
def gauged(M):return adjG(M,G)
def ungauged(M):return adjG(M,dagger(G))
def PhiG(M):return gauged(Phi(ungauged(M)))
for i in range(N):
    for j in range(N):
        M=unit(i,j)
        assert PhiG(gauged(M))==gauged(Phi(M))
        assert diag(gauged(M))==diag(M)
        assert hidden(gauged(M))==gauged(hidden(M))
        assert xi(gauged(M))==gauged(xi(M))

for seed in range(N):
    original=unit(seed,seed)
    transformed=gauged(original)
    for depth in range(1,9):
        original=Phi(original)
        transformed=PhiG(transformed)
        assert transformed==gauged(original)
        assert diag(transformed)==diag(original)
for depth in (1,2,3):
    for seed in (0,1):
        state=unit(seed,seed)
        for _ in range(depth):state=PhiG(state)
        assert hidden(state)==gauged(H[depth][seed])
assert rr(image(3))==6
assert rr([gauged(v) for v in image(3)])==6
print("PASS H65: H32 original-P3 Krylov Xi, hidden return and 9-unit CPTP channel all exactly diagonal-gauge covariant")

# An apparent pure-imaginary 'odd control' can be a coordinate
# rotation of a real P6-path exchange when the apparatus and states
# are transformed coherently. No independent physical X/Y standard
# is supplied by that coordinate change.
A01=sub(unit(0,1),unit(1,0))
B12=sub(unit(2,1),unit(1,2))
X01=add(unit(0,1),unit(1,0))
X12=add(unit(1,2),unit(2,1))
assert gauged(A01)==scale(X01,-I)
assert gauged(B12)==scale(X12,-I)
assert transpose(gauged(A01))==gauged(A01)
assert transpose(gauged(B12))==gauged(B12)
print("PASS H65: tree path real exchange becomes imaginary-symmetric under diagonal unitary, not a new physical knob")

# The entire triangle of an explicitly enlarged Hermitian hopping
# Hamiltonian carries a non-removable oriented flux. Here
# H01=1,H12=1,H20=i; Hermiticity supplies reverse edges.
chiral=z()
chiral[0][1]=O;chiral[1][0]=O
chiral[1][2]=O;chiral[2][1]=O
chiral[2][0]=I;chiral[0][2]=-I
assert dagger(chiral)==chiral
flux=phase_loop(chiral)
assert flux==I
assert phase_loop(gauged(chiral))==I
# Real-valued edge phases would force a real loop product,
# contradicting the invariant imaginary value +i.
assert flux.i==F(1) and flux.r==0
print("PASS H65: non-real triangular Wilson loop flux is diagonal-gauge invariant, unlike path edge phases")

# Exact analytical t^2/t^3 population coefficients under
# exp(-it H) |0>, via a_j(t)=-it H_j0 - t^2 (H^2)_j0/2+O(t^3).
H2=mm(chiral,chiral)
coeff={}
for j in (1,2):
    a1=(-I)*chiral[j][0]
    a2=gc(F(-1,2))*H2[j][0]
    c2=a1*a1.conj()
    c3=a1*a2.conj()+a2*a1.conj()
    coeff[j]=(c2,c3)
# Opposite signed odd-time coefficients on the two output sites.
assert coeff[1]==(gc(1),gc(1))
assert coeff[2]==(gc(1),gc(-1))
assert coeff[1][1]-coeff[2][1]==gc(2)
# Certified finite positive physical time, using ||H||op<=2
# (Hermitian, row sum 2), ||-i ad_H||_{1->1}<=4,
# per-observable fourth+ Taylor remainder
# <=(4t)^4/[24(1-4t)] for t<1/4.
t=F(1,100)
signal=F(2)*t**3
tail=F(2)*(4*t)**4/(F(24)*(1-4*t))
assert signal>tail>0
print("PASS H65: genuine Hermitian 3-cycle chiral population difference =2t^3+O(t^4); rigorously positive at t=1/100")
print("PASS H65: distinguish path-gauge convention from gauge-invariant cycle flux; loop/chord is EXTRA beyond frozen P6")
print("BOUNDARY: ordinary QM only; no independent microscopic P3 to physical P6 sourced map, odd hardware, absolute phase, or GR")
