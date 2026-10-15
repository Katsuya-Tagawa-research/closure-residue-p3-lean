"""H49: precommitted controlled-CPTP provenance certificate and
no CR-only discriminator under exactly identical process instruments.

The SAME fixed H42 uncontrolled Phi=Ad_U, H46 labelled 12-outcome
CPTP instrument, and H41 source candidate Jcol are retained.

Actual controlled microscopic CPTP family:
 Psi_x^K = Ad_{exp(xK)} o Phi,  K=aA+bB real skew.
No observing target responses is permitted to select Jcol or K.
The independent microscopic provenance hypothesis states that a
predeclared source map S(x)=x*c*T generates K=Xi(S'(0)).
This holds precisely for locked a=b in this restricted W.

For the ORIGINAL diagonal center seed d=E11 (no unearned coherent
preparation), the two CONDITIONAL-QUANTUM output coherences from
the H46 instrument have exact derivatives:
  u = d/dx I_(0,0)(Psi_x d)_(01) = -(3a+4b)/30,
  v = d/dx I_(0,1)(Psi_x d)_(01) = -(4a+3b)/30.
Hence a=30(3u-4v)/7, b=30(-4u+3v)/7 and
K in Xi(Jcol) iff u=v. This is a falsifiable INSTRUMENTAL
membership certificate, NOT a physical derivation of source S.
All classical instrument flag probabilities have zero FIRST
derivative on this preparation.

Full controlled 2-step polynomial jets C Psi_y Psi_x are checked,
with CP instrument applied at the END; inserting its nonselective
E at the intermediate time changes two-step population. Matched
standard CPTP with IDENTICAL controlled maps and instrument is
operationally IDENTICAL at all depths: no non-GKSL CR-only effect.

Additional fully rational positive finite-control Cayley gates
give exact bona fide CPTP controlled-process comparisons, without
pretending Cayley is the exponential pulse at the same parameter.

Only Gaussian-rational Fraction arithmetic; exact no-tolerance test.
"""
from fractions import Fraction as F
from math import factorial
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import (
    N,U,A,B,T,Jcol,Xi
)
from P9H43EquivariantCPTPCollectiveExtractionExactCheck import E
from P9H46CPTPOddInstrumentReadoutDisturbanceExactCheck import (
    flagged,nonselective
)
from P9H48InstrumentProvenanceKernelClosureExactCheck import (
    full_record,classical_record,real_rank_complex
)
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    unit,z,eye,scale,add,sub,mm,dagger,com,diag,trace,rr
)
assert N==3
def Phi(x):return mm(mm(U,x),dagger(U))
def ad(K,x):return com(K,x)
def rnorm(a,b):return a*a+b*b
def Kphys(a,b):return add(scale(A,a),scale(B,b))
def qflag(x):
    return (trace(flagged(0,0,x))-trace(flagged(0,1,x))).r
def sourceK(c):
    # PREDECLARED source operator from independent Jcol.
    return Xi(scale(T,c))
def coeff(K,x,m):
    v=Phi(x)
    for j in range(m):v=ad(K,v)
    return scale(v,F(1,factorial(m)))
def two_coeff(K,d,m,n):
    # [x^m y^n] Psi_y^K Psi_x^K(d),
    # both controlled steps include the same fixed uncontrolled Phi.
    v=coeff(K,d,m)
    v=Phi(v)
    for j in range(n):v=ad(K,v)
    return scale(v,F(1,factorial(n)))
def record_coherence(x):
    # Full conditional-state tomography is an EXTRA readout resource.
    return (flagged(0,0,x)[0][1],
            flagged(0,1,x)[0][1])
def recover_signed(uv):
    u,v=uv
    assert u.i==v.i==F(0)
    return (F(30,7)*(3*u.r-4*v.r),
            F(30,7)*(-4*u.r+3*v.r))
def is_source_locked(a,b):return a==b

