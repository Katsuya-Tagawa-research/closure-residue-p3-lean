#!/usr/bin/env python3
"""EXACT original H75 AX-OA five typed-port sensitivity / non-deletion.

Same unmodified 4-Kraus six-level source once for all 10 typed protocols.
Each of five pairs differs in precisely ONE typed operational coordinate.
Rational Born probabilities checked without float or external hardware claim.
"""
import sympy as sp

R,I=sp.Rational,sp.I
I2,I3,I6=sp.eye(2),sp.eye(3),sp.eye(6)
E=lambda i,j:I3[:,i]*I3[j,:]
O=sp.Matrix([[R(2,3),R(2,3),-R(1,3)],
             [-R(2,3),R(1,3),-R(2,3)],
             [-R(1,3),R(2,3),R(2,3)]])
U=sp.diag(I,1,I)*O
M=[sp.diag(1,R(3,5),R(3,5)),sp.diag(0,R(4,5),R(4,5))]
K=[sp.kronecker_product(I2[:,a]*I2[b,:],U*M[a])
   for a in range(2) for b in range(2)]
assert sum((k.H*k for k in K),sp.zeros(6))==I6

def source(X):
    return sum((k*X*k.H for k in K),sp.zeros(6))

S=E(0,1)+E(1,0)+E(2,2)
F=sp.kronecker_product(sp.diag(1,0),I3) + sp.kronecker_product(sp.diag(0,1),S)
assert F.T*F==I6 and F==F.H
def ket(a,j):
    return sp.kronecker_product(I2[:,a],I3[:,j])
def rho(a,j):
    w=ket(a,j)
    return w*w.H
def Q(j):
    return sp.kronecker_product(I2,E(j,j))

plus=(I3[:,0]+I3[:,2])/sp.sqrt(2)
Qplus=sp.kronecker_product(I2,plus*plus.H)
assert Qplus.H==Qplus and Qplus**2==Qplus

L=[sp.kronecker_product(I2,E(j,j)) for j in range(3)]
assert sum((x.H*x for x in L),sp.zeros(6))==I6
def identity_instrument(X):
    return X
def dephase_instrument(X):
    return sum((x*X*x.H for x in L),sp.zeros(6))
# A true nonunitary channel: coherence between site |0> and |2> disappears.
offdiag=sp.kronecker_product(I2,E(0,2))
assert dephase_instrument(offdiag)==sp.zeros(6)
assert identity_instrument(offdiag)==offdiag

# The five coordinates of each TYPED experiment are
# (preparation, control, post-source instrument, schedule, binary POVM effect).
# The H75 CPTP source is kept fixed and executed exactly once.
def evaluate(c):
    state,control,instr,sched,effect=c
    assert state.H==state and state.trace()==1
    assert control.H*control==I6
    assert effect.H==effect and effect*effect==effect
    assert (I6-effect).H==I6-effect
    if sched=="pre":
        out=instr(source(control*state*control.H))
    elif sched=="post":
        out=instr(control*source(state)*control.H)
    else:
        raise AssertionError("bad schedule")
    assert sp.simplify(out.trace())==1
    ans=sp.simplify(sp.trace(effect*out))
    assert ans.is_Rational and 0<=ans<=1
    return ans

Id=I6
pre="pre"
post="post"
ID=identity_instrument
DELTA=dephase_instrument
pairs={
    "Preparation":(
        (rho(0,0),Id,ID,pre,Q(1)),
        (rho(0,1),Id,ID,pre,Q(1))),
    "Control":(
        (rho(1,0),Id,ID,pre,Q(1)),
        (rho(1,0),F,ID,pre,Q(1))),
    "Instrument":(
        (rho(0,0),Id,ID,pre,Qplus),
        (rho(0,0),Id,DELTA,pre,Qplus)),
    "Scheduling":(
        (rho(1,0),F,ID,pre,Q(1)),
        (rho(1,0),F,ID,post,Q(1))),
    "Readout":(
        (rho(0,1),Id,ID,pre,Q(1)),
        (rho(0,1),Id,ID,pre,Q(2)))
}
expected={
    "Preparation":(R(4,9),R(1,9)),
    "Control":(R(4,9),R(1,9)),
    "Instrument":(R(1,18),R(5,18)),
    "Scheduling":(R(1,9),R(4,9)),
    "Readout":(R(1,9),R(4,9))
}
assert len(pairs)==5 and set(pairs)==set(expected)
order={"Preparation":0,"Control":1,"Instrument":2,"Scheduling":3,"Readout":4}
for name,(a,b) in pairs.items():
    k=order[name]
    for j in range(5):
        if j!=k:
            if j in (0,1,4):
                assert a[j]==b[j]
            else:
                assert a[j] is b[j] if j==2 else a[j]==b[j]
    # Component k changes without collapsing to identical abstract resource.
    if k in (0,1,4):
        assert a[k]!=b[k]
    else:
        assert a[k] is not b[k] if k==2 else a[k]!=b[k]
    actual=(evaluate(a),evaluate(b))
    assert actual==expected[name]
    assert actual[0]!=actual[1]   # non-factorization after forgetting coordinate k

# Independently verify the simple analytic site probability vectors.
site0=[sp.simplify((U[:,0].H*E(j,j)*U[:,0])[0]) for j in range(3)]
site1=[sp.simplify((U[:,1].H*E(j,j)*U[:,1])[0]) for j in range(3)]
assert site0==[R(4,9),R(4,9),R(1,9)]
assert site1==[R(4,9),R(1,9),R(4,9)]
assert evaluate(pairs["Instrument"][0])==R(1,18)
assert evaluate(pairs["Instrument"][1])==R(5,18)

# Gate port remains original H75 conditional SWAP; source unchanged.
assert F*rho(1,0)*F.H==rho(1,1)
# H75 output of site0 is confined to flag0, thus post-source F is trivial.
assert F*source(rho(1,0))*F.H==source(rho(1,0))

for label,(v,w) in expected.items():
    print(f"PASS original H75 {label:12s}: {v} vs {w}; difference={v-w}")
print("PASS: all five typed coordinates have an exact witness of non-deletion")
print("BOUNDARY: this does NOT prove axiomatic independence or unique AX-OA minimality")
print("OPEN: F-origin of operational grants, P6 provenance, P9/P11 full geometry")
