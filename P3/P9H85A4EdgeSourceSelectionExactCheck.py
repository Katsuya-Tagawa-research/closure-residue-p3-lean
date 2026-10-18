"""H85: exact A4 affine edge-classifier and conditional H75-source K4 metric selector.

No P3-only graph/edge Hamiltonian provenance is assumed. The four physical
cell labels, a relabeling A4 action, flag-readout response, an all-pairs K4
candidate and the normalization budget are independent physical/mathematical
data. Entirely Fraction-rational, no numerical tolerance or external package.
"""
from fractions import Fraction as F
from itertools import permutations, combinations

from P9H24PhaseSensitiveResidueGaugeExactCheck import I, Z0, gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    micro, embed, d0, d1, d2, matadd, matscale, mattrace, envblock, R60
)

assert R60[0][0] == I*gc(F(-32,135))
assert R60 != [[Z0]*6 for _ in range(6)]

def flag1(rho):
    output = micro(embed(rho))
    value = mattrace(envblock(output,1,1))
    assert value.i == 0 and F(0)<=value.r<=F(1)
    return value.r

rho3=matadd(matscale(d0,F(3,4)),matscale(d1,F(1,4)))
r=tuple(flag1(x) for x in (d0,d1,d2,rho3))
assert r==(F(0),F(16,25),F(16,25),F(4,25))
assert sum(r)==F(36,25)
print("PASS H85: four true physical positive flag-1 effects from unchanged six-level H75 micro are (0,16/25,16/25,4/25)")

