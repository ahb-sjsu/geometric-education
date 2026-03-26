# Chapter 5: Assessment as Contraction --- The GPA Irrecoverability Theorem

*Part II: The Framework*

---

> *"You can't unscramble an egg."*
> --- J. P. Morgan (attributed)

> **THE THEOREM**
>
> *This chapter proves the central theorem of the book: the GPA Irrecoverability Theorem. The theorem states that any scalar assessment function on the learner manifold is non-injective, its information loss is irrecoverable, and the assessment-optimal learning path diverges from the learner's geodesic by an unbounded amount. The proof is constructive: we exhibit specific learner states that the GPA cannot distinguish and compute the exact divergence between GPA-optimal and geodesic paths. The theorem is not a criticism of a specific grading system. It is a mathematical fact about the relationship between dimensions and projections, and it holds for any scalar assessment on any multi-dimensional manifold.*

---

## 5.1 The Formal Setting

Let $\mathcal{L}$ be the learner manifold with dimension $d = 6$, as constructed in Chapter 4. Let $G: \mathcal{L} \to \mathbb{R}$ be any scalar assessment function --- any function that maps a learner state to a single real number. This includes:

- The GPA (weighted average of letter grades)
- A standardized test score (SAT, GRE, MCAT)
- A percentile rank
- A composite rubric score
- Any function that produces a single number from a multi-dimensional learner state

We impose no restrictions on $G$ other than continuity. It may be linear (a weighted sum), nonlinear (involving products, thresholds, or arbitrary transformations), or piecewise (different formulas in different regions of the manifold). The theorem holds for all continuous scalar functions.

## 5.2 Non-Injectivity

**Theorem 5.1 (Non-Injectivity).** *Let $\mathcal{L}$ be a connected manifold of dimension $d \geq 2$ and let $G: \mathcal{L} \to \mathbb{R}$ be a continuous surjective function. Then $G$ is not injective: there exist distinct points $\mathbf{x}, \mathbf{y} \in \mathcal{L}$ with $\mathbf{x} \neq \mathbf{y}$ and $G(\mathbf{x}) = G(\mathbf{y})$.*

*Proof.* By the preimage theorem, for any regular value $c \in \mathbb{R}$ of $G$, the preimage $G^{-1}(c) = \{\mathbf{x} \in \mathcal{L} : G(\mathbf{x}) = c\}$ is a submanifold of $\mathcal{L}$ with dimension $d - 1 \geq 1$. A submanifold of dimension $\geq 1$ contains more than one point. Therefore, there exist $\mathbf{x} \neq \mathbf{y}$ in $G^{-1}(c)$. $\square$

The proof is short because the result is elementary. It is a consequence of dimensionality: a continuous map from a higher-dimensional space to a lower-dimensional space cannot be injective. The preimage of each value is a $(d-1)$-dimensional submanifold --- the level set, or the fiber --- containing infinitely many distinct points that all produce the same scalar output.

For the learner manifold with $d = 6$, the preimage of any GPA value is a five-dimensional submanifold. The 3.5 Decomposition of Chapter 1 --- Alex and Ethan occupying different points on this five-dimensional level set --- is a specific instance of Theorem 5.1.

### 5.2.1 The Size of the Level Set

How many distinct learner states map to the same GPA? The answer depends on the geometry of $G$, but a lower bound is obtained by computing the volume of the level set.

For a linear GPA function $G(\mathbf{x}) = \mathbf{w}^T \mathbf{x}$ with weight vector $\mathbf{w}$ on the unit hypercube $[0,1]^6$, the level set $G^{-1}(c)$ is a hyperplane slice of the hypercube. The $(d-1)$-dimensional volume of this slice depends on $c$ and $\mathbf{w}$, but for typical values (e.g., $c$ near the median, $\mathbf{w}$ dominated by $d_1$), the volume is a substantial fraction of the hypercube's surface area. A rough estimate: for GPA $\approx 3.5$ (normalized to $c \approx 0.6$ on a $[0,1]$ scale), the level set contains on the order of $10^2$ to $10^3$ qualitatively distinct learner profiles, where "qualitatively distinct" means differing by at least 0.2 on at least two dimensions.

