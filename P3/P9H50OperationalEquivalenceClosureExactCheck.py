"""H50: operational-equivalence boundary for fixed H42-H49 standard CPTP
sector; EXACT adaptive two-instrument/controlled-process verification;
matched-calibration CR submodel is nested within ordinary CPTP model.

A theorem, proved in the accompanying note by induction: when the two
model labels specify exactly the SAME initial state, SAME complete
controlled Markovian CPTP family, SAME outcome-resolved CP instruments
and SAME adaptive decision rule, every finite outcome tree agrees.
Not merely equality of the uncontrolled map, one-time marginal, or
aggregate strength.

An independent NON-MARKOVIAN counterexample shows that equality of
the one-step reduced map does NOT imply equality of two-step
experiment statistics without the Markov/complete-process assumption.

The conditional P6 collective a=b hypothesis merely restricts the
physical CONTROL parameter space of a standard CPTP subfamily; it
can be rejected against unlocked equal-norm CPTP controls, but its
success is not a violation of standard quantum mechanics.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import (
    N,U,A,B,T,Jcol,H,Xi
)
from P9H46CPTPOddInstrumentReadoutDisturbanceExactCheck import (
    flagged,Ds,P,nonselective
)
from P9H48InstrumentProvenanceKernelClosureExactCheck import (
    full_record,classical_record
)
from P9H49ControlledProcessProvenanceCertificateExactCheck import (
    LOCKED,UNLOCKED,OPPOSITE,Kphys,cayley,gate,qflag
)
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    unit,z,eye,scale,add,sub,mm,dagger,com,diag,trace,rr
)
assert N==3
def Phi(x):return gate(U,x)
def norm2(pair):return pair[0]*pair[0]+pair[1]*pair[1]
def cayley_at(pair,h):
    K=Kphys(*pair)
    den=F(1)+h*h*norm2(pair)
    W=add(eye(),add(scale(K,2*h/den),
                    scale(mm(K,K),2*h*h/den)))
    assert mm(W,dagger(W))==eye()
    assert mm(dagger(W),W)==eye()
    return W
def controlled(pair,h,rho):
    """One controlled microscopic CPTP STEP; no instrument yet."""
    return gate(cayley_at(pair,h),Phi(rho))
def outcome_matrix(k,t):
    """One Kraus for the H46 branch WITHOUT its 1/sqrt(2) weight."""
    return mm(Ds[k],P) if t else Ds[k]
def atbranch(k,t,rho):return flagged(k,t,rho)
def sum_mats(seq):
    out=z()
    for X in seq:out=add(out,X)
    return out

# Frozen Dataset A graph, center seed, independent Jcol SOURCE
# metadata, identical H46 instrument and exact total control norm.
controls=(LOCKED,UNLOCKED,OPPOSITE)
assert all(norm2(x)==F(18,25) for x in controls)
assert all(a!=0 and b!=0 for a,b in controls)
assert Xi(T)==add(A,B)
assert rr([Xi(T),Xi(scale(T,I)),Kphys(*LOCKED)])==2
for pair in (UNLOCKED,OPPOSITE):
    assert rr([Xi(T),Xi(scale(T,I)),Kphys(*pair)])==3
# The ACTUAL H42 original P3 full-diagonal hidden Xi image is
# distinct from the independently DECLARED candidate Jcol. Thus
# attaching Jcol to the common standard channel is an extra
# selection hypothesis, not a P3-derived provenance certificate.
assert rr([Xi(scale(h,I)) for h in H]+[add(A,B)])==6

# Exact finite POSITIVE Cayley pulse comparator, separate from
# H47's e^(xK) finite-time sine formula. At h=1/4,
# norm=18/25, W|1>=f(a|0>+b|2>)+c|1>
# with f=2h/(1+h²r²)=100/209, c=(1-h²r²)/(1+h²r²)
h=F(1,4)
r2=F(18,25)
den=F(1)+h*h*r2
f=2*h/den
c=(F(1)-h*h*r2)/den
assert f==F(100,209) and c==F(191,209)
seed=unit(1,1)
outcomes={}
for pair in controls:
    a,b=pair
    rho=gate(cayley_at(pair,h),seed)
    assert dagger(rho)==rho and trace(rho)==O
    assert rho[0][0]==gc(f*f*a*a)
    assert rho[1][1]==gc(c*c)
    assert rho[2][2]==gc(f*f*b*b)
    assert qflag(rho)==f*f*(a*a-b*b)/2
    assert sum((trace(atbranch(k,t,rho))
                for k in range(6) for t in (0,1)),Z0)==O
    outcomes[pair]=rho
assert outcomes[LOCKED][1][1]==outcomes[UNLOCKED][1][1]
assert outcomes[OPPOSITE][1][1]==outcomes[LOCKED][1][1]
assert qflag(outcomes[LOCKED])==F(0)
assert qflag(outcomes[UNLOCKED])==F(-3456,43681)
assert qflag(outcomes[OPPOSITE])==F(0)
# Oriented selection IS STRICTER than the unoriented classical null.
assert classical_record(outcomes[LOCKED])==classical_record(
    outcomes[OPPOSITE])
assert full_record(outcomes[LOCKED])!=full_record(
    outcomes[OPPOSITE])

# An actual 12-branch first instrument followed by a control chosen
# from its CLASSICAL outcome, followed by a second 12-branch
# instrument: 144 distinct valid joint instrument outcomes.
# Compare two INDEPENDENT ways to compute the same stochastic
# controlled process: sequential CP maps vs global Kraus path.
# This is a finite executable instance of the general
# all-depth adaptive operational-equivalence induction.
def choose_after(k,t):
    i=(k+2*t)%3
    return controls[i], F(1,4) if t==0 else F(1,5)
for initial in (unit(1,1),
                unit(0,0),
                scale(eye(),F(1,3))):
    first=controlled(LOCKED,F(1,4),initial)
    branch_sum=z()
    first_branches=[]
    total=Z0
    for k in range(6):
        for t in (0,1):
            alpha=(k,t)
            first_out=atbranch(k,t,first)
            first_branches.append(first_out)
            second_pair,h2=choose_after(k,t)
            W2=cayley_at(second_pair,h2)
            W1=cayley_at(LOCKED,F(1,4))
            # Composition of unnormalized Kraus factors
            # B= D_l P^s W2 U D_k P^t W1 U; each flagged step
            # contributes 1/sqrt(2), total density factor 1/4.
            prefix=mm(W2,mm(U,mm(outcome_matrix(k,t),
                                   mm(W1,U))))
            for l in range(6):
                for s in (0,1):
                    second_out=atbranch(l,s,controlled(
                        second_pair,h2,first_out))
                    Bpath=mm(outcome_matrix(l,s),prefix)
                    direct=scale(gate(Bpath,initial),F(1,4))
                    assert second_out==direct
                    assert dagger(second_out)==second_out
                    prob=trace(second_out)
                    assert prob.i==F(0) and prob.r>=0
                    total+=prob
                    branch_sum=add(branch_sum,second_out)
    assert len(first_branches)==12
    assert sum_mats(first_branches)==nonselective(first)
    assert trace(branch_sum)==total==O
    # Two differently named models with the same exact controlled
    # CPTP maps, reference state and instruments MUST share all
    # 144 joint branch probabilities, including adaptive choices.

# A comparison against a DIFFERENT control is allowed, but then
# the processes differ already inside completely standard QM.
assert classical_record(outcomes[LOCKED])!=classical_record(
    outcomes[UNLOCKED])
assert norm2(LOCKED)==norm2(UNLOCKED)
# The collective class {a=b} is a PROPER standard-CPTP submodel
# of the equal-norm standard class {a²+b²=18/25}; it does not
# introduce an additional postulate about the channel outcome law.

# Sharp logical guard: equality of FRESH one-step REDUCED channel
# does NOT imply equality of multi-time/process tensors if a hidden
# environment keeps memory. A standard correlated classical sign
# environment shows the failure (not CR-exclusive).
Psign=add(scale(unit(0,0),-1),
          add(unit(1,1),unit(2,2)))
assert mm(Psign,Psign)==eye() and dagger(Psign)==Psign
def sign_channel(x):
    return scale(add(x,gate(Psign,x)),F(1,2))
def correlated_two(x):
    # One fixed random hidden sign, reused at both steps:
    # U_sigma²=I for sigma=0,1.
    return scale(add(x,gate(mm(Psign,Psign),x)),F(1,2))
def independent_two(x):
    # Independently re-sampled sign at both steps:
    return sign_channel(sign_channel(x))
superposed=scale(add(add(unit(0,0),unit(1,1)),
                     add(unit(0,1),unit(1,0))),F(1,2))
assert trace(superposed)==O and dagger(superposed)==superposed
assert sign_channel(sign_channel(superposed))==sign_channel(superposed)
assert correlated_two(superposed)==superposed
assert independent_two(superposed)[0][1]==Z0
assert correlated_two(superposed)[0][1]==gc(F(1,2))
assert correlated_two(superposed)!=independent_two(superposed)
# Both schemes possess the SAME fresh one-step reduced sign_channel,
# but unequal two-step processes because their environments carry
# different classical temporal correlations. Thus H50's
# equivalence theorem REQUIRES matched entire controlled process
# (or a common Markov CPTP composition), not equality of a single
# reduced map in an arbitrary non-Markovian world.

print("PASS H50: identical controlled CPTP + identical CP instruments imply identical 144 adaptive two-outcome-tree blocks")
print("PASS H50: all-step equality follows by CP-composition induction, independently of CR semantic labeling")
print("PASS H50: exact equal-norm positive-Cayley collective null0 versus ordinary unlocked flag -3456/43681")
print("PASS H50: sign-opposite physical tangent has same CLASSICAL flag records but distinct conditional quantum records")
print("PASS H50: a=b is a proper selection submodel WITHIN standard finite CPTP, not non-GKSL dynamics")
print("PASS H50: same fresh reduced CPTP step need not imply same two-step NONMARKOVIAN process")
print("SCOPE: no impossibility for all CR models; applies only when the COMPLETE accessible controlled process matches standard QM")
print("SCOPE: original P3/P4-derived physical provenance, independent HDA/Einstein dynamics and hardware remain OPEN")
