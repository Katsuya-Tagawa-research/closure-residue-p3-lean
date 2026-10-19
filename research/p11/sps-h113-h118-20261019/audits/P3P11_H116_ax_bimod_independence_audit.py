#!/usr/bin/env python3
"""H116 exact finite 5-site H37 algebra and gauge-selection audit.
Requires sympy. Prints and writes JSON. Proof of general statements is in Markdown.
"""
from pathlib import Path
import json
import sympy as sp

N=5
I=sp.I
E=lambda i,j: sp.eye(N)[:,i]*sp.eye(N)[j,:]
P=[E(i,i) for i in range(N)]
X=[E(i,i+1)+E(i+1,i) for i in range(N-1)]
K=[E(i,i+1)-E(i+1,i) for i in range(N-1)]
Hhop=sp.Rational(1,2)*sum(X,sp.zeros(N))
Hdiag=sp.diag(0,sp.Rational(1,7),-sp.Rational(1,9),sp.Rational(2,11),-sp.Rational(3,13))
H=Hdiag+Hhop
Jmix=[Hhop]+K
Jfull=[E(i,i+1) for i in range(N-1)]+[E(i+1,i) for i in range(N-1)]
D=[E(i,i) for i in range(N)]
checks=[]
def ok(name, p):
    assert bool(p), name
    checks.append(name)

def v(M): return sp.Matrix(list(M))
def rank(S): return sp.Matrix.hstack(*[v(M) for M in S]).rank() if S else 0
def inside(A,S): return rank(S+[A])==rank(S)
def equalspan(A,B): return rank(A)==rank(B)==rank(A+B)
def dagger(A): return A.conjugate().T
def bracket(A,B): return A*B-B*A
def delta(A): return sp.diag(*[A[i,i] for i in range(N)])
def dclosure(S):
    T=[]
    for s in S:
        for q in [s,dagger(s)]:
            for i in range(N):
                for j in range(N):
                    Z=P[i]*q*P[j]
                    if Z != sp.zeros(N): T.append(Z)
    return T

def anti_real_vec(A):
    # vector over real rationals of an anti-Hermitian matrix
    return sp.Matrix([sp.re(q) for q in A]+[sp.im(q) for q in A])
def xirealrank(S):
    V=[]
    for s in S:
        V.extend([s-dagger(s),I*(s+dagger(s))])
    return sp.Matrix.hstack(*[anti_real_vec(A) for A in V]).rank()

ok('H37 correct hop entries', all(H[i,i+1]==sp.Rational(1,2) and H[i+1,i]==sp.Rational(1,2) for i in range(4)))
ok('H37 detunings', list(H.diagonal())==[0,sp.Rational(1,7),-sp.Rational(1,9),sp.Rational(2,11),-sp.Rational(3,13)])
ok('H37 Hermitian Hamiltonian', dagger(H)==H)
ok('diagonal algebra dimension 5',rank(D)==5)
ok('native real skew rank 4',rank(K)==4)
ok('mixed sector complex rank 5',rank(Jmix)==5)
ok('full sector complex rank 8',rank(Jfull)==8)
ok('mixed sector contained in full',all(inside(s,Jfull) for s in Jmix))
ok('mixed sector star stable',all(inside(dagger(s),Jmix) for s in Jmix))
ok('full sector star stable',all(inside(dagger(s),Jfull) for s in Jfull))
ok('Xi mixed real dimension 5',xirealrank(Jmix)==5)
ok('Xi full real dimension 8',xirealrank(Jfull)==8)
ok('four native Ke belong to mixed',all(inside(k,Jmix) for k in K))
ok('four native Ke belong to full',all(inside(k,Jfull) for k in K))
ok('mixed residue rank 4',rank([delta(bracket(Hhop,k)) for k in K])==4)
ok('full residue rank 4',rank([delta(bracket(E(e,e+1),E(e+1,e))) for e in range(4)])==4)
ok('K closure equals full',equalspan(dclosure(K),Jfull))
ok('mixed closure equals full',equalspan(dclosure(Jmix),Jfull))
ok('Hhop alone closure equals full',equalspan(dclosure([Hhop]),Jfull))
ok('full is a diagonal bimodule',equalspan(dclosure(Jfull),Jfull))
ok('mixed is not a diagonal bimodule',not inside(P[0]*Hhop*P[1],Jmix))
ok('explicit extracted E01',P[0]*Hhop*P[1]==sp.Rational(1,2)*E(0,1))
ok('E01 is not contained in mixed',not inside(E(0,1),Jmix))
ok('K0 alone closure selects edge pair',rank(dclosure([K[0]]))==2)
ok('Hhop vs controls sources are unequal lists',rank([Hhop])==1 and rank(K)==4)

