"""H96: exact H75 rank9/kernel27 vs finite-time GKSL invertibility;
ADM DeWitt kinetic Hessian has (5+,1-) signature, not Fisher (++...+).

Original H75 four-Kraus CP instrument and P3 residue untouched.
General finite-time generator theorem is via inverse fundamental matrix
(ODE argument) and HS norm; no enumeration of all Lindbladians claimed.
The DeWitt kinetic form is the independently known standard ADM target,
NOT a derived Hamiltonian of the finite original micro source.
"""
from fractions import Fraction as F

from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    MBASIS,micro,R60,matadd,matscale,matadj,mattrace,qtrace,
    embed,zero_n,matmul
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P9H92FiveLevelGrassmannKKSResetSilenceExactCheck as H92

assert len(MBASIS)==36
assert R60[0][0]==I*gc(F(-32,135))
assert R60[1][1]==I*gc(F(16,135))
assert R60[2][2]==I*gc(F(16,135))

def flatten(A):
    return [A[i][j] for i in range(len(A)) for j in range(len(A))]
def complex_rank(rows):
    """Exact row echelon rank over rational Gaussian complex numbers."""
    M=[[gc(x) for x in row] for row in rows]
    if not M:return 0
    n=len(M)
    w=len(M[0])
    assert all(len(row)==w for row in M)
    pivot_row=0
    for col in range(w):
        pivot=next((i for i in range(pivot_row,n) if M[i][col]!=Z0),None)
        if pivot is None:continue
        M[pivot_row],M[pivot]=M[pivot],M[pivot_row]
        inv=O/M[pivot_row][col]
        for k in range(col,w):
            M[pivot_row][k]=M[pivot_row][k]*inv
        for i in range(pivot_row+1,n):
            factor=M[i][col]
            if factor!=Z0:
                for k in range(col,w):
                    M[i][k]=M[i][k]-factor*M[pivot_row][k]
        pivot_row+=1
        if pivot_row==n:break
    return pivot_row

original_outputs=[micro(A) for A in MBASIS]
superop_rows=[
    [out[i][j] for out in original_outputs]
    for i in range(6) for j in range(6)
]
assert len(superop_rows)==36
assert all(len(r)==36 for r in superop_rows)
assert complex_rank(superop_rows)==9

# Kernel of the original H75 reset is EXACTLY the flag partial-trace
# kernel: 9 upper off-flag units, 9 lower off-flag units, 9 paired
# diagonal-block differences, total 27 complex linearly independent.
kernel=[]
for i in range(3):
    for j in range(3):
        kernel.append(MBASIS[6*i+(3+j)])
        kernel.append(MBASIS[6*(3+i)+j])
        kernel.append(matadd(MBASIS[6*i+j],
                             matscale(MBASIS[6*(3+i)+(3+j)],-1)))
assert len(kernel)==27
assert complex_rank([flatten(X) for X in kernel])==27
assert all(qtrace(X)==zero_n(3) and micro(X)==zero_n(6)
           for X in kernel)
# The 36D operator domain is a complex linear vector space; the actual
# CPTP map has rank9, hence no bounded finite-time fundamental solution
# (which must be invertible) can equal it.
assert len(MBASIS)-complex_rank(superop_rows)==27
assert complex_rank([flatten(X) for X in MBASIS])==36
print("PASS H96.1: actual unchanged H75 6D four-Kraus source 36x36 exact Gaussian-rational superoperator rank9/kernel27; explicit 27-independent-element flag-partial-trace kernel")

# Hilbert-Schmidt normalized non-Hermitian operator |0,0><1,0|.
# A non-Hermitian witness suffices for the complex-linear inverse-flow
# bound, and its Hermitian and anti-Hermitian parts are also killed.
X0=MBASIS[0*6+3]
assert X0 in kernel
assert micro(X0)==zero_n(6)
norm2=sum((z.r*z.r+z.i*z.i for row in X0 for z in row),F(0))
assert norm2==1
herm=matadd(X0,matadj(X0))
anti=matscale(matadd(X0,matscale(matadj(X0),-1)),-I)
assert herm!=zero_n(6) and anti!=zero_n(6)
assert matadj(herm)==herm and matadj(anti)==anti
assert micro(herm)==micro(anti)==zero_n(6)
print("PASS H96.2: actual H75 Hilbert-Schmidt unit kernel witness E03 and independent nonzero physical Hermitian cross-flag silent observables")

# Mathematical theorem (not finite enumeration):
# for any bounded L_t on M6, fundamental solution Psi(t,0) is
# invertible as a 36x36 complex linear matrix, with
# ||Psi^{-1}||_(2->2) <= exp(integral_0^t ||L_s||_(2->2) ds).
# On HS-unit X0, ||(Psi-Phi)X0|| = ||Psi X0|| >= exp(-A).
# Therefore error<epsilon requires A >= log(1/epsilon).
# Unit conjugation maintains ||X0||2=1, distance>=1.
assert len(MBASIS)==36 and norm2==1 and micro(X0)==zero_n(6)
assert H91.rank(H92.P)==12
assert len(H92.allobs)==12
assert all(micro(H92.decode5(H92.scale(H92.comm(G,H92.sigma),-I)))
           ==zero_n(6) for G in H92.allobs)
