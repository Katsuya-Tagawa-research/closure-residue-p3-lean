"""H38: exact P6 REAL exchange observer gate vs calibrated diagonal phase resource.

P6's *specific* frozen 3-site benchmark only declares two real path
exchange generators K=a(E01-E10)+b(E21-E12), diagonal population readout.
All real-orthogonal exchange pulses and calibrated pure site dephasing
preserve the real-symmetric / imaginary-skew decomposition.

Original P3 residue from any diagonal seed is identically zero in
this restricted baseline, at EVERY Krylov depth. Extra independently
calibrated diagonal coherent phase is sufficient for the missing Y
quadrature, but is NOT part of the original physical target controls.

Exact Gaussian rationals; ordinary CPTP/GKSL, not a CR-only prediction.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    N, unit, z, eye, scale, add, sub, mm, dagger, com, diag,
    hidden, trace, rr
)
assert N==3
def iszero(a):return a==z()
def transp(a):return [[a[j][i] for j in range(N)] for i in range(N)]
def conj(a):return [[a[i][j].conj() for j in range(N)] for i in range(N)]
def dephase(a,q):
    # q*rho+(1-q)*Delta_D(rho) is CPTP for rational 0<=q<=1.
    assert F(0)<=q<=F(1)
    return add(scale(a,gc(q)),scale(diag(a),gc(1-q)))
def unitary_channel(u,rho):return mm(mm(u,rho),dagger(u))
def diagonal_values(a):return [a[i][i] for i in range(N)]
def ortho_edge(a,b,c,s):
    # Real rotation on ab: block [[c,s],[-s,c]], c^2+s^2=1.
    c=gc(c);s=gc(s)
    assert c*c+s*s==O
    u=eye()
    u[a][a]=c;u[b][b]=c;u[a][b]=s;u[b][a]=-s
    assert transp(u)==dagger(u)
    assert mm(transp(u),u)==eye()
    return u
A=sub(unit(0,1),unit(1,0))
B=sub(unit(2,1),unit(1,2))
X01=add(unit(0,1),unit(1,0))
Y01=scale(A,-I) # Hermitian Y=-i(E01-E10)
assert dagger(A)==scale(A,-1)
assert dagger(B)==scale(B,-1)
assert transp(A)==scale(A,-1)
assert transp(B)==scale(B,-1)
assert dagger(X01)==X01 and dagger(Y01)==Y01
assert diag(com(X01,Y01))==scale(sub(unit(0,0),unit(1,1)),gc(2)*I)

# Density witnesses rho_±=I_3/3±(i/6)(E01-E10).
# Eigenvalues exactly (1/6,1/3,1/2), so positive.
center=scale(eye(),F(1,3))
delta=scale(A,I/F(6))
rho_p=add(center,delta)
rho_m=sub(center,delta)
assert dagger(rho_p)==rho_p and dagger(rho_m)==rho_m
assert trace(rho_p)==trace(rho_m)==O
assert diagonal_values(rho_p)==diagonal_values(rho_m)==[gc(F(1,3))]*3
assert delta[0][1]==I/F(6)
assert rho_p[0][0]*rho_p[1][1]-rho_p[0][1]*rho_p[1][0]==gc(F(1,12))
assert rho_p[2][2]==gc(F(1,3))
assert rho_m==conj(rho_p)
rot01=ortho_edge(0,1,F(3,5),F(4,5))
rot12=ortho_edge(1,2,F(5,13),F(12,13))
rot10=transp(rot01)
for state in (rho_p,rho_m):
    assert dagger(state)==state
    assert all(state[i][i].i==0 for i in range(N))

# Every physically legitimate finite sequence composed of real exchange
# rotations + independently calibrated q-pinching has identical
# diagonal readout on states differing only by a pure imaginary skew.
# Proof: real channel maps real symmetric -> real symmetric and imaginary
# skew -> imaginary skew with vanishing diagonal, even with site dephasing.
u_seq=[rot01,rot12,rot10,rot12,rot01]
q_seq=[F(2,3),F(3,5),F(4,5),F(1),F(5,7)]
p=rho_p;m=rho_m
for u,q in zip(u_seq,q_seq):
    p=dephase(unitary_channel(u,p),q)
    m=dephase(unitary_channel(u,m),q)
    assert m==conj(p)
    assert diagonal_values(p)==diagonal_values(m)
    assert all(t.i==0 for t in diagonal_values(p))
    assert dagger(p)==p and dagger(m)==m and trace(p)==trace(m)==O
assert p!=m

# More stringent ORIGINAL P3 statement for the restricted real model:
# K=a A+b B, and every generator step [K,.]+gamma(Delta-I)
# preserves real symmetric hidden Hermitian iterates from any real
# diagonal seed. Their complex span is complex symmetric; the diagonal
# of commutator of any two complex symmetric matrices is IDENTICALLY 0.
def gksl_real_step(rho,K,gamma):
    assert dagger(K)==scale(K,-1) and transp(K)==scale(K,-1)
    return sub(com(K,rho),scale(hidden(rho),gc(gamma)))
K=add(scale(A,F(2,3)),scale(B,F(5,4)))
for gamma in (F(0),F(2,3),F(5,4)):
    for seed in (unit(0,0),unit(1,1),unit(2,2)):
        jets=[seed]
        for k in range(1,9):
            jets.append(gksl_real_step(jets[-1],K,gamma))
        hidden_jets=[hidden(v) for v in jets]
        for u in hidden_jets:
            assert transp(u)==u and conj(u)==u
        for u in hidden_jets:
            for v in hidden_jets:
                assert diag(com(u,dagger(v)))==z()
# Hence every original P3 depth-k residue subspace of Phi_t
# constructed from diagonal inputs is zero at ALL k for real-exchange
# plus dephasing dynamics (analyticity propagates this invariant sector).

# Accessible X quadrature: derivative of population p0 under A.
def exch_slope(rho):
    return com(A,rho)[0][0]
for state in (rho_p,rho_m):
    assert exch_slope(state)==gc(2)*state[0][1].r
    assert exch_slope(state)==Z0
# A generic Hermitian state with real and imaginary coherences:
generic=add(center,add(scale(X01,F(1,12)),scale(Y01,F(-1,18))))
assert dagger(generic)==generic
assert generic[0][1]==C(F(1,12),F(1,18))
assert (generic[0][0]*generic[1][1]-
        generic[0][1]*generic[1][0])==C(F(1,9)-F(1,144)-F(1,324))
assert exch_slope(generic)==gc(F(1,6))

# Sufficient EXTRA CPTP RESOURCE: a phase-calibrated diagonal unitary
# V=diag(-i,1,1) plus calibrated q dephasing; the phase shift turns
# Im rho01 into Re rho01. This is NOT derivable from two real P6
# exchange knobs or from site-dephasing calibration alone.
phase=eye();phase[0][0]=-I
assert mm(dagger(phase),phase)==eye()
def phase_dephase(state,q):
    return dephase(unitary_channel(phase,state),q)
q=F(2,3)
assert phase_dephase(rho_p,q)[0][1]==gc(q/F(6))
assert phase_dephase(rho_m,q)[0][1]==gc(-q/F(6))
assert exch_slope(phase_dephase(rho_p,q))==gc(q/F(3))
assert exch_slope(phase_dephase(rho_m,q))==gc(-q/F(3))
for state in (rho_p,rho_m,generic):
    x=exch_slope(state)
    y=exch_slope(phase_dephase(state,q))
    assert x.i==0 and y.i==0
    assert x.r/2==state[0][1].r
    assert y.r/(2*q)==state[0][1].i
# The gamma-dephasing term has zero population derivative, so the
# infinitesimal switch-on response remains exact in the GKSL model.
for gamma in (F(0),F(3,5),F(5,4)):
    assert gksl_real_step(generic,A,gamma)[0][0]==exch_slope(generic)
    assert gksl_real_step(phase_dephase(generic,q),A,gamma)[0][0]==exch_slope(
        phase_dephase(generic,q))

# Calibration/measurement conditioning: if two measured population
# slopes have abs errors <=eta_x, eta_y, and exchange scale a!=0,
# then |delta Re rho01| <= eta_x/(2|a|),
# |delta Im rho01| <= eta_y/(2|a| q).
a=F(2,3);eta_x=F(1,1000);eta_y=F(1,2000)
slope_x=a*exch_slope(generic)
slope_y=a*exch_slope(phase_dephase(generic,q))
observed_x=slope_x+gc(eta_x)
observed_y=slope_y-gc(eta_y)
rec_re=observed_x.r/(2*a)
rec_im=observed_y.r/(2*a*q)
assert abs(rec_re-generic[0][1].r)==eta_x/(2*a)
assert abs(rec_im-generic[0][1].i)==eta_y/(2*a*q)

# An extra independently calibrated diagonal Hamiltonian is also
# exactly what releases a nonzero LEADING original-P3 depth-three
# quadratic residue from diagonal preparations (cf P9.38 +2i Lw a).
# Fix frozen P6 real coherent exchange K, with independent detuning
# alpha; the pure real-exchange witness vanishes, but alpha != const
# creates an imaginary-skew second hidden jet and its commutator.
def Lalpha(rho,K,gamma,alpha):
    h=diag_from(alpha)
    return sub(gksl_real_step(rho,K,gamma),scale(com(h,rho),I))
def diag_from(a):
    v=z()
    for k,t in enumerate(a):v[k][k]=gc(t)
    return v
def threejet_residue(alpha,gamma):
    d=unit(0,0)
    l1=Lalpha(d,K,gamma,alpha)
    l2=Lalpha(l1,K,gamma,alpha)
    ah=hidden(l1);bh=hidden(l2)
    return diag(com(ah,bh))
for gamma in (F(0),F(2,3),F(5,4)):
    assert threejet_residue((F(0),F(0),F(0)),gamma)==z()
    av=(F(1,7),F(0),F(0))
    predicted=scale(sub(unit(0,0),unit(1,1)),
                    gc(2)*(F(2,3)**2)*I*gc(F(1,7)))
    assert threejet_residue(av,gamma)==predicted

print("PASS H38: population-only measurement cannot see imaginary coherence under ANY real-exchange/dephasing circuit")
print("PASS H38: genuine original-P3 residue subspaces vanish for diagonal-prepared real P6 exchange model")
print("PASS H38: real exchange population slope exactly reads Re of an allowed edge coherence")
print("PASS H38: independently calibrated diagonal phase+dephasing CPTP gate unlocks Im readout")
print("PASS H38: tomography conditioning and independent q calibration factors explicit")
print("PASS H38: added diagonal Stark detuning creates nonzero leading original-P3 cubic witness")
print("SCOPE: Stark phase gate is EXTRA physical control; frozen P6 device accessibility remains OPEN")
