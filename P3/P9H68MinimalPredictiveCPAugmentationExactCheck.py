"""H68 — exact minimal predictive completion versus CPTP reversibility.

Reuse SAME H42 Phi + H46 12-branch CP quantum instrument C as H48.
C has rank7, kernel span(E02,E20), while (C,C Phi) has rank9.
One independently DECLARED rational real 01-exchange Cayley *probe*
allows a rank9 two-arm CP instrument via classical randomization.
It yields minimal two extra COMPLEX linear sensor functionals, but no
single-shot CPTP quantum recovery: a CP branch effect is nonscalar.

The two arms are interventions / quantum-block tomographic data,
NOT passive nondisturbing P3 observations or frozen P6 readout.
No CR-specific physics, inherited J_N, KKS gravity, HDA/Einstein.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    N,z,eye,unit,add,sub,scale,mm,dagger,trace
)
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import A
from P9H46CPTPOddInstrumentReadoutDisturbanceExactCheck import (
    flagged,Ds,nonselective
)
from P9H48InstrumentProvenanceKernelClosureExactCheck import (
    Phi,full_record,real_rank_complex,E02,E20
)
assert N==3
MAT=[unit(i,j) for i in range(N) for j in range(N)]
def rankmap(f):
    return real_rank_complex([f(X) for X in MAT])
def conj(U,X):
    return mm(mm(U,X),dagger(U))
def cat(X,Y):
    return X+Y
def is_zero(v):
    return all(t==Z0 for t in v)

assert rankmap(full_record)==7
assert is_zero(full_record(E02)) and is_zero(full_record(E20))
assert rankmap(lambda x: cat(full_record(x),full_record(Phi(x))))==9
print("PASS H68: SAME H48 current instrument rank7, passive two-copy (C,C Phi) information rank9")

# Build a true rational real-orthogonal Cayley gate from H67's
# already declared physical-type 01 real exchange direction.
h=F(1,4)
assert dagger(A)==scale(A,-1)
assert mm(mm(A,A),A)==scale(A,-1)
UA=add(eye(),add(scale(A,2*h/(1+h*h)),
                 scale(mm(A,A),2*h*h/(1+h*h))))
assert mm(dagger(UA),UA)==eye()
def probe(X):
    return full_record(conj(UA,X))
k1=probe(E02)
k2=probe(E20)
assert len(k1)==len(k2)==108
assert real_rank_complex([k1,k2])==2
assert rankmap(lambda x:cat(full_record(x),probe(x)))==9

# Select just TWO complex-valued readout components to complement
# C: exact Gaussian rational 2x2 minor over missing chord sector.
pair=None
for i in range(len(k1)):
    for j in range(i+1,len(k1)):
        d=k1[i]*k2[j]-k1[j]*k2[i]
        if d!=Z0:
            pair=(i,j,d)
            break
    if pair is not None:break
assert pair is not None
i,j,minor=pair
def minimal_record(X):
    p=probe(X)
    return full_record(X)+[p[i],p[j]]
assert rankmap(minimal_record)==9
assert rankmap(full_record)==7
print("PASS H68: exactly TWO extra COMPLEX linear probe functionals complete rank7 -> rank9")
print("H68 exact chord pivot coordinates and minor:",i,j,minor)

# Over the Hermitian trace-one physical state affine space these lost
# complex E02/E20 directions correspond to two REAL quadratures.
odd_real=add(E02,E20)
odd_imag=scale(sub(E02,E20),I)
assert dagger(odd_real)==odd_real and dagger(odd_imag)==odd_imag
def coords(X):
    v=probe(X)
    out=[]
    for x in v:
        out.extend([x.r,x.i])
    return out
p=coords(odd_real);q=coords(odd_imag)
real_pair=None
for a in range(len(p)):
    for b in range(a+1,len(p)):
        det=p[a]*q[b]-p[b]*q[a]
        if det:
            real_pair=(a,b,det)
            break
    if real_pair:break
assert real_pair is not None
print("PASS H68: two extra REAL calibrated signal quadratures suffice on Hermitian states")
print("H68 Hermitian chord pivot coordinates and minor:",real_pair)

# A bona fide trace-preserving 24-branch CP instrument:
# with classical probability 1/2, perform existing H46 instrument,
# OR first perform real UA then H46 instrument. Output includes
# (arm,k,t) labels and FULL quantum conditional branch block.
def arm_blocks(arm,X):
    Y=X if arm==0 else conj(UA,X)
    return [scale(flagged(k,t,Y),F(1,2))
            for k in range(6) for t in (0,1)]
def joint(X):
    return [v for arm in (0,1)
            for block in arm_blocks(arm,X)
            for row in block for v in row]
def joint_total_trace(X):
    return sum((trace(M) for a in (0,1) for M in arm_blocks(a,X)),Z0)
for X in MAT:
    assert joint_total_trace(X)==trace(X)
    assert joint(X)==[v/F(2) for v in full_record(X)]+[
                     v/F(2) for v in probe(X)]
assert rankmap(joint)==9
print("PASS H68: random half-and-half real-Cayley plus ORIGINAL CP instrument is CPTP and informationally complete as a linear record")

# Explicit positive physical chord witnesses: same old instrument
# outputs but different *joint* quantum-block outputs.
rho0=scale(eye(),F(1,3))
for chord in (odd_real,odd_imag):
    rho_plus=add(rho0,scale(chord,F(1,6)))
    rho_minus=sub(rho0,scale(chord,F(1,6)))
    assert dagger(rho_plus)==rho_plus and dagger(rho_minus)==rho_minus
    assert trace(rho_plus)==trace(rho_minus)==O
    # 2x2 nontrivial principal subblock has eigenvalues 1/6, 1/2,
    # site 1 has 1/3, hence both states are positive.
    assert full_record(rho_plus)==full_record(rho_minus)
    assert joint(rho_plus)!=joint(rho_minus)
    assert all((trace(M).r>=0 and trace(M).i==0)
               for rho in (rho_plus,rho_minus)
               for arm in (0,1) for M in arm_blocks(arm,rho))
print("PASS H68: positive chord-state pairs invisible to C alone but distinguished by physical CP random-arm quantum-block observer")

# A linear inverse exists on the 9D image (informational completeness);
# this is NOT a CPTP inverse/recovery on unknown quantum states.
# Full-subspace Knill-Laflamme necessary condition: a reversible
# flagged CP instrument has every Kraus E_j^dagger E_j = scalar I.
# Here arm=0,k=0,t=0 Kraus is (1/2) D_0, and
# its effect is diag(1/4,9/100,0), manifestly non-scalar.
D0=Ds[0]
effect=scale(mm(dagger(D0),D0),F(1,4))
assert effect==add(scale(unit(0,0),F(1,4)),
                   scale(unit(1,1),F(9,100)))
assert effect!=scale(eye(),F(1,4))
assert effect!=scale(eye(),F(9,100))
print("PASS H68: quantum instrument has no full-state CPTP recovery despite injective linear record (non-scalar branch effect)")

# Since C and C Phi already form rank9, any linear predictive
# recorder R from which both factor must be injective (rank>=9).
# Joint rank9 gives an explicit mathematical sufficient carrier,
# but induced dynamics on image(J) need not be CPTP.
assert rankmap(lambda x:cat(full_record(x),full_record(Phi(x))))==N*N
assert rankmap(joint)==N*N
print("PASS H68: full-source rank9 is necessary to predict all C and C Phi outputs and achievable by an invasive CPTP information-complete instrument")
print("BOUNDARY: separate-preparation tomography, not one noninvasive monitored history; no microscopic P3->frozen P6 hardware provenance")
