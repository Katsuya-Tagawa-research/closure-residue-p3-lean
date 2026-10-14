"""H35 exact nearest-neighbor GKSL soft-locality and leakage audit.

One-ended finite 5-site path, initial |0><0|, real hopping J, arbitrary
site energies v_j, uniform calibrated site dephasing gamma>=0.

For rho_jk(t), exact first nonzero Taylor coefficient has degree j+k
and coefficient (-i J)^j (i J)^k/(j! k!) independent of v and gamma.
Dyson-path estimate |rho_jk(t)| <= sum_{m>=j+k}(4Jt)^m/m!
for J>=0, gamma>=0; no hard finite support cone for any distance.

Finite Fraction tests and a rational certified sample do NOT replace
the all-time bound's analytic Dyson/graph-path proof in the companion note.
"""
from fractions import Fraction as F
from math import factorial
from P9H24PhaseSensitiveResidueGaugeExactCheck import C, gc, I, O, Z0

N=5
def zeros():return [[Z0 for _ in range(N)] for _ in range(N)]
def ident():return [[O if i==j else Z0 for j in range(N)] for i in range(N)]
def ed(i,j):
    m=zeros();m[i][j]=O;return m
def plus(a,b):return [[a[i][j]+b[i][j] for j in range(N)] for i in range(N)]
def sc(a,s):return [[a[i][j]*s for j in range(N)] for i in range(N)]
def matmul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(N)),Z0)
             for j in range(N)] for i in range(N)]
def dagger(a):return [[a[j][i].conj() for j in range(N)] for i in range(N)]
def comm(a,b):return plus(matmul(a,b),sc(matmul(b,a),-1))
def tr(a):return sum((a[i][i] for i in range(N)),Z0)
def scalar_pow(a,n):
    out=O
    for _ in range(n):out=out*a
    return out
def hamiltonian(J,energies):
    h=zeros()
    for i in range(N):h[i][i]=gc(energies[i])
    for i in range(N-1):
        h[i][i+1]=gc(J)
        h[i+1][i]=gc(J)
    assert dagger(h)==h
    return h
def generator(a,H,gamma):
    out=sc(comm(H,a),-I)
    for j in range(N):
        for k in range(N):
            if j!=k:out[j][k]=out[j][k]-gc(gamma)*a[j][k]
    return out
def jets(J,gamma,v,maxdeg):
    H=hamiltonian(J,v)
    co=[ed(0,0)]
    for m in range(1,maxdeg+1):
        co.append(sc(generator(co[-1],H,gamma),F(1,m)))
    assert co[0]==ed(0,0)
    for m,A in enumerate(co):
        assert dagger(A)==A
        assert tr(A)==(O if m==0 else Z0)
    return co

v0=(F(0),)*N
v1=(F(0),F(1,7),F(-1,9),F(2,11),F(-3,13))
configs=[(J,gamma,v) for J in (F(1),F(2,3))
         for gamma in (F(0),F(2,3),F(5,4))
         for v in (v0,v1)]
for J,gamma,v in configs:
    co=jets(J,gamma,v,2*(N-1)+2)
    for j in range(N):
        for k in range(N):
            distance=j+k
            assert all(co[m][j][k]==Z0 for m in range(distance)), (J,gamma,v,j,k)
            target=scalar_pow(-I,j)*scalar_pow(I,k)*gc(
                J**distance/F(factorial(j)*factorial(k)))
            assert co[distance][j][k]==target, (j,k,co[distance][j][k],target)
    for r in range(1,N):
        leading=J**(2*r)/F(factorial(r)**2)
        assert co[2*r][r][r]==gc(leading)
        assert leading>0
        assert co[2*r-1][r][r]==Z0
    # The first-coefficient identity doesn't depend on the diagonal
    # potential or the site-dephasing rate; later coefficients can.
    assert co[1][0][1]==I*gc(J)
    assert co[2][1][1]==gc(J*J)

co_clean=jets(F(1),F(0),v0,10)
co_noise=jets(F(1),F(2,3),v1,10)
assert co_clean[3][1][1]!=co_noise[3][1][1]
assert co_clean[4][2][2]==co_noise[4][2][2]==gc(F(1,4))
assert co_clean[6][3][3]==co_noise[6][3][3]==gc(F(1,36))
assert co_clean[8][4][4]==co_noise[8][4][4]==gc(F(1,576))

# The Dyson series is in the offdiagonal "hopping" superoperator
# B, with diagonal field+dephasing D having factor |e^{sD_jk}|<=1.
# At each hop (j,k) changes one site index by +/-1, so each
# physical coefficient requires >=j+k hops from initial (0,0).
# With nearest-neighbor degree<=2, at most four transitions, each
# amplitude <=J, yielding uniform bound:
# |rho_jk(t)| <= sum_{m>=j+k} (4Jt)^m / m!
# <= (4Jt)^(j+k) e^(4Jt)/(j+k)! .
# This does NOT depend on gamma or site-energy differences.

# Produce a concrete completely RATIONAL rigorous bound on the full
# physical output rho(t), not merely its finite Taylor truncation.
# Entrywise generator ||L||_infty <= 4J+gamma+(vmax-vmin) =: M0.
# For t small with M0*t<1, the Taylor remainder after degree M is
# <= (M0*t)^(M+1)/((M+1)!*(1-M0*t)).
J=F(1,2);gamma=F(2,3);v=v1;t=F(1,16)
maxdeg=16
co=jets(J,gamma,v,maxdeg)
Ct=(4*J+gamma+max(v)-min(v))*t
x=4*J*t
assert F(0)<Ct<1 and F(0)<x<1
rem=Ct**(maxdeg+1)/F(factorial(maxdeg+1)) / (1-Ct)
for r in range(1,N):
    p_trunc=sum((co[m][r][r].r*t**m for m in range(maxdeg+1)),F(0))
    assert all(co[m][r][r].i==0 for m in range(maxdeg+1))
    bound=x**(2*r)/F(factorial(2*r))/(1-x)
    assert p_trunc>=-rem
    assert p_trunc+rem<=bound, (r,p_trunc,rem,bound)
    assert co[2*r][r][r].r>0
# Outgoing population leakage from root beyond radius R is bounded
# by summing the independent sitewise Dyson upper bounds:
for radius in range(1,N):
    leak_bound=sum(
        (x**(2*r)/F(factorial(2*r))/(1-x) for r in range(radius,N)),
        F(0))
    trunc=sum((co[m][r][r].r*t**m for m in range(maxdeg+1)
               for r in range(radius,N)),F(0))
    assert trunc+(N-radius)*rem<=leak_bound

print("PASS H35: 12 exact GKSL cases, coherence leading degree j+k for every path pair")
print("PASS H35: p_r(t) first nonzero degree 2r with coefficient J^(2r)/(r!)^2")
print("PASS H35: leading coefficients independent of calibrated gamma and diagonal energies")
print("PASS H35: dephasing/potentials alter later jets but not minimal propagation degree")
print("PASS H35: rational Taylor plus rigorous remainder below soft-locality Dyson bound")
print("PASS H35: finite-distance population leakage certified without hard support cone")
print("SCOPE: proof is standard path GKSL/Dyson, not CR-specific or gravity curvature")
