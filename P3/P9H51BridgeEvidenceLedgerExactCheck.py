"""H51 exact machine-checkable evidence ledger and P9 no-promotion gates.

This audit intentionally DOES NOT claim new physics or independent human
review. It checks the 16-entry H35-H50 ledger, PR provenance chain,
necessary source restrictions and selected existing exact finite
witnesses. Original H35-H50 CI remains independently archived.

Run from repository root:
    python3 P3/P9H51BridgeEvidenceLedgerExactCheck.py
"""
import json
from pathlib import Path
from fractions import Fraction as F

ROOT=Path(__file__).resolve().parent.parent
LEDGER=ROOT/"research-notes/P9-H51-evidence-ledger-20261015.json"
D=json.loads(LEDGER.read_text(encoding="utf-8"))
rows=D["milestones"]
assert len(rows)==16
assert [e["id"] for e in rows]==[f"H{i}" for i in range(35,51)]
assert [e["pr"] for e in rows]==list(range(54,70))
assert all(e["pr_url"].endswith(f"/pull/{e['pr']}") for e in rows)
assert all(all(e[k] for k in ("claim","assumptions","p9_import","guard",
                               "status")) for e in rows)
assert all(e["status"] in D["definitions"] for e in rows)
assert D["source_cross_audit"]["pr"]==53
assert D["source_chain"]["first_pr"]==54
assert D["source_chain"]["last_pr"]==69
assert D["source_chain"]["all_draft_unmerged_at_audit"]
assert D["source_chain"]["ci_report"]["workflows_passed"]==63
assert D["source_chain"]["ci_report"]["workflows_total"]==63
assert "not human expert" in D["source_chain"]["ci_report"]["limitation"]
statuses={name:sum(e["status"]==name for e in rows)
          for name in D["definitions"]}
assert statuses=={
 "PROVEN_FINITE":7,
 "PROVEN_GENERAL_CONDITIONAL_PREMISES":1,
 "CONDITIONAL":5,
 "REFUTED_IMPLICATION":3,
 "OPEN":0
}
by_id={r["id"]:r for r in rows}
# Explicit categorical safeguards against the major observed research
# overclaims, and a nonempty physical-source exclusion for the
# conditional experiment and the completed process-equivalence theorem.
for idx in ("H39","H41","H46","H47","H49"):
    assert by_id[idx]["status"]=="CONDITIONAL"
for idx in ("H37","H38","H42"):
    assert by_id[idx]["status"]=="REFUTED_IMPLICATION"
assert by_id["H50"]["status"]=="PROVEN_GENERAL_CONDITIONAL_PREMISES"
assert "FULL" in by_id["H50"]["assumptions"]
assert len(D["global_open_gates"])==8
gate_ids={g["gate"] for g in D["global_open_gates"]}
assert gate_ids=={
 "G-SOURCE","G-PHYSICAL-CONTROL","G-DISCRIMINATOR",
 "G-SOLDER","G-ACTION","G-DYNAMICS","G-CONTINUUM",
 "G-COMPLETENESS"
}
assert len(D["forbidden_promotions"])>=8
assert len(D["p9_allowed"])>=4 and len(D["p9_not_allowed"])>=4

# Exact previously audited original-P3 and observer assertions.
# Imported modules execute their original rational checks; H51 is
# evidence-INTEGRATION, not a replacement for the previous audits.
from P9H45QuadraticResidueSufficientOddSeedExactCheck import (
    R_EE,R_OE,R_OO,real_parity_parameters,D as Seed,R12,
    same_seed_formula
)
from P9H44MinimalObserverMemoryQuadraticResidueExactCheck import (
    carrier,coordsE,memory,basis as even_basis,odd_basis,Phi,
    real_rank_complex
)
from P9H48InstrumentProvenanceKernelClosureExactCheck import (
    vec_rank,classical_record,quantum_record,full_record,
    LOCKED,UNLOCKED,Kphys,Jimage,rr,unit
)
from P9H47PreregisteredInstrumentComparatorExactCheck import (
    lower,lower_timed,p_wrong,EXACT_CALIBRATION
)
from P9H50OperationalEquivalenceClosureExactCheck import (
    controls,outcomes,qflag,sign_channel,
    correlated_two,independent_two,superposed
)
assert R_OO==3*R_EE and R_EE!=R_OE
assert rr([R_EE,R_OE])==2
d=Seed(F(3,8),F(1,2),F(1,8))
_,e,q=real_parity_parameters(d)
assert R12(d,d)==same_seed_formula(e,q)
assert len(even_basis)==5 and len(odd_basis)==4
assert real_rank_complex([carrier(unit(i,j))
       for i in range(3) for j in range(3)])==5
assert real_rank_complex([coordsE(unit(i,j))
       for i in range(3) for j in range(3)])==4
assert vec_rank(classical_record)==3
assert vec_rank(quantum_record)==4
assert vec_rank(full_record)==7
assert vec_rank(full_record,2)==9
assert rr(Jimage+[Kphys(*LOCKED)])==2
assert rr(Jimage+[Kphys(*UNLOCKED)])==3
assert lower>F(0) and lower_timed>F(0)
assert p_wrong<F(1,100)
assert EXACT_CALIBRATION["total_coherent_tangent_squared_norm"]==F(18,25)
assert qflag(outcomes[LOCKED])==F(0)
assert qflag(outcomes[UNLOCKED])==F(-3456,43681)
assert correlated_two(superposed)!=independent_two(superposed)

print("PASS H51: exactly 16 H35-H50 grounded Draft-PR evidence rows, PR #54-69")
print("PASS H51: primary classification 7 proven finite, 1 proven conditional-process lemma, 5 conditional, 3 refuted implications")
print("PASS H51: 8 independently OPEN source/provenance/soldering/EH/HDA/continuum/completeness gates")
print("PASS H51: actual original-P3 residue, 4/5 and 3/4/7/9 observer-rank hierarchy independently cross-checked")
print("PASS H51: conditional H47 finite-time gap and H50 same-standard-process/no-go scope preserved")
print("PASS H51: complete one-time-only non-Markovian-equivalence caveat preserved")
print("BOUNDARY: numeric CI PASS != human peer review, actual P6 hardware, CR-only observation or Einstein dynamics")
