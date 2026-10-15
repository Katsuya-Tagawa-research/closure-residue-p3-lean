"""H74 — three real population bases force full quantum recoverability.

H74.1 universal theorem: any CPTP channel C whose SINGLE-OUTPUT POVMs
can exactly simulate computational site populations plus 01 and 12
45-degree real-rotation population measurements on EVERY M3 density
must obey full-space Knill-Laflamme K_a†K_b=c_ab I, hence possess a
CPTP left recovery. If input/output Hilbert dimensions both 3 then
C is UNITARY. No noninjective CPTP exact three-basis observer exists.

H74.2 physically restricted positive escape: the SAME original H42
nonzero genuine P3 signed-R3 microscopic source admits an exact
CPTP-recoverable 2D even-parity code for its symmetry-locked controls
with exact single-copy readout on that code. Not invariant under BOTH
independently offered frozen P6 real-exchange knobs.

Finite analytic KL constraints recomputed EXACT with rational
unnormalized (equivalently normalized) 45-degree eigenvectors.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    N,z,unit,eye,scale,add,sub,mm,dagger,com,trace,rr
)
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import (
    U,reflection,A,B
)
from P9H43EquivariantCPTPCollectiveExtractionExactCheck import twirl
from P9H44MinimalObserverMemoryQuadraticResidueExactCheck import Phi
from P9H45QuadraticResidueSufficientOddSeedExactCheck import R12,R_EE
from P9H48InstrumentProvenanceKernelClosureExactCheck import real_rank_complex
from P9H73NativeRealControlOperatorSystemCPTPExactCheck import eclosed,rankmap

assert N==3
MAT=[unit(i,j) for i in range(3) for j in range(3)]
def conj(W,X):
    return mm(mm(W,X),dagger(W))
def vec(M):
    return [M[i][j] for i in range(3) for j in range(3)]

# Each measurement basis is orthogonal. The unnormalized 45-degree
# vectors are sufficient for ZERO orthogonality equations, and
# divide by sqrt(2) physically to obtain orthonormal state vectors.
B0=[(1,0,0),(0,1,0),(0,0,1)]
B01=[(1,1,0),(1,-1,0),(0,0,1)]
B12=[(1,0,0),(0,1,1),(0,1,-1)]
bases=(B0,B01,B12)
for V in bases:
    for i in range(3):
        for j in range(3):
            dot=sum(V[i][k]*V[j][k] for k in range(3))
            if i!=j:assert dot==0
            else:assert dot in (1,2)

# If a single-output POVM on C(rho) reproduces the original
# population measurement for this basis, C(|vi><vi|) and
# C(|vj><vj|) have mutually ORTHOGONAL supports for i != j.
# For EVERY pair of Kraus operators K_a,K_b of C,
# <vi|K_a†K_b|vj> must vanish. Treat the nine complex entries
# of B_ab=K_a†K_b as formal unknowns and solve linear constraints.
rows=[]
for V in bases:
    for i in range(3):
        for j in range(3):
            if i==j:continue
            v,w=V[i],V[j]
            rows.append([gc(v[a]*w[b]) for a in range(3) for b in range(3)])
assert len(rows)==18
assert real_rank_complex(rows)==8
ident_vec=vec(eye())
assert all(sum((coeff*t for coeff,t in zip(row,ident_vec)),Z0)==Z0
           for row in rows)
# 8D constraint rank on 9D coefficient space => 1D nullspace;
# identity solves => unique nullspace span_C{I}. This is full-space
# Knill-Laflamme condition for every pair of Kraus operators.
print("PASS H74: just THREE real population bases generate exact rank-8 Kraus-Gram orthogonality constraints => K_a†K_b=c_ab I")
print("PASS H74: full-space KL implies CPTP quantum recovery; 3-input to 3-output then forces UNITARY channel")

# H73 CP rank6 observer violates even the original computational
# readout distinguishability, and its 3D skew kernel blocks KL.
E00=unit(0,0)
E11=unit(1,1)
D=sub(E00,E11)
assert eclosed(D)==scale(D,F(2,5))
assert rankmap(eclosed)==6
assert eclosed(A)==z()
assert eclosed(E00)!=E00
print("PASS H74: H73 CPTP rank6 witness contracts an exactly distinguishable population pair 1 -> 2/5; cannot satisfy strong single-copy readout")

# Physical positive restricted-code example uses the SAME ORIGINAL
# H42 (non-real) microscopic unitary Φ, whose true P3 signed
# quadratic depth-three residue on E11 is nonzero (H45).
P=reflection
assert mm(P,P)==eye() and dagger(P)==P
Pplus=scale(add(eye(),P),F(1,2))
Pminus=scale(sub(eye(),P),F(1,2))
assert mm(Pplus,Pplus)==Pplus
assert mm(Pminus,Pminus)==Pminus
assert mm(Pplus,Pminus)==z()
assert trace(Pplus)==gc(2)
assert trace(Pminus)==O
assert mm(P,U)==mm(U,P)
assert R12(E11,E11)==R_EE
assert R_EE!=z()
assert R_EE==scale(add(add(scale(unit(0,0),F(-8,81)),
                             scale(unit(1,1),F(16,81))),
                       scale(unit(2,2),F(-8,81))),I)

def code(X):
    return mm(mm(Pplus,X),Pplus)
def recovery_plus(X):
    # CP: Pplus X Pplus plus nonnegative measure/prepare channel.
    return add(code(X),scale(Pplus,trace(mm(Pminus,X))/2))
for X in MAT:
    assert trace(recovery_plus(X))==trace(X)
    Y=code(X)
    assert twirl(Y)==Y
    assert recovery_plus(twirl(Y))==Y
    assert code(Phi(Y))==Phi(Y)
    assert recovery_plus(twirl(Phi(Y)))==Phi(Y)
assert code(E11)==E11
assert Phi(E11)!=E11
# On this 2D code the twirl is literally the identity: every
# POVM probability for the input equals the SAME output POVM.
assert twirl(code(D))==code(D)
print("PASS H74: same genuine nonzero-original-P3-R3 H42 source has a parity-even 2D quantum code with exact CPTP recovery, coherent closed Φ dynamics and exact single-copy POVM data on code")

# But independent real frozen P6-type edge controls A,B do not
# preserve the chosen 2D code: their odd components leak to Pminus.
assert mm(Pminus,mm(A,Pplus))!=z()
assert mm(Pminus,mm(B,Pplus))!=z()
# Irreducibility of their complex Lie action, exact rank-8
# simultaneous commutant => no nontrivial common invariant proper
# 2D code for ALL independently available controls.
comm_rows=[vec(com(E,A))+vec(com(E,B)) for E in MAT]
assert real_rank_complex(comm_rows)==8
print("PASS H74: parity-even protected P3 code is NOT stable under full independent frozen P6 real A/B manifold")
print("BOUNDARY: H74 global no-go assumes exact SINGLE-COPY measurement instrument compatibility for 3 real bases, not ensemble prediction")
print("BOUNDARY: parity code success uses reflection-matched micro source and restricted controls, not frozen P6 full controls/dephasing")
print("BOUNDARY: no independently inferred P3-origin P6 hardware, CR-only experiment, ADM/HDA/Einstein or P9 Minimum Success")
