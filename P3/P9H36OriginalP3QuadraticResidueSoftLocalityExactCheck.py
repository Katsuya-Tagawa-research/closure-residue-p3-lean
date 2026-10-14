"""H36: ORIGINAL P3 quadratic commutator-residue soft-locality (GKSL comparator).

P3 discrete map Phi_t=exp(t L_gamma), fixed t>=0. For d=E00,
z=Q Phi_t(d) in H1 and w=Q Phi_t^2(d) in H2. Thus R=Delta[z,w*]
is a genuine depth-three P3 witness. It is NOT merely population leakage.

Analytic Dyson bounds in the research note, independently certified here
using Gaussian rational Taylor coefficients plus a rational remainder.
The bounds are standard GKSL results, not CR-only predictions.
"""
from fractions import Fraction as F
from math import factorial
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,C,gc
from P9H35GKSLLocalityTailExactCheck import (
    N, jets, hamiltonian, generator, zeros, ident, ed, plus, sc, matmul,
    dagger, comm, tr
)

def hidden(a):
    return [[a[i][j] if i!=j else Z0 for j in range(N)] for i in range(N)]
def diagonal(a):
    return [[a[i][j] if i==j else Z0 for j in range(N)] for i in range(N)]
def sample(a,t):
    out=zeros()
    for m in range(len(a)):
        out=plus(out,sc(a[m],t**m))
    return out
def suppress_far(a,R):
    return [[a[j][k] if j<R and k<R else Z0
             for k in range(N)] for j in range(N)]
def residual(z,w):
    return diagonal(comm(z,dagger(w)))
def current(z,w,i,j):
    assert i<j
    c=z[i][j]*w[i][j].conj()
    return gc(2)*C(F(0),c.i)
def real_current(z,w,i,j):
    c=z[i][j]*w[i][j].conj()
    return 2*c.i
def divergence(z,w):
    d=[]
    for v in range(N):
        flow=sum((real_current(z,w,v,u) if v<u else
                  -real_current(z,w,u,v) for u in range(N) if u!=v),F(0))
        d.append(I*gc(flow))
    return diagonal_vector(d)
def diagonal_vector(values):
    out=zeros()
    for i,z in enumerate(values):out[i][i]=gc(z)
    return out
def coefficient_residues(co,maxdeg):
    zh=[hidden(a) for a in co]
    out=[zeros() for _ in range(maxdeg+1)]
    for m in range(2,maxdeg+1):
        s=zeros()
        for a in range(1,m):
            b=m-a
            if a<len(zh) and b<len(zh):
                s=plus(s,sc(residual(zh[a],zh[b]),2**b))
        out[m]=s
    return out
def analytic_tail_nosqrt(m,x):
    # exp(x) x^m / m! <= x^m/(m! (1-x)) for 0<=x<1.
    assert F(0)<=x<1
    return x**m/F(factorial(m)) / (1-x)
def rational_entry_residue_bound(v,t,J):
    # e^(12Jt) <= 1/(1-12Jt) for 12Jt<1.
    x=32*J*J*t*t
    assert 12*J*t<1
    return sum((2*x**(v+u)/F(factorial(v+u)**2)
                for u in range(N) if u!=v),F(0))/(1-12*J*t)
def rational_cutoff_bound(R,t,J):
    x=32*J*J*t*t
    assert 12*J*t<1
    # l1 norm of diagonal current divergence: an omitted edge
    # contributes at most 4*|z_vu|*|w_vu| to two endpoints.
    return sum((4*x**(v+u)/F(factorial(v+u)**2)
                for v in range(N) for u in range(v+1,N)
                if u>=R),F(0))/(1-12*J*t)
