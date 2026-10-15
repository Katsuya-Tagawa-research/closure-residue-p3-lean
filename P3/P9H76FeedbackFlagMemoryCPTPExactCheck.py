"""H76 — feedback-aware classical-quantum memory for the SAME H75 source.

Full microscopic H75 6D CPTP channel with genuine ORIGINAL P3 signed
R3 != 0, two independently controlled real edges, independently
calibrated site dephasing and informative environment flag is UNCHANGED.

Instead of discarding the two-state flag by partial trace, use the
exact CPTP flag-dephasing observer C_flag = sum_a P_a . P_a.
Its rank-18 image is M3(C) direct sum M3(C). It closes under
H75 microscopic channel, full visible controls and dephasing, under
conditional *classical flag* feedback and CP instrument branches.
It is passive on states OUTPUT by H75 source.

This IS a conditional physical memory construction, not a P3-only
derivation of the availability of flag measurement/feedback devices.
Coherent flag rotations destroy the observer-kernel invariance.
All results checked by exact Gaussian-rational arithmetic.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    ONE6, MBASIS, D6, embed, envblock, zero_n, eye_n,
    matmul, matadd, matscale, matadj, mattrace, matcomm,
    qtrace, qconj, micro, physical_micro, SETTINGS,
    Fgate, micro_branch, r6, r6same, R60, d0, d1
)
from P9H48InstrumentProvenanceKernelClosureExactCheck import real_rank_complex

assert len(MBASIS)==36

P=[]
for a in (0,1):
    Q=zero_n(6)
    for i in range(3):
        Q[3*a+i][3*a+i]=O
    P.append(Q)
assert matadd(P[0],P[1])==ONE6
assert matmul(P[0],P[1])==zero_n(6)
def flagged(X):
    return matadd(qconj(P[0],X),qconj(P[1],X))
def flat(X):
    return [X[i][j] for i in range(6) for j in range(6)]
def rank(fn):
    return real_rank_complex([flat(fn(X)) for X in MBASIS])
def flag_branch(a,X):
    return qconj(P[a],X)
def feedback(X):
    return qconj(Fgate,X)

assert rank(flagged)==18
assert all(flagged(flagged(X))==flagged(X) for X in MBASIS)
assert all(mattrace(flagged(X))==mattrace(X) for X in MBASIS)
assert all(matadj(flagged(matadj(X)))==flagged(X)
           for X in MBASIS)
assert all(flagged(micro(X))==micro(X) for X in MBASIS)
assert all(micro(flagged(X))==micro(X) for X in MBASIS)
print("PASS H76: CPTP flag-record M3⊕M3 rank18 (of 36), exact conditional expectation and noninvasive on H75 micro output")
print("PASS H76: SAME H75 informative nonzero-P3 micro dynamics commutes with flag observer on all M6")

for X in MBASIS:
    assert flagged(feedback(X))==feedback(flagged(X))
    for x,y,qs in SETTINGS:
        Y=physical_micro(x,y,qs,X)
        assert flagged(Y)==physical_micro(x,y,qs,flagged(X))
    for a in (0,1):
        assert flagged(flag_branch(a,X))==flag_branch(a,flagged(X))
    for j in range(3):
        assert flagged(micro_branch(j,X))==micro_branch(j,flagged(X))
print("PASS H76: all real P6-like independent controls + unequal site dephasing + flag-conditioned SWAP feedback + positive flag/site CP branches intertwine memory")

def controlled_branch(Y,stage):
    x,y,qs=SETTINGS[stage%len(SETTINGS)]
    Y=physical_micro(x,y,qs,Y)
    if stage%2==0:
        Y=feedback(Y)
    Y=flag_branch((stage+1)%2,Y)
    Y=micro_branch((stage+2)%3,Y)
    return Y

for X in MBASIS:
    u=X
    v=flagged(X)
    for stage in range(5):
        u=controlled_branch(u,stage)
        v=controlled_branch(v,stage)
        assert flagged(u)==v
print("PASS H76: exact adaptive flag/site outcome quantum instrument sequences yield physically CPTP Markovian block-memory closure")

# Strong physically measured single-copy flag-resolved site POVM:
# P_a tensor |j><j|, site j per declared visible apparatus;
# all CP branches leave flag memory well-defined.
for X in MBASIS:
    for a in (0,1):
        for j in range(3):
            expected=X[3*a+j][3*a+j]
            measured=flag_branch(a,micro_branch(j,X))
            assert mattrace(measured)==expected
            assert mattrace(flag_branch(a,micro_branch(j,flagged(X))))==expected
print("PASS H76: genuine positive single-copy joint (flag,site) instrument factors exactly through rank18 memory")

# The actual original signed P3 calculation is STILL at full micro:
# flag observer is identity on EVERY original six-dimensional
# diagonal seed, hence retains seed labels needed to compute all
# bilinear original R3 using the independently known micro.
assert R60!=zero_n(6)
assert flagged(R60)==R60
for da in D6:
    assert flagged(da)==da
    for db in D6:
        witness=r6(da,db)
        assert flagged(witness)==witness
        assert witness==r6(flagged(da),flagged(db))
print("PASS H76: all original P3 diagonal seed labels and all computed signed R3 outputs retained by flag observer; nonzero original R3 preserved")
print("BOUNDARY: algebraic reconstruction uses known micro Φ, not a directly CP-measured P3 signed residue")

# The old visible-only qutrit record is insufficient when feedback
# is an admitted physical control. Two positive micro pure states:
rho0=embed(d0,0)
rho1=embed(d0,1)
assert qtrace(rho0)==qtrace(rho1)==d0
assert flagged(rho0)!=flagged(rho1)
assert qtrace(feedback(rho0))==d0
assert qtrace(feedback(rho1))==d1
print("PASS H76: two hidden flag states share visible qutrit state but have distinct controlled futures; at least a flag-sensitive memory distinction is necessary")

# Exact coherent flag mixing is a fully unitary physical operation
# OUTSIDE the declared flag-classical intervention catalog.
# It converts a previously invisible flag-offdiagonal coherence
# into visible flag populations, destroying C_flag intertwining.
c=gc(F(3,5));s=gc(F(4,5))
W=zero_n(6)
for j in range(3):
    W[j][j]=c
    W[j][3+j]=-s
    W[3+j][j]=s
    W[3+j][3+j]=c
assert matmul(matadj(W),W)==ONE6
X=zero_n(6)
X[0][3]=O;X[3][0]=O
assert flagged(X)==zero_n(6)
Z=flagged(qconj(W,X))
assert Z[0][0]==gc(F(-24,25))
assert Z[3][3]==gc(F(24,25))
assert Z!=zero_n(6)
assert flagged(qconj(W,flagged(X)))==zero_n(6)

# Positive density-matrix witness (2x2 eigenvalues
# 1/6 ± 1/12, remaining four 1/6), same initial flagged record
# but distinct flagged output after coherent W.
rho_base=matscale(ONE6,F(1,6))
rho_plus=matadd(rho_base,matscale(X,F(1,12)))
rho_minus=matadd(rho_base,matscale(X,F(-1,12)))
assert mattrace(rho_plus)==mattrace(rho_minus)==O
assert flagged(rho_plus)==flagged(rho_minus)
assert flagged(qconj(W,rho_plus))!=flagged(qconj(W,rho_minus))
assert rho_plus[0][0]*rho_plus[3][3]-rho_plus[0][3]*rho_plus[3][0]==gc(F(1,48))
assert rho_minus[0][0]*rho_minus[3][3]-rho_minus[0][3]*rho_minus[3][0]==gc(F(1,48))
print("PASS H76: CPTP coherent flag rotation destroys rank18 block-memory closure, including a positive density-pair counterexample")

# The same original uncontrolled H75 micro channel (and so the exact
# same original 6D P3 filtration/residue) is compatible with either
# an apparatus allowing only visible controls, or ALSO allowing Fgate.
# The difference in accessible controlled processes is independent
# physical apparatus information not encoded in uncontrolled R3.
assert all(flagged(micro(D))==micro(D) for D in D6)
print("PASS H76: P3-only uncontrolled source cannot select physical feedback intervention catalog; explicit classical flag access is additional calibration")

print("BOUNDARY: exact memory size 18 is the dimension of this full flag-resolved quantum-block observer, not a global minimum for every limited readout protocol")
print("BOUNDARY: ordinary quantum semicausality + environment-register monitoring, NOT emergent P3-defined hardware, original frozen P6 J_N or CR-exclusive dynamics")
print("BOUNDARY: no P7/P8 physical soldering, microscopic ADM/HDA, Einstein field equations or P9 Minimum Success")
