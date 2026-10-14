"""H47: frozen Dataset-A calibration / Dataset-B held-out instrument response.

A genuinely different finite-time P6 COLLECTIVE conditional hypothesis:
  locked a=b, ex-ante static Jcol + STAR-COMPATIBLE ACCESSIBILITY,
versus a BEST SAME-DATA ordinary standard CPTP/GKSL control comparator
whose calibrated aggregate a²+b² is the same, but relative edge
allocation was NOT measured in Dataset A.

One FIXED H46, calibrated 12-outcome instrument is used at readout,
with classical flag E[Z]=(rho00-rho22)/2. No reselecting Jcol, no
fitting the instrument, Stark phase, or control amplitudes to Dataset B.

The precommitted locked and an unlocked alternative both have EXACT
aggregate norm18/25 and same CENTER POPULATION SURVIVAL FOR ALL TIMES.
Yet at finite positive pulse x=1/2, their flag means differ by at
least rational 1269/15625 (and a robust timing-interval lower bound).
Finite n=100000 copies plus detector bias<=1/500 yields a nonvacuous
Chebyshev worst-case conditional model-comparison certificate.

The gap COLLAPSES if independent Dataset-A calibration also fixes the
relative amplitudes (or an even-coherence that infers them): standard
ordinary QM then predicts the identical collective null. This is a
conditional physical-provenance hypothesis test, NOT a CR-exclusive
dynamics law, and no physical P6 hardware success is demonstrated.
"""
from fractions import Fraction as F
from math import factorial
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import N,A,B
from P9H46CPTPOddInstrumentReadoutDisturbanceExactCheck import (
    D,flagged,effectprob,nonselective,classical_flag_moments
)
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    unit,z,eye,scale,add,sub,mm,dagger,com,diag,hidden,trace
)
assert N==3
# SPECIFY DATASET A BEFORE TARGET OUTPUTS. No signed left-right
# output, coherent collective output tomography, or individually
# calibrated edge strengths in this dataset.
EXACT_CALIBRATION={
  "graph":"3-site connected path, both exchange edges active",
  "prepared_seed":"E11 center population projector",
  "coherent_control":"one positive duration signed real exchange pulse",
  "total_coherent_tangent_squared_norm":F(18,25),
  "background_noise":"same independently calibrated post-exchange site-dephasing",
  "post_exchange_dephasing":F(3,4),
  "diagonal_Stark_alpha":(F(0),F(0),F(0)),
  "instrument":"H46 separately effect-calibrated 12-flag CPTP instrument",
  "calibration_population":"center survival p1(t) for arbitrary positive t",
  "dataset_B":"unseen signed left-minus-right flag after controlled pulse"
}
# CR's EXTERNAL CONDITIONAL assumptions are preregistered separately,
# not inferred from H46 readout or P3 static full-D3 filtration.
COLLECTIVE_HYPOTHESES=(
 "independently certified microscopic Jcol",
 "star-compatible oriented first-residue physical provenance",
 "physical tangent a=b for EVERY declared one-knob real control"
)
aL,bL=F(3,5),F(3,5)
aS,bS=F(3,25),F(21,25)
def r2(a,b):return a*a+b*b
norm=r2(aL,bL)
assert norm==r2(aS,bS)==EXACT_CALIBRATION[
    "total_coherent_tangent_squared_norm"]==F(18,25)
assert all(q>0 for q in (aL,bL,aS,bS))
assert (aL==bL) and (aS!=bS)
def K_of(a,b):return add(scale(A,a),scale(B,b))
def mvec(M,v):
    return [sum((M[i][j]*v[j] for j in range(N)),Z0)
            for i in range(N)]
def zero_vec():return [Z0,Z0,Z0]
def center_jets(a,b,order):
    """Exact x-Taylor coefficients of e^(xK)|1>."""
    K=K_of(a,b)
    assert dagger(K)==scale(K,-1)
    state=[Z0,O,Z0]
    out=[state]
    for j in range(1,order+1):
        state=[t/gc(j) for t in mvec(K,state)]
        out.append(state)
    assert out[0]==[Z0,O,Z0]
    assert out[1]==[gc(a),Z0,gc(b)]
    # K^3=-r²K, the exact finite-time closed two-level rotation.
    K3=mm(mm(K,K),K)
    assert K3==scale(K,-r2(a,b))
    return out
def pop_jets(a,b,order):
    v=center_jets(a,b,order)
    return [
        [sum((v[j][i]*v[m-j][i].conj()
              for j in range(m+1)),Z0) for m in range(order+1)]
        for i in range(N)
    ]
def g_coeff(k):
    # sin²(sqrt(r²) x)/r², exact rational even coefficient
    if k<2 or k%2:return F(0)
    j=k//2
    return F((-1)**(j+1)*2**(2*j-1),factorial(2*j))*norm**(j-1)
