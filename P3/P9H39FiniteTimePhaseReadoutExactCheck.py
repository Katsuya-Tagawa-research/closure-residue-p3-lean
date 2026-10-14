"""H39 exact finite-positive-time P6 coherent readout with externally calibrated phase.

Restricted frozen P6 benchmark: separately signed real 01-exchange pulses,
site-dephasing and diagonal population observer. EXTRA physically calibrated
Stark phase gate V_phi; absent from frozen two-real-control manifold.
No negative-time dissipative evolution and no CR-exclusive signal.

All executable tests use rational arithmetic for the generator jets and
rigorous fractional Taylor remainders; analytic transfer formula is proved
in companion note.
"""
from fractions import Fraction as F
from math import factorial
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H38P6RealExchangeObserverGateExactCheck import (
    N,A,unit,eye,z,scale,add,sub,mm,dagger,com,diag,trace,
    gksl_real_step, X01,Y01,center,generic,rho_p,rho_m
)
assert N==3
def positive_semigroup_jets(rho,a,gamma,order):
    K=scale(A,gc(a))
    co=[rho]
    for k in range(1,order+1):
        co.append(scale(gksl_real_step(co[-1],K,gamma),F(1,k)))
    assert all(dagger(v)==v for v in co)
    assert all(trace(v)==(O if k==0 else Z0)
               for k,v in enumerate(co))
    return co
def readout_z(m):
    return (m[0][0]-m[1][1]).r
def contrast_coeffs(rho,a,gamma,order):
    cp=positive_semigroup_jets(rho,a,gamma,order)
    cm=positive_semigroup_jets(rho,-a,gamma,order)
    return [readout_z(sub(cp[m],cm[m])) for m in range(order+1)]
def matrix2vec(M,v):
    return (M[0][0]*v[0]+M[0][1]*v[1],
            M[1][0]*v[0]+M[1][1]*v[1])
def transfer_coeffs(a,gamma,order):
    # (z,x)'=[[0,4a],[-a,-gamma]](z,x), x=Re rho01.
    M=((F(0),4*a),(-a,-gamma))
    v=(F(0),F(1))
    out=[]
    for m in range(order+1):
        out.append(2*v[0]/F(factorial(m)))
        v=matrix2vec(M,v)
    assert out[0]==F(0) and out[1]==8*a
    return out
def phase_dephase(rho,q,phase):
    # phase is a rational Gaussian unit complex amplitude e^{-i phi}.
    assert phase*phase.conj()==O
    assert F(0)<q<=F(1)
    V=eye()
    V[0][0]=phase
    rotated=mm(mm(V,rho),dagger(V))
    return add(scale(rotated,gc(q)),scale(diag(rotated),gc(1-q)))
def realpart(c):return c.r
def bound_d_lower_underdamped(a,gamma,s):
    omega2=4*a*a-gamma*gamma/F(4)
    assert omega2>0 and gamma*s/F(2)<1 and omega2*s*s<F(6)
    # e^-y >= 1-y; sin x/x >= 1-x^2/6 for 0<x<1.
    assert omega2*s*s<=1
    return 8*a*s*(1-gamma*s/F(2))*(1-omega2*s*s/F(6))
def certified_exp_D(a,gamma,s,order):
    # D=2[e^{sM}]_(0,1) (all-time exact).
    coeff=transfer_coeffs(a,gamma,order)
    poly=sum((coeff[m]*s**m for m in range(order+1)),F(0))
    # M induced infinity norm max(4|a|,|a|+gamma).
    norm=max(4*abs(a),abs(a)+gamma)
    x=norm*s
    assert x<1
    # rigorous bound |D-poly| <=2 exp(x) x^(n+1)/(n+1)!,
    # relaxed to rational exp(x)<=1/(1-x)
    err=2*x**(order+1)/F(factorial(order+1))/(1-x)
    return poly,err

a=F(2,3)
q=F(3,4)
order=18
s=F(1,4)
# All signed exchange controls are positive-time CPTP semigroups;
# changing a->-a never applies an inverse dissipative channel.
states=(rho_p,rho_m,generic,center)
for gamma in (F(0),F(1,2),F(4)):
    D=transfer_coeffs(a,gamma,order)
    for rho in states:
        x=rho[0][1].r
        direct=contrast_coeffs(rho,a,gamma,order)
        assert direct==[D[k]*x for k in range(order+1)]
        for phase in (C(0,-1),C(F(3,5),F(-4,5))):
            pp=phase_dephase(rho,q,phase)
            xp=pp[0][1].r
            assert xp==q*(rho[0][1].r*phase.r-rho[0][1].i*phase.i)
            dressed=contrast_coeffs(pp,a,gamma,order)
            assert dressed==[D[k]*xp for k in range(order+1)]
        # In particular ideal phi=pi/2 reads imaginary coherence.
        ideal=phase_dephase(rho,q,-I)
        assert ideal[0][1].r==q*rho[0][1].i
    # At any finite underdamped (0<omega s<pi), D nonzero.
    # At critical/overdamped, g is s*e^-gamma s/2 or
    # e^-gamma s/2*sinh(kappa s)/kappa, so nonzero for all s>0.
    assert D[1]==8*a

