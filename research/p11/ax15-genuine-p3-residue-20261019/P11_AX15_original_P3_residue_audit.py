#!/usr/bin/env python3
"""P11 AX15: original P3 CR filtration vs projected GKSL return; exact SymPy audit.
Original P3: H_k=Q span(D,Phi D,...,Phi^k D), R_k=span E[z,w†], i+j<=k.
"""
from pathlib import Path
import json
import sympy as s
I=s.I
C=[]
def ck(test,tag):
    assert bool(test),tag
    C.append(tag)
def E(n,i,j):
    m=s.zeros(n);m[i,j]=1;return m
def eq(a,b):return a.shape==b.shape and all(s.simplify(x)==0 for x in a-b)
def vec(a):return s.Matrix(list(a))
def rank(mm):return s.Matrix.hstack(*[vec(x) for x in mm]).rank() if mm else 0
def comm(a,b):return a*b-b*a
def delta(a):return s.diag(*[a[i,i] for i in range(a.rows)])
def q(a):return a-delta(a)
def krylov_hidden(Phi,n,k):
    dd=[E(n,i,i) for i in range(n)]
    rr=[];cur=dd
    for j in range(k+1):
        if j:rr += [q(a) for a in cur]
        cur=[Phi(a) for a in cur]
    return rr

def res_r2(H1):return [delta(comm(a,b.H)) for a in H1 for b in H1]
X=E(2,0,1)+E(2,1,0);Y=-I*E(2,0,1)+I*E(2,1,0);Z=s.diag(1,-1)
p0=E(2,0,0);p1=E(2,1,1)
ck(eq(comm(X,Y),2*I*Z),'Pauli XY commutator')
# Counterexample A: continuous Hamiltonian returns populations but actual P3 Rk is silent all depths.
H=X/2
L=lambda a: -I*comm(H,a)
K=lambda a:delta(L(q(L(delta(a)))))
ck(eq(K(p0),(p1-p0)/2),'A dynamical K on p0 nonzero')
ck(eq(K(p1),(p0-p1)/2),'A dynamical K on p1 nonzero')
ck(rank([K(p0),K(p1)])==1,'A K range rank1')
U=(s.eye(2)-I*X)/s.sqrt(2)
Phi=lambda a:U*a*U.H
ck(eq(U.H*U,s.eye(2)),'A Kraus unitary TP')
ck(eq(U**2,-I*X),'A U squared -iX')
ck(eq(U**4,-s.eye(2)),'A U fourth scalar')
ck(eq(Phi(Phi(Phi(Phi(p0)))),p0),'A channel has period4')
for k in range(1,9):
    hidden=krylov_hidden(Phi,2,k)
    ck(rank(hidden)==1,f'A genuine P3 H{k} rank1')
    ck(all(eq(comm(a,b.H),s.zeros(2)) for a in hidden for b in hidden),f'A P3 R2k zero through depth{k}')
    ck(all(eq(q(a),a) for a in hidden),f'A hidden Q-projected depth{k}')
ck(eq(q(Phi(p0)),-Y/2),'A genuine H1 spans Y')
ck(eq(q(Phi(p1)),Y/2),'A H1 p1 minus')

# Counterexample B: genuine Poisson GKSL generator L=Psi-id, P3 residue nonzero, K=0.
rho_x=(s.eye(2)+X)/2;rho_y=(s.eye(2)+Y)/2
K0=s.Matrix([[1,0],[1,0]])/s.sqrt(2) # |+><0|
K1=s.Matrix([[0,1],[0,I]])/s.sqrt(2) # |+y><1|
Psi=lambda a: K0*a*K0.H+K1*a*K1.H
L2=lambda a:Psi(a)-a
Kret=lambda a:delta(L2(q(L2(delta(a)))))
ck(eq(K0.H*K0+K1.H*K1,s.eye(2)),'B Psi genuine Kraus TP')
ck(eq(Psi(p0),rho_x),'B prepared state X')
ck(eq(Psi(p1),rho_y),'B prepared state Y')
for a in [X,Y,E(2,0,1),E(2,1,0)]:
    ck(eq(Psi(a),s.zeros(2)),'B Psi annihilates offdiag '+str(a))
for a in [p0,p1]:ck(eq(Kret(a),s.zeros(2)),'B K=0 on diagonal basis')
T=s.log(2)
# exp[T(Psi-id)] CPTP via Poisson mixture. Psi^n=Psi^2 for n>=2.
PhiT=lambda a:s.expand(s.Rational(1,2))*(a+T*Psi(a)+(1-T)*Psi(Psi(a)))
for a in [p0,p1,X,Y,Z,s.eye(2)]:
    ck(eq(Psi(Psi(Psi(a))),Psi(Psi(a))),'B Psi cubic stabilizes')
ck(eq(delta(PhiT(p0)+PhiT(p1)),s.eye(2)),'B Phi_T unital on diag aggregate')
h0=q(PhiT(p0));h1=q(PhiT(p1))
ck(rank([h0,h1])==2,'B P3 H1 rank2')
ck(eq(h0,(X+Y+T*(X-Y))/8),'B exact h0 expression')
ck(eq(h1,(X+Y-T*(X-Y))/8),'B exact h1 expression')
rr=delta(comm(h0,h1.H))
ck(eq(rr,I*T*Z/8),'B exact P3 R2 nonzero i log2 Z/8')
ck(rank(res_r2([h0,h1]))==1,'B P3 R2 rank1')
for k in range(2,6):
    ck(rank(krylov_hidden(PhiT,2,k))==2,f'B P3 H{k} full offdiag')
    ck(rank(res_r2(krylov_hidden(PhiT,2,k)))==1,f'B residue rank1 depth{k}')

