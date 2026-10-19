"""H113 — original H75 source: H112 causal-break 'quantum memory' response is
EXACTLY simulated by old source OUTPUT FLAG bit classical feedforward,
on ALL 36 M6 matrix units, and lacks any irreducibly quantum-memory
certification. Original Kraus, original B control and observer unchanged.

Further exact operational no-go: a coherent old-record controlled-B
unitary G cannot be generated from independent (noninteracting)
old-register + original-system Hamiltonians, although a classical
measurement-conditioned local B pulse can simulate reduced response.
Return G commutes with declared total energy ONLY if local source
site1/site2 energies degenerate when the old a-bit is held fixed.
All energy statements apply to G, not arbitrary H75 source U.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    LK,R60,micro,MBASIS,U,B,
    eye_n,zero_n,matmul,matadj,matadd,mattrace,qconj
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P11H112ReturnedH75RecordCausalBreakNonMarkovExactCheck as H112

assert R60[0][0]==I*gc(F(-32,135))
assert len(LK)==4 and len(MBASIS)==36
assert H112.r0==F(1) and H112.r1==F(369,625)
assert H112.r0-H112.r1==F(256,625)

def trace(X):return mattrace(X)
def minus(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A))]
            for i in range(len(A))]
def scale(A,z):
    return [[z*A[i][j] for j in range(len(A))]
            for i in range(len(A))]
def comm(A,B):
    return minus(matmul(A,B),matmul(B,A))
def kron(A,B):
    n,m=len(A),len(B)
    return [[A[i//m][j//m]*B[i%m][j%m] for j in range(n*m)]
            for i in range(n*m)]
def effect_event(E,S):
    z=trace(matmul(E,S))
    assert z.i==0
    return z.r

# H113.1: H75 has an honest OUTPUT FLAG readout P_a on the very
# system. It is NOT necessary to access the Stinespring outgoing
# four-dimensional quantum environment to observe/store its a-bit.
P0=zero_n(6)
P1=zero_n(6)
for i in range(3):
    P0[i][i]=O
    P1[3+i][3+i]=O
assert matadd(P0,P1)==eye_n(6)
assert matmul(P0,P1)==zero_n(6)
for X in MBASIS:
    orig=micro(X)
    assert orig==matadd(qconj(P0,orig),qconj(P1,orig))
    for a,P in enumerate((P0,P1)):
        selected=zero_n(6)
        for b in (0,1):
            selected=matadd(selected,qconj(LK[2*a+b],X))
        assert qconj(P,orig)==selected
        assert trace(selected)==H112.pa(X)[a]
print("PASS H113.1: TRUE original H75 output flag P_a gives old Stinespring a probabilities and unchanged first-output state EXACTLY on all 36 M6 matrix units; a is a classical accessible flag candidate, not intrinsically a hidden quantum bath observable")

# Original 4D minimal Stinespring OUTGOING environment after tracing
# the old system has NO off-diagonal coherence between different
# output a values, because original L_ab output SYSTEM flag a
# sectors are orthogonal. This remains true for arbitrary M6 input.
A0=zero_n(4);A1=zero_n(4)
for k in (0,1):A0[k][k]=O
for k in (2,3):A1[k][k]=O
assert matadd(A0,A1)==eye_n(4)
for X in MBASIS:
    Z=H112.old_env(X)
    assert Z==matadd(qconj(A0,Z),qconj(A1,Z))
    for j in (0,1):
        for k in (2,3):
            assert Z[j][k]==Z[k][j]==Z0
    assert trace(matmul(A0,Z))==H112.pa(X)[0]
    assert trace(matmul(A1,Z))==H112.pa(X)[1]
print("PASS H113.2: for ALL original H75 input operators, first Stinespring reduced 4D environment state is ALREADY BLOCK-DIAGONAL in outgoing a; quantum a-coherence absent after the full system causal break")

# H113.3: A single classical saved a-bit plus delayed conditional
# ordinary ORIGINAL B drive reproduces EXACT same final 6D source
# output as H112's coherently controlled 4D old ancilla.
# Classical processor is an EXTRA delayed feedback/clock permission.
R6=H112.Win
assert matmul(matadj(R6),R6)==eye_n(6)
tau,tauB=H112.tau,H112.tauB
for X in MBASIS:
    p=(trace(matmul(P0,micro(X))),trace(matmul(P1,micro(X))))
    assert p==H112.pa(X)
    classical=matadd(scale(micro(tau),p[0]),scale(micro(tauB),p[1]))
    assert classical==H112.full_return_process(X)
    assert H112.reduced_env_after_return(X)==matadd(scale(tau,p[0]),scale(tauB,p[1]))
print("PASS H113.3: measured native first H75 output a-bit, stored through FULL causal break, delayed local native B pulse and unchanged final Phi reproduce H112 coherent old-environment G return on ALL 36 original M6 matrix units")

for rho in (H112.rho0,H112.rho1):
    assert trace(rho)==O
    val=effect_event(H112.Esite1,H112.full_return_process(rho))
    cl=effect_event(H112.Esite1,
                    matadd(scale(micro(tau),H112.pa(rho)[0]),
                           scale(micro(tauB),H112.pa(rho)[1])))
    assert val==cl
assert effect_event(H112.Esite1,H112.full_return_process(H112.rho0))==F(1)
assert effect_event(H112.Esite1,H112.full_return_process(H112.rho1))==F(369,625)
print("PASS H113.3: EXACT H112 causal-break 1 vs 369/625 (delta256/625) is not a quantum-specific memory witness: ONE classical a-bit plus permitted B pulse suffices (delayed controller independently assumed)")

# H113.4: In contrast, the FULL COHERENT controlled old-register
# G cannot be synthesized from isolated old-register operations
# plus original system-only local controls. Such uncorrelated
# Hamiltonian drives factor U_old tensor U_sys at all times.
G=H112.G
assert matmul(matadj(G),G)==eye_n(24)
assert G!=kron(eye_n(4),R6)
assert G!=eye_n(24)
assert R6!=eye_n(6)

# G entangles a coherent old-a superposition (not obtained by the
# physical first H75 trace/discard!) with source site |flag0,site1>.
# State density input = (|old00,site1>+|old10,site1>)(bra...)/2.
v=[Z0 for k in range(24)]
v[1]=O
v[13]=O
pure=[[gc(F(1,2))*v[i]*v[j].conj() for j in range(24)]
      for i in range(24)]
assert trace(pure)==O and matmul(pure,pure)==pure
post=qconj(G,pure)
assert trace(post)==O and matmul(post,post)==post
oldred=[[sum((post[6*k+i][6*l+i] for i in range(6)),Z0)
         for l in range(4)] for k in range(4)]
assert oldred[0][0]==oldred[2][2]==gc(F(1,2))
assert oldred[0][2]==oldred[2][0]==gc(F(3,10))
purity=trace(matmul(oldred,oldred))
assert purity==gc(F(17,25))
assert purity!=O
print("PASS H113.4: H112 coherent G has operator Schmidt rank2 (NOT local product): its explicit old-a coherent + site1 pure input becomes entangled, reduced old-register purity 17/25, impossible with any independent old-only plus source-only unitary drives")
print("BOUNDARY: first H75 source after tracing system NEVER supplies old-a coherent input; this is a NONFACTORIZATION certificate for G, NOT an experimentally existing quantum old-record entanglement")

# H113.5: Test energy conservation of the ACTUAL unchanged H112
# 24D coherent memory RETURN G under explicitly DECLARED diagonal
# site Hamiltonian and a PRESERVED old a-register energy.
def Hsite(e1,e2):
    S=zero_n(6)
    for f in (0,1):
        S[3*f+1][3*f+1]=gc(e1)
        S[3*f+2][3*f+2]=gc(e2)
    return S
H_old=zero_n(4)
for k in (2,3):H_old[k][k]=gc(F(3)) # arbitrary a-sector record energy
def total_energy(e1,e2):
    return matadd(kron(H_old,eye_n(6)),kron(eye_n(4),Hsite(e1,e2)))
Hsplit=total_energy(F(1),F(2))
Hdeg=total_energy(F(1),F(1))
comm_split=comm(G,Hsplit)
comm_deg=comm(G,Hdeg)
assert comm_split!=zero_n(24)
assert comm_deg==zero_n(24)
assert comm(G,kron(H_old,eye_n(6)))==zero_n(24)
assert comm(G,kron(eye_n(4),Hsite(F(1),F(2))))==comm_split
assert G[6*2+2][6*2+1]*gc(F(1))!=Z0 # conditional B mixes site1->2
print("PASS H113.5: coherent H112 old-a-preserving memory return G fails strict energy conservation for DECLARED nondegenerate site levels epsilon1=1,epsilon2=2, regardless of diagonal preserved old-a memory energy; it commutes exactly for test epsilon1=epsilon2=1")

def gate_work_for(rho,H):
    incoming=kron(H112.old_env(rho),tau)  # exact state AFTER full break
    outgoing=qconj(G,incoming)
    de=trace(matmul(H,minus(outgoing,incoming)))
    assert de.i==0
    return de.r
assert gate_work_for(H112.rho0,Hsplit)==F(0)
assert gate_work_for(H112.rho1,Hsplit)==F(256,625)
assert gate_work_for(H112.rho0,Hdeg)==F(0)
assert gate_work_for(H112.rho1,Hdeg)==F(0)
print("PASS H113.5: on ACTUAL original H75 positive histories, conditional return G changes declared split-site gate-stage energy by 0 vs +256/625; degenerate-site gate-stage energy change identically zero")

# Do not silently call the WHOLE source energy preserving:
# The original fixed complex U of H75 couples site0 to site1/2,
# so the unmodified last H75 CPTP reset generally changes
# the declared site H, even if return G itself preserves it.
source_energy_before=effect_event(Hsite(F(1),F(1)),tau)
source_energy_after=effect_event(Hsite(F(1),F(1)),micro(tau))
assert source_energy_before==F(1)
assert source_energy_after==F(5,9)
assert source_energy_before!=source_energy_after
print("PASS H113.6: declared degenerate-site Hamiltonian makes MEMORY RETURN G energy conserving but NOT the original H75 reset Phi (native U changes test site energy 1 -> 5/9); avoid whole-process conservation overclaim")

gate_status={
"AX-SRC genuine H75 output a and available source B coherent site control":"EXACT",
"AX-OA one stored classical a-bit simulates H112 causal-break final source output":"CONDITIONAL_EXACT",
"AX-OA actual delayed measurement record storage and conditional pulse controller":"INDEPENDENT",
"AX-CAN full coherent controlled old quantum register G from uncoupled native controls":"SCOPED_NO_GO",
"AX-CAN exact G total-energy conservation for fixed a and nondegenerate eps1 eps2":"SCOPED_NO_GO",
"AX-CAN same G energy conservation if site1/2 degenerate":"CONDITIONAL_EXACT",
"Intrinsic quantum P5 memory that cannot be simulated by classical feedback":"NOT_SHOWN",
"AX-SP P9 genuine Cartan solder/curvature":"OPEN",
"AX-DYN sourced DeWitt full HDA Einstein":"OPEN",
"AX-GEN noncircular F completeness":"OPEN"
}
assert len(gate_status)==10
print("VERDICT H113: the source-matched H112 history effect is conditionally CLASSICAL record-memory feedback, not irreducible quantum memory; coherent G needs old-system coupling; energy-preserving iff doublet degenerate under declared fixed-bit diagonal energy model")
print("BOUNDARY: H75 source includes positive output flag and local B pulses but not automatically an independently timed autonomous feedback controller; neither controller nor its energy battery/clock/observer law is generated by original P3 residue or F")
print("BOUNDARY: no new arbitrary Hamiltonian, P9 16/48D Cartan model identification, physical solder/ADM/Einstein dynamics or F generative completeness")
