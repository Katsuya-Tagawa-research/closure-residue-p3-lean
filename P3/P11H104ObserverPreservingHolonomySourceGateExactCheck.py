"""H104 — SAME original H75 CPTP source:
    exact B quantum-channel covariance DOES preserve coarse flag observer,
    but fails fine computational diagonal observer; no nonzero connected
    covariance+fine-observer real Hamiltonian source direction survives.
    Two EXTERNALLY ASSIGNED K4 edge transport sets, each using only an
    inherited locally permitted B pulse / identity and each commuting
    with ALL 36-unit local CPTP diagrams, have nonconjugate holonomies.

This is a precise observer/source-connection NONSELECTION statement.
An independent physical intercell Hamiltonian, spatial solder, Cartan
torsion-free dynamics, DeWitt action and Einstein fields are NOT sourced.
Reported P9.125-128 Cartan model is NOT identified with H75 here.
"""
from fractions import Fraction as F

from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    R60,U,A,B,M0,M1,MBASIS,
    micro,edge_cayley,lift,qconj,matmul,matadj,mattrace,
    zero_n,eye_n
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P9H85A4EdgeSourceSelectionExactCheck as H85
import P9H99SourceMetricRankCurvatureJetNonselectionExactCheck as H99
import P11H103SourceEquivariantTransportCartanInterfaceExactCheck as H103

assert len(MBASIS)==36
assert R60[0][0]==I*gc(F(-32,135))
assert H85.r==(F(0),F(16,25),F(16,25),F(4,25))
assert H85.wa==(4,4,1,8,5,5)
assert H91.rank(H99.composite)==3
assert H103.Rb==edge_cayley(B,F(1,2))

Rb=H103.Rb
Rbi=matadj(Rb)
Id3=eye_n(3)
Id6=eye_n(6)
assert matmul(Rb,Rbi)==matmul(Rbi,Rb)==Id3
assert matmul(Rb,M0)==matmul(M0,Rb)
assert matmul(Rb,M1)==matmul(M1,Rb)

def flag_proj(a):
    P=zero_n(6)
    for i in range(3):
        P[3*a+i][3*a+i]=O
    return P

P0,P1=flag_proj(0),flag_proj(1)
assert P0!=P1
assert matmul(P0,P1)==zero_n(6)
assert matmul(P0,P0)==P0 and matmul(P1,P1)==P1
assert [[P0[i][j]+P1[i][j] for j in range(6)] for i in range(6)]==Id6

# Two observers are ON THE SAME original six-level microscopic source.
# Coarse flag algebra span(P0,P1) is invariant under both source and
# decoded output B control, so it is an exact observer-preserving square.
Win=lift(Rb)
Wout=H103.Wout
for P in (P0,P1):
    assert qconj(Win,P)==P
    assert qconj(Wout,P)==P
for E in MBASIS:
    assert micro(qconj(Win,E))==qconj(Wout,micro(E))
print("PASS H104.1: original H75 B input and source-defined output representations commute with genuine coarse flag observer, and complete CPTP square commutes on ALL 36 original 6x6 matrix units")

def is_diag(X):
    return all(X[i][j]==Z0 for i in range(len(X))
               for j in range(len(X)) if i!=j)

D11=H91.e(3,1,1)
rot=qconj(Rb,D11)
assert not is_diag(rot)
assert rot[1][2]==gc(F(12,25))
assert rot[2][1]==gc(F(12,25))
assert qconj(Win,H91.e(6,1,1))!=H91.e(6,1,1)
# The ORIGINAL six-level site-plus-flag diagonal algebra
# is not normalized by input B rotations. Even choosing an
# output site observer ADAPTED to fixed U does not repair this,
# because its preimage under U is exactly this non-diagonal.
U_d11=qconj(U,D11)
out_Ud11=qconj(H103.outRb,U_d11)
assert out_Ud11==qconj(U,rot)
assert out_Ud11!=U_d11
print("PASS H104.1: fine diagonal site population observer fails fixed-algebra normalization, exact original H75 B pulse creates offdiagonal 12/25 from |1><1| (adapted output observer also fails)")

# Independent Lie-algebra nullspace obstruction:
# H103 found the source-real so3 covariance centralizer span B.
# A connected subgroup preserving EVERY computational diagonal
# site projection must have zero continuous real-skew generator.
C=H91.comm(A,B)
KS=(A,B,C)
def offdiag_flat(X):
    return [X[i][j].r for i in range(len(X))
            for j in range(len(X)) if i!=j]+[
            X[i][j].i for i in range(len(X))
            for j in range(len(X)) if i!=j]
def flatten_commutator_action(K):
    blocks=[]
    for k in range(3):
        blocks.extend(offdiag_flat(H91.comm(K,H91.e(3,k,k))))
    return blocks
observer_constraint=[flatten_commutator_action(K) for K in KS]
assert H91.rank(observer_constraint)==3
assert H91.rank(H103.restrictions)==2
assert offdiag_flat(H91.comm(B,D11))!=[F(0)]*len(offdiag_flat(D11))
print("PASS H104.1: connected source-real so3 normalizer of fine site population MASA has rank0; intersection with 1D CPTP-covariant B generator is EXACTLY zero")
print("BOUNDARY: discrete nonidentity signed-permutation normalizers may exist; H104 No-Go concerns nonzero CONNECTED infinitesimal Hamiltonian transport and fixed fine observer")

