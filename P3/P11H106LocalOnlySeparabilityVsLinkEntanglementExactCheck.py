"""H106: same genuine H75 two-cell source and already-existing H105
conditional link. NO newly postulated Hamiltonian is introduced here.

Every control generated only by the ORIGINAL local A/B Hamiltonian
catalog belongs to so3⊕so3 and factors across cells. Local source
CPTP reset and local feedforward cannot entangle a separable state.
The independently POSTULATED H105 controlled-X link, although exactly
compatible with the unchanged 16 original H75×H75 Kraus operators,
does entangle a product state and leaves a rigorously NPT genuine
flag00 positive-output branch. All four coarse flags are unchanged.

Exact Fraction/Gaussian-rational certificates: Lie locality, local
Hamiltonian exclusion commutator/partial trace, Schmidt determinant,
reduced purity 17/25, flag00 p=153/625, PT minor -2916/390625,
normalized pure-state negativity 6/17. NOT source-created GR/Cartan.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    A,B,M0,M1,R60,matmul,matadj,mattrace,eye_n,zero_n
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P11H105TwoCellConditionalCoherentCanonicalTransportExactCheck as H105

assert R60[0][0]==I*gc(F(-32,135))
assert len(H105.Mpair)==4
assert H91.mm(H91.dag(H105.R),H105.R)==eye_n(9)
assert H105.H_X==H105.kron(H105.X,H105.P1)
assert H105.H_Y==H105.kron(H105.Y,eye_n(3))
assert H105.pb(H105.H_X,H105.H_Y)==F(1)
print("PASS H106.0: reused exact physical H75 x H75 source and H105 pre-existing hypothetical link unchanged; original P3 nonzero signed residue maintained")

I3=eye_n(3)
I9=eye_n(9)
ZERO9=zero_n(9)
def skew_real_vec(K):
    return [z.r for row in K for z in row]+[z.i for row in K for z in row]
C=H91.comm(A,B)
local_first=[H105.kron(K,I3) for K in (A,B,C)]
local_second=[H105.kron(I3,K) for K in (A,B,C)]
local=local_first+local_second
assert H91.rank([skew_real_vec(K) for K in local])==6
assert all(H91.comm(K,L)==ZERO9 for K in local_first for L in local_second)
assert all(H91.dag(K)==H91.scale(K,-1) for K in local)
for K in local_first:
    for L in local_first:
        assert H91.rank([skew_real_vec(V) for V in local_first]+[
            skew_real_vec(H91.comm(K,L))])==3
for K in local_second:
    for L in local_second:
        assert H91.rank([skew_real_vec(V) for V in local_second]+[
            skew_real_vec(H91.comm(K,L))])==3
print("PASS H106.1: full locally generated original source Hamiltonian Lie algebra is exact so3⊕so3 (real rank6), all cross-cell commutators vanish, all time-dependent coherent protocols remain local products")

# The fixed H105 controlled-X link cannot equal K⊗I+I⊗L even
# allowing arbitrary K,L in M3(C), hence cannot occur in the much
# smaller original site real Lie algebra.
Q=H91.hermX(3,0,1)
witness=H91.comm(H105.H_X,H105.kron(I3,Q))
assert witness==H105.kron(H105.X,H91.comm(H105.P1,Q))
assert witness!=ZERO9
def ptr_first(X):
    return [[sum((X[3*a+i][3*a+j] for a in range(3)),Z0)
             for j in range(3)] for i in range(3)]
assert ptr_first(witness)==zero_n(3)
# If Hlink were K⊗I + I⊗L, the same commutator would
# I⊗[L,Q], whose partial trace would be 3[L,Q]. Since ptr1=0,
# it would force [L,Q]=0, and witness=0, contradiction.
assert H91.tr(H105.X)==Z0
assert H105.H_X not in local
print("PASS H106.1: operator-algebraic partial-trace commutator certificate excludes original H105 controlled X⊗P link from ALL local Hamiltonian sums K⊗I + I⊗L, not merely source-real generators")

# A genuinely positive separable PRODUCT input with entirely rational
# density matrix: cell1=|1><1|, cell2=(|0>+|1>)(<0|+<1|)/2.
plus=zero_n(3)
for i in (0,1):
    for j in (0,1):plus[i][j]=gc(F(1,2))
assert H91.dag(plus)==plus and H91.tr(plus)==O
assert H91.mm(plus,plus)==plus
rho=H105.kron(H105.P1,plus)
assert H91.dag(rho)==rho and H91.tr(rho)==O
assert H91.mm(rho,rho)==rho
assert rho[3][3]==rho[3][4]==rho[4][3]==rho[4][4]==gc(F(1,2))
rhoR=H91.mm(H91.mm(H105.R,rho),H91.dag(H105.R))
assert H91.dag(rhoR)==rhoR and H91.tr(rhoR)==O
assert H91.mm(rhoR,rhoR)==rhoR
# R maps the unnormalized (|1,0>+|1,1>)/sqrt2 to
# (|1,0> + (3/5)|1,1> -(4i/5)|2,1>)/sqrt2.
v=[Z0 for _ in range(9)]
v[3]=O
v[4]=gc(F(3,5))
v[7]=-I*gc(F(4,5))
expect_rho=[[v[i]*v[j].conj()*gc(F(1,2))
             for j in range(9)] for i in range(9)]
assert rhoR==expect_rho
# Matrix 2x2 for first site rows 1,2 vs cell2 columns 0,1.
# Unnormalized minor det=-4i/5; normalized minor det=-2i/5.
assert v[3]*v[7]-v[4]*v[6]==-I*gc(F(4,5))
assert (v[3]*v[7]-v[4]*v[6])*gc(F(1,2))==-I*gc(F(2,5))
def ptr_second(X):
    return [[sum((X[3*i+b][3*j+b] for b in range(3)),Z0)
             for j in range(3)] for i in range(3)]
red=ptr_second(rhoR)
pur=H91.tr(H91.mm(red,red))
assert pur.i==0 and pur.r==F(17,25)
assert H91.tr(H91.mm(ptr_second(rho),ptr_second(rho)))==O
print("PASS H106.2: conditional H105 link converts exact positive product input into pure Schmidt-rank2 entangled state; first-cell reduced purity changes 1 -> 17/25, IMPOSSIBLE for any original local-unitary protocol")

# Same actual H75 H75 four-flag outcomes for the ORIGINAL product
# input and the conditional entangled one. Strong commutation of
# H105.R with each real positive attenuator assures equality of all
# four physical source flag-pair outcomes.
prob_native=[]
prob_link=[]
for M in H105.Mpair:
    assert H91.comm(M,H105.R)==ZERO9
    pi=H91.tr(H91.mm(H91.mm(M,rho),M))
    pl=H91.tr(H91.mm(H91.mm(M,rhoR),M))
    assert pi.i==pl.i==0
    assert pi==pl
    assert pi.r>=0
    prob_native.append(pi.r)
    prob_link.append(pl.r)
assert sum(prob_native,F(0))==sum(prob_link,F(0))==1
assert prob_native==prob_link
print("PASS H106.3: ALL FOUR genuine unchanged H75xH75 coarse flag-pair probabilities are IDENTICAL for local-only product and hypothetical coherent-link entangled preparations")

# The true original output 00 Kraus block is U⊗U M00 rho M00
# (U⊗U)dag. A local U⊗U basis calibration does NOT change cell
# entanglement. Work with the unrotated 9D physical block sigma00.
M00=H105.Mpair[0]
sig=H91.mm(H91.mm(M00,rhoR),M00)
sigi=H91.mm(H91.mm(M00,rho),M00)
assert H91.dag(sig)==sig
assert H91.tr(sig).i==0 and H91.tr(sigi).i==0
p=H91.tr(sig).r
assert p==F(153,625)
assert H91.tr(sigi).r==p
u=[Z0 for _ in range(9)]
u[3]=gc(F(3,5))
u[4]=gc(F(27,125))
u[7]=-I*gc(F(36,125))
assert sig==[[u[i]*u[j].conj()*gc(F(1,2))
             for j in range(9)] for i in range(9)]
out=H91.mm(H91.mm(H105.U2,sig),H91.dag(H105.U2))
assert H91.tr(out).r==p and H91.dag(out)==out

# Exact partial transpose on SECOND site. The 2x2 principal
# submatrix of sig^{T2} indexed by |1,1> and |2,0> has determinant
# strictly negative. Thus sig is NOT PPT -> NOT separable.
def partial_transpose_second(X):
    return [[X[3*(i//3)+(j%3)][3*(j//3)+(i%3)]
             for j in range(9)] for i in range(9)]
pt=partial_transpose_second(sig)
assert H91.dag(pt)==pt
assert pt[4][6]==I*gc(F(54,625))
assert pt[6][4]==-I*gc(F(54,625))
assert pt[6][6]==Z0
minor=pt[4][4]*pt[6][6]-pt[4][6]*pt[6][4]
assert minor.i==0 and minor.r==F(-2916,390625)<0
# Original positive local flag00 product output is manifestly a
# tensor product of local positive flagged effects, separable.
a=H91.mm(H91.mm(M0,H105.P1),M0)
b=H91.mm(H91.mm(M0,plus),M0)
assert sigi==H105.kron(a,b)
# For a Schmidt rank2 PURE output branch, negativity is the
# product of the two normalized Schmidt coefficients. Equivalently
# the magnitude of the normalized 2x2 coefficient determinant.
norm_det=F(54,625)/p
assert norm_det==F(6,17)
print("PASS H106.4: same TRUE original flag00 CPTP probability 153/625, but conditional link branch is NPT with principal PT minor -2916/390625 and normalized pure-state entanglement negativity 6/17; local-only flag00 is separable")

# No closed-system source-native local protocols, nor local CPTP
# operations and (possibly classically correlated) local instruments,
# can generate a NPT output branch from an initially separable
# two-cell state without a physical quantum intercell operation.
# This is the mathematical separable-map/LOCC invariant, not a
# claim that an untested physical experimental implementation
# of the H105 link has occurred.
assert H91.tr(H91.mm(H105.seed,H105.seed)).i==0
status={
 "AX-SRC original local H75 source":"EXACT",
 "AX-OA coarse flags distinguish link entanglement":"NO-GO",
 "AX-CAN native local Hamiltonian entangler":"NO-GO",
 "AX-CAN H105 EXTRA controlled link CPTP compatibility":"CONDITIONAL EXACT",
 "AX-CAN H105 EXTRA link physical existence":"OPEN",
 "AX-SP verified same-source P9 Cartan intercell solder":"OPEN",
 "AX-DYN sourced ADM/DeWitt/Einstein":"OPEN",
 "AX-NORM F physical coupling normalizations":"OPEN",
 "AX-GEN actual generative completeness":"OPEN",
}
assert len(status)==9
print("BOUNDARY: hypothetical link creates ordinary-QM entanglement IF separately physically sourced; NO H75 original-local protocol, real or complex source-allowed local controls plus local H75 CPTP operations, can create it from separable input")
print("BOUNDARY: P9.125-128 Cartan micro/source/observer unavailable as independently matching original H75; no source-derived spatial curvature, six canonical ADM pairs, DeWitt/HDA/Einstein or P11 F completeness")
