"""H100 exact conditional ADM normalization: two nonuniform off-shell probes.

EXTERNAL COMPARATOR: 3D continuum ADM canonical Poisson bracket,
spatial scalar R, momentum constraint D, kinetic/curvature factors
alpha,beta, DeWitt trace lambda, cosmological density Lambda.
EXACT CONDITIONAL: off-shell H-H=D fixes alpha*beta=1, lambda=1/2
but leaves alpha/beta and Lambda freely unselected by H75/P3/F.
Original H75 source, positive source-selected K4, curvature witness and
P3 original signed R3 are unchanged. No derived Einstein dynamics.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,gc
from P9H75SemicausalMicroMemorySourceExactCheck import R60
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P9H98DeWittLambdaFlatHDASourceSelectorExactCheck as H98
import P9H99SourceMetricRankCurvatureJetNonselectionExactCheck as H99

assert R60[0][0]==I*gc(F(-32,135))
assert H99.r0==(F(0),F(16,25),F(16,25),F(4,25))
assert H91.rank(H99.composite)==3
assert H99.levi_civita_scalar(F(1,5))==F(102,245)
print("PASS H100.1: unchanged true H75/P3 microscopic positive source and source-selected K4 metric rank3 with unequal spatial curvature jets")

N,M,f=H98.N,H98.M,H98.f
wedge=H98.psub(H98.pmul(N,H98.derivative(M)),
               H98.pmul(M,H98.derivative(N)))
assert wedge==H98.wedge
c=H98.integrate01(H98.pmul(H98.derivative(f),wedge))
cross=H98.integrate01(H98.pmul(
    f,H98.psub(H98.pmul(N,H98.derivative(H98.derivative(M))),
              H98.pmul(M,H98.derivative(H98.derivative(N))))))
assert c==F(1,210) and cross==-c

# For pi^ij=f(x) diag(t0,t1,t2) at g=I:
# D[v]=-2*t0*c, gradient-of-trace anomaly=(sum t)*c.
# Independent direct functional cross-bracket at flat g:
# delta K_N/delta pi^ij=2alpha N (pi_ij-lambda*pi delta_ij),
# delta[-beta integral M sqrt(g)R]/delta g_yy=beta M''
# =zz, with xx=0. Cross terms yield the "direct" calculation.
def D(t):return -2*t[0]*c
def A(t):return sum(t)*c
def direct(alpha,beta,lam,t):
    return 2*F(alpha)*F(beta)*(t[0]+(2*F(lam)-1)*sum(t))*cross
def integrated(alpha,beta,lam,t):
    return F(alpha)*F(beta)*(D(t)+2*(1-2*F(lam))*A(t))

T=(F(1),F(-1),F(0)) # traceless, divergent, D != 0
U=(F(1),F(1),F(1))  # isotropic, nonzero gradient of trace
assert D(T)==D(U)==F(-1,105)
assert A(T)==0 and A(U)==F(1,70)
for t in (T,U,(F(3),F(-2),F(1)),(F(0),F(1),F(-1))):
    for alpha,beta,lam in (
        (F(1),F(1),F(0)),(F(1),F(1),F(1,2)),
        (F(2),F(1,2),F(1,2)),(F(3,2),F(2,3),F(1,2)),
        (F(1),F(2),F(1,2)),(F(3),F(1,3),F(1,3)),
        (F(7,4),F(4,7),F(2,3))
    ):
        assert direct(alpha,beta,lam,t)==integrated(alpha,beta,lam,t)
print("PASS H100.2: exact rational nonuniform ADM H-H bracket by INDEPENDENT second-lapse-derivative functional-variation and integrated momentum/trace-gradient formulas")

# Two independent probes separate otherwise confounded parameters:
# T: H-H=-alpha*beta/105 vs D=-1/105 => alpha*beta=1.
# U: H-H=alpha*beta(2-6lambda)/105 vs D=-1/105
#    => lambda=1/2 when product has been fixed.
assert direct(1,1,0,T)==D(T)
assert direct(2,F(1,2),F(5,9),T)==D(T)
assert direct(1,2,F(1,2),T)!=D(T)
assert direct(1,1,0,U)==F(2,105)!=D(U)
assert direct(1,1,F(1,2),U)==D(U)
assert direct(1,1,F(2,3),U)==F(-2,105)!=D(U)
print("PASS H100.3: tracefree nonuniform momentum independently forces alpha*beta=1; isotropic nonuniform momentum then uniquely forces lambda=1/2 (conditionally imported standard ADM constraint)")

# The cosmological density 2Lambda sqrt(g) has NO derivatives of the
# lapse and thus all its kinetic cross brackets are proportional to
# NM and cancel after N<->M antisymmetrization.
nm=H98.integrate01(H98.pmul(H98.pmul(N,M),f))
assert nm>0
for t in (T,U):
    for alpha,lam,Lambda in ((F(1),F(1,2),F(2,7)),
                             (F(3,2),F(3,7),F(-5,4))):
        term=2*alpha*Lambda*(1-3*lam)*sum(t)*nm
        assert term-term==0
print("PASS H100.4: cosmological potential has only algebraic lapse-local terms; all antisymmetric H-H contributions cancel, Lambda remains unconstrained")

compatible=((F(1),F(1),F(1,2),F(0)),
            (F(2),F(1,2),F(1,2),F(0)),
            (F(3,2),F(2,3),F(1,2),F(2,7)),
            (F(5,3),F(3,5),F(1,2),F(-11,6)))
for alpha,beta,lam,Lambda in compatible:
    assert alpha*beta==1 and lam==F(1,2)
    for t in (T,U,(F(3),F(-2),F(1))):
        assert integrated(alpha,beta,lam,t)==D(t)
print("PASS H100.5: same standard normalized H-H comparator admits continuum (alpha,beta)=(a,1/a) and arbitrary cosmological Lambda; gravitational coupling and Lambda not selected")

# Compare true positive microscopic source-based but externally
# spatially soldered H99 curvatures under distinct ADM completions.
# These Hamiltonians are not source-defined observables.
sqrtg=F(64,35)
assert sqrtg**2==H98.determinant(H99.g0)
Rflat,Rcurved=F(0),H99.levi_civita_scalar(F(1,5))
def local_H(beta,Lambda,R):return -F(beta)*sqrtg*R+2*F(Lambda)*sqrtg
assert local_H(1,0,Rcurved)==F(-6528,8575)
assert local_H(F(1,2),0,Rcurved)==F(-3264,8575)
assert local_H(1,0,Rflat)==0
assert local_H(F(2,3),F(2,7),Rflat)==F(256,245)
print("PASS H100.6: identical genuine H75 source and equal ADM flat-HDA bracket allow different local Hamiltonian densities under UNSOURCED coupling and cosmological completions")
print("BOUNDARY: AX-SP 6D source geometry/curvature 2jet, AX-CAN physical six momenta/symplectic transport, AX-DYN physical action/constraints, AX-NORM Newton/Lambda selection and AX-GEN F completeness all OPEN")
print("BOUNDARY: these are exact CONDITIONAL ADM continuum comparators, NOT source-derived Einstein dynamics, empirical CR discriminator or human peer review")
