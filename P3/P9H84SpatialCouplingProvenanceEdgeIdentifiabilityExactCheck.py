"""H84 — exact spatial-source nonidentifiability and conditional edge-response audit.

The unchanged H75 original 6D CPTP source supplies a positive input/output
witness. Extra correlated or independent post-source noise is separately
declared; it is NOT P3-derived spatial dynamics. All arithmetic is rational
or previously audited Gaussian-rational (from H75).

The four-qubit ZZ edge experiment is a separate conventional QM comparator,
not an implemented intercell port of the H75 source, nor ADM/HDA.
"""
from fractions import Fraction as F
from itertools import product

from P9H24PhaseSensitiveResidueGaugeExactCheck import I, O, Z0, gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    micro, embed, qtrace, d0, R60
)

assert R60[0][0] == I * gc(F(-32,135))
assert R60 != [[Z0 for j in range(6)] for i in range(6)]

# H84.1 actual unchanged H75 output of the physical positive input
# rho_in = |flag0,site0><flag0,site0|.  Its visible qutrit part has
# (0,1) coherence -4i/9.  Hermitian site Y01 has expectation +8/9.
sigma = qtrace(micro(embed(d0)))
assert sigma[0][1] == -I * gc(F(4,9))
assert sigma[1][0] == I * gc(F(4,9))
alpha = I * (sigma[0][1]-sigma[1][0])
assert alpha == gc(F(8,9))
assert alpha.i == 0
a = alpha.r
p0,p1 = F(9,25),F(16,25)
assert p0+p1 == 1 and F(3,5)**2 == p0 and F(4,5)**2 == p1

# Each local output has the SAME D_p o Phi_micro in both architectures.
# The two-cell joint source output is sigma_micro \otimes sigma_micro.
# Under independent noise, the odd Y01 expectation gets multiplied
# by (p0-p1) on EACH cell; under common Z \otimes Z noise the product
# Y01 \otimes Y01 is even.  The two-cell effect
# Q+=(I_36+ (I_flag⊗Y01)⊗(I_flag⊗Y01))/2 is positive (spectral |O|<=1).
p_ind = (F(1)+(p0-p1)**2 * a*a)/2
p_com = (F(1)+a*a)/2
assert p_ind == F(53761,101250)
assert p_com == F(145,162)
assert p_com-p_ind == F(2048,5625)>0
assert 0<p_ind<1 and 0<p_com<1
print("PASS H84: unchanged H75 nonzero original P3 source plus declared common/independent noise yields positive joint POVM contrast 2048/5625")

# A completely explicit two-qubit CPTP companion audit checks same *full*
# local marginal channel on ALL 16 matrix units, including correlated input
# matrix units.  The Kraus coefficients are rational: 3/5,4/5 common and
# 9/25,12/25,12/25,16/25 independent.
Zs=([1,1,-1,-1],[1,-1,1,-1])
phase=[tuple(x*y for x,y in zip(Zs[0] if s&1 else [1]*4,
                               Zs[1] if s&2 else [1]*4))
       for s in range(4)]
ind=[(p0*p0,phase[0]),(p0*p1,phase[2]),
     (p1*p0,phase[1]),(p1*p1,phase[3])]
com=[(p0,phase[0]),(p1,phase[3])]
assert sum((v for v,_ in ind),F(0))==1
assert sum((v for v,_ in com),F(0))==1

def noise(X,kraus):
    return [[sum((w*z[i]*z[j]*X[i][j] for w,z in kraus),F(0))
             for j in range(4)] for i in range(4)]

def trace2(X):
    return [[X[2*i][2*j]+X[2*i+1][2*j+1]
             for j in range(2)] for i in range(2)]

def trace1(X):
    return [[X[i][j]+X[2+i][2+j]
             for j in range(2)] for i in range(2)]

for i in range(4):
    for j in range(4):
        E=[[F(int(a==i and b==j)) for b in range(4)]
           for a in range(4)]
        assert trace2(noise(E,ind))==trace2(noise(E,com))
        assert trace1(noise(E,ind))==trace1(noise(E,com))

rho_plusplus=[[F(1,4) for j in range(4)] for i in range(4)]
XX=[[F(int(j==(i^3))) for j in range(4)] for i in range(4)]
def expect(M,X):
    return sum((M[i][j]*X[j][i] for i in range(4)
                for j in range(4)),F(0))
q_ind=(1+expect(XX,noise(rho_plusplus,ind)))/2
q_com=(1+expect(XX,noise(rho_plusplus,com)))/2
assert q_ind==F(337,625)
assert q_com==1
assert q_com-q_ind==F(288,625)
print("PASS H84: independent/common 2-qubit CPTP maps have IDENTICAL all-input local marginals, but positive XX parity probabilities differ by 288/625")

# H84.2, a DIFFERENT conditional four-qubit ZZ Hamiltonian comparator.
# Pauli Y = -i J where J = iY = [[0,1],[-1,0]].
# d/dt <Y_i Z_j> = <[H, J_i Z_j]>, evaluated on |+>^4.
V=list(product((0,1),repeat=4))
edges=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
weights=(F(1,2),F(-2,3),F(3,5),F(0),F(7,4),F(-1,3))
index={v:i for i,v in enumerate(V)}

def hdiag(Js):
    return [sum((Js[k]*(1 if bits[a]==bits[b] else -1)
                 for k,(a,b) in enumerate(edges)),F(0))
            for bits in V]

def JZmat(i,j):
    T=[[0]*16 for k in range(16)]
    for k,bits in enumerate(V):
        flipped=list(bits);flipped[i]^=1
        col=index[tuple(flipped)]
        T[k][col]=(1 if bits[i]==0 else -1)*(1 if bits[j]==0 else -1)
    return T

def Xmat(i):
    T=[[0]*16 for k in range(16)]
    for k,bits in enumerate(V):
        flipped=list(bits);flipped[i]^=1
        T[k][index[tuple(flipped)]]=1
    return T

def slope(h,O):
    return sum(((h[a]-h[b])*O[a][b]
               for a in range(16) for b in range(16)),F(0))/16

for k,e in enumerate(edges):
    Js=[F(int(t==k)) for t in range(6)]
    h=hdiag(Js)
    for l,f in enumerate(edges):
        # derivative expectation for Y_i Z_j = 2*delta; physical positive
        # effect Q_+=(I+Y_i Z_j)/2 has derivative delta.
        assert slope(h,JZmat(*f)) == 2*int(k==l)
print("PASS H84: six-by-six physical positive-POVM ZZ-edge slope Jacobian is EXACT IDENTITY")

h=hdiag(weights)
for k,e in enumerate(edges):
    assert slope(h,JZmat(*e)) == 2*weights[k]
for i in range(4):
    Xi=Xmat(i)
    second=-sum(((h[a]-h[b])**2*Xi[a][b]
                 for a in range(16) for b in range(16)),F(0))/16
    expected=-4*sum((weights[k]**2 for k,(a,b) in enumerate(edges)
                     if i in (a,b)),F(0))
    assert second==expected
print("PASS H84: local X_i first derivative 0 and second derivative -4 sum_j J_ij^2; signs require stronger two-site readout")
print("BOUNDARY: correlated noise != Hamiltonian spatial edge, and reconstruction of separately calibrated J is NOT CR generation")
print("BOUNDARY: physical intercell topology, K4 solder, ADM HDA, Einstein dynamics and F generative completeness remain OPEN")