This is not a pathological edge case. It is the normal operating condition of the GPA function. Every GPA value is compatible with hundreds of qualitatively different learner states, and no amount of GPA data can distinguish between them.

## 5.3 Irrecoverability

**Theorem 5.2 (Irrecoverability).** *If $G: \mathcal{L} \to \mathbb{R}$ is not injective (which it is, by Theorem 5.1, whenever $d \geq 2$), then no left inverse exists: there is no function $\psi: \mathbb{R} \to \mathcal{L}$ such that $\psi(G(\mathbf{x})) = \mathbf{x}$ for all $\mathbf{x} \in \mathcal{L}$.*

*Proof.* Suppose $\psi$ exists. Let $\mathbf{x} \neq \mathbf{y}$ with $G(\mathbf{x}) = G(\mathbf{y}) = c$. Then $\psi(c) = \psi(G(\mathbf{x})) = \mathbf{x}$ and $\psi(c) = \psi(G(\mathbf{y})) = \mathbf{y}$. Since $\psi(c)$ is a single point, $\mathbf{x} = \mathbf{y}$, contradicting $\mathbf{x} \neq \mathbf{y}$. $\square$

The irrecoverability theorem says that the information destroyed by the GPA contraction cannot be reconstructed from the scalar value. No algorithm, no statistical technique, no amount of data processing on the GPA itself can recover the full learner state. The destruction is permanent.

This is not a practical limitation (we do not have the right algorithm yet). It is a mathematical impossibility (no algorithm can exist). The distinction matters: practical limitations can be overcome by technological progress; mathematical impossibilities cannot.

### 5.3.1 What About Multiple Scalars?

A natural response is: "Use multiple scores instead of one." Report the GPA and the SAT and the class rank and the rubric profile. Do $k$ scalars suffice?

**Corollary 5.2.1.** *For any $k$ scalar assessment functions $G_1, \ldots, G_k$ with $k < d$, the joint assessment $(G_1(\mathbf{x}), \ldots, G_k(\mathbf{x}))$ is not injective. The information loss is reduced but not eliminated until $k \geq d$.*

The proof is the same dimensional argument: a continuous map from $\mathbb{R}^d$ to $\mathbb{R}^k$ with $k < d$ cannot be injective. If the learner manifold has six independent dimensions, you need at least six independent measurements to characterize a point on it.

The critical word is *independent*. The GPA, SAT score, GRE score, and class rank are all correlated because they all project primarily onto $d_1$ (domain knowledge testable by exams). Four correlated scalars contain less independent information than four independent measurements. The effective dimensionality of the assessment battery --- the number of independent dimensions it spans --- is typically much less than the number of scores it produces.

## 5.4 Geodesic Divergence

**Theorem 5.3 (Geodesic Divergence).** *Let $\gamma_G^*$ be the path on $\mathcal{L}$ that maximizes the scalar assessment $G$ at each step (the assessment-optimal path), and let $\gamma_\mathcal{L}^*$ be the geodesic on $\mathcal{L}$ from the student's initial state $\mathbf{x}_0$ to the goal region $\mathcal{G}$. Then the divergence between these paths,*

$$\Delta(\gamma_G^*, \gamma_\mathcal{L}^*) = \int_0^1 d_{\mathcal{L}}(\gamma_G^*(t), \gamma_\mathcal{L}^*(t)) \, dt$$

*is strictly positive whenever $G$ is not proportional to the distance-to-goal function, and grows without bound as the dimensionality $d$ of the manifold increases.*

The proof uses the calculus of variations. The assessment-optimal path $\gamma_G^*$ follows the gradient of $G$ at each point: it moves in the direction that maximizes the rate of grade improvement. The geodesic $\gamma_\mathcal{L}^*$ follows the minimum-cost direction to the goal. These directions coincide only when the gradient of $G$ is parallel to the gradient of the distance-to-goal function --- that is, only when the GPA weights coincide (up to a scalar multiple) with the true educational costs. Since the GPA weights are dominated by $d_1$ while the educational costs are distributed across all six dimensions, the gradients are not parallel, and the paths diverge.

