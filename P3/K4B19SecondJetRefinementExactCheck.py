"""P9 B19: finite K4 TT second-control-jet descent obstruction.

Exact rational verification only (Python stdlib), independent of Lean.
The underlying time-jet model is the declared unitary K4 family from
B14. This does not identify inherited P3/P6 CR physical controls.
"""
from fractions import Fraction as Q
from itertools import combinations

edges = list(combinations(range(4), 2))
r = [tuple(Q(int(j == a) - int(j == b)) for j in range(4))
     for a,b in edges]
zero = Q(0)
def dot(u,v):
    return sum((a*b for a,b in zip(u,v)), zero)

f1 = tuple(Q(v,2) for v in (1,1,-1,-1))
f2 = tuple(Q(v,2) for v in (1,-1,1,-1))
f3 = tuple(Q(v,2) for v in (1,-1,-1,1))
fs = [f1,f2,f3]
assert all(dot(fs[i],fs[j]) == Q(int(i==j))
           for i in range(3) for j in range(3))
assert all(sum(f,zero)==0 for f in fs)

# In h=4 dot, e_i=f_i/2 are h-orthonormal.
# The target TT coordinates q11-q22 and q12 of the form
# q_ij = h(e_i,A_w e_j)=f_i^T A_w f_j.
T = [[dot(f1,v)**2-dot(f2,v)**2 for v in r],
     [dot(f1,v)*dot(f2,v) for v in r]]
assert T == [[Q(-1),Q(1),zero,zero,Q(1),Q(-1)],
             [zero,zero,Q(1),Q(-1),zero,zero]]

uniform = tuple(Q(1,4) for _ in range(4))
p1 = tuple(a+b/4 for a,b in zip(uniform,f1))
p2 = tuple(a+b/4 for a,b in zip(uniform,f2))
assert p1 == tuple(Q(v,8) for v in (3,3,1,1))
assert p2 == tuple(Q(v,8) for v in (3,1,3,1))
assert all(sum(p,zero)==1 and min(p)>0 for p in (p1,p2))

# q_p(x)=(1/2) diag Phi''_{t=0,x}(diag p) = -A_{x^2} p.
# For each prepared population, L_p is the linear map w -> q_p.
def L(p):
    return [[-v[a]*dot(v,p) for v in r] for a in range(4)]
Lp1,Lp2 = L(p1),L(p2)
extracted = [
    [-4*(sum((f1[a]*Lp1[a][j] for a in range(4)),zero)
         -sum((f2[a]*Lp2[a][j] for a in range(4)),zero))
     for j in range(6)],
    [-4*sum((f1[a]*Lp2[a][j] for a in range(4)),zero)
     for j in range(6)]
]
assert extracted == T

# Define the observable control response y_alpha(x)=sum_e T_alpha,e x_e^2.
def y(x):
    return [sum((T[a][e]*x[e]**2 for e in range(6)),zero)
            for a in range(2)]
def J(x):
    return [[2*T[a][e]*x[e] for e in range(6)] for a in range(2)]
def H(u,v):
    return [2*sum((T[a][e]*u[e]*v[e] for e in range(6)),zero)
            for a in range(2)]
basis = [tuple(Q(int(e==j)) for e in range(6)) for j in range(6)]

def rank(rows):
    A = [list(map(Q,row)) for row in rows]
    if not A:return 0
    n,m=len(A),len(A[0]); i=0
    for j in range(m):
        k=next((k for k in range(i,n) if A[k][j]),None)
        if k is None:continue
        A[i],A[k]=A[k],A[i]; piv=A[i][j]
        for k in range(i+1,n):
            t=A[k][j]/piv
            for ell in range(j,m):A[k][ell]-=t*A[i][ell]
        i+=1
        if i==n:break
    return i

# At x=0: the first derivative is zero; the bilinear Hessian is
# nevertheless radical-free as a map u -> (v -> H(u,v)).
origin = (zero,)*6
assert all(all(v==0 for v in row) for row in J(origin))
radical_matrix = [
    [H(basis[e],basis[j])[a] for e in range(6)]
    for j in range(6) for a in range(2)
]
assert rank(radical_matrix)==6
assert all(H(basis[j],basis[j])==[2*T[a][j] for a in range(2)]
           for j in range(6))

# A *positive uniform-amplitude* basepoint, away from the origin.
xstar=(Q(1),)*6
assert rank(J(xstar))==2
k=(Q(1),Q(1),zero,zero,zero,zero)
assert [dot(row,k) for row in J(xstar)]==[zero,zero]
assert H(k,basis[0])==[Q(-2),zero]

# Therefore H cannot factor through J(xstar) on both entries:
# any factorization H(u,v)=Hbar(Ju,Jv) would kill k.
# Only the finite coefficient claim is checked by the script;
# logical factorization obstruction follows immediately.
for x in (origin,xstar,(Q(1),Q(2),Q(3),Q(4),Q(5),Q(6))):
    for j in range(6):
        assert H(basis[j],basis[j])==[
            (y(tuple(x[e]+basis[j][e] for e in range(6)))[a]
             +y(tuple(x[e]-basis[j][e] for e in range(6)))[a]
             -2*y(x)[a]) for a in range(2)]

# The Hessian being radical-free does not make y injective:
# individual edge signs are invisible to diagonal quadratic readout.
flip=list(xstar); flip[0]=-flip[0]
assert y(tuple(flip))==y(xstar)

print("PASS B19: P7 h=4 TT extraction from two positive K4 preparations")
print("PASS B19: D_x y(0)=0, Hessian radical rank six")
print("PASS B19: uniform positive point rank(D_y)=2 with explicit non-descending k")
print("PASS B19: exact centered second differences and edge-sign ambiguity")
print("Scope: declared finite K4 control family, no inherited physical P6 accessibility")
