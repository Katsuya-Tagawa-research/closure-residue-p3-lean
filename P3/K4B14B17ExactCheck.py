"""Exact rational executable B14/B17 finite K4 audit.

This is NOT a Lean theorem, a proof that CR requires six physical controls,
or an unconditional CR-specific prediction. No third-party dependencies.
"""
from fractions import Fraction as Q
from itertools import combinations

edges = list(combinations(range(4), 2))
pairs = [(0,0), (1,1), (2,2), (0,1), (0,2), (1,2)]

def det(a):
    a = [[Q(z) for z in row] for row in a]
    out = Q(1)
    for k in range(len(a)):
        p = next((i for i in range(k,len(a)) if a[i][k]), None)
        if p is None:
            return Q(0)
        if p != k:
            a[p], a[k] = a[k], a[p]
            out = -out
        v = a[k][k]
        out *= v
        for i in range(k+1,len(a)):
            c = a[i][k]/v
            for j in range(k+1,len(a)):
                a[i][j] -= c*a[k][j]
            a[i][k] = Q(0)
    return out

# Basis b_i=e_i-e_3 of 1-perp, i=0,1,2.
basis = [[int(a==i)-int(a==3) for a in range(4)] for i in range(3)]
proj = [[sum(basis[i][t]*(int(t==a)-int(t==b)) for t in range(4))
         for a,b in edges] for i in range(3)]
M = [[proj[i][e]*proj[j][e] for e in range(6)] for i,j in pairs]
assert det(M) == -256
G_uniform = [[sum(proj[i][e]*proj[j][e] for e in range(6))
              for j in range(3)] for i in range(3)]
assert G_uniform == [[8,4,4],[4,8,4],[4,4,8]]
# At x=(1,...,1), w_e=x_e**2, Dw=diag(2,...,2).
assert det([[2*int(i==j) for j in range(6)] for i in range(6)]) == 64
assert det([[2*z for z in row] for row in M]) == -16384

def matmul(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]

def comm(a,b):
    ab,ba=matmul(a,b),matmul(b,a)
    return [[ab[i][j]-ba[i][j] for j in range(len(a))]
            for i in range(len(a))]

def trace(a):
    return sum(a[i][i] for i in range(len(a)))

def edgeK(a,b):
    out=[[0]*4 for _ in range(4)]
    out[a][b]=1;out[b][a]=-1
    return out

K=[edgeK(a,b) for a,b in edges]
assert comm(K[0],K[3]) == K[1]  # [K_01,K_12]=K_02
J=K[1]
c=[[Q(-trace(matmul(J,comm(K[e],K[f]))),2)
    for f in range(6)] for e in range(6)]
assert all(c[e][f]==-c[f][e] for e in range(6) for f in range(6))
assert c[0][3]==1 and c[3][0]==-1
# V_(01,12)=partial_01 F_12 - partial_12 F_01.
assert c[3][0]-c[0][3]==-2
# Pullback of the same 1-form through w_e=x_e**2 at x=1.
assert Q(c[3][0]-c[0][3],4)==Q(-1,2)

print('Exact K4 tensor matrix determinant:',det(M))
print('Uniform symmetric quadratic form:',G_uniform)
print('Full six-weight Jacobian det at x=1:',64)
print('Composed symmetric tensor Jacobian det:',-16384)
print('Bracket-force curl with affine w section:',-2)
print('Bracket-force curl in w=x^2 chart at w=1:',Q(-1,2))
print('PASS: B14/B17 exact finite arithmetic; CR provenance is conditional')
