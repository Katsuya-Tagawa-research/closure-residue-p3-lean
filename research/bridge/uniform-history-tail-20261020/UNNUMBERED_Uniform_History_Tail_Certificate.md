# Uniform History-Tail Certificate — independent audit candidate

**2026-10-20 | P11 OA-G39–G42 → P3–P11 Mathematical Bridge (H82)**
**Status:** UNNUMBERED research audit only. No H identifier, pull request, merge, frozen-paper update or claim of human peer review.

## Three distinct proof obligations

Finite weighted-Hankel rank is a **linear prediction** property. A finite positive/CPTP quantum instrument realization is a second property. Exact retrieval of individual event times from an **archive** is a third property. None of these can be substituted for the others in a P11 access certificate.

### OA-G39/G40
For \(0<\eta<1\) let \(K_N=\operatorname{diag}(1,\sqrt{\eta})\) and \(K_E=\sqrt{1-\eta}|0\rangle\langle1|\). This is a two-dimensional CP quantum instrument with first-event distribution \((1-\eta)\eta^{k-1}\). Its all-event-word series admits a two-state representation; the 2×2 Hankel minor on empty/E prefixes and suffixes has determinant \(-(1-\eta)^2\ne0\), hence **rank exactly two**. Terminal perfect classification of event times \(1,\ldots,n\) plus a no-event-by-\(n\) symbol requires at least \(n+1\) orthogonal states, if no external clock supplies the unknown event time.

### OA-G41 — qualification
For exact-event-time classification with expected error \(\le\varepsilon\), \(0<\eta,\varepsilon<1\), no free side-information of K, and **no compulsory separate overflow indicator**, the optimal D-dimensional (even quantum) terminal archive has success \(\sum_{k=1}^D p_k=1-\eta^D\), hence \(D_\varepsilon=\lceil\log\varepsilon/\log\eta\rceil\). For a D-dimensional code with conditional guessing success \(t_k=\mathrm{Tr}(M_k\rho_k)\), \(0\le t_k\le1\), and \(\sum_k t_k\le D\). Maximizing weighted success over these constraints selects the D largest priors; D orthogonal codewords attain it. Requiring an independently recognizable overflow label changes the number of recorded symbols. This is **not** a minimum *online CP memory* dimension. A terminal horizon can be known without the hidden K being provided.

### OA-G42 — correct quantifier
For substochastic finite absorbing Markov \(Q_M\) and \(s_M(K)=\alpha_MQ_M^K\mathbf 1\), the **existence of one common truncation cutoff for every worst-case error tolerance** is equivalent to \(\lim_{K\to\infty}\sup_Ms_M(K)=0\). This is not a theorem about every possible lossy compression or a model-dependent K.
* If \(d_M\le d_*\) and \(\rho(Q_M)\le1-\delta\), then uniform convergence follows via compactness of substochastic matrices, continuity of powers, a finite cover of strict power-contraction neighborhoods, and finitely many dimensions.
* The uniform spectral gap is not necessary: \(Q_m=\operatorname{diag}(0,1-1/m)\), \(\alpha_m=(1-1/m,1/m)\), give \(s_m(K)=m^{-1}(1-1/m)^K\le1/(K+1)\) for \(K\ge1\), while \(\rho(Q_m)\to1\).
* Unbounded dimensions defeat gap-only sufficiency: deterministic forward shifts \(Q_m\), with \(Q_m^m=0\), have \(\rho(Q_m)=0\) but \(\sup_m s_m(K)=1\) for every K.

### Quantum no-event certificate
Candidate typed object: \(\mathsf{UH}=(\mathcal H,\mathcal N,\{\mathcal E_a\},\mathsf S,\mathsf{Sched},\ell,b,\varepsilon,K)\).
Audit Choi \(J_{\mathcal N}\succeq0\), trace nonincrease \(\mathcal N^*(I)\preceq I\), complete CP instrument normalization, allowed initial states and legal repeated no-event schedule. If \(\mathcal N^{*\ell}(I)\preceq bI\), \(0\le b<1\), then \(\mathrm{Tr}\mathcal N^n(\rho)\le b^{\lfloor n/\ell\rfloor}\) for every density input. For \(0<b<1\), \(K=\ell\lceil\log\varepsilon/\log b\rceil\) suffices. A reachability-only certificate is weaker and needs its own invariance audit.

Exact nontrivial example: \(K_N=\left(\begin{smallmatrix}0&1\\1/2&0\end{smallmatrix}\right)\), \(K_E=\operatorname{diag}(\sqrt3/2,0)\) give a CPTP instrument, \(\mathcal N^*(I)=\operatorname{diag}(1/4,1)\) (no strict one-step contraction), but \(\mathcal N^{*2}(I)=I/4\). Both CP/TNI no-event maps with induced Hermitian trace-norm difference \(\le\xi\) satisfy a conservative perturbed bound \(b+\ell\xi\), by telescoping and trace/operator norm duality; it is useful when \(b+\ell\xi<1\). Source-model parameter differences alone are **not** this operator-norm bound.

### Source versus event spectral gap
Let \(\mathcal S(X)=\operatorname{Tr}(X)|0\rangle\langle0|\), a qubit replacer CPTP source, with superoperator eigenvalues \(1,0,0,0\), hence maximal nonstationary spectral gap. For \(p>0\), two-outcome CP instrument \(\mathcal N_p=(1-p)\mathcal S,\ \mathcal E_p=p\mathcal S\) sums to that same \(\mathcal S\), while no-event survival is \((1-p)^K\), not uniformly small over \(p\downarrow0\). Source spectral gap and event-history tail are not interchangeable.

### Required provenance and exclusions
The verified **finite** proofs do not derive the quantum instrument or recurrence schedule from F. No equality with original P3 quadratic Closure–Residue filtration, no frozen P6 observer provenance, no KKS→ADM/Einstein and no P11 Generative Completeness. Do not reopen finite-memory rank optimization. This unnumbered branch carries an exact regression checker; H82 formal integration remains a separate approval step.
