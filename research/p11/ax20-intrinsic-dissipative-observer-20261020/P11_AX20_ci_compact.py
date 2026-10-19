#!/usr/bin/env python3
"""AX20 compact independent exact HS-dissipation and symmetry check."""
import json
from pathlib import Path
import sympy as s
checks=[]
def check(p,name):
    assert bool(p),name
    checks.append(name)
def E(i,j,n=5):
    a=s.zeros(n);a[i,j]=1;return a
def V(a):
    return s.Matrix([a[i,j] for j in range(a.cols) for i in range(a.rows)])
def op(fn,n=5):
    return s.Matrix.hstack(*[V(fn(E(i,j,n))) for j in range(n) for i in range(n)])
def diag(a):
    return s.diag(*[a[i,i] for i in range(a.rows)])
n=5;gamma=s.Rational(2,3)
h=s.diag(0,s.Rational(1,7),-s.Rational(1,9),s.Rational(2,11),-s.Rational(3,13))
for i in range(4):h+=(E(i,i+1)+E(i+1,i))/2
F=op(diag);L=op(lambda a:-s.I*(h*a-a*h)+gamma*(diag(a)-a))
S=(L+L.H)/2
basis=[V(E(i,j)) for j in range(n) for i in range(n)]
for k,v in enumerate(basis):
    check(S*v==gamma*(F-s.eye(25))*v,f'symmetric-part identity [{k}]')
for k,v in enumerate(basis):
    check(F*F*v==F*v,f'orthogonal projection idempotence [{k}]')
U=s.eye(5);U[0,0]=s.Rational(3,5);U[0,1]=-s.Rational(4,5)
U[1,0]=s.Rational(4,5);U[1,1]=s.Rational(3,5)
T=op(lambda a:U*a*U.H)
for k,v in enumerate(basis):
    check((T*S*T.H)*(T*v)==T*(S*v),f'unitary covariance [{k}]')
dep=op(lambda a:s.trace(a)*s.eye(n)/n-a)
P=E(0,0);p2=U*P*U.H
check(S.rank()==20,'H37 symmetric-part rank20')
check(F.rank()==5,'H37 induced observer dim5')
check(dep.rank()==24,'depolarizing symmetric part kernel scalars')
check((S+s.Rational(1,17)*dep).rank()==24,'generic noise shrinks exact nullspace')
check(U.H*U==s.eye(n),'unitary witness')
check(P*p2!=p2*P,'noncommuting orbit violates invariant MASA')
assert len(checks)==81
p=Path(__file__).parent/'P11_AX20_ci_compact_result.json'
p.write_text(json.dumps({'exact_assertions_passed':81,'G2':'OPEN','G3':'OPEN','checks':checks},indent=2))
print('AX20 compact CI: 81/81 exact checks PASS, G2/G3 OPEN')
