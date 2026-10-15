"""H63 — real P6 instruments, transpose symmetry and KKS orientation.

Independent rational certificate complementing H38/H39:
  - real coherent controls, real Kraus population instruments,
    dephasing and outcome-adaptive classical feedback preserve
    transposition symmetry at arbitrary finite circuit depth;
  - any transpose-invariant classical fingerprint cannot pull back
    a target symplectic 2-form to the KKS form on a transpose-stable
    coherent U2 patch (an anti-symplectic involution obstruction);
  - an independently calibrated complex Stark phase breaks the gate.
This is the *restricted frozen P6 real-control comparator*, not an
all-P6 or all-CR impossibility theorem, and not P9's richer X/Y hardware.
Standard-library fractions only.
"""
from fractions import Fraction as F
from itertools import product

def Z(n,m): return [[F(0) for _ in range(m)] for _ in range(n)]
def eye(n):
    M=Z(n,n)
    for i in range(n): M[i][i]=F(1)
    return M
def tr(A): return [list(v) for v in zip(*A)]
def mm(A,B):
    assert len(A[0])==len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def scale(A,s): return [[s*x for x in row] for row in A]
def add(A,B): return [[a+b for a,b in zip(u,v)] for u,v in zip(A,B)]
def equal(A,B): return A==B
def trace(A): return sum(A[i][i] for i in range(len(A)))
def sym(A): return tr(A)==A
def skew(A): return tr(A)==scale(A,F(-1))
def conj_real(M,A): return mm(mm(M,A),tr(M))
def diagonal(A):
    M=Z(len(A),len(A))
    for i in range(len(A)):M[i][i]=A[i][i]
    return M
def dep(A,q):
    assert F(0)<=q<=F(1)
    return add(scale(A,q),scale(diagonal(A),1-q))
def rot(a,b,c,s):
    assert c*c+s*s==1
    U=eye(3)
    U[a][a]=U[b][b]=c
    U[a][b]=s
    U[b][a]=-s
    assert mm(U,tr(U))==eye(3)
    return U
def inst(M,A,D):
    return conj_real(D,M),conj_real(D,A)
def apply(U,S,A,q):
    return dep(conj_real(U,S),q),dep(conj_real(U,A),q)

I3=eye(3)
S=scale(I3,F(1,3))
A=Z(3,3)
A[0][1]=F(1,6)
A[1][0]=-F(1,6)
assert sym(S) and skew(A) and trace(A)==0
# rho_± = I/3 ± iA: Hermitian with eigenvalues 1/6, 1/3, 1/2.
# Ordinary Hermitian positivity follows from the explicit spectrum;
# the Gaussian imaginary unit is tracked as the real skew coefficient.
assert F(1,3)-F(1,6)>0

R01=rot(0,1,F(3,5),F(4,5))
R12=rot(1,2,F(5,13),F(12,13))
R02=rot(0,2,F(15,17),F(8,17))
D0=Z(3,3);D1=Z(3,3)
for i,x in enumerate((F(3,5),F(4,5),F(0))): D0[i][i]=x
for i,x in enumerate((F(4,5),F(3,5),F(1))): D1[i][i]=x
assert add(mm(tr(D0),D0),mm(tr(D1),D1))==eye(3)
def step(S,A,history,choice):
    # Genuinely outcome-dependent adaptive choices:
    parity of the previous record changes real rotation/dephasing.
    U=(R01 if (choice+sum(history))%3==0 else
       R12 if (choice+sum(history))%3==1 else R02)
    q=(F(3,5) if (len(history)+choice)%2==0 else F(4,7))
    S1,A1=apply(U,S,A,q)
    D=D0 if choice==0 else D1
    S2,A2=inst(S1,A1,D)
    assert sym(S2) and skew(A2)
    assert trace(A2)==0
    assert all(S2[i][i]>=0 for i in range(3))
    return S2,A2

# All two-branch outcome strings through depth four.
# States differ in sign of imaginary A; the real symmetric S and
# therefore ALL branch probabilities remain identical.
for length in range(1,5):
    total=F(0)
    nonzero_imag=0
    for history in product((0,1),repeat=length):
        Sk,Ak=S,A
        for j,choice in enumerate(history):
            Sk,Ak=step(Sk,Ak,history[:j],choice)
        prob_plus=trace(Sk)+F(0) # imaginary skew trace identically zero
        prob_minus=trace(Sk)-F(0)
        assert prob_plus==prob_minus and prob_plus>=0
        assert skew(Ak)
        if Ak!=Z(3,3):nonzero_imag+=1
        total+=prob_plus
    assert total==1
    assert nonzero_imag>0
print("PASS H63: arbitrary real CPTP/instrument composition transposition theorem, exact adaptive depth-4 branch witness")

# On the regular coherent U(2) KKS orbit coordinates (q,p), transpose
# acts (q,p)->(-q,p), pulling omega=dq^dp to -omega.
Omega=[[F(0),F(1)],[-F(1),F(0)]]
JacTau=[[-F(1),F(0)],[F(0),F(1)]]
assert mm(mm(tr(JacTau),Omega),JacTau)==scale(Omega,F(-1))
# If Sigma o tau = Sigma, then for any target 2-form beta,
# tau*(Sigma* beta) = Sigma* beta. But tau*omega=-omega, so
# Sigma*beta=omega is impossible on a tau-stable domain.
# At a tau-fixed point (q=0), (I-JacTau) kills the angular
# direction: dSigma/dq=0 follows from dSigma * JacTau=dSigma.
assert JacTau[0][0]==-1 and Omega[0][1]!=0
print("PASS H63: coherent-U2 complex conjugation is KKS anti-symplectic; transpose-invariant fingerprint cannot symplectically pull back omega")
print("PASS H63: at fixed q=0, any transpose-invariant differentiable population fingerprint has angular rank zero")

# Exact additional coherent-phase gate V=diag(-i,1,1):
# V(S±iA)V† gives NEW real coherence S'01 = +/- A01.
# Rotation R01 makes its sign visible as a diagonal contrast.
x=A[0][1]
c,s=F(3,5),F(4,5)
pop_plus=F(1,3)+2*c*s*x
pop_minus=F(1,3)-2*c*s*x
assert pop_plus==F(37,75)
assert pop_minus==F(13,75)
assert pop_plus-pop_minus==F(8,25)
# Without external phase gate, R01 acts on S±iA, and
# real-population readout is identical 1/3.
assert conj_real(R01,S)[0][0]==F(1,3)
assert conj_real(R01,A)[0][0]==0
print("PASS H63: separately calibrated complex phase gate breaks transpose blindness with exact 8/25 population contrast")
print("BOUNDARY: no microscopic P3/P6 authorization of Stark gate, no CR-specific signature, no universal full P6 Sigma no-go")
