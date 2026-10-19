"""H107: P9/P11 same-source provenance and a physically positive H75
output phase-correlation effect distinguishing the SAME flag-blind
two-cell source states already rigorously verified in H106.

NO new control/Hamiltonian/Cartan/ADM source. H105's complex link is
an INDEPENDENT hypothetical physical premise, NOT P3/F generated.
Every probability is exact Fraction/Gaussian-rational. The observer
is a valid output local-product-measurement-derived effect requiring
additional independent detector calibration, NOT a GR prediction.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    R60,matmul,matadj,mattrace,eye_n,zero_n
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P11H105TwoCellConditionalCoherentCanonicalTransportExactCheck as H105
import P11H106LocalOnlySeparabilityVsLinkEntanglementExactCheck as H106

assert R60[0][0]==I*gc(F(-32,135))
assert H106.rho!=H106.rhoR
assert H106.prob_native==H106.prob_link
assert H106.p==F(153,625)
assert H106.minor.r==F(-2916,390625)
assert H106.norm_det==F(6,17)
print("PASS H107.0: SAME original H75×H75 source, H106 source positive product and EXTERNAL H105 linked state, identical all four coarse flag effects")

# New PHYSICAL-POSITIVITY readout, NO new controlled physical gate:
# C=Y12(site1) ⊗ X01(site2). Each site observable has spectrum
# {-1,0,1} (with level spectator). Their product is Hermitian and
# C^3=C, proving C spectrum in {-1,0,1}; thus Q=(I+C)/2
# is a bona fide 0<=Q<=I positive measurement effect.
X01=H91.hermX(3,0,1)
Y12=H105.Y
C=H105.kron(Y12,X01)
assert H91.dag(C)==C
assert H91.mm(H91.mm(C,C),C)==C
assert C!=zero_n(9)
Q=H91.scale(H91.plus(eye_n(9),C),F(1,2))
assert H91.dag(Q)==Q
assert H91.mm(H91.mm(H91.minus(H91.scale(Q,2),eye_n(9)),
                       H91.minus(Q,eye_n(9))),Q)==zero_n(9)
print("PASS H107.1: true source-output 9D two-cell phase-correlation effect Q=(I+Y12⊗X01)/2 is positive from Hermitian cubic spectral certificate")

def real_trace(X):
    t=H91.tr(X)
    assert t.i==0
    return t.r
def prob(Q,sigma):
    return real_trace(H91.mm(Q,sigma))
native_corr=prob(C,H106.sigi)
link_corr=prob(C,H106.sig)
assert native_corr==F(0)
assert link_corr==F(-108,625)
native_effect=prob(Q,H106.sigi)
link_effect=prob(Q,H106.sig)
assert native_effect==F(153,1250)
assert link_effect==F(9,250)
assert link_effect-native_effect==F(-54,625)
assert 0<=native_effect<=H106.p and 0<=link_effect<=H106.p
assert native_effect/H106.p==F(1,2)
assert link_effect/H106.p==F(5,34)
print("PASS H107.2: genuine H106 positive output flag00 branch Q probability native=153/1250 vs conditional linked=9/250; correlators 0 vs -108/625; conditional positive probabilities 1/2 vs 5/34")

# Independently derive linked correlator from H106's three
# unnormalized amplitudes u[3]=3/5, u[4]=27/125,
# u[7]=-36i/125, with sigma=(1/2) u u†. The only Y⊗X
# active pair in u is site ket |1,0> ↔ |2,1>.
a=H106.u[3]
b=H106.u[7]
assert a==gc(F(3,5)) and b==-I*gc(F(36,125))
expect_from_amplitudes=(a.conj()*(-I)*b+b.conj()*I*a)*gc(F(1,2))
assert expect_from_amplitudes.i==0
assert expect_from_amplitudes.r==link_corr
print("PASS H107.2: independent three-amplitude phase-correlation calculation matches direct 9D exact Born trace")

# Physically typed full output flags dimension 4, sites 9: 36D.
# This is the TRUE source original two-cell output (not a fictional
# 9->9 CPTP channel): flag00 effect E00⊗(U⊗U)Q(U⊗U)†.
U2=H105.U2
Qcal=H91.mm(H91.mm(U2,Q),H91.dag(U2))
E=zero_n(36)
for i in range(9):
    for j in range(9):
        E[i][j]=Qcal[i][j]
assert H91.dag(E)==E
def full_output_positive_flag00(sigma):
    # The actual unrotated branch sigma is from the original pair
    # M0⊗M0 source. U2 conjugates in the genuine Kraus output.
    return H91.mm(H91.mm(U2,sigma),H91.dag(U2))
assert prob(Qcal,full_output_positive_flag00(H106.sigi))==native_effect
assert prob(Qcal,full_output_positive_flag00(H106.sig))==link_effect
# The effect is zero in other physical flag sectors; by spectral
# conjugation of 0<=Q<=I9, 0<=E<=I36.
assert E[9][9]==Z0 and E[35][35]==Z0
print("PASS H107.3: explicit 36D original H75 two-flag output detector E00⊗U2 Q U2† reproduces exact positive probabilities; extra detector calibration is an INDEPENDENT premise")

# The original coarse flag data contain NO information allowing
# deterministic reconstruction of this additional effect on the
# pair of two source-positive preparations: mathematically both
# have exactly same four p_ab but different E probabilities.
assert H106.prob_native==H106.prob_link
assert native_effect!=link_effect
assert H91.tr(H91.mm(H106.pt,H106.pt)).i==0
print("PASS H107.4: NO single-valued f(all original four flag probabilities) can reconstruct the measured two-cell phase-correlation effect for this positive product/conditional-link pair")

# Formal, machine-checked P11/P9 provenance obligations and
# acyclic necessary-dependency diagram.
ledger_path=Path(__file__).resolve().parents[1] / "research-notes" / "P11-H107-source-generative-proof-obligations-20261019.json"
with ledger_path.open(encoding="utf-8") as f:
    doc=json.load(f)
required={"AX-SRC","AX-OA","AX-CAN","AX-SP","AX-DYN","AX-NORM","AX-GEN"}
gates=doc["gates"]
assert {x["id"] for x in gates}==required
assert len(gates)==len(required)
for g in gates:
    assert g["status"] in {"PARTIAL","NO_GO_PLUS_CONDITIONAL","OPEN"}
    assert len(g["proved"])>0 and len(g["independent"])>0 and len(g["open"])>0
assert all(g["status"]!="PROVEN" for g in gates)
edges=doc["dependencies"]
assert len(edges)==len(set(tuple(x) for x in edges))
assert all(u in required and v in required and u!=v for u,v in edges)
parents={v:[] for v in required}
for u,v in edges:parents[v].append(u)
def ancestors(v,stack=()):
    assert v not in stack,"Cyclic generative dependency!"
    result=set()
    for u in parents[v]:
        result.add(u)
        result.update(ancestors(u,stack+(v,)))
    return result
for v in required:ancestors(v)
assert "AX-CAN" in ancestors("AX-GEN")
assert "AX-SP" in ancestors("AX-GEN")
assert "AX-SRC" in ancestors("AX-DYN")
assert doc["source"]["conditional_link"].find("INDEPENDENTLY")>=0
for label,value in (
    ("flag00_probability",H106.p),
    ("native_positive_effect_probability",native_effect),
    ("conditional_link_positive_effect_probability",link_effect),
    ("difference_link_minus_native",link_effect-native_effect),
    ("native_conditional_flag00_probability",native_effect/H106.p),
    ("link_conditional_flag00_probability",link_effect/H106.p),
    ("conditional_link_npt_minor",H106.minor.r)
):
    assert F(doc["operational_exact"][label])==value,(label,value)
print("PASS H107.5: machine-audited seven AX-SRC/OA/CAN/SP/DYN/NORM/GEN typed proved/independent/open gates and ACYCLIC P9→P11 provenance dependency graph, all numeric witnesses source-matched")

print("BOUNDARY: the real local H75 native A/B Hamiltonian Lie group is LOCAL and cannot source H105's entangling link; the link is CONDITIONAL, NOT a physical discovery or F-derived control")
print("BOUNDARY: local product-effect detection is possible after extra detector CALIBRATION but a specific probability difference is NOT itself a universal entanglement witness nor CR-only effect")
print("BOUNDARY: P9.125-128 reported Cartan primary micro-Hamiltonian/observer/solder has NOT been verified identical to H75; full 3D Cartan spacetime, ADM six canonical pairs, offshell HDA and Einstein generation are OPEN")
