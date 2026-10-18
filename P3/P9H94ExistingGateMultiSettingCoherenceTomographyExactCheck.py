"""H94: exact MULTI-SETTING classical tomography, not quantum coherent ADM.

Uses ONLY original H75/H76 real physical gate matrices W,F,UA and
original four-Kraus micro reset, plus standard positive site POVMs.
Conditional on the EXTRA operational premise that pre-reset sequences
of W/F/UA and reproducible coherent H92 input copies are accessible.
Does not infer a code-preserving U5 Hamiltonian or source-generated GR.
"""
from fractions import Fraction as F
from itertools import combinations

from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    micro,qtrace,visible,matmul,matadj,qconj,mattrace,
    ONE6,UM,M0,M1,R60
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P9H92FiveLevelGrassmannKKSResetSilenceExactCheck as H92
import P9H93ExistingRealControlGrassmannAccessExactCheck as H93

assert R60[0][0]==I*gc(F(-32,135))
assert H93.real_orbit_rank==12 and H93.cross_response_rank==9
assert H92.pairs==tuple((a,b) for a in range(3) for b in range(3,5))
assert H91.rank([H91.block_coords(H91.J5(B)) for B in H91.traceless])==8

def d3(X):
    return H91.tr(X)

# Original source entirely factors via the partial trace, and U
# occurs DOWNSTREAM of the destructive flag erasure. Test all 36
# matrix units of the original 6D micro quantum operator domain.
from P9H75SemicausalMicroMemorySourceExactCheck import MBASIS
for X in MBASIS:
    reduced=qtrace(X)
    target=H91.zero(6)
    for a in (0,1):
        Z=H91.mm(H91.mm((M0,M1)[a],reduced),(M0,M1)[a])
        Z=H91.mm(H91.mm(H92.U,Z),H91.dag(H92.U))
        for i in range(3):
            for j in range(3):target[3*a+i][3*a+j]=Z[i][j]
    assert micro(X)==target
    assert qtrace(micro(X))==visible(qtrace(X))
print("PASS H94.1: exact all-36-matrix-unit reset factorization through flag partial trace; fixed complex H42 U is downstream of erasure")

# The positive reduced qutrit channel is injective as a LINEAR map:
# M0 Z M0 + M1 Z M1 is a Schur multiplier with strictly positive
# entry factors c00=1, c01=c02=3/5, c11=c12=c22=1.
coeff=((F(1),F(3,5),F(3,5)),
       (F(3,5),F(1),F(1)),
       (F(3,5),F(1),F(1)))
for a in range(3):
    for b in range(3):
        X=H91.e(3,a,b)
        got=H91.mm(H91.mm(H92.U,H91.plus(H91.mm(H91.mm(M0,X),M0),
                      H91.mm(H91.mm(M1,X),M1))),H91.dag(H92.U))
        expected=H91.mm(H91.mm(H92.U,H91.scale(X,gc(coeff[a][b]))),H91.dag(H92.U))
        assert got==expected
assert all(c>0 for row in coeff for c in row)
print("PASS H94.1: reduced qutrit H75 CPTP channel is injective on all nine complex qutrit matrix units")

# H92 source-seeded full Gr2(C5) 12D complex-KKS tangent basis,
# physically embedded in the actual H75 six-level Hilbert space.
tangents=[
    H92.decode5(H92.scale(H92.comm(Q,H92.sigma),-I))
    for Q in H92.allobs
]
assert len(tangents)==12 and H91.rank([H93.v36(T) for T in tangents])==12
assert all(qtrace(micro(T))==H91.zero(3) for T in tangents)
print("PASS H94.1: ORIGINAL unswitched micro reset annihilates ALL twelve genuine 6D source-seeded Grassmann tangents")

gates={"W":H93.controls["W"],"F":H93.controls["F"],
       "UA":H93.controls["UA"]}
words=(
    ("W","F","UA","F"),
    ("F","W","F"),
    ("W","F"),
    ("UA","F","W","F"),
)

def word_gate(word):
    G=ONE6
    for g in word:
        G=matmul(gates[g],G)
    assert matmul(matadj(G),G)==ONE6
    return G

def herm_coords(Z):
    assert len(Z)==3
    assert H91.dag(Z)==Z and H91.tr(Z).i==0
    return (
       [Z[i][i].r for i in range(3)]
       +[Z[i][j].r for i,j in combinations(range(3),2)]
       +[Z[i][j].i for i,j in combinations(range(3),2)]
    )

def source_matrix(G,after_reset):
    cols=[]
    for T in tangents:
        Y=qconj(G,T)
        if after_reset:Y=qtrace(micro(Y))
        else:Y=qtrace(Y)
        cols.append(herm_coords(Y))
    return [list(row) for row in zip(*cols)]

raw=[];post=[]
for w in words:
    G=word_gate(w)
    raw.append(source_matrix(G,False))
    post.append(source_matrix(G,True))
