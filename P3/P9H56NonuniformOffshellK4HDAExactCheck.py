"""H56: nonuniform OFF-SHELL ADM HDA pulled back to the local K4
positive-edge canonical chart; exact cone failure under fixed-solder
finite coordinate shear; strictly distinct from CR/KKS origin.

EXTERNAL premises: C4 smooth spatial 3-manifold, soldered K4 metric
g=16 G B(w)^-1 G, ADM action, symplectic structure, lapse, shift,
compactly supported smearing variations / valid boundary terms.

Main exact H-H local divergence identity on arbitrary NONUNIFORM
metric/momentum/smearing jets, with NONZERO constraints (OFF SHELL):
  2 pi^ij (N nabla_i nabla_j M - M nabla_i nabla_j N)
   = beta^i H_i + partial_i[2 pi^ij (N partial_j M-M partial_j N)]
where beta^i=g^ij(N partial_j M - M partial_j N).
After integrating a legitimate vanishing boundary flux:
  {H[N],H[M]}=D[beta].
Also checks metric Lie derivative representation of D-D, kinetic
Hamiltonian density transformation for D-H, and full six-coordinate
canonical cotangent lift. THESE inherit standard ADM HDA; they do NOT
derive Einstein dynamics from P3/P4 or KKS.

All exact fractions, no random sampling or numeric tolerances.
"""
from fractions import Fraction as F
from P9H52K4DeWittKinematicsCurvatureExactCheck import (
    I,zeros,add,scale,mm,trans,trace,inv,det,rank,B,G,V,
    flatten_symmetric,cov_metric,positive_definite
)
from P9H53K4SolderedSpatialCurvatureExactCheck import (
    metric_jets,levi_civita_curvature
)
from P9H55K4ADMCanonicalChartExactCheck import (
    Jmatrix,p_of,pi_of,solve_weights,lie_metric,
    tensor_contract,hamiltonian_kin
)
n=3
ZERO=F(0)
def sub(A,B):return add(A,scale(B,F(-1)))
def mdot(x,y):return sum((a*b for a,b in zip(x,y)),ZERO)
def contract(A,C):return sum((A[i][j]*C[i][j]
                              for i in range(n) for j in range(n)),ZERO)
def mv(A,x):
    return [sum((A[i][j]*x[j] for j in range(n)),ZERO)
            for i in range(n)]
def mat_flat(g):return flatten_symmetric(g)
def mat_linear_combo(v,A):
    R=zeros(n,n)
    for x,M in zip(v,A):R=add(R,scale(M,x))
    return R
def standard_j(w):
    return [ [flatten_symmetric(
        scale(mm(mm(mm(mm(G,inv(B(w))),V[e]),inv(B(w))),G),
              F(-16)))[k]
          for e in range(6)] for k in range(6)]
def weight_from_cov_metric(g):
    # Exact inverse to the six-weight K4 response chart in fixed
    # physical coordinate solder/frame.
    mat=scale(mm(mm(G,inv(g)),G),F(16))
    coeff=[[mat_flat(V[e])[k] for e in range(6)]
           for k in range(6)]
    cols=mv6(inv(coeff),mat_flat(mat))
    return cols
def mv6(A,x):
    return [sum((A[i][j]*x[j] for j in range(6)),ZERO)
            for i in range(6)]

w=(F(1),)*6
g=cov_metric(w)
assert g==scale(G,F(4)) and det(g)==F(256)
assert standard_j(w)==Jmatrix(w)
assert weight_from_cov_metric(g)==list(w)

# H56.1: a finite, valid, orientation-preserving spatial COORDINATE
# shear sends a strictly positive K4 chart point to the boundary
# exterior if one insists on the SAME fixed physical solder chart.
Q=[[F(1),F(1,2),F(0)],
   [F(0),F(1),F(0)],
   [F(0),F(0),F(1)]]
assert det(Q)==1
gprime=mm(mm(trans(Q),g),Q)
assert positive_definite(gprime) and det(gprime)==det(g)
wprime=weight_from_cov_metric(gprime)
assert wprime==[F(5,2),F(1,2),F(7,4),F(1),F(-1,2),F(3,2)]
assert wprime[4]<0 and all(t>0 for t in w)
assert cov_metric(wprime)==gprime
# Covariant transformation of the EXTERNAL solder/frame returns
# to the original g in the original physical coordinate chart.
Qinv=inv(Q)
assert mm(mm(trans(Qinv),gprime),Qinv)==g
assert weight_from_cov_metric(mm(mm(trans(Qinv),gprime),Qinv))==list(w)
# Infinitesimal shear remains in the open positive cone locally:
X=[[F(0),F(1),F(0)],[F(0),F(0),F(0)],[F(0),F(0),F(0)]]
LieQ=add(mm(trans(X),g),mm(g,X))
dwQ=solve_weights(w,LieQ)
assert mat_linear_combo(dwQ,[scale(mm(mm(mm(mm(G,inv(B(w))),V[e]),
                       inv(B(w))),G),F(-16)) for e in range(6)])==LieQ
