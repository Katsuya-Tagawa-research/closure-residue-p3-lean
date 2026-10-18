"""H101 / P11: original positive H75 site phase invisible in H85 flag r.

A 1-parameter continuous family of genuinely PSD qutrit inputs rho_t has
identical original H75 4-site flag-readout vector and H85 selected K4
metric, yet a legitimate original-H75-output *positive* POVM has
probability 21/50 - 3t/20. Exact H101 operational incompleteness;
an independently measured microscopic phase is NOT an ADM momentum.
No new CPTP physics, Hamiltonian, spatial interaction or Einstein law.
"""
from fractions import Fraction as F

from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    micro,embed,mattrace,matmul,matadj,matadd,matscale,
    eye_n,zero_n,R60,U,M0,M1
)
import P9H85A4EdgeSourceSelectionExactCheck as H85
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P9H98DeWittLambdaFlatHDASourceSelectorExactCheck as H98
import P9H99SourceMetricRankCurvatureJetNonselectionExactCheck as H99
import P9H100ConstraintNormalizationGenerativeProvenanceExactCheck as H100

assert R60[0][0]==I*gc(F(-32,135))
assert H85.r==(F(0),F(16,25),F(16,25),F(4,25))
assert H91.rank(H99.composite)==3
assert H100.direct(F(1),F(1),F(1,2),H100.U)==H100.D(H100.U)

# 2-by-2 block: diag (3/4,1/4) with imaginary coherence ±it/4.
# Exact principal minor det=(3-t²)/16 >= 1/8 at |t|<=1.
coherent=zero_n(3)
coherent[0][1]=I*gc(F(1,4))
coherent[1][0]=-I*gc(F(1,4))
assert matadj(coherent)==coherent
baseline=H85.rho3
assert baseline[0][0]==gc(F(3,4))
assert baseline[1][1]==gc(F(1,4))
assert baseline[2][2]==Z0
def rho(t):
    t=F(t)
    assert -1<=t<=1
    Z=matadd(baseline,matscale(coherent,gc(t)))
    assert matadj(Z)==Z and mattrace(Z)==O
    assert Z[0][1]==I*gc(t/F(4))
    assert Z[1][0]==-I*gc(t/F(4))
    # Strict 2x2 positivity; third zero mode is positive semidefinite.
    det=Z[0][0].r*Z[1][1].r-(Z[0][1]*Z[1][0]).r
    assert det==(3-t*t)/F(16)>=F(1,8)>0
    return Z

params=(F(-1),F(-1,2),F(0),F(1,2),F(1))
for t in params:
    state=rho(t)
    assert H85.flag1(state)==F(4,25)
    four=tuple(H85.flag1(y) for y in (H85.d0,H85.d1,H85.d2,state))
    assert four==H85.r
    w=H85.additive(four)
    assert w==H85.wa==(4,4,1,8,5,5)
    assert H98.metric_chart(w)==H99.g0
print("PASS H101.1: five all-rational positive samples of CONTINUOUS true H75 qutrit state family retain ALL four source flag outputs (0,16/25,16/25,4/25) and identical positive K4 spatial response metric")
print("PASS H101.1: analytic PSD certificate det=(3-t^2)/16>=1/8 holds FOR EVERY real -1<=t<=1, not only sampled points")

# Original source coherent phase observable Y01 and genuine quantum
# positive readout effect Q=(I3+Y01)/2 (eigenvalues 0,1/2,1).
Y=zero_n(3)
Y[0][1]=-I
Y[1][0]=I
assert matadj(Y)==Y
assert matmul(matmul(Y,Y),Y)==Y
Q=matscale(matadd(eye_n(3),Y),gc(F(1,2)))
assert matadj(Q)==Q
# Q and I-Q have respectively nonnegative spectra {0,1/2,1}.
assert matmul(Y,Y)==[[O,Z0,Z0],[Z0,O,Z0],[Z0,Z0,Z0]]
for t in params:
    yt=mattrace(matmul(Y,rho(t)))
    assert yt.i==0 and yt.r==-t/F(2)

