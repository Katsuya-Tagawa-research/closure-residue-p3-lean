"""H69: informative CP observer need not admit CPTP autonomous dynamics.

Exactly the SAME H42 original P3 microscopic Phi, H46 instrument C,
and H68 rank-nine 24-branch CPTP completion I are reused.

An explicit physical state difference X=E02+E20 has
  || I(X) ||_1 <= 1
but the DIAGONAL PINCH of I Phi(X) has norm 3856/2601 > 1.
CPTP trace-norm contractivity rules out ANY CPTP output T obeying
T I = I Phi on ALL input quantum states. Injectivity does imply a
linear intertwiner on range(I) only.

This is conventional finite QM, not CR-specific or physical P6 origin.
"""
from fractions import Fraction as F
from P9H68MinimalPredictiveCPAugmentationExactCheck import (
    N,I,O,Z0,gc,unit,eye,scale,add,dagger,trace,
    Phi,full_record,UA,arm_blocks,joint,rankmap
)
from P9H24PhaseSensitiveResidueGaugeExactCheck import C
assert N==3 and rankmap(joint)==9
X=add(unit(0,2),unit(2,0))
assert dagger(X)==X and trace(X)==Z0
assert full_record(X)==[Z0]*108
# I=1/2 C + 1/2 C Ad_UA, each arm individually CPTP (H68).
# The first arm vanishes on X. Since ||X||1=2, contractivity
# gives ||I(X)||1 <= (1/2) ||X||1 =1 exactly.
prior_upper=F(1)

def diagonal_pinching_norm_of_joint(Y):
    # Every block is Hermitian for a Hermitian Y.
    # Trace norm >= sum of |diagonal entries|, by CP pinching.
    out=F(0)
    arm_terms=[]
    for arm in (0,1):
        subtotal=F(0)
        for block in arm_blocks(arm,Y):
            assert dagger(block)==block
            for j in range(N):
                v=block[j][j]
                assert v.i==0
                subtotal+=abs(v.r)
        arm_terms.append(subtotal)
        out+=subtotal
    return out,arm_terms

before_diag,before_arms=diagonal_pinching_norm_of_joint(X)
after_diag,after_arms=diagonal_pinching_norm_of_joint(Phi(X))
assert before_diag==F(0) and before_arms==[F(0),F(0)]
assert after_arms==[F(8,9),F(1544,2601)]
assert after_diag==F(3856,2601)
assert after_diag>prior_upper
print("PASS H69: EXACT trace-norm obstruction before <= 1 and after >= 3856/2601")
print("PASS H69: original H42 Phi, H68 CPTP random-arm I are unchanged, and observer rank = 9")

# Explicit valid positive Hermitian input pair:
# rho±=I3/3 ± (E02+E20)/6.
# eigenvalues are {1/6,1/3,1/2}. Difference =X/3.
rho0=scale(eye(),F(1,3))
p=add(rho0,scale(X,F(1,6)))
m=add(rho0,scale(X,F(-1,6)))
assert dagger(p)==p and dagger(m)==m
assert trace(p)==trace(m)==O
assert p[0][0]*p[2][2]-p[0][2]*p[2][0]==gc(F(1,12))
assert m[0][0]*m[2][2]-m[0][2]*m[2][0]==gc(F(1,12))
assert all(trace(block).r>=0 and trace(block).i==0
           for state in (p,m)
           for arm in (0,1)
           for block in arm_blocks(arm,state))
diff=[x-y for x,y in zip(joint(p),joint(m))]
assert diff==[x/F(3) for x in joint(X)]
prior_physical_upper=prior_upper/F(3)
later_physical_lower=after_diag/F(3)
assert later_physical_lower>prior_physical_upper
print("PASS H69: positive density pair violates the output data-processing inequality required by any CPTP T")

# A separate full quantum-state isometric memory admits CPTP dynamics:
# J(rho)=|0><0|_flag tensor rho (a 6x6 block matrix).
# \\tilde{Phi}(Y)=(I_flag tensor U)Y(I_flag tensor U†)
# and Tr_flag[J(rho)]=rho. This is a *full-state storage* example,
# not an emergent smaller P3/P6 observer nor the H68 instrument.
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import U
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import mm

def zero6():
    return [[Z0 for j in range(6)] for i in range(6)]
def embed(Y):
    K=zero6()
    for i in range(3):
        for j in range(3):
            K[i][j]=Y[i][j]
    return K
def partial_flag_trace(Y):
    return [[Y[i][j]+Y[i+3][j+3] for j in range(3)] for i in range(3)]
def tildeU():
    K=zero6()
    for i in range(3):
        for j in range(3):
            K[i][j]=U[i][j]
            K[i+3][j+3]=U[i][j]
    return K
def adjoint6(M):
    return [[M[j][i].conj() for j in range(6)] for i in range(6)]
def mm6(M,P):
    return [[sum((M[i][k]*P[k][j] for k in range(6)),Z0)
             for j in range(6)] for i in range(6)]
U6=tildeU()
identity6=zero6()
for k in range(6):identity6[k][k]=O
assert mm6(adjoint6(U6),U6)==identity6
for a in range(3):
    for b in range(3):
        E=unit(a,b)
        assert partial_flag_trace(embed(E))==E
        lhs=mm6(mm6(U6,embed(E)),adjoint6(U6))
        assert lhs==embed(Phi(E))
print("PASS H69: full quantum isometric memory admits an actual CPTP intertwiner and CPTP left recovery")
print("BOUNDARY: this sufficient full-state storage is tautological and does not derive smaller physical CR observer memory")
print("BOUNDARY: NO-GO belongs to fixed H68 24-branch instrument; full P6/P9 operational provenance/GR remain OPEN")
