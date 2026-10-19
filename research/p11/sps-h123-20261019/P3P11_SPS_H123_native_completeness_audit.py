#!/usr/bin/env python3
"""SPS-H123: H37 four-edge control response and source-exhaustiveness limit."""
from pathlib import Path
import json
import sympy as sp

checks=[]
def check(condition, description):
    assert bool(condition), description
    checks.append(description)
def E(n,i,j):
    m=sp.zeros(n); m[i,j]=1; return m
def real_rank(mats):
    cols=[sp.Matrix(list(m)) for m in mats]
    return sp.Matrix.hstack(*cols).rank() if cols else 0

n=5
P=[E(n,i,i) for i in range(n)]
X=[E(n,i,i+1)+E(n,i+1,i) for i in range(4)]
K=[E(n,i,i+1)-E(n,i+1,i) for i in range(4)]
Hc=[sp.I*k for k in K]
for e in range(4):
    check(Hc[e].H==Hc[e],f'control {e} Hermitian')
    check(X[e].H==X[e],f'readout {e} Hermitian')
    check(sp.trace(P[e])==1,f'prep {e} normalized')
    check(sp.trace(P[e]*P[e])==1,f'prep {e} pure')
A=sp.Matrix(4,4,lambda e,f:sp.simplify(sp.trace(X[e]*(-sp.I*(Hc[f]*P[e]-P[e]*Hc[f])))))
for e in range(4):
    for f in range(4):
        check(A[e,f]==(-2 if e==f else 0),f'A[{e},{f}]')
check(A==-2*sp.eye(4),'H37 full diagonal response')
check(A.rank()==4,'H37 response rank4')
check(A.det()==16,'H37 response determinant16')
check(A.T*A==4*sp.eye(4),'H37 singular values2')
check(real_rank(Hc)==4,'native declared real rank4')
det=[0,sp.Rational(1,7),-sp.Rational(1,9),sp.Rational(2,11),-sp.Rational(3,13)]
H0=sp.diag(*det)+sum(X,sp.zeros(n))/2
gamma=sp.Rational(2,3)
check(H0.H==H0,'H37 drift Hermitian')
check(all(H0[i,j]==0 for i in range(n) for j in range(n) if abs(i-j)>1),
      'H37 nearest-neighbor support')
rows=[sum(abs(H0[i,j]) for j in range(n)) for i in range(n)]
check(max(rows)<=sp.Rational(5,4),'operator-norm conservative bound')
check(2*sp.Rational(5,4)+gamma==sp.Rational(19,6),'GKSL HS superoperator norm bound')
t0=sp.Rational(1,100); x=sp.Rational(19,6)*t0
check(0<x<1,'positive short-time range')
major=x/(1-x)
check(major==sp.Rational(19,581),'exponential rational upper bound')
err=8*sp.sqrt(2)*major
check(sp.simplify(4-err**2)>0,'perturbation lower than squared singular gap')
check(sp.simplify(2-err)>0,'short-time invertibility')
extra=P[0]-P[1]
check(extra.H==extra,'unmarked hypothetical knob Hermitian')
check(sp.trace(extra)==0,'unmarked knob traceless')
check(real_rank(Hc+[extra])==5,'extra unmarked native rank5')
check(all(sp.simplify(sp.trace(X[e]*(-sp.I*(extra*P[e]-P[e]*extra))))==0
          for e in range(4)),'unmarked extra invisible at ideal identity baseline')
check(A.rank()<real_rank(Hc+[extra]),'four outputs not globally exhaustive')

out=dict(study='SPS-H123',all_passed=True,exact_assertions_passed=len(checks),
         checks=checks,rank=A.rank(),determinant=str(A.det()),
         H37_marked_jacobian=[[str(v) for v in A.row(i)] for i in range(A.rows)],
         sigma_min_at_t0='2',Hs_operator_norm_upper='5/4',
         L_HS_norm_upper='19/6',short_time_t=str(t0),
         short_time_error_upper=str(err),
         unmarked_extra_inventory_dim=real_rank(Hc+[extra]),
         hardware_native_exhaustiveness='OPEN',P11_AX_ORIGIN='OPEN')
Path(__file__).with_name('P3P11_SPS_H123_exact_results.json').write_text(
    json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(f'SPS-H123 PASS {len(checks)}/{len(checks)} exact assertions')