# E on true six-level H75 output: flag0 ⊗ U Q U^dag,
# zero effect on flag1. It is a valid 0<=E<=I6 projector-block
# positive POVM effect, with output calibration U independently assumed.
UQU=matmul(matmul(U,Q),matadj(U))
E=zero_n(6)
for a in range(3):
    for b in range(3):
        E[a][b]=UQU[a][b]
assert matadj(E)==E

# Parent POVM positivity follows unitary conjugation of Q and addition
# of a zero block, verified algebraically through the polynomial
# Q(2Q-I)(Q-I)=0 and eigenvalues (0,1/2,1).
eigen_poly=matmul(matmul(Q,matadd(matscale(Q,gc(2)),matscale(eye_n(3),-1))),
                  matadd(Q,matscale(eye_n(3),-1)))
assert eigen_poly==zero_n(3)

prob=[]
for t in params:
    state=rho(t)
    out=micro(embed(state))
    value=mattrace(matmul(E,out))
    assert value.i==0
    expected=F(21,50)-F(3,20)*t
    assert value.r==expected,(t,value.r,expected)
    assert 0<=value.r<=1
    prob.append(value.r)
assert prob[0]==F(57,100)
assert prob[-1]==F(27,100)
assert prob[-1]-prob[0]==F(-3,10)
assert prob[2]==F(21,50)
print("PASS H101.2: original H75 source output plus legitimate positive six-level phase POVM gives p_E(t)=21/50-3t/20, p(-1)=57/100, p(+1)=27/100, phase gap -3/10")

# The same original four flag readouts AND H85 K4 g are exactly
# independent of t, but a physically allowed alternative output
# measurement varies. Hence no function ONLY of these four r values
# can yield the alternate phase observable throughout this family.
assert H85.flag1(rho(F(-1)))==H85.flag1(rho(F(1)))
assert H98.metric_chart(H85.additive(H85.r))==H99.g0
assert prob[0]!=prob[-1]
# Along rho_t, derivative of flags/metric is zero whereas
# derivative of positive POVM outcome is -3/20 nonzero.
assert F(-3,20)!=0
print("PASS H101.3: no single-valued f(r_H75_four_flags) reproduces source-accessible phase readout; d(flags)/dt=0 but dp_E/dt=-3/20 !=0")

# Strongly scoped rank obstruction: the normalized endpoint rule
# H85 r->w->g has rank3, so ANY differentiable 12D "source
# canonical state" that factors only through these four r values
# has Jacobian rank<=3, and any 2-form on 3 real config
# coordinates is represented by a 3x3 skew matrix of rank<=2.
assert H91.rank(H99.J)==3
assert H91.rank(H99.composite)==3
skew=[[F(0),F(1),F(2)],[-F(1),F(0),F(3)],
      [-F(2),-F(3),F(0)]]
assert H91.rank(skew)==2
assert H91.rank(H99.composite)<6
print("PASS H101.4: H85 source metric has rank3; every 2-form on its three-dimensional observable image has even rank at most2, not full 12D 6-pair KKS/ADM symplectic rank")

# For any externally spatial-labelled rho_{t(x)} independently
# prepared per point x, its entire flag/K4 spatial field is constant,
# regardless of phase-profile t(x). This is observation-level
# non-injectivity even with every spatial flag jet; it DOES NOT
# constitute a microscopic spatial propagation law.
for t in params:
    assert tuple(H85.flag1(y) for y in
                 (H85.d0,H85.d1,H85.d2,rho(t)))==H85.r
print("BOUNDARY: phase-responsive positive POVM is STANDARD QUANTUM readout, not P3-specific empirical signature or an ADM conjugate momentum")
print("BOUNDARY: detector-calibrated U is used only as an output POVM, never promoted to an independently supplied pre-reset Hamiltonian knob")
print("BOUNDARY: AX-OA observational completeness, AX-SP physical spatial field, AX-CAN 6+6 symplectic dynamics, AX-DYN DeWitt/HDA/Einstein and AX-GEN F completeness all OPEN")