assert any(dwQ)
# Canonical ADM phase-space chart is a local diffeomorphism,
# NOT invariant as a single globally positive K4 coordinate patch.
pi=[[F(2),F(1,3),F(-1,5)],
    [F(1,3),F(-3,2),F(2,7)],
    [F(-1,5),F(2,7),F(4,3)]]
p=p_of(pi,w)
assert pi_of(p,w)==pi
assert mdot(p,dwQ)==contract(pi,LieQ)

# H56.2: genuinely NONUNIFORM positive weight jets (gradients
# nonzero), momentum-density jets and two nonconstant lapse tests.
w0=[F(1)]*6
wi=[[F((i+1)*(e%3-1),20) for e in range(6)]
    for i in range(n)]
wij=[[[F((i+j+2)*(1 if e%2 else -1),50)
       for e in range(6)] for j in range(n)] for i in range(n)]
gg,gi,gij=metric_jets(w0,wi,wij)
R,Ric,Ein,Gamma=levi_civita_curvature(gg,gi,gij)
assert gg==g and Gamma[0][0][0]==F(-1,40)
assert any(gi[i][j][k] for i in range(n)
           for j in range(n) for k in range(n))
dpi=[[[F((m+1)*(i+j+2),37)
        for j in range(n)] for i in range(n)] for m in range(n)]
assert all(t==trans(t) for t in dpi)
# lapses N(x), M(x) have independent values, gradients, Hessians:
N=F(3,2);M=F(5,3)
Ng=[F(1,3),F(-2,5),F(3,7)]
Mg=[F(2,9),F(1,4),F(-3,8)]
Nh=[[F((i+1)*(j+1),13) for j in range(n)]
    for i in range(n)]
Mh=[[F((i+2)*(j+2),17) for j in range(n)]
    for i in range(n)]
alpha=[N*Mg[i]-M*Ng[i] for i in range(n)]
ginv=inv(gg)
beta=mv(ginv,alpha)
def cov_hess(Uh,Ug):
    return [[Uh[i][j]-sum((Gamma[k][i][j]*Ug[k]
                            for k in range(n)),ZERO)
             for j in range(n)] for i in range(n)]
Hn=cov_hess(Nh,Ng);Hm=cov_hess(Mh,Mg)
# Bracket density of two standard ADM Hamiltonian constraints:
# ultralocal kinetic/curvature terms cancel under antisymmetry;
# the only relevant potential variation is
#  sqrt g (g^ij Delta N - nabla^i nabla^j N).
# Contract with δH/δpi=2 M/sqrtg*(pi_ij-(pi/2)g_ij).
raw=2*sum((pi[i][j]*(N*Hm[i][j]-M*Hn[i][j])
           for i in range(n) for j in range(n)),ZERO)
# pi is a contravariant symmetric tensor DENSITY of weight one:
# ∇_i pi^{ij}=∂_i pi^{ij}+Gamma^j_{ik} pi^{ik}.
divpi=[sum((dpi[i][i][j] for i in range(n)),ZERO)
       +sum((Gamma[j][i][k]*pi[i][k] for i in range(n)
             for k in range(n)),ZERO)
       for j in range(n)]
Hcov=[-2*sum((gg[j][k]*divpi[j] for j in range(n)),ZERO)
      for k in range(n)]
Dsmear=mdot(beta,Hcov)
# Crucial: at one point raw bracket density != momentum constraint.
# They differ by an explicit total spatial divergence. Under
# compact support / boundary flux=0 their spatial integrals agree.
divJ=2*sum(
    (dpi[i][i][j]*alpha[j]
     +pi[i][j]*(Ng[i]*Mg[j]+N*Mh[i][j]
                -Mg[i]*Ng[j]-M*Nh[i][j])
     for i in range(n) for j in range(n)),ZERO)
assert raw==Dsmear+divJ
assert raw==F(150139237,93562560)
assert Dsmear==F(4413193,3132864)
assert divJ==F(56099,286195)
assert all(v!=0 for v in (raw,Dsmear,divJ))
# No constraint surface (Hperp=0, H_i=0) was assumed anywhere.
sqrtg=F(16)
Hkin=hamiltonian_kin(gg,pi,F(1),sqrtg)
Hperp=Hkin-sqrtg*R
assert Hperp!=0 and any(Hcov)
# Verify pullback of shift/canonical generator at this point:
xi=[F(1,3),F(0),F(-2,5)]
X=[[F(1),F(0),F(0)],
   [F(0),F(-1,2),F(0)],
   [F(0),F(0),F(1,4)]]
Lieg=lie_metric(gg,gi,xi,X)
dwx=solve_weights(w0,Lieg)
assert mdot(p_of(pi,w0),dwx)==contract(pi,Lieg)
# Density-current identity, including nonflat g_i:
shift_current_div=2*sum(
    (dpi[j][j][i]*gg[i][k]*xi[k]
     +pi[j][i]*gi[j][i][k]*xi[k]
     +pi[j][i]*gg[i][k]*X[k][j]
     for j in range(n) for i in range(n) for k in range(n)),ZERO)
