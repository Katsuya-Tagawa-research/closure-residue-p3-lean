"""H89: exact positive physical-gate U4 KKS tomography and access hierarchy.

This four-level single-excitation register is an independently assumed
physical comparator, not a sector derived from H75's six-level CPTP
instrument or a complete P9 ADM source.  Exchange and phase controls
are additional calibrated hardware assumptions, not P3 consequences.
"""
from fractions import Fraction as F
from P9H87KKSADMPoissonNonclosureDeWittExactCheck import (
    C,gc,I,O,Z0,n,edges,lam,star,xs,ys,
    zz,eye,E,plus,scale,minus,mm,dag,com,tr,X,Y,
    pb,read,diag,unitary_t
)
assert n==4 and len(edges)==6
cs=F(3,5); ss=F(4,5)
assert cs*cs+ss*ss==1
assert cs*ss==F(12,25)

def phase(b):
    U=eye()
    U[b][b]=-I
    assert mm(dag(U),U)==eye()
    return U

def uy(a,b):
    U=eye()
    U[a][a]=gc(cs);U[b][b]=gc(cs)
    U[a][b]=-I*gc(ss);U[b][a]=-I*gc(ss)
    assert mm(dag(U),U)==eye()
    return U

def ux(a,b):
    D=phase(b)
    U=mm(mm(D,uy(a,b)),dag(D))
    assert U[a][a]==gc(cs) and U[b][b]==gc(cs)
    assert U[a][b]==gc(ss) and U[b][a]==gc(-ss)
    assert mm(dag(U),U)==eye()
    return U

def evolve(U,rho):
    return mm(mm(U,rho),dag(U))

def prob_after(U,rho,a):
    return read(evolve(U,rho),E(a,a))

def frame_measure(rho):
    d=[read(rho,E(a,a)) for a in range(4)]
    px=[prob_after(ux(a,b),rho,a) for a,b in edges]
    py=[prob_after(uy(a,b),rho,a) for a,b in edges]
    return d,px,py

def recon(d,px,py):
    assert sum(d,Z0)==O
    x=[(px[k]-gc(cs*cs)*d[a]-gc(ss*ss)*d[b])/gc(cs*ss)
       for k,(a,b) in enumerate(edges)]
    y=[(py[k]-gc(cs*cs)*d[a]-gc(ss*ss)*d[b])/gc(cs*ss)
       for k,(a,b) in enumerate(edges)]
    rho=diag(d)
    for k,(a,b) in enumerate(edges):
        rho[a][b]=(x[k]-I*y[k])/gc(2)
        rho[b][a]=(x[k]+I*y[k])/gc(2)
    return rho,x,y

# 15-outcome equations hold AS LINEAR OPERATOR IDENTITIES on all 16
# complex matrix units, not just on specially prepared positive states.
for a,b in edges:
    for k in range(4):
        for l in range(4):
            rho=E(k,l)
            qx=prob_after(ux(a,b),rho,a)
            qy=prob_after(uy(a,b),rho,a)
            da=read(rho,E(a,a));db=read(rho,E(b,b))
            expectedx=gc(cs*cs)*da+gc(ss*ss)*db+gc(cs*ss)*read(rho,X(a,b))
            expectedy=gc(cs*cs)*da+gc(ss*ss)*db+gc(cs*ss)*read(rho,Y(a,b))
            assert qx==expectedx,(a,b,k,l,qx,expectedx)
            assert qy==expectedy,(a,b,k,l,qy,expectedy)
print("PASS H89.1: exact physical unitary R/Y edge gates and positive site-projector response formula on ALL 16 complex matrix units")

def rank_det(M):
    A=[[F(v) for v in row] for row in M]
    m=len(A);ncol=len(A[0]);i=0;det=F(1)
    for j in range(ncol):
        k=next((k for k in range(i,m) if A[k][j]),None)
        if k is None:
            if m==ncol:return i,F(0)
            continue
        if k!=i:
            A[i],A[k]=A[k],A[i]
            det=-det
        lead=A[i][j]
        det*=lead
        A[i]=[v/lead for v in A[i]]
        for k in range(i+1,m):
            if A[k][j]:
                scale=A[k][j]
                A[k]=[v-scale*w for v,w in zip(A[k],A[i])]
        i+=1
        if i==m:break
    if m!=ncol:return i,None
    return i,det if i==m else F(0)

# Unknown affine state coordinates z=(d0,d1,d2,x0..x5,y0..y5),
# with known trace1 and d3=1-d0-d1-d2.  Constants do not enter Jacobian.
matrix=[]
for a in range(3):
    r=[F(0)]*15;r[a]=F(1);matrix.append(r)
for quadrature in (0,1):
    for k,(a,b) in enumerate(edges):
        r=[F(0)]*15
        for i in range(3):
            r[i]=(F(cs*cs) if a==i else F(0)) + (
                F(ss*ss) if b==i else F(0)) - (
                F(ss*ss) if b==3 else F(0))
        r[3+k+6*quadrature]=F(cs*ss)
        matrix.append(r)
