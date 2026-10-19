# P11-SPS H113–H118 — Static Primitive Selection (2026-10-19)

**Naming:** SPS-H113…SPS-H118 are the local P3–P11 Mathematical Bridge results on static primitive selection. They are **not** the GitHub PR #132 P11-H113 result on H75 memory feedback. This Draft branch is based on `main`, not the existing stacked P11/P9 PRs.

## Reproduce
```bash
python -m pip install sympy==1.14.0
python research/p11/sps-h113-h118-20261019/audits/verify_sps_h113_h118.py
```

| Study | Result and scope |
|---|---|
| SPS-H113 | Fibre-descent condition and baseline-control nonidentifiability in 3 levels. H37 sector ranks initially supplied from Step 1D, not audited here. |
| SPS-H114 | All-order nonidentifiability **only over the specified marked-control alphabet**; Lie-reachability vs native locality. |
| SPS-H115 | Actual rational H37 generator model: Krylov ranks 5,9,13,17,21,23,25; hidden 0,4,8,12,16,18,20; `so(5)` native Lie closure. Grade-by-grade equality with original P3 discrete channel not claimed. |
| SPS-H116 | Relative independence of AX-BIMOD under the specified weak H37 interface; fixed sector invariance is stronger than gauge covariance. Not independence from every possible P3/P4 axiom. |
| SPS-H117 | Equivariant sector assignments on H37's gauge orbit can differ; `cl_D` forgets primitive-source provenance. Equivariance on an orbit is **not** universal categorical naturality. |
| SPS-H118 | Fibre-refinement criterion and conditional gauge-covariant, locality-preserving, restriction-compatible sector closure from **externally supplied** source operators. |

### Distinguish

`H_k(Phi,D)`: dynamical P3 filtration; `S_static`: sourced primitive list; `J_N`: static operator sector; `T_0M_phys`: native calibrated tangent; `Lie(K_native)`: switch-generated controllability. Their equality is not assumed.

### Limits / STOP
Finite symbolic PASS does not mean physical provenance, independent apparatus calibration, experimental P6 gate, CR-exclusive GKSL separation, P9 Einstein dynamics, or P11 Generative Completeness. No Lean mechanization or human peer review of this package. Frozen P1–P8, main, and other Draft PRs are not changed. No new arbitrary `J5` candidates are introduced.

**Next gate SPS-H119:** intrinsic, non-circular source-origin rule or an explicit justified source-selection stop condition. A selector on data already derived from the same CR fingerprint cannot resolve a nonconstant fibre.
