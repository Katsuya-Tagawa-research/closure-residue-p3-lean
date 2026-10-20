#!/usr/bin/env python3
"""Exact canonical minimal H75 observer quotient and normalized affine rank.

Reruns original four-Kraus 9/36/45-by-18 rational response implementation
from P11 G2/G3 #171; constructs exact rational surjective quotient maps,
universal factor matrices, and normalized trace-one affine input slice.
No floating point, no F-access generation, no physical provenance claim.
"""
from pathlib import Path
import importlib.util
import sympy as sp

base=Path(__file__).resolve().parents[1]
upstream=base/"p11-g2-g3-relative-access-20261020"/"H75_G2_G3_Selector_Exact.py"
assert upstream.is_file(),f"missing original H75 exact finite checker: {upstream}"
spec=importlib.util.spec_from_file_location("h75_g2_g3_source",str(upstream))
h=importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)

def observer_coordinates(C):
    """Independent rows of C define V -> Q_C coordinates (no added inputs)."""
    rank=C.rank()
    pivots=C.T.rref()[1]
    assert len(pivots)==rank
    B=C[list(pivots),:]
    assert B.shape==(rank,18) and B.rank()==rank
    return B

def unique_left_factor(A,B):
    """Exact unique T with A=T B, B full row rank, row(A) subset row(B)."""
    solution, free=B.T.gauss_jordan_solve(A.T)
    assert free.rows==0
    T=solution.T
    assert T*B==A
    return T

C0,C4,C5=h.C0,h.C4,h.C5
assert [C.shape for C in (C0,C4,C5)]==[(9,18),(36,18),(45,18)]
assert [C.rank() for C in (C0,C4,C5)]==[6,17,18]

B0,B4,B5=[observer_coordinates(C) for C in (C0,C4,C5)]
D0,D4,D5=[unique_left_factor(C,B) for C,B in
           ((C0,B0),(C4,B4),(C5,B5))]
for C,B,D in ((C0,B0,D0),(C4,B4,D4),(C5,B5,D5)):
    assert C==D*B
    assert D.rank()==B.rows
    assert len(B.nullspace())==18-B.rows

# Canonical source-identity quotient maps, expressed in pivot coordinates.
T54=unique_left_factor(B4,B5)
T40=unique_left_factor(B0,B4)
T50=unique_left_factor(B0,B5)
assert [M.shape for M in (T54,T40,T50)]==[(17,18),(6,17),(6,18)]
assert [M.rank() for M in (T54,T40,T50)]==[17,6,6]
assert [len(M.nullspace()) for M in (T54,T40,T50)]==[1,11,12]
assert T40*T54==T50
assert [len(M.nullspace()) for M in (B0,B4,B5)]==[12,1,0]

# The original H75 previously audited signed flag ambiguity is precisely
# the single dimension lost by projection from Q5 (18D) to Q4 (17D).
x=h.xc
assert x.shape==(18,1)
assert B4*x==sp.zeros(17,1)
assert B5*x!=sp.zeros(18,1)
assert T54*B5*x==sp.zeros(17,1)

# These are REAL linear quotient dimensions. Density matrices additionally
# have trace 1; the normalized Born image is a one-codimension affine slice.
trace_row=sp.Matrix([[sp.trace(X) for X in h.basis]])
assert trace_row.shape==(1,18)
assert trace_row.rank()==1
for C in (C0,C4,C5):
    assert sp.Matrix.vstack(C,trace_row).rank()==C.rank()
tracezero=sp.Matrix.hstack(*trace_row.nullspace())
assert tracezero.shape==(18,17) and trace_row*tracezero==sp.zeros(1,17)
assert [int((C*tracezero).rank()) for C in (C0,C4,C5)]==[5,16,17]

# The genuine H75 flag-phase stabilizer fixes native flagged block inputs;
# it acts trivially on all three linear and normalized observer quotients.
phase=sp.kronecker_product(sp.diag(1,-1),sp.eye(3))
assert all(phase*X*phase==X for X in h.basis)

print("PASS: original H75 exact four-Kraus response matrices 9/36/45 x18")
print("PASS: minimal observer quotient dimensions Q0=6 Q4=17 Q5=18")
print("PASS: exact universal prediction factorization C_A = D_A B_A")
print("PASS: quotient surjections Q5 -> Q4 -> Q0 and their composition")
print("PASS: transition kernel dimensions 1,11,12")
print("PASS: native X_flag spans the 1D Q5->Q4 kernel")
print("PASS: normalized density-state response affine dimensions 5,16,17")
print("PASS: genuine H75 D_pi fixes the entire native quotient input")
print("OPEN: original source does not select the physical access catalog")
print("OPEN: F-generative completeness, P6 provenance and P9 Einstein")