# Diagonal gauge acting on marked input.  U K0 U† = iX0, absent Jmix.
U=sp.diag(I,1,1,1,1)
act=lambda A: U*A*dagger(U)
ok('U is diagonal unitary',U*dagger(U)==sp.eye(N))
ok('U preserves D pointwise',all(act(p)==p for p in P))
ok('gauge maps K0 to iX0',act(K[0])==I*X[0])
ok('iX0 absent from mixed sector',not inside(I*X[0],Jmix))
ok('fixed mixed sector not gauge invariant',not all(inside(act(s),Jmix) for s in Jmix))
ok('full sector remains fixed under chosen gauge',all(inside(act(s),Jfull) for s in Jfull))
ok('mixed covariant family maintains dimension',rank([act(s) for s in Jmix])==5)
ok('mixed covariant output is span of transformed marked inputs',equalspan([act(Hhop)]+[act(k) for k in K],[act(s) for s in Jmix]))
ok('full covariant family maintains dimension',rank([act(s) for s in Jfull])==8)
ok('gauge and D closure commute on native',equalspan(dclosure([act(s) for s in K]),[act(s) for s in dclosure(K)]))
ok('gauge and D closure commute on mixed',equalspan(dclosure([act(s) for s in Jmix]),[act(s) for s in dclosure(Jmix)]))
ok('Hhop is not fixed by nontrivial gauge',act(Hhop)!=Hhop)
ok('H is not fixed by nontrivial gauge',act(H)!=H)

# Additional finite gauge choices (phase coordinate rotations).
for e in range(N):
    V=sp.diag(*[I if j==e else 1 for j in range(N)])
    ok(f'gauge generator site {e} unitary',V*dagger(V)==sp.eye(N))
    ok(f'full invariant generator site {e}',all(inside(V*s*dagger(V),Jfull) for s in Jfull))

# Gauge-fixed diagonal sector counterexample when offdiag assumption dropped.
ok('C I is fixed by diagonal torus',U*sp.eye(N)*dagger(U)==sp.eye(N))
ok('C I is not a D bimodule',not inside(P[0]*sp.eye(N)*P[0],[sp.eye(N)]))

# Linear algebraic compatibility does not certify physical primitive source.
# Under the chosen interface data (H37, K), either sector is a valid interpretation.
ok('weak interface mixed valid',rank(Jmix)==5 and all(inside(k,Jmix) for k in K))
ok('weak interface full valid',rank(Jfull)==8 and all(inside(k,Jfull) for k in K))
ok('AX-BIMOD false in mixed expansion',not equalspan(dclosure(Jmix),Jmix))
ok('AX-BIMOD true in full expansion',equalspan(dclosure(Jfull),Jfull))

result={
    'study':'H116 — AX-BIMOD Relative Independence and Diagonal Gauge Covariance',
    'date':'2026-10-19',
    'system':'Fixed 5-site H37 Hamiltonian and marked native four K_e controls',
    'exact_assertions_passed':len(checks),
    'all_passed':True,
    'complex_sector_dimensions':{'J_mix':rank(Jmix),'J_full':rank(Jfull)},
    'real_Xi_dimensions':{'J_mix':xirealrank(Jmix),'J_full':xirealrank(Jfull)},
    'diagonal_residue_rank':4,
    'closure_dimensions':{'dclosure_Knative':rank(dclosure(K)),'dclosure_Hhop':rank(dclosure([Hhop])),'dclosure_Jmix':rank(dclosure(Jmix))},
    'gauge_example':'diag(i,1,1,1,1)',
    'weak_interface_expansions':{'J_mix_AX_BIMOD':False,'J_full_AX_BIMOD':True},
    'limits':['Not a formal completeness/independence proof for a future fully axiomatized P3/P4 theory',
              'No hardware device validation or phase-frame evidence','No F source selection',
              'No experimental CR-exclusive result','No P9 Einstein/ADM/HDA or P11 generative completeness'],
    'assertions':checks
}
path=Path(__file__).with_name('P3P11_H116_ax_bimod_exact_results.json')
path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('H116 PASS:',len(checks),'exact symbolic assertions')
print('Output:',path)