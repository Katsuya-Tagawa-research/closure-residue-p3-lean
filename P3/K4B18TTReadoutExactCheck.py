"""B18: exact finite K4 TT-only second-Hessian observability audit.

All arithmetic is rational. P7 spatial h=4 dot is respected through
the rational h-orthonormal frame e_i=f_i/2, where f_i are Euclidean
orthonormal Hadamard vectors. No continuum/physical CR accessibility
or Einstein equation is inferred.
"""
from fractions import Fraction as F
from itertools import combinations

EDGES = list(combinations(range(4), 2))
R = [tuple(F(int(i == a) - int(i == b)) for i in range(4))
     for a, b in EDGES]

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))

def rank(rows):
    a = [list(map(F, row)) for row in rows]
    if not a:
        return 0
    m, n, k = len(a), len(a[0]), 0
    for j in range(n):
        piv = next((i for i in range(k, m) if a[i][j]), None)
        if piv is None:
            continue
        a[k], a[piv] = a[piv], a[k]
        c = a[k][j]
        for i in range(k + 1, m):
            t = a[i][j] / c
            for jj in range(j, n):
                a[i][jj] -= t*a[k][jj]
        k += 1
        if k == m:
            break
    return k

def hessian_rows(preparations):
    # Rows of q=-A_w p, where q=(1/2) diag rho''(0).
    return [[-r[a]*dot(r, p) for r in R]
            for p in preparations for a in range(4)]

f1 = tuple(map(F, (F(1,2), F(1,2), -F(1,2), -F(1,2))))
f2 = tuple(map(F, (F(1,2), -F(1,2), F(1,2), -F(1,2))))
f3 = tuple(map(F, (F(1,2), -F(1,2), -F(1,2), F(1,2))))
fs = (f1, f2, f3)
assert all(dot(a,b) == (1 if i == j else 0)
           for i,a in enumerate(fs) for j,b in enumerate(fs))
assert all(sum(v) == 0 for v in fs)

# In h=4 dot, e_i=f_i/2 is orthonormal. Tensor form coordinates
# h(e_i,A_w e_j)=f_i^T A_w f_j. xi=e3, TT=(q11-q22,q12).
plus = [dot(f1,r)**2 - dot(f2,r)**2 for r in R]
cross = [dot(f1,r)*dot(f2,r) for r in R]
T = [plus, cross]
assert T == [[F(-1),F(1),F(0),F(0),F(1),F(-1)],
             [F(0),F(0),F(1),F(-1),F(0),F(0)]]
assert rank(T) == 2

delta = lambda i: tuple(F(int(j == i)) for j in range(4))
for i in range(4):
    m = hessian_rows([delta(i)])
    assert rank(m) == 3
    assert rank(m+T) == 5

for i,j in combinations(range(4),2):
    m = hessian_rows([delta(i),delta(j)])
    assert rank(m) == 5
    assert rank(m+T) == 6

uniform = tuple(F(1,4) for _ in range(4))
prep1 = tuple(u + a/4 for u,a in zip(uniform,f1))
prep2 = tuple(u + a/4 for u,a in zip(uniform,f2))
assert prep1 == (F(3,8),F(3,8),F(1,8),F(1,8))
assert prep2 == (F(3,8),F(1,8),F(3,8),F(1,8))
assert all(sum(p)==1 and min(p)>0 for p in (prep1,prep2))

m = hessian_rows([prep1,prep2])
assert rank(m)==5
assert rank(m+T)==5

# Direct extraction from two measured short-time Hessian vectors:
# plus = -4(f1·q(prep1) - f2·q(prep2))
# cross = -4 f1·q(prep2), coefficientwise for each of six weights.
computed_plus = [-4*(sum(f1[a]*m[a][j] for a in range(4))
                     -sum(f2[a]*m[4+a][j] for a in range(4)))
                 for j in range(6)]
computed_cross = [-4*sum(f1[a]*m[4+a][j] for a in range(4))
                  for j in range(6)]
assert computed_plus == plus
assert computed_cross == cross

# One nonzero undetected conductance perturbation remains but is TT-silent.
hidden = (F(1),F(1),F(-1),F(-1),F(1),F(1))
assert all(dot(row,hidden)==0 for row in m)
assert all(dot(row,hidden)==0 for row in T)

print("PASS: exact h=4 Hadamard spatial frame and finite TT rank two")
print("PASS: two localized preparations do not determine TT")
print("PASS: two calibrated positive mixed preparations determine TT exactly")
print("PASS: full six conductances remain underdetermined at two probes")
print("Scope: static finite TT coordinates from K4 quadratic readout only")
