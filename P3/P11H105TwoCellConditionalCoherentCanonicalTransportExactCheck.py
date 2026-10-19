"""H105: real H75 two-cell source, exact strong Kraus-commuting link
criterion and CONDITIONAL first nondegenerate 2D KKS Hamiltonian pair.

Source: tensor product of SAME original 4-Kraus 6-level CPTP H75 reset,
with source native real B-local controls only. These commute and KKS is
isotropic. Strongly attenuation-commuting TWO-SITE operators have exact
complex dimension25 (joint blocks 1,2,2,4). A deliberately NEW, NOT
SOURCE-DERIVED entangling Hamiltonian X12⊗|1><1| would yield one KKS
symplectic pair with native Y12 local, preserved true CPTP covariance
and exact source-positive flag00 X/Y POVM response Jacobian. This is
not a sourced P9 Cartan connection, ADM field or Einstein Hamiltonian.
"""
from fractions import Fraction as F

from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    U,A,B,M0,M1,R60,edge_cayley,matmul,matadj,
    mattrace,eye_n,zero_n
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P11H102RealControlLagrangianConditionalSU2ExactCheck as H102
import P11H103SourceEquivariantTransportCartanInterfaceExactCheck as H103
import P11H104ObserverPreservingHolonomySourceGateExactCheck as H104

assert R60[0][0]==I*gc(F(-32,135))
assert H104.Rb==edge_cayley(B,F(1,2))
assert H91.tr(H91.mm(H103.rho,H103.rho))==gc(F(5,8))

