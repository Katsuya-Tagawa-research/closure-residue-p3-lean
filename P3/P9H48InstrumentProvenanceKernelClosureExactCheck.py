"""H48: necessary/sufficient LINEAR instrument quotient criterion, exact
minimal observer memory and independently calibrated provenance boundary.

For H42's SAME rational reflection-symmetric CPTP Phi=Ad_U,
and H46's SAME 12-outcome CP instrument I_{k,t},
the full labelled quantum-classical channel C: M3 -> direct sum_12 M3
has complex rank 7, with kernel span(E02,E20). The full CLASSICAL
outcome probability map has rank 3; the nonselective quantum marginal
E has rank 4. All THREE are distinct operational information models.

rank([C; C Phi])=9: both lost chord quadratures return after ONE
step. Thus no autonomous linear (hence no CPTP) dynamics exists on
CURRENT labelled instrument outputs alone, even for physical states.
The minimum LINEAR predictive state for arbitrary Hermitian input
is the FULL 9-complex-dimensional M3 operator space (=8 real affine
parameters for trace-one densities), with two missing real chord
quadratures beyond a full labelled physical quantum instrument.

For source static Jcol and SAME fixed Phi,C, same norm, two perfectly
legitimate CPTP coherent control extensions have different tangent
splits: instrument compatibility does not create a microphysical
control-selection/provenance theorem. Quantum conditional-outcome
coherence at FIRST order detects signed amplitudes, whereas the
classical flag expectation starts at second order (squares).

Exact Gaussian rationals, existing H42-H46 matrix algorithms only.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import (
    N,U,A,B,T,Jcol,reflection,Xi
)
from P9H43EquivariantCPTPCollectiveExtractionExactCheck import E,twirl
from P9H44MinimalObserverMemoryQuadraticResidueExactCheck import real_rank_complex
from P9H46CPTPOddInstrumentReadoutDisturbanceExactCheck import (
    flagged,nonselective,parity_q
)
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    unit,z,eye,scale,add,sub,mm,dagger,com,diag,hidden,trace,rr
)
assert N==3
MATS=[unit(i,j) for i in range(N) for j in range(N)]
def Phi(x):return mm(mm(U,x),dagger(U))
def flat(x):return [x[i][j] for i in range(N) for j in range(N)]
def classical_record(x):
    # All 12 outcome probabilities on physical states, extended
    # linearly to arbitrary complex operators for rank questions.
    return [trace(flagged(k,t,x))
            for k in range(6) for t in (0,1)]
def full_record(x):
    # Quantum-classical instrument output. Each 3x3 CP branch is
    # labelled by its (k,t); the record is a full quantum BLOCK,
    # NOT just 12 classical label probabilities!
    return [w for k in range(6) for t in (0,1)
            for w in flat(flagged(k,t,x))]
def quantum_record(x):return flat(nonselective(x))
def stacked(fun,n,x):
    out=[]
    for _ in range(n):
        out+=fun(x)
        x=Phi(x)
    return out
def vec_rank(fun,n=1):
    return real_rank_complex([stacked(fun,n,x) for x in MATS])
# rank function accepts ROWS (each matrix basis vector maps to
# a row of its outputs). Rank of rows equals rank of linear map.
assert vec_rank(classical_record)==3
assert vec_rank(quantum_record)==4
assert vec_rank(full_record)==7
assert vec_rank(classical_record,2)==5
assert vec_rank(full_record,2)==9
assert vec_rank(full_record,3)==9

# Kernel(C) is exactly the TWO complex directed endpoint chords.
E02=unit(0,2)
E20=unit(2,0)
assert full_record(E02)==[Z0]*108
assert full_record(E20)==[Z0]*108
assert real_rank_complex([flat(E02),flat(E20)])==2
assert Phi(E02)!=z() and Phi(E20)!=z()
assert full_record(Phi(E02))!=[Z0]*108
assert full_record(Phi(E20))!=[Z0]*108
assert real_rank_complex([full_record(Phi(E02)),
                          full_record(Phi(E20))])==2
# Necessary/sufficient condition for a well-defined LINEAR quotient
# dynamics C Phi = Phi_eff C is Phi(ker C) subset ker C. Violated.
# In particular, an autonomous CPTP effective quantum channel on the
# compressed current output cannot exist; even LINEAR fails.
assert vec_rank(full_record,2)==vec_rank(full_record)+2

# Explicit physical density pairs that are currently
# instrument-indistinguishable but dynamically distinguishable.
real_chord=add(E02,E20)
imag_chord=scale(sub(E02,E20),I)
rho0=scale(eye(),F(1,3))
for chord in (real_chord,imag_chord):
    assert dagger(chord)==chord and diag(chord)==z()
    pos=add(rho0,scale(chord,F(1,6)))
    neg=sub(rho0,scale(chord,F(1,6)))
    assert dagger(pos)==pos and dagger(neg)==neg
    assert trace(pos)==trace(neg)==O
    # PSD verified analytically: nontrivial two-site block has
    # eigenvalues 1/3+-1/6; center eigenvalue 1/3.
    assert pos[0][0]*pos[2][2]-pos[0][2]*pos[2][0]==gc(F(1,12))
    assert neg[0][0]*neg[2][2]-neg[0][2]*neg[2][0]==gc(F(1,12))
    assert full_record(pos)==full_record(neg)
    assert full_record(Phi(pos))!=full_record(Phi(neg))
    assert classical_record(pos)==classical_record(neg)
    assert quantum_record(pos)==quantum_record(neg)
# Specific distinguishable outcomes: even chord moves to center
# population; imaginary chord moves to H46 (0,0)-branch edge
# conditional quantum coherence, not necessarily classical count.
real_diff=Phi(real_chord)
imag_diff=Phi(imag_chord)
assert real_diff[1][1]==gc(F(8,9))
assert imag_diff[1][1]==Z0
assert flagged(0,0,imag_diff)[0][1]==gc(F(1,5))
assert flagged(0,0,real_diff)[0][1]==-I*gc(F(1,15))
# Under full instrument data, only Hermitian chord Re/Im are
# dynamically missing, i.e. TWO real parameters on trace-one
# physical density states. This is distinct from H44's 1-REAL
# memory closure on the reflection-even reduced observer.
assert real_rank_complex([flat(real_chord),flat(imag_chord)])==2
assert vec_rank(full_record,2)==9

# Compare SOURCE CONTROL PROVENANCE under the exactly same
# uncontrolled microscopic Phi, H46 instrument, independently
# declared static Jcol, connected graph and aggregate tangent norm.
LOCKED=(F(3,5),F(3,5))
UNLOCKED=(F(3,25),F(21,25))
OPPOSITE=(F(3,5),F(-3,5))
def Kphys(a,b):return add(scale(A,a),scale(B,b))
def norm2(pair):return pair[0]**2+pair[1]**2
assert norm2(LOCKED)==norm2(UNLOCKED)==norm2(OPPOSITE)==F(18,25)
Klock=Kphys(*LOCKED)
Kunlock=Kphys(*UNLOCKED)
Kopp=Kphys(*OPPOSITE)
Jimage=[Xi(T),Xi(scale(T,I))]
assert rr(Jimage)==2
assert rr(Jimage+[Klock])==2
assert rr(Jimage+[Kunlock])==3
assert rr(Jimage+[Kopp])==3
assert Klock!=Kunlock and Klock!=Kopp
# Each Ψ_x^(a,b)=Ad_exp(x Kphys(a,b)) o Phi is a valid
# one-knob CPTP control family for any real x, with SAME
# uncontrolled channel at x=0. Source Jcol is additional
# static metadata, not a theorem selecting its coherent control.
d=unit(1,1)
def controlled_first_derivative(pair):
    # derivative_x Ψ_x(d) at x=0, for fixed Phi pre-step
    # the source controlled AFTER Phi(d) would have different
    # derivative. Here choose the FROZEN P6 directly prepared
    # center seed to expose instrument tangent identifiability.
    return com(Kphys(*pair),d)
for pair in (LOCKED,UNLOCKED,OPPOSITE):
    a,b=pair
    response=controlled_first_derivative(pair)
    assert response[0][1]==gc(a)
    assert response[2][1]==gc(b)
    assert flagged(0,0,response)[0][1]==gc(F(3,10)*a)
    assert flagged(0,1,response)[0][1]==gc(F(3,10)*b)
    # Individual CLASSICAL instrument outcome probabilities have
    # zero FIRST derivative on a center diagonal state.
    assert classical_record(response)==[Z0]*12
    # Thus doing independent conditional-outcome COHERENCE
    # tomography at first order would calibrate both signed a,b;
    # measuring merely the flags, even with full 12-classical
    # probabilities, does not recover the signs at first order.
assert flagged(0,0,controlled_first_derivative(LOCKED))[0][1]!=flagged(
    0,0,controlled_first_derivative(UNLOCKED))[0][1]
assert flagged(0,1,controlled_first_derivative(LOCKED))[0][1]!=flagged(
    0,1,controlled_first_derivative(UNLOCKED))[0][1]

# The H47 signed classical flag ONLY detects a²-b², so both
# a=b and a=-b give ZERO for any time, although a=-b is NOT in
# the declared oriented Jcol first-residue direction.
for pair in (LOCKED,OPPOSITE,UNLOCKED):
    a,b=pair
    flag2=(a*a-b*b)/2
    if pair==UNLOCKED:
        assert flag2==F(-216,625)!=0
    else:
        assert flag2==0
assert rr(Jimage+[Kopp])==3
# Hence an exact null on Dataset B never proves the orientation
# of a left/right coherent tangent. It is a falsification test
# of the conditional model, not a verification of provenance.

print("PASS H48: H46 classical-label probabilities rank3, nonselective quantum output rank4, full labelled quantum instrument rank7")
print("PASS H48: one-step full-instrument observability rank9; ker instrument span(E02,E20) not invariant")
print("PASS H48: no autonomous linear instrument-output channel for the fixed original H42 microscopic Phi")
print("PASS H48: positive real- and imaginary-chord twin states currently identical but future instrument-distinguishable")
print("PASS H48: SAME uncontrolled Phi,Jcol,H46 instrument,norm permit locked/unlocked CPTP physical control families")
print("PASS H48: conditional outcome quantum coherence first derivative identifies SIGNED a,b; classical flags do not")
print("PASS H48: opposite-sign control a=-b gives same H47 null but violates oriented P6 Jcol")
print("SCOPE: necessary/sufficient kernel criterion is LINEAR; quantum CP quotient needs additional structure if invariance holds")
print("SCOPE: no microderived instrument-compatible physical provenance, CR-only prediction or Einstein gravity")
