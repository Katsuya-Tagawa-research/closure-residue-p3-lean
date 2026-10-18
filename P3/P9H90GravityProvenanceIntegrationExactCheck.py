"""H90: exact relative micro-to-gravity symbol nonuniqueness and P9/P11 proof-gate audit.

The H75 microscopic CPTP source remains unchanged. K4 selectors, physical
solder and H83 scalar edge Hamiltonians are SEPARATELY DECLARED comparator
data. Different comparator matter H-H brackets are NOT different Einstein
solutions or any unconditional no-go against a stronger future F axiom.
"""
import json
from fractions import Fraction as F
from pathlib import Path

import P9H85A4EdgeSourceSelectionExactCheck as H85
import P9H83UltralocalGradientHDAGateExactCheck as H83
from P9H75SemicausalMicroMemorySourceExactCheck import R60
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,gc,Z0

assert R60[0][0]==I*gc(F(-32,135))
assert R60 != [[Z0 for j in range(6)] for i in range(6)]
assert H85.r==(F(0),F(16,25),F(16,25),F(4,25))
assert H85.W==27 and sum(H85.r)==F(36,25)
w_add=H85.additive(H85.r)
w_uni=H85.uniform(H85.r)
assert w_add==(4,4,1,8,5,5)
assert w_uni==(F(9,2),)*6
assert sum(w_add)==sum(w_uni)==27
assert w_add!=w_uni and all(w>0 for w in w_add+w_uni)
for perm in H85.A4:
    assert H85.additive(H85.permute_vertices(H85.r,perm))==H85.permute_edges(w_add,perm)
    assert H85.uniform(H85.permute_vertices(H85.r,perm))==H85.permute_edges(w_uni,perm)
print("PASS H90.1: identical genuine H75 micro flag data and fixed budget admit distinct A4-equivariant positive K4 weight selectors")

L_add,G_add=H85.k4metric(w_add)
L_uni,G_uni=H85.k4metric(w_uni)
v=(F(1),F(-1),F(0),F(0))
k_add=H85.contraction(L_add,v)
k_uni=H85.contraction(L_uni,v)
assert (k_add,k_uni)==(F(17,8),F(9,4))
assert G_add!=G_uni and k_add>0 and k_uni>0
print("PASS H90.1: same externally soldered v=e0-e1 gives candidate inverse-metric symbols 17/8 and 9/4")

P=H83.Poly
q=H83.q;mom=H83.p;N=H83.N;M=H83.M
assert H83.n==4

def edge_scalar(L,kinetic_A,gradient_k):
    return sum((
        F(kinetic_A,2)*L[i]*mom[i]*mom[i]
        + F(gradient_k,4)*(L[i]+L[(i+1)%4])
        *(q[(i+1)%4]-q[i])*(q[(i+1)%4]-q[i])
        for i in range(4)),P())

B=sum((
    (N[i]*M[(i+1)%4]-M[i]*N[(i+1)%4])
    *(mom[i]+mom[(i+1)%4])*(q[(i+1)%4]-q[i])
    for i in range(4)),P())
assert H83.HH == F(H83.A*H83.kappa,2)*B
profile=[F(0),F(1,2),F(1,3),F(-1,4),
         F(1),F(2),F(-1),F(3),
         F(1),F(0),F(2),F(-1),
         F(0),F(1),F(-1),F(2)]
assert profile==H83.state
assert B.eval(profile)==F(-11,3)
assert H83.HH.eval(profile)==F(-55,12)
print("PASS H90.1: independent canonical H83 polynomial antisymmetric lapse wedge B=-11/3")

def checked_bracket(k):
    HN=edge_scalar(N,F(1),k)
    HM=edge_scalar(M,F(1),k)
    bracket=H83.PB(HN,HM)
    assert bracket==F(k,2)*B
    return bracket.eval(profile)

b_add=checked_bracket(k_add)
b_uni=checked_bracket(k_uni)
assert b_add==F(-187,48)
assert b_uni==F(-33,8)
assert b_add-b_uni==F(11,48)
print("PASS H90.1: same source/solder but two imposed metric-coupled matter brackets -187/48 vs -33/8; delta=11/48")
print("BOUNDARY: conditional one-dimensional scalar matter H-H symbol only, NOT full off-shell ADM, observed gravity or Einstein solution")

ledger=json.loads(Path("research-notes/P9-H90-gravity-proof-gates-20261018.json").read_text(encoding="utf-8"))
valid={"EXACT","CONDITIONAL","NO-GO","OPEN"}
assert set(ledger["classification"])==valid
gates=ledger["gates"]
assert len(gates)==8 and [g["id"] for g in gates]==[f"G{i}" for i in range(8)]
assert gates[0]["generative_status"]=="EXACT"
assert all(g["generative_status"]=="OPEN" for g in gates[1:])
assert all(g["scope"].strip() and g["sources"] for g in gates)
assert all(item["classification"] in valid and item["sources"]
           for item in ledger["comparator_results"])
assert any(item["classification"]=="NO-GO" and "H90" in item["sources"]
           for item in ledger["comparator_results"])
print("PASS H90.2: typed P9/P11 ledger distinguishes proven H75 source from seven unresolved physical generative gates")
print("BOUNDARY: AX-OA/AX-SP/AX-CAN/AX-DYN are independent so far; four-level KKS and P9/HDA/Einstein dynamics not generated from H75/F")
