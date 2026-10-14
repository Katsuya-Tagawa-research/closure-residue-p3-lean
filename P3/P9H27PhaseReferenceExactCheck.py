"""H27: exact U(1) observer stabilizer and conditional intercell interferometry.

Imports H24's genuinely nonzero P3 Krylov residue microscopic witness.
The Ramsey link instrument is an explicitly ADDED CPTP model, not P6-derived.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import (
    C, gc, I, O, Z0, U, Z, z1, phi, mm, dagger, scale)

E=[[O,Z0],[Z0,O]]
def phase(q):
    assert q*q.conj()==O
    return [[q,Z0],[Z0,q.conj()]]
def adj(g,a): return mm(mm(g,a),dagger(g))
def tr(a): return a[0][0]+a[1][1]
a=z1[0][1]
assert a==C(F(8,9),F(4,9))
amp_norm=a*a.conj()
assert amp_norm==C(F(80,81))
assert mm(dagger(U),U)==E
q=C(F(3,5),F(4,5)); tau=q*q
q2=C(F(5,13),F(12,13)); tau2=q2*q2
assert tau==C(F(-7,25),F(24,25))
assert tau*tau.conj()==O and tau2*tau2.conj()==O
assert adj(phase(q),Z)==Z
assert adj(phase(q),z1)[0][1]==tau*a
assert adj(phase(q),phi(Z))!=phi(adj(phase(q),Z))
# For nonzero a, preserving the first hidden complex line requires
# tau=conj(tau), hence tau=+/-1; preserving labeled z1 requires +1.
for t in (O,-O,tau,tau.conj(),tau2):
    preserves_line=(t==t.conj())
    image=[[Z0,t*a],[t.conj()*a.conj(),Z0]]
    assert preserves_line==(image==scale(z1,t))
    assert (image==z1)==(t==O)
assert adj(phase(I),z1)==scale(z1,-O)
assert adj(phase(I),phi(Z))!=phi(Z)

nodes=tuple(range(4))
tree=((0,1),(1,2),(2,3)); chords=((0,2),(0,3))
edges=tree+chords
assert len(edges)-len(nodes)+1==2
flat={e:O for e in edges}
twist=dict(flat); twist[(0,2)]=tau;twist[(0,3)]=tau2

def gauge(A,g):
    return {(u,v):g[v]*A[(u,v)]*g[u].conj() for u,v in edges}
def local_amp(g): return {v:g[v]*a for v in nodes}
def link_signal(A,amp):
    return {(u,v):amp[v].conj()*A[(u,v)]*amp[u]/amp_norm
            for u,v in edges}
def hol02(s):return s[(0,1)]*s[(1,2)]*s[(0,2)].conj()
def hol03(s):return s[(0,1)]*s[(1,2)]*s[(2,3)]*s[(0,3)].conj()
plain_amp={v:a for v in nodes}
s0=link_signal(twist,plain_amp)
assert s0==twist
lambdas={0:O,1:tau,2:tau2,3:tau*tau2}
s1=link_signal(gauge(twist,lambdas),local_amp(lambdas))
assert s1==s0
assert hol02(s0)==tau.conj() and hol03(s0)==tau2.conj()
assert hol02(s1)==hol02(s0) and hol03(s1)==hol03(s0)
assert hol02(link_signal(flat,plain_amp))==O
# A parallel nonzero coherence section enforces trivial loop holonomy.
parallel=gauge(flat,lambdas); parallel_amp=local_amp(lambdas)
assert all(parallel[(u,v)]*parallel_amp[u]==parallel_amp[v]
           for u,v in edges)
assert all(x==O for x in link_signal(parallel,parallel_amp).values())

# Standard CPTP Ramsey comparator (an ADDITIONAL cross-cell capability).
X=[[Z0,O],[O,Z0]];Y=[[Z0,-I],[I,Z0]]
p=[[C(F(1,2)),C(F(1,2))],[C(F(1,2)),C(F(1,2))]]
def ramsey(r):
    assert r*r.conj()==O
    g=[[O,Z0],[Z0,r]]
    assert mm(dagger(g),g)==E
    rho=adj(g,p)
    assert rho[0][0]==C(F(1,2)) and rho[1][1]==C(F(1,2))
    return tr(mm(rho,X)),tr(mm(rho,Y))
for r in (O,-O,tau,tau.conj(),tau2):
    assert ramsey(r)==(C(r.r),C(r.i))
assert ramsey(tau)[0]==ramsey(tau.conj())[0]
assert ramsey(tau)[1]!=ramsey(tau.conj())[1]

print('PASS H27: H24 original P3 first-residue phase stabilizer U1 -> Z2 -> identity')
print('PASS H27: identical CPTP-channel intertwining eliminates nontrivial diagonal twists')
print('PASS H27: gauge-invariant cross-cell complex phase recovers both cycle holonomies')
print('PASS H27: parallel nonzero coherence section forces flat SO2 holonomy')
print('PASS H27: exact CPTP Ramsey X/Y quadratures separate conjugate phase ambiguity')
print('SCOPE: coherent intercell link instrumentation is an additional assumption')
