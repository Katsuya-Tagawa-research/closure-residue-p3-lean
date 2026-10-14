"""H46: physically CPTP/instrument-compatible readout of the signed odd
diagonal seed label required for ORIGINAL P3 quadratic residue.

Two precise protocols:
(1) A 12-outcome completely-positive flagged instrument whose
    NONSELECTIVE quantum marginal is exactly H43's fixed E=S_(3/5)T,
    but whose outcome record has mean q=(rho00-rho22)/2. The quantum
    marginal ALONE forgets q; its environment/flags need not.
    This changes subsequent microscopic dynamics if inserted, because
    E Phi != Phi E.
(2) A two-outcome site-0 yes/no Lüders instrument that is non-invasive
    NONSELECTIVELY on all original P3 diagonal seeds, and reveals
    a=rho00. Combined with parity-even u=(a+c)/2 it recovers q=a-u.
    It is NOT nondisturbing on arbitrary coherent quantum states.

Finite ensemble estimation is statistical, not single-shot exact.
The original P3 signed R(d) is nonlinear and must be computed from
ensemble-prepared unconditioned d, NOT averaged conditional branch R.
No P6 inherited hardware access or CR-only comparator is proved.

Exact Fraction-Gaussian rational arithmetic; no floating tolerances.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import N,U,reflection
from P9H43EquivariantCPTPCollectiveExtractionExactCheck import E,twirl
from P9H45QuadraticResidueSufficientOddSeedExactCheck import (
    D,R12,real_parity_parameters,R_EE,R_OE,same_seed_formula,paired_formula
)
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    unit,z,eye,scale,add,sub,mm,dagger,com,diag,hidden,trace
)
assert N==3
def matdiag(x):
    return D(x[0],x[1],x[2])
def Phi(x):
    return mm(mm(U,x),dagger(U))
def scalartrace(x):return trace(x)
def quantum_norm_diag(x):
    assert x==diag(x)
    assert all(x[i][i].r==0 for i in range(N))
    return sum((abs(x[i][i].i) for i in range(N)),F(0))
def superpose(items):
    total=z()
    for x in items:total=add(total,x)
    return total
def parity_q(rho):
    assert dagger(rho)==rho
    return (rho[0][0].r-rho[2][2].r)/2
def effectprob(out):
    val=trace(out)
    assert val.i==0
    return val.r

# A RATIONAL Gram decomposition of Schur correlation matrix
# M_s=[[1,s,0],[s,1,s],[0,s,1]], s=3/5.
# Vectors indexed by site:
# v0=(1,0,0,0,0,0)
# v1=(3/5,4/5,0,0,0,0)
# v2=(0,3/4,1/4,1/4,1/4,1/2)
# Their inner products are M_s, allowing all-rational Kraus
# D_k=diag(v0_k,v1_k,v2_k).
KRAUS=[
 (F(1), F(3,5), F(0)),
 (F(0), F(4,5), F(3,4)),
 (F(0), F(0), F(1,4)),
 (F(0), F(0), F(1,4)),
 (F(0), F(0), F(1,4)),
 (F(0), F(0), F(1,2))
]
def gram(i,j):
    return sum((a[i]*a[j] for a in KRAUS),F(0))
assert [[gram(i,j) for j in range(N)] for i in range(N)]==[
    [F(1),F(3,5),F(0)],
    [F(3,5),F(1),F(3,5)],
    [F(0),F(3,5),F(1)]]
Ds=[matdiag(v) for v in KRAUS]
P=reflection
def flagged(k,t,rho):
    # CP outcome map: (1/2) D_k P^t rho P^t D_k†.
    assert k in range(6) and t in (0,1)
    x=rho if t==0 else mm(mm(P,rho),P)
    return scale(mm(mm(Ds[k],x),dagger(Ds[k])),F(1,2))
def nonselective(rho):
    return superpose(flagged(k,t,rho)
                     for k in range(6) for t in (0,1))
basis=[unit(i,j) for i in range(N) for j in range(N)]
for x in basis:
    # Exact equality as superoperators; hence E's whole quantum
    # channel, not just a few diagonal populations, is preserved.
    assert nonselective(x)==E(x)
    assert trace(nonselective(x))==trace(x)
    assert dagger(nonselective(x))==nonselective(dagger(x))
# CP is manifest from individual Kraus maps.
# Each outcome has Kraus D_k P^t/sqrt(2) with positive weight;
# their sum is a unital, trace-preserving E channel.

def classical_flag_moments(rho):
    dist={(k,t):effectprob(flagged(k,t,rho))
          for k in range(6) for t in (0,1)}
    assert all(v>=0 for v in dist.values())
    assert sum(dist.values(),F(0))==F(1)
    # Recorded Z=+1 for (k=0,t=0), Z=-1 for (0,1), else 0.
    mean=dist[(0,0)]-dist[(0,1)]
    second=dist[(0,0)]+dist[(0,1)]
    variance=second-mean*mean
    assert F(0)<=variance<=F(1)
    return mean,variance,dist
samples=[
    unit(0,0),unit(1,1),unit(2,2),
    D(F(3,8),F(1,2),F(1,8)),
    D(F(1,8),F(1,2),F(3,8)),
    D(F(2,7),F(1,7),F(4,7)),
    scale(eye(),F(1,3)),
    scale(add(add(unit(0,0),unit(1,1)),
              add(unit(0,1),unit(1,0))),F(1,2)),
    scale(add(add(unit(0,0),unit(2,2)),
              add(unit(0,2),unit(2,0))),F(1,2))
]
for rho in samples:
    assert dagger(rho)==rho and trace(rho)==O
    q,var,dist=classical_flag_moments(rho)
    assert q==parity_q(rho)
    # This distribution yields unbiased q for *every* physical
    # Hermitian rho, even before imposing diagonal seed restriction.
    # Chebyshev over n independent copies: probability deviation
    # >=eps <= var/(n eps²) <= 1/(n eps²).
    n=10000
    eps=F(1,5)
    assert var/F(n)/eps**2<=F(1,n)/eps**2

# Operationally identical H43 quantum outputs can have
# distinguishable H46 CLASSICAL outcome labels.
r0=unit(0,0);r2=unit(2,2)
assert E(r0)==E(r2)
assert classical_flag_moments(r0)[0]==F(1,2)
assert classical_flag_moments(r2)[0]==F(-1,2)
assert classical_flag_moments(r0)[2][(0,0)]==F(1,2)
assert classical_flag_moments(r0)[2][(0,1)]==F(0)
assert classical_flag_moments(r2)[2][(0,0)]==F(0)
assert classical_flag_moments(r2)[2][(0,1)]==F(1,2)

# FLAGGED E IS NOT nondisturbing microscopic Φ preparation even
# for diagonal seed d=E00: the nonselective state is twirled.
assert nonselective(r0)==twirl(r0)!=r0
assert Phi(nonselective(r0))!=Phi(r0)
assert E(Phi(r0))!=Phi(E(r0))
# There is no contradiction: the classical record carries q but
# the emitted quantum system is compressed, so its natural later
# history is Φ E, not Φ on the untouched microscopic state.

# A second distinct 2-outcome Lüders instrument is nondisturbing
# in the NONSELECTIVE sense for ALL original diagonal seeds:
# P0=E00, Q0=I-P0.
P0=unit(0,0);Q0=sub(eye(),P0)
def J0(x):return mm(mm(P0,x),P0)
def J1(x):return mm(mm(Q0,x),Q0)
def Jsum(x):return add(J0(x),J1(x))
assert add(P0,Q0)==eye()
assert mm(P0,Q0)==z()
for x in basis:
    assert trace(Jsum(x))==trace(x)
for a,b,c in ((F(1),F(0),F(0)),
              (F(3,8),F(1,2),F(1,8)),
              (F(1,8),F(1,2),F(3,8)),
              (F(1,3),F(1,3),F(1,3)),
              (F(2,7),F(1,7),F(4,7))):
    rho=D(a,b,c)
    assert Jsum(rho)==rho
    # q=a-u, with u from the parity-even E quantum observer
    # and a from classical yes/no P0 outcome probability.
    even_u=E(rho)[0][0].r
    p_yes=effectprob(J0(rho))
    assert p_yes==a
    assert p_yes-even_u==(a-c)/2==parity_q(rho)
    # Keeping both outcomes UNCONDITIONALLY after initial
    # nondemolition readout yields the EXACT original Φ^n(d).
    x=rho
    y=Jsum(rho)
    for _ in range(9):
        x=Phi(x);y=Phi(y)
        assert x==y
# It is a two-outcome (not full three-site-resolved) classical
# measurement. A single shot samples a Bernoulli variable;
# p_yes and q are estimated over independently prepared copies.
# Chebyshev for n shots, even_u assumed independently calibrated,
# Pr(|qhat-q|>=eps) <= 1/(4n eps²) since Bernoulli var<=1/4.

# On COHERENT states, the two-outcome instrument is disruptive,
# since it destroys 01 and 02 coherence. The inability to be
# universally nondisturbing is a standard information-disturbance
# fact, not a P3-specific new physical law.
coherent=scale(add(add(unit(0,0),unit(1,1)),
                   add(unit(0,1),unit(1,0))),F(1,2))
assert dagger(coherent)==coherent and trace(coherent)==O
assert coherent[0][1]==gc(F(1,2))
assert Jsum(coherent)[0][1]==Z0
assert Jsum(coherent)!=coherent
assert Phi(Jsum(coherent))!=Phi(coherent)

# Crucial nonlinear bookkeeping: R(linear mixture) generally
# differs from mixture of conditional branch residues.
rho=D(F(3,8),F(1,2),F(1,8))
pa=F(3,8)
left=unit(0,0)
rest=scale(add(scale(unit(1,1),F(1,2)),
               scale(unit(2,2),F(1,8))),F(8,5))
assert J0(rho)==scale(left,pa)
assert J1(rho)==scale(rest,1-pa)
assert add(scale(left,pa),scale(rest,1-pa))==rho
original_R=R12(rho,rho)
branch_average=add(scale(R12(left,left),pa),
                   scale(R12(rest,rest),1-pa))
assert branch_average!=original_R
assert original_R==same_seed_formula(*real_parity_parameters(rho)[1:])

# Deterministic total trace-norm reconstruction uncertainty.
norm_EE=F(32,81)
norm_OE=F(48,81)
assert quantum_norm_diag(R_EE)==norm_EE
assert quantum_norm_diag(R_OE)==norm_OE
def output_with_estimated_q(d,qhat):
    _,e,_=real_parity_parameters(d)
    return same_seed_formula(e,qhat)
def bound_same_seed(d,eps):
    _,e,q=real_parity_parameters(d)
    assert eps>=0
    return 3*norm_EE*(2*abs(q)*eps+eps*eps)+4*norm_OE*abs(e)*eps
for d in [D(*abc) for abc in (
    (F(3,8),F(1,2),F(1,8)),
    (F(1,8),F(1,2),F(3,8)),
    (F(2,7),F(1,7),F(4,7)),
    (F(1,3),F(1,3),F(1,3)),
    (F(0),F(1),F(0))
)]:
    _,e,q=real_parity_parameters(d)
    for delta in (F(-1,100),F(1,100),F(-1,40),F(1,40)):
        qhat=q+delta
        err=quantum_norm_diag(sub(R12(d,d),
                                output_with_estimated_q(d,qhat)))
        assert err<=bound_same_seed(d,abs(delta))
# Joint/mixed witness from 2 seeds with independent q estimates:
# |delta R|_1 <=3||REE||1(|q|eps'+|q'|eps+eps eps')
#             +||ROE||1(3|e|eps'+|e'|eps).
ds=[D(F(3,8),F(1,2),F(1,8)),
    D(F(2,7),F(1,7),F(4,7))]
d,f=ds
_,e,q=real_parity_parameters(d)
_,ep,qp=real_parity_parameters(f)
eps=F(1,100);epsp=F(1,60)
for sign in (-1,1):
    estimated=paired_formula(e,q+sign*eps,ep,qp-sign*epsp)
    error=quantum_norm_diag(sub(estimated,R12(d,f)))
    bound=3*norm_EE*(abs(q)*epsp+abs(qp)*eps+eps*epsp)
    bound+=norm_OE*(3*abs(e)*epsp+abs(ep)*eps)
    assert error<=bound

print("PASS H46: 12-outcome exact CP instrument reproduces H43 E as full nonselective quantum channel")
print("PASS H46: classical outcome flag estimates signed odd q for EVERY Hermitian physical input")
print("PASS H46: quantum marginal alone erases q; environment record can retain it, without violating no-broadcasting")
print("PASS H46: two-outcome initial projective instrument is nonselectively nondisturbing on ALL original diagonal P3 seeds")
print("PASS H46: the same two-outcome probe DISTURBS coherent input; flagged E disturbs diagonal microscopic future")
print("PASS H46: averaging branch-specific quadratic residues does not reconstruct original mixture residue")
print("PASS H46: exact deterministic signed P3 residue error budget, with independent shot-noise concentration")
print("SCOPE: estimated ensemble information, not single-shot exact q; phase/control/P6 hardware provenance OPEN")
print("SCOPE: standard quantum CPTP theory; no CR-only comparator, GR or Einstein dynamics")
