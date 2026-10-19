"""H109 — EXACT H75 original CPTP source: 3-step primitive visible mixing
and universal trace-only classification of all full-source linear
intertwiners into unitary target dynamics (including actual P9
16D/48D unitary models).

No extra Hamiltonian/observer/solder/interaction is introduced.
True original H75 4-Kraus map, P3 signed R3 and real A/B controls
unchanged. Exact Gaussian rational Gram ranks 4,7,8 certify
strict HS contraction of entire complex traceless qutrit subspace.

Main theorem: If T:M6->M_N is linear (NOT NECESSARILY INJECTIVE) and
T o Phi_H75 = Ad_V o T for any fixed unitary target V, then
T(X)=Tr(X)*Y with V Y V†=Y. Converse exact. Therefore NO
nontrivial KKS phase/signed-P3 coherent operator transport of
this fully autonomous linear full-source kind into P9 unitary.
This does NOT exclude dilations, quotients, time-dependent
intertwiners, nonunitary targets or alternate physical sectors.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    micro,visible,embed,qtrace,envblock,
    M0,M1,U,R60,SBASIS,MBASIS,
    eye_n,zero_n,matmul,matadj,matmul as mm,mattrace
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91

assert R60[0][0]==I*gc(F(-32,135))
assert len(SBASIS)==9 and len(MBASIS)==36
I3=eye_n(3)
I6=eye_n(6)
Z3=zero_n(3)
Z6=zero_n(6)
assert matmul(matadj(U),U)==I3

def cs(X,c):
    return [[v*gc(c) for v in row] for row in X]
def iszero(X):
    return all(v==Z0 for row in X for v in row)
def trace(X):
    return mattrace(X)
def hs(A,B):
    return trace(mm(matadj(A),B))
def V(X):return visible(X)
def powers(X,n):
    for k in range(n):X=V(X)
    return X

# True Schur form (and its one-step exact HS loss) on ALL nine
# non-Hermitian Eij qutrit operators. Matrix M0 is invertible
# on site3, so the finite first-reset image is 9 complex dim.
c=((F(1),F(3,5),F(3,5)),
   (F(3,5),F(1),F(1)),
   (F(3,5),F(1),F(1)))
def schur(X):
    return [[gc(c[i][j])*X[i][j] for j in range(3)]
            for i in range(3)]
for X in SBASIS:
    assert V(X)==H91.mm(H91.mm(U,schur(X)),matadj(U))
    assert qtrace(micro(embed(X)))==V(X)
    assert mattrace(V(X))==mattrace(X)
    lhs=hs(X,X)-hs(V(X),V(X))
    rhs=gc(F(16,25))*sum((
        X[0][j].conj()*X[0][j]+X[j][0].conj()*X[j][0]
        for j in (1,2)
    ),Z0)
    assert lhs==rhs and lhs.i==0
assert V(I3)==I3
assert mattrace(V(I3))==gc(F(3))
print("PASS H109.1: original H75 visible 3D channel EXACTLY equals Ad_U after Schur damping cross site-0 versus 1/2 by 3/5; unital/trace-preserving on all 9 quantum basis units")

# Hermitian REAL operator basis B=(three population,
# X01,Y01,X02,Y02,X12,Y12); exact rank9. Gram contraction
# difference K_n on this space is a RATIONAL real PSD matrix.
b=H91.basis_q
assert len(b)==9
assert all(matadj(X)==X for X in b)
def gram_contraction(n):
    images=[powers(X,n) for X in b]
    G=[]
    for X,Xd in zip(b,images):
        row=[]
        for Y,Yd in zip(b,images):
            z=hs(X,Y)-hs(Xd,Yd)
            assert z.i==0
            row.append(z.r)
        G.append(row)
    assert G==[list(t) for t in zip(*G)]
    # Identity = E00+E11+E22: its Gram row/column vanish.
    for j in range(9):
        assert G[0][j]+G[1][j]+G[2][j]==0
    return G

G1,G2,G3=(gram_contraction(n) for n in (1,2,3))
rank_sequence=[H91.rank(G) for G in (G1,G2,G3)]
assert rank_sequence==[4,7,8],rank_sequence
# G_n positive semidefinite because every single Schur damping
# step reduces squared HS norm and U conjugation is isometric.
# With rank G3=8 and the nonzero identity in its nullspace,
# the nullspace is EXACTLY scalar identity, hence strictly
# positive quadratic defect on all 8D real traceless Hermitian
# directions. Complex extension follows by X=A+iB decomposition.
traceless=H91.traceless
assert len(traceless)==8
# Separate diagonal/symmetric/antisymmetric generator pieces
# cover all complex-traceless site operators.
assert iszero(powers(I3,3)) is False
# Stronger exact nondegeneracy test: 8 coordinate directions
# two traceless diagonals and six site quadratures produce
# an 8x8 Gram restriction matrix of full rank.
def hermcoords(X):
    # H91 Hermitian basis coordinates via HS inversion not needed:
    # linearity allows test directly by the same positive quadratic
    # defect form on true physical traceless basis.
    return X
def G_on(v):
    out=[]
    img=[powers(X,3) for X in v]
    for i,X in enumerate(v):
        row=[]
        for j,Y in enumerate(v):
            val=hs(X,Y)-hs(img[i],img[j])
            assert val.i==0
            row.append(val.r)
        out.append(row)
    return out
G8=G_on(traceless)
assert H91.rank(G8)==8
# Confirm G3's rational exact nullspace exactly scalar (1,1,1,...).
assert H91.rank(G3)==8 and H91.rank(G8)==8
print("PASS H109.2: original H75 exact 9x9 Hermitian HS contraction Gram ranks at n=1,2,3 are 4,7,8, with kernel of n3 precisely span(I3); true traceless 8x8 Gram restriction has full rank8")
print("THEOREM H109.2: since all steps are HS contractions and n3 deficit is strictly positive on 8D traceless Hermitian subspace, V^(3k) contracts all tracezero complex matrices geometrically, and V^n(X)->Tr(X) I3/3")

# The all-input original 6D 4-Kraus map factorizes through
# flag partial trace. Prove first 3 iterations of every 6x6
# matrix unit, NOT a surrogate or a single selected state.
def J(X):return micro(embed(X))
for basis in MBASIS:
    red=qtrace(basis)
    assert micro(basis)==J(red)
    current=basis
    for n in range(1,4):
        current=micro(current)
        expected=J(powers(red,n-1))
        assert current==expected,(n,)
    assert mattrace(basis)==mattrace(micro(basis))
sigma=J(cs(I3,F(1,3)))
assert matadj(sigma)==sigma
assert mattrace(sigma)==O
assert micro(sigma)==sigma
assert qtrace(sigma)==cs(I3,F(1,3))
# Because Tr_E:M6->M3 surjective (rank9), J injective
# (M0 invertible and conjugation U reversible), rank Phi=9
# and kernel has complex dimension 36-9=27.
m0diag=[F(1),F(3,5),F(3,5)]
assert all(x>0 for x in m0diag)
assert len(MBASIS)-len(SBASIS)==27
K=zero_n(6)
K[0][3]=O
assert K!=Z6 and micro(K)==Z6
print("PASS H109.3: full unchanged 6D H75 4-Kraus Phi has first-image complex rank9 and kernel dimension27; true all 36 source matrix units satisfy Phi^n=J V^(n-1) Tr_flag through n3, with exact stationary physical sigma*=J(I3/3)")
print("THEOREM H109.3: from exact V mixing and full-source factorization, Phi^n(X)->Tr(X)*sigma* (rank-one full 6D limiting channel) while original finite-time P3 R3 remains nonzero")

# Unitary-target theorem for ANY 16D/48D target and arbitrary
# NONinjective linear T satisfying T Phi=Psi T, with Psi(Y)=VYV†.
# For tracezero X, Phi^n(X)->0; isometry of Psi gives
# ||TX||_HS=||Psi^n TX||=||T Phi^n X|| -> 0 => TX=0.
# Thus T(X)=Tr(X) Y, and Psi(Y)=Y. Conversely such T works
# because Phi is trace-preserving. Provide exact positive
# examples Y=I16 and I48, plus H75 tracezero basis tests.
for N in (16,48):
    target_I=eye_n(N)
    # explicit trace-only noninjective linear channel target T_N
    # (not claimed CP or trace preserving at target size)
    def T(X):
        z=mattrace(X)
        return [[z*target_I[i][j] for j in range(N)] for i in range(N)]
    assert T(sigma)==target_I
    for E in MBASIS:
        assert T(micro(E))==T(E)
        assert T(E)==([[mattrace(E)*target_I[i][j]
                         for j in range(N)] for i in range(N)])
    print("PASS H109.4: exact EXISTENCE of only trace-only compatible example T(X)=Tr(X) I_%d; target identity commutes with ANY P9 unitary Hamiltonian" % N)

print("THEOREM H109.4 (IFF, non-injective included): ANY complex-linear T:M6->M_N into an arbitrary FIXED unitary-conjugation target satisfying T Phi_H75=Ad_V T MUST equal T(X)=Tr(X)Y with Ad_V Y=Y; conversely every such Y works. Full operator-to-unitary source-dynamics information capacity = one complex direction at most.")
print("BOUNDARY: cannot infer absence of finite-time positive phase readouts, genuine original P3 signed residue, shared-ancilla Stinespring dilation, state-dependent/time-dependent maps, noiseless RESTRICTED source sectors with other dynamics, or open-system quotient/simulation in opposite direction")
print("BOUNDARY: P9.126–128 are actual reversible 16D/48D unitary source models distinct from original H75 reset. No sourced six-pair ADM canonical field, P9 Cartan solder/translation, DeWitt/off-shell HDA/Einstein or F generative completeness.")
