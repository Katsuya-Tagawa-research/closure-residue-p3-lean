#!/usr/bin/env python3
"""H75 finite AX-OA subcatalog minimum and calibrated phase witness.
Imports prior independent phase/certificate CI from #165.
"""
from pathlib import Path
import importlib.util
import itertools
from sympy.polys.matrices import DomainMatrix

parent=Path(__file__).resolve().parents[1]/'h75-phase-orientation-20261020'/'H75_Phase_CI_Compact_Check.py'
assert parent.exists(),f'parent H75 phase audit not found: {parent}'
spec=importlib.util.spec_from_file_location('h75_phase_parent',parent)
p=importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
C=p.c; R=p.R; s=p.s
assert C.shape==(36,18)
def rank(a):return DomainMatrix.from_Matrix(a).convert_to(s.QQ).rank()
pre={}
for n in range(1,5):
 for ix in itertools.combinations(range(4),n):
  pre[ix]=rank(C[[i for i in range(36) if (i//9) in ix],:])
assert pre[(0,1,2,3)]==18
assert all(v<18 for k,v in pre.items() if len(k)<4)
assert pre[(0,1,2)]==15
assert max(v for k,v in pre.items() if len(k)==3)==16
post={}
for n in range(1,4):
 for ix in itertools.combinations(range(3),n):
  post[ix]=rank(C[[i for i in range(36) if ((i//3)%3) in ix],:])
assert post[(0,1,2)]==18
assert [post[(0,1)],post[(0,2)],post[(1,2)]]==[13,17,17]
site={}
for n in range(1,4):
 for ix in itertools.combinations(range(3),n):
  site[ix]=rank(C[[i for i in range(36) if (i%3) in ix],:])
assert all(site[k]==18 for k in ((0,1),(0,2),(1,2)))
assert all(site[(j,)]<18 for j in range(3))
# A signed imaginary coherence state requires INDEPENDENT phase preparation.
rho=s.eye(6)/6+p.h18[4]/12
assert rho.H==rho and s.trace(rho)==1
assert rho.eigenvals()=={R(1,12):1,R(1,4):1,R(1,6):4}
vec=s.Matrix([s.trace(h*rho)/s.trace(h*h) for h in p.h18])
pu=(p.c[3,:]*vec)[0]
pc=(p.conj[3,:]*vec)[0]
pr=(p.real[3,:]*vec)[0]
assert (pu,pc,pr)==(R(265,867),R(313,867),R(1,3))
assert pu-pc==-R(16,289)
assert (p.conj[3,:]*s.Matrix([-z if j in p.imag else z for j,z in enumerate(vec)]))[0]==pu
print('H75 AX-OA MINIMAL CATALOG PASS: all four PRE + all three POST required among the fixed settings; any two sites suffice; phase contrast -16/289. G2/G3 OPEN')
