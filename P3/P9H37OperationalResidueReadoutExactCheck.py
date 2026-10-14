"""H37: P3 residue's population-only no-go and calibrated-coherence readout gate.

All computations exact Fraction/Gaussian-rational. This is a *conditional*
standard-GKSL tomography protocol; the coherent X/Y measurement is an
EXTRA independently calibrated physical observer capability, NOT forced
by frozen P6's population observer/First-Residue Accessibility.
"""
from fractions import Fraction as F
from math import factorial
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H35GKSLLocalityTailExactCheck import N,jets,zeros,dagger,sc,tr
from P9H36OriginalP3QuadraticResidueSoftLocalityExactCheck import (
    sample,hidden,residual,divergence,suppress_far,
    rational_cutoff_bound
)
def vec_rho(co,t):
    return sample(co,t)
def conjugate_matrix(m):
    return [[m[a][b].conj() for b in range(N)] for a in range(N)]
def diagonal(m):
    return [m[a][a] for a in range(N)]
def X_expect(rho,a,b):
    # X_ab=E_ab+E_ba, tr(X_ab rho)=2Re rho_ab.
    assert a<b
    return rho[a][b]+rho[b][a]
def Y_expect(rho,a,b):
    # Y_ab=-iE_ab+iE_ba => tr(Y_ab rho)=-2 Im rho_ab.
    assert a<b
    return I*(rho[a][b]-rho[b][a])
def reconstructed_edge(rho,a,b):
    return (X_expect(rho,a,b)-I*Y_expect(rho,a,b))/2
def edge_j(z,w,a,b):
    assert a<b
    return F(2)*(z[a][b]*w[a][b].conj()).i
def all_currents(z,w):
    return {(a,b):edge_j(z,w,a,b) for a in range(N)
            for b in range(a+1,N)}
def from_currents(J):
    out=[F(0)]*N
    for (a,b),value in J.items():
        out[a]+=value;out[b]-=value
    return [I*gc(t) for t in out]
def l1_imag_diag(a):
    return sum((abs(a[v][v].i) for v in range(N)),F(0))
def mask_edges_to_radius(J,rad):
    return {(a,b):v for (a,b),v in J.items() if a<rad and b<rad}
def phase_gauge(rho,lam):
    return [[lam[a]*rho[a][b]*lam[b].conj()
             for b in range(N)] for a in range(N)]
def detuning_model_params():
    return F(1,2),F(2,3),(F(0),F(1,7),F(-1,9),F(2,11),F(-3,13))

J,gamma,v=detuning_model_params()
n=16;t=F(1,64)
# PLUS and MINUS Hamiltonians, same physical nonnegative site dephasing.
# H and -H are real-symmetric matrices. Complex conjugation maps
# their CPTP GKSL semigroups for real diagonal preparations.
plus=jets(J,gamma,v,n)
minus=jets(-J,gamma,tuple(-x for x in v),n)
assert all(minus[k]==conjugate_matrix(plus[k]) for k in range(n+1))
assert all(diagonal(minus[k])==diagonal(plus[k]) for k in range(n+1))
rho_p=vec_rho(plus,t);sigma_p=vec_rho(plus,2*t)
rho_m=vec_rho(minus,t);sigma_m=vec_rho(minus,2*t)
assert diagonal(rho_p)==diagonal(rho_m)
assert diagonal(sigma_p)==diagonal(sigma_m)
z_p=hidden(rho_p);w_p=hidden(sigma_p)
z_m=hidden(rho_m);w_m=hidden(sigma_m)
R_p=residual(z_p,w_p);R_m=residual(z_m,w_m)
assert R_m==sc(R_p,-1)
assert R_p==divergence(z_p,w_p)
assert R_p[0][0].i!=0
# Rigorous semigroup remainder for the nonzero signed residue:
M0=4*J+gamma+max(v)-min(v)
assert 2*M0*t<1
eps1=(M0*t)**(n+1)/F(factorial(n+1))/(1-M0*t)
eps2=(2*M0*t)**(n+1)/F(factorial(n+1))/(1-2*M0*t)
# Physical semigroups are PSD of trace 1, so each |rho_uv|<=1/2.
# 2*(N-1)*(eps1+(1+eps1)*eps2) is a conservative residue error.
error_site=2*(N-1)*(eps1+(1+eps1)*eps2)
assert abs(R_p[0][0].i)>error_site
# Thus true infinite semigroup signed R is nonzero and opposite
# under H->-H, despite EXACT equality of populations at ALL times.
# (All-time equality follows from conjugation covariance, not from
# finite Taylor agreement.)
assert tr(R_p)==Z0 and dagger(R_p)==sc(R_p,-1)

# Hermitian hidden entries are fully recovered from two quadratures
# measured on separately prepared copies at t and 2t.
for k in range(n+1):
    assert plus[k]==dagger(plus[k])