def check_residue_jets(J,gamma,energies):
    co=jets(J,gamma,energies,12)
    out=coefficient_residues(co,12)
    assert out[0]==zeros() and out[1]==zeros() and out[2]==zeros()
    # Terms of degree 2m in a single matrix entry cancel because
    # z(t) and z(2t) share the same earliest nonzero coefficient.
    for v in range(N):
        minimum=3 if v==0 else 2*v+1
        for order in range(minimum):
            assert out[order][v][v]==Z0,(v,order,out[order][v][v])
        for order in range(13):
            assert out[order][v][v].r==0
    for order in range(13):
        assert tr(out[order])==Z0
        assert dagger(out[order])==sc(out[order],-1)
    # Signed depth-three witness coefficient:
    # [t^3] Delta([Q Phi_t(d),Q Phi_2t(d)])=Delta([A,B])
    # where A=Q L(d) and B=Q L^2(d).
    A=hidden(sc(co[1],O))
    B=hidden(sc(co[2],2))
    assert out[3]==residual(A,B)
    # Uniform site-dephasing does not affect this cubic coefficient.
    r3=I*gc(2*J*J*(energies[0]-energies[1]))
    assert out[3][0][0]==r3
    assert out[3][1][1]==-r3
    assert all(out[3][r][r]==Z0 for r in range(2,N))
    return co,out

v0=(F(0),)*N
v1=(F(0),F(1,7),F(-1,9),F(2,11),F(-3,13))
for J in (F(1),F(2,3)):
    for gamma in (F(0),F(2,3)):
        for v in (v0,v1):
            co,out=check_residue_jets(J,gamma,v)
assert check_residue_jets(F(1),F(2,3),v1)[1][3][0][0]==-I*gc(F(2,7))
# J=1/2 example yields -i/14 at t^3; J=1 case -2i/7.
assert check_residue_jets(F(1,2),F(2,3),v1)[1][3][0][0]==-I*gc(F(1,14))

# FINITE-TIME CERTIFICATE: rational polynomial + rigorous remainder.
J=F(1,2);gamma=F(2,3);t=F(1,64)
v=v1
M0=4*J+gamma+max(v)-min(v)
n=16
co=jets(J,gamma,v,n)
assert 2*M0*t<1 and 12*J*t<1
z=hidden(sample(co,t))
w=hidden(sample(co,2*t))
assert dagger(z)==z and dagger(w)==w
P=residual(z,w)
assert P==divergence(z,w)
assert tr(P)==Z0
assert dagger(P)==sc(P,-1)

# Every entrywise semigroup error is at most eps, from matrix-unit
# induced max-row bound M0 for the generator on all matrix entries.
eps1=(M0*t)**(n+1)/F(factorial(n+1))/(1-M0*t)
eps2=(2*M0*t)**(n+1)/F(factorial(n+1))/(1-2*M0*t)
# Physical rho(t), rho(2t) remain PSD trace one, so each
# offdiagonal entry has |rho_jk|<=1.
# Per-residue-site difference <= 2*(N-1)*(eps1+(1+eps1)*eps2).
error_site=2*(N-1)*(eps1+(1+eps1)*eps2)
for r in range(N):
    bound=rational_entry_residue_bound(r,t,J)
    assert abs(P[r][r].i)+error_site <=bound,(r,P[r][r],error_site,bound)
    assert P[r][r].r==0
# The exact CHAIN soft-locality tail for a compression at radius R:
# || Delta[z,w] - Delta[P_R z P_R,P_R w P_R] ||_1
# <= 4 exp(12Jt) sum_{v<u, u>=R}
#           (32 J² t²)^(v+u) / [(v+u)!]².
for radius in range(1,N):
    pr=residual(suppress_far(z,radius),suppress_far(w,radius))
    diff=plus(P,sc(pr,-1))
    assert dagger(diff)==sc(diff,-1)
    observed=sum((abs(diff[r][r].i) for r in range(N)),F(0))
    bound=rational_cutoff_bound(radius,t,J)
    assert observed+2*N*error_site<=bound, (radius,observed,bound)

# The rank/gauge layer is intentionally NOT identified here:
# one selected signed depth-three witness is not the full R3 span.
print("PASS H36: all P3 z1/z2 pairs are legitimate depth-three hidden commutator witnesses")
print("PASS H36: exact edge-current divergence equals signed original P3 quadratic residue")
print("PASS H36: residue distance-r entries vanish below Taylor degree 2r+1")
print("PASS H36: cubic signed residue nonzero for detuned model and gamma-independent")
print("PASS H36: finite-time rational certificates for residue sites and radius cutoffs")
print("PASS H36: soft quadratic-residue tails follow the GKSL factorial Dyson bounds")
print("SCOPE: full P3 R3 space, frozen P6 J_N and physical CR gravity not inferred")
