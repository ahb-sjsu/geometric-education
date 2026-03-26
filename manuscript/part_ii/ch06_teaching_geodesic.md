# Chapter 6: Teaching as Geodesic Guidance

*Part II: The Framework*

---

> *"The teacher who is indeed wise does not bid you to enter the house of his wisdom but rather leads you to the threshold of your mind."*
> --- Khalil Gibran

> **THE HEURISTIC**
>
> *A teacher does not move the student. The student moves themselves. What the teacher provides is the heuristic field --- the guidance function that estimates the student's distance from understanding, suggests directions, warns of dead ends, and adjusts as the student's position changes. This chapter formalizes the teacher's role as a heuristic field on the learner manifold and establishes the conditions under which teaching is optimal: when the teacher's heuristic is admissible, A* search on the learner manifold finds the geodesic, and the student learns along the path of minimum total cost.*

---

## 6.1 The Teacher as Heuristic Field

The heuristic field formalism from *Geometric Reasoning* (Ch. 3) provides the mathematical framework for teaching. In the general theory, a heuristic function $h(n)$ estimates the remaining cost from state $n$ to the goal. In A* search, the heuristic guides the search by prioritizing states with low estimated total cost $f(n) = g(n) + h(n)$, where $g(n)$ is the cost already incurred and $h(n)$ is the estimated remaining cost.

Teaching is A* search on the learner manifold. The student's current position is $n$. The goal region is $G$ (the set of learner states that satisfy the educational objective). The teacher's heuristic function $h_T(n)$ estimates the student's distance from the goal. The teacher uses this estimate to guide the student: suggesting the next topic, adjusting the difficulty, choosing examples, assigning practice, and monitoring progress.

### 6.1.1 The Pedagogical Heuristic

**Definition 6.1 (Pedagogical Heuristic).** *The pedagogical heuristic $h_T: \mathcal{L} \to \mathbb{R}_{\geq 0}$ is the teacher's estimate of the remaining educational cost from the student's current state $\mathbf{x}$ to the goal region $G$:*

