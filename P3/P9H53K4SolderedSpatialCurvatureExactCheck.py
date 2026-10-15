"""H53: CONDITIONAL smooth K4 edge-field gluing, Levi-Civita 2-jets,
and exact convergent 3D spatial scalar curvature stencil.

Requires an EXTERNAL smooth spatial base and a locally consistent
physical solder/frame identifying fixed K4 S basis with TxM. Such a
solder is not obtained by P3 finite residue or H52 edge metric.

No black-box differential geometry: all derivatives are finite
matrix inverse identities in rational arithmetic. For positive local
conformal K4 weights w_e(x)=1-c x^T G x, exact continuum scalar
R3(0)=-3c, and a central spatial finite-difference stencil obeys
  Rh(c,h)=3c(-1+9ch²)/[(1-6ch²)(1-2ch²)]
and |Rh-R|<=1632/91*c²*h² for |c|<=3/2, 0<h<=1/4.

This reproduces standard Riemannian geometry on an ADDED field,
not physical Einstein-Hilbert dynamics or a P7/P8 solder origin.
"""
from fractions import Fraction as F
from itertools import combinations
from P9H52K4DeWittKinematicsCurvatureExactCheck import (
    I,zeros,add,scale,mm,trans,trace,det,inv,rank,
    T as frame,G,edges,V,B,cov_metric,positive_definite
)
assert len(edges)==6 and len(G)==3
def sub(a,b):return add(a,scale(b,-1))
def mat2(a,b,c,d):return [[a,b],[c,d]]
def metric_jets(w0,wi,wij):
    """Exact 0,1,2 spatial jets of g(w(x)) at a chart origin.

    wi[i][e]=∂_i w_e; wij[i][j][e]=∂_i∂_j w_e,
    with externally supplied spatial chart and soldered metric.
    """
    assert len(w0)==6 and len(wi)==len(wij)==3
    assert all(wij[i][j]==wij[j][i] for i in range(3) for j in range(3))
    assert positive_definite(B(w0))
    R=inv(B(w0))
    Bi=[B(wi[i]) for i in range(3)]
    Bij=[[B(wij[i][j]) for j in range(3)] for i in range(3)]
    def sand(X):return scale(mm(mm(G,X),G),F(16))
    g=sand(R)
    gi=[scale(sand(mm(mm(R,X),R)),-1) for X in Bi]
    gij=[]
    for i in range(3):
        row=[]
        for j in range(3):
            X=add(
                mm(mm(mm(mm(R,Bi[i]),R),Bi[j]),R),
                mm(mm(mm(mm(R,Bi[j]),R),Bi[i]),R))
            row.append(sand(sub(X,mm(mm(R,Bij[i][j]),R))))
        gij.append(row)
    assert g==cov_metric(w0)
    assert gij==[[gij[j][i] for j in range(3)] for i in range(3)]
    return g,gi,gij

