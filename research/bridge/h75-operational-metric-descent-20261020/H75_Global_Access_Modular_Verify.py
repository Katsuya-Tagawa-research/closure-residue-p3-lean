#!/usr/bin/env python3
"""Dependency-free rational modular determinant verification of saved 18x18.
Does not rely on SymPy's rank implementation; data produced by exact audit.
"""
from pathlib import Path
from fractions import Fraction
import csv,json
folder=Path(__file__).parent
rows=[[Fraction(z) for z in row] for row in csv.reader((folder/'H75_Global_Access_18x18_Certificate.csv').open())]
assert len(rows)==18 and all(len(r)==18 for r in rows)
p=1000000007
arr=[[int(x.numerator%p)*pow(int(x.denominator%p),-1,p)%p for x in row] for row in rows]
det=1
for j in range(18):
    k=next((i for i in range(j,18) if arr[i][j]),None)
    assert k is not None,'singular mod prime; full-rank witness invalid'
    if k!=j:
        arr[j],arr[k]=arr[k],arr[j];det=-det
    pivot=arr[j][j]
    det=det*pivot%p
    inv=pow(pivot,-1,p)
    for i in range(j+1,18):
        factor=arr[i][j]*inv%p
        for q in range(j+1,18):arr[i][q]=(arr[i][q]-factor*arr[j][q])%p
        arr[i][j]=0
actual=det%p
result=json.loads((folder/'H75_Global_Access_Exact_Results.json').read_text())
assert actual==result['nonzero_rational_determinant_mod_prime']==39156989
assert result['matrix_rank_exact']==18
print('DEPENDENCY-FREE EXACT CERTIFICATE PASS: det mod',p,'=',actual)
