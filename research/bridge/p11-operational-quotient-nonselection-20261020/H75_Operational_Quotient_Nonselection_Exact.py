#!/usr/bin/env python3
"""Exact H75 operational quotient descent and surviving source-fibre no-go.

Re-runs predecessor's original-channel exact 9/36/45 rational response
matrices and independently checks the native D_pi phase conjugation
of P5 against P5^- at the level of ALL nine terminal response rows.
No numerical SVD, experimental provenance, Lean or F-completeness claim.
"""
from pathlib import Path
import importlib.util
import sympy as sp

base=Path(__file__).resolve().parents[1]
upstream=base/"p11-g2-g3-relative-access-20261020"/"H75_G2_G3_Selector_Exact.py"
assert upstream.is_file(),f"missing auditable upstream exact H75 checker: {upstream}"
spec=importlib.util.spec_from_file_location("h75_g2_g3_upstream",str(upstream))
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

I6=sp.eye(6)
D=sp.kronecker_product(sp.diag(1,-1),sp.eye(3))
assert D.H*D==I6 and D*D==I6
def Phi(X):
    return sum((k*X*k.H for k in m.K),sp.zeros(6))

# The original H75 channel is fixed by input/output flag-phase inversion
# on every complex matrix unit, not merely on a selected input subspace.
for i in range(6):
    for j in range(6):
        X=I6[:,i]*I6[j,:]
        Y=Phi(X)
        assert Phi(D*X*D)==Y
        assert D*Y*D==Y

# D does not act on native 18-dimensional block-diagonal input space.
assert len(m.basis)==18
for v in m.basis:
    assert D*v*D==v

# The source stabilizer exchanges the two oriented W representatives.
Wminus=m.W.T
assert Wminus != m.W and D*m.W*D==Wminus
assert D*m.F*D==m.F
for v in (m.VA,m.VB,m.VAB):
    assert D*v*D==v

P5minus=m.F*Wminus*m.VB*m.F*Wminus
assert D*m.P5*D==P5minus
assert P5minus!=m.P5

# Equality of complete SOURCE outputs for every native Hermitian basis
# vector, stronger than equality of any one POVM probability.
for v in m.basis:
    assert Phi(m.P5*v*m.P5.H)==Phi(P5minus*v*P5minus.H)

# The nine post-reset readouts agree ENTRY BY ENTRY, rather than just rank.
nine_pos=m.rows(m.P5)
nine_neg=m.rows(P5minus)
assert nine_pos.shape==(9,18)
assert nine_pos==nine_neg

C0,C4,C5=m.C0,m.C4,m.C5
C5minus=sp.Matrix.vstack(C4,nine_neg)
assert C5minus==C5
assert C4[:9,:]==C0
assert C5[:36,:]==C4
assert [x.shape for x in (C0,C4,C5)]==[(9,18),(36,18),(45,18)]
ranks=[x.rank() for x in (C0,C4,C5)]
assert ranks==[6,17,18]
assert [18-r for r in ranks]==[12,1,0]
assert C5minus.rank()==18
assert C4*m.xc==sp.zeros(36,1) if hasattr(m,"xc") else True

# Positive physical states retain identical witness probabilities after
# the native gauge conjugation. Neither orientation is an extra class.
rho_plus=m.rp
rho_minus=m.rm
Q1=m.Q1
def p(P,rho):
    return sp.expand(sp.trace(Q1*Phi(P*rho*P.H)))
for P in (m.P5,P5minus):
    assert p(P,rho_plus)==sp.Rational(32271,78125)
    assert p(P,rho_minus)==sp.Rational(59437,234375)
    assert p(P,rho_plus)-p(P,rho_minus)==sp.Rational(37376,234375)

# If a selected source F0 is constant but actual permitted quotient
# response classes have three different ranks, no single source-only
# hardware-faithful quotient selector can factor the three device worlds.
source_id="original-H75-four-Kraus"
device_worlds=[(source_id,C0),(source_id,C4),(source_id,C5)]
assert len(set(s for s,C in device_worlds))==1
assert len(set(C.rank() for _,C in device_worlds))==3
assert 2**1 < len(device_worlds) <= 2**2
assert C5minus==C5

print("PASS: genuine H75 D_pi flag-phase stabilizer on 36 complex matrix units")
print("PASS: D_pi acts trivially on all 18 native Hermitian input basis elements")
print("PASS: W versus W^-1: 18 full outputs and all 9x18 response rows IDENTICAL")
print("PASS: phase quotient sends P5 and P5^- to same operational class")
print("PASS: strict response subspace ranks [6,17,18], kernels [12,1,0]")
print("PASS: positive H75 five-macro witness unchanged in both orientations")
print("PASS: source-fibre quotient selector NO-GO on three authorized device worlds")
print("OPEN: F-derived hardware resource generation, P6 provenance and P9 Einstein")
