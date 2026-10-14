"""H40: a SINGLE fully fixed 3-site CPTP/GKSL preparation channel, exact original
P3 two-step residue, calibrated finite-time P6-style operational readout,
and strong diagonal/*-compatible gauge-coordinate intertwining.

The static radius-one microscopic sector J_static=span_C(E01,E21)
is INDEPENDENTLY DECLARED, not asserted equal to frozen P6's inherited J_N
and not inferred from P3 Krylov data after seeing the result.

Additional Stark phase, coherent reference preparation and readout
hardware are explicitly extra resources. Standard GKSL predicts it all.
"""
from fractions import Fraction as F
from math import factorial
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H38P6RealExchangeObserverGateExactCheck import (
    N,A,B,unit,eye,z,scale,add,sub,mm,dagger,com,diag,hidden,trace,
    gksl_real_step
)
from P9H39FiniteTimePhaseReadoutExactCheck import (
    certified_exp_D,contrast_coeffs,transfer_coeffs,phase_dephase
)
assert N==3

def target_diag(vals):
    x=z()
    for k,v in enumerate(vals): x[k][k]=gc(v)
    return x
def generator(x,K,alpha,gamma):
    return sub(gksl_real_step(x,K,gamma),
               scale(com(target_diag(alpha),x),I))
def jets(x,K,alpha,gamma,order):
    out=[x]
    for m in range(1,order+1):
        out.append(scale(generator(out[-1],K,alpha,gamma),F(1,m)))
    return out
def sample(coeffs,t):
    value=z()
    for m,c in enumerate(coeffs):
        value=add(value,scale(c,t**m))
    return value
def dpart(x):return diag(x)
def signed_residue(x,y):return diag(com(hidden(x),hidden(y)))
def frob_phase(rho,G):return mm(mm(G,rho),dagger(G))
def site_current(x,y,p,q):
    return 2*(x[p][q]*y[p][q].conj()).i
def no_negative_support(gamma):
    assert gamma>=0
def rank_complex_two(u,v):
    return u!=z() and v!=z() and u!=v

# FIX the microscopic GKSL dynamics and STATIC P6-style graph sector
# BEFORE constructing its P3 hidden iterates or measuring the residue.
a=F(2,3)
b=F(3,5)
gamma=F(1,2)
alpha=(F(1,7),F(0),F(-1,11))
K=add(scale(A,a),scale(B,b))
J_static=(unit(0,1),unit(2,1))
def Xi(j):return hidden(sub(j,dagger(j)))
assert Xi(J_static[0])==A and Xi(J_static[1])==B
assert Xi(add(scale(J_static[0],a),scale(J_static[1],b)))==K
assert all(abs(i-j)==1 for k in J_static for i in range(N)
           for j in range(N) if k[i][j]!=Z0)
assert dagger(K)==scale(K,-1)
assert all(isinstance(v,F) for v in alpha)
no_negative_support(gamma)

d=unit(0,0)
order=16
coeff=jets(d,K,alpha,gamma,order)
assert coeff[0]==d
for n,c in enumerate(coeff):
    assert dagger(c)==c and trace(c)==(O if n==0 else Z0)

# Exact P3 quadratic residue legal depth 1+2 for the single Phi_t.
t=F(1,4096)
rho1=sample(coeff,t)
rho2=sample(coeff,2*t)
z1=hidden(rho1)
z2=hidden(rho2)
Rpoly=signed_residue(rho1,rho2)
assert dagger(Rpoly)==scale(Rpoly,-1)
assert trace(Rpoly)==Z0
assert Rpoly[0][0].r==0 and Rpoly[0][0].i!=0
# Compare the ORIGINAL depth-three leading jet to P9.38 Laplacian:
Ahidden=hidden(coeff[1])
Bhidden=hidden(scale(coeff[2],2))
R3=diag(com(Ahidden,Bhidden))
expected=scale(sub(unit(0,0),unit(1,1)),
               I*gc(2*a*a*alpha[0]))
assert R3==expected
# No dephasing contribution to this leading cubic witness.
for gam in (F(0),gamma,F(5,4)):
    cc=jets(d,K,alpha,gam,2)
    assert diag(com(hidden(cc[1]),hidden(scale(cc[2],2))))==expected

# The population projection is NOT a valid two-step intertwiner.
# P=Delta, T=Delta Phi_t restricted to D. Leading in t:
# Delta Phi_t²(d) - T²(d) = t² Delta L²(d) + O(t³).
L2diag=diag(scale(coeff[2],2))
assert L2diag==scale(sub(unit(1,1),unit(0,0)),gc(2*a*a))
assert L2diag!=z()
# Identity of the full quantum update WOULD give the correct two steps.
assert len(coeff)==17

# Nontrivial (but only coordinate/gauge) exact strong intertwiner:
# G diagonal unitary, iota=Ad_G, L_phys=Ad_G L_micro Ad_G^-1,
# with the SAME fixed gamma and alpha, and K_phys=G K G†.
g=target_diag((O,C(F(3,5),F(4,5)),O))
assert mm(g,dagger(g))==eye()
Kg=frob_phase(K,g)
def physical_law(y):
    return generator(y,Kg,alpha,gamma)
basis=[unit(i,j) for i in range(N) for j in range(N)]
for x in basis:
    assert frob_phase(generator(x,K,alpha,gamma),g)==physical_law(frob_phase(x,g))
    assert frob_phase(diag(x),g)==diag(frob_phase(x,g))
    assert frob_phase(dagger(x),g)==dagger(frob_phase(x,g))
