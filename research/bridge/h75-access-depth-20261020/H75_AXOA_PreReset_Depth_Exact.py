#!/usr/bin/env python3
"""Exact H75 AX-OA pre-reset control-depth audit (SymPy over Gaussian rationals)."""
import sympy as sp
from itertools import combinations

R, I = sp.Rational, sp.I
E = lambda i, j: sp.eye(3)[:, i] * sp.eye(3)[j, :]
Id = sp.eye(6)
S = E(0, 1) + E(1, 0) + E(2, 2)
W = sp.kronecker_product(
    sp.Matrix([[R(3, 5), -R(4, 5)], [R(4, 5), R(3, 5)]]),
    sp.eye(3)
)
F = (sp.kronecker_product(sp.diag(1, 0), sp.eye(3))
     + sp.kronecker_product(sp.diag(0, 1), S))
A = E(0, 1) - E(1, 0)
B = E(2, 1) - E(1, 2)

def V(x, y):
    v = ((sp.eye(3) + x*A)*(sp.eye(3) - x*A).inv()
         *(sp.eye(3) + y*B)*(sp.eye(3) - y*B).inv())
    return sp.kronecker_product(sp.eye(2), v)

VA, VB, VAB = V(R(1, 4), 0), V(0, R(1, 2)), V(R(1, 4), R(1, 3))
G = {"W": W, "F": F, "A": VA, "B": VB, "C": VAB}
for gate in G.values():
    assert gate.T * gate == Id
X = sp.diag(-1, -1, -1, 1, 1, 1)
pt = lambda z: z[:3, :3] + z[3:, 3:]
assert pt(X) == sp.zeros(3)

# Enumerate ALL 5^0 + ... + 5^4 = 781 word expressions,
# including repetitions and algebraically duplicate words.
current = [("", X)]
counts = []
for depth in range(5):
    assert all(pt(z) == sp.zeros(3) for seq, z in current)
    counts.append(len(current))
    current = [(seq + label, gate*z*gate.T)
               for seq, z in current for label, gate in G.items()]
assert counts == [1, 5, 25, 125, 625]

Pshort = F*VB                  # chronological VB, F
Plong = F*W*VB*F*W             # chronological W, F, VB, W, F
assert pt(Pshort*X*Pshort.T) == sp.zeros(3)
expected = sp.Matrix([
    [-R(9216, 15625), 0, R(18432, 15625)],
    [0, R(9216, 15625), -R(18432, 15625)],
    [R(18432, 15625), -R(18432, 15625), 0]
])
assert pt(Plong*X*Plong.T) == expected and expected != sp.zeros(3)

# Exact original H75 four-Kraus source; no substitute channel.
O = sp.Matrix([
    [R(2, 3), R(2, 3), -R(1, 3)],
    [-R(2, 3), R(1, 3), -R(2, 3)],
    [-R(1, 3), R(2, 3), R(2, 3)]
])
U = sp.diag(I, 1, I)*O
M = [sp.diag(1, R(3, 5), R(3, 5)),
     sp.diag(0, R(4, 5), R(4, 5))]
K = [sp.kronecker_product(sp.eye(2)[:, a]*sp.eye(2)[b, :], U*M[a])
     for a in range(2) for b in range(2)]
assert sum((k.H*k for k in K), sp.zeros(6)) == Id
post = [Id, VA, VAB]
qs = [sp.kronecker_product(sp.eye(2), E(j, j)) for j in range(3)]
effects = [
    sum((k.H*t.H*q*t*k for k in K), sp.zeros(6))
    for t in post for q in qs
]

# 18 real Hermitian coordinates, three diag + three X/Y pairs per flag.
basis = []
for flag in range(2):
    for j in range(3):
        b = sp.zeros(6)
        b[3*flag:3*flag+3, 3*flag:3*flag+3] = E(j, j)
        basis.append(b)
    for j, k in combinations(range(3), 2):
        for block in (E(j, k)+E(k, j), I*(E(j, k)-E(k, j))):
            b = sp.zeros(6)
            b[3*flag:3*flag+3, 3*flag:3*flag+3] = block
            basis.append(b)
assert len(basis) == 18

def response(P):
    rows = []
    for ef in effects:
        op = P.T*ef*P
        row = [sp.expand(sp.trace(op*b)) for b in basis]
        assert all(t.is_Rational for t in row)
        rows.append(row)
    return sp.Matrix(rows)

base = sp.Matrix.vstack(*(response(p) for p in [Id, F, F*VA]))
Cshort = sp.Matrix.vstack(base, response(Pshort))
Clong = sp.Matrix.vstack(base, response(Plong))
assert Cshort.shape == (36, 18) and Cshort.rank() == 17
assert Clong.shape == (36, 18) and Clong.rank() == 18
xcoords = sp.Matrix([-1, -1, -1]+[0]*6+[1, 1, 1]+[0]*6)
assert sum((xcoords[i]*basis[i] for i in range(18)), sp.zeros(6)) == X
assert Cshort*xcoords == sp.zeros(36, 1)
assert Clong*xcoords != sp.zeros(36, 1)

rho_plus, rho_minus = Id/6+X/12, Id/6-X/12
assert rho_plus.trace() == rho_minus.trace() == 1
assert all(x > 0 for x in rho_plus.diagonal())
assert all(x > 0 for x in rho_minus.diagonal())
readout = effects[1]          # post identity, site-1 positive projector
p_plus = sp.expand(sp.trace(readout*Plong*rho_plus*Plong.T))
p_minus = sp.expand(sp.trace(readout*Plong*rho_minus*Plong.T))
assert p_plus == R(32271, 78125)
assert p_minus == R(59437, 234375)
assert p_plus-p_minus == R(37376, 234375)
print("PASS exact: word counts", counts, "total", sum(counts))
print("PASS exact: short-depth common silent flag direction")
print("PASS exact: 36x18 rank transition", Cshort.rank(), "to", Clong.rank())
print("PASS exact: first depth-5 partial trace", expected)
print("PASS exact: strictly-positive Born pair", p_plus, p_minus,
      "delta", p_plus-p_minus)
