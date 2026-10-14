"""H41: independent collective CR sector versus SAME-Dataset-A standard GKSL.

No retrofitting static micro sector to measured response. Reproduces the
*frozen P6 v9.1 conditional collective-mode strict comparator*, not an
unconditional GR/CR-specific quantum signal.

All calculations are exact Gaussian-rational Fraction identities. Static
collective sector fixes locked left/right oriented first-residue tangent;
a standard GKSL comparator with the SAME graph and the SAME independently
calibrated aggregate tangent norm, but unspecified relative edge angles,
allows a nonzero left/right population Hessian.

When the independent calibration ALSO fixes the relative edge ratio,
the standard prediction collapses to the same null: no discrimination.

Separately test that an uncalibrated diagonal Stark Hamiltonian leaves
the first P6 target Hessian / first-residue tangent untouched, but changes
the actual ORIGINAL P3 depth-three signed quadratic witness.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    N,unit,z,eye,scale,add,sub,mm,dagger,com,diag,hidden,trace,rr
)
assert N==3

# 0-based sites: left 0, center 1, right 2.
E01=unit(0,1);E21=unit(2,1)
T=add(E01,E21)
Tdag=dagger(T)
A=sub(E01,dagger(E01))
B=sub(E21,dagger(E21))
def Xi(J):return hidden(sub(J,dagger(J)))
def R(a,b):return add(scale(A,gc(a)),scale(B,gc(b)))
def readout(h):
    # Left-right population observable on the 3-site path.
    return (h[0][0]-h[2][2]).r
def hes(a,b,c,d):
    # D² Sigma(0)[X,Y] = 1/2 (ad_KX ad_KY + ad_KY ad_KX)
    # of population state? Full second mixed derivative is
    # [K_X,[K_Y,rho0]] for commuting-symmetric Hessian average.
    rho=unit(1,1)
    Kx=R(a,b);Ky=R(c,d)
    h=scale(add(com(Kx,com(Ky,rho)),com(Ky,com(Kx,rho))),F(1,2))
    return h
def hess_scalar(a,b,c,d):return readout(hes(a,b,c,d))
def norm2(a,b):return a*a+b*b
def physical_coherent_jets(a,b,alpha,gamma):
    # One fixed ordinary physical GKSL model, no CR-only postulate.
    rho=unit(1,1);K=R(a,b)
    def Lop(x):
        D=z()
        for j in range(N):D[j][j]=gc(alpha[j])
        return sub(sub(com(K,x),scale(hidden(x),gc(gamma))),
                   scale(com(D,x),I))
    A0=hidden(Lop(rho))
    B0=hidden(Lop(Lop(rho)))
    return A0,B0,diag(com(A0,B0))
def isunitary_edge(u):
    return dagger(u)==scale(u,-1)

assert isunitary_edge(A) and isunitary_edge(B)
assert Xi(E01)==A and Xi(E21)==B
assert Xi(T)==add(A,B)
# Full frozen P6 COLLECTIVE sector Jcol=span_C{T,T†}.
# Its Xi image has only 2 real dimensions and only one real-skew
# direction (locked equal left/right amplitudes).
Jcol_image=[Xi(T),Xi(scale(T,I)),Xi(Tdag),Xi(scale(Tdag,I))]
assert rr(Jcol_image)==2
Jfree_image=[Xi(E01),Xi(scale(E01,I)),Xi(E21),Xi(scale(E21,I))]
assert rr(Jfree_image)==4
assert rr(Jcol_image+[A])==3
assert rr(Jcol_image+[B])==3
assert rr(Jcol_image+[add(A,B)])==2
assert all(abs(i-j)<=1 for M in (T,Tdag,E01,E21)
           for i in range(N) for j in range(N) if M[i][j]!=Z0)
# The CR collective oriented-provenance hypothesis fixes a_X=b_X
# for all declared real-skew coherent tangents.
for ax,cx in ((F(1,2),F(3,5)),(F(3,5),F(-2,3)),
              (F(-3,7),F(1,4))):
    assert hess_scalar(ax,ax,cx,cx)==0
    assert hess_scalar(ax,ax,ax,ax)==0
# Source P6 population Hessian factorization:
# D² population(X,Y)=2 [a_X a_Y(E00-E11)
#                       +b_X b_Y(E22-E11)].
for ax,bx,cx,dx in ((F(1,2),F(3,5),F(2,3),F(4,5)),
                    (F(3,25),F(21,25),F(3,25),F(21,25)),
                    (F(-2,7),F(5,11),F(2,3),F(-7,9))):
    target=add(scale(sub(unit(0,0),unit(1,1)),
                     gc(2*ax*cx)),
               scale(sub(unit(2,2),unit(1,1)),
                     gc(2*bx*dx)))
    assert hes(ax,bx,cx,dx)==target
    assert hess_scalar(ax,bx,cx,dx)==2*(ax*cx-bx*dx)

# H41 fixed SAME Dataset-A information:
# (i) support=both path edges, (ii) squared aggregate norm=18/25.
# Dataset A supplies STATIC collective Jcol separately, but does NOT
# observe exact relative dynamical tangent amplitudes of standard GKSL.
locked=(F(3,5),F(3,5))
unlocked=(F(3,25),F(21,25))
assert all(x!=0 for x in locked+unlocked)
assert norm2(*locked)==norm2(*unlocked)==F(18,25)
assert hess_scalar(*locked,*locked)==F(0)
assert hess_scalar(*unlocked,*unlocked)==F(-864,625)
assert hess_scalar(*unlocked,*unlocked)!=0
# Both GKSL models have same calibrated aggregate tangent norm and
# graph. ONE additionally satisfies CR-selected collective alignment.
assert rr(Jcol_image+[R(*locked)])==2
assert rr(Jcol_image+[R(*unlocked)])==3
# Counterfactual comparator with independent physical calibration
# of locked ratio: ordinary GKSL also predicts exactly the zero null.
assert hess_scalar(*locked,*locked)==F(0)

# Strict separation cannot be claimed from graph and total norm alone
# unless independent Jcol & star-compatible P6 oriented provenance are
# adopted *before Dataset B*. Otherwise both 0 and nonzero are allowed.

# Stark α is independent calibrated data and is invisible to Xi/first
# exchange tangent and to the P6 intervention Hessian; but influences
# ORIGINAL P3 depth-three signed residue.
gamma=F(1,2)
a,b=locked
A0,B0,R_zero=physical_coherent_jets(a,b,(F(0),)*3,gamma)
A1,B1,R_stark=physical_coherent_jets(
    a,b,(F(1,7),F(0),F(0)),gamma)
assert A0==A1
assert R_zero==z()
assert R_stark==scale(sub(unit(0,0),unit(1,1)),
                      I*gc(F(18,175)))
assert R_stark!=R_zero
assert hess_scalar(*locked,*locked)==F(0)
for gamma_i in (F(0),F(1,2),F(5,4)):
    _,_,rr0=physical_coherent_jets(a,b,(F(0),)*3,gamma_i)
    _,_,rr1=physical_coherent_jets(
        a,b,(F(1,7),F(0),F(0)),gamma_i)
    assert rr0==z() and rr1==R_stark
# The P9.38 +2i weighted graph-Laplacian cubic witness is just
# standard GKSL dynamics, and α must be calibrated independently.

# Operational output sets: CR conditional null {0}. Same-A norm
# standard contains {0, -864/625} at least; exact calibration of
# locked (a,b) collapses standard null also to {0}.
# The above is a prediction-set difference ONLY while the standard
# comparator has an *independent relative-angle uncertainty* not
# already closed by the calibration data.

print("PASS H41: frozen P6 Jcol Xi real rank2 versus same connected Jfree rank4")
print("PASS H41: collective oriented tangent locking gives exact left-minus-right Hessian null")
print("PASS H41: equal path support and EXACT equal aggregate tangent norm allow nonzero standard GKSL Hessian")
print("PASS H41: standard calibration fixing the relative left/right ratio ALSO gives the null")
print("PASS H41: diagonal Stark variation changes true original P3 cubic residue, leaves Xi and intervention Hessian unchanged")
print("PASS H41: standard GKSL predicts every H40 residue/readout; conditional collective comparator is the only strict set gap audited here")
print("SCOPE: Jcol and star-compatible physical provenance remain CONDITIONAL ex-ante inputs, not P3-derived facts")
print("SCOPE: no CR-only signal once matched calibrated standard microscopic restrictions imply same tangent alignment")
