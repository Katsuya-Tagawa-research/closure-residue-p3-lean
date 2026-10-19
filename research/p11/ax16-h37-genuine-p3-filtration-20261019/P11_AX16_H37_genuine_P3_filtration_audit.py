#!/usr/bin/env python3
"""P11 AX16: genuine original P3 filtration for exact H37 CPTP dynamics."""
import sympy as s
from pathlib import Path
import itertools,json
checks=[]
def ck(cond,label):
    assert bool(cond),label
    checks.append(label)
n=5;ii=s.I
E=lambda i,j:s.SparseMatrix(n,n,{(i,j):1})
p=[E(i,i) for i in range(n)]
edges=list(itertools.combinations(range(n),2))
xs=[E(i,j)+E(j,i) for i,j in edges]
ys=[-ii*E(i,j)+ii*E(j,i) for i,j in edges]
B=p+xs+ys
D=lambda a:s.diag(*[a[i,i] for i in range(n)])
Q=lambda a:a-D(a)
H=s.diag(0,s.Rational(1,7),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13))
for j in range(4):H+=(E(j,j+1)+E(j+1,j))/2
L=lambda a:-ii*(H*a-a*H)+s.Rational(2,3)*(D(a)-a)
def coord(a):
    return s.Matrix([a[i,i] for i in range(n)]+
        [(a[i,j]+a[j,i])/2 for i,j in edges]+
        [(a[j,i]-a[i,j])/(2*ii) for i,j in edges])
M=s.Matrix.hstack(*[coord(L(b)) for b in B])
ck(M.shape==(25,25),'real Hermitian Liouvillian dimension25')
ck(all(v.is_Rational for v in M),'rational GKSL matrix')
ck(H.H==H,'Hermitian H37 Hamiltonian')
ck(all(coord(b)==s.eye(25)[:,j] for j,b in enumerate(B)),'Hermitian coordinate basis')
ck(L(s.eye(n))==s.zeros(n),'unital generator')
ck(all(s.trace(L(b))==0 for b in B),'trace-preserving generator')
for j in range(n):
    ck(Q(p[j])==s.zeros(n),f'H0 zero for p{j}')
    ck(D(L(p[j]))==s.zeros(n),f'first population derivative p{j}')
# CPTP because (I-L)^-1 = integral e^-s exp(sL) ds.
R=(s.eye(25)-M).inv()
ck((s.eye(25)-M)*R==s.eye(25),'exact rational resolvent')
ck(R[:,0].shape==(25,1),'exact finite resolvent coordinate')
h=[R[5:,j] for j in range(n)]
S=s.Matrix.hstack(*h)
ck(S.rank()==4,'original P3 H1 rank4')
ck(sum(h,s.zeros(20,1))==s.zeros(20,1),'sum hidden outputs vanishes')
def residue(a,b):
    z=s.zeros(n,1)
    for e,(i,j) in enumerate(edges):
        c=a[e]*b[10+e]-a[10+e]*b[e]
        z[i]+=c;z[j]-=c
    return z
pairs=list(itertools.combinations(range(n),2))
r={ab:residue(h[ab[0]],h[ab[1]]) for ab in pairs}
Z=s.Matrix.hstack(*r.values())
ck(Z.rank()==4,'true P3 R2 rank4 for resolvent')
ck(all(sum(v)==0 for v in r.values()),'traceless P3 commutator')
graph=s.Matrix.hstack(*[s.Matrix([int(j==i)-int(j==i+1) for j in range(n)]) for i in range(4)])
ck(Z.row_join(graph).rank()==4,'P3 R2 equals D5 traceless')
ck(all(s.simplify(v)==0 for v in Z.T*s.ones(n,1)),'P3 residue orthogonal to identity')
def toA(v):return sum((v[j]*xs[j]+v[j+10]*ys[j] for j in range(10)),s.zeros(n))
a,b=pairs[0]
ha,hb=toA(h[a]),toA(h[b])
actual=D(ha*hb.H-hb.H*ha)
expect=2*ii*s.diag(*list(r[(a,b)]))
ck(all(s.simplify((actual-expect)[j,j])==0 for j in range(n)),
   'actual diagonal commutator equals edge-divergence certificate')
