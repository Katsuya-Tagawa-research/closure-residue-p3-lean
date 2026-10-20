#!/usr/bin/env python3
"""Exact 18-dimensional H75/H81 global conditional access certificate.

The 6D input domain is BLOCK DIAGONAL Hermitian M3 ⊕ M3; source, ports,
sequence and POVM exactly specified. No claim of physical native availability,
complete microscopic M6 tomography, F-generated access, KKS->GR, or
verification of the externally reported native 15-vector/GT metric formulas.
"""
import json
import csv
from pathlib import Path
import sympy as s

I=s.I
R=s.Rational
N=6
checks=0

def ck(c,msg):
    global checks
    if c is not True and c!=s.true:
        raise AssertionError(f'{msg}: {c}')
    checks+=1

def simp(A):return A.applyfunc(s.simplify)
def ad(V,X):return simp(V*X*V.H)
def E(i,j,n):
    a=s.zeros(n);a[i,j]=1;return a

O=s.Matrix([[R(2,3),R(2,3),-R(1,3)],[-R(2,3),R(1,3),-R(2,3)],[-R(1,3),R(2,3),R(2,3)]])
U=s.diag(I,1,I)*O
M0=s.diag(1,R(3,5),R(3,5)); M1=s.diag(0,R(4,5),R(4,5))
W=s.kronecker_product(s.Matrix([[R(3,5),-R(4,5)],[R(4,5),R(3,5)]]),s.eye(3))
SW=E(0,1,3)+E(1,0,3)+E(2,2,3)
F=s.diag(s.eye(3),SW)
A=E(0,1,3)-E(1,0,3)
B=E(2,1,3)-E(1,2,3)

def cav(K,t):return simp((s.eye(3)+t*K)*(s.eye(3)-t*K).inv())
def V(x,y):return s.kronecker_product(s.eye(2),cav(A,x)*cav(B,y))
I6=s.eye(6)
VA=V(R(1,4),s.S.Zero)
VAB=V(R(1,4),R(1,3))
Vhalf=V(s.S.Zero,R(1,2))
PRE=[('Identity',I6),
     ('F',F),
     ('V_A then F',F*VA),
     ('W then F then V_B(1/2) then W then F',F*W*Vhalf*F*W)]
POST=[('Identity',I6),('V_A(1/4)',VA),('V_AB(1/4,1/3)',VAB)]
Q=[s.kronecker_product(s.eye(2),E(j,j,3)) for j in range(3)]
Ks=[s.kronecker_product(E(a,b,2),U*Ms[a]) for a in range(2) for b in range(2) for Ms in ((M0,M1),)]

ck(simp(U*U.H)==s.eye(3),'H75 U unitary')
ck(M0.H*M0+M1.H*M1==s.eye(3),'H75 Kraus complete')
ck(simp(sum((K.H*K for K in Ks),s.zeros(6)))==I6,'H75 microscopic TP')
for nm,Vv in PRE+POST:
    ck(simp(Vv.H*Vv)==I6,f'{nm} unitary')
for j,Qj in enumerate(Q):
    ck(Qj.H==Qj and Qj*Qj==Qj,f'Q{j} positive projector')
ck(sum(Q,s.zeros(6))==I6,'positive readout POVM complete')

def phi(X):return simp(sum((K*X*K.H for K in Ks),s.zeros(6)))
def phi_star(X):return simp(sum((K.H*X*K for K in Ks),s.zeros(6)))

# An exact real basis of Hermitian M3, and direct-sum input basis (18 elements).
HB=[E(j,j,3) for j in range(3)]
for i,j in [(0,1),(0,2),(1,2)]:
    HB.append(E(i,j,3)+E(j,i,3))
    HB.append(I*(E(i,j,3)-E(j,i,3)))
ck(len(HB)==9 and all(a==a.H for a in HB),'nine Hermitian basis elements')
HBD=[]
for block in range(2):
    for a in HB:
        HBD.append(s.diag(a,s.zeros(3)) if block==0 else s.diag(s.zeros(3),a))
ck(len(HBD)==18 and all(a==a.H for a in HBD),'block diagonal 18 real input directions')

row_names=[];rows=[]
for pren,pre in PRE:
    for postn,post in POST:
        for j,Qj in enumerate(Q):
            heff=simp(pre.H*phi_star(post.H*Qj*post)*pre)
            # The coefficient of the output probability on each Hermitian basis direction.
            row=[s.simplify(s.trace(heff*H)) for H in HBD]
            ck(all(x.is_Rational for x in row),f'Gaussian-rational output for {pren}/{postn}/Q{j}')
            row_names.append([pren,postn,j]);rows.append(row)
C=s.Matrix(rows)
ck(C.shape==(36,18),'36 positive physical setting rows by 18 Hermitian input directions')
# Gaussian elimination on the transpose selects exactly 18 independent physical effects.
_,pivots=C.T.rref()
ck(len(pivots)==18,f'full rank 18, found {len(pivots)}')
subset_ranks=[]
for number in range(1,5):
    rr=C[:9*number,:].rank()
    subset_ranks.append(rr)
    ck(rr==[6,10,15,18][number-1],f'prefix rank {number} = {rr}')
selected=C[list(pivots),:]
ck(selected.shape==(18,18),'square certificate of 18 readout effects')
# Rational invertibility proof: nonzero modular determinant after rational reduction.
prime=1000000007

def rmod(x):
    xx=s.Rational(x)
    assert int(xx.q)%prime
    return (int(xx.p)%prime)*pow(int(xx.q)%prime,-1,prime)%prime

