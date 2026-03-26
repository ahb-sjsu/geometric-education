# Index of Framework Concepts

---

This index lists the major concepts of the geometric framework for education, with their definitions, first appearances, and cross-references to the general Geometric Series theory.

## A

**A* search algorithm.** Optimal pathfinding on weighted graphs; the formal basis for curriculum design as pathfinding. Appendix A.8, Ch. 7.1--7.2. *Series: GR Ch. 3.*

**Admissible heuristic.** A heuristic function that never overestimates the remaining cost to the goal; the condition for optimal teaching. Def. 6.2, Ch. 6.2.1. *Series: GR Ch. 3.*

**Assessment function.** A map $A: \mathcal{L} \times \mathcal{I} \to \mathbb{R}$ from learner states and instruments to scores. Ch. 9.2.

**Assessment Gauge Invariance Theorem.** Theorem 9.1: valid assessment must be invariant under meaning-preserving re-description of the instrument. Ch. 9.2. *Series: GR Ch. 8, 11 (BIP).*

## B

**Bond Index, Educational.** $\text{BI}(P, S)$: the expected learning deviation imposed on population $S$ by policy $P$. Def. 13.1, Ch. 13.1. *Series: GE Ch. 16 (general Bond Index).*

**Boundary, educational.** A threshold on the learner manifold where the accessible region changes: prerequisite, institutional, or developmental. Def. 4.3, Ch. 4.7.

**Bloom's taxonomy.** Six levels of cognitive engagement (Knowledge through Evaluation), interpreted as six dimensions of the learner manifold. Ch. 3.5. Historical precursor.

## C

**Cold-start problem.** The challenge of estimating a new student's metric from limited data; the exploration-exploitation trade-off. Ch. 10.3.3.

**Contraction, scalar.** The mapping of a multi-dimensional learner state to a single number (GPA, test score). The central operation whose irreversibility is the book's core claim. Ch. 1.2, Ch. 5.

**Covariance matrix, learner.** $\Sigma$: the $6 \times 6$ SPD matrix encoding cross-dimensional interactions on the learner manifold. Ch. 4.4.1.

**Creativity ($d_6$).** The sixth dimension of the learner manifold: novel recombination and generative capacity. Ch. 4.2.6.

**Curvature.** The position-dependent difficulty of learning transitions; high curvature = hard transitions. Ch. 4.4.2, Appendix A.4.

## D