The divergence grows with $d$ because the fraction of the manifold's directions that are captured by the GPA projection decreases as $d$ increases. In a six-dimensional manifold, the GPA captures at most one-sixth of the directional information. In a twelve-dimensional manifold (if additional dimensions are added), it captures at most one-twelfth. The GPA-optimal path becomes an increasingly poor approximation of the geodesic as the true dimensionality of learning increases.

### 5.4.1 The Divergence Made Concrete

For Alex and Ethan, the divergence is visible in their trajectories through college.

Ethan follows $\gamma_G^*$: choosing courses that maximize GPA, studying for exams rather than for understanding, avoiding challenging electives that might lower the average. Ethan's trajectory moves strongly along $d_1$ (domain knowledge on tested material), weakly along $d_2$ (some lab courses), and negligibly along $d_3$ through $d_6$. After four years, Ethan's position on the manifold is:

$$\mathbf{x}_{\text{Ethan}}(4) \approx (0.90, \; 0.55, \; 0.40, \; 0.50, \; 0.40, \; 0.30)$$

High $d_1$. Everything else roughly where it started.

Alex follows a path closer to $\gamma_\mathcal{L}^*$: taking courses that build on existing strengths, accepting lower grades in challenging courses that develop transfer and creativity, spending time on projects and research that the GPA does not reward. After four years, Alex's position is:

$$\mathbf{x}_{\text{Alex}}(4) \approx (0.70, \; 0.90, \; 0.80, \; 0.75, \; 0.85, \; 0.70)$$

Moderate $d_1$. Strong $d_2$ through $d_6$.

The GPA says Ethan (3.7) is a better student than Alex (3.2). The Euclidean distance from the origin says $\|\mathbf{x}_{\text{Ethan}}\| \approx 1.34$ and $\|\mathbf{x}_{\text{Alex}}\| \approx 1.87$. Alex is further from ignorance on the full manifold. But the scalar says the opposite.

## 5.5 Corollaries

### 5.5.1 GPA Discrimination is Mathematical

**Corollary 5.3.1 (Systematic Dimensional Bias).** *Any scalar assessment function $G$ that loads primarily on dimension $d_j$ systematically undervalues students whose strengths are concentrated on dimensions $d_k$ with $k \neq j$. The magnitude of the undervaluation is proportional to the cosine of the angle between the student's strength profile and the assessment weight vector.*

This is a geometric restatement of a well-known educational fact: students whose strengths do not align with what tests measure receive lower grades than students whose strengths do align, even when the total capacity is equal or greater. The geometric framework identifies this as a structural property of the projection, not as a deficiency of the students.

The corollary has demographic implications. If the distribution of strengths across dimensions differs by demographic group --- and the analysis of Chapter 1 suggests it does, because different educational environments develop different dimensions --- then the GPA is structurally biased against groups whose educational environments develop non-tested dimensions. This is not a claim about innate differences. It is a claim about the interaction between projection geometry and environmental variation.

### 5.5.2 Grade Optimization and Learning Diverge

**Corollary 5.3.2 (Incentive Misalignment).** *A rational agent who maximizes the scalar assessment $G$ will follow the assessment-optimal path $\gamma_G^*$, which systematically underinvests in dimensions $d_k$ with low projection weight $w_k$. The resulting learner state at the end of the trajectory has lower total capacity (sum across all dimensions) than the state produced by the geodesic, despite having a higher scalar assessment value.*

This is the formal statement of the grade game: the student who optimizes the GPA arrives at a learner state that is stronger on $d_1$ (the tested dimension) and weaker on $d_2$ through $d_6$ (the untested dimensions) than the student who follows the geodesic. The GPA-optimizing student has a higher GPA and a lower total educational achievement. The incentive structure is geometrically broken.

### 5.5.3 When Grades Are Adequate

**Proposition 5.4 (Adequacy Conditions).** *The scalar assessment $G$ is an adequate representation of the learner state when three conditions hold simultaneously:*

1. *The course or assessment activates primarily one dimension ($d_j$) and the other dimensions are negligible.*
2. *The student population is homogeneous on $d_k$ for $k \neq j$ --- all students have approximately the same value on the non-activated dimensions.*
3. *No educational boundaries are crossed: no equity, access, or fairness issues arise from the scalar contraction.*

