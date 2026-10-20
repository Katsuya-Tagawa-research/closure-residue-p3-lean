#!/usr/bin/env python3
"""Exact, independent H75/H81 AX-OA enlargement on user-supplied fixed-orbit pair.

Source: existing H75 U/M0/M1/Kraus, H81 W/F, H75 Cayley B and Q1.
Re-verifies same orbit, CPTP and positive effects, the H75 no-reset-first
witness, F-before-reset+Cayley-after-reset discrimination, and residual gates.
Does NOT independently verify the previously reported native 15-vector or
P9.181 GT-K4 map (complete formulas were not present in the handoff).
"""
import json
from pathlib import Path
import sympy as s

I=s.I
z57=s.sqrt(57)
n=6
checks=0

def check(condition,message):
    global checks
    if condition is not True and condition != s.true:
        raise AssertionError(message)
    checks+=1

def simp(M):
    return M.applyfunc(s.simplify)

def ad(U,X):
    return simp(U*X*U.H)

def b(a,b,p,q):
    return s.Matrix([[a,I*p,0],[-I*p,b,I*q],[0,-I*q,a]])

params=[(z57/50,s.S.Zero,s.S.Zero,s.Rational(8,75)),
        (257*z57/38450,s.Rational(2736,19225),256*z57/19225,-s.Rational(2056,57675))]
a=s.Rational(3,25);bb=s.Rational(11,25);cc=s.Rational(8,75)

def state(ps): return s.diag(b(a,bb,ps[0],ps[1]),b(cc,cc,ps[2],ps[3]))
rho,sigma=map(state,params)
delta=simp(sigma-rho)

# Fixed coadjoint orbit and positivity.
for x in [rho,sigma]:
    check(x==x.H,'Hermitian state')
    check(s.trace(x)==1,'unit trace')
    ev=x.eigenvals()
    check(all(y.is_nonnegative for y in ev),'positive semidefinite state')
for k in (0,1):
    sl=slice(3*k,3*k+3)
    check(rho[sl,sl].charpoly().as_expr()==sigma[sl,sl].charpoly().as_expr(),'same orbit block spectrum')
check(s.simplify(params[0][0]**2+params[0][1]**2-params[1][0]**2-params[1][1]**2)==0,'block0 radius')
check(s.simplify(params[0][2]**2+params[0][3]**2-params[1][2]**2-params[1][3]**2)==0,'block1 radius')

O=s.Matrix([[s.Rational(2,3),s.Rational(2,3),-s.Rational(1,3)],
            [-s.Rational(2,3),s.Rational(1,3),-s.Rational(2,3)],
            [-s.Rational(1,3),s.Rational(2,3),s.Rational(2,3)]])
U=s.diag(I,1,I)*O
M0=s.diag(1,s.Rational(3,5),s.Rational(3,5))
M1=s.diag(0,s.Rational(4,5),s.Rational(4,5))
check(U*U.H==s.eye(3),'H75 complex unitary')
check(M0.H*M0+M1.H*M1==s.eye(3),'H75 effects sum to identity')
Ks=[]
for alpha,M in enumerate([M0,M1]):
    for beta in range(2):
        ketbra=s.eye(2)[:,alpha]*s.eye(2)[beta,:]
        Ks.append(s.kronecker_product(ketbra,U*M))
check(sum((K.H*K for K in Ks),s.zeros(6))==s.eye(6),'four Kraus TP')

def phi(X):
    return simp(sum((K*X*K.H for K in Ks),s.zeros(6)))

W=s.kronecker_product(s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],
                                [s.Rational(4,5),s.Rational(3,5)]]),s.eye(3))
SW=s.Matrix([[0,1,0],[1,0,0],[0,0,1]])
Ffb=s.diag(s.eye(3),SW)
B=s.Matrix([[0,0,0],[0,0,-1],[0,1,0]])
y=s.Rational(1,3)
V3=simp((s.eye(3)+y*B)*(s.eye(3)-y*B).inv())
V=s.kronecker_product(s.eye(2),V3)
Q1=s.kronecker_product(s.eye(2),s.diag(0,1,0))
for name,u in [('W',W),('Ffb',Ffb),('Cayley',V)]:
    check(simp(u.H*u)==s.eye(6),name+' unitary')
check(Q1==Q1.H and simp(Q1*Q1)==Q1,'physical projective readout')
check(s.trace(Q1)==2,'rank2 measured site effect')

check(delta!=s.zeros(6),'distinct microscopic preparations')
check(phi(delta)==s.zeros(6),'compulsory reset first exactly erases pair')
check(phi(ad(W,delta))==s.zeros(6),'W alone before reset erased')

# Trace-preserving instrument branches: outcome site population probabilities.
def prob_after(z,prior):
    return s.simplify(s.trace(Q1*ad(V,phi(ad(prior,z)))))
def raw_prob_after(z,prior):
    return s.simplify(s.trace(Q1*phi(ad(prior,z))))

for name,prior in [('none',s.eye(6)),('W',W),('F',Ffb),('WF',Ffb*W),('FW',W*Ffb)]:
    dval=s.simplify(prob_after(sigma,prior)-prob_after(rho,prior))
    if name in ['none','W']:
        check(dval==0,'postreset readout still blind '+name)
    else:
        check(dval!=0,'added access distinguishes '+name)
    check(raw_prob_after(sigma,prior)-raw_prob_after(rho,prior)==0,'site readout before Cayley blind '+name)

