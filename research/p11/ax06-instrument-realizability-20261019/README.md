# P11–AX06: Instrument Realizability and Non-Circular Observer Selection

P11 axiomatization Draft stacked on AX05 #143. Separate from SPS primitive-origin series. Formal POVM and dilation **do not imply independently calibrated hardware**.

Reproduce with Python 3.11 and SymPy 1.14.0:

    python research/p11/ax06-instrument-realizability-20261019/P11_AX06_instrument_realizability_audit.py

Expect **133 exact checks PASS**: informationally complete six-outcome qubit POVM with two distinct selective instruments; a stronger matched-POVM/matched-nonselective-channel ambiguity; ancilla isometries; sequential-effect rank; full-qubit instrument-tomography frame rank16; formal H37 population Lüders/reset two-time distinction.

**OPEN**: actual native instruments, two-stage P6 CPTP gate, F-derived observer choice, original P3 residue identification, P9 Einstein dynamics, P11 Generative Completeness. No Lean formalization or human specialist review of this package.
