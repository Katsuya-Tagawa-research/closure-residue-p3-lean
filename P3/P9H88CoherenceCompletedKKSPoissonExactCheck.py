"""H88 exact KKS Poisson completion: local 12-response vs global 15-observable.

Uses the independently assumed U4 coadjoint comparator and the previously
audited H87 exact Gaussian-rational engine. All physically available
coherence-phase instruments remain EXTERNAL access conditions, not original
H75/P3 source consequences.
"""
from fractions import Fraction as F
from itertools import permutations,combinations
from math import factorial

from P9H87KKSADMPoissonNonclosureDeWittExactCheck import (
    C,gc,I,O,Z0,n,edges,lam,star,xs,ys,
    zz,eye,E,plus,scale,minus,mm,dag,com,tr,X,Y,
    pb,read,diag,unitary_t
)

assert n==4 and len(edges)==6 and len(xs+ys)==12

def rank(rows):
    A=[[F(v) for v in row] for row in rows]
    m=len(A);ncol=len(A[0]);i=0
    for j in range(ncol):
        k=next((k for k in range(i,m) if A[k][j]),None)
        if k is None:continue
        A[i],A[k]=A[k],A[i]
        f=A[i][j]
        A[i]=[v/f for v in A[i]]
        for k in range(m):
            if k!=i and A[k][j]:
                c=A[k][j]
                A[k]=[v-c*w for v,w in zip(A[k],A[i])]
        i+=1
        if i==m:break
    return i

B12=xs+ys
P12=[[pb(star,a,b).r for b in B12] for a in B12]
assert rank(P12)==12
assert all(pb(star,xs[k],ys[l]) == gc(
           2*(lam[edges[k][0]]-lam[edges[k][1]])*int(k==l))
           for k in range(6) for l in range(6))
assert all(pb(star,xs[k],xs[l])==Z0 and
           pb(star,ys[k],ys[l])==Z0
           for k in range(6) for l in range(6))
print("PASS H88.1: exact 12x12 KKS Poisson rank12 / six nonzero root-plane pairs; local full-response coordinates")

# The spectral Casimir Jacobian wrt all four real diagonal entries:
# V_ka=k lambda_a^(k-1), k=1..4. Its determinant is
# 24 times the ordinary Vandermonde determinant.
def determinant(M):
    m=len(M)
    return sum((F((-1)**sum(p[i]>p[j] for i in range(m)
                    for j in range(i+1,m)))*
                __import__('math').prod(M[i][p[i]] for i in range(m))
                for p in permutations(range(m))),F(0))

V=[[F(k)*lam[a]**(k-1) for a in range(4)]
   for k in range(1,5)]
vand=F(factorial(4))*__import__('math').prod(
    (lam[b]-lam[a] for a,b in combinations(range(4),2)))
assert determinant(V)==vand==F(9,31250)
assert rank(V)==4
print("PASS H88.2: exact spectral-Casimir diagonal reconstruction Jacobian det 9/31250")

# Generic Hermitian offdiag coherence C^(1). Compute the analytic
# inverse's quadratic diagonal coefficient
# u_a = - sum_{b!=a} |C_ab|^2 / (lambda_a-lambda_b).
off=zz()
for a,b in edges:
    z=C(F(a+1,17*(b+1)), F(b+1,31*(a+2)))
    off[a][b]=z
    off[b][a]=z.conj()
assert dag(off)==off and all(off[i][i]==Z0 for i in range(n))
def abs2(z):
    return z.r*z.r+z.i*z.i
qshift=[]
for a in range(n):
    val=-sum((abs2(off[a][b])/(lam[a]-lam[b])
              for b in range(n) if b!=a),F(0))
    qshift.append(val)
assert sum(qshift)==0

def polynomial_mul(A,B):
    out=[zz(),zz(),zz()]
    for k in range(3):
        for j in range(k+1):
            out[k]=plus(out[k],mm(A[j],B[k-j]))
    return out

rho_series=[star,off,diag(qshift)]
power=[eye(),zz(),zz()]
for k in range(1,5):
    power=polynomial_mul(power,rho_series)
    assert tr(power[0])==gc(sum((x**k for x in lam),F(0)))
    assert tr(power[1])==Z0,(k,tr(power[1]))
    assert tr(power[2])==Z0,(k,tr(power[2]))
print("PASS H88.2: generic Gaussian-rational offdiag perturbation with analytic quadratic population repair preserves ALL FOUR spectral Casimirs through degree 2")

