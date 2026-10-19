# P11–AX12: Independent source axioms and completeness decision

P11 axiomatization track, stacked as Draft on P11–AX11 (#149), not the SPS-H113–H123 primitive-selection series. Parent branches and `main` remain unchanged.

## Reproduce

```sh
python -m pip install sympy==1.14.0
python research/p11/ax12-source-axioms-20261019/P11_AX12_source_axioms_audit.py
```

Expect **312/312 exact checks**: rank-16 qubit tomography with independently specified tetrahedral state/effect frames; marked-port inventory gap; external orientation reference; locally unobservable environment dynamics with full 8-versus-0 superoperator trace witness; elementary no-equivariant-selector group action.

**Status:** Relative reconstruction G1 is conditional; physical source G2 and F Generative Completeness G3 are OPEN. The proposed independent input axioms are a proof-obligation ledger, not inferred facts. No original P3 R_k identification, P6 physical gate, P9 GR/HDA or independent human review is claimed.