**Developmental topology.** The topological transitions in the learner manifold during cognitive development (Piaget's stages geometrized). Ch. 4.6.

**Domain knowledge ($d_1$).** The first dimension of the learner manifold: factual and conceptual understanding. Ch. 4.2.1.

## E

**Elective as geodesic freedom.** Elective courses provide student-directed exploration of the manifold, promoting transfer ($d_5$) and creativity ($d_6$). Prop. 7.3, Ch. 7.5.

**Epsilon-admissible heuristic.** A heuristic that overestimates by at most $\epsilon$; produces near-optimal teaching paths. Ch. 6.2.2.

## F

**Fiber.** The set of learner states that produce the same scalar grade; the level set of the GPA function. Ch. 1.4.3.

**First-generation heuristic deficit.** The absence of the inherited heuristic field $h_P$ for first-generation college students. Def. 6.5, Ch. 6.4.

**Format gauge violation.** Score change under assessment format transformation; one of five gauge invariance tests. Ch. 9.3.2.

## G

**Gauge invariance.** The requirement that measured understanding be invariant under meaning-preserving re-description. Ch. 9.1, Appendix A.7. *Series: GR Ch. 8, 11.*

**Gauge violation tensor.** $V_{ij}$: the matrix of expected score changes under gauge transformations. Def. 9.2, Ch. 9.4.

**Geodesic, learner.** The minimum-cost path on $\mathcal{L}$ from a starting state to the goal region. Def. 4.2, Ch. 4.5.

**Geodesic divergence.** Theorem 5.3: the GPA-optimal path diverges from the geodesic by an unbounded amount. Ch. 5.4.

**Goal region.** The set of learner states satisfying the educational objective. Def. 4.4, Ch. 4.8.

**GPA contraction.** The mapping $G: \mathcal{L} \to \mathbb{R}$; the specific scalar assessment function analyzed throughout the book. Ch. 1.2.1.

**GPA Irrecoverability Theorem.** Theorems 5.1--5.3: any scalar assessment on the learner manifold is non-injective, its loss is irrecoverable, and the assessment-optimal path diverges from the geodesic. Ch. 5.

**Grade inflation as moral numbing.** The mechanism by which accumulated moral injury from grading reduces the teacher's boundary penalty for issuing inaccurate grades. Ch. 8.4.1.

## H

**Heuristic field, educational.** $h: \mathcal{L} \to \mathbb{R}_{\geq 0}$: the guidance function estimating remaining distance to the goal. Def. 4.5, Ch. 4.9. *Series: GR Ch. 3.*

**Hidden curriculum.** The unwritten norms and expectations of academic life, formalized as an implicit metric on the learner manifold. Ch. 7.6.

**Holonomy.** The rotation accumulated during parallel transport; measures distortion in knowledge transfer. Ch. 11.1, Appendix A.6.

## I

**Inadmissible heuristic.** A heuristic that overestimates remaining cost; produces non-geodesic teaching paths. Ch. 6.2.3.

**Intersectionality as metric product.** Multiple sources of metric distortion compound multiplicatively, not additively. Prop. 15.2, Ch. 15.4.

## L

**Learner manifold ($\mathcal{L}$).** The 6-dimensional Riemannian manifold of learner states; the central mathematical object of the book. Ch. 4.

**Learner metric ($g_{ij}$).** The Riemannian metric tensor encoding the cost of learning transitions. Def. 4.1, Ch. 4.4.

**Learning deviation ($\text{LD}$).** The integrated distance between the actual learning path and the geodesic. Ch. 13.1.

## M

**Mahalanobis distance.** The distance measure on the learner manifold when the metric is approximated as constant. Appendix A.9.

**Metacognitive awareness ($d_3$).** The third dimension of the learner manifold: self-monitoring, calibration, strategy. Ch. 4.2.3.

**Metric gap.** The difference in effective metrics between student populations; the geometric cause of the achievement gap. Def. 15.1, Ch. 15.1.

**Metric inequality.** The condition in which different populations experience different curvature on the same manifold. Ch. 15.1.

**Metric repair.** An intervention that reduces metric distortion without changing content; the geometric model of effective educational support. Def. 15.2, Ch. 15.5.

**Moral injury, grading.** The distortion of the teacher's heuristic from forced scalar contraction. Def. 8.1, Ch. 8. *Series: GMed Ch. 13--15.*

**Motivation ($d_4$).** The fourth dimension of the learner manifold: intrinsic interest, persistence, engagement. Ch. 4.2.4.

## N

**No Escape Theorem for educational AI.** Theorem 12.1: AI constrained by the learner manifold cannot escape its structure. Ch. 12.3. *Series: GE Ch. 19.*

## P

**Parallel transport.** Carrying a knowledge vector along a path on the manifold; the geometric formalization of transfer learning. Ch. 11.1, Appendix A.6.

**Pedagogical content knowledge (PCK).** Shulman's concept, reinterpreted as domain-specific heuristic calibration. Ch. 6.1.2.

**Prerequisite.** A connectivity constraint on the learner manifold; genuine prerequisites reflect domain structure. Prop. 7.2, Ch. 7.3.

**Procedural skill ($d_2$).** The second dimension of the learner manifold: execution, construction, performance. Ch. 4.2.2.

## S

**Scaffolding.** Temporary local metric adjustment in the Zone of Proximal Development. Def. 6.4, Ch. 6.3.

**Scalar Irrecoverability Theorem.** The parent theorem from *Geometric Reasoning*; the GPA Irrecoverability Theorem is its education-specific instantiation. *Series: GR Ch. 13.*

**Standardized Testing Gauge Violation Theorem.** Theorem 14.1: standardized test scores are not gauge-invariant. Ch. 14.1.

## T

**Transfer ability ($d_5$).** The fifth dimension of the learner manifold: cross-domain application. Ch. 4.2.5.

**Transfer Holonomy Theorem.** Theorem 11.1: the holonomy of knowledge transfer is bounded by curvature and path area. Ch. 11.3.

## Z

**Zone of Proximal Development (ZPD).** Vygotsky's concept, formalized as a neighborhood on the learner manifold reachable with support but not independently. Ch. 3.7, Ch. 6.3.