# Globally, rho* and the physical permutation-conjugate state belong to
# one orbit and have the exact same 12 offdiag x/y outcomes =0, while
# the bracket {x01,y01}=2(d0-d1) has opposite signs.
swap=diag((lam[1],lam[0],lam[2],lam[3]))
assert all(read(star,A)==Z0 and read(swap,A)==Z0 for A in B12)
assert pb(star,xs[0],ys[0])==gc(F(1,5))
assert pb(swap,xs[0],ys[0])==gc(-F(1,5))
for p in permutations(range(4)):
    rho=diag(tuple(lam[p[i]] for i in range(n)))
    assert all(read(rho,A)==Z0 for A in B12)
print("PASS H88.3: 24 legitimate diagonal states on SAME U4 orbit have identical twelve response records, not global Poisson-projectable")

Zdiag=[minus(E(a,a),E(3,3)) for a in range(3)]
basis=xs+ys+Zdiag
assert len(basis)==15
assert all(dag(A)==A and tr(A)==Z0 for A in basis)

def reconstruct_traceless(H):
    """Recover any Hermitian traceless 4x4 matrix in the full 15 basis."""
    assert dag(H)==H and tr(H)==Z0
    out=zz()
    for k,(a,b) in enumerate(edges):
        coeffx=F(H[a][b].r)
        coeffy=-F(H[a][b].i)
        out=plus(out,scale(xs[k],coeffx))
        out=plus(out,scale(ys[k],coeffy))
    for a in range(3):
        out=plus(out,scale(Zdiag[a],H[a][a].r))
    return out

for A in basis:
    assert reconstruct_traceless(A)==A
for A in basis:
    for B in basis:
        K=scale(com(A,B),-I)
        assert reconstruct_traceless(K)==K
assert scale(com(xs[0],ys[0]),-I)==scale(minus(E(0,0),E(1,1)),2)
assert pb(star,xs[0],ys[0])==gc(F(1,5))
print("PASS H88.4: all 225 pair brackets of the 15 traceless Hermitian su4-observable basis close exactly by real linear combinations")

# Valid positive effects Q_+=(I+A)/2 for X_ab/Y_ab, A has spectrum
# -1,+1,0,0 (verified exactly by A^3=A, A^2=P_a+P_b).
for k,(a,b) in enumerate(edges):
    for A in (xs[k],ys[k]):
        assert mm(mm(A,A),A)==A
        assert mm(A,A)==plus(E(a,a),E(b,b))
        assert dag(A)==A
        Q=scale(plus(eye(),A),F(1,2))
        assert dag(Q)==Q
        assert tr(Q)==gc(2)
# Positive population projectors E_aa are separately available
# instruments ONLY BY CONDITIONAL ACCESS ASSUMPTION.
for a in range(3):
    Q=E(a,a)
    assert mm(Q,Q)==Q and dag(Q)==Q

def reconstruct_density(rho):
    xs_vals=[read(rho,A).r for A in xs]
    ys_vals=[read(rho,A).r for A in ys]
    ds=[rho[i][i].r for i in range(3)]
    ds.append(F(1)-sum(ds))
    reconstructed=diag(ds)
    for (a,b),x,y in zip(edges,xs_vals,ys_vals):
        reconstructed[a][b]=C(x/F(2),-y/F(2))
        reconstructed[b][a]=reconstructed[a][b].conj()
    return reconstructed

U,_,_=unitary_t(F(1,2))
turned=mm(mm(U,star),dag(U))
mix=scale(plus(turned,swap),F(1,2))
for rho in (star,swap,turned,mix):
    assert tr(rho)==O and dag(rho)==rho
    assert reconstruct_density(rho)==rho
    for A in xs+ys:
        x=read(rho,A)
        assert x.i==0 and -1<=x.r<=1
        assert 0<=F(1,2)*(1+x.r)<=1
    for a in range(3):
        assert 0<=rho[a][a].r<=1
print("PASS H88.4: 12 positive coherence-POVM effects plus 3 positive population effects give exact GLOBAL 4-level trace-one state tomography")
print("BOUNDARY: 12 local Poisson-complete nonlinear coordinates DO NOT form an open-region Darboux chart without further corrections")
print("BOUNDARY: 15 global linear Lie–Poisson closure is not a global exact ADM cotangent symplectomorphism")
print("BOUNDARY: additional coherent measurement access is independent AX-OA; source-KKS/ADM map, DeWitt selection, off-shell HDA, Einstein dynamics and F completeness OPEN")