for a in range(N):
    for b in range(a+1,N):
        assert reconstructed_edge(rho_p,a,b)==z_p[a][b]
        assert reconstructed_edge(sigma_p,a,b)==w_p[a][b]
j_exact=all_currents(z_p,w_p)
assert from_currents(j_exact)==diagonal(R_p)

# A common site-phase change is a representation gauge of all
# measured coherences at BOTH times, leaving j and R unchanged.
lambdas=(O,C(F(3,5),F(4,5)),I,
         C(F(5,13),F(12,13)),-O)
assert all(x*x.conj()==O for x in lambdas)
zg=phase_gauge(z_p,lambdas)
wg=phase_gauge(w_p,lambdas)
assert all_currents(zg,wg)==j_exact
assert residual(zg,wg)==R_p
# Uncalibrated drift between t and 2t measurements is different:
# it can change the inferred j even if populations stay unchanged.
drift=(I,O,O,O,O)
w_drift=phase_gauge(w_p,drift)
assert all(diagonal(phase_gauge(sigma_p,drift))[u]==sigma_p[u][u] for u in range(N))
assert all_currents(z_p,w_drift)!=j_exact

# Independent phase-calibrated X/Y tomography, each expectation
# with a declared absolute error <=eta, gives complex-entry errors
# <=eta for each preparation; use a worst-case rational example.
eta=F(1,10000)
def noisy_reconstruction(rho,a,b,offset):
    # Errors +-eta in the real X/Y expectation, bounded
    # independently of signal amplitude.
    x=X_expect(rho,a,b)+gc(eta if offset%2==0 else -eta)
    y=Y_expect(rho,a,b)+gc(-eta if offset%3==0 else eta)
    assert x.i==0 and y.i==0
    return (x-I*y)/2
def empirical_currents(rad):
    out={}
    for a in range(rad):
        for b in range(a+1,rad):
            ze=noisy_reconstruction(rho_p,a,b,a+b)
            we=noisy_reconstruction(sigma_p,a,b,a+2*b)
            assert (ze-z_p[a][b])*(ze-z_p[a][b]).conj()<=gc(eta*eta)
            assert (we-w_p[a][b])*(we-w_p[a][b]).conj()<=gc(eta*eta)
            out[(a,b)]=F(2)*(ze*we.conj()).i
    return out
# Uncertainty from polynomial replacement also accounted for
# via eps1/eps2; estimates are within eta+eps_s of TRUE rho entries.
ez=eta+eps1;ew=eta+eps2
per_edge=ez+ew+2*ez*ew
for rad in range(1,N+1):
    hat=from_currents(empirical_currents(rad))
    err=sum((abs(R_p[u][u].i-hat[u].i) for u in range(N)),F(0))
    E=rad*(rad-1)//2
    # Actual semigroup residue differs from R_p by <=N*error_site.
    # Cutoff true-residue norm bounded by H36; tomography noise:
    # one edge current affects two vertices, hence factor 2.
    upper=rational_cutoff_bound(rad,t,J) if rad<N else F(0)
    upper+=2*E*per_edge
    assert err+N*error_site<=upper,(rad,err,N*error_site,upper)

# Algebraic incidence nullspace: on full hidden COMPLETE edge graph
# K5, the map from 10 edge currents to 5 divergences has cycle rank 6.
edges=[(a,b) for a in range(N) for b in range(a+1,N)]
def divergence_real(curr):
    out=[F(0)]*N
    for (a,b),val in curr.items():
        out[a]+=val;out[b]-=val
    return out
cycle=dict.fromkeys(edges,F(0))
cycle[(0,1)]=F(1);cycle[(0,2)]=F(-1);cycle[(1,2)]=F(1)
assert divergence_real(cycle)==[F(0)]*N
shifted={e:j_exact[e]+cycle[e] for e in edges}
assert shifted!=j_exact
assert divergence_real(shifted)==divergence_real(j_exact)
# Equality of original signed P3 residue cannot determine hidden
# cycle currents, let alone interface Wilson holonomy.
assert len(edges)-N+1==6

# Algebraic scale: bounds require independent calibration, not merely
# P6 population-only control or the site-dephasing rate.
print("PASS H37: exact all-time population indistinguishability H versus -H under same GKSL dephasing")
print("PASS H37: opposite nonzero signed ORIGINAL P3 R3 witness with rigorous rational remainder")
print("PASS H37: two phase-calibrated X/Y quadratures reconstruct hidden pairs and edge currents")
print("PASS H37: common site gauge preserves j/R; uncalibrated relative phase drift changes inferred j")
print("PASS H37: certified local readout trace-norm error = H36 cutoff + explicit tomography term")
print("PASS H37: equal divergence permits nonzero hidden cycle-current differences")
print("SCOPE: coherent quadrature observer/readout and physical P6 provenance are ADDITIONAL assumptions")
