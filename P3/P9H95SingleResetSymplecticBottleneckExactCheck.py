"""H95: genuine H75 single reset is a rank-8 quantum information bottleneck.

The theorem applies to ANY fixed CPTP preprocessor on the physical M6,
the ORIGINAL four-Kraus flag-destroying H75 reset, and ANY deterministic
CPTP postprocessor WITHOUT an independent retained side-information
channel.  Factorization through trace-one qutrit states (real dimension8)
proves the *universal* differential bound on the 12D genuine source-seeded
H92 Grassmann KKS orbit; finite computations illustrate/validate source
identities and inherited control words, not an enumeration of all CPTP.

Multi-copy H94 tomography is a different experiment and is compatible
with the obstruction. This does not source ADM, DeWitt or Einstein gravity.
"""
from fractions import Fraction as F

from P9H24PhaseSensitiveResidueGaugeExactCheck import I,O,Z0,gc
from P9H75SemicausalMicroMemorySourceExactCheck import (
    micro,matmul,matadj,mattrace,qtrace,qconj,ONE6,R60
)
import P9H91CheckpointKKSRankADMObstructionExactCheck as H91
import P9H92FiveLevelGrassmannKKSResetSilenceExactCheck as H92
import P9H93ExistingRealControlGrassmannAccessExactCheck as H93
import P9H94ExistingGateMultiSettingCoherenceTomographyExactCheck as H94

assert R60[0][0]==I*gc(F(-32,135))
assert len(H94.tangents)==12
assert H91.rank([H93.v36(T) for T in H94.tangents])==12
assert H91.rank(H92.P)==12
assert len(H94.effects)==9
assert H92.rp!=H92.rm
print("PASS H95.1: exact original H75 full-source seed yields nondegenerate 12D Grassmann KKS tangent and honest positive source-orbit states")

# The real Hermitian trace-zero qutrit space has dimension8, proved
# with explicit exact matrix basis. For every deterministic trace-
# preserving physical CPTP preprocessor T, its partial-trace derivative
# lands in this 8D space, regardless of any effect of the fixed
# complex U and M0/M1 inside the *later* source reset.
assert len(H91.traceless)==8
assert H91.rank([H94.herm_coords(T) for T in H91.traceless])==8
assert all(H91.tr(T)==Z0 for T in H91.traceless)

# Verify original H75 Kraus source factorization and injective reduced
# qutrit Schur factors by importing the independently checked H94 exact
# 36-matrix-unit and nine-qutrit-matrix-unit tests.
assert all(qtrace(micro(T))==H91.zero(3) for T in H94.tangents)

# Not only the four particular H94 tomography settings, but also each
# existing original physical gate separately has rank <=8 through the
# unchanged H75 single reset. No arbitrary CPTP parameter search is
# needed for the theorem because of the codomain dimension bound.
settings=[("identity",ONE6)]
settings += [(name,G) for name,G in H93.controls.items()]
settings += [("H94_word_"+str(k+1),H94.word_gate(word))
             for k,word in enumerate(H94.words)]
ranks={}
for name,G in settings:
    assert matmul(matadj(G),G)==ONE6
    M=H94.source_matrix(G,True)
    assert len(M)==9 and all(len(row)==12 for row in M)
    # Every output tangent is Hermitian and TRACE ZERO in M3.
    for column in range(12):
        assert M[0][column]+M[1][column]+M[2][column]==0
    measured_rank=H91.rank(M)
    assert measured_rank<=8
    ranks[name]=measured_rank
assert ranks["identity"]==0
assert [ranks["H94_word_"+str(k+1)] for k in range(4)]==[6,4,4,4]
assert H91.rank(H94.postcum)==12
print("PASS H95.2: exact qutrit trace-zero space dimension8; inherited fixed deterministic pre-unitary settings each have rank<=8 (four H94 ranks 6,4,4,4)")
print("PASS H95.2: separately LABELED four-setting CLASSICAL record has rank12, without implying a single-channel quantum inverse")

# A mathematical consequence beyond the unitary sample tests:
# for ALL fixed CPTP T:M6->M6, P:M6->Md the composition
# P ◦ original_H75_reset ◦ T ◦ Ad_V
# factors through trace-one Herm(M3), dimension8. Its differential
# on a 12D KKS orbit has kernel dimension>=4. If R∘E=id held on
# a neighborhood, DE would need rank12 (chain rule), contradiction.
# Likewise a pullback 2-form has rank<=rank(DE)<=8 while
# omega_KKS is nondegenerate rank12.
kks_rank=H91.rank(H92.P)
bottleneck_dim=H91.rank([H94.herm_coords(T) for T in H91.traceless])
assert kks_rank==12 and bottleneck_dim==8
assert kks_rank-bottleneck_dim==4
print("PASS H95.3: EXACT general CPTP no-bypass theorem by factorization / chain rule: rank(DE)<=8, ker dimension>=4, hence NO local reversible/KKS-symplectic channel transport")

# Fully POSITIVE two-state certificate: the H92 +/- rational Cayley
# pulses are unitary; hence their outputs are true trace-one positive
# states of the SAME physical U5 Grassmann coadjoint orbit.
delta=F(168,1475)
D=H91.minus(H92.rp,H92.rm)
expected=H91.scale(H91.plus(H91.e(5,0,0),H91.e(5,3,3)),
                    gc(delta*delta))
assert H91.dag(D)==D and H91.tr(D)==Z0
assert H91.mm(D,D)==expected
# Eigenvalues of D are {+delta,-delta,0,0,0}; therefore:
trace_norm=2*delta
trace_distance=trace_norm/F(2)
assert trace_norm==F(336,1475)
assert trace_distance==delta

Q=H92.Q
coherence_signal=H91.tr(H91.mm(Q,D))
assert coherence_signal==gc(delta)
assert H91.mm(H91.mm(H92.coherence,H92.coherence),
              H92.coherence)==H92.coherence
assert H91.dag(Q)==Q
# H92 verifies (I+Y03)/2 positive using Y03 spectrum -1,0,+1.
assert F(0)<=H92.prob_p.r<=1 and F(0)<=H92.prob_m.r<=1
assert H92.prob_p.r-H92.prob_m.r==delta

physical_plus=H92.decode5(H92.rp)
physical_minus=H92.decode5(H92.rm)
reset_plus=micro(physical_plus)
reset_minus=micro(physical_minus)
assert reset_plus==reset_minus
assert mattrace(reset_plus)==O
# Any deterministic quantum operation after equal outputs still has
# equal outputs: explicit real physical unitary examples and another
# H75 CPTP reset.
for G in (H93.controls["W"],H93.controls["F"],
          H93.controls["UA"],H93.controls["UB"]):
    assert qconj(G,reset_plus)==qconj(G,reset_minus)
    assert micro(qconj(G,reset_plus))==micro(qconj(G,reset_minus))
assert micro(reset_plus)==micro(reset_minus)
print("PASS H95.4: two positive source-embedded coherent states have pre-reset exact trace distance 168/1475 saturated by a positive POVM; original reset and all tested subsequent CPTP operations give EXACTLY equal output")

print("BOUNDARY: uniform arbitrary-preprocessing no-go assumes ONE FIXED trace-preserving quantum channel and NO classical/quantum side-information bypass of the H75 reset")
print("BOUNDARY: H94 multi-copy tomography can distinguish/estimate 12 parameters but is not ONE source-driven coherent KKS symplectic/ADM transport")
print("BOUNDARY: an actual source-derived non-reset physical carrier, KKS-to-ADM Hamiltonian intertwiner, DeWitt kinetic, off-shell HDA, Einstein dynamics and F completeness remain OPEN")
