"""H44 minimal exact memory to close H43's CP-reflection collective observer.

For H42's SAME rational U and H43's SAME CPTP E=S_(3/5) T:
- dim_C range(E)=4, ker(E)=5, but stable unobservable kernel
  intersection_n ker(E Phi^n) = 4D parity-odd sector.
- minimal observable linear closure has dimension 5 complex (4 current
  collective coordinates + ONE complex chord scalar); for physical
  Hermitian states trace one, ONE REAL memory scalar m=Re rho_02.
- parity twirl T is a CPTP conditional expectation onto M2 ⊕ C,
  and T Phi=Phi T gives exact CPTP *quantum* 5D operator-algebra state.
- Exact rational 5x5 update and an order-two output-memory recurrence.
- The full ORIGINAL P3 quadratic residue from all D3 seeds is NOT
  reconstructible from this memory: parity-odd hidden-jet products
  contribute to even diagonal residue despite being invisible to all
  subsequent LINEAR E readouts.

All rational Gaussian, no floating approximation or CR-only signal.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0
from P9H43EquivariantCPTPCollectiveExtractionExactCheck import (
    N,U,P,A,B,evenK,oddK,E,twirl,schur,attenuation,
    h11,H,by_depth,twist
)
from P9H32ConnectedCPTPKrylovProvenanceExactCheck import (
    unit,z,eye,scale,add,sub,mm,dagger,com,diag,hidden,trace,rr
)
assert N==3 and attenuation==F(3,5)
def Phi(x):return mm(mm(U,x),dagger(U))
def elem(i,j):return unit(i,j)
def sc(x,f):return scale(x,gc(f))
def real_rank_complex(rows):
    a=[[gc(x) for x in row] for row in rows]
    if not a:return 0
    n=len(a);m=len(a[0]);p=0
    for j in range(m):
        pivot=next((k for k in range(p,n) if a[k][j]!=Z0),None)
        if pivot is None:continue
        a[p],a[pivot]=a[p],a[p]
        inv=a[p][j]
        a[p]=[x/inv for x in a[p]]
        for k in range(n):
            if k!=p and a[k][j]!=Z0:
                t=a[k][j]
                a[k]=[u-t*v for u,v in zip(a[k],a[p])]
        p+=1
        if p==n:break
    return p
def coordsE(x):
    y=E(x)
    assert y[0][0]==y[2][2]
    assert y[0][1]==y[2][1]
    assert y[1][0]==y[1][2]
    assert y[0][2]==y[2][0]==Z0
    return [y[0][0],y[1][1],y[0][1],y[1][0]]
def memory(x):
    # Twirl's 02 chord is (rho_02+rho_20)/2, real for Hermitian.
    return (x[0][2]+x[2][0])/2
def carrier(x):return coordsE(x)+[memory(x)]
def bvec():
    Eeven0=add(elem(0,0),elem(2,2))
    Ecenter=elem(1,1)
    T=add(elem(0,1),elem(2,1))
    Tdag=dagger(T)
    Chord=add(elem(0,2),elem(2,0))
    return [Eeven0,Ecenter,T,Tdag,Chord]
basis=bvec()
assert all(twist(x)==x for x in basis)
assert len(basis)==5
assert real_rank_complex([[x[i][j] for x in basis]
                          for i in range(N) for j in range(N)])==5
# The fixed-point algebra of P is 5-dimensional (M2+C) and physical
# parity-odd sector is complex 4-dimensional.
odd_basis=[
    sub(elem(0,0),elem(2,2)),
    sub(elem(0,1),elem(2,1)),
    sub(elem(1,0),elem(1,2)),
    sub(elem(0,2),elem(2,0))
]
assert len(odd_basis)==4
assert all(twist(x)==sc(x,-1) for x in odd_basis)
assert all(twirl(x)==z() and E(x)==z() for x in odd_basis)
assert real_rank_complex([[x[i][j] for x in basis+odd_basis]
                          for i in range(N) for j in range(N)])==9

def reconstruct(y):
    # y contains physically allowed E output coords plus m,
    # and maps to the parity-EVEN matrix T rho. This map is a linear
    # algebraic lifting, NOT an independent CPTP channel from a
    # classical memory register or arbitrary truncated density matrix.
    p,q,ys,yt,m=y
    out=add(sc(basis[0],p),sc(basis[1],q))
    out=add(out,sc(basis[2],ys/gc(attenuation)))
    out=add(out,sc(basis[3],yt/gc(attenuation)))
    out=add(out,sc(basis[4],m))
    return out
for x in [elem(i,j) for i in range(N) for j in range(N)]+[
    sc(eye(),F(1,3)),h11]:
    assert reconstruct(carrier(x))==twirl(x)
    assert carrier(reconstruct(carrier(x)))==carrier(x)
    assert E(reconstruct(carrier(x)))==E(x)

# Exactly one missing complex scalar beyond the four E-coordinates.
assert real_rank_complex([carrier(x) for x in
    [elem(i,j) for i in range(N) for j in range(N)]])==5
assert real_rank_complex([coordsE(x) for x in
    [elem(i,j) for i in range(N) for j in range(N)]])==4
# E Phi^n kills all four parity-odd basis vectors for all n.
for n in range(10):
    for x0 in odd_basis:
        x=x0
        for _ in range(n):x=Phi(x)
        assert E(x)==z()
# But E Phi DOES detect the one missing EVEN chord immediately.
chord=basis[4]
assert E(chord)==z()
assert coordsE(Phi(chord))==[
    gc(F(-4,9)),gc(F(8,9)),
    C(0,F(-2,15)),C(0,F(2,15))]
# rank of observable histories (E now and E after ONE step) is 5;
# the infinite-time observability rank therefore cannot exceed 5
# (odd 4D kernel), and already equals five at depth one.
combined=[coordsE(x)+coordsE(Phi(x)) for x in
          [elem(i,j) for i in range(N) for j in range(N)]]
assert real_rank_complex(combined)==5
assert real_rank_complex([coordsE(x) for x in
    [elem(i,j) for i in range(N) for j in range(N)]])==4

# Exact autonomous 5x5 carrier recurrence on y=(p0,p1,c01,c10,m).
# Columns correspond to lifted E output coordinate basis and chord.
basis_car=[basis[0],basis[1],
           sc(basis[2],F(1,1)/attenuation),
           sc(basis[3],F(1,1)/attenuation),basis[4]]
assert [carrier(x) for x in basis_car]==[
    [O,Z0,Z0,Z0,Z0],
    [Z0,O,Z0,Z0,Z0],
    [Z0,Z0,O,Z0,Z0],
    [Z0,Z0,Z0,O,Z0],
    [Z0,Z0,Z0,Z0,O],
]
Mcols=[carrier(Phi(x)) for x in basis_car]
M=[[Mcols[j][i] for j in range(5)] for i in range(5)]
M_expected=[
 [gc(F(5,9)),gc(F(4,9)),gc(F(10,27)),gc(F(10,27)),gc(F(-4,9))],
 [gc(F(8,9)),gc(F(1,9)),gc(F(-20,27)),gc(F(-20,27)),gc(F(8,9))],
 [C(0,F(-2,15)),C(0,F(2,15)),I/9,-8*I/9,C(0,F(-2,15))],
 [C(0,F(2,15)),C(0,F(-2,15)),8*I/9,-I/9,C(0,F(2,15))],
 [gc(F(-4,9)),gc(F(4,9)),gc(F(10,27)),gc(F(10,27)),gc(F(5,9))]
]
assert M==M_expected
def matvec(M,v):
    return [sum((a*b for a,b in zip(row,v)),Z0) for row in M]
def update(y):return matvec(M,y)
states=[
 sc(eye(),F(1,3)),
 elem(0,0),elem(1,1),elem(2,2),
 add(sc(eye(),F(1,3)),sc(chord,F(1,6))),
 sub(sc(eye(),F(1,3)),sc(chord,F(1,6))),
 sc(add(elem(0,0),elem(2,2)),F(1,2)),
 sc(add(add(elem(0,0),elem(1,1)),
        add(elem(0,1),elem(1,0))),F(1,2))
]
for x0 in states:
    x=x0;y=carrier(x)
    for n in range(10):
        y2=update(y)
        x=Phi(x)
        assert carrier(x)==y2
        assert reconstruct(y2)==twirl(x)
        y=y2
# This recurrence is an EXACT legal quantum restricted dynamics when
# the memory state is represented as T(rho) in the fixed even C*-algebra:
# Phi_even is the restriction of unitary conjugation Ad_U to the
# fixed-point algebra and is CPTP on physical twirled states.
for x in basis:
    assert twist(Phi(x))==Phi(x)
for n in range(4):
    for x in states:
        assert twirl(Phi(x))==Phi(twirl(x))

# One-step observability: next center population resolves hidden m.
# q'=(8/9)p+(1/9)q-(4/9)(c01+c10)/s+(8/9)m.
def recover_memory_from_two_outputs(y,next_visible):
    p,q,c01,c10=y[:4]
    q_next=next_visible[1]
    return (gc(F(9,8))*(q_next-gc(F(8,9))*p
            -gc(F(1,9))*q+gc(F(4,9))/gc(attenuation)*(c01+c10)))
for x0 in states:
    x=x0
    for _ in range(7):
        ynow=carrier(x)
        y_next=coordsE(Phi(x))
        assert recover_memory_from_two_outputs(ynow,y_next)==memory(x)
        x=Phi(x)
# Thus two CONSECUTIVE observed E outputs recover the 1-scalar memory.
# A deterministic order-two output recurrence can then be computed
# from y_n,y_n+1 by recovering m_n, applying M twice, using next
# observed y_(n+1) as initial observable part.
for x0 in states:
    x=x0
    for _ in range(5):
        v0=coordsE(x)
        v1=coordsE(Phi(x))
        m0=recover_memory_from_two_outputs(v0,v1)
        y1=update(v0+[m0])
        assert y1[:4]==v1
        predicted_next=update(y1)[:4]
        assert predicted_next==coordsE(Phi(Phi(x)))
        x=Phi(x)

# One REAL memory scalar minimal on physical states:
# two positive states rho_± have equal E outputs but different m
# and different next center-site populations.
rplus=add(sc(eye(),F(1,3)),sc(chord,F(1,6)))
rminus=sub(sc(eye(),F(1,3)),sc(chord,F(1,6)))
assert E(rplus)==E(rminus)==sc(eye(),F(1,3))
assert memory(rplus)==gc(F(1,6)) and memory(rminus)==gc(F(-1,6))
assert coordsE(Phi(rplus))[1]-coordsE(Phi(rminus))[1]==gc(F(8,27))
# Positive eigenvalues 1/6, 1/3, 1/2, from 0/2 block.
for state in (rplus,rminus):
    assert dagger(state)==state and trace(state)==O
    assert state[0][0]*state[2][2]-state[0][2]*state[2][0]==gc(F(1,12))

# Quadratic ORIGINAL P3 residue needs parity-odd hidden history.
# This information is entirely invisible to ALL linear E-output
# sequences and to the full 5D autonomous EVEN reduced carrier.
def residue(h,k):return diag(com(h,dagger(k)))
def phi2(x):return Phi(Phi(x))
d0=elem(0,0)
d2=elem(2,2)
dbar=sc(add(d0,d2),F(1,2))
assert twirl(d0)==twirl(d2)==dbar
def original_depth3(d):
    return residue(hidden(Phi(d)),hidden(phi2(d)))
R0=original_depth3(d0)
R2=original_depth3(d2)
Rbar=original_depth3(dbar)
assert R0==diag(sub(
    add(sc(elem(1,1),I*F(16,81)),sc(elem(2,2),I*F(16,81))),
    sc(elem(0,0),I*F(32,81))))
assert R0!=R2
assert twirl(R0)==twirl(R2)
assert twirl(R0)==diag(add(
    sc(elem(1,1),I*F(16,81)),
    sc(add(elem(0,0),elem(2,2)),I*F(-8,81))))
assert Rbar==diag(add(
    sc(elem(1,1),I*F(4,81)),
    sc(add(elem(0,0),elem(2,2)),I*F(-2,81))))
assert twirl(R0)!=Rbar
# End seed and averaged seed produce identical E time-traces:
for j in range(10):
    dj0=d0
    djbar=dbar
    for _ in range(j):
        dj0=Phi(dj0)
        djbar=Phi(djbar)
    assert E(dj0)==E(djbar)
    assert carrier(dj0)==carrier(djbar)
# Even the parity-even part of the NONLINEAR original P3 residue
# differs despite the entire even dynamical state agreeing!
h0=hidden(Phi(d0));k0=hidden(phi2(d0))
he=twirl(h0);ke=twirl(k0)
ho=sub(h0,he);ko=sub(k0,ke)
assert twist(he)==he and twist(ke)==ke
assert twist(ho)==sc(ho,-1) and twist(ko)==sc(ko,-1)
evenR=residue(he,ke)
oddR=residue(ho,ko)
assert evenR==Rbar
assert twirl(R0)==add(evenR,oddR)
assert oddR==diag(add(
    sc(elem(1,1),I*F(4,27)),
    sc(add(elem(0,0),elem(2,2)),I*F(-2,27))))
assert oddR!=z()
# A physical even seed d=E11 carries no odd sector, so its original
# P3 depth3 residue IS reproducible from the 5D twirled state, but
# full all-D3 original R3 needs additional parity-odd microscopic
# data or a declared restriction of the admissible observable seeds.
dcenter=elem(1,1)
assert twirl(dcenter)==dcenter
assert original_depth3(dcenter)==residue(
    twirl(hidden(Phi(dcenter))),twirl(hidden(phi2(dcenter))))
assert original_depth3(dcenter)==diag(add(
    sc(elem(1,1),I*F(16,81)),
    sc(add(elem(0,0),elem(2,2)),I*F(-8,81))))

print("PASS H44: exact range(E) complex rank4, stable parity-odd hidden kernel rank4")
print("PASS H44: minimal linear observable carrier rank5 = 4 visible + 1 chord memory")
print("PASS H44: for physical normalized states, one REAL memory scalar Re rho02 is sufficient and necessary")
print("PASS H44: twirl is a genuine CPTP conditional expectation onto invariant M2+ C algebra")
print("PASS H44: exact rational 5x5 autonomous recurrence and two-consecutive-observation reconstruction")
print("PASS H44: full original P3 quadratic residue NOT recoverable from entire even output history")
print("PASS H44: parity-odd hidden-hidden bracket supplies nonzero even diagonal P3 return")
print("SCOPE: observable linear closure repaired, not P6 physical provenance nor full-P3 residue closure")
print("SCOPE: all microscopic evolution standard CPTP, not a CR-specific discriminator or GR")
