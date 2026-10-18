"""H81: operational-accessibility axiom and exact causal scheduling witness.

This uses the SAME unchanged H75 6D original-P3 CPTP source with
genuine signed R3 != 0 and the SAME H76 rank18 physical flag CP
observer. It compares DIFFERENT PHYSICAL INTERVENTION CATALOGS on
that exact same microscopic channel.

If unavoidable source reset happens BEFORE any coherent flag port,
the pair rho± differing solely by hidden flag coherence have
identical source output and no subsequent legal operation can tell
them apart. If the independently certified coherent flag rotation W
and the already H75 physical flag-conditioned site SWAP F are both
addressable BEFORE reset, then the ordinary final site-population
measurement reveals the formerly hidden input flag coherence.

This distinction is an exact positive-state, positive-POVM,
all-CPTP counterexample to inferring the apparatus's causal
accessibility from uncontrolled P3 microscopic dynamics alone.
It motivates an explicit independent operational-accessibility
premise for P11 and a controlled-source evidence gate for P9.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    MBASIS,ONE6,R60,micro,embed,matmul,matadj,matadd,matscale,
    mattrace,zero_n,qconj,qtrace,U,Fgate,d0,d1,r6
)
from P9H76FeedbackFlagMemoryCPTPExactCheck import W,flagged
from P9H48InstrumentProvenanceKernelClosureExactCheck import real_rank_complex

assert len(MBASIS)==36
assert R60[0][0]==I*gc(F(-32,135))
assert R60!=zero_n(6)

def sub(X,Y):
    return matadd(X,matscale(Y,-1))
def flatten(X):
    return [c for row in X for c in row]
def after_reset_first(X):
    # Reset is compulsory BEFORE any independently available port.
    return micro(X)
def pre_reset_ports_then_reset(X):
    # W and F are independently addressable BEFORE source reset.
    return micro(qconj(Fgate,qconj(W,X)))
def after_reset_then_ports(X):
    # SAME physical devices but compulsory reset first.
    return qconj(Fgate,qconj(W,micro(X)))
def positive_joint_flag_site_probability(X,a,j):
    assert a in (0,1) and j in (0,1,2)
    c=X[3*a+j][3*a+j]
    assert c.i==0
    return c.r
def positive_site_probability(X,j):
    c=qtrace(X)[j][j]
    assert c.i==0
    return c.r

# Two POSITIVE and normalised six-level states: identity plus/minus
# one Hermitian flag coherence |0,site0><1,site0| + adjoint.
X=zero_n(6)
X[0][3]=O
X[3][0]=O
assert flagged(X)==zero_n(6)
rho0=matscale(ONE6,F(1,6))
rho_plus=matadd(rho0,matscale(X,F(1,12)))
rho_minus=matadd(rho0,matscale(X,F(-1,12)))
for rho in (rho_plus,rho_minus):
    assert matadj(rho)==rho
    assert mattrace(rho)==O
    # Two eigenvalues 1/6±1/12 are strictly positive, others 1/6.
    assert rho[0][0]*rho[3][3]-rho[0][3]*rho[3][0]==gc(F(1,48))
    assert rho[0][0].r>0 and rho[3][3].r>0
assert rho_plus!=rho_minus
assert flagged(rho_plus)==flagged(rho_minus)
assert after_reset_first(rho_plus)==after_reset_first(rho_minus)
print("PASS H81: pair of full-rank positive micro states indistinguishable by original flag observer and by the SAME uncontrolled P3 source reset")

# The flag-coherent rotation W converts hidden flag coherence into
# visible flag populations: exact + and - output in H76.
assert matmul(matadj(W),W)==ONE6
assert matmul(matadj(Fgate),Fgate)==ONE6
rotated_X=flagged(qconj(W,X))
assert rotated_X[0][0]==gc(F(-24,25))
assert rotated_X[3][3]==gc(F(24,25))
assert all(rotated_X[i][i]==Z0 for i in (1,2,4,5))

# A calibrated W pulse before the reset ALONE is not sufficient to
# expose X AFTER reset: flag mixing does not change partial trace.
assert micro(qconj(W,X))==zero_n(6)
# Nor is conditional feedback alone sufficient before reset for
# this purely offdiagonal flag-coherence witness.
assert micro(qconj(Fgate,X))==zero_n(6)

# But first W then flag-1-conditional F converts the hidden input
# into a visible SITE population difference prior to reset.
pre_reset_response=pre_reset_ports_then_reset(X)
expected=matscale(sub(micro(embed(d1)),micro(embed(d0))),F(24,25))
assert pre_reset_response==expected
assert pre_reset_response!=zero_n(6)
assert qtrace(pre_reset_response)!=zero_n(3)

delta=sub(pre_reset_ports_then_reset(rho_plus),
          pre_reset_ports_then_reset(rho_minus))
assert delta==matscale(expected,F(1,6))
assert qtrace(delta)[1][1]==gc(F(-4,75))
assert qtrace(delta)[2][2]==gc(F(4,75))
assert qtrace(delta)[0][0]==Z0
# This is a GENUINE positive-POVM single-site effect, not signed
# response tomography. Site2 population difference =4/75.
p_plus=positive_site_probability(pre_reset_ports_then_reset(rho_plus),2)
p_minus=positive_site_probability(pre_reset_ports_then_reset(rho_minus),2)
assert p_plus-p_minus==F(4,75)
assert F(0)<p_plus<F(1) and F(0)<p_minus<F(1)
print("PASS H81: exact pre-reset W then F then SAME microscopic Φ yields nonzero single-copy SITE2 probability contrast 4/75")

# SAME channel, SAME ports, different compulsory causal order:
# reset FIRST erases distinguishing coherence, so no subsequent
# CPTP processing (including W,F and any more operations) can
# distinguish the initial positive pair.
assert after_reset_then_ports(rho_plus)==after_reset_then_ports(rho_minus)
assert after_reset_then_ports(X)==zero_n(6)
assert positive_site_probability(after_reset_then_ports(rho_plus),2)==(
       positive_site_probability(after_reset_then_ports(rho_minus),2))
print("PASS H81: same hardware pulses AFTER compulsory reset produce ZERO contrast; actual accessibility requires certified PORT + SCHEDULING premises")

# Exact finite operational observability witness: initial Cflag
# record rank18; appending one physically measured final qutrit
# site2 effect after W,F,Φ provides a nonzero functional on its
# kernel, increasing the observable rank AT LEAST one.
def q2_after_pre_reset_ports(Z):
    return qtrace(pre_reset_ports_then_reset(Z))[2][2]
R0=[flatten(flagged(Z)) for Z in MBASIS]
R1=[flatten(flagged(Z))+[q2_after_pre_reset_ports(Z)]
    for Z in MBASIS]
rank0=real_rank_complex(R0)
rank1=real_rank_complex(R1)
assert rank0==18
assert rank1==19,(rank0,rank1)
assert q2_after_pre_reset_ports(X)==gc(F(8,25))
assert q2_after_pre_reset_ports(after_reset_first(X))==Z0
print("PASS H81: a SINGLE physical controlled site probability enlarges source-fixed predictive linear observation rank 18→19 when pre-reset access is certified")

# A necessary-and-sufficient finite algebraic closure test for a
# GIVEN linear observer C and intervention T:
# ker(C) invariant under T iff exists linear map Ttilde
# on im(C) with Ttilde C=C T. CP extension not automatic.
# Here the physical actual Cflag is CPTP and its image is a
# C*-algebra. Micro and flag-classical F preserve Cflag kernel,
# while W violates it with exact witness.
for Z in MBASIS:
    assert flagged(micro(Z))==micro(flagged(Z))
    assert flagged(qconj(Fgate,Z))==qconj(Fgate,flagged(Z))
assert flagged(qconj(W,X))!=zero_n(6)
assert flagged(qconj(W,flagged(X)))==zero_n(6)
print("PASS H81: CP-autonomous output maps exist for catalog {micro,F}, but W violates the fixed CP flag observer kernel on a physical state pair")

# Source-only P3 data are identical in both experimental programs,
# since they use the SAME untouched micro map: exact original-P3
# signed quadratic residue is nonzero and independent of how
# external controls are physically certified.
D6=[MBASIS[7*i] for i in range(6)]
assert all(micro(Z)==after_reset_first(Z) for Z in MBASIS)
assert r6(D6[0],D6[0])==R60
assert R60[0][0]==I*gc(F(-32,135))
print("PASS H81: identical uncontrolled Φ and full original-P3 R3 under two DIFFERENT causal control-access catalogs; P3-alone cannot select apparatus")

print("BOUNDARY: AX-OA requires independent certificate of physical ports, allowed pulse words, causal ordering, prepared-state scope and output instruments")
print("BOUNDARY: the finite intersection kernel theorem gives optimal LINEAR predictive rank, but CPTP quantum memory demands independent CP construction")
print("BOUNDARY: H80's sharp 5-level / rank13 CPTP checkpoint memory is conditional on mandatory reset and full quantum-output recovery, unaffected")
print("BOUNDARY: measured 4/75 contrast is STANDARD quantum physics; NOT CR-exclusive, nor a direct measurement of P3 signed R3")
print("BOUNDARY: no P3-only generation of frozen-P6 J_N or P9 EH/HDA/Einstein equations; P11 generative completeness remains OPEN")