F_diff=s.simplify(prob_after(sigma,Ffb)-prob_after(rho,Ffb))
WF_diff=s.simplify(prob_after(sigma,Ffb*W)-prob_after(rho,Ffb*W))
F_expected=-(s.Integer(350208)+12288*z57)/2403125
WF_expected=(s.Integer(2451456)+86016*z57)/60078125
check(s.simplify(F_diff-F_expected)==0,'F source Cayley exact signed contrast')
check(s.simplify(WF_diff-WF_expected)==0,'W F source Cayley exact signed contrast')

pvals={}
for n,prior in [('F',Ffb),('WF',Ffb*W)]:
    for tag,x in [('rho',rho),('sigma',sigma)]:
        pv=prob_after(x,prior)
        check(bool(s.N(pv)>0 and s.N(pv)<1),n+' valid probability '+tag)
        pvals[f'{n}_{tag}']=str(pv)

# If reset is mandatory first, no later intervention separates pair.
check(simp(phi(rho)-phi(sigma))==s.zeros(6),'full density matrix equality after source reset')
check(s.simplify(s.trace(Q1*ad(V,ad(Ffb,phi(rho))))-s.trace(Q1*ad(V,ad(Ffb,phi(sigma)))))==0,'postreset F Cayley cannot recover')

# A second source collision after F-only also converts coherence into population.
second=s.simplify(s.trace(Q1*(phi(phi(ad(Ffb,sigma)))-phi(phi(ad(Ffb,rho))))))
check(second!=0,'second reset accessible alternative distinguishes')
check(s.simplify(second+ s.Rational(93632,1441875)+22528*z57/4325625)==0,'two source contrast exact')


# A one-parameter, exactly nonzero-on-an-open-dense-set discrimination law.
# F before source makes a real 1-2 visible coherence; 2x2 Cayley rotates it
# into ordinary site1 population. No global metric descent is inferred.
postF=phi(ad(Ffb,delta))
real12=s.simplify(s.re(postF[1,2]+postF[4,5]))
expected_real12=(s.Integer(14592)+512*z57)/96125
check(s.simplify(real12-expected_real12)==0,'F-triggered real 1-2 coherence')
parameter=s.symbols('y',real=True)
response_family=s.factor(-4*parameter*(1-parameter**2)/(1+parameter**2)**2*real12)
for value in (s.Rational(1,3),s.Rational(1,4),s.Rational(-2,5),s.Rational(2),s.S.Zero,s.Integer(1),s.Integer(-1)):
    v3=s.simplify((s.eye(3)+value*B)*(s.eye(3)-value*B).inv())
    v6=s.kronecker_product(s.eye(2),v3)
    observed=s.simplify(s.trace(Q1*ad(v6,postF)))
    check(s.simplify(observed-response_family.subs(parameter,value))==0,f'generic-family {value}')
check(s.simplify(response_family.subs(parameter,s.Rational(1,3))-F_diff)==0,'generic formula special case')

# Reported GT six-vector difference is input data, NOT re-derived without full F formula.
GT_delta=s.Matrix([0,0,s.Rational(7485696,369600625),0,0,-s.Rational(3735552,369600625)])
check(GT_delta!=s.zeros(6,1),'reported GT vector collision conditional witness has nonzero components')
check(s.simplify(max(abs(x) for x in GT_delta)/2)==s.Rational(3742848,369600625),'reported GT half gap')

result={
 'title':'H75 fixed-orbit counterpair: existing-operations AX-OA separation',
 'date':'2026-10-20',
 'exact_assertions_passed':checks,
 'state_pair_same_U3_times_U3_orbit':True,
 'Phi_micro_delta_exact_zero':True,
 'one_step_preF_Phi_no_postCayley_site_readout_contrast_zero':True,
 'postreset_Cayley_V_0_1third_F_first_site1_sigma_minus_rho':str(F_diff),
 'postreset_Cayley_V_0_1third_W_then_F_site1_sigma_minus_rho':str(WF_diff),
 'CPTP_and_positive_POVM':True,
 'postreset_Cayley_y':str(y),
 'generic_V_0_y_site1_response_formula':str(response_family),
 'exceptional_real_Cayley_parameters':[0,1,-1],
 'F_only_post_source_visible_real_12_coherence':str(real12),
 'state_probabilities':pvals,
 'site1_second_Phi_after_F_sigma_minus_rho':str(second),
 'native_15_observables_collision':'REPORTED by independent source; not independently rederived',
 'GT_K4_metric_difference':'REPORTED by independent source; not independently rederived',
 'AX_OA_new_schedule_physical_executability':'OPEN',
 'H75_pair_physical_preparation':'OPEN',
 'global_operational_metric_descent':'OPEN',
 'G2_physical_provenance':'OPEN',
 'G3_F_generated_access':'OPEN',
 'KKS_fixed_orbit_intermediate_preservation':'NOT ASSUMED; micro CPTP interventions may leave orbit',
 'notes':'F feedback denotes flag-conditioned SWAP, not generative map F. All exact witnesses are conditional on these declared operators and this initial 6D basis.'
}
Path(__file__).with_name('H75_Access_Descent_Exact_Results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('EXACT PASS',checks,'assertions; F pre-reset Phi V(0,1/3) Q1 distinguishes original KKS counterpair')
print('F-only contrast:',F_diff,'\u2248',s.N(F_diff,14))
print('W then F contrast:',WF_diff,'\u2248',s.N(WF_diff,14))
print('Original Phi alone sends pair difference to zero; global descent remains OPEN')