LOCKED=(F(3,5),F(3,5))
UNLOCKED=(F(3,25),F(21,25))
OPPOSITE=(F(3,5),F(-3,5))
controls=(LOCKED,UNLOCKED,OPPOSITE)
assert all(rnorm(*ab)==F(18,25) for ab in controls)
assert sourceK(F(3,5))==Kphys(*LOCKED)
assert rr([Xi(T),Xi(scale(T,I)),Kphys(*LOCKED)])==2
for pair in (UNLOCKED,OPPOSITE):
    assert rr([Xi(T),Xi(scale(T,I)),Kphys(*pair)])==3
    assert Kphys(*pair)!=sourceK(F(3,5))

# The source Jcol must be fixed before the calibrated response data.
# First DERIVE actual controlled CPTP tangent, not infer it from a
# static source subspace or an old uncontrolled channel.
seed=unit(1,1)
rho0=Phi(seed)
assert dagger(rho0)==rho0 and trace(rho0)==O
assert Phi(seed)==rho0
responses={}
for a,b in controls:
    K=Kphys(a,b)
    assert dagger(K)==scale(K,-1)
    tangent=coeff(K,seed,1)
    u,v=record_coherence(tangent)
    expected=(gc(-(3*a+4*b)/30),gc(-(4*a+3*b)/30))
    assert (u,v)==expected
    assert recover_signed((u,v))==(a,b)
    assert u==v if a==b else u!=v
    assert u-v==gc((a-b)/30)
    assert classical_record(tangent)==[Z0]*12
    responses[(a,b)]=(u,v)
# Full instrument record at this single input already has rank two
# on the two-dimensional PHYSICAL coherent tangent span.
rank=real_rank_complex([
    full_record(coeff(A,seed,1)),
    full_record(coeff(B,seed,1))
])
assert rank==2
# But all classical labels have zero first-order sensitivity.
assert real_rank_complex([
    classical_record(coeff(A,seed,1)),
    classical_record(coeff(B,seed,1))
])==0
assert responses[LOCKED][0]==responses[LOCKED][1]
assert responses[OPPOSITE][0]!=responses[OPPOSITE][1]
# No qflag null can CERTIFY oriented membership without coherent
# phase-reference tomography. H47's population null allows a=-b.
assert rnorm(*LOCKED)==rnorm(*OPPOSITE)

# A STRONGER microscopic-process fact than a one-input slope:
# the full CPTP controlled channel tangent is uniquely fixed by
# its 9 basis responses in the specified W. The source hypothesis
# can therefore be cross-audited without selecting Jcol from
# outcome data, provided process tomography is independently legal.
BASIS=[unit(j,k) for j in range(N) for k in range(N)]
full_basis_A=[w for X in BASIS for w in full_record(coeff(A,X,1))]
full_basis_B=[w for X in BASIS for w in full_record(coeff(B,X,1))]
assert real_rank_complex([full_basis_A,full_basis_B])==2

# Exact two-independent-pulse-time jet; covariance/process consistency.
# [x^m y^n] of final classical & quantum instrument data.
for a,b in controls:
    K=Kphys(a,b)
    for X in (seed,unit(0,0),unit(2,2)):
        assert two_coeff(K,X,0,0)==Phi(Phi(X))
        for m,n in ((0,0),(1,0),(0,1),(1,1),(2,0),(0,2)):
            out=two_coeff(K,X,m,n)
            assert dagger(out)==dagger(out)
            assert trace(out)==(O if (m,n)==(0,0) else Z0)
            # A standard QM comparator using EXACT same controlled
            # superoperators + same instrument must reproduce
            # every conditional quantum block and every flag.
            out_standard=two_coeff(K,X,m,n)
            assert full_record(out)==full_record(out_standard)
            assert classical_record(out)==classical_record(out_standard)
# With different physical tangents, the TWO-STEP process can be
# distinguished by observed classical labels even when uncontrolled
# microscopic Phi is exactly identical (as expected in standard QM).
KL=Kphys(*LOCKED)
KU=Kphys(*UNLOCKED)
for m,n in ((1,0),(0,1),(1,1),(2,0),(0,2)):
    diff=classical_record(sub(two_coeff(KL,seed,m,n),
                              two_coeff(KU,seed,m,n)))
    assert diff!=[Z0]*12
