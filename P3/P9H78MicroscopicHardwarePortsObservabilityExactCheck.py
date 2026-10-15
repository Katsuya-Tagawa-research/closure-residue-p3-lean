"""H78 — calibrated microscopic control ports determine exact predictive rank.

SAME unchanged H75 six-dimensional four-Kraus quantum source,
and SAME H76 physical CPTP flag-block observer Cflag.
Replace H77's four merely listed finished pulses by independently
specified PHYSICAL CONTROL-PORT GENERATORS:

  flag real skew J_E (switchable, real amplitude),
  visible real skew A and B (independently switchable),
  conditional-SWAP F (from a calibrated flag-conditioned projector).

Prove EXACT infinitesimal Heisenberg response (continuous-port)
observability ranks 18,27,31,35,36, agreeing with H77 finite pulses.
A calibrated known port Hamiltonian + pulse availability is a distinct
microscopic source assumption; uncontrolled original P3 R3 does not
identify which ports the actual device supplies.

A crucial causal/practical refinement: H75's mandatory reset channel
has complex operator rank 9, not 36. If preparations are strictly
post-reset micro outputs, the prediction-data manifold has linear
dimension only 9 even if the expanded port catalog is accessible.
H77/H78's full rank36 theorem requires arbitrary 6D pre-reset states
and the option to apply control words BEFORE compulsory resetting.
Rank 9 is a linear manifold claim, NOT a 3D CPTP recovery claim.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    ONE6,MBASIS,R60,micro,edge_cayley,A,B,lift,
    matmul,matadj,matadd,matscale,zero_n,
)
from P9H76FeedbackFlagMemoryCPTPExactCheck import (
    Fgate,W,flagged,
)
from P9H77ControlObservabilityMemoryRankExactCheck import (
    OBS_ROWS,add_independent,apply_row,build_action,GATES,closure,
)
from P9H48InstrumentProvenanceKernelClosureExactCheck import real_rank_complex

N=6
N2=N*N
E=ONE6
ZZ=zero_n(N)
assert len(MBASIS)==N2 and R60[0][0]==I*gc(F(-32,135))

# A reversible REAL flag-control Hamiltonian port.
# J_E = (|1><0| - |0><1|)_flag tensor I_3.
J=zero_n(N)
for j in range(3):
    J[j][3+j]=-O
    J[3+j][j]=O
assert matadj(J)==matscale(J,-1)
assert matmul(J,J)==matscale(E,-1)

def flag_cayley(t):
    assert t*t+1
    return matadd(
        matscale(E,gc((1-t*t)/(1+t*t))),
        matscale(J,gc(2*t/(1+t*t))))
assert flag_cayley(F(0))==E
assert flag_cayley(F(1,2))==W
assert matmul(matadj(W),W)==E
print("PASS H78: exact CALIBRATED real flag port J_E Cayley(1/2) produces H76 coherent flag unitary W")

# H75's independently defined physical real coherent edge controls
# are recovered as exact finite pulses of the known edge port generators.
KA=lift(A)
KB=lift(B)
UA=lift(edge_cayley(A,F(1,2)))
UB=lift(edge_cayley(B,F(2,3)))
assert UA==GATES["A"] and UB==GATES["B"]
assert matadj(KA)==matscale(KA,-1)
assert matadj(KB)==matscale(KB,-1)
assert matmul(matadj(UA),UA)==matmul(matadj(UB),UB)==E

# The source-declared real feedback F is a pulse of an actual
# Hermitian PROJECTOR Hamiltonian H_F=(I-F)/2:
# e^{-i*pi*H_F}=I-2 H_F=F exactly by spectral calculus.
# Independent hardware premise: an addressable conditional interaction
# port with calibrated pulse area pi; P3 source DOES NOT imply this port.
HF=matscale(matadd(E,matscale(Fgate,-1)),gc(F(1,2)))
assert matadj(HF)==HF
assert matmul(HF,HF)==HF
assert matadd(E,matscale(HF,-2))==Fgate
assert matmul(matadj(Fgate),Fgate)==E
print("PASS H78: conditional-feedback F is an exact pi-pulse of a calibrated Hermitian projector port")
print("PASS H78: both independently adjustable visible real exchange ports give original H77 finite Cayley pulses")

def index(i,j):return i*N+j
def tangent_action(K):
    # Exact generator d/dt Ad_{exp(tK)} at t=0 = [K,X].
    # Cayley(tK) derivative at 0 is 2K; scalar factor 2 does
    # not change the generated row space or kernel filtration.
    out=[[F(0)]*N2 for _ in range(N2)]
    for i in range(N):
        for j in range(N):
            rr=out[index(i,j)]
            for k in range(N):
                for l in range(N):
                    a=K[i][k] if j==l else Z0
                    b=K[l][j] if i==k else Z0
                    d=a-b
                    assert d.i==0
                    rr[index(k,l)]=d.r
    return out

PORTS={"J":tangent_action(J),"A":tangent_action(KA),
       "B":tangent_action(KB),"F":build_action(Fgate)}
assert PORTS["F"]==build_action(GATES["F"])

def tangent_closure(names,max_depth=12):
    basis={}
    new=[]
    for row in OBS_ROWS:
        v=add_independent(row,basis)
        if v is not None:new.append(v)
    depths=[len(basis)]
    for _ in range(max_depth):
        nextrows=[]
        for row in new:
            for name in names:
                v=add_independent(apply_row(row,PORTS[name]),basis)
                if v is not None:nextrows.append(v)
        depths.append(len(basis))
        if not nextrows:return depths,basis
        new=nextrows
    raise AssertionError("control-port tangent span did not stabilize")

EXPECTED={
    ("F",):[18,18],
    ("J",):[18,27,27],
    ("J","F"):[18,27,31,31],
    ("J","F","A"):[18,27,31,34,35,35],
    ("J","F","A","B"):[18,27,31,35,36,36],
    ("F","A","B"):[18,18],
    ("J","A","B"):[18,27,27],
}
for names,want in EXPECTED.items():
    depths,pivots=tangent_closure(names)
    assert depths==want,(names,depths,want)
    print("PASS H78 exact PORT-TANGENT control catalog",names,"rank depths",depths)
assert len(tangent_closure(("J","F","A","B"))[1])==36
assert closure(("W","F","A","B"))[0]==[18,27,31,35,36,36]
print("PASS H78: true infinitesimal calibrated-port observability exactly matches H77 full finite-pulse rank36")

# An independently specified on/off control-port apparatus makes the
# catalog physically determinate. But original uncontrolled H75
# microscopic channel and all its P3 residues are IDENTICAL under
# any choice of port switches (the port gates are NOT inserted into
# the uncontrolled Phi_mu definition).
assert all(micro(X)==micro(X) for X in MBASIS)
assert R60[0][0]==I*gc(F(-32,135))
assert flagged(micro(MBASIS[3]))==micro(MBASIS[3])

# Critically inspect reset/preparation scope. H75 Φ_mu factors
# through partial trace to M3 and then creates a flagged output.
# It has rank exactly 9 (M3 complex dimension). The flag record
# is ID on its range, therefore even when all post-reset control
# words are available, the set of records as a function of a
# pre-reset input occupies at most 9 LINEAR dimensions.
def vector(X):return [q for row in X for q in row]
rankmicro=real_rank_complex([vector(micro(X)) for X in MBASIS])
rankflagmicro=real_rank_complex([vector(flagged(micro(X))) for X in MBASIS])
assert rankmicro==rankflagmicro==9,(rankmicro,rankflagmicro)
assert all(flagged(micro(X))==micro(X) for X in MBASIS)
print("PASS H78: mandatory H75 measurement/reset prepares a rank-NINE complex-linear microscopic output manifold, not arbitrary M6 states")
print("PASS H78: after compulsory reset the flagged observer is injective on that source-output manifold; minimal linear record rank is 9 for these preparations")

# A direct genuinely POSITIVE readout calibration checks the flag
# port distinguishes a pair of microscopic states initially equal
# under Cflag, BEFORE a mandatory reset.
X=zero_n(N)
X[0][3]=O
X[3][0]=O
assert flagged(X)==ZZ
dX=matadd(matmul(J,X),matscale(matmul(X,J),-1))
p=flagged(dX)
assert p[0][0]==gc(-2) and p[3][3]==gc(2)
assert p!=ZZ
P=matscale(E,gc(F(1,6)))
rp=matadd(P,matscale(X,gc(F(1,12))))
rm=matadd(P,matscale(X,gc(F(-1,12))))
assert flagged(rp)==flagged(rm)
assert matadj(rp)==rp and matadj(rm)==rm
assert rp[0][0]*rp[3][3]-rp[0][3]*rp[3][0]==gc(F(1,48))
assert rm[0][0]*rm[3][3]-rm[0][3]*rm[3][0]==gc(F(1,48))
assert flagged(matmul(W,matmul(rp,matadj(W))))!=flagged(
       matmul(W,matmul(rm,matadj(W))))
print("PASS H78: positive 6D states with the same flag record have distinct calibrated real-port responses; physically detecting the port needs coherent pre-reset preparation")

print("BOUNDARY: port availability, pulses, flag quantum-block tomography and pre-reset preparation are INDEPENDENT HARDWARE facts")
print("BOUNDARY: FULL rank36 necessity is conditional on arbitrary M6 pre-reset inputs and observability before unavoidable reset")
print("BOUNDARY: source-only P3 signed residue cannot select a control-port set or infer a new CR-only operational law")
print("BOUNDARY: rank9 of reset image is a linear preparation manifold, NOT proof of rank9 CPTP memory under all later controls")
print("BOUNDARY: no frozen P6 J_N provenance, physical P7/P8 metric soldering, ADM/HDA/Einstein or P9 Minimum Success")
