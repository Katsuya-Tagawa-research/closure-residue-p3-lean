"""H82: exact finite reachable-observable quotient and Hankel-rank audit.

Small independent Fraction-rational examples illustrate the finite *linear*
theorem; the inherited H80/H81 checkers separately retest the actual physical
six-dimensional source, CPTP recovery minimum, and positive-POVM schedule
counterexample. These examples are NOT universal CP sufficiency proofs.
"""
from fractions import Fraction as Q

def rank(rows):
    if not rows:
        return 0
    A = [[Q(x) for x in row] for row in rows]
    n = len(A[0])
    assert all(len(row) == n for row in A)
    i = 0
    for j in range(n):
        k = next((k for k in range(i, len(A)) if A[k][j]), None)
        if k is None:
            continue
        A[i], A[k] = A[k], A[i]
        d = A[i][j]
        A[i] = [v/d for v in A[i]]
        for k in range(len(A)):
            if k != i and A[k][j]:
                f = A[k][j]
                A[k] = [x-f*y for x,y in zip(A[k],A[i])]
        i += 1
        if i == len(A):
            break
    return i

def mm(A,B):
    assert all(len(row) == len(B) for row in A)
    return [[sum((a*b for a,b in zip(row,col)),Q(0))
             for col in zip(*B)] for row in A]

def mv(A,x):
    return [sum((a*b for a,b in zip(row,x)),Q(0)) for row in A]

def dot(x,y):
    return sum((a*b for a,b in zip(x,y)),Q(0))

def powers(T,n):
    I=[[Q(int(i==j)) for j in range(n)] for i in range(n)]
    out=[I]
    for k in range(1,n):
        out.append(mm(out[-1],T))
    return out

# A genuine finite-dimensional system with three reachable and
# three distinguishable directions under one reversible real control.
T=[[0,0,1],[1,0,0],[0,1,0]]
assert mm(T,mm(T,T))==[[1,0,0],[0,1,0],[0,0,1]]
e0=[1,0,0]
r=[1,0,0]
Ps=powers(T,3)
reachable=[mv(p,e0) for p in Ps]
future_rows=[mm([r],p)[0] for p in Ps]  # one input basis row per future word
H=[[dot(s,col) for col in reachable] for s in future_rows]
assert rank(reachable)==3
assert rank(future_rows)==3
assert H==[[1,0,0],[0,0,1],[0,1,0]],H
assert rank(H)==3
print("PASS H82: exact finite Hankel rank 3 equals reachable dimension minus common future-silent dimension 0")

# A strict preparation-scope gate: without the cyclic control, only
# the first prepared direction is reachable and exactly one linear
# initial record direction is required.
I=Ps[0]
restricted=[mv(I,e0)]
assert rank(restricted)==1
assert rank([[dot(r,x) for x in restricted]])==1
print("PASS H82: only one physically prepared direction gives one-dimensional restricted linear response")

# With the SAME full three-dimensional physical input span and no
# additional control, adding physically distinct positive-coordinate
# readouts can increase the LINEAR accessible dimension from 1 to 3.
E=[[1,0,0],[0,1,0],[0,0,1]]
assert [rank(E[:k]) for k in (1,2,3)]==[1,2,3]
assert rank(E[:2]) < rank(E[:3])
print("PASS H82: adding calibrated independent readouts monotonically refines observational linear rank 1→2→3")

# Simulated kernel filtration: row-span closure along all future control
# words stabilizes at n=3 and is the transpose picture of K*=intersection.
rows=[r]
depth_ranks=[rank(rows)]
for _ in range(3):
    rows=rows+[mm([u],T)[0] for u in rows]
    depth_ranks.append(rank(rows))
assert depth_ranks==[1,2,3,3],depth_ranks
print("PASS H82: descending silent-kernel dual stabilizes after finite depth, ranks 1→2→3→3")
print("BOUNDARY: linear quotient/hankel rank alone does not entail a CP encoder, CPTP decoder, quantum realization, F-derived ports, or Einstein dynamics")