def levi_civita_curvature(g,gi,gij):
    """The exact torsion-free metric connection, Ricci and R at a point.

    Ric_ij=∂kΓ^k_ij-∂jΓ^k_ik
             +Γ^k_ijΓ^l_kl-Γ^l_ikΓ^k_jl.
    """
    gi_inv=inv(g)
    dgi_inv=[scale(mm(mm(gi_inv,gi[m]),gi_inv),-1)
             for m in range(3)]
    Gamma=[[[sum((gi_inv[k][l]*
                    (gi[i][j][l]+gi[j][i][l]-gi[l][i][j])
                    for l in range(3)),F(0))/2
              for j in range(3)] for i in range(3)]
           for k in range(3)]
    dGamma=[[[[sum(
                  (dgi_inv[m][k][l]*
                   (gi[i][j][l]+gi[j][i][l]-gi[l][i][j])
                   +gi_inv[k][l]*
                   (gij[m][i][j][l]+gij[m][j][i][l]
                    -gij[m][l][i][j])
                   for l in range(3)),F(0))/2
                 for j in range(3)] for i in range(3)]
             for k in range(3)] for m in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                assert Gamma[k][i][j]==Gamma[k][j][i]
                for m in range(3):
                    lhs=gi[m][i][j]
                    rhs=sum((Gamma[a][m][i]*g[a][j]
                           +Gamma[a][m][j]*g[i][a]
                            for a in range(3)),F(0))
                    assert lhs==rhs
    Ric=zeros(3,3)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                Ric[i][j]+=dGamma[k][k][i][j]-dGamma[j][k][i][k]
                for l in range(3):
                    Ric[i][j]+=(Gamma[k][i][j]*Gamma[l][k][l]
                               -Gamma[l][i][k]*Gamma[k][j][l])
    assert Ric==trans(Ric)
    R=trace(mm(gi_inv,Ric))
    Einstein=sub(Ric,scale(g,R/2))
    assert trace(mm(gi_inv,Einstein))==-R/2
    return R,Ric,Einstein,Gamma

# Independent non-isotropic rational weight 2-jet, including
# nonzero first jets, nonzero Levi-Civita connection and curvature.
w0=[F(x) for x in (1,2,1,3,2,4)]
wi=[[F((i+1)*(e%3-1),20) for e in range(6)] for i in range(3)]
wij=[[[F((i+j+2)*(1 if e%2 else -1),50) for e in range(6)]
       for j in range(3)] for i in range(3)]
g,gi,gij=metric_jets(w0,wi,wij)
R,Ric,Ein,Gamma=levi_civita_curvature(g,gi,gij)
assert R==F(-120893,8640000)
assert Gamma[0][0][0]==F(-7,540)
assert Ric[0][1]==F(3713,1215000)
assert R!=0 and any(gi[k][a][b] for k in range(3)
                    for a in range(3) for b in range(3))
# Exact spatial inverse-metric jet chain against independent
# finite neighbor metrics with two-sided displacement:
def w_at(x):
    return [w0[e]
            +sum((wi[i][e]*x[i] for i in range(3)),F(0))
            +sum((wij[i][j][e]*x[i]*x[j]/2 for i in range(3)
                  for j in range(3)),F(0))
            for e in range(6)]
for h in (F(1,1000),F(1,10000)):
    for i in range(3):
        xp=[F(int(k==i))*h for k in range(3)]
        xn=[-x for x in xp]
        central=scale(sub(cov_metric(w_at(xp)),
                          cov_metric(w_at(xn))),1/(2*h))
        assert max(abs(central[a][b]-gi[i][a][b])
                   for a in range(3) for b in range(3))<F(1,100)

# Exact site-relabel / internal S-frame gauge covariance.
# EXTERNALLY DECLARED solder must be transformed accordingly;
# otherwise these matrices are not spatial coordinate tensors.
perm=(1,0,2,3)
P=zeros(4,4)
for a,b in enumerate(perm):P[b][a]=F(1)
L=mm(mm(inv(G),trans(frame)),mm(P,frame))
assert mm(frame,L)==mm(P,frame)
def permute_weights(w):
    d={}
    for (a,b),v in zip(edges,w):
        d[tuple(sorted((perm[a],perm[b])))]=v
    return [d[e] for e in edges]
wp=permute_weights(w0)
gp,gpi,gpij=metric_jets(wp,[permute_weights(x) for x in wi],
    [[permute_weights(x) for x in row] for row in wij])
assert mm(mm(trans(L),gp),L)==g
for i in range(3):
    assert mm(mm(trans(L),gpi[i]),L)==gi[i]
    for j in range(3):
        assert mm(mm(trans(L),gpij[i][j]),L)==gij[i][j]
# If solder frame transforms compatibly as above, same physical
# scalar curvature follows (spatial coordinates are held fixed).
Rp,Ricp,Einp,Gamp=levi_civita_curvature(gp,gpi,gpij)
assert Rp==R
assert mm(mm(trans(L),Ricp),L)==Ric
assert mm(mm(trans(L),Einp),L)==Ein

# A physically independent solder choice is NECESSARY: S is an
# internal fiber. For this audit we adopt a constant chosen solder
# mapping frame f_i to spatial coordinate directions ∂_i and
# Euclidean BACKGROUND norm q=x^T G x, NOT |x|² in this
# nonorthonormal f-basis. This makes scalar R=-3c match the
# orthonormal-frame formulation in H52.
def quad(x):
    return sum((x[i]*G[i][j]*x[j]
                for i in range(3) for j in range(3)),F(0))
def isotropic_w(c,x):
    w=F(1)-c*quad(x)
    assert w>0
    return [w]*6
def isotropic_metric(c,x):
    return cov_metric(isotropic_w(c,x))
def conformal_jets(c):
    ww=[F(1)]*6
    dw=[[F(0)]*6 for _ in range(3)]
    d2w=[[[-2*c*G[i][j]]*6 for j in range(3)]
         for i in range(3)]
    return metric_jets(ww,dw,d2w)
for c in (F(-2),F(0),F(1),F(3,2)):
    gg,gg_i,gg_ij=conformal_jets(c)
    sc,Ricci,En,Ga=levi_civita_curvature(gg,gg_i,gg_ij)
    assert gg==scale(G,F(4))
    assert all(x==zeros(3,3) for x in gg_i)
    for i in range(3):
        for j in range(3):
            assert gg_ij[i][j]==scale(G,8*c*G[i][j])
    assert sc==-3*c
    assert Ricci==scale(G,-4*c)
# H52 no-go remains: c=0 and c=1 have same w(0)=1 and
# first jets but distinct scalar R(0)=0,-3.

# Neighbor-cell gluing stencil with exact rational samples.
# 2nd derivatives from 6 axis neighbors, plus 4 diagonal
# neighbors for each mixed pair. This presupposes a COMMON
# spatial coordinate chart and solder across ALL cells.
def metric_stencil(c,h):
    center=[F(0)]*3
    base=isotropic_metric(c,center)
    basis=I(3)
    def evalx(x):return isotropic_metric(c,x)
    gi_st=[];gij_st=[]
    for i in range(3):
        plus=[h*x for x in basis[i]]
        minus=[-x for x in plus]
        gi_st.append(scale(sub(evalx(plus),evalx(minus)),1/(2*h)))
    for i in range(3):
        row=[]
        for j in range(3):
            if i==j:
                plus=[h*x for x in basis[i]]
                minus=[-x for x in plus]
                H=scale(add(sub(evalx(plus),scale(base,2)),
                            evalx(minus)),1/(h*h))
            else:
                pp=[h*(basis[i][k]+basis[j][k]) for k in range(3)]
                pm=[h*(basis[i][k]-basis[j][k]) for k in range(3)]
                mp=[-v for v in pm]
                nn=[-v for v in pp]
                H=scale(add(sub(evalx(pp),evalx(pm)),
                            sub(evalx(nn),evalx(mp))),1/(4*h*h))
            row.append(H)
        gij_st.append(row)
    return base,gi_st,gij_st

# Conformal family exact stencil identity and uniform rate.
def Rh_formula(c,h):
    u=c*h*h
    return F(3)*c*(F(-1)+9*u)/((1-6*u)*(1-2*u))
def err_formula(c,h):
    u=c*h*h
    return 3*c*c*h*h*(1+12*u)/((1-6*u)*(1-2*u))
for c in (F(-3,2),F(-1),F(0),F(1),F(3,2)):
    for h in (F(1,4),F(1,10),F(1,20),F(1,40)):
        st=metric_stencil(c,h)
        approx,_,_,_=levi_civita_curvature(*st)
        assert approx==Rh_formula(c,h)
        assert approx+3*c==err_formula(c,h)
        # Exact worst-case bound for |c|<=3/2, h<=1/4:
        # denominator >=(7/16)(13/16)=91/256,
        # |1+12 c h²| <=17/8.
        assert abs(approx+3*c)<=F(1632,91)*c*c*h*h
        if c!=0 and h<=F(1,10):
            assert abs(approx+3*c)<F(20)*c*c*h*h
# Smooth w∈C^4 on a compact positive domain ⇒ central
# first/second difference g_jets O(h²); local curvature is
# continuous rational function of the nondegenerate 2-jet,
# giving R_h=R+O(h²). Above family certifies exact constants.
print("PASS H53: exact K4 inverse-metric 2-jets and Levi-Civita torsion-free metric-compatibility")
print("PASS H53: nontrivial anisotropic gradient + Hessian gives exact rational Ricci and R")
print("PASS H53: K4 vertex permutation plus transformed solder/frame preserves scalar and Ricci tensors")
print("PASS H53: spatial curvature R(0)=-3c from independently supplied smooth positive field 2-jets")
print("PASS H53: neighboring-cell central curvature stencil exact Rh=3c(-1+9ch²)/((1-6ch²)(1-2ch²))")
print("PASS H53: rigorously bounded O(h²) scalar-curvature stencil error 1632/91*c²*h²")
print("BOUNDARY: spatial base, gluing, coordinate-solder consistency, derivatives are EXTERNAL assumptions")
print("BOUNDARY: no emergent P7/P8 physical solder, EH/ADM/HDA constraint closure or Einstein equations")
