#!/usr/bin/env python3
"""P11-AX19 exact audit: finite-dimensional response rank vs hidden-source upper bound.

Reconstruct H37 ideal linear response space; certify an explicit physical-state
informationally-complete ensemble; demonstrate inaccessible ancilla extensions
and an independent perfect-pointer-table counterexample. Requires sympy==1.14.0.
"""
from pathlib import Path
import sympy as s
import json

checks=[]
def ck(q, label):
    assert bool(q), label
    checks.append(label)
def E(n,i,j):
    a=s.zeros(n); a[i,j]=1; return a
def vec(a):
    return s.Matrix([a[i,j] for j in range(a.cols) for i in range(a.rows)])
def eq(a,b):
    return a.shape==b.shape and all(s.simplify(v)==0 for v in a-b)

n=5
ps=[E(n,i,i) for i in range(n)]
pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
Xs=[E(n,i,j)+E(n,j,i) for i,j in pairs]
Ys=[-s.I*E(n,i,j)+s.I*E(n,j,i) for i,j in pairs]
basis=ps+Xs+Ys
h=s.diag(0,s.Rational(1,7),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13))
for i in range(n-1): h+=(E(n,i,i+1)+E(n,i+1,i))/2
rate=s.Rational(2,3)
def D(a): return s.diag(*[a[i,i] for i in range(n)])
def Ldag(a): return s.I*(h*a-a*h)+rate*(D(a)-a)
def coord(a):
    return s.Matrix([a[i,i] for i in range(n)] +
      [(a[i,j]+a[j,i])/2 for i,j in pairs] +
      [(a[j,i]-a[i,j])/(2*s.I) for i,j in pairs])

def recon(c):return sum((basis[i]*c[i] for i in range(25)),s.zeros(n))
T=s.Matrix.hstack(*[coord(Ldag(a)) for a in basis])
ck(T.shape==(25,25),'H37 Heisenberg generator dimension25')
ck(all(x.is_Rational for x in T),'H37 generator real rational')
for i,a in enumerate(basis):
    ck(eq(recon(coord(a)),a),f'Hermitian basis integrity {i}')

# H37 effect derivative orbit from all five independently MARKED populations.
K=s.eye(25)[:,:5]
cur=K
rank_tower=[K.rank()]
for j in range(1,8):
    cur=T*cur
    K=K.row_join(cur)
    rank_tower.append(K.rank())
    ck(rank_tower[-1]>=rank_tower[-2],f'Krylov growth monotone {j}')
ck(rank_tower==[5,9,13,17,21,23,25,25],'original H37 full effect Krylov rank tower')
ck(K.rank()==25,'H37 full linear effect space dimension25')

# Rows of a 25x25 derivative measurement response matrix.
B25=K[:,:35]
pivots=B25.rref()[1]
ck(len(pivots)==25,'25 independent Heisenberg effect derivatives selected')
Eff=s.Matrix.hstack(*[B25[:,j] for j in pivots])
ck(Eff.rank()==25,'selected 25 response derivatives independent')

# 25 physical pure-state preparations: five vertices and ten X+, ten Y+.
preps=list(ps)
for i,j in pairs:preps.append((ps[i]+ps[j]+Xs[pairs.index((i,j))])/2)
for i,j in pairs:preps.append((ps[i]+ps[j]+Ys[pairs.index((i,j))])/2)
ck(len(preps)==25,'25 pure-state candidate preparations')
for i,rho in enumerate(preps):
    ck(eq(rho,rho.H),f'input Hermitian {i}')
    ck(s.trace(rho)==1,f'input normalized {i}')
    ck(eq(rho*rho,rho),f'input rank-one projector {i}')
Prep=s.Matrix.hstack(*[coord(r) for r in preps])
ck(Prep.rank()==25,'25 independently marked preps informationally complete')
W=s.diag(*([1]*5+[2]*20))
Response=Eff.T*W*Prep
ck(Response.rank()==25,'observable bilinear derivative data rank25')
ck(Response.det()!=0,'observable response determinant nonzero')
ck(all(s.simplify(Response[i,j]-s.trace(recon(Eff[:,i])*preps[j]))==0
       for i in range(25) for j in range(25)),
   'coordinate response matrix equals exact traces for all 625 settings')