def detmod(mat,p):
    a=[[rmod(mat[i,j]) for j in range(mat.cols)] for i in range(mat.rows)]
    n=len(a); sign=1;det=1
    for i in range(n):
        pivot=next((k for k in range(i,n) if a[k][i]%p),None)
        if pivot is None:return 0
        if pivot!=i:
            a[i],a[pivot]=a[pivot],a[i]
            sign=-sign
        v=a[i][i]%p;det=det*v%p;inv=pow(v,-1,p)
        for k in range(i+1,n):
            factor=a[k][i]*inv%p
            if factor:
                for j in range(i+1,n):a[k][j]=(a[k][j]-factor*a[i][j])%p
            a[k][i]=0
    return sign*det%p

moddet=detmod(selected,prime)
with Path(__file__).with_name('H75_Global_Access_18x18_Certificate.csv').open('w',newline='') as f:
    cw=csv.writer(f)
    for i in range(selected.rows):cw.writerow([str(selected[i,j]) for j in range(selected.cols)])
ck(moddet!=0,f'nonzero modular determinant mod {prime}')

# Construct the user-supplied fixed-orbit pair and independently verify that
# its original observed collision is broken by this new globally IC certificate.
rad=s.sqrt(57)

def b(a,b,p,q):return s.Matrix([[a,I*p,0],[-I*p,b,I*q],[0,-I*q,a]])
a=R(3,25); bmid=R(11,25); b1=R(8,75)
rho=s.diag(b(a,bmid,rad/50,0),b(b1,b1,0,R(8,75)))
sigma=s.diag(b(a,bmid,257*rad/38450,R(2736,19225)),b(b1,b1,256*rad/19225,-R(2056,57675)))
delta=simp(sigma-rho)
for k in range(2):
    v=slice(3*k,3*k+3)
    ck(rho[v,v].charpoly().as_expr()==sigma[v,v].charpoly().as_expr(),f'pair fixed orbit block{k}')
ck(delta!=s.zeros(6),'distinct fixed-orbit states')
ck(phi(delta)==s.zeros(6),'reset-first erasure')
# First certificate contains some nonzero contrasts: explicitly verify selection.
def record(X):return s.Matrix([s.simplify(s.trace(Qj*ad(post,phi(ad(pre,X))))) for _,pre in PRE for _,post in POST for Qj in Q])
contrasts=record(delta)
ck(any(s.simplify(t)!=0 for t in contrasts),'36-entry operational record separates prior pair')
ck(contrasts==C*s.Matrix([s.trace(b*delta)/(s.trace(b*b)) for b in HBD]),'18-basis readout reproduces analytic state pair')

# 3 extra demonstrations: block-diagonal preparation scope only, conditional rank
# suffices for every function on this domain, plus the physical source can wipe
# out off-block coherences, so no full M6 tomography is claimed.
for ix in [0,1,2]:
    H=s.zeros(6);H[ix,3+ix]=1;H[3+ix,ix]=1
    ck(all(s.simplify(s.trace(h*H))==0 for h in [HBD[j] for j in range(18)]),'offflag coherence orthogonal to domain')

results={
  'title':'H75 / AX-OA finite global informational-completeness certificate on block-diagonal M3+M3',
  'date':'2026-10-20',
  'exact_assertions_passed':checks,
  'all_passed':True,
  'matrix_shape':[36,18],
  'matrix_rank_exact':18,
  'ranks_by_added_prereset_programs':subset_ranks,
  'chosen_18_row_indices_zero_based':list(pivots),
  'chosen_18_row_labels':[row_names[j] for j in pivots],
  'rational_matrix_prime':prime,
  'nonzero_rational_determinant_mod_prime':moddet,
  'controls_before_reset':[a for a,_ in PRE],
  'controls_after_reset':[a for a,_ in POST],
  'site_readout_indices':[0,1,2],
  'full_block_diag_Hermitian_dimension':18,
  'fixed_U3xU3_KKS_orbit_embedded':'YES',
  'fixed_orbit_pair_sep_in_36_records':'YES',
  'all_metric_maps_on_domain_set_theoretic_descent':'YES when augmented certificate 36-records physically permitted',
  'smooth_stable_descent':'CONDITIONAL on metric regularity; finite linear left inverse is bounded',
  'pre_reset_long_control_word_physical_certification':'OPEN',
  'arbitrary_full_M6_correlated_flag_tomography':'NOT CLAIMED',
  'native_15_observation_and_GT_metric_original_formulas':'NOT INDEPENDENTLY RECOMPUTED',
  'G2_physical_hardware_provenance':'OPEN',
  'G3_F_generated_access':'OPEN',
  'KKS_to_ADM_and_physical_soldering':'OPEN',
  'qualification':'This is a conditional mathematical 36-setting effect IC result with pre-reset W/F/real-site pulse interleaving. Same original H75 reset, explicit existing gate matrices. The longer pre-reset schedule is additional hardware-access assumption.'
}
Path(__file__).with_name('H75_Global_Access_Exact_Results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print('EXACT',checks,'checks PASS; 36 records / 18 Hermitian directions, rank=',len(pivots))
print('Exact modular determinant:',moddet,'mod',prime)
print('Selected row indices:',pivots)
print('Counterpair separated:',[i for i,x in enumerate(contrasts) if x!=0][:8])
print('Conditional metric descent on full fixed orbit: yes; hardware and F origin OPEN')
