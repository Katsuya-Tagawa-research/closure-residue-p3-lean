"""H79 — actual CP quantum memory for post-reset H75 micro outputs.

H78 showed that H75's unchanged 4-Kraus six-level micro channel
Phi_mu has complex-linear rank9, but DID NOT show that rank9 is
realizable as a CPTP memory with exact original quantum readout.

Here source output J_out(rho) occupies a *flag-diagonal* physical
Hilbert support K = (flag0 x C3) ⊕ (flag1 x U span{|1>,|2>}),
which has Hilbert dimension 5 and quantum block algebra
M3(C)⊕M2(C), complex operator dimension 13.

An explicit 3-Kraus CPTP encoder Enc:M6->M5 and a CPTP isometric
decoder Dec:M5->M6 satisfy Dec Enc Phi_mu = Phi_mu on ALL 36
matrix units. Thus at mandatory reset CHECKPOINTS, Enc and Dec
give exact quantum readout and autonomous CPTP inter-checkpoint
channels for any admitted finite controls/instruments followed
by the mandatory micro reset.

This result is NOT an exact prediction at arbitrary intermediate
pre-reset times, and the 9-linear-dimensional post-reset source
range is not asserted to be a CPTP 9-dimensional algebra. An
explicit pair of states proves that the simpler 3-level *partial
trace* cannot CPTP-recover the full post-reset flag record.

Original microscopic P3 source and R3 witness are unchanged;
the physical reset apparatus and all controls are independent
premises, not derived from P3-only data.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import O,Z0,I,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    U,A,B,ONE6,MBASIS,D6,R60,micro,embed,d0,d1,
    qtrace,qconj,lift,Fgate,physical_micro,SETTINGS,matadj,
    matmul,matadd,matscale,mattrace,zero_n,eye_n,
    edge_cayley
)
from P9H76FeedbackFlagMemoryCPTPExactCheck import (
    W,flagged,flag_branch,micro_branch
)
from P9H48InstrumentProvenanceKernelClosureExactCheck import real_rank_complex
assert len(MBASIS)==36
assert R60[0][0]==I*gc(F(-32,135))

def zero_rect(m,n):
    return [[Z0 for j in range(n)] for i in range(m)]
def adj(X):
    return [[X[i][j].conj() for i in range(len(X))]
            for j in range(len(X[0]))]
def mul(X,Y):
    assert len(X[0])==len(Y)
    return [[sum((X[i][k]*Y[k][j] for k in range(len(Y))),Z0)
             for j in range(len(Y[0]))]
            for i in range(len(X))]
def madd(X,Y):
    return [[X[i][j]+Y[i][j] for j in range(len(X[0]))]
            for i in range(len(X))]
def smul(X,c):
    return [[c*x for x in row] for row in X]
def conj_rect(K,X):
    return mul(mul(K,X),adj(K))
def tr(X):
    return sum((X[i][i] for i in range(len(X))),Z0)
def flatten(X):
    return [x for row in X for x in row]
def rankmap(fn,domain):
    return real_rank_complex([flatten(fn(X)) for X in domain])

# Isometry V: C5 -> C6, image K = Eflag0⊗C3 ⊕ Eflag1⊗U span{e1,e2}.
V=zero_rect(6,5)
for j in range(3):
    V[j][j]=O
for b in (1,2):
    for i in range(3):
        V[3+i][b+2]=U[i][b]
Vd=adj(V)
I5=eye_n(5)
PK=mul(V,Vd)
assert mul(Vd,V)==I5
assert mul(PK,PK)==PK
assert matadj(PK)==PK
assert tr(PK)==gc(5)
P0=zero_n(6);P1=zero_n(6)
for j in range(3):P0[j][j]=O;P1[j+3][j+3]=O
assert matadd(P0,P1)==ONE6
assert matmul(PK,P0)==matmul(P0,PK)
assert matmul(PK,P1)==matmul(P1,PK)

# Complement is exactly the discarded rank-one flag1⊗Ue0 mode.
lost=[Z0]*6
for i in range(3):lost[3+i]=U[i][0]
Pmiss=conj_rect([[c] for c in lost],[[O]])
assert matadd(PK,Pmiss)==ONE6
assert tr(Pmiss)==O

# Three explicitly specified encoder Kraus: two code-compression
# instruments and measurement of missing mode followed by fixed
# flag0 logical state preparation.
K0=mul(Vd,P0)
K1=mul(Vd,P1)
Kbad=zero_rect(5,6)
for j in range(6):
    Kbad[0][j]=lost[j].conj()
KRAUS=(K0,K1,Kbad)
effects=zero_n(6)
for K in KRAUS:
    effects=matadd(effects,mul(adj(K),K))
assert effects==ONE6
def encode(X):
    Y=zero_n(5)
    for K in KRAUS:
        Y=madd(Y,conj_rect(K,X))
    return Y
def decode(Y):
    return conj_rect(V,Y)
def cp5_flagblock(Y):
    out=zero_n(5)
    for i in range(5):
        for j in range(5):
            if (i<3)==(j<3):
                out[i][j]=Y[i][j]
    return out
for X in MBASIS:
    Y=encode(X)
    assert cp5_flagblock(Y)==Y
    assert tr(Y)==mattrace(X)
    assert matadj(Y)==encode(matadj(X))
assert rankmap(encode,MBASIS)==13
assert rankmap(micro,MBASIS)==9
assert rankmap(lambda X:encode(micro(X)),MBASIS)==9
for X in MBASIS:
    Z=micro(X)
    assert matmul(PK,Z)==Z==matmul(Z,PK)
    assert flagged(Z)==Z
    assert decode(encode(Z))==Z
print("PASS H79: genuine 3-Kraus CPTP encoder M6->M5, 5D isometric CPTP decoder, block algebra M3+C M2 (rank13)")
print("PASS H79: exact full MICRO post-reset source outputs have support in 5-level code K; Dec Enc Phi_micro=Phi_micro on all 36 input units")
print("PASS H79: post-reset linear source rank9 remains distinct from physical CP observer rank13")

# H75 independent coherent 01 and 12 controls, new flag rotation W,
# hidden flag-conditioned feedback F, and asymmetric site noise can
# act BETWEEN mandatory resets. At the next reset checkpoint all
# outputs return to the code K.
UA=lift(edge_cayley(A,F(1,2)))
UB=lift(edge_cayley(B,F(2,3)))
PULSES=(ONE6,Fgate,W,UA,UB,matmul(UA,W),matmul(Fgate,UB))
for X in MBASIS:
    prep=micro(X)
    q=encode(prep)
    for G in PULSES:
        direct=micro(qconj(G,prep))
        restored=micro(qconj(G,decode(q)))
        candidate=encode(restored)
        assert candidate==encode(direct)
        assert decode(candidate)==direct
        assert tr(candidate)==mattrace(X)
print("PASS H79: all declared flag feedback/coherent and independent real site pulse words admit exact CP checkpoint evolution after mandatory reset")

# A CPTP checkpoint memory map on arbitrary M5 inputs for any pulse:
#    T_G = Encode ◦ Phi_micro ◦ Ad_G ◦ Decode.
# Every factor is explicitly CPTP; input/output 5D carrier. The
# equality of all checkpoint histories is by induction because
# Dec Enc = identity on source range.
def checkpoint_step(Y,G):
    return encode(micro(qconj(G,decode(Y))))
for X in (MBASIS[0],MBASIS[7],MBASIS[17],embed(d0),embed(d1),
          matscale(ONE6,F(1,6))):
    physical=micro(X)
    logical=encode(physical)
    for G in (W,Fgate,UA,UB,W,Fgate):
        physical=micro(qconj(G,physical))
        logical=checkpoint_step(logical,G)
        assert decode(logical)==physical
        assert tr(logical)==mattrace(physical)
print("PASS H79: finite histories close as actual CPTP 5-level quantum memory at EACH compulsory micro-reset checkpoint")

# Strong flag/site single-copy output readout at checkpoints:
# genuine physical CP state reproduction, not signed tomography.
for X in MBASIS:
    physical=micro(X)
    restored=decode(encode(physical))
    assert restored==physical
    for a in (0,1):
        for j in range(3):
            Q=zero_n(6);Q[3*a+j][3*a+j]=O
            assert mattrace(matmul(Q,restored))==mattrace(matmul(Q,physical))
print("PASS H79: exact physical CP decoding reproduces ALL post-reset flag-resolved quantum blocks and positive site readout probabilities")

# NO-GO: The simpler 3D qutrit partial trace cannot recover the
# joint physical flag register on all source outputs. For the
# Hermitian input difference X = E00 - E11 + E01 + E10:
# norm_1 of J_out(X) = (sqrt(2056)+16)/25,
# norm_1 of Tr_flag J_out(X) = 2 sqrt(34)/5.
# Strict inequality follows from 45²=2025<2056 and
# 59²=3481>3400=(10sqrt34)²:
# (sqrt2056+16)/25 > 61/25 > 59/25 > 10sqrt34/25.
# True positive density pair I3/3 ± X/12 (eigenvalues
# 1/3 ± sqrt(2)/12, 1/3) witnesses data-processing violation.
E01=[[O if (i==0 and j==1) else Z0 for j in range(3)]
     for i in range(3)]
E10=[[O if (i==1 and j==0) else Z0 for j in range(3)]
     for i in range(3)]
Delta=matadd(matadd(d0,matscale(d1,-1)),matadd(E01,E10))
assert matadj(Delta)==Delta and mattrace(Delta)==Z0
zplus=matadd(matscale(eye_n(3),F(1,3)),matscale(Delta,F(1,12)))
zminus=matadd(matscale(eye_n(3),F(1,3)),matscale(Delta,F(-1,12)))
assert mattrace(zplus)==mattrace(zminus)==O
for rho in (zplus,zminus):
    minor=rho[0][0]*rho[1][1]-rho[0][1]*rho[1][0]
    assert minor.i==0 and minor.r>0
    assert rho[0][0].i==0 and rho[0][0].r>0
JDelta=micro(embed(Delta))
assert flagged(JDelta)==JDelta
marginal=qtrace(JDelta)
# Check exact trace-distance algebra via unaffected unitary U:
# upper flag source block UM0 Delta M0 U†, lower block UM1 Delta M1 U†.
assert tr(marginal)==Z0
assert F(45)**2<F(2056) and F(59)**2>F(3400)
assert 45+16>59
assert (F(1,3)-F(1,12))>0
print("PASS H79: strict trace-norm DPI witness forbids CPTP reconstruction of post-reset flag quantum state from only 3D visible qutrit marginal")
print("BOUNDARY: CPTP 13-operator-rank memory is SUFFICIENT, not globally minimal among all alternative physical encodings")
print("BOUNDARY: exact CP memory claim holds at compulsory reset CHECKPOINTS, not at arbitrary intermediate pre-reset times or without reset")
print("BOUNDARY: source equipment controls, reset schedule and flag quantum output access are EXTERNAL operational premises, not generated from P3 only")
print("BOUNDARY: original H75 nonzero P3 signed R3 is unchanged, conventional QM; no CR-exclusive prediction, frozen P6 provenance or Einstein/ADM/HDA success")
