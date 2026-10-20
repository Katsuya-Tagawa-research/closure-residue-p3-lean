#!/usr/bin/env python3
"""H75 exact single-use AX-OA behavioral normal form and rank-nine bottleneck.

Uses original four six-level Kraus operators. Checks:
- source ranks 9 on whole Herm(6) / 18D native Herm(3)+Herm(3);
- phase-coherent POVM effects with same Phi* pullback;
- distinct native density states in source kernel;
- nonunitary CPTP instrument/readout absorption on all 36 matrix units;
- PRE and POST control normal form on all 36 matrix units, for multiple
  controls, instruments and effects.
No physical F-generated resource or unique AX-OA decomposition is claimed.
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

def Phi(X):
    return sum((k*X*k.H for k in K),sp.zeros(6))
def Phi_star(X):
    return sum((k.H*X*k for k in K),sp.zeros(6))
def flag_trace(X):
    return X[:3,:3]+X[3:,3:]
def original_output(Y):
    out=sp.zeros(6)
    out[:3,:3]=U*M[0]*Y*M[0]*U.H
    out[3:,3:]=U*M[1]*Y*M[1]*U.H
    return out

# Exact H75 source factorization on the full complex operator space.
full_basis=[I6[:,i]*I6[j,:] for i in range(6) for j in range(6)]
assert len(full_basis)==36
for X in full_basis:
    assert Phi(X)==original_output(flag_trace(X))
assert M[0].det()!=0

S_full=sp.Matrix.hstack(*[Phi(X).reshape(36,1) for X in full_basis])
assert S_full.shape==(36,36)
assert S_full.rank()==9

native_basis=[]
for flag in range(2):
    for i in range(3):
        for j in range(3):
            X=sp.zeros(6)
            X[3*flag+i,3*flag+j]=1
            native_basis.append(X)
assert len(native_basis)==18
S_native=sp.Matrix.hstack(*[Phi(X).reshape(36,1) for X in native_basis])
assert S_native.shape==(36,18)
assert S_native.rank()==9
assert 36-S_full.rank()==27
assert 18-S_native.rank()==9

# Physical input states that differ but give exactly the same source output.
Xflag=sp.diag(-1,-1,-1,1,1,1)
rho_plus,rho_minus=I6/6+Xflag/12,I6/6-Xflag/12
assert rho_plus!=rho_minus
assert rho_plus.trace()==rho_minus.trace()==1
assert all(x>0 for x in list(rho_plus.diagonal())+list(rho_minus.diagonal()))
assert Phi(rho_plus)==Phi(rho_minus)

# Distinct PSD effects with eigenvalues 1/4 and 3/4, and same Phi* effect.
T=sp.kronecker_product(sp.Matrix([[0,1],[1,0]]),I3)
E_plus,E_minus=I6/2+T/4,I6/2-T/4
assert E_plus!=E_minus and E_plus.H==E_plus and E_minus.H==E_minus
assert set(E_plus.eigenvals())=={R(1,4),R(3,4)}
assert set(E_minus.eigenvals())=={R(1,4),R(3,4)}
assert Phi_star(E_plus)==I6/2 and Phi_star(E_minus)==I6/2
assert Phi_star(E_plus-E_minus)==sp.zeros(6)

# The original conditional SWAP, plus a valid nonunitary site dephasing
# one-outcome instrument and an imported site-coherent readout Q.
S=E(0,1)+E(1,0)+E(2,2)
F=sp.kronecker_product(sp.diag(1,0),I3)+sp.kronecker_product(sp.diag(0,1),S)
assert F.H*F==I6
site_coherent=(I3[:,0]+I3[:,2])/sp.sqrt(2)
Q_coherent=sp.kronecker_product(I2,site_coherent*site_coherent.H)
Q_site=sp.kronecker_product(I2,E(1,1))
L=[sp.kronecker_product(I2,E(j,j)) for j in range(3)]
assert sum((k.H*k for k in L),sp.zeros(6))==I6
def identity_inst(X):return X
def identity_star(X):return X
def dephase(X):return sum((k*X*k.H for k in L),sp.zeros(6))
def dephase_star(X):return sum((k.H*X*k for k in L),sp.zeros(6))

flag_site_coherence=sp.kronecker_product(I2,E(0,2))
assert dephase(flag_site_coherence)==sp.zeros(6)
assert identity_inst(flag_site_coherence)==flag_site_coherence
Q_effective=dephase_star(Q_coherent)
assert Q_effective==sp.kronecker_product(I2,(E(0,0)+E(2,2))/2)
assert Q_effective!=Q_coherent and Q_effective*Q_effective!=Q_effective
for X in full_basis:
    # Even after source, all input operators obey Heisenberg absorption.
    assert sp.simplify(sp.trace(Q_coherent*dephase(Phi(X)))
                       -sp.trace(Q_effective*Phi(X)))==0

# Two distinct (preparation,pre-source control) resources give equal source outputs.
rho_10=sp.kronecker_product(I2[:,1]*I2[1,:],E(0,0))
rho_11=sp.kronecker_product(I2[:,1]*I2[1,:],E(1,1))
assert F*rho_10*F.H==rho_11
assert Phi(F*rho_10*F.H)==Phi(rho_11)

# The universal normal form is checked on all 36 operator basis elements
# for two controls, two genuinely different instruments, three readouts,
# and both possible schedules.
for C in (I6,F):
    for inst,adj in ((identity_inst,identity_star),(dephase,dephase_star)):
        for Q in (Q_coherent,Q_site,E_plus):
            Eeff=adj(Q)
            assert Eeff.H==Eeff
            for X in full_basis:
                pre=sp.trace(Q*inst(Phi(C*X*C.H)))
                post=sp.trace(Q*inst(C*Phi(X)*C.H))
                assert sp.simplify(pre-sp.trace(Eeff*Phi(C*X*C.H)))==0
                assert sp.simplify(post-sp.trace(C.H*Eeff*C*Phi(X)))==0

# Reproduce genuine H75 effect difference (not a new experiment).
rho_00=sp.kronecker_product(I2[:,0]*I2[0,:],E(0,0))
p_dephased=sp.simplify(sp.trace(Q_coherent*dephase(Phi(rho_00))))
p_normalform=sp.simplify(sp.trace(Q_effective*Phi(rho_00)))
assert p_dephased==p_normalform==R(5,18)

print("PASS: original H75 four-Kraus CPTP factorization on all 36 complex units")
print("PASS: source rank 9 on full Herm(6) (kernel 27), native 18D (kernel 9)")
print("PASS: positive native rho_+ and rho_- have exactly identical H75 outputs")
print("PASS: distinct strictly positive POVM effects E_+/E_- yield Phi*=I/2")
print("PASS: nonunitary dephasing instrument absorbs into Q_eff (all 36 units)")
print("PASS: prep+precontrol and instrument+readout behavioral identifications")
print("PASS: PRE/POST universal normal form on 36 inputs x 2x2x3 port choices")
print("PASS: original rational H75 dephasing probability 5/18")
print("BOUNDARY: valid formal effective readout is not necessarily hardware-authorized")
print("OPEN: G2-intrinsic F access origin, AX-OA axiomatic independence and P11 completion")
