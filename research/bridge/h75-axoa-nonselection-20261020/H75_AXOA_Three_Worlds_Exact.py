#!/usr/bin/env python3
"""H75 3-access-world source-only AX-OA nonselection: exact rational finite witness.

This checks the same original source and source-catalog response matrices.
The abstract set-theoretic factorization theorem is proved in the research
note, not represented as a universally quantified computational check.
"""
import importlib.util
from pathlib import Path
import sympy as sp

# Import prior exact source checker from the stacked #168/#169 code,
# so we compare precisely the SAME four H75 Kraus operators/gates.
source_path = (Path(__file__).resolve().parents[1]
               / "h75-access-depth-20261020"
               / "H75_AXOA_PreReset_Depth_Exact.py")
assert source_path.is_file(), "Expected source-verified H75 predecessor checker"
spec = importlib.util.spec_from_file_location("h75_source_depth", source_path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)     # independently rechecks 781 short words and source witness

C0 = m.response(m.Id)                      # 1 * 3 * 3 = 9 effects
C4 = m.Cshort                             # 4 * 3 * 3 = 36 effects
C5 = sp.Matrix.vstack(C4, m.response(m.Plong))  # 5 * 3 * 3 = 45 effects
assert (C0.shape, C4.shape, C5.shape) == ((9,18),(36,18),(45,18))
assert C4[:9,:] == C0
assert C5[:36,:] == C4

# All rank certificates are exact over Gaussian rational input/source,
# with real rational output probabilities.
ranks = [C0.rank(), C4.rank(), C5.rank()]
assert ranks == [6, 17, 18]
assert [18-r for r in ranks] == [12,1,0]

# Common kernel of the four short pre-programs is exactly the positive-state
# flag-bias direction, no unseen independent dimension.
Xcoords = m.xcoords
assert C0*Xcoords == sp.zeros(9,1)
assert C4*Xcoords == sp.zeros(36,1)
assert C5*Xcoords != sp.zeros(45,1)
null4 = C4.nullspace()
assert len(null4) == 1
assert sp.Matrix.hstack(null4[0], Xcoords).rank() == 1
assert C5.nullspace() == []

# The STRICT inclusion ker(C4) subset ker(C0) proves the classes differ
# already as observable equivalences, not just number of registered outcomes.
null0 = C0.nullspace()
assert len(null0)==12
assert all(C4*u == sp.zeros(36,1) for u in null4)
assert any(C4*u != sp.zeros(36,1) for u in null0)

# Every undetectable Hermitian input direction has zero trace: the sum of
# the three site POVM effects for a fixed program equals identity.
assert all(sum(m.basis[i].trace()*v[i] for i in range(18)) == 0 for v in null0)

rho_p, rho_m = m.rho_plus, m.rho_minus
assert rho_p != rho_m
assert rho_p.trace()==1 and rho_m.trace()==1
assert all(v > 0 for v in list(rho_p.diagonal())+list(rho_m.diagonal()))

# The SAME strictly positive witness is indistinguishable by A0/A4 but
# distinguishable by the newly registered fifth pre-reset macro word.
delta = (m.response(m.Plong) * Xcoords)[1] / 6
assert delta == sp.Rational(37376,234375)
assert m.p_plus-m.p_minus == delta

print("PASS: same H75 source, three nested catalogs of 9/36/45 genuine positive-effect rows")
print("PASS: exact rank triple",ranks,"and kernel nullities",[18-r for r in ranks])
print("PASS: exact kernel chain ker(C5)=0 < ker(C4)=span Xflag < ker(C0)")
print("PASS: strictly positive same-source witness delta",delta)
print("NO-GO: source-only single-valued hardware-faithful AX-OA selector on three worlds")
print("BOUNDARY: does not exclude a new F-side physical selection axiom or calibrated hardware priors")
