#!/usr/bin/env python3
"""Exact H75 24-output Herm(3)+Herm(3) stability audit.

The exact theorem is verified over Q by LDL positivity.
Floating-point SVD values are informative only, not proof.
Requires sympy and numpy. No external input artifacts.
"""
from itertools import combinations
import math
import sympy as sp
import numpy as np

I, R = sp.I, sp.Rational
eye = sp.eye
def E(i, j):
    return eye(3)[:, i] * eye(3)[j, :]

O = sp.Matrix([
    [R(2, 3), R(2, 3), -R(1, 3)],
    [-R(2, 3), R(1, 3), -R(2, 3)],
    [-R(1, 3), R(2, 3), R(2, 3)]
])
U = sp.diag(I, 1, I) * O
M = [sp.diag(1, R(3, 5), R(3, 5)), sp.diag(0, R(4, 5), R(4, 5))]
kraus = [
    sp.kronecker_product(eye(2)[:, a] * eye(2)[b, :], U * M[a])
    for a in range(2) for b in range(2)
]
assert sum((k.H * k for k in kraus), sp.zeros(6)) == eye(6)

W = sp.kronecker_product(
    sp.Matrix([[R(3, 5), -R(4, 5)], [R(4, 5), R(3, 5)]]), eye(3)
)
S = E(0, 1) + E(1, 0) + E(2, 2)
F_fb = (sp.kronecker_product(sp.diag(1, 0), eye(3))
        + sp.kronecker_product(sp.diag(0, 1), S))
A = E(0, 1) - E(1, 0)
B = E(2, 1) - E(1, 2)

def V(x, y):
    v = (eye(3) + x * A) * (eye(3) - x * A).inv()
    v *= (eye(3) + y * B) * (eye(3) - y * B).inv()
    return sp.kronecker_product(eye(2), v)

V_A = V(R(1, 4), R(0))
V_B = V(R(0), R(1, 2))
V_AB = V(R(1, 4), R(1, 3))
pre = [eye(6), F_fb, F_fb * V_A, F_fb * W * V_B * F_fb * W]
post = [eye(6), V_A, V_AB]
site_effect = [sp.kronecker_product(eye(2), E(j, j)) for j in range(3)]

for gate in pre + post:
    assert sp.simplify(gate.H * gate) == eye(6)

basis = []
for flag in range(2):
    for j in range(3):
        b = sp.zeros(6)
        b[3 * flag:3 * (flag + 1), 3 * flag:3 * (flag + 1)] = E(j, j)
        basis.append(b)
    for j, k in combinations(range(3), 2):
        for block in [E(j, k) + E(k, j), I * (E(j, k) - E(k, j))]:
            b = sp.zeros(6)
            b[3 * flag:3 * (flag + 1), 3 * flag:3 * (flag + 1)] = block
            basis.append(b)
assert len(basis) == 18

rows = []
for p in pre:
    for t in post:
        for q in site_effect:
            effect = t.H * q * t
            propagated = sum((k.H * effect * k for k in kraus), sp.zeros(6))
            effective = p.H * propagated * p
            row = [sp.simplify(sp.trace(effective * b)) for b in basis]
            assert all(value.is_Rational for value in row)
            rows.append(row)
C = sp.Matrix(rows)
assert C.shape == (36, 18)
assert C.rank() == 18

bounds = {(0, 1): R(3, 50), (0, 2): R(1, 20),
          (1, 2): R(1, 25)}
targets = {(0, 1): 0.0691704520303242,
           (0, 2): 0.057503007424694844,
           (1, 2): 0.04453557089591342}

for pair, lower in bounds.items():
    # Each 9 rows represent 3 post programs x 3 site projectors,
    # within each of the 4 pre-reset programs.
    indices = [9 * i + 3 * j + k
               for i in range(4) for j in range(3) for k in pair]
    D = C[indices, :]
    assert D.shape == (24, 18) and D.rank() == 18
    shifted_gram = D.T * D - lower ** 2 * eye(18)
    L, Diag = shifted_gram.LDLdecomposition(hermitian=False)
    assert all(v.is_Rational and v > 0 for v in Diag.diagonal())
    assert L * Diag * L.T == shifted_gram
    spectrum = np.linalg.svd(np.array(D, dtype=float), compute_uv=False)
    smin = float(spectrum[-1])
    assert abs(smin - targets[pair]) < 1e-9
    eps = math.sqrt(24) / smin * math.sqrt(math.log(48 / 0.05) / 200000)
    print(f"{pair}: rank=18, EXACT sigma_min>{lower}, "
          f"SVD sigma_min~{smin:.10f}, kappa~{spectrum[0]/smin:.6f}, "
          f"Hoeffding bound at 100000 shots/effect~{eps:.6f}")

sig_full = np.linalg.svd(np.array(C, dtype=float), compute_uv=False)
assert abs(float(sig_full[-1]) - 0.08639602732862814) < 1e-9
print(f"all 36: rank=18, SVD sigma_min~{sig_full[-1]:.10f}")
print("PASS: original H75 source, exact rational rank/LDL spectral lower bounds")
