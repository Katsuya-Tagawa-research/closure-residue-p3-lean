"""H112 — EXACT H75 causal-break quantum-memory-return witness, using
ONLY ORIGINAL source true four-Kraus reset and original physical B
site rotation. The ability to retain 1st COLLISION STINESPRING
ancilla and coherently control a LATER B pulse with its old output
flag a is an INDEPENDENT NEW MEMORY-INTERACTION PERMISSION.

The fresh environmental collision without this returned record
remains exactly Markovian (H111), including correlated outgoing
records. With returned old a-bit, SAME fixed process and SAME full
system causal-break tau yield next site effect 1 vs 369/625 under
different original positive preparations (Delta=256/625).
Original second flags are BLIND to this return. All exact Gaussian
rational. NOT sourced P5 Omega/P6 memory from P3, P9 Cartan,
Einstein or P11 generative completeness.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    LK,R60,U,B,micro,embed,qtrace,MBASIS,
    eye_n,zero_n,matmul,matadj,matadd,mattrace,qconj,
    edge_cayley,lift
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91

assert R60[0][0]==I*gc(F(-32,135))
assert len(LK)==4 and len(MBASIS)==36
I6=eye_n(6)
I4=eye_n(4)
Z6=zero_n(6)
tau=embed(H91.e(3,1,1))
assert matadj(tau)==tau and mattrace(tau)==O
assert qconj(tau,tau)==tau
Rb=edge_cayley(B,F(1,2))
Win=lift(Rb)
assert matmul(matadj(Win),Win)==I6
assert Rb[1][1]==gc(F(3,5))
assert Rb[2][1]*Rb[2][1].conj()==gc(F(16,25))
tauB=qconj(Win,tau)
assert matadj(tauB)==tauB and mattrace(tauB)==O
assert tauB!=tau
print("PASS H112.0: original H75 genuine 4-Kraus source and real local B-Cayley H103 control reused unchanged, with exact fixed positive causal-break re-preparation tau")

def scale(X,c):
    return [[c*X[i][j] for j in range(len(X))] for i in range(len(X))]
def trace(X):return mattrace(X)
def diff(X,Y):
    return [[X[i][j]-Y[i][j] for j in range(len(X))] for i in range(len(X))]
def same(X,Y):return X==Y
def kronecker(A,B):
    n,m=len(A),len(B)
    return [[A[i//m][j//m]*B[i%m][j%m] for j in range(n*m)] for i in range(n*m)]

# The TRUE four Kraus records are labeled k=2a+b:
# k0=(a0,b0),k1=(a0,b1),k2=(a1,b0),k3=(a1,b1).
# First Stinespring ancilla 4D holds (a,b), retaining a bit.
def pk(X):
    return [trace(qconj(L,X)) for L in LK]
def pa(X):
    ps=pk(X)
    return (ps[0]+ps[1],ps[2]+ps[3])
for E in MBASIS:
    x,y=pa(E)
    assert x+y==trace(E)
print("PASS H112.1: actual H75 first Stinespring record a probabilities sum to true original full-M6 trace on ALL 36 source matrix units")

# Memory-return quantum unitary: old 4D ancilla controls a genuine
# physical local B site pulse on *later* six-level system.
# This 24D controlled SOURCE-MEMORY G is a NEW interaction premise,
# not inherited merely because local B pulses are available.
G=zero_n(24)
for k in range(4):
    Vk=I6 if k<2 else Win
    for i in range(6):
        for j in range(6):
            G[6*k+i][6*k+j]=Vk[i][j]
assert matmul(matadj(G),G)==eye_n(24)
assert matmul(G,matadj(G))==eye_n(24)
assert G!=eye_n(24)
print("PASS H112.2: exact 24x24 fixed unitary G_return = (A0⊗I6)+(A1⊗B_lift) is a coherent OLD RECORD -> FUTURE SYSTEM interaction, independently assumed and source-B compatible")

# A complete causal break (trace-and-reprepare tau) DISCARDs all
# 6D system data but retains old environment history register.
# Build the TRUE outgoing old environment density from the
# genuine H75 minimal Stinespring isometry without importing a
# different artificial quantum register.
def old_env(X):
    return [[trace(matmul(matmul(LK[k],X),matadj(LK[l])))
             for l in range(4)] for k in range(4)]
def reduced_env_after_return(X):
    old=old_env(X)
    combined=kronecker(old,tau)         # after FULL system break
    post=qconj(G,combined)             # fixed controlled memory return
    return [[sum((post[6*k+i][6*k+j] for k in range(4)),Z0)
             for j in range(6)] for i in range(6)]
def predicted_pre_second(X):
    p0,p1=pa(X)
    return matadd(scale(tau,p0),scale(tauB,p1))
# An exact 24D pre/post controlled-unitary test on all original
# source matrix units, proving that old-record coherences do not
# survive final environment trace for this diagonal G.
for E in MBASIS:
    assert reduced_env_after_return(E)==predicted_pre_second(E)
print("PASS H112.2: COMPLETE system causal break plus ACTUAL old Stinespring environment plus fixed coherent G_return yields p0(X)tau+p1(X)RtauR† for ALL 36 original H75 M6 matrix units")

# The TRUE second collision is always unchanged H75 source Phi.
# The process has a physical full-system causal break and a fixed
# returned-memory controller on the intermediate environment.
def full_return_process(X):
    return micro(reduced_env_after_return(X))
def fresh_markov_control(X):
    # original first Phi; then full causal break to tau; then
    # no historic record -> future ordinary native source Phi.
    return scale(micro(tau),trace(X))
for E in MBASIS:
    assert full_return_process(E)==matadd(
        scale(micro(tau),pa(E)[0]),
        scale(micro(tauB),pa(E)[1]))
    assert trace(full_return_process(E))==trace(E)
    assert trace(fresh_markov_control(E))==trace(E)
print("PASS H112.3: exact true second 4-Kraus H75 CPTP composition after causal break and memory-return unitary, with all-unit original M6 trace preservation")

# Physical P6-style POSITIVE site effect after the actual fixed U
# in the source final collision, with no independent output U
# Hamiltonian control asserted: E1=I_flag⊗U|1><1|Udag.
Psite1=H91.e(3,1,1)
Esite1=lift(qconj(U,Psite1))
assert matadj(Esite1)==Esite1
assert matmul(Esite1,Esite1)==Esite1
assert Esite1!=Z6 and Esite1!=I6
def event(E,S):
    r=trace(matmul(E,S))
    assert r.i==0
    return r.r
native_after_break=micro(tau)
rotated_after_break=micro(tauB)
assert event(Esite1,native_after_break)==F(1)
assert event(Esite1,rotated_after_break)==F(9,25)
print("PASS H112.4: source-U-calibrated positive actual H75 site effect reads native pre-rotation 1 vs genuine B-rotation 9/25 after unchanged final H75 collision")

# Two explicitly POSITIVE histories. Both share the EXACT SAME
# subsequent full 6D re-preparation tau, and future channel,
# observer and conditional G_return are fixed.
rho0=embed(H91.e(3,0,0))
rho1=embed(H91.e(3,1,1))
for s in (rho0,rho1):
    assert matadj(s)==s and trace(s)==O
assert pa(rho0)==(O,Z0)
assert pa(rho1)==(gc(F(9,25)),gc(F(16,25)))
for x in (rho0,rho1):
    assert trace(reduced_env_after_return(x))==O
    assert event(Esite1,fresh_markov_control(x))==F(1)
r0=event(Esite1,full_return_process(rho0))
r1=event(Esite1,full_return_process(rho1))
assert r0==F(1)
assert r1==F(369,625)
assert r0-r1==F(256,625)
assert r1==F(9,25)*F(1)+F(16,25)*F(9,25)
print("PASS H112.5: EXACT conditional past-to-future causal-break non-Markov witness: same tau gives positive site readout 1 vs 369/625 (difference 256/625) when fixed externally added old a-record controlled native B pulse RETURNS after break; without return both read 1")

# Second output flag-only observers are BLIND to the record return:
# M0/M1 have identical attenuation on source site levels 1,2.
Pflag0=zero_n(6);Pflag1=zero_n(6)
for i in range(3):
    Pflag0[i][i]=O
    Pflag1[3+i][3+i]=O
for X in (micro(tau),micro(tauB),
          full_return_process(rho0),full_return_process(rho1)):
    assert event(Pflag0,X)==F(9,25)
    assert event(Pflag1,X)==F(16,25)
print("PASS H112.6: BOTH final original coarse H75 output flags stay exactly (9/25,16/25) even when old memory return creates site effect difference 256/625; coarse observer is blind")

# An *intrinsic* original H75 source without returned environment
# and without novel future intervention remains H111 strict
# quantum Markov, no old-record backflow across complete break.
# Conditional G_return is a NEW past-dependent interaction
# permission and not proof of non-Markovity from P3 alone.
gates={
"AX-SRC authentic H75 Kraus and old a-record":"EXACT",
"AX-OA complete system causal break and positive site effect":"EXACT_MATHEMATICAL",
"AX-OA detector availability and old record access":"INDEPENDENT_PREMISE",
"AX-CAN future controlled-B old environment G unitary":"INDEPENDENT_PREMISE",
"P5/P6 genuine causal-break influence if G implemented":"CONDITIONAL_EXACT",
"Intrinsic H75 unmodified source temporal nonMarkov":"NO",
"AX-SP actual same-source P9 Cartan solder/curvature":"OPEN",
"AX-DYN DeWitt / Einstein action / full HDA":"OPEN",
"AX-NORM gravity normalization / AX-GEN completeness":"OPEN"
}
assert len(gates)==9
print("BOUNDARY: causal-break violation belongs to the FIXED EXTENDED MEMORY-RETURN process, not original fresh H75 Markov source or its signed P3 residue by itself; feedback/controller physical provenance remains OPEN")
print("BOUNDARY: source-positive temporal memory-response witness neither sources P5 Omega nonMarkov F axiom, P9 Cartan spatial transport, nondegenerate KKS ADM, nor universal GR Einstein dynamics")
