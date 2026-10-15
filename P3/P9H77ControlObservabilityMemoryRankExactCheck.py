"""H77 — exact minimal predictive linear memory rank by physical control catalog.

The microscopic H75/H76 six-dimensional CPTP source is UNCHANGED.
Its original P3 signed R3 is nonzero, and H76's actual CP flag
observer Cflag has complex rank18 on M6.

Exact constructive operational observability lemma:
K_* = intersection over finite permitted control words w
      of ker(Cflag o T_w).
Any LINEAR predictive record R for all future full flag-block quantum
outputs obeys ker R subset K_*, so rank R >= 36-dim K_*.
The span of the Heisenberg-pulled quantum-block observations
achieves that minimal LINEAR rank. This does NOT grant an arbitrary
quotient a CPTP physical implementation.

For SAME H75 source, Cflag observation, same classical feedback F,
one extra independently declared REAL flag mixing W, and selected
P6-type separate real edge controls A and B, exact row-observability
ranks exhibit:
  flag + F (no coherent flag control): 18
  flag + W: 27
  flag + W + F: 31
  flag + W + F + A: 35
  flag + W + F + A + B: 36 (full quantum M6)

Thus full complex-36 memory is NECESSARY for exact prediction of all
full quantum-block flag observations for all M6 initial states and
all finite words in the final physical catalog. Full state identity
is a CPTP sufficient memory. The 18,27,31,35,36 dimensions are
linear observability ranks, NOT minimum physical Hilbert dimensions.
Catalog access and observation tomography are external physical data
not derived from uncontrolled original P3 residues alone.

Gaussian rational / exact Fraction operations only, stdlib.
"""
from fractions import Fraction as F
from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    A,B,edge_cayley,lift,ONE6,MBASIS,D6,R60,micro,
    matadj,matmul
)
from P9H76FeedbackFlagMemoryCPTPExactCheck import (
    flagged,Fgate,W,rank as flag_rank,feedback
)
assert len(MBASIS)==36
assert flag_rank(flagged)==18
assert R60!=[[Z0 for j in range(6)] for i in range(6)]
assert all(flagged(micro(X))==micro(X) for X in MBASIS)

def real_value(c):
    assert c.i==0
    return c.r

GATES={
    "F":Fgate,
    "W":W,
    "A":lift(edge_cayley(A,F(1,2))),
    "B":lift(edge_cayley(B,F(2,3))),
}
n=6
N2=n*n
def index(i,j):return i*n+j

def build_action(U):
    # On complex 6x6 operator entries in row-major order,
    # [Ad_U(X)]_ij = sum_{k,l} U_ik conj(U_jl) X_kl.
    assert matmul(matadj(U),U)==ONE6
    assert matmul(U,matadj(U))==ONE6
    out=[[F(0)]*N2 for _ in range(N2)]
    for i in range(n):
        for j in range(n):
            v=out[index(i,j)]
            for k in range(n):
                for l in range(n):
                    v[index(k,l)]=real_value(U[i][k]*U[j][l].conj())
    return out

ACTION={name:build_action(g) for name,g in GATES.items()}
def apply_row(row,T):
    # Pull Heisenberg linear functionals backwards through T.
    out=[F(0)]*N2
    for i,c in enumerate(row):
        if c:
            for j,a in enumerate(T[i]):
                if a:out[j]+=c*a
    return out

OBS_ROWS=[]
for a in (0,1):
    for i in range(3):
        for j in range(3):
            row=[F(0)]*N2
            row[index(3*a+i,3*a+j)]=F(1)
            OBS_ROWS.append(row)
assert len(OBS_ROWS)==18

def add_independent(row,pivot_vectors):
    """Fraction-rational incremental row elimination, no heuristics."""
    v=list(row)
    for pivot in sorted(pivot_vectors):
        c=v[pivot]
        if c:
            basis=pivot_vectors[pivot]
            v=[a-c*b for a,b in zip(v,basis)]
    if all(x==0 for x in v):
        return None
    pivot=next(i for i,x in enumerate(v) if x)
    c=v[pivot]
    normal=[x/c for x in v]
    assert pivot not in pivot_vectors
    # Maintain REDUCED row echelon form: earlier inserted basis rows
    # can have nonzero entries in this newly discovered pivot.
    # Clearing them is essential so a later elimination does not
    # reintroduce an already eliminated earlier pivot coordinate.
    for old_p,basis in list(pivot_vectors.items()):
        coeff=basis[pivot]
        if coeff:
            pivot_vectors[old_p]=[a-coeff*b for a,b in zip(basis,normal)]
    pivot_vectors[pivot]=normal
    assert all(pivot_vectors[p][q]==(F(1) if p==q else F(0))
               for p in pivot_vectors for q in pivot_vectors)
    return normal

def closure(names,max_depth=10):
    pivots={}
    new=[]
    for r in OBS_ROWS:
        v=add_independent(r,pivots)
        if v is not None:new.append(v)
    depths=[len(pivots)]
    for depth in range(max_depth):
        additions=[]
        for row in new:
            for name in names:
                candidate=apply_row(row,ACTION[name])
                v=add_independent(candidate,pivots)
                if v is not None:additions.append(v)
        depths.append(len(pivots))
        if not additions:return depths,pivots
        new=additions
    raise AssertionError("observability iteration did not stabilize")

EXPECTED={
    ("F",):[18,18],
    ("W",):[18,27,27],
    ("W","F"):[18,27,31,31],
    ("W","F","A"):[18,27,31,34,35,35],
    ("W","F","A","B"):[18,27,31,35,36,36],
}
for names,want in EXPECTED.items():
    depths,pivots=closure(names)
    assert depths==want,(names,depths,want)
    print("PASS H77 EXACT observability",names,"rank by word-depth",depths)

# A full 36D observability rank means K_*=0: for any distinct
# 6D microscopic Hermitian states, at least one finite word of
# W, classical-feedback F and BOTH independent real edge controls
# produces a different *flag-quantum-block* output.
# We do not claim a 36D physical Hilbert memory: the rank is
# the COMPLEX-LINEAR dimension of the required record.
depths,basis=closure(("W","F","A","B"))
assert len(basis)==N2
assert depths[4]==N2
print("PASS H77: all 36 complex microscopic operator directions become observable after at most FOUR coherent control steps")
print("PASS H77: strong full-catalog exact linear predictive memory rank is 36; identity M6 recorder is CPTP sufficient")

# The semicausal source does not itself reveal hidden flag coherences:
# it erases them, and its ORIGINAL P3 signed R3 is exactly unchanged
# regardless of which additional physical control library is admitted.
X=MBASIS[index(0,3)]
assert flagged(X)==[[Z0 for j in range(6)] for i in range(6)]
assert micro(X)==[[Z0 for j in range(6)] for i in range(6)]
assert R60[0][0]==I*gc(F(-32,135))
print("PASS H77: SAME uncontrolled 6D original-P3 source and residue across incompatible allowed apparatus/control catalogs")
print("BOUNDARY: not a P3-only selection of W/F/A/B or a non-Markovian microscopic origin theorem")
print("BOUNDARY: exact ranks assume ALL microscopic input states and full flag-resolved quantum output (tomographic), NOT scalar site probabilities alone")
print("BOUNDARY: measurements from separate preparations and arbitrary intermediate reversible control words, NOT an undisturbed single quantum trajectory")
print("BOUNDARY: original P3->frozen P6 physical J_N, CR-only discriminator, P9 ADM/HDA/Einstein success remain OPEN")