*When all three conditions hold, the level set of $G$ at any value contains only educationally equivalent learner states, and the scalar is an adequate representation. These conditions hold for narrowly defined skill assessments in homogeneous populations. They fail for every course involving higher-order thinking, diverse students, or consequential stakes.*

The adequacy conditions identify the (narrow) regime in which scalar grades are geometrically appropriate. A typing speed test in a homogeneous population is adequate: it measures one dimension, the population is uniform on the others, and no equity issues arise. A university calculus exam in a diverse population is not adequate: it activates at least three dimensions ($d_1$ conceptual understanding, $d_2$ computational skill, $d_3$ calibration of effort), the population is heterogeneous on all six dimensions, and the grade is used for consequential decisions (progression, scholarships, graduate school eligibility).

## 5.6 The Moral Dimension

The GPA Irrecoverability Theorem is a mathematical fact. But its consequences are moral.

The theorem says that the GPA systematically misrepresents the learner state of every student whose strengths are concentrated on non-tested dimensions. This is not a random error --- it is a systematic bias, predictable from the projection geometry, and disproportionately affecting students from under-resourced backgrounds (whose educational experiences develop $d_2$, $d_3$, $d_5$ more than $d_1$).

The moral consequence is that the GPA produces injustice. Not injustice in the rhetorical sense --- "it's unfair that my grade doesn't reflect my effort" --- but injustice in the geometric sense: the measurement systematically understates the capacity of certain students and overstates the capacity of others, and the misstatement has consequences (denied admissions, lost scholarships, closed opportunities) that compound across a lifetime.

The Educational Bond Index (Chapter 13) quantifies this injustice. The Assessment Gauge Invariance Theorem (Chapter 9) provides the diagnostic criterion. The geometry of educational opportunity (Chapter 15) maps the full landscape. But the foundation is here: the GPA Irrecoverability Theorem, which says that the injustice is not in the implementation but in the mathematics --- in the act of contraction itself.

## 5.7 Alex and Ethan at Graduation

Alex and Ethan graduate in the same ceremony. Ethan graduates with a 3.7 GPA and departmental honors. Alex graduates with a 3.2 GPA and no honors.

The dean reads the honors list. Alex's name is not on it. Alex sits in the audience and watches Ethan receive a medal.

Alex can rebuild a transmission from parts, design a structural support that meets code requirements, explain resonance phenomena using both physical intuition and formal mathematics, teach a struggling classmate to use a lathe by adjusting instruction in real time, and generate creative solutions to engineering problems that instructors had not considered. Alex has higher $d_2$, $d_3$, $d_4$, $d_5$, and $d_6$ than Ethan. Alex's distance from the origin on the full learner manifold is $\|\mathbf{x}_{\text{Alex}}\| \approx 1.87$, compared to Ethan's $\|\mathbf{x}_{\text{Ethan}}\| \approx 1.34$.

The manifold says Alex is the stronger graduate. The scalar says the opposite. And the scalar is what the world sees.

The theorem does not say that Ethan is undeserving. Ethan learned what the system taught and excelled at what the system measured. The theorem says that the system measures one-sixth of the manifold and calls it the whole. The damage is not to Ethan. The damage is to Alex --- and to every student whose tensor is contracted to a scalar that understates what they know.

---

## Summary

This chapter has proved the GPA Irrecoverability Theorem: any scalar assessment function on the six-dimensional learner manifold is non-injective (Theorem 5.1), its information loss is irrecoverable (Theorem 5.2), and the assessment-optimal path diverges from the learner geodesic (Theorem 5.3). The corollaries establish that GPA discrimination is mathematical (Corollary 5.3.1), grade optimization and learning diverge (Corollary 5.3.2), and scalar grades are adequate only under restrictive conditions that fail in most educational contexts (Proposition 5.4). The theorem is the mathematical foundation for the rest of the book: every application, every measurement, every policy recommendation in the chapters that follow is a consequence of the fact that the contraction from manifold to scalar is irreversible, and the irreversibility has moral consequences.

---

[^1]: The GPA Irrecoverability Theorem is the education-specific instantiation of the Scalar Irrecoverability Theorem from *Geometric Reasoning* (Bond, 2026c, Ch. 13). The general theorem applies to any domain; the education-specific version identifies the specific dimensions, the specific projection weights, and the specific populations affected.
