"""H30 exact coherent-control gate: P6 real path plus one edge quadrature.

Reuses H24's rational Gaussian arithmetic; all arithmetic is exact Fraction.
The finite SU(3) Lie closure is not a calibrated static control manifold.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C, gc, I, O, Z0

N=3
def zeros():return [[Z0 for j in range(N)] for i in range(N)]
def unit(a,b):
    m=zeros();m[a][b]=O;return m
def ident():return [[O if i==j else Z0 for j in range(N)] for i in range(N)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(N)] for i in range(N)]
def times(a,s):return [[a[i][j]*s for j in range(N)] for i in range(N)]
def sub(a,b):return add(a,times(b,-1))
def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(N)),Z0)
             for j in range(N)] for i in range(N)]
def dagger(a):return [[a[j][i].conj() for j in range(N)] for i in range(N)]
def comm(a,b):return sub(mm(a,b),mm(b,a))
def diag(a):return [[a[i][j] if i==j else Z0 for j in range(N)] for i in range(N)]
def off(a):return sub(a,diag(a))
def trace(a):return sum((a[i][i] for i in range(N)),Z0)
def W(h):return h[0][1]*h[1][2]*h[2][0]
def vector(a):
    return [a[i][j].r for i in range(N) for j in range(N)]+[
            a[i][j].i for i in range(N) for j in range(N)]
def rank(mats):
    if not mats:return 0
    vs=[vector(a) for a in mats]
    M=[[v[i] for v in vs] for i in range(len(vs[0]))]
    pivot=0
    for col in range(len(vs)):
        row=next((i for i in range(pivot,len(M)) if M[i][col]!=0),None)
        if row is None:continue
        M[pivot],M[row]=M[row],M[pivot]
        q=M[pivot][col]
        M[pivot]=[v/q for v in M[pivot]]
        for j in range(len(M)):
            if j!=pivot and M[j][col]:
                z=M[j][col]
                M[j]=[v-z*w for v,w in zip(M[j],M[pivot])]
        pivot+=1
        if pivot==len(M):break
    return pivot

A=sub(unit(0,1),unit(1,0))
B=sub(unit(2,1),unit(1,2))
Cbr=comm(A,B)
K02=sub(unit(0,2),unit(2,0))
Q01=times(add(unit(0,1),unit(1,0)),-I)
Q02=times(add(unit(0,2),unit(2,0)),-I)
assert Cbr==times(K02,-1)
assert comm(A,Cbr)==times(B,-1)
assert comm(B,Cbr)==A
assert rank([A,B])==2
assert rank([A,B,Cbr])==3
assert rank([A,B,Cbr,Q01])==4
for k in (A,B,Cbr,Q01,Q02):
    assert dagger(k)==times(k,-1) and trace(k)==Z0

# Without the added quadrature: full coherent Lie closure = real so(3).
# A single additional PHYSICAL real control tangent on an existing path
# edge is outside that algebra, while adding no edge to the support graph.
primitive=[A,B,Q01]
basis=primitive[:]
for depth in range(8):
    old=basis[:]
    for a in old:
        for b in old:
            c=comm(a,b)
            if rank(basis+[c])>len(basis):
                basis.append(c)
    if len(basis)==len(old):break
assert len(basis)==8 and rank(basis)==8
assert all(dagger(k)==times(k,-1) and trace(k)==Z0 for k in basis)
assert rank(basis+[Cbr])==8 and rank(basis+[Q02])==8
# Real dimension of traceless anti-Hermitian 3x3 is eight.
# Hence the generated real Lie algebra is exactly su(3).
assert len(basis)==N*N-1

# Enlarging the *direct static linear manifold* by Q01 alone
# still leaves the same PATH support, so its Wilson loop vanishes.
for a,b,d in ((F(1),F(1),F(1)),(F(2,3),F(5,4),F(-3,7)),
              (F(0),F(1),F(2))):
    h=times(add(add(times(A,a),times(B,b)),times(Q01,d)),I)
    assert W(h)==Z0

# Admitting both extra static CHORD quadratures, one of which is Cbr
# available ONLY through coherent Lie synthesis in the 3-control model,
# reproduces H28's full flux family exactly.
G=[O,I,O]  # diagonal site-gauge matrix with G_11=i
def gauge(a):
    return [[G[i]*a[i][j]*G[j].conj() for j in range(N)]
            for i in range(N)]
def target(a,b,q):
    q=gc(q)
    return [[Z0,gc(a),q.conj()],[gc(a),Z0,gc(b)],
            [q,gc(b),Z0]]
def controls(a,b,q):
    q=gc(q)
    return add(add(times(A,a),times(B,b)),
               add(times(Cbr,q.i),times(Q02,q.r)))
def K_xi(J):return off(sub(J,dagger(J)))
for a,b in ((F(1),F(1)),(F(2,3),F(5,4))):
    base=C(F(3,5),F(4,5))
    qnorm=base*base.conj()
    assert qnorm==O
    for lam in (O,-O,I,-I):
        q=lam*base
        k=controls(a,b,q)
        h=times(k,I)
        assert dagger(h)==h
        assert gauge(h)==target(a,b,q)
        assert W(h)==gc(a*b)*q
        assert (h[2][0]*h[2][0].conj())==qnorm
        assert rank(basis+[k])==8
        # Formal P6 Xi(J) representation exists if the microscopic
        # sector is separately chosen to contain J=k/2.
        assert K_xi(times(k,F(1,2)))==k

# Exact one-edge-QUADRATURE witness: Q01 has no direct P6 real-lift
# representation, despite having only the original path support.
assert rank([A,B,Q01])==3
assert rank([A,B,Cbr,Q02])==4
assert rank([A,B,Cbr,Q02,Q01])==5

# A diagonal phase transform cannot turn a nonzero pure-imaginary
# Wilson invariant of so(3) into the real Wilson setting needed by H28.
for a,b,c in ((F(1),F(1),F(1)),(F(2,3),F(5,4),F(-7,6))):
    k=add(add(times(A,a),times(B,b)),times(Cbr,c))
    h=times(k,I)
    assert W(h)==C(F(0),a*b*c)
    assert W(gauge(h))==W(h)
    assert (I*W(h)).r!=0

print("PASS H30: one added existing-edge coherent quadrature generates su(3)")
print("PASS H30: original P6 real path generates only so(3)")
print("PASS H30: three-control static path has Wilson W=0")
print("PASS H30: Lie-reachable chord controls reproduce all four H28 flux settings")
print("PASS H30: explicit site gauge maps the four H families to H28 convention")
print("PASS H30: representation inside Xi depends on independently fixed CR sector")
print("SCOPE: Lie reachability is not static GKSL pulse synthesizability/physical provenance")