for x in basis:
    for y in basis:
        assert frob_phase(mm(x,y),g)==mm(frob_phase(x,g),frob_phase(y,g))
assert frob_phase(d,g)==d
phys_coeff=[frob_phase(x,g) for x in coeff]
assert phys_coeff==jets(d,Kg,alpha,gamma,order)
prho1=sample(phys_coeff,t);prho2=sample(phys_coeff,2*t)
assert prho1==frob_phase(rho1,g) and prho2==frob_phase(rho2,g)
assert signed_residue(prho1,prho2)==frob_phase(Rpoly,g)==Rpoly
assert Xi(frob_phase(J_static[0],g))==frob_phase(A,g)
assert Xi(frob_phase(J_static[1],g))==frob_phase(B,g)
# This is a rigorously intertwining gauge *coordinate* model only;
# P6 independently inherited microscopic J_N provenance remains OPEN.

# Certified semigroup remainder: |rho_exact(s)-rho_poly(s)| entrywise.
# Bound ||L||entry-infty <=2*(a+b)+gamma+range(alpha), relaxed.
M=4*(a+b)+gamma+max(alpha)-min(alpha)
def error(s):
    x=M*s
    assert 0<x<1
    return x**(order+1)/F(factorial(order+1))/(1-x)
eps1,eps2=error(t),error(2*t)
err_res=2*(N-1)*(eps1+(1+eps1)*eps2)
assert abs(Rpoly[0][0].i)>err_res
# Hence TRUE signed original depth-three residue at finite t is nonzero.

# Full P3 witness root current includes edges 01 AND 02; the
# H39 single-edge observer only measures j01. Quantify its omission.
j01=site_current(z1,z2,0,1)
j02=site_current(z1,z2,0,2)
assert Rpoly[0][0]==I*gc(j01+j02)
Jmax=max(a,b)
assert 12*Jmax*t<1
x=(32*Jmax*Jmax*t*t)
missing_bound=2*x*x/F(4)/(1-12*Jmax*t)
assert abs(j02)<=missing_bound
assert abs(Rpoly[0][0].i)>missing_bound+err_res
# The bound is from H36's all-time Dyson trace-tail with uneven path
# hopping |a|,|b|<=Jmax and arbitrary real onsite energies.

# Conditional FINITE-POSITIVE-TIME interrogation: during readout turn
# OFF right exchange & prep Stark, use ±a A with same gamma, and
# separately calibrated V_phi=diag(-i,1,1), attenuation q.
s=F(1,4)
q=F(3,4)
Dhat,Derr=certified_exp_D(a,gamma,s,18)
assert Dhat>Derr>0
for state in (rho1,rho2):
    contrast_plus=contrast_coeffs(state,a,gamma,10)
    transfer=transfer_coeffs(a,gamma,10)
    assert contrast_plus==[u*state[0][1].r for u in transfer]
    dressed=phase_dephase(state,q,-I)
    assert dressed[0][1].r==q*state[0][1].i
    contrast_y=contrast_coeffs(dressed,a,gamma,10)
    assert contrast_y==[u*q*state[0][1].i for u in transfer]
    assert dagger(dressed)==dressed
    assert trace(dressed)==O

# Artificial observation values are declared separately from the
# TRUE semigroup: η-bounded independent readout errors + D uncertainty.
eta=F(1,10**16)
def estimate(state,sign):
    Cx=Dhat*state[0][1].r +sign*eta
    Cy=Dhat*q*state[0][1].i-sign*eta
    return C(Cx/Dhat,Cy/(Dhat*q))
zhat=estimate(rho1,F(1))
what=estimate(rho2,F(-1))
jhat=2*(zhat*what.conj()).i
# Deterministic per-time coherence uncertainty (conservative),
# incorporating finite-time D calibration, contrast noise, and
# *certified full-semigroup preparation Taylor error*.
cal=(eta+Derr/F(2))/Dhat
e1=eps1+cal*(1+1/q)
e2=eps2+cal*(1+1/q)
j_error=e1+e2+2*e1*e2
assert abs(j01-jhat)<=j_error
assert abs(Rpoly[0][0].i-jhat)+err_res<=missing_bound+j_error+err_res
assert abs(jhat)>missing_bound+j_error+err_res
# This detects nonzero signed ROOT residue even when 02 coherence is
# not directly tomographed, but with extraordinarily accurate readings.
# It does NOT measure the FULL P3 R3 vector or entire current graph.

# Standard GKSL itself supplies all amplitudes, contrasts, and R:
# the declared CR static sector imposes no stricter independent
# experiment constraint here. Therefore no CR-exclusive signature.
print("PASS H40: independently declared radius-one P6-style J_static supports original real exchanges")
print("PASS H40: ONE fixed three-site GKSL Phi_t gives genuine P3 two-step signed R3 nonzero")
print("PASS H40: diagonal-gauge *-isomorphism intertwines generator, two steps, Delta and R")
print("PASS H40: population pinching fails exact two-step Markov/intertwiner at order t²")
print("PASS H40: SAME prepared states are read through finite-positive-time H39 coherent contrasts")
print("PASS H40: certified rational errors bound missing 02 current and signed root residue")
print("SCOPE: gauge equivalence is NOT independently derived P3/P6 physical provenance")
print("SCOPE: external Stark, phase/readout calibration and standard GKSL comparator remain required")