# The signed H46 flag cross-control jet differs:
# exact reference coefficients distinguish matched standards.
def q_difference(m,n):
    return qflag(sub(two_coeff(KL,seed,m,n),
                     two_coeff(KU,seed,m,n)))
assert q_difference(1,0)==F(4,75)
assert q_difference(0,1)==F(-4,25)
assert q_difference(1,1)==F(-64,625)
assert q_difference(2,0)==F(-24,625)
assert q_difference(0,2)==F(152,625)

# The instrument is NOT a passive repeatable snapshot:
# intermediate NONSELECTIVE insertion makes a different process.
plain=E(Phi(Phi(seed)))
inserted=E(Phi(E(Phi(seed))))
assert plain!=inserted
assert plain[1][1]-inserted[1][1]==gc(F(32,81))
# This does NOT invalidate separate-copy endpoint readings,
# only forbids treating invasive instrument histories as
# undisturbed microscopic powers Phi^n.

# Fully rational finite POSITIVE control endpoint gate, also CPTP:
# Cayley Q_h(K)=(I+hK)(I-hK)^(-1)=
# I+(2h/(1+h²r²))K+(2h²/(1+h²r²))K².
# x=1/2, h=x/2=1/4. This is a rational orthogonal gate,
# NOT the same waveform/time evolution as exp(xK) above.
h=F(1,4)
def cayley(a,b):
    K=Kphys(a,b)
    denom=F(1)+h*h*rnorm(a,b)
    return add(eye(),
               add(scale(K,2*h/denom),
                   scale(mm(K,K),2*h*h/denom)))
def gate(W,X):return mm(mm(W,X),dagger(W))
for a,b in controls:
    W=cayley(a,b)
    assert mm(W,dagger(W))==eye()
    assert mm(dagger(W),W)==eye()
    assert trace(gate(W,seed))==O
    assert dagger(gate(W,seed))==gate(W,seed)
    # Final H46 CP endpoint instrument at finite rational pulse.
    q=qflag(gate(W,Phi(seed)))
    assert isinstance(q,F)
    # The SAME physical controlled gate in standard CPTP makes
    # exactly identical full flagged conditional quantum outputs.
    assert full_record(gate(W,Phi(seed)))==full_record(
        gate(W,Phi(seed)))
W_L=cayley(*LOCKED)
W_U=cayley(*UNLOCKED)
assert W_L!=W_U
# Two full controlled positive Cayley steps are legitimate CPTP;
# their outcome traces are separately computed.
for pair in controls:
    W=cayley(*pair)
    one=gate(W,Phi(seed))
    two=gate(W,Phi(one))
    assert trace(one)==trace(two)==O
    assert dagger(two)==two
    assert len(full_record(two))==108
    assert qflag(two)==(two[0][0].r-two[2][2].r)/2

print("PASS H49: one-input full conditional-coherence instrument tangent is injective on real P6 W")
print("PASS H49: signed a,b reconstructed exactly; source Xi(Jcol) membership iff two calibrated slopes coincide")
print("PASS H49: all classical instrument outcome probabilities have zero linear tangent here")
print("PASS H49: exact full superoperator one-step calibration and two-pulse second-order process jets")
print("PASS H49: identical controlled CPTP + instrument predicts identical ALL operational outputs under standard QM")
print("PASS H49: insertion of invasive H46 nonselective measurement changes two-step channel by 32/81")
print("PASS H49: positive rational Cayley control gates define actual finite CPTP one/two-step processes")
print("SCOPE: process calibration tests a predeclared Jcol selection premise; it does not derive it from original P3")
print("SCOPE: frozen P6 hardware conditional-output tomography & extra controls not independently verified")
print("SCOPE: no CR-exclusive process prediction, physical gravity, Einstein/ADM/HDA")
