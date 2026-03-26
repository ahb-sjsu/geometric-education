# Appendix D: Notation and Conventions

---

All notation is consistent with the Geometric Series convention established in *Geometric Methods* (Bond, 2026a) and *Geometric Reasoning* (Bond, 2026c).

## D.1 Core Objects

| Symbol | Object | Definition |
|--------|--------|-----------|
| $\mathcal{L}$ | Learner manifold | 6-dimensional Riemannian manifold of learner states |
| $\mathbf{x}$ | Learner state | Point on $\mathcal{L}$; $\mathbf{x} = (d_1, d_2, d_3, d_4, d_5, d_6)$ |
| $d_1$ | Domain knowledge | Factual and conceptual understanding |
| $d_2$ | Procedural skill | Construction, execution, performance ability |
| $d_3$ | Metacognitive awareness | Self-monitoring, calibration, strategy regulation |
| $d_4$ | Motivation and engagement | Intrinsic interest, persistence, self-efficacy |
| $d_5$ | Transfer ability | Cross-domain application, structural analogy |
| $d_6$ | Creativity | Novel recombination, generative capacity |
| $g_{ij}$ | Learner metric | Riemannian metric tensor on $\mathcal{L}$ |
| $\Sigma$ | Covariance matrix | $6 \times 6$ symmetric positive-definite matrix |
| $\gamma^*$ | Geodesic | Minimum-cost path on $\mathcal{L}$ |
| $G$ | Goal region | Set of acceptable learner states (degree requirements) |
| $G(\mathbf{x})$ | GPA function | Scalar assessment: $G: \mathcal{L} \to \mathbb{R}$ |
| $h_T$ | Pedagogical heuristic | Teacher's estimate of distance to goal |
| $h_P$ | Inherited heuristic | Heuristic field from parents/family |
| $h_{\text{AI}}$ | AI heuristic | Heuristic field from AI tutoring system |
| $R_{ijkl}$ | Riemann curvature | Curvature tensor of the learner manifold |
| $\Gamma^k_{ij}$ | Christoffel symbols | Connection coefficients for geodesic equation |

## D.2 Assessment and Evaluation

| Symbol | Object | Definition |
|--------|--------|-----------|
| $A(\mathbf{x}, I)$ | Assessment function | Maps learner state and instrument to score |
| $V_{ij}$ | Gauge violation tensor | Expected score change under gauge transformation $i$ on dimension $j$ |
| $\text{GIS}$ | Gauge invariance score | Composite measure of assessment gauge invariance |
| $\psi$ | Reconstruction function | Best estimate of $\mathbf{x}$ from $G(\mathbf{x})$ |

## D.3 Moral Injury

| Symbol | Object | Definition |
|--------|--------|-----------|
| $\text{MI}$ | Moral injury | Accumulated distortion from forced contraction |
| $\Delta \text{MI}(t)$ | Moral injury increment | Injury from a single grading event at time $t$ |

## D.4 Structural Inequality

| Symbol | Object | Definition |
|--------|--------|-----------|
| $\text{BI}(P, S)$ | Bond Index | Expected learning deviation under policy $P$ for population $S$ |
| $\text{LD}(\gamma)$ | Learning deviation | Integrated distance between actual path and geodesic |
| $\gamma_P^*$ | Policy-constrained path | Learning trajectory available under policy $P$ |
| $\gamma_\mathcal{L}^*$ | Manifold geodesic | Optimal trajectory on the full manifold |
| $\Delta g$ | Metric gap | Difference in effective metrics between populations |

## D.5 Transfer

| Symbol | Object | Definition |
|--------|--------|-----------|
| $D_1, D_2$ | Domain charts | Coordinate neighborhoods on $\mathcal{L}$ |
| $\mathbf{k}$ | Knowledge vector | Tangent vector representing a concept |
| $H(\gamma)$ | Holonomy | Rotation accumulated during parallel transport |
| $\omega$ | Connection 1-form | Encodes parallel transport rule |

## D.6 Series Cross-References

| Abbreviation | Full Title |
|-------------|-----------|
| GM | *Geometric Methods in Computational Modeling* (Bond, 2026a) |
| GR | *Geometric Reasoning: From Search to Manifolds* (Bond, 2026c) |
| GE | *Geometric Ethics: The Mathematical Structure of Moral Reasoning* (Bond, 2026b) |
| GEcon | *Geometric Economics* (Bond, 2026d) |
| GL | *Geometric Law* (Bond, 2026e) |
| GCog | *Geometric Cognition* (Bond, 2026f) |
| GComm | *Geometric Communication* (Bond, 2026g) |
| GMed | *Geometric Medicine* (Bond, 2026h) |
| GEd | *Geometric Education* (this volume) |

## D.7 Conventions

- **Indices.** Latin indices $i, j, k, l$ run from 1 to 6 (the dimensions of the learner manifold). Einstein summation convention is used: repeated upper and lower indices are summed.
- **Units.** All dimension values are normalized to $[0, 1]$ unless otherwise stated.
- **Metric signature.** The learner metric is positive-definite (Riemannian, not pseudo-Riemannian).
- **Path parameterization.** Paths are parameterized by $t \in [0, 1]$ (normalized time) or by arc length $s$ (distance along the path).
