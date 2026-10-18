"""H103: actual original H75 source-equivariant quantum control classification.

The inherited physically allowed B site rotation on levels 1/2 has
EXACT output unitary channel covariance on ALL 36 six-level matrix
units. A site rotation on levels 0/1 is a genuine PHYSICAL INPUT
Hamiltonian, but the full H75 CPTP outputs of two isospectral positive
input states have DISTINCT purity: cannot share one output U6 orbit.

P9 Cartan connection 125-128 uses a DIFFERENT not-yet-matched micro
source; its solder/control/observer data are not silently imported.
No generated ADM/HDA/Einstein, no independently sourced new phase gate.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    A,B,M0,M1,U,R60,MBASIS,
    edge_cayley,lift,micro,embed,qconj,
    matmul,matadj,matadd,matscale,mattrace,zero_n,eye_n
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P11H101PhaseBlindFlagCanonicalProvenanceExactCheck as H101
import P11H102RealControlLagrangianConditionalSU2ExactCheck as H102

assert R60[0][0]==I*gc(F(-32,135))
assert len(MBASIS)==36
rho=H101.rho(F(0))
assert rho==H102.rho
assert rho==[
  [gc(F(3,4)),Z0,Z0],
  [Z0,gc(F(1,4)),Z0],
  [Z0,Z0,Z0],
]
def HS2(X):
    Y=matmul(X,X)
    val=mattrace(Y)
    assert val.i==0
    return val.r
def flatten_real(X):
    return [z.r for row in X for z in row]+[
            z.i for row in X for z in row]
def commute(X,Y):
    return H91.comm(X,Y)

# This is ACTUAL inherited physical source B control, not a newly
# postulated nonreal quadrature. Since attenuators are constant on
# site 1,2, B commutes with M0,M1.
Rb=edge_cayley(B,F(1,2))
Ra=edge_cayley(A,F(1,2))
assert matmul(matadj(Rb),Rb)==eye_n(3)
assert matmul(matadj(Ra),Ra)==eye_n(3)
assert commute(B,M0)==commute(B,M1)==zero_n(3)
assert commute(Rb,M0)==commute(Rb,M1)==zero_n(3)
assert commute(A,M0)!=zero_n(3)
assert commute(A,M1)!=zero_n(3)
# W_B is a mathematically defined output representation, its
# independent PHYSICAL pulse availability is not assumed.
outRb=matmul(matmul(U,Rb),matadj(U))
assert matmul(matadj(outRb),outRb)==eye_n(3)
Win=lift(Rb)
Wout=lift(outRb)
for unit in MBASIS:
    assert micro(qconj(Win,unit))==qconj(Wout,micro(unit))
print("PASS H103.1: actual inherited B Cayley input control exactly intertwines unchanged genuine H75 reset through unitary Wout=(Iflag⊗U Rb Udag) on ALL 36 M6 matrix units")

# Exact Lie algebra centralizer inside original physically declared
# REAL so3 site Lie closure span{A,B,[A,B]}.
C=commute(A,B)
KS=(A,B,C)
assert H91.rank([flatten_real(K) for K in KS])==3
restrictions=[
    flatten_real(commute(K,M0))+flatten_real(commute(K,M1))
    for K in KS
]
assert H91.rank(restrictions)==2
assert restrictions[1]==[F(0)]*(2*2*9)
assert restrictions[0]!=restrictions[1]
assert restrictions[2]!=restrictions[1]
print("PASS H103.2: exactly one real infinitesimal source-site direction, span(B), commutes with both genuine attenuation M0/M1; strict one-dimensional centralizer within inherited so3")

# One-parameter B action has tangent rank one (or zero at a B-symmetric
# seed). At the actual H101 rho0 it has exactly one nonzero tangent.
TB=commute(B,rho)
assert TB!=zero_n(3) and H91.dag(TB)==TB
assert H91.rank([flatten_real(TB)])==1
# Any alternating (symplectic) 2-form restricts identically to zero
# on a one-dimensional orbit; hence no nondegenerate canonical PAIR.
assert H102.poisson(H91.scale(B,I),H91.scale(B,I))==0
print("PASS H103.2: actual B source-equivariant control orbit from rho0 has dimension1 and intrinsically zero alternating KKS two-form, insufficient for ONE symplectic pair")

# The ACTUAL H75 allowed A rational Cayley pulse rotates sites 0,1.
# Positive isospectral input states rho and rhoA have the same pure
# quantum spectrum since rhoA=RA rho RA†, but source output CPTP
# purities are different. Thus NO six-level unitary output can
# intertwine these two physical states.
assert Ra[0][0]==gc(F(3,5))
assert Ra[0][1]==gc(F(4,5))
assert Ra[1][0]==gc(F(-4,5))
assert Ra[1][1]==gc(F(3,5))
rhoA=qconj(Ra,rho)
assert matadj(rhoA)==rhoA
assert mattrace(rhoA)==O
assert HS2(rho)==HS2(rhoA)==F(5,8)
assert rhoA[0][0]==gc(F(43,100))
assert rhoA[1][1]==gc(F(57,100))
assert rhoA[0][1]==gc(F(-6,25))
Y0=micro(embed(rho))
YA=micro(embed(rhoA))
assert matadj(Y0)==Y0 and matadj(YA)==YA
assert mattrace(Y0)==mattrace(YA)==O
assert HS2(Y0)==F(2981,5000),HS2(Y0)
assert HS2(YA)==F(1254869,3125000),HS2(YA)
assert HS2(YA)-HS2(Y0)==F(-76032,390625)
assert Y0!=YA
# The spectral moment Tr(Y^2) is invariant under every U6
# conjugation, so NO output unitary W can obey YA=W Y0 W†.
print("PASS H103.3: actual allowed A Cayley maps two isospectral positive qutrit inputs, yet genuine 6-level output purities 2981/5000 vs 1254869/3125000 differ; ANY output-unitary orbit intertwiner is impossible")

# This spectral No-Go is independent of information-injectivity:
# the original H75 J_U maps qutrit operator algebra injectively,
# as H91 checks. One cannot confuse exact recovered qutrit POVM
# information with unitary orbit preservation.
assert H91.rank([H91.block_coords(H91.J5(e)) for e in H91.basis_q])==9
assert H102.P and H91.rank(H102.P)==6

# Full physical common-source Cartan bridge is not instantiated here.
# The user-reported P9.125-128 Cartan model has its OWN 48-level
# dynamic-register source, observer and torsion protocols; assuming
# it is this H75 source would be an invalid provenance shortcut.
proof_obligations={
    "AX-SRC common microsource and declared operations":"OPEN",
    "AX-OA observer algebra preserved by cross-cell controls":"OPEN",
    "AX-CAN sourced nondegenerate KKS controls and transport":"OPEN",
    "AX-SP source-derived solder/connection/2jet and holonomy":"OPEN",
    "AX-DYN source-defined action/DeWitt/full offshell HDA":"OPEN",
    "AX-NORM gravity scale/cosmological selection":"OPEN",
    "AX-GEN noncircular F completeness":"OPEN",
}
assert len(proof_obligations)==7
assert set(proof_obligations.values())=={"OPEN"}
print("PASS H103.4: strict typed P9 Cartan/H75 and P11 AX-SRC/OA/CAN/SP/DYN/NORM/GEN integration registry; NO false common-source identification")
print("BOUNDARY: B covariance defines an exact OUTPUT REPRESENTATION, not certified independent physical implementation of Wout")
print("BOUNDARY: A spectral obstruction and B one-control survivor are SOURCE SPECIFIC; no universal CR gravity No-Go, derived torsion-free selector, Einstein action or physical six-pair ADM symplectic transport")
