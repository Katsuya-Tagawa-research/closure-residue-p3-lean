"""H108: exact universal SEPARABLE upper bound on a POSITIVE effect
for unchanged ORIGINAL H75×H75 36D physical output, and a conditional
H105 link state violating it. No newly assumed Hamiltonian.

W=(|eta><eta|)^T_site2 for eta=(|1,1>+i|2,0>)/sqrt2.
Every separable positive sigma has Tr(W sigma)>=0. W is Hermitian
with W^3=W/4 -> eigenvalues in {0, +/-1/2}; Q=I/2-W is a
legitimate positive POVM effect and separability implies p(Q)<=1/2.
Original flag00 p=153/625. Separably prepared source native gives
p_native(Q|00)=25/68; independently EXTRA H105 entangling link gives
p_link(Q|00)=1369/1700 > 1/2; trace-distance lower bound
D(link_conditional, ANY separable normalized output)>=519/1700.

The original link is NOT a permitted native H75 Hamiltonian.
This is NOT physical Einstein gravity, independent Cartan
connection, a CR-exclusive test or a lab measurement.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import R60
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P11H105TwoCellConditionalCoherentCanonicalTransportExactCheck as H105
import P11H106LocalOnlySeparabilityVsLinkEntanglementExactCheck as H106
import P11H107TypedP9P11GenerativeHandoffPositivePhaseReadoutExactCheck as H107

assert R60[0][0]==I*gc(F(-32,135))
assert H106.p==F(153,625)
assert H106.minor.r==F(-2916,390625)
assert H106.prob_link==H106.prob_native
assert H106.norm_det==F(6,17)
assert H107.native_effect==F(153,1250)
assert H107.link_effect==F(9,250)
print("PASS H108.0: unchanged genuine H75 x H75 output, native product and H105 EXTRA link inputs with identical ALL coarse flags; H106 NPT and H107 general phase-correlation witnesses preserved")

zero=Z0
I9=H91.eye(9) if hasattr(H91,'eye') else H105.I9
I36=H91.eye(36) if hasattr(H91,'eye') else [[gc(int(i==j)) for j in range(36)] for i in range(36)]
eta=[Z0 for _ in range(9)]
eta[4]=O
eta[6]=I
# norm |eta> is sqrt(2); eta eta^dag /2 is an exact
# normalized rank-one projector with no irrational matrix entries.
Pi=[[eta[i]*eta[j].conj()*gc(F(1,2)) for j in range(9)]
    for i in range(9)]
assert H91.mm(Pi,Pi)==Pi and H91.tr(Pi)==O
assert H91.dag(Pi)==Pi
W=H106.partial_transpose_second(Pi)
assert H91.dag(W)==W
assert H91.mm(H91.mm(W,W),W)==H91.scale(W,F(1,4))
assert W[4][4]==gc(F(1,2))
assert W[6][6]==gc(F(1,2))
assert W[3][7]==-I*gc(F(1,2))
assert W[7][3]==I*gc(F(1,2))
# W eigenvalues in {1/2,0,-1/2} from Hermitian cubic.
# All possible nonzero entries are either:
#  diagonal 4,6 = +1/2; offdiag 3,7 = +/-i/2.
# Hence ||W||_infty=1/2. This directly certifies
# 0<=Q=I/2-W<=I9 from the spectral cubic.
Q=H91.minus(H91.scale(I9,F(1,2)),W)
assert H91.dag(Q)==Q
assert H91.mm(H91.mm(Q,H91.minus(H91.scale(Q,2),I9)),
               H91.minus(Q,I9))==H105.ZERO9
assert Q[4][4]==Z0 and Q[6][6]==Z0
assert Q[3][3]==gc(F(1,2)) and Q[7][7]==gc(F(1,2))
print("PASS H108.1: exact decomposable entanglement witness W=(|eta><eta|)^T2 has W^3=W/4, ||W||inf=1/2; Q=I9/2-W is mathematically bona fide positive POVM, universal separable p(Q)<=1/2")

# A local-measurement reconstruction:
# W=1/2(P1⊗P1+P2⊗P0)
#   +1/4(Y12⊗X01 + X12⊗Y01).
# No nonlocal entangling *detector* is needed to estimate its
# statistics if separately calibrated local site X/Y and
# population detectors are independently accessible.
P0=H91.e(3,0,0)
P1=H91.e(3,1,1)
P2=H91.e(3,2,2)
X01=H91.hermX(3,0,1)
Y01=H91.hermY(3,0,1)
X12=H105.X
Y12=H105.Y
local_w=H91.plus(
    H91.scale(H91.plus(H105.kron(P1,P1),H105.kron(P2,P0)),F(1,2)),
    H91.scale(H91.plus(H105.kron(Y12,X01),H105.kron(X12,Y01)),F(1,4))
)
assert local_w==W
print("PASS H108.2: exact local detector decomposition W=1/2(P1⊗P1+P2⊗P0)+1/4(Y12⊗X01+X12⊗Y01) matches ALL 81 entries; calibration remains additional operational premise")

def val(X):
    z=H91.tr(X)
    assert z.i==0
    return z.r
def born(E,s):
    return val(H91.mm(E,s))
native_W=born(W,H106.sigi)
linked_W=born(W,H106.sig)
assert native_W==F(81,2500),native_W
assert linked_W==F(-4671,62500),linked_W
native_Q=born(Q,H106.sigi)
linked_Q=born(Q,H106.sig)
assert native_Q==F(9,100),native_Q
assert linked_Q==F(12321,62500),linked_Q
assert native_Q/H106.p==F(25,68)
assert linked_Q/H106.p==F(1369,1700)
assert linked_Q/H106.p-F(1,2)==F(519,1700)
assert linked_Q-native_Q==F(1674,15625)
assert 0<=native_Q<=H106.p and 0<=linked_Q<=H106.p
assert native_Q/H106.p<=F(1,2) and linked_Q/H106.p>F(1,2)
print("PASS H108.3: original genuine H75 flag00 native separable W=81/2500 and Q=9/100 (conditional 25/68), conditional H105 link W=-4671/62500 and Q=12321/62500 (conditional 1369/1700); link violates universal separable bound by 519/1700")

# Independent two-index computation from physical original flag00
# positive output partial transpose: principal block indices4,6.
pt=H106.pt
assert pt[4][4]==gc(F(729,31250))
assert pt[6][6]==Z0
assert pt[4][6]==I*gc(F(54,625))
assert pt[6][4]==-I*gc(F(54,625))
analytic=(pt[4][4].r+pt[6][6].r)/2-F(54,625)
assert analytic==linked_W
assert H106.minor.r==pt[4][4].r*pt[6][6].r-F(54,625)**2
# Separable source's strictly positive W expectation is correct;
# the original H107 unrelated phase detector had native 153/1250.
assert H106.sigi[4][4]==gc(F(81,1250))
assert native_W==H106.sigi[4][4].r/2
print("PASS H108.3: independent analytic 2x2 original H106 partial-transpose subblock and native site population reproduce BOTH witness expectations without numerical diagonalization")

# Physically correct REAL output two-flag (4) and two-site (9)
# 36D source POVM with actual original U⊗U after Kraus attenuation.
cal=H91.mm(H91.mm(H105.U2,Q),H91.dag(H105.U2))
E=[[Z0 for _ in range(36)] for _ in range(36)]
for i in range(9):
    for j in range(9):
        E[i][j]=cal[i][j]
assert H91.dag(E)==E
assert H91.tr(E).i==0
assert E[9][9]==E[35][35]==Z0
for sig,q in ((H106.sigi,native_Q),(H106.sig,linked_Q)):
    true_output_branch=H91.mm(H91.mm(H105.U2,sig),H91.dag(H105.U2))
    assert born(cal,true_output_branch)==q
# E is positive as orthogonal direct sum of locally U2 conjugated
# Q and zero blocks; its complement I36-E is also positive.
print("PASS H108.4: actual 36-level two-flag original-H75 detector E00⊗U2 Q U2dag preserves valid POVM positivity and exact event probabilities")

# Quantitative robust mismatch with ANY separable normalized state:
# Tr(W s_sep)>=0 but Tr(W s_link)=-519/1700. Since ||W||∞=1/2,
# ||s_link - s_sep||1 >= 2*(519/1700), so trace DISTANCE
# D=||...||1/2 >=519/1700. These are algebraic inequalities
# proven for all separable density operators, not a numeric fit.
link_negative=-linked_W/H106.p
assert link_negative==F(519,1700)
assert link_negative>0 and link_negative<F(1)
assert H106.prob_native==H106.prob_link
print("PASS H108.5: universal separability witness plus ||W||inf=1/2 certifies exact trace-distance LOWER BOUND 519/1700 of conditional linked state from EVERY separable normalized state")

gates={
"AX-SRC original H75 CPTP and source-local control Lie algebra":"EXACT",
"AX-OA calibrated phase/product site positive POVMs":"INDEPENDENT_DETECTOR_PREMISE",
"AX-CAN native local-only production of conditional H105 entangling link":"SCOPED_NO_GO",
"AX-CAN physical implementation of hypothetical intercell link":"OPEN",
"AX-SP same-source physical Cartan solder/intercell/spatial curvature":"OPEN",
"AX-DYN source-derived DeWitt/HDA/Einstein":"OPEN",
"AX-NORM Newton/cosmological constants sourced":"OPEN",
"AX-GEN noncircular F completeness":"OPEN",
}
assert len(gates)==8
print("BOUNDARY: linked case requires independently assumed H105 coherent intercell Hamiltonian; extra calibrated local X/Y detectors are operational premises, not generator theorems or hardware experiments")
print("BOUNDARY: mathematically source-compatible nonlocal link and universal entanglement witness prove neither common P9.125-128 Cartan source identity nor Einstein dynamics or F generative completeness")