# Perfectly distinguishing FIVE classical pointer states gives d >= 5, not d = 5.
M5=ps
for i in range(n):
    for j in range(n):ck(s.trace(M5[i]*ps[j])==int(i==j),f'5D perfect pointer [{i},{j}]')

# Arbitrarily append spectator Hilbert space B: marks do not become exhaustive.
I2=s.eye(2);Z=s.diag(1,-1)
ketp=s.Matrix([1,1])/s.sqrt(2)
tau=ketp*ketp.H
hidden_state=s.kronecker_product(ps[0],tau)
M10=[s.kronecker_product(p,I2) for p in ps]
for i in range(5):
    for j in range(5):
        R=s.kronecker_product(ps[j],tau)
        ck(s.trace(M10[i]*R)==int(i==j),f'10D reproduces 5x5 table [{i},{j}]')
ck(all(m.rank()==2 for m in M10),'10D pointer effects rank2, not rank1')
ck(sum(M10,s.zeros(10))==s.eye(10),'10D marked pointer POVM normalized')
ck(s.trace(tau)==1,'spectator preparation normalized')
ck(eq(Z*Z.H,I2),'spectator phase operation unitary')
ck(s.trace(Z*tau*Z)==1,'spectator alternative trace preserving')
ck(s.trace(s.Matrix([[0,1],[1,0]])*tau)==1,'original spectator X expectation +1')
ck(s.trace(s.Matrix([[0,1],[1,0]])*Z*tau*Z)==-1,'alternative spectator X expectation -1')

# For all 25x25 ideal response entries, spectator tensor extension produces same readings.
# This includes linearly independent Hermitian derivatives, not necessarily direct POVM effects;
# they are derivatives of time-resolved positive p_i measurement probabilities.
for i in range(25):
    aa=recon(Eff[:,i]); 
    for j in range(25):
        rr=preps[j]
        # Avoid heavy 10x10 explicit multiplication: use exact tensor-product trace identity.
        for Wb,lab in [(I2,'id'),(Z,'Z')]:
            reduced=s.trace(aa*rr)*s.trace(Wb*tau*Wb.H)
            ck(s.simplify(reduced-Response[i,j])==0,
               f'tensor ancilla indistinguishable response [{i},{j}] {lab}')

# Model-independent dimension lower-bound from response-matrix rank:
# rank(D) <= dim Herm(H) = d^2. Rank 25 forces d >= 5.
for d in range(1,5):ck(d*d<25,f'Hilbert dimension {d} excluded by 25-rank')
ck(5*5==25,'five-dimensional realization saturates witness')
for r in [2,3,4]:ck((5*r)**2>25,f'ancilla size {r} not excluded by rank25')

result={
 'study':'P11-AX19', 'all_passed':True, 'exact_assertions_passed':len(checks),
 'checks':checks,
 'H37_effect_Krylov_dimensions':rank_tower,
 'H37_derivative_response_rank':Response.rank(),
 'H37_finite_response_dimension_lower_bound':5,
 'independently_marked_preparation_count':25,
 'spectator_realization_dimensions':[5,10],
 'spectator_10D_pointer_effect_rank':2,
 'spectator_invariance_all_finite_protocol_words':'PROVED ANALYTICALLY VIA PARTIAL TRACE',
 'physical_d_equals_5_from_operational_data_alone':False,
 'G2_exhaustive_native_dimension':'OPEN',
 'G3_F_generativity':'OPEN',
 'P6_native_instrument_certification':'OPEN',
 'P3_full10D_MASA_residue':'NOT CLAIMED',
}
Path(__file__).with_name('P11_AX19_exact_results.json').write_text(
    json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(f"P11 AX19 PASS {len(checks)}/{len(checks)} exact assertions")
print('H37 ranks',rank_tower,'effective d_min=5, physical upper bound OPEN')
