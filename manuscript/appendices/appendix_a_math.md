# Appendix A: Mathematical Prerequisites

---

This appendix provides the mathematical background needed to follow the formal arguments in the text. It is self-contained for readers with undergraduate linear algebra and basic real analysis. For full proofs and deeper development, see *Geometric Methods in Computational Modeling* (Bond, 2026a) and *Geometric Reasoning: From Search to Manifolds* (Bond, 2026c).

## A.1 Manifolds

A **smooth manifold** $M$ of dimension $d$ is a topological space that is locally homeomorphic to $\mathbb{R}^d$. Every point $p \in M$ has a neighborhood that can be mapped bijectively to an open subset of $\mathbb{R}^d$ by a coordinate chart $\phi: U \to \mathbb{R}^d$. The collection of charts $\{(U_\alpha, \phi_\alpha)\}$ is an atlas. When the transition maps $\phi_\beta \circ \phi_\alpha^{-1}$ are smooth (infinitely differentiable), the manifold is smooth.

**Intuition for the learner manifold.** The learner manifold $\mathcal{L}$ is a six-dimensional smooth manifold. Each point represents a learner state. The six coordinate functions $(d_1, \ldots, d_6)$ provide a coordinate chart. The smoothness assumption means that small changes in the learner state produce small changes in the coordinates --- learning is locally continuous.

## A.2 Tangent Spaces and Vectors

At each point $p \in M$, the **tangent space** $T_pM$ is the $d$-dimensional vector space of directions in which one can move from $p$. A tangent vector $v \in T_pM$ represents an infinitesimal displacement.

**Intuition.** The tangent space at a learner state represents the local neighborhood of accessible learning transitions. A tangent vector represents a learning step: a small change in domain knowledge, procedural skill, metacognition, or any combination.

## A.3 Riemannian Metrics

A **Riemannian metric** is a smooth assignment of an inner product $g_p: T_pM \times T_pM \to \mathbb{R}$ to each tangent space. In coordinates, the metric is represented by a symmetric positive-definite matrix $g_{ij}(x)$, the **metric tensor**. The squared length of a tangent vector $v$ is:

$$\|v\|^2 = g_{ij}(x) v^i v^j$$

The **geodesic distance** between two points is the infimum of the lengths of all smooth paths connecting them:

$$d(p, q) = \inf_{\gamma: p \to q} \int_0^1 \sqrt{g_{ij}(\gamma(t)) \dot{\gamma}^i(t) \dot{\gamma}^j(t)} \, dt$$

**Intuition.** The metric tensor at a learner state encodes the cost of learning transitions. If $g_{11}$ is large, increasing domain knowledge is expensive at this position. If $g_{12}$ is large, simultaneous changes in domain knowledge and procedural skill interact strongly. The geodesic is the minimum-cost learning path.

## A.4 Curvature

The **Riemann curvature tensor** $R^l_{ijk}$ measures how the metric varies from point to point. Positive curvature means that geodesics converge; negative curvature means they diverge. Zero curvature means the space is flat (Euclidean).

The **Ricci curvature** $R_{ij} = R^k_{ikj}$ and the **scalar curvature** $R = g^{ij}R_{ij}$ are contractions of the Riemann tensor that summarize the curvature in lower-dimensional form.

**Intuition.** High curvature on the learner manifold means that the difficulty of learning varies sharply from one position to another. A student in a high-curvature region experiences rapidly changing learning conditions --- small moves on the manifold produce large changes in the learning cost.

## A.5 Geodesics

A **geodesic** is a curve $\gamma(t)$ on $M$ that satisfies the geodesic equation:

$$\frac{d^2 \gamma^k}{dt^2} + \Gamma^k_{ij} \frac{d\gamma^i}{dt} \frac{d\gamma^j}{dt} = 0$$

where $\Gamma^k_{ij}$ are the **Christoffel symbols**, computed from the metric:

$$\Gamma^k_{ij} = \frac{1}{2} g^{kl}\left(\frac{\partial g_{il}}{\partial x^j} + \frac{\partial g_{jl}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^l}\right)$$

On a flat manifold, geodesics are straight lines. On a curved manifold, geodesics curve in response to the geometry.

## A.6 Parallel Transport and Holonomy

**Parallel transport** carries a vector along a curve on the manifold while keeping it "as constant as possible" relative to the manifold's geometry. The transported vector $v(t)$ satisfies:

$$\frac{Dv^k}{dt} = \frac{dv^k}{dt} + \Gamma^k_{ij} \frac{d\gamma^i}{dt} v^j = 0$$

The **holonomy** of a closed loop is the rotation accumulated during parallel transport around the loop. On a flat manifold, holonomy is zero. On a curved manifold, holonomy is proportional to the curvature enclosed by the loop.

**Intuition.** Parallel transport is the geometric formalization of transfer learning: carrying knowledge from one domain to another along a path through the manifold. Holonomy is the distortion incurred during transfer.

## A.7 Gauge Invariance

A **gauge transformation** is a change of coordinates that preserves the physical content of a theory. A quantity is **gauge-invariant** if its value does not change under gauge transformations.

In the educational context, a gauge transformation is a meaning-preserving re-description of the assessment instrument (different format, different language, different examiner, different context). The Assessment Gauge Invariance Theorem requires that the measured learner state be invariant under these transformations.

## A.8 The A* Search Algorithm

The **A* algorithm** finds the minimum-cost path from a start state to a goal region on a weighted graph. It maintains a priority queue ordered by $f(n) = g(n) + h(n)$, where $g(n)$ is the cost from start to $n$ and $h(n)$ is a heuristic estimate of the remaining cost from $n$ to the goal.

**Optimality theorem.** If $h(n)$ is admissible (never overestimates the true remaining cost), A* finds the minimum-cost path.

**Intuition.** Curriculum design is A* search on the learner manifold. The heuristic function is provided by the curriculum designer (or teacher). If the heuristic is admissible, the curriculum is optimal.

## A.9 The Mahalanobis Distance

The **Mahalanobis distance** between points $\mathbf{x}$ and $\mathbf{y}$ with respect to covariance matrix $\Sigma$ is:

$$d_M(\mathbf{x}, \mathbf{y}) = \sqrt{(\mathbf{x} - \mathbf{y})^T \Sigma^{-1} (\mathbf{x} - \mathbf{y})}$$

The Mahalanobis distance is the geodesic distance on a manifold with constant metric $g_{ij} = (\Sigma^{-1})_{ij}$. It accounts for correlations between dimensions and differences in scale: dimensions with high variance contribute less to the distance, and correlated dimensions are treated as partially redundant.

**Intuition.** The Mahalanobis distance is the "natural" distance on the learner manifold when the metric is approximated by its value at a single point (a local linear approximation). It accounts for the fact that some learning dimensions are correlated and that changes along correlated dimensions are partially redundant.

---

*For complete proofs and fuller development of all topics, see Bond (2026a), Chapters 2--5.*