assert [H91.rank(M) for M in raw]==[6,4,4,4]
assert [H91.rank(M) for M in post]==[6,4,4,4]
rawcum=[];postcum=[]
for a,b in zip(raw,post):
    rawcum.extend(a)
    postcum.extend(b)
    rankraw=H91.rank(rawcum)
    rankpost=H91.rank(postcum)
    assert rankraw==rankpost
    rawranks=rankraw
assert [H91.rank(sum(raw[:k],[])) for k in range(1,5)]==[6,10,11,12]
assert [H91.rank(sum(post[:k],[])) for k in range(1,5)]==[6,10,11,12]
assert H91.rank(rawcum)==H91.rank(postcum)==12
print("PASS H94.2: EXACT qutrit ORIGINAL micro outputs after four inherited pre-reset control WORDS have per-setting ranks 6,4,4,4 and cumulative ranks 6,10,11,12")
print("PASS H94.2: fixed source H42 complex U does NOT need to be isolated as an independent pre-reset gate")

# The 9 effects are ALL valid positive qutrit effects:
# 3 site projectors, 3 (I+X_ab)/2, 3 (I+Y_ab)/2.
eye3=H91.plus(H91.plus(H91.e(3,0,0),H91.e(3,1,1)),H91.e(3,2,2))
effects=[H91.e(3,k,k) for k in range(3)]
for a,b in combinations(range(3),2):
    A=H91.hermX(3,a,b)
    assert H91.mm(H91.mm(A,A),A)==A
    effects.append(H91.scale(H91.plus(eye3,A),F(1,2)))
for a,b in combinations(range(3),2):
    A=H91.hermY(3,a,b)
    assert H91.mm(H91.mm(A,A),A)==A
    effects.append(H91.scale(H91.plus(eye3,A),F(1,2)))
assert len(effects)==9 and all(H91.dag(Q)==Q for Q in effects)
# X/Y are Hermitian with eigenvalues -1,0,1: hence Q is a
# genuinely POSITIVE quantum effect and I-Q also positive.

poisson_readout=[]
for w in words:
    G=word_gate(w)
    columns=[]
    for T in tangents:
        v=qtrace(micro(qconj(G,T)))
        vals=[H91.tr(H91.mm(Q,v)) for Q in effects]
        assert all(z.i==0 for z in vals)
        columns.append([z.r for z in vals])
    M=[list(row) for row in zip(*columns)]
    poisson_readout+=M
assert H91.rank(poisson_readout)==12
assert [H91.rank(poisson_readout[:9*k]) for k in range(1,5)]==[6,10,11,12]

# These are ACTUAL positive (unitary-gated and CPTP-reset) physical
# states from original H75 source. All 9 effects have true [0,1]
# Born-rule probabilities, including positive coherence effects.
for w in words:
    Y=qtrace(micro(qconj(word_gate(w),H92.physical_seed)))
    assert H91.dag(Y)==Y and H91.tr(Y)==O
    outcomes=[H91.tr(H91.mm(Q,Y)) for Q in effects]
    assert all(z.i==0 and 0<=z.r<=1 for z in outcomes)
print("PASS H94.2: FOUR sets of genuine positive site/qutrit coherence POVM probabilities give full 12-column LOCAL tomography Jacobian rank12")

# Physical positive-state witness: H92 independently supplied
# opposite coherent U5 pulse states. The SAME original pre-reset
# W,F,UA schedule + H75 micro makes them operationally distinguishable,
# even though no-precontrol reset had precisely equal states.
phys_plus=H92.decode5(H92.rp)
phys_minus=H92.decode5(H92.rm)
assert micro(phys_plus)==micro(phys_minus)
G=word_gate(words[0])
output_plus=qtrace(micro(qconj(G,phys_plus)))
output_minus=qtrace(micro(qconj(G,phys_minus)))
pa=H91.tr(H91.mm(effects[0],output_plus))
pb=H91.tr(H91.mm(effects[0],output_minus))
assert pa.i==pb.i==0 and 0<=pa.r<=1 and 0<=pb.r<=1
assert pa.r-pb.r==F(7168,921875)
print("PASS H94.3: opposite genuine positive pre-reset source-orbit states are indistinguishable under raw reset but distinguishable by existing 4-step precontrol + POSITIVE site0 POVM, exact gap 7168/921875")

print("BOUNDARY: multi-copy observational informational completeness is NOT single-channel coherent quantum recovery or code-preserving U5 reachability")
print("BOUNDARY: W/F pre-reset sequential availability and reproducible arbitrary H92-orbit input states are ADDITIONAL AX-OA assumptions; no new phase Hamiltonian postulated")
print("BOUNDARY: no sourced symplectic ADM intertwiner, gravitational DeWitt dynamics, full off-shell HDA, Einstein equation or F completeness")
