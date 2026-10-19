"""H114: exact 3-level all-marked-orders obstruction and locality saturation.
Uses SymPy, no independent reproduction of H37 or a full physical P6 experiment.
Run: python P3P11_H114_all_order_locality_audit.py
"""
import sympy as s

N=3
I=s.I
Eye=s.eye(N)
Z=s.zeros(N)
E=lambda i,j: Eye[:,i]*Eye[j,:]
X12=E(0,1)+E(1,0)
X23=E(1,2)+E(2,1)
X13=E(0,2)+E(2,0)
Y12=-I*(E(0,1)-E(1,0))
comm=lambda A,B:A*B-B*A
vec=lambda M:s.Matrix(M).reshape(N*N,1)
Mrank=lambda ms:s.Matrix.hstack(*[vec(M) for M in ms]).rank()

checks=0
def ok(condition, name):
    global checks
    assert bool(condition),name
    checks+=1

theta=s.pi/4
U0=Eye+(s.cos(theta)-1)*(E(0,0)+E(1,1))-I*s.sin(theta)*X12
U0=s.simplify(U0)
ok(s.simplify(U0.H*U0-Eye)==Z,'U0 is unitary')
ok((U0*E(0,0)*U0.H)[0,1]!=0,'Baseline generates coherence')

# Baseline Phi0 and the marked u-control are identically the same in
# implementation A and in implementation B restricted to v=0.
# Here the matrices are the common declared map, so equality to every
# order follows analytically from the identity on a neighborhood of u=0.
Uu=lambda u: Eye+(s.cos(u)-1)*(E(0,0)+E(1,1))-I*s.sin(u)*X12
u=s.symbols('u',real=True)
ok(s.simplify(Uu(u).H*Uu(u)-Eye)==Z,'u-family unitary')
ok(s.simplify(Uu(0)-Eye)==Z,'u-family at zero')
ok(s.simplify(s.diff(Uu(u),u).subs(u,0)+I*X12)==Z,'u-derivative')

def action(H,A):
    return -I*comm(H,U0*A*U0.H)

basis=[E(i,j) for i in range(N) for j in range(N)]
def col_der(H):
    return s.Matrix.vstack(*[vec(s.simplify(action(H,B))) for B in basis])
D12=col_der(X12)
D23=col_der(X23)
ok(s.Matrix.hstack(D12).rank()==1,'one control derivative')
ok(s.Matrix.hstack(D12,D23).rank()==2,'two control derivatives')

# Independent infinitesimal coherent controls vs Lie-closure by switching.
A,B=I*X12,I*X23
C=comm(A,B)
ok(C==E(2,0)-E(0,2),'nonzero derived commutator')
ok(comm(A,C)==-B,'lie closure 1')
ok(comm(B,C)==A,'lie closure 2')
ok(Mrank([A])==1,'first Lie algebra dimension')
ok(Mrank([A,B,C])==3,'second Lie algebra dimension')

# D_N-bimodule closures: row-column matrix units of primitive support.
J_A=[E(0,1),E(1,0)]
J_B=J_A+[E(1,2),E(2,1)]
ok(Mrank(J_A)==2,'closure A dimension')
ok(Mrank(J_B)==4,'closure B dimension')
# If the *reachable Lie closure* is misread as the native primitive list,
# the bracket generates the nonnative 1--3 edge.
J_lie=J_B+[E(0,2),E(2,0)]
ok(E(0,0)*C*E(2,2)==-E(0,2),'Lie-produced edge 1->3')
ok(E(2,2)*C*E(0,0)==E(2,0),'Lie-produced edge 3->1')
ok(Mrank(J_lie)==6,'Lie support closure six complex dimensions')
for (a,b,source) in [(0,1,X12),(1,0,X12),(1,2,X23),(2,1,X23)]:
    ok(E(a,a)*source*E(b,b)==E(a,b),f'diagonal row-column isolation {a},{b}')