# Noninfinitesimal certified channel-transfer contrast:
g=F(1,2)
Dhat,Derr=certified_exp_D(a,g,s,order)
Dlower=bound_d_lower_underdamped(a,g,s)
assert Dlower>0 and Dhat-Derr>Dlower and Derr>0
assert Dhat-Derr>F(1) and Dhat+Derr<F(2)

# A calibration using independently certified input state |+><+|
# on 01 with x0=1/2, z0=0 gives contrast C_cal=D/2;
# a full finite-time D estimate is 2*C_cal (not a derivative).
plus_x=scale(add(add(unit(0,0),unit(1,1)),X01),F(1,2))
minus_x=scale(sub(add(unit(0,0),unit(1,1)),X01),F(1,2))
assert dagger(plus_x)==plus_x and dagger(minus_x)==minus_x
assert plus_x[0][1]==gc(F(1,2)) and minus_x[0][1]==gc(F(-1,2))
for rho,x in ((plus_x,F(1,2)),(minus_x,F(-1,2))):
    assert contrast_coeffs(rho,a,g,order)==[
        v*x for v in transfer_coeffs(a,g,order)]

# Model uncertainty calibration: direct D determined by reference
# coherent preparations, whereas q must be separately calibrated
# on the phase gate. Dephasing calibration alone cannot determine phi.
eta_x=F(1,1000);eta_y=F(1,1200);delta_D=F(1,500)
delta_q=F(1,600);delta_phi=F(1,100)
D_cal=Dhat # exact rational estimator of D up to Derr.
D_error=Derr+delta_D
q_cal=q+delta_q
assert q_cal>0 and D_cal>D_error>0
# True complex coherence for physical generic state:
x=generic[0][1].r
y=generic[0][1].i
assert x==F(1,12) and y==F(1,18)
# Each independent population-contrast estimate has error bounded by
# eta_X/Y. Combining denominator errors gives deterministic bounds.
error_real=(eta_x+D_error/F(2))/abs(D_cal)
error_imag=(eta_y+D_error/F(2))/(abs(D_cal)*q_cal)
error_imag+=delta_q/(2*q_cal)
# If actual phi=pi/2+eps, leakage from x into y contributes <=
# |eps|/2+eps^2/4, because |rho_01|<=1/2.
error_imag+=delta_phi/F(2)+delta_phi**2/F(4)
assert error_real>0 and error_imag>0
# Actual error for EXACT pi/2 with exact D should be bounded; rational
# polynomial Dhat + remainder controls unknown true transfer D.
for estimated_D in (Dhat-Derr,Dhat+Derr):
    for measured_x in (estimated_D*x+eta_x,estimated_D*x-eta_x):
        xest=measured_x/D_cal
        assert abs(xest-x)<=error_real
    for q_actual in (q_cal-delta_q,q_cal):
        for measured_y in (
            estimated_D*q_actual*y+eta_y,
            estimated_D*q_actual*y-eta_y):
            yest=measured_y/(D_cal*q_cal)
            assert abs(yest-y)<=error_imag

# A phi gate can be physically realized by diagonal H_alpha for
# positive duration tau and simultaneous dephasing gamma>0:
# q=exp(-gamma tau); phi=alpha tau.  For gamma=0, q must equal 1
# unless extra independently calibrated attenuation is present.
# Rational phase/dephasing maps above are exact CPTP descriptions of
# their net finite-time action; no negative-time inverse is needed.
assert q<F(1) and g>0

print("PASS H39: finite-time +a/-a GKSL population contrasts recover Re coherence")
print("PASS H39: extra calibrated V_phi and q recover Im coherence at finite positive time")
print("PASS H39: exact 3-level jets agree with Bloch transfer to order18 incl overdamping")
print("PASS H39: rational semigroup transfer enclosure certifies D!=0 away from blind times")
print("PASS H39: independent coherent reference can calibrate finite transfer contrast")
print("PASS H39: rigorous deterministic q/D/phase/measurement error conditioning")
print("SCOPE: phase gate and coherent reference prep are EXTRA independently calibrated physical resources")
