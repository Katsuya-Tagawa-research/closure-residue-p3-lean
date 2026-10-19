#!/usr/bin/env python3
"""P11-AX14 exact conditional quadratic population return; NOT P3 original R_k."""
from pathlib import Path
import json
import sympy as s

checks=[]
def ck(x,label):
    assert bool(x),label
    checks.append(label)
def E(n,i,j):
    a=s.zeros(n);a[i,j]=1;return a
def eq(a,b):
    return a.shape==b.shape and all(s.simplify(v)==0 for v in a-b)
def setup(H,gamma):
    n=H.rows
    def D(a):return s.diag(*[a[i,i] for i in range(n)])
    def L(a):return -s.I*(H*a-a*H)+gamma*(D(a)-a)
    def Q(a):return a-D(a)
    return D,L,Q

n=5
p=[E(n,i,i) for i in range(n)]
H=s.diag(0,s.Rational(1,7),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13))
for i in range(n-1):H+=(E(n,i,i+1)+E(n,i+1,i))/2
gamma=s.Rational(2,3)
D,L,Q=setup(H,gamma)
ck(eq(H,H.H),'H37 Hermitian')
ck(eq(L(s.eye(n)),s.zeros(n)),'H37 unital generator')
ck(eq(D(s.eye(n)),s.eye(n)),'D unital')
for i in range(n):
    ck(eq(D(L(p[i])),s.zeros(n)),f'first diagonal derivative site{i} is0')
    exp=sum((2*abs(H[j,i])**2*(p[j]-p[i]) for j in range(n) if j!=i),s.zeros(n))
    ck(eq(D(L(L(p[i]))),exp),f'second derivative site{i}')
    ck(eq(D(L(Q(L(p[i])))),exp),f'projected hidden return site{i}')
    ck(s.simplify(s.trace(exp))==0,f'population conservation site{i}')
    for j in range(n):
        expected=2*abs(H[j,i])**2 if j!=i else -sum((2*abs(H[k,i])**2 for k in range(n) if k!=i),s.Integer(0))
        ck(s.simplify(exp[j,j]-expected)==0,f'graph coefficient {i}->{j}')
ck(eq(D(L(L(p[0]))),(p[1]-p[0])/2),'H37 endpoint return')
ck(eq(D(L(L(p[4]))),(p[3]-p[4])/2),'H37 far endpoint return')
ck(eq(sum((D(L(L(x))) for x in p),s.zeros(n)),s.zeros(n)),'global population conservation')
for g in [s.Integer(0),s.Rational(1,3),s.Rational(2,3),s.Rational(7,2)]:
    De,Le,Qe=setup(H,g)
    for i in range(n):
        ck(eq(De(Le(Le(p[i]))),D(L(L(p[i])))),f'gamma invariance gamma={g} site{i}')
a,b,di,dj,gg=s.symbols('a b di dj gg',real=True)
H2=s.Matrix([[di,a+s.I*b],[a-s.I*b,dj]])
D2,L2,Q2=setup(H2,gg)
p2=[E(2,i,i) for i in range(2)]
w=2*(a*a+b*b)
ck(eq(D2(L2(p2[0])),s.zeros(2)),'symbolic first derivative0')
ck(eq(D2(L2(L2(p2[0]))),w*(p2[1]-p2[0])),'symbolic 2-site quadratic current')
ck(eq(D2(L2(Q2(L2(p2[0])))),w*(p2[1]-p2[0])),'symbolic 2-site projected return')
ck(eq(D2(L2(L2(p2[1]))),w*(p2[0]-p2[1])),'symbolic reverse return')
ck(eq(D2(L2(L2(p2[0]+p2[1]))),s.zeros(2)),'symbolic trace conservation')
ck(w.subs({a:0,b:0})==0,'no hopping return zero')
K=s.Matrix(n,n,lambda j,i:s.simplify(D(L(L(p[i])))[j,j]))
ck(K==K.T,'weighted return matrix symmetric')
ck(all(sum(K[:,i])==0 for i in range(n)),'column sums0')
ck(all(sum(K[i,:])==0 for i in range(n)),'row sums0')
ck(all(K[j,i]>=0 for i in range(n) for j in range(n) if i!=j),'nonnegative transfers')
lap=-sum((2*abs(H[j,i])**2*(s.eye(n)[:,i]-s.eye(n)[:,j])*(s.eye(n)[:,i]-s.eye(n)[:,j]).T for i in range(n) for j in range(i+1,n) if H[j,i]!=0),s.zeros(n))
ck(eq(K,lap),'negative weighted graph Laplacian')
ck(K.rank()==n-1,'H37 graph rank4')
ck(s.ones(1,n)*K==s.zeros(1,n),'left constant null')
ck(eq(K*s.ones(n,1),s.zeros(n,1)),'right constant null')
Hdiag=s.diag(0,s.Rational(3,7),s.Rational(11,9),-s.Rational(3,8),s.Rational(5,11))
Dd,Ld,Qd=setup(Hdiag,gamma)
for i in range(n):
    ck(eq(Dd(Ld(Ld(p[i]))),s.zeros(n)),f'diagonal H no quadratic return {i}')
    ck(eq(Qd(Ld(p[i])),s.zeros(n)),f'diagonal H no hidden first flow {i}')
