# P11–AX04 (2026-10-19): Observer-Effect Generation and Markov Closure

Stacked on AX03 Draft PR #141; independent of SPS native-static source selection. No changes to main or frozen P1–P8.

Run:

\`\`\`sh
python -m pip install sympy==1.14.0
python research/p11/ax04-effect-generation-20261019/P11_AX04_effect_generation_audit.py
\`\`\`

Expected **195 exact SymPy assertions PASS**. H37 full population POVM: D5 dim5 -> invariant generated M5 dim25 in 1 *-algebra stage. One-endpoint effect tower: 2,5,10,17,25. Original D5 observer is not dynamically autonomous. Same phase channel with X/Z effect list has different observable *-algebra closure.

**OPEN:** Independent observer effect list from F, physical readout availability of derived algebra elements, P3-original residue matching, P6 experimental gate, P9 gravity, P11 Generative Completeness. CI finite checks are not Lean formal proof or human peer review.
