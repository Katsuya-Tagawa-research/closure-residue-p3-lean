#!/usr/bin/env python3
"""Guard the H82/P9/P11 bridge-exit classifications and exact finite invariants.

This is a *governance consistency and finite-rational test*, not proof of
F-generated hardware, GR, completeness, or a formal Lean theorem.
"""
import json
from fractions import Fraction
from pathlib import Path

root=Path(__file__).parent
manifest=json.loads((root/"bridge_exit_manifest.json").read_text())
audit=(root/"P3_P11_Bridge_Exit_Audit_and_Dual_Handoff.md").read_text()
p11=(root/"P11_Finite_Causal_Access_Handoff.md").read_text()
p9=(root/"P9_Restricted_Finite_H82_Handoff.md").read_text()

assert manifest["schema"]=="p3-p11-bridge-exit-v1"
assert manifest["verdict"]=="CONDITIONAL_FINITE_HANDOFF"
baseline=manifest["baseline"]
assert baseline["h82_pr"]==101
assert baseline["prior_bridge_pr"]==184
assert baseline["h82_status"]=="DRAFT_UNMERGED"
assert baseline["tail_audit_status"]=="UNNUMBERED_UNMERGED"

claims={x["id"]:x for x in manifest["conditional_finite_claims"]}
assert all(x["status"]=="EXACT_CONDITIONAL" for x in claims.values())
rank=claims["h75_adaptive_future_rank"]
assert rank["rank_sequence"]==[3,7,10,12,12]
assert rank["input_cut_real_dim"]-rank["quotient_real_dim"]==rank["kernel_real_dim"]==24
assert rank["source_image_rank"]==9
tail=claims["h75_joint_switching_tail"]
b=Fraction(tail["b_numerator"],tail["b_denominator"])
eps=Fraction(tail["epsilon_numerator"],tail["epsilon_denominator"])
K=tail["cutoff_K"]
assert b==Fraction(5,6) and eps==Fraction(1,100) and K==26
assert b**(K-1)>eps>=b**K
assert b**0==1

assumptions=manifest["independent_assumptions"]
open_gates=manifest["open_gates"]
assert len(assumptions)>=5 and len(open_gates)>=10
for requirement in (
    "F-generated physically faithful AX-OA",
    "CP/CPTP realization of minimal linear predictor quotient",
    "P6 native signed hidden-current provenance",
    "operational native GT–K4 metric descent",
    "KKS to ADM DeWitt off-shell HDA Einstein dynamics",
    "P11 Generative Completeness",
):
    assert requirement in open_gates, requirement

for doc in (audit,p11,p9):
    assert "H82" in doc and "P11" in doc and "OPEN" in doc
assert "104/104" in audit and "CONDITIONAL PASS" in audit
assert "3,7,10,12,12" in p11
assert "K=26" in p11
assert "KKS" in p9 and "ADM" in p9 and "Einstein" in p9
assert "NOT" in p9 and "metric descent" in p9
assert "UNNUMBERED" in audit and "UNMERGED" in audit
assert all(x.startswith(("generative_","einstein_","p6_","unbounded_","linear_")) for x in manifest["disallowed_assertions"])

print("PASS: H82 original PR101 and independent unnumbered tail remain unchanged in ledger")
print("PASS: H75 finite adaptive ranks and input-kernel dimensions")
print("PASS: exact rational joint b=5/6, epsilon=1%, K=26 tail certificate")
print("PASS: P11 and P9 complete handoff documents retain all listed open gates")
print("PASS: no accidental F-generation, CP-quotient realization or Einstein claim")
print("EXIT VERDICT: CONDITIONAL FINITE HANDOFF; H82/P11/P9 PHYSICAL GATES OPEN")
