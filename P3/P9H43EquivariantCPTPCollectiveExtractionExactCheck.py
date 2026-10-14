"""H43: Reflection-equivariant tangent classification and CP collective extraction.

Two distinct symmetry axioms are NOT equivalent:
- covariance of the FULL two-knob physical control FAMILY under parameter swap
- pointwise reflection invariance of EVERY physically permitted tangent.
Only the second (or exclusion of the swap-odd control mode) forces a=b.

H42's actual reflection-covariant, genuine original-P3-R3-saturated CPTP
microscopic update is reused without modification.
A parity twirl IS CPTP and Phi-intertwining; a path Schur cutoff with
unattenuated both edges is NOT CP; attenuated CP cutoff exists iff
|s|<=1/sqrt(2). Its composition with the twirl gives a conditional
collective tangent but breaks Phi-intertwining and destroys odd
population readout. It is extra microscopic instrumentation, not a
CR-derived or automatically inherited P6 J_N provenance map.

Exact Gaussian rational / Fraction only; no floating tolerances.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H42ReflectionCPTPCollectiveProvenanceExactCheck import (
    N,U,reflection,A,B,K,T,Jcol,h11,H,by_depth,
    Xi,action,rank_complex
)
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    unit,z,eye,scale,add,sub,mm,dagger,com,diag,hidden,trace,rr
)
assert N==3
P=reflection
evenK=add(A,B)
oddK=sub(A,B)
def twist(x):return action(P,x)
def twirl(x):return scale(add(x,twist(x)),F(1,2))
def L_minus(x):return (x[0][0]-x[2][2]).r
def kappa(c,d,x,y):
    return add(scale(A,c*x+d*y),scale(B,d*x+c*y))
def hessian_xy(Kx,Ky,d):
    return scale(add(com(Kx,com(Ky,d)),com(Ky,com(Kx,d))),F(1,2))
def mat_eq(x,y):return x==y
def edgeMask(s):
    return [[O if i==j else (gc(s) if abs(i-j)==1 else Z0)
            for j in range(N)] for i in range(N)]
def hadamard(m,x):
    return [[m[i][j]*x[i][j] for j in range(N)] for i in range(N)]
def schur(s,x):return hadamard(edgeMask(s),x)
def select(s,x):return schur(s,twirl(x))
def determinant_fraction_3(m):
    a=lambda i,j:m[i][j].r
    return (a(0,0)*(a(1,1)*a(2,2)-a(1,2)*a(2,1))
            -a(0,1)*(a(1,0)*a(2,2)-a(1,2)*a(2,0))
            +a(0,2)*(a(1,0)*a(2,1)-a(1,1)*a(2,0)))
def m2(a,b,c,d):return a*d-b*c

assert twist(A)==B and twist(B)==A
assert twist(evenK)==evenK and twist(oddK)==scale(oddK,-1)
assert [trace(mm(P,unit(k,k))) for k in range(N)]==[Z0,O,Z0]
for c,d in ((F(3,5),F(1,5)),(F(1,2),F(1,2)),
            (F(3,5),F(0)),(F(-2,7),F(5,11))):
    for x,y in ((F(1),F(0)),(F(0),F(1)),
                (F(2,5),F(-3,7)),(F(1),F(1)),(F(1),F(-1))):
        assert twist(kappa(c,d,x,y))==kappa(c,d,y,x)
        assert kappa(c,d,x,x)==scale(evenK,(c+d)*x)
        assert kappa(c,d,x,-x)==scale(oddK,(c-d)*x)
        assert dagger(kappa(c,d,x,y))==scale(kappa(c,d,x,y),-1)
# A 2-knob swap-equivariant family admits a freely variable
# reflection-odd control tangent unless c=d.
c,d=F(3,5),F(1,5)
assert twist(kappa(c,d,1,0))!=kappa(c,d,1,0)
assert kappa(c,d,1,-1)!=z()
assert kappa(F(1,2),F(1,2),1,-1)==z()
assert kappa(F(1,2),F(1,2),2,3)==scale(evenK,F(5,2))
# On a 1-knob TRIVIAL reflection representation, invariance demands
# a=b (and is sufficient).
def control_by_coeff(a,b):return add(scale(A,a),scale(B,b))
assert twist(control_by_coeff(F(2,5),F(2,5)))==control_by_coeff(F(2,5),F(2,5))
assert twist(control_by_coeff(F(2,5),F(3,5)))!=control_by_coeff(F(2,5),F(3,5))

dcenter=unit(1,1)
# The predicted antisymmetric population Hessian vanishes if both
# physical tangents are pointwise P-even, but two independent swap-
# equivariant controls have a nonzero mixed even/odd Hessian.
Ke=kappa(c,d,1,1)
Ko=kappa(c,d,1,-1)
assert L_minus(hessian_xy(Ke,Ke,dcenter))==0
assert L_minus(hessian_xy(Ko,Ko,dcenter))==0
assert L_minus(hessian_xy(Ke,Ko,dcenter))==4*(c+d)*(c-d)==F(32,25)
assert L_minus(hessian_xy(Ko,Ke,dcenter))==F(32,25)
# Nontrivial covariance of the controlled CPTP family
# Psi_(x,y)=Ad_exp(kappa(x,y)) o Phi:
# since P U=U P and P kappa(x,y) P=kappa(y,x),
# all power-series coefficients of e^kappa intertwine.
assert twist(U)==U
for x in (unit(0,0),unit(1,1),unit(0,1),unit(2,0)):
    for j in range(4):
        k1=kappa(c,d,F(2,7),F(-1,3))
        k2=kappa(c,d,F(-1,3),F(2,7))
        def itercomm(k,xx,steps):
            for _ in range(steps):xx=com(k,xx)
            return xx
        lhs=twist(itercomm(k1,action(U,x),j))
        rhs=itercomm(k2,action(U,twist(x)),j)
        assert lhs==rhs

# CPTP symmetry twirling T = 1/2 (identity channel + Ad_P).
# Proof is two normalized unitary Kraus operators I/sqrt(2),
# P/sqrt(2), and P²=I. It is unital and trace preserving.
for i in range(N):
    for j in range(N):
        x=unit(i,j)
        assert twirl(twirl(x))==twirl(x)
        assert twirl(dagger(x))==dagger(twirl(x))
        assert trace(twirl(x))==trace(x)
        assert twist(twirl(x))==twirl(x)
        # Since the ACTUAL microscopic U commutes with P, T Phi=Phi T.
        assert twirl(action(U,x))==action(U,twirl(x))
assert twirl(dcenter)==dcenter
assert twirl(unit(0,0))==scale(add(unit(0,0),unit(2,2)),F(1,2))
# Twirl destroys the odd population readout if used on the final state.
assert L_minus(twirl(unit(0,0)))==0
assert L_minus(unit(0,0))==1

# A path support Schur mask preserving all three populations, both
# edge coherences by factor s, and deleting the 02 chord is CPTP
# iff M_s=[[1,s,0],[s,1,s],[0,s,1]] >= 0.
# Its eigenvalues are 1,1+sqrt(2)s,1-sqrt(2)s.
# For real s>=0 this is iff 2s²<=1.
attenuation=F(3,5)
M=edgeMask(attenuation)
assert all(M[k][k]==O for k in range(N))
assert M[0][1]==M[1][2]==gc(F(3,5)) and M[0][2]==Z0
assert determinant_fraction_3(M)==1-2*attenuation**2==F(7,25)
assert m2(F(1),attenuation,attenuation,F(1))==F(16,25)>0
assert 1-attenuation**2>0
# Choi criterion of Schur multipliers then proves S_s CPTP,
# and Kraus may be chosen diagonal from a PSD Gram factorization.
invalid=F(4,5)
assert determinant_fraction_3(edgeMask(invalid))==F(-7,25)<0
assert determinant_fraction_3(edgeMask(F(1)))==F(-1)
# This also forbids ANY unital CP map FIXING EVERY E_ii that acts
# as identity on BOTH E_01 and E_12 yet kills E_02:
# fixed rank-one projections lie in its multiplicative domain;
# hence such a map must be a Schur multiplier with the impossible M1.

# CPTP twirl+attenuated CP Schur cutoff, makes a reflection-even
# path-local output; both constituent channels legitimate.
E=lambda x: select(attenuation,x)
for i in range(N):
    for j in range(N):
        x=unit(i,j)
        out=E(x)
        assert dagger(out)==E(dagger(x))
        assert trace(out)==trace(x)
        assert twist(out)==out
        assert out[0][2]==out[2][0]==Z0
# For hidden P3 original full diagonal sector, CPTP coarse graining
# yields a collective (reflection-even path) *linear output*, with
# no guarantee that it is a microscopic control permission.
def inJcol(x):
    if diag(x)!=z():return False
    if x[0][2]!=Z0 or x[2][0]!=Z0:return False
    return x[0][1]==x[2][1] and x[1][0]==x[1][2]
for h in H:
    assert inJcol(E(h))
assert E(h11)[0][1]==I*gc(F(2,9)*attenuation)
assert E(h11)[2][1]==I*gc(F(2,9)*attenuation)
assert Xi(scale(E(h11),I))==scale(evenK,-F(4,9)*attenuation)
assert Xi(scale(E(h11),I))==scale(evenK,F(-4,15))
assert Xi(scale(E(h11),I))!=z()

# Symmetry twirl ALONE cannot manufacture the missing K from
# the original dynamic Xi(H), since it commutes with Xi:
even_hidden=[twirl(h) for h in H]
even_Xi=[Xi(scale(h,I)) for h in even_hidden]
assert rr(even_Xi+[evenK])==rr(even_Xi)+1
assert rr([Xi(scale(E(h),I)) for h in H]+[evenK])==rr(
    [Xi(scale(E(h),I)) for h in H])

# The successful CPTP coarse-graining is NOT a dynamical intertwiner:
# it erases Phi(E11)'s actual 0--2 chord while Phi E(E11)
# retains it (since E(E11)=E11).
assert E(dcenter)==dcenter
assert E(action(U,dcenter))[0][2]==Z0
assert action(U,E(dcenter))[0][2]==gc(F(4,9))
assert E(action(U,dcenter))!=action(U,E(dcenter))
assert twirl(action(U,dcenter))==action(U,twirl(dcenter))
# Extra orientation/polarization/tangent-provenance is still required
# to identify the CP-extracted image with independently frozen P6 J_N
# and its *physical* 2D/1D target control selection.

print("PASS H43: exchange control FAMILY swap covariance does not force pointwise locked tangents")
print("PASS H43: pointwise reflection invariance/odd-mode exclusion forces a=b")
print("PASS H43: exact mixed parity P6 population Hessian 32/25 in a covariant two-knob CPTP control family")
print("PASS H43: group twirl is CPTP, commutes with fixed H42 Phi, but erases antisymmetric population readout")
print("PASS H43: path Schur multiplier S_s is CPTP iff |s|<=1/sqrt(2), cannot preserve both path coherences unattenuated")
print("PASS H43: CPTP twirl+Schur attenuation yields locked collective Xi direction from center hidden jet")
print("PASS H43: CPTP extracted static locality breaks Phi intertwining; extra provenance axiom remains indispensable")
print("SCOPE: this is standard finite quantum CP theory, not CR-specific response or Einstein dynamics")
