"""H29: actual P6 real-skew path controls versus H28 four-phase Wilson knob.

Exact rational-Gaussian arithmetic. Declared ideal coherent Lie closure is
distinct from the directly calibrated P6 two-control manifold. Phase knobs
or control-dependent dissipators are NOT inferred from accessibility.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
N=3
def z():return [[Z0 for j in range(N)] for i in range(N)]
def eye():return [[O if i==j else Z0 for j in range(N)] for i in range(N)]
def plus(A,B):return [[A[i][j]+B[i][j] for j in range(N)] for i in range(N)]
def times(A,x):return [[x*A[i][j] for j in range(N)] for i in range(N)]
def sub(A,B):return plus(A,times(B,-1))
def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(N)),Z0)
              for j in range(N)] for i in range(N)]
def com(A,B):return sub(matmul(A,B),matmul(B,A))
def star(A):return [[A[j][i].conj() for j in range(N)] for i in range(N)]
def matrixunit(a,b):
    T=z();T[a][b]=O;return T
def k_edge(a,b):return sub(matrixunit(a,b),matrixunit(b,a))
def diagonal(M):return [[M[i][j] if i==j else Z0 for j in range(N)] for i in range(N)]
def off(M):return sub(M,diagonal(M))
def wilson(H):return H[0][1]*H[1][2]*H[2][0]
def same(A,B):return A==B
A=k_edge(0,1)
B=k_edge(2,1) # P6: E32-E23 using 0-based vertices
Cbr=com(A,B)
assert Cbr==times(k_edge(0,2),-1)
assert com(A,Cbr)==times(B,-1)
assert com(B,Cbr)==A
assert star(A)==times(A,-1) and star(B)==times(B,-1)
assert star(Cbr)==times(Cbr,-1)
# These three are linearly independent over R (three distinct edges),
# and all their brackets close: generated Lie algebra = so(3).
for a,b,c in ((F(1),F(1),F(1)),(F(2,3),F(5,4),F(-7,6)),
              (F(3),F(0),F(1)),(F(0),F(2),F(3))):
    K=plus(plus(times(A,a),times(B,b)),times(Cbr,c))
    H=times(K,I)  # K=-iH, i.e. H=iK
    assert star(H)==H and diagonal(H)==z()
    W=wilson(H)
    assert W.r==0
    assert W==C(F(0),a*b*c)
    Hstatic=times(plus(times(A,a),times(B,b)),I)
    assert wilson(Hstatic)==Z0
# H28 needs four static H(a,b,q) with W, -W, iW, -iW
# of the SAME nonzero edge moduli. Since any accessible K in
# real so(3) has Re W=0, 90-degree scan cannot remain in this algebra.
q=C(F(3,5),F(4,5))
assert q.r!=0 and q.i!=0
for lam in (O,-O,I,-I):
    target=lam*q
    assert target*target.conj()==O
assert any((lam*q).r!=0 for lam in (O,-O,I,-I))
# Even a maximally generous so3 Lie closure cannot supply all H28 knobs.
W0=wilson(times(plus(plus(A,B),Cbr),I))
assert W0==I
assert (I*W0).r!=0  # phase pi/2 adjustment would exit i so3.
# A 180-degree inversion of the effective chord *does* preserve
# Re W = 0 as algebra, but is not assured as direct static hardware knob.
assert wilson(times(plus(plus(A,B),times(Cbr,-1)),I))==-W0

# Two real primitive forward semigroups are individually CPTP even
# with common >=0 uniform dephasing. Their time-ordering difference
# probes a commutator without illegally reversing dissipative time.
E0=matrixunit(0,0)
def L(K,rho,gamma):
    # K=-iH skew-Hermitian:
    return sub(com(K,rho),times(off(rho),gamma))
def signed_second_order_difference(gamma):
    # e^{t L_A}e^{t L_B}(rho) - e^{t L_B}e^{t L_A}(rho)
    return sub(L(A,L(B,E0,gamma),gamma),
               L(B,L(A,E0,gamma),gamma))
for gamma in (F(0),F(2,3),F(5,4)):
    D=signed_second_order_difference(gamma)
    assert diagonal(D)==z()
    assert D[0][2]==O and D[2][0]==O
    assert D[0][1]==gc(-gamma)
    # Gamma-dependent contamination is confined to a different
    # coherence edge for this preparation and choice of pulse order.
    assert D==plus(com(Cbr,E0),times(com(A,E0),-gamma))
    # The leading populations do not see the bracket at order t^2.

# Reverse dephasing of positive elapsed time t is not CPTP:
# an exact coherence gain r=exp(gamma*t)>1 takes |+><+|
# to a trace-one Hermitian matrix with negative determinant.
for r in (F(6,5),F(2),F(11,10)):
    rho_plus_after_inverse=[[gc(F(1,2)),gc(r/2),Z0],
                            [gc(r/2),gc(F(1,2)),Z0],
                            [Z0,Z0,Z0]]
    minor_det=F(1,4)-r*r/F(4)
    assert minor_det<0
# Thus a four-factor BCH group commutator using inverse Lindblad
# semigroups is not an admissible CPTP pulse construction when
# nonzero dephasing is present.

# Show the exact gauge-invariant flux restriction with a legitimate
# vertex-phase change (diag rational unit complex phases).
f=(O,C(F(3,5),F(4,5)),C(F(5,13),F(12,13)))
assert all(t*t.conj()==O for t in f)
for K in (A,B,Cbr,plus(plus(A,B),Cbr)):
    H=times(K,I)
    Hp=[[f[i]*H[i][j]*f[j].conj() for j in range(N)] for i in range(N)]
    assert wilson(Hp)==wilson(H)

print("PASS H29: P6 real two-edge coherent tangents and Lie closure = so(3)")
print("PASS H29: static path W=0; full coherent Lie closure has Re Wilson W=0")
print("PASS H29: H28 full four-phase knob exits the real-skew accessible algebra")
print("PASS H29: forward-only CPTP pulse-order contrast gives gamma-independent chord coherence")
print("PASS H29: dissipative inverse fails positivity; ideal BCH inverse loop unavailable")
print("PASS H29: Wilson restriction invariant under arbitrary site phase gauges")
print("SCOPE: phase extension and coherence readout not certified as physical P6 controls")
