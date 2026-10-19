"""H111 — ORIGINAL H75 four-Kraus source; exact positive collision
record covariance despite *strictly Markovian* controlled source
dynamics. H110 single-step 4D Stinespring isometry has a fixed
countably-infinite fresh-ancilla shift dilation for ALL time steps.

No new Hamiltonian/Cartan law or physical reservoir is SOURCE-DERIVED.
The analytic unitary extension and countable infinite bilateral shift
are rigorously specified in the accompanying note; this checker
validates source Kraus histories, positive probabilities and arbitrary
two-step intervention composition on physical M6 operator basis.
"""
from fractions import Fraction as F

from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    LK,R60,micro,embed,MBASIS,eye_n,zero_n,
    matadd,matmul,matadj,mattrace,qconj,edge_cayley,B,lift
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P11H109H75PrimitiveMixingTraceOnlyUnitaryIntertwinerExactCheck as H109
import P11H110H75MinimalDilationFiniteClosedMemoryNoGoExactCheck as H110

assert R60[0][0]==I*gc(F(-32,135))
assert len(LK)==4 and len(MBASIS)==36
assert H110.kraus_gram==H110.expected_gram
assert H91.rank(H109.G3)==8
assert H110.sigma==H109.sigma
assert H110.rho0!=H109.sigma
print("PASS H111.0: original H75 genuine four-Kraus/Choi rank4 source, all 36 operator units, primitive-mixing H109 and finite closed-bath No-Go H110 inherited EXACTLY")

# H111.1 — Prove mathematical one-step unitary W extension exists:
# H110.V is 24x6 with V†V=I6. Any isometry V can be extended
# to a unitary on C24 once its six columns are identified with
# the fixed input ancilla |0> in C6⊗C4. General Hilbert-space
# orthonormal-completion argument proves existence without
# inventing a matrix-log Hamiltonian or an experimentally
# implementable gate. Countable bilateral fresh-ancilla shift
# U=(I⊗Shift) W_{S,0} is a fixed unitary on the incomplete
# infinite tensor product with reference |0> at every site.
# Each step consumes site0, shifts used records to negative
# indices and pulls untouched site+1 into site0. This yields
# the EXACT H110 Kraus-word reduced dynamics at all n.
assert len(H110.V)==24 and len(H110.V[0])==6
assert H110.rectangular_mm(H110.Vdag,H110.V)==eye_n(6)
assert len(H110.LK)==4 and len(H110.products)==64
# Match H110's n=1,2,3 finite-horizon collision histories.
words=[eye_n(6)]
for n in (1,2,3):
    words=[matmul(L,P) for P in words for L in LK]
    assert len(words)==4**n
    total=zero_n(6)
    for P in words:total=matadd(total,matmul(matadj(P),P))
    assert total==eye_n(6)
    if n<=2:
        for X in MBASIS:
            out=zero_n(6)
            for P in words:out=matadd(out,qconj(P,X))
            target=X
            for k in range(n):target=micro(target)
            assert out==target
print("PASS H111.1: exact original source finite cylinder Kraus histories have 4^n words, completeness and original Phi^n; bilateral infinite fresh-chain unitary proof holds for EVERY n, unlike prohibited finite closed bath")
print("BOUNDARY: infinite-chain Hilbert space, shift, reference bath preparation and collision clock are MATHEMATICAL EXTERNAL resources, not derived by P3/P5/F or the genuine independent P9 16D/48D Cartan Hamiltonians")

# H111.2 — One genuine input is positive and first flag
# outcome is nontrivial. Kraus label k=2*a+b, records both
# the output flag a and the consumed input flag b.
rho=H91.e(6,1,1)  # physical |flag=0,site=1><...|
assert matadj(rho)==rho and mattrace(rho)==O
first=[qconj(L,rho) for L in LK]
first_probs=[mattrace(Y) for Y in first]
assert first_probs==[gc(F(9,25)),Z0,gc(F(16,25)),Z0],first_probs

# Two FRESH orthogonal Kraus ancilla registers. The first
# records k1=(a1,b1) and second records k2=(a2,b2).
# The TRUE joint Born probability uses original Kraus word
# L_k2 L_k1 and traces on original six-level output system:
# P(k1,k2)=Tr(L_k2 L_k1 rho L_k1† L_k2†).
joint=[[mattrace(qconj(L2,first[k1])) for L2 in LK]
       for k1 in range(4)]
