"""P9.23 H21-H23 audit: silent ideals, CPTP commutator loop, P3 residue mismatch.

Pure standard-library, exact rational truncated power series to degree 5.
These finite facts are NOT an inherited physical P6 control or soldering theorem.
"""
from fractions import Fraction as Q
from math import factorial
from itertools import combinations

n=4
edges=list(combinations(range(n),2))
q0=Q(0)
def zero(): return [[q0 for _ in range(n)] for _ in range(n)]
def ident():
    a=zero()
    for i in range(n): a[i][i]=Q(1)
    return a
def add(a,b): return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
def scale(a,t): return [[t*a[i][j] for j in range(n)] for i in range(n)]
def sub(a,b): return add(a,scale(b,-1))
def mul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(n)),q0)
             for j in range(n)] for i in range(n)]
def bracket(a,b): return sub(mul(a,b),mul(b,a))
def transpose(a): return [list(v) for v in zip(*a)]
def gen(i,j):
    a=zero();a[i][j]=Q(1);a[j][i]=Q(-1);return a
def dmat(v):
    a=zero()
    for i in range(n):a[i][i]=Q(v[i])
    return a
def vec(a): return [a[i][j] for i,j in edges]
def symmetric(a): return transpose(a)==a

K01,K02,K03,K12,K13,K23=[gen(*e) for e in edges]
assert bracket(K01,K12)==K02
assert bracket(K01,K02)==scale(K12,-1)

# Projection onto lower-right 3x3 Lie block (indices 1,2,3).
def visible_block(a): return tuple(a[i][j] for i,j in combinations((1,2,3),2))
null_block=(K01,K02,K03)
assert all(visible_block(x)==(q0,)*3 for x in null_block)
assert visible_block(bracket(K01,K02))!=(q0,)*3
# Therefore this kernel is not an ideal and this block projection is
# not a Lie algebra homomorphism from so(4) onto so(3).

# Self/anti-self-dual decomposition, oriented standard R^4.
plus=[add(K01,K23),sub(K02,K13),add(K03,K12)]
minus=[sub(K01,K23),add(K02,K13),sub(K03,K12)]
def lin(basis,coeffs):
    out=zero()
    for a,c in zip(basis,coeffs):out=add(out,scale(a,c))
    return out
assert all(bracket(a,b)==zero() for a in plus for b in minus)
assert all(bracket(g,x)==lin(minus,vec(bracket(g,x))[:3])
           for g in (K01,K02,K03,K12,K13,K23) for x in minus)
assert all(bracket(g,x)==lin(plus,vec(bracket(g,x))[:3])
           for g in (K01,K02,K03,K12,K13,K23) for x in plus)
# Both 3-dimensional eigenspaces are genuine ideals.

# Full first-time population observer on any diagonal state is zero.
p=(Q(1),q0,q0,q0); D=dmat(p)
assert all(bracket(g,D)[i][i]==0 for g in (K01,K12,K02)
           for i in range(n))
# Its complete kernel is all so(4), trivially an ideal, yet
# population quadratic return from K02 is NONZERO.
return02=scale(bracket(K02,bracket(K02,D)),Q(1,2))
assert [return02[i][i] for i in range(n)]==[Q(-1),q0,Q(1),q0]

# IMPORTANT: Original P3 quadratic residue is Delta_D([z,w*])
# with z,w in off-diagonal Krylov hidden space; for an orthogonal
# channel every U^j D U^(j)^T is complex symmetric, so its hidden
# subspace consists of complex symmetric matrices.
# For any complex symmetric z,w, w* = conjugate(w) is symmetric,
# and every diagonal entry of [z,w*] is zero.
# On the real generators, explicitly audit all diagonal-seed
# first hidden response pairs (their conjugate transpose = themselves).
symmetric_hidden=[]
for g in (K01,K02,K03,K12,K13,K23):
    for b in range(n):
        h=bracket(g,dmat([Q(i==b) for i in range(n)]))
        assert symmetric(h)
        assert all(h[i][i]==0 for i in range(n))
        symmetric_hidden.append(h)
assert all(bracket(x,y)[i][i]==0 for x in symmetric_hidden
           for y in symmetric_hidden for i in range(n))
# Thus P3's original quadratic residue is ZERO for this real-
# orthogonal conjugation family, despite nonzero Lie bracket,
# nonzero commutator holonomy, and nonzero P6 population return.

DEG=5
def poly_mul(a,b):
    c=[zero() for _ in range(DEG+1)]
    for i in range(DEG+1):
        for j in range(DEG+1-i): c[i+j]=add(c[i+j],mul(a[i],b[j]))
    return c
def exp_series(a,s):
    out=[]; power=ident()
    for k in range(DEG+1):
        out.append(scale(power,Q(s**k,factorial(k))))
        power=mul(power,a)
    return out
def poly_transpose(a): return [transpose(v) for v in a]
def emb(a):return [a]+[zero() for _ in range(DEG)]
loop=exp_series(K01,1)
for factor in (exp_series(K12,1),exp_series(K01,-1),
               exp_series(K12,-1)):
    loop=poly_mul(loop,factor)
assert loop[0]==ident() and loop[1]==zero() and loop[2]==K02
output=poly_mul(poly_mul(loop,emb(D)),poly_transpose(loop))
assert output[1]==zero()
assert output[2][0][2]==-1 and output[2][2][0]==-1
assert all(output[2][i][i]==0 for i in range(n))
assert all(output[3][i][i]==0 for i in range(n))
assert [output[4][i][i] for i in range(n)]==[Q(-1),q0,Q(1),q0]
# Coherence starts at order 2 and population at order 4.
assert all(output[k][i][i]==0 for k in (1,2,3)
           for i in range(n))
# CPTP holds at all epsilon because each exact factor exp(eps*K)
# is real orthogonal (K^T=-K); the truncated series is used only
# to certify the first nonvanishing response orders.

# H23 soldering: a necessary closed-loop condition is conjugacy
# of internal U_hol and physical LC holonomy P_hol. Choosing identity
# internal transport and a nontrivial geometric rotation refutes
# an unconditional identification.
R90=[[Q(0),Q(-1),Q(0)],[Q(1),Q(0),Q(0)],[Q(0),Q(0),Q(1)]]
I3=[[Q(i==j) for j in range(3)] for i in range(3)]
assert R90!=I3
assert sum(R90[i][i] for i in range(3))==Q(1)
assert sum(I3[i][i] for i in range(3))==Q(3)
# Gauge conjugation preserves trace. Without soldering and an
# independent geometric transport, internal nonzero holonomy
# alone cannot determine LC/Regge curvature.

print("PASS H21: self-dual ideal vs nonideal spatial-block kernel")
print("PASS H21: ideal population silence still permits quadratic return")
print("PASS H21: P3 diagonal commutator residue vanishes for orthogonal orbit")
print("PASS H22: exact CPTP group-loop leading K02 holonomy at degree two")
print("PASS H22: coherence O(eps^2), population O(eps^4)")
print("PASS H23: noncanonical soldering; closed-loop trace obstruction")
print("Scope: declared finite K4 controls; actual P6 admissibility unproved")