for a,b in ((aL,bL),(aS,bS)):
    coeffs=pop_jets(a,b,16)
    for m in range(17):
        assert coeffs[0][m]==gc(a*a*g_coeff(m))
        assert coeffs[2][m]==gc(b*b*g_coeff(m))
        assert coeffs[1][m]==gc((F(1) if m==0 else F(0))
                                 -norm*g_coeff(m))
        assert sum((coeffs[i][m] for i in range(N)),Z0)==(
            O if m==0 else Z0)
    # Post-unitary finite CPTP dephasing leaves ALL diagonal outcomes
    # unchanged, including centered calibration survival and odd q.
    lam=EXACT_CALIBRATION["post_exchange_dephasing"]
    for m in range(17):
        cstate=z()
        v=center_jets(a,b,16)
        for j in range(m+1):
            vv=[[v[j][i]*v[m-j][k].conj()
                 for k in range(N)] for i in range(N)]
            cstate=add(cstate,vv)
        after=add(scale(cstate,lam),scale(diag(cstate),F(1)-lam))
        assert diag(after)==diag(cstate)
        # Taylor coefficients of a physical channel need not be
        # positive individually; extract the flag expectation as
        # a linear trace functional WITHOUT probability positivity.
        flag_q=(trace(flagged(0,0,after))
                -trace(flagged(0,1,after))).r
        assert flag_q==(after[0][0].r-after[2][2].r)/2

# Exact closed finite-time response:
# p1=cos²(sqrt(norm)x), same for both; p0=a²*g,
# p2=b²*g, q=(a²-b²)*g/2.
deltaL=aL*aL-bL*bL
deltaS=aS*aS-bS*bS
assert deltaL==F(0)
assert deltaS==F(-432,625)
assert F(2)*(aL*aL-bL*bL)==F(0)
assert F(2)*(aS*aS-bS*bS)==F(-864,625)
# Same Dataset-A center population for ALL x, not merely 16 jets:
# center survival cos²(sqrt(norm)*x) is a function of norm only.
# H46 flag mean on HELD-OUT post-control state differs.

x=F(1,2)
y2=norm*x*x
assert y2==F(9,50)<F(1)
# sin(y)>=y(1-y²/6), so sin²(y)>=y²(1-y²/3), y²<=1.
sin2_lower=y2*(F(1)-y2/F(3))
sin2_upper=y2
factor=abs(deltaS)/(2*norm)
assert factor==F(12,25)
lower=factor*sin2_lower
upper=factor*sin2_upper
assert lower==F(1269,15625)
assert lower>F(0) and lower<upper
# True held-out flag mean of unlocked comparison is <=-lower.
# Locked conditional mean is EXACTLY zero at all x.

# Robust allowed pulse duration deviation +/- 1/100:
# Use min y² to lower bound y² factor and max y² in
# (1-y²/3). No use of unverified floating trig values.
dt=F(1,100)
y2min=norm*(x-dt)**2
y2max=norm*(x+dt)**2
assert F(0)<y2min<y2<y2max<F(1)
lower_timed=factor*y2min*(F(1)-y2max/F(3))
assert F(0)<lower_timed<lower

# Same independently effect-calibrated H46 flag, later applied
# to a separately prepared controlled state. This measurement
# is DESTRUCTIVE and therefore placed at the END of the pulse.
for state in (D(F(1),F(0),F(0)),
              D(F(0),F(1),F(0)),
              D(F(0),F(0),F(1))):
    mean,var,dist=classical_flag_moments(state)
    assert mean==(state[0][0].r-state[2][2].r)/2
# Separately calibrated detector systematic bias bound:
# |E[Z_actual]-q_ideal|<=1/500 in the target mode;
# this is a DECLARED experimental condition, not something
# proved from those ideal reference checks.
bias=F(1,500)
n=100000
gap=lower_timed
threshold=gap/F(2)
margin=threshold-bias
assert margin>0
# Worst-case error probability using Var(Z)<=1 and n independent
# preparations: Pr(|sample mean - calibrated mean|>=margin)
# <=1/(n margin²). Both the locked null and THIS fixed unlocked
# example are separated by the midpoint decision threshold.
p_wrong=F(1)/(F(n)*margin*margin)
assert p_wrong<F(1,100),(p_wrong,gap,margin)
# This excludes neither *all* arbitrarily-near-locked standard
# controls at finite n, nor unrestricted alternative systematics.

# Calibration leakage audit: if physical relative edge amplitude
# is also independently calibrated in Dataset A, best standard
# microscopic QM ALSO predicts the same locked null.
assert (aL+bL)**2==2*norm
assert (aS+bS)**2<2*norm
assert 2*norm-(aS+bS)**2==(aS-bS)**2>0
assert 2*norm-(aL+bL)**2==(aL-bL)**2==0
# A phase-calibrated EVEN coherence response from center launch,
# proportional to (a+b)*sin(sqrt(norm)x)*cos(sqrt(norm)x),
# can also determine that sum when the factor is nonzero.
# Thus calibrating E's coherent quantum output on TARGET controlled
# samples in Dataset A can collapse the gap even without signed q.

# Extra odd instrument CALIBRATION on reference preparations
# is NOT equivalent to using held-out target response q to infer
# the a:b physical ratio. Data separation must be enforced.
# No inference of Jcol, physical control locking, or tau from
# H46 instrument exists without independent P6 provenance.
print("PASS H47: Dataset-A-matched locked/unlocked standard CPTP with exact same full-time center survival")
print("PASS H47: exact exchange channel Taylor jets through degree16 and invariant post-pulse dephasing populations")
print("PASS H47: target signed H46 flag q=0 versus |q|>=1269/15625 at positive finite x=1/2")
print("PASS H47: robust timing-window lower bound and finite-shot Chebyshev error <1/100")
print("PASS H47: effect-calibration flag must be independent of held-out target-response Dataset B")
print("PASS H47: adding physical relative-edge or coherent sum calibration collapses standard prediction gap")
print("SCOPE: conditional accessibility/provenance restriction NOT derivable from P3 nor CR-exclusive dynamics")
print("SCOPE: hardware nuisance/stark/crosstalk uncertainty outside declared bounds remains OPEN")