assert contract(pi,Lieg)==mdot(xi,Hcov)+shift_current_div
assert shift_current_div!=0

# H56.3: diffeomorphism (D,D) algebra on a NONUNIFORM metric:
# [£xi, £eta]g=£[xi,eta]g for two affine spatial vector fields.
eta=[F(-1,4),F(2,7),F(1,5)]
Y=[[F(0),F(1,3),F(0)],
   [F(1,5),F(0),F(1,6)],
   [F(0),F(-1,4),F(0)]]
def liejet(values,gradient,v,Jv):
    LV=lie_metric(values,gradient,v,Jv)
    gradients=[]
    for m in range(n):
        dLie=zeros(n,n)
        for i in range(n):
            for j in range(n):
                dLie[i][j]=sum(
                    (Jv[k][m]*gradient[k][i][j]
                     +v[k]*gij[m][k][i][j]
                     +gradient[m][k][j]*Jv[k][i]
                     +values[k][j]*F(0)
                     +gradient[m][i][k]*Jv[k][j]
                     for k in range(n)),ZERO)
        gradients.append(dLie)
    return LV,gradients
# More general derivative of L_v g includes terms with
# derivative of vector GRADIENT. Here v is affine, so d²v=0.
Lie_eta,grad_eta=liejet(gg,gi,eta,Y)
Lie_xi,grad_xi=liejet(gg,gi,xi,X)
commLie=sub(lie_metric(Lie_eta,grad_eta,xi,X),
            lie_metric(Lie_xi,grad_xi,eta,Y))
commv=[sum((Y[i][k]*xi[k]-X[i][k]*eta[k] for k in range(n)),ZERO)
       for i in range(n)]
commJ=sub(mm(Y,X),mm(X,Y))
assert commLie==lie_metric(gg,gi,commv,commJ)
assert commLie!=zeros(n,n)

# H56.4: (D,H_kin) scalar DENSITY transformation for generic
# nonuniform g, pi-density under same spatial Lie derivative:
# L_xi H_kin = xi^i ∂_i H_kin + H_kin div xi.
def pi_cov_density_lie(pi,dpi,xi,X):
    divxi=sum((X[i][i] for i in range(n)),ZERO)
    return [[sum((xi[k]*dpi[k][i][j] for k in range(n)),ZERO)
             -sum((pi[k][j]*X[i][k]+pi[i][k]*X[j][k]
                   for k in range(n)),ZERO)
             +pi[i][j]*divxi
             for j in range(n)] for i in range(n)]
def kinetic_num(g,pi):
    pilower=mm(mm(g,pi),g)
    trpi=contract(pi,g)
    return contract(pi,pilower)-trpi*trpi/2
def kinetic_der(g,pi,dg,dpi):
    trpi=contract(pi,g)
    trpid=contract(dpi,g)+contract(pi,dg)
    return (2*contract(dpi,mm(mm(g,pi),g))
            +2*contract(dg,mm(mm(pi,g),pi))
            -trpi*trpid)
pidot=pi_cov_density_lie(pi,dpi,xi,X)
num=kinetic_num(gg,pi)
Lkin=(kinetic_der(gg,pi,Lieg,pidot)
      -num*trace(mm(ginv,Lieg))/2)/sqrtg
spatial_kin_der=[
    (kinetic_der(gg,pi,gi[k],dpi[k])
     -num*trace(mm(ginv,gi[k]))/2)/sqrtg
    for k in range(n)]
divxi=sum((X[i][i] for i in range(n)),ZERO)
assert Lkin==mdot(xi,spatial_kin_der)+Hkin*divxi
assert Lkin!=0
# The full -sqrtg R potential is also a scalar density once
# H53's smooth soldered manifold/metric is GIVEN, by standard
# tensor calculus. This is NOT independently P3-generated HDA.

print("PASS H56: finite spatial shear maps positive K4 weights to (-1/2) exterior while SPD metric remains valid")
print("PASS H56: chart is local and needs physical solder-compatible transitions for general diffeomorphisms")
print("PASS H56: exact nonuniform OFF-SHELL Hamiltonian-Hamiltonian bracket = D[beta] + boundary divergence")
print("PASS H56: nonzero R3 and Hperp/H_i not constrained to zero; genuine nonhomogeneous field jets")
print("PASS H56: pointwise D-shift/K4 induced weight Lie action and explicit boundary-current identity")
print("PASS H56: [Lie_xi,Lie_eta]g = Lie_[xi,eta]g on nonuniform 2-jets")
print("PASS H56: ADM kinetic Hamiltonian density transforms as weight-one spatial scalar density")
print("PASS H56: symplectic cotangent chart transports standard ADM brackets under EXTERNAL assumptions")
print("BOUNDARY: full spatial HDA is CONDITIONAL inherited ADM; not independently CR/KKS generated")
print("BOUNDARY: all HDA integral equalities require correct support/boundary and positive-chart domain")