def kron(A,B):
    n=len(A);m=len(B)
    return [[A[i//m][j//m]*B[i%m][j%m] for j in range(n*m)]
            for i in range(n*m)]

I3=eye_n(3)
I9=eye_n(9)
ZERO9=zero_n(9)
Mpair=[kron(Ma,Mb) for Ma in (M0,M1) for Mb in (M0,M1)]
U2=kron(U,U)
assert H91.dag(U2)==H91.dag(U2)
assert H91.mm(H91.dag(U2),U2)==I9
assert all(H91.dag(M)==M for M in Mpair)
total=ZERO9
for M in Mpair:total=H91.plus(total,H91.mm(H91.dag(M),M))
assert total==I9
# For ANY incoming two flags, exactly the same four Mpair output
# branches are summed. With 4 incoming flag pairs, these are the
# sixteen actual pair-register H75×H75 physical Kraus blocks.
assert len(Mpair)*4==16
print("PASS H105.0: SAME original 4-Kraus H75 six-level micro source tensor-square has 16 true two-cell Kraus blocks; exact original CP completeness on full 9-site register")

# The source's ACTUALLY inherited independently available local site
# B controls on each copy. Their Lie algebra is Abelian, so every
# moment-map Poisson bracket vanishes for every input state.
K1=kron(B,I3)
K2=kron(I3,B)
assert H91.dag(K1)==H91.scale(K1,-1)
assert H91.dag(K2)==H91.scale(K2,-1)
assert H91.comm(K1,K2)==ZERO9
assert H91.rank([H104.H103.flatten_real(K1),
                 H104.H103.flatten_real(K2)])==2
for K in (K1,K2):
    assert all(H91.comm(K,M)==ZERO9 for M in Mpair)
print("PASS H105.1: two actual original B local real controls span a 2D ABELIAN Lie algebra and their KKS pullback is identically zero (no source-generated symplectic pair)")

# Strong source-Kraus-compatible commutant of all M_a⊗M_b:
# for site state (i,j), joint attenuation eigenvalues form one of
# four distinct signatures 00,0d,d0,dd of multiplicity 1,2,2,4.
signatures=[]
for k in range(9):
    signatures.append(tuple(M[k][k] for M in Mpair))
assert sorted(set(signatures),key=str)==sorted(set(signatures),key=str)
counts=sorted([signatures.count(v) for v in set(signatures)])
assert counts==[1,2,2,4]
commuting_units=[]
for i in range(9):
    for j in range(9):
        E=H91.e(9,i,j)
        passes=all(H91.comm(E,M)==ZERO9 for M in Mpair)
        assert passes==(signatures[i]==signatures[j])
        if passes:commuting_units.append(E)
assert len(commuting_units)==25
assert sum(v*v for v in counts)==25
print("PASS H105.2: exact full 9x9 matrix-unit simultaneous commutant of four genuine M_a⊗M_b has complex dimension25 =1²+2²+2²+4²; mathematical compatibility is NOT physical access")

P1=H91.e(3,1,1)
P2=H91.e(3,2,2)
P12=H91.plus(P1,P2)
X=H91.hermX(3,1,2)
Y=H91.hermY(3,1,2)
Z=H91.minus(P1,P2)
assert Y==H91.scale(B,I)
assert H91.comm(X,Y)==H91.scale(Z,2*I)
H_X=kron(X,P1)    # EXTRA independent, genuinely two-cell conditional Hamiltonian
H_Y=kron(Y,I3)    # SOURCE native local B Hamiltonian (up to drive sign)
Ydet=kron(Y,P1)  # calibrated detector observable on the conditioned sector
P_link=kron(P12,P1)
assert H91.dag(H_X)==H_X and H91.dag(H_Y)==H_Y
assert H91.mm(H_X,H_X)==P_link
assert H91.mm(H_X,P_link)==H_X
assert all(H91.comm(H_X,M)==ZERO9 for M in Mpair)
assert all(H91.comm(H_Y,M)==ZERO9 for M in Mpair)
assert H91.comm(H_X,H_Y)!=ZERO9
assert H_X!=kron(X,I3)
assert H_X!=kron(X,H91.scale(I3,F(1,3)))
# H_X is mathematically compatible but not in the available local
# two-real-generator Lie span, which is real skew after multiplication
# by -i; no fabricated source Hamiltonian is claimed.
assert H91.rank([
    H104.H103.flatten_real(H91.scale(K1,I)),
    H104.H103.flatten_real(H91.scale(K2,I)),
    H104.H103.flatten_real(H_X)
])==3

# Explicit EXACT rational Gaussian Cayley unitary with t=1/2:
# R=I+(c-1)P_link - i s H_X, c=3/5, s=4/5.
R=H91.plus(H91.plus(I9,H91.scale(P_link,F(-2,5))),
           H91.scale(H_X,-I*gc(F(4,5))))
assert H91.mm(H91.dag(R),R)==I9
assert R!=I9
assert all(H91.comm(R,M)==ZERO9 for M in Mpair)
Wout=H91.mm(H91.mm(U2,R),H91.dag(U2))
assert H91.mm(H91.dag(Wout),Wout)==I9

# For each of 4 output flag choices and 4 incoming flag choices,
# the 16 physical Kraus block identities follow from strong 9D
# matrix relation Wout (U2 M_ab)=(U2 M_ab) R.
# These suffice on ALL two-cell 36x36 matrix units, not just
# on chosen input states or one marginal measurement:
# L_{a,b; c,d} = |a,b><c,d|⊗U2 M_ab.
for incoming_flag in range(4):
    for M in Mpair:
        K=H91.mm(U2,M)
        assert H91.mm(Wout,K)==H91.mm(K,R)
print("PASS H105.3: ADDITIONALLY ASSUMED intercell complex X⊗P is EXACT unitary and intertwines ALL 16 TRUE H75×H75 two-cell Kraus flag blocks, hence entire CPTP source")

# Positive source product seed. First site occupied 1/2 doublet with
# nontrivial population gap; second at |1> so controlled link active.
ra=H91.plus(H91.scale(P1,F(3,4)),H91.scale(P2,F(1,4)))
rb=P1
seed=kron(ra,rb)
assert H91.dag(seed)==seed and H91.tr(seed)==O
assert H91.mm(seed,seed)!=seed
T_X=H91.scale(H91.comm(H_X,seed),-I)
T_Y=H91.scale(H91.comm(H_Y,seed),-I)
for T in (T_X,T_Y):
    assert H91.dag(T)==T and H91.tr(T)==Z0
def herm9vec(T):
    return [z.r for row in T for z in row]+[
            z.i for row in T for z in row]
assert H91.rank([herm9vec(T_X),herm9vec(T_Y)])==2
def pb(H,J):
    x=-I*H91.tr(H91.mm(seed,H91.comm(H,J)))
    assert x.i==0
    return x.r
assert pb(H_X,H_Y)==F(1)
assert pb(H_Y,H_X)==F(-1)
assert H91.rank([[pb(H_X,H_X),pb(H_X,H_Y)],
                 [pb(H_Y,H_X),pb(H_Y,H_Y)]])==2
print("PASS H105.4: genuine POSITIVE product qutrit source seed supports exact ONE conditional canonical KKS pair when independently postulated intercell H_X=X12⊗P1 is allowed; KKS bracket=1")

# Two true positive H75×H75 output effects in the original flag
# pair 00, with site calibration via exactly the fixed U2 within
# the source reset. Spectral polynomial H³=H => effects 0<=Q<=I.
def effect(H):
    assert H91.dag(H)==H and H91.mm(H91.mm(H,H),H)==H
    return H91.scale(H91.plus(I9,H),F(1,2))
QX=effect(H_X)
QY=effect(Ydet)
M00=Mpair[0]
def branch_probability(Q,T):
    # true original 00 flag block = U2 M00 T M00 U2† and output
    # positive detector E00⊗U2 Q U2†. Cyclic trace cancels U2.
    cal=H91.mm(H91.mm(U2,Q),H91.dag(U2))
    branch=H91.mm(H91.mm(U2,H91.mm(H91.mm(M00,T),M00)),H91.dag(U2))
    result=H91.tr(H91.mm(cal,branch))
    assert result.i==0
    assert result==H91.tr(H91.mm(Q,H91.mm(H91.mm(M00,T),M00)))
    return result.r

jac=[[branch_probability(Q,T) for T in (T_X,T_Y)]
     for Q in (QX,QY)]
assert jac==[[F(0),F(81,1250)],[F(-81,1250),F(0)]],jac
assert H91.rank(jac)==2
assert jac[0][0]*jac[1][1]-jac[0][1]*jac[1][0]==F(81,1250)**2
assert 0<=branch_probability(QX,seed)<=1
assert 0<=branch_probability(QY,seed)<=1
print("PASS H105.5: exact original H75×H75 positive flag00 X/Y POVMs read conditional pair; response [[0,81/1250],[-81/1250,0]], nonzero determinant")

# Strict fixed fine site population MASA is NOT preserved by these
# connected controls, even though coarse flag records always remain.
assert H91.comm(H_X,kron(P1,P1))!=ZERO9
assert H91.comm(H_Y,kron(P1,P1))!=ZERO9
assert H91.mm(R,kron(P1,P1))!=H91.mm(kron(P1,P1),R)
print("PASS H105.6: conditional source-compatible coherent link preserves coarse flag observer but not fixed fine site population algebra; single link has NO triangle/Cartan curvature")

gate_status={
    "AX-SRC copied authentic CPTP local source":"EXACT",
    "AX-CAN native local B symplectic generator":"NO-GO",
    "AX-CAN extra controlled X link physical implementation":"INDEPENDENT ASSUMPTION",
    "AX-OA output X/Y positive readout physical calibration":"INDEPENDENT ASSUMPTION",
    "AX-SP real physical intercell Cartan/solder/holonomy":"OPEN",
    "AX-DYN microscopic DeWitt/curvature/Einstein":"OPEN",
    "AX-NORM gravitation scale and Lambda":"OPEN",
    "AX-GEN F noncircular physics selection":"OPEN",
}
assert len(gate_status)==8
print("BOUNDARY: commuting with original H75 Mpair is an EXACT SOURCE compatibility test, NOT physical derivation of a new intercell complex Hamiltonian, its amplitude, or output apparatus")
print("BOUNDARY: ONE conditional SU2 pair is not ADM six-pair field, cannot determine physical Cartan spatial curvature from TWO cells or generate full offshell HDA/Einstein/F completeness")