Ha=H+s.diag(7,-4,5,-9,11)
Da,La,Qa=setup(Ha,s.Rational(13,5))
for i in range(n):
    ck(eq(Da(La(La(p[i]))),D(L(L(p[i])))),f'different diagonal/gamma same return {i}')
ck(not eq(H,Ha),'different microscopic Hamiltonians')
Hr=s.Matrix([[0,1,1],[1,0,1],[1,1,0]])
Hc=s.Matrix([[0,1,s.I],[1,0,1],[-s.I,1,0]])
Dr,Lr,Qr=setup(Hr,s.Rational(1,3));Dc,Lc,Qc=setup(Hc,s.Rational(1,3))
tp=[E(3,i,i) for i in range(3)]
ck(eq(Hr,Hr.H) and eq(Hc,Hc.H),'two triangle Hamiltonians Hermitian')
for i in range(3):
    ck(eq(Dr(Lr(Lr(tp[i]))),Dc(Lc(Lc(tp[i])))),f'triangle second-order equality site{i}')
third_r=[Dr(Lr(Lr(Lr(tp[i])))) for i in range(3)]
third_c=[Dc(Lc(Lc(Lc(tp[i])))) for i in range(3)]
ck(not eq(third_r[0],third_c[0]),'chiral triangle differs at third order')
ck(all(eq(Dr(Lr(tp[i])),Dc(Lc(tp[i]))) for i in range(3)),'same first derivative')
ck(all(s.simplify(sum(third_c[i][j,j] for j in range(3)))==0 for i in range(3)),'third trace conservation')
ck(s.im(Hr[0,1]*Hr[1,2]*Hr[2,0])==0,'real triangle flux0')
ck(s.im(Hc[0,1]*Hc[1,2]*Hc[2,0])==-1,'chiral flux -1')
ck(K[1,0]==s.Rational(1,2),'H37 p1 from p0 second derivative1/2')
ck(K[1,0]/2==s.Rational(1,4),'H37 t² coefficient1/4')
ck(K[0,0]==-s.Rational(1,2),'H37 origin survival second derivative')
ck(K[2,0]==0,'H37 second neighbor no second derivative')
results={'study':'P11-AX14','all_passed':True,'exact_checks':len(checks),'checks':checks,
'H37_quadratic_population_generator':[[str(K[i,j]) for j in range(n)] for i in range(n)],
'H37_weighted_graph_laplacian_rank':K.rank(),
'H37_short_time_p1_from_p0_t2_coefficient':'1/4',
'triangle_same_second_derivative':True,
'triangle_third_derivative_distinguishable':True,
'triangle_real_p0_third':[str(x) for x in third_r[0].diagonal()],
'triangle_flux_p0_third':[str(x) for x in third_c[0].diagonal()],
'original_P3_Rk_identification':'OPEN','F_derived_generator_origin':'OPEN',
'G2_source_completeness':'OPEN','G3_generativity_completeness':'OPEN'}
Path(__file__).with_name('P11_AX14_exact_results.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
print(f'P11 AX14 PASS {len(checks)}/{len(checks)} exact assertions')