# Positive bridge witness: coherent hopping plus separately specified CPTP preparation noise.
# For Lmix=-i[X/2,.]+Psi-id, the t->0 sampled semigroup has two independent
# first-order hidden directions and hence nonzero genuine P3 R2 for small t>0.
Lmix=lambda a:L(a)+L2(a)
Kmix=lambda a:delta(Lmix(q(Lmix(delta(a)))))
z0=q(Lmix(p0));z1=q(Lmix(p1))
ck(rank([z0,z1])==2,'C first-order hidden jets resolve both complex edge orientations')
ck(eq(delta(comm(z0,z1.H)),I*Z),'C leading t² P3 commutator residue iZ')
ck(rank([Kmix(p0),Kmix(p1)])==1,'C nonzero dynamical K rank1')
ck(eq(Kmix(p0),(p1-p0)/2),'C projected K action on p0')
ck(eq(Kmix(p1),p0-p1),'C projected K action on p1')
ck(rank([Kmix(p0),Kmix(p1),delta(comm(z0,z1.H))])==1,
   'C small-time conditional equality of P3 R2 and K image')
ck(eq(delta(Lmix(p0)),delta(L2(p0))),'C Lindblad GKSL sum with coherent Hamiltonian')

# Positive conditional bridge theorem: for connected hopping edges resolved as Eij in H_m,
# R_2m equals im K, which is weighted graph divergence. No unconditional equality.
n=5
p=[E(n,i,i) for i in range(n)]
H37=s.diag(0,s.Rational(1,7),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13))
for i in range(4):H37+=(E(n,i,i+1)+E(n,i+1,i))/2
gamma=s.Rational(2,3)
def L37(a):return -I*comm(H37,a)+gamma*(delta(a)-a)
def K37(a):return delta(L37(q(L37(delta(a)))))
W=s.Matrix.hstack(*(s.Matrix([K37(x)[i,i] for i in range(n)]) for x in p))
expected=s.zeros(n)
for i in range(4):
    expected[i,i]-=s.Rational(1,2);expected[i+1,i+1]-=s.Rational(1,2)
    expected[i,i+1]+=s.Rational(1,2);expected[i+1,i]+=s.Rational(1,2)
ck(W==expected,'H37 K projected return -1/2 Laplacian')
ck(W.rank()==4,'H37 K rank4')
ck((W*s.ones(n,1))==s.zeros(n,1),'H37 population sum preserved')
ck(eq(K37(p[0]),(p[1]-p[0])/2),'H37 p0 second derivative')
for j in range(n):
    ck(eq(delta(L37(p[j])),s.zeros(n)),f'H37 L diagonal zero on p{j}')
    ck(eq(delta(L37(L37(p[j]))),K37(p[j])),f'H37 L2=K p{j}')
for i in range(4):
    z=E(n,i,i+1)
    ck(eq(delta(comm(z,z.H)),p[i]-p[i+1]),f'edge certificate {i}-{i+1}')
    ck(vec(p[i]-p[i+1])!=s.zeros(n*n,1),f'edge diff nonzero{i}')
ck(rank([p[i]-p[i+1] for i in range(4)])==4,'graph edge return vectors span K image')
ck(rank([K37(pi) for pi in p]+[p[i]-p[i+1] for i in range(4)])==4,
   'H37 K image equals graph edge divergence span (conditional P3 bridge)')

out={
 'study':'P11-AX15','exact_assertions_passed':len(C),'all_passed':True,'checks':C,
 'original_P3_definition':'R_k=span delta([z,w^dagger]); z in H_i,w in H_j,i+j<=k; H_k=Q span(D,Phi D,...,Phi^k D)',
 'model_A':'unitary X/2, U=(I-iX)/sqrt(2)',
 'model_A_K_rank':rank([K(p0),K(p1)]),
 'model_A_all_P3_Rk':'ZERO analytic periodicity U^4=-I; verified through depth8',
 'model_B':'genuine CPTP measure-prepare Poisson semigroup Phi_{ln 2}',
 'model_B_K_rank':rank([Kret(p0),Kret(p1)]),
 'model_B_P3_R2_rank':rank(res_r2([h0,h1])),
 'model_B_P3_R2_exact_generator':'I*log(2)*Z/8',
 'positive_C_mix':'small-time CPTP semigroup Lmix=-i[X/2,.]+Psi-id, R2=im K=span Z for sufficiently small t>0',
 'H37_dynamical_K_rank':W.rank(),
 'H37_original_P3_Rk':'NOT COMPUTED / OPEN for Phi_t=e^{t L}',
 'positive_bridge':'conditional directed-edge hidden resolution yields R_{2m}=im K for coherent+dephasing graph model',
 'identification_Rk_equals_K_as_operators':False,
 'P3_formalism_modified':False,
 'P6_physical_gate':'OPEN','G2_source_completeness':'OPEN','G3_generativity':'OPEN'}
(Path(__file__).with_name('P11_AX15_exact_results.json')).write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('PASS P11-AX15',len(C),'/',len(C))
print('A K_rank',out['model_A_K_rank'],'P3 all zero')
print('B K_rank',out['model_B_K_rank'],'P3_R2_rank',out['model_B_P3_R2_rank'])
print('H37 K_rank',out['H37_dynamical_K_rank'])