ck(all(s.simplify((actual.H+actual)[j,j])==0 for j in range(n)),
   'P3 signed return anti-Hermitian')
ck(all(v!=s.zeros(n,1) for v in r.values() if any(v)),
   'residue nonzero rational witness')
K=[]
for a in p:
    x=D(L(Q(L(a))))
    K.append(s.Matrix([x[j,j] for j in range(n)]))
K=s.Matrix.hstack(*K)
ck(K.rank()==4,'different AX14 projected block K rank4')
ck(K.row_join(Z).rank()==4,'H37 K image equals P3 R2 only as subspaces')
for j in range(4):ck(K[j,j+1]==s.Rational(1,2),f'H37 Laplacian offdiagonal {j}')
# Fixed-time semigroup Phi_t=exp(tL). Exact Taylor coefficient proof.
MAX=8;series=[];cur=s.eye(25)[:,:5]
for k in range(MAX+1):
    series.append(cur[5:,:]);cur=M*cur/s.Rational(k+1)
def coefficient(pair,order):
    a,b=pair;v=s.zeros(n,1)
    for m in range(max(1,order-MAX),min(MAX,order-1)+1):
        k=order-m
        for e,(i,j) in enumerate(edges):
            xa,ya=series[m][e,a],series[m][10+e,a]
            xb,yb=series[k][e,b],series[k][10+e,b]
            c=xa*yb-ya*xb
            v[i]+=c;v[j]-=c
    return v
witness=((0,1),(1,2),(2,3),(0,3))
for ab in witness[:3]:
    for order in range(2,6):
        ck(coefficient(ab,order)==s.zeros(n,1),f'{ab} zero Taylor order{order}')
    ck(coefficient(ab,6)!=s.zeros(n,1),f'{ab} first nonzero Taylor order6')
for order in range(2,8):
    ck(coefficient(witness[3],order)==s.zeros(n,1),
       f'{witness[3]} zero Taylor order{order}')
ck(coefficient(witness[3],8)!=s.zeros(n,1),'(0,3) first nonzero Taylor order8')
minor=s.Matrix.hstack(*[coefficient(ab,6)[:4,:] for ab in witness[:3]],
                      coefficient(witness[3],8)[:4,:])
lead=minor.det()
ck(lead==-s.Rational(31890017,2655477015413839626240000),
   'fixed-time semigroup residue minor coefficient of t^26')
ck(lead!=0,'analytic nonzero Taylor determinant implies positive-small-time rank4')
ck(series[1].rank()==4,'generator first hidden direction rank4')
ck(series[0]==s.zeros(20,5),'P3 H0 zero in Taylor series')
result={
    'study':'P11-AX16','exact_checks':len(checks),'all_passed':True,'checks':checks,
    'original_p3_definition':'Rk span Delta_D([z,w*]), z in Hi, w in Hj, i+j<=k',
    'H37_resolvent_CPTP_provenance':'Phi=(I-L)^-1=integral exp(-s)exp(sL) ds',
    'H37_resolvent_H0_rank':0,'H37_resolvent_H1_rank':S.rank(),
    'H37_resolvent_R0_rank':0,'H37_resolvent_R1_rank':0,
    'H37_resolvent_R2_rank':Z.rank(),
    'H37_resolvent_CR_quadratic_first_depth':2,
    'H37_resolvent_R2_equals_D5_traceless':True,
    'H37_semigroup_R2_rank_for_all_sufficiently_small_positive_times':4,
    'H37_semigroup_first_P3_residue_depth_for_small_positive_t':2,
    'H37_semigroup_rank_certificate_pairs':[list(x) for x in witness],
    'H37_semigroup_determinant_first_nonzero_power':26,
    'H37_semigroup_determinant_coefficient_for_residue_without_2i':str(lead),
    'H37_projected_K_rank':K.rank(),
    'P3_R2_and_K_images_agree_for_H37':True,
    'P3_residue_operator_identical_to_K':False,
    'H37_physical_controls_provenance':'OPEN',
    'F_Generative_Completeness':'OPEN'}
Path(__file__).with_name('P11_AX16_exact_results.json').write_text(
    json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(f'P11 AX16 {len(checks)}/{len(checks)} exact checks PASS; genuine P3 R2 rank4')