assert len(matrix)==15
rr,det=rank_det(matrix)
assert rr==15 and det==(F(12,25)**12),(rr,det)
print("PASS H89.1: exact physical 15-outcome affine tomography Jacobian rank15 and determinant (12/25)^12")

# Physical genuine positive fixed-spectrum orbit states: only
# unitary-conjugations of rho_star, no artificial nonpositive matrices.
states=[star]
U=mm(mm(mm(ux(0,1),uy(1,2)),ux(2,3)),uy(0,2))
assert mm(dag(U),U)==eye()
states.append(evolve(U,star))
for t in (F(1,10),F(1,2)):
    V,_,_=unitary_t(t)
    states.append(evolve(V,star))
for rho in states:
    assert dag(rho)==rho and tr(rho)==O
    d,px,py=frame_measure(rho)
    assert all(v.i==0 and F(0)<=v.r<=F(1) for v in d+px+py)
    reconstructed,x,y=recon(d,px,py)
    assert reconstructed==rho
    assert all(read(rho,A)==z for A,z in zip(xs,x))
    assert all(read(rho,A)==z for A,z in zip(ys,y))
print("PASS H89.1: complete 15-probability CPTP/unitary+positive-projector tomography of genuine physical 4-level orbit states")

# Purely REAL instrument catalogs do not distinguish the conjugate
# U02(+t) and U02(-t) states, even after any adaptive real-Kraus
# trajectory.  Every history POVM effect is real symmetric K^T K.
Vplus,_,_=unitary_t(F(1,2))
Vminus,_,_=unitary_t(F(-1,2))
rp=evolve(Vplus,star)
rm=evolve(Vminus,star)
assert rp!=rm
assert all(rp[a][b].r==rm[a][b].r for a in range(4) for b in range(4))
assert all(rp[a][b].i==-rm[a][b].i for a in range(4) for b in range(4))
dp,pxp,pyp=frame_measure(rp)
dm,pxm,pym=frame_measure(rm)
assert dp==dm and pxp==pxm
assert pyp!=pym
assert pb(rp,xs[0],xs[3])==gc(F(-24,125))
assert pb(rm,xs[0],xs[3])==gc(F(24,125))
# A real orthogonal control's Heisenberg effects remain symmetric real.
for Ureal in (eye(),ux(0,1),ux(0,2),ux(1,3),ux(2,3),
              mm(ux(0,1),ux(1,2))):
    for a in range(4):
        Q=mm(mm(dag(Ureal),E(a,a)),Ureal)
        assert all(Q[i][j].i==0 and Q[i][j]==Q[j][i]
                   for i in range(4) for j in range(4))
        assert read(rp,Q)==read(rm,Q)
print("PASS H89.2: real-Kraus operational catalog has same ALL real symmetric POVM outcomes for conjugate orbit states with KKS bracket -24/125 vs +24/125")

# Connected path graph + calibrated diagonals Lie-generate all su(4).
# Hermitian Lie bracket B(A,B)=-i[A,B] stays Hermitian traceless.
Zdiag=[minus(E(a,a),E(3,3)) for a in range(3)]
def coords(A):
    assert dag(A)==A and tr(A)==Z0
    c=[]
    for a,b in edges:
        c.append(A[a][b].r)
    for a,b in edges:
        c.append(-A[a][b].i)
    for a in range(3):
        c.append(A[a][a].r)
    assert len(c)==15
    return c

def lie_rank(active_edges):
    base=[X(*e) for e in active_edges]+Zdiag
    pool=[]
    queue=[]
    rows=[]
    def register(A):
        row=coords(A)
        rank,_=rank_det(rows+[row])
        if rank>len(rows):
            rows.append(row);pool.append(A);queue.append(A)
    for G in base:register(G)
    while queue:
        A=queue.pop(0)
        for G in base:
            H=scale(com(A,G),-I)
            register(H)
        assert len(rows)<=15
    return len(rows),pool

connected_rank,_=lie_rank(((0,1),(1,2),(2,3)))
disconnected_rank,_=lie_rank(((0,1),(2,3)))
assert connected_rank==15,connected_rank
assert disconnected_rank==7,disconnected_rank
print("PASS H89.3: connected path X01 X12 X23 + independent onsite phases generates exact su4 rank15; disconnected 2+2 graph rank7 traceless (u2+u2 rank8 incl global identity)")
print("BOUNDARY: genuine selectable cross-cell exchange and phase ports are externally postulated; Lie controllability is not an unconditional finite-pulse physical synthesis")
print("BOUNDARY: operationally tomographing U4 KKS is NOT deriving actual H75/P3 source, ADM canonical map, DeWitt, HDA, Einstein dynamics or F-completeness")
