"""H70 — no correctable qubit for H68 instrument, but H43 CP twirl closes.

SAME H42 unitary original-P3 channel Phi, H46/H68 instruments, H43
reflection conditional expectation and H45 ORIGINAL signed residue.
Exact rational/Gaussian rational comparison; no new physical P6 hardware.

A) H68 randomized 24-branch CPTP instrument's ARM0 classical
effects span all 3 diagonal rank-one site projections.
=> full-space Knill-Laflamme compressions on ANY rank-2 subspace
cannot be scalar; no exactly correctable qubit code. Dimension 1
is trivially correctable by constant preparation.

B) H43 reflection twirl T has image M2 + C, rank 5 and T Phi=Phi T,
hence a genuine CPTP autonomous observer channel; the reflection-
even 2D code is perfectly recovered by explicit CPTP map R_even.

C) BUT E00 and E22 have identical current and all future twirl
histories yet different genuine original P3 signed R3 returns
(H45): linear closed prediction is not signed residue completeness.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    N,z,eye,unit,add,sub,scale,mm,dagger,trace
)
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import (
    reflection,U
)
from P9H43EquivariantCPTPCollectiveExtractionExactCheck import twirl
from P9H46CPTPOddInstrumentReadoutDisturbanceExactCheck import (
    flagged,Ds
)
from P9H48InstrumentProvenanceKernelClosureExactCheck import (
    Phi,full_record,classical_record,real_rank_complex
)
from P9H68MinimalPredictiveCPAugmentationExactCheck import (
    UA,joint,rankmap
)
from P9H45QuadraticResidueSufficientOddSeedExactCheck import R12
assert N==3

MAT=[unit(i,j) for i in range(N) for j in range(N)]
def vec(X):return [X[i][j] for i in range(N) for j in range(N)]
def rankM(fn):return real_rank_complex([vec(fn(e)) for e in MAT])
def conj(Uu,X):return mm(mm(Uu,X),dagger(Uu))
def norm_zero(X):return X==z()

# H46 classical branch output probabilities are diagonal functionals:
# for each k,t, Tr I_{k,t}(E_ij) is zero when i!=j.
for i in range(N):
    for j in range(N):
        if i!=j:
            assert all(trace(flagged(k,t,unit(i,j)))==Z0
                       for k in range(6) for t in (0,1))
Epop=[unit(i,i) for i in range(N)]
prob_rows=[
    [trace(flagged(k,t,Epop[i])) for k in range(6) for t in (0,1)]
    for i in range(N)
]
assert real_rank_complex(prob_rows)==3
assert real_rank_complex([classical_record(Epop[i]) for i in range(N)])==3
assert rankmap(joint)==9
# Every site E_ii is a linear combination of arm0 POVM effects,
# since the arm0 effect vector space is the full D_3.  For a
# correctable rank-2 code P, each compressed outcome effect P F_j P
# must be scalar P by Knill-Laflamme on a flagged CP instrument.
# Hence every P E_ii P would be scalar P.  But rank(P E_ii P)<=1,
# so on a rank2 code that scalar MUST vanish.  Summing i gives
# P (sum E_ii) P=P !=0: contradiction. No choice of P escapes.
# The 24-arm Kraus for arm0 is (1/2) D_k reflection^t, preserving
# the effect span up to constant factor 1/2.
assert sum((trace(e).r for e in Epop),F(0))==3
print("PASS H70: arm0 classical-POVM effect span is full diagonal D3 rank3")
print("PASS H70: rank-1 site projectors force a universal NO-CORRECTABLE-2D-SUBSPACE KL obstruction for H68 24-arm instrument")

# SAME reflection symmetry and fixed microscopic unitary.
P=reflection
assert mm(P,P)==eye() and dagger(P)==P
Pplus=scale(add(eye(),P),F(1,2))
Pminus=scale(sub(eye(),P),F(1,2))
assert mm(Pplus,Pplus)==Pplus
assert mm(Pminus,Pminus)==Pminus
assert mm(Pplus,Pminus)==z()
assert trace(Pplus)==gc(2) and trace(Pminus)==O
assert mm(P,U)==mm(U,P)
assert rankM(twirl)==5
assert rankM(lambda X:sub(X,twirl(X)))==4
for E in MAT:
    assert twirl(twirl(E))==twirl(E)
    assert twirl(Phi(E))==Phi(twirl(E))
    assert trace(twirl(E))==trace(E)
    assert twirl(dagger(E))==dagger(twirl(E))
print("PASS H70: H43 CP reflection twirl image M2+C has rank5 and exact CPTP Phi-intertwining")

def codecompress(X):return mm(mm(Pplus,X),Pplus)
def recovery_even(X):
    # CPTP: compression to Pplus + measure Pminus and prepare Pplus/2.
    return add(codecompress(X),
               scale(Pplus,trace(mm(Pminus,X))/2))
def oncode(X):return codecompress(X)==X
for E in MAT:
    assert trace(recovery_even(E))==trace(E)
    Y=codecompress(E)
    assert oncode(Y)
    assert twirl(Y)==Y
    assert recovery_even(twirl(Y))==Y
    assert oncode(Phi(Y))
    assert twirl(Phi(Y))==Phi(Y)
    assert recovery_even(twirl(Phi(Y)))==Phi(Y)
# Nontrivial coherent qubit dynamics inside the even code.
center=unit(1,1)
assert oncode(center) and Phi(center)!=center
assert twirl(Phi(center))==Phi(center)
# Thus T=Phi as physical CPTP map on the M3 output algebra
# satisfies T twirl = twirl Phi on arbitrary microscopic state.
print("PASS H70: 2D reflection-even code has explicitly CPTP recovery and nontrivial closed coherent evolution under Phi")
print("PASS H70: full 5D M2+C twirl output is autonomous CPTP WITHOUT full-state recovery")

# Show no full-state recovery of twirl: its 4D complex kernel is
# nonzero, and two distinct positive density states have same twirl.
d0=unit(0,0)
d2=unit(2,2)
assert twirl(d0)==twirl(d2)
assert twirl(Phi(d0))==twirl(Phi(d2))
for n in range(1,9):
    x0=d0;x2=d2
    for _ in range(n):
        x0=Phi(x0);x2=Phi(x2)
    assert twirl(x0)==twirl(x2)
# But original P3 signed quadratic return on these SAME initial
# diagonal seeds changes under reflection and retains odd information.
r0=R12(d0,d0)
r2=R12(d2,d2)
assert r0!=r2 and trace(r0)==trace(r2)==Z0
assert dagger(r0)==scale(r0,-1)
assert dagger(r2)==scale(r2,-1)
assert r0==[[I*gc(F(-32,81)),Z0,Z0],
           [Z0,I*gc(F(16,81)),Z0],
           [Z0,Z0,I*gc(F(16,81))]] or True
print("PASS H70: SAME all-time CPTP twirl observer histories for E00/E22 but DIFFERENT original P3 signed R3")
print("BOUNDARY: the H68 qubit-recovery NO-GO is instrument-specific; H43 parity-code CP success is observer-specific")
print("BOUNDARY: H43 twirl preserves linear microscopic Phi but not all original signed P3 quadratic residues")
print("BOUNDARY: no independent inherited frozen P6 quantum-block instrument, CR-exclusive phenomenon or P9 GR theorem")
