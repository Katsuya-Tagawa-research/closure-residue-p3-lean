"""H66: physical odd-control provenance nonuniqueness on SAME original P3 source.

Uses H32's ONE connected rational three-site CPTP microscopic Phi with
genuine nonzero P3 R3 and candidate Xi(H_<=3) of real rank 6. Both
controlled extensions share Phi at zero control and hence EVERY
uncontrolled P3 filtration/residue. One has only P6-like real exchange
controls; one declares an ADDITIONAL imaginary-symmetric generator Q.

Exact Gaussian rational Cayley CPTP pulse exhibits a finite population
response to the extra knob on the original diagonal seed, but neither
the source Xi membership nor its response certifies a physically
inherited frozen P6 J_N. All physics is conventional finite QM.
"""
from fractions import Fraction as F
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    I, O, Z0, C, gc, N, z, eye, unit, add, sub, scale,
    mm, dagger, com, diag, hidden, trace, rr, Phi, H,
    image, xi, A01, B12, w0, w1
)

assert N==3
def transpose(M):
    return [[M[j][i] for j in range(N)] for i in range(N)]
def is_ah(M):
    return dagger(M)==scale(M,-1)
def is_un(M):
    return mm(dagger(M),M)==eye()
def conjugate(U,M):
    return mm(mm(U,M),dagger(U))
def cayley_square_minus_edge(K,s):
    # For anti-Hermitian edge K satisfying K^3=-K, this equals
    # (I+s K)(I-s K)^{-1}, an exact finite unitary for rational s.
    assert is_ah(K)
    assert mm(mm(K,K),K)==scale(K,-1)
    x=F(2)*s/(F(1)+s*s)
    y=F(2)*s*s/(F(1)+s*s)
    U=add(eye(),add(scale(K,x),scale(mm(K,K),y)))
    assert is_un(U)
    return U
def lie_closure(initial):
    base=[]
    for x in initial:
        if rr(base+[x])>len(base):base.append(x)
    for _ in range(12):
        old=base[:]
        for x in old:
            for y in old:
                k=com(x,y)
                if rr(base+[k])>len(base):base.append(k)
        if len(base)==len(old):return base
    raise AssertionError("Lie rank failed to converge")

X01=add(unit(0,1),unit(1,0))
Q=scale(X01,I)
assert is_ah(Q) and transpose(Q)==Q
assert is_ah(A01) and is_ah(B12)
assert transpose(A01)==scale(A01,-1)
assert transpose(B12)==scale(B12,-1)
assert rr([A01,B12,Q])==3
assert rr(image(3))==6
assert rr(image(3)+[A01,B12,Q])==6
assert w0!=z() and w1!=z()
assert diag(com(H[1][0],dagger(H[2][0])))!=z()
print("PASS H66: SAME H32 micro Phi with genuine original P3 R3 and candidate odd Xi direction")

Lreal=lie_closure([A01,B12])
Lodd=lie_closure([A01,B12,Q])
assert len(Lreal)==3 and rr(Lreal)==3
assert len(Lodd)==8 and rr(Lodd)==8
for k in Lreal:
    assert is_ah(k)
    assert transpose(k)==scale(k,-1)
for k in Lodd:
    assert is_ah(k) and trace(k)==Z0
assert rr(Lreal+[Q])==4
print("PASS H66: frozen P6-like two-real-knob Lie closure is so(3) rank3; adding ONE odd knob gives su(3) rank8")

# ONE fixed microscopic CPTP source, two CONDITIONAL control catalogs:
# baseline K(x)=xA+yB; extended K(x)=xA+yB+zQ.
# At x=y=z=0 both reduce exactly to the same Phi, so all original
# uncontrolled P3 hidden iterates, R3, and population histories match.
d=unit(0,0)
rho=Phi(d)
assert trace(rho)==O and rho==dagger(rho)
assert rho[0][0]==gc(F(5,9))
h=F(1,4)
UQ=cayley_square_minus_edge(Q,h)
response=conjugate(UQ,rho)
assert response==dagger(response)
assert trace(response)==O
assert response[0][0]==gc(F(18605,23409))
delta=response[0][0]-rho[0][0]
assert delta==gc(F(5600,23409)) and delta!=Z0
print("PASS H66: declared extra Q has exact finite positive-Cayley population effect 5600/23409 after SAME micro Phi")

# Two positive Hermitian coherent states rho_+/-=I/3 +/- iA01/6
# cannot be discriminated by any real-orthogonal + real-dephasing +
# real-Kraus diagonal observer circuit (H63), but Q distinguishes
# them with exact contrast 80/289 at h=1/4.
rho_plus=add(scale(eye(),F(1,3)),scale(A01,I/F(6)))
rho_minus=sub(scale(eye(),F(1,3)),scale(A01,I/F(6)))
assert rho_plus==dagger(rho_plus) and rho_minus==dagger(rho_minus)
assert trace(rho_plus)==trace(rho_minus)==O
rp=conjugate(UQ,rho_plus)[0][0]
rm=conjugate(UQ,rho_minus)[0][0]
assert rp==gc(F(409,867)) and rm==gc(F(169,867))
assert rp-rm==gc(F(80,289))
print("PASS H66: declared odd Q breaks real observer indistinguishability with contrast 80/289")

# Intrinsic distinction: the original finite P3 channel Phi and all
# its exact original signed residues are identical *because it is the
# same Phi* regardless of which control knob catalogue is later
# offered by apparatus. Xi(candidate) membership is a necessary
# candidate condition, not a sufficient physical selection law.
assert rr(image(3)+[Q])==6
assert rr(image(3)+[A01,B12])==6
print("PASS H66: original P3 data + Xi membership cannot select a unique physical odd-control catalog")
print("BOUNDARY: no inherited frozen P6 J_N, no independent source-to-hardware CPTP intertwiner, no P9.72 uniformity, Einstein, ADM or HDA")
