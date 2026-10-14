"""H32: one connected 3-site rational unitary CPTP with full P3 residue and Xi ranks.

Exact rational Gaussian arithmetic reused from audited H24; stdlib only.
J_k := complex span of H_k is a CANONICALLY COMPUTED CANDIDATE sector,
not automatically the independently fixed P6 physical microscopic J_N.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import C,gc,I,O,Z0,U as U2
N=3
def z():return [[Z0 for _ in range(N)] for _ in range(N)]
def eye():return [[O if i==j else Z0 for j in range(N)] for i in range(N)]
def unit(i,j):
    a=z();a[i][j]=O;return a
def add(a,b):return [[a[i][j]+b[i][j] for j in range(N)] for i in range(N)]
def scale(a,c):return [[a[i][j]*c for j in range(N)] for i in range(N)]
def sub(a,b):return add(a,scale(b,-1))
def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(N)),Z0)
             for j in range(N)] for i in range(N)]
def dagger(a):return [[a[j][i].conj() for j in range(N)] for i in range(N)]
def com(a,b):return sub(mm(a,b),mm(b,a))
def diag(a):return [[a[i][j] if i==j else Z0 for j in range(N)] for i in range(N)]
def hidden(a):return sub(a,diag(a))
def trace(a):return sum((a[i][i] for i in range(N)),Z0)
def flatten(a):
    return [a[i][j].r for i in range(N) for j in range(N)]+[
            a[i][j].i for i in range(N) for j in range(N)]
def rr(matrices):
    if not matrices:return 0
    columns=[flatten(a) for a in matrices]
    m=[[v[k] for v in columns] for k in range(2*N*N)]
    pivot=0
    for col in range(len(columns)):
        idx=next((j for j in range(pivot,len(m)) if m[j][col]!=0),None)
        if idx is None:continue
        m[pivot],m[idx]=m[idx],m[pivot]
        x=m[pivot][col];m[pivot]=[a/x for a in m[pivot]]
        for j in range(len(m)):
            if j!=pivot and m[j][col]:
                v=m[j][col]
                m[j]=[a-v*b for a,b in zip(m[j],m[pivot])]
        pivot+=1
        if pivot==len(m):break
    return pivot
def xi(J):return hidden(sub(J,dagger(J)))
def diag_matrix(v):
    a=z()
    for i,c in enumerate(v):a[i][i]=c
    return a
def embed_edge(u,v):
    E=eye()
    for i in (u,v):
        for j in (u,v):E[i][j]=U2[i-u][j-u]
    return E
# Two noncommuting nearest-neighbor rational unitaries define ONE
# fixed discrete channel, not independent physically admissible controls.
U01=embed_edge(0,1)
U12=embed_edge(1,2)
U3=mm(U12,U01)
assert mm(dagger(U3),U3)==eye()
assert U3[0][1]==C(F(0),F(-2,3))
assert U3[1][2]==C(F(0),F(-2,3))
assert U3[2][0]==C(F(-4,9))
assert U3[0][2]==Z0
def Phi(a):return mm(mm(U3,a),dagger(U3))
assert Phi(eye())==eye()
# Connected finite coupling/support graph (not a disconnected spectator):
# both 01 and 12 microscopic matrix entries are nonzero.
assert all(U3[i][j]!=Z0 for i,j in ((0,1),(1,0),(1,2),(2,1)))
D=[unit(j,j) for j in range(N)]
iterates=D[:]
H={}
allh=[]
for k in (1,2,3):
    iterates=[Phi(d) for d in iterates]
    # Only E00 and E11 needed: since Phi^k(I)=I, the third
    # diagonal direction yields minus their hidden sum.
    H[k]=[hidden(iterates[j]) for j in (0,1)]
    assert hidden(iterates[2])==scale(add(H[k][0],H[k][1]),-1)
    assert all(dagger(h)==h and diag(h)==z() for h in H[k])
    allh.extend(H[k])
    rank=rr([scale(h,I) for h in allh])
    assert rank==2*k, (k,rank)
# At k=3 the extracted anti-Hermitian Xi-image exhausts all six
# zero-diagonal anti-Hermitian 3x3 directions.
assert rr([xi(scale(h,I/F(2))) for h in allh])==6
assert all(xi(scale(h,I/F(2)))==scale(h,I) for h in allh)
assert rr([scale(h,I) for h in H[1]])==2
assert rr([scale(h,I) for k in (1,2) for h in H[k]])==4

# Original P3 quadratic residue: R2 comes from H1 x H1 and vanishes
# on the diagonal; R3 contains H1 x H2, where witnesses saturate D3^0.
for a in H[1]:
    for b in H[1]:
        assert diag(com(a,dagger(b)))==z()
w0=diag(com(H[1][0],dagger(H[2][0])))
w1=diag(com(H[1][1],dagger(H[2][0])))
assert w0==diag_matrix([
    C(F(0),F(80,243)),
    C(F(0),F(-16,2187)),
    C(F(0),F(-704,2187))])
assert w1==diag_matrix([
    C(F(0),F(-80,243)),
    C(F(0),F(80,243)), Z0])
assert trace(w0)==Z0 and trace(w1)==Z0
assert rr([w0,w1])==2
# Hence R_2={0} and R_3=D_3^0 in the ORIGINAL P3 definition.

# Test the P6 actual two real exchange controls and H30 quadrature.
A01=sub(unit(0,1),unit(1,0))
B12=sub(unit(2,1),unit(1,2))
Q01=scale(add(unit(0,1),unit(1,0)),-I)
Q02=scale(add(unit(0,2),unit(2,0)),-I)
def image(k):return [scale(h,I) for j in range(1,k+1) for h in H[j]]
for k in (1,2,3):
    V=image(k)
    for target in (A01,B12,Q01,Q02):
        belongs=rr(V+[target])==rr(V)
        assert belongs==(k==3), ("membership",k,belongs)
assert rr(image(3))==6
assert rr(image(3)+[A01,B12,Q01,Q02])==6

# Lie closure of extracted controls reaches su3, CONDITIONAL on
# choosing the canonical Krylov sector J_micro := H3 as the P6 J_N.
# The necessary real control directions A01,B12,Q01 all lie in Xi(J).
def lie_closure(initial):
    basis=[]
    for a in initial:
        if rr(basis+[a])>len(basis):basis.append(a)
    for depth in range(10):
        old=basis[:]
        for a in old:
            for b in old:
                c=com(a,b)
                if rr(basis+[c])>len(basis):basis.append(c)
        if len(basis)==len(old):return basis
    raise AssertionError("Lie closure unfinished")
L=lie_closure(image(3))
assert len(L)==8 and rr(L)==8
assert all(dagger(k)==scale(k,-1) and trace(k)==Z0 for k in L)
# No new operator was appended to J to achieve full rank: all six
# anti-Hermitian directions are extracted from the single Phi channel.
print("PASS H32: one connected 3-site unitary CPTP map with exact rational entries")
print("PASS H32: original P3 R2=0 and R3=D3^0 with two explicit residue witnesses")
print("PASS H32: Xi(H1,H2,H3) real ranks 2,4,6, exhausting all edge quadratures")
print("PASS H32: P6 path A01/B12 and H30 Q01 enter precisely at Krylov depth3")
print("PASS H32: conditionally chosen J_micro=H3 gives su3 Lie closure")
print("SCOPE: independent P6 frozen J_N identification and physical access are not proved")