# Every input data functional depending only on Phi0, D3 and all marked
# u-control words must coincide because the underlying marked maps coincide.
# Code tests several words explicitly; the universal statement is a proof
# by pointwise identity, not finite sampling.
for val in [s.Integer(0),s.pi/6,s.pi/3]:
    W=s.simplify(Uu(val)*U0)
    for k in [1,2,3]:
        Wk=s.simplify(W**k)
        ok(s.simplify(Wk.H*Wk-Eye)==Z,f'marked word u={val},power={k}')

# Linear-algebra tomography: H -> -i[H,Phi0(Eij)] has kernel scalars.
Tom=s.Matrix.hstack(*[col_der(H) for H in basis])
ok(Tom.rank()==N*N-1,'Hamiltonian tomography rank 8')
ok(Tom*vec(Eye)==s.zeros(N**4,1),'identity in Hamiltonian kernel')

# Static graph graded algebra versus its eventual saturation.
def reach_layers(n, edges, maxk):
    e=set(tuple(sorted(z)) for z in edges)
    directed={(a,b) for a,b in e}|{(b,a) for a,b in e}
    reachable={(i,i) for i in range(n)}
    outputs=[set(reachable)]
    for _ in range(maxk):
        reachable=reachable|{(i,k) for i,j in reachable for a,k in directed if j==a}
        outputs.append(set(reachable))
    return outputs
P=reach_layers(N,[(0,1),(1,2)],3)
T=reach_layers(N,[(0,1),(1,2),(0,2)],3)
ok([len(z) for z in P]==[3,7,9,9],'path support growth')
ok([len(z) for z in T]==[3,9,9,9],'triangle support growth')
ok(P[2]==T[2]=={(i,j) for i in range(N) for j in range(N)},'same saturated algebra')
ok(P[1]!=T[1],'different primitive adjacency')

# Continuous-time symmetric Markov generators have full positive support for
# t>0 on a connected graph (proved by uniformization in the note).
Qp=s.Matrix([[-1,1,0],[1,-2,1],[0,1,-1]])
Qt=s.Matrix([[-2,1,1],[1,-2,1],[1,1,-2]])
ok(Qp* s.ones(N,1)==s.zeros(N,1),'path row-stochastic generator')
ok(Qt* s.ones(N,1)==s.zeros(N,1),'triangle row-stochastic generator')
ok(Qp[0,2]==0 and Qt[0,2]==1,'distinct instantaneous edges')
# Rigorous positivity witness at t=1 from transformed nonnegative matrices:
# e^Q=e^{-nu} sum_{m>=0} (nu^m/m!) P^m, where P>=0 and a path
# from each i to j exists, so some summand has a strictly positive entry.
nu=s.Integer(3)
Pp=Eye+Qp/nu
Pt=Eye+Qt/nu
ok(all(x>=0 for x in Pp),'uniformized path nonnegative')
ok(all(x>=0 for x in Pt),'uniformized triangle nonnegative')
for M in [Pp,Pt]:
    W3=Eye+M+M**2+M**3
    ok(all(x>0 for x in W3),'every pair reachable within <=3 steps')

# Gauge covariance prohibits selecting a phase-fixed real X12 operator from
# input fixed under all diagonal phases. The complex edge span remains invariant.
G=s.diag(I,1,1)
ok(s.simplify(G*X12*G.H+Y12)==Z,'phase rotates X12 to -Y12')
ok(Mrank([X12,Y12])==2,'X12 and Y12 real directions independent')
ok(G*E(0,1)*G.H==I*E(0,1),'complex edge weight')
ok(G*E(1,0)*G.H==-I*E(1,0),'opposite edge weight')

print(f'PASS H114: {checks}/{checks} exact assertions.')
print('Common nonidentity baseline Phi0=Ad(U0); same marked u-control for all u, times/words/orders.')
print('Raw coherent control derivative rank: 1 vs 2; Lie closures: 1 vs 3.')
print('Diagonal-bimodule dimensions: 2 vs 4. Full Hamiltonian tomography rank=8 (kernel scalars).')
print('Path/triangle algebra dimensions by grade: [3,7,9,9] vs [3,9,9,9].')
print('H37 Xi dimensions and full P3/P4 filtrations are NOT recalculated.')