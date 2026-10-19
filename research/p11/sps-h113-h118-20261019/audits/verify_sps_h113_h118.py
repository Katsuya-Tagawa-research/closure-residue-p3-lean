#!/usr/bin/env python3
"""SPS H113–H118 finite reproducibility runner. Not a physical-source certificate."""
from pathlib import Path
import subprocess
import sys
import json

D = Path(__file__).resolve().parent
cases = [
 ("H113", "P3P11_H113_static_primitive_no_go_audit.py", "PASS: H113 toy witness"),
 ("H114", "P3P11_H114_all_order_locality_audit.py", "47/47 exact assertions"),
 ("H115", "P3P11_H115_h37_exact_audit.py", '"rank_mod_1009": 25'),
 ("H116", "P3P11_H116_ax_bimod_independence_audit.py", "54 exact symbolic assertions"),
 ("H117", "P3P11_H117_primitive_functor_audit.py", '"gauge_H_stabilizer_dimension": 1'),
 ("H118", "P3P11_H118_source_locality_audit.py", "70 exact assertions"),
]
for name, script, marker in cases:
    proc = subprocess.run([sys.executable, str(D / script)],
                          cwd=D, text=True, capture_output=True, check=False)
    if proc.returncode or marker not in proc.stdout:
        print("FAIL", name, proc.returncode, proc.stdout[-1200:], proc.stderr[-1200:])
        raise SystemExit(1)
    print("SPS", name, "PASS")
h115 = json.loads((D / "P3P11_H115_h37_exact_results.json").read_text())
assert [x["M_rank"] for x in h115["generator_krylov_ranks"]] == [5,9,13,17,21,23,25]
assert [x["H_rank"] for x in h115["generator_krylov_ranks"]] == [0,4,8,12,16,18,20]
assert h115["L2_p0_02"] == "-1/4"
assert h115["rank_mod_101"] == h115["rank_mod_1009"] == 25
for key, file, count in [
 ("H116", "P3P11_H116_ax_bimod_exact_results.json", 54),
 ("H117", "P3P11_H117_primitive_functor_results.json", 50),
 ("H118", "P3P11_H118_source_locality_results.json", 70),
]:
    r=json.loads((D/file).read_text())
    assert r["all_passed"] and r.get("exact_assertions_passed",r.get("passed"))==count,key
print("SPS-H113--H118 finite audits PASS; physical source and P11 completeness OPEN")