edges=list(combinations(range(4),2))
eid={pair:k for k,pair in enumerate(edges)}
assert edges==[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def parity_even(p):
    return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2==0
A4=[p for p in permutations(range(4)) if parity_even(p)]
assert len(A4)==12

def row_rank(rows,ncols):
    """Incremental Fraction Gaussian reduction; works for rectangular rows."""
    pivots={}
    for rr in rows:
        a=[F(x) for x in rr]
        assert len(a)==ncols
        for lead,b in sorted(pivots.items()):
            if a[lead]:
                t=a[lead]
                a=[v-t*u for v,u in zip(a,b)]
        j=next((j for j,x in enumerate(a) if x),None)
        if j is not None:
            f=a[j]
            pivots[j]=[x/f for x in a]
    return len(pivots)

# Unknown affine map coefficients: 6 edge offsets + 6*4 vertex-input slopes.
# For each even permutation, every input coefficient and edge constant
# of T(P r) - P_E T(r) must vanish.
constraints=[]
for p in A4:
    for k,edge in enumerate(edges):
        out_idx=eid[tuple(sorted((p[edge[0]],p[edge[1]])))]
        for src in range(5):
            row=[0]*30
            if src==4:
                row[out_idx]+=1
                row[k]-=1
            else:
                row[6+4*out_idx+p[src]]+=1
                row[6+4*k+src]-=1
            if any(row):constraints.append(row)

assert len(constraints)==324,len(constraints)
assert row_rank(constraints,30)==27
print("PASS H85.1: exact 324 A4 affine-equivariance constraints have rank27 / nullity3")

W=F(27)
def affine(x,c,alpha,beta):
    total=sum(x)
    return tuple(c+alpha*(x[i]+x[j])+beta*(total-x[i]-x[j])
                 for i,j in edges)

def additive(x):
    assert sum(x)>0
    return affine(x,F(0),W/(3*sum(x)),F(0))

def complement(x):
    assert sum(x)>0
    return affine(x,F(0),F(0),W/(3*sum(x)))

def uniform(x):
    return tuple(W/6 for _ in edges)

def quadratic(x):
    raw=tuple((x[i]+x[j])**2 for i,j in edges)
    assert sum(raw)>0
    return tuple(W*v/sum(raw) for v in raw)

def permute_vertices(x,p):
    y=list(x)
    for i in range(4):y[p[i]]=x[i]
    return tuple(y)

def permute_edges(w,p):
    result=list(w)
    for i,(a,b) in enumerate(edges):
        result[eid[tuple(sorted((p[a],p[b])))]]=w[i]
    return tuple(result)

profiles=(r, (F(1),F(2),F(3),F(4)))
for x in profiles:
    for p in A4:
        for fun in (additive,complement,uniform,quadratic):
            assert fun(permute_vertices(x,p))==permute_edges(fun(x),p)
print("PASS H85.1: all twelve A4 cell relabelings respect all four exact candidate selectors")

wa=additive(r)
wc=complement(r)
wu=uniform(r)
wq=quadratic(r)
assert wa==(4,4,1,8,5,5)
assert wc==(5,5,8,1,4,4)
assert wu==(F(9,2),)*6
assert wq==(F(144,49),F(144,49),F(9,49),
            F(576,49),F(225,49),F(225,49))
assert len({wa,wc,wu,wq})==4
for w in (wa,wc,wu,wq):
    assert all(v>0 for v in w)
    assert sum(w)==W
print("PASS H85.2: strict-positive A4-equivariant normalized ADD/COMP/UNIFORM/QUADRATIC assignments differ for the SAME physical r")

# Affine A4 map classification: c=0, beta=0 fixed by zero-origin and
# strict endpoint-only dependence. Then for this fixed r the budget
# determines a unique coefficient alpha. A universal map with fixed alpha
# cannot have the fixed budget for every nonzero r, so the selector is
# globally nonlinear when the profile varies.
alpha=W/(3*sum(r))
assert alpha==F(25,4)
assert affine(r,F(0),alpha,F(0))==wa
assert sum(affine(r,F(0),F(1),F(0)))==3*sum(r)
print("PASS H85.2: under separately declared additive linear edge-locality and fixed-profile total budget, alpha=25/4 is unique")

# P9 K4 metric algebra: the 4x4 weighted Laplacian L_w has kernel span{1}
# and defines a positive inverse on S=1^perp. Nonorthonormal S basis
# B=(e0-e3,e1-e3,e2-e3). C=B^T L B, and L^+ = B C^-1 B^T.
def matmul(A,B):
    assert all(len(row)==len(B) for row in A)
    return [[sum((a*b for a,b in zip(row,col)),F(0))
              for col in zip(*B)] for row in A]

def transpose(A):
    return [list(row) for row in zip(*A)]

def inv(A):
    n=len(A)
    X=[[F(v) for v in row]+[F(int(i==j)) for j in range(n)]
       for i,row in enumerate(A)]
    for j in range(n):
        i=next((k for k in range(j,n) if X[k][j]),None)
        assert i is not None
        X[j],X[i]=X[i],X[j]
        d=X[j][j]
        X[j]=[x/d for x in X[j]]
        for k in range(n):
            if k!=j and X[k][j]:
                f=X[k][j]
                X[k]=[x-f*y for x,y in zip(X[k],X[j])]
    return [row[n:] for row in X]

B=[[F(int(i==j)-int(i==3)) for j in range(3)] for i in range(4)]
P=[[F(int(i==j))-F(1,4) for j in range(4)] for i in range(4)]

def Lmatrix(w):
    L=[[F(0) for _ in range(4)] for _ in range(4)]
    for z,(i,j) in zip(w,edges):
        L[i][i]+=z;L[j][j]+=z
        L[i][j]-=z;L[j][i]-=z
    return L

def k4metric(w):
    L=Lmatrix(w)
    assert all(sum(row)==0 for row in L)
    C=matmul(matmul(transpose(B),L),B)
    Ci=inv(C)
    Lplus=matmul(matmul(B,Ci),transpose(B))
    assert matmul(L,Lplus)==P
    assert matmul(Lplus,L)==P
    # Ambient representation of the positive metric on S.
    G=[[16*z for z in row] for row in Lplus]
    for k,(i,j) in enumerate(edges):
        # fixed-solder inverse metric: -16 <P e_i,g^-1 P e_j> = -L_ij
        assert -L[i][j]==w[k]
    return L,G

La,ga=k4metric(wa)
Lu,gu=k4metric(wu)
assert La!=Lu and ga!=gu
v=(F(1),F(-1),F(0),F(0))
def contraction(L,v):
    return sum((v[i]*L[i][j]*v[j] for i in range(4)
                for j in range(4)),F(0))/16
assert contraction(La,v)==F(17,8)
assert contraction(Lu,v)==F(9,4)
print("PASS H85.4: conditional positive K4 metrics differ; inverse-symbol contractions 17/8 vs 9/4, despite identical source readouts")
print("BOUNDARY: physical four-cell A4 controls, graph topology, additive ansatz, budget W, and solder are independent assumptions")
print("BOUNDARY: finite R3 !=0 does not generate an intercell Hamiltonian, ADM DeWitt kinetic term, off-shell HDA, Einstein equations or F-completeness")