$$h_T(\mathbf{x}) = \text{teacher's estimate of } d_{\mathcal{L}}(\mathbf{x}, G)$$

*where $d_{\mathcal{L}}(\mathbf{x}, G) = \inf_{\mathbf{y} \in G} d_{\mathcal{L}}(\mathbf{x}, \mathbf{y})$ is the geodesic distance from $\mathbf{x}$ to the nearest point in $G$.*

The pedagogical heuristic is not a number the teacher consciously computes. It is the formalization of what teaching intuition does: a skilled teacher looks at a student's work and forms an estimate of how far the student is from understanding. "This student is almost there --- they just need to see one more example." That is $h_T(\mathbf{x}) \approx \epsilon$. "This student is fundamentally confused --- we need to go back to prerequisites." That is $h_T(\mathbf{x}) \gg 0$. The estimate may be accurate or inaccurate, but every teaching decision is implicitly a decision based on an estimate of the student's distance from the goal.

### 6.1.2 Shulman's Pedagogical Content Knowledge

Lee Shulman's (1986) concept of pedagogical content knowledge (PCK) --- the specialized knowledge of how to teach specific content to specific students --- is precisely the calibration of the heuristic function for a specific domain and student population.

A teacher with strong PCK in calculus knows:
- How far a typical student is from understanding limits after the first lecture ($h_T$ for post-lecture states)
- Which misconceptions create high curvature (e.g., the confusion between a limit and a function value --- a high-curvature region where the metric is steep)
- Which examples reduce the distance most efficiently (examples that transport the student along the geodesic)
- Which common errors indicate which specific learning gaps (diagnostic: the error reveals the student's position on the manifold)

PCK is domain-specific heuristic calibration. A teacher with strong PCK in calculus may have weak PCK in linear algebra --- the heuristic is well-calibrated for one domain and poorly calibrated for another. This is a local property of the heuristic field: it is accurate in regions the teacher has mapped and inaccurate in unfamiliar territory.

## 6.2 The Admissibility Hierarchy

The quality of teaching corresponds to the quality of the heuristic. The A* algorithm produces optimal paths if and only if the heuristic is admissible --- that is, if it never overestimates the true remaining cost. This condition has a direct educational interpretation.

### 6.2.1 Strictly Admissible: Master Teachers

**Definition 6.2 (Admissible Pedagogical Heuristic).** *A pedagogical heuristic $h_T$ is admissible if $h_T(\mathbf{x}) \leq d_{\mathcal{L}}(\mathbf{x}, G)$ for all $\mathbf{x} \in \mathcal{L}$.*

An admissible heuristic never overestimates the student's distance from understanding. The teacher may think the student is further from understanding than they actually are (leading to extra practice, which is suboptimal but safe), but the teacher never thinks the student understands when they do not (which would cause the teacher to move on before the student is ready, potentially sending the student onto a path where the manifold is disconnected).

**Theorem 6.1 (Pedagogical Optimality).** *If the pedagogical heuristic $h_T$ is admissible, then A* search on the learner manifold using $h_T$ finds the geodesic $\gamma^*$ --- the minimum-cost path from the student's current state to the goal region.*

This theorem is a direct instantiation of the A* optimality theorem from *Geometric Reasoning* (Ch. 3). Its educational content is: if the teacher's estimate of student understanding is reliably conservative (never overestimates readiness), then the teaching path is optimal. Good teaching is admissible heuristic guidance.

Master teachers have strictly admissible heuristics. They reliably detect gaps in understanding. They are careful not to advance before the student is ready. They may occasionally provide more practice than strictly necessary (because the heuristic underestimates --- the teacher thinks the student is further from understanding than they are), but they never skip essential steps. The result is a near-geodesic path through the manifold.

### 6.2.2 Epsilon-Admissible: Competent Teachers

An epsilon-admissible heuristic satisfies $h_T(\mathbf{x}) \leq d_{\mathcal{L}}(\mathbf{x}, G) + \epsilon$ for some small $\epsilon > 0$. The teacher's estimate may slightly overestimate the student's distance from understanding. The resulting teaching path is within $\epsilon$ of optimal: not perfect, but close.

Most competent teachers have epsilon-admissible heuristics. They occasionally misjudge a student's readiness, moving on slightly too fast or providing slightly too little practice. The resulting teaching path is near-geodesic but not exactly geodesic. The epsilon is the gap between professional competence and pedagogical perfection.

### 6.2.3 Inadmissible: Miscalibrated Teachers

An inadmissible heuristic systematically overestimates the student's readiness: $h_T(\mathbf{x}) > d_{\mathcal{L}}(\mathbf{x}, G) + \epsilon$ for many states $\mathbf{x}$. The teacher thinks the student is closer to understanding than they actually are, and moves on before prerequisites are established.

Inadmissible heuristics produce non-geodesic paths. The student is pushed into regions of the manifold where the prerequisites have not been built, the metric is degenerate (the necessary tangent vectors are absent), and learning stalls. The student does not merely fail to learn; they arrive at a position on the manifold from which further progress requires backtracking to build the missing prerequisites --- a longer and more costly path than the geodesic would have been.

Two common causes of inadmissible heuristics:

**Pace pressure.** Curriculum schedules that require covering a fixed amount of material in a fixed time create pressure to advance regardless of student readiness. The teacher's heuristic becomes inadmissible not because the teacher misjudges the student but because the institution overrides the teacher's judgment with a pace constraint. The schedule overestimates the student's readiness by assumption: "Students should understand derivatives by week 6" is a heuristic value imposed externally, regardless of the actual student state.

**Frustration deflation.** Teachers who have experienced years of student underperformance may develop heuristics that underestimate student capacity --- expecting less than students can achieve, providing scaffolding that is not needed, and accepting lower standards. This is the opposite of inadmissibility: the heuristic is too pessimistic, producing paths that are longer than the geodesic (too much review, too many prerequisites revisited). Frustration deflation is a suboptimal heuristic, but it is admissible and therefore safe --- the student arrives at the goal, just more slowly than necessary.

### 6.2.4 Gauge-Variant: Biased Teachers

**Definition 6.3 (Gauge-Variant Pedagogical Heuristic).** *A pedagogical heuristic $h_T$ is gauge-variant if $h_T(\mathbf{x})$ depends on features of the student that are not coordinates on the learner manifold --- features such as race, gender, accent, clothing, first language, family background, or physical appearance.*

A gauge-variant heuristic assigns different distance estimates to students at the same point on the learner manifold, based on surface features that should not affect the assessment. If the teacher estimates that Alex (first-generation, working-class, Latinx) is further from understanding than Ethan (continuing-generation, upper-middle-class, white) when both are at the same learner state, the heuristic is gauge-variant.

Gauge variance in the pedagogical heuristic is not always conscious bias. It can arise from statistical conditioning: if the teacher has observed (correctly) that students from certain backgrounds tend to arrive with lower $d_1$, the teacher may apply this prior to new students from those backgrounds without checking whether the specific student fits the pattern. The prior shifts the heuristic estimate. The shift is gauge-variant because it depends on the student's background (a non-manifold feature), not on the student's current learner state (a manifold position).

The damage from gauge-variant heuristics is directional: they systematically underestimate the capacity of students from disadvantaged backgrounds and overestimate the capacity of students from advantaged backgrounds. The resulting teaching paths diverge: the underestimated student receives less challenge, less scaffolding into advanced material, and lower expectations --- a path that stays in low-curvature regions of the manifold and reaches a goal region that is smaller and less ambitious. The overestimated student receives more challenge, more opportunity, and higher expectations --- a path that explores more of the manifold and reaches a larger, more ambitious goal region.

## 6.3 Scaffolding as Local Metric Adjustment

Vygotsky's Zone of Proximal Development (ZPD), introduced in Chapter 3, is formalized here as a local metric adjustment.

**Definition 6.4 (Scaffolding).** *A scaffold is a temporary modification of the local metric on $\mathcal{L}$ in a neighborhood of the student's current state $\mathbf{x}$, such that certain transitions that are too costly in the natural metric ($g_{ij}(\mathbf{x})$ large) become feasible in the scaffolded metric ($\tilde{g}_{ij}(\mathbf{x})$ small).*

The scaffold does not move the student. It temporarily reshapes the manifold in the student's local neighborhood, enabling traversal that the natural curvature would have prevented. As the student develops (moves to a new position where the natural metric is more favorable), the scaffold is removed and the metric returns to its natural value.

Examples of scaffolding as metric adjustment:

- **Worked examples** reduce the curvature between "doesn't know the procedure" and "knows the procedure" by providing a partially completed path that the student can follow.
- **Visual representations** reduce the curvature in the spatial dimension ($d_2$) by providing an alternative tangent direction through the visual modality.
- **Peer discussion** reduces the curvature in the metacognitive dimension ($d_3$) by externalizing the monitoring process --- the peer provides metacognitive feedback that the student has not yet internalized.
- **Simplified notation** reduces the curvature in the formal dimension ($d_1$) by temporarily replacing complex notation with simpler representations, enabling the student to engage with the concept before mastering the notation.

### 6.3.1 When to Remove the Scaffold

The scaffold should be removed when the student can traverse the transition independently --- that is, when the student's position on the manifold has changed enough that the natural metric in the relevant neighborhood is low enough for independent traversal.

The timing of scaffold removal is a heuristic judgment: the teacher must estimate when the student's natural metric has changed sufficiently. Removing the scaffold too early (the student is not yet ready for independent traversal) forces the student back into a high-curvature region without support. Removing the scaffold too late (the student has already mastered the transition) wastes time and can create dependence --- the student relies on the scaffold instead of developing the natural metric.

## 6.4 The Empty-Heuristic Problem

First-generation college students navigate the educational manifold without the inherited heuristic field that continuing-generation students receive from their parents.

**Definition 6.5 (Inherited Heuristic).** *The inherited heuristic $h_P$ is the component of the educational heuristic field provided by parents or family members who have previously navigated the educational manifold. For continuing-generation students, $h_P$ provides estimates of distance to educational goals based on the parents' own experience: "Office hours are worth attending" (low cost of help-seeking), "This professor is demanding but fair" (heuristic estimate for course difficulty), "Take a lighter load in your first semester" (path planning advice).*

For first-generation students, $h_P \approx 0$: the parents have not navigated the educational manifold and cannot provide heuristic estimates. The student must discover navigational knowledge by trial and error, at a cost measured in time, grades, and self-confidence.

The geometric framework reframes first-generation status from a student characteristic to a heuristic field deficit. The student is not deficient --- the student may be at the same point on the learner manifold as a continuing-generation peer, with the same $d_1$ through $d_6$. What is missing is not capacity but guidance. The field, not the student, is deficient.

This reframing has practical implications. If first-generation difficulty is caused by a missing heuristic field (not by a missing capacity), then the intervention is to provide the field, not to remediate the student. Mentoring programs, navigational workshops, proactive advising, and peer mentoring are heuristic field supplements: they provide the guidance values that the family cannot. They are not remediation. They are navigation support.

### 6.4.1 The Cost of Absent Heuristics

The cost of navigating without a heuristic is well-quantified in search theory: A* with $h = 0$ degenerates to uniform-cost search (Dijkstra's algorithm), which explores states in order of cost-from-start without any estimate of cost-to-goal. Uniform-cost search is complete (it finds the goal) but maximally inefficient (it explores every state up to the geodesic cost).

The educational analogue: a first-generation student without a heuristic field will eventually find the path to the degree (given sufficient time, resources, and persistence), but the path will be longer, more expensive, and involve more dead ends than the path of a student guided by a well-calibrated heuristic. The additional path cost is measurable: first-generation students take, on average, 1.5 to 2 semesters longer to complete a degree, change majors more frequently, and have higher rates of late withdrawal from courses --- all indicators of exploratory search without heuristic guidance.

## 6.5 The Four Heuristic Failure Modes in Teaching

The four failure modes from *Geometric Reasoning* (Ch. 5--8) have direct educational instantiations:

### 6.5.1 Heuristic Corruption

The teacher's heuristic is corrupted by irrelevant information. In teaching, heuristic corruption occurs when the teacher's estimate of student understanding is warped by factors unrelated to understanding: the student's behavior (a quiet student is assumed not to understand), the student's background (a student from a "low-performing" school is assumed to be behind), or the teacher's own projections (a student who reminds the teacher of a previously unsuccessful student is assumed to be similarly at risk).

### 6.5.2 Objective Hijacking

The teacher optimizes for a proxy rather than the actual educational objective. The most common form: optimizing for test scores rather than for learning. A teacher who "teaches to the test" is following the gradient of the scalar projection ($G$) rather than the gradient of the geodesic. The teacher's heuristic estimates distance-to-high-test-score rather than distance-to-understanding. The resulting path is $\gamma_G^*$ rather than $\gamma_\mathcal{L}^*$ --- the GPA-optimal path rather than the geodesic.

### 6.5.3 Local Minima

The student gets stuck in a state from which the heuristic provides no productive direction. Educational local minima include: prerequisite traps (the student lacks a prerequisite but the system does not offer remediation), motivation valleys (the student has lost interest and the curriculum does not recover it), and skill plateaus (the student has automatized an incorrect procedure and the correct procedure requires unlearning).

### 6.5.4 Gauge Breaking

The teacher's heuristic varies under gauge transformations --- it gives different estimates for the same learner state depending on the student's surface characteristics. This is gauge variance, discussed in Section 6.2.4.

## 6.6 Alex and Professor Vasquez

Alex has been struggling in Differential Equations. The standard course follows a formal-first path: definitions, theorems, proofs, then applications. Alex's learner state has high $d_2$ (procedural skill in applied mathematics) but lower $d_1$ (formal mathematical notation). The formal-first path is a high-curvature route for Alex --- it demands the dimension where Alex is weakest.

Professor Vasquez teaches a different section. Vasquez has twenty years of teaching experience and a well-calibrated heuristic. In the first week, Vasquez gives a diagnostic problem: "Describe a system you've seen in the real world that oscillates. Explain what happens when the oscillation is damped."

Alex writes about engine vibrations. The description is physically precise, mechanically detailed, and mathematically correct in its conceptual content, though expressed in informal language rather than formal notation. Vasquez reads the response and estimates: $d_2 \approx 0.85$, $d_5 \approx 0.75$ (the connection between engine vibrations and damped oscillation is a transfer), $d_1 \approx 0.50$ (the formal notation is weak but the conceptual understanding is strong).

Vasquez adjusts the local metric for Alex: providing a notation scaffold (a guide that translates between informal mechanical descriptions and formal mathematical notation) and rerouting Alex through a problem sequence that starts with physical applications and builds the formal machinery as needed. This is a different geodesic through the same content, optimized for Alex's actual position on the manifold rather than for the default position assumed by the standard curriculum.

Alex's trajectory changes. The notation scaffold reduces the curvature in the $d_1$ direction. The application-first sequence leverages Alex's strong $d_2$ and $d_5$ as foundations for building $d_1$. Alex begins to recognize that the eigenvalue structure of a differential equation is the same mathematical object as the resonance frequency of an engine --- a transfer ($d_5$) that connects Alex's strongest dimension to the formal content.

Vasquez's intervention is not inspiration. It is heuristic recalibration: a teacher with an admissible, gauge-invariant heuristic replacing the default curriculum's inadmissible, gauge-variant heuristic with a better one. The result is a learning trajectory that is closer to Alex's geodesic than the default path. The grade in Vasquez's course: A-.

The difference between the C+ from the standard section and the A- from Vasquez's section is not a difference in Alex's capacity. It is a difference in the heuristic field --- a difference in the teacher's estimate of who Alex is and what Alex needs. The capacity was always there. The guidance was not.

---

## Summary

This chapter has formalized the teacher's role as a heuristic field on the learner manifold. The pedagogical heuristic $h_T$ estimates the student's distance from the goal region, and its quality determines the quality of the teaching path: admissible heuristics produce geodesic paths, epsilon-admissible heuristics produce near-geodesic paths, inadmissible heuristics produce non-geodesic paths, and gauge-variant heuristics produce systematically biased paths. Scaffolding is local metric adjustment in the Zone of Proximal Development. First-generation students navigate without an inherited heuristic field, and the resulting inefficiency is measurable. The four heuristic failure modes from the general theory --- corruption, hijacking, local minima, and gauge breaking --- have direct educational instantiations. Good teaching is admissible heuristic guidance. Great teaching is gauge-invariant, near-optimal heuristic calibration across all dimensions of the learner manifold.

---

[^1]: Shulman, L. S. (1986). Those who understand: Knowledge growth in teaching. *Educational Researcher*, 15(2), 4--14.