# H104.2: Four local copies of THE SAME H75 site channel on
# externally labelled K4 cells. Original positive H85 weights held.
# Edges are NOT actual source-generated spatial transfer operations.
# Each edge is a mathematical ASSIGNMENT of an already permitted
# locally source-compatible rotation, with correct inverse on
# reverse edge.
assert tuple(H85.edges)==((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
site_edges=dict((e,Id3) for e in H85.edges)
site_edges[(0,1)]=Rb
def edge(directed,nontrivial):
    i,j=directed
    raw=(min(i,j),max(i,j))
    R=site_edges[raw] if nontrivial else Id3
    return R if i<j else matadj(R)

# Every unique edge channel is original B (or inverse) or identity.
# All have the same H75 underlying microscopic source and preserve
# coarse flag observers at source and the formal target.
for R in (Id3,Rb,Rbi):
    V=lift(R)
    U_R=qconj(U,R)
    Vout=lift(U_R)
    for P in (P0,P1):
        assert qconj(V,P)==P and qconj(Vout,P)==P
    for E in MBASIS:
        assert micro(qconj(V,E))==qconj(Vout,micro(E))
for j,k in ((0,1),(1,2),(2,0),(0,2),(2,3),(3,0)):
    for nontrivial in (False,True):
        assert matmul(edge((j,k),nontrivial),
                      edge((k,j),nontrivial))==Id3
print("PASS H104.2: identity/actual B/actual inverse B all satisfy EXACT common H75 36-unit CPTP squares, preserve flag observer and define consistent mathematical orientation-inverted edge assignments")

def hol_triangle(on):
    return matmul(matmul(edge((0,1),on),edge((1,2),on)),
                  edge((2,0),on))
hol_flat=hol_triangle(False)
hol_nonzero=hol_triangle(True)
assert hol_flat==Id3 and hol_nonzero==Rb
assert mattrace(hol_flat)==gc(F(3))
assert mattrace(hol_nonzero)==gc(F(11,5))
assert mattrace(hol_flat)!=mattrace(hol_nonzero)
assert mattrace(qconj(U,hol_flat))==mattrace(hol_flat)
assert mattrace(qconj(U,hol_nonzero))==mattrace(hol_nonzero)
print("PASS H104.2: two externally assigned BUT source-commuting common-K4 transport systems have gauge-inequivalent triangle loop traces 3 vs 11/5, with identical H75 micro/CPTP/flag observer/positive K4 weights")
print("BOUNDARY: nontrivial mathematical edge assignment is NOT physically generated intercell transport; local allowed B site pulse alone does not determine/spatially implement an edge law")

# H104.3: source qutrit site unitary and spatial K4 response S
# live on DIFFERENT representation spaces. In the PARTICULAR
# externally imposed IDENTITY SOLDER of site R3 with the K4
# coordinate basis, the H75 B control is not metric compatible.
# This is NOT a No-Go for every unknown future solder.
gsp=[[gc(x) for x in row] for row in H99.g0]
rot_metric=matmul(matmul(Rbi,gsp),Rb)
difference=[[rot_metric[i][j]-gsp[i][j] for j in range(3)]
            for i in range(3)]
assert difference!=zero_n(3)
assert difference[0][1]==gc(F(128,245))
assert difference[0][2]==gc(F(-384,245))
assert difference[1][1]==gc(F(33792,30625))
print("PASS H104.3: conditional IDENTITY solder fails K4 response metric compatibility: rational source B congruence defect nonzero, e.g. 128/245")
print("BOUNDARY: no physically sourced canonical solder maps H75 site Hilbert coordinates to K4 S=1_perp; a DIFFERENT sourced solder may satisfy metric/Cartan constraints")

# The same reference positive state is not automatically transported
# identically from vertex to vertex under a nontrivial assigned edge.
# Require this extra actual state naturality if claiming a physical
# source-specific connection.
rho=H103.rho
assert qconj(Rb,rho)!=rho
print("PASS H104.4: additional edge-state naturality would have independent content, since original H75 positive seed is NOT invariant under B; it cannot be silently inferred from CPTP-channel covariance")

open_axioms={
    "AX-SRC common source and permitted physical intercell Hamiltonian":"OPEN",
    "AX-OA exact specified observer algebra and covariance rule":"OPEN",
    "AX-CAN nondegenerate source-produced KKS and physical momentum":"OPEN",
    "AX-SP source-generated solder/connection/torsion/curvature 2jet":"OPEN",
    "AX-DYN sourced DeWitt/R/constraints/off-shell HDA":"OPEN",
    "AX-NORM scale/cosmological coupling physical selection":"OPEN",
    "AX-GEN F generative completeness and discriminating empirical test":"OPEN"
}
assert len(open_axioms)==7 and set(open_axioms.values())=={"OPEN"}
print("PASS H104.5: typed seven-gate H75/P9 Cartan/P11 handoff; reported P9.125-128 separate model NOT asserted to be original H75 source")
print("VERDICT: exact same-source observer-normalizer connected No-Go; exact conditional source-compatible but externally assigned gauge-inequivalent loop systems; physical intercell Cartan/Levi-Civita and Einstein dynamics OPEN")
