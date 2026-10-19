# P11-SPS H121: Infinitesimal Choi Noise Tangent

Stacked research Draft on PR #135. Distinct from H75-memory P11 H113 (#132); existing main and frozen P1–P8 stay untouched.

Reproduce after installing SymPy 1.14.0: python research/p11/sps-h121-20261019/P3P11_SPS_H121_infinitesimal_choi_audit.py

Expected: 78 exact assertions PASS, noise_C_rank=2, h37_noise_rank=4, canonical_H_coeffs=[1/5,0,1/7]; native control provenance remains OPEN. The positive compressed Choi derivative, associated traceless Lindblad span and canonical Hamiltonian extraction are standard conditional mathematical consequences of GKSL, not independent hardware provenance or P11 completeness. No human peer review, physical gate, or P9 gravity derivation.