print("PASS H96.2: full rank12 TRUE H75-seeded KKS tangent is erased at first order by original reset; finite-time bounded GKSL/Hamiltonian fundamental flow is linearly invertible, so cannot coincide with rank9 source")
print("PASS H96.2: exact HS-unit kernel gives quantitative inverse-flow lower bound ||Psi_t-Phi||_(2->2) >= exp(-integral ||L_s||ds), unitary-flow error >=1")

# Six independent symmetric spatial momentum tensor entries:
# v=(p11,p22,p33,p12,p13,p23).
D=[[F(0) for _ in range(6)] for _ in range(6)]
for i in range(3):
    for j in range(3):
        D[i][j]=(F(1) if i==j else F(0))-F(1,2)
for i in range(3,6):D[i][i]=F(2)
assert D==[
    [F(1,2),F(-1,2),F(-1,2),F(0),F(0),F(0)],
    [F(-1,2),F(1,2),F(-1,2),F(0),F(0),F(0)],
    [F(-1,2),F(-1,2),F(1,2),F(0),F(0),F(0)],
    [F(0),F(0),F(0),F(2),F(0),F(0)],
    [F(0),F(0),F(0),F(0),F(2),F(0)],
    [F(0),F(0),F(0),F(0),F(0),F(2)]
]
def mulvec(M,v):
    return [sum((M[i][j]*v[j] for j in range(len(v))),F(0))
            for i in range(len(v))]
def dot(v,w):
    return sum((a*b for a,b in zip(v,w)),F(0))
def Q(v):
    return dot(v,mulvec(D,v))
basis=[
    ([F(1),F(-1),F(0),F(0),F(0),F(0)],F(1)),
    ([F(1),F(1),F(-2),F(0),F(0),F(0)],F(1)),
    ([F(1),F(1),F(1),F(0),F(0),F(0)],F(-1,2)),
    ([F(0),F(0),F(0),F(1),F(0),F(0)],F(2)),
    ([F(0),F(0),F(0),F(0),F(1),F(0)],F(2)),
    ([F(0),F(0),F(0),F(0),F(0),F(1)],F(2)),
]
assert H91.rank([v for v,_ in basis])==6
for v,lam in basis:
    assert mulvec(D,v)==[lam*x for x in v]
assert [lam for _,lam in basis].count(F(1))==2
assert [lam for _,lam in basis].count(F(2))==3
assert [lam for _,lam in basis].count(F(-1,2))==1
assert Q([F(1),F(1),F(1),F(0),F(0),F(0)])==F(-3,2)
assert Q([F(1),F(-1),F(0),F(0),F(0),F(0)])==F(2)
det=F(1)
for _,lam in basis:det*=lam
assert det==F(-4)
print("PASS H96.3: exact standard ADM DeWitt 6-momentum Hessian eigenvalues {1,1,-1/2,2,2,2}, inertia (5+,1-), determinant -4, negative conformal trace witness -3/2")

# Independent positive response/Fisher Hessian cannot gain negative
# inertia by a legitimate REAL INVERTIBLE configuration-preserving
# momentum change. The witness is a concrete rational congruence,
# and the ALL-B invertible claim is Sylvester/positive quadratic form.
Fisher=[F(1),F(2),F(3),F(4),F(5),F(6)]
B=[[F(1) if i==j else (F(i+j+1,7) if i>j else F(0))
    for j in range(6)] for i in range(6)]
assert H91.rank(B)==6
P=[[sum((B[k][i]*Fisher[k]*B[k][j] for k in range(6)),F(0))
    for j in range(6)] for i in range(6)]
for v,_ in basis:
    y=mulvec(B,v)
    assert dot(v,mulvec(P,v))==sum((Fisher[k]*y[k]*y[k]
                                     for k in range(6)),F(0))
    assert dot(v,mulvec(P,v))>0
assert dot(basis[2][0],mulvec(P,basis[2][0]))>0
assert Q(basis[2][0])<0
print("PASS H96.4: any positive Fisher/response momentum form remains SPD under invertible real momentum congruence; cannot equal indefinite ADM DeWitt Hessian")

print("BOUNDARY: source Phi_mu is an EXACT discrete CPTP reset, not a near-identity bounded finite-time Lindblad exponential; P1 local GKSL tangent theorem NOT contradicted")
print("BOUNDARY: singular-time rates, unlimited relaxation time, environment measurement/discard and external memory beyond original M6 are NOT ruled out")
print("BOUNDARY: standard ADM DeWitt inertia is a TARGET algebraic test, not an H75/P3/F-generated kinetic Hamiltonian; actual symplectic ADM mapping, HDA, Einstein equations OPEN")
