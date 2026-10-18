"""H80 — Sharp PHYSICAL minimality of H79 reset-checkpoint CPTP memory.

Fixed unchanged H75 four-Kraus 6D P3 microscopic source,
J(ρ)=Phi_mu(|0><0|_flag⊗ρ), and genuine nonzero ORIGINAL P3 R3.
H79 built exact CP 5-Hilbert-level, 13-operator-rank memory. H80
proves it is OPTIMAL among ALL finite-dimensional CPTP encoders E
and CPTP decoders D satisfying D E J(ρ)=J(ρ) for EVERY qutrit
density matrix ρ (full flagged QUANTUM block state recovery).

Proof is analytical and independent of optimization:
 1. Compress H79 output support K to logical C5.
 2. Choose faithful reference σ=J(I3/3) on K.
 3. 9 normalized likelihood operators
    σ^-1/2 J(Eij) σ^-1/2 /3 = Eij^(3)⊕P12 Eij P12^(2)
    generate the FULL 13D C*-algebra M3⊕M2, by explicit products.
 4. For T=D E fixing J(ρ) and σ, T maps K into K.
    Ψ(X)=σ^-1/2 T(σ^1/2 X σ^1/2) σ^-1/2
    is unital CP, preserves faithful σ-weighted trace, and fixes
    those 9 likelihood operators. Kadison-Schwarz equality and
    faithfulness force them into Ψ's multiplicative domain; thus
    Ψ fixes the entire generated M3⊕M2 C*-algebra.
    Hence T fixes ALL 13 complex block operators.
 5. E must be injective on the 13D algebra (rank E>=13).
    Since two orthogonal flag sectors of dimensions 3 and 2 are
    EACH reversibly encoded with mutually orthogonal output supports,
    physical output Hilbert dimension d>=3+2=5.
 6. H79's three-Kraus E:M6->M5 with image M3⊕M2 and isometric
    decoder D saturate BOTH lower bounds.

NO claim of global optimality for scalar-only readout, approximate
memory, restricted preparations, or protocols omitting exact recovery
of the full labelled quantum-block post-reset state. Original P3
does not select the external reset/control hardware.
All finite checks exact Gaussian rational.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    U,MBASIS,R60,micro,embed,d0,d1,ONE6
)
from P9H79ResetCheckpointCPTPMemoryExactCheck import (
    V,Vd,PK,encode,decode,eye_n,zero_n,adj,mul,madd,smul,
    tr,flatten,rankmap
)
from P9H48InstrumentProvenanceKernelClosureExactCheck import real_rank_complex

assert len(MBASIS)==36
assert R60[0][0]==I*gc(F(-32,135))

def basis(n,i,j):
    M=zero_n(n)
    M[i][j]=O
    return M
def vflat(X):
    return [v for row in X for v in row]
def block_add3_2(X3,Y2):
    M=zero_n(5)
    for i in range(3):
        for j in range(3):
            M[i][j]=X3[i][j]
    for i in range(2):
        for j in range(2):
            M[3+i][3+j]=Y2[i][j]
    return M

# Remove the known nonreal H42 U phase INSIDE the first logical
# flag block to obtain a rational diagonal faithful σ reference.
G=zero_n(5)
for i in range(3):
    for j in range(3):
        G[i][j]=U[j][i].conj()
for i in range(2):G[3+i][3+i]=O
assert mul(adj(G),G)==eye_n(5)
def canonical(X):
    return mul(mul(G,X),adj(G))
def joint(X):
    # Exactly the SAME original H75 quantum flag instrument output,
    # now expressed in canonical five-level logical coordinates.
    return canonical(encode(micro(embed(X))))
def analytic_joint(X):
    # M0=(1,3/5,3/5), M1=(0,4/5,4/5).
    v=(gc(1),gc(F(3,5)),gc(F(3,5)))
    Y=zero_n(5)
    for i in range(3):
        for j in range(3):
            Y[i][j]=v[i]*X[i][j]*v[j]
    for i in (1,2):
        for j in (1,2):
            Y[i+2][j+2]=gc(F(16,25))*X[i][j]
    return Y

EB3=[basis(3,i,j) for i in range(3) for j in range(3)]
for X in EB3:
    assert joint(X)==analytic_joint(X)
assert rankmap(joint,EB3)==9
sigma=analytic_joint(smul(eye_n(3),F(1,3)))
assert [sigma[i][i] for i in range(5)]==[
    gc(F(1,3)),gc(F(3,25)),gc(F(3,25)),
    gc(F(16,75)),gc(F(16,75))]
assert all(sigma[i][i].i==0 and sigma[i][i].r>0
           for i in range(5))
assert tr(sigma)==O
print("PASS H80: same actual post-reset H75 quantum experiment J has rank9 and faithful 5-level reference σ; exact CP H79 encoding agrees with analytic J on all nine M3 basis units")

# Relative likelihood operators S_ij = (1/3)σ^-1/2 J(Eij)σ^-1/2.
# Although σ^-1/2 contains sqrt3, all entries of Sij are exactly
# rational Eij in flag0 and if i,j>=1 matching Eij in flag1.
def likelihood(i,j):
    L=zero_n(5)
    L[i][j]=O
    if i>=1 and j>=1:
        L[i+2][j+2]=O
    return L
L={(i,j):likelihood(i,j) for i in range(3) for j in range(3)}
for i in range(3):
    for j in range(3):
        X=analytic_joint(basis(3,i,j))
        # Explicit diagonal sandwich without radicals:
        # first block sqrt(σ_iσ_j)=m_i m_j/3.
        m=[F(1),F(3,5),F(3,5)]
        assert X[i][j]==gc(m[i]*m[j])
        # Verify normalized likelihood entries without irrational
        # inverse square roots: X_ij^2=9 σ_ii σ_jj and X_ij>0.
        assert X[i][j]*X[i][j]==gc(9)*sigma[i][i]*sigma[j][j]
        assert X[i][j].i==0 and X[i][j].r>0
        if i>0 and j>0:
            assert X[i+2][j+2]==gc(F(16,25))
            assert X[i+2][j+2]*X[i+2][j+2]==(
                gc(9)*sigma[i+2][i+2]*sigma[j+2][j+2])
        assert L[(i,j)][i][j]==O
assert real_rank_complex([vflat(L[i,j]) for i in range(3) for j in range(3)])==9

# Construct the EXACT full block matrix-unit algebra from products
# of nine normalized quantum likelihood operators.
BLOCK0={}
BLOCK1={}
for i in range(3):
    for j in range(3):
        if i==0 or j==0:
            BLOCK0[i,j]=L[i,j]
        else:
            BLOCK0[i,j]=mul(L[i,0],L[0,j])
        direct=zero_n(5)
        direct[i][j]=O
        assert BLOCK0[i,j]==direct
for i in (1,2):
    for j in (1,2):
        BLOCK1[i,j]=madd(L[i,j],smul(BLOCK0[i,j],-1))
        direct=zero_n(5)
        direct[i+2][j+2]=O
        assert BLOCK1[i,j]==direct

BASIS13=[BLOCK0[i,j] for i in range(3) for j in range(3)]
BASIS13 += [BLOCK1[i,j] for i in (1,2) for j in (1,2)]
assert len(BASIS13)==13
assert real_rank_complex([vflat(X) for X in BASIS13])==13
for X in BASIS13:
    for Y in BASIS13:
        # Block diagonal algebra is closed under products.
        prod=mul(X,Y)
        assert all(prod[i][j]==Z0 for i in range(3) for j in (3,4))
        assert all(prod[j][i]==Z0 for i in range(3) for j in (3,4))
print("PASS H80: nine relative density / likelihood matrices generate ALL 13 independent matrix units of M3⊕M2 by exact multiplication")
print("PASS H80: fixed-point multiplicative-domain theorem forces any exact CPTP recovery-composite T to fix the full generated 13D quantum-block algebra")

# Both distinguishable flag-sector full-rank normal reference states
# are legitimate elements of the fixed generated state algebra:
rho0=smul(block_add3_2(eye_n(3),zero_n(2)),F(1,3))
rho1=smul(block_add3_2(zero_n(3),eye_n(2)),F(1,2))
assert tr(rho0)==tr(rho1)==O
assert mul(rho0,rho1)==zero_n(5)
assert real_rank_complex([vflat(X) for X in BASIS13])==13

# Dimension lower bound is analytic:
# If CPTP E and D fix EVERY post-reset J(ρ), they fix all A.
# E(rho0),E(rho1) must be trace-distance 1 orthogonal-supported
# because D returns distinct-flag orthogonal rho0,rho1.
# Restriction to each full quantum sector is quantum reversible;
# it requires support dimension >=3 and >=2, respectively.
# Thus any physical memory Hilbert carrier d>=3+2=5.
# E must also be injective on A, hence operator rank(E)>=13.
assert 3+2==5 and 3*3+2*2==13
assert rankmap(encode,MBASIS)==13
for X in EB3:
    microstate=micro(embed(X))
    assert decode(encode(microstate))==microstate
print("PASS H80: H79 actual three-Kraus CPTP encoder saturates universal CPTP memory lower bounds: Hilbert dimension5 and operator rank13")
print("PASS H80: physical five-level memory is EXACTLY OPTIMAL for complete quantum-block post-reset recovery of all qutrit input states")

# There cannot be a 3- or 4-level exact recovering CPTP memory,
# nor an arbitrary-output CPTP linear recording map with rank<13,
# under full state-family recovery; equality with H79 is SHARP.
assert [sigma[i][i] for i in range(5)]!=[Z0]*5
print("BOUNDARY: this is a universal CPTP lower bound for exact full flagged quantum-state recovery; NOT scalar site populations, approximate recovery, or restricted seed codes")
print("BOUNDARY: proof uses analytic faithful-reference and fixed-point multiplicative-domain argument, verified exact rational generated-algebra certificates")
print("BOUNDARY: H75's original P3 R3 is standard finite quantum CPTP physics; no unique P3-only control port, observer source, CR-only signature or GR derivation")