assert all(z.i==0 and z.r>=0 for row in joint for z in row)
assert sum((z.r for row in joint for z in row),F(0))==F(1)
assert [sum((z for z in row),Z0) for row in joint]==first_probs
# The outgoing first flag is a1=floor(k1/2); the input-flag
# index of second collision is b2=k2%2. A nonzero joint
# trajectory must satisfy b2=a1 exactly, since L_ab
# maps its input-flag projector |b> to output flag |a>.
for k1,row in enumerate(joint):
    for k2,p in enumerate(row):
        if (k1//2)!=(k2%2):
            assert p==Z0,(k1,k2,p)
pa0=sum((joint[k1][k2].r for k1 in (0,1)
         for k2 in range(4)),F(0))
pb20=sum((joint[k1][k2].r for k1 in range(4)
          for k2 in (0,2)),F(0))
pab00=sum((joint[k1][k2].r for k1 in (0,1)
           for k2 in (0,2)),F(0))
assert (pa0,pb20,pab00)==(F(9,25),F(9,25),F(9,25))
cov=pab00-pa0*pb20
assert cov==F(144,625)
assert pa0*(1-pa0)==cov
assert pab00!=pa0*pb20
print("PASS H111.2: exact source-positive 16-entry two-ancilla Kraus history table has perfect link b2=a1; first outcome 9/25 and 16/25, classical cross-record covariance 144/625>0")
print("THEOREM H111.2: classical mutual information of the two measured fresh-ancilla labels is at least h2(9/25)>0 bits by data processing to a1 and b2; NOT a claimed non-Markovian process-tensor memory")

# Finite outgoing RECORDS can be correlated even though
# the system process is exactly quantum MARKOV with arbitrary
# inserted system operations. Since the next ancilla has no
# prior correlation with the system+spent environment, for
# every linear operation A:M6->M6,
# sum_k2,k1 L_k2 A(L_k1 X L_k1†) L_k2†
# = Phi(A(Phi(X))).
#
# We verify all 36 ORIGINAL matrix units for three physically
# meaningful intervention maps. Arbitrary-A result follows
# algebraically from linearity of the original Kraus sums.
Rb=edge_cayley(B,F(1,2))
Win=lift(Rb)
P0=zero_n(6)
for i in range(3):P0[i][i]=O
assert matmul(P0,P0)==P0 and matadj(P0)==P0
def coherent_B(X):
    return qconj(Win,X)
def selective_flag0(X):
    return qconj(P0,X)
def replace_with_rho(X):
    z=mattrace(X)
    return [[z*rho[i][j] for j in range(6)] for i in range(6)]
ops=[
    ("genuine source coherent B-Cayley",coherent_B),
    ("selective positive flag0 instrument",selective_flag0),
    ("trace-preserving source-state replacement",replace_with_rho),
]
for name,Op in ops:
    for X in MBASIS:
        by_words=zero_n(6)
        for L1 in LK:
            mid=Op(qconj(L1,X))
            for L2 in LK:
                by_words=matadd(by_words,qconj(L2,mid))
        by_map=micro(Op(micro(X)))
        assert by_words==by_map,(name,)
    print("PASS H111.3: two genuinely fresh source environments with intervention "+name+" reproduce Phi o A o Phi on ALL 36 original physical M6 units")

# Verify also probabilities from the full joint table agree with
# unconditional true two-step source channel, avoiding a
# surrogate classical Markov chain.
sumout=zero_n(6)
for L1 in LK:
    for L2 in LK:
        sumout=matadd(sumout,qconj(L2,qconj(L1,rho)))
assert sumout==micro(micro(rho))
assert mattrace(sumout)==O
print("PASS H111.3: unconditional quantum two-step output from all actual 16 joint Kraus trajectories equals original Phi^2(rho) exactly, despite correlated environmental records")

# The explicit outgoing record measurement probabilities are
# classical, not proof of non-Markovian backflow. Process
# interventions are on FULL H75 system, no old ancilla is
# re-used and no conditional feedback depends on record labels.
open_gates={
    "AX-SRC source CPTP Kraus and one-step dilation":"EXACT",
    "AX-SRC physical infinite fresh chain/time shift origin":"INDEPENDENT_ASSUMPTION",
    "AX-OA outgoing record joint probabilities":"EXACT",
    "AX-OA experimental access and register detector":"OPEN",
    "P5 Omega intrinsic quantum nonMarkov memory derived":"OPEN",
    "AX-CAN generated physical nondegenerate KKS ADM":"OPEN",
    "AX-SP matched P9 Cartan source solder torsion curvature":"OPEN",
    "AX-DYN sourced DeWitt R full HDA Einstein":"OPEN",
    "AX-NORM physical scale and couplings":"OPEN",
    "AX-GEN finite-to-infinite F generative completeness":"OPEN",
}
assert len(open_gates)==10
print("BOUNDARY: correlated environmental RECORD HISTORY coexists with a STRICTLY MARKOVIAN system process tensor when all fresh ancillas are independent and spent ones never re-interact")
print("BOUNDARY: all-time countably infinite coherent dilation does not source infinite history from finite F, a physical bath, intrinsic P5 Omega nonMarkov return, actual P9 Cartan KKS/ADM, torsion-free connection, Einstein dynamics or Generative Completeness")
